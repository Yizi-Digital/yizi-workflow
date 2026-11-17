# Design

## Context

El repositorio tenía solo el esqueleto de OpenSpec en la raíz (`config.yaml`, `specs/`, `changes/`). OpenSpec 2.x busca su raíz en `openspec/` y, desde la 2.1, permite que un repositorio sea un **store** al que otros repositorios hacen referencia con `references:`. Claude Code carga subagentes desde `.claude/agents/`, skills desde `.claude/skills/` y puede distribuir ambos como **plugin** a otros repositorios. El estándar abierto de skills (`.agents/skills/`) lo leen además otros asistentes de IA.

Restricciones: un solo humano (el CEO), poca caja, y el deseo de que el marco funcione con cualquier herramienta de IA pero de forma óptima con Claude.

## Goals / Non-Goals

**Goals:**
- Que cualquier agente, de cualquier herramienta, pueda leer la cultura, las reglas y su rol desde archivos de texto del repo.
- Que en Claude Code los cinco directivos sean subagentes reales, invocables por nombre.
- Que un satélite herede specs y agentes del núcleo sin copiarlos.
- Costo de infraestructura cero.

**Non-Goals:**
- Orquestación automática 24/7 (autonomía A4). Queda para un cambio futuro con presupuesto de Edith.
- Crear los repositorios de los satélites.

## Decisions

### D1 · Estructura estándar de OpenSpec — [Vision]
Se mueven `config.yaml`, `specs/` y `changes/` a `openspec/` y se ejecuta `openspec init --tools claude,agents --scope project` con los 12 flujos activados (propose, explore, new, continue, ff, apply, update, verify, sync, archive, bulk-archive, onboard).
- *Alternativa descartada:* mantener la raíz plana. El CLI y los skills no la encuentran.

### D2 · El núcleo es un store de OpenSpec — [Vision, Viernes]
El repo se registra como store con id `yizi-workflow` (`.openspec-store/store.yaml`, con el remoto de GitHub). Cada satélite declara en su `openspec/config.yaml`:

```yaml
references:
  - id: yizi-workflow
    remote: https://github.com/YiziDigital/yizi-workflow
```

Así, al proponer cambios en un satélite, OpenSpec entrega a los agentes un índice de las specs del núcleo y la receta para leerlas (`--store yizi-workflow`), sin copiarlas.
- *Alternativas descartadas:* submódulos de git (frágiles para un equipo pequeño); copiar specs (se desincronizan y contradicen la spec `satelites`).
- *Riesgo:* los stores están en beta. Mitigación: la plantilla de satélite también explica cómo leer el núcleo directamente desde GitHub.

### D3 · Fichas de agente = subagentes de Claude Code — [Ultron]
Cada directivo es un archivo `.claude/agents/<nombre>.md` con frontmatter (`name`, `description`, `tools`, `model`) y un cuerpo en Markdown que sirve de ficha completa (identidad, dominio, compuerta, autonomía, reglas). Claude Code los usa como subagentes; cualquier otra herramienta los lee como texto (instrucción en `AGENTS.md`).
- *Alternativa descartada:* fichas en una carpeta aparte y subagentes generados. Duplica la fuente de verdad.

### D4 · Herencia de agentes con un plugin de Claude Code — [Vision]
El repo incluye `.claude-plugin/plugin.json` (plugin `yizi-nucleo`) y `.claude-plugin/marketplace.json` (marketplace `yizi`). El plugin expone los cinco agentes y los skills de Yizi. Un satélite lo activa en su `.claude/settings.json`:

```json
{
  "extraKnownMarketplaces": {
    "yizi": { "source": { "source": "github", "repo": "YiziDigital/yizi-workflow" } }
  },
  "enabledPlugins": { "yizi-nucleo@yizi": true }
}
```

Actualizar el núcleo actualiza a los directivos en todos los satélites (`claude plugin update`).

### D5 · Skills propios de Yizi — [Ultron]
Se crean en `.agents/skills/` (estándar abierto) con enlace simbólico desde `.claude/skills/`, igual que hace OpenSpec:
- `yizi-consejo`: convoca a los agentes de las compuertas que correspondan y escribe `consejo.md`.
- `yizi-satelite`: crea un satélite desde `satelites/plantilla/` y lo inscribe en el registro.

Sus nombres no empiezan por `openspec-` para que `openspec update` no los sobrescriba.

### D6 · Política de modelos (niveles de costo) — [Edith]
Correspondencia vigente al 2026-11-17 (fuente: *Guía de campo de la IA*, 16 nov 2026; revisar cada trimestre):

| Nivel | Uso | Claude | Equivalentes en otras herramientas |
|---|---|---|---|
| Ligero | Tareas mecánicas y de volumen | Haiku 5.5 (`haiku`) | GPT-6 Luna, Gemini 3.8 Flash |
| Estándar | Ejecución diaria | Sonnet 5.5 (`sonnet`) | GPT-6 Instant, Gemini 4 Hydrogen |
| Avanzado | Arquitectura, estrategia, finanzas | Opus 5.5 (`opus`) | GPT-6.1 Sol, Gemini 4 Argon |
| Frontera | Decisiones críticas, con aprobación del CEO | Fable 5.2 (`fable`) | GPT-6 Astra |

Asignación por defecto: Vision, Viernes y Edith → Avanzado (`opus`); Jarvis y Ultron → Estándar (`sonnet`). Los ejecutores N4 usan Ligero siempre que alcance.

### D7 · Satélites iniciales propuestos — [Viernes]
Registro inicial en `satelites/registro.yaml`. Los estados y los nombres de los líderes son **propuestas para el CEO**:

| id | Nombre | Tipo | Estado propuesto | Patrocinador | Líder N2 propuesto |
|---|---|---|---|---|---|
| `yizi-soluciones` | Yizi Soluciones | linea | activo | Vision | K.A.R.E.N (Karen) |
| `yizi-impulso` | Yizi Impulso | linea | incubacion | Jarvis | H.O.M.E.R (Homer) |
| `yizi-talento` | Yizi Talento | linea | incubacion | Ultron | J.O.C.A.S.T.A (Jocasta) |

Solo Soluciones queda activo porque es la línea que describe el Manual de Marca; las otras dos se preparan sin ofrecerse, para no diluir la marca. Los proyectos MACRO no tienen satélite hasta que la Autoridad MACRO autorice uno (límite inicial: 1).

### D8 · Registro del Consejo — [Ultron]
Cada cambio M, L o MACRO incluye `consejo.md` en su carpeta, con una tabla de veredictos y la línea de aprobación del CEO. OpenSpec ignora ese archivo al validar, así que convive con los artefactos del esquema.

### D9 · Permisos de Claude Code en el repo — [Vision]
`.claude/settings.json` permite los comandos de OpenSpec y de lectura de git, y pide confirmación para `git push`. Bloquea `git push --force`, `rm -rf` y la lectura de archivos `.env`. Es la versión mínima de la spec `gobierno-agentes`.

## Risks / Trade-offs

- **Nombres de agentes con propiedad intelectual de terceros** (los cinco directivos son nombres de personajes de Marvel). Uso interno aceptable; la spec `comunicacion` prohíbe mostrarlos a clientes. Si algún día se comercializa el marco, habrá que renombrarlos.
- **Stores y plugins son funciones recientes** de OpenSpec y Claude Code; pueden cambiar. Mitigación: todo sigue siendo Markdown legible.
- **Enlaces simbólicos en Windows**: `.claude/skills/` usa enlaces. Mitigación documentada en el README (`git config core.symlinks true` u `openspec update`).
- **Un solo humano aprueba todo**: cuello de botella consciente. Los cambios S tienen camino corto para no frenar la operación.
