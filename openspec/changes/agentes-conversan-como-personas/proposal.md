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

**Valores que lo justifican:** Empatía Operativa (el CEO trabaja con personas de su equipo, no con un tablero) y Robustez Invisible (el tono cambia; las reglas de seguridad no cambian).

## What Changes

- **Respuesta directa:** Ultron entrega el mensaje de cada agente tal como lo escribió, en primera persona y firmado ("Edith: Te cuento…"). Ultron no lo reescribe en tercera persona.
- **Hablar con un agente por su nombre:** si el CEO nombra a un agente, ese agente responde con su voz. Ultron solo coordina.
- **Sesión directa (opcional):** el CEO puede abrir Claude Code como un agente con `claude --agent <nombre>` para una conversación larga a solas.
- **Tono de colegas:** saludo breve, "yo", opinión con su motivo, desacuerdo respetuoso, reconocer errores, pedir lo que falta y cerrar con el siguiente paso. Sin frases de bot. Humano no es largo.
- **"Cómo hablas":** cada ficha de agente añade una sección corta con su voz, sus expresiones y cómo da malas noticias.
- **Modo reunión del Consejo:** en la conversación, cada agente habla en primera persona y Ultron modera y cierra con las decisiones pendientes. `consejo.md` conserva la tabla resumen.
- **Límites:** los agentes dicen que son IA si alguien pregunta, no inventan vida privada y no cambian ninguna regla de `gobierno-agentes`. Ante clientes, la identidad sigue siendo El Guía Yizi.
- **Spec nueva:** `conversacion-agentes`.

## Capabilities

### New Capabilities
- `conversacion-agentes`: cómo hablan los agentes con el CEO y entre ellos: voz en primera persona, tono de colegas, reuniones y límites de identidad.

### Modified Capabilities
- Ninguna. `comunicacion` (Jarvis) sigue siendo la dueña del tono hacia clientes y de la guía de escritura. La nueva spec la cita y no la contradice.

## Impact

- Archivos: `CLAUDE.md` y `AGENTS.md` del núcleo, las 8 fichas del núcleo, la plantilla del líder de satélite, el skill `yizi-consejo` y `marca/guia-de-escritura.md` (nota de tono).
- Satélites: Karen (Yizi Solutions) y Herbie (Yizi Projects) aplican "Cómo hablas" a sus fichas con un cambio propio en su repositorio.
- Costo: sin gasto nuevo. Tokens extra: un saludo y una firma por mensaje. Estimación no medida; Edith la revisa en su compuerta.
- Organigrama: no cambia. No se crea, activa ni retira ningún agente.

## Out of Scope

- Cambiar la voz de El Guía Yizi ante clientes. Eso es de Jarvis, en `comunicacion`.
- Crear agentes nuevos o cambiar nombres.
- Dar a los agentes memoria entre sesiones o "vida" propia.
- Fijar `agent` por defecto en `.claude/settings.json`. La conversación principal sigue siendo Ultron.
