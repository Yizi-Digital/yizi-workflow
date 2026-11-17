# Spec Delta

## MODIFIED Requirements

### Requirement: Veredictos de la Autoridad MACRO
La decisión sobre un proyecto MACRO SHALL ser una de tres: AUTORIZADO, que lo registra como proyecto de Yizi Projects en estado `incubacion`; EN ESPERA, que lo guarda en la cartera para revisarlo después; o RECHAZADO, con sus motivos. La decisión MUST registrarse en el registro del Consejo del cambio.

#### Scenario: Proyecto autorizado
- **WHEN** el CEO autoriza un proyecto MACRO
- **THEN** se añade a la lista de proyectos de Yizi Projects en el registro de satélites, en `incubacion`, con Viernes como patrocinadora

### Requirement: Revisión periódica y criterio de cierre
Todo proyecto MACRO de Yizi Projects SHALL revisarse en los puntos de control definidos en su expediente. Si se cumple su criterio de cierre, Viernes MUST proponer pausarlo o cerrarlo.

#### Scenario: Criterio de cierre alcanzado
- **WHEN** un proyecto MACRO no alcanza la métrica mínima en el plazo acordado
- **THEN** Viernes propone al CEO pausarlo o cerrarlo, con la recomendación financiera de Edith
