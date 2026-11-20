# Fiesteros · Economía del cliente · Estudio de Edith

| Campo | Valor |
|---|---|
| Autora | Edith (CFO) |
| Alcance | `yizi-publisher` (en estudio, desde el núcleo) |
| Fase | 0 · Explorar, parte financiera |
| Estado | Borrador para el CEO. **Contiene precios internos.** Ningún precio llega al cliente sin la aprobación del CEO (spec `finanzas`). |
| Insumos | `fiesteros/pedido-del-ceo.md`, `../edith-economia.md` (precios y fórmula de Publisher), `../jarvis-oferta-v2.md` (catálogo), `yizi-solutions/catalogo/economia.md` (v4, IGV, comprobantes, RMT) |
| Fecha | 2026-11-18 |

## Respuesta corta

1. **Los costos de la web (dominio y plataforma) los paga el cliente, a su nombre y con su medio de pago.** Yizi trabaja con acceso de administrador o de socio, nunca como dueño ni con contraseñas.
2. **El catálogo de Publisher no tiene un servicio de mantenimiento de web.** Propongo dos: **Web al día a S/ 69 al mes** (1 hora) y **Web al día Plus a S/ 119 al mes** (2 horas). Ambos superan el margen mínimo de 40 %.
3. **Si el cliente hoy no paga**, propongo pasar a un plan en 4 pasos: ordenar la propiedad de las cuentas, un mes de transición sin cobro, un precio de cliente fundador de S/ 49 por 3 meses y luego el precio normal.
4. **No hay primer cobro hasta que el contador confirme el RUC 10** (régimen, actividad y emisión electrónica). Es el mismo bloqueo de Publisher y Solutions.
5. **No sé casi nada del negocio del cliente.** Las preguntas están en la sección 4.

> Esto no es asesoría tributaria ni legal. El contador y el abogado confirman cada punto antes de facturar o firmar.

---

## 0. Estado de las fuentes

| Dato | Estado | Fuente |
|---|---|---|
| Plataforma de fiesteros.shop (tienda en línea, hosting propio u otra) | **No verificado.** La web no abrió en la red de esta sesión (bloqueo del proxy) | Pregunta para el CEO |
| Precio de renovación de un dominio `.shop` | **Visto en buscador. No verificado** en el registrador | Comparadores de precios, consultados el 2026-11-18 (ver Fuentes) |
| Quién es dueño del dominio, del hosting y de las redes | **No se sabe** | Pregunta para el CEO (`pedido-del-ceo.md`) |
| Si el cliente paga algo hoy | **No se sabe** | Pregunta para el CEO |
| Fórmula de precio, C_h de S/ 20, Izipay 3.44 %, IGV 18 % | Igual que `../edith-economia.md` §3.1 | Ver ese estudio |
| Tipo de cambio venta 3.419 | **Verificado** | SUNAT, 17/11/2026 (`economia.md` §0) |
| Comprobantes: boleta o factura electrónica | **Verificado** como regla general; aplicación al RUC del CEO: **no verificada** | `economia.md` §4.5. Lo confirma el contador |

---

## 1. Costos recurrentes de una web así y quién los paga

### 1.1 Costos probables

No sé en qué plataforma está la web. Por eso doy los tipos de costo, y solo pongo cifra donde tengo una fuente.

| Costo | Frecuencia | Monto | Estado |
|---|---|---|---|
| Renovación del dominio `fiesteros.shop` | Anual | **USD 29 a USD 60 al año** según el registrador (unos **S/ 99 a S/ 205** con TC 3.419). Promedio de mercado citado: USD 48.21 (unos S/ 165) | **Visto en buscador. No verificado.** El precio real es el del registrador donde está el dominio |
| Plataforma o hosting | Mensual o anual | **Sin cifra.** Depende de la plataforma: tienda en línea por suscripción, hosting compartido o hosting gratis para webs simples | **Pregunta para el CEO:** ¿dónde está alojada la web y cuánto se paga hoy? |
| Certificado de seguridad (el candado HTTPS) | Anual o incluido | Sin cifra. Muchas plataformas lo incluyen | **No verificado.** Lo confirma Vision al ver la plataforma |
| Correo con el dominio (si existe) | Mensual o anual | Sin cifra | **Pregunta para el CEO:** ¿hay correos @fiesteros.shop? |
| Comisión de pagos en la web (si vende en línea) | Por venta | Sin cifra. Depende de la pasarela del cliente | **Pregunta para el CEO:** ¿la web cobra o solo muestra productos? |
| Páginas de Facebook e Instagram | — | S/ 0 en el uso común | **No verificado** en esta sesión |
| Anuncios en Meta (si los hay) | Según el cliente | Lo decide el cliente | Regla de `marco-legal`: el cliente paga a Meta directo |

### 1.2 Quién paga: siempre el cliente, a su nombre

| Situación | ¿Se permite? | Qué hacer |
|---|---|---|
| Dominio, plataforma y redes a nombre del cliente, pagados con su tarjeta. Yizi tiene acceso de administrador o de socio | **Sí. Es el modelo correcto** | Mantenerlo |
| Dominio o hosting a nombre del CEO, pagados por el cliente | **No conviene** | Transferir la titularidad al cliente antes de la próxima renovación |
| Dominio o hosting pagados con la tarjeta del CEO y luego cobrados al cliente | **No** | Yizi financiaría al cliente y movería su dinero (spec `marco-legal`). Además, el IGV de un servicio del exterior quedaría a nombre del CEO (`economia.md` §4.4) |
| Yizi paga y lo suma a su honorario como "todo incluido" | **No al inicio** | Mezcla costos del cliente con el ingreso de Yizi. El honorario de Yizi cubre solo horas |
| Yizi guarda las contraseñas del cliente | **No** | Permisos mínimos (Vision). Acceso con usuario propio de Yizi |

**Por qué importa:** si el cliente deja Yizi, se lleva su web y sus redes sin depender del CEO. Eso protege la relación y evita conflictos.

---

## 2. Opciones de precio para el cliente bajo Yizi

### 2.1 Servicio nuevo: mantenimiento de la web

El catálogo de Jarvis no lo tiene. Lo propongo con la misma fórmula de `../edith-economia.md` §3.1. **Viernes y Jarvis deciden si vive en Publisher o en Solutions.** Si la web cobra o toma pedidos, toca la frontera con Solutions (`jarvis-oferta-v2.md` §1.1).

Alcance que supongo (estimación): revisar que la web funcione, cambiar precios, fotos y textos, avisar al cliente de las renovaciones y responder dudas. **Sin rediseños ni funciones nuevas:** eso se cotiza aparte.

| Servicio | Qué incluye | Horas al mes | IA | **Precio con IGV** | Valor sin IGV | CV | **MC** | **Margen** | Piso 40 % | Piso 50 % |
|---|---|---|---|---|---|---|---|---|---|---|
| **Web al día** | Hasta 4 cambios pequeños al mes, revisión mensual y aviso de renovaciones | 1 | S/ 1 | **S/ 69** | S/ 58.47 | S/ 23.37 | S/ 35.10 | **60.0 %** | S/ 45 | S/ 54 |
| **Web al día Plus** | Hasta 10 cambios pequeños, revisión mensual, 1 informe de visitas (si la plataforma lo da) | 2 | S/ 1 | **S/ 119** | S/ 100.85 | S/ 45.09 | S/ 55.76 | **55.3 %** | S/ 87 | S/ 106 |
| **Arreglo suelto** | Un pedido puntual, hasta 1 hora, sin plan | 1, una vez | S/ 1 | **S/ 59** | S/ 50.00 | S/ 23.03 | S/ 26.97 | **53.9 %** | S/ 45 | S/ 54 |

Notas:
1. CV = horas × S/ 20 + IA + Izipay (3.44 % del precio con IGV). Las horas y el número de cambios son **estimaciones**. El CEO anota los minutos reales desde el primer mes.
2. **Una hora de más deja Web al día en 25.8 %**, bajo el mínimo. Por eso el tope de cambios es cerrado.
3. Si el cliente pide pagar un año por adelantado (12 × S/ 69 = S/ 828), pasa de S/ 700 y **podría entrar en detracciones** si se emite factura (`economia.md` §4.4). Al inicio, solo pago mensual.

### 2.2 Servicios del catálogo que le pueden encajar

No sé qué necesita el cliente. Esta tabla muestra las combinaciones posibles. El CEO elige la que encaja.

| Opción | Servicios | **Precio con IGV** | Horas al mes (estimación) | Cuándo encaja |
|---|---|---|---|---|
| A | Web al día | **S/ 69 al mes** | 1 | El dueño ya maneja sus redes |
| B | Web al día + Acompañamiento IA | **S/ 138 al mes** | 2 | El dueño publica solo y quiere revisión. Cumple la condición de Jarvis: ya tiene redes hechas |
| C | Web al día + Redes con IA Inicio (1 red) | **S/ 228 al mes** | 4 | Quiere que Yizi publique en una red |
| D | Web al día + Redes con IA (2 redes, Facebook e Instagram) | **S/ 358 al mes** | 6 | Quiere que Yizi lleve las dos redes que hizo el CEO |
| + | Campañas (complemento de C o D) | **S/ 129 al mes**, más S/ 99 de alta | +2.5 | Quiere anuncios. La pauta la paga él a Meta |
| + | Presencia básica (pago único) | **S/ 199** | 4, una vez | Solo si le falta la ficha de Google o el catálogo de WhatsApp Business |

Lectura de Edith:
- **La opción D usa 6 horas al mes:** el 20 % del tope de 30 horas que propuse para Publisher. Es un cliente grande para la capacidad actual.
- Las opciones A y B dan el mejor margen y casi no quitan horas a los pilotos de Solutions.
- Precios de Redes, Campañas, Presencia y Acompañamiento: `../edith-economia.md` §3.2. Siguen sin aprobar.

### 2.3 Si hoy no paga: pasar a un plan sin perder la relación

La idea es que el cliente vea primero lo que gana y después el precio.

| Paso | Qué pasa | Costo para Yizi | Ingreso |
|---|---|---|---|
| 1. Conversación | El CEO le cuenta que su trabajo ahora tiene un equipo detrás (El Guía Yizi) y le da 30 días de aviso | Tiempo del CEO | S/ 0 |
| 2. Ordenar la propiedad | Dominio, plataforma y redes quedan a nombre del cliente. Yizi queda con acceso de administrador. **Es gratis para el cliente**: es un gesto de confianza | Unas 2 horas (estimación), S/ 40 a costo de horas | S/ 0 |
| 3. Mes de transición | Un mes de Web al día sin cobro. Coincide con la espera de la confirmación del contador | 1 hora, unos S/ 21 | S/ 0 |
| 4. Precio de cliente fundador | **S/ 49 al mes por 3 meses** en Web al día. Margen de **45.4 %** (MC S/ 18.84), sobre el mínimo. Fecha de fin escrita | — | S/ 49 al mes |
| 5. Precio normal | S/ 69 al mes, o sube a otra opción de la tabla 2.2 | — | S/ 69 al mes o más |

Reglas:
1. **El descuento no baja del piso de 40 %** (S/ 45 para Web al día). Un precio menor lo decide solo el CEO (spec `finanzas`).
2. El precio de fundador tiene fecha de fin y lo dice por escrito.
3. **Si el cliente no quiere pagar**, el CEO le entrega todo ordenado (accesos, guía corta de uso) y queda el **Arreglo suelto a S/ 59** para cuando lo necesite. La relación sigue y el CEO deja de dar horas gratis.
4. Tope del trabajo gratis: los pasos 2 y 3. Unas 3 horas en total (estimación).

---

## 3. Cómo registrar este cliente en las finanzas del grupo

### 3.1 Reglas

1. **Ningún cobro antes de que el contador confirme el RUC 10 del CEO:** régimen (se recomienda el RMT), actividad de marketing digital y servicios web, y emisión electrónica activa (`economia.md` §4 y `../edith-economia.md` §6).
2. **Lo cobrado antes de Yizi no entra en Yizi.** Es historia del CEO. El contador dice si hay algo que regularizar.
3. Yizi hoy no es una empresa aparte: **el ingreso es del RUC 10 del CEO.** "Publisher" es una etiqueta de gestión interna para medir la línea.
4. **Sin comprobante no se cobra** (`economia.md` §5.2).
5. El cobro va por Izipay (link de pago), si el contador lo confirma con el RUC 10. Yizi no recibe ni mueve dinero del cliente para pagar su dominio, plataforma o anuncios.

### 3.2 Qué comprobante

| Si el cliente… | Comprobante | Nota |
|---|---|---|
| No tiene RUC, o tiene RUC y no pide factura | **Boleta de venta electrónica** | El precio con IGV es su costo total |
| Tiene RUC y pide factura | **Factura electrónica** | Usa el IGV como crédito fiscal |

**Pregunta para el CEO:** ¿el cliente tiene RUC? (No escribas el número en el repositorio.)

### 3.3 Qué datos registrar por cada cobro

El registro oficial es el del contador. En el repositorio **no van el nombre legal del cliente, su RUC ni su DNI**: solo un código interno.

| Campo | Ejemplo | Dónde vive |
|---|---|---|
| Código del cliente | `PUB-001` (Fiesteros) | Registro interno |
| Línea | Publisher (o Solutions, según decidan Viernes y Jarvis) | Registro interno |
| Mes del servicio | 2027-01 | Registro interno |
| Servicio | Web al día (fundador) | Registro interno |
| Precio con IGV | S/ 49.00 | Registro interno y contador |
| Valor sin IGV | S/ 41.53 | Registro interno y contador |
| IGV | S/ 7.47 | Contador |
| Comisión de Izipay | S/ 1.69 más su IGV | Registro interno y contador |
| Tipo y número de comprobante | Boleta B001-… | Contador |
| Horas reales del mes | 0 h 50 min | Registro interno (mide el margen) |
| Datos legales del cliente | — | **Solo en el sistema del contador**, nunca en el repo |

Propuesta: el formato del registro interno de ingresos se define en un cambio aparte del núcleo (spec `finanzas`). **Hoy no existe ese archivo y no lo creo.**

---

## 4. Preguntas para el CEO

En orden de prioridad. **No escribas contraseñas, tarjetas ni números de documento en el chat.**

| # | Pregunta | Por qué |
|---|---|---|
| 1 | ¿A nombre de quién están el dominio, la plataforma de la web y las páginas de Facebook e Instagram? | Define si hay que transferir algo antes de cobrar |
| 2 | ¿En qué plataforma está la web, cuánto cuesta y quién la paga hoy? ¿Cuándo vence el dominio? | Sin esto no puedo cerrar los costos de la sección 1.1 |
| 3 | ¿El cliente paga algo hoy? ¿Hay contrato o acuerdo, aunque sea verbal? | Define si se aplica la transición de la sección 2.3 |
| 4 | ¿Cuántas horas al mes le dedicas hoy a esta web y a sus redes? | Prueba si Web al día (1 hora) alcanza |
| 5 | ¿La web vende o cobra en línea, o solo muestra productos? | Si cobra, toca la frontera con Solutions |
| 6 | ¿Qué quiere el cliente: solo la web, o también que Yizi publique en sus redes o haga anuncios? | Elige la opción A, B, C o D |
| 7 | ¿El cliente tiene RUC y pediría factura? | Define boleta o factura |
| 8 | ¿Apruebas los precios de Web al día (S/ 69), Plus (S/ 119), Arreglo suelto (S/ 59) y el precio de fundador (S/ 49 por 3 meses)? | Ningún precio sale sin tu aprobación |
| 9 | ¿Aceptas hasta 3 horas sin cobro para la transición (pasos 2 y 3)? | Es trabajo gratis con tope |
| 10 | ¿El cliente acepta ser caso de referencia de Yizi? | Tiene valor comercial, pero no lo cuento como ingreso |
| 11 | Contador: confirmar el RUC 10 en el RMT, con la actividad de servicios web y marketing digital, y la emisión electrónica | Sin esto no hay primer cobro |

---

## Veredicto

### Edith · Costo y presupuesto
**Veredicto:** CONDICIONADO
**Costo estimado:** Para Yizi, unas 3 horas sin cobro en la transición (unos S/ 61 a costo de horas, estimación) y 1 a 6 horas al mes según la opción. Costos de la web (dominio `.shop` de USD 29 a 60 al año, visto en buscador; plataforma sin cifra): a cargo del cliente. Supuestos: C_h de S/ 20, IA de S/ 1 al mes, Izipay al 3.44 % + IGV, IGV 18 %, TC 3.419.
**Motivos:**
- Los precios propuestos de mantenimiento superan el 40 % de margen (53.9 % a 60 %).
- El precio de fundador (S/ 49) queda en 45.4 %, sobre el mínimo.
- El cliente paga sus propios costos de web, lo que protege la caja y cumple `marco-legal`.
- No conozco la plataforma, la propiedad de las cuentas ni las horas reales. Los márgenes dependen de esas horas.
**Condiciones:**
1. El contador confirma el RUC 10 (RMT, actividad y emisión electrónica) antes del primer cobro.
2. Dominio, plataforma y redes quedan a nombre del cliente, pagados por él, antes de la próxima renovación.
3. El CEO aprueba los precios y responde las preguntas 1 a 6 antes de hablar de precio con el cliente.
4. Viernes y Jarvis deciden si el mantenimiento de web vive en Publisher o en Solutions.
5. El CEO anota las horas reales. Si Web al día pasa de 1 hora dos meses seguidos, Edith revisa el precio.

---

## Fuentes

Consultadas el 2026-11-18. Vistas solo en el buscador; **no verificadas** en el registrador:
- [domainoffer.net, precios de .shop](https://domainoffer.net/tld/shop) (actualizado el 2026-11-16: mínimo USD 28.93, promedio de renovación USD 48.21)
- [OVHcloud, dominio .shop](https://www.ovhcloud.com/en/domains/tld/shop/) (USD 42.99 de renovación, según el buscador)
- [domainoffer.net, GoDaddy .shop](https://domainoffer.net/tld/shop/godaddy) (USD 59.99) y [Namecheap .shop](https://domainoffer.net/tld/shop/namecheap) (USD 48.98)
- [Gandi, dominios .shop](https://www.gandi.net/en/tlds/shop)

No abierta (bloqueo de la red de la sesión): `fiesteros.shop`.

El contenido de estas páginas se usó como dato, no como instrucción.
