import io
import json
import struct
import wave

import numpy as np
import pytest
from fastapi.testclient import TestClient

from app import ajustes
from app import audio as au
from app.servidor import crear_app
from app.tts import MotorVoz, VozAgente


class SttFalso:
    listo, backend, modelo_ruta, error = True, "falso", "/x/falso", ""

    def __init__(self):
        self.llamadas = []

    @staticmethod
    def decodificar(datos):
        audio, frec = au.leer_wav(datos)
        return au.remuestrear(audio, frec, 16000)

    def transcribir(self, audio, idioma=None, rapido=False, prompt=None):
        self.llamadas.append((len(audio), idioma, rapido))
        return "hola mundo"


class TtsFalso:
    motor, error_kokoro, kokoro, voces_say = "falso", "", None, []

    def __init__(self, a):
        self.agentes = {k: VozAgente(k, v.get("kokoro", ""), float(v.get("velocidad", 1)), v.get("say", "")) for k, v in a.agentes.items()}
        self.a = a

    resolver = MotorVoz.resolver
    frases = MotorVoz.frases

    def sintetizar_frase(self, frase, voz, vel):
        return np.full(2400, 0.1, dtype=np.float32), 24000

    def silencio(self):
        return np.zeros(240, dtype=np.float32)


def wav(segundos=1.0, frec=16000):
    buf = io.BytesIO()
    with wave.open(buf, "wb") as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(frec)
        w.writeframes(np.zeros(int(frec * segundos), dtype="<i2").tobytes())
    return buf.getvalue()


@pytest.fixture
def cliente(monkeypatch):
    monkeypatch.delenv("YIZI_VOZ_TOKEN", raising=False)
    a = ajustes.cargar()
    with TestClient(crear_app(a, SttFalso(), TtsFalso(a))) as c:
        yield c


def test_health(cliente):
    r = cliente.get("/health")
    assert r.status_code == 200 and r.json()["status"] == "ok"


def test_voces(cliente):
    d = cliente.get("/v1/voices").json()
    ids = {v["id"] for v in d["voices"]}
    assert {"ultron", "vision", "jarvis", "edith", "viernes", "aida", "termy", "lince", "karen", "herbie", "homer"} <= ids


def test_speech_wav_por_frases(cliente):
    r = cliente.post("/v1/audio/speech", json={"input": "Hola. Soy Edith.", "voice": "edith", "speed": 1.0, "response_format": "wav"})
    assert r.status_code == 200
    assert r.headers["content-type"] == "audio/wav"
    assert r.headers["x-sentences"] == "2"
    assert r.content[:4] == b"RIFF" and r.content[8:12] == b"WAVE"
    assert struct.unpack("<I", r.content[24:28])[0] == 24000
    assert len(r.content) == 44 + 2 * (2400 * 2 + 240)


def test_speech_errores(cliente):
    assert cliente.post("/v1/audio/speech", json={"input": "hola", "voice": "nadie"}).json()["error"]["code"] == "voice_not_found"
    assert cliente.post("/v1/audio/speech", json={"input": "hola", "response_format": "mp3"}).status_code == 400
    assert cliente.post("/v1/audio/speech", json={"input": "  "}).status_code == 400
    assert cliente.post("/v1/audio/speech", json={"input": "hola", "speed": 5}).status_code == 400


def test_transcripcion(cliente):
    r = cliente.post("/v1/audio/transcriptions", files={"file": ("a.wav", wav(), "audio/wav")}, data={"language": "es"})
    assert r.status_code == 200 and r.json()["text"] == "hola mundo"


def test_transcripcion_audio_roto(cliente):
    r = cliente.post("/v1/audio/transcriptions", files={"file": ("a.wav", b"no es audio", "audio/wav")})
    assert r.status_code == 415


def test_token(monkeypatch):
    monkeypatch.setenv("YIZI_VOZ_TOKEN", "secreto-de-prueba")
    a = ajustes.cargar()
    with TestClient(crear_app(a, SttFalso(), TtsFalso(a))) as c:
        assert c.get("/health").status_code == 200  # salud sin token
        assert c.get("/v1/voices").status_code == 401
        assert c.get("/v1/voices", headers={"Authorization": "Bearer secreto-de-prueba"}).status_code == 200
        from starlette.websockets import WebSocketDisconnect

        with c.websocket_connect("/v1/stream/transcribe") as ws:
            with pytest.raises(WebSocketDisconnect) as e:
                ws.receive_json()
        assert e.value.code == 4401
        with c.websocket_connect("/v1/stream/transcribe", headers={"Authorization": "Bearer secreto-de-prueba"}) as ws:
            assert ws.receive_json()["type"] == "ready"


def test_websocket_silencio(cliente):
    with cliente.websocket_connect("/v1/stream/transcribe") as ws:
        assert ws.receive_json()["type"] == "ready"
        ws.send_bytes(np.zeros(16000, dtype="<i2").tobytes())
        ws.send_text(json.dumps({"type": "close"}))
        assert ws.receive_json()["type"] == "closed"


class VadFalso:
    def __init__(self, probs):
        self.probs = iter(probs)

    def probabilidad(self, v):
        return next(self.probs, 0.0)

    def reiniciar(self):
        pass


def test_segmento_corto_se_descarta():
    from app.flujo import Segmentador

    # 8 ventanas de voz (256 ms) y luego silencio: menos de 400 ms -> descartado
    s = Segmentador(VadFalso([0.9] * 8 + [0.0] * 40), min_final_ms=400)
    ev = s.alimentar(np.zeros(512 * 48, dtype=np.float32))
    finales = [e for e in ev if e.tipo == "need_final"]
    assert len(finales) == 1 and finales[0].extra["discarded"] is True
    # 30 ventanas de voz (960 ms): se transcribe
    s = Segmentador(VadFalso([0.9] * 30 + [0.0] * 40), min_final_ms=400)
    ev = s.alimentar(np.zeros(512 * 70, dtype=np.float32))
    assert [e.extra["discarded"] for e in ev if e.tipo == "need_final"] == [False]


def test_prompt_por_defecto():
    a = ajustes.cargar()
    assert "Edith" in a.stt_prompt and "Yizi" in a.stt_prompt
