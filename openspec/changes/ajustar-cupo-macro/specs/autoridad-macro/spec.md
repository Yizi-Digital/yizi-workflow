# Spec Delta

## MODIFIED Requirements

### Requirement: Veredictos de la Autoridad MACRO
La decisión sobre un proyecto MACRO SHALL ser una de tres: AUTORIZADO, EN ESPERA o RECHAZADO, con sus motivos. AUTORIZADO SHALL registrar el proyecto en Yizi Projects en estado `incubacion`, con Viernes como patrocinadora, solo si hay cupo libre. El CEO MAY limitar la autorización al Discovery del proyecto; entonces el proyecto SHALL registrarse en `discovery` con su tope y MUST NOT ocupar el cupo. EN ESPERA guarda el proyecto en la cartera para revisarlo después. La decisión MUST registrarse en el registro del Consejo del cambio.

#### Scenario: Proyecto autorizado
- **WHEN** el CEO autoriza un proyecto MACRO y ningún proyecto está en `incubacion` ni en `activo`
- **THEN** se añade a la lista de proyectos de Yizi Projects en el registro de satélites, en `incubacion`, con Viernes como patrocinadora

#### Scenario: Autorización limitada al Discovery
- **WHEN** el CEO autoriza solo la fase de validación de un proyecto MACRO, con tope de 24 h, S/ 100 y fecha de fin
- **THEN** el proyecto se registra en `discovery` con ese tope y el cupo MACRO sigue libre

### Requirement: Límite de proyectos MACRO simultáneos
El número de proyectos MACRO en `incubacion` o `activo` SHALL estar limitado por el valor `limites.macro_simultaneos_max` del registro de satélites, que Edith propone según la caja disponible y el CEO decide. Mientras la caja sea limitada, el valor SHALL ser un proyecto MACRO a la vez. Los proyectos en `propuesto`, `discovery`, `pausado` o `cerrado` MUST NOT contar para este límite. Yizi MAY tener varios proyectos en `propuesto` y varios en `discovery` a la vez, dentro del tope total de Discovery.

#### Scenario: Segundo proyecto con el límite alcanzado
- **WHEN** ya hay un proyecto MACRO en `incubacion` y el CEO autoriza otro
- **THEN** el nuevo queda EN ESPERA hasta que se libere el cupo o el CEO cambie el límite

#### Scenario: Dos Discovery y el cupo libre
- **WHEN** hay dos proyectos en `discovery`, cada uno con su tope aprobado, y ninguno en `incubacion` ni en `activo`
- **THEN** el cupo MACRO figura libre y la Autoridad MACRO puede autorizar un proyecto en `incubacion`

#### Scenario: Pasar de Discovery a incubación con el cupo lleno
- **WHEN** un proyecto en `discovery` cumple su criterio de éxito y otro proyecto ya está en `incubacion`
- **THEN** Viernes recomienda como máximo EN ESPERA y el proyecto no pasa a `incubacion` hasta que se libere el cupo o el CEO elija cuál sigue

## ADDED Requirements

### Requirement: Estados de un proyecto MACRO
Todo proyecto de Yizi Projects SHALL tener en el registro uno de seis estados: `propuesto` (en evaluación), `discovery` (validación con tope, sin código), `incubacion` (autorizado para construir), `activo` (en el mercado), `pausado` (sin horas ni caja en curso) o `cerrado`. Solo `incubacion` y `activo` SHALL ocupar el cupo MACRO.

#### Scenario: Qué estados ocupan el cupo
- **WHEN** hay un proyecto en `propuesto`, dos en `discovery` y uno en `pausado`
- **THEN** el cupo MACRO figura libre, porque ninguno está en `incubacion` ni en `activo`

#### Scenario: Estado que no existe
- **WHEN** un proyecto figura en el registro con un estado fuera de esta lista
- **THEN** Lince lo marca como fallo de verificación y Viernes corrige el estado

### Requirement: Pausa real
Un proyecto con horas del CEO o caja en curso MUST NOT figurar como `pausado`. Un proyecto que sale de `pausado` MUST cumplir la regla del estado al que vuelve: tope libre para `discovery` o cupo libre para `incubacion`.

#### Scenario: Proyecto pausado con trabajo autorizado
- **WHEN** un proyecto figura como `pausado` pero tiene horas o caja autorizadas en curso
- **THEN** Viernes propone corregir su estado en el registro al que corresponde a su trabajo, por ejemplo `discovery`

#### Scenario: Reanudar un proyecto pausado
- **WHEN** un proyecto en `pausado` quiere volver a `incubacion` y otro proyecto ya ocupa el cupo
- **THEN** sigue en `pausado` hasta que se libere el cupo o el CEO cambie el límite

### Requirement: Discovery con tope propio
Un proyecto SHALL pasar a `discovery` solo cuando el CEO apruebe por escrito su tope: horas del CEO por semana, caja total en soles y fecha de fin. El proyecto MUST tener también una hipótesis principal y un criterio de cierre. Un Discovery MUST NOT escribir código de producto, cobrar a usuarios ni lanzar una marca al público. Un Discovery no exige el expediente MACRO completo ni el veredicto de la Autoridad MACRO.

#### Scenario: Discovery sin fecha de fin
- **WHEN** un proyecto en `discovery` no tiene fecha de fin aprobada por el CEO
- **THEN** Ultron detiene su trabajo nuevo y Viernes pide al CEO que fije la fecha

#### Scenario: Discovery que necesita código
- **WHEN** un Discovery necesita construir código de producto para seguir
- **THEN** el trabajo para y Viernes tramita el paso a `incubacion` ante la Autoridad MACRO

### Requirement: Tope total de Discovery
El registro de satélites SHALL fijar un tope total para todos los Discovery abiertos, en horas del CEO por semana y en caja total en soles. Edith MUST proponer las cifras según la caja disponible y el CEO MUST decidirlas. La suma de los topes aprobados de todos los proyectos en `discovery` MUST NOT superar el tope total. Mientras el CEO no fije el tope total, ningún Discovery nuevo MAY abrirse.

#### Scenario: Discovery nuevo que no cabe en el tope total
- **WHEN** el CEO quiere abrir un Discovery nuevo y la suma de su tope con los topes abiertos supera el tope total
- **THEN** el proyecto sigue en `propuesto` y Viernes presenta al CEO tres opciones: esperar, reducir un tope o pedir a Edith que revise el tope total

### Requirement: Vigilancia del consumo de Discovery
U.L.T.R.O.N SHALL llevar el consumo real de horas y caja de cada Discovery y la suma de todos. Ultron MUST avisar al CEO cuando un Discovery o la suma lleguen al 80 % de su tope, y MUST detener el trabajo de ese Discovery al llegar al 100 %. Las horas de Discovery MUST NOT desplazar el trabajo comprometido con clientes de un satélite `activo`.

#### Scenario: Aviso al 80 %
- **WHEN** la suma de horas consumidas por todos los Discovery llega al 80 % del tope total
- **THEN** Ultron avisa al CEO con el consumo de cada Discovery antes de seguir

#### Scenario: Choque con un cliente
- **WHEN** una semana no alcanzan las horas del CEO para un Discovery y para la entrega a un cliente de Yizi Solutions
- **THEN** Ultron da prioridad al cliente y mueve las horas del Discovery a la semana siguiente

### Requirement: Fin de un Discovery
Cuando un Discovery llegue a su fecha de fin, agote su tope o cumpla su criterio de cierre, Viernes SHALL proponer al CEO uno de cuatro caminos: pasar a `incubacion`, extender con un tope nuevo, pausar o cerrar. Edith MUST dar su recomendación financiera. Pasar a `incubacion` MUST exigir el expediente MACRO completo, el veredicto AUTORIZADO del CEO y cupo libre.

#### Scenario: Discovery con tope agotado
- **WHEN** un Discovery consume todas sus horas aprobadas antes de su fecha de fin
- **THEN** Ultron detiene su trabajo y Viernes presenta al CEO los cuatro caminos con la recomendación de Edith

#### Scenario: Discovery exitoso sin expediente
- **WHEN** un Discovery confirma su hipótesis pero el proyecto no tiene expediente MACRO completo
- **THEN** Viernes devuelve el paso a `incubacion` hasta completar el expediente
