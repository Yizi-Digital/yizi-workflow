# Spec Delta

## ADDED Requirements

### Requirement: Repositorio propio en la organización Yizi Digital
Cada satélite SHALL vivir en su propio repositorio dentro de la organización de GitHub `YiziDigital`, con un nombre igual a su id (por ejemplo, `YiziDigital/yizi-solutions`). El núcleo MUST NOT contener el código ni las specs de un satélite; solo su entrada en el registro y la plantilla. Crear el repositorio remoto MUST contar con confirmación del CEO.

#### Scenario: Génesis de Yizi Solutions
- **WHEN** el CEO aprueba crear el satélite `yizi-solutions`
- **THEN** su contenido se genera en un repositorio separado `YiziDigital/yizi-solutions` y el registro del núcleo apunta a esa URL

#### Scenario: Specs de un satélite dentro del núcleo
- **WHEN** alguien intenta añadir specs de negocio de un satélite en `yizi-workflow`
- **THEN** se rechaza y se proponen en el repositorio del satélite
