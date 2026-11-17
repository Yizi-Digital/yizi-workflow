# Design

## Context

El cambio `big-bang-nucleo` dejó cuatro decisiones pendientes para el CEO. El CEO respondió el 2026-11-17:
1. Los satélites llevan nombre en inglés y cada uno es un repositorio separado dentro de la organización `YiziDigital`.
2. Yizi Solutions es el primer satélite y el primer repositorio externo que se crea.
3. Las siglas de los agentes no tienen un significado: son nombres propios.
4. El límite de gasto depende de observar el consumo mensual y el límite de uso de 5 horas del plan de IA.

## Goals / Non-Goals

**Goals:**
- Reflejar las decisiones en specs, registro, fichas, skill y documentación.
- Dejar el repositorio `yizi-solutions` generado y listo para subirse a `YiziDigital/yizi-solutions`.

**Non-Goals:**
- Empezar el trabajo de negocio de Yizi Solutions.
- Crear los repositorios de Growth y Talent.

## Decisions

### D1 · Nombres e ids en inglés — [Viernes, Jarvis]

| Antes | Ahora | Repositorio |
|---|---|---|
| Yizi Soluciones (`yizi-soluciones`) | **Yizi Solutions** | `YiziDigital/yizi-solutions` |
| Yizi Impulso (`yizi-impulso`) | **Yizi Growth** | `YiziDigital/yizi-growth` |
| Yizi Talento (`yizi-talento`) | **Yizi Talent** | `YiziDigital/yizi-talent` |

"Impulso" se traduce como *Growth* porque es el término habitual para una agencia de marketing y ventas digitales. *Alternativa considerada:* "Boost", más literal pero menos reconocible en el mercado. El CEO puede cambiarlo con un cambio S.

El contenido de los repositorios (specs, documentos) sigue en español; solo el nombre comercial y el id van en inglés.

### D2 · Líderes de satélite aprobados — [Viernes]
El CEO aprobó la propuesta de nombres del punto 1 ("están excelentes y está bien"). K.A.R.E.N (Solutions), H.O.M.E.R (Growth) y J.O.C.A.S.T.A (Talent) pasan de `propuesto` a `aprobado` en el registro.

### D3 · Creación del repositorio remoto — [Ultron]
Crear un repositorio en la organización es una acción hacia afuera (spec `satelites`). El contenido se genera en local (`../yizi-solutions`, junto al núcleo) con su primer commit. El CEO crea el repositorio vacío `YiziDigital/yizi-solutions` en GitHub (o confirma su creación) y después se sube.

### D4 · Registro de consumo de IA — [Edith]
Nuevo archivo `finanzas/consumo-ia.md` en el núcleo, con una fila por mes: plan, ventanas de 5 horas agotadas, uso semanal, gastos extra y observaciones. Tras dos meses, Edith puede proponer un límite. El uso del plan se consulta en la configuración de la cuenta de Claude o, dentro de Claude Code, con el comando de uso del plan (`/usage`).

### D5 · Nombres de agentes sin significado — [CEO]
Se eliminan de las fichas las líneas con el "significado Yizi" de cada sigla. Los nombres son propios, se escriben con puntos y se invocan por su forma corta.

## Risks / Trade-offs

- **Repositorio remoto pendiente:** hasta que exista `YiziDigital/yizi-solutions`, el satélite solo existe en local; si el contenedor de trabajo se recicla antes de subirlo, se regenera con el skill `yizi-satelite`.
- **Sin cifra de gasto durante dos meses:** se compensa con la regla de la ventana de 5 horas y el aviso de gastos extra.
