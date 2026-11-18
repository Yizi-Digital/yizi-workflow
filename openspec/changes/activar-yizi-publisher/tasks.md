# Tasks

> Regla de todo el cambio: nada se publica ni se cobra sin la confirmación del CEO, y ningún cobro ocurre antes de que el contador confirme el RUC 10. Subir al repositorio remoto también pide confirmación del CEO.

## 1. Decisiones previas del CEO [Viernes]

- [ ] 1.1 Registrar en `consejo.md` los veredictos de Vision, Jarvis, Edith, Viernes y Ultron
- [ ] 1.2 El CEO aprueba la activación, el orden de arranque (pilotos de Solutions primero) y el tope de S/ 300
- [ ] 1.3 El CEO confirma sus horas por semana para Publisher; Edith recalcula el tope de clientes si cambian

## 2. Génesis del repositorio [Ultron, Vision]

- [ ] 2.1 Generar `/home/user/yizi-publisher` desde la plantilla del núcleo con `/yizi-satelite` (tipo `linea`, patrocina Jarvis, líder Homer)
- [ ] 2.2 Verificar la referencia al núcleo con `openspec doctor` y `openspec list --specs --store yizi-workflow`
- [ ] 2.3 Subir a `Yizi-Digital/yizi-publisher` solo con la confirmación del CEO

## 3. Registro y spec del núcleo [Viernes, Edith]

- [ ] 3.1 Cambiar `yizi-publisher` a `estado: activo` en `satelites/registro.yaml` y poner su `repo`
- [ ] 3.2 Comprobar que el delta de `satelites` pasa `openspec validate activar-yizi-publisher --strict`

## 4. Equipo de agentes en el satélite [Aida, Jarvis]

- [ ] 4.1 Crear la ficha de Homer en `yizi-publisher/.claude/agents/homer.md` desde el borrador de Aida
- [ ] 4.2 Incorporar la propuesta de equipo de Aida (`estudio/aida-equipo-v2.md`) cuando exista, con los nombres que apruebe el CEO
- [ ] 4.3 Crear las fichas aprobadas del equipo con un cambio en el satélite; Jarvis aprueba la voz de El Guía Yizi

## 5. Catálogo, precios y flujo [Jarvis, Edith, Vision]

- [ ] 5.1 Escribir el catálogo de 4 servicios en el satélite, cada uno con su lección de IA y su medición
- [ ] 5.2 Resolver con el CEO las preguntas abiertas 1 (escalón de salida) y 2 (quién responde mensajes)
- [ ] 5.3 Jarvis consigue 3 cotizaciones reales de Lima, sin datos del CEO ni de Yizi
- [ ] 5.4 El CEO aprueba los precios de Edith o pide ajustes; Edith los registra
- [ ] 5.5 Vision escribe el flujo de 7 pasos, la lista de revisión y la guía de accesos sin contraseñas
- [ ] 5.6 Jarvis redacta el kit de plantillas de IA para el cliente

## 6. Personas [Termy]

- [ ] 6.1 Registrar el perfil "Creador de contenido de barrio" como borrador en `talento/mapa-de-roles.md`, sin aviso ni contacto

## 7. Organigrama y pendientes [Ultron]

- [ ] 7.1 Actualizar `README.md` (portafolio y organigrama: Publisher activo, Homer con ficha)
- [ ] 7.2 Actualizar `AGENTS.md` y `agentes/mapa-de-agentes.md`
- [ ] 7.3 Actualizar `ceo/pendientes.md`: quitar "Decidir cuándo activar Yizi Publisher" y sumar contador, abogado, horas y precios
- [ ] 7.4 Actualizar la ficha de Jarvis: patrocina un satélite activo

## 8. Antes del primer cliente [CEO, Edith]

- [ ] 8.1 El contador confirma el RUC 10 (RMT, actividad de marketing digital y emisión electrónica)
- [ ] 8.2 El abogado revisa el contrato de servicio (accesos de socio, propiedad de cuentas y contenido, datos personales)
- [ ] 8.3 El CEO elige el piloto propio de Publisher después de los 3 pilotos de Solutions

## 9. Verificación y cierre [Lince, Ultron]

- [ ] 9.1 Lince verifica el registro, la génesis, la ficha de Homer, el catálogo y el organigrama; nadie que construyó verifica
- [ ] 9.2 Validar con `openspec validate activar-yizi-publisher --strict`
- [ ] 9.3 Archivar cuando 2.3, 3.1 y 9.1 estén hechas
