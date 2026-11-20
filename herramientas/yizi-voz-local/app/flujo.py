"""Lógica del dictado en streaming: VAD + parciales + finales. Sin red, para poder probarla sola."""
from __future__ import annotations

import time
from dataclasses import dataclass, field

import numpy as np

from .vad import VENTANA

FRECUENCIA = 16000


@dataclass
class Evento:
    tipo: str  # speech_start | speech_end | need_partial | need_final
    segmento: int
    audio: np.ndarray | None = None
    inicio: float = 0.0
    fin: float = 0.0
    extra: dict = field(default_factory=dict)


class Segmentador:
    """Recibe PCM float32 16 kHz por trozos y emite eventos según la detección de voz."""

    def __init__(self, vad, umbral=0.5, silencio_fin_ms=600, parcial_cada_ms=800,
                 max_segmento_s=25.0, preroll_ms=300, min_voz_ms=250, min_final_ms=400):
        self.vad = vad
        self.umbral = umbral
        self.umbral_bajo = max(0.05, umbral - 0.15)
        self.v_silencio = max(1, int(silencio_fin_ms / 32))
        self.v_parcial = max(1, int(parcial_cada_ms / 32))
        self.v_max = int(max_segmento_s * FRECUENCIA / VENTANA)
        self.v_preroll = max(0, int(preroll_ms / 32))
        self.v_min_voz = max(1, int(min_voz_ms / 32))
        self.v_min_final = max(0, int(min_final_ms / 32))
        self.voz_en_segmento = 0
        self.pendiente = np.zeros(0, dtype=np.float32)
        self.previas: list[np.ndarray] = []
        self.segmento_actual: list[np.ndarray] = []
        self.hablando = False
        self.silencio = 0
        self.voz = 0
        self.desde_parcial = 0
        self.n_segmento = 0
        self.ventanas = 0
        self.t_inicio = 0.0
        self.creado = time.monotonic()

    def _t(self) -> float:
        return round(self.ventanas * VENTANA / FRECUENCIA, 3)

    def alimentar(self, audio: np.ndarray) -> list[Evento]:
        eventos: list[Evento] = []
        self.pendiente = np.concatenate([self.pendiente, audio.astype(np.float32)])
        while len(self.pendiente) >= VENTANA:
            v, self.pendiente = self.pendiente[:VENTANA], self.pendiente[VENTANA:]
            self.ventanas += 1
            p = self.vad.probabilidad(v)
            if not self.hablando:
                self.previas.append(v)
                if len(self.previas) > self.v_preroll + self.v_min_voz:
                    self.previas.pop(0)
                self.voz = self.voz + 1 if p >= self.umbral else 0
                if self.voz >= max(1, self.v_min_voz // 2):
                    self.hablando = True
                    self.n_segmento += 1
                    self.segmento_actual = list(self.previas)
                    self.voz_en_segmento = self.voz
                    self.previas = []
                    self.silencio = 0
                    self.desde_parcial = 0
                    self.t_inicio = max(0.0, self._t() - len(self.segmento_actual) * VENTANA / FRECUENCIA)
                    eventos.append(Evento("speech_start", self.n_segmento, inicio=self.t_inicio))
                continue
            self.segmento_actual.append(v)
            if p >= self.umbral:
                self.voz_en_segmento += 1
            self.desde_parcial += 1
            self.silencio = self.silencio + 1 if p < self.umbral_bajo else 0
            if self.silencio >= self.v_silencio or len(self.segmento_actual) >= self.v_max:
                eventos.extend(self._cerrar())
            elif self.desde_parcial >= self.v_parcial:
                self.desde_parcial = 0
                eventos.append(Evento("need_partial", self.n_segmento, audio=np.concatenate(self.segmento_actual),
                                      inicio=self.t_inicio, fin=self._t()))
        return eventos

    def _cerrar(self) -> list[Evento]:
        audio = np.concatenate(self.segmento_actual) if self.segmento_actual else np.zeros(0, np.float32)
        ev = [Evento("speech_end", self.n_segmento, inicio=self.t_inicio, fin=self._t()),
              Evento("need_final", self.n_segmento, audio=audio, inicio=self.t_inicio, fin=self._t(),
                     extra={"discarded": self.voz_en_segmento < self.v_min_final})]
        self.voz_en_segmento = 0
        self.hablando = False
        self.segmento_actual = []
        self.silencio = 0
        self.voz = 0
        self.vad.reiniciar()
        return ev

    def vaciar(self) -> list[Evento]:
        """Cierra el segmento en curso (mensaje 'flush' o fin del audio)."""
        if self.hablando:
            return self._cerrar()
        return []
