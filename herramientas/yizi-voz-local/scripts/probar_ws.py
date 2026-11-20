#!/usr/bin/env python3
"""Envía un WAV al WebSocket de dictado como PCM 16 kHz mono 16 bits e imprime los mensajes.

Uso: python scripts/probar_ws.py audio.wav [http://127.0.0.1:8765] [--tiempo-real]
"""
from __future__ import annotations

import asyncio
import json
import os
import sys
import time
import wave

import numpy as np
import websockets


def leer_16k(ruta: str) -> bytes:
    with wave.open(ruta, "rb") as w:
        frec, canales = w.getframerate(), w.getnchannels()
        datos = np.frombuffer(w.readframes(w.getnframes()), dtype="<i2").astype(np.float32)
    if canales > 1:
        datos = datos.reshape(-1, canales).mean(axis=1)
    if frec != 16000:
        n = int(len(datos) * 16000 / frec)
        datos = np.interp(np.linspace(0, 1, n, endpoint=False), np.linspace(0, 1, len(datos), endpoint=False), datos)
    silencio = np.zeros(16000, dtype=np.float32)  # 1 s de silencio para cerrar el turno
    return np.concatenate([datos, silencio]).astype("<i2").tobytes()


async def main() -> None:
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    tiempo_real = "--tiempo-real" in sys.argv
    pcm = leer_16k(args[0])
    base = (args[1] if len(args) > 1 else "http://127.0.0.1:8765").replace("http", "ws", 1)
    cab = {}
    if os.environ.get("YIZI_VOZ_TOKEN"):
        cab["Authorization"] = "Bearer " + os.environ["YIZI_VOZ_TOKEN"]
    t0 = time.perf_counter()
    async with websockets.connect(base + "/v1/stream/transcribe?language=es", additional_headers=cab) as ws:
        primero = json.loads(await ws.recv())
        print("  <-", json.dumps(primero, ensure_ascii=False))
        if primero.get("type") != "ready":
            print("  El servidor no está listo para dictado (revisa GET /health).")
            return

        async def recibir():
            async for m in ws:
                d = json.loads(m)
                print(f"  <- [{time.perf_counter() - t0:5.2f}s] {json.dumps(d, ensure_ascii=False)}")
                if d.get("type") == "closed":
                    return

        r = asyncio.create_task(recibir())
        trozo = 640  # 20 ms
        for i in range(0, len(pcm), trozo):
            await ws.send(pcm[i:i + trozo])
            await asyncio.sleep(0.02 if tiempo_real else 0.002)
        await ws.send(json.dumps({"type": "close"}))
        await r


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (OSError, websockets.exceptions.WebSocketException) as e:
        print(f"  Error de WebSocket: {e}")
        sys.exit(1)
