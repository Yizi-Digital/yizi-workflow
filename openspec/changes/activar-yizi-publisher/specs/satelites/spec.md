# Spec Delta

## ADDED Requirements

### Requirement: Yizi Publisher activo con IA en el centro
Yizi Publisher SHALL figurar como satélite `activo` de tipo `linea`, con repositorio `Yizi-Digital/yizi-publisher`. Cada servicio que ofrezca MUST incluir una lección en la que el cliente usa la IA por sí mismo. Sus servicios MUST limitarse a lo que Yizi hace en remoto con IA; lo presencial solo se mapea. Ninguna pieza MUST publicarse sin la confirmación de una persona de Yizi y del cliente.

#### Scenario: Servicio sin lección de IA
- **WHEN** Publisher propone un servicio que no enseña al cliente a usar la IA
- **THEN** Viernes lo bloquea en su compuerta hasta que el servicio incluya la lección

#### Scenario: Cliente que pide un servicio presencial
- **WHEN** un cliente pide fotos, video o una visita en su local
- **THEN** Publisher responde que hoy no se ofrece, no da plazos ni precios y registra una señal para Viernes

#### Scenario: Publicación preparada por un agente
- **WHEN** un agente de Publisher deja lista una publicación para la cuenta de un cliente
- **THEN** la pieza no se programa hasta que una persona de Yizi y el cliente la confirmen, y queda registrada la aprobación

#### Scenario: Consulta del estado de Publisher
- **WHEN** un agente consulta el registro de satélites
- **THEN** encuentra `yizi-publisher` en estado `activo` con la URL de su repositorio
