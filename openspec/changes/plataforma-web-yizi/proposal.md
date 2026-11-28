# Proposal: Plataforma web de Yizi Digital

| Campo | Valor |
|---|---|
| Dueño | J.A.R.V.I.S (Jarvis) · CDO |
| Alcance | nucleo |
| Tipo | marca-comunicacion (con efecto comercial) |
| Tamaño | L (cara pública del grupo; toca marca, técnica, finanzas, estrategia y legal; gasto recurrente pequeño) |
| Compuertas | Consejo completo (Vision, Jarvis, Edith, Viernes, Ultron) + abogado colegiado antes de publicar + confirmación del CEO |
| Aprobación | Pendiente. Pedido del CEO del 2026-11-28 (`estudio/pedido-del-ceo.md`): una plataforma "como las de Tesla o Apple, súper robusta", que venda a inversionistas y a clientes |
| Insumos | `estudio/`: pedido del CEO, narrativa de Jarvis, arquitectura de Vision, encaje de Viernes y costo de Edith |

## Why

Yizi no tiene hoy una cara pública. El CEO empieza los pilotos de Solutions y habla con inversionistas. Una web clara da confianza al dueño de un negocio que recibe un enlace por WhatsApp. También da un lugar donde el inversionista lee la tesis y la etapa real.

La web debe vender sin mentir. Hoy solo Solutions está activo y aún no tiene pilotos cerrados. Publisher y Talent están en incubación. Projects no tiene un proyecto autorizado en marcha. Una etapa temprana contada con claridad vende más que una promesa inflada.

**Valores que lo justifican:** Empatía Operativa (una web que el bodeguero entiende en su celular), Robustez Invisible (rápida y accesible sin que nadie lo note) y Agilidad Real (se publica primero lo que está listo).

## What Changes

- **Repositorio propio** `Yizi-Digital/yizi-web` (lo crea el CEO). Es un canal de la marca madre, no un satélite. El plan y las decisiones viven en este cambio del núcleo.
- **Stack:** Astro estático con islas de React. Es una desviación del stack por defecto (React + Vite), justificada por Vision en `design.md` (D2). Plan B: React + Vite pre-renderizado.
- **Metas medibles:** Lighthouse de 95 o más en celular, WCAG 2.2 AA, LCP de 2,5 s o menos. Si una prueba automática falla, el PR no se fusiona.
- **Nueva spec `presencia-web`** (delta ADDED): reglas de contenido, estados de cada línea, datos, analítica, calidad y salida a producción. Justificación en `design.md` (D1).
- **Reglas de contenido** (detalle en `design.md`, D4): solo se vende Solutions, sin precios ni pagos hasta Izipay y el contador. Publisher y Talent van como "Próximamente". Los productos propios van como visión, sin nombres internos. A inversionistas se les dice "etapa temprana", sin cifras ni proyecciones. Sin nombres de agentes. Fiesteros solo con permiso escrito. Trato de usted.
- **Formulario sin base de datos**, con consentimiento y sin cookies de terceros en la analítica.
- **Producción solo con la confirmación del CEO**, después de Lince y del abogado.
- **Sin chat con IA en la v1.**

## Opciones de alcance (decide el CEO)

El CEO pidió algo "súper robusto, estilo Apple o Tesla, que venda a inversionistas y a clientes". Hay dos caminos.

| | A · Sitio completo de 9 páginas, por fases (Jarvis) | B · v1 de una sola página, y crecer después (Viernes) |
|---|---|---|
| Qué es | Inicio (7 pantallas), Solutions, Publisher, Projects, Talent, Inversionistas, Nosotros, Contacto y Legales. Se construye por fases y se publica primero lo que está listo | Una página con 7 secciones: portada, Solutions, cuatro frentes, cómo trabajamos, inversionistas, contacto y pie legal |
| Qué se ve al inicio | Lo mismo que B: la primera salida (fases 1 a 3) cubre el contenido de B | Lo esencial, nada más |
| Impresión "Apple o Tesla" | Alta: una página por idea, sistema de diseño completo | Media: una sola página larga con mucho aire |
| Riesgo | Páginas casi vacías para Publisher y Talent, que no venden nada hoy. Más textos que revisar y que mantener | Quedarse corto ante un inversionista que espera ver cada línea |
| Horas del CEO (Edith) | Unas 7 h en dos semanas, más 1,5 h por ronda extra | Menos que A. Edith no la estimó por separado |
| Foco del CEO | Se protege si las páginas de líneas sin oferta salen después | Se protege mejor |
| Cómo crece | Se publica por fases sin rehacer nada | Se divide en páginas cuando haya motivo (pilotos, Publisher activo) |

**Recomendación de Jarvis: A, pero por fases y con la regla "se publica primero lo listo".** El mismo trabajo técnico (fases 1 a 3) entrega primero la versión de B: Inicio, Solutions, estados de las líneas, Inversionistas, Contacto y Legales. Las páginas de Publisher, Projects, Talent y Nosotros salen cuando estén aprobadas, sin frenar la primera salida. Así el CEO tiene la sensación de plataforma que pidió, sin vitrinas vacías. Si el CEO prefiere B, se hace solo con las tareas 3.1 a 3.3 y 3.6, y el resto queda para un cambio posterior.

Viernes pide B por foco: los 3 pilotos son la prioridad. La recomendación A respeta ese foco porque la primera salida es la de B y el resto espera su turno. La decisión es del CEO.

## Lo que queda fuera

- Precios, pagos en línea, cuentas de usuario y chat con IA.
- Publisher, Talent y los productos propios como oferta.
- Cifras de mercado, proyecciones, clientes, logos o testimonios.
- Lista de espera de Publisher (recoge datos personales sin servicio que prometer). Se decide en un cambio posterior.
- Inglés y formulario completo: fases 4 y 5, después de la primera salida.

## Impact

- Specs: nueva `presencia-web`. No cambia `comunicacion` ni `arquitectura`; las cita.
- Documentos: corregir la sección 6.4 del manual de marca (dice que no hay proyectos MACRO y el registro ya tiene dos). Es un cambio de marca aparte (tarea 1.5).
- Dinero: gasto nuevo mínimo (dominio .com y un buzón de correo). Los precios no están verificados; ver `estudio/edith-costo.md`.
- Horas del CEO: unas 7 (estimación de Edith, sin dato histórico).
