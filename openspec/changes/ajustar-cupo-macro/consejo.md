# Consejo · ajustar-cupo-macro

| Campo | Valor |
|---|---|
| Dueño | V.I.E.R.N.E.S (Viernes) |
| Alcance | nucleo |
| Tipo / Tamaño | estrategico / L |
| Fecha de revisión | 2026-11-22 |
| Revisión | Consejo completo, en paralelo (skill `yizi-consejo`) |

## Veredictos

Ninguna compuerta está BLOQUEADA. Las cinco están CONDICIONADAS: el cambio vuelve a la fase 1 para incorporar las condiciones antes de pedir la aprobación del CEO.

| Agente | Compuerta | Veredicto | Condiciones principales |
|---|---|---|---|
| Vision | Viabilidad técnica | CONDICIONADO | toFinance sigue `pausado` hasta reanudar; "en espera" se asigna a un estado; topes en horas por semana y horas totales, con la misma unidad en los escenarios; MUST NOT en vez de MAY; definir "código de producto"; un solo lugar para registrar el consumo |
| Jarvis | Marca y cliente | CONDICIONADO | Jarvis revisa todo texto o prototipo que vea una persona externa; ningún Discovery usa marca pública ni "por Yizi" sin su aprobación; un proyecto en `propuesto` o `discovery` no se ofrece a clientes; explicar "Discovery", "cupo" y "tope"; partir frases largas |
| Edith | Costo y presupuesto | CONDICIONADO | Tope total de caja por trimestre con lo gastado más lo comprometido; una sola extensión por Discovery; Edith revisa cada tope; el tope semanal baja a la mitad con piloto de Solutions; corregir el costo del cambio. Propuesta (estimación): 6 h por semana (3 h con piloto) y S/ 180 por trimestre, aviso al 80 % |
| Viernes | Alineación estratégica | CONDICIONADO | Reflejar la pausa del CEO del 2026-11-22; llevar al CEO solo las decisiones 1 y 2; las decisiones de cada proyecto van a su ficha; anotar el fin de un Discovery en la ficha; definir "en espera" frente a `pausado`; alinear el id `plan-mercado` con la carpeta |
| Ultron | Operabilidad | CONDICIONADO | Definir cómo se miden las horas del CEO (él las reporta cada viernes; la caja la anota Edith); tabla "Consumo" en la sección 4 de cada ficha, no en el README; reordenar `tasks.md` (cifras de Edith antes de la decisión del CEO); el cambio en `yizi-projects` va aparte; escenario de transición sin tope total |

### Coincidencias entre compuertas

- **toFinance sigue `pausado`** hasta que el CEO lo retome (Vision, Viernes, Ultron).
- **Un solo lugar para topes y consumo:** la sección 4 de `ficha.md` de cada proyecto (Vision, Viernes, Ultron).
- **Las decisiones de cada proyecto viven en su ficha**, no en `ceo/pendientes.md` (Vision, Viernes), según la spec `ficha-proyecto-macro` de Yizi Projects.
- **Unidades claras:** horas por semana y horas totales, comparadas en la misma unidad (Vision, Ultron, Edith).

### Matiz para el CEO

- Edith quiere fijar ya el tope total y pregunta con qué caja trimestral se cuenta. Viernes propone dejar esa cifra para cuando se retome un Discovery, porque la spec ya impide abrir uno sin tope total. No es un bloqueo: decide el CEO.

## Detalle

Vision: CONDICIONADO. La regla es simple y la apruebo en su idea: un proyecto en curso y varios Discovery con tope. Hay tres fallos. Primero, toFinance no tiene horas en curso y el CEO lo dejó en espera: hoy es `pausado`, no `discovery`. Segundo, el tope total mezcla horas por semana con horas acumuladas. Tercero, la tarea 5.1 choca con `ficha-proyecto-macro`. Pido corregir esos estados, unidades y tareas, y definir "código de producto" antes de implementar.

Jarvis: Condicionado. Nada de esto sale hacia afuera hoy, pero cada Discovery sí hablará con gente real, y varios a la vez pueden confundir qué es Yizi. Pido tres cosas: que yo revise todo texto o prototipo que vea una persona externa, antes de usarse; que ningún Discovery use marca pública ni "por Yizi" sin mi aprobación; y que expliquen "Discovery", "cupo" y "tope" en palabras simples. Con eso, apruebo.

Edith: CONDICIONADO. El cambio no cuesta caja, pero la salvaguarda tiene un hueco. Un Discovery cierra, otro abre, y el gasto no tiene fin. Propongo un tope total de 6 h por semana (3 h con piloto) y S/ 180 por trimestre, contando lo gastado. Es una estimación. Pido que la cifra se mida por trimestre, que cada Discovery tenga una sola extensión y que yo revise cada tope. CEO, ¿con qué caja trimestral contamos?

Viernes: CONDICIONADO. Mantengo la regla: un MACRO en curso y varios Discovery con tope. Pero el CEO pausó los dos proyectos el 2026-11-22, y la ficha ya guarda sus preguntas. Pido cinco cosas: toFinance sigue `pausado` hasta reanudar. Al CEO solo las decisiones 1 y 2; la fecha y el tope van a cada ficha. "Fin de un Discovery" se anota en la ficha. Tope y consumo, en su sección 4. Y "en espera" se define frente a `pausado`.

Ultron: Condicionado. Hoy no puedo medir las horas del CEO: nadie las registra, y por eso el aviso al 80 % no es verificable. Pido una tabla "Consumo" en cada ficha, con horas que el CEO me reporta cada viernes y caja que anota Edith. Pido también reordenar las tareas: primero las cifras de Edith, luego el CEO decide. El cambio de yizi-projects va aparte. Con eso, apruebo.

## Decisión del CEO

- Decisión: PENDIENTE
- Fecha:
- Anulaciones de compuertas BLOQUEADAS (con motivo): ninguna (no hay compuertas bloqueadas)
