# Design

## Context

La spec `autoridad-macro` creaba un satélite por cada proyecto MACRO autorizado. El CEO prefiere un satélite único para todos.

## Goals / Non-Goals

**Goals:** un solo satélite activo para incubar productos propios, sin que el portafolio crezca con cada idea.
**Non-Goals:** autorizar proyectos ni definir sus marcas.

## Decisions

### D1 · Un repositorio, una carpeta por proyecto — [Vision, Viernes]
Cada proyecto MACRO autorizado vive en `proyectos/<id-del-proyecto>/` dentro de `Yizi-Digital/yizi-projects`, con sus specs como capacidades `<id-del-proyecto>/<capacidad>`. Si un proyecto crece hasta necesitar su propio equipo o repositorio, la Autoridad MACRO puede proponer separarlo con un cambio del núcleo.
*Alternativa descartada:* un repositorio por proyecto desde el inicio, que multiplica la gestión con un solo CEO.

### D2 · "Activo" sin oferta a clientes — [Viernes, Jarvis]
Yizi Projects no vende servicios a clientes: su "estado activo" significa que está operativo para recibir proyectos autorizados. Los productos que salgan de él usan su propia marca con respaldo "por Yizi", según la spec `comunicacion`.

### D3 · Líder propuesto H.E.R.B.I.E (Herbie) — [Viernes]
Sigue el estilo de los demás líderes. Su rol: incubar productos propios, cuidar el expediente y los criterios de cierre de cada proyecto y reportar a Viernes. **Pendiente de aprobación del CEO.**

## Risks / Trade-offs

- Varios productos en un repositorio pueden mezclarse; se mitiga con una carpeta y una capacidad por proyecto, y con el límite de un proyecto MACRO a la vez.
