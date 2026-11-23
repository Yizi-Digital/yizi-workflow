# Mis pendientes y mis documentos

Archivo vivo del CEO. Lo actualiza Ultron cada vez que algo se decide, se fusiona o se crea.
Última actualización: 2026-11-22 (cupo MACRO aprobado; Publisher Media guardada como señal; preguntas de proyectos MACRO en sus fichas).

## 1. Mis pendientes

### Decidir
- Las decisiones de toFinance y del plan de comidas y mercado pasan a la ficha de cada proyecto en Yizi Projects (`proyectos/<id>/ficha.md`). Están en espera hasta que el CEO retome los proyectos.

### Fusionar en GitHub
- [ ] yizi-projects · PR #6 · ficha de proyecto MACRO (spec, plantilla y fichas de toFinance y plan de comidas). Verificado por Lince.
- [ ] yizi-workflow · PR #15 · cambio `ajustar-cupo-macro` (aprobado el 2026-11-22, en implementación), cartera de señales y estos pendientes. Fusionar cuando Lince verifique y el cambio se archive.

### Hacer yo
- [ ] Persona de respaldo (Lesfer Garcia, nombrada el 2026-11-22): confirmar que acepta, escribir el procedimiento de emergencia y pedir al abogado el instrumento legal que fija su alcance. No recibe tus credenciales (spec `gobierno-agentes`).
- [ ] Sala Yizi: probar los criterios de la fase 5 (Consejo de 15 min con acta, reunión solo con teclado, Consejo de 30 min sin agotar la ventana) y anotar el cambio de `/usage`. Ver `yizi-reuniones/docs/tareas.md`.
- [ ] Sala Yizi: crear una API key en la Consola de Anthropic, comprar crédito prepago y apagar la recarga automática (falta para comparar la latencia y el costo con API key).
- [ ] Fiesteros: renombrar el repo a `fiesteros-web`, pasar Vercel a un equipo Pro y conectarlo, proteger `main` y confirmar que `@fiesteros.pe` es la cuenta correcta.
- [ ] Crear la cuenta de Google de Yizi con verificación en dos pasos (carpetas privadas de clientes de Publisher).
- [ ] Probar `claude --agent edith` en mi computadora (la primera vez en modo interactivo, aceptando la carpeta como confiable).
- [ ] Revisar mi RUC 10 en SUNAT: régimen MYPE, actividad de software, activo y habido, emisión electrónica.
- [ ] Abrir la cuenta de API de Claude a nombre de Yizi, con medio de pago y límite de gasto.
- [ ] Abrir la cuenta de Meta (WhatsApp) en soles.
- [ ] Confirmar con Izipay el link de pago con RUC 10.
- [ ] Registrar gratis la base de datos de Cuentas del barrio en la ANPD (gob.pe).
- [ ] Pedir 3 cotizaciones de abogado y contratar contador (cuando decida).
- [ ] Configurar mi computadora: clonar los 3 repos, instalar OpenSpec, registrar el núcleo, aceptar el plugin.
- [ ] Revisar que la Claude GitHub App tenga acceso a todos los repos.

### Rutina
- [ ] Fin de mes: registrar mi consumo de IA en `finanzas/consumo-ia.md`.
- [ ] Buscar 3 bodegas o kioskos para los pilotos (los hago yo).

### Más adelante
- [ ] Decidir cuándo activar Yizi Publisher y Yizi Talent.
- [ ] Llevar las consultas al contador y al abogado cuando tenga ese talento.

## 2. Mis documentos

Ruta = repositorio / archivo. Si dice "rama", aún no está fusionado.

### Núcleo · yizi-workflow
| Qué | Ruta |
|---|---|
| Visión general y organigrama | `yizi-workflow/README.md` |
| Reglas para los agentes | `yizi-workflow/AGENTS.md` |
| Manual de marca v3 (misión y visión) | `yizi-workflow/marca/manual-de-marca.md` |
| Guía de escritura (lenguaje simple) | `yizi-workflow/marca/guia-de-escritura.md` |
| Satélites y su estado | `yizi-workflow/satelites/registro.yaml` |
| Registro de consumo de IA | `yizi-workflow/finanzas/consumo-ia.md` |
| Reglas vigentes (15 specs) | `yizi-workflow/openspec/specs/` |
| Fichas de los agentes | `yizi-workflow/.claude/agents/` |
| Mapa de personas que faltan | `yizi-workflow/talento/mapa-de-roles.md` (v2) |
| Mapa de agentes que faltan | `yizi-workflow/agentes/mapa-de-agentes.md` |
| Ficha de Lince (verificador) | `yizi-workflow/.claude/agents/lince.md` |
| Marco legal del grupo | `yizi-workflow/openspec/specs/marco-legal/spec.md` |

### Yizi Solutions · yizi-solutions
| Qué | Ruta |
|---|---|
| Mis decisiones (registro) | `yizi-solutions/catalogo/decisiones-ceo.md` |
| Catálogo y priorización | `yizi-solutions/catalogo/README.md` |
| Problemas de los negocios | `yizi-solutions/catalogo/problematicas.md` |
| Las 10 soluciones | `yizi-solutions/catalogo/*.md` |
| Oferta principal y hoja de ruta | `yizi-solutions/catalogo/recomendacion.md` |
| Precios, márgenes, impuestos | `yizi-solutions/catalogo/economia.md` |
| Plataforma técnica | `yizi-solutions/catalogo/bloques-tecnologicos.md` |
| Cláusula de ajuste por Meta | `yizi-solutions/catalogo/clausula-ajuste-meta.md` |
| Flujo operativo | `yizi-solutions/operacion/flujo-operativo.md` |
| Cómo se paga la IA del producto | `yizi-solutions/operacion/ia-del-producto.md` |
| Perfil del Promotor de barrio | `yizi-solutions/equipo/perfil-promotor-de-barrio.md` |
| Pago del Promotor | `yizi-solutions/equipo/compensacion-promotor-de-barrio.md` |
| Aviso y entrevista (borrador) | `yizi-solutions/equipo/aviso-y-entrevista-promotor.md` |
| Cotización de contador, abogado y facturador | `yizi-solutions/equipo/cotizacion-asesores-externos.md` |
| Plantilla de la demo | `yizi-solutions/demo/plantilla-demo.md` |
| Ficha de Ábaco (analista de pilotos) | `yizi-solutions/.claude/agents/abaco.md` |
| Ficha de Chaski (El Guía en modo ayuda) | `yizi-solutions/producto/agentes/chaski.md` |

### Yizi Projects · yizi-projects
| Qué | Ruta |
|---|---|
| Cómo nace un proyecto MACRO | `yizi-projects/proyectos/README.md` |
| Equipo de 14 agentes (fichas) | `yizi-projects/.claude/agents/` |
| Equipo y quién decide qué | `yizi-projects/AGENTS.md` |

### Sala Yizi · yizi-reuniones (solo en esta Mac: `~/Desktop/yizi-reuniones`, sin commits ni remoto)
| Qué | Ruta |
|---|---|
| Diseño y decisiones | `yizi-reuniones/docs/design.md` |
| Tareas por fase | `yizi-reuniones/docs/tareas.md` |
| Verificación de las fases 0 a 5 | `yizi-reuniones/docs/verificacion-fase*.md` |
| Latencia de voz | `yizi-reuniones/docs/latencia.md` |

### toFinance y otros · yizi-projects
| Qué | Ruta |
|---|---|
| toFinance · reevaluación frente a la competencia | `yizi-projects/proyectos/tofinance/reevaluacion-competencia.md` |
| toFinance · estudio de la competencia (CEO) | `yizi-projects/proyectos/tofinance/estudio-competencia-quipuk.md` |
| toFinance · backlog: épicas, features e historias (Vera) | `yizi-projects/proyectos/tofinance/backlog.md` |
| Plan de comidas y mercado · enfoque de Discovery (Viernes) | `yizi-projects/proyectos/idea-mercado-barrio/discovery/enfoque-discovery.md` |
| Plan de comidas y mercado · backlog (Vera) | `yizi-projects/proyectos/idea-mercado-barrio/discovery/backlog.md` |
| App de compras del barrio · evaluación (Viernes) | `yizi-projects/proyectos/idea-mercado-barrio/evaluacion.md` |
| App de compras del barrio · 6 informes | `yizi-projects/proyectos/idea-mercado-barrio/estudio/` |
| Yizi Publisher · plan de activación y Consejo | `yizi-workflow/openspec/changes/activar-yizi-publisher/` |
| Fiesteros · estudio (Vision, Jarvis, Temis, Edith) | `yizi-workflow/openspec/changes/activar-yizi-publisher/estudio/fiesteros/` |
| Sala Yizi · prompt para construir la app (Vision, revisado por Aida y Edith) | `yizi-workflow/agentes/reuniones-por-voz/prompt-app-reuniones-mac.md` |
| Reuniones por voz · opciones (Vision) y costo (Edith) | `yizi-workflow/agentes/reuniones-por-voz/` |
| Agentes que conversan como personas · en curso | `yizi-workflow/openspec/changes/agentes-conversan-como-personas/` |
| toFinance · revisión legal (Temis) | `yizi-projects/proyectos/tofinance/revision-legal.md` |
| toFinance · manual de marca v2 (Iris) | `yizi-projects/proyectos/tofinance/manual-de-marca-v2.md` |
| toFinance · expediente MACRO | `yizi-projects/proyectos/tofinance/expediente.md` |
| Talentos Cronos y Tempo (en espera) | `yizi-projects/openspec/changes/talentos-tofinance/` |
