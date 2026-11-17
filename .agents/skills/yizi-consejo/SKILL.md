---
name: yizi-consejo
description: Convoca al Consejo Ejecutivo de Yizi (Vision, Jarvis, Edith, Viernes, Ultron) para revisar un cambio de OpenSpec antes de su aprobación, o a la Autoridad MACRO para evaluar un proyecto propio. Activa las compuertas según el tamaño del cambio, reúne los veredictos en consejo.md y pide la decisión al CEO. Úsalo cuando el usuario diga "consejo", "revisión del consejo", "que lo revise el consejo", "compuertas", "Autoridad MACRO" o "evalúa este proyecto macro".
license: Propietaria · Yizi Digital
metadata:
  author: yizi-digital
  version: "1.0"
  nucleo: yizi-workflow
---

Convoca la revisión multiagente de un cambio (fase 2 del ciclo SDD de Yizi) y deja el resultado en `consejo.md`.

**Límite de planificación:** este skill no implementa nada. Termina cuando `consejo.md` está escrito y el CEO tiene la información para decidir.

---

## 1. Identifica el cambio

- Si el usuario nombró un cambio, úsalo. Si no, ejecuta `openspec list --json` y, si hay más de uno, pregunta cuál.
- En un satélite, las specs del núcleo se leen con `--store yizi-workflow`.

## 2. Comprueba que está listo para revisión

1. Ejecuta `openspec validate <cambio> --strict`. Si falla, detente y muestra los errores: el Consejo no revisa planes inválidos.
2. Lee `proposal.md` y extrae la tabla de metadatos: **Dueño, Alcance, Tipo, Tamaño, Compuertas**. Si falta alguno, detente y pide completarlo (spec `ciclo-sdd`).

## 3. Decide qué compuertas se activan

| Tamaño | Quién revisa |
|---|---|
| S | Solo el dueño. No hace falta este skill: pide la confirmación breve al CEO y termina. |
| M | El dueño + cada agente cuyo dominio se ve afectado |
| L | Consejo completo (los cinco) |
| MACRO | Autoridad MACRO (ver sección 6) |

Dominios: técnico → **Vision** · marca, textos, interfaz o cliente → **Jarvis** · costo, precio o gasto → **Edith** · estrategia, foco, satélites o cultura → **Viernes** · tareas, plazos, capacidad o procesos → **Ultron**.

## 4. Reúne los veredictos

**En Claude Code:** lanza en paralelo un subagente por compuerta (`vision`, `jarvis`, `edith`, `viernes`, `ultron`; si vienen del plugin pueden aparecer como `yizi-nucleo:<nombre>`). A cada uno pásale:
- la ruta del cambio y la instrucción de leer `proposal.md`, `specs/`, `design.md` y `tasks.md`;
- que revise **solo su compuerta** con el checklist de su ficha;
- que devuelva su veredicto en el formato de su ficha (APROBADO, CONDICIONADO o BLOQUEADO, con motivos y condiciones).

**Si la ventana de 5 horas del plan de IA está cerca de agotarse** (spec `finanzas`): no lances subagentes en paralelo; revisa las compuertas una a una, empezando por la de mayor riesgo, y avisa al CEO si alguna queda pendiente.

**En otra herramienta de IA:** asume cada rol por turnos leyendo su ficha en `.claude/agents/<nombre>.md` y escribe cada veredicto por separado. No mezcles los criterios de un rol con los de otro.

## 5. Escribe `consejo.md`

Crea o actualiza `openspec/changes/<cambio>/consejo.md` con esta estructura:

```markdown
# Consejo · <cambio>

| Campo | Valor |
|---|---|
| Dueño | <agente> |
| Alcance | <nucleo o id de satélite> |
| Tipo / Tamaño | <tipo> / <tamaño> |
| Fecha de revisión | <AAAA-MM-DD> |

## Veredictos

| Agente | Compuerta | Veredicto | Condiciones |
|---|---|---|---|
| Vision | Viabilidad técnica | ... | ... |

## Detalle

<pega aquí el veredicto completo de cada agente>

## Decisión del CEO

- Decisión: PENDIENTE
- Fecha:
- Anulaciones de compuertas BLOQUEADAS (con motivo):
```

Reglas:
- Si alguna compuerta está **BLOQUEADA**, el resumen lo dice primero y el cambio **no** pasa a implementación.
- Nunca escribas "APROBADO" en la decisión del CEO por tu cuenta. Solo regístralo cuando el CEO lo diga explícitamente en la conversación, con su fecha.

## 6. Modo MACRO (Autoridad MACRO)

Úsalo cuando el tipo o el tamaño es `macro`.

1. **Viernes** comprueba que el expediente está completo: problema y público, encaje con la misión, modelo de ingresos, costo estimado y tiempo de retorno, riesgo de dilución de marca, capacidad requerida, criterio de éxito y criterio de cierre. Si falta algo, devuélvelo sin evaluar.
2. Comprueba en `satelites/registro.yaml` (del núcleo) el límite `macro_simultaneos_max` y cuántos proyectos MACRO hay en `incubacion` o `activo`.
3. Evalúan **Edith** (finanzas), **Vision** (técnica), **Jarvis** (mercado y marca) y **Ultron** (capacidad).
4. **Viernes** consolida una recomendación: AUTORIZADO, EN ESPERA o RECHAZADO. Si el cupo está lleno, la recomendación máxima es EN ESPERA.
5. Escribe todo en `consejo.md` y pide la decisión al CEO.

## 7. Cierra

Muestra al CEO:
- una línea por agente con su veredicto;
- las condiciones que deben cumplirse;
- la pregunta concreta: "¿Apruebas este plan para implementar?" (o "¿Autorizas este proyecto MACRO?").
