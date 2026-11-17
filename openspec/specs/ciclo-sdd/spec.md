# ciclo-sdd Specification

## Purpose
Define el ciclo de desarrollo guiado por especificaciones (SDD) de Yizi sobre OpenSpec, con sus fases, metadatos, compuertas del Consejo y criterios de archivo, para todo cambio del núcleo y de los satélites. Dueño: U.L.T.R.O.N (Ultron).

## Requirements

### Requirement: Spec antes que acción
Todo cambio de comportamiento (software, proceso, oferta comercial, política o estructura de agentes) SHALL empezar como un cambio OpenSpec. Los cambios que no alteran comportamiento (erratas, formato, refactor sin efecto visible) MAY declarar `skip_specs: true`, pero igualmente MUST tener propuesta y tareas.

#### Scenario: Petición de construir directamente
- **WHEN** el CEO pide "agrega pagos con tarjeta al menú"
- **THEN** el agente crea primero el cambio OpenSpec con propuesta, specs y tareas, y no escribe código hasta su aprobación

#### Scenario: Corrección de una errata
- **WHEN** solo se corrige una errata en un documento
- **THEN** el cambio puede usar `skip_specs: true`

### Requirement: Fases del ciclo
Todo cambio SHALL recorrer estas fases en orden: 0 Explorar (opcional), 1 Proponer, 2 Revisión del Consejo, 3 Aprobación humana, 4 Implementar, 5 Verificar y 6 Archivar. Un cambio MUST poder volver a una fase anterior cuando la revisión o la implementación descubren que el plan es incorrecto.

#### Scenario: El plan falla durante la implementación
- **WHEN** durante la fase 4 se descubre que un requisito es inviable
- **THEN** el cambio vuelve a la fase 1, se actualizan sus artefactos y se repiten las fases 2 y 3

### Requirement: Metadatos obligatorios de la propuesta
Toda `proposal.md` SHALL empezar con una tabla que declare: Dueño (agente responsable), Alcance (`nucleo` o el id de un satélite), Tipo (`tecnico`, `marca-comunicacion`, `comercial`, `financiero`, `operacion`, `estrategico` o `macro`), Tamaño (`S`, `M`, `L` o `MACRO`) y las Compuertas requeridas.

#### Scenario: Propuesta sin tamaño
- **WHEN** una propuesta no declara su tamaño
- **THEN** Ultron la devuelve a la fase 1 antes de convocar al Consejo

### Requirement: Tamaños de cambio
El tamaño de un cambio SHALL determinarse así: S si se completa en menos de un día, es reversible y no toca dinero ni clientes; M si dura hasta una semana o afecta a un solo dominio; L si dura más de una semana, afecta a varios dominios, compromete gasto o cambia el núcleo; MACRO si es un proyecto propio de Yizi según la spec autoridad-macro.

#### Scenario: Cambio que toca precios
- **WHEN** un cambio pequeño modifica el precio de un servicio
- **THEN** se clasifica al menos como M, porque toca dinero

### Requirement: Compuertas del Consejo
Las compuertas SHALL activarse según el tamaño: en S, solo el dueño; en M, el dueño más cada agente cuyo dominio se ve afectado; en L, el Consejo completo; en MACRO, el proceso de la Autoridad MACRO. Los dominios son: técnico → Vision; marca y cliente → Jarvis; costo y precio → Edith; estrategia y foco → Viernes; operación y plazos → Ultron.

#### Scenario: Cambio M que afecta interfaz y costo
- **WHEN** un cambio M modifica la pantalla de pedidos y añade una herramienta de pago
- **THEN** revisan el dueño, Vision (técnico), Jarvis (cliente) y Edith (costo)

### Requirement: Registro del Consejo
Los veredictos de las compuertas SHALL registrarse en `consejo.md`, dentro de la carpeta del cambio, con el agente, el veredicto (APROBADO, CONDICIONADO o BLOQUEADO) y sus motivos. Un veredicto BLOQUEADO MUST impedir la implementación hasta que se resuelva, salvo que el CEO lo anule por escrito en ese mismo registro.

#### Scenario: Compuerta bloqueada
- **WHEN** Edith bloquea un cambio por falta de presupuesto
- **THEN** el cambio no pasa a implementación hasta que se ajuste el plan o el CEO registre su decisión de continuar

### Requirement: Validación estricta
Antes de la aprobación humana y antes de archivar, `openspec validate <cambio> --strict` SHALL terminar sin errores ni advertencias.

#### Scenario: Validación con advertencias
- **WHEN** la validación estricta reporta un requisito sin escenario
- **THEN** el cambio no se presenta a aprobación hasta corregirlo

### Requirement: Implementación orquestada y en contexto limpio
La implementación SHALL hacerse en un contexto limpio, siguiendo `tasks.md`, con cada grupo de tareas asignado a un agente responsable y orquestado por Ultron. Cada tarea completada MUST marcarse en `tasks.md` en el momento en que se termina.

#### Scenario: Implementación interrumpida
- **WHEN** una sesión se corta a mitad de la implementación
- **THEN** la siguiente sesión retoma desde la primera tarea sin marcar de `tasks.md`

### Requirement: Archivo y documentación viva
Un cambio SHALL archivarse solo cuando todas sus tareas están completas, la verificación pasó y la validación estricta no tiene errores. Al archivar, las specs vigentes MUST actualizarse con el delta y el archivo MUST guardarse en git junto con la implementación.

#### Scenario: Archivo con tareas pendientes
- **WHEN** se intenta archivar un cambio con tareas sin marcar
- **THEN** el archivo se detiene y Ultron informa qué tareas faltan

### Requirement: Idioma de los artefactos
Los artefactos de OpenSpec SHALL escribirse en español, manteniendo en inglés los encabezados estructurales (`## ADDED Requirements`, `### Requirement:`, `#### Scenario:`) y las palabras clave SHALL y MUST.

#### Scenario: Requisito escrito con "DEBE"
- **WHEN** un requisito usa "DEBE" en lugar de SHALL o MUST
- **THEN** el agente lo corrige antes de validar
