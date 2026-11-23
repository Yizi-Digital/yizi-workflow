# Licencias · Yizi Voz Local

Revisado por Vision el 2026-11-20. Fuente de cada licencia: la ficha del modelo en Hugging Face, el archivo LICENSE del repositorio o los metadatos del paquete instalado (`importlib.metadata`). Esto no es asesoría legal.

**Resumen:** nada de lo que se instala obliga a la app Sala Yizi a cambiar su licencia. La app habla con este servidor por HTTP, como un proceso aparte, y no enlaza ninguna de sus librerías. No se usan Piper, espeak-ng ni phonemizer (GPL-3.0).

## Código propio

| Componente | Licencia |
|---|---|
| Código de Yizi Voz Local (`app/`, `scripts/`, `tests/`), incluido el conversor de español a fonemas `app/g2p_es.py` | Sin licencia definida. Uso interno hasta que el CEO decida |
| `app/kokoro_vocab.json` (tabla de fonemas de Kokoro, copiada de `config.json` de hexgrad/Kokoro-82M) | Apache-2.0 |

## Modelos

| Modelo | Origen | Licencia | Estado |
|---|---|---|---|
| Whisper *small* en formato CTranslate2 | `Systran/faster-whisper-small` (revisión `536b066`) | MIT | Verificado en la ficha de Hugging Face |
| Whisper *large-v3-turbo* en CTranslate2 (opcional) | `dropbox-dash/faster-whisper-large-v3-turbo` (antes `mobiuslabsgmbh`, revisión `0a363e9`) | MIT | Verificado en la ficha de Hugging Face |
| Whisper *large-v3-turbo* y *small* para MLX (opcionales) | `mlx-community/whisper-large-v3-turbo`, `mlx-community/whisper-small-mlx` | MIT, heredada de Whisper de OpenAI | **No verificado:** las fichas de mlx-community no declaran licencia |
| Kokoro-82M v1.0 en ONNX y `voices-v1.0.bin` | Release `model-files-v1.0` de github.com/thewh1teagle/kokoro-onnx; pesos de hexgrad/Kokoro-82M | Apache-2.0 (pesos); MIT (repo de conversión) | Verificado en la ficha de hexgrad/Kokoro-82M |
| Silero VAD v6 (`silero_vad_v6.onnx`, incluido en el paquete faster-whisper) | github.com/snakers4/silero-vad | MIT | Verificado en el archivo LICENSE del repo |

## Librerías de Python (`requirements.txt`)

| Paquete | Licencia |
|---|---|
| fastapi | MIT |
| starlette | BSD-3-Clause |
| pydantic, pydantic-core | MIT |
| uvicorn | BSD-3-Clause |
| websockets | BSD-3-Clause |
| python-multipart | Apache-2.0 |
| PyYAML | MIT |
| numpy | BSD-3-Clause (y licencias permisivas de sus partes) |
| onnxruntime | MIT |
| faster-whisper | MIT |
| ctranslate2 | MIT |
| av (PyAV) | BSD-3-Clause. **Ver nota sobre FFmpeg** |
| tokenizers | Apache-2.0 |
| huggingface_hub, hf-xet | Apache-2.0 |
| certifi | MPL-2.0 |
| tqdm (dependencia) | MPL-2.0 y MIT |
| anyio, h11, click, filelock, idna, fsspec, protobuf, flatbuffers, packaging y otras dependencias | MIT, BSD o Apache-2.0 |
| mlx-whisper, mlx (solo con `--mlx`) | MIT |
| pytest, httpx (solo pruebas) | MIT, BSD-3-Clause |

### Nota sobre FFmpeg dentro de PyAV

- faster-whisper necesita PyAV para leer archivos de audio. La rueda de PyAV trae FFmpeg compilado como **LGPL-3.0** (`libavcodec license: LGPL version 3 or later`, comprobado en la rueda de Linux).
- La rueda de Linux también trae librerías GPL (`libx264`, `libx265`) como archivos aparte. El servidor solo decodifica audio y no las usa. El contenido de la rueda de macOS **no se revisó**.
- LGPL permite este uso: son librerías dinámicas dentro del entorno del servidor, no de la app.

## Herramientas del sistema

| Herramienta | Licencia | Uso |
|---|---|---|
| `say` de macOS y sus voces | De Apple, parte de macOS | Respaldo de texto a voz, solo en la Mac del usuario |
| Python | PSF-2.0 | Intérprete |

## Lo que se dejó fuera a propósito

| Componente | Motivo |
|---|---|
| Piper (`piper1-gpl`) | GPL-3.0; algunas voces no permiten uso comercial |
| kokoro-onnx (paquete) | Es MIT, pero depende de phonemizer y espeak-ng (GPL-3.0). Se usa solo su archivo de modelo |
| espeak-ng, phonemizer | GPL-3.0. Se reemplazan con `app/g2p_es.py` |
