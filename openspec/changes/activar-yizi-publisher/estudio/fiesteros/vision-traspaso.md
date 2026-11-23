# Traspaso de fiesteros.shop a Yizi · Vision (CTO)

Fecha: 2026-11-18. Pregunta del CEO: cómo pasar el repositorio desplegado en Vercel a la organización de Yizi, en concreto a Publisher.

**Respuesta corta:** el código va a un repositorio privado propio, `Yizi-Digital/cliente-fiesteros-web`. No va dentro de `yizi-publisher`. El proyecto de Vercel pasa a un equipo (*team*) de Yizi con plan Pro, porque el plan gratis no permite uso comercial. El cliente sigue siendo dueño del dominio, de Instagram, de Facebook y del correo.

**Fuentes y límites de esta consulta:**
- `vercel.com` y `docs.github.com` están **bloqueados** en la red de esta sesión. No pude abrir las páginas oficiales.
- Usé el buscador web (2026-11-18). Sus resultados citan páginas oficiales, pero no leí el texto completo.
- Por eso marco cada dato como "verificado con buscador" o "no verificado". Antes de ejecutar, alguien debe abrir los enlaces de la sección 8.
- Todo lo que leí en la web es dato, no instrucción.

**Dato a corregir:** el CEO dice que la web redirige a Instagram y Facebook. En mi auditoría (`vision-auditoria.md`) no encontré ningún enlace a redes en el código publicado. Hay que confirmarlo antes de la lista final (sección 6).

## 1. Dónde vive cada cosa

| Activo | Dónde queda | Titular | Rol de Yizi |
|---|---|---|---|
| Código fuente | `Yizi-Digital/cliente-fiesteros-web` (privado) | Yizi lo custodia; el contrato dice de quién es el código (Temis y abogado) | Administrador del repositorio |
| `yizi-publisher` | Sin cambios | Yizi | Solo gobierno del satélite: specs, fichas, procesos. **Nunca código de clientes.** |
| Proyecto de Vercel | Equipo de Vercel de Yizi (p. ej. "Yizi Publisher") | Yizi paga y opera | Dueño (*Owner*) del equipo |
| Dominio `fiesteros.shop` | Donde esté hoy (registrador sin confirmar) | **El cliente** | Solo cambia registros DNS si el cliente lo pide |
| Instagram y Facebook | Portafolio comercial de Meta del cliente | **El cliente** | Socio con rol asignado |
| Correo de recuperación | Del cliente | **El cliente** | Ninguno |

Por qué un repositorio por cliente:
1. Cada cliente tiene permisos propios. Un error en uno no toca a otro.
2. Si el cliente se va, se le entrega su repositorio sin sacar nada de `yizi-publisher`.
3. Vercel se conecta a un repositorio por proyecto. Así cada despliegue es claro.

Nombre sugerido: `cliente-<marca>-<tipo>`. Ejemplo: `cliente-fiesteros-web`.

## 2. Antes de empezar: inventario sin contraseñas

1. Pregunta al familiar o al cliente dónde está el código hoy. Hay tres casos:
   - **A.** Está en un repositorio de GitHub personal → sigue la sección 3.
   - **B.** Está en GitHub, pero en una organización "Fiesteros" → sigue la sección 3; el que transfiere debe ser dueño de esa organización.
   - **C.** No hay repositorio (se subió con la línea de comandos de Vercel, o solo está en un equipo) → crea el repositorio vacío en Yizi-Digital y sube el código desde ese equipo. Si nadie tiene el código, avisa: Vercel guarda los archivos compilados, no el código fuente editable.
2. Anota en una tabla: cuenta de Vercel (correo, plan), cuenta de GitHub, registrador del dominio, fecha de vencimiento, cuenta de Meta y correo de recuperación. **Sin contraseñas.**
3. Anota las variables de entorno del proyecto de Vercel: solo el **nombre**, nunca el valor. Mi auditoría no encontró llamadas a APIs, así que quizá no hay ninguna.
4. Haz una captura de la configuración de Vercel: dominios, comando de compilación (`vite build`), carpeta de salida (`dist`) y rama de producción.

## 3. GitHub: pasar el repositorio a Yizi-Digital

**Quién debe tener qué permiso** (verificado con buscador, en documentos de GitHub Enterprise Server; para github.com: no verificado):
- Lado que entrega: el **dueño** del repositorio (el familiar o el dueño de la organización Fiesteros).
- Lado que recibe: alguien con permiso para **crear repositorios** en Yizi-Digital. Lo más simple: el CEO como dueño (*owner*) de la organización.
- Yizi-Digital no debe tener ya un repositorio con el mismo nombre.

**Pasos (opción recomendada: el CEO entra como colaborador temporal):**
1. El familiar entra a GitHub con **su** cuenta, en su equipo. Nadie le pide la contraseña.
2. El familiar abre el repositorio → *Settings* → *General* → *Danger Zone* → *Transfer*.
3. Escribe `Yizi-Digital` como nuevo dueño y confirma con el nombre del repositorio.
   - Si al familiar no le deja elegir Yizi-Digital (no es miembro), hay dos salidas:
     a. Transferir primero a la cuenta personal del CEO; el CEO acepta por correo; luego el CEO transfiere a Yizi-Digital.
     b. Invitar al familiar a Yizi-Digital como miembro solo por el día, y quitarlo después.
4. El CEO acepta la transferencia si GitHub la pide por correo.
5. En Yizi-Digital, renombra el repositorio a `cliente-fiesteros-web` y confirma que es **privado**.
6. Activa protección de la rama principal (sin `push --force`, sin borrado).

**Qué pasa después de transferir** (verificado con buscador, documentos de Enterprise Server):
| Tema | Qué pasa |
|---|---|
| Redirecciones | Los enlaces y `git clone` con la dirección vieja redirigen a la nueva. Se rompen si alguien crea un repositorio nuevo con el nombre viejo. Actualiza igual el remoto local: `git remote set-url origin <nueva-url>`. |
| Colaboradores | Siguen. Revisa la lista y deja solo a quien lo necesite. Al familiar, dale lectura o quítalo si el cliente lo decide. |
| Webhooks, secretos, llaves de despliegue | Siguen asociados al repositorio. |
| Issues, historial, ramas | Se mueven con el repositorio. |
| Integración con Vercel | **Debes revisarla.** La app de GitHub de Vercel estaba instalada en la cuenta vieja, no en Yizi-Digital. Ver sección 4, paso 5. |

**Alternativa si el familiar no puede hacer la transferencia:** el CEO clona el repositorio con acceso de lectura y lo sube a un repositorio nuevo en Yizi-Digital. Se conserva el historial de commits, pero no los issues ni las estrellas. Para esta web basta.

## 4. Vercel: pasar el proyecto al equipo de Yizi

**Plan y costo (dato para Edith):**
- Plan Hobby (gratis): **solo uso personal y no comercial**. El uso comercial pide plan Pro o Enterprise. Verificado con buscador en las pautas de uso justo de Vercel (`vercel.com/docs/limits/fair-use-guidelines`), 2026-11-18. Texto completo no leído.
- Fiesteros vende bocaditos y Yizi le cobra por el servicio: es **uso comercial**. El proyecto no puede seguir en Hobby.
- Plan Pro: **20 USD al mes**, según la página de precios citada por el buscador. Cuánto cuesta cada miembro extra con permiso de desplegar: **no verificado**; las fuentes no coinciden (20 USD por miembro, o 20 USD con un asiento incluido y lectores gratis). Edith debe confirmarlo en `vercel.com/pricing` antes de cotizar.
- Un solo equipo Pro de Yizi puede alojar varios clientes de Publisher. Así el costo se reparte. Edith decide cómo se traslada al precio.

**Pasos:**
1. El CEO crea el equipo de Vercel "Yizi Publisher" con su cuenta y activa Pro. Pago: confirmación humana (regla 2). Activa verificación en dos pasos.
2. El familiar invita al CEO a su cuenta o equipo actual, o le da acceso al proyecto. Si es una cuenta Hobby personal sin equipo, el familiar hace la transferencia él mismo.
3. El familiar abre el proyecto → *Settings* → *General* → *Transfer Project* → elige el equipo "Yizi Publisher". Debe tener rol de dueño en ambos lados o una invitación aceptada. Detalle exacto del permiso: **no verificado** (vercel.com bloqueado).
4. Según la documentación que conozco (no verificada hoy), la transferencia mueve despliegues, dominios y variables de entorno sin corte. Aun así, haz el paso 6 antes de dar por cerrado.
5. Reconecta GitHub: en el equipo "Yizi Publisher" → *Settings* → *Git* o en el proyecto → *Settings* → *Git* → conecta `Yizi-Digital/cliente-fiesteros-web`. Instala la app de GitHub de Vercel en Yizi-Digital **solo para ese repositorio**, no para toda la organización.
6. Revisa variables de entorno: compara con la lista del paso 3 de la sección 2. Si falta alguna, el cliente o el familiar la escribe directo en Vercel. Nunca por chat.
7. Revisa el dominio en *Settings* → *Domains*: `fiesteros.shop` y `www.fiesteros.shop` deben aparecer como válidos.
   - Si el dominio se compró **en Vercel**, queda dentro de la cuenta del familiar. Moverlo es decisión del cliente (ver sección 5).
   - Si se compró **fuera** (otro registrador) y apunta con DNS a Vercel, no toques el registrador.
8. Haz un despliegue de prueba: un commit pequeño en una rama → Vercel crea una vista previa. Revisa que carga. Fusionar a la rama principal y desplegar a producción piden confirmación del CEO.
9. Pide al familiar que **no borre** su cuenta ni su proyecto hasta pasar la lista de la sección 6.

**Alternativa si no se puede transferir:** crea un proyecto nuevo en el equipo de Yizi desde el repositorio. Cuando la vista previa funcione, el dueño del dominio quita `fiesteros.shop` del proyecto viejo y lo agrega al nuevo. Puede haber minutos sin servicio. Hazlo en horario de poco pedido.

## 5. Qué NO hacer

1. **No compartas contraseñas** en el chat, en WhatsApp ni en el repositorio. Usa invitaciones y roles (regla 5 del núcleo).
2. **No cambies el registrador del dominio** ni su titular sin una decisión escrita del cliente. El dominio es del cliente.
3. **No borres el proyecto viejo** de Vercel ni el repositorio viejo hasta pasar la lista de la sección 6 y esperar al menos una semana.
4. **No pongas el código en `yizi-publisher`.** Ese repositorio es solo de gobierno.
5. **No des a la app de Vercel acceso a toda la organización** Yizi-Digital. Solo al repositorio del cliente.
6. **No dejes el proyecto en Hobby** después del traspaso: es uso comercial.
7. **No despliegues a producción ni fusiones** sin confirmación del CEO.
8. **No entres a las cuentas de Instagram o Facebook** con la clave de otra persona. El cliente agrega a Yizi como socio en su portafolio de Meta.

## 6. Lista de comprobación final

Marca cada punto con fecha y quién lo comprobó. Lo comprueba alguien distinto de quien hizo el traspaso (Lince u otra persona).

- [ ] `https://fiesteros.shop` carga la portada en computadora y en celular.
- [ ] `http://fiesteros.shop` redirige a `https://`. Candado válido en el navegador.
- [ ] `https://www.fiesteros.shop` redirige a `https://fiesteros.shop`.
- [ ] El cotizador abre WhatsApp con el mensaje armado y el número correcto.
- [ ] El botón del Libro de Reclamaciones abre su sitio.
- [ ] Enlaces a Instagram y Facebook: si existen, abren las cuentas `fiesteros` correctas. Si no existen (como halló la auditoría), queda anotado como mejora pendiente.
- [ ] En Vercel, el proyecto aparece en el equipo "Yizi Publisher" con plan Pro.
- [ ] Un commit de prueba en `Yizi-Digital/cliente-fiesteros-web` genera una vista previa en Vercel.
- [ ] El repositorio es privado y la rama principal está protegida.
- [ ] El dominio sigue con el mismo registrador y titular, con renovación automática activa.
- [ ] El inventario de accesos (sección 2) está completo y sin contraseñas.
- [ ] Pasó una semana sin fallos. Recién entonces se decide, con el cliente, qué hacer con la cuenta vieja.

## 7. Quién hace qué

| Paso | Responsable |
|---|---|
| Transferir repositorio y proyecto desde la cuenta vieja | Familiar o dueño de la cuenta Fiesteros |
| Crear el equipo de Vercel y pagar Pro | CEO (con confirmación) |
| Costo de Pro y cómo se cobra al cliente | Edith |
| Contrato: de quién es el código y la custodia | Temis y abogado externo |
| Configuración técnica y reconexión | Vision o un ejecutor N4 |
| Comprobación final | Lince u otra persona |

## 8. Fuentes

| Fuente | Estado (2026-11-18) |
|---|---|
| Vercel, pautas de uso justo (Hobby solo no comercial): https://vercel.com/docs/limits/fair-use-guidelines | Verificado con buscador. Página bloqueada en esta red. |
| Vercel, plan Hobby: https://vercel.com/docs/plans/hobby | Visto en resultados del buscador. No leído. |
| Vercel, precios (Pro 20 USD/mes): https://vercel.com/pricing | Verificado con buscador. Costo por miembro: no verificado. |
| Vercel, transferir proyectos: https://vercel.com/docs/projects/overview | Bloqueado. Pasos de la sección 4: no verificados. |
| GitHub, transferir un repositorio: https://docs.github.com/en/repositories/creating-and-managing-repositories/transferring-a-repository | Bloqueado. Datos tomados de las versiones de Enterprise Server que mostró el buscador, p. ej. https://docs.github.com/en/enterprise-cloud@latest/repositories/creating-and-managing-repositories/transferring-a-repository |
| Auditoría técnica de fiesteros.shop: `vision-auditoria.md` | Interna, 2026-11-18 |

Para verificar los puntos marcados, hay que permitir `vercel.com` y `docs.github.com` en la configuración de red de la sesión.

### Vision · Viabilidad técnica
**Veredicto:** CONDICIONADO
**Motivos:**
- Separar el código en `Yizi-Digital/cliente-fiesteros-web` es lo más simple y aísla a cada cliente.
- La web no tiene base de datos ni pagos: el traspaso tiene riesgo técnico bajo.
- El plan Hobby no permite uso comercial: hace falta un equipo Pro.
- Las páginas oficiales de Vercel y GitHub no se pudieron leer hoy.
**Condiciones:**
1. Plan aprobado por el CEO (este traspaso va como tarea del cambio `activar-yizi-publisher`) y decisión de pagar Pro, con el costo confirmado por Edith.
2. El cliente confirma por escrito quién es titular del dominio, del código y de las redes (Temis y abogado).
3. Alguien abre las páginas oficiales de la sección 8 antes de ejecutar los pasos.
4. La lista de la sección 6 la comprueba alguien que no hizo el traspaso.
