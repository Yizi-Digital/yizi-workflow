"""Voz a texto: faster-whisper (CPU, int8) o mlx-whisper (Metal, Mac con Apple Silicon)."""
from __future__ import annotations

import io
import os
import threading

import numpy as np

from .ajustes import es_mac_arm64

FRECUENCIA = 16000


class MotorTexto:
    def __init__(self, ajustes):
        self.a = ajustes
        self.backend = ""
        self.modelo_ruta = ""
        self.error = ""
        self._modelo = None
        self._mlx = None
        self._candado = threading.Lock()
        self._cargar()

    @property
    def listo(self) -> bool:
        return self._modelo is not None or self._mlx is not None

    def _cargar(self) -> None:
        quiere = self.a.stt_backend
        if quiere in ("auto", "mlx") and es_mac_arm64():
            try:
                import mlx_whisper  # noqa: F401

                if not (self.a.stt_modelo_mlx / "config.json").exists():
                    raise FileNotFoundError(f"no está el modelo MLX en {self.a.stt_modelo_mlx}")
                self._mlx = mlx_whisper
                self.backend, self.modelo_ruta = "mlx-whisper", str(self.a.stt_modelo_mlx)
                return
            except Exception as e:
                self.error = f"mlx no disponible ({e}); uso faster-whisper"
                if quiere == "mlx":
                    self.error = f"mlx pedido pero no disponible: {e}"
        try:
            from faster_whisper import WhisperModel

            if not (self.a.stt_modelo / "model.bin").exists():
                raise FileNotFoundError(f"no está el modelo en {self.a.stt_modelo}. Ejecuta install.sh")
            self._modelo = WhisperModel(
                str(self.a.stt_modelo), device="cpu", compute_type=self.a.stt_compute_type,
                cpu_threads=self.a.stt_hilos or min(8, os.cpu_count() or 4),
            )
            self.backend, self.modelo_ruta = "faster-whisper", str(self.a.stt_modelo)
        except Exception as e:
            self.error = (self.error + "; " if self.error else "") + str(e)

    @staticmethod
    def decodificar(datos: bytes) -> np.ndarray:
        """Decodifica cualquier formato que entienda FFmpeg (wav, m4a, mp3, ogg...) en memoria."""
        from faster_whisper.audio import decode_audio

        return decode_audio(io.BytesIO(datos), sampling_rate=FRECUENCIA)

    def transcribir(self, audio: np.ndarray, idioma: str | None = None, rapido: bool = False,
                    prompt: str | None = None) -> str:
        """audio: float32 mono a 16 kHz. rapido=True para parciales (sin filtro VAD)."""
        if not self.listo:
            raise RuntimeError(f"El modelo de voz a texto no está cargado: {self.error}")
        idioma = idioma or self.a.stt_idioma
        prompt = prompt or self.a.stt_prompt or None  # nombres propios para que Whisper los escriba bien
        if len(audio) < FRECUENCIA * 0.1:
            return ""
        with self._candado:
            if self._mlx is not None:
                r = self._mlx.transcribe(audio.astype(np.float32), path_or_hf_repo=self.modelo_ruta,
                                         language=idioma, initial_prompt=prompt, verbose=None,
                                         condition_on_previous_text=False)
                return (r.get("text") or "").strip()
            segmentos, _ = self._modelo.transcribe(
                audio, language=idioma, beam_size=self.a.stt_beam_size, vad_filter=not rapido,
                initial_prompt=prompt, condition_on_previous_text=False, without_timestamps=True,
            )
            return " ".join(s.text.strip() for s in segmentos).strip()
