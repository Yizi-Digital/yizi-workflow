# Spec Delta

## MODIFIED Requirements

### Requirement: Niveles de la jerarquía
El universo Yizi SHALL organizar a humanos y agentes en cinco niveles: N0 es el CEO humano; N1 son los agentes del núcleo, que heredan todos los satélites: el Consejo Ejecutivo y los agentes de área; N2 es el líder de un satélite; N3 es un especialista de un satélite; N4 es un ejecutor efímero, sin identidad persistente, que existe solo durante una tarea.

#### Scenario: Se define un agente nuevo
- **WHEN** se crea un agente persistente
- **THEN** su ficha declara a qué nivel pertenece (N1, N2 o N3)

## ADDED Requirements

### Requirement: Agentes de área del núcleo
Un agente de área del núcleo SHALL ser un agente N1 que atiende a todo el grupo en un dominio especializado, sin formar parte del Consejo Ejecutivo y sin custodiar una compuerta. Cada agente de área MUST reportar a un miembro del Consejo. Los agentes de área iniciales son A.I.D.A (diseño de agentes) y T.E.R.M.Y (talento humano), y ambos reportan a U.L.T.R.O.N.

#### Scenario: Revisión de un cambio grande
- **WHEN** un cambio de tamaño L pasa por el Consejo
- **THEN** revisan solo los cinco miembros del Consejo, y Aida o Termy opinan solo si el cambio toca su dominio
