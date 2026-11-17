# Proposal: Satélite Yizi Projects, casa de los proyectos MACRO

| Campo | Valor |
|---|---|
| Dueño | V.I.E.R.N.E.S (Viernes) · CSO |
| Alcance | nucleo |
| Tipo | estrategico |
| Tamaño | L (nuevo satélite y cambios en specs del núcleo) |
| Compuertas | Consejo completo + aprobación del CEO |
| Aprobación | Decisión del CEO del 2026-11-17: crear Yizi Projects, casa de los proyectos MACRO, en estado activo |

## Why

Hasta ahora, cada proyecto MACRO autorizado se convertía en un satélite nuevo. Eso multiplica repositorios, marcas y líderes, justo lo que puede diluir la visión. El CEO decidió crear un último satélite, **Yizi Projects**, que concentra todos los productos propios de Yizi.

**Valor que lo justifica:** Agilidad Real (un solo lugar y un solo líder para incubar productos propios) y foco (el portafolio no crece con cada idea).

## What Changes

- `satelites`: el tipo `macro` tiene un único satélite, Yizi Projects; los proyectos MACRO viven dentro de él.
- `autoridad-macro`: un proyecto AUTORIZADO se registra dentro de Yizi Projects, no como satélite nuevo.
- Registro: nuevo satélite `yizi-projects` (Yizi Projects), tipo `macro`, estado `activo`, patrocinadora Viernes, líder propuesto H.E.R.B.I.E (Herbie), y lista de proyectos vacía.
- Ficha de Viernes, `README.md` y borrador del Manual v3.0 al día.
- Génesis local del repositorio `yizi-projects` desde la plantilla.

## Capabilities

### New Capabilities
- Ninguna.

### Modified Capabilities
- `satelites`: requisito "Tipos de satélite".
- `autoridad-macro`: requisitos "Veredictos de la Autoridad MACRO" y "Revisión periódica y criterio de cierre".

## Impact

- `satelites/registro.yaml`, `.claude/agents/viernes.md`, `README.md`, `marca/manual-de-marca.md`.
- Repositorio `Yizi-Digital/yizi-projects`: lo crea el CEO vacío; luego se sube.
- **Costo (Edith):** 0 USD. Estar activo no implica gasto: no hay proyectos MACRO todavía y el límite sigue en uno a la vez.

## Out of Scope

- Autorizar algún proyecto MACRO.
- Activar Yizi Publisher o Yizi Talent (siguen en incubación).
