# Proposal: Activar Yizi Publisher con la IA en el centro

| Campo | Valor |
|---|---|
| Dueño | V.I.E.R.N.E.S (Viernes) · CSO |
| Alcance | nucleo |
| Tipo | estrategico |
| Tamaño | L (cambio de estado de un satélite, gasto, varios dominios y una spec del núcleo) |
| Compuertas | Consejo completo (Vision, Jarvis, Edith, Viernes, Ultron) + aprobación del CEO |
| Aprobación | Pendiente. Pedido del CEO del 2026-11-18: "si va por ahí, activemos Yizi Publisher… pero no nos alejemos de la visión de incluir IA y hacer que todo el mundo la use" |
| Insumos | `estudio/`: pedido del CEO, oferta de Jarvis, economía de Edith, herramientas de Vision, agentes de Aida, personas de Termy y frontera de Karen |

## Why

El CEO quiere ofrecer presencia digital, gestión de redes y ventas digitales. Ese servicio pertenece a Yizi Publisher, el frente del mercado, que hoy está en `incubacion`. Un satélite en incubación no puede ofrecerse a clientes (spec `satelites`). Por eso hace falta este cambio.

Publisher es la caja más rápida del grupo. Según Edith, un cliente de "Redes con IA" deja unos S/ 230 de caja al mes, y 3 a 4 clientes cubren los costos fijos (estimación, sin medir). Solutions necesita unos 143 negocios para lo mismo. Publisher es un **ingreso puente**, no el motor: no escala sin más personas.

La condición del CEO marca el encaje: Publisher no es una agencia más. **Cada servicio enseña al cliente a usar la IA.** Así acerca a la misión ("hacer fácil la tecnología y la IA para todos") y no la diluye.

**Valores que lo justifican:** Empatía Operativa (el dueño aprende con su propio negocio), Agilidad Real (se cobra desde el mes 1 sin construir software) y Robustez Invisible (doble confirmación antes de publicar).

## What Changes

- **Estado:** Yizi Publisher pasa de `incubacion` a `activo` en `satelites/registro.yaml`, con su repositorio `https://github.com/Yizi-Digital/yizi-publisher`.
- **IA en el centro:** cada servicio de Publisher incluye una lección corta en la que el cliente hace una pieza propia con IA. Es parte fija del servicio, no un extra.
- **Spec `satelites`:** se añade el requisito "Yizi Publisher activo con IA en el centro".
- **Catálogo inicial:** 4 servicios en escalera (de Jarvis), con precios propuestos por Edith. Ningún precio llega a un cliente sin la aprobación del CEO.
- **Flujo:** sin código propio, con herramientas oficiales de Meta y Google y doble confirmación humana por pieza (de Vision).
- **Frontera con Solutions:** la herramienta que el negocio usa cada día es de Solutions; el servicio que atrae y vende es de Publisher (de Karen).
- **Equipo:** Homer, líder N2 con nombre aprobado (2026-11-17), recibe su ficha. El resto del equipo de agentes queda **pendiente de la propuesta de Aida** (`estudio/aida-equipo-v2.md`), sin nombres en este cambio.
- **Génesis** del repositorio `yizi-publisher` desde la plantilla del núcleo (`/yizi-satelite`).
- **Organigrama:** `README.md`, `AGENTS.md`, `ceo/pendientes.md`, `agentes/mapa-de-agentes.md` y `talento/mapa-de-roles.md` al día.

### Orden de arranque (de Karen)

1. **Primero, los 3 pilotos de Solutions.** El CEO los hace él solo; Publisher no les quita horas.
2. En el Diagnóstico Flash de cada piloto se **anota** la necesidad de presencia digital, sin ofrecerla.
3. Mientras tanto, los agentes preparan el satélite: ficha de Homer, catálogo, precios y textos.
4. **Publisher arranca con 1 piloto propio**, de preferencia entre los clientes del Paquete Base, cuando el CEO lo decida con la evidencia de los pilotos.
5. Opción, no recomendación principal: usar Publisher primero como caso interno (las redes de Yizi).

### Capacidad

- **Supuesto de Edith:** el CEO da 10 horas por semana a Publisher. Quedan unas 30 horas productivas al mes.
- **Tope:** unos **6 clientes** equivalentes de "Redes con IA" mientras el CEO sea la única persona.
- El CEO confirma sus horas reales. Si cambian, Edith recalcula el tope.

## What Does Not Change

- Misión, visión y valores (spec `cultura`).
- Las reglas del núcleo: confirmación humana antes de publicar o cobrar, sin custodia de dinero de terceros (`marco-legal`), nombres internos ocultos ante clientes.
- Yizi Solutions sigue siendo la línea principal y su catálogo no se mueve, salvo lo que la frontera asigna a Publisher.
- Yizi Talent sigue en `incubacion`. Yizi Projects y el límite de un proyecto MACRO no cambian.
- No se contrata a nadie. El perfil humano de Termy queda como borrador.

## Capabilities

### New Capabilities
- Ninguna en el núcleo. Las specs de negocio de Publisher viven en su repositorio.

### Modified Capabilities
- `satelites`: se añade el requisito "Yizi Publisher activo con IA en el centro".

## Impact

- **Núcleo:** `satelites/registro.yaml`, `README.md`, `AGENTS.md`, `ceo/pendientes.md`, `agentes/mapa-de-agentes.md`, `talento/mapa-de-roles.md`, ficha de Jarvis (patrocina un satélite activo).
- **Satélite:** repositorio `Yizi-Digital/yizi-publisher` (ya creado vacío por el CEO). Se llena desde la plantilla; subir pide confirmación del CEO.
- **Costo (Edith, estimación):**
  - Activación: tope de **S/ 300 en 2 meses** (S/ 160 sin anuncios propios). Alarma a los S/ 250 sin clientes.
  - Costo fijo propio: S/ 75 al mes; S/ 425 con la parte administrativa del RUC.
  - IA: menos de S/ 5 por cliente al mes (niveles Ligero y Estándar, sin Avanzado ni Frontera en el servicio).
  - Horas del CEO: unas 10 horas para activar y de 1 a 5 horas por cliente al mes. Sin medir.
- **Bloqueo de cobro:** no hay primer cobro hasta que el contador confirme el RUC 10 (régimen, actividad de marketing digital y emisión electrónica).
- **Pauta:** el cliente paga los anuncios a Meta, directo, desde su propia cuenta. Yizi no recibe, no adelanta y no cobra un porcentaje de la pauta.

## Out of Scope

- Integración propia por API de Meta, Google o WhatsApp (fase 2, con un cambio aparte).
- Crear las fichas del equipo de agentes distinto de Homer: espera la propuesta de Aida y un cambio en el satélite.
- Publicar avisos o contratar al creador de contenido de barrio.
- Activar Yizi Talent.
- Publicar precios o textos comerciales hacia afuera.
