# Spec Delta

## ADDED Requirements

### Requirement: Organigrama vivo
El organigrama de Yizi (sección "Organigrama" del `README.md` del núcleo) SHALL mostrar a todos los agentes persistentes del universo, con su nivel, a quién reportan y su estado. Todo cambio OpenSpec que agregue, renombre, active o retire un agente MUST actualizar el organigrama en el mismo cambio. Ultron SHALL verificarlo antes de archivar.

#### Scenario: Agente nuevo aprobado
- **WHEN** el CEO aprueba el nombre de un agente nuevo
- **THEN** el mismo cambio lo añade al organigrama con su estado (aprobado, activo o retirado)

#### Scenario: Cambio sin actualizar el organigrama
- **WHEN** un cambio agrega un agente y no actualiza el organigrama
- **THEN** Ultron no lo archiva hasta que se actualice

### Requirement: Roles humanos como perfiles
Los roles humanos que aún no están contratados SHALL aparecer en el organigrama y en los mapas de talento solo como perfiles (rol, dedicación y estado), sin nombres de personas. El nombre de una persona MUST aparecer solo cuando esté contratada y con su consentimiento.

#### Scenario: Promotor aún no contratado
- **WHEN** el organigrama muestra el rol de Promotor de barrio sin contratar
- **THEN** aparece como perfil "Promotor de barrio · por contratar", sin nombre
