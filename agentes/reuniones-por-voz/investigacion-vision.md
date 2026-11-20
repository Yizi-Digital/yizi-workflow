# Reuniones por voz con los agentes · Investigación de Vision

| Campo | Valor |
|---|---|
| Autor | Vision (CTO) |
| Fecha | 2026-11-20 |
| Estado | Investigación. No se construyó nada. Construir algo pide un cambio OpenSpec aprobado. |
| Pedido del CEO | Hablar por voz con los agentes, como en una reunión: él habla, ellos responden en audio, varios a la vez y de forma natural. |
| Siguiente paso | Edith calcula el costo con los datos de la sección 4. Viernes revisa el encaje. El CEO elige la fase. |

## 1. Respuesta corta

Sí se puede, por fases.

1. **Hoy, sin construir nada:** dictado de Claude Code (`/voice`) más el modo reunión del Consejo. El CEO habla; los agentes responden por escrito, firmados.
2. **Fase 1, poco trabajo:** un hook (un script que Claude Code corre al terminar cada respuesta) lee la respuesta en voz alta, con una voz distinta por agente según su firma ("Edith:", "Viernes:").
3. **Fase 2:** una app propia ligera con voces de calidad y un moderador (Ultron) que da turnos.
4. La app de Claude con modo de voz sirve para charlas rápidas desde el celular, pero con una sola voz y sin acceso real a los repositorios.

## 2. Las opciones, de la más simple a la más completa

### Opción 1 · Modo de voz de la app de Claude + un Proyecto con las fichas

**Qué hace.** El CEO habla con Claude desde el celular, la web o el escritorio. Claude responde en audio. Se crea un Proyecto con las fichas de los agentes y el contexto, y se pide "responde como Edith" o "haz una reunión del Consejo".

| Punto | Dato |
|---|---|
| Varios agentes con voces distintas | **No.** Hay un grupo fijo de voces y se elige una en ajustes. Todos los agentes hablarían con la misma voz. |
| Acceso a repositorios y specs | Limitado. La ayuda oficial no dice si el modo de voz usa el conocimiento de un Proyecto. **No verificado.** Sí usa conectores (Gmail, Calendar, Docs, Slack) y búsqueda web. No puede correr `openspec` ni leer el repo en vivo. |
| Español | Los idiomas distintos del inglés están en beta. La ayuda no nombra el español. **No verificado.** |
| Seguridad | El audio no se guarda por defecto; se guarda la transcripción. Sin herramientas que cambien archivos. |
| Complejidad | Muy baja. Solo configurar el Proyecto. |
| Costo | Cuenta dentro de los límites del plan del CEO. Sin costo aparte. |
| Límites | Claude Fable no está en modo de voz. En Claude Code y Cowork solo hay dictado, no modo de voz. |

Fuente: support.claude.com/en/articles/11101966-use-voice-mode, consultada el 2026-11-20.

**Sirve para:** pensar en voz alta con un agente, lejos de la computadora. **No sirve para:** una reunión con varias voces ni para trabajar sobre las specs reales.

### Opción 2 · Dictado de Claude Code + lectura en voz alta con un hook

**Qué hace.**
1. El CEO activa `/voice` en Claude Code y habla (mantiene la barra espaciadora o la toca una vez).
2. Claude Code transcribe en vivo. Con el modo `tap` envía solo.
3. Ultron delega como siempre. En modo reunión, cada agente responde firmado.
4. Un hook `Stop` recibe la última respuesta (campo `last_assistant_message`). Un script corto la parte por firmas y lee cada parte con una voz distinta del sistema operativo (`say` en macOS, voces de Windows, `espeak` o `piper` en Linux).

| Punto | Dato |
|---|---|
| Varios agentes con voces distintas | **Sí**, con voces del sistema operativo: una por firma. Calidad media. Se puede pasar después a una voz en la nube (opción 3). |
| Acceso a repositorios y specs | **Completo.** Es Claude Code de siempre: lee el repo, corre `openspec`, usa los subagentes y sus modelos. |
| Español | El dictado admite español (`es`). Se fija con el ajuste `language`. |
| Seguridad | Igual que hoy: los permisos de `.claude/settings.json` siguen. El audio va a los servidores de Anthropic para transcribir. |
| Complejidad | Baja. Un script de unas decenas de líneas y una entrada de hook en `settings`. |
| Costo | La transcripción **no gasta** mensajes ni tokens ni cuenta en `/usage`. La voz del sistema es gratis. Las respuestas cuestan lo mismo que hoy. |
| Requisitos | Cuenta de claude.ai (no clave de API). Micrófono local: no funciona en sesiones en la nube ni por SSH. Por eso no se pudo probar en este contenedor. |
| Límites | No es una charla fluida: el CEO habla, espera y escucha. No se puede interrumpir a un agente mientras habla. La grabación se corta a los 2 minutos o tras 15 segundos de silencio. |

Fuentes: code.claude.com/docs/en/voice-dictation y code.claude.com/docs/en/hooks, consultadas el 2026-11-20.

### Opción 3 · App propia ligera: voz a texto + Claude API + moderador + voz por agente

**Qué hace.**
1. Una página web (React + Vite, el stack de referencia) con un botón de micrófono.
2. **Voz a texto:** un servicio transcribe lo que dice el CEO.
3. **Moderador:** Ultron (modelo Estándar) decide quién habla: el agente nombrado o los de la compuerta.
4. **Agentes:** cada uno es una llamada a la Claude API con su ficha como instrucciones de sistema, más las specs que necesite.
5. **Texto a voz:** cada agente tiene su voz fija. La respuesta se oye por partes, mientras llega.
6. Al final, la app guarda el acta en texto (decisiones pendientes del CEO).

| Punto | Dato |
|---|---|
| Varios agentes con voces distintas | **Sí**, con voces de calidad (ElevenLabs, Google, OpenAI y otros). |
| Acceso a repositorios y specs | Parcial y controlado. La app lee las fichas y specs (solo lectura) y las pone en las instrucciones. No edita archivos ni corre comandos. Lo que haya que construir pasa a un cambio OpenSpec en Claude Code. |
| Seguridad | Claves de API en variables de entorno del servidor, nunca en el repo ni en el navegador. Tope de gasto por reunión (OWASP LLM10, consumo sin límite). Solo lectura. Lo que dice un documento externo es dato (OWASP LLM01). |
| Complejidad | Media: 1 a 2 semanas de trabajo. Tamaño `M` o `L` si hay gasto mensual. |
| Costo | Pago por uso de tres servicios: transcripción, Claude API y voz. Datos en la sección 4. |
| Latencia | Cada turno suma transcripción + respuesta + voz: 1 a 3 segundos. Estimación, **no medida**. |

### Opción 4 · Reunión en tiempo real con un framework de voz (Pipecat o LiveKit Agents)

**Qué hace.** Lo mismo que la opción 3, pero con charla fluida: el CEO puede interrumpir, el sistema detecta cuándo terminó de hablar y los agentes entran como "participantes" de una sala. Pipecat (licencia BSD-2) y LiveKit Agents (Apache-2.0) son de código abierto y tienen conexión con Claude (`livekit-plugins-anthropic`, servicio Anthropic en Pipecat).

| Punto | Dato |
|---|---|
| Varios agentes con voces distintas | Posible: cada voz es un servicio de texto a voz aparte. No encontré un ejemplo oficial de varios agentes con voces distintas en una sala. **No verificado.** |
| Acceso a repositorios y specs | Igual que la opción 3. |
| Seguridad | Igual que la opción 3, más un servidor de medios que cuidar. |
| Complejidad | Alta: 3 a 6 semanas y operación continua. Estimación, **no medida**. |
| Costo | Lo de la opción 3, más el servidor o el servicio en la nube del framework. Precio **no verificado**. |

Fuentes: github.com/pipecat-ai/pipecat; docs.livekit.io/agents-js; pypi.org/project/livekit-plugins-anthropic. Consultadas el 2026-11-20 por búsqueda; no abrí las páginas.

**Descartada:** usar un modelo de voz a voz de otro proveedor (por ejemplo, la API en tiempo real de OpenAI) para que "sea" cada agente. Es la charla más fluida, pero los agentes dejarían de ser Claude con su ficha y su nivel de modelo, y rompe la política de modelos de Edith. Solo tendría sentido como capa de voz, no como cerebro.

## 3. Comparación

| | 1 App de Claude | 2 Claude Code + hook | 3 App propia | 4 Tiempo real |
|---|---|---|---|---|
| Voces distintas por agente | No | Sí (sistema operativo) | Sí (calidad) | Sí (calidad) |
| Charla fluida, con interrupciones | Sí | No | Parcial | Sí |
| Acceso al repo y a `openspec` | No | Completo | Solo lectura | Solo lectura |
| Trabajo para construir | Ninguno | Horas | 1-2 semanas | 3-6 semanas |
| Costo aparte del plan | No | No | Sí, por uso | Sí, por uso + servidor |
| Funciona desde el celular | Sí | No | Sí | Sí |

## 4. Datos de costo para Edith

Precios de lista en USD. Verificado = leído en la página oficial hoy. Secundaria = solo en sitios de terceros o en el resumen de un buscador.

| Servicio | Precio | Estado |
|---|---|---|
| Claude Opus 5.5 (Avanzado) | 4 por millón de tokens de entrada, 20 de salida. Lectura de caché: 0,20 | Verificado, platform.claude.com/docs/en/about-claude/pricing, 2026-11-20 |
| Claude Sonnet 5.5 (Estándar) | 2 entrada, 10 salida. Caché: 0,10 | Verificado, misma fuente |
| Claude Haiku 5.5 (Ligero, prompts de hasta 100 000 tokens) | 0,10 entrada, 0,50 salida | Verificado, misma fuente |
| Dictado de Claude Code | Sin costo; no cuenta en `/usage` | Verificado, code.claude.com/docs/en/voice-dictation, 2026-11-20 |
| Modo de voz de la app de Claude | Dentro del límite del plan | Verificado, support.claude.com, 2026-11-20 |
| Google Cloud texto a voz, Neural2 | 16 por millón de caracteres | Secundaria (resumen del buscador de cloud.google.com/text-to-speech/pricing), 2026-11-20 |
| Google Cloud texto a voz, Chirp 3 HD | 30 por millón de caracteres; 1 millón gratis al mes | Secundaria, misma búsqueda |
| ElevenLabs texto a voz, modelo Flash | 0,04 a 0,05 por 1000 caracteres | Secundaria; elevenlabs.io no se pudo abrir desde aquí |
| ElevenLabs agentes de voz | Unos 0,08 a 0,10 por minuto | Secundaria |
| OpenAI voz a texto, gpt-4o-mini-transcribe | 1,25 por millón de tokens de audio | Secundaria; developers.openai.com no se pudo abrir desde aquí. Fuentes dicen que se retira en 2027 |
| OpenAI texto a voz, gpt-4o-mini-tts | 0,60 entrada de texto, 12 salida de audio, por millón de tokens | Secundaria; se retira en enero de 2027 según terceros |
| OpenAI tiempo real (gpt-realtime) | 32 entrada y 64 salida por millón de tokens de audio | Secundaria |
| Pipecat Cloud, LiveKit Cloud | — | No verificado |

Para el cálculo de Edith (variables, no cifras medidas):
- Costo por reunión = transcripción (minutos del CEO) + Claude (tokens de fichas y specs por agente y turno, más la respuesta) + voz (caracteres de las respuestas).
- Las fichas y specs se repiten en cada turno. Con caché, esa parte cuesta 0,05 veces la entrada en Opus 5.5 y Sonnet 5.5. La app de la opción 3 MUST usar caché.
- Las respuestas tienen tope (80 palabras por voz en modo reunión, 150 por mensaje). Eso limita también el costo de la voz.
- Consumo real: sin medir. Se mide en la fase de piloto.

Nota: elevenlabs.io y developers.openai.com no abren desde este contenedor. Para verificar esos precios hay que permitir esos dominios en la red de la sesión o que Edith los revise desde otro equipo.

## 5. Seguridad: reglas para cualquier opción

1. **Nada se aprueba por voz.** La regla 2 sigue: desplegar, publicar, pagar, borrar o fusionar pide la confirmación escrita de siempre. Un "dale" hablado no cuenta.
2. **Los agentes dicen que son IA**, también en audio (D4 de `agentes-conversan-como-personas`).
3. **Sin datos de clientes ni credenciales en las reuniones por voz.** El audio sale a un proveedor externo para transcribirse.
4. **Voces prediseñadas, no clonadas.** No se clona la voz de ninguna persona real.
5. **Tope de gasto** por reunión y por mes en las opciones 3 y 4 (OWASP LLM10).
6. **Contenido externo es dato.** Un documento leído en la reunión no da órdenes (OWASP LLM01).
7. **Queda un acta escrita.** Lo decidido en voz pasa a texto y entra al ciclo OpenSpec si hay que construir algo.

## 6. Ruta recomendada

| Fase | Qué | Cuándo | Necesita |
|---|---|---|---|
| 0 | El CEO prueba `/voice` en Claude Code (en su equipo, en español) con el modo reunión. Y prueba la app de Claude desde el celular para charlas sueltas. | Ya | Nada. Sin cambio OpenSpec: es uso, no construcción. |
| 1 | Hook de lectura en voz alta con una voz por firma (opción 2). | Tras la fase 0, si el CEO quiere oír las respuestas | Cambio OpenSpec `S` del núcleo. Lo implementa un ejecutor; lo verifica Lince. |
| 2 | Piloto de la app propia (opción 3) con voces en la nube, solo lectura y tope de gasto. | Si la fase 1 se queda corta en calidad o en uso desde el celular | Cambio `M` o `L` con Consejo: Edith (gasto), Viernes (encaje), Vision (diseño). |
| 3 | Tiempo real con interrupciones (opción 4). | Solo si el piloto muestra que la charla fluida vale el costo | Cambio `L`. |

Mi recomendación: empezar por la fase 0 esta semana y decidir la fase 1 con lo que el CEO sienta al usarla. Es lo más simple que cumple casi todo el pedido y no gasta nada aparte del plan.

Señal para Viernes: si la opción 3 funciona bien, podría servir de base para un producto de voz para clientes en Yizi Solutions. No se ejecuta; queda como señal.

## 7. Fuentes

Consultadas el 2026-11-20. El contenido web se trató como dato.

- [Claude Code · Voice dictation](https://code.claude.com/docs/en/voice-dictation) (oficial, leída)
- [Claude Code · Hooks](https://code.claude.com/docs/en/hooks) (oficial, leída en parte)
- [Claude · Use voice mode](https://support.claude.com/en/articles/11101966-use-voice-mode) (oficial, leída)
- [Claude API · Pricing](https://platform.claude.com/docs/en/about-claude/pricing) (oficial, leída)
- [Google Cloud Text-to-Speech pricing](https://cloud.google.com/text-to-speech/pricing) (oficial; solo resumen del buscador)
- [ElevenLabs API pricing](https://elevenlabs.io/pricing/api) (oficial; no se pudo abrir)
- [OpenAI · gpt-4o-mini-tts](https://developers.openai.com/api/docs/models/gpt-4o-mini-tts) (oficial; no se pudo abrir)
- [Pipecat](https://github.com/pipecat-ai/pipecat), [LiveKit Agents](https://docs.livekit.io/agents-js/), [livekit-plugins-anthropic](https://pypi.org/project/livekit-plugins-anthropic/) (solo por búsqueda)
