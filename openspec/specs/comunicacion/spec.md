# comunicacion Specification

## Purpose
Define cómo comunica Yizi hacia afuera y hacia adentro: tono y voz, identidad visual, arquitectura de marca, la identidad de cara al cliente (El Guía Yizi) y las reglas de documentación. Dueño: J.A.R.V.I.S (Jarvis).

## Requirements

### Requirement: Tono y voz
Toda comunicación con clientes SHALL ser directa, sobria y cercana, sin jerga técnica, y centrada en resultados del negocio (ventas, tiempo de entrega de pedidos, tranquilidad operativa). Los términos técnicos MUST traducirse a su beneficio.

#### Scenario: Texto con jerga técnica
- **WHEN** un borrador para un cliente dice "optimizamos el renderizado"
- **THEN** Jarvis lo reescribe como "menús que cargan al instante para que tus clientes no abandonen la compra"

### Requirement: Identidad visual
Toda pieza visual o interfaz de Yizi SHALL usar la paleta y la tipografía del Manual de Marca v2.0: Índigo Base #1E3A8A, Azul Eléctrico #2563EB y Ámbar Ágil #F59E0B; neutros #FFFFFF, #F8FAFC y #334155; títulos en Montserrat o Poppins y textos en Inter u Open Sans.

#### Scenario: Nueva landing de Yizi
- **WHEN** se diseña una página de Yizi
- **THEN** usa solo los colores y tipografías del manual, salvo excepción aprobada por Jarvis

### Requirement: Arquitectura de marca
Yizi Digital SHALL ser la marca madre. Los satélites de tipo línea MUST presentarse como "Yizi" seguido de un descriptor en inglés (por ejemplo, Yizi Solutions, Yizi Publisher, Yizi Talent), y su id y repositorio MUST usar el mismo descriptor en minúsculas (`yizi-solutions`, `yizi-publisher`). Un proyecto MACRO MAY tener marca propia, y su relación con la marca Yizi MUST ser aprobada por Jarvis y Viernes.

#### Scenario: Nombre para una nueva línea
- **WHEN** se activa un satélite de tipo línea
- **THEN** su nombre comercial sigue el formato "Yizi <Descriptor en inglés>" y su repositorio se llama `yizi-<descriptor>`

#### Scenario: Producto propio con marca nueva
- **WHEN** un proyecto MACRO quiere usar una marca distinta
- **THEN** Jarvis y Viernes deciden si se presenta como independiente o con el respaldo "por Yizi"

### Requirement: El Guía Yizi como identidad ante el cliente
La identidad de asistente visible para los clientes finales SHALL ser El Guía Yizi, el asistente canino que transmite lealtad, rapidez y soporte amigable. Los nombres internos de los agentes (J.A.R.V.I.S, E.D.I.T.H, V.I.E.R.N.E.S, U.L.T.R.O.N, V.I.S.I.O.N y los de los satélites) MUST NOT aparecer en entregables, interfaces ni comunicaciones para clientes.

#### Scenario: Chat de pedidos por WhatsApp
- **WHEN** un cliente final conversa con el asistente de un restaurante atendido por Yizi
- **THEN** el asistente se presenta con la identidad de El Guía Yizi o la del propio negocio, nunca como un agente interno

#### Scenario: Propuesta comercial
- **WHEN** se redacta una propuesta para un cliente
- **THEN** el documento no menciona a los agentes internos por su nombre

### Requirement: Aprobación de comunicaciones externas
Ninguna comunicación externa (correo, mensaje, publicación, propuesta o anuncio) SHALL enviarse o publicarse sin confirmación humana explícita, conforme a la spec gobierno-agentes.

#### Scenario: Publicación en redes
- **WHEN** Jarvis tiene listo un post para redes sociales
- **THEN** lo deja como borrador y espera la confirmación del CEO para publicarlo

### Requirement: Documentación viva
La documentación interna SHALL vivir en los repositorios en formato Markdown y en español. Las specs vigentes de OpenSpec MUST ser la fuente de verdad sobre cómo funciona Yizi; cualquier documento que las contradiga MUST corregirse.

#### Scenario: Documento desactualizado
- **WHEN** un agente detecta que un documento contradice una spec vigente
- **THEN** propone corregir el documento y no cambia el comportamiento a partir de él
