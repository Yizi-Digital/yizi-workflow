# Contrato de la API · Yizi Voz Local 1.0

| Campo | Valor |
|---|---|
| Versión del contrato | 1.0 (2026-11-20) |
| Dueño | Vision (CTO) |
| Regla de cambio | Nada de este contrato cambia sin avisar antes a quien construye Sala Yizi. Los campos nuevos se añaden; los existentes no se quitan ni cambian de tipo. |
| Base | `http://127.0.0.1:8765` (puerto en `config/config.yaml` o variable `YIZI_VOZ_PUERTO`) |

## 1. Reglas generales

1. El servidor escucha **solo** en `127.0.0.1` (o `::1`). Si la configuración pide otra dirección, no arranca.
2. **Token opcional.** Si el servidor arranca con la variable `YIZI_VOZ_TOKEN`, todas las rutas `/v1/...` piden la cabecera `Authorization: Bearer <token>`. También se acepta `X-API-Key: <token>`. `GET /health` nunca pide token.
3. El audio que llega o sale vive solo en memoria. No se escribe en disco. Única excepción: el respaldo `say` de macOS escribe un WAV en una carpeta temporal privada (permisos 700) y la borra al terminar cada frase.
4. Todo error HTTP devuelve JSON con esta forma (estilo OpenAI):

```json
{"error": {"code": "voice_not_found", "message": "Voz desconocida: 'x'. Consulta GET /v1/voices."}}
```

### Códigos de error HTTP

| HTTP | `code` | Cuándo |
|---|---|---|
| 400 | `invalid_request` | Falta un campo, el tipo no es válido, `speed` fuera de 0.5 a 2.0, `input` vacío |
| 400 | `voice_not_found` | `voice` no es un agente de `config/voces.yaml` ni una voz de Kokoro |
| 400 | `unsupported_format` | `response_format` distinto de `wav` o `pcm` |
| 401 | `unauthorized` | Hay token configurado y la petición no lo trae o no coincide |
| 413 | `input_too_long` | `input` pasa de 4096 caracteres (`servidor.max_texto`) |
| 413 | `file_too_large` | El audio pasa de 25 MB (`servidor.max_audio_mb`) |
| 415 | `unsupported_audio` | No se pudo decodificar el audio subido |
| 503 | `stt_unavailable` | El modelo de voz a texto no está cargado (ver `/health`) |
| 503 | `tts_unavailable` | No hay motor de texto a voz (falta Kokoro y no hay `say`) |

## 2. `GET /health`

Sin token. Sirve para saber si el servidor está listo antes de abrir una reunión.

```json
{
  "status": "ok",
  "version": "1.0.0",
  "stt": {"ready": true, "backend": "faster-whisper", "model": "faster-whisper-small", "error": ""},
  "tts": {"ready": true, "engine": "kokoro", "error": ""},
  "auth": false
}
```

- `status`: `ok` si las dos partes están listas; `degraded` si falta una.
- `stt.backend`: `faster-whisper` o `mlx-whisper`.
- `tts.engine`: `kokoro`, `say` o `ninguno`.
- `auth`: `true` si el servidor pide token.

## 3. `GET /v1/voices`

```json
{
  "engine": "kokoro",
  "default": "vision",
  "voices": [
    {"id": "edith", "kokoro_voice": "ef_dora", "speed": 1.0, "say_voice": "Paulina", "description": "CFO"}
  ],
  "kokoro_voices": ["af_alloy", "ef_dora", "em_alex", "em_santa", "..."],
  "say_voices": ["Paulina", "Jorge"]
}
```

- `voices[].id` es el valor que se manda en `voice`. Ids de la v1.0: `ultron`, `vision`, `jarvis`, `edith`, `viernes`, `aida`, `termy`, `lince`, `karen`, `herbie`, `homer`, `abaco`, `guia`.
- `say_voices` solo trae datos en macOS.

## 4. `POST /v1/audio/speech` (texto a voz, en streaming por frases)

Petición: `Content-Type: application/json`.

| Campo | Tipo | Obligatorio | Valor por defecto | Nota |
|---|---|---|---|---|
| `input` | string | Sí | — | 1 a 4096 caracteres |
| `voice` | string | No | `por_defecto` de `voces.yaml` (`vision`) | Id de agente. También acepta una voz de Kokoro directa (`ef_dora`) |
| `speed` | número | No | 1.0 | 0.5 a 2.0. Se multiplica por la velocidad del agente; el resultado se limita a 0.5–2.0 |
| `response_format` | string | No | `wav` | `wav` o `pcm` |
| `model` | string | No | — | Se acepta y se ignora (compatibilidad con OpenAI) |

Respuesta `200`, con transferencia por trozos (`Transfer-Encoding: chunked`):

| `response_format` | `Content-Type` | Cuerpo |
|---|---|---|
| `wav` | `audio/wav` | Cabecera WAV de 44 bytes y luego PCM. Los campos de tamaño de la cabecera valen `0xFFFFFFFF` (longitud desconocida, porque es streaming) |
| `pcm` | `audio/L16; rate=24000; channels=1` | Solo PCM, sin cabecera |

- Audio: **24 000 Hz, mono, 16 bits con signo, little-endian**.
- El servidor parte `input` en frases (por `. ! ? … ; :` y saltos de línea; las frases de más de 220 caracteres se cortan en una coma o un espacio). Envía cada frase en cuanto la genera, seguida de 120 ms de silencio (salvo la última).
- Cabeceras extra: `X-Sample-Rate: 24000`, `X-Voice: <id>`, `X-Voice-Engine: kokoro|say`, `X-Sentences: <número de frases>`.
- **Para cortar una respuesta** (el CEO interrumpe), el cliente cierra la conexión. El servidor deja de generar tras la frase en curso.
- Consejo para la app: pide `pcm`, lee el cuerpo por trozos y pásalo a un `AVAudioPCMBuffer` de 24 kHz. Con `wav`, salta los primeros 44 bytes.

## 5. `POST /v1/audio/transcriptions` (voz a texto de un archivo)

Petición: `multipart/form-data`.

| Campo | Tipo | Obligatorio | Valor por defecto | Nota |
|---|---|---|---|---|
| `file` | archivo | Sí | — | WAV, M4A/AAC, MP3, OGG/Opus, FLAC, WebM (lo que decodifique FFmpeg). Máximo 25 MB |
| `language` | string | No | `es` | Código ISO 639-1 |
| `prompt` | string | No | — | Texto de contexto (nombres propios, jerga) |
| `response_format` | string | No | `json` | `json` o `text` |
| `model` | string | No | — | Se acepta y se ignora |

Respuesta `200` con `json`:

```json
{"text": "Buenos días, el pedido llegó a tiempo.", "language": "es", "duration": 2.84, "processing_ms": 610}
```

- `text` es el único campo garantizado por compatibilidad con OpenAI. `duration` está en segundos de audio; `processing_ms` es el tiempo del modelo.
- Con `response_format=text`, el cuerpo es solo el texto (`text/plain; charset=utf-8`).

## 6. WebSocket `ws://127.0.0.1:8765/v1/stream/transcribe` (dictado en vivo)

### 6.1 Conexión
- Parámetro opcional en la URL: `?language=es`.
- Si hay token: cabecera `Authorization: Bearer <token>` en el *handshake*. Sin token válido, el servidor cierra con el código **4401**.
- Si el modelo de voz a texto no está listo, el servidor envía un mensaje `error` con `stt_unavailable` y cierra con **1011**.

### 6.2 Lo que envía el cliente
1. **Audio:** mensajes **binarios** con PCM **16 000 Hz, mono, 16 bits con signo, little-endian**. Cualquier tamaño de trozo; se recomiendan 20 a 100 ms (640 a 3200 bytes). Tamaño máximo de un mensaje: 1 MB.
2. **Control:** mensajes de **texto** con JSON:

| Mensaje | Efecto |
|---|---|
| `{"type": "config", "language": "es"}` | Cambia el idioma de los segmentos siguientes |
| `{"type": "flush"}` | Cierra ya el segmento en curso y pide su texto final (por ejemplo, el CEO pulsa "enviar") |
| `{"type": "close"}` | Cierra el segmento en curso, espera sus textos pendientes, envía `closed` y cierra con 1000 |

### 6.3 Lo que envía el servidor (siempre texto JSON)

| `type` | Campos | Cuándo |
|---|---|---|
| `ready` | `sample_rate` (16000), `encoding` (`pcm_s16le`), `channels` (1), `language`, `backend` | Al abrir la conexión |
| `speech_start` | `segment_id`, `start` | El detector de voz (Silero VAD) oye voz. Úsalo para la **interrupción** (barge-in) |
| `partial` | `segment_id`, `text`, `start`, `end`, `processing_ms` | Cada ~800 ms mientras se habla. El texto puede cambiar en el siguiente parcial |
| `speech_end` | `segment_id`, `end` | Tras 600 ms de silencio (fin de turno) o 25 s de voz seguida |
| `final` | `segment_id`, `text`, `start`, `end`, `processing_ms` | Texto definitivo del segmento. Llega después de `speech_end` |
| `error` | `code`, `message` | `invalid_message`, `transcription_failed`, `stt_unavailable` |
| `closed` | — | Respuesta a `close`, justo antes de cerrar |

- `segment_id` es un entero que empieza en 1 y sube con cada segmento.
- `start` y `end` son segundos desde que se abrió la conexión, medidos sobre el audio recibido.
- Un parcial se descarta si el modelo está ocupado. Un final nunca se descarta.
- Ejemplo de secuencia: `ready` → `speech_start(1)` → `partial(1)` → `partial(1)` → `speech_end(1)` → `final(1)` → `closed`.

### 6.4 Códigos de cierre

| Código | Motivo |
|---|---|
| 1000 | Cierre normal tras `close` |
| 1011 | El modelo de voz a texto no está listo |
| 4401 | Falta el token o no es válido |

## 7. Ajustes que cambian el comportamiento (sin cambiar el contrato)

`config/config.yaml`, sección `vad`: `umbral` (0.5), `silencio_fin_ms` (600), `parcial_cada_ms` (800), `max_segmento_s` (25), `preroll_ms` (300).
