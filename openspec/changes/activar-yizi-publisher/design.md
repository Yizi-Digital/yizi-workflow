# Design

## Context

Yizi Publisher está en `incubacion` desde el 2026-11-17, con Jarvis como patrocinador y Homer como líder con nombre aprobado y sin ficha. El CEO pidió activarlo para dar presencia digital, gestión de redes y ventas digitales, con una condición: la IA en el centro y el cliente aprendiendo a usarla. Siete estudios (`estudio/`) dan la base. El CEO es hoy la única persona de Yizi y hace él mismo los 3 pilotos de Solutions.

## Goals / Non-Goals

**Goals:**
- Pasar Publisher a `activo` con una oferta pequeña, medible y sin código propio.
- Hacer de la enseñanza de IA una parte fija de cada servicio.
- Proteger los 3 pilotos de Solutions y la caja del CEO.

**Non-Goals:**
- Construir integraciones por API (fase 2).
- Definir el equipo completo de agentes (lo propone Aida en `estudio/aida-equipo-v2.md`).
- Contratar personas.

## Decisions

### D1 · Catálogo inicial de 4 servicios en escalera — [Jarvis, Edith]

Todo servicio empieza con un Diagnóstico Flash único (ver D3). Cada servicio termina con una lección de 15 minutos: el cliente hace una pieza propia con IA.

| # | Servicio (Jarvis) | Qué aprende el cliente con IA | Precio con IGV (Edith) | Margen |
|---|---|---|---|---|
| 1 | Presencia Base (Google Business, WhatsApp Business con catálogo, un perfil ordenado) | Responder una reseña y describir un producto | **S/ 199**, pago único | 47.3 % |
| 2 | Contenido con IA (calendario y piezas para revisar) | Escribir la instrucción de su propia publicación | **S/ 159** al mes ("Redes con IA Inicio") | 49.2 % |
| 3 | Gestión mensual de redes | Una herramienta de IA nueva cada mes | **S/ 289** al mes ("Redes con IA") | 53.1 % |
| 4 | Embudo de ventas por WhatsApp (campaña pequeña y flujo) | Leer su tablero y decidir qué anuncio repetir | **S/ 129** al mes + **S/ 99** de alta ("Campañas") | 48.4 % |

- **Todos los precios son PROPUESTA de Edith.** El CEO los aprueba antes de que lleguen a un cliente. Jarvis consigue al menos 3 cotizaciones reales de Lima antes de publicarlos.
- Supuestos de Edith: costo de la hora de S/ 20, de 1 a 5 horas por cliente (estimación) y Canva a S/ 44.90 (no verificado).
- Una hora de más por cliente deja casi todos los planes bajo el 40 %. Cada plan tiene alcance cerrado y tope de horas. El CEO anota los minutos reales.
- Edith propone un escalón de salida, "Acompañamiento IA" (**S/ 69** al mes, margen 60 %), para el cliente que ya publica solo. Ver pregunta abierta 1.
- Se promete método y medición, no números. Sin métricas de vanidad.

*Alternativa descartada:* campañas pagadas como servicio suelto. Sin tope del cliente, el gasto se descontrola.

### D2 · Flujo sin código propio y con doble confirmación — [Vision]

1. Ficha del negocio (fuente única de datos).
2. Calendario del mes: la IA propone; una persona de Yizi ajusta.
3. Piezas con IA en estado "borrador".
4. Revisión de una persona de Yizi con una lista fija (precios, promesas, derechos, datos personales).
5. Aprobación del cliente, pieza por pieza, con registro de quién y cuándo.
6. Programación por una persona de Yizi en Meta Business Suite; publicación manual en Google.
7. Control al día siguiente: "publicado" o "falló" con aviso.

Reglas:
- Estados: `borrador → lista → aprobada → programada → publicada`. Una pieza editada vuelve a "lista".
- **Doble confirmación:** una persona de Yizi y el cliente. Ningún agente programa ni publica.
- Durante el piloto no hay lotes. Después, el CEO MAY aprobar un lote con plantilla, tope y fecha de fin.
- Yizi **no pide contraseñas**. Trabaja con acceso de socio en Meta y de administrador en Google.
- Prohibido: librerías no oficiales, bots, compra de seguidores o reseñas, mensajes sin permiso y scraping.
- **IA:** nivel Ligero (Haiku 5.5) y Estándar (Sonnet 5.5). Nunca Avanzado ni Frontera en el servicio. Respaldo si el modelo falla: plantillas fijas y trabajo manual. El texto de comentarios entra como dato, nunca como instrucción (OWASP LLM01:2025, según la ficha de Vision).
- Costo de IA: menos de S/ 5 por cliente al mes (estimación de Edith con precio de API verificado). Edith lo mide en el piloto.

*Alternativa descartada:* integración propia por API desde el inicio. La revisión de apps de Meta y el acceso a la API de Google no son automáticos, y no hay clientes que la paguen. Queda para la fase 2, con un cambio aparte.

### D3 · Frontera con Yizi Solutions — [Karen, Jarvis]

**Regla:** la herramienta que el negocio usa cada día es de Solutions. El servicio que Yizi opera para atraer o vender es de Publisher.

| Tema | Dueño |
|---|---|
| Caja, tablero, cuentas, inventario, menú QR, pedidos por WhatsApp | Solutions |
| Ficha de Google, perfil y catálogo de WhatsApp Business, redes, contenido, anuncios | Publisher |
| Fidelización por WhatsApp | Compartido: Solutions da la herramienta; Publisher diseña y opera las campañas |
| Contenido del menú (fotos y textos) | Publisher diseña; el flujo a cocina es de Solutions |

- **Un solo Diagnóstico Flash** pregunta por operación y por presencia. Se cobra una vez.
- **Derivación** con una ficha corta: el cliente no repite el diagnóstico.
- **Una factura** con dos líneas; Edith evita solapes. Lidera la relación el satélite que vendió primero.
- **Un solo catálogo de productos:** Publisher usa el bloque B03 de Solutions y no crea otra copia (Vision confirma en la fase 2).
- Ante el cliente solo existe El Guía Yizi y la marca Yizi Digital.

### D4 · Equipo de agentes — [Aida, Viernes]

- **Homer** (H.O.M.E.R), líder N2, nombre aprobado por el CEO el 2026-11-17. Recibe su ficha en el satélite, a partir del borrador de Aida. Reporta a Jarvis.
- **Resto del equipo:** pendiente de la propuesta de Aida (`estudio/aida-equipo-v2.md`). El CEO pidió un equipo de marketing completo y descartó los nombres del primer estudio. Este cambio no fija roles ni nombres.
- Reglas que ya aplican a todo el equipo: ningún agente publica, ningún agente accede a cuentas del cliente y ningún agente verifica lo que construyó (verifica Lince).

### D5 · Primer perfil humano — [Termy]

- **Creador de contenido de barrio:** graba en el local, produce con IA y enseña al dueño.
- Modalidad propuesta: locación de servicios por entregable. El pago lo fija Edith; el contrato lo revisa el abogado.
- Disparadores (propuesta de Termy, sin medir): un cliente pide fotos o videos en su local, o el dueño no aprende a usar la IA en remoto.
- **No se abre** hasta que Publisher esté activo y el CEO lo apruebe. No se duplica con el Promotor de barrio de Solutions: el Promotor vende el sistema; el creador produce y enseña.

### D6 · Dinero: tope de activación y pauta — [Edith]

- **Tope de activación: S/ 300 en 2 meses** (Canva, chip de WhatsApp y hasta S/ 140 de anuncios propios). Sin anuncios propios: S/ 160. Lo paga el CEO.
- Alarma: a los S/ 250 sin cliente firmado, Edith avisa y se paran los anuncios propios.
- **El cliente paga la pauta a Meta, directo,** desde su propia cuenta y su propio medio de pago. Yizi no recibe, no adelanta y no cobra un porcentaje (spec `marco-legal`).
- **Sin cobro** hasta que el contador confirme el RUC 10.

### D7 · Arranque y capacidad — [Viernes, Karen, Edith]

- Primero, los 3 pilotos de Solutions. Publisher arranca después con **1 piloto propio**.
- Tope: unos **6 clientes** equivalentes (30 horas al mes), con el supuesto de 10 horas por semana del CEO.
- Para crecer: pasar clientes al escalón de salida, dar talleres grupales o sumar una persona (Termy y Edith).

*Alternativa descartada:* abrir Publisher en paralelo a los pilotos. Quita horas al CEO y mezcla la medición del Paquete Base.

## Risks / Trade-offs

| Riesgo | Mitigación |
|---|---|
| Publisher quita horas a los pilotos de Solutions | Orden de Karen: pilotos primero, 1 piloto de Publisher después |
| El ingreso no escala (lineal en horas del CEO) | Tope de 6 clientes; escalón de salida; perfil humano con disparador |
| Una hora de más por cliente rompe el margen | Alcance cerrado, tope de horas y registro de minutos reales |
| Publisher se vuelve "agencia genérica" y diluye la marca | La lección de IA es parte fija de cada servicio; requisito en la spec `satelites` |
| El cliente aprende y se va | Escalera hacia el Acompañamiento IA; un cliente que se gradúa libera horas |
| Publicar un error a nombre del cliente | Doble confirmación por pieza y registro de aprobaciones |
| Bloqueo de la cuenta del cliente | Solo herramientas oficiales; nada de automatizaciones no oficiales |
| Promesas de resultados o datos falsos | Se promete método, no números; revisión contra la ficha del negocio |
| Reglas de negocio del satélite dentro del núcleo | El núcleo solo fija el estado y la regla de la IA; el catálogo y el flujo viven en `yizi-publisher` |

## Open Questions

1. ¿El catálogo inicial suma el "Acompañamiento IA" (S/ 69) como quinto escalón? Jarvis propone 4 servicios; Edith propone el escalón de salida. Deciden Jarvis, Edith y el CEO.
2. ¿Quién responde los mensajes y comentarios del cliente? Jarvis los incluye en la Gestión mensual; Edith los deja fuera para proteger el margen ("el dueño responde; Yizi le enseña"). Hay que elegir antes de fijar el precio.
3. ¿Cuántas horas por semana puede dar el CEO a Publisher? Define el tope real de clientes.
4. ¿Qué equipo de agentes propone Aida en `estudio/aida-equipo-v2.md` y con qué nombres?
5. Abogado: contrato de servicio, propiedad de cuentas y contenido, Ley 29733, DL 1044 y política de mensajes de WhatsApp (no verificada).
6. Contador: RUC 10 en el RMT, actividad de marketing digital y emisión electrónica.
7. ¿El plan de IA del CEO permite el uso para clientes? No verificado; Edith cuenta el costo de la API por prudencia.
8. Proveedor de imágenes con IA: costo, derechos y uso de datos. Lo decide Vision.
9. ¿Publisher arranca como caso interno (las redes de Yizi) antes del piloto externo?
