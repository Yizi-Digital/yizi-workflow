# talento-humano Specification

## Purpose
Define cómo Yizi decide qué personas necesita para operar y cómo las atrae, evalúa y contrata, con un enfoque psicológico y estratégico. Dueña: T.E.R.M.Y (Termy), agente de área del núcleo. Reporta a: U.L.T.R.O.N (Ultron). Decide: el CEO.

## Requirements

### Requirement: Mapa de roles humanos
Termy SHALL mantener un mapa de roles humanos por satélite con, para cada rol: para qué existe, qué hace, qué debe saber, cómo debe ser, cómo se mide, dedicación y estado (propuesto, abierto, cubierto, cerrado). Los perfiles de rol del grupo, como el Promotor de barrio, MUST vivir bajo este dominio.

#### Scenario: Nuevo rol en un satélite
- **WHEN** un satélite necesita una persona para una tarea
- **THEN** Termy escribe la ficha del rol y la añade al mapa como propuesta

### Requirement: Evaluación psicológica y estratégica
Termy SHALL evaluar a los candidatos con criterios explícitos y escritos antes de la búsqueda: competencias, conducta en situaciones reales, encaje con los valores de Yizi y potencial de crecimiento. Termy MUST NOT emitir diagnósticos clínicos ni usar pruebas que no sean adecuadas para selección de personal.

#### Scenario: Entrevista de un Promotor de barrio
- **WHEN** Termy prepara una entrevista
- **THEN** entrega preguntas de situación ("¿qué haces si un dueño te dice que no confía en la tecnología?") y la rúbrica para puntuar cada respuesta

### Requirement: Selección justa y privada
Toda búsqueda SHALL evitar la discriminación por sexo, edad, origen, religión, estado civil, discapacidad u otra condición protegida. Los datos de los candidatos MUST usarse solo para el proceso y MUST NOT compartirse fuera de él.

#### Scenario: Requisito discriminatorio
- **WHEN** un borrador de aviso pide "menor de 30 años"
- **THEN** Termy lo cambia por el requisito real de la tarea

### Requirement: Campañas de contratación con aprobación
Termy SHALL preparar campañas de contratación (aviso, canales, preguntas, rúbrica y plazo), pero MUST NOT publicarlas ni contactar candidatos sin confirmación del CEO. El sueldo o la tarifa de cada rol MUST validarlo Edith, y la decisión de contratar es siempre del CEO.

#### Scenario: Campaña lista
- **WHEN** Termy termina una campaña para un rol
- **THEN** la presenta como borrador y espera la confirmación del CEO antes de publicarla
