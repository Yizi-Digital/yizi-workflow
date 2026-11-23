# Consejo · agentes-conversan-como-personas

| Campo | Valor |
|---|---|
| Dueño | A.I.D.A (Aida) |
| Alcance | nucleo |
| Tipo / Tamaño | marca-comunicacion / L |
| Fecha de revisión | 2026-11-20 |

## Veredictos

| Agente | Compuerta | Veredicto | Condiciones |
|---|---|---|---|
| Vision | Viabilidad técnica | CONDICIONADO | Probar `--agent` con una ficha antes de documentarlo; prohibir `--agent ultron` por escrito; tope de 150 palabras solo para el mensaje al CEO; Ultron marca contenido externo que dé órdenes |
| Jarvis | Marca y cliente | CONDICIONADO | "Tono entre colegas" solo interno, remite a `comunicacion`; borrador para cliente separado, sin firma ni nombre interno, marcado "requiere aprobación" |
| Edith | Costo y presupuesto | CONDICIONADO | Modelo por tarea en `tasks.md` (Sonnet, Haiku, nunca Fable); sesiones `--agent` anotadas aparte en `finanzas/consumo-ia.md` |
| Viernes | Alineación estratégica | CONDICIONADO | Justificar con Agilidad Real y los principios humano-IA (o explicar la analogía con Empatía Operativa) |
| Ultron | Operabilidad | CONDICIONADO | Prueba de Lince para "mensaje que rompe una regla"; tarea 1.1 pide al subagente un "mensaje para el CEO" en primera persona |

**Resumen:** ninguna compuerta está BLOQUEADA. Aida incorporó las condiciones el 2026-11-20 (validación estricta OK).

## Reunión (modo propuesto por el cambio)

**Vision:** Leí el cambio completo. Técnicamente es viable y simple: solo cambia texto en fichas, CLAUDE.md y el skill. No toca código, pagos ni datos. Tengo tres reparos: probar `--agent` antes de documentarlo, que el tope de 150 palabras sea solo para el mensaje al CEO, y que Ultron marque el contenido externo que dé órdenes (riesgo LLM01 de OWASP).

**Jarvis:** El cambio me parece bueno. Los siete gestos y la tabla "No digas / Di" siguen la guía de escritura. Pido que "Tono entre colegas" quede como solo interno y que el borrador para un cliente vaya separado del mensaje firmado al CEO, sin firma ni nombre interno.

**Edith:** Lo apruebo con dos condiciones. No hay gasto nuevo: el saludo y la firma suman pocos tokens y el tope puede ahorrar. El riesgo está en la sesión directa: con `claude --agent edith` uso Opus toda la sesión. Pido el modelo por tarea y anotar esas sesiones aparte.

**Viernes:** Apoyo el cambio. No toca la misión, la visión ni los valores, y mantiene "humano al mando" y "verdad antes que velocidad". Mi reparo: Empatía Operativa y Robustez Invisible se definen para el cliente final. Prefiero justificarlo con Agilidad Real y los principios humano-IA.

**Ultron:** Funciona para mí. Dejo de resumir, pego el mensaje firmado de cada agente y modero. Faltan dos cosas: una prueba de Lince para el mensaje que rompe una regla, y que la tarea 1.1 pida al subagente un "mensaje para el CEO" en primera persona.

**Ultron (cierre):** Los cinco dan CONDICIONADO y nadie bloquea. Aida aplica las condiciones. Queda la decisión del CEO.

## Decisión del CEO

- Decisión: **APROBADO**. El CEO: "Sí".
- Fecha: 2026-11-20
- Tope por mensaje: el CEO decide: "Si la respuesta puede ser corta, en menos de 150 palabras, que lo haga en un lenguaje natural como una persona o colega. Si es larga, que siga hablando como un colega, pero que al final me lance un detalle más detallado en un mensaje directo." Aida lo incorpora a D1.1 y a la spec.
- Anulaciones de compuertas BLOQUEADAS (con motivo): ninguna
