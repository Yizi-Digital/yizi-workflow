# Fiesteros · Revisión legal de Temis

> **Borrador — requiere revisión de abogado colegiado.** Temis no es abogada y no da asesoría legal vinculante. Fecha: 2026-11-18.

## Respuesta corta

Fiesteros puede pasar al gobierno de Yizi, pero primero hace falta un acuerdo escrito con el cliente. Hoy no se sabe si existe uno. El dominio, las cuentas de redes y el diseño deben estar a nombre del cliente. Yizi debe entrar como socio con acceso, no como dueño.

## Qué no pude verificar

- **La web no se pudo abrir.** WebFetch falló: `fiesteros.shop` no resuelve desde esta sesión. Hay que permitir ese dominio en la red de la sesión y repetir la revisión.
- Por eso todo lo que sigue sobre el contenido de la web (formularios, pedidos, política de privacidad, términos, Libro de Reclamaciones) está **no verificado**.
- No leí el texto oficial de los artículos concretos de las leyes. Cito solo el nombre de la norma. Los números de artículo quedan para el abogado.

## 1. Qué hace falta para que el cliente sea cliente de Yizi

Hoy Yizi opera con el RUC 10 del CEO (spec `marco-legal`, requisito "RUC con el que opera Yizi"). El servicio original lo hizo el CEO como persona natural, antes de Yizi. Pasarlo a Yizi es un cambio de marco. Conviene dejarlo por escrito.

Acuerdo escrito simple. Contenido mínimo:

| Punto | Qué debe decir |
|---|---|
| Partes | Cliente (nombre o razón social y RUC) y CEO con su RUC 10, que opera bajo la marca Yizi. |
| Alcance | Qué hace Yizi: mantener la web, gestionar Instagram y Facebook. Qué no hace. |
| Precio | Monto, moneda, fecha de pago, comprobante. Si el trabajo anterior fue gratis o ya pagado, decirlo. |
| Propiedad | Dominio, hosting, cuentas y contenido a nombre del cliente (ver punto 2). |
| Confidencialidad | Ambas partes guardan reserva de la información del negocio y de los clientes finales. |
| Datos personales | Quién es responsable y quién encarga el tratamiento (ver punto 3). |
| Referencia | Si el cliente permite o no usarlo como caso (ver punto 4). |
| Fin del servicio | Cómo se termina, con qué aviso, y qué entrega Yizi: accesos, copias y archivos. |
| Trabajo previo | Que el trabajo hecho antes de Yizi queda cubierto por este acuerdo, sin cambiar lo ya pactado. |

Pasos sugeridos:
1. El CEO confirma los hechos de la sección 5.
2. Temis prepara un borrador de una o dos páginas.
3. Un abogado colegiado lo revisa.
4. El CEO decide si lo firma. Temis no firma ni envía nada.
5. Un contador revisa el comprobante y el RUC (tema tributario: Edith y contador).

## 2. Propiedad: dominio, cuentas, código y diseño

**Recomendación de Temis:** todo a nombre del cliente. Yizi entra con acceso de socio o administrador delegado.

| Activo | Lo correcto | Cómo entra Yizi |
|---|---|---|
| Dominio `fiesteros.shop` | Registrado a nombre del cliente. | Acceso delegado del registrador, si lo permite. |
| Hosting o plataforma | Cuenta del cliente. | Usuario adicional con permisos limitados. |
| Instagram y Facebook | Página y cuenta del cliente. | Rol de socio o administrador en Meta. No se comparte la contraseña. |
| Contenido (textos, fotos, logo) | Del cliente, o con licencia escrita para usarlo. | Licencia de uso para operar la cuenta. |
| Código y diseño de la web | Por defecto, el autor es quien lo creó: el CEO. | Acuerdo escrito: o cede al cliente, o le da licencia de uso. |

Norma de apoyo: Decreto Legislativo 822, Ley sobre el Derecho de Autor. Fuente: https://www.wipo.int/wipolex/es/legislation/details/18762 (consulta 2026-11-18). **No verificado** el texto de los artículos sobre software y cesión. Lo que sé en general: el software se protege como obra, y la cesión de derechos suele pedirse por escrito. El abogado debe confirmarlo.

Riesgo: si hoy el dominio o las cuentas están a nombre del CEO, el cliente podría reclamar su control. Si están a nombre del cliente y Yizi no tiene rol, Yizi no puede operar. Hay que saber cuál es el caso. Riesgo medio.

Revisar también las licencias de terceros (plantilla, tema, plugins, fuentes, fotos) y confirmar que permiten uso comercial para un cliente. **No verificado**: no vi qué usa la web.

## 3. Datos personales y consumidor

### Datos personales (Ley 29733)

- Norma: Ley 29733, Ley de Protección de Datos Personales, y su reglamento D.S. 016-2024-JUS. Fuente: https://www.gob.pe/institucion/anpd/normas-legales/6554453-16-2024-jus (consulta 2026-11-18). La vigencia del reglamento desde el 29 de marzo de 2025 viene de fuentes secundarias. **No verificado** en el texto oficial.
- Spec `marco-legal`, requisito "Datos personales": pedir consentimiento informado, no usar los datos para otro fin y revisar con el abogado la inscripción del banco de datos y el texto de consentimiento.

**Quién es responsable (hipótesis):** quien decide para qué se recogen los datos suele ser el titular del negocio, es decir, el cliente. Yizi, si opera la web, sería quien encarga o apoya el tratamiento. El abogado debe confirmar los roles y reflejarlos en el acuerdo. **No verificado.**

**Qué revisar en la web (todo no verificado, porque no pude abrirla):**

| Elemento | Qué mirar | Estado |
|---|---|---|
| Formularios de contacto o pedido | ¿Piden nombre, teléfono, correo, dirección? | No verificado |
| Política de privacidad | ¿Existe, es visible y dice fin, plazo y derechos? | No verificado |
| Consentimiento | ¿Hay casilla o aviso antes de enviar datos? | No verificado |
| Banco de datos | ¿Está inscrito ante la autoridad, si corresponde? | No verificado |
| Terceros | ¿Usa analítica, píxel de Meta, WhatsApp, pasarela de pago? | No verificado |
| Mensajes de Instagram y Facebook | Los datos de clientes finales también cuentan. | No verificado |

Si la web recoge datos y no tiene política ni consentimiento, el riesgo es **alto** hasta que se corrija. Si no recoge datos, baja a bajo. Un riesgo alto va a Herbie y al CEO de inmediato. Hoy no puedo confirmar ninguno de los dos casos.

Si los datos van a servicios externos, avisar a Cerbero, Vision y el CEO.

### Consumidor (Ley 29571)

- Norma: Ley 29571, Código de Protección y Defensa del Consumidor. Fuente: https://diariooficial.elperuano.pe/Normas/obtenerDocumento?idNorma=17 (consulta 2026-11-18). **No verificado** el texto de los artículos.
- Lo que sé en general: los proveedores deben tener un Libro de Reclamaciones. Existe una modalidad virtual para quien vende en línea. El número de artículo, el reglamento aplicable y el alcance exacto **no están verificados**. El abogado debe confirmarlos.
- Si la web **vende o toma pedidos en línea**, hay que revisar: Libro de Reclamaciones visible, datos del proveedor (razón social, RUC, dirección), precios claros con impuestos, condiciones de entrega y cambios, y publicidad veraz.
- Si la web es solo una vitrina sin venta ni pedido, el alcance puede ser menor. **No verificado**; depende de lo que haga la web.
- Estado hoy de Libro de Reclamaciones, términos y condiciones, y datos del proveedor en la web: **no verificado**.

Yizi no custodia dinero (spec `marco-legal`). Si la web cobra, el pago debe pasar por una pasarela autorizada a nombre del cliente.

## 4. Permiso para usarlo como caso de referencia

Hoy no hay permiso conocido. Reglas:

1. No publicar el nombre, logo, capturas ni resultados de Fiesteros sin permiso escrito del cliente.
2. El permiso debe decir: qué se muestra, dónde (web, redes, propuestas), por cuánto tiempo y cómo retirarlo.
3. No inventar cifras ni resultados del caso (regla 4 de AGENTS.md). Cada cifra necesita fuente y fecha.
4. No mostrar datos personales de clientes finales ni capturas con ellos.
5. Si el cliente dice que no, se usa como caso anónimo o no se usa.
6. Publicar es una acción hacia afuera: confirmación del CEO, cada vez.

## 5. Preguntas para el CEO (sin credenciales)

Prioridad de arriba hacia abajo.

1. ¿Existe hoy algún contrato, mensaje o acuerdo con el cliente? ¿Qué dice sobre precio y propiedad?
2. ¿A nombre de quién están el dominio, el hosting y las cuentas de Instagram y Facebook: del cliente, tuyo u otro?
3. ¿El cliente paga algo hoy? ¿Qué, cuánto y con qué comprobante?
4. ¿La web recibe pedidos, pagos o formularios? ¿O solo muestra información?
5. ¿Qué datos de personas llegan (nombre, teléfono, dirección) y dónde se guardan?
6. ¿Qué plantilla, tema, plugins, fotos y fuentes usa la web? ¿De quién son?
7. ¿El cliente acepta ser caso de referencia? ¿Con qué límites?
8. ¿Quién es el cliente: persona natural o empresa, y con qué RUC?
9. ¿Quieres que se pase a cesión de derechos del código y diseño al cliente, o una licencia de uso?
10. ¿Puedes pedir que se permita el dominio `fiesteros.shop` en la red de la sesión, para revisar la web?

## Qué escala Temis

| Tema | A quién |
|---|---|
| Acuerdo, cesión de derechos, interpretación de normas | Abogado colegiado y CEO |
| Firmar o publicar cualquier documento | CEO, con abogado |
| Riesgo alto de datos personales en la web | Herbie y CEO de inmediato (si se confirma) |
| RUC, comprobantes e impuestos | Edith y contador |
| Datos hacia servicios externos | Cerbero, Vision y CEO |
