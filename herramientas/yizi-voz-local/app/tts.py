"""Texto a voz: Kokoro-82M en ONNX (principal) y el comando `say` de macOS (respaldo).

Kokoro se ejecuta con onnxruntime directamente, sin kokoro-onnx, para no depender de
espeak-ng ni de phonemizer (GPL-3.0). Los fonemas salen de app/g2p_es.py.
"""
from __future__ import annotations

import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import threading
from dataclasses import dataclass
from pathlib import Path

import numpy as np

from . import audio as au
from .g2p_es import dividir_frases, texto_a_fonemas

FRECUENCIA_KOKORO = 24000
MAX_FONEMAS = 510
VOCAB = json.loads((Path(__file__).parent / "kokoro_vocab.json").read_text(encoding="utf-8"))
_MEZCLA = re.compile(r"^\s*([a-z]{2}_[a-z]+)\s*(?:\*\s*([0-9.]+))?\s*$")


@dataclass
class VozAgente:
    id: str
    kokoro: str
    velocidad: float
    say: str
    descripcion: str = ""


class ErrorVoz(ValueError):
    """Voz desconocida o mal configurada."""


class Kokoro:
    def __init__(self, modelo: Path, voces: Path, hilos: int = 0):
        import onnxruntime as ort

        opciones = ort.SessionOptions()
        if hilos:
            opciones.intra_op_num_threads = hilos
        opciones.log_severity_level = 3
        self.sesion = ort.InferenceSession(str(modelo), opciones, providers=["CPUExecutionProvider"])
        self.voces = dict(np.load(str(voces)))
        nombres = {i.name for i in self.sesion.get_inputs()}
        self.entrada_tokens = "input_ids" if "input_ids" in nombres else "tokens"

    def estilo(self, especificacion: str) -> np.ndarray:
        """'em_alex' o una mezcla 'em_alex*0.6+em_santa*0.4'."""
        partes = [p for p in especificacion.split("+") if p.strip()]
        total, mezcla = 0.0, None
        for p in partes:
            m = _MEZCLA.match(p)
            if not m or m.group(1) not in self.voces:
                raise ErrorVoz(f"Voz de Kokoro desconocida: '{p.strip()}'")
            peso = float(m.group(2) or 1.0)
            v = self.voces[m.group(1)] * peso
            mezcla = v if mezcla is None else mezcla + v
            total += peso
        if mezcla is None or total <= 0:
            raise ErrorVoz(f"Voz de Kokoro vacía: '{especificacion}'")
        return (mezcla / total).astype(np.float32)

    def sintetizar_fonemas(self, fonemas: str, estilo: np.ndarray, velocidad: float) -> np.ndarray:
        tokens = [VOCAB[c] for c in fonemas if c in VOCAB][:MAX_FONEMAS]
        if not tokens:
            return np.zeros(0, dtype=np.float32)
        ref = estilo[min(len(tokens), len(estilo)) - 1]  # (1, 256)
        salida = self.sesion.run(None, {
            self.entrada_tokens: np.array([[0, *tokens, 0]], dtype=np.int64),
            "style": np.asarray(ref, dtype=np.float32).reshape(1, -1),
            "speed": np.array([velocidad], dtype=np.float32),
        })
        return np.asarray(salida[0], dtype=np.float32).ravel()


def voces_say_disponibles() -> list[str]:
    if sys.platform != "darwin" or not shutil.which("say"):
        return []
    try:
        salida = subprocess.run(["say", "-v", "?"], capture_output=True, text=True, timeout=10).stdout
    except Exception:
        return []
    voces = []
    for linea in salida.splitlines():
        m = re.match(r"^(.+?)\s{2,}(es[_-]\w+)\s", linea)
        if m:
            voces.append(m.group(1).strip())
    return voces


class MotorVoz:
    """Elige Kokoro o `say` y sintetiza frase a frase."""

    def __init__(self, ajustes):
        self.a = ajustes
        self.kokoro: Kokoro | None = None
        self.error_kokoro = ""
        self.voces_say = voces_say_disponibles()
        self.motor = "ninguno"
        self._candado_say = threading.Lock()
        quiere = ajustes.tts_motor
        if quiere in ("auto", "kokoro"):
            try:
                if not ajustes.tts_modelo.exists() or not ajustes.tts_voces.exists():
                    raise FileNotFoundError(f"faltan {ajustes.tts_modelo.name} o {ajustes.tts_voces.name} en models/kokoro")
                self.kokoro = Kokoro(ajustes.tts_modelo, ajustes.tts_voces)
                self.motor = "kokoro"
            except Exception as e:  # sin modelo o sin onnxruntime
                self.error_kokoro = str(e)
        if self.motor == "ninguno" and quiere in ("auto", "say") and shutil.which("say"):
            self.motor = "say"
        self.agentes = self._cargar_agentes()

    def _cargar_agentes(self) -> dict[str, VozAgente]:
        agentes = {}
        for aid, conf in self.a.agentes.items():
            agentes[aid] = VozAgente(
                id=aid,
                kokoro=str(conf.get("kokoro", "em_alex")),
                velocidad=float(conf.get("velocidad", 1.0)),
                say=str(conf.get("say", "")),
                descripcion=str(conf.get("descripcion", "")),
            )
            if self.kokoro:
                self.kokoro.estilo(agentes[aid].kokoro)  # falla pronto si la voz no existe
        return agentes

    def resolver(self, voz: str | None) -> VozAgente:
        vid = (voz or self.a.voz_por_defecto).strip().lower()
        if vid in self.agentes:
            return self.agentes[vid]
        if self.kokoro and vid in self.kokoro.voces:
            return VozAgente(id=vid, kokoro=vid, velocidad=1.0, say="")
        raise ErrorVoz(f"Voz desconocida: '{voz}'. Consulta GET /v1/voices.")

    def frases(self, texto: str) -> list[str]:
        return dividir_frases(texto)

    def sintetizar_frase(self, frase: str, voz: VozAgente, velocidad: float) -> tuple[np.ndarray, int]:
        """Devuelve audio float32 a 24 kHz para una frase."""
        vel = max(0.5, min(2.0, voz.velocidad * velocidad))
        if self.motor == "kokoro" and self.kokoro:
            fonemas = texto_a_fonemas(frase, self.a.lexico)
            return self.kokoro.sintetizar_fonemas(fonemas, self.kokoro.estilo(voz.kokoro), vel), FRECUENCIA_KOKORO
        if self.motor == "say":
            return self._say(frase, voz, vel), FRECUENCIA_KOKORO
        raise RuntimeError("No hay motor de voz: falta el modelo Kokoro y no hay 'say' (solo macOS).")

    def _say(self, frase: str, voz: VozAgente, vel: float) -> np.ndarray:
        """`say` no escribe a la salida estándar: usa un archivo temporal privado que se borra al instante."""
        nombre = voz.say if voz.say in self.voces_say else (self.voces_say[0] if self.voces_say else "")
        with self._candado_say, tempfile.TemporaryDirectory(prefix="yizi-voz-") as tmp:
            os.chmod(tmp, 0o700)
            salida = Path(tmp) / "f.wav"
            cmd = ["say", "-r", str(int(175 * vel)), "-o", str(salida),
                   "--file-format=WAVE", f"--data-format=LEI16@{FRECUENCIA_KOKORO}"]
            if nombre:
                cmd += ["-v", nombre]
            cmd += ["--", frase]
            subprocess.run(cmd, check=True, timeout=60, capture_output=True)
            datos = salida.read_bytes()
        audio, frec = au.leer_wav(datos)
        return au.remuestrear(audio, frec, FRECUENCIA_KOKORO)

    def silencio(self) -> np.ndarray:
        return np.zeros(int(FRECUENCIA_KOKORO * self.a.tts_pausa_ms / 1000), dtype=np.float32)
