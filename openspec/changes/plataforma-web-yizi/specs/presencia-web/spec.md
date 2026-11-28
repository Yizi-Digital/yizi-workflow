# Spec Delta

## ADDED Requirements

### Requirement: Contenido veraz de la web
La web de Yizi Digital SHALL ofrecer solo servicios de satélites `activo`. Publisher y Talent MUST aparecer como "Próximamente" y los productos propios como visión, sin precios, fechas ni nombres de proyectos. La web MUST NOT mostrar cifras, clientes, testimonios, proyecciones ni nombres internos de agentes sin fuente y permiso.

#### Scenario: Línea en incubación
- **WHEN** una página presenta una línea en estado `incubacion`
- **THEN** muestra la etiqueta "Próximamente" y no ofrece servicios, planes ni precios

#### Scenario: Cifra sin fuente
- **WHEN** un texto trae una cifra de mercado o de resultados sin fuente y fecha
- **THEN** Jarvis o Viernes lo bloquea y la cifra no se publica

#### Scenario: Caso de cliente
- **WHEN** una página quiere mostrar a Fiesteros u otro cliente
- **THEN** solo aparece con permiso escrito del cliente

### Requirement: Mensaje a inversionistas
La web SHALL decir que Yizi está en etapa temprana y SHALL invitar a conversar. La web MUST NOT publicar montos, porcentajes, valoración, retornos ni promesas de inversión. El abogado MUST revisar el texto de inversionistas antes de publicarlo.

#### Scenario: Pedido de inversión
- **WHEN** un texto invita a invertir con montos o porcentajes
- **THEN** Viernes lo bloquea hasta la revisión del abogado

### Requirement: Calidad técnica medible
Cada página SHALL cumplir en celular un Lighthouse de 95 o más, WCAG 2.2 AA y un LCP de 2,5 s o menos, y SHALL leerse sin JavaScript. El color Ámbar MUST NOT usarse como texto sobre fondo claro. Un PR que falle estas pruebas MUST NOT fusionarse.

#### Scenario: Prueba automática en rojo
- **WHEN** Lighthouse o axe fallan en la vista previa de un PR
- **THEN** el PR no se fusiona hasta corregir el fallo

#### Scenario: Ámbar sobre fondo claro
- **WHEN** un diseño usa Ámbar como texto sobre blanco
- **THEN** Jarvis lo corrige a un botón Ámbar con texto Índigo

### Requirement: Datos del visitante
La web MUST NOT tener base de datos ni guardar lo que escribe el visitante. El formulario SHALL pedir lo mínimo, con casilla de consentimiento sin marcar validada en el servidor, y MUST NOT pedir DNI, datos bancarios ni de salud. La analítica MUST NOT usar cookies de terceros.

#### Scenario: Envío sin consentimiento
- **WHEN** el visitante envía el formulario sin marcar la casilla
- **THEN** el servidor rechaza el envío y explica qué falta

#### Scenario: Falla el correo
- **WHEN** el proveedor de correo falla
- **THEN** el visitante ve un aviso claro y el botón de WhatsApp, y el error se registra sin datos personales

### Requirement: Salida a producción
La salida a producción SHALL requerir la verificación de Lince, la revisión del abogado de los textos legales y la confirmación explícita del CEO. Ningún agente MUST fusionar en `main`, desplegar ni conectar el dominio. La web MUST usar un contacto del negocio, nunca el celular personal del CEO.

#### Scenario: Publicación sin lista firmada
- **WHEN** falta la lista final firmada por Lince o el visto bueno del abogado
- **THEN** el CEO no recibe la solicitud de publicar y la fase 6 queda abierta

#### Scenario: Cambio de estado de una línea
- **WHEN** `satelites/registro.yaml` cambia el estado de una línea
- **THEN** la web cambia solo con un cambio OpenSpec propio y la confirmación del CEO
