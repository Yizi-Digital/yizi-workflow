#!/usr/bin/env bash
# Prueba cada endpoint con curl. Requiere el servidor en marcha (./run.sh).
# Uso: scripts/probar.sh            (o PUERTO=8765 YIZI_VOZ_TOKEN=... scripts/probar.sh)
set -euo pipefail
cd "$(dirname "$0")/.."
URL="http://127.0.0.1:${PUERTO:-8765}"
AUTH=()
[ -n "${YIZI_VOZ_TOKEN:-}" ] && AUTH=(-H "Authorization: Bearer ${YIZI_VOZ_TOKEN}")
TMP="$(mktemp -d)"; trap 'rm -rf "$TMP"' EXIT   # el audio de prueba se borra al salir

echo "== GET /health";    curl -sS "$URL/health"; echo
echo "== GET /v1/voices"; curl -sS ${AUTH[@]+"${AUTH[@]}"} "$URL/v1/voices" | head -c 600; echo

echo "== POST /v1/audio/speech (voz de Edith)"
curl -sS ${AUTH[@]+"${AUTH[@]}"} -X POST "$URL/v1/audio/speech" -H "Content-Type: application/json" \
  -d '{"input":"Hola, soy Edith. Esta es una prueba de voz local. Nada sale de tu equipo.","voice":"edith","speed":1.0,"response_format":"wav"}' \
  -o "$TMP/edith.wav" -w "   %{http_code}, %{size_download} bytes, primer byte %{time_starttransfer}s, total %{time_total}s\n"

echo "== POST /v1/audio/transcriptions (transcribe ese mismo audio)"
curl -sS ${AUTH[@]+"${AUTH[@]}"} -X POST "$URL/v1/audio/transcriptions" \
  -F "file=@$TMP/edith.wav;type=audio/wav" -F "language=es" -w "\n   %{http_code}, total %{time_total}s\n"

echo "== WS /v1/stream/transcribe (envía el audio como PCM 16 kHz)"
.venv/bin/python scripts/probar_ws.py "$TMP/edith.wav" "$URL"

if command -v afplay >/dev/null 2>&1 && [ "${ESCUCHAR:-0}" = "1" ]; then afplay "$TMP/edith.wav"; fi
