# Spec Delta

## Purpose

Define cómo Yizi decide qué agentes de IA necesita cada línea de negocio, con qué criterio, experiencia y referencias, y cómo se mantiene actualizado ese conocimiento. Dueña: A.I.D.A (Aida), agente de área del núcleo. Reporta a: U.L.T.R.O.N (Ultron).

## ADDED Requirements

### Requirement: Mapa de agentes por satélite
Aida SHALL mantener un mapa de agentes por satélite que diga, para cada agente existente o propuesto: rol, nivel, dominio, criterio de decisión, experiencia que representa, referencias en las que se basa y estado (propuesto, aprobado, activo, retirado).

#### Scenario: Consulta del CEO
- **WHEN** el CEO pregunta qué agentes tiene o necesita Yizi Solutions
- **THEN** Aida responde a partir del mapa, con el estado de cada agente

### Requirement: Diseño de un agente nuevo
Todo agente nuevo SHALL diseñarse con una ficha que siga la spec `jerarquia-agentes` e incluya su criterio, su experiencia de referencia y sus fuentes. Ningún agente MUST crearse ni activarse sin un cambio OpenSpec aprobado por el CEO.

#### Scenario: Un satélite pide un especialista
- **WHEN** Karen pide un agente especialista para Yizi Solutions
- **THEN** Aida diseña la ficha, la propone como cambio OpenSpec y espera la aprobación del CEO

### Requirement: Referencias verificables
Las referencias de un agente (marcos de trabajo, normas, buenas prácticas, autores) SHALL citarse con su fuente y fecha de consulta. Una referencia que no se pueda verificar MUST marcarse como "no verificado".

#### Scenario: Agente de finanzas de un satélite
- **WHEN** Aida diseña un agente que aplica normas tributarias
- **THEN** su ficha cita la norma oficial con fuente y fecha

### Requirement: Actualización del conocimiento
Aida SHALL revisar las fichas y el mapa de agentes al menos cada trimestre, y también cuando un satélite cambie de estado o cuando un agente falle dos veces en lo mismo. Cada revisión MUST proponer las mejoras como cambio OpenSpec.

#### Scenario: Un agente se equivoca dos veces
- **WHEN** un agente comete el mismo error dos veces
- **THEN** Aida propone un cambio en su ficha que añade la regla o el criterio que faltaba
