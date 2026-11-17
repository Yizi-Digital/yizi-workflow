# Spec Delta

## REMOVED Requirements

### Requirement: Límite de gasto mensual
**Reason**: El CEO decidió que el límite no es una cifra fija con avisos al 80 % y 100 %, sino el consumo observado del plan de IA (ventanas de 5 horas y consumo mensual).
**Migration**: Reemplazado por "Límite de gasto según consumo observado" y "Consumo por ventana de 5 horas".

## ADDED Requirements

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
