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

### Requirement: Límite de gasto mensual
El universo Yizi SHALL tener un límite mensual de gasto en IA y herramientas fijado por el CEO. Al alcanzar el 80 % del límite, Edith MUST avisar al CEO; al alcanzar el 100 %, el trabajo no crítico MUST pausarse hasta que el CEO decida.

#### Scenario: Gasto al 80 %
- **WHEN** el gasto del mes alcanza el 80 % del límite
- **THEN** Edith avisa al CEO con el detalle por satélite y por agente

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
