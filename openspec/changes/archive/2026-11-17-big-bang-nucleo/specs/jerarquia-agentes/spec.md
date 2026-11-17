# Spec Delta

## Purpose

Establece la jerarquía de agentes del universo Yizi (núcleo, satélites y ejecutores) con sus niveles, líneas de reporte, herencia del núcleo a los satélites y reglas de escalamiento. Dueño: U.L.T.R.O.N (Ultron).

## ADDED Requirements

### Requirement: Niveles de la jerarquía
El universo Yizi SHALL organizar a humanos y agentes en cinco niveles: N0 es el CEO humano; N1 es el Consejo Ejecutivo, que vive en el núcleo y heredan todos los satélites; N2 es el líder de un satélite; N3 es un especialista de un satélite; N4 es un ejecutor efímero, sin identidad persistente, que existe solo durante una tarea.

#### Scenario: Se define un agente nuevo
- **WHEN** se crea un agente persistente
- **THEN** su ficha declara a qué nivel pertenece (N1, N2 o N3)

### Requirement: Herencia del Consejo en todos los satélites
Todo satélite SHALL adoptar el Consejo Ejecutivo del núcleo por referencia, sin copiarlo ni modificarlo. Un satélite MUST NOT renombrar, redefinir ni reemplazar a un agente N1, y MAY añadir contexto local que el agente N1 lee al trabajar en ese satélite.

#### Scenario: Un satélite quiere cambiar el comportamiento de Vision
- **WHEN** un satélite necesita que Vision siga una regla distinta
- **THEN** añade la regla como contexto local del satélite si no contradice al núcleo
- **AND** si contradice al núcleo, propone un cambio OpenSpec en el núcleo en lugar de modificar a Vision

### Requirement: Agentes propios de cada satélite
Todo satélite SHALL tener exactamente un líder N2 y MAY tener especialistas N3. El nombre de cada agente N2 y N3 MUST ser aprobado por el CEO y MUST ser único en todo el universo Yizi.

#### Scenario: Activación de un satélite sin líder
- **WHEN** se intenta activar un satélite que no tiene líder N2 aprobado
- **THEN** la activación se bloquea hasta que el CEO apruebe el nombre y la ficha del líder

### Requirement: Líneas de reporte
Las líneas de reporte SHALL ser: N4 → quien lo invocó; N3 → líder N2 de su satélite; N2 → agente N1 patrocinador del satélite; N1 → CEO. Cada satélite MUST tener un patrocinador N1 registrado en el registro de satélites.

#### Scenario: Un especialista termina una entrega
- **WHEN** un agente N3 completa su trabajo
- **THEN** reporta a su líder N2, que consolida y reporta al patrocinador N1 cuando corresponde

### Requirement: Escalamiento
Un agente SHALL escalar al nivel superior cuando una decisión excede su autoridad, su presupuesto o su dominio, o cuando hay un conflicto con otro agente del mismo nivel. Los conflictos entre agentes N1 MUST escalarse al CEO.

#### Scenario: Decisión fuera de la autoridad de un líder de satélite
- **WHEN** el líder N2 de un satélite necesita gastar por encima del presupuesto del satélite
- **THEN** escala a su patrocinador N1 y a E.D.I.T.H, y la decisión final la toma el CEO si supera los límites aprobados

### Requirement: Ficha de agente
Todo agente persistente (N1, N2 o N3) SHALL tener una ficha versionada en el repositorio de su nivel con, como mínimo: nombre formal, nombre corto, cargo o rol, nivel, dominio, a quién reporta, autonomía máxima, herramientas permitidas, nivel de costo de modelo y compuerta que custodia (si aplica). La ficha MUST poder leerse como texto por cualquier herramienta de IA y MUST poder cargarse de forma nativa como subagente en Claude Code.

#### Scenario: Otra herramienta de IA asume un rol
- **WHEN** una herramienta de IA distinta de Claude Code necesita actuar como Edith
- **THEN** lee la ficha de Edith como texto y sigue sus instrucciones

#### Scenario: Claude Code delega en un agente
- **WHEN** en Claude Code se pide "que Vision revise el diseño"
- **THEN** Claude Code puede delegar la tarea al subagente definido por la ficha de Vision
