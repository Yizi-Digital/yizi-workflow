# Tasks

Nada de esto se implementa hasta que el CEO apruebe el cambio. Antes de implementar, el CEO envía `/clear`.

**Orden de trabajo:** 1.1 → sección 2 → 1.2 → secciones 3 a 8. Las cifras de Edith van antes de la decisión del CEO.

## 1. Consejo y decisión del CEO [Viernes]

- [ ] 1.1 Volver a pasar el cambio por el Consejo con `/yizi-consejo`; cada agente confirma en `consejo.md` que se cumplen sus condiciones
- [x] 1.2 Tras la sección 2, presentar al CEO solo las decisiones 1 (la regla) y 2 ("activo" incluye `incubacion`). Registrar sus respuestas en `consejo.md` (el CEO aprobó las dos el 2026-11-22, antes de 1.1 y de la sección 2; esas tareas siguen pendientes)

## 2. Antes de la decisión del CEO [Edith, Ultron, Jarvis]

- [ ] 2.1 [Edith] Dejar en `consejo.md` la propuesta de tope total: 6 h por semana, 3 h con piloto, S/ 180 por trimestre, aviso al 80 %. Marcarla "estimación, no verificada"
- [ ] 2.2 [Edith] Proponer las horas del CEO por trimestre del tope total, o dejarlas como "pendiente"
- [ ] 2.3 [Ultron] Confirmar con el CEO si puede dar 6 h por semana a los Discovery; sin su confirmación, la cifra sigue como estimación
- [ ] 2.4 [Jarvis] Revisar los textos de `proposal.md`, la spec y `tasks.md`: resumen inicial, glosario, decisión 2 y frases de 25 palabras o menos

## 3. Registro de satélites [Viernes] (tras decisión del CEO)

- [ ] 3.1 En `satelites/registro.yaml`, añadir al comentario de `yizi-projects` los seis estados de proyecto y cuáles ocupan el cupo. Aclarar que `activo` de un proyecto no es `activo` de un satélite
- [ ] 3.2 Dejar toFinance en `pausado`; cambiar su `etapa` "discovery indefinido" por "pausado por el CEO el 2026-11-22; tope guardado en su ficha"
- [ ] 3.3 Al reanudar toFinance: pasarlo a `discovery` solo con tope total fijado y la fecha de fin que fije el CEO (requisito "Pausa real")
- [ ] 3.4 Cambiar el id `plan-mercado` por `idea-mercado-barrio`, igual que su carpeta; dejarlo en `propuesto` y quitar "discovery" de su `etapa`
- [ ] 3.5 Al reanudar el plan de mercado: pasarlo a `discovery` solo con tope aprobado por el CEO, revisado por Edith, y tope total fijado
- [ ] 3.6 Al retomar el primer Discovery: llevar al CEO la decisión del tope total; antes, el CEO confirma su caja por trimestre y Ultron las horas por semana
- [ ] 3.7 Con esa decisión, añadir a `limites` las claves del tope total: horas por semana, horas por trimestre y caja por trimestre

## 4. Skill y fichas de agentes [cada dueño]

- [ ] 4.1 [Ultron] En `.agents/skills/yizi-consejo/SKILL.md` (modo MACRO, paso 2), añadir tres revisiones: tope propio con supuestos de Edith, tope total y nota de marca
- [ ] 4.2 [Viernes] En `.claude/agents/viernes.md`, ajustar el punto 4 de "Qué haces": 1 MACRO en curso, varios Discovery dentro del tope total
- [ ] 4.3 [Edith] En `.claude/agents/edith.md`, ajustar el punto 7: propone el tope total por trimestre y revisa el tope de cada Discovery
- [ ] 4.4 [Ultron] En `.claude/agents/ultron.md`, definir el recordatorio de cada viernes al CEO; su respuesta la anota Herbie en la tabla "Consumo" de la ficha
- [ ] 4.5 [Jarvis] En `.claude/agents/jarvis.md`, añadir dos tareas: revisar textos externos de cada Discovery y aprobar la "Nota de marca" de cada ficha

## 5. Pendientes del CEO [Ultron]

- [ ] 5.1 En `ceo/pendientes.md`, reemplazar la línea del cupo MACRO por las decisiones 1 y 2, y anotar "tope total: al retomar el primer Discovery"; la fecha de fin de toFinance no entra

## 6. Cambio hermano en yizi-projects [Herbie]

Es un cambio aparte, en el repo `yizi-projects`, con su propia revisión y aprobación del CEO. Nombre propuesto: `tope-y-consumo-discovery`. El archivo de este cambio (8.1) espera a que ese cambio se archive, porque esta spec apunta a la tabla "Consumo".

- [ ] 6.1 Abrir el cambio hermano y corregir `proyectos/README.md`: la línea "Hoy no hay proyectos autorizados" y la tabla, con los estados del registro
- [ ] 6.2 Corregir la sección 1 de las dos fichas con el estado del registro: `pausado` (toFinance) y `propuesto` (plan de mercado), sin "en espera" como estado
- [ ] 6.3 Añadir con Jarvis la "Nota de marca" a la sección 1 de cada ficha. Incluye nombre de trabajo hacia afuera, uso de "por Yizi" y quién lo aprobó
- [ ] 6.4 Crear la tabla "Consumo" (semana, horas, caja, quién la anotó) en la sección 4 de las dos fichas. Dejar ahí el tope guardado de cada una
- [ ] 6.5 Registrar en la sección 8 de cada ficha las decisiones pendientes: fecha de fin de toFinance y tope del plan de mercado
- [ ] 6.6 Enmendar la spec `ficha-proyecto-macro`: tabla "Consumo" en la sección 4, Herbie actualiza las secciones 1 y 4, y anota el fin de cada Discovery
- [ ] 6.7 Pasar el cambio hermano por su revisión y archivarlo tras la aprobación del CEO

## 7. Verificación [Lince]

- [ ] 7.1 Ejecutar `openspec validate ajustar-cupo-macro --strict` sin errores ni advertencias
- [ ] 7.2 Comprobar el registro: ningún `pausado` con trabajo en curso y ningún "en espera" como estado. Los ids son iguales a las carpetas. Cada `discovery` tiene tope y fecha de fin en su ficha
- [ ] 7.3 Comprobar que la suma de topes de los proyectos en `discovery` cabe en el tope total, si hay alguno
- [ ] 7.4 Comprobar que el skill, las fichas y los pendientes usan los mismos estados y el término "tope total de Discovery"

## 8. Archivo [Ultron]

- [ ] 8.1 Archivar con `/openspec-archive-change` cuando Lince apruebe y el cambio hermano (6.7) esté archivado; el archivo aplica el delta a la spec vigente `autoridad-macro`
