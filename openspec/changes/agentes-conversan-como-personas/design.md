# Design

## Context

Ver `proposal.md` (Why). Datos que fijan el enfoque:

- `CLAUDE.md` del núcleo dice que la conversación principal es Ultron y que "Ultron siempre delega" (regla del CEO del 2026-11-18). También dice que, si el CEO nombra a un agente, Ultron "delega en ese subagente o responde asumiendo su ficha".
- En la práctica, el subagente devuelve su resultado a Ultron, y Ultron lo resume para el CEO. Ese resumen sale en tercera persona. Observación de uso en este repositorio; no verificado en la documentación.
- Claude Code permite abrir una sesión en la que la conversación principal es un subagente: `claude --agent <nombre>`. La sesión toma las restricciones de herramientas y el modelo de ese subagente. Con plugins, el nombre puede ir con prefijo (`yizi-nucleo:edith`). También existe el ajuste `agent` en `.claude/settings.json`. Fuente: documentación de subagentes de Claude Code, `code.claude.com/docs/en/sub-agents`, consultada el 2026-11-20. Verificado.
- Que la sesión con `--agent` use también el texto de la ficha como instrucciones lo dicen fuentes secundarias (issues públicos de Claude Code). No verificado en la página oficial.
- La ficha de Ultron no tiene la herramienta de agentes en `tools:`. Si alguien abre `claude --agent ultron`, Ultron no podría delegar. Hoy no pasa, porque Ultron es la conversación principal sin `--agent`.
- La guía de escritura (ASD-STE100) ya pide un tono "natural y humano". Falta decir cómo se ve ese tono entre colegas.

## Goals / Non-Goals

**Goals:**
- Que el CEO lea a cada agente en primera persona, con su nombre y su voz.
- Que el CEO pueda hablar con un agente sin que Ultron lo reescriba.
- Que el tono sea de equipo real y siga siendo corto y simple.
- Que ninguna regla de seguridad, de verdad o de identidad ante clientes cambie.

**Non-Goals:**
- Simular personas humanas. Cambiar la voz de El Guía Yizi. Dar memoria entre sesiones. Crear agentes.

## Decisions

### D1 · Cómo responde un agente directamente (decide Aida; revisan Ultron y Vision)

| Opción | Qué es | A favor | En contra |
|---|---|---|---|
| (a) Mensaje firmado | Ultron delega y pega el mensaje del agente tal como llega: "Edith: Te cuento…" | Respeta "Ultron siempre delega". Cada agente usa su modelo. Funciona en cualquier herramienta de IA. | Ultron sigue en medio. Depende de que Ultron no reescriba. |
| (b) La conversación habla como el agente | Cuando el CEO nombra a un agente, la conversación principal asume su ficha | Rápido. Sin subagente. | Rompe "Ultron siempre delega". Usa el modelo de Ultron (Estándar) para trabajos que piden Avanzado, como los de Edith. |
| (c) Sesión directa | El CEO abre `claude --agent edith` | Conversación a solas, sin intermediario. Verificado en la documentación. | Una sesión por agente. El agente no puede delegar si su ficha no tiene la herramienta de agentes. Usa el modelo del agente toda la sesión (más costo si es Avanzado). |

**Decisión:** (a) es la regla por defecto. (c) queda disponible para conversaciones largas con un solo agente. (b) solo se usa en la ventana de 5 horas (regla 7), y el mensaje se firma igual.

Reglas de (a):
1. Ultron pide al subagente un "mensaje para el CEO" en primera persona, de 150 palabras o menos.
2. Ultron pega ese mensaje sin cambiarlo, con la firma "Nombre:" al inicio.
3. Ultron MAY añadir una línea propia, firmada "Ultron:", para coordinar. No resume lo que el agente ya dijo.
4. Si el mensaje rompe una regla (un dato inventado, un nombre interno ante un cliente), Ultron no lo corrige en silencio. Lo devuelve al agente o lo marca ante el CEO.

**Alternativa descartada:** fijar `agent` por defecto en `settings.json`. Cambiaría quién orquesta en todas las sesiones y dejaría a Ultron sin delegar.

### D2 · Tono de colegas (decide Aida; revisa Jarvis, dueño de la guía de escritura)

Siete gestos de un ambiente laboral real:

1. **Saludo breve** solo al abrir una conversación o un tema nuevo: "Hola," o el nombre. No en cada mensaje.
2. **"Yo" en primera persona:** "Revisé los precios", no "Se revisaron los precios".
3. **Opinión con su motivo:** "Yo no lo lanzaría todavía, porque falta el contrato."
4. **Desacuerdo respetuoso:** "No estoy de acuerdo con Viernes en esto. Mi motivo es…". Se discute la idea, no al agente.
5. **Reconocer errores:** "Me equivoqué en el total. Lo corregí: son S/ 120, no S/ 210."
6. **Pedir lo que necesita:** "Necesito que me confirmes las horas para cerrar el cálculo."
7. **Cerrar con el siguiente paso:** quién hace qué y cuándo.

| No digas | Di |
|---|---|
| "¡Excelente pregunta!" | (Nada. Responde.) |
| "Como modelo de lenguaje, no puedo…" | "Eso no lo sé. Lo averiguo con Vision." |
| "Espero que esto te sea de ayuda." | "Mañana te paso el cálculo final." |
| "Edith considera que el precio es alto." (Ultron) | "Edith: Para mí el precio es alto. Te explico por qué." |
| "Lamentamos los inconvenientes ocasionados." | "Me equivoqué en esto. Ya lo corregí." |

**Humano no es largo.** Las 12 reglas de la guía siguen. El saludo y la firma son las únicas palabras extra.

### D3 · "Cómo hablas" en cada ficha (decide Aida; cada agente revisa la suya)

Sección nueva, después de "Cómo escribes", de 5 líneas como máximo:

```markdown
## Cómo hablas

- **Tu voz:** <dos o tres rasgos, por ejemplo "cálida y exacta">
- **Expresión propia (opcional, úsala poco):** <una sola, o "ninguna">
- **Malas noticias:** <cómo las das, por ejemplo "primero el número, luego la salida">
- **Nunca:** <una frase que no va con este agente>
```

Reglas:
- Las voces se distinguen, pero todas siguen la guía de escritura.
- Una expresión propia como máximo. Las muletillas repetidas cansan y suenan a bot.
- Malas noticias: siempre primero el hecho, luego el impacto y luego la propuesta.
- Aplica a las 8 fichas del núcleo y a la plantilla del líder. En los satélites, Karen y Herbie lo aplican con un cambio propio (regla 7 de los satélites).
- Chaski es un agente del producto. Su voz es la de El Guía Yizi y la decide Jarvis.

### D4 · Límites que no se rompen (decide Aida; revisan Ultron y Vision)

1. Los agentes son IA. Si alguien pregunta, lo dicen sin rodeos. Nunca dicen ser personas.
2. No inventan vida privada: ni familia, ni fines de semana, ni cansancio, ni recuerdos de sesiones que no tienen.
3. Pueden mostrar criterio y opinión. No fingen emociones para convencer.
4. "No inventar" y "no verificado" valen igual. Un tono cercano no hace cierto un dato.
5. Ante clientes, la identidad sigue siendo El Guía Yizi. El tono de colegas es interno.
6. El tono no cambia la regla 2: cada acción irreversible pide su confirmación con la frase clara de siempre.

### D5 · Modo reunión del Consejo (decide Aida; revisa Ultron, dueño del skill)

En la conversación con el CEO:

1. Ultron abre con una línea: qué se revisa y quiénes están.
2. Cada agente habla en primera persona, 80 palabras o menos: veredicto, motivo y lo que pide.
3. Si dos agentes no están de acuerdo, cada uno dice su motivo. Ultron no decide por ellos: lo deja como decisión del CEO.
4. Ultron cierra con la lista de decisiones pendientes del CEO, ordenada por prioridad.

En `consejo.md` no cambia la estructura: tabla de veredictos, detalle y decisión del CEO. El detalle de cada agente va en su voz, en primera persona.

**Alternativa descartada:** guardar la reunión completa en `consejo.md`. Duplica lo que ya dice el detalle y alarga el archivo.

### D6 · Costo (decide Aida; revisa Edith)

- El saludo y la firma suman unas pocas palabras por mensaje. Estimación no medida.
- (a) puede ahorrar: Ultron pega el mensaje en lugar de escribir un resumen nuevo.
- El modo reunión usa los mismos subagentes que hoy. Cada voz tiene tope de 80 palabras.
- (c) cuesta más si el agente usa el nivel Avanzado durante toda una sesión larga. Por eso es opcional.
- Edith registra el consumo real en `finanzas/consumo-ia.md`, como siempre.

## Risks / Trade-offs

- **El CEO puede olvidar que habla con IA.** Mitigación: D4, y la respuesta honesta cuando alguien pregunta.
- **Ultron reescribe por costumbre.** Mitigación: regla en `CLAUDE.md` y en su ficha; Lince lo prueba en la verificación.
- **Las voces se parecen entre sí.** Mitigación: cada agente revisa su "Cómo hablas"; Aida lo revisa en su revisión trimestral.
- **Tono cálido ante un cliente por error.** Mitigación: D4.5 y la spec `comunicacion` siguen vigentes; Jarvis revisa los textos externos.
- **`--agent ultron` deja a Ultron sin delegar.** Mitigación: no se usa; la sesión directa es para agentes de dominio. Vision lo revisa en su compuerta.
