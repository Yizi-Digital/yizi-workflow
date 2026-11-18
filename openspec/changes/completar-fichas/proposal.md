# Proposal: Completar las fichas de los agentes y diseñar los 3 agentes de antes de los pilotos

| Campo | Valor |
|---|---|
| Dueño | A.I.D.A (Aida) · diseño de agentes |
| Alcance | nucleo |
| Tipo | operacion |
| Tamaño | M (un dominio, el de los agentes, sin dinero ni clientes; toca fichas del Consejo) |
| Compuertas | Dueña (Aida) + dominios afectados: Vision (herramientas y verificación), Jarvis (Diagnóstico Flash, spec `comercial`), Edith (modelos y costo por uso), Ultron (herramientas, `jerarquia-agentes` y `gobierno-agentes`) |
| Aprobación | Aprobado por el CEO el 2026-11-18 |
| Base | `agentes/mapa-de-agentes.md` (estudio de Aida, 2026-11-18), secciones 1.3, 2.3 y 7 |

## Why

Ninguna de las fichas de Yizi cumple completa la lista de revisión de Aida (estudio, sección 1.3). Faltan tres cosas en todas:

1. **Referencias con fuente y fecha.** La spec `diseno-agentes` lo exige.
2. **El costo por uso.** Sin ese dato, Edith no puede medir el gasto por agente.
3. **Permisos mínimos en Vision y Ultron.** Sus fichas no tienen la línea `tools:`. Sin ella, Claude Code les da todas las herramientas (documentación de subagentes de Claude Code, consultada el 2026-11-18). Eso rompe el requisito "Permisos mínimos" de `gobierno-agentes`.

Además, hay un cruce: la ficha de Jarvis dice que él "dirige el Ciclo de Servicio", y el flujo operativo de Yizi Solutions dice que Karen "define el Diagnóstico Flash". Nadie sabe quién lo lidera.

Por último, el CEO pidió los nombres de los 3 agentes que hacen falta antes de los pilotos: el verificador independiente, el analista de pilotos y El Guía Yizi en modo ayuda (versión mínima).

**Valor que lo justifica:** Robustez Invisible. Un agente que cita sus fuentes, sabe qué decide y solo tiene las herramientas que necesita falla menos y se puede revisar.

## What Changes

- **Siete fichas del núcleo** (`.claude/agents/`): Vision, Jarvis, Edith, Viernes, Ultron, Aida y Termy. Cada una recibe:
  - una sección **Referencias** con fuente y fecha de consulta, o "no verificado";
  - una fila **Costo por uso** en su tabla;
  - lo que faltaba según el estudio (ver la tabla de abajo).
- **Línea `tools:` en Vision y Ultron**, con la justificación escrita en su ficha.
- **Regla del Diagnóstico Flash:** lo lidera el líder N2 del satélite que atiende al cliente (en Yizi Solutions, Karen). Jarvis es dueño del método y de la plantilla, y apoya en marca y cliente. Entra como cambio del requisito "Diagnóstico Flash" de la spec `comercial`.
- **Karen y Herbie:** sus fichas viven en sus satélites. Este cambio **no edita** esos repositorios. El texto propuesto está en `fichas-satelites.md`. Karen y Herbie lo aplican con un cambio en su propio satélite.
- **Tres fichas nuevas en diseño**, en `fichas-nuevas/`. No se copian a `.claude/agents/` ni se activan hasta que el CEO apruebe los nombres y el cambio propio de cada agente.

### Qué se completó en cada ficha

| Ficha | Qué se añadió |
|---|---|
| Vision | `tools:` con justificación. Referencias (ISO/IEC 25010, OWASP Top 10 web y LLM, WCAG 2.2, Anthropic). Costo por uso. Regla de delegar tareas simples a ejecutores N4 de nivel Estándar. Regla: no verifica lo que él implementó. |
| Jarvis | El Diagnóstico Flash lo lidera el líder del satélite; Jarvis es dueño del método y apoya en marca y cliente. Referencias (ASD-STE100, WCAG 2.2). Costo por uso. |
| Edith | Fuente y fecha de la tabla de modelos, con el precio por millón de tokens de cada nivel. Referencias. Costo por uso. |
| Viernes | Referencias (solo fuentes internas; sin marcos externos inventados). Costo por uso. |
| Ultron | `tools:` con justificación. Referencias (OpenSpec, Claude Code). Costo por uso. Regla: pide verificación independiente antes de archivar. |
| Aida | Criterio escrito: qué decide y qué escala. Referencias. Costo por uso. |
| Termy | Criterio escrito: qué decide y qué escala. Referencias de normas laborales y de datos personales de Perú, marcadas para revisión del abogado. Costo por uso. |

## Nombres propuestos para aprobación del CEO

Los tres nombres son únicos en todo Yizi. Revisé los nombres y las alternativas en uso en el núcleo, en Yizi Solutions y en Yizi Projects (incluidos Argos y Talos, ya propuestos en Yizi Projects). Ninguno aparece ante clientes.

| Rol | Nombre formal | Corto | Alternativa | Por qué el nombre |
|---|---|---|---|---|
| Verificador independiente (N1 de área del núcleo, bajo Ultron) | L.I.N.C.E | Lince | T.A.R.S / Tars | "Ojo de lince": no se le escapa nada. Tars es el robot de *Interstellar* con su "nivel de honestidad". |
| Analista de pilotos y de operación (N3 de Yizi Solutions, bajo Karen) | Y.U.P.A.N.A | Yupana | Á.B.A.C.O / Ábaco | La yupana es el ábaco inca: sirve para contar. Las cifras salen de contar, no de suponer. |
| El Guía Yizi · modo ayuda (agente del producto, N3 de Yizi Solutions) | C.H.A.S.K.I | Chaski | A.M.A.U.T.A / Amauta | El chaski era el mensajero inca que llevaba el recado rápido a quien debía resolverlo. El modo ayuda responde rápido y pasa a una persona lo que no resuelve. |

**Nota sobre Chaski:** es un nombre **interno**. Ante el bodeguero, el agente siempre se llama El Guía Yizi.

## Capabilities

### New Capabilities
- Ninguna.

### Modified Capabilities
- `comercial`: el requisito "Diagnóstico Flash" dice quién lo lidera y qué hace Jarvis.

## Impact

- `.claude/agents/vision.md`, `jarvis.md`, `edith.md`, `viernes.md`, `ultron.md`, `aida.md` y `termy.md`.
- Spec `comercial` (al archivar).
- Nuevos archivos del cambio: `fichas-satelites.md` y `fichas-nuevas/` (3 fichas de diseño).
- El plugin `yizi-nucleo` entrega las fichas nuevas a los satélites cuando el CEO fusione la rama.
- **Costo:** 0 USD de gasto extra. Consumo de una sesión de Aida (nivel Avanzado) dentro del plan de IA.

## Out of Scope

- **Crear o activar** los 3 agentes nuevos. Cada uno necesita su propio cambio aprobado por el CEO. El verificador necesita además cambiar `jerarquia-agentes`: hoy esa spec nombra solo a Aida y Termy como agentes de área.
- **Agentes del producto en `jerarquia-agentes`.** La spec aún no contempla agentes del producto (El Guía Yizi). Lo propone Ultron, su dueño, en un cambio aparte.
- **Editar los repositorios** `yizi-solutions` y `yizi-projects`.
- **Fichas de Homer y Jocasta.** Sus satélites están en incubación.
- **La regla de aprobación por lote** y la "bandeja de lotes" de Ultron. Esperan su propio cambio en `gobierno-agentes`.
- **Cómo se paga la IA del producto** (API o plan). Lo confirman Vision y Edith.
- **Medir el costo real por agente.** Edith lo registra en `finanzas/consumo-ia.md`. Hoy todas las fichas dicen "sin medir".
