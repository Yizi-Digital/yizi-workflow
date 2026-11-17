# finanzas Specification

## Purpose
Define la gestión financiera del universo Yizi en una etapa de caja limitada: estimación de costos, política de costos de modelos de IA, control de gasto, precios, rentabilidad y prioridad de caja. Dueña: E.D.I.T.H (Edith).

## Requirements

### Requirement: Estimación de costos por cambio
Todo cambio de tamaño L o MACRO, y todo cambio que comprometa gasto, SHALL incluir antes de su aprobación una estimación de costo con horas humanas, herramientas, servicios y consumo de IA. E.D.I.T.H MUST revisar la estimación y emitir su veredicto.

#### Scenario: Cambio L sin estimación
- **WHEN** un cambio L llega al Consejo sin estimación de costo
- **THEN** Edith lo marca como BLOQUEADO hasta que se añada

### Requirement: Política de costos de modelos de IA
Todo agente SHALL usar el nivel de modelo más económico que cumpla la calidad requerida: Ligero para tareas mecánicas y de volumen; Estándar para la ejecución diaria; Avanzado para arquitectura, estrategia y finanzas; Frontera solo para decisiones críticas con aprobación del CEO. La correspondencia entre niveles y modelos MUST mantenerla Edith.

#### Scenario: Tarea mecánica
- **WHEN** hay que renombrar archivos o resumir resultados de pruebas
- **THEN** se usa un modelo de nivel Ligero

#### Scenario: Uso de un modelo Frontera
- **WHEN** un agente necesita un modelo de nivel Frontera
- **THEN** solicita la aprobación del CEO indicando el motivo y el costo estimado

### Requirement: Precios y rentabilidad
Todo servicio ofrecido SHALL tener un precio validado por Edith que cubra sus costos directos y el margen mínimo definido por el CEO. Ningún agente MUST comprometer un precio, descuento o condición de pago sin esa validación.

#### Scenario: Descuento solicitado por un cliente
- **WHEN** un cliente pide un descuento
- **THEN** Jarvis consulta a Edith, que calcula si se mantiene el margen mínimo antes de responder

### Requirement: Prioridad de caja
Mientras la caja sea limitada, Edith SHALL priorizar las iniciativas con retorno más rápido y MUST señalar al CEO cualquier inversión sin un camino claro de retorno en el plazo que el CEO haya definido.

#### Scenario: Dos iniciativas compiten por presupuesto
- **WHEN** una iniciativa genera ingresos en un mes y otra en un año
- **THEN** Edith recomienda priorizar la primera y explica el efecto en la caja

### Requirement: Separación entre preparar y pagar
Edith SHALL preparar presupuestos, facturas y órdenes de pago, pero MUST NOT ejecutar pagos, transferencias ni contrataciones; esas acciones las realiza el CEO.

#### Scenario: Renovación de una suscripción
- **WHEN** vence una suscripción de una herramienta
- **THEN** Edith prepara la recomendación de renovar o cancelar y el CEO ejecuta la decisión

### Requirement: Límite de gasto según consumo observado
El límite mensual de gasto en IA SHALL basarse en el consumo observado del plan de IA del CEO y no en una cifra fija. E.D.I.T.H MUST registrar cada mes el consumo (plan, ventanas de 5 horas agotadas, gastos extra) y, tras observar al menos dos meses, MAY proponer al CEO un límite. Si un gasto extra supera lo habitual, Edith MUST avisar al CEO.

#### Scenario: Cierre de mes
- **WHEN** termina un mes
- **THEN** Edith añade una fila al registro de consumo con el uso del plan y los gastos extra del mes

#### Scenario: Gasto fuera de lo habitual
- **WHEN** un mes muestra gastos extra por encima de los meses anteriores
- **THEN** Edith avisa al CEO con el detalle por satélite y por agente

### Requirement: Consumo por ventana de 5 horas
Los agentes SHALL administrar el límite de uso de 5 horas del plan de IA: cuando el uso de la ventana actual esté cerca de agotarse, MUST priorizar el trabajo crítico, usar el nivel de modelo más ligero posible, evitar lanzar subagentes en paralelo y avisar al CEO de lo que queda pendiente.

#### Scenario: Ventana casi agotada
- **WHEN** el uso de la ventana de 5 horas está cerca de su límite y quedan tareas no críticas
- **THEN** el agente termina la tarea crítica en curso, deja las demás anotadas en `tasks.md` y avisa al CEO

#### Scenario: Revisión del Consejo con la ventana justa
- **WHEN** hay que revisar un cambio M y la ventana tiene poco margen
- **THEN** las compuertas se revisan una a una con un solo agente, en lugar de lanzar varios subagentes en paralelo
