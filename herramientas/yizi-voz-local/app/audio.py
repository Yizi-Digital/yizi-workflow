"""Utilidades de audio en memoria: WAV, PCM y remuestreo. Nada se escribe en disco."""
from __future__ import annotations

import io
import struct
import wave

import numpy as np


def float_a_pcm16(audio: np.ndarray) -> bytes:
    audio = np.clip(np.asarray(audio, dtype=np.float32), -1.0, 1.0)
    return (audio * 32767.0).astype("<i2").tobytes()


def pcm16_a_float(datos: bytes) -> np.ndarray:
    if len(datos) % 2:
        datos = datos[:-1]
    return np.frombuffer(datos, dtype="<i2").astype(np.float32) / 32768.0


def cabecera_wav_stream(frecuencia: int, canales: int = 1, bits: int = 16) -> bytes:
    """Cabecera WAV para streaming: tamaños 0xFFFFFFFF (longitud desconocida).

    Es la misma convención que usan otros servidores de voz en streaming.
    La mayoría de reproductores la aceptan; si un cliente no, que pida 'pcm'.
    """
    tasa_bytes = frecuencia * canales * bits // 8
    alineacion = canales * bits // 8
    return (
        b"RIFF" + struct.pack("<I", 0xFFFFFFFF) + b"WAVE"
        + b"fmt " + struct.pack("<IHHIIHH", 16, 1, canales, frecuencia, tasa_bytes, alineacion, bits)
        + b"data" + struct.pack("<I", 0xFFFFFFFF)
    )


def wav_completo(audio: np.ndarray, frecuencia: int) -> bytes:
    buf = io.BytesIO()
    with wave.open(buf, "wb") as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(frecuencia)
        w.writeframes(float_a_pcm16(audio))
    return buf.getvalue()


def leer_wav(datos: bytes) -> tuple[np.ndarray, int]:
    """Lee un WAV PCM 16 bits en memoria. Mezcla a mono si hace falta."""
    with wave.open(io.BytesIO(datos), "rb") as w:
        canales, ancho, frec = w.getnchannels(), w.getsampwidth(), w.getframerate()
        crudo = w.readframes(w.getnframes())
    if ancho != 2:
        raise ValueError("Solo se admite WAV PCM de 16 bits")
    audio = pcm16_a_float(crudo)
    if canales > 1:
        audio = audio.reshape(-1, canales).mean(axis=1)
    return audio, frec


def remuestrear(audio: np.ndarray, origen: int, destino: int) -> np.ndarray:
    """Remuestreo lineal simple (suficiente para voz)."""
    if origen == destino or len(audio) == 0:
        return audio.astype(np.float32)
    n = int(round(len(audio) * destino / origen))
    x_viejo = np.linspace(0.0, 1.0, num=len(audio), endpoint=False)
    x_nuevo = np.linspace(0.0, 1.0, num=n, endpoint=False)
    return np.interp(x_nuevo, x_viejo, audio).astype(np.float32)
