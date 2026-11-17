# Consejo · big-bang-nucleo

| Campo | Valor |
|---|---|
| Dueño | V.I.E.R.N.E.S (Viernes) |
| Alcance | nucleo |
| Tipo / Tamaño | estrategico / L |
| Fecha de revisión | 2026-11-17 |

> Revisión de génesis: el Consejo aún no existía al iniciar este cambio, así que los veredictos se redactaron en la misma sesión que creó sus fichas, aplicando el checklist de cada una. Los siguientes cambios usan el skill `yizi-consejo`.

## Veredictos

| Agente | Compuerta | Veredicto | Condiciones |
|---|---|---|---|
| Vision | Viabilidad técnica | CONDICIONADO | Validar plugin y specs con las herramientas oficiales antes de archivar |
| Jarvis | Marca y cliente | CONDICIONADO | Nombres internos fuera de todo material para clientes |
| Edith | Costo y presupuesto | APROBADO | Fijar el límite mensual de gasto en IA |
| Viernes | Alineación estratégica | CONDICIONADO | El CEO confirma estados de satélites y nombres de líderes |
| Ultron | Operabilidad | APROBADO | Ninguna |

## Detalle

### Vision · Viabilidad técnica
**Veredicto:** CONDICIONADO
**Motivos:**
- Estructura estándar de OpenSpec 2.1; sin dependencias de ejecución ni infraestructura.
- Herencia por referencia (store + plugin), sin copias que se desincronicen.
- Stores (beta) y plugins son funciones recientes: riesgo de cambios de formato.
**Condiciones:** `openspec validate --strict` y `claude plugin validate` sin errores antes de archivar (el único aviso estricto del plugin, que el `CLAUDE.md` raíz no viaja con él, es intencional). *(Cumplida: ver tareas 2.6, 4.1 y 7.2.)*

### Jarvis · Marca y cliente
**Veredicto:** CONDICIONADO
**Motivos:**
- Tono, paleta y tipografías del Manual de Marca v2.0 incorporados a la spec `comunicacion`.
- Arquitectura de marca "Yizi <Descriptor>" evita confundir a los clientes.
- Los nombres del Consejo son de personajes de ficción con propiedad intelectual de terceros.
**Condiciones:** los nombres internos nunca aparecen ante clientes (requisito incluido en `comunicacion`).

### Edith · Costo y presupuesto
**Veredicto:** APROBADO
**Costo estimado:** 0 USD de infraestructura; tokens de IA de una sesión de trabajo y tiempo de revisión del CEO.
**Motivos:**
- Todo corre sobre herramientas que el CEO ya usa (Git, OpenSpec, Claude Code).
- La política de niveles de modelo reduce el gasto recurrente.
**Condiciones:** el CEO debe fijar el límite mensual de gasto en IA y herramientas (spec `finanzas`) en un cambio posterior.

### Viernes · Alineación estratégica
**Veredicto:** CONDICIONADO
**Motivos:**
- Da una sola estructura a todas las líneas sin diluir la marca madre.
- La Autoridad MACRO con límite de un proyecto protege la caja y el foco.
- Solo Yizi Soluciones queda activa: es la línea que describe el Manual de Marca.
**Condiciones:** el CEO confirma los estados propuestos en `satelites/registro.yaml` y aprueba (o cambia) los nombres de los líderes K.A.R.E.N, H.O.M.E.R y J.O.C.A.S.T.A.

### Ultron · Operabilidad
**Veredicto:** APROBADO
**Motivos:**
- 23 tareas pequeñas, con responsable y verificación.
- Las acciones hacia afuera (push, PR) quedan sujetas a confirmación humana.
**Condiciones:** Ninguna.

## Decisión del CEO

- Decisión: APROBADO para implementar y archivar (instrucción del CEO en la sesión: "Construye los specs base", rama `yizi/big-bang-corporate`).
- Fecha: 2026-11-17
- Pendientes del CEO: condiciones de Edith y Viernes (límite de gasto; estados de satélites y nombres de líderes).
- Anulaciones de compuertas BLOQUEADAS: ninguna.
