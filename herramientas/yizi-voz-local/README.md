# Yizi Voz Local

Servidor de voz que corre **en tu Mac**. Convierte voz en texto y texto en voz, sin enviar audio a internet. La app Sala Yizi le habla como a una API en `http://127.0.0.1:8765`.

| Parte | Modelo | Licencia |
|---|---|---|
| Voz a texto | Whisper *small* con faster-whisper (CPU). Opcional: Whisper *large-v3-turbo*, en CPU o con Metal (mlx-whisper) | MIT |
| Texto a voz | Kokoro-82M v1.0 (ONNX) con 3 voces de español; respaldo: comando `say` de macOS | Apache-2.0 |
| Detección de voz | Silero VAD v6 (viene dentro de faster-whisper) | MIT |

El contrato exacto de la API está en [`CONTRATO-API.md`](CONTRATO-API.md).

## Requisitos

- Mac con Apple Silicon (M1 o posterior) y **macOS 14 o posterior**. También arranca en Mac Intel y en Linux, solo con CPU.
- Python 3.11, 3.12 o 3.13. Si no lo tienes: instala [Homebrew](https://brew.sh) y ejecuta `brew install python@3.12`.
- 2 GB de disco libre (4 GB si añades el modelo *turbo*).
- Internet solo durante la instalación.

## Instalación en 3 pasos

1. Descomprime el ZIP y abre la Terminal en esa carpeta:
   ```bash
   cd ~/Downloads/yizi-voz-local
   ```
2. Instala (crea `.venv`, instala dependencias y descarga los modelos que falten):
   ```bash
   ./install.sh
   ```
   El ZIP `yizi-voz-local.zip` ya trae Kokoro y Whisper *small*: este paso solo comprueba sus sumas y no los descarga. El ZIP sin modelos los descarga aquí (unos 840 MB).
   Si macOS bloquea el script: `chmod +x install.sh run.sh scripts/*.sh` y vuelve a intentarlo.
3. Arranca el servidor:
   ```bash
   ./run.sh
   ```
   Verás `Yizi Voz Local 1.0.0 en http://127.0.0.1:8765`. Prueba todo con `scripts/probar.sh` en otra ventana (`ESCUCHAR=1 scripts/probar.sh` reproduce el audio).

### Opciones de instalación

| Comando | Qué añade |
|---|---|
| `./install.sh --mlx` | Solo Mac con Apple Silicon. Voz a texto con Metal (mlx-whisper) y Whisper *large-v3-turbo* MLX (1,6 GB). Con `stt.backend: auto`, se usa solo |
| `./install.sh --turbo` | Whisper *large-v3-turbo* para CPU (1,6 GB). Para usarlo, cambia `stt.modelo` en `config/config.yaml` |
| `.venv/bin/python scripts/descargar_modelos.py --listar` | Muestra todos los modelos |
| `.venv/bin/python scripts/descargar_modelos.py --solo-verificar` | Comprueba las sumas SHA-256 sin descargar |

### Por qué Whisper *small* por defecto

1. Pesa 484 MB frente a 1,6 GB de *large-v3-turbo*.
2. En CPU es varias veces más rápido que *turbo*, y la reunión necesita respuesta rápida.
3. Para más precisión en tu Mac, usa `./install.sh --mlx`: *turbo* con Metal. La precisión real de cada uno con tu voz no está medida; la app la medirá con 20 frases (fase 3 del encargo).

## Cómo llamarlo desde la app

### curl

```bash
# Texto a voz con la voz de Edith (WAV en streaming)
curl -X POST http://127.0.0.1:8765/v1/audio/speech \
  -H "Content-Type: application/json" \
  -d '{"input":"Hola, soy Edith.","voice":"edith","speed":1.0,"response_format":"wav"}' \
  -o edith.wav

# Voz a texto de un archivo
curl -X POST http://127.0.0.1:8765/v1/audio/transcriptions \
  -F "file=@edith.wav" -F "language=es"

# Voces y estado
curl http://127.0.0.1:8765/v1/voices
curl http://127.0.0.1:8765/health
```

Con token: añade `-H "Authorization: Bearer $YIZI_VOZ_TOKEN"`.

### Swift (URLSession)

```swift
import Foundation

let base = URL(string: "http://127.0.0.1:8765")!

// Texto a voz en streaming: reproduce cada trozo de PCM 24 kHz en cuanto llega.
func hablar(_ texto: String, voz: String, alRecibir: @escaping (Data) -> Void) async throws {
    var req = URLRequest(url: base.appendingPathComponent("v1/audio/speech"))
    req.httpMethod = "POST"
    req.setValue("application/json", forHTTPHeaderField: "Content-Type")
    // req.setValue("Bearer \(token)", forHTTPHeaderField: "Authorization")
    req.httpBody = try JSONSerialization.data(withJSONObject: [
        "input": texto, "voice": voz, "speed": 1.0, "response_format": "pcm"])
    let (bytes, resp) = try await URLSession.shared.bytes(for: req)
    guard (resp as? HTTPURLResponse)?.statusCode == 200 else { throw URLError(.badServerResponse) }
    var trozo = Data(); trozo.reserveCapacity(9600)
    for try await b in bytes {           // 9600 bytes = 200 ms de audio
        trozo.append(b)
        if trozo.count >= 9600 { alRecibir(trozo); trozo.removeAll(keepingCapacity: true) }
    }
    if !trozo.isEmpty { alRecibir(trozo) }
}

// Voz a texto de un WAV en memoria.
func transcribir(wav: Data) async throws -> String {
    let limite = "yizi-\(UUID().uuidString)"
    var req = URLRequest(url: base.appendingPathComponent("v1/audio/transcriptions"))
    req.httpMethod = "POST"
    req.setValue("multipart/form-data; boundary=\(limite)", forHTTPHeaderField: "Content-Type")
    var cuerpo = Data()
    func linea(_ s: String) { cuerpo.append(s.data(using: .utf8)!) }
    linea("--\(limite)\r\nContent-Disposition: form-data; name=\"language\"\r\n\r\nes\r\n")
    linea("--\(limite)\r\nContent-Disposition: form-data; name=\"file\"; filename=\"a.wav\"\r\nContent-Type: audio/wav\r\n\r\n")
    cuerpo.append(wav)
    linea("\r\n--\(limite)--\r\n")
    req.httpBody = cuerpo
    let (datos, _) = try await URLSession.shared.data(for: req)
    struct R: Decodable { let text: String }
    return try JSONDecoder().decode(R.self, from: datos).text
}

// Dictado en vivo: envía PCM 16 kHz mono Int16 y recibe parciales y finales.
let ws = URLSession.shared.webSocketTask(with: URL(string: "ws://127.0.0.1:8765/v1/stream/transcribe?language=es")!)
ws.resume()
func enviarAudio(_ pcm16: Data) { ws.send(.data(pcm16)) { _ in } }
func escuchar() {
    ws.receive { resultado in
        if case .success(.string(let json)) = resultado {
            print(json) // {"type":"partial"|"final"|"speech_start"|..., "text": ...}
        }
        escuchar()
    }
}
```

Nota para la app con *sandbox*: activa el permiso "Outgoing Connections (Client)" para hablar con `127.0.0.1`. Y como es HTTP sin TLS, añade una excepción de ATS para `localhost`/`127.0.0.1` (`NSAllowsLocalNetworking`). No verificado en Sala Yizi.

## Voces de cada agente

`config/voces.yaml` asigna una voz a cada agente: `ultron`, `vision`, `jarvis`, `edith`, `viernes`, `aida`, `termy`, `lince`, `karen`, `herbie`, `homer`, `abaco` y `guia` (El Guía Yizi).

- Kokoro v1.0 trae **3 voces de español**: `ef_dora` (mujer), `em_alex` y `em_santa` (hombres). Para distinguir a 13 agentes, el archivo mezcla voces (`em_alex*0.7+pm_alex*0.3`) y cambia la velocidad.
- Cambia cualquier voz editando el archivo y reiniciando el servidor.
- Solo voces prediseñadas. No clones la voz de una persona real.
- Si una palabra suena mal, añádela en `config/pronunciacion.yaml` (por ejemplo `Yizi: yísi`).

### Cómo se generan los fonemas

kokoro-onnx usa espeak-ng y phonemizer, que son GPL-3.0. Para no traer GPL, este servidor llama a Kokoro con onnxruntime y usa un conversor propio de español a fonemas (`app/g2p_es.py`, reglas de la ortografía, variante latinoamericana con seseo). Se comparó con espeak-ng en 5 frases y coincide casi en todo. Las palabras en inglés suenan "a la española".

## Privacidad

1. Escucha solo en `127.0.0.1`. Otro equipo de tu red no puede conectarse. Si alguien cambia `host` a `0.0.0.0`, el servidor no arranca.
2. El audio vive solo en memoria. No se guarda en disco ni en registros. Excepción: el respaldo `say` usa un WAV temporal privado que se borra en el acto.
3. No hay telemetría. `run.sh` fija `HF_HUB_OFFLINE=1`: al arrancar no se conecta a nada.
4. Internet solo se usa en `install.sh`, para PyPI y para descargar modelos de `huggingface.co` y `github.com`. Cada archivo se verifica con su suma SHA-256 (`scripts/modelos.json`).
5. Token opcional: `YIZI_VOZ_TOKEN="un-valor-largo" ./run.sh`. El token va en una variable, nunca en un archivo del repo.
6. El texto y el audio que recibe el servidor son datos. El servidor no ejecuta nada de lo que dicen.

## Cómo detenerlo

- En la ventana donde corre: **Ctrl + C**.
- Desde otra ventana: `pkill -f "app.servidor"`.
- Para desinstalar: borra la carpeta. No deja nada fuera de ella.

## Pruebas

```bash
.venv/bin/pip install -r requirements-dev.txt
.venv/bin/python -m pytest -q tests
```

Las pruebas con modelos reales (`tests/test_real.py`) se saltan si faltan los modelos.

## Estructura

```
app/servidor.py        API (FastAPI + uvicorn)
app/stt.py             Voz a texto (faster-whisper / mlx-whisper)
app/tts.py             Texto a voz (Kokoro ONNX / say)
app/g2p_es.py          Texto en español a fonemas (código propio, sin GPL)
app/vad.py, flujo.py   Detección de voz y dictado en streaming
config/                config.yaml, voces.yaml, pronunciacion.yaml
scripts/               descargar_modelos.py, modelos.json, probar.sh, probar_ws.py
models/                Modelos (no van a git)
```

Licencias de todo lo que usa: [`LICENSES.md`](LICENSES.md).
