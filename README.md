# yizi-workflow · El núcleo de Yizi Digital

> **Yizi** = la "Y" de **Y**efer + "**izi**" (*easy*). Hacemos fácil lo complejo.

Este repositorio es el **núcleo** del universo Yizi: el marco de trabajo corporativo del que nacen todas las líneas de negocio (satélites). Contiene la cultura, las reglas de gobierno, el ciclo de trabajo **SDD (desarrollo guiado por especificaciones)** sobre [OpenSpec](https://github.com/Fission-AI/OpenSpec) y el **Consejo Ejecutivo** de agentes de IA que dirigen la empresa junto al CEO.

Funciona con cualquier asistente de IA compatible con `AGENTS.md` y `.agents/skills/`, y está optimizado para **Claude Code**.

---

## El universo Yizi

```mermaid
flowchart TB
    CEO["👤 CEO · Yefer<br/>autoridad final"]

    subgraph NUCLEO["⚛️ NÚCLEO · yizi-workflow"]
        direction LR
        VISION["V.I.S.I.O.N<br/>CTO"]
        JARVIS["J.A.R.V.I.S<br/>CDO"]
        EDITH["E.D.I.T.H<br/>CFO"]
        VIERNES["V.I.E.R.N.E.S<br/>CSO"]
        ULTRON["U.L.T.R.O.N<br/>COO"]
        AIDA["A.I.D.A<br/>diseño de agentes"]
        TERMY["T.E.R.M.Y<br/>talento humano"]
        MACRO{{"Autoridad MACRO<br/>preside Viernes"}}
    end

    subgraph SAT["🛰️ SATÉLITES (heredan el núcleo)"]
        direction LR
        SOL["Yizi Solutions<br/>tecnología e IA<br/>líder: Karen<br/>repo: yizi-solutions"]
        IMP["Yizi Publisher<br/>marketing y ventas<br/>líder: Homer<br/>(incubación)"]
        TAL["Yizi Talent<br/>outsourcing IA/software<br/>líder: Jocasta<br/>(incubación)"]
        PM["Yizi Projects<br/>casa de los proyectos MACRO<br/>líder: Herbie<br/>repo: yizi-projects"]
    end

    CEO --> NUCLEO
    ULTRON -. supervisa .-> AIDA
    ULTRON -. supervisa .-> TERMY
    VISION -. patrocina .-> SOL
    JARVIS -. patrocina .-> IMP
    ULTRON -. patrocina .-> TAL
    VIERNES -. patrocina .-> PM
    MACRO -. autoriza proyectos .-> PM
```

Cada satélite es un **repositorio separado** dentro de la organización [Yizi-Digital](https://github.com/Yizi-Digital) (`Yizi-Digital/<id>`). El primero es [`yizi-solutions`](https://github.com/Yizi-Digital/yizi-solutions); Publisher y Talent están en incubación y no se ofrecen todavía a clientes. **Yizi Projects** es la casa de todos los proyectos propios (MACRO): cada producto autorizado vive en su carpeta dentro de ese repo.

### Organigrama

Estado al 2026-11-18. Hoy hay **1 persona** (el CEO). Agentes de IA: **26 activos**: 5 del Consejo, 3 de área (Aida, Termy, Lince), 2 líderes de satélite (Karen, Herbie), Ábaco y Chaski en Yizi Solutions y 14 en el equipo de Yizi Projects. Jocasta tiene nombre aprobado, pero su satélite está en incubación y aún no tiene ficha. El CEO aprobó el 2026-11-18 el equipo de Yizi Publisher: Homer (líder), Ágora, Faro, Quirón y Prisma se activan con Publisher, y Sagita y Kepler con un disparador. Siguen sin ficha y **no cuentan como activos** hasta que el CEO apruebe el cambio `activar-yizi-publisher`. Al activarse Publisher, el grupo pasa a **31 agentes activos**, y a **33** con Sagita y Kepler. Los roles humanos sin contratar aparecen solo como **perfiles**, sin nombres. Lo mantiene Ultron en cada cambio de agentes (spec `jerarquia-agentes`).

```mermaid
flowchart TB
    CEO["👤 CEO<br/>autoridad final"]

    subgraph CONSEJO["Consejo Ejecutivo · núcleo (N1)"]
        direction LR
        VIERNES["V.I.E.R.N.E.S<br/>CSO · estrategia"]
        VISION["V.I.S.I.O.N<br/>CTO · tecnología"]
        JARVIS["J.A.R.V.I.S<br/>CDO · marca y ventas digitales"]
        EDITH["E.D.I.T.H<br/>CFO · finanzas"]
        ULTRON["U.L.T.R.O.N<br/>COO · operaciones"]
    end

    subgraph AREA["Agentes de área · núcleo (N1)"]
        direction LR
        AIDA["A.I.D.A<br/>diseño de agentes"]
        TERMY["T.E.R.M.Y<br/>talento humano"]
        LINCE["L.I.N.C.E<br/>verificador"]
    end

    subgraph SOL["Yizi Solutions · ✅ activo"]
        KAREN["K.A.R.E.N<br/>líder (N2)"]
        ABACO["Á.B.A.C.O<br/>analista de pilotos (N3)"]
        CHASKI["C.H.A.S.K.I<br/>El Guía Yizi en modo ayuda<br/>(agente del producto)"]
        PROMOTOR["👤 Perfil: Promotor de barrio<br/>por contratar"]
    end

    subgraph PRJ["Yizi Projects · ✅ activo · sin proyectos"]
        HERBIE["H.E.R.B.I.E<br/>líder (N2)"]
        subgraph GOB["Gobierno de proyectos (N3)"]
            direction LR
            ATLAS["A.T.L.A.S · PMO"]
            ORION["O.R.I.O.N · Program Manager"]
            VERA["V.E.R.A · Product Owner"]
            KAIZEN["K.A.I.Z.E.N · Scrum Master"]
        end
        subgraph TEC["Equipo técnico (N3)"]
            direction LR
            DEDALO["D.E.D.A.L.O · Arquitecto"]
            PIXEL["P.I.X.E.L · Frontend"]
            FORJA["F.O.R.J.A · Backend"]
            KIPU["K.I.P.U · Bases de datos"]
            IRIS["I.R.I.S · UI/UX"]
            HERMES["H.E.R.M.E.S · DevOps e Infra"]
        end
        subgraph IND["Revisión independiente (N3)"]
            direction LR
            CERBERO["C.E.R.B.E.R.O · Ciberseguridad"]
            ARGOS["A.R.G.O.S · QA"]
            TALOS["T.A.L.O.S · QE"]
            TEMIS["T.E.M.I.S · Legal"]
        end
    end

    subgraph PUB["Yizi Publisher · en incubación · aprobados, se activan con Publisher"]
        HOMER["H.O.M.E.R<br/>líder (N2)"]
        subgraph PUBACT["Se activan al arrancar (N3)"]
            direction LR
            AGORA["Á.G.O.R.A · Community Manager"]
            FARO["F.A.R.O · presencia local y reseñas"]
            QUIRON["Q.U.I.R.O.N · El Guía Yizi en modo enseñar IA"]
            PRISMA["P.R.I.S.M.A · diseño y video con IA"]
        end
        subgraph PUBDIS["Se activan con disparador (N3)"]
            direction LR
            SAGITA["S.A.G.I.T.A · anuncios y embudo"]
            KEPLER["K.E.P.L.E.R · analista de marketing"]
        end
        PUBPER["👤 Perfiles humanos mapeados, no se ofrecen hoy<br/>creador de contenido, fotógrafo o videógrafo, ilustrador, apoyo de atención, ejecutivo de cuentas"]
    end

    subgraph INC["En incubación"]
        JOCASTA["J.O.C.A.S.T.A<br/>Yizi Talent"]
    end

    subgraph EXT["👤 Perfiles externos · por contratar"]
        direction LR
        CONTADOR["Contador"]
        ABOGADO["Abogado"]
    end

    CEO --> CONSEJO
    ULTRON --> AIDA
    ULTRON --> TERMY
    ULTRON --> LINCE
    VISION -. patrocina .-> KAREN
    VIERNES -. patrocina .-> HERBIE
    JARVIS -. patrocina .-> HOMER
    ULTRON -. patrocina .-> JOCASTA
    HOMER --> PUBACT
    HOMER -.-> PUBDIS
    HOMER -.-> PUBPER
    KAREN --> ABACO
    KAREN -. coordina .-> PROMOTOR
    HERBIE --> GOB
    HERBIE --> TEC
    HERBIE --> IND
    ATLAS --> ORION --> VERA
    ORION --> KAIZEN
    CEO -. contrata .-> EXT
```

- **Línea continua:** a quién reporta.
- **Línea punteada:** quién patrocina un satélite o coordina a una persona.
- **👤 Perfil:** rol humano sin contratar. No lleva nombre de persona hasta que se contrate (spec `jerarquia-agentes`).
- **Equipo de Yizi Projects:** reporta formalmente a Herbie. En el día a día: Atlas → Orion → Vera y Kaizen → equipo técnico. Dédalo, Cerbero, Argos y Talos tienen línea técnica o de calidad con Vision.

### Jerarquía de agentes

| Nivel | Quién | Vive en |
|---|---|---|
| **N0** | CEO (humano) | Todo el universo |
| **N1** | Consejo Ejecutivo (Vision, Jarvis, Edith, Viernes, Ultron) y agentes de área (Aida, Termy, Lince) | Núcleo · heredado por todos los satélites |
| **N2** | Líder de satélite | Su satélite |
| **N3** | Especialistas de satélite | Su satélite |
| **N4** | Ejecutores efímeros (subagentes de una tarea) | Una tarea |

### El Consejo Ejecutivo

| Agente | Llámalo | Cargo | Custodia la compuerta de… |
|---|---|---|---|
| **V.I.S.I.O.N** | Vision | CTO | Viabilidad técnica, calidad y seguridad |
| **J.A.R.V.I.S** | Jarvis | CDO · Chief Digital Officer | Marca, cliente y canales digitales |
| **E.D.I.T.H** | Edith | CFO | Costo, precio y presupuesto |
| **V.I.E.R.N.E.S** | Viernes | CSO · Chief Strategy Officer | Alineación estratégica y foco |
| **U.L.T.R.O.N** | Ultron | COO | Operabilidad, capacidad y plazos |

Todos conocen todas las specs del núcleo; cada uno decide solo en su dominio. Sus nombres son **internos**: ante clientes, Yizi habla a través de **El Guía Yizi**.

---

## Los 14 núcleos (specs vigentes)

Viven en `openspec/specs/` y son la verdad vigente de cómo funciona Yizi.

| Spec | Qué define | Dueño |
|---|---|---|
| `cultura` | Nombre, misión, visión, valores, arquetipo, principios humano-IA, foco | CEO · Viernes |
| `consejo-ejecutivo` | Los cinco directivos, su dominio y su compuerta | CEO |
| `jerarquia-agentes` | Niveles N0–N4, reportes, herencia, escalamiento, fichas | Ultron |
| `gobierno-agentes` | Humano al mando, autonomía A1–A4, irreversibles, seguridad, veracidad | Ultron · Vision |
| `ciclo-sdd` | Fases, metadatos, tamaños, compuertas, registro del Consejo | Ultron |
| `calidad` | Definition of Done, escenarios como pruebas, revisión independiente | Vision |
| `arquitectura` | Stack de referencia, seguridad, estabilidad transaccional, IA responsable | Vision |
| `comunicacion` | Tono, identidad visual, arquitectura de marca, El Guía Yizi | Jarvis |
| `comercial` | Diagnóstico Flash → Sprint Inicial → Iteración y Escala | Jarvis · Viernes |
| `finanzas` | Estimación de costos, niveles de modelos de IA, consumo por ventana de 5 horas, precios | Edith |
| `satelites` | Modelo núcleo-satélite, registro, ciclo de vida, herencia | Viernes |
| `autoridad-macro` | Cómo se autorizan los proyectos propios de gran alcance | Viernes · CEO |
| `diseno-agentes` | Qué agentes necesita cada satélite: criterio, experiencia y referencias | Aida |
| `talento-humano` | Qué personas necesita Yizi y cómo se contratan | Termy |

Consúltalas con `openspec list --specs` y `openspec show <spec> --type spec`.

---

## El ciclo de trabajo

```mermaid
flowchart LR
    E["0 · Explorar<br/>(opcional)"] --> P["1 · Proponer"] --> C["2 · Consejo<br/>compuertas"] --> A["3 · Aprobación<br/>del CEO"] --> I["4 · Implementar<br/>contexto limpio"] --> V["5 · Verificar"] --> R["6 · Archivar"]
    C -- BLOQUEADO --> P
    I -- el plan falla --> P
```

| Tamaño | Cuándo | Revisan |
|---|---|---|
| **S** | < 1 día, reversible, sin dinero ni clientes | Solo el dueño + confirmación del CEO |
| **M** | ≤ 1 semana o un solo dominio | Dueño + agentes de los dominios afectados |
| **L** | Varios dominios, gasto o cambios al núcleo | Consejo completo |
| **MACRO** | Proyecto propio de gran alcance | Autoridad MACRO → decide el CEO |

---

## Inicio rápido

**Requisitos:** Node.js 22.12 o superior, Git y Claude Code (u otro asistente compatible).

1. Instala OpenSpec (una vez por computadora):

   ```bash
   npm install -g @fission-ai/openspec@latest
   ```

2. Clona el núcleo y regístralo como store (así los satélites pueden leerlo):

   ```bash
   git clone https://github.com/Yizi-Digital/yizi-workflow.git
   ```

   ```bash
   cd yizi-workflow && openspec store register . --id yizi-workflow
   ```

3. Abre Claude Code en la carpeta y habla con el Consejo:

   ```text
   Viernes, quiero lanzar una app de reservas para todos los restaurantes de la ciudad. ¿Encaja con Yizi?
   ```

   ```text
   /openspec-propose agregar pagos con tarjeta al menú digital
   ```

   ```text
   /yizi-consejo
   ```

> **Windows:** `.claude/skills/` usa enlaces simbólicos. Activa el modo de desarrollador y ejecuta `git config --global core.symlinks true` antes de clonar, o ejecuta `openspec update` después de clonar.

---

## Crear un satélite

1. Viernes propone el satélite con un cambio del núcleo (`/openspec-propose`), que actualiza `satelites/registro.yaml`.
2. El Consejo lo revisa (`/yizi-consejo`) y el CEO lo aprueba.
3. El skill `/yizi-satelite` genera un **repositorio separado** `Yizi-Digital/<id>` desde `satelites/plantilla/` (el CEO crea el repositorio vacío en GitHub o confirma su creación):
   - su `openspec/config.yaml` declara `references: [yizi-workflow]`, así OpenSpec entrega a los agentes el índice de las specs del núcleo;
   - su `.claude/settings.json` activa el plugin `yizi-nucleo@yizi`, así los cinco directivos y los skills de Yizi están disponibles sin copiarlos;
   - incluye la ficha de su líder N2.

Para instalar el plugin a mano en cualquier repositorio:

```text
/plugin install yizi-nucleo --marketplace Yizi-Digital/yizi-workflow
```

Cuando el núcleo cambia, los satélites lo adoptan con `git pull` en el núcleo y `claude plugin update yizi-nucleo@yizi`.

---

## Estructura

```
yizi-workflow/
├── AGENTS.md                 Instrucciones para cualquier agente de IA
├── CLAUDE.md                 Instrucciones específicas de Claude Code
├── openspec/
│   ├── config.yaml           Contexto y reglas de Yizi para OpenSpec
│   ├── specs/                Los 12 núcleos (verdad vigente)
│   └── changes/              Cambios en curso y archive/ (historial)
├── .claude/
│   ├── agents/               Fichas del Consejo (vision, jarvis, edith, viernes, ultron)
│   ├── skills/               Enlaces a .agents/skills/
│   └── settings.json         Permisos mínimos
├── .agents/skills/           openspec-* (flujo SDD) y yizi-* (consejo, satélite)
├── .claude-plugin/           Plugin yizi-nucleo + marketplace yizi
├── .openspec-store/          Identidad del núcleo como store de OpenSpec
├── finanzas/
│   └── consumo-ia.md         Registro mensual de consumo de IA (Edith)
└── satelites/
    ├── registro.yaml         Portafolio de satélites (cada uno en Yizi-Digital/<id>)
    └── plantilla/            Plantilla de satélite
```

---

<sub>Yizi Digital · Uso interno. Los nombres de los agentes del Consejo son nombres en clave internos y no se usan como marca ante clientes.</sub>
