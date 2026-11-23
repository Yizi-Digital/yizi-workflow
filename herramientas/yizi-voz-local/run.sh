#!/usr/bin/env bash
# Arranca Yizi Voz Local en http://127.0.0.1:8765 (o el puerto de config/config.yaml).
# Token opcional:  YIZI_VOZ_TOKEN="algo-secreto" ./run.sh
# Detener: Ctrl+C en esta ventana.
set -euo pipefail
cd "$(dirname "$0")"
if [ ! -x .venv/bin/python ]; then
  echo "Falta instalar. Ejecuta primero: ./install.sh"; exit 1
fi
export HF_HUB_OFFLINE=1          # nunca descarga nada al arrancar
export PYTHONDONTWRITEBYTECODE=1
exec .venv/bin/python -m app.servidor
