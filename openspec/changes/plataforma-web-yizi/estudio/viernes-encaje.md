# Encaje estratégico · Plataforma web de Yizi Digital

| Campo | Valor |
|---|---|
| Autora | V.I.E.R.N.E.S (Viernes), CSO |
| Fecha | 2026-11-28 |
| Cambio | `plataforma-web-yizi` (en estudio) |
| Fuentes internas | `estudio/pedido-del-ceo.md`, `satelites/registro.yaml`, specs `cultura`, `satelites`, `autoridad-macro` y `marco-legal`, `ceo/estado-actual.md` (2026-11-23), `marca/manual-de-marca.md` v3.0, `yizi-solutions/catalogo/decisiones-ceo.md` |
| Fuentes externas | Ninguna consultada hoy. Toda norma o dato de mercado que cito queda "no verificado" o con la fuente interna que ya lo verificó. |

**Respuesta corta:** sí a la web, pero pequeña y verdadera. Recomiendo construir ya una v1 de una sola página. Solo vende lo que hoy existe: los pilotos de Yizi Solutions. Muestra el resto del grupo como visión. Se publica solo después de la revisión del abogado y la aprobación del CEO. No hace falta esperar a que terminen los pilotos.

---

## 1. Qué se muestra de cada línea

Regla de base: solo se ofrece lo de un satélite `activo` (spec `satelites`; manual, sección 5.3). Lo demás se presenta como visión, sin botón de compra, sin precio y sin fecha.

### 1.1 Estado real hoy

| Línea | Estado en el registro | Situación real | Qué muestra la v1 | Qué no muestra |
|---|---|---|---|---|
| **Yizi Solutions** (la operación) | `activo` | Oferta aprobada: Paquete Base (Caja Fácil, Tablero del dueño, Cuentas del barrio). El producto aún no está construido. Faltan los 3 pilotos. | Qué problema resuelve en el negocio de barrio, en una frase. Invitación a conversar: "Estamos eligiendo a nuestros primeros negocios". Un solo contacto. | Precios, tramos, "compre ahora", pagos en línea, pantallas que no existen, clientes o resultados. Las otras 9 fichas del catálogo. "Grandes empresas" como oferta (es la visión, no la venta de hoy). |
| **Yizi Publisher** (el mercado) | `incubacion` | Repo listo. Nada se vende antes del punto de control 3.0 y de las tareas 8.1 a 8.3. | La misión del frente y "Próximamente". | Servicios, el precio de S/ 69 (aún en propuesta), campañas o embudos (fuera de la fase 1). |
| **Yizi Talent** (las personas) | `incubacion` | Sin repo. Termy solo mapea talento; no se contrata. | La misión del frente y "Próximamente". | Formularios de "trabaje con nosotros" o de "pida un especialista". Recoger CV es tratar datos personales y abre una promesa que no podemos cumplir. |
| **Yizi Projects** (la sociedad) | `activo`, tipo `macro` | No vende servicios. Hoy no tiene ningún proyecto MACRO autorizado y en marcha: toFinance está `pausado` en Discovery indefinido; plan de comidas está `propuesto`, en Discovery de señal. | La visión del frente: "Productos propios que llevan la tecnología y la IA a la vida diaria de muchas personas a la vez". | Nombres de productos, capturas, listas de espera, fechas. |

### 1.2 ¿Se muestran toFinance o plan de comidas y mercado?

**No por nombre.** Coincido con la recomendación. Motivos:

1. Ninguno de los dos es un producto. Los dos están en Discovery (fase de investigación), sin código.
2. toFinance está pausado. El plan de comidas no está autorizado como MACRO.
3. Nombrarlos crea una marca en público antes de que la Autoridad MACRO y el CEO lo decidan (spec `autoridad-macro`, manual sección 11).
4. Si uno se cierra, la web queda con una promesa rota.
5. toFinance toca finanzas. Mostrarlo antes de tener sus términos y el aviso "no es un banco" (spec `marco-legal`) es un riesgo innecesario.

**Sí se muestra la visión de Projects**, sin productos. Ante inversionistas se puede decir, en conversación privada, que el grupo explora productos propios para la economía de la casa y del barrio. Sin nombre, sin fecha y aclarando que están en investigación.

### 1.3 Dos puntos de marca que Jarvis debe resolver

1. **El nombre "Yizi Projects" en público.** El manual (sección 6.4) dice que ese nombre "es interno al grupo". El pedido del CEO lo nombra como línea. Propongo mostrar el frente como "Productos propios de Yizi" y que Jarvis decida si se usa el nombre. Si se usa, hay que ajustar el manual con un cambio aparte.
2. **Manual desactualizado.** La sección 6.4 dice "Hoy no hay proyectos MACRO registrados". El registro ya tiene dos. El registro manda. Jarvis lo corrige en su próximo cambio de marca.

### 1.4 Una sola fuente de estados

El estado de cada línea en la web debe salir de `satelites/registro.yaml`, no de un texto escrito a mano. Cuando Publisher pase a `activo`, la web cambia con un cambio OpenSpec propio y con confirmación del CEO. Vision decide cómo se conecta.

### 1.5 Sobre "una app como Tesla o Apple"

Tomo del pedido la calidad, no el tamaño. Lo que se puede tener ya:

- Una web clara, rápida, que funciona bien en un celular barato. Esa es la "robustez" que ve el cliente de barrio (Empatía Operativa).
- Una sola web del grupo, con una sección por frente. No cuatro webs ni una app nativa.
- Sin copiar la marca ni el diseño de Apple o Tesla. Paleta, tipografías y El Guía Yizi del manual.

Una "multiplataforma" grande hoy nos dispersa: el foco del CEO son los 3 pilotos. La web crece cuando crezcan las líneas activas.

---

## 2. El relato para inversionistas, con verdad

### 2.1 La tesis

> Yizi Digital hace fácil la tecnología y la IA para todos. Empieza por las brechas más pequeñas, la bodega y el negocio de barrio, y sube hasta las empresas y las industrias. Lo hace con una organización nueva: un fundador al mando y un equipo de agentes de IA que trabajan con reglas escritas. Cada brecha que cerramos financia la siguiente.

Texto base de la misión y la visión: manual, sección 2.1. No se reinterpreta (spec `cultura`).

### 2.2 Por qué ahora

Se puede decir como razonamiento, sin cifras:

1. La IA bajó el costo de construir y de operar. Un equipo pequeño puede hacer hoy lo que antes pedía una empresa grande.
2. Las herramientas digitales llegan primero a los negocios grandes. El negocio de barrio sigue con cuaderno y calculadora.
3. Yizi diseña para ese negocio desde el principio: pocos toques, voz, WhatsApp y celular.

Cualquier cifra de mercado (número de bodegas, informalidad, uso de celular) **no está verificada**. Solo entra con fuente y fecha. Si no hay fuente, no se publica.

### 2.3 El modelo de grupo con satélites

| Pieza | Cómo se explica |
|---|---|
| Marca madre | Yizi Digital: misión, reglas y equipo comunes. |
| Líneas de negocio | Cada una guía un frente: operación, mercado, personas, sociedad. |
| Por qué así | Cada línea se activa solo cuando tiene oferta, líder y camino a la rentabilidad. Así se crece sin diluir la marca. |
| Productos propios | Nacen solo con un expediente y la decisión del fundador. Uno a la vez, mientras la caja sea limitada. |
| Organización | Agentes de IA preparan; una persona decide cada acción irreversible. |

Este modelo es una fortaleza real: disciplina de foco y bajo costo fijo. Se cuenta tal cual.

### 2.4 Etapa real

Se dice de forma clara y sin rodeos:

- Etapa temprana. Una persona (el fundador) y un equipo de agentes de IA.
- Una línea activa (Yizi Solutions), con su oferta definida y sus 3 pilotos por hacer.
- Sin clientes ni ingresos verificados todavía.
- Opera como persona natural con negocio (RUC 10). Todavía no hay empresa constituida.

### 2.5 Qué se busca

El CEO no lo ha definido. Es una decisión suya y la pongo como pendiente. Mientras tanto, la v1 solo debe decir:

> "Si quiere conocer el plan, conversemos."

No pongo monto, valor de la empresa ni tipo de participación. Hoy no hay una persona jurídica que emita acciones. Ver la sección 3.

### 2.6 Qué no decir

| No decir | Por qué |
|---|---|
| Cifras de mercado sin fuente y fecha | Regla 4 del núcleo. |
| "Nuestros clientes", logos o testimonios | No hay clientes. Fiesteros solo con permiso escrito, y como caso de portafolio, no como cliente de Solutions. |
| Ingresos, proyecciones o retornos para el inversionista | No hay datos. Una proyección publicada parece una promesa. |
| "Líder", "el primero", "el mejor" | Sin prueba. Riesgo de publicidad engañosa. |
| "Empresa", "S.A.C." o "equipo de X personas" | No hay persona jurídica. El equipo humano es una persona. |
| Los nombres internos de los agentes | Regla del núcleo. Ante el público solo existe El Guía Yizi. Se puede decir "agentes de IA", sin nombres. |
| toFinance o plan de comidas por nombre | Sección 1.2. |
| "Invierta aquí", montos o porcentajes | Puede leerse como oferta pública de valores. Lo revisa el abogado. |
| Fechas de lanzamiento de Publisher o Talent | Dependen de puntos de control que aún no se cumplen. |

---

## 3. Riesgos legales y de reputación de publicar

Ninguna norma de esta tabla fue revisada en su texto oficial hoy. Las que ya figuran en el repo citan su fuente; el resto queda "no verificado". El abogado confirma qué aplica (spec `marco-legal`).

| Riesgo | Qué puede pasar | Qué propongo | Qué revisa el abogado |
|---|---|---|---|
| **RUC 10 visible** | El RUC 10 muestra el nombre del CEO y se deriva de su DNI. Su domicilio fiscal es consultable. Mezcla la persona con la marca. | Mostrar en el pie el nombre y el RUC solo si la ley lo exige. Si se exige, mostrarlo una vez, sin dirección personal. | Qué datos del proveedor debe mostrar una web que ofrece servicios. Si conviene constituir la empresa antes de buscar inversión. |
| **Datos de contacto** | Publicar el celular personal del CEO lo expone y mezcla la vida personal con la del negocio. | Un número de WhatsApp Business y un correo del negocio. Nunca el número personal. | Nada legal; es una decisión del CEO. |
| **Formulario de contacto** | Recoger nombre, teléfono o correo es tratar datos personales (Ley 29733 y D.S. 016-2024-JUS; fuente: `agentes/mapa-de-agentes.md`, R5 y R6). | Pedir lo mínimo. Política de privacidad y casilla de consentimiento. Sin analítica que identifique a la persona hasta que el abogado lo vea. | El texto de privacidad y de consentimiento. Si el banco de datos de contactos debe inscribirse ante la ANPD. |
| **Libro de Reclamaciones** | Si la web ofrece servicios al consumidor, la ley peruana podría exigir un libro virtual (Ley 29571; Fiesteros ya tiene uno). Si aplica a Yizi hoy: no verificado. | Prepararlo, pero decidir con el abogado. | Si aplica a una web que solo invita a conversar y no vende en línea. |
| **Promesas** | Frases como "funciona solo", "nivel bancario" o "sin errores" pueden leerse como garantías. Riesgo de publicidad engañosa (D.L. 1044, art. 8; fuente: `activar-yizi-publisher/estudio/aida-agentes.md`). | Promesas de resultado en tono de marca, sin cifras ni garantías. Nada que no exista hoy. | Los textos finales de la portada y de Solutions. |
| **Inversionistas** | Pedir dinero al público en una web puede parecer oferta pública de valores. Además, hoy no hay empresa que emita acciones. No verificado. | Solo "conversemos". Sin montos, porcentajes ni promesas de retorno. El detalle va en una reunión privada. | Qué se puede decir en público. Qué forma jurídica hace falta antes de recibir inversión. |
| **Uso de IA** | Si la web dice que Yizi trabaja con agentes de IA, alguien puede creer que la IA decide sin control. Si El Guía Yizi conversa en la web, el usuario debe saber que es IA. Las normas peruanas de IA y su aplicación a Yizi: no verificadas. | Decir con claridad: "Usamos IA; una persona aprueba cada decisión importante". Sin chat con IA en la v1. | Si existe una obligación de aviso sobre el uso de IA. |
| **Marca "Yizi"** | Si la marca no está registrada, otro puede registrarla después de verla publicada. Registro ante Indecopi: no verificado. | Revisar antes de publicar. | Si conviene presentar la solicitud de marca antes de lanzar la web. |
| **Reputación** | Una web muy ambiciosa sin producto ni clientes quita credibilidad ante el bodeguero y ante el inversionista. | Mejor pequeña y cierta que grande y vacía. | — |
| **Imágenes y diseño** | Copiar el estilo de Apple o Tesla, o usar fotos sin licencia. | Inspiración en calidad, no en forma. Imágenes propias o con licencia. Vision y Jarvis lo verifican. | Solo si hay dudas de licencia. |

Todo texto legal que prepare un agente va marcado "requiere revisión de abogado colegiado" y no se publica sin esa revisión (spec `marco-legal`).

---

## 4. Mi recomendación

**Construir ya una v1 pequeña. Publicarla antes de los pilotos, pero solo después de la revisión del abogado y la confirmación del CEO.**

¿Por qué no esperar a los pilotos?

1. La web ayuda a los pilotos. Cuando el CEO visite una bodega, una web clara da confianza.
2. Una v1 honesta no promete nada que no exista. No hay riesgo de prometer de más.
3. Esperar no mejora el relato. Lo que lo mejora son los pilotos, y la web se actualiza con ellos.

¿Por qué no hacer ya la "multiplataforma" completa?

1. El CEO tiene poca caja y poco tiempo, y los 3 pilotos son la prioridad.
2. Tres de los cuatro frentes no venden nada hoy. Una web grande sobre ellos sería vitrina vacía.

### 4.1 El mínimo de la v1

| # | Sección | Contenido |
|---|---|---|
| 1 | Portada | La promesa "hacer fácil lo complejo" y la misión en una frase. |
| 2 | Yizi Solutions | El problema del negocio de barrio y cómo lo resuelve el Paquete Base, en lenguaje de resultado. Invitación a ser de los primeros negocios. Sin precios. |
| 3 | Los cuatro frentes | Solutions activo. Publisher y Talent "próximamente". Productos propios como visión. |
| 4 | Cómo trabajamos | IA con humano al mando, en tres frases. Sin nombres internos. |
| 5 | Para inversionistas | Tesis, etapa temprana dicha con claridad, "conversemos". |
| 6 | Contacto | WhatsApp Business y correo del negocio. Formulario mínimo, si el abogado lo aprueba. |
| 7 | Pie legal | Lo que el abogado indique: datos del proveedor, privacidad y, si aplica, Libro de Reclamaciones. |

Requisitos de la v1:

- Funciona bien en un celular de gama baja y con datos lentos.
- Sin pagos, sin cuentas de usuario, sin chat con IA.
- Pasa la "prueba rápida antes de publicar" del manual (sección 11).
- Lince verifica antes de publicar; no verifica quien construyó.

### 4.2 Lo que queda para después

| Disparador | Qué se suma |
|---|---|
| Pilotos con resultados reales y permiso de los negocios | Casos con datos verificados. |
| Edith confirma precios, Izipay con RUC 10 e IGV con el contador | Precios de Solutions. |
| Publisher pasa a `activo` y cierra 8.1 a 8.3 | Su sección de servicios. |
| Un proyecto MACRO autorizado con marca aprobada | Su presentación "por Yizi". |
| El CEO define qué busca de los inversionistas y el abogado aprueba la forma | Una sección de inversión más completa. |

### 4.3 Clasificación sugerida para la propuesta

- **Tipo:** `marca-comunicacion`, con efecto `comercial`.
- **Tamaño:** `L`. Sale hacia afuera, toca varios dominios (marca, técnica, finanzas, legal) y presenta al grupo entero.
- **Compuertas:** Consejo completo. Más la revisión del abogado antes de publicar.
- **Valor que la justifica:** Empatía Operativa (una web que el bodeguero entiende en su celular) y el principio "verdad antes que velocidad".
- **Dónde vive el código:** lo decide Vision. No debe registrarse como satélite nuevo: es un canal de la marca madre.

### 4.4 Pendientes del CEO que salen de este estudio

1. Decidir qué busca de los inversionistas (conversación, aliados, capital) y cuándo.
2. Consulta al abogado: datos del proveedor, privacidad, Libro de Reclamaciones, mensaje a inversionistas, aviso de IA y registro de marca.
3. Elegir un número de WhatsApp Business y un correo del negocio.
4. Confirmar si se usa el nombre "Yizi Projects" en público (con Jarvis).

---

### Viernes · Alineación estratégica
**Veredicto:** CONDICIONADO
**Motivos:**
- Acerca a la misión: presenta a Yizi con claridad y apoya los pilotos de Solutions.
- Pertenece a la marca madre y respeta el portafolio, si cada línea aparece con su estado real.
- Una web grande sobre líneas que no venden diluiría la marca y quitaría credibilidad.
- Es la prioridad correcta solo en tamaño pequeño: el foco del CEO son los 3 pilotos.

**Condiciones:**
1. v1 de una sola página, con el mínimo de la sección 4.1. Sin precios, pagos, cuentas de usuario ni chat con IA.
2. Solo Yizi Solutions se ofrece. Publisher y Talent como "próximamente". Projects solo como visión, sin toFinance ni plan de comidas por nombre.
3. Ninguna cifra, cliente o resultado sin fuente. Etapa temprana dicha con claridad. Inversionistas: solo "conversemos".
4. El abogado revisa los textos legales y el mensaje a inversionistas antes de publicar.
5. Contacto con número y correo del negocio, nunca los personales del CEO.
6. Lince verifica y el CEO confirma la publicación, en ese orden.
