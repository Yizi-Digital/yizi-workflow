# autoridad-macro Specification

## Purpose
Define la Autoridad MACRO: el órgano del núcleo que evalúa y autoriza los proyectos propios de Yizi de gran alcance (aplicaciones y soluciones para un público amplio), protegiendo la caja y la visión de la marca. Preside: V.I.E.R.N.E.S (Viernes). Decide: el CEO.

## Requirements

### Requirement: Composición de la Autoridad MACRO
La Autoridad MACRO SHALL estar presidida por V.I.E.R.N.E.S y SHALL incluir como evaluadores a E.D.I.T.H (viabilidad financiera), V.I.S.I.O.N (viabilidad técnica), J.A.R.V.I.S (mercado y marca) y U.L.T.R.O.N (capacidad operativa). La decisión final MUST tomarla el CEO.

#### Scenario: Evaluación completa
- **WHEN** se presenta un expediente MACRO
- **THEN** los cuatro evaluadores emiten su veredicto, Viernes consolida una recomendación y el CEO decide

### Requirement: Qué es un proyecto MACRO
Un proyecto SHALL considerarse MACRO cuando sea un producto o aplicación propia de Yizi dirigida a un público amplio, cuando cree una marca nueva, cuando requiera una inversión superior al límite fijado por el CEO o cuando cambie el posicionamiento público de Yizi. Un proyecto para un solo cliente MUST NOT tramitarse como MACRO.

#### Scenario: App para todos los restaurantes de una ciudad
- **WHEN** se propone una aplicación propia de pedidos para todos los restaurantes de una ciudad
- **THEN** se tramita como proyecto MACRO

#### Scenario: Sistema para un solo restaurante
- **WHEN** un restaurante contrata un sistema a medida
- **THEN** se gestiona en el satélite de soluciones y no como MACRO

### Requirement: Expediente MACRO
Toda propuesta MACRO SHALL incluir: problema y público objetivo, encaje con la misión, modelo de ingresos, costo estimado y tiempo de retorno, riesgo de dilución de la marca, capacidad que requiere, criterio de éxito y criterio de cierre. Un expediente incompleto MUST devolverse sin evaluar.

#### Scenario: Expediente sin criterio de cierre
- **WHEN** una propuesta MACRO no define cuándo se abandonaría el proyecto
- **THEN** Viernes la devuelve para completarla antes de convocar a los evaluadores

### Requirement: Veredictos de la Autoridad MACRO
La decisión sobre un proyecto MACRO SHALL ser una de tres: AUTORIZADO, que lo registra como satélite `macro` en estado `incubacion`; EN ESPERA, que lo guarda en la cartera para revisarlo después; o RECHAZADO, con sus motivos. La decisión MUST registrarse en el registro del Consejo del cambio.

#### Scenario: Proyecto autorizado
- **WHEN** el CEO autoriza un proyecto MACRO
- **THEN** se añade al registro de satélites como tipo `macro` en `incubacion`, con Viernes como patrocinador

### Requirement: Límite de proyectos MACRO simultáneos
El número de proyectos MACRO en incubación o activos SHALL estar limitado por el valor fijado en el registro de satélites, que Edith propone según la caja disponible. Mientras la caja sea limitada, el valor inicial SHALL ser un proyecto MACRO a la vez.

#### Scenario: Segundo proyecto con el límite alcanzado
- **WHEN** ya hay un proyecto MACRO en incubación y se autoriza otro
- **THEN** el nuevo queda EN ESPERA hasta que se libere el cupo o el CEO cambie el límite

### Requirement: Revisión periódica y criterio de cierre
Todo satélite `macro` SHALL revisarse en los puntos de control definidos en su expediente. Si se cumple su criterio de cierre, Viernes MUST proponer pausarlo o cerrarlo.

#### Scenario: Criterio de cierre alcanzado
- **WHEN** un proyecto MACRO no alcanza la métrica mínima en el plazo acordado
- **THEN** Viernes propone al CEO pausarlo o cerrarlo, con la recomendación financiera de Edith
