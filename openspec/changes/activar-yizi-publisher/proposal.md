# Proposal: Activar Yizi Publisher con la IA en el centro

| Campo | Valor |
|---|---|
| Dueño | V.I.E.R.N.E.S (Viernes) · CSO |
| Alcance | nucleo |
| Tipo | estrategico |
| Tamaño | L (cambio de estado de un satélite, gasto, varios dominios y una spec del núcleo) |
| Compuertas | Consejo completo (Vision, Jarvis, Edith, Viernes, Ultron) + aprobación del CEO |
| Aprobación | Pendiente. Pedido del CEO del 2026-11-18: "si va por ahí, activemos Yizi Publisher… pero no nos alejemos de la visión de incluir IA y hacer que todo el mundo la use". Decisiones ya tomadas por el CEO el 2026-11-18: nombres del equipo ("Está bien los nombres") y frontera ("que nuestra frontera y servicios actuales sean solo lo que podemos hacer con IA") |
| Insumos | `estudio/`: pedido del CEO, oferta de Jarvis (v2 vigente), economía de Edith, herramientas de Vision, equipo de Aida (v2 vigente), personas de Termy y frontera de Karen |

## Why

El CEO quiere ofrecer presencia digital, gestión de redes y ventas digitales. Ese servicio pertenece a Yizi Publisher, el frente del mercado, que hoy está en `incubacion`. Un satélite en incubación no puede ofrecerse a clientes (spec `satelites`). Por eso hace falta este cambio.

Publisher es la caja más rápida del grupo. Según Edith, un cliente de "Redes con IA" deja unos S/ 230 de caja al mes, y 3 a 4 clientes cubren los costos fijos (estimación, sin medir). Solutions necesita unos 143 negocios para lo mismo. Publisher es un **ingreso puente**, no el motor: no escala sin más personas.

La condición del CEO marca el encaje: Publisher no es una agencia más. **Cada servicio enseña al cliente a usar la IA.** Así acerca a la misión ("hacer fácil la tecnología y la IA para todos") y no la diluye.

**Valores que lo justifican:** Empatía Operativa (el dueño aprende con su propio negocio), Agilidad Real (se cobra desde el mes 1 sin construir software) y Robustez Invisible (doble confirmación antes de publicar).

## What Changes

- **Estado:** Yizi Publisher pasa de `incubacion` a `activo` en `satelites/registro.yaml`, con su repositorio `https://github.com/Yizi-Digital/yizi-publisher`. Su descripción y el rol de Homer se reescriben: "con la IA en el centro", "solo remoto" y "sin embudo en la fase 1".
- **`activo` no autoriza vender:** Publisher no ofrece ni cobra nada antes de cerrar el RUC 10, el contrato y la elección del piloto propio (tareas 8.1 a 8.3).
- **IA en el centro:** cada servicio de Publisher incluye una lección corta en la que el cliente hace una pieza propia con IA. Es parte fija del servicio, no un extra.
- **Frontera "solo con IA" (decisión del CEO, 2026-11-18):** Publisher solo ofrece lo que Yizi hace en remoto con IA, con el material que el cliente graba con su celular. Fotos, video, eventos e influencers en el local quedan **mapeados y no se ofrecen**. Si un cliente los pide, se registra una señal para Viernes.
- **Spec `satelites`:** se añade el requisito "Yizi Publisher activo con IA en el centro", con la frontera "solo con IA".
- **Catálogo inicial:** 5 servicios en escalera (`estudio/jarvis-oferta-v2.md`), con precios propuestos por Edith. Sale el embudo de ventas por WhatsApp: no hay embudo en la fase 1. Los precios son propuesta hasta tener 3 cotizaciones de Lima y la aprobación del CEO. Ningún precio ni texto comercial sale sin Edith y el CEO, ni antes de que Publisher esté activo.
- **Flujo:** sin código propio, con herramientas oficiales de Meta y Google y doble confirmación humana por pieza (de Vision). La aprobación del cliente es simple y funciona en el celular (WhatsApp o enlace corto). Cada aprobación queda registrada (quién, cuándo y qué versión). Hay un flujo de salida del cliente con lista firmada.
- **Frontera con Solutions:** la herramienta que el negocio usa cada día es de Solutions; el servicio que atrae y vende es de Publisher (de Karen).
- **Equipo (nombres aprobados por el CEO, `estudio/aida-equipo-v2.md`):** Homer, líder N2 (aprobado el 2026-11-17). Activos al arrancar, N3 bajo Homer (aprobados el 2026-11-18): Ágora (Community Manager), Faro (presencia local y reseñas), Quirón (El Guía Yizi en modo enseñar IA) y Prisma (diseño y video con IA). Diseñados, con disparador: Sagita (anuncios) y Kepler (medición). Las 5 fichas de arranque se crean en `yizi-publisher`.
- **Génesis** del repositorio `yizi-publisher` desde la plantilla del núcleo (`/yizi-satelite`).
- **Organigrama:** `README.md`, `AGENTS.md`, `ceo/pendientes.md`, `agentes/mapa-de-agentes.md` y `talento/mapa-de-roles.md` al día.

### Orden de arranque (de Karen)

1. **Primero, los 3 pilotos de Solutions.** El CEO los hace él solo; Publisher no les quita horas.
2. En el Diagnóstico Flash de cada piloto se **anota** la necesidad de presencia digital, sin ofrecerla.
3. **Punto de control:** Publisher no pasa a `activo` hasta terminar el Diagnóstico Flash del tercer piloto de Solutions.
4. Después de los pilotos, los agentes preparan el satélite: fichas de Homer, Ágora, Faro, Quirón y Prisma, catálogo, precios y textos. Si la ventana de 5 horas está justa, trabaja un agente a la vez.
5. **Publisher arranca con 1 piloto propio**, de preferencia entre los clientes del Paquete Base, cuando el CEO lo decida con la evidencia de los pilotos.
6. Opción, no recomendación principal: usar Publisher primero como caso interno (las redes de Yizi).

### Decisiones pendientes del CEO

| # | Decisión | Recomendación de Jarvis |
|---|---|---|
| 1 | ¿Se suma "Acompañamiento IA" (S/ 69 al mes, propuesta de Edith)? | Sí, solo como último escalón: para quien ya publica solo, nunca al inicio |
| 2 | ¿Los planes incluyen responder los mensajes del público? | No. El dueño responde; Yizi le da un banco de respuestas y le enseña a usar la IA |

### Capacidad

- **Supuesto de Edith:** el CEO da 10 horas por semana a Publisher. Quedan unas 30 horas productivas al mes.
- **Tope:** unos **6 clientes** equivalentes de "Redes con IA" mientras el CEO sea la única persona.
- El CEO confirma sus horas reales. **Recomendación de Ultron:** máximo 5 horas por semana hasta cerrar los pilotos de Solutions. Edith recalcula el tope con las horas confirmadas.
- El CEO anota los minutos reales de cada cliente desde el primer cliente.
- **Regla de pausa:** si el CEO pierde horas de Solutions, el trabajo de Publisher se pausa.

## What Does Not Change

- Misión, visión y valores (spec `cultura`).
- Las reglas del núcleo: confirmación humana antes de publicar o cobrar, sin custodia de dinero de terceros (`marco-legal`), nombres internos ocultos ante clientes.
- Yizi Solutions sigue siendo la línea principal y su catálogo no se mueve, salvo lo que la frontera asigna a Publisher.
- Yizi Talent sigue en `incubacion`. Yizi Projects y el límite de un proyecto MACRO no cambian.
- No se contrata a nadie. Los perfiles humanos de Publisher (creador de contenido de barrio, fotógrafo o videógrafo) quedan mapeados en `talento/mapa-de-roles.md` y no se ofrecen.

## Capabilities

### New Capabilities
- Ninguna en el núcleo. Las specs de negocio de Publisher viven en su repositorio.

### Modified Capabilities
- `satelites`: se añade el requisito "Yizi Publisher activo con IA en el centro".

## Impact

- **Núcleo:** `satelites/registro.yaml`, `README.md`, `AGENTS.md`, `ceo/pendientes.md`, `agentes/mapa-de-agentes.md`, `talento/mapa-de-roles.md`, ficha de Jarvis (patrocina un satélite activo).
- **Agentes:** el grupo pasa de 26 a 31 agentes activos (Homer y 4 N3). Con Sagita y Kepler llegaría a 33 (cifras de Aida).
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
- Activar a Sagita y Kepler: esperan su disparador (Aida, sección 2.3).
- Embudo de ventas por WhatsApp (fase 2, con API propia).
- Servicios presenciales: fotos, video, eventos o influencers en el local. Solo mapeados.
- Responder por el dueño los mensajes del público, salvo que el CEO decida lo contrario.
- Publicar avisos o contratar al creador de contenido de barrio.
- Activar Yizi Talent.
- Publicar precios o textos comerciales hacia afuera.
