# Auditoría técnica de fiesteros.shop · Vision (CTO)

Fecha: 2026-11-18. Método: solo lectura pública con `curl` de la portada, del código JavaScript y de la hoja de estilos que la web entrega a cualquier visitante. No entré a paneles ni hice escaneos. Instagram, Facebook y el sitio del Libro de Reclamaciones siguen bloqueados en la red de la sesión: **no revisados**.

**Resumen:** es una web de una sola página para vender bocaditos para fiestas en Lima. Está bien hecha y funciona. Todo pedido se cierra por WhatsApp y no hay pagos en línea. Lo débil es el SEO, la falta de política de privacidad y que no se sabe quién es dueño de las cuentas.

## 1. Qué es

| Punto | Hallazgo |
|---|---|
| Negocio | "Fiesteros · Bocaditos Salados". Cocina de bocaditos artesanales (tequeños, mini burguers, empanaditas, petipanes) con delivery en Lima Metropolitana, Perú. |
| Qué ofrece la web | Catálogo con 8 productos y precios en soles (combos de S/. 105, 210 y 380, y unidades de S/. 30 a 40). Secciones "Nosotros" y "Preguntas frecuentes". Un cotizador para armar el pedido. |
| Tecnología | Aplicación React compilada con Vite, con React Router y animaciones de Framer Motion. Alojada en **Vercel** (cabecera `server: Vercel`). Fuentes de Google Fonts. Coincide con el stack de referencia de Yizi. |
| Tienda o pagos | **No hay pago en línea.** El cotizador arma un mensaje y abre WhatsApp. Según las preguntas frecuentes, se paga con Yape, Plin o transferencia (BCP, BBVA, Interbank). |
| Formulario | El cotizador pide nombre, teléfono, fecha y hora del evento, dirección, distrito, número de invitados y notas. Los datos **no van a un servidor**: el navegador los pone en un mensaje de WhatsApp. No encontré llamadas a ninguna base de datos ni API. |
| WhatsApp | Sí. Varios botones llevan a un número de Perú (+51) con mensajes ya escritos. |
| Redes sociales | **La web no enlaza a Instagram ni a Facebook.** No encontré ningún enlace a redes en el código. |
| Libro de Reclamaciones | Hay un botón en el pie de página: "Libro de Reclamaciones Virtual - Conforme a Ley N° 29571". Lleva a `gestor-de-reclamos-fiesteros.ai.studio`, un sitio aparte. No revisado (bloqueado). |
| Modo mantenimiento | El código trae una pantalla de "web en mantenimiento". Está apagada por defecto. |
| Analítica | No encontré Google Analytics, píxel de Meta ni otro rastreador. |

**Texto con instrucciones:** no encontré texto dirigido a agentes de IA. Solo un comentario HTML: "New APP IS PROPERTY TO FIESTEROS PE". Lo anoto como dato: sugiere que el cliente se considera dueño de la aplicación.

## 2. Estado técnico visible

| Punto | Estado | Detalle |
|---|---|---|
| HTTPS | Bien | Certificado válido. HSTS (obliga a usar HTTPS) por 2 años. `www.fiesteros.shop` redirige al dominio sin `www`. |
| Velocidad | Aceptable | La portada respondió en 0,5 s desde la caché de Vercel. El JavaScript pesa 447 KB (142 KB comprimido). En celular con red lenta, la página queda en blanco hasta que carga ese archivo, más una pantalla de carga de 2 s. Sin medición con PageSpeed: **no verificado**. |
| Celular | Probablemente bien | Tiene la etiqueta `viewport` y usa diseño adaptable (clases `sm:` y `md:`). No probado en un teléfono real. |
| Errores visibles | Uno | Rutas como `/catalogo` responden 404 del servidor. Hoy no afecta porque la web es de una sola página. |
| SEO básico | Débil | Tiene título ("Fiesteros \| Bocaditos Salados") e idioma `es`. **No tiene** meta descripción, etiquetas para compartir en redes (Open Graph), `robots.txt` ni `sitemap.xml`. El contenido solo aparece con JavaScript, así que algunos buscadores y vistas previas de WhatsApp ven una página vacía. |
| Accesibilidad | Regular | Las imágenes son dibujos SVG dentro del código, sin texto alternativo. No hay etiquetas `aria-label` en botones de icono. Hay textos de 10 a 11 px, pequeños para leer en celular. No revisé el contraste. |
| Seguridad | Aceptable | No hay secretos ni claves en el código. No expone mapas de código fuente. Faltan cabeceras de seguridad (CSP, X-Frame-Options, Referrer-Policy). El riesgo es bajo porque no hay inicio de sesión ni pagos. |
| Privacidad y términos | **No existen** | No hay política de privacidad, términos ni aviso de cookies. `/privacidad` y `/terminos` dan 404. |

## 3. Riesgos

| Riesgo | Qué sabemos | Qué hacer |
|---|---|---|
| Cuenta de Vercel | La web vive en Vercel. No sabemos a nombre de quién está la cuenta. | Pasar el proyecto a un equipo (*team*) de Vercel de Yizi o del cliente. Dar acceso por invitación a cada persona. |
| Dominio `fiesteros.shop` | No sabemos el registrador ni el titular. Los `.shop` se renuevan cada año. | Confirmar titular y vencimiento. Activar renovación automática y bloqueo de transferencia. Decidir con el cliente quién es titular. |
| Código fuente | No sabemos dónde está el repositorio. Si solo está en el equipo del CEO, se puede perder. | Subirlo a un repositorio de la organización Yizi-Digital o del cliente. |
| Libro de Reclamaciones en `ai.studio` | Parece una app hecha con una herramienta de IA, fuera de Vercel. No sabemos quién la administra ni dónde se guardan los reclamos. | Confirmar la cuenta, dónde quedan los datos y quién responde en plazo. |
| Instagram y Facebook | No revisados. La web no los enlaza. | Crear un portafolio comercial de Meta a nombre del cliente. Yizi entra como socio con rol asignado. Nunca compartir contraseñas. |
| Correo de recuperación | Desconocido. Quien controla ese correo controla las cuentas. | Usar un correo de empresa y verificación en dos pasos en cada cuenta. |
| Contraseñas | No deben pasar por el chat ni por el repositorio (regla 5 del núcleo). | Usar invitaciones y roles. Si hace falta una clave, guardarla en un gestor de contraseñas con bóveda compartida. |
| Copias de seguridad | Vercel guarda los despliegues anteriores, pero eso no reemplaza al código fuente. | Repositorio remoto con el código, más una copia de textos y logos. |

## 4. Mejoras priorizadas (Publisher, solo remoto con IA)

1. **Inventario de accesos.** Tabla con Vercel, dominio, repositorio, sitio de reclamos, Meta y correo. Titular y vencimiento. Sin contraseñas.
2. **Pasar accesos al modelo de roles:** equipo en Vercel, socio en Meta, repositorio en la organización.
3. **Política de privacidad** visible junto al cotizador, porque pide nombre, teléfono y dirección. La redacta la IA y la revisan Temis y el abogado externo.
4. **SEO y vista previa:** meta descripción, Open Graph con imagen, `robots.txt` y `sitemap.xml`.
5. **Enlaces a Instagram y Facebook** en la web, cuando sepamos qué cuentas son del cliente.
6. **Accesibilidad:** texto alternativo en los dibujos, `aria-label` en botones de icono y textos de al menos 12 px.
7. **Rendimiento en red lenta:** quitar o acortar la pantalla de carga de 2 s y medir con PageSpeed antes y después.
8. **Cabeceras de seguridad** en `vercel.json` (CSP, X-Frame-Options, Referrer-Policy). Es un cambio pequeño.

## 5. Para Temis (legal)

| Punto | Hallazgo |
|---|---|
| Política de privacidad | **No existe.** |
| Términos y condiciones | **No existen.** |
| Aviso de cookies | No hay. Tampoco encontré cookies de rastreo. La web guarda una marca en `sessionStorage`, el almacén temporal del navegador, que no es una cookie. |
| Libro de Reclamaciones | **Sí hay un enlace**, que cita la Ley N° 29571 (Código de Protección y Defensa del Consumidor de Perú). Lleva a un sitio externo en `ai.studio`, no revisado. Falta comprobar si cumple el formato oficial y quién lo atiende. |
| Formularios que recogen datos | **Sí.** El cotizador pide nombre, teléfono, dirección, distrito, fecha y notas. Los datos van por WhatsApp al negocio y no se guardan en un servidor. Aun así, el negocio recibe datos personales. Temis debe revisar la Ley N° 29733 de Protección de Datos Personales. |
| Pagos en línea | **No.** El pago se coordina por WhatsApp con Yape, Plin o transferencia. |
| Datos del proveedor | No encontré razón social ni RUC en la web. |

### Vision · Viabilidad técnica
**Veredicto:** CONDICIONADO
**Motivos:**
- La web es simple y estable: React con Vite en Vercel, sin servidor propio, sin pagos y sin secretos en el código.
- Pasarla al gobierno de Yizi es viable y remoto: casi todo es ordenar cuentas y roles.
- Riesgo principal: no sabemos quién es titular de Vercel, del dominio, del código, del sitio de reclamos ni de Meta.
- Hay un hueco legal: el cotizador recoge datos personales y no hay política de privacidad.
**Condiciones:**
- Inventario de accesos completo y sin contraseñas antes de tocar nada.
- Política de privacidad revisada por Temis y el abogado externo antes de mejorar el cotizador.
- Revisión de Instagram, Facebook y el sitio de reclamos cuando la red lo permita.
- Confirmación del CEO antes de desplegar, mover el dominio o publicar en redes.
- Lince u otro agente verifica cualquier cambio que yo implemente.
