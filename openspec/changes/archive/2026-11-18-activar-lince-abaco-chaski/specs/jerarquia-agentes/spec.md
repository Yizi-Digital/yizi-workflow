# Spec Delta

## MODIFIED Requirements

### Requirement: Agentes de área del núcleo
Un agente de área del núcleo SHALL ser un agente N1 que atiende a todo el grupo en un dominio especializado, sin formar parte del Consejo Ejecutivo y sin custodiar una compuerta. Cada agente de área MUST reportar a un miembro del Consejo. Los agentes de área son A.I.D.A (diseño de agentes), T.E.R.M.Y (talento humano) y L.I.N.C.E (verificación independiente), y los tres reportan a U.L.T.R.O.N.

#### Scenario: Revisión de un cambio grande
- **WHEN** un cambio de tamaño L pasa por el Consejo
- **THEN** revisan solo los cinco miembros del Consejo, y Aida, Termy o Lince opinan solo si el cambio toca su dominio

#### Scenario: Verificación antes de archivar
- **WHEN** un cambio terminó su implementación
- **THEN** Lince lo verifica y nunca lo verifica el mismo agente que lo construyó

## ADDED Requirements

### Requirement: Agentes del producto
Un agente del producto SHALL ser un agente que trabaja con clientes dentro de la plataforma de un satélite, no como subagente de Claude Code. Su ficha MUST vivir en el repositorio del satélite, en `producto/agentes/`, con su nombre interno, su nivel de modelo, su respaldo humano y sus límites. Ante clientes MUST presentarse siempre como El Guía Yizi.

#### Scenario: Chaski conversa con un bodeguero
- **WHEN** un bodeguero pide ayuda en la plataforma
- **THEN** lo atiende Chaski presentándose como El Guía Yizi, nunca con su nombre interno
