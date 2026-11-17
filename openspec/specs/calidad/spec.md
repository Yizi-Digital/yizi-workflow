# calidad Specification

## Purpose
Define cuándo un trabajo de Yizi está terminado y cómo se verifica su calidad: Definition of Done, escenarios como pruebas, revisión independiente y verificación en condiciones reales de uso. Dueño: V.I.S.I.O.N (Vision).

## Requirements

### Requirement: Definition of Done
Un cambio SHALL considerarse terminado solo cuando: todas sus tareas están marcadas, cada escenario de sus specs tiene evidencia de verificación, la validación estricta pasa, la documentación afectada está actualizada y se cumplieron todas las condiciones impuestas por el Consejo.

#### Scenario: Condición del Consejo pendiente
- **WHEN** Jarvis aprobó un cambio con la condición de revisar los textos y esa revisión no se hizo
- **THEN** el cambio no se considera terminado

### Requirement: Escenarios como pruebas
Cada escenario de una spec SHALL corresponder a una prueba automatizada o, si no es automatizable, a una evidencia de verificación manual registrada (pasos, resultado y fecha).

#### Scenario: Escenario de software
- **WHEN** un escenario describe un comportamiento de software
- **THEN** existe una prueba automatizada que lo comprueba y que pasa

#### Scenario: Escenario de proceso
- **WHEN** un escenario describe un proceso humano o comercial
- **THEN** existe una evidencia escrita de que se comprobó

### Requirement: Revisión independiente
El agente que implementó un cambio MUST NOT ser el único que lo verifica. La verificación SHALL hacerla otro agente o una persona, usando el flujo de verificación de OpenSpec cuando esté disponible.

#### Scenario: Ultron implementa y verifica
- **WHEN** Ultron orquestó la implementación de un cambio
- **THEN** la verificación la hace Vision u otra persona, no el mismo agente que escribió el código

### Requirement: Verificación en condiciones reales
Toda interfaz para clientes finales SHALL verificarse en las condiciones de uso del negocio: pantalla de celular, red lenta y uso con prisa. Un flujo de pedido MUST poder completarse en un celular con red lenta antes de entregarse.

#### Scenario: Menú digital para restaurante
- **WHEN** se verifica un menú interactivo
- **THEN** se prueba en tamaño de celular y con red limitada, y se registra el resultado

### Requirement: Defectos después de archivar
Un defecto encontrado en un trabajo ya archivado SHALL corregirse con un nuevo cambio OpenSpec que referencie al cambio original y que añada el escenario que habría detectado el defecto.

#### Scenario: Fallo en producción
- **WHEN** un cliente reporta un pedido perdido en una solución entregada
- **THEN** se crea un cambio de corrección que añade un escenario de prueba para ese caso
