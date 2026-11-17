# Spec Delta

## MODIFIED Requirements

### Requirement: Misión y visión vigentes
La misión y la visión del grupo y de cada satélite SHALL ser las del Manual de Marca vigente (`marca/manual-de-marca.md`, sección 2), aprobadas por el CEO, y los agentes MUST citarlas sin reinterpretarlas. La misión del grupo SHALL ser hacer fácil la tecnología y la IA para todos, cerrando las brechas desde las más pequeñas hasta las más grandes, con un satélite que guía cada frente.

#### Scenario: Un agente redacta un documento que menciona la misión
- **WHEN** un agente escribe una propuesta, presentación o documento interno que menciona la misión o la visión
- **THEN** usa el texto vigente del manual y no una versión inventada

#### Scenario: Alguien quiere cambiar la misión
- **WHEN** un agente o persona propone modificar la misión o la visión
- **THEN** el cambio se tramita como un cambio OpenSpec de tipo `estrategico` y tamaño `L`
- **AND** solo entra en vigor cuando el CEO lo aprueba

#### Scenario: Documento de un satélite
- **WHEN** un agente redacta un documento propio de un satélite
- **THEN** usa la misión y visión de ese satélite y, si menciona al grupo, la del núcleo

## ADDED Requirements

### Requirement: Autogestión y crecimiento rentable
El universo Yizi SHALL organizarse para operar de forma autogestionada y rentable: cada satélite MUST tener un líder, un patrocinador, un proceso escrito y un camino a la rentabilidad, y los agentes SHALL proponer mejoras que reduzcan la dependencia de intervención manual, sin saltarse la aprobación humana de las acciones irreversibles.

#### Scenario: Tarea repetitiva detectada
- **WHEN** un agente detecta que el CEO hace a mano la misma tarea varias veces
- **THEN** propone un cambio OpenSpec para automatizarla o asignarla a un agente

#### Scenario: Satélite sin camino a la rentabilidad
- **WHEN** un satélite no tiene definido cómo genera ingresos
- **THEN** Edith y Viernes lo señalan antes de proponer su activación
