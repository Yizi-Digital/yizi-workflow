"""Pruebas con los modelos reales. Se saltan si no están en ./models."""
import os
import time

import numpy as np
import pytest

from app import ajustes
from app import audio as au

A = ajustes.cargar()
HAY_KOKORO = A.tts_modelo.exists() and A.tts_voces.exists()
HAY_WHISPER = (A.stt_modelo / "model.bin").exists()


@pytest.mark.skipif(not HAY_KOKORO, reason="falta el modelo Kokoro")
def test_kokoro_todas_las_voces():
    from app.tts import MotorVoz

    m = MotorVoz(A)
    assert m.motor == "kokoro"
    for aid in m.agentes:
        audio, frec = m.sintetizar_frase("Hola, soy parte del equipo.", m.resolver(aid), 1.0)
        assert frec == 24000 and len(audio) > 24000 * 0.5, aid
        assert float(np.abs(audio).max()) > 0.05, aid


@pytest.mark.skipif(not HAY_KOKORO, reason="falta el modelo Kokoro")
def test_vad_y_segmentador_con_voz_real():
    from app.flujo import Segmentador
    from app.tts import MotorVoz
    from app.vad import SileroStream

    m = MotorVoz(A)
    v = m.resolver("vision")
    a1, _ = m.sintetizar_frase("Primera frase del dictado.", v, 1.0)
    a2, _ = m.sintetizar_frase("Y esta es la segunda frase.", v, 1.0)
    silencio = np.zeros(int(24000 * 1.2), dtype=np.float32)
    todo = au.remuestrear(np.concatenate([a1, silencio, a2, silencio]), 24000, 16000)
    s = Segmentador(SileroStream())
    eventos = []
    for i in range(0, len(todo), 320):
        eventos += s.alimentar(todo[i:i + 320])
    finales = [e for e in eventos if e.tipo == "need_final"]
    assert len(finales) == 2


@pytest.mark.skipif(not (HAY_KOKORO and HAY_WHISPER), reason="faltan modelos")
def test_ida_y_vuelta():
    from app.stt import MotorTexto
    from app.tts import MotorVoz

    m, s = MotorVoz(A), MotorTexto(A)
    audio, _ = m.sintetizar_frase("Buenos días, el pedido llegó a tiempo.", m.resolver("edith"), 1.0)
    texto = s.transcribir(au.remuestrear(audio, 24000, 16000), "es").lower()
    assert "pedido" in texto


@pytest.mark.skipif(not HAY_KOKORO, reason="falta el modelo Kokoro")
def test_websocket_con_voz_real_y_stt_falso():
    import json

    from fastapi.testclient import TestClient

    from app.servidor import crear_app
    from app.tts import MotorVoz
    from tests.test_api import SttFalso

    m = MotorVoz(A)
    a1, _ = m.sintetizar_frase("Necesito el informe de ventas.", m.resolver("vision"), 1.0)
    pcm = au.float_a_pcm16(au.remuestrear(np.concatenate([a1, np.zeros(24000, np.float32)]), 24000, 16000))
    with TestClient(crear_app(A, SttFalso(), m)) as c, c.websocket_connect("/v1/stream/transcribe") as ws:
        assert ws.receive_json()["type"] == "ready"
        for i in range(0, len(pcm), 640):
            ws.send_bytes(pcm[i:i + 640])
        ws.send_text(json.dumps({"type": "close"}))
        tipos = []
        while True:
            d = ws.receive_json()
            tipos.append(d["type"])
            if d["type"] == "closed":
                break
    assert tipos.count("speech_start") == 1 and tipos.count("final") == 1, tipos
