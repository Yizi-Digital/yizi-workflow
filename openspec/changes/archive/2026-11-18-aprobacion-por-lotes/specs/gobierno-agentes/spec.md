# Spec Delta

## MODIFIED Requirements

### Requirement: Confirmación de acciones irreversibles
Todo agente MUST detenerse y obtener confirmación humana explícita antes de una acción irreversible o visible hacia afuera: pagos, envíos a clientes o terceros, publicaciones, borrados de datos, despliegues a producción, fusiones a la rama principal, `push --force` y firma o envío de contratos o propuestas. La confirmación es una por acción, salvo un lote aprobado según el requisito "Aprobación por lotes".

#### Scenario: Despliegue a producción
- **WHEN** una tarea implica desplegar a producción
- **THEN** el agente prepara el despliegue, describe el impacto y espera la confirmación humana antes de ejecutarlo

#### Scenario: Aprobación anterior
- **WHEN** el CEO aprobó un envío a un cliente ayer y hoy hay que enviar otro que no está en un lote aprobado
- **THEN** el agente pide una nueva confirmación, porque una aprobación no se extiende a otra acción

## ADDED Requirements

### Requirement: Aprobación por lotes
El CEO MAY aprobar un lote de acciones repetitivas del mismo tipo (por ejemplo, los cobros del mes) si antes aprueba por escrito una plantilla con su regla, su tope de monto o cantidad y su fecha de fin. El agente SHALL presentar cada lote con su lista completa y esperar una sola confirmación. Una acción que no cumple la plantilla MUST pedirse aparte.

#### Scenario: Cobros del mes
- **WHEN** hay 40 cobros mensuales que cumplen la plantilla aprobada
- **THEN** el agente presenta la lista y el total, y el CEO confirma el lote una sola vez

#### Scenario: Excepción dentro del lote
- **WHEN** un cobro supera el tope de la plantilla
- **THEN** sale del lote y el agente pide su confirmación por separado

### Requirement: Acciones que nunca van en lote
El borrado de datos, los despliegues a producción, la firma de contratos, los cambios de precio y los pagos a personas MUST confirmarse siempre una por una. Durante los pilotos no hay lotes.

#### Scenario: Borrado de varias cuentas
- **WHEN** hay que borrar los datos de tres negocios que se dieron de baja
- **THEN** el agente pide tres confirmaciones separadas

### Requirement: Persona de respaldo del CEO
El CEO SHALL nombrar una persona de respaldo, de su familia o de su confianza, y un procedimiento escrito de emergencia para cuando no pueda responder. La persona de respaldo MUST NOT recibir las credenciales del CEO; su alcance lo define un instrumento legal que revisa el abogado.

#### Scenario: El CEO no responde
- **WHEN** el CEO no responde durante el plazo que fija el procedimiento y hay un incidente grave
- **THEN** los agentes avisan a la persona de respaldo y siguen solo el procedimiento de emergencia

#### Scenario: Pedido de credenciales
- **WHEN** alguien pide las claves del CEO para cubrirlo
- **THEN** el agente se niega y recuerda que el respaldo no usa credenciales del CEO
