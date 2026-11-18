# Design

## Context

Yizi Publisher está en `incubacion` desde el 2026-11-17, con Jarvis como patrocinador y Homer como líder con nombre aprobado y sin ficha. El 2026-11-18 el CEO aprobó los nombres del equipo y fijó la frontera: solo lo que Yizi hace en remoto con IA. El CEO pidió activarlo para dar presencia digital, gestión de redes y ventas digitales, con una condición: la IA en el centro y el cliente aprendiendo a usarla. Los estudios de `estudio/` dan la base; para la oferta y el equipo valen las versiones 2 (`jarvis-oferta-v2.md` y `aida-equipo-v2.md`). El CEO es hoy la única persona de Yizi y hace él mismo los 3 pilotos de Solutions.

## Goals / Non-Goals

**Goals:**
- Pasar Publisher a `activo` con una oferta pequeña, medible y sin código propio.
- Hacer de la enseñanza de IA una parte fija de cada servicio.
- Proteger los 3 pilotos de Solutions y la caja del CEO.

**Non-Goals:**
- Construir integraciones por API (fase 2).
- Activar a Sagita y Kepler antes de su disparador.
- Ofrecer servicios presenciales o contratar personas.

## Decisions

### D1 · Catálogo inicial de 5 servicios en escalera — [Jarvis, Edith]

Fuente: `estudio/jarvis-oferta-v2.md`, que reemplaza al catálogo de la v1. Todo servicio empieza con un Diagnóstico Flash único (ver D3). Cada servicio termina con una lección de 15 minutos: el cliente hace una pieza propia con IA.

| # | Servicio (Jarvis) | Qué aprende el cliente con IA | Precio con IGV (Edith) | Margen |
|---|---|---|---|---|
| 1 | Presencia básica (Google, WhatsApp Business con catálogo, Facebook e Instagram ordenados), pago único | Responder una reseña y describir un producto | **S/ 199** | 47.3 % |
| 2 | Redes con IA Inicio (1 red, 4 publicaciones y 4 historias) | Escribir su propia instrucción y corregir el borrador | **S/ 159** al mes | 49.2 % |
| 3 | Redes con IA (2 redes, 8 publicaciones y 8 historias) | Una herramienta de IA nueva cada mes | **S/ 289** al mes | 53.1 % |
| 4 | Campañas (complemento de un plan de redes; 1 campaña en Meta) | Leer su informe y decidir qué anuncio repetir | **S/ 129** al mes + **S/ 99** de alta | 48.4 % |
| 5 | Acompañamiento IA (1 hora al mes; el dueño publica solo) | Crear y programar solo, con revisión de Yizi | **S/ 69** al mes | 60 % |

- **Todos los precios son PROPUESTA de Edith.** El CEO los aprueba antes de que lleguen a un cliente. Jarvis consigue al menos 3 cotizaciones reales de Lima antes de publicarlos.
- **El servicio 5 espera la decisión del CEO** (pregunta abierta 1). Recomendación de Jarvis: solo como último escalón, nunca al inicio, con 3 mejoras por escrito al mes.
- **El servicio 4 no se vende** hasta que el CEO y Edith lo aprueben; su primer cliente es el disparador de Sagita (D4).
- **Sin embudo de ventas por WhatsApp en la fase 1.** Pide API propia (Vision) y toca la frontera con Solutions.
- **Ningún plan incluye responder los mensajes del público** mientras el CEO no decida (pregunta abierta 2). Cada plan entrega un banco de respuestas y una plantilla de IA; el dueño responde.
- Supuestos de Edith: costo de la hora de S/ 20, de 1 a 5 horas por cliente (estimación) y Canva a S/ 44.90 (no verificado).
- Una hora de más por cliente deja casi todos los planes bajo el 40 %. Cada plan tiene alcance cerrado y tope de horas. El CEO anota los minutos reales.
- Se promete método y medición, no números. Sin métricas de vanidad.

*Alternativa descartada:* campañas pagadas como servicio suelto. Sin tope del cliente, el gasto se descontrola.

### D1b · Frontera "solo con IA" — [CEO, Jarvis, Termy]

**Decisión del CEO (2026-11-18):** "que nuestra frontera y servicios actuales sean solo lo que podemos hacer con IA".

- Publisher trabaja **solo en remoto y con IA**. El cliente graba con su celular y envía el material; la IA crea o edita las piezas.
- La guía "Graba así con tu celular" (Jarvis) explica al cliente cómo enviar fotos y videos.
- La sesión de enseñanza es por videollamada. No hay visitas al local.
- **Mapeado, no se ofrece:** fotos y video en el local, cobertura de eventos e influencers presenciales. Los perfiles humanos (creador de contenido de barrio, fotógrafo o videógrafo) están en `talento/mapa-de-roles.md`.
- Si un cliente lo pide, Yizi lo dice con claridad, no inventa plazos ni precios y registra una **señal para Viernes**.
- Activar un servicio presencial pide su propio cambio OpenSpec, el perfil de Termy, el costo de Edith y la aprobación del CEO.

*Alternativa descartada:* ofrecer fotos en el local desde el inicio. Yizi no tiene hoy ese talento y prometerlo sería una oferta falsa.

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

Fuente: `estudio/aida-equipo-v2.md`. Nombres aprobados por el CEO: Homer el 2026-11-17; el resto el 2026-11-18.

| Agente | Rol | Nivel | Estado |
|---|---|---|---|
| H.O.M.E.R (Homer) | Líder de Publisher; reporta a Jarvis | N2 | Al activar |
| Á.G.O.R.A (Ágora) | Community Manager: calendario, textos y respuestas sugeridas | N3 | Al arrancar |
| F.A.R.O (Faro) | Presencia local: Google, WhatsApp Business y reseñas | N3 | Al arrancar |
| Q.U.I.R.O.N (Quirón) | El Guía Yizi en modo enseñar IA (agente del producto) | N3 | Al arrancar, versión mínima sin IA en vivo |
| P.R.I.S.M.A (Prisma) | Diseño y video con IA, con el material del cliente | N3 | Al arrancar |
| S.A.G.I.T.A (Sagita) | Anuncios pagados | N3 | Con disparador: primer cliente de Campañas aprobado por el CEO y Edith |
| K.E.P.L.E.R (Kepler) | Medición de marketing | N3 | Con disparador: junto con Sagita o con 10 clientes activos |

- Las fichas de Homer, Ágora, Faro, Quirón y Prisma se crean en `yizi-publisher/.claude/agents/`. Sagita y Kepler quedan diseñados, sin ficha activa.
- Hasta su disparador, Homer cubre esas tareas con agentes N4 de nivel Ligero, o el servicio no se vende.
- Con la activación, el grupo pasa de 26 a 31 agentes activos (cifras de Aida).
- Reglas para todo el equipo: ningún agente publica, paga ni entra a las cuentas del cliente. Ningún agente verifica lo que construyó (verifica Lince). Ante clientes, la identidad es El Guía Yizi.
- Quirón debe quedar cubierto por el cambio de `jerarquia-agentes` sobre agentes del producto, que lleva Ultron.

### D5 · Personas: solo mapeadas — [Termy]

- Hoy el CEO hace lo que un agente no debe hacer: revisa y programa cada pieza, es el contacto del cliente y da la sesión por videollamada.
- **Creador de contenido de barrio, fotógrafo y videógrafo:** perfiles futuros, mapeados en `talento/mapa-de-roles.md`. No se ofrecen hoy: sin aviso, sin contacto y sin contratación.
- Disparadores (propuesta de Termy, sin medir): clientes que piden fotos o videos en su local (D1), o un dueño que no usa la IA solo tras la capacitación remota (D4).
- Si entra una persona, Prisma sigue siendo dueño de la edición; la persona solo graba.

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
| Un cliente pide fotos o video en su local | Se dice que hoy no se ofrece y se registra una señal para Viernes |
| Publicar un error a nombre del cliente | Doble confirmación por pieza y registro de aprobaciones |
| Bloqueo de la cuenta del cliente | Solo herramientas oficiales; nada de automatizaciones no oficiales |
| Promesas de resultados o datos falsos | Se promete método, no números; revisión contra la ficha del negocio |
| Reglas de negocio del satélite dentro del núcleo | El núcleo solo fija el estado y la regla de la IA; el catálogo y el flujo viven en `yizi-publisher` |

## Open Questions

1. **Decisión del CEO pendiente.** ¿Se suma "Acompañamiento IA" (S/ 69)? Jarvis recomienda sí, solo como último escalón y nunca al inicio.
2. **Decisión del CEO pendiente.** ¿Los planes incluyen responder los mensajes del público? Jarvis recomienda no: el dueño responde y Yizi le enseña. Un complemento "Bandeja de mensajes" queda como idea futura, sin precio.
3. ¿Cuántas horas por semana puede dar el CEO a Publisher? Define el tope real de clientes.
4. Resuelta (2026-11-18): el CEO aprobó los nombres del equipo de Aida.
5. Abogado: contrato de servicio, propiedad de cuentas y contenido, Ley 29733, DL 1044 y política de mensajes de WhatsApp (no verificada).
6. Contador: RUC 10 en el RMT, actividad de marketing digital y emisión electrónica.
7. ¿El plan de IA del CEO permite el uso para clientes? No verificado; Edith cuenta el costo de la API por prudencia.
8. Proveedor de imágenes con IA: costo, derechos y uso de datos. Lo decide Vision.
9. ¿Publisher arranca como caso interno (las redes de Yizi) antes del piloto externo?
