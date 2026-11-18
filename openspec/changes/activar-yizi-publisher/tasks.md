# Tasks

> Regla de todo el cambio: nada se publica ni se cobra sin la confirmación del CEO, y ningún cobro ocurre antes de que el contador confirme el RUC 10. Subir al repositorio remoto también pide confirmación del CEO.

## 1. Decisiones previas del CEO [Viernes]

- [ ] 1.1 Registrar en `consejo.md` los veredictos de Vision, Jarvis, Edith, Viernes y Ultron
- [ ] 1.2 El CEO aprueba la activación, el orden de arranque (pilotos de Solutions primero) y el tope de S/ 300
- [ ] 1.3 El CEO confirma sus horas por semana para Publisher; Edith recalcula el tope de clientes si cambian
- [x] 1.4 El CEO aprueba los nombres del equipo (2026-11-18): Homer, Ágora, Faro, Quirón, Prisma, Sagita y Kepler
- [x] 1.5 El CEO fija la frontera "solo con IA" (2026-11-18): solo remoto; lo presencial se mapea y no se ofrece
- [ ] 1.6 El CEO decide si suma "Acompañamiento IA" (S/ 69); Jarvis recomienda solo como último escalón
- [ ] 1.7 El CEO decide si los planes responden mensajes del público; Jarvis recomienda que no

## 2. Génesis del repositorio [Ultron, Vision]

- [ ] 2.1 Generar `/home/user/yizi-publisher` desde la plantilla del núcleo con `/yizi-satelite` (tipo `linea`, patrocina Jarvis, líder Homer)
- [ ] 2.2 Verificar la referencia al núcleo con `openspec doctor` y `openspec list --specs --store yizi-workflow`
- [ ] 2.3 Subir a `Yizi-Digital/yizi-publisher` solo con la confirmación del CEO

## 3. Registro y spec del núcleo [Viernes, Edith]

- [ ] 3.1 Cambiar `yizi-publisher` a `estado: activo` en `satelites/registro.yaml` y poner su `repo`
- [ ] 3.2 Comprobar que el delta de `satelites` pasa `openspec validate activar-yizi-publisher --strict`

## 4. Equipo de agentes en el satélite [Aida, Jarvis]

Fuente de las fichas: `estudio/aida-equipo-v2.md` (secciones 2.2 y 2.3) y la ficha de Homer de `estudio/aida-agentes.md`, con su línea "Equipo" al día.

- [ ] 4.1 Crear la ficha de Homer (N2) en `yizi-publisher/.claude/agents/homer.md`
- [ ] 4.2 Crear la ficha de Ágora (Community Manager, N3) en `yizi-publisher/.claude/agents/agora.md`
- [ ] 4.3 Crear la ficha de Faro (presencia local y reseñas, N3) en `yizi-publisher/.claude/agents/faro.md`
- [ ] 4.4 Crear la ficha de Quirón (El Guía Yizi en modo enseñar IA, N3, versión mínima) en `yizi-publisher/producto/agentes/quiron.md`; Jarvis aprueba la voz
- [ ] 4.5 Crear la ficha de Prisma (diseño y video con IA, N3) en `yizi-publisher/.claude/agents/prisma.md`
- [ ] 4.6 Registrar a Sagita y Kepler como diseñados, con su disparador, en el `AGENTS.md` del satélite, sin ficha activa
- [ ] 4.7 Cada ficha incluye: ningún agente publica, paga ni entra a cuentas del cliente; ante clientes solo existe El Guía Yizi; solo servicios remotos con IA

## 5. Catálogo, precios y flujo [Jarvis, Edith, Vision]

- [ ] 5.1 Escribir el catálogo de 5 servicios (`estudio/jarvis-oferta-v2.md`) en el satélite, cada uno con su lección de IA y su medición, sin embudo de WhatsApp; el servicio 5 queda sujeto a 1.6
- [ ] 5.2 Escribir la frontera "solo con IA" en el satélite: lo que sí se hace, lo mapeado y la regla de señal para Viernes
- [ ] 5.3 Jarvis consigue 3 cotizaciones reales de Lima, sin datos del CEO ni de Yizi
- [ ] 5.4 El CEO aprueba los precios de Edith o pide ajustes; Edith los registra
- [ ] 5.5 Vision escribe el flujo de 7 pasos, la lista de revisión y la guía de accesos sin contraseñas
- [ ] 5.6 Jarvis redacta el kit de plantillas de IA para el cliente y la guía "Graba así con tu celular"; una persona de Yizi la revisa

## 6. Personas [Termy]

- [x] 6.1 Registrar los perfiles humanos de Publisher como mapeados, no ofrecidos, en `talento/mapa-de-roles.md`, sin aviso ni contacto

## 7. Organigrama y pendientes [Ultron]

- [ ] 7.1 Al activar, actualizar `README.md` (portafolio y organigrama: Publisher activo; Homer, Ágora, Faro, Quirón y Prisma activos; Sagita y Kepler con disparador)
- [ ] 7.2 Al activar, actualizar `AGENTS.md` y `agentes/mapa-de-agentes.md` (de 26 a 31 agentes activos)
- [ ] 7.3 Actualizar `ceo/pendientes.md`: quitar "Decidir cuándo activar Yizi Publisher" y sumar contador, abogado, horas y precios
- [ ] 7.4 Actualizar la ficha de Jarvis: patrocina un satélite activo

## 8. Antes del primer cliente [CEO, Edith]

- [ ] 8.1 El contador confirma el RUC 10 (RMT, actividad de marketing digital y emisión electrónica)
- [ ] 8.2 El abogado revisa el contrato de servicio (accesos de socio, propiedad de cuentas y contenido, datos personales)
- [ ] 8.3 El CEO elige el piloto propio de Publisher después de los 3 pilotos de Solutions

## 9. Verificación y cierre [Lince, Ultron]

- [ ] 9.1 Lince verifica el registro, la génesis, las 5 fichas de arranque, el catálogo, la frontera y el organigrama; nadie que construyó verifica
- [ ] 9.2 Validar con `openspec validate activar-yizi-publisher --strict`
- [ ] 9.3 Archivar cuando 2.3, 3.1 y 9.1 estén hechas
