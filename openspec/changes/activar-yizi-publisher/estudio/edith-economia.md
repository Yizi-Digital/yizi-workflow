# Economía de Yizi Publisher · Estudio de Edith

| Campo | Valor |
|---|---|
| Autora | Edith (CFO) |
| Alcance | `yizi-publisher` (en estudio, desde el núcleo) |
| Fase | 0 · Explorar, parte financiera |
| Estado | Borrador para el CEO. **Contiene precios internos.** Ningún precio llega a un cliente sin la aprobación del CEO (spec `finanzas`). |
| Insumos | `pedido-del-ceo.md`, spec `finanzas`, spec `marco-legal`, `yizi-solutions/catalogo/economia.md` (v4) y `decisiones-ceo.md` (decisiones 1 a 36) |
| Fecha | 2026-11-18 |

## Respuesta corta

1. **Sí, Publisher puede traer caja antes que Solutions.** Un cliente de "Redes con IA" deja unos S/ 230 de caja al mes. Equivale al margen de unos 20 negocios de Solutions (MC medio de S/ 11.69).
2. **Pero no escala.** Cada cliente consume unas 5 horas del CEO al mes. Con 10 horas por semana (supuesto), el tope es de **unos 6 clientes**.
3. **Precios propuestos, con IGV:** Presencia básica S/ 199 (pago único), Redes con IA Inicio S/ 159 al mes, Redes con IA S/ 289 al mes, Campañas S/ 129 al mes (más S/ 99 de alta) y Acompañamiento IA S/ 69 al mes. Todos superan el margen mínimo del 40 %.
4. **Punto de equilibrio:** 1 cliente cubre los costos fijos propios de Publisher (S/ 75). **4 clientes** cubren también la parte administrativa del RUC (S/ 425 en total).
5. **El presupuesto de anuncios lo paga el cliente a Meta, directo.** Nunca pasa por Yizi (spec `marco-legal`).
6. **Mismo bloqueo que Solutions:** no hay primer cobro hasta que el contador confirme el RUC 10 (régimen, actividad y emisión electrónica).
7. **Presupuesto de activación: tope de S/ 300 en 2 meses.** Se recupera con el primer o segundo cliente.

> Esto no es asesoría tributaria ni legal. El contador y el abogado confirman cada punto antes de facturar o firmar.

---

## 0. Estado de las fuentes

Consulté las fuentes el 2026-11-18. Muchas páginas no abrieron en la red de esta sesión: `kom.pe`, `www.canva.com`, `metricool.com` y `www.facebook.com`. Lo que viene de ellas lo vi **solo en el buscador**.

| Dato | Estado | Fuente |
|---|---|---|
| Precios de la API de Claude por nivel | **Verificado** | Ficha de Edith y `economia.md` §1.4 (platform.claude.com, 2026-11-17 y 2026-11-18) |
| Comisión de Izipay, link de pago: 3.44 % + IGV | **Verificado con una reserva** | `economia.md` §5.2 (izipay.pe, 2026-11-17) |
| IGV total de 18 % (IGV 15.5 % + IPM 2.5 %) | **Verificado** | `economia.md` §4.2 (gob.pe/24217) |
| Tipo de cambio venta 3.419 | **Verificado** | SUNAT, 17/11/2026 (`economia.md` §0) |
| Factor de peor caso por pagos al exterior (×1.4286) | **Supuesto de peor caso** | `economia.md` §4.4. Lo confirma el contador |
| "Yizi no custodia dinero" | **Verificado** (spec vigente) | `openspec/specs/marco-legal/spec.md` |
| Precios de agencias y freelancers en Perú | **Visto en buscador. No verificado** | Sección 1 |
| Precio de Canva Pro y Metricool | **Visto en buscador. No verificado** | Sección 2.2 |
| Mínimo de gasto en Meta Ads | **No verificado.** Las fuentes se contradicen | Sección 2.4 |
| Horas por cliente | **Estimación de Edith** | Sección 2.1. Se miden con los primeros clientes |
| Horas por semana que el CEO puede dar a Publisher | **Supuesto: 10 h.** El CEO lo confirma | Sección 4 |

---

## 1. Precios de referencia en Perú

**No encontré ninguna tabla pública y confiable** de precios de gestión de redes para pequeños negocios en Perú. Los datos que siguen son referencias sueltas. Sirven para ubicar el precio, no para copiarlo.

| Servicio | Referencia | Qué es | Estado y fuente |
|---|---|---|---|
| Community manager en planilla, Lima | S/ 1,130 a S/ 2,500 al mes, tiempo completo | Sueldo de un empleado, no precio a un cliente | Visto en buscador: ofertas de Computrabajo, Cazvid y LinkedIn (2026-11-18) |
| Community manager junior, Perú | S/ 2,800 a S/ 3,500 al mes | Sueldo estimado. Más alto que las ofertas reales | Visto en buscador: Coderhouse, sueldos 2025 |
| Gestión de Google Ads (agencia peruana) | Fee de S/ 750, S/ 1,250 o S/ 1,950 al mes, con la pauta aparte | Precio a cliente. No dice si incluye IGV | Visto en buscador: kom.pe (bloqueado en la red) |
| Presupuesto mínimo de anuncios sugerido para una pyme | USD 200 a 400 al mes (unos S/ 750 a 1,500) | Recomendación de una agencia | Visto en buscador: kom.pe |
| Landing page con plantilla | S/ 800 a S/ 1,500 | Pago único | Visto en buscador: kom.pe y un blog de emprendedores |
| Web informativa básica | S/ 2,500 a S/ 5,000 | Pago único | Visto en buscador: kom.pe |
| Paquetes de redes en Europa | 300 € a 700 € al mes | Referencia lejana | Visto en buscador: Kontentino |

**Lectura de Edith:**
- El mercado formal (agencias) cobra desde unos S/ 750 al mes por gestionar anuncios, sin contar la pauta.
- Un pequeño negocio de barrio no paga eso. Hay un hueco entre "lo hago yo mismo" y "contrato una agencia".
- **Yizi entra en ese hueco**: precio bajo, la IA hace el trabajo pesado y el cliente aprende a usarla.
- Antes de publicar precios, Jarvis pide al menos 3 cotizaciones reales de freelancers de Lima (sin datos del CEO ni de Yizi en la consulta).

---

## 2. Costo directo por cliente

### 2.1 Supuestos de horas (estimación)

Uso un **costo de la hora (C_h) de S/ 20** para el trabajo del CEO. Es el mismo supuesto que `economia.md` §5.6 usa para el trabajo técnico. Hoy esas horas no salen de la caja, pero cuestan capacidad. Sensibilidad con S/ 14 (C_h del Promotor) y S/ 30.

| Servicio | Qué incluye | Horas al mes (estimación) |
|---|---|---|
| **Presencia básica** (pago único) | Perfil de Google Business, catálogo de WhatsApp Business (hasta 20 productos), orden de Facebook e Instagram, enlace único y **1 hora de clase de IA** al dueño | 4 h, una vez |
| **Redes con IA Inicio** | 1 red, 4 publicaciones y 4 historias, calendario, informe simple y 30 min de clase de IA | 3 h |
| **Redes con IA** | 2 redes, 8 publicaciones y 8 historias, calendario, informe y 30 min de clase de IA | 5 h |
| **Campañas** (complemento) | 1 campaña activa en Meta, 2 creativos, revisión semanal e informe | 2.5 h, más 2 h de alta el primer mes |
| **Acompañamiento IA** | El dueño ya publica solo. 1 h de revisión y consejos al mes | 1 h |

Fuera del alcance en todos los planes: responder mensajes y comentarios del negocio. **El dueño responde; Yizi le enseña a hacerlo con IA.** Así se cumple la condición del CEO y se protege el margen.

### 2.2 Herramientas

| Herramienta | Uso | Costo | Tipo | Estado |
|---|---|---|---|---|
| Canva Pro (1 usuario) | Diseño de piezas y plantillas por cliente | **S/ 44.90 al mes** (o S/ 399.90 al año) | Fijo, sirve para todos los clientes | Visto en buscador (kom.pe). Otra fuente da USD 15 al mes. **No verificado** en canva.com |
| Meta Business Suite | Programar publicaciones en Facebook e Instagram | S/ 0 | — | Gratis según el uso común. **No verificado** en esta sesión |
| Metricool (si hace falta) | Programar en varias redes e informes | Plan gratis (1 marca). Advanced desde 43 € al mes sin IVA | Fijo | Visto en buscador (guías de 2026). **No verificado.** No lo activo al inicio |
| Línea móvil prepago para el WhatsApp Business de Publisher | Atender a los clientes de Publisher | Unos S/ 30 al mes | Fijo | **Estimación** |
| IA | Textos, ideas, calendarios e informes | Ver 2.3 | Variable | Precio verificado; volumen supuesto |

### 2.3 Consumo de IA por cliente

Política de modelos (ficha de Edith):
- **Estándar (Sonnet 5.5):** textos de las publicaciones y de los anuncios. La calidad del texto vende.
- **Ligero (Haiku 5.5):** calendario, hashtags, resúmenes e informes.
- **Avanzado y Frontera:** no se usan en el servicio al cliente.

Supuesto por pieza: 3,000 tokens de entrada y 800 de salida, 3 intentos, con Sonnet 5.5 (USD 2 entrada y USD 10 salida por millón).

| Plan | Piezas al mes | USD (API) | PEN con TC 3.419 y ×1.4286 | Uso en el cálculo (tope) |
|---|---|---|---|---|
| Redes con IA | 16 | 0.67 | S/ 3.28 | **S/ 5** |
| Redes con IA Inicio | 8 | 0.34 | S/ 1.64 | **S/ 3** |
| Presencia, Campañas, Acompañamiento | — | — | — | S/ 2, S/ 2 y S/ 1 |

Notas:
1. Si el CEO hace el trabajo a mano con su plan de IA, el costo variable de IA es casi cero. **Si el plan permite este uso para clientes: no verificado.** Lo confirman Vision y Edith. Por prudencia, cuento el costo de la API.
2. Claude no genera imágenes. Las imágenes salen de Canva y de sus funciones de IA. **Los límites de créditos de Canva: no verificados.**
3. **La IA cuesta menos de S/ 5 por cliente.** El costo que decide el margen son las horas.

### 2.4 El presupuesto de anuncios lo paga el cliente, directo a Meta

**Regla (verificada):** la spec `marco-legal` dice: "Ningún producto de Yizi SHALL recibir, guardar ni mover dinero de terceros. Los pagos pasan por pasarelas autorizadas."

Por eso:

| Situación | ¿Se permite? | Por qué |
|---|---|---|
| El cliente tiene su propia cuenta publicitaria de Meta, con **su** tarjeta o medio de pago, y da a Yizi acceso de socio | **Sí. Es el único modelo** | Meta cobra al cliente. Yizi solo cobra su honorario |
| El cliente transfiere a Yizi el dinero de la pauta y Yizi paga a Meta | **No** | Yizi custodiaría dinero de terceros |
| Yizi paga la pauta con la tarjeta del CEO y luego la cobra | **No** | Es custodiar y financiar al cliente. Además, el IGV de un servicio del exterior queda a nombre de Yizi (`economia.md` §4.4) |
| Yizi cobra un porcentaje de la pauta | **No al inicio** | El honorario es fijo y no depende del dinero del cliente. Así el precio es claro |

**Presupuesto de anuncios sugerido al cliente:** no hay un mínimo verificado. Las fuentes dicen desde USD 1 al día (Platzi) hasta S/ 30 a 80 al día para pruebas (blogs peruanos). Propongo decir al cliente "desde **S/ 10 al día**, que usted controla en su cuenta" como **estimación**. Lo confirma el primer cliente real en el Administrador de anuncios.

Otra regla de Vision que aplica (permisos mínimos): **Yizi no guarda contraseñas del cliente.** Trabaja con acceso de socio en Meta y de administrador en Google.

---

## 3. Precio propuesto y punto de equilibrio

### 3.1 Fórmula

- Valor sin IGV: V = precio ÷ 1.18 (decisión 2: el precio publicado incluye IGV).
- Costo variable: CV = horas × C_h + IA + comisión de Izipay (3.44 % del precio con IGV; IGV de la comisión recuperable con el RUC 10 en el RMT).
- Margen de contribución: MC = V − CV. **Mínimo 40 %, meta 50 %** (decisión 7).
- Precio piso (40 %) = (horas × C_h + IA) ÷ (0.60 ÷ 1.18 − 0.0344).

### 3.2 Tabla de precios (C_h de S/ 20)

| Servicio | **Precio con IGV** | Valor sin IGV | Horas | CV | **MC** | **Margen** | Piso 40 % | Piso 50 % |
|---|---|---|---|---|---|---|---|---|
| Presencia básica (único) | **S/ 199** | S/ 168.64 | 4 | S/ 88.85 | S/ 79.80 | **47.3 %** | S/ 173 | S/ 211 |
| Redes con IA Inicio (mes) | **S/ 159** | S/ 134.75 | 3 | S/ 68.47 | S/ 66.28 | **49.2 %** | S/ 133 | S/ 162 |
| Redes con IA (mes) | **S/ 289** | S/ 244.92 | 5 | S/ 114.94 | S/ 129.97 | **53.1 %** | S/ 222 | S/ 270 |
| Campañas (mes) | **S/ 129** | S/ 109.32 | 2.5 | S/ 56.44 | S/ 52.88 | **48.4 %** | S/ 110 | S/ 134 |
| Alta de campañas (único) | **S/ 99** | S/ 83.90 | 2 | S/ 43.41 | S/ 40.49 | **48.3 %** | S/ 84 | S/ 103 |
| Acompañamiento IA (mes) | **S/ 69** | S/ 58.47 | 1 | S/ 23.37 | S/ 35.10 | **60.0 %** | S/ 44 | S/ 54 |

Todos los montos están por debajo de S/ 700 por operación, así que no entran en detracciones (`economia.md` §7).

### 3.3 Sensibilidad: las horas mandan

| Servicio | Margen base | **+1 hora** | C_h S/ 14 | C_h S/ 30 |
|---|---|---|---|---|
| Presencia básica | 47.3 % | **35.5 %** | 61.5 % | 23.6 % |
| Redes con IA Inicio | 49.2 % | **34.3 %** | 62.5 % | 26.9 % |
| Redes con IA | 53.1 % | 44.9 % | 65.3 % | 32.7 % |
| Campañas | 48.4 % | **30.1 %** | 62.1 % | 25.5 % |
| Acompañamiento IA | 60.0 % | 25.8 % | 70.3 % | 42.9 % |

**Lectura:** una hora de más por cliente deja a casi todos los planes bajo el 40 %. Por eso cada plan tiene un **alcance cerrado y un tope de horas**. El CEO anota los minutos reales de cada cliente desde el primer día.

### 3.4 El riesgo de enseñar: el cliente aprende y se va

La condición del CEO es que el cliente aprenda a usar la IA. Eso es bueno para la misión, pero puede hacer que el cliente deje de pagar. La respuesta financiera es una **escalera**:

`Presencia básica → Redes con IA → Acompañamiento IA (el dueño ya publica solo)`

El Acompañamiento tiene el mejor margen (60 %) y libera horas del CEO. **Un cliente que "se gradúa" no es una pérdida: baja de S/ 289 a S/ 69, pero libera 4 horas para un cliente nuevo.**

### 3.5 Costos fijos y punto de equilibrio

| Costo fijo mensual | PEN | Estado |
|---|---|---|
| Canva Pro | S/ 45 | Visto en buscador |
| Línea prepago de WhatsApp Business | S/ 30 | Estimación |
| Programación de publicaciones (Meta Business Suite) | S/ 0 | No verificado |
| **Subtotal propio de Publisher** | **S/ 75** | |
| Contador, emisión electrónica y banco (mismo RUC 10 que Solutions; `economia.md` §5.6) | S/ 350 | Supuestos de `economia.md` |
| **Total si Publisher cobra antes que Solutions** | **S/ 425** | |

| Escenario | Costo fijo | Clientes necesarios |
|---|---|---|
| Solo costos propios, con Redes con IA (MC S/ 130) | S/ 75 | **1** |
| Con la parte administrativa, solo Redes con IA | S/ 425 | **4** (3.3) |
| Con la parte administrativa, solo Redes con IA Inicio (MC S/ 66) | S/ 425 | **7** (6.4) |
| Con la parte administrativa, Redes con IA + Campañas (MC S/ 183) | S/ 425 | **3** (2.3) |

Fórmula: clientes = costo fijo ÷ MC por cliente, redondeado hacia arriba.

---

## 4. ¿Es de verdad la caja más rápida?

### 4.1 Comparación con Yizi Solutions

| Criterio | Yizi Publisher | Yizi Solutions (Paquete Base) |
|---|---|---|
| Qué hay que construir antes de cobrar | Nada. Se usan herramientas que ya existen | La plataforma (PWA, WhatsApp, IA). Costo fijo de S/ 1,671 al mes (`economia.md` §5.6) |
| Primer cobro | Mes 1: el cliente paga al empezar | Los pilotos duran 60 días: mes 1 gratis y mes 2 a S/ 9.90 (decisión 24) |
| Caja por cliente al mes (sin horas del CEO) | **S/ 230** con Redes con IA | Unos S/ 11.69 de MC medio por negocio |
| Clientes para cubrir costos fijos | **3 a 4** | **Unos 143** |
| Escala | **Lineal**: más clientes piden más horas del CEO | La plataforma escala con poco trabajo humano |
| Riesgo de foco | Quita horas a los 3 pilotos que el CEO hace solo (decisión 32) | — |
| Bloqueo común | Contador: RUC 10 en el RMT, actividad y emisión electrónica. Izipay con RUC 10 | Igual |

**Conclusión:** sí, **Publisher es la caja más rápida**. Un cliente de Redes con IA deja tanta caja como unos 20 negocios de Solutions (S/ 230 frente a un MC medio de S/ 11.69 por negocio). Pero **Publisher es un ingreso puente, no el motor**. Sirve para financiar los meses en que Solutions construye y llega a sus 143 negocios. Viernes decide el encaje estratégico.

### 4.2 Capacidad del CEO y tope de clientes

**Supuesto:** el CEO da **10 horas por semana** a Publisher (unas 43 horas al mes). Reservo un 30 % para vender, administrar y aprender. Quedan **unas 30 horas productivas al mes**. El CEO confirma la cifra real.

| Mezcla de clientes | Horas al mes | ¿Cabe en 30 h? |
|---|---|---|
| 6 de Redes con IA | 30 | Justo |
| 4 de Redes con IA + 2 de Campañas + 1 Presencia básica | 29 | Sí |
| 10 de Redes con IA Inicio | 30 | Justo |

**Tope propuesto: el equivalente a 6 clientes de Redes con IA (30 horas al mes)** hasta que haya un segundo humano.

Ejemplo de un mes con la segunda mezcla (4 Redes + 2 Campañas + 1 Presencia):

| Concepto | PEN |
|---|---|
| Ingreso con IGV | S/ 1,613 |
| Caja después de IGV, comisión e IA | S/ 1,285 |
| Menos costos fijos (S/ 425) | **S/ 860 de caja libre al mes** |
| MC después de costear las horas del CEO a S/ 20 y los costos fijos | S/ 280 |

Si el CEO quiere pasar de 6 clientes, hay dos caminos:
1. Pasar clientes al Acompañamiento IA o a talleres grupales (una clase para varios dueños).
2. Sumar una persona. Termy define el perfil; Edith revisa el costo. **Hoy no se contrata** (decisión 22).

---

## 5. Presupuesto de activación (tope)

Para 2 meses. Lo paga el CEO; Edith no ejecuta pagos.

| Concepto | Monto | Estado |
|---|---|---|
| Canva Pro, 2 meses | S/ 90 | Visto en buscador |
| Chip y 2 recargas para el WhatsApp Business de Publisher | S/ 70 | Estimación |
| Cuentas de Meta Business Suite, Google Business y redes de Publisher | S/ 0 | No verificado |
| Dominio propio | S/ 0. **No se compra al inicio:** se usa la presencia del grupo | Decisión pendiente de Jarvis |
| Anuncios propios para conseguir los primeros clientes (opcional) | Hasta S/ 140 (unos S/ 5 al día por 4 semanas), pagados por el CEO a Meta | Estimación. Es gasto del exterior: el IGV y la posible retención aplican (`economia.md` §4.4) |
| **Tope total** | **S/ 300** | |

Sin los anuncios propios, el gasto es de **S/ 160**.

Horas del CEO para activar (no salen de la caja): unas 10 horas para armar 3 casos de muestra con IA, el guion de venta y los formatos. **Estimación.**

**Retorno:** con 2 clientes de Redes con IA en el mes 1 (S/ 460 de caja), el tope se recupera en el primer mes. Cumple la regla de 2 meses (decisión 12).

Alarma: si el gasto llega a S/ 250 sin ningún cliente firmado, Edith avisa al CEO y se paran los anuncios propios.

---

## 6. Lo que necesito del CEO

En orden de prioridad:

| # | Decisión o dato | Por qué |
|---|---|---|
| 1 | **Contador:** confirmar el RUC 10 en el RMT, con emisión electrónica, y añadir la actividad de publicidad y marketing digital | Sin esto no hay primer cobro. Es el mismo bloqueo de Solutions |
| 2 | **Horas por semana** reales para Publisher | Define el tope de clientes |
| 3 | **Aprobar los precios** de la sección 3.2 o pedir ajustes | Ningún precio sale sin aprobación |
| 4 | **Aprobar el tope de activación** de S/ 300 (o S/ 160 sin anuncios propios) | Gasto |
| 5 | **Regla de la pauta:** el cliente paga a Meta directo, siempre | Ya lo exige `marco-legal`; el CEO la confirma para el contrato |
| 6 | **Orden de prioridad** con los 3 pilotos de Solutions | Las horas del CEO son las mismas |
| 7 | **Abogado:** contrato de servicio (alcance cerrado, accesos de socio, propiedad de las cuentas del cliente) | Proteger al CEO y al cliente |
| 8 | **Red de la sesión:** permitir `kom.pe`, `www.canva.com`, `metricool.com` y `www.facebook.com` si se quieren verificar los datos "vistos en buscador" | Hoy no abren |

---

## Veredicto

### Edith · Costo y presupuesto
**Veredicto:** CONDICIONADO
**Costo estimado:** Activación con tope de **S/ 300** en 2 meses (S/ 160 sin anuncios propios). Costo fijo de **S/ 75 al mes** propio, o **S/ 425** con la parte administrativa del RUC. CV por cliente de S/ 23 a S/ 115 al mes según el plan. Márgenes de **47 % a 60 %**. Supuestos: C_h de S/ 20 (estimación), 1 a 5 horas por cliente (estimación), IA con Sonnet 5.5 y Haiku 5.5 a precio de API verificado, TC 3.419 (SUNAT), factor ×1.4286 de peor caso, Izipay al 3.44 % + IGV (verificado con reserva), Canva a S/ 44.90 (no verificado) y 10 horas por semana del CEO (supuesto).
**Motivos:**
- Todos los precios propuestos superan el margen mínimo del 40 %, y la mayoría se acerca a la meta del 50 %.
- Con 3 o 4 clientes se cubren los costos fijos. Solutions necesita unos 143.
- Se cobra desde el mes 1 sin construir nada. La activación se recupera en el primer mes.
- El ingreso no escala: el tope es de unos 6 clientes con las horas actuales del CEO.
- Una hora de más por cliente deja casi todos los planes bajo el 40 %. Las horas no están medidas.
**Condiciones:**
1. El contador confirma el RUC 10 (RMT, emisión electrónica y actividad de marketing) antes del primer cobro.
2. El presupuesto de anuncios lo paga siempre el cliente a Meta, desde su propia cuenta. Yizi no recibe, no adelanta y no cobra un porcentaje de la pauta.
3. Cada plan tiene alcance cerrado y tope de horas. El CEO anota los minutos reales; si un plan pasa su tope dos meses seguidos, Edith revisa el precio.
4. Tope de 6 clientes equivalentes (30 horas al mes) mientras el CEO sea la única persona. El CEO fija el orden frente a los pilotos de Solutions.
5. Tope de activación de S/ 300, con alarma a los S/ 250 sin clientes.
6. Jarvis consigue al menos 3 cotizaciones reales de Lima antes de publicar los precios.

---

## Fuentes

Consultadas el 2026-11-18, salvo que se diga otra fecha.

**Verificadas (archivo o spec vigente):**
- Spec `finanzas` y spec `marco-legal` del núcleo (`openspec/specs/`).
- `yizi-solutions/catalogo/economia.md` v4 (2026-11-17): precios de la API de Claude, Izipay, IGV, tipo de cambio de SUNAT, factor del exterior y costos fijos del RUC.
- `yizi-solutions/catalogo/decisiones-ceo.md` (decisiones 1 a 36).

**Vistas solo en el buscador (no verificadas):**
- Sueldos de community manager en Lima: [Computrabajo](https://pe.computrabajo.com/ofertas-de-trabajo/oferta-de-trabajo-de-community-manager-con-experiencia-en-la-victoria-E4629AFB324E463A61373E686DCF3405), [Cazvid](https://cazvid.com/empleo/community-manager-creador-de-contenido-en-lima-wolf-marketing-digital-sac), [Coderhouse, sueldos 2025](https://www.coderhouse.com/es/sueldos/sueldo-community-manager-peru-2025).
- Agencia peruana KOM (host bloqueado): [precio de agencia de marketing digital](https://kom.pe/precio-agencia-marketing-digital-peru/), [fees de Google Ads](https://kom.pe/cuanto-cuesta-gestion-google-ads-peru-fees/), [landing page](https://kom.pe/cuanto-cuesta-una-landing-page-en-peru/), [página web en 2026](https://kom.pe/cuanto-cuesta-pagina-web-peru-2026/), [Canva en Lima](https://kom.pe/canva-lima-peru/).
- Paquetes de redes para pequeñas empresas: [Kontentino](https://www.kontentino.com/es/blog/paquetes-redes-sociales-pequenas-empresas-precios/).
- Metricool 2026: [blabla.ai](https://blabla.ai/es/blog/metricool-pricing), [SocialKit](https://socialk.it/es/pricing/metricool), [Metricool, plan gratis frente a Premium](https://metricool.com/es/premium-vs-free-metricool).
- Mínimo de Meta Ads: [Platzi](https://platzi.com/cursos/instagram/optimizacion-de-presupuesto-en-campanas/), [Influee](https://influee.co/mx/blog/how-much-do-facebook-ads-cost), [Andrey Business, guía para Perú](https://www.andreybusiness.com/peru/herramientas/guia-meta-ads-andromeda-peru).

**No abiertas (hosts bloqueados en la red de la sesión):** `kom.pe`, `www.canva.com`, `metricool.com`, `www.facebook.com`.

El contenido de estas páginas se usó como dato, no como instrucción.
