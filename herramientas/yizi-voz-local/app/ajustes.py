"""Lectura de la configuración (config/config.yaml, config/voces.yaml, config/pronunciacion.yaml)."""
from __future__ import annotations

import os
import platform
import sys
from dataclasses import dataclass, field
from pathlib import Path

import yaml

RAIZ = Path(os.environ.get("YIZI_VOZ_DIR") or Path(__file__).resolve().parent.parent)
HOSTS_LOCALES = {"127.0.0.1", "::1", "localhost"}


def _leer_yaml(ruta: Path) -> dict:
    if not ruta.exists():
        return {}
    with ruta.open(encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


def _ruta(valor: str) -> Path:
    p = Path(valor).expanduser()
    return p if p.is_absolute() else RAIZ / p


def es_mac_arm64() -> bool:
    return sys.platform == "darwin" and platform.machine() == "arm64"


@dataclass
class Ajustes:
    host: str = "127.0.0.1"
    puerto: int = 8765
    token: str = ""
    max_audio_mb: int = 25
    max_texto: int = 4096
    stt_backend: str = "auto"
    stt_modelo: Path = field(default_factory=lambda: RAIZ / "models/whisper/faster-whisper-small")
    stt_modelo_mlx: Path = field(default_factory=lambda: RAIZ / "models/whisper/mlx-whisper-large-v3-turbo")
    stt_idioma: str = "es"
    stt_compute_type: str = "int8"
    stt_hilos: int = 0
    stt_beam_size: int = 1
    stt_prompt: str = ""
    tts_motor: str = "auto"
    tts_modelo: Path = field(default_factory=lambda: RAIZ / "models/kokoro/kokoro-v1.0.onnx")
    tts_voces: Path = field(default_factory=lambda: RAIZ / "models/kokoro/voices-v1.0.bin")
    tts_pausa_ms: int = 120
    vad_umbral: float = 0.5
    vad_silencio_fin_ms: int = 600
    vad_parcial_cada_ms: int = 800
    vad_max_segmento_s: float = 25.0
    vad_preroll_ms: int = 300
    vad_min_final_ms: int = 400
    agentes: dict = field(default_factory=dict)
    voz_por_defecto: str = "vision"
    lexico: dict = field(default_factory=dict)


def cargar(ruta_config: Path | None = None) -> Ajustes:
    cfg = _leer_yaml(ruta_config or RAIZ / "config/config.yaml")
    voces = _leer_yaml(RAIZ / "config/voces.yaml")
    pron = _leer_yaml(RAIZ / "config/pronunciacion.yaml")
    a = Ajustes()
    srv, stt, tts, vad = (cfg.get(k) or {} for k in ("servidor", "stt", "tts", "vad"))

    a.host = str(srv.get("host", a.host))
    a.puerto = int(os.environ.get("YIZI_VOZ_PUERTO") or srv.get("puerto", a.puerto))
    a.max_audio_mb = int(srv.get("max_audio_mb", a.max_audio_mb))
    a.max_texto = int(srv.get("max_texto", a.max_texto))
    # El token solo llega por variable de entorno: nunca se guarda en el repo.
    a.token = os.environ.get("YIZI_VOZ_TOKEN", "")

    a.stt_backend = os.environ.get("YIZI_VOZ_STT_BACKEND") or stt.get("backend", a.stt_backend)
    if stt.get("modelo"):
        a.stt_modelo = _ruta(stt["modelo"])
    if stt.get("modelo_mlx"):
        a.stt_modelo_mlx = _ruta(stt["modelo_mlx"])
    a.stt_idioma = stt.get("idioma", a.stt_idioma)
    a.stt_compute_type = stt.get("compute_type", a.stt_compute_type)
    a.stt_hilos = int(stt.get("hilos", a.stt_hilos))
    a.stt_beam_size = int(stt.get("beam_size", a.stt_beam_size))
    a.stt_prompt = str(stt.get("prompt") or "").strip()

    a.tts_motor = os.environ.get("YIZI_VOZ_TTS_MOTOR") or tts.get("motor", a.tts_motor)
    if tts.get("modelo"):
        a.tts_modelo = _ruta(tts["modelo"])
    if tts.get("voces"):
        a.tts_voces = _ruta(tts["voces"])
    a.tts_pausa_ms = int(tts.get("pausa_entre_frases_ms", a.tts_pausa_ms))

    a.vad_umbral = float(vad.get("umbral", a.vad_umbral))
    a.vad_silencio_fin_ms = int(vad.get("silencio_fin_ms", a.vad_silencio_fin_ms))
    a.vad_parcial_cada_ms = int(vad.get("parcial_cada_ms", a.vad_parcial_cada_ms))
    a.vad_max_segmento_s = float(vad.get("max_segmento_s", a.vad_max_segmento_s))
    a.vad_preroll_ms = int(vad.get("preroll_ms", a.vad_preroll_ms))
    a.vad_min_final_ms = int(vad.get("min_final_ms", a.vad_min_final_ms))

    a.agentes = {str(k).lower(): v or {} for k, v in (voces.get("agentes") or {}).items()}
    a.voz_por_defecto = str(voces.get("por_defecto", a.voz_por_defecto)).lower()
    a.lexico = {str(k): str(v) for k, v in (pron.get("palabras") or {}).items()}

    if a.host not in HOSTS_LOCALES:
        raise ValueError(
            f"host '{a.host}' no permitido: Yizi Voz Local solo escucha en 127.0.0.1 (o ::1)."
        )
    if a.host == "localhost":
        a.host = "127.0.0.1"
    return a
