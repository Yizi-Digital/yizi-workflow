# Proposal: Satélites en repos propios, nombres en inglés y consumo de IA

| Campo | Valor |
|---|---|
| Dueño | V.I.E.R.N.E.S (Viernes) · CSO |
| Alcance | nucleo |
| Tipo | estrategico |
| Tamaño | L (cambia specs del núcleo) |
| Compuertas | Consejo completo (Vision, Jarvis, Edith, Viernes, Ultron) + aprobación del CEO |
| Aprobación | Decisiones del CEO del 2026-11-17 (respuesta a los pendientes del cambio `big-bang-nucleo`) |

## Why

El CEO resolvió los pendientes del Big Bang: los satélites llevan nombre comercial en inglés, cada satélite es un repositorio separado dentro de la organización de GitHub de Yizi Digital, Yizi Solutions es el primer satélite que se crea, y el límite de gasto en IA no es una cifra fija sino el consumo observado del plan (ventanas de 5 horas y consumo mensual). Las siglas de los agentes no tienen un significado: son nombres propios.

**Valor que lo justifica:** Agilidad Real (un repo por satélite permite que cada línea avance a su ritmo) y Robustez Invisible (el consumo de IA se controla sin frenar el trabajo crítico).

## What Changes

- `satelites`: nuevo requisito que obliga a que cada satélite viva en su propio repositorio dentro de la organización `YiziDigital`, con nombre igual a su id.
- `comunicacion`: la arquitectura de marca usa descriptores en inglés ("Yizi Solutions", "Yizi Growth", "Yizi Talent").
- `finanzas`: se retira el límite fijo con avisos al 80 % y 100 %; se añaden "Límite de gasto según consumo observado" y "Consumo por ventana de 5 horas".
- Registro de satélites: ids y nombres en inglés (`yizi-solutions`, `yizi-growth`, `yizi-talent`), líderes aprobados y repositorio de Yizi Solutions.
- Fichas de los agentes: se eliminan los significados inventados de las siglas y se actualizan los satélites que patrocinan.
- Skill `yizi-satelite`: crea el repo remoto en `YiziDigital/<id>` (con confirmación humana).
- Nuevo registro mensual de consumo de IA para Edith.
- Génesis local del repositorio `yizi-solutions` desde la plantilla.

## Capabilities

### New Capabilities
- Ninguna.

### Modified Capabilities
- `satelites`: se añade el requisito de repositorio propio en la organización.
- `comunicacion`: cambia el requisito de arquitectura de marca.
- `finanzas`: se retira "Límite de gasto mensual" y se añaden dos requisitos de consumo de IA.

## Impact

- `satelites/registro.yaml`, `.claude/agents/*.md`, `.agents/skills/yizi-satelite/SKILL.md`, `README.md`, nuevo `finanzas/consumo-ia.md`.
- Nuevo repositorio local `yizi-solutions` (junto al núcleo). El repositorio remoto `YiziDigital/yizi-solutions` lo crea el CEO o se crea con su confirmación.
- **Estimación de costo (compuerta de Edith):** 0 USD; consumo de IA de una sesión dentro del plan vigente.

## Out of Scope

- Primer cambio de negocio dentro de Yizi Solutions (su primer Diagnóstico Flash o MVP).
- Repositorios de Yizi Growth y Yizi Talent (siguen en incubación).
- Fijar una cifra de gasto: se decidirá tras observar el consumo de los primeros meses.
