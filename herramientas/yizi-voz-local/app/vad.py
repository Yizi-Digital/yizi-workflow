"""Detección de voz en streaming con Silero VAD v6 (MIT).

Usa el archivo silero_vad_v6.onnx que ya trae faster-whisper: no hace falta otra descarga.
Procesa ventanas de 512 muestras (32 ms a 16 kHz) y conserva el estado entre ventanas.
"""
from __future__ import annotations

from pathlib import Path

import numpy as np

VENTANA = 512
CONTEXTO = 64


def ruta_modelo() -> Path:
    from faster_whisper.utils import get_assets_path

    return Path(get_assets_path()) / "silero_vad_v6.onnx"


class SileroStream:
    _sesion = None

    def __init__(self):
        if SileroStream._sesion is None:
            import onnxruntime as ort

            o = ort.SessionOptions()
            o.inter_op_num_threads = 1
            o.intra_op_num_threads = 1
            o.log_severity_level = 4
            SileroStream._sesion = ort.InferenceSession(str(ruta_modelo()), o, providers=["CPUExecutionProvider"])
        self.reiniciar()

    def reiniciar(self) -> None:
        self.h = np.zeros((1, 1, 128), dtype=np.float32)
        self.c = np.zeros((1, 1, 128), dtype=np.float32)
        self.contexto = np.zeros(CONTEXTO, dtype=np.float32)

    def probabilidad(self, ventana: np.ndarray) -> float:
        """ventana: 512 muestras float32 a 16 kHz."""
        x = np.concatenate([self.contexto, ventana.astype(np.float32)]).reshape(1, -1)
        prob, self.h, self.c = SileroStream._sesion.run(None, {"input": x, "h": self.h, "c": self.c})
        self.contexto = ventana[-CONTEXTO:].astype(np.float32)
        return float(np.asarray(prob).ravel()[0])
