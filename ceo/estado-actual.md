# Estado actual de Yizi

Foto del trabajo para abrir una sesión nueva con contexto. Ultron la mantiene al día.
Última actualización: 2026-11-23. Los detalles viven en `ceo/pendientes.md` y en cada repo.

## 1. Satélites y proyectos

| Satélite | Estado | Dónde va |
|---|---|---|
| Yizi Solutions | Activo | Faltan 3 pilotos (los hace el CEO, sin Promotor). Oferta: Paquete Base. |
| Yizi Publisher | Aprobado, repo listo | En incubación hasta el punto de control 3.0. Nada se vende antes. |
| Yizi Projects | Activo (MACRO) | Cupo MACRO: máximo 1 a la vez. Ver proyectos abajo. |
| Yizi Talent | Incubación | Sin repo. Jocasta aprobada como líder. Patrocina Ultron. |

| Proyecto (Projects) | Estado | Etapa |
|---|---|---|
| toFinance | Pausado | Discovery indefinido. Caja de la casa y del negocio de barrio. Sin código. |
| Plan de comidas y mercado | Propuesto | Discovery de señal. Tope y cupo MACRO esperan al CEO. |

## 2. Cambios OpenSpec abiertos

| Cambio | Repo | Fase |
|---|---|---|
| `activar-yizi-publisher` | núcleo | Aprobado. Tareas pendientes (8.1, 8.2, 8.3 antes de vender). |
| `agentes-conversan-como-personas` | núcleo | Aprobado. Implementado en parte (12 tareas hechas, 22 abiertas). |
| `talentos-tofinance` (Cronos y Tempo) | projects | Aprobado, sin activar. En espera. |

Archivados recientes (2026-11-17 y 18): `activar-lince-abaco-chaski`, `aprobacion-por-lotes`, `completar-fichas`, `marco-legal-del-grupo`, `organigrama-vivo`.

## 3. Decisiones recientes del CEO

| Fecha | Decisión |
|---|---|
| 2026-11-18 | Ultron siempre delega. Lo que construye un agente lo verifica otro. |
| 2026-11-18 | toFinance cambia de rumbo a Discovery indefinido. Plan de comidas pasa a Discovery. |
| 2026-11-20 | Los agentes hablan en primera persona, firmados, de 150 palabras o menos, con bloque "Detalle". |
| 2026-11-20 | Trato de usted con los clientes. |
| 2026-11-20 | Se prepara el repo de Publisher. El estado `activo` espera el punto de control 3.0. |
| 2026-11-20 | Acompañamiento IA de Publisher aprobado como último escalón: S/ 69 al mes (precio aún en propuesta hasta 3 cotizaciones). Fuente: `openspec/changes/activar-yizi-publisher/consejo.md`. |
| 2026-11-18 | Publisher recibe 5 horas por semana del CEO (tope de unos 3 clientes). Fuente: `openspec/changes/activar-yizi-publisher/consejo.md`. |
| 2026-11-18 | Fiesteros pasa a Yizi como caso de portafolio; repo transferido a Yizi-Digital. Fuente: `openspec/changes/activar-yizi-publisher/estudio/fiesteros/pedido-del-ceo.md`. |
| 2026-11-20 | Sala Yizi: el plan de IA del CEO es el motor principal. API key de respaldo. |
| 2026-11-20 | Yizi Voz Local corre en 127.0.0.1:8765. Contrato 1.0.1. |

## 4. Trabajos en curso

| Trabajo | Dónde |
|---|---|
| Sala Yizi (reuniones por voz): prompt, opciones y costo | `agentes/reuniones-por-voz/` |
| Yizi Voz Local (servidor de voz para Mac) | `herramientas/yizi-voz-local/` (README y `CONTRATO-API.md`) |
| Plan de activación de Publisher y estudio de Fiesteros | `openspec/changes/activar-yizi-publisher/` |
| Agentes que conversan como personas | `openspec/changes/agentes-conversan-como-personas/` |
| Proyectos MACRO (toFinance, plan de comidas) | `/yizi-projects/proyectos/` |
| Decisiones de Solutions (36 registradas) | `/yizi-solutions/catalogo/decisiones-ceo.md` |
| Pendientes del CEO | `ceo/pendientes.md` |

## 5. Repos y ramas de trabajo

| Repo | Rama de trabajo |
|---|---|
| yizi-workflow (núcleo) | `yizi/activar-lince-abaco-chaski` |
| yizi-solutions | `karen/catalogo-inicial` |
| yizi-publisher | `homer/genesis` |
| yizi-projects | `herbie/proyecto-tofinance` |

Un solo PR abierto por repo y por flujo. Nada se fusiona ni se sube sin confirmación del CEO.

## 6. Cómo retomar

1. Lee `CLAUDE.md` (y `AGENTS.md`).
2. Lee `ceo/pendientes.md`.
3. Lee este archivo.
4. Confirma ramas con `git status` y cambios con `openspec list`.
5. Si algo de aquí no coincide con el repo, el repo manda. Corrige este archivo.
