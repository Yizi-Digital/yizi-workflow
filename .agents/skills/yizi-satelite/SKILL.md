---
name: yizi-satelite
description: Crea (génesis) un satélite del universo Yizi a partir de la plantilla del núcleo yizi-workflow - un repositorio separado Yizi-Digital/<id> para una línea de negocio, que hereda specs y agentes del núcleo - y lo inscribe en el registro de satélites. Úsalo cuando el usuario diga "crea el satélite", "nuevo satélite", "génesis de satélite", "arranca Yizi <línea>" o "arranca Yizi Projects".
license: Propietaria · Yizi Digital
metadata:
  author: yizi-digital
  version: "1.0"
  nucleo: yizi-workflow
---

Genera el repositorio de un satélite a partir de `satelites/plantilla/` del núcleo, conectado al núcleo como store de OpenSpec y como plugin de Claude Code.

**Reglas de gobierno:** crear un repositorio remoto, hacer push o cambiar el estado de un satélite son acciones visibles hacia afuera. Prepáralas y pide confirmación humana antes de ejecutarlas.

---

## 1. Comprueba la autorización

Un satélite solo nace con un cambio aprobado en el núcleo (spec `satelites`).

1. Lee `satelites/registro.yaml` del núcleo.
2. Los proyectos MACRO **no** son satélites: viven en `proyectos/<id>/` dentro de Yizi Projects. Para uno de ellos, no uses este skill.
3. Si el satélite no figura en el registro, o no hay un cambio del núcleo aprobado por el CEO que lo cree, **detente** y ofrece proponerlo con `/openspec-propose` (tipo `estrategico`, dueña Viernes).
4. Si figura, toma de allí: `id`, `nombre`, `tipo`, `descripcion`, `patrocinador` y `lider`.
5. Si el líder N2 está como `propuesto`, pregunta al CEO si aprueba el nombre antes de continuar.

## 2. Reúne los datos que faltan

Cada satélite es un **repositorio separado** en la organización de GitHub de Yizi: `Yizi-Digital/<id>` (spec `satelites`). Nunca generes un satélite dentro del repositorio del núcleo.

Pregunta solo lo que no esté en el registro:
- carpeta destino local (por defecto, junto al núcleo: `../<id>`);
- rol del líder N2 en una frase.

## 3. Genera el repositorio

1. Copia `satelites/plantilla/` del núcleo a la carpeta destino, incluidos los archivos ocultos (`.claude/`).
2. Renombra `.claude/agents/lider-satelite.md` a `.claude/agents/<lider-id>.md`, donde `<lider-id>` es el nombre corto del líder en minúsculas y sin puntos.
3. Sustituye estos marcadores en todos los archivos copiados:

| Marcador | Valor |
|---|---|
| `{{SATELITE_ID}}` | id del satélite (kebab-case, por ejemplo `yizi-solutions`; siempre `yizi-<descriptor en inglés>`) |
| `{{SATELITE_NOMBRE}}` | nombre comercial en inglés (por ejemplo, Yizi Solutions) |
| `{{SATELITE_TIPO}}` | `linea` o `macro` |
| `{{SATELITE_DESCRIPCION}}` | descripción del registro |
| `{{PATROCINADOR}}` | agente N1 patrocinador (por ejemplo, V.I.S.I.O.N (Vision)) |
| `{{LIDER_FORMAL}}` | nombre formal del líder (por ejemplo, K.A.R.E.N) |
| `{{LIDER_CORTO}}` | nombre corto (por ejemplo, Karen) |
| `{{LIDER_ID}}` | `<lider-id>` |
| `{{LIDER_ROL}}` | rol del líder en una frase |

4. Comprueba que no queda ningún marcador: `grep -rn "{{" <carpeta>` no debe devolver nada.

## 4. Inicializa OpenSpec y la conexión con el núcleo

Dentro de la carpeta del satélite:

```bash
git init
openspec init --tools claude,agents --scope project
openspec store list --json
```

- Si el store `yizi-workflow` no está registrado en esta máquina, regístralo apuntando a la copia local del núcleo: `openspec store register <ruta-del-núcleo> --id yizi-workflow`.
- Verifica la conexión con `openspec doctor`: el satélite debe ver la referencia `yizi-workflow` sin errores.
- Verifica que `openspec instructions proposal` muestra el índice de specs del núcleo.

## 5. Sube el satélite a la organización

1. Haz el primer commit en la rama `main` del satélite: `Génesis de <id> desde la plantilla del núcleo yizi-workflow`.
2. Crear `Yizi-Digital/<id>` en GitHub es una acción hacia afuera: pide al CEO que cree el repositorio **vacío** (sin README ni licencia) o que confirme que lo creas tú, si tu herramienta tiene permiso para crear repositorios en la organización.
3. Con el repositorio creado: `git remote add origin https://github.com/Yizi-Digital/<id>.git` y `git push -u origin main` (con confirmación).

## 6. Actualiza el registro del núcleo

En `satelites/registro.yaml` del núcleo, completa el campo `repo` con `https://github.com/Yizi-Digital/<id>`. Ese cambio del registro se hace dentro del cambio OpenSpec que autorizó el satélite.

## 7. Cierra

Muestra al CEO:
- la ruta del nuevo repositorio y su árbol de archivos;
- el resultado de `openspec doctor`;
- la URL `https://github.com/Yizi-Digital/<id>` (o el paso pendiente si el repositorio aún no existe);
- los siguientes pasos: abrir Claude Code en el satélite y aceptar el plugin `yizi-nucleo`, y proponer el primer cambio del satélite.
