# comercial Specification

## Purpose
Define el proceso comercial y de descubrimiento con clientes de Yizi: el Ciclo de Servicio (Diagnóstico Flash, Sprint Inicial y Iteración y Escala), la calificación de oportunidades por satélite y las reglas de las propuestas comerciales. Dueño: J.A.R.V.I.S (Jarvis), con V.I.E.R.N.E.S (Viernes) para el encaje estratégico.

## Requirements

### Requirement: Ciclo de Servicio Yizi
Todo proyecto de cliente SHALL seguir el Ciclo de Servicio: 1 Diagnóstico Flash, 2 Sprint Inicial (MVP) y 3 Iteración y Escala. Cada fase del ciclo de servicio MUST gestionarse como uno o más cambios OpenSpec en el satélite que atiende al cliente.

#### Scenario: Nuevo cliente restaurante
- **WHEN** un restaurante contrata a Yizi
- **THEN** el trabajo empieza con un Diagnóstico Flash y no con desarrollo

### Requirement: Diagnóstico Flash
El Diagnóstico Flash SHALL producir un documento con el flujo de pedidos, los cuellos de botella y dónde pierde tiempo y dinero el negocio; sus hallazgos MUST convertirse en la propuesta del primer cambio OpenSpec. Lo SHALL liderar el líder N2 del satélite (en Yizi Solutions, Karen). Jarvis MUST ser dueño del método y la plantilla y apoyar en marca y cliente. Un satélite MAY adaptar la plantilla solo con aprobación de Jarvis.

#### Scenario: Diagnóstico terminado
- **WHEN** termina el Diagnóstico Flash de un cliente
- **THEN** existe una propuesta OpenSpec cuyo apartado Why cita los cuellos de botella encontrados

#### Scenario: Quién lidera un diagnóstico en Yizi Solutions
- **WHEN** un negocio de barrio empieza el Diagnóstico Flash en Yizi Solutions
- **THEN** Karen lidera el diagnóstico y firma el documento como responsable
- **AND** Jarvis revisa que la plantilla, los textos y el trato con el cliente siguen la marca

#### Scenario: Un satélite quiere cambiar la plantilla
- **WHEN** Karen propone un formulario más corto para el Diagnóstico Flash
- **THEN** el formulario se usa solo después de que Jarvis lo aprueba

### Requirement: Sprint Inicial
El Sprint Inicial SHALL entregar en días una solución mínima (por ejemplo, una landing o webapp con menú interactivo y rutas automatizadas) que estandarice la recepción de pedidos. Su alcance MUST limitarse a lo aprobado en las specs del cambio.

#### Scenario: Pedido de alcance adicional
- **WHEN** el cliente pide una función nueva durante el Sprint Inicial
- **THEN** se registra como un cambio posterior y no se añade al sprint en curso

### Requirement: Iteración y Escala
Después del Sprint Inicial, las mejoras (inventario, pasarelas de pago, análisis de retención y otras) SHALL priorizarse por su impacto en ventas o en tiempo operativo, y cada una MUST tramitarse como un cambio OpenSpec independiente.

#### Scenario: Dos mejoras compiten
- **WHEN** el cliente quiere inventario y analítica a la vez
- **THEN** se prioriza la que más reduce el cuello de botella identificado en el diagnóstico

### Requirement: Calificación de oportunidades
Toda oportunidad comercial SHALL asignarse a un satélite activo. Una oportunidad que no encaja en ningún satélite activo MUST NOT ofrecerse al cliente y MUST registrarse como señal para V.I.E.R.N.E.S.

#### Scenario: Petición fuera de las líneas activas
- **WHEN** un prospecto pide un servicio que ningún satélite activo ofrece
- **THEN** el agente no lo cotiza y registra la oportunidad para que Viernes la evalúe

### Requirement: Propuestas comerciales
Toda propuesta comercial SHALL incluir: el problema del cliente en sus palabras, el alcance (alineado con las specs), lo que queda fuera de alcance, el plazo y un precio validado por E.D.I.T.H. Su envío MUST contar con confirmación humana.

#### Scenario: Propuesta sin precio validado
- **WHEN** una propuesta tiene un precio que Edith no ha validado
- **THEN** no se presenta al CEO para su envío hasta que Edith la valide
