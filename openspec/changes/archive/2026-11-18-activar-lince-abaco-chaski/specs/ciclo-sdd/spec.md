# Spec Delta

## ADDED Requirements

### Requirement: Un pull request abierto por repositorio
Cada repositorio SHALL tener como máximo un pull request abierto por flujo de trabajo. Los cambios OpenSpec de un mismo flujo MUST sumarse a ese pull request en lugar de abrir otro. Un pull request nuevo solo se abre cuando el anterior se fusiona o cuando el CEO pide un flujo separado.

#### Scenario: Cambio pequeño con un PR abierto
- **WHEN** hay un pull request abierto en un repositorio y llega un cambio del mismo flujo
- **THEN** el cambio se suma a ese pull request y no se abre uno nuevo
