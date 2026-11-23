# Proposal: Los agentes conversan como personas de un equipo real

| Campo | Valor |
|---|---|
| Dueño | A.I.D.A (Aida) · diseño de agentes |
| Alcance | nucleo (y fichas de los satélites, cada uno con su propio cambio) |
| Tipo | marca-comunicacion |
| Tamaño | L (toca el núcleo y varios dominios: orquestación de Ultron, tono de Jarvis, fichas de Aida y el skill del Consejo) |
| Compuertas | Consejo completo (Vision, Jarvis, Edith, Viernes, Ultron) + aprobación del CEO |
| Aprobación | Pendiente. Pedido del CEO del 2026-11-20: "Quiero que mis agentes me respondan directamente o que hable con ellos como si fueran personas normales, y todo lo que hablemos sea lo más humano y parecido a un ambiente laboral real." |

## Why

Hoy el CEO habla con Ultron, y Ultron resume en tercera persona lo que dijo cada agente: "Edith opina que…". El CEO no oye a su equipo; oye un informe sobre su equipo. Las respuestas cumplen la guía de escritura, pero suenan a sistema, no a colegas.

El CEO quiere lo contrario: que cada agente le hable en primera persona, con su propia voz, como en una oficina real. Quiere también poder hablar con un agente sin intermediario.

**Valores y principios que lo justifican:**

- **Agilidad Real:** el CEO lee al agente directo, sin un resumen en medio. Hay menos pasos y menos texto entre la pregunta y la respuesta.
- **Principios humano-IA:** "humano al mando" (el CEO habla con cada agente y decide él) y "verdad antes que velocidad" (cada agente firma lo que dice y responde por ello; nadie lo reescribe).
- **Robustez Invisible:** el tono cambia; las reglas de seguridad no cambian.
- **Empatía Operativa, por analogía:** este valor habla de entender la operación del cliente. Aquí lo aplicamos al CEO como usuario interno: trabaja con un equipo, no con un tablero.

## What Changes

- **Respuesta directa:** Ultron pide a cada subagente un "mensaje para el CEO" en primera persona y lo pega sin reescribir, firmado ("Edith: Te cuento…"). El informe técnico entre agentes no cambia.
- **Hablar con un agente por su nombre:** si el CEO nombra a un agente, ese agente responde con su voz. Ultron solo coordina.
- **Sesión directa (opcional):** el CEO puede abrir Claude Code como un agente con `claude --agent <nombre>` para una conversación larga a solas. Vision lo prueba antes con una ficha. `--agent ultron` queda prohibido.
- **Tono de colegas:** saludo breve, "yo", opinión con su motivo, desacuerdo respetuoso, reconocer errores, pedir lo que falta y cerrar con el siguiente paso. Sin frases de bot. Humano no es largo.
- **"Cómo hablas":** cada ficha de agente añade una sección corta con su voz, sus expresiones y cómo da malas noticias.
- **Modo reunión del Consejo:** en la conversación, cada agente habla en primera persona y Ultron modera y cierra con las decisiones pendientes. `consejo.md` conserva la tabla resumen.
- **Límites:** los agentes dicen que son IA si alguien pregunta, no inventan vida privada y no cambian ninguna regla de `gobierno-agentes`. Ante clientes, la identidad sigue siendo El Guía Yizi: un borrador para un cliente va separado del mensaje al CEO, sin firma ni nombre interno, y marcado "requiere aprobación".
- **Spec nueva:** `conversacion-agentes`.

## Capabilities

### New Capabilities
- `conversacion-agentes`: cómo hablan los agentes con el CEO y entre ellos: voz en primera persona, tono de colegas, reuniones y límites de identidad.

### Modified Capabilities
- Ninguna. `comunicacion` (Jarvis) sigue siendo la dueña del tono hacia clientes y de la guía de escritura. La nueva spec la cita y no la contradice.

## Impact

- Archivos: `CLAUDE.md` y `AGENTS.md` del núcleo, las 8 fichas del núcleo, la plantilla del líder de satélite, el skill `yizi-consejo` y `marca/guia-de-escritura.md` (nota de tono).
- Satélites: Karen (Yizi Solutions) y Herbie (Yizi Projects) aplican "Cómo hablas" a sus fichas con un cambio propio en su repositorio.
- Costo: sin gasto nuevo. Tokens extra: un saludo y una firma por mensaje. Estimación no medida. Cada tarea indica su modelo (Sonnet o Haiku; ninguna con Fable). Las sesiones `--agent` se anotan aparte en `finanzas/consumo-ia.md`.
- Organigrama: no cambia. No se crea, activa ni retira ningún agente.

## Out of Scope

- Cambiar la voz de El Guía Yizi ante clientes. Eso es de Jarvis, en `comunicacion`.
- Crear agentes nuevos o cambiar nombres.
- Dar a los agentes memoria entre sesiones o "vida" propia.
- Fijar `agent` por defecto en `.claude/settings.json`. La conversación principal sigue siendo Ultron.
