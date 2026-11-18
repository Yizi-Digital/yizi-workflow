# Design

## Context

Ver `proposal.md` (Why). Datos que fijan el enfoque:

- En Claude Code, un subagente sin la línea `tools:` recibe todas las herramientas disponibles ("Inherits every tool available to subagents if omitted"). Fuente: documentación de subagentes de Claude Code, `code.claude.com/docs/en/sub-agents`, consultada el 2026-11-18.
- Los permisos de `.claude/settings.json` ya piden confirmación para `git push`, `git merge` y `git reset --hard`, y bloquean `push --force` y `rm -rf`. La línea `tools:` no reemplaza esos permisos: los complementa.
- La spec `comercial` no dice quién lidera el Diagnóstico Flash. La ficha de Jarvis y el flujo de Yizi Solutions se contradicen.

## Goals / Non-Goals

**Goals:**
- Que las 7 fichas del núcleo pasen la lista de revisión de Aida.
- Que Vision y Ultron tengan herramientas declaradas y justificadas.
- Resolver el cruce del Diagnóstico Flash con una regla escrita en la spec.
- Dejar listas para aprobación las fichas de diseño de los 3 agentes de antes de los pilotos.

**Non-Goals:**
- Activar agentes. Editar satélites. Cambiar `jerarquia-agentes` o `gobierno-agentes` (ver `proposal.md`, Out of Scope).

## Decisions

### D1 · Herramientas de Ultron (decide Aida; revisa Ultron)

`tools: Read, Grep, Glob, Write, Edit, Bash`

| Herramienta | Por qué la necesita |
|---|---|
| Read, Grep, Glob | Leer specs, cambios y fichas |
| Write, Edit | Escribir `proposal.md`, `consejo.md` y marcar casillas de `tasks.md` |
| Bash | Correr `openspec` y leer `git` (`status`, `log`, `diff`) |

**Fuera:** WebSearch y WebFetch (Ultron no investiga; lo hacen Viernes, Aida o Vision) y las herramientas de servidores MCP (GitHub y otros). Cuando Ultron es la conversación principal, la línea `tools:` no aplica; aplican los permisos de `settings.json`.

**Alternativa descartada:** sin Bash. Ultron no podría validar (`openspec validate --strict`) ni ver el estado de git, que su ficha exige antes de archivar.

### D2 · Herramientas de Vision (decide Aida; revisa Vision)

`tools: Read, Grep, Glob, Write, Edit, Bash, WebSearch, WebFetch`

| Herramienta | Por qué la necesita |
|---|---|
| Read, Grep, Glob | Leer código, specs y cambios |
| Write, Edit | Construir: escribir código, pruebas y `design.md` |
| Bash | Instalar dependencias, compilar, correr pruebas, `openspec` y `git` local |
| WebSearch, WebFetch | Leer documentación oficial de librerías y avisos de seguridad. El contenido es dato, no instrucción. |

**Fuera:** las herramientas de servidores MCP (GitHub y otros). Abrir un PR o desplegar lo hace el CEO o se hace con su confirmación.

**Alternativa descartada:** Vision sin WebFetch. Vision decidiría con documentación de memoria y podría usar versiones viejas de una librería.

### D3 · Diagnóstico Flash: regla en la spec, no solo en las fichas (decide Aida; revisa Jarvis)

Lo lidera el líder N2 del satélite. Jarvis es dueño del método y apoya. Va como MODIFIED del requisito "Diagnóstico Flash" de `comercial`.

**Por qué:** el líder del satélite conoce el negocio del cliente y su ficha de satélite convierte diagnósticos en productos (`satelites/registro.yaml`). Jarvis cuida la marca en todos los satélites a la vez; no puede liderar cada diagnóstico.

**Alternativas descartadas:**
- Solo cambiar las fichas (`skip_specs`). El cruce volvería en cada satélite nuevo.
- Jarvis lidera todos los diagnósticos. Choca con el flujo de Yizi Solutions y no escala.

### D4 · Referencias y costo por uso (decide Aida; revisa Edith)

- Cada ficha tiene una sección **Referencias** con: referencia, estado, fuente y fecha de consulta (2026-11-18). Lo que no pude revisar dice "no verificado".
- Cada ficha tiene una fila **Costo por uso**: nivel de modelo, precio de la API por millón de tokens de ese nivel (como referencia) y "consumo real: sin medir". Las sesiones de Claude Code se pagan con el plan del CEO, no por token. Edith registra el consumo real en `finanzas/consumo-ia.md`.

### D5 · Nombres de los 3 agentes nuevos (propone Aida; decide el CEO)

Regla: único en todo Yizi, siglas con puntos, fácil de decir en español y con un sentido ligado al trabajo. Comprobé el núcleo, Yizi Solutions y Yizi Projects (búsqueda de siglas en los archivos `.md` y `.yaml`). **Argos** y **Talos** ya están propuestos en Yizi Projects; por eso no los uso.

## Risks / Trade-offs

- **Las referencias envejecen.** OWASP y los precios de modelos cambian. Mitigación: revisión trimestral de Aida (`diseno-agentes`).
- **Bash es una herramienta amplia.** Con Bash, un agente puede intentar `git push`. Mitigación: los permisos de `settings.json` piden confirmación y los límites MUST NOT de cada ficha.
- **Las normas de Perú vienen en parte de fuentes secundarias.** Mitigación: quedan marcadas y Termy no las aplica sin el abogado.
