"""Servidor HTTP de Yizi Voz Local. Escucha solo en 127.0.0.1. Contrato: CONTRATO-API.md."""
from __future__ import annotations

import asyncio
import hmac
import json
import logging
import time
from contextlib import asynccontextmanager

import numpy as np
from fastapi import FastAPI, File, Form, Request, UploadFile, WebSocket, WebSocketDisconnect
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse, StreamingResponse
from pydantic import BaseModel, Field

from . import audio as au
from .ajustes import Ajustes, cargar
from .flujo import Segmentador
from .stt import MotorTexto
from .tts import ErrorVoz, MotorVoz
from .vad import SileroStream

VERSION = "1.0.0"
log = logging.getLogger("yizi-voz")


class ErrorApi(Exception):
    def __init__(self, estado: int, codigo: str, mensaje: str):
        self.estado, self.codigo, self.mensaje = estado, codigo, mensaje


def error_json(estado: int, codigo: str, mensaje: str) -> JSONResponse:
    return JSONResponse(status_code=estado, content={"error": {"code": codigo, "message": mensaje}})


class PeticionVoz(BaseModel):
    input: str = Field(..., description="Texto a leer")
    voice: str | None = Field(None, description="Id de agente de config/voces.yaml o voz de Kokoro")
    speed: float = Field(1.0, ge=0.5, le=2.0)
    response_format: str = Field("wav")
    model: str | None = None  # se acepta y se ignora (compatibilidad con OpenAI)


def crear_app(ajustes: Ajustes | None = None, stt: MotorTexto | None = None,
              tts: MotorVoz | None = None) -> FastAPI:
    a = ajustes or cargar()
    estado: dict = {"stt": stt, "tts": tts}

    @asynccontextmanager
    async def _vida(_app):
        t = time.perf_counter()
        if estado["tts"] is None:
            estado["tts"] = await asyncio.to_thread(MotorVoz, a)
        if estado["stt"] is None:
            estado["stt"] = await asyncio.to_thread(MotorTexto, a)
        log.info("Modelos listos en %.1f s (stt=%s, tts=%s)", time.perf_counter() - t,
                 estado["stt"].backend or "sin modelo", estado["tts"].motor)
        yield

    app = FastAPI(title="Yizi Voz Local", version=VERSION, docs_url="/docs", redoc_url=None, lifespan=_vida)

    def autorizar(cabeceras) -> None:
        if not a.token:
            return
        valor = cabeceras.get("authorization", "")
        dado = valor[7:] if valor.lower().startswith("bearer ") else cabeceras.get("x-api-key", "")
        if not hmac.compare_digest(dado.encode(), a.token.encode()):
            raise ErrorApi(401, "unauthorized", "Falta el token o no es válido (cabecera Authorization: Bearer <token>).")

    @app.exception_handler(ErrorApi)
    async def _err(_: Request, e: ErrorApi):
        return error_json(e.estado, e.codigo, e.mensaje)

    @app.exception_handler(RequestValidationError)
    async def _val(_: Request, e: RequestValidationError):
        detalle = "; ".join(f"{'.'.join(str(x) for x in er['loc'][1:])}: {er['msg']}" for er in e.errors())
        return error_json(400, "invalid_request", detalle or "Petición no válida")

    @app.middleware("http")
    async def _token(request: Request, call_next):
        if request.url.path not in ("/health",) and request.url.path.startswith("/v1"):
            try:
                autorizar(request.headers)
            except ErrorApi as e:
                return error_json(e.estado, e.codigo, e.mensaje)
        return await call_next(request)

    @app.get("/health")
    async def salud():
        s: MotorTexto | None = estado["stt"]
        v: MotorVoz | None = estado["tts"]
        listo = bool(s and s.listo and v and v.motor != "ninguno")
        return {
            "status": "ok" if listo else "degraded",
            "version": VERSION,
            "stt": {"ready": bool(s and s.listo), "backend": s.backend if s else "", "model": (s.modelo_ruta.split("/")[-1] if s and s.modelo_ruta else ""),
                    "error": s.error if s else "cargando"},
            "tts": {"ready": bool(v and v.motor != "ninguno"), "engine": v.motor if v else "",
                    "error": v.error_kokoro if v else "cargando"},
            "auth": bool(a.token),
        }

    @app.get("/v1/voices")
    async def voces():
        v: MotorVoz = _tts()
        lista = [{"id": x.id, "kokoro_voice": x.kokoro, "speed": x.velocidad, "say_voice": x.say,
                  "description": x.descripcion} for x in v.agentes.values()]
        return {"engine": v.motor, "default": a.voz_por_defecto, "voices": lista,
                "kokoro_voices": sorted(v.kokoro.voces) if v.kokoro else [],
                "say_voices": v.voces_say}

    def _tts() -> MotorVoz:
        v = estado["tts"]
        if v is None or v.motor == "ninguno":
            raise ErrorApi(503, "tts_unavailable", "El texto a voz no está listo: " + (v.error_kokoro if v else "cargando"))
        return v

    def _stt() -> MotorTexto:
        s = estado["stt"]
        if s is None or not s.listo:
            raise ErrorApi(503, "stt_unavailable", "La voz a texto no está lista: " + (s.error if s else "cargando"))
        return s

    @app.post("/v1/audio/speech")
    async def hablar(p: PeticionVoz):
        v = _tts()
        texto = p.input.strip()
        if not texto:
            raise ErrorApi(400, "invalid_request", "El campo 'input' está vacío.")
        if len(texto) > a.max_texto:
            raise ErrorApi(413, "input_too_long", f"El texto pasa de {a.max_texto} caracteres.")
        fmt = p.response_format.lower()
        if fmt not in ("wav", "pcm"):
            raise ErrorApi(400, "unsupported_format", "response_format debe ser 'wav' o 'pcm'.")
        try:
            voz = v.resolver(p.voice)
        except ErrorVoz as e:
            raise ErrorApi(400, "voice_not_found", str(e))
        frases = v.frases(texto)

        async def generar():
            if fmt == "wav":
                yield au.cabecera_wav_stream(24000)
            for i, frase in enumerate(frases):
                audio, _ = await asyncio.to_thread(v.sintetizar_frase, frase, voz, p.speed)
                if i < len(frases) - 1:
                    audio = np.concatenate([audio, v.silencio()])
                yield au.float_a_pcm16(audio)

        tipo = "audio/wav" if fmt == "wav" else "audio/L16; rate=24000; channels=1"
        return StreamingResponse(generar(), media_type=tipo, headers={
            "X-Sample-Rate": "24000", "X-Voice": voz.id, "X-Voice-Engine": v.motor,
            "X-Sentences": str(len(frases)), "Cache-Control": "no-store"})

    @app.post("/v1/audio/transcriptions")
    async def transcribir(file: UploadFile = File(...), language: str = Form("es"),
                          prompt: str | None = Form(None), response_format: str = Form("json"),
                          model: str | None = Form(None)):
        s = _stt()
        datos = await file.read(a.max_audio_mb * 1024 * 1024 + 1)
        if len(datos) > a.max_audio_mb * 1024 * 1024:
            raise ErrorApi(413, "file_too_large", f"El audio pasa de {a.max_audio_mb} MB.")
        if not datos:
            raise ErrorApi(400, "invalid_request", "El archivo de audio está vacío.")
        try:
            audio = await asyncio.to_thread(s.decodificar, datos)
        except Exception:
            raise ErrorApi(415, "unsupported_audio", "No pude leer el audio. Usa WAV, M4A, MP3, OGG o FLAC.")
        finally:
            del datos
        t = time.perf_counter()
        texto = await asyncio.to_thread(s.transcribir, audio, language or a.stt_idioma, False, prompt)
        dur = time.perf_counter() - t
        if response_format == "text":
            return StreamingResponse(iter([texto.encode()]), media_type="text/plain; charset=utf-8")
        return {"text": texto, "language": language, "duration": round(len(audio) / 16000, 3),
                "processing_ms": int(dur * 1000)}

    @app.websocket("/v1/stream/transcribe")
    async def dictado(ws: WebSocket):
        try:
            autorizar(ws.headers)
        except ErrorApi:
            await ws.close(code=4401, reason="unauthorized")
            return
        s = estado["stt"]
        await ws.accept()
        if s is None or not s.listo:
            await ws.send_json({"type": "error", "code": "stt_unavailable", "message": "La voz a texto no está lista."})
            await ws.close(code=1011)
            return
        idioma = ws.query_params.get("language") or a.stt_idioma
        seg = Segmentador(SileroStream(), a.vad_umbral, a.vad_silencio_fin_ms, a.vad_parcial_cada_ms,
                          a.vad_max_segmento_s, a.vad_preroll_ms)
        cola: asyncio.Queue = asyncio.Queue()
        ocupado = {"parcial": False}
        enviar_lock = asyncio.Lock()

        async def enviar(msg: dict):
            async with enviar_lock:
                await ws.send_json(msg)

        async def trabajador():
            while True:
                ev = await cola.get()
                if ev is None:
                    return
                t = time.perf_counter()
                try:
                    texto = await asyncio.to_thread(s.transcribir, ev.audio, idioma, ev.tipo == "need_partial")
                except Exception as e:
                    await enviar({"type": "error", "code": "transcription_failed", "message": str(e)})
                    continue
                finally:
                    if ev.tipo == "need_partial":
                        ocupado["parcial"] = False
                ms = int((time.perf_counter() - t) * 1000)
                tipo = "partial" if ev.tipo == "need_partial" else "final"
                await enviar({"type": tipo, "segment_id": ev.segmento, "text": texto,
                              "start": ev.inicio, "end": ev.fin, "processing_ms": ms})

        tarea = asyncio.create_task(trabajador())
        await enviar({"type": "ready", "sample_rate": 16000, "encoding": "pcm_s16le", "channels": 1,
                      "language": idioma, "backend": s.backend})

        async def despachar(eventos):
            for ev in eventos:
                if ev.tipo == "speech_start":
                    await enviar({"type": "speech_start", "segment_id": ev.segmento, "start": ev.inicio})
                elif ev.tipo == "speech_end":
                    await enviar({"type": "speech_end", "segment_id": ev.segmento, "end": ev.fin})
                elif ev.tipo == "need_partial":
                    if not ocupado["parcial"] and cola.empty():
                        ocupado["parcial"] = True
                        await cola.put(ev)
                else:
                    await cola.put(ev)

        try:
            while True:
                msg = await ws.receive()
                if msg["type"] == "websocket.disconnect":
                    break
                if msg.get("bytes") is not None:
                    await despachar(seg.alimentar(au.pcm16_a_float(msg["bytes"])))
                elif msg.get("text") is not None:
                    try:
                        orden = json.loads(msg["text"])
                    except ValueError:
                        await enviar({"type": "error", "code": "invalid_message", "message": "Mensaje de texto no es JSON."})
                        continue
                    tipo = orden.get("type")
                    if tipo == "config" and orden.get("language"):
                        idioma = str(orden["language"])[:8]
                    elif tipo == "flush":
                        await despachar(seg.vaciar())
                    elif tipo == "close":
                        await despachar(seg.vaciar())
                        await cola.put(None)
                        await tarea
                        await enviar({"type": "closed"})
                        await ws.close(code=1000)
                        return
                    else:
                        await enviar({"type": "error", "code": "invalid_message", "message": f"Tipo desconocido: {tipo}"})
        except WebSocketDisconnect:
            pass
        finally:
            if not tarea.done():
                tarea.cancel()

    return app


def principal() -> None:
    import uvicorn

    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
    a = cargar()
    print(f"Yizi Voz Local {VERSION} en http://{a.host}:{a.puerto}  (token: {'sí' if a.token else 'no'})", flush=True)
    uvicorn.run(crear_app(a), host=a.host, port=a.puerto, log_level="info", access_log=False,
                ws_max_size=1 << 20)


if __name__ == "__main__":
    principal()
