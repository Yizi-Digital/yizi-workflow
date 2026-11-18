# Auditoría técnica de fiesteros.shop · Vision (CTO)

Fecha: 2026-11-18. Estado: **incompleta**. No se pudo leer la web.

## 0. Lo importante primero

No pude abrir fiesteros.shop desde esta sesión. La red de la sesión bloquea el dominio:

| Intento | Resultado |
|---|---|
| WebFetch a `https://fiesteros.shop/` | El nombre no resuelve (`ENOTFOUND`). La sesión no tiene el dominio en su lista de dominios permitidos. |
| `curl -I` por el proxy de la sesión | El proxy rechaza la conexión (403). |
| WebSearch "fiesteros.shop" | Ningún resultado del dominio. Aparece un vendedor "FiesterOnline" en Mercado Libre, pero nada lo une a fiesteros.shop. **No verificado.** |

Por eso no afirmo nada sobre la web. Todo lo que sigue es **lo que hay que comprobar** y **los riesgos que aplican a cualquier web hecha a título personal**. No encontré texto con instrucciones dirigidas a agentes, porque no leí ninguna página.

Para terminar la auditoría hay dos caminos:
1. El CEO permite `fiesteros.shop` en la configuración de red de la sesión y Vision repite la lectura.
2. El CEO abre la web en su navegador y comparte capturas o el código fuente de la portada (sin contraseñas).

## 1. Qué es

| Punto | Estado |
|---|---|
| Tipo de negocio | **No verificado.** El nombre sugiere artículos o servicios para fiestas. Es una suposición. |
| Qué ofrece la web | No verificado. |
| Plataforma (Shopify, WordPress, Wix u otra) | No verificado. Se ve en el código fuente: `cdn.shopify.com`, `wp-content` o `wix.com`. |
| Tienda o pagos | No verificado. Si cobra en línea, hay que saber qué pasarela usa y a nombre de quién está la cuenta. |
| Formularios | No verificado. |
| WhatsApp | No verificado. Revisar enlaces `wa.me` y a qué número llevan. |
| Enlaces a Instagram y Facebook | No verificado. El CEO dice que creó ambas cuentas. |

## 2. Estado técnico visible

Lista de comprobación para la segunda lectura. Ninguna casilla está verificada.

- [ ] HTTPS activo y sin avisos del navegador. Certificado vigente.
- [ ] Velocidad aparente en celular con red lenta (PageSpeed Insights, prueba pública).
- [ ] Se ve bien en celular: menú, botones grandes, textos legibles.
- [ ] Sin errores visibles: enlaces rotos, imágenes caídas, páginas 404.
- [ ] SEO básico: título de la página y meta descripción (texto que muestra Google).
- [ ] Accesibilidad básica: texto alternativo en imágenes, contraste, idioma declarado (WCAG 2.2).
- [ ] Aviso de privacidad y términos. Si hay formulario o tienda, son obligatorios en la práctica. El marco legal lo revisa Viernes con el abogado externo.

## 3. Riesgos

Estos riesgos aplican aunque no haya leído la web. Vienen de que el CEO la hizo antes de Yizi y a título personal.

| Riesgo | Por qué importa | Qué hacer |
|---|---|---|
| Dominio a nombre del CEO | Si vence o el CEO pierde el correo, la web cae. El cliente no controla su marca. | Confirmar registrador, titular y fecha de vencimiento. Activar renovación automática y bloqueo de transferencia. Decidir con el cliente quién es titular. |
| Hosting o plataforma en la cuenta personal | Un cobro fallido o una cuenta cerrada apaga la web. | Pasar a una cuenta de empresa de Yizi o del cliente. En Shopify y WordPress se puede dar acceso de colaborador sin dar la contraseña. |
| Correo de recuperación personal | Quien controla el correo controla todo lo demás. | Usar un correo de la empresa para recuperar cada cuenta. Activar verificación en dos pasos. |
| Instagram y Facebook creados con el perfil personal | Si el perfil personal tiene un problema, se pierden las páginas. | Crear un portafolio comercial de Meta (Meta Business Suite). El cliente es dueño. Yizi entra como socio con rol asignado. Nunca compartir la contraseña. |
| Contraseñas en el chat o en el repositorio | Rompe la regla 5 del núcleo. | Usar un gestor de contraseñas con bóveda compartida. Nada de credenciales en conversaciones ni en archivos. |
| Sin copias de seguridad | Un error o un ataque borra todo. | Copia automática semanal del sitio y de los textos e imágenes. Probar una restauración una vez. |
| Pasarela de pago a nombre del CEO | El dinero del cliente pasa por una persona. Riesgo legal y fiscal. | Si existe, la cuenta de cobro va a nombre del cliente. Edith y Viernes revisan. |

## 4. Mejoras priorizadas (para Publisher, solo remoto con IA)

Orden provisional. Se confirma tras leer la web.

1. **Inventario de accesos.** Tabla de cuentas: dominio, hosting, correo, Meta, pagos. Titular y fecha de vencimiento. Sin contraseñas.
2. **Pasar accesos al modelo de roles.** Portafolio comercial de Meta, colaborador en la plataforma, gestor de contraseñas. Todo remoto.
3. **Copias de seguridad automáticas** y una restauración de prueba.
4. **Aviso de privacidad y términos**, redactados con apoyo de IA y revisados por el abogado externo.
5. **SEO básico:** título, descripción y texto alternativo en imágenes. Lo redacta la IA y lo revisa Jarvis.
6. **Rendimiento en celular:** comprimir imágenes y medir con PageSpeed antes y después.
7. **Botón de WhatsApp y enlaces a redes** visibles y probados.
8. **Calendario de contenido** para Instagram y Facebook, generado con IA y aprobado por una persona antes de publicar.

## Preguntas para el CEO (sin credenciales)

1. ¿Qué plataforma usaste para la web y a nombre de quién está?
2. ¿Quién es titular del dominio y cuándo vence?
3. ¿Las páginas de Instagram y Facebook cuelgan de tu perfil personal?
4. ¿La web cobra en línea?
5. ¿Puedes permitir `fiesteros.shop` en la red de la sesión para terminar esta auditoría?

### Vision · Viabilidad técnica
**Veredicto:** CONDICIONADO
**Motivos:**
- No pude leer la web: la red de la sesión bloquea el dominio. No hay datos técnicos verificados.
- Pasar la web al gobierno de Yizi es viable y simple: casi todo es ordenar accesos y roles, en remoto.
- El mayor riesgo es la dependencia de cuentas personales del CEO (dominio, correo, Meta).
- Las mejoras encajan con Publisher "solo remoto con IA". Ninguna exige visitas ni desarrollo pesado.
**Condiciones:**
- Repetir la lectura pública de la web antes de proponer cambios técnicos.
- Inventario de accesos completo y sin contraseñas antes de cualquier trabajo.
- Ningún acceso se comparte por chat. Solo roles, colaboradores y gestor de contraseñas.
- Confirmación del CEO antes de tocar el dominio, el hosting o publicar en redes.

Fuentes consultadas: WebSearch "fiesteros.shop" (2026-11-18), sin resultados del dominio. Ejemplo de resultado no relacionado: [Mercado Libre, recuerdos piñatería fiestas](https://www.mercadolibre.com.co/shorts/clips/c/recuerdos-pinateria-fiestas).
