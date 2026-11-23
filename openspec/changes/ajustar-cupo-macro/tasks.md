# Tasks

Nada de esto se implementa hasta que el CEO apruebe el cambio. Antes de implementar, el CEO envía `/clear`.

## 1. Consejo y decisión [Viernes]

- [ ] 1.1 Pasar el cambio por el Consejo completo con `/yizi-consejo` y consolidar los veredictos en `consejo.md`
- [ ] 1.2 Presentar al CEO las cinco decisiones de `proposal.md` y registrar sus respuestas en `consejo.md`

## 2. Cifras del tope total [Edith]

- [ ] 2.1 Proponer el tope total de Discovery (horas del CEO por semana y caja en soles), con fuente y fecha
- [ ] 2.2 Confirmar o corregir la suma de referencia (6 h por semana y S/ 180), marcada hoy como no verificada
- [ ] 2.3 Validar el umbral de aviso del 80 %

## 3. Registro de satélites [Viernes]

- [ ] 3.1 En `satelites/registro.yaml`, añadir a `limites` las claves del tope total de Discovery con las cifras que fije el CEO
- [ ] 3.2 Añadir al comentario de `yizi-projects` los estados de proyecto y cuáles ocupan el cupo (`incubacion` y `activo`)
- [ ] 3.3 Pasar toFinance de `pausado` a `discovery`, con su tope (24 h, S/ 100) y la fecha de fin que fije el CEO
- [ ] 3.4 Dejar el plan de comidas y mercado en `propuesto`, o pasarlo a `discovery` con su tope si el CEO lo aprueba
- [ ] 3.5 Añadir a cada proyecto en `discovery` los campos de tope: horas por semana, caja y fecha de fin

## 4. Skill y fichas [Ultron]

- [ ] 4.1 En `.agents/skills/yizi-consejo/SKILL.md` (modo MACRO, paso 2), revisar también el tope total de Discovery
- [ ] 4.2 En `.claude/agents/viernes.md`, ajustar el punto 4 de "Qué haces": 1 MACRO en curso, varios Discovery dentro del tope total
- [ ] 4.3 En `.claude/agents/edith.md`, ajustar el punto 7: también propone el tope total de Discovery

## 5. Pendientes del CEO [Ultron]

- [ ] 5.1 En `ceo/pendientes.md`, reemplazar la línea del cupo MACRO por la nueva decisión y añadir el tope total y la fecha de fin de toFinance

## 6. Satélite yizi-projects [Viernes]

- [ ] 6.1 Abrir un cambio en `yizi-projects` para actualizar `proyectos/README.md` (hoy dice "Hoy no hay proyectos autorizados")
- [ ] 6.2 En ese cambio, añadir al README de cada Discovery una sección "Tope y consumo" que Ultron actualiza cada semana

## 7. Verificación [Lince]

- [ ] 7.1 Ejecutar `openspec validate ajustar-cupo-macro --strict` sin errores ni advertencias
- [ ] 7.2 Comprobar que el registro cumple cada escenario: ningún proyecto `pausado` con trabajo en curso, cada `discovery` con tope y fecha de fin, y la suma de topes dentro del tope total
- [ ] 7.3 Comprobar que el skill, las fichas y los pendientes usan los mismos estados y el mismo término "tope total de Discovery"

## 8. Archivo [Ultron]

- [ ] 8.1 Archivar con `/openspec-archive-change` cuando Lince apruebe; el archivo aplica el delta a la spec vigente `autoridad-macro`
