# Design

## Context

El CEO pidió el 2026-11-28 una plataforma web del grupo que venda a inversionistas y a clientes. Los cinco estudios de `estudio/` dan la base: narrativa (Jarvis), arquitectura (Vision), encaje (Viernes) y costo (Edith). Estado real hoy: Solutions `activo` sin pilotos cerrados; Publisher y Talent en `incubacion`; Projects `activo` sin proyecto MACRO autorizado en marcha. Yizi opera como persona natural con negocio (RUC 10); no hay empresa constituida. El CEO es la única persona de Yizi.

## Goals / Non-Goals

**Goals:**
- Una web rápida, accesible y sobria que cuente la verdad del grupo.
- Vender Solutions con una invitación a un Diagnóstico Flash.
- Dar al inversionista la tesis y la etapa real, sin cifras.

**Non-Goals:**
- Vender Publisher, Talent o productos propios.
- Mostrar precios, pagos, cuentas de usuario o chat con IA.
- Guardar datos de visitantes en una base de datos.

## Decisions

### D1 · Capacidad del delta: spec nueva `presencia-web` — [Jarvis]

`comunicacion` trata del tono, la identidad y la aprobación de textos. La web suma otras cosas: estados de cada línea, datos del visitante, analítica, metas técnicas y salida a producción. Si todo entra en `comunicacion`, esa spec pierde foco y mezcla marca con técnica. `arquitectura` es de Vision y no debe cargar con reglas de contenido. Una spec nueva, de Jarvis, con Vision en lo técnico, deja cada tema en su dueño. Las demás specs se citan, no se copian. Las futuras páginas o canales públicos (por ejemplo, la web de un producto propio) pueden pedir su delta aparte.

### D2 · Stack: Astro estático con islas de React — [Vision]

Desviación de la spec `arquitectura` (React + Vite por defecto), con la justificación que ella exige. Fuente: `estudio/vision-arquitectura.md`, sección 2.1.

| Opción | Sin JavaScript | Celular con red lenta | Veredicto |
|---|---|---|---|
| A. React + Vite (SPA) | No: sale en blanco | Bajo | Descartada. Es el fallo visto en la web de Fiesteros |
| B. React + Vite pre-renderizado | Sí | Bueno, pero carga React en cada página | **Plan B** si Astro falla |
| **C. Astro (usa Vite) + React en islas** | **Sí** | **El mejor: 0 KB de JavaScript sin interacción** | **Elegida** |
| D. Next.js | Sí | Más pesado para un sitio de contenido | Descartada |

Riesgo: Cloudflare compró la empresa de Astro el 2026-01-16 y dijo que sigue de código abierto (blog de Astro y nota de Cloudflare, consultados por Vision el 2026-11-28). Mitigación: salida estática, sin dependencia de un proveedor. Si hace falta salir, el HTML, el CSS y los componentes React pasan a la opción B. La aprueba el CEO (tarea 0.6).

### D3 · Repositorio y despliegue — [Vision, Edith]

1. Código en `Yizi-Digital/yizi-web`, creado por el CEO. Recomendación de Vision: público, porque el sitio es público y la protección de rama es gratis en repos públicos (no verificado hoy). Los borradores para inversionistas no entran al repo hasta que el CEO los apruebe.
2. Alojamiento en Vercel con un equipo de Yizi de plan Pro (el plan gratis es solo no comercial). El precio no está verificado; Edith lo confirma. Un solo equipo para Publisher y la web.
3. Vistas previas por PR, protegidas y sin indexar (se verifica al crear el proyecto).
4. Producción: solo el CEO fusiona en `main` o lo confirma, cada vez. Ningún agente despliega ni conecta el dominio. Se puede volver a la versión anterior con confirmación del CEO.

### D4 · Reglas de contenido — [Jarvis, Viernes]

| Tema | Regla |
|---|---|
| Solutions | Es lo único que se vende. Llamada a la acción: pedir un Diagnóstico Flash. Sin precios, tramos ni pagos hasta que Edith valide y se cierren Izipay (RUC 10) y el contador |
| Publisher y Talent | "Próximamente". Una idea de misión, sin servicios, planes, precios ni fechas |
| Productos propios | Solo la visión. Sin nombres de proyectos (toFinance y plan de comidas no se nombran), capturas ni fechas |
| Inversionistas | Tesis, etapa temprana dicha con claridad y "conversemos". Sin montos, porcentajes, proyecciones ni cifras de mercado sin fuente y fecha |
| Agentes | Sin nombres internos. Se puede decir "agentes de IA" y "una persona aprueba cada decisión importante". Ante el público existe El Guía Yizi, que no tiene chat en la v1 |
| Casos | Sin clientes, logos ni testimonios. Fiesteros solo con permiso escrito del cliente y como caso de portafolio |
| Trato | De usted, con clientes e inversionistas (decisión del CEO, 2026-11-20) |
| Promesas | De método, no de cifras. Sin "líder", "el mejor" ni garantías |
| Estados | Etiquetas visibles: "Activo", "Próximamente", "En exploración". El estado sale de `satelites/registro.yaml`, no de un texto escrito a mano. Vision decide cómo se conecta |
| Contacto | WhatsApp Business y correo del negocio. Nunca el celular personal del CEO |
| Datos pendientes | Todo `[dato pendiente]` de la narrativa se resuelve antes de publicar o se quita |

### D5 · El nombre "Yizi Projects" en público — [Jarvis]

**Decisión de Jarvis (la confirma el CEO):** la web llama al frente "Productos propios de Yizi" y no usa el nombre "Yizi Projects". El manual (6.4) dice que ese nombre es interno y que cada producto sale con su marca. Así se respeta el manual sin cambiarlo. Los otros tres frentes sí llevan el nombre de su línea. La narrativa de Jarvis lo usaba; se corrige antes de construir (tarea 2.1). Si el CEO prefiere mostrar "Yizi Projects", hace falta un cambio de marca aparte que ajuste la sección 6.4. Además, la sección 6.4 del manual dice que no hay proyectos MACRO y el registro ya tiene dos. El registro manda; se corrige en un cambio de marca aparte (tarea 1.5).

### D6 · Calidad visual y metas — [Vision, Jarvis]

El nivel "Apple o Tesla" se logra con orden, espacio, tipografía y buenas imágenes, no con librerías pesadas. Sin copiar su marca ni su diseño.

| Meta | Valor |
|---|---|
| Lighthouse en celular (rendimiento, accesibilidad, buenas prácticas, SEO) | 95 o más en cada página, mediana de 3 corridas |
| LCP / CLS | 2,5 s o menos / 0,1 o menos |
| INP | 200 ms o menos, con datos reales cuando haya tráfico |
| JavaScript | 0 KB sin interacción; 50 KB comprimido como máximo por página |
| Primera vista de la portada en celular | 600 KB o menos |
| Accesibilidad | WCAG 2.2 AA: axe sin fallos más lista manual (teclado, 24 × 24 px, lector de pantalla, 200 % de zoom) |
| Sin JavaScript | Se leen los textos y se usa el menú |
| Celular | De 360 a 430 px sin desplazamiento horizontal; prueba en celular real con red lenta |
| Seguridad | Cabeceras con nota A o mejor en HTTP Observatory; gitleaks y `npm audit` en cada PR |

Reglas visuales: paleta y tipografías del manual, alojadas en el sitio, sin Google Fonts. **El Ámbar nunca va como texto sobre fondo claro** (contraste de 2,15:1 sobre blanco, calculado por Vision): solo como fondo de botón con texto Índigo (4,82:1) o sobre fondo Índigo. Movimiento con propósito, apagado con `prefers-reduced-motion`. Imágenes propias o con licencia comercial; maquetas marcadas como maqueta. Los umbrales de rendimiento son los "buenos" de web.dev y los presupuestos de peso son propuesta de Vision. WCAG 2.2: texto oficial no revisado.

### D7 · Datos: formulario sin base de datos y analítica sin cookies de terceros — [Vision, abogado]

1. Lanzamiento: botón de WhatsApp (`wa.me`) y `mailto:`. No pasan datos por la web.
2. Formulario (fase 4): recibe y reenvía por correo; no guarda nada. Pide lo mínimo: nombre, contacto, tipo de negocio, línea de interés y mensaje. Nunca DNI, datos bancarios ni de salud.
3. Casilla de consentimiento sin marcar, validada también en el servidor. Aviso de privacidad redactado como borrador y revisado por abogado colegiado (Ley 29733).
4. Si falla el correo, el visitante ve un aviso claro y el botón de WhatsApp. El error se registra sin datos personales.
5. Anti-spam en niveles: campo trampa, tiempo mínimo y límite por red. Un desafío de terceros solo con su propio análisis de privacidad.
6. Analítica: Vercel Web Analytics y Speed Insights, que según Vercel no usan cookies de terceros (documentación vista el 2026-11-28; el abogado lo confirma). Sin Google Analytics ni píxeles. Ningún evento lleva datos personales.
7. El buzón que recibe contactos funciona como banco de datos. El abogado decide si se inscribe antes de lanzar el formulario.

### D8 · Qué revisa el abogado antes de publicar — [Viernes, abogado]

Ninguna norma de esta lista está verificada en su texto oficial. El abogado confirma qué aplica (spec `marco-legal`). Todo texto legal va marcado "requiere revisión de abogado colegiado".

1. Datos del proveedor que debe mostrar la web (RUC 10, sin domicilio personal) y si conviene constituir la empresa antes de buscar inversión.
2. Privacidad, consentimiento e inscripción del banco de datos (Ley 29733 y D.S. 016-2024-JUS).
3. Libro de Reclamaciones virtual: si aplica a una web que solo invita a conversar (Ley 29571).
4. Qué se puede decir a inversionistas sin que parezca oferta pública de valores.
5. Aviso por el uso de IA.
6. Registro de la marca "Yizi" ante Indecopi antes de lanzar.
7. Promesas de la portada y de Solutions (publicidad engañosa).

### D9 · Costo y horas — [Edith]

Fuente: `estudio/edith-costo.md`. Casi ningún precio de proveedor está verificado; no se pone cifra en soles o dólares hasta confirmarlo.

| Partida | Propuesta |
|---|---|
| Dominio .com | Uno, en el registrador de renovación más barata. El CEO compara 2 o 3. El .pe queda para después |
| Hosting | Equipo de Vercel compartido con Publisher; precio por confirmar |
| Correo | Un buzón con alias (`contacto@`, `inversionistas@`, `clientes@`); confirmar si los alias son gratis |
| Imágenes, banco de fotos, herramientas de pago | USD 0. Material propio o bancos gratuitos con licencia comercial |
| IA | Dentro del plan del CEO. Sin gasto extra: si la ventana de 5 horas se agota, se espera |
| Horas del CEO | Unas 7 en dos semanas (estimación, sin dato histórico); 1,5 h por ronda extra |
| Tope | El costo de un dominio .com y un buzón. El CEO lo fija con cotizaciones. Cambiarlo requiere nueva estimación de Edith |

Hoy no se muestra ninguna cifra financiera en la web. Si el CEO quiere una, trae la fuente; Edith la revisa y se publica con fuente y fecha.

### D10 · Fases y verificación — [Ultron, Vision, Lince]

Las fases van de 0 (preparación del CEO) a 6 (producción), como en `tasks.md`. Construye Vision con ejecutores N4 de nivel Estándar. Verifica Lince en cada fase; quien construye no verifica. Modelos: Sonnet para construir, Haiku para lo mecánico, nunca Fable. Las fases 1 a 3 forman la primera versión publicable. El formulario y el inglés salen después sin rehacer nada.

## Risks / Trade-offs

| Riesgo | Mitigación |
|---|---|
| Web ambiciosa sin producto ni clientes pierde credibilidad | Etapa temprana dicha con claridad; se publica primero lo listo |
| Una promesa se lee como garantía | Textos de método, sin cifras; revisión de Jarvis, Viernes y abogado |
| Se publica antes de la revisión legal | Fase 6 exige la lista firmada por Lince y el visto bueno del abogado |
| RUC 10 y datos personales del CEO quedan expuestos | Solo lo que el abogado indique; contacto del negocio |
| Marca "Yizi" sin registrar | Se revisa antes de lanzar (D8) |
| Astro cambia de rumbo | Salida estática y plan B |
| La web quita horas a los pilotos | Revisión por bloques; la web se pausa si el CEO pierde horas de Solutions |
| Precios de proveedores sin verificar | Edith confirma antes de pagar |

## Open Questions

Las decisiones del CEO están en `consejo.md`, en orden de prioridad.
