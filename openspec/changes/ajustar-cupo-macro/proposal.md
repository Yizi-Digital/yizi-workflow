# Proposal: Ajustar el cupo MACRO (uno en curso, varios en Discovery)

| Campo | Valor |
|---|---|
| Dueño | V.I.E.R.N.E.S (Viernes) · CSO |
| Alcance | nucleo |
| Tipo | estrategico |
| Tamaño | L (cambia una regla del núcleo que protege la caja y las horas del CEO) |
| Compuertas | Consejo completo (Viernes, Edith, Ultron, Vision, Jarvis) + aprobación del CEO |
| Pedido | CEO, 2026-11-22: "Yizi solo puede tener un proyecto MACRO 'activo' a la vez, pero sí puede tener varios proyectos en discovery o propuesta" |
| Aprobación | PENDIENTE |

## Why

La regla actual cuenta los proyectos "en incubación o activos". No dice nada de los Discovery. Por eso hoy hay dudas:

1. toFinance figura como `pausado`, pero tiene trabajo autorizado (24 h y S/ 100). Por la letra no ocupa el cupo. Por los hechos, consume horas y caja.
2. El plan de comidas y mercado espera su Discovery. Con la regla actual no sabemos si cabe junto a toFinance.
3. Mi propuesta anterior permitía solo 1 Discovery a la vez. El CEO pide permitir varios.

El límite existe para cuidar la caja y las horas del CEO, que es la única persona de Yizi. Un Discovery cuesta poco y enseña mucho. Construir un producto cuesta mucho. Por eso proponemos separar las dos cosas:

- **Un solo proyecto MACRO en curso** (`incubacion` o `activo`): el que construye o opera un producto.
- **Varios Discovery a la vez**, cada uno con su propio tope y todos dentro de un tope total que vigila Ultron.

**Valor que lo justifica:** Agilidad Real. Yizi prueba varias ideas en paralelo, rápido y barato, sin abrir dos productos a la vez. También Robustez Invisible: la caja queda protegida por topes claros y medibles.

## What Changes

1. **Estados de un proyecto MACRO** (requisito nuevo). Se definen `propuesto`, `discovery`, `incubacion`, `activo`, `pausado` y `cerrado`. Solo `incubacion` y `activo` ocupan el cupo.
2. **Límite de proyectos MACRO simultáneos** (requisito modificado). El cupo cuenta solo los proyectos en `incubacion` o `activo`. Los proyectos en `propuesto` y `discovery` no lo ocupan. Pueden ser varios.
3. **Discovery con tope propio** (requisito nuevo). Cada Discovery tiene tope de horas del CEO, caja y fecha de fin, aprobado por el CEO. Sin código, sin cobro y sin lanzamiento público.
4. **Tope total de Discovery** (requisito nuevo). La suma de los topes de todos los Discovery abiertos no puede pasar el tope total del registro. Edith propone la cifra. El CEO decide. Ultron vigila el consumo real.
5. **Fin de un Discovery** (requisito nuevo). Al llegar a su fecha o a su tope, Viernes propone uno de cuatro caminos: pasar a `incubacion`, extender con un tope nuevo, pausar o cerrar.
6. **Veredictos de la Autoridad MACRO** (requisito modificado). El CEO puede autorizar solo el Discovery de un proyecto MACRO. Pasar a `incubacion` exige expediente completo, veredicto AUTORIZADO y cupo libre.

Esta regla reemplaza mi propuesta anterior en `yizi-projects/proyectos/idea-mercado-barrio/discovery/enfoque-discovery.md` (sección 10) y `evaluacion.md` (sección 4): ya no hay "máximo 1 Discovery", y toFinance no pasa a `incubacion`.

### Qué es cada estado

| Estado | Qué significa | ¿Ocupa el cupo? | ¿Cuántos a la vez? |
|---|---|---|---|
| `propuesto` | Idea o expediente en evaluación. Solo gasta sesiones de agentes y el tiempo del CEO para decidir. | No | Varios |
| `discovery` | Validación con tope aprobado por el CEO: entrevistas, prototipo en papel o pantallas, estudio. Sin código, sin cobro y sin lanzamiento. | No | Varios, dentro del tope total |
| `incubacion` | Autorizado por la Autoridad MACRO para construir: código, marca pública, gasto mayor. | **Sí** | 1 (`macro_simultaneos_max`) |
| `activo` | Producto en el mercado, con usuarios. | **Sí** | Comparte el cupo con `incubacion` |
| `pausado` | Cero horas y cero caja en curso. Volver al estado anterior exige su regla (tope o cupo). | No | Varios |
| `cerrado` | Terminado. Se guarda lo aprendido. | No | — |

### Qué pasa con cada proyecto de hoy

| Proyecto | Hoy | Con esta regla | Qué falta |
|---|---|---|---|
| toFinance | `pausado`, "discovery indefinido", autorizado MACRO solo para la fase 0 (Ruta B) | `discovery`, con su tope de 24 h y S/ 100. No ocupa el cupo. | El CEO fija la fecha de fin. "Indefinido" no cabe en la regla. Propuesta, no verificada: 6 semanas desde que se reanude, como en la autorización original. |
| Plan de comidas y mercado | `propuesto`, Discovery de señal sin tope aprobado | Sigue en `propuesto` hasta que el CEO apruebe su tope. Luego pasa a `discovery`. No ocupa el cupo. | El CEO aprueba su tope (propuesto: 12 h, S/ 80, 6 semanas). |

Así, **el cupo MACRO queda libre**. Ningún proyecto construye hoy un producto. El primero que pida pasar a `incubacion` lo ocupará. toFinance solo puede hacerlo si cumple la Ruta A.

### Por qué toFinance va a `discovery` y no a `incubacion`

Antes propuse `incubacion`. Lo cambio por dos razones:

1. La fase 0 de toFinance es un Discovery: sin código, con entrevistas y con tope chico. Llamarla `incubacion` le daría el cupo sin construir nada.
2. `pausado` tampoco es correcto: tiene trabajo autorizado. Con la nueva regla, `pausado` significa cero horas y cero caja.

### Salvaguarda de caja y horas

Varios Discovery a la vez pueden sumar más horas de las que el CEO tiene. La salvaguarda tiene tres capas:

1. **Tope propio.** Cada Discovery tiene horas, caja y fecha de fin aprobadas por el CEO. Si se acaba, para.
2. **Tope total.** La suma de los topes de todos los Discovery abiertos no puede pasar el tope total del registro. Se mide en horas del CEO por semana y en caja total en soles. Si un Discovery nuevo no cabe, espera en `propuesto`.
3. **Vigilancia de Ultron.** Ultron lleva el consumo real de cada Discovery y la suma. Avisa al CEO al 80 % de cualquier tope y para el trabajo al 100 %. Las horas de Discovery nunca desplazan el trabajo comprometido con clientes de un satélite activo.

Sumamos topes aprobados, no consumo real. Así el CEO sabe desde el inicio cuánto puede comprometer como máximo.

**Cifra del tope total: decide el CEO, con propuesta de Edith.** Como referencia, la suma de los dos topes de hoy es 6 h por semana (4 h de toFinance + 2 h del plan de mercado) y S/ 180 (S/ 100 + S/ 80). Esa suma es una propuesta, no verificada: Edith debe confirmarla con la caja disponible. El umbral de aviso del 80 % también es una propuesta.

## Capabilities

### New Capabilities
- Ninguna.

### Modified Capabilities
- `autoridad-macro`: se modifican dos requisitos ("Veredictos de la Autoridad MACRO" y "Límite de proyectos MACRO simultáneos") y se añaden seis ("Estados de un proyecto MACRO", "Pausa real", "Discovery con tope propio", "Tope total de Discovery", "Vigilancia del consumo de Discovery" y "Fin de un Discovery").

## Impact

- `satelites/registro.yaml`: claves nuevas en `limites` para el tope total de Discovery; estado `discovery` para los proyectos; tope y fecha de fin de cada Discovery; toFinance a `discovery`.
- `.agents/skills/yizi-consejo/SKILL.md`: el modo MACRO revisa también el tope total de Discovery.
- Fichas de Viernes y Edith: una línea cada una sobre el cupo y el tope total.
- `ceo/pendientes.md`: la decisión del cupo cambia de texto.
- `yizi-projects` (satélite): el README de proyectos y el README de cada Discovery muestran su tope y su consumo. Va por un cambio en ese repositorio.
- No cambia la spec `satelites`: sus estados son de los satélites, no de los proyectos.

## Costo estimado (para Edith)

| Concepto | Estimación | Fuente |
|---|---|---|
| Horas del CEO | Unos 30 minutos para leer y decidir | Estimación de Viernes, no verificada |
| Sesiones de agentes | Consejo, implementación y verificación por Lince: unas 4 sesiones dentro del plan de IA del CEO | Estimación de Viernes. Consumo real: sin medir. Edith lo registra en `finanzas/consumo-ia.md`. |
| Herramientas o caja | S/ 0 | Solo cambia texto y registro |

El cambio no gasta caja. Su efecto es limitar el gasto futuro de los Discovery.

## Decisiones del CEO

1. Aprobar la regla: 1 MACRO en curso (`incubacion` o `activo`) y varios en `propuesto` o `discovery`.
2. Confirmar que "activo" en tu pedido incluye `incubacion`. Recomiendo que sí: construir es lo que más caja y horas gasta.
3. Fijar el tope total de Discovery, con la propuesta de Edith.
4. Fijar la fecha de fin del Discovery de toFinance.
5. Aprobar el tope del plan de comidas y mercado (decisión ya pendiente).

## Out of Scope

- Subir `macro_simultaneos_max` a 2. Edith no lo recomienda mientras Yizi Solutions no llegue a su punto de equilibrio.
- Los estados de los satélites (spec `satelites`). No cambian.
- Fusionar toFinance con el plan de comidas y mercado. Siguen separados.
- Las cifras finales del tope total y de cada Discovery: las decide el CEO.
- Implementar el cambio: este cambio solo propone. No toca la spec vigente, el registro ni los pendientes hasta que el CEO apruebe.
