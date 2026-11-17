# Spec Delta

## MODIFIED Requirements

### Requirement: Arquitectura de marca
Yizi Digital SHALL ser la marca madre. Los satélites de tipo línea MUST presentarse como "Yizi" seguido de un descriptor en inglés (por ejemplo, Yizi Solutions, Yizi Growth, Yizi Talent), y su id y repositorio MUST usar el mismo descriptor en minúsculas (`yizi-solutions`). Un proyecto MACRO MAY tener marca propia, y su relación con la marca Yizi MUST ser aprobada por Jarvis y Viernes.

#### Scenario: Nombre para una nueva línea
- **WHEN** se activa un satélite de tipo línea
- **THEN** su nombre comercial sigue el formato "Yizi <Descriptor en inglés>" y su repositorio se llama `yizi-<descriptor>`

#### Scenario: Producto propio con marca nueva
- **WHEN** un proyecto MACRO quiere usar una marca distinta
- **THEN** Jarvis y Viernes deciden si se presenta como independiente o con el respaldo "por Yizi"
