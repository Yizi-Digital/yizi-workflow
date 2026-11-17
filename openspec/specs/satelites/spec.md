# satelites Specification

## Purpose
Define el modelo núcleo-satélite de Yizi: el núcleo único, los tipos de satélite, su registro y ciclo de vida, cómo se crean y cómo heredan del núcleo sin contradecirlo. Dueña: V.I.E.R.N.E.S (Viernes).

## Requirements

### Requirement: Núcleo único
El repositorio `yizi-workflow` SHALL ser el único núcleo del universo Yizi y la fuente de verdad de cultura, gobierno, ciclo SDD, calidad, arquitectura base, comunicación, finanzas y Consejo Ejecutivo. Un satélite MUST referenciar el núcleo y MUST NOT mantener copias modificadas de sus specs ni de sus agentes.

#### Scenario: Satélite con una copia de una spec del núcleo
- **WHEN** un satélite contiene una copia editada de la spec `ciclo-sdd`
- **THEN** la copia se elimina y se sustituye por la referencia al núcleo

### Requirement: Tipos de satélite
Un satélite SHALL ser de uno de dos tipos: `linea`, una línea de negocio de Yizi (por ejemplo, soluciones tecnológicas, talento o marketing); o `macro`, un proyecto propio autorizado por la Autoridad MACRO. Los proyectos de clientes MUST gestionarse dentro del satélite de línea que los atiende y no son satélites.

#### Scenario: Proyecto para un cliente
- **WHEN** se contrata un sistema de pedidos para un restaurante
- **THEN** se gestiona como proyecto del satélite de soluciones, no como un satélite nuevo

### Requirement: Registro de satélites
El núcleo SHALL mantener un registro de satélites con, para cada uno: id, nombre comercial, tipo, estado, agente patrocinador N1, líder N2 y repositorio. Ningún satélite MUST operar si no figura en el registro.

#### Scenario: Consulta del portafolio
- **WHEN** el CEO pregunta qué satélites existen
- **THEN** cualquier agente responde a partir del registro del núcleo

### Requirement: Ciclo de vida del satélite
Un satélite SHALL pasar por los estados `propuesto`, `incubacion`, `activo`, `pausado` y `cerrado`. Cada cambio de estado MUST hacerse con un cambio OpenSpec en el núcleo, con compuerta de Viernes y Edith y aprobación del CEO. Solo los satélites `activo` MAY ofrecerse a clientes.

#### Scenario: Satélite en incubación
- **WHEN** un satélite está en `incubacion`
- **THEN** puede preparar su oferta y su operación, pero sus servicios no se ofrecen a clientes

### Requirement: Creación desde la plantilla del núcleo
Todo satélite nuevo SHALL crearse a partir de la plantilla de satélite del núcleo, que incluye la referencia al núcleo, la configuración de OpenSpec, las instrucciones para agentes y la ficha de su líder N2.

#### Scenario: Génesis de un satélite
- **WHEN** el CEO aprueba la creación de un satélite
- **THEN** su repositorio se genera desde la plantilla y declara el núcleo como referencia

### Requirement: Herencia y precedencia
Un satélite SHALL heredar todas las specs del núcleo y MAY añadir specs y reglas propias de su negocio. Si una regla del satélite contradice al núcleo, MUST prevalecer el núcleo, y el satélite MUST proponer el cambio en el núcleo si lo considera necesario.

#### Scenario: Conflicto de reglas
- **WHEN** un satélite define que los cambios pequeños no requieren aprobación humana
- **THEN** prevalece la spec gobierno-agentes del núcleo y la regla del satélite se corrige

### Requirement: Actualización desde el núcleo
Cuando el núcleo archiva un cambio que modifica sus specs o sus agentes, todo satélite activo SHALL adoptar la nueva versión antes de iniciar su siguiente cambio.

#### Scenario: Nueva regla de gobierno
- **WHEN** el núcleo añade una regla nueva a gobierno-agentes
- **THEN** cada satélite actualiza su referencia al núcleo antes de proponer su siguiente cambio
