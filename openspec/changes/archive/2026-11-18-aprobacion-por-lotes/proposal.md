# Proposal: Aprobación por lotes y persona de respaldo del CEO

| Campo | Valor |
|---|---|
| Dueño | U.L.T.R.O.N (Ultron) · COO |
| Alcance | nucleo |
| Tipo | operacion |
| Tamaño | L (cambia una regla de gobierno del núcleo) |
| Compuertas | Consejo completo + aprobación del CEO |
| Aprobación | Aprobado por el CEO el 2026-11-18 (lotes: "sí está bien"; respaldo: "un familiar") |

## Why

El estudio del flujo operativo mostró que el CEO es el único punto de decisión. Confirmar cada cobro uno por uno no escala más allá de los pilotos. Además, si el CEO no está, nadie lo cubre.

**Valor que lo justifica:** autogestión y crecimiento rentable, sin perder el control humano.

## What Changes

- `gobierno-agentes`: la confirmación de acciones irreversibles admite lotes aprobados con plantilla, tope y fecha de fin.
- Nuevos requisitos: "Aprobación por lotes", "Acciones que nunca van en lote" y "Persona de respaldo del CEO".

## Capabilities

### New Capabilities
- Ninguna.

### Modified Capabilities
- `gobierno-agentes`: se modifica un requisito y se añaden tres.

## Impact

- Los agentes que preparan cobros (cierre mensual) usarán lotes cuando existan. Costo: 0 USD.

## Out of Scope

- El nombre de la persona de respaldo y el instrumento legal (los define el CEO con el abogado).
