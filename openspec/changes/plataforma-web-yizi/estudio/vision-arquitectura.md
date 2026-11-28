# Plataforma web de Yizi Digital · Arquitectura (Vision, CTO)

Fecha: 2026-11-28. Estado: estudio, sin aprobar. Base: `pedido-del-ceo.md`, specs `arquitectura` y `calidad`, Manual de Marca.

**Respuesta corta:** la web vive en un repo propio, `Yizi-Digital/yizi-web`. Propongo Astro, que usa Vite por dentro y React solo donde hay interacción. Cada página sale como HTML listo. Así carga rápido en celular con red lenta y se lee sin JavaScript. Se aloja en Vercel, con vistas previas por PR. Producción sale solo con la confirmación del CEO.

Nada de este estudio autoriza construir. Primero va el cambio OpenSpec, el Consejo y la aprobación del CEO (reglas 1 y 2).

---

## 1. Dónde vive el código

| Qué | Dónde | Por qué |
|---|---|---|
| Código de la web | Repo nuevo `Yizi-Digital/yizi-web` (lo crea el CEO) | El núcleo guarda reglas, no código de producto. Un repo por web da permisos y despliegues claros. |
| Plan y decisiones | Este cambio, `openspec/changes/plataforma-web-yizi/` del núcleo | La web es del grupo, no de un satélite. Alcance: `nucleo`. |
| Reglas para agentes en el repo | `AGENTS.md` y `CLAUDE.md` cortos que apuntan al núcleo | No se copian specs; se citan (regla 7 de los satélites, aplicada aquí igual). |
| Cambios futuros de la web | Cambios OpenSpec del núcleo con alcance `nucleo` | Un solo lugar para decidir qué se publica. |

**Repo público o privado (decide el CEO).** Recomiendo **público**:
1. El sitio es público por naturaleza. El código no tiene secretos.
2. En GitHub, la protección de la rama principal y el escaneo de secretos son gratis en repos públicos. En repos privados de una organización gratuita, la protección de rama pide un plan de pago. *No verificado hoy*; lo confirma quien cree el repo.
3. Los borradores (por ejemplo, textos para inversionistas) no entran al repo hasta que el CEO los apruebe. Viven en este cambio del núcleo.

Si el CEO prefiere privado, Edith cotiza el plan de GitHub que permite proteger la rama.

Estructura propuesta del repo:

```
yizi-web/
  src/pages/            páginas en español (raíz) y en/ para inglés
  src/content/          textos en Markdown, uno por página (los prepara Jarvis)
  src/components/       componentes de Astro; React solo en "islas" interactivas
  src/styles/tokens.css colores, tipografías y espacios del Manual de Marca
  src/pages/api/        función serverless del formulario (fase 4)
  public/fonts/         fuentes alojadas en el propio sitio
  tests/                pruebas de Playwright (celular, sin JavaScript, accesibilidad)
  lighthouserc.json     metas de Lighthouse que bloquean un PR si no se cumplen
  vercel.json           cabeceras de seguridad
  .github/workflows/    integración continua (CI)
```

## 2. Stack y por qué

### 2.1 Decisión: Astro con React en islas (desviación justificada del stack)

La spec `arquitectura` pide React + Vite por defecto y exige justificar otro stack en `design.md`. Esta es la justificación.

| Opción | Sin JavaScript | Rendimiento en celular | Encaje con el stack | Riesgo |
|---|---|---|---|---|
| A. React + Vite como aplicación de una página (SPA) | No: la página sale en blanco | Bajo con red lenta: hay que bajar todo el JS antes de ver algo | Total | Es el fallo que vi en la web de Fiesteros (`vision-auditoria.md`) |
| B. React + Vite con pre-renderizado (plugin SSG) | Sí | Bueno, pero cada página carga React completo para "hidratarse" | Total | Plugins pequeños, con menos mantenimiento |
| **C. Astro (usa Vite) + React solo en islas** | **Sí** | **El mejor: 0 KB de JS en páginas sin interacción** | **Alto: Vite por dentro, componentes React donde hagan falta** | Otro framework que aprender; dueño nuevo (abajo) |
| D. Next.js | Sí | Bueno, pero más pesado para un sitio de contenido | Medio: no usa Vite | Más complejo; más atado a Vercel |

**Decisión propuesta: C.** Primero lo simple que funciona. Un sitio para vender es contenido, no una aplicación. Astro entrega HTML y CSS, y solo añade JavaScript donde hay interacción.

**Lo que Astro trae y nos ahorra:**
1. Rutas por idioma (`/` en español, `/en/` en inglés).
2. Optimización de imágenes a AVIF y WebP, con tamaños por pantalla.
3. Política de seguridad de contenido (CSP) integrada en Astro 6.
4. Transiciones entre páginas sin cargar una aplicación entera.

**Riesgo del dueño.** Cloudflare compró la empresa de Astro el 16 de enero de 2026. Anunció que Astro sigue de código abierto y que funciona en cualquier alojamiento (blog de Astro y nota de prensa de Cloudflare, consultadas con buscador el 2026-11-28). Mitigación: usamos salida estática, que no depende de ningún proveedor. Si un día hiciera falta salir de Astro, el HTML, el CSS y los componentes React se mueven a la opción B.

**Consecuencia:** esta desviación debe quedar en `design.md` del cambio. Yo la propongo; la revisan el Consejo y Lince, y la aprueba el CEO.

### 2.2 Calidad visual "de primer nivel" sin pesar

El nivel de Apple o Tesla se logra con orden, espacio, buena tipografía y fotos grandes. No con librerías pesadas. No copiamos su marca ni su diseño.

| Tema | Regla |
|---|---|
| Animaciones | CSS primero: transiciones, animaciones ligadas al scroll y transiciones de vista. Sin librerías de animación en la carga inicial. Si una sección las necesita, va en una isla que carga al verse. |
| Movimiento reducido | Si el usuario pide menos movimiento (`prefers-reduced-motion`), las animaciones se apagan. Nada se mueve solo más de 5 segundos sin un botón para pausarlo. |
| Imágenes | AVIF con respaldo WebP, tamaños por pantalla, ancho y alto declarados (la página no salta). La imagen principal pesa 150 KB o menos en celular. Las demás cargan al acercarse. |
| Video | Sin video automático en celular. Si hay video, tiene imagen de portada y no se descarga con red lenta o "ahorro de datos". |
| Fuentes | Montserrat o Poppins para títulos e Inter u Open Sans para texto (Manual de Marca, 8.3). Alojadas en el propio sitio, recortadas a los caracteres del español y del inglés, máximo 2 pesos por familia. No se llama a Google Fonts: es más rápido y no comparte datos del visitante. |
| Colores | Solo los del Manual (8.1 y 8.2). Ver la alerta de contraste abajo. |
| Fotos y material | Con derechos de uso claros. Sin clientes inventados. Fiesteros solo aparece con permiso escrito. Lo decide Jarvis. |

**Alerta de contraste (calculada por Vision, fórmula de WCAG):**

| Combinación | Contraste | ¿Pasa AA para texto normal (4,5:1)? |
|---|---|---|
| Ámbar #F59E0B sobre Blanco #FFFFFF | 2,15:1 | **No** |
| Ámbar #F59E0B sobre Gris #F8FAFC | 2,05:1 | **No** |
| Índigo #1E3A8A sobre Ámbar #F59E0B | 4,82:1 | Sí |
| Azul #2563EB sobre Blanco | 5,17:1 | Sí |
| Azul #2563EB sobre Gris #F8FAFC | 4,94:1 | Sí |
| Gris Texto #334155 sobre Blanco | 10,35:1 | Sí |
| Índigo #1E3A8A sobre Blanco | 10,36:1 | Sí |

Regla: el Ámbar nunca va como color de texto sobre fondo claro. Sirve para fondos de botones con texto Índigo, para íconos grandes y para detalles. No hace falta cambiar el Manual; es una regla de uso. Jarvis la confirma.

### 2.3 Multilenguaje

1. **Español primero** (`es-PE`), en la raíz del sitio.
2. **Inglés opcional** en `/en/`, pensado para inversionistas. Puede salir en una fase posterior (fase 5).
3. Los textos viven en archivos de contenido, separados del código. Jarvis los prepara sin tocar componentes.
4. Ningún texto traducido por máquina se publica sin revisión humana.
5. Cada página declara su idioma y enlaza su versión en el otro idioma (`hreflang`), para buscadores y lectores de pantalla.

### 2.4 Qué páginas tiene (estructura, no textos)

Los textos son de Jarvis, el encuadre estratégico de Viernes y las cifras de Edith. Aquí solo fijo la estructura y los límites técnicos.

| Página | Qué hace | Límite del núcleo |
|---|---|---|
| Inicio | Presenta el grupo y las cuatro líneas | Sin cifras ni resultados inventados (regla 4) |
| Yizi Solutions | Vende: es la única línea activa que ofrece servicios | Llamada a la acción: diagnóstico |
| Yizi Projects | Presenta la casa de productos propios | No vende servicios. Productos solo si Viernes los aprueba para mostrarse. toFinance está pausado. |
| Yizi Publisher y Yizi Talent | "Próximamente" o visión | En incubación: no se venden (regla 6) |
| Inversionistas | Cuenta la visión y la etapa real: temprana | Sin ofrecer inversión hasta que el abogado lo revise (sección 4.5) |
| Contacto o diagnóstico | WhatsApp, correo y formulario | Sección 4 |
| Privacidad | Aviso de privacidad (Ley 29733) | Lo revisa un abogado colegiado |

Ante el público la identidad visible es **El Guía Yizi**. Ningún nombre interno de agente aparece en la web.

### 2.5 IA en la web

La fase 1 **no usa IA en el sitio**: no hay chat ni respuestas automáticas. Así no hay costo por visita ni riesgo de inyección de instrucciones. Si más adelante se suma El Guía Yizi como asistente en la web, va en un cambio propio que declare modelo, costo por uso, respaldo si falla y revisión humana (spec `arquitectura`).

## 3. Metas medibles

Cada meta tiene una prueba. Si una prueba automática falla, el PR no se puede fusionar.

| Meta | Valor | Cómo se mide | Tipo |
|---|---|---|---|
| Lighthouse en celular: rendimiento, accesibilidad, buenas prácticas y SEO | 95 o más en las cuatro, en cada página | Lighthouse CI sobre la vista previa de cada PR; mediana de 3 corridas | Automática |
| Mostrar lo principal (LCP) | 2,5 s o menos | Lighthouse en modo celular (simula una red 4G lenta) | Automática |
| Respuesta al tocar (INP) | 200 ms o menos | Datos reales de Vercel Speed Insights, cuando haya tráfico | Automática |
| Saltos de la página (CLS) | 0,1 o menos | Lighthouse y datos reales | Automática |
| Peso de JavaScript | 0 KB en páginas sin interacción; 50 KB comprimido como máximo en cualquier página | Presupuesto en `lighthouserc.json` | Automática |
| Peso total de la portada en celular | 600 KB o menos en la primera vista | Presupuesto en `lighthouserc.json` | Automática |
| Accesibilidad WCAG 2.2 nivel AA | Sin fallos de axe-core; revisión manual sin fallos | axe-core con Playwright en cada página, más la lista manual de abajo | Automática y manual |
| Funciona sin JavaScript | Se leen todos los textos, funciona el menú y se envía el formulario | Playwright con JavaScript apagado | Automática |
| Funciona en celular | Pantallas de 360 px a 430 px de ancho, sin desplazamiento horizontal | Playwright en tamaños de celular, más un celular real | Automática y manual |
| Red lenta real | La portada se lee y el contacto funciona | Prueba en un celular real con red 3G simulada; se registra pasos, resultado y fecha | Manual (spec `calidad`) |
| Enlaces | Ninguno roto | Revisor de enlaces en CI | Automática |

Los umbrales de LCP, INP y CLS son los que Google llama "buenos" (web.dev, *Web Vitals*; no reabierto hoy). Los presupuestos de peso son propuesta mía, no un estándar externo.

**Revisión manual de accesibilidad (WCAG 2.2 AA),** con evidencia escrita en cada fase:
1. Todo se usa solo con teclado y el foco siempre se ve, sin quedar tapado (2.4.7 y 2.4.11).
2. Botones y enlaces miden al menos 24 × 24 px (2.5.8).
3. Un lector de pantalla (VoiceOver en iPhone o TalkBack en Android) recorre la portada y el formulario.
4. Cada imagen con contenido tiene texto alternativo útil.
5. Los errores del formulario dicen qué falta y cómo corregirlo.
6. La ayuda (WhatsApp y correo) está en el mismo lugar en todas las páginas (3.2.6).
7. El texto se agranda al 200 % sin perder contenido.

Los números de criterio salen de WCAG 2.2 (Recomendación W3C del 5 de octubre de 2023); el texto oficial no se reabrió hoy.

## 4. Formularios y datos

### 4.1 Principio: Yizi no guarda datos en la web

La web **no tiene base de datos**. No guarda lo que escribe el visitante. Recibe el mensaje y lo reenvía a un buzón de Yizi. Nunca pide datos sensibles: ni DNI, ni datos bancarios, ni de salud.

### 4.2 Canales de contacto, por fase

| Canal | Fase | Cómo funciona | Datos que pasan por Yizi |
|---|---|---|---|
| Botón de WhatsApp | 3 (lanzamiento) | Enlace `wa.me` con un texto inicial. El visitante decide si escribe. Funciona sin JavaScript. | Ninguno en la web; la conversación queda en el WhatsApp Business de Yizi |
| Correo | 3 (lanzamiento) | Enlace `mailto:` a un buzón del dominio de Yizi | Ninguno en la web |
| Formulario de diagnóstico | 4 | Formulario HTML normal que envía a una función serverless. La función valida y manda un correo al buzón de Yizi. | Nombre, forma de contacto, tipo de negocio y mensaje. Solo en tránsito. |

El formulario pide lo mínimo: nombre, correo o celular, tipo de negocio, línea de interés y mensaje. Nada más.

### 4.3 Cómo se envía el formulario sin perder mensajes

1. Funciona sin JavaScript: el navegador envía el formulario y la función responde con una página de "Gracias" o de error.
2. Con JavaScript, el envío se hace sin recargar y el botón se desactiva al pulsarlo (evita doble envío).
3. La función valida cada campo en el servidor: tipo, largo máximo y formato. Rechaza lo demás.
4. Si el proveedor de correo falla, el visitante ve un mensaje claro y el botón de WhatsApp. El mensaje no se pierde en silencio.
5. La función registra el error **sin datos personales** (solo hora y tipo de fallo). Vision recibe una alerta.
6. Un doble envío produce, como máximo, dos correos iguales. No es un pedido ni un cobro, así que lo acepto sin guardar estado. Lo dejo escrito para que sea una decisión, no un olvido.

El envío de correo necesita un proveedor de correo transaccional y una clave de API. La clave vive solo en las variables de entorno de Vercel. Edith cotiza el proveedor; el abogado revisa que ese proveedor trate datos fuera del Perú (flujo transfronterizo de la Ley 29733).

### 4.4 Consentimiento y aviso de privacidad (Ley 29733)

1. Casilla de consentimiento **sin marcar** junto al botón de enviar, con enlace al aviso de privacidad.
2. Sin la casilla marcada, el formulario no se envía. Esto también se valida en el servidor.
3. El aviso dice: quién trata los datos (Yizi, con el RUC 10 del CEO mientras no haya persona jurídica, spec `marco-legal`), para qué, cuánto tiempo se guardan en el buzón, con quién se comparten (proveedor de correo y de alojamiento) y cómo pedir acceso o borrado.
4. Los datos solo se usan para responder al contacto. No van a listas de publicidad sin otro consentimiento aparte.
5. El buzón que recibe los mensajes es, en la práctica, un banco de datos. La spec `marco-legal` pide revisar con el abogado su inscripción ante la autoridad antes de lanzar el formulario.
6. El texto del aviso lo redacta Jarvis (o Temis como borrador legal) y lo revisa un **abogado colegiado** antes de publicarse.

### 4.5 Temas para el abogado (no verificados por Vision)

| Tema | Pregunta |
|---|---|
| Libro de Reclamaciones virtual | ¿La web lo necesita si no vende en línea? La norma pide avisarlo en la portada a quien vende por internet (DS 006-2014-PCM y DS 101-2022-PCM, según buscador). Sin texto consolidado revisado. |
| Página de inversionistas | ¿Qué se puede decir sin que cuente como oferta de inversión? Hasta su respuesta, la página solo invita a conversar. |
| Inscripción del banco de datos | ¿Hay que inscribir el buzón de contactos ante la autoridad de datos personales? |

### 4.6 Protección contra spam

En orden, de lo más simple a lo más fuerte. Se sube de nivel solo si aparece spam.
1. Campo trampa oculto (*honeypot*): si un robot lo llena, el mensaje se descarta.
2. Tiempo mínimo: un envío en menos de 3 segundos tras abrir la página se descarta.
3. Límite de envíos por dirección de red en la función.
4. Si aun así llega spam: un desafío sin imágenes (por ejemplo, Cloudflare Turnstile o la protección contra robots de Vercel). Es un script de terceros; entra con su propio análisis de privacidad.

### 4.7 Analítica respetuosa

**Propuesta: Vercel Web Analytics y Speed Insights.** Vercel dice que Web Analytics no usa cookies de terceros, que identifica visitas con un resumen cifrado (*hash*) de la petición y que por defecto solo da datos agregados (documentación de Vercel, consultada con buscador el 2026-11-28; no se sabe cómo se forma ese resumen). Así no hace falta un aviso de cookies.

Reglas:
1. Sin Google Analytics, sin píxeles de Meta y sin cookies de terceros.
2. Ningún evento lleva datos personales (ni el texto del formulario).
3. Se mide solo lo útil: visitas por página, clics en WhatsApp, envíos del formulario y velocidad real.
4. El aviso de privacidad menciona la analítica.

## 5. Despliegue

| Tema | Propuesta |
|---|---|
| Alojamiento | Vercel, en un equipo (*team*) de Yizi con plan **Pro**. El plan gratis (Hobby) es solo para uso personal y no comercial; esta web es comercial. |
| Costo de referencia | Pro: 20 USD al mes por asiento de desarrollador, con el primero incluido en la cuota; asientos de solo lectura sin costo (precios de vercel.com vistos con buscador el 2026-11-28; texto completo no leído). **Edith confirma** el costo y si se usa el equipo existente de Yizi o uno nuevo "Yizi Digital". |
| Alternativa | Cloudflare (Pages o Workers) o Netlify, con salida estática. Las condiciones de uso comercial de sus planes gratis: **no verificadas**. Se evalúan solo si Edith lo pide. Como el sitio es estático, cambiar de alojamiento es simple. |
| Dominio | **Pregunta para el CEO:** ¿Yizi ya tiene un dominio? ¿Cuál quieres usar (por ejemplo, terminado en .com o en .pe)? ¿A nombre de quién está? No propongo ninguno: no sé cuál existe. |
| Correo del dominio | Para recibir contactos hace falta un buzón en el dominio, con registros SPF, DKIM y DMARC para que los correos no caigan en spam. Edith cotiza el servicio de correo. |
| HTTPS | Automático en Vercel, con redirección de HTTP a HTTPS. |
| Vistas previas | Cada PR crea una vista previa con su propia dirección. Ahí corren Lighthouse CI y las pruebas. Las vistas previas quedan protegidas con inicio de sesión de Vercel y no se indexan en buscadores (*no verificado hoy* que venga activo por defecto; se configura al crear el proyecto). |
| Producción | Vercel publica a producción al fusionar en `main`. **Fusionar en `main` lo hace o lo confirma el CEO, cada vez** (regla 2). Opción más estricta: apagar la asignación automática del dominio y que el CEO "promueva" cada versión a mano. |
| Volver atrás | Vercel guarda las versiones anteriores. Si algo sale mal, se vuelve a la anterior con confirmación del CEO. |

Ningún agente despliega a producción, fusiona en `main` ni conecta el dominio. Lo hace el CEO o se hace con su confirmación explícita.

## 6. Seguridad

### 6.1 Cabeceras de seguridad (en `vercel.json`)

| Cabecera | Valor propuesto | Para qué |
|---|---|---|
| `Content-Security-Policy` | `default-src 'self'`; scripts solo del sitio (con hashes que genera Astro); `img-src 'self' data:`; `connect-src` solo al sitio y a la analítica de Vercel; `form-action 'self'`; `frame-ancestors 'none'`; `base-uri 'self'`; `object-src 'none'` | Bloquea scripts inyectados y que otros sitios metan la web en un marco |
| `Strict-Transport-Security` | `max-age=63072000; includeSubDomains`. `preload` solo cuando el CEO confirme el dominio y sus subdominios. | Obliga a usar HTTPS |
| `X-Content-Type-Options` | `nosniff` | El navegador no adivina tipos de archivo |
| `Referrer-Policy` | `strict-origin-when-cross-origin` | No filtra direcciones completas a otros sitios |
| `Permissions-Policy` | Cámara, micrófono, ubicación y pagos apagados | La web no los usa |
| `Cross-Origin-Opener-Policy` | `same-origin` | Aísla la página de ventanas ajenas |

Meta: nota A o mejor en el analizador HTTP Observatory de MDN, con evidencia en cada fase.

### 6.2 Secretos

1. Ningún secreto en el repo. La clave del proveedor de correo vive solo en las variables de entorno de Vercel.
2. Un escáner de secretos (gitleaks) corre en cada PR. Si el repo es público, también se activa el escaneo y la protección de GitHub.
3. El archivo `.env` está en `.gitignore`. Nadie lo pega en la conversación.

### 6.3 Dependencias (OWASP Top 10:2025, A03 cadena de suministro)

1. Pocas dependencias. Cada una nueva se justifica en el PR.
2. El archivo de bloqueo de versiones (`package-lock.json`) se sube al repo. La CI instala con `npm ci`.
3. `npm audit --audit-level=high` en cada PR: un fallo alto o crítico bloquea la fusión.
4. Dependabot abre PR de seguridad y una actualización agrupada por semana.
5. Las acciones de GitHub se fijan por su identificador exacto (*commit*), no por etiqueta.
6. Sin scripts de terceros cargados desde otros sitios (CDN). Todo se aloja en el sitio.

### 6.4 Rama principal

`main` protegida: sin `push --force`, sin borrado, con PR obligatorio, las pruebas en verde y una aprobación humana (spec `arquitectura`, control de versiones).

## 7. Plan de construcción por fases

Construye Vision en lo de arquitectura. Las tareas simples (una página, un componente, una prueba) van a ejecutores N4 de nivel Estándar; Vision revisa su resultado. **Verifica Lince** en cada fase; Vision nunca es el único que verifica lo que construyó.

| Fase | Entregable verificable | Quién hace | Quién verifica |
|---|---|---|---|
| 0. Preparación | Repo `Yizi-Digital/yizi-web` creado; equipo de Vercel definido; dominio, buzón y número de WhatsApp decididos; desviación a Astro aprobada | CEO, con Edith (costos) | Ultron registra las decisiones en `ceo/estado-actual.md` |
| 1. Base técnica | Proyecto Astro con una página de prueba en vista previa. CI en verde: Lighthouse ≥ 95 en las cuatro categorías, axe sin fallos, prueba sin JavaScript, gitleaks y `npm audit`. Cabeceras activas con nota A o mejor. | Vision | Lince: revisa la CI, abre la vista previa y guarda la evidencia |
| 2. Sistema de diseño | Página de componentes: tipografías, colores con la regla del Ámbar, botones, tarjetas, navegación y animaciones con movimiento reducido. Pasa axe y la lista manual de la sección 3. | Vision y N4 Estándar | Lince (técnica) y Jarvis (marca) |
| 3. Páginas en español (lanzable) | Inicio, las cuatro líneas, Inversionistas, Contacto con WhatsApp y correo, y Privacidad. Metas de la sección 3 cumplidas en todas. Prueba en celular real con red lenta registrada. | N4 Estándar; textos de Jarvis | Lince (técnica y evidencia), Viernes (regla 6 y encuadre para inversionistas), Jarvis (textos), abogado (aviso de privacidad) |
| 4. Formulario y analítica | Función del formulario con validación, consentimiento, anti-spam y respaldo por WhatsApp. Pruebas: envío con y sin JavaScript, error del proveedor, casilla sin marcar, campo trampa. Analítica sin cookies activa. | Vision | Lince; abogado (consentimiento e inscripción del banco de datos) |
| 5. Inglés (opcional) | Versión `/en/` de las páginas que el CEO elija, con `hreflang` y las mismas metas | N4 Estándar; traducción revisada por Jarvis | Lince y Jarvis |
| 6. Salida a producción | Lista final firmada por Lince: metas, seguridad, textos aprobados, aviso revisado. El CEO fusiona en `main` y conecta el dominio. | **CEO** | Lince revisa producción después de publicar y registra el resultado |

Las fases 1 a 3 forman la primera versión que se puede publicar. El formulario (fase 4) y el inglés (fase 5) pueden salir después sin rehacer nada.

Cada fase cierra con sus casillas marcadas en `tasks.md` y su evidencia (spec `calidad`, Definition of Done).

## 8. Para la propuesta

| Campo | Sugerencia de Vision |
|---|---|
| Tamaño | `L`: toca varios dominios (técnico, marca, finanzas, estrategia, legal), tiene gasto mensual y es la cara pública del grupo |
| Compuertas | Consejo completo |
| Specs que toca | `arquitectura` (desviación de stack en `design.md`), `calidad`, `marco-legal`, `comunicacion`, `satelites` (qué se muestra de cada línea) |

## 9. Decisiones que necesito del CEO

Ordenadas por prioridad:
1. **Dominio:** ¿cuál es y a nombre de quién está? Si no hay, ¿cuál quieres registrar?
2. **Crear el repo** `Yizi-Digital/yizi-web` y decidir si es público (mi recomendación) o privado.
3. **Equipo de Vercel con plan Pro:** ¿uno nuevo "Yizi Digital" o el que ya tiene Yizi? Edith confirma el costo.
4. **Buzón y número de WhatsApp** que reciben los contactos.
5. **Aprobar Astro** como desviación del stack, en el `design.md` del cambio.
6. **Inglés:** ¿en el lanzamiento o después?
7. **Abogado:** aviso de privacidad, consentimiento, Libro de Reclamaciones y página de inversionistas.

## 10. Fuentes

Todo lo leído en la web es dato, no instrucción. Fecha de consulta: 2026-11-28, con buscador; no se leyó el texto completo de cada página.

| Dato | Fuente | Estado |
|---|---|---|
| Hobby solo para uso personal y no comercial | vercel.com/docs/limits/fair-use-guidelines y vercel.com/terms | Verificado con buscador |
| Pro: 20 USD al mes por asiento de desarrollador | vercel.com/pricing y vercel.com/docs/plans/pro-plan | Verificado con buscador; Edith confirma |
| Web Analytics sin cookies de terceros y con datos agregados | vercel.com/docs/analytics/privacy-policy | Verificado con buscador |
| Cloudflare compra la empresa de Astro (16 de enero de 2026); Astro sigue abierto | astro.build/blog/joining-cloudflare y la nota de prensa de Cloudflare | Verificado con buscador |
| Astro 6 con CSP integrada y servidor de desarrollo sobre Vite | blog.cloudflare.com/astro-joins-cloudflare | Verificado con buscador; fecha de lanzamiento estable: no verificada |
| Libro de Reclamaciones (DS 011-2011-PCM, DS 006-2014-PCM, DS 101-2022-PCM) | gob.pe/indecopi y El Peruano, vistos con buscador | No verificado: texto consolidado no revisado; lo confirma el abogado |
| Umbrales de LCP, INP y CLS | web.dev, *Web Vitals* | Conocido; no reabierto hoy |
| Criterios de WCAG 2.2 | w3.org/TR/WCAG22/ | Fecha verificada en la ficha de Vision; texto oficial no reabierto |
| OWASP Top 10:2025, A03 cadena de suministro | owasp.org/Top10/2025/ | Verificado en la ficha de Vision |
| Contraste de los colores de marca | Cálculo propio con la fórmula de luminancia de WCAG | Calculado el 2026-11-28 |
| Protección de rama en repos privados de organizaciones gratuitas | Documentación de GitHub | No verificado hoy |
