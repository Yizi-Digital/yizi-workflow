#!/usr/bin/env bash
# Instala Yizi Voz Local: entorno de Python, dependencias y modelos.
# Uso: ./install.sh            (modelos por defecto)
#      ./install.sh --turbo    (añade Whisper large-v3-turbo para CPU, 1,6 GB)
#      ./install.sh --mlx      (Mac con Apple Silicon: mlx-whisper + modelo turbo MLX, 1,6 GB)
set -euo pipefail
cd "$(dirname "$0")"

EXTRA=()
MLX=0
for arg in "$@"; do
  case "$arg" in
    --turbo) EXTRA+=(--paquete whisper-large-v3-turbo) ;;
    --mlx)   MLX=1; EXTRA+=(--paquete mlx-whisper-large-v3-turbo) ;;
    -h|--help) sed -n 2,6p "$0"; exit 0 ;;
    *) echo "Opción desconocida: $arg"; exit 2 ;;
  esac
done

echo "== 1/3 Busco Python 3.11, 3.12 o 3.13"
PY=""
for c in python3.13 python3.12 python3.11 python3; do
  if command -v "$c" >/dev/null 2>&1; then
    if "$c" -c 'import sys; sys.exit(0 if (3,11) <= sys.version_info[:2] <= (3,13) else 1)'; then PY="$c"; break; fi
  fi
done
if [ -z "$PY" ]; then
  echo "No encontré Python 3.11 a 3.13."
  echo "En Mac: instala Homebrew (https://brew.sh) y luego: brew install python@3.12"
  exit 1
fi
echo "   Uso $("$PY" --version) ($PY)"

echo "== 2/3 Creo .venv e instalo dependencias (solo la primera vez tarda)"
[ -d .venv ] || "$PY" -m venv .venv
.venv/bin/python -m pip install --quiet --upgrade pip
.venv/bin/python -m pip install --quiet -r requirements.txt
if [ "$(uname -s)" = "Darwin" ] && [ "$(uname -m)" = "arm64" ]; then
  if [ "$MLX" = "1" ]; then
    .venv/bin/python -m pip install --quiet -r requirements-mlx.txt || echo "   Aviso: no se pudo instalar mlx-whisper; se usará faster-whisper."
  else
    echo "   Consejo: en tu Mac con Apple Silicon, ./install.sh --mlx activa la voz a texto con Metal (más rápida)."
  fi
fi

echo "== 3/3 Modelos en ./models (si ya están y sus sumas coinciden, no se descargan)"
if ! .venv/bin/python scripts/descargar_modelos.py ${EXTRA[@]+"${EXTRA[@]}"} --paquete whisper-small --paquete kokoro; then
  echo
  echo "Faltan modelos. Revisa tu conexión a internet y vuelve a ejecutar ./install.sh"
  echo "(lo ya descargado no se repite). El servidor arranca, pero sin la parte que falta."
  exit 1
fi

echo
echo "Listo. Arranca el servidor con: ./run.sh"
