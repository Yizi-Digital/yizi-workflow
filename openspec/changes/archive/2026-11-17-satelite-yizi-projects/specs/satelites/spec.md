# Spec Delta

## MODIFIED Requirements

### Requirement: Tipos de satélite
Un satélite SHALL ser de uno de dos tipos: `linea`, una línea de negocio de Yizi (por ejemplo, soluciones tecnológicas, talento o marketing); o `macro`, cuyo único satélite es Yizi Projects, la casa de todos los proyectos propios autorizados por la Autoridad MACRO. Un proyecto MACRO MUST vivir dentro de Yizi Projects y no es un satélite. Los proyectos de clientes MUST gestionarse dentro del satélite de línea que los atiende y no son satélites.

#### Scenario: Proyecto para un cliente
- **WHEN** se contrata un sistema de pedidos para un restaurante
- **THEN** se gestiona como proyecto del satélite de soluciones, no como un satélite nuevo

#### Scenario: Proyecto MACRO autorizado
- **WHEN** el CEO autoriza un proyecto MACRO
- **THEN** el proyecto se crea dentro del repositorio de Yizi Projects y no se crea un satélite nuevo
