# Proposal: Ajustar el cupo MACRO (uno en curso, varios en Discovery)

**Resumen.** Yizi tiene un solo proyecto MACRO en construcción o en el mercado, y varios en prueba barata, cada uno con su tope.
**Hoy decides dos cosas:** apruebas la regla y confirmas que "activo" incluye la etapa de construcción (`incubacion`).

| Campo | Valor |
|---|---|
| Dueño | V.I.E.R.N.E.S (Viernes) · CSO |
| Alcance | nucleo |
| Tipo | estrategico |
| Tamaño | L (cambia una regla del núcleo que protege la caja y las horas del CEO) |
| Compuertas | Consejo completo (Viernes, Edith, Ultron, Vision, Jarvis) + aprobación del CEO |
| Pedido | CEO, 2026-11-22: "Yizi solo puede tener un proyecto MACRO 'activo' a la vez, pero sí puede tener varios proyectos en discovery o propuesta" |
| Pausa | CEO, 2026-11-22: "no veremos los proyectos aún". toFinance y el plan de comidas y mercado quedan en espera. |
| Consejo | 2026-11-22: cinco compuertas CONDICIONADO (`consejo.md`). Esta versión incorpora sus condiciones. |
| Aprobación | PENDIENTE |

## Palabras de este cambio

| Palabra | Qué significa aquí |
|---|---|
| Discovery | Fase de prueba barata de una idea. Usa entrevistas y prototipos simples. No tiene código de producto ni cobro. |
| Código de producto | Software que corre en un servidor o guarda datos reales de usuarios. Un prototipo sin servidor ni datos reales no lo es: pantallas dibujadas o una hoja de cálculo. |
| Cupo | El lugar para un proyecto en construcción o en el mercado. Hoy hay un solo cupo. |
| Tope | El máximo que un Discovery puede gastar: horas del CEO por semana, horas totales, caja en soles y fecha de fin. |
| Tope total | El máximo que pueden sumar todos los Discovery abiertos. Tiene horas por semana, horas por trimestre y caja por trimestre. |
| Trimestre | Trimestre calendario: enero a marzo, abril a junio, julio a septiembre, octubre a diciembre. |
| En espera | No es un estado del registro. Un veredicto EN ESPERA deja el proyecto en `propuesto`. Si el CEO pone en espera un proyecto en curso, pasa a `pausado`. |

## Why

La regla actual cuenta los proyectos "en incubación o activos". No dice nada de los Discovery. Por eso hay dudas:

1. toFinance figura `pausado` con un tope aprobado de 24 h y S/ 100. No sabemos si ese tope ocupa el cupo.
2. El plan de comidas y mercado sigue `propuesto`. Con la regla actual no sabemos si cabe junto a toFinance.
3. Mi propuesta anterior permitía un solo Discovery a la vez. El CEO pide permitir varios.

El 2026-11-22 el CEO pausó los dos proyectos. Por eso toFinance sigue `pausado` y el plan de mercado sigue `propuesto`. Esta regla no los mueve. Solo dice qué deben cumplir cuando el CEO los retome.

El límite cuida la caja y las horas del CEO, la única persona de Yizi. Un Discovery cuesta poco y enseña mucho. Construir un producto cuesta mucho. Por eso separamos las dos cosas:

- **Un solo proyecto MACRO en curso.** Está en `incubacion` (se construye) o en `activo` (está en el mercado).
- **Varios Discovery a la vez.** Cada uno tiene su tope. Todos caben dentro del tope total.

**Valor que lo justifica:** Agilidad Real, porque Yizi prueba varias ideas rápido y barato. Robustez Invisible, porque topes claros protegen la caja.

## What Changes

1. **Estados de un proyecto MACRO** (requisito nuevo). Son seis: `propuesto`, `discovery`, `incubacion`, `activo`, `pausado` y `cerrado`. Solo `incubacion` y `activo` ocupan el cupo.
2. **Límite de proyectos MACRO simultáneos** (modificado). El cupo cuenta solo `incubacion` y `activo`. Puede haber varios proyectos en `propuesto` y en `discovery`.
3. **Pausa real** (nuevo). `pausado` significa cero horas y cero caja en curso. El tope aprobado se guarda en la ficha. Salir de `pausado` hacia `discovery` cuenta como un Discovery nuevo.
4. **Discovery con tope propio** (nuevo). Edith revisa el tope y el CEO lo aprueba. Un Discovery no escribe código de producto, no cobra y no lanza marca.
5. **Marca y público en un Discovery** (nuevo). Jarvis revisa todo texto o prototipo que vea una persona externa. Una persona confirma cada envío.
6. **Tope total de Discovery** (nuevo). Lo propone Edith y lo decide el CEO. Sin tope total, ningún Discovery se abre.
7. **Vigilancia del consumo de Discovery** (nuevo). El CEO reporta sus horas cada viernes y Edith anota la caja. Todo queda en la tabla "Consumo" de la ficha. Ultron avisa y detiene las sesiones de agentes.
8. **Fin de un Discovery** (nuevo). Viernes propone uno de cuatro caminos. Herbie anota en la ficha el camino que elige el CEO.
9. **Veredictos de la Autoridad MACRO** (modificado). El CEO puede autorizar solo el Discovery. EN ESPERA deja el proyecto en `propuesto`.

Esta regla reemplaza mi propuesta anterior en `yizi-projects/proyectos/idea-mercado-barrio/discovery/enfoque-discovery.md` (sección 10) y `evaluacion.md` (sección 4). Ya no hay "máximo 1 Discovery". toFinance no pasa a `incubacion`.

### Qué es cada estado

| Estado | Qué significa | ¿Ocupa el cupo? | ¿Cuántos a la vez? |
|---|---|---|---|
| `propuesto` | Idea o expediente en evaluación. Solo gasta sesiones de agentes y el tiempo del CEO para decidir. | No | Varios |
| `discovery` | Prueba barata con tope aprobado. Entrevistas, pantallas o una hoja de cálculo. Sin código de producto, sin cobro, sin marca pública. | No | Varios, dentro del tope total |
| `incubacion` | Autorizado por la Autoridad MACRO para construir: código, marca pública, gasto mayor. | **Sí** | 1 (`macro_simultaneos_max`) |
| `activo` | Producto en el mercado, con usuarios. | **Sí** | Comparte el cupo con `incubacion` |
| `pausado` | Cero horas y cero caja en curso. Su tope aprobado queda guardado en la ficha. | No | Varios |
| `cerrado` | Terminado. Se guarda lo aprendido. | No | — |

`activo` de un proyecto no es `activo` de un satélite. Un satélite `activo` es una línea de negocio que opera (spec `satelites`). Un proyecto `activo` es un producto MACRO en el mercado.

### Qué pasa con cada proyecto de hoy

| Proyecto (id y carpeta) | Hoy | Con esta regla | Al reanudar |
|---|---|---|---|
| toFinance (`tofinance`) | `pausado` por el CEO el 2026-11-22. Tope aprobado y sin usar: 4 h por semana, 24 h totales, S/ 100. | Sigue `pausado`. Su tope queda guardado en la sección 4 de su ficha. No ocupa el cupo. | Pasa a `discovery` solo con tope total fijado y fecha de fin. La fecha de fin es una decisión de su ficha (sección 8). |
| Plan de comidas y mercado (`idea-mercado-barrio`) | `propuesto`, en espera. El registro usa el id `plan-mercado`. | Sigue `propuesto`. El id del registro pasa a `idea-mercado-barrio`, igual que su carpeta. No ocupa el cupo. | Pasa a `discovery` con tope aprobado y tope total fijado. Su tope es una decisión de su ficha (sección 8). |

Hoy **el cupo MACRO está libre**. Ningún proyecto construye. El primero que cumpla la Ruta A (expediente completo y veredicto AUTORIZADO) lo ocupará.

El id del registro debe coincidir con la carpeta del proyecto. Si el plan de mercado cambia de nombre al pasar a `discovery`, Herbie cambia la carpeta y el id en el mismo cambio.

### Por qué toFinance no va a `discovery` ni a `incubacion` hoy

1. `incubacion` le daría el cupo sin construir nada. Su fase 0 es un Discovery: entrevistas, sin código.
2. `discovery` exige horas en curso. El CEO pausó el proyecto y nadie gasta horas en él.
3. `pausado` es el estado correcto. Su tope aprobado queda guardado para cuando el CEO lo retome.

### Salvaguarda de caja y horas

Varios Discovery pueden sumar más horas de las que el CEO tiene. Por eso hay tres capas:

1. **Tope propio.** Cada Discovery tiene horas por semana, horas totales, caja y fecha de fin. Edith lo revisa con sus supuestos. El CEO lo aprueba.
2. **Tope total.** Mide horas por semana, horas por trimestre y caja por trimestre. Cuenta lo gastado más lo comprometido. Una extensión cuenta como gasto nuevo. En semanas con piloto de Yizi Solutions, el tope semanal baja a la mitad.
3. **Vigilancia de Ultron.** El CEO le reporta sus horas cada viernes. Edith anota la caja. Ultron avisa al 80 % y detiene las sesiones de agentes al 100 %. Ultron no puede detener las horas del CEO: le avisa.

**Propuesta de Edith para el tope total** (estimación, no verificada contra la caja):

| Concepto | Propuesta | Estado |
|---|---|---|
| Horas del CEO por semana | 6 h (3 h en semanas con piloto de Yizi Solutions) | Estimación, no verificada. Ultron debe confirmar que el CEO tiene esas horas. |
| Horas del CEO por trimestre | Sin propuesta | Pendiente de Edith |
| Caja por trimestre | S/ 180, lo gastado más lo comprometido | Estimación, no verificada. El CEO debe confirmar cuánta caja propia puede poner. |
| Aviso | Al 80 % de cada tope | Estimación, no verificada |

Esa cifra no se decide hoy. La spec impide abrir un Discovery sin tope total. Por eso el CEO la decide al retomar el primer Discovery.

## Capabilities

### New Capabilities
- Ninguna.

### Modified Capabilities
- `autoridad-macro`: se modifican dos requisitos ("Veredictos de la Autoridad MACRO" y "Límite de proyectos MACRO simultáneos"). Se añaden dieciséis:
  - Estados: "Estados de un proyecto MACRO", "En espera no es un estado", "Id del proyecto igual a su carpeta" y "Pausa real".
  - Discovery: "Discovery con tope propio" y "Código de producto en un Discovery".
  - Marca: "Proyectos sin autorizar ante clientes", "Textos externos de un Discovery" y "Marca pública de un Discovery".
  - Topes: "Tope total de Discovery" y "Cómo se mide el tope total".
  - Consumo: "Registro del consumo de Discovery", "Vigilancia del consumo de Discovery" y "Sesiones de agentes de un Discovery".
  - Cierre: "Fin de un Discovery" y "Extensión y aviso al cerrar un Discovery".

## Impact

- `satelites/registro.yaml`: comentario con los estados de proyecto; toFinance sigue `pausado` con su `etapa` corregida; el id `plan-mercado` pasa a `idea-mercado-barrio`. Las claves del tope total en `limites` llegan al retomar el primer Discovery.
- `.agents/skills/yizi-consejo/SKILL.md`: el modo MACRO revisa el tope propio, el tope total y la marca de cada Discovery.
- Fichas de agentes: Viernes (cupo), Edith (tope total y revisión de topes), Ultron (recordatorio de los viernes) y Jarvis (textos externos y nota de marca). Cada dueño edita su ficha.
- `ceo/pendientes.md`: la línea del cupo cambia. La fecha de fin de toFinance no entra: va a su ficha.
- `yizi-projects` (satélite), por un cambio hermano que abre Herbie: README de proyectos, secciones 1, 4 y 8 de las dos fichas, tabla "Consumo" y una enmienda pequeña a la spec `ficha-proyecto-macro`.
- No cambia la spec `satelites`: sus estados son de los satélites, no de los proyectos.

## Costo estimado (Edith)

| Concepto | Estimación | Fuente |
|---|---|---|
| Horas del CEO | 45 a 60 minutos para leer y decidir | Edith, `consejo.md`, 2026-11-22. Estimación, no verificada. |
| Sesiones de agentes | 5 o 6 sesiones dentro del plan de IA del CEO: Consejo, cifras, implementación, cambio hermano y verificación de Lince | Edith, `consejo.md`, 2026-11-22. Estimación. Consumo real: sin medir. Edith lo registra en `finanzas/consumo-ia.md`. |
| Caja | S/ 0 | Edith, `consejo.md`, 2026-11-22. Estimación: solo cambia texto y registro. |

El cambio no gasta caja. Limita el gasto futuro de los Discovery.

## Decisiones del CEO

Hoy decides solo dos cosas:

1. **La regla.** ¿Apruebas un solo proyecto MACRO en construcción o en el mercado, y varios en `propuesto` o `discovery`?
2. **Qué incluye "activo".** Cuando dijiste "activo", ¿incluyes `incubacion`, la etapa en que se construye? Recomiendo que sí. Construir es lo que más caja y horas gasta.

Decisiones que no tomas hoy:

- **El tope total.** Lo decides al retomar el primer Discovery. Antes confirmas cuánta caja propia puedes poner por trimestre. La spec impide abrir un Discovery sin esa cifra.
- **La fecha de fin de toFinance y el tope del plan de mercado.** Son decisiones de cada proyecto. Herbie las anota en la sección 8 de cada ficha. Las decides al retomar cada proyecto.

## Out of Scope

- Subir `macro_simultaneos_max` a 2. Edith no lo recomienda mientras Yizi Solutions no llegue a su punto de equilibrio.
- Los estados de los satélites (spec `satelites`). No cambian.
- Fusionar toFinance con el plan de comidas y mercado. Siguen separados.
- Reanudar toFinance o el plan de mercado. Los retoma el CEO cuando decida.
- Las cifras finales del tope total y de cada Discovery: las decide el CEO.
- Editar el repo `yizi-projects`: va por el cambio hermano que abre Herbie.
- Implementar el cambio: este cambio solo propone. No toca la spec vigente, el registro ni los pendientes hasta que el CEO apruebe.
