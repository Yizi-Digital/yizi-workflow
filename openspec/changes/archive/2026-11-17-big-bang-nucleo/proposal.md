# Proposal: Big Bang del núcleo Yizi

| Campo | Valor |
|---|---|
| Dueño | V.I.E.R.N.E.S (Viernes) · CSO |
| Alcance | nucleo (`yizi-workflow`) |
| Tipo | estrategico |
| Tamaño | L |
| Compuertas | Consejo completo (Vision, Jarvis, Edith, Viernes, Ultron) + aprobación del CEO |
| Aprobación | Solicitada por el CEO el 2026-11-17 ("construye los specs base") |

## Why

Yizi Digital nace como un grupo matriz con varias líneas de negocio (soluciones tecnológicas e IA, outsourcing de talento, marketing y ventas digitales) y la ambición de lanzar proyectos propios de gran alcance. Hoy el CEO trabaja solo, con poca caja, y necesita un equipo de agentes de IA que opere con reglas claras sin diluir la visión de la marca ni confundir a los clientes.

Sin un núcleo escrito, cada agente y cada futuro satélite inventaría su propia cultura, sus propias reglas y su propio proceso. Este cambio crea el "Big Bang": el marco corporativo del que nacen todos los satélites.

**Valor que lo justifica:** Agilidad Real (un solo proceso SDD para todo, menos burocracia) y Robustez Invisible (reglas de gobierno que hacen que los agentes trabajen seguros sin que el cliente lo note).

## What Changes

- Se reorganiza el repositorio al formato estándar de OpenSpec (`openspec/`) y se instalan los 12 flujos de OpenSpec para Claude Code y para cualquier agente compatible con `.agents/skills/`.
- Se crean las **12 capacidades base del núcleo** (specs), que describen la cultura, el Consejo Ejecutivo, la jerarquía de agentes, el gobierno, el ciclo SDD, la calidad, la arquitectura, la comunicación, el proceso comercial, las finanzas, el modelo de satélites y la Autoridad MACRO.
- Se implementa el **Consejo Ejecutivo** como agentes reales: V.I.S.I.O.N (CTO), J.A.R.V.I.S (CDO), E.D.I.T.H (CFO), V.I.E.R.N.E.S (CSO) y U.L.T.R.O.N (COO).
- Se crean los skills de Yizi `yizi-consejo` (revisión multiagente de un cambio) y `yizi-satelite` (génesis de un satélite).
- Se publica el núcleo como **plugin de Claude Code** (`yizi-nucleo`) y como **store de OpenSpec** (`yizi-workflow`) para que los satélites hereden agentes y specs sin copiarlos.
- Se crea el registro de satélites y la plantilla de satélite.
- Se documenta el universo para humanos (`README.md`) y para agentes (`AGENTS.md`, `CLAUDE.md`).

## Capabilities

### New Capabilities
- `cultura`: ADN de Yizi (origen del nombre, misión, visión, valores, arquetipo y principios de trabajo humano-IA).
- `consejo-ejecutivo`: el CEO y los cinco agentes directivos, su identidad, dominio y responsabilidades.
- `jerarquia-agentes`: niveles de agentes, líneas de reporte, herencia núcleo→satélite y escalamiento.
- `gobierno-agentes`: autonomía, permisos, acciones irreversibles, seguridad, trazabilidad y veracidad.
- `ciclo-sdd`: el ciclo de desarrollo guiado por especificaciones con compuertas del Consejo.
- `calidad`: Definition of Done, verificación de escenarios y revisión independiente.
- `arquitectura`: estándares técnicos base, seguridad por defecto e IA aplicada responsable.
- `comunicacion`: tono, identidad visual, arquitectura de marca y documentación.
- `comercial`: Ciclo de Servicio Yizi y reglas para propuestas y oportunidades.
- `finanzas`: presupuesto, política de costos de IA, control de gasto y rentabilidad.
- `satelites`: modelo núcleo-satélite, registro, ciclo de vida y herencia.
- `autoridad-macro`: órgano que evalúa y autoriza los proyectos propios MACRO de Yizi.

### Modified Capabilities
- Ninguna (es el primer cambio del núcleo).

## Impact

- Estructura del repo: `config.yaml`, `specs/` y `changes/` se mueven a `openspec/`.
- Archivos nuevos: `.claude/agents/`, `.agents/skills/`, `.claude/skills/` (enlaces), `.claude/settings.json`, `.claude-plugin/`, `.openspec-store/`, `satelites/`, `README.md`, `AGENTS.md`, `CLAUDE.md`.
- Sin dependencias de ejecución. Herramientas requeridas: OpenSpec ≥ 2.1 y, para la experiencia completa, Claude Code.
- **Estimación de costo (compuerta de Edith):** 0 USD en infraestructura; solo tiempo del CEO para revisar y tokens de IA de una sesión de trabajo.

## Out of Scope

- Crear los repositorios de los satélites (se hará con el skill `yizi-satelite` en cambios posteriores).
- Definir los agentes especialistas de cada satélite; aquí solo se proponen sus líderes.
- Automatizaciones de CI, hooks y tableros de métricas.
- Contenido comercial final (precios, catálogo de servicios, sitio web).
