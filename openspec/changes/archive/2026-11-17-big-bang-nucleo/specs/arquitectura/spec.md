# Spec Delta

## Purpose

Fija los estándares técnicos base del núcleo que hacen posible la Robustez Invisible: stack de referencia, seguridad por defecto, estabilidad transaccional, IA aplicada responsable y registro de decisiones técnicas. Dueño: V.I.S.I.O.N (Vision).

## ADDED Requirements

### Requirement: Stack de referencia
Las soluciones web de Yizi SHALL construirse por defecto con el stack de referencia del Manual de Marca: interfaces basadas en React y Vite, desplegadas en plataformas serverless. Usar otro stack MUST justificarse en `design.md` y contar con el veredicto favorable de Vision.

#### Scenario: Proyecto que necesita otro stack
- **WHEN** un cliente exige una plataforma distinta
- **THEN** el `design.md` explica la desviación, sus costos y riesgos, y Vision la aprueba o la rechaza

### Requirement: Seguridad por defecto
Toda solución SHALL cumplir una línea base de seguridad: secretos fuera del código, tráfico cifrado, mínimo privilegio en accesos, dependencias revisadas contra vulnerabilidades conocidas y validación de toda entrada externa. Yizi MUST NOT almacenar datos completos de tarjetas; los pagos se procesan con pasarelas certificadas.

#### Scenario: Integración de pagos
- **WHEN** una solución acepta pagos con tarjeta
- **THEN** usa una pasarela certificada y no guarda los datos de la tarjeta en sistemas de Yizi ni del cliente

### Requirement: Estabilidad transaccional
Los flujos de pedidos, pagos e inventario SHALL ser confiables: una operación repetida por error MUST NOT duplicar pedidos ni cobros, y todo fallo MUST quedar visible para el negocio en lugar de perderse en silencio.

#### Scenario: Doble envío de un pedido
- **WHEN** un cliente final pulsa dos veces "confirmar pedido" con red lenta
- **THEN** el sistema registra un solo pedido

#### Scenario: Fallo al guardar
- **WHEN** un pedido no puede guardarse
- **THEN** el negocio recibe un aviso claro y el pedido no se pierde sin rastro

### Requirement: IA aplicada responsable
Toda funcionalidad que use modelos de IA SHALL declarar en `design.md`: el modelo y su nivel de costo, el costo estimado por uso, el comportamiento de respaldo si el modelo falla y si sus resultados requieren revisión humana. Los datos de clientes MUST NOT usarse para entrenar modelos sin consentimiento escrito.

#### Scenario: Asistente de WhatsApp con IA
- **WHEN** se diseña un asistente que responde pedidos por WhatsApp
- **THEN** el diseño indica qué pasa si el modelo no responde (por ejemplo, derivar a una persona) y cuánto cuesta cada conversación

### Requirement: Registro de decisiones técnicas
Toda decisión técnica relevante SHALL registrarse en el `design.md` del cambio con contexto, alternativas consideradas, decisión y consecuencias, para que cualquier agente futuro entienda por qué se tomó.

#### Scenario: Cambio de base de datos
- **WHEN** se decide cambiar la base de datos de un proyecto
- **THEN** el `design.md` documenta las alternativas evaluadas y el motivo de la elección

### Requirement: Control de versiones
Todo trabajo SHALL versionarse en git, en una rama por cambio, con commits que mencionen el cambio OpenSpec. La rama principal de cada repositorio MUST recibir cambios solo mediante revisión y con confirmación humana.

#### Scenario: Agente intenta escribir en la rama principal
- **WHEN** un agente tiene trabajo listo para la rama principal
- **THEN** lo deja en su rama, abre la solicitud de revisión cuando se le pide y espera la aprobación humana
