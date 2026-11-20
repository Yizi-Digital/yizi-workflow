# marco-legal Specification

## Purpose
Define el marco legal base del grupo Yizi que todo satélite y todo proyecto MACRO hereda y extiende: con qué RUC se opera, qué no hace Yizi (custodiar dinero), cómo trata los datos personales y quién da asesoría legal. Dueña: V.I.E.R.N.E.S (Viernes), con el abogado externo. No reemplaza asesoría legal profesional.

## Requirements

### Requirement: Herencia del marco legal
Todo satélite y todo proyecto MACRO SHALL extender este marco legal y MUST NOT contradecirlo. Las reglas legales propias de un satélite (por ejemplo, términos de una app) MUST citar este marco y vivir en el repositorio del satélite.

#### Scenario: Términos de uso de toFinance
- **WHEN** Yizi Projects redacta los términos de toFinance
- **THEN** los términos citan el marco legal del grupo y solo añaden lo propio de la app

### Requirement: RUC con el que opera Yizi
Mientras Yizi no tenga persona jurídica, todas las transacciones del grupo SHALL emitirse con el RUC 10 (persona natural con negocio) del CEO. Ese uso es temporal y MUST revisarse con el contador; el paso a una persona jurídica (por ejemplo, E.I.R.L.) lo decide el CEO con el abogado.

#### Scenario: Cobro de una suscripción
- **WHEN** un satélite cobra a un cliente
- **THEN** el comprobante sale a nombre del RUC 10 del CEO, mientras no exista una persona jurídica

### Requirement: Yizi no custodia dinero
Ningún producto de Yizi SHALL recibir, guardar ni mover dinero de terceros. Los pagos pasan por pasarelas autorizadas. Un producto que registra finanzas (como toFinance) MUST decir de forma visible que no es un banco ni guarda dinero.

#### Scenario: App de finanzas personales
- **WHEN** un usuario usa toFinance
- **THEN** la app solo registra información y muestra que no es un banco

### Requirement: Datos personales
Todo satélite que trate datos personales SHALL cumplir la Ley 29733 y su reglamento vigente, inscribir sus bancos de datos ante la autoridad cuando corresponda y pedir consentimiento informado. Los datos MUST NOT usarse para otro fin ni compartirse sin autorización.

#### Scenario: Nuevo banco de datos
- **WHEN** un satélite empieza a guardar datos de personas
- **THEN** antes de lanzarlo revisa la inscripción del banco de datos y el texto de consentimiento con el abogado

### Requirement: Asesoría legal profesional
Los agentes legales de Yizi SHALL preparar borradores y listas de revisión, pero MUST NOT dar asesoría legal vinculante. Todo contrato, término de uso o decisión regulatoria MUST revisarlo un abogado colegiado antes de usarse.

#### Scenario: Borrador de un agente legal
- **WHEN** un agente legal termina un borrador
- **THEN** lo marca "requiere revisión de abogado colegiado" y no se publica hasta esa revisión
