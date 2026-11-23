# Spec Delta

## MODIFIED Requirements

### Requirement: Veredictos de la Autoridad MACRO
La decisión sobre un proyecto MACRO SHALL ser una de tres: AUTORIZADO, EN ESPERA o RECHAZADO, con sus motivos. AUTORIZADO SHALL registrar el proyecto en Yizi Projects en `incubacion`, con Viernes como patrocinadora, solo si hay cupo libre. El CEO MAY limitar la autorización al Discovery del proyecto. Entonces el proyecto SHALL pasar a `discovery` según el requisito "Discovery con tope propio" y MUST NOT ocupar el cupo. EN ESPERA SHALL dejar el proyecto en `propuesto`, en la cartera, para revisarlo después. La decisión MUST registrarse en el registro del Consejo del cambio.

#### Scenario: Proyecto autorizado
- **WHEN** el CEO autoriza un proyecto MACRO y ningún proyecto está en `incubacion` ni en `activo`
- **THEN** se añade a la lista de proyectos de Yizi Projects en el registro de satélites, en `incubacion`, con Viernes como patrocinadora

#### Scenario: Autorización limitada al Discovery
- **WHEN** el CEO autoriza solo la fase de prueba de un proyecto MACRO, con tope aprobado y tope total fijado
- **THEN** el proyecto pasa a `discovery` con ese tope y el cupo MACRO sigue libre

#### Scenario: Veredicto EN ESPERA
- **WHEN** el CEO da el veredicto EN ESPERA a un proyecto en `propuesto`
- **THEN** el proyecto sigue en `propuesto` y no figura como `pausado`

### Requirement: Límite de proyectos MACRO simultáneos
El número de proyectos MACRO en `incubacion` o `activo` SHALL estar limitado por `limites.macro_simultaneos_max` del registro de satélites. Edith propone ese valor según la caja disponible y el CEO lo decide. Mientras la caja sea limitada, el valor SHALL ser un proyecto MACRO a la vez. Los proyectos en `propuesto`, `discovery`, `pausado` o `cerrado` MUST NOT contar para este límite. Yizi MAY tener varios proyectos en `propuesto` y varios en `discovery`, dentro del tope total de Discovery.

#### Scenario: Segundo proyecto con el límite alcanzado
- **WHEN** ya hay un proyecto MACRO en `incubacion` y el CEO autoriza otro
- **THEN** el nuevo sigue en `propuesto` hasta que se libere el cupo o el CEO cambie el límite

#### Scenario: Dos Discovery y el cupo libre
- **WHEN** hay dos proyectos en `discovery`, cada uno con su tope aprobado, y ninguno en `incubacion` ni en `activo`
- **THEN** el cupo MACRO figura libre y la Autoridad MACRO puede autorizar un proyecto en `incubacion`

#### Scenario: Pasar de Discovery a incubación con el cupo lleno
- **WHEN** un proyecto en `discovery` cumple su criterio de éxito y otro proyecto ya está en `incubacion`
- **THEN** Viernes recomienda como máximo EN ESPERA
- **AND** el proyecto no pasa a `incubacion` hasta que se libere el cupo o el CEO elija cuál sigue

## ADDED Requirements

### Requirement: Estados de un proyecto MACRO
Todo proyecto de Yizi Projects SHALL tener en el registro uno de seis estados: `propuesto`, `discovery`, `incubacion`, `activo`, `pausado` o `cerrado`. Solo `incubacion` y `activo` SHALL ocupar el cupo MACRO. El estado `activo` de un proyecto MUST NOT confundirse con el estado `activo` de un satélite (spec `satelites`).

#### Scenario: Qué estados ocupan el cupo
- **WHEN** hay un proyecto en `propuesto`, dos en `discovery` y uno en `pausado`
- **THEN** el cupo MACRO figura libre, porque ninguno está en `incubacion` ni en `activo`

#### Scenario: Estado que no existe
- **WHEN** un proyecto figura en el registro con un estado fuera de esta lista
- **THEN** Lince lo marca como fallo de verificación y Viernes corrige el estado

### Requirement: En espera no es un estado
"En espera" MUST NOT usarse como estado del registro. Un proyecto en `discovery`, `incubacion` o `activo` que el CEO pone en espera SHALL pasar a `pausado`. Un proyecto en `propuesto` que el CEO pone en espera SHALL seguir en `propuesto`.

#### Scenario: El CEO pone en espera un proyecto en curso
- **WHEN** el CEO pone en espera un proyecto en `discovery`
- **THEN** Viernes lo pasa a `pausado` en el registro
- **AND** Herbie actualiza las secciones 1 y 4 de su ficha (spec `ficha-proyecto-macro` de Yizi Projects)

#### Scenario: "En espera" escrito como estado
- **WHEN** un proyecto figura en el registro con el estado "en espera"
- **THEN** Lince lo marca como fallo y Viernes lo cambia a `pausado` o a `propuesto`, según la regla

### Requirement: Id del proyecto igual a su carpeta
El id de cada proyecto en el registro MUST coincidir con el nombre de su carpeta en `proyectos/` de Yizi Projects. Si el proyecto cambia de nombre, Herbie SHALL cambiar la carpeta y el id en el mismo cambio.

#### Scenario: Id distinto de la carpeta
- **WHEN** el id de un proyecto en el registro no coincide con su carpeta
- **THEN** Lince lo marca como fallo y Viernes alinea el id con la carpeta

### Requirement: Proyectos sin autorizar ante clientes
Un proyecto en `propuesto` o `discovery` MUST NOT ofrecerse ni mencionarse a clientes como servicio de Yizi. Ese proyecto MUST NOT aparecer en propuestas comerciales.

#### Scenario: Propuesta comercial
- **WHEN** un agente prepara una propuesta comercial y un proyecto está en `propuesto` o `discovery`
- **THEN** el agente no ofrece ni menciona ese proyecto como servicio de Yizi

### Requirement: Pausa real
Un proyecto con horas del CEO o caja en curso MUST NOT figurar como `pausado`. Un proyecto en `pausado` MAY guardar su tope aprobado y sin usar en la sección 4 de su ficha. Un proyecto que sale de `pausado` MUST cumplir la regla del estado al que vuelve. Volver a `discovery` SHALL contar como un Discovery nuevo. Volver a `incubacion` exige cupo libre.

#### Scenario: Proyecto pausado con trabajo en curso
- **WHEN** un proyecto figura como `pausado` pero alguien gasta horas o caja en él
- **THEN** Viernes propone al CEO parar ese gasto o pasar el proyecto al estado que corresponde, por ejemplo `discovery`

#### Scenario: Reanudar un proyecto pausado hacia Discovery
- **WHEN** el CEO retoma un proyecto `pausado` con un tope guardado de 4 h por semana, 24 h totales y S/ 100
- **THEN** el proyecto pasa a `discovery` solo con tres condiciones: tope total fijado, tope que cabe en él y fecha de fin nueva
- **AND** si falta alguna de las tres, el proyecto sigue en `pausado`

#### Scenario: Reanudar un proyecto pausado hacia incubación
- **WHEN** un proyecto en `pausado` quiere volver a `incubacion` y otro proyecto ya ocupa el cupo
- **THEN** sigue en `pausado` hasta que se libere el cupo o el CEO cambie el límite

### Requirement: Discovery con tope propio
Un proyecto SHALL pasar a `discovery` solo cuando el CEO apruebe por escrito su tope. El tope MUST tener horas del CEO por semana, horas totales, caja en soles y fecha de fin. Antes, Edith MUST revisar el tope y escribir sus supuestos. El proyecto MUST tener una hipótesis principal y un criterio de cierre. Un Discovery no exige el expediente MACRO completo ni el veredicto de la Autoridad MACRO.

#### Scenario: Discovery sin fecha de fin
- **WHEN** un proyecto en `discovery` no tiene fecha de fin aprobada por el CEO
- **THEN** Ultron detiene sus sesiones de agentes y Viernes pide al CEO que fije la fecha

#### Scenario: Tope sin revisión de Edith
- **WHEN** Viernes lleva al CEO el tope de un Discovery sin la revisión de Edith
- **THEN** el CEO no lo aprueba todavía y Edith revisa el tope con sus supuestos

### Requirement: Código de producto en un Discovery
Un Discovery MUST NOT escribir código de producto, cobrar a usuarios ni lanzar una marca al público. Código de producto es software que corre en un servidor o guarda datos reales de usuarios. Un Discovery MAY usar un prototipo sin servidor ni datos reales, como pantallas dibujadas o una hoja de cálculo.

#### Scenario: Prototipo permitido
- **WHEN** un Discovery prueba unas pantallas dibujadas o una hoja de cálculo sin servidor y sin datos reales de usuarios
- **THEN** el trabajo sigue en `discovery`, porque no es código de producto

#### Scenario: Discovery que necesita código
- **WHEN** un Discovery necesita código de producto para seguir
- **THEN** el trabajo para y Viernes tramita el paso a `incubacion` ante la Autoridad MACRO

### Requirement: Textos externos de un Discovery
J.A.R.V.I.S SHALL revisar, antes de usarlo, todo texto o prototipo de un Discovery que vea una persona externa. Esto incluye la guía de entrevista, la invitación, la pantalla de prueba y el consentimiento. Una persona MUST confirmar cada envío. Esos textos MUST NOT mostrar nombres internos de agentes. Si un agente habla con el público, SHALL presentarse como El Guía Yizi.

#### Scenario: Invitación a una entrevista
- **WHEN** un Discovery prepara una invitación para entrevistar a una persona externa
- **THEN** Jarvis revisa el texto antes de usarlo
- **AND** una persona confirma cada envío
- **AND** el texto firma como El Guía Yizi, sin nombres internos de agentes

### Requirement: Marca pública de un Discovery
Un Discovery MUST NOT crear perfiles públicos, dominio ni logo sin aprobación de Jarvis. Un Discovery MUST NOT usar "por Yizi" hacia afuera sin esa aprobación. Cada ficha SHALL tener una "Nota de marca" en su sección 1: nombre de trabajo usado hacia afuera, si usa "por Yizi" y quién lo aprobó.

#### Scenario: Perfil público sin aprobación
- **WHEN** un Discovery quiere abrir un perfil en redes o comprar un dominio sin aprobación de Jarvis
- **THEN** el trabajo no se hace y Herbie anota la pregunta para Jarvis en la ficha

### Requirement: Tope total de Discovery
El registro de satélites SHALL fijar un tope total para todos los Discovery abiertos. El tope total MUST tener horas del CEO por semana, horas del CEO por trimestre calendario y caja por trimestre calendario. Edith MUST proponer las cifras y el CEO MUST decidirlas. La suma de los topes de los proyectos en `discovery` MUST NOT superar el tope total. Mientras el CEO no fije el tope total, un Discovery nuevo MUST NOT abrirse.

#### Scenario: Discovery nuevo que no cabe en el tope total
- **WHEN** con un tope total de 6 h por semana, los Discovery abiertos suman 5 h y llega uno de 2 h
- **THEN** el proyecto sigue en `propuesto` y Viernes presenta al CEO tres opciones: esperar, reducir un tope o pedir a Edith que revise el tope total

#### Scenario: Transición sin tope total
- **WHEN** el CEO no ha fijado el tope total y retoma toFinance o el plan de comidas y mercado
- **THEN** toFinance sigue en `pausado` y el plan de mercado sigue en `propuesto`
- **AND** pasan a `discovery` solo cuando el CEO fije el tope total

### Requirement: Cómo se mide el tope total
La caja del trimestre SHALL sumar lo gastado más lo comprometido, es decir, la caja aún no gastada de los topes abiertos. En semanas con piloto de Yizi Solutions, el tope semanal SHALL bajar a la mitad. Antes de fijar las cifras, el CEO MUST confirmar su caja propia por trimestre y Ultron MUST confirmar las horas por semana. Sin esas confirmaciones, las cifras SHALL figurar como estimación.

#### Scenario: Semana con piloto de Yizi Solutions
- **WHEN** hay un piloto de Yizi Solutions en una semana y el tope total es de 6 h por semana
- **THEN** los Discovery abiertos suman como máximo 3 h del CEO esa semana

#### Scenario: Caja comprometida
- **WHEN** en un trimestre un Discovery cerrado gastó S/ 60 y otro abierto tiene S/ 80 de tope sin gastar
- **THEN** Edith cuenta S/ 140 de la caja del trimestre

### Requirement: Registro del consumo de Discovery
El consumo de cada Discovery SHALL registrarse en un solo lugar: la tabla "Consumo" de la sección 4 de su `ficha.md` en Yizi Projects. La tabla tiene semana, horas del CEO, caja y quién la anotó. Herbie MUST mantenerla y MUST actualizar las secciones 1 (estado) y 4 (topes) de la ficha. El CEO MUST reportar sus propias horas: U.L.T.R.O.N SHALL preguntarle cada viernes. Edith MUST registrar la caja.

#### Scenario: Reporte del viernes
- **WHEN** llega el viernes y hay un Discovery abierto
- **THEN** Ultron pregunta al CEO cuántas horas dio a cada Discovery y Herbie anota la respuesta en la tabla "Consumo"

#### Scenario: El CEO no reporta sus horas
- **WHEN** llega el viernes y el CEO no responde
- **THEN** Herbie anota "sin reporte" en la tabla "Consumo" y Ultron no supone ninguna cifra

### Requirement: Vigilancia del consumo de Discovery
U.L.T.R.O.N SHALL leer la tabla "Consumo" y avisar al CEO al 80 % de dos umbrales. Uno compara las horas acumuladas de un Discovery con sus horas totales. El otro compara la suma de horas de la semana con el tope total semanal. Al 100 %, Ultron MUST detener las sesiones de agentes de ese Discovery y avisar al CEO. Ultron no puede detener las horas del CEO. Las horas de Discovery MUST NOT desplazar el trabajo comprometido con clientes de un satélite `activo`.

#### Scenario: Aviso al 80 %
- **WHEN** un Discovery de 24 h totales acumula 19,2 h, o los Discovery suman 4,8 h en una semana de tope 6 h
- **THEN** Ultron avisa al CEO con las horas de cada Discovery, en la misma unidad que el tope, antes de seguir

#### Scenario: Choque con un cliente
- **WHEN** una semana no alcanzan las horas del CEO para un Discovery y para la entrega a un cliente de Yizi Solutions
- **THEN** Ultron da prioridad al cliente y mueve las horas del Discovery a la semana siguiente

### Requirement: Sesiones de agentes de un Discovery
U.L.T.R.O.N SHALL poner al final de la cola las sesiones de agentes de un Discovery cuando la ventana de 5 horas esté justa. Esas sesiones MUST NOT usar subagentes en paralelo.

#### Scenario: Ventana de 5 horas justa
- **WHEN** el uso del plan de IA está cerca del límite de la ventana de 5 horas
- **THEN** Ultron pone las sesiones de Discovery al final de la cola y no lanza subagentes en paralelo

### Requirement: Fin de un Discovery
Un Discovery termina al llegar a su fecha de fin, agotar su tope o cumplir su criterio de cierre. Entonces Viernes SHALL proponer al CEO uno de cuatro caminos. Los caminos son: pasar a `incubacion`, extender con un tope nuevo, pausar o cerrar. Edith MUST dar su recomendación financiera y Jarvis la de marca. Pasar a `incubacion` MUST exigir expediente MACRO completo, veredicto AUTORIZADO y cupo libre. Herbie MUST anotar en la ficha el camino elegido, con fecha.

#### Scenario: Discovery con tope agotado
- **WHEN** un Discovery acumula sus 24 h totales aprobadas antes de su fecha de fin
- **THEN** Ultron detiene sus sesiones de agentes y Viernes presenta al CEO los cuatro caminos con las recomendaciones de Edith y Jarvis

#### Scenario: Discovery exitoso sin expediente
- **WHEN** un Discovery confirma su hipótesis pero el proyecto no tiene expediente MACRO completo
- **THEN** Viernes devuelve el paso a `incubacion` hasta completar el expediente

### Requirement: Extensión y aviso al cerrar un Discovery
Un Discovery MAY extenderse una sola vez. La extensión SHALL contar como gasto nuevo en el tope total. Una segunda extensión MUST volver a la Autoridad MACRO. Si el Discovery se pausa o se cierra, Jarvis MUST redactar el aviso a quienes participaron. Una persona MUST confirmar el aviso antes de enviarlo.

#### Scenario: Segunda extensión
- **WHEN** un Discovery ya extendido una vez pide otra extensión
- **THEN** Viernes lo lleva a la Autoridad MACRO y no al CEO directamente

#### Scenario: Cierre con personas que participaron
- **WHEN** el CEO cierra un Discovery que entrevistó a personas externas
- **THEN** Herbie anota el cierre en la ficha
- **AND** Jarvis redacta el aviso a esas personas y una persona lo confirma antes de enviarlo
