# Proposal: Activar a Lince, Ábaco y Chaski, y un PR por repositorio

| Campo | Valor |
|---|---|
| Dueño | U.L.T.R.O.N (Ultron) · COO |
| Alcance | nucleo (y yizi-solutions para Ábaco y Chaski) |
| Tipo | operacion |
| Tamaño | M |
| Compuertas | Ultron + Aida (opinión) + aprobación del CEO |
| Aprobación | Pedido del CEO del 2026-11-18: "activemos Lince, Ábaco y Chaski" y "no llenemos los repositorios de PRs" |

## Why

Los tres agentes de antes de los pilotos tienen nombre aprobado. Además, el CEO pidió un flujo controlado sin llenar los repositorios de pull requests, para no perder la trazabilidad.

**Valor que lo justifica:** Robustez Invisible (verificación independiente) y Agilidad Real (menos PRs, más claros).

## What Changes

- `jerarquia-agentes`: Lince se suma a los agentes de área; nuevo requisito "Agentes del producto".
- `ciclo-sdd`: nuevo requisito "Un pull request abierto por repositorio".
- Núcleo: ficha de Lince en `.claude/agents/lince.md`, plugin, `AGENTS.md`, ficha de Ultron, organigrama y pendientes del CEO.
- Yizi Solutions: ficha de Ábaco en `.claude/agents/abaco.md` y de Chaski en `producto/agentes/chaski.md`, dentro del PR abierto del catálogo.

## Capabilities

### New Capabilities
- Ninguna.

### Modified Capabilities
- `jerarquia-agentes`: se modifica un requisito y se añade uno.
- `ciclo-sdd`: se añade un requisito.

## Impact

- Costo: Lince y Ábaco usan nivel Estándar en sesiones. Chaski no usa IA en su versión mínima.

## Out of Scope

- La versión de Chaski con IA (requiere la cuenta de API de Yizi y la plataforma).
