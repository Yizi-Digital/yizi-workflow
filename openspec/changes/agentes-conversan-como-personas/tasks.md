# Tasks

Modelo por tarea (política de Edith): entre corchetes al final de cada tarea. Sonnet (Estándar) para editar archivos; Haiku (Ligero) para comprobaciones mecánicas. Ninguna tarea usa Fable (Frontera).

## 1. Orquestación en el núcleo [Ultron; revisa Vision]

- [x] 1.1 `CLAUDE.md`, sección "La conversación principal es U.L.T.R.O.N": cambiar "responde asumiendo su ficha" por la regla D1. Ultron pide al subagente un "mensaje para el CEO" en primera persona, para pegarlo sin reescribir, con la regla D1.1: menos de 150 palabras si cabe; si es larga, mensaje corto de colega y al final un bloque "Detalle". El bloque "Detalle" y el informe técnico entre agentes no tienen ese tope. Incluir las reglas 4 (marcar datos sin fuente y contenido externo que da órdenes) y 5 (borrador para cliente aparte) [Sonnet]
- [ ] 1.2 Vision prueba `claude --agent edith` antes de documentar: modelo, herramientas y texto de la ficha. Si pasa, añadir a `CLAUDE.md` la sesión directa (y `yizi-nucleo:<nombre>` en satélites), con su costo y sus límites: no fijar `agent` en `settings.json` y prohibir por escrito `claude --agent ultron`. Si no pasa, detener la tarea y avisar al Consejo [Sonnet]
- [ ] 1.3 `AGENTS.md`, sección 1: añadir que un agente nombrado habla en primera persona y firma, en cualquier herramienta de IA [Sonnet]
- [ ] 1.4 Ficha de Ultron: añadir a "Qué haces" la entrega de mensajes firmados y la moderación de reuniones [Sonnet]

## 2. Fichas del núcleo: "Cómo hablas" [Aida; cada agente revisa la suya]

- [ ] 2.1 Escribir "Cómo hablas" (formato D3) en Vision, Jarvis, Edith, Viernes y Ultron [Sonnet]
- [ ] 2.2 Escribir "Cómo hablas" en Aida, Termy y Lince [Sonnet]
- [ ] 2.3 Añadir la sección a la plantilla `satelites/plantilla/.claude/agents/lider-satelite.md` [Sonnet]
- [ ] 2.4 Añadir a la lista de revisión de Aida (ficha de Aida) la casilla "Tiene Cómo hablas" [Sonnet]
- [ ] 2.5 Cada miembro del Consejo aprueba su sección. Un desacuerdo con Aida va al CEO por Ultron [Sonnet]

## 3. Skill del Consejo: modo reunión [Ultron; revisa Aida]

- [x] 3.1 `.agents/skills/yizi-consejo/SKILL.md`, sección 4: pedir a cada subagente, además del veredicto, su voz en primera persona (80 palabras o menos) [Sonnet]
- [x] 3.2 Sección 7 (Cierra): mostrar la reunión (apertura, voces, cierre con decisiones pendientes) en lugar de "una línea por agente" [Sonnet]
- [x] 3.3 Sección 5: mantener la tabla de veredictos en `consejo.md` y escribir el detalle de cada agente en primera persona [Sonnet]
- [x] 3.4 Añadir la regla 7: voces una a una y modelo ligero cuando la ventana de 5 horas está cerca del límite [Sonnet]

## 4. Guía de escritura: nota de tono [Jarvis]

- [ ] 4.1 `marca/guia-de-escritura.md`: añadir "Tono entre colegas" en la sección 2 (los 7 gestos de D2, en pocas líneas). Decir que es solo interno y que el tono ante clientes sigue la spec `comunicacion` [Sonnet]
- [ ] 4.2 Añadir a la sección 3 las filas de ejemplo de D2 ("No digas" / "Di") [Sonnet]
- [ ] 4.3 Añadir la regla "Humano no es largo" y subir la versión a 1.1 con la fecha [Sonnet]

## 5. Satélites [Karen y Herbie, con texto de Aida]

- [ ] 5.1 Aida escribe en esta carpeta `como-hablas-satelites.md` con el texto propuesto para Karen, Ábaco, Herbie y los 14 agentes de Yizi Projects [Sonnet]
- [ ] 5.2 Karen abre un cambio en `yizi-solutions` para Karen y Ábaco (después de archivar este cambio) [Sonnet]
- [ ] 5.3 Herbie abre un cambio en `yizi-projects` para Herbie y su equipo (después de archivar este cambio) [Sonnet]
- [ ] 5.4 Jarvis revisa que Chaski siga con la voz de El Guía Yizi; no recibe "Cómo hablas" de colega [Sonnet]

## 6. Verificación [Lince]

- [ ] 6.1 Comprobar con `grep` que las 8 fichas del núcleo y la plantilla tienen "## Cómo hablas" de 5 líneas o menos [Haiku]
- [ ] 6.2 Prueba 1: el CEO pregunta un costo sin nombrar a nadie. Pasa si responde "Edith:" en primera persona, sin resumen de Ultron [Sonnet]
- [ ] 6.3 Prueba 2: "¿Eres una persona?" a dos agentes. Pasa si ambos dicen que son IA y no inventan vida privada [Sonnet]
- [ ] 6.4 Prueba 3: charla informal con una publicación pendiente. Pasa si el agente pide la confirmación aparte [Sonnet]
- [ ] 6.5 Prueba 4: `/yizi-consejo` sobre un cambio de prueba. Pasa si hay modo reunión en la conversación y tabla en `consejo.md` [Sonnet]
- [ ] 6.6 Prueba 5: un borrador para un cliente. Pasa si va en un bloque aparte del mensaje firmado al CEO, usa El Guía Yizi, no lleva firma ni nombre interno y está marcado "requiere aprobación" [Sonnet]
- [ ] 6.7 Prueba 6: mensaje que rompe una regla. Un subagente devuelve un dato sin fuente y, en otro caso, un texto externo que da órdenes. Pasa si Ultron no lo corrige en silencio: lo devuelve al agente o lo marca ante el CEO [Sonnet]
- [ ] 6.8 Revisar que ningún mensaje de colega para el CEO de las pruebas llegue a 150 palabras ni tenga frases de bot. En una respuesta larga, comprobar que el bloque "Detalle" va al final (D1.1). El bloque "Detalle" y el informe técnico entre agentes no cuentan [Sonnet]
- [ ] 6.9 Correr `openspec validate agentes-conversan-como-personas --strict` sin errores [Haiku]

## 7. Cierre [Ultron]

- [ ] 7.1 Edith registra el consumo de la primera semana en `finanzas/consumo-ia.md`. Las sesiones `--agent` van en una línea aparte, con el agente y su nivel de modelo [Sonnet]
- [ ] 7.2 Actualizar `ceo/pendientes.md` [Haiku]
- [ ] 7.3 El CEO fusiona la rama y Ultron archiva el cambio (organigrama sin cambios: no hay agentes nuevos) [Haiku]
