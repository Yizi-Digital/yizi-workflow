# Tasks

## 1. Estructura OpenSpec [Vision]

- [x] 1.1 Mover `config.yaml`, `specs/` y `changes/` a `openspec/` y verificar que `openspec list` encuentra la raíz
- [x] 1.2 Ejecutar `openspec init --tools claude,agents --scope project` con los 12 flujos y verificar que existen en `.agents/skills/` y `.claude/skills/`
- [x] 1.3 Escribir el contexto y las reglas de Yizi en `openspec/config.yaml` y verificar que `openspec instructions proposal` los incluye

## 2. Consejo Ejecutivo como agentes [Ultron]

- [x] 2.1 Crear la ficha de V.I.S.I.O.N en `.claude/agents/vision.md`
- [x] 2.2 Crear la ficha de J.A.R.V.I.S en `.claude/agents/jarvis.md`
- [x] 2.3 Crear la ficha de E.D.I.T.H en `.claude/agents/edith.md`
- [x] 2.4 Crear la ficha de V.I.E.R.N.E.S en `.claude/agents/viernes.md`
- [x] 2.5 Crear la ficha de U.L.T.R.O.N en `.claude/agents/ultron.md`
- [x] 2.6 Verificar que las cinco fichas pasan `claude plugin validate`

## 3. Skills de Yizi [Ultron]

- [x] 3.1 Crear el skill `yizi-consejo` en `.agents/skills/` con su enlace en `.claude/skills/`
- [x] 3.2 Crear el skill `yizi-satelite` en `.agents/skills/` con su enlace en `.claude/skills/`
- [x] 3.3 Verificar que ambos skills pasan la validación

## 4. Herencia núcleo → satélites [Vision, Viernes]

- [x] 4.1 Crear `.claude-plugin/plugin.json` y `.claude-plugin/marketplace.json` y verificar con `claude plugin validate`
- [x] 4.2 Registrar el repo como store de OpenSpec `yizi-workflow` y versionar `.openspec-store/store.yaml`
- [x] 4.3 Crear `satelites/registro.yaml` con los satélites propuestos
- [x] 4.4 Crear la plantilla `satelites/plantilla/` (README, AGENTS.md, CLAUDE.md, config de OpenSpec con `references`, settings con el plugin y ficha del líder N2)

## 5. Gobierno en Claude Code [Vision]

- [x] 5.1 Crear `.claude/settings.json` con permisos mínimos (permitir OpenSpec, pedir confirmación para push y bloquear force push, `rm -rf` y lectura de `.env`)

## 6. Documentación [Jarvis]

- [x] 6.1 Escribir `AGENTS.md` con instrucciones universales para cualquier agente de IA
- [x] 6.2 Escribir `CLAUDE.md` que importa `AGENTS.md` y añade lo específico de Claude Code
- [x] 6.3 Escribir `README.md` con el universo Yizi, la jerarquía, el ciclo y el inicio rápido

## 7. Verificación y archivo [Ultron]

- [x] 7.1 Registrar los veredictos en `consejo.md`
- [x] 7.2 Ejecutar `openspec validate big-bang-nucleo --strict` sin errores
- [x] 7.3 Archivar el cambio y verificar que `openspec list --specs` muestra las 12 capacidades
