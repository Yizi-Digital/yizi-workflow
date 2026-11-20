# Tasks

> Reglas de todo el cambio:
> - Nada se publica ni se cobra sin la confirmación del CEO. Ningún cobro ocurre antes de que el contador confirme el RUC 10 (8.1).
> - Subir al repositorio remoto pide confirmación del CEO.
> - **Punto de control:** 3.1 no se hace hasta terminar el Diagnóstico Flash del tercer piloto de Solutions.
> - `activo` no autoriza vender: nada se ofrece ni se cobra antes de cerrar 8.1, 8.2 y 8.3.
> - Ningún precio ni texto comercial sale sin Edith y el CEO, ni antes de que Publisher esté activo.
> - **Regla de pausa:** si el CEO pierde horas de Solutions, el trabajo de Publisher se pausa.
> - Las secciones 4 y 5 se hacen después de los pilotos de Solutions. Si la ventana de 5 horas está justa, trabaja un agente a la vez.
> - Cada tarea dura como máximo medio día.

## 1. Decisiones previas del CEO [Viernes]

- [x] 1.1 Registrar en `consejo.md` los veredictos de Vision, Jarvis, Edith, Viernes y Ultron
- [x] 1.2 El CEO aprueba la activación, el orden de arranque (pilotos de Solutions primero) y el tope de S/ 300
- [x] 1.3 El CEO confirma sus horas reales por semana para Publisher (Ultron recomienda máximo 5 horas hasta cerrar los pilotos)
- [x] 1.3b Edith recalcula el tope de clientes con las horas confirmadas y lo anota en `design.md` (D7)
- [x] 1.4 El CEO aprueba los nombres del equipo (2026-11-18): Homer, Ágora, Faro, Quirón, Prisma, Sagita y Kepler
- [x] 1.5 El CEO fija la frontera "solo con IA" (2026-11-18): solo remoto; lo presencial se mapea y no se ofrece
- [x] 1.6 El CEO decide si suma "Acompañamiento IA" (S/ 69): sí, como último escalón (2026-11-20)
- [x] 1.7 El CEO decide si los planes responden mensajes del público: fuera de los planes actuales, en la mira como propuesta futura ("que la agencia sea un Community Manager del cliente"), 2026-11-18

## 2. Génesis del repositorio [Ultron, Vision]

- [x] 2.1 Generar `/home/user/yizi-publisher` desde la plantilla del núcleo con `/yizi-satelite` (tipo `linea`, patrocina Jarvis, líder Homer)
- [x] 2.2 Verificar la referencia al núcleo con `openspec doctor` y `openspec list --specs --store yizi-workflow`
- [ ] 2.3 Subir a `Yizi-Digital/yizi-publisher` solo con la confirmación del CEO

## 3. Registro y spec del núcleo [Viernes, Edith]

- [ ] 3.0 Punto de control: Ultron confirma que terminó el Diagnóstico Flash del tercer piloto de Solutions
- [ ] 3.1 En `satelites/registro.yaml`: cambiar `yizi-publisher` a `estado: activo`, poner su `repo` y reescribir su `descripcion` y el `rol` de Homer ("con la IA en el centro", "solo remoto", "sin embudo en fase 1"); anotar que `activo` no autoriza vender antes de 8.1 a 8.3
- [ ] 3.2 Comprobar que el delta de `satelites` pasa `openspec validate activar-yizi-publisher --strict`

## 4. Equipo de agentes en el satélite [Aida, Jarvis]

Fuente de las fichas: `estudio/aida-equipo-v2.md` (secciones 2.2 y 2.3) y la ficha de Homer de `estudio/aida-agentes.md`, con su línea "Equipo" al día.

- [x] 4.1a Redactar la ficha de Homer (N2): quién es, qué hace y límites, en `yizi-publisher/.claude/agents/homer.md`
- [x] 4.1b Completar la ficha de Homer: compuerta, equipo, liderazgo del Diagnóstico Flash único (D3) y formato de veredicto
- [x] 4.2a Redactar la ficha de Ágora (Community Manager, N3): quién es, qué hace y límites, en `yizi-publisher/.claude/agents/agora.md`
- [x] 4.2b Completar la ficha de Ágora: modelos por tarea, respuestas sugeridas que nunca se envían solas y revisión
- [x] 4.3a Redactar la ficha de Faro (presencia local y reseñas, N3): quién es, qué hace y límites, en `yizi-publisher/.claude/agents/faro.md`
- [x] 4.3b Completar la ficha de Faro: Google, WhatsApp Business, reseñas y uso del catálogo B03 de Solutions
- [x] 4.4a Redactar la ficha de Quirón (El Guía Yizi en modo enseñar IA, N3, versión mínima) en `yizi-publisher/producto/agentes/quiron.md`
- [ ] 4.4b Completar la ficha de Quirón: lección por servicio y su duración (D1); Jarvis aprueba la voz (ficha completa por Aida el 2026-11-20; falta la aprobación de voz de Jarvis)
- [x] 4.5a Redactar la ficha de Prisma (diseño y video con IA, N3): quién es, qué hace y límites, en `yizi-publisher/.claude/agents/prisma.md`
- [x] 4.5b Completar la ficha de Prisma: proveedores aprobados (D2), derechos de imagen y regla de fotos reales
- [x] 4.6 Registrar a Sagita y Kepler como diseñados, con su disparador, en el `AGENTS.md` del satélite, sin ficha activa
- [x] 4.7 Cada ficha incluye: ningún agente publica, paga ni entra a cuentas del cliente; ante clientes solo existe El Guía Yizi; solo servicios remotos con IA
- [ ] 4.8 Ultron refleja a Quirón (agente del producto) en la spec `jerarquia-agentes` del núcleo, con un cambio OpenSpec aparte si hace falta

## 5. Catálogo, precios y flujo [Jarvis, Edith, Vision]

- [x] 5.1a Escribir en el satélite los servicios 1 y 2 del catálogo (`estudio/jarvis-oferta-v2.md`), con su lección de IA, su duración (D1) y su medición
- [x] 5.1b Escribir los servicios 3 y 4, con la misma estructura; Campañas queda sin vender hasta su aprobación (D1)
- [x] 5.1c Escribir el servicio 5 (sujeto a 1.6) y la nota "sin embudo de WhatsApp en la fase 1"
- [x] 5.2 Escribir la frontera "solo con IA" en el satélite: lo que sí se hace, lo mapeado y la regla de señal para Viernes
- [ ] 5.3 Jarvis consigue 3 cotizaciones reales de Lima, sin datos del CEO ni de Yizi
- [ ] 5.4 Con las 3 cotizaciones, el CEO aprueba los precios de Edith o pide ajustes; Edith los registra. Hasta entonces son propuesta
- [ ] 5.5a Vision escribe el flujo de 7 pasos y sus estados; la aprobación del cliente es simple y funciona en el celular (WhatsApp o enlace corto)
- [ ] 5.5b Vision escribe la lista de revisión y la guía de accesos sin contraseñas
- [ ] 5.5c Vision define el registro de aprobaciones (dónde vive; quién, cuándo, qué versión y canal) y la lista de salida del cliente (se quitan accesos, se entrega su material y el cliente firma)
- [ ] 5.5d Vision verifica, antes del primer cliente, costo, derechos de uso y política de datos de cada proveedor de IA de D2, y elige el de imágenes
- [x] 5.6a Jarvis redacta el kit de plantillas de IA para el cliente, pensado para el celular; una persona de Yizi lo revisa
- [x] 5.6b Jarvis redacta la guía "Graba así con tu celular" y el mensaje corto de aprobación por WhatsApp; una persona de Yizi los revisa

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
- [ ] 8.4 Desde el primer cliente, el CEO anota los minutos reales por cliente; Edith los revisa cada mes

## 9. Verificación y cierre [Lince, Ultron]

- [ ] 9.1 Lince verifica el registro, la génesis, las 5 fichas de arranque, el catálogo, la frontera y el organigrama; nadie que construyó verifica
- [ ] 9.2 Validar con `openspec validate activar-yizi-publisher --strict`
- [ ] 9.3 Archivar cuando 2.3, 3.1, 8.3 y 9.1 estén hechas; sin el piloto propio elegido (8.3) no se archiva
