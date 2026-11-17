# Registro de consumo de IA

Dueña: **E.D.I.T.H (Edith)** · Spec: `finanzas` (requisitos "Límite de gasto según consumo observado" y "Consumo por ventana de 5 horas").

No hay una cifra fija de gasto: el límite es el uso del plan de IA del CEO. Edith añade una fila al cerrar cada mes y, tras dos meses de datos, puede proponer un límite al CEO.

## Cómo medir

- **Uso del plan:** en la configuración de uso de la cuenta de Claude o, dentro de Claude Code, con `/usage`.
- **Ventanas de 5 horas agotadas:** cuántas veces en el mes se llegó al límite de uso de la ventana.
- **Gastos extra:** cualquier pago fuera del plan (uso adicional, API, herramientas nuevas).

## Registro mensual

| Mes | Plan | Ventanas de 5 h agotadas | Uso semanal más alto | Gastos extra (moneda) | Satélite o agente que más consumió | Observaciones |
|---|---|---|---|---|---|---|
| 2026-11 | Por completar | | | | | Mes de génesis del núcleo y de Yizi Solutions |

## Regla de la ventana de 5 horas

Cuando la ventana actual esté cerca de su límite:
1. Termina solo la tarea crítica en curso.
2. Usa el nivel de modelo más ligero que cumpla la calidad.
3. No lances subagentes en paralelo; revisa las compuertas del Consejo una a una.
4. Deja lo pendiente marcado en `tasks.md` y avisa al CEO.
