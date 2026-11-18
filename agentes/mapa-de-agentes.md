# Mapa de agentes de IA · Yizi Digital

| Campo | Valor |
|---|---|
| Dueña | A.I.D.A (Aida), diseño de agentes del núcleo |
| Spec | `diseno-agentes` |
| Para quién | El CEO, Ultron (que pidió el estudio) y Termy (que cubre las personas) |
| Estado | **Estudio.** No es un plan aprobado. No crea fichas ni activa agentes. Cada agente nuevo necesita su propio cambio OpenSpec aprobado por el CEO. |
| Base | `yizi-solutions/operacion/flujo-operativo.md` (Ultron, 2026-11-18), specs `diseno-agentes`, `jerarquia-agentes`, `gobierno-agentes`, `finanzas`, `calidad`, `comunicacion` y `comercial`, las 9 fichas que existen, `satelites/registro.yaml`, `talento/mapa-de-roles.md` y `catalogo/bloques-tecnologicos.md` de Yizi Solutions |
| Fecha | 2026-11-18 |

---

## 0. La respuesta corta

1. **Yizi tiene 11 agentes en el mapa.** Hay 9 fichas escritas y 2 líderes con nombre aprobado y sin ficha (Homer y Jocasta). **Ninguna de las 11 fichas cumple completa mi lista de revisión.** El fallo común: ninguna tiene referencias con fuente y fecha, y la spec `diseno-agentes` lo exige.
2. **Propongo 9 agentes nuevos.** Los ocho huecos de Ultron quedan en 7 agentes, porque fusiono los que se cruzan. Añado 2 agentes que faltaban.
3. **Solo 3 hacen falta antes de los pilotos:** el verificador independiente, el analista de pilotos y El Guía Yizi en modo ayuda (en versión mínima). El cumplimiento de antes de los pilotos se hace con tareas sueltas, sin agente fijo.
4. **Hay dos tipos de agente, y no se deben mezclar.** Los **agentes del producto** trabajan dentro de la plataforma con los bodegueros, siempre como El Guía Yizi. Los **agentes internos** trabajan para Yizi en sesiones de Claude Code y nunca hablan con un cliente.
5. **La regla de aprobación por plantilla y por lote es necesaria** antes de unos 50 negocios. La apoyo con 8 condiciones (sección 5). El borrado de datos queda siempre fuera del lote.
6. **Ningún agente interno necesita trabajar siempre encendido (A4) antes de 143 negocios.** El trabajo continuo lo hace el sistema (código), y el agente revisa en sesión. En cambio, los agentes del producto funcionan siempre por naturaleza: cada función necesita una aprobación A4 del CEO y una cuota de Edith.

---

## 1. Mapa de agentes actual (11)

### 1.1 Cómo leer la tabla

**Estado** (spec `diseno-agentes`): propuesto, aprobado, activo, retirado.

**Lista de revisión de Aida.** Cada columna es una casilla de mi ficha:

| Columna | Qué reviso |
|---|---|
| C1 | Tiene nivel, dominio, a quién reporta y autonomía |
| C2 | Su criterio está escrito: qué decide y qué escala |
| C3 | Sus referencias tienen fuente y fecha, o dicen "no verificado" |
| C4 | Usa el nivel de modelo más barato que cumple la calidad |
| C5 | Respeta `gobierno-agentes` (incluye permisos mínimos) y la guía de escritura |
| C6 | No se cruza con otro agente |

Valores: **Sí** · **Parcial** · **No** · **—** (no aplica, porque no hay ficha).

### 1.2 Tabla

| Agente | Nivel | Dominio | Reporta a | Estado | Modelo | C1 | C2 | C3 | C4 | C5 | C6 | ¿Ficha completa? |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Vision (CTO) | N1 Consejo | Tecnología, arquitectura, calidad, seguridad técnica | CEO | Activo | Avanzado | Sí | Sí | No | Parcial | Parcial | Parcial | No |
| Jarvis (CDO) | N1 Consejo | Marca, comunicación, ventas digitales, cliente | CEO | Activo | Estándar | Sí | Sí | Parcial | Sí | Sí | Parcial | No |
| Edith (CFO) | N1 Consejo | Finanzas, precios, costos de IA | CEO | Activo | Avanzado | Sí | Sí | Parcial | Sí | Sí | Sí | No |
| Viernes (CSO) | N1 Consejo | Estrategia, satélites, MACRO, cultura | CEO | Activo | Avanzado | Sí | Sí | No | Sí | Sí | Sí | No |
| Ultron (COO) | N1 Consejo | Ciclo SDD, orquestación, reglas | CEO | Activo | Estándar | Sí | Sí | No | Sí | Parcial | Sí | No |
| Aida | N1 área | Diseño de agentes | Ultron | Activo | Avanzado | Sí | Parcial | No | Sí | Sí | Sí | No |
| Termy | N1 área | Talento humano | Ultron | Activo | Estándar | Sí | Parcial | No | Sí | Sí | Sí | No |
| Karen | N2 Yizi Solutions | Entrega de soluciones | Vision | Activo | Estándar | Sí | No | No | Sí | Sí | Parcial | No |
| Herbie | N2 Yizi Projects | Proyectos MACRO propios | Viernes | Activo (sin proyectos) | Estándar | Sí | No | No | Sí | Sí | Sí | No |
| Homer | N2 Yizi Publisher | Campañas y embudos | Jarvis | Nombre aprobado, sin ficha | — | — | — | — | — | — | — | No existe |
| Jocasta | N2 Yizi Talent | Outsourcing de talento | Ultron | Nombre aprobado, sin ficha | — | — | — | — | — | — | — | No existe |

**El Guía Yizi no está en la tabla.** Hoy es una identidad de marca (spec `comunicacion`) y unas funciones de la plataforma (bloques B01, B09 y B10). No tiene ficha de agente. La sección 3 lo trata.

### 1.3 Qué falta en cada ficha

| Agente | Qué falta | Por qué importa |
|---|---|---|
| Todas | Una sección de **referencias** con fuente y fecha. | La spec `diseno-agentes` lo exige. Sin referencias, el agente decide solo con lo que "sabe". |
| Todas | El **costo por uso** estimado. | Ultron y Edith lo piden en cada ficha nueva. Sin ese dato, Edith no puede medir por agente. |
| Vision y Ultron | La línea `tools:` de su cabecera. | Sin esa línea, Claude Code les da **todas** las herramientas. Eso rompe la regla de permisos mínimos. |
| Vision | Delegar la ejecución diaria. | Vision usa el nivel Avanzado. Si también escribe todo el código, cada tarea simple cuesta como una de arquitectura. Puede delegar tareas a ejecutores N4 de nivel Estándar. |
| Vision | Un verificador que no sea él. | Vision implementa casi todo y también es quien más verifica. La spec `calidad` prohíbe que quien implementa sea el único que verifica. |
| Jarvis y Karen | Quién es dueño del Diagnóstico Flash. | Jarvis "dirige el Ciclo de Servicio" (su ficha). El flujo de Ultron dice que Karen "define el Diagnóstico Flash". Hay que fijar un dueño. |
| Edith | Fuente y fecha de la tabla de modelos. | Su ficha nombra los modelos de cada nivel, sin fecha de consulta. |
| Termy | Referencias de selección y de normas laborales. | Opina sobre la locación de servicios y sobre pruebas psicológicas. Necesita fuentes oficiales, revisadas con el abogado. |
| Aida y Termy | Un criterio de escalamiento escrito. | Sus fichas dicen qué hacen, pero no qué deciden solas ni qué escalan. |
| Karen y Herbie | Un criterio propio. | Son la plantilla genérica del satélite. Karen no dice qué decide en Yizi Solutions (por ejemplo, el criterio de paso de oleada o qué tarea va a cada especialista). |
| Homer y Jocasta | La ficha completa. | **No hace falta todavía.** Sus satélites están en incubación. La ficha se escribe cuando Viernes proponga activarlos. |

**Recomendación:** un solo cambio OpenSpec de tamaño S o M ("completar fichas") arregla las referencias, el costo por uso, las herramientas de Vision y Ultron y el dueño del Diagnóstico Flash. Lo propongo después de este estudio, si el CEO lo aprueba.

---

## 2. Agentes que faltan

### 2.1 Cómo traté los huecos de Ultron

| Hueco de Ultron | Mi decisión | Por qué |
|---|---|---|
| IA-1 Soporte de primera línea | **Se crea** como modo de El Guía Yizi (agente del producto). | Lo ve el bodeguero. Debe ser El Guía Yizi, no un agente aparte. |
| IA-2 Verificador independiente | **Se crea** como agente de área del núcleo (N1), bajo Ultron. | Si reporta a Karen, reporta a Vision. Entonces no es independiente de quien construye. |
| IA-3 Medición y analista de pilotos | **Se crea.** Absorbe el costo por negocio y el análisis de los motivos del "no". | Todo es medición. Un solo agente da una sola versión de los números. |
| IA-4 Cobros y conciliación | **Se fusiona con IA-7** en un agente de cierre mensual. | Las dos tareas preparan dinero del mes, con las mismas reglas: Edith valida y el CEO ejecuta. |
| IA-5 Cumplimiento | **Se crea en dos pasos.** Antes de los pilotos: tareas N4 sueltas. A los 50 negocios: agente fijo. | Antes de los pilotos es un trabajo de una sola vez. Un agente fijo para eso es un costo sin uso. |
| IA-6 Alta guiada | **Se fusiona con IA-1** como otro modo de El Guía Yizi. | Lo usan el dueño (a distancia) y el Promotor (en el local), en la misma plataforma. |
| IA-7 Liquidación del Promotor | **Se fusiona con IA-4.** | Ver IA-4. |
| IA-8 Prospección | **Se redefine y se pospone** a 143 negocios, como planificador de campo. | Los guiones ya son de Jarvis. Los motivos del "no" pasan al analista. Lo que queda (rutas y jornadas) solo pesa con varios promotores. |

**Agentes que añado:**

| Nuevo | Por qué falta |
|---|---|
| Triaje de incidencias y vigilancia de la plataforma | Nadie clasifica la gravedad de un fallo ni revisa cada día si el respaldo corrió (flujo, etapa 6 y sección B). Con una sola versión para todos, un defecto toca a 50 negocios a la vez. |
| Evaluador de las conversaciones del Guía | Nadie revisa si El Guía Yizi responde bien en producción. El verificador revisa antes de publicar; este revisa después. |

**Lo que NO propongo como agente nuevo**, porque otro ya lo cubre:

| Tarea | Quién la cubre |
|---|---|
| Textos de plantillas de WhatsApp, avisos de Meta y de mora | Jarvis |
| Preparar la bandeja de lotes para el CEO | Ultron. Hay que añadirlo a su ficha. |
| Costo de IA del mes y por agente | Edith, con datos del analista |
| Contactar a los deudores del bodeguero | **Nadie.** Está descartado por defecto (flujo, etapa 5). Un agente que cobra a terceros tiene riesgo legal (Ley 29571, artículos 61 y 62, ver referencias). |
| Vender por WhatsApp sin una persona | **Nadie.** Cada envío hacia afuera necesita al CEO. |
| Tareas de una sola vez (unir las dos cláusulas de Meta, datos de la demo, inventario de datos) | Ejecutores N4 de nivel Ligero o Estándar, bajo el agente dueño |

### 2.2 Resumen priorizado

Nombres de trabajo descriptivos. **El CEO elige los nombres propios.** Deben ser únicos en todo Yizi (`jerarquia-agentes`).

| # | Agente (nombre de trabajo) | Tipo | Nivel | Dónde | Momento | Prioridad | Hueco |
|---|---|---|---|---|---|---|---|
| 1 | Verificador independiente | Interno | N1 área | Núcleo | **Antes de los pilotos** | Crítica | IA-2 |
| 2 | Analista de pilotos y de operación | Interno | N3 | Yizi Solutions | **Antes de los pilotos** | Alta | IA-3, parte de IA-8 |
| 3 | El Guía Yizi · modo ayuda | Producto | N3 | Yizi Solutions | **Antes de los pilotos** (versión mínima). Con IA, antes de 50 | Alta | IA-1 |
| 4 | Cumplimiento y datos personales | Interno | N4 antes de los pilotos; N3 a los 50 | Yizi Solutions | **Antes de los pilotos** (tareas sueltas). Agente fijo, a los 50 | Alta | IA-5 |
| 5 | Cierre mensual: cobros, conciliación y liquidación del Promotor | Interno | N3 | Yizi Solutions | **Entre los pilotos y 50**, con el primer cobro a precio de lista | Alta | IA-4 + IA-7 |
| 6 | El Guía Yizi · modo alta guiada | Producto | N3 | Yizi Solutions | **Antes de 50** | Media | IA-6, T-17 |
| 7 | Triaje de incidencias y vigilancia de la plataforma | Interno | N3 | Yizi Solutions | **Al llegar a 50** | Media | Nuevo (etapa 6, sección B, T-19) |
| 8 | Evaluador de las conversaciones del Guía | Interno | N3 | Yizi Solutions | **Al llegar a 143** | Media | Nuevo |
| 9 | Planificador de campo | Interno | N3 | Yizi Solutions | **Al llegar a 143** | Baja | IA-8 redefinido |

**A los 300 negocios no propongo tipos nuevos de agente.** Propongo revisar tres cosas (sección 2.4).

**Ningún agente nuevo para Yizi Publisher, Yizi Talent ni Yizi Projects.** Publisher y Talent están en incubación. Projects no tiene proyectos. Regla de foco: no se diseña para satélites que no operan.

### 2.3 Fichas de estudio

Cada ficha de estudio tiene los campos que pidió Ultron. **No son fichas de agente:** son la base para el cambio OpenSpec de cada uno.

Referencias: la lista completa, con enlaces y fecha, está en la sección 6. Aquí uso su número (R1, R2…).

Niveles de modelo (ficha de Edith, sin fecha de consulta): Ligero = Haiku 5.5 · Estándar = Sonnet 5.5 · Avanzado = Opus 5.5 · Frontera = Fable 5.2.

---

#### 1 · Verificador independiente

| Campo | Detalle |
|---|---|
| Tipo, nivel, dónde | Interno · N1 agente de área · núcleo (llega a los satélites con el plugin `yizi-nucleo`) |
| Reporta a | Ultron → CEO. **No reporta a Vision**, para ser independiente de quien construye. |
| Momento y prioridad | Antes de los pilotos · Crítica. La plataforma de la Oleada 1 se construye antes de los pilotos, y sin verificación independiente no se puede archivar (spec `calidad`). |
| Hueco que cubre | IA-2. También la condición de Ultron para archivar: "verificación independiente hecha". |
| Qué decide | Si cada escenario de la spec tiene evidencia. Si la prueba pasa en tamaño de celular y con red lenta simulada. Si las pruebas de aislamiento entre negocios pasan. Su veredicto: VERIFICADO, CON OBSERVACIONES o NO VERIFICADO. |
| Qué escala | A Ultron: cualquier NO VERIFICADO. A Vision y al CEO: un fallo de aislamiento entre negocios, de pagos o de datos personales. Al CEO: un desacuerdo con Vision. |
| Experiencia que representa | Un ingeniero de pruebas (QA) con experiencia en aplicaciones móviles y en pagos. Conoce pruebas de aceptación y de seguridad básica. |
| Referencias | R1 (ISO/IEC 25010:2023), R2 (OWASP Top 10 para LLM 2025), spec `calidad` del núcleo, `bloques-tecnologicos.md` (reglas R6 y R11). Programa ISTQB de nivel básico: **no verificado.** |
| Modelo | **Estándar.** Ligero para correr pruebas y resumir resultados (N4). Avanzado solo si Ultron y Edith lo aprueban para un cambio L de seguridad. |
| Autonomía máxima | A3: corre pruebas y escribe el informe de verificación dentro del cambio. |
| Herramientas | Read, Grep, Glob y Bash para correr pruebas. Write solo en el informe de verificación del cambio. Sin acceso a producción. Sin WebFetch. |
| Qué NO puede hacer | Verificar algo que él implementó. Corregir el código que verifica (lo devuelve). Desplegar, fusionar a la rama principal ni archivar sin el CEO. Marcar como verificado un escenario sin evidencia. Usar datos reales de negocios en las pruebas. |
| Costo por uso | Una sesión por cambio, en el plan de IA. Sin medir. Edith lo registra por agente en `finanzas/consumo-ia.md`. |
| Cómo se mide | 100 % de los cambios archivados con verificación de otro agente o persona. Defectos encontrados en producción por versión (meta: bajar con el tiempo). Escenarios sin evidencia al archivar: 0. |
| Límite real | No puede probar en una bodega real. La prueba en el celular del dueño y con la señal del barrio la hace una persona (sección 4). |

---

#### 2 · Analista de pilotos y de operación

| Campo | Detalle |
|---|---|
| Tipo, nivel, dónde | Interno · N3 · Yizi Solutions |
| Reporta a | Karen. Entrega sus datos a Edith (costos) y a Karen (mejoras). |
| Momento y prioridad | Antes de los pilotos · Alta. Los pilotos existen para medir. La hoja semanal debe estar lista en la semana 1. |
| Hueco que cubre | IA-3, T-10 (hoja semanal y costo por negocio), el análisis de motivos del "no" (antes en IA-8). A los 50 negocios, también revisa una muestra pequeña de conversaciones del Guía, hasta que entre el agente 8. |
| Qué decide | Qué datos faltan y qué alertas mandar: soporte por encima del supuesto, costo variable más de 20 % sobre el supuesto, un negocio que deja de registrar. |
| Qué escala | A Karen: ideas de mejora y negocios en riesgo. A Edith: costo fuera del supuesto. Al CEO, por Karen: el criterio de paso de oleada. |
| Experiencia que representa | Una analista de operaciones y de éxito del cliente en una empresa de software por suscripción. |
| Referencias | `economia.md` sección 6 (métricas de los pilotos), criterio de éxito del CEO (flujo, etapa 9), bloques B10 y B12. Regla de la plataforma: "la IA no calcula cifras" (`bloques-tecnologicos.md`). |
| Modelo | **Estándar** para el informe semanal. Las cifras salen de consultas y scripts, nunca de la IA. Ligero (N4) para armar tablas. |
| Autonomía máxima | A3: corre consultas de solo lectura y escribe la hoja semanal. |
| Herramientas | Read, Grep, Glob. Bash solo para consultas de solo lectura sobre datos agregados por negocio. Write solo en la carpeta de medición del satélite. |
| Qué NO puede hacer | Inventar o estimar una cifra que falta (escribe "sin medir"). Ver datos de deudores con nombre: trabaja con datos agregados. Cambiar precios, cuotas ni tramos. Publicar testimonios. Hablar con dueños. |
| Costo por uso | Una sesión por semana en los pilotos, en el plan de IA. Sin medir. |
| Cómo se mide | Hoja semanal entregada cada semana de piloto. Cifras sin fuente: 0. Correcciones de Edith a sus números (meta: 0). |

---

#### 3 · El Guía Yizi · modo ayuda

| Campo | Detalle |
|---|---|
| Tipo, nivel, dónde | **Producto** · N3 · Yizi Solutions. Vive en la plataforma (B01 y B10), no en Claude Code. |
| Reporta a | Karen (comportamiento). Vision es dueño técnico (`design.md`). Jarvis es dueño de la voz (spec `comunicacion`). |
| Momento y prioridad | **Antes de los pilotos, versión mínima:** menú de botones, preguntas frecuentes y paso a una persona. Anota minutos y motivo. **Con IA (Ligero), antes de 50**, cuando los pilotos digan qué preguntan los dueños. Prioridad Alta. |
| Hueco que cubre | IA-1, T-9 (registro de minutos y motivo de soporte). |
| Qué decide | Qué flujo guiado ofrecer según la pregunta. Cuándo pasar a una persona: no entiende dos veces, el dueño lo pide, hay dinero en juego, el dueño está molesto, o se reporta un posible fallo de datos. |
| Qué escala | A una persona (Promotor o CEO; después, soporte humano): todo lo que no resuelve. Al triaje (agente 7): cada posible fallo. |
| Experiencia que representa | Una persona de mesa de ayuda de primer nivel, paciente y con trato de barrio. Explica con ejemplos de la bodega. |
| Referencias | R3 (Anthropic, "Building effective agents"): flujos fijos antes que agentes libres. R4 (ITIL 4, gestión de incidentes). R2 (OWASP: inyección de instrucciones y consumo sin límite). Bloques B01 y B10, guía de escritura. Política de WhatsApp Business: **no verificado.** |
| Modelo | Escalera de B10: botones sin IA → **Ligero** → Estándar solo si el Ligero no alcanza → persona. **Nunca Avanzado ni Frontera** (regla de Vision). |
| Autonomía máxima | A3 en cada conversación. Como corre siempre, la función necesita **una aprobación A4 del CEO y una cuota de Edith** (`gobierno-agentes`). |
| Herramientas | Solo funciones de la plataforma de ese negocio: leer la guía de ayuda, ver el estado de su cuenta, abrir una incidencia. Sin archivos. Sin internet. |
| Qué NO puede hacer | Ver los datos del negocio sin permiso del dueño (queda en B12). Prometer funciones, fechas o precios. Dar descuentos. Confirmar un pago. Mover dinero o stock. Borrar nada. Presentarse con un nombre interno. Obedecer instrucciones que vengan en un mensaje o una foto. |
| Costo por uso | Llamadas de IA y mensajes por consulta. **Los supuestos de cuota de Edith no separan las llamadas de ayuda.** Edith debe decidir si caben en la cuota del tramo. Los mensajes que inicia el dueño cuentan en la franja de servicio de WhatsApp (flujo, sección 7). |
| Cómo se mide | Minutos de soporte humano por negocio al mes, frente al supuesto (10, 15 y 20 min por tramo). Porcentaje de consultas resueltas sin persona: **sin dato**, se mide en pilotos. Respuestas con una promesa falsa: 0. Costo de IA por consulta. |

---

#### 4 · Cumplimiento y datos personales

| Campo | Detalle |
|---|---|
| Tipo, nivel, dónde | Interno · Yizi Solutions. **Antes de los pilotos:** tareas N4 bajo Karen y Vision. **A los 50:** agente N3 fijo. Pasa al núcleo cuando Yizi Publisher maneje datos de clientes. |
| Reporta a | Karen. Vision en lo técnico. Su material va al abogado por el CEO (decisión 30). |
| Momento y prioridad | Antes de los pilotos (tareas sueltas) · Alta. Cargar deudas de terceros espera la revisión del abogado (flujo, etapa 4). |
| Hueco que cubre | IA-5, sección D del flujo, parte de T-7 y T-19. |
| Qué hace antes de los pilotos | Tres tareas sueltas: (1) inventario de qué datos se guardan, dónde y por cuánto tiempo; (2) lista de consentimientos que hacen falta, con fecha; (3) paquete de preguntas para el abogado. |
| Qué decide (agente fijo) | Si cada negocio y cada mensaje tienen su consentimiento con fecha. Si un texto de cobro rompe una regla escrita por el abogado. Qué hallazgos van al informe del mes. |
| Qué escala | Al CEO y a Vision: cualquier posible fuga o uso fuera del fin acordado, el mismo día. Al abogado, por el CEO: toda duda legal. |
| Experiencia que representa | Una asistente de cumplimiento normativo y de protección de datos. Ordena evidencia. No es abogada. |
| Referencias | R5 (Ley 29733 de Perú), R6 (su reglamento, D.S. 016-2024-JUS), R7 (Ley 29571, artículos 61 y 62, cobranza), R9 (NIST AI RMF y perfil de IA generativa). **Qué obligaciones aplican a Yizi: no verificado.** Lo decide el abogado. |
| Modelo | **Estándar.** Ligero (N4) para cruzar listas de consentimientos. |
| Autonomía máxima | A3 (prepara informes). Lectura de datos: solo metadatos y registros de consentimiento, no el contenido de las deudas. |
| Herramientas | Read, Grep, Glob. Bash de solo lectura sobre registros de consentimiento y auditoría (B12). Write solo en la carpeta de cumplimiento. WebSearch solo para buscar la norma oficial, con fecha. |
| Qué NO puede hacer | Dar asesoría legal. Decir "esto es legal". Avisar a una autoridad o a un afectado (lo decide el CEO con el abogado). Borrar datos. Ver el contenido de las deudas. |
| Costo por uso | Antes de los pilotos: unas pocas sesiones, una vez. Después: una sesión al mes. Sin medir. |
| Cómo se mide | Fichas de deudores con consentimiento y fecha: 100 %. Hallazgos abiertos de más de 30 días: 0. Paquete al abogado entregado antes del primer piloto. |

---

#### 5 · Cierre mensual: cobros, conciliación y liquidación del Promotor

| Campo | Detalle |
|---|---|
| Tipo, nivel, dónde | Interno · N3 · Yizi Solutions. Si otro satélite empieza a cobrar, se evalúa moverlo al núcleo, bajo Edith. |
| Reporta a | Karen. **Edith valida cada salida**, porque es su dominio. El CEO ejecuta. |
| Momento y prioridad | Entre los pilotos y 50, con el primer cobro a precio de lista · Alta. En los 3 pilotos, el CEO y Edith lo hacen a mano. Así se aprende la regla. |
| Hueco que cubre | IA-4 e IA-7, la fila "conciliar" de la sección C, parte de T-16 (lista de mora). |
| Qué decide | Nada que mueva dinero. Prepara cuatro listas: (1) cobros del mes por negocio y tramo; (2) pagos de Izipay que cuadran y los que no; (3) negocios en mora según la regla aprobada; (4) liquidación del Promotor (comisión al tercer mes, bono desde el mes 4, movilidad y datos). |
| Qué escala | A Edith: cada diferencia sin explicar y la liquidación completa. Al CEO, en un solo lote: cobros, comprobantes, pasos a solo lectura y pago al Promotor. |
| Experiencia que representa | Un asistente contable con experiencia en cobranza de suscripciones y conciliación bancaria. |
| Referencias | Spec `finanzas` (separar preparar de pagar), regla de B07 (una captura no confirma un pago; la conciliación usa reglas fijas, sin IA), decisiones 25 y 27 (pago del Promotor), R8 (SUNAT, emisión electrónica). Tarifa de Izipay: verificada por Edith con una reserva. Que Izipay acepte RUC 10: **no verificado.** |
| Modelo | **Ligero.** La conciliación la hace un script con reglas fijas. El agente explica las diferencias. Estándar solo para un caso raro. |
| Autonomía máxima | A3: corre el script y prepara las listas. |
| Herramientas | Read, Grep, Glob. Bash de solo lectura sobre el reporte exportado de Izipay y sobre los negocios activos. Write solo en la carpeta del cierre del mes. **Sin acceso al banco, a Izipay ni a la Clave SOL.** |
| Qué NO puede hacer | Cobrar, emitir un comprobante, pagar, pasar un negocio a solo lectura ni borrar. Confirmar un pago con una captura. Juzgar el trabajo del Promotor (solo calcula). Escribir datos bancarios en el repositorio. |
| Costo por uso | Una o dos sesiones al mes. Sin medir. |
| Cómo se mide | Pagos conciliados por el script sin intervención (meta: subir mes a mes). Diferencias sin explicar al cierre: 0. Correcciones de Edith a la liquidación: 0. Días desde el fin de mes hasta el lote listo. |

---

#### 6 · El Guía Yizi · modo alta guiada

| Campo | Detalle |
|---|---|
| Tipo, nivel, dónde | **Producto** · N3 · Yizi Solutions (B02, B03, B05, B08, B09, B10). |
| Reporta a | Karen. Vision es dueño técnico. Jarvis, de la voz. |
| Momento y prioridad | Antes de 50 · Media. Los 3 pilotos son presenciales. Lo que se aprenda ahí se convierte en los pasos de la alta a distancia. |
| Hueco que cubre | IA-6 y T-17 (Diagnóstico Flash ligero, como primer paso del alta). |
| Qué decide | El orden de los pasos. Qué dato falta. El tramo sugerido, con la tabla de Edith y reglas fijas. |
| Qué escala | Al Promotor o al CEO: un dato que el dueño no confirma, un alta que pasa del tiempo máximo, un dueño que no acepta el aviso de privacidad o los mensajes. |
| Experiencia que representa | Una persona que instala y capacita en sistemas de caja para pequeños negocios. |
| Referencias | Tiempos máximos de alta (flujo, etapa 4), bloques B08 y B10 (lectura de la foto del cuaderno con revisión del dueño), R3, R2. |
| Modelo | Ligero. Estándar (visión) solo para leer la foto del cuaderno, si el Ligero no alcanza. Nunca Avanzado. |
| Autonomía máxima | A3 en cada alta. Como función siempre disponible, necesita la aprobación A4 del CEO y una cuota de Edith. |
| Herramientas | Funciones de alta de la plataforma, solo para el negocio que se da de alta. |
| Qué NO puede hacer | Guardar un dato sin que el dueño lo confirme. Cargar deudas de terceros sin el aviso de privacidad aceptado. Dar un precio o un descuento fuera de la tabla. Activar el cobro. |
| Costo por uso | Llamadas de IA por alta (sobre todo la foto del cuaderno). Sin medir. Edith lo suma al costo de instalación. |
| Cómo se mide | Minutos de alta a distancia por tramo, frente al máximo (45 min, 1 h y 1.5 h). Altas que terminan sin persona. Datos corregidos por el dueño en la primera semana. |

---

#### 7 · Triaje de incidencias y vigilancia de la plataforma

| Campo | Detalle |
|---|---|
| Tipo, nivel, dónde | Interno · N3 · Yizi Solutions |
| Reporta a | Karen. Vision en lo técnico. |
| Momento y prioridad | Al llegar a 50 · Media. En los pilotos, el CEO lo hace a mano. Con 50 negocios, un defecto toca a todos a la vez. |
| Hueco que cubre | Nuevo. Etapa 6 (gravedad y tiempo de respuesta), sección B (respaldo y vuelta atrás), T-15 y T-19. |
| Qué decide | La gravedad de cada incidencia, con una tabla escrita por Vision. Si un grupo de consultas pequeñas es el mismo problema. Si el respaldo de la noche y la prueba de aislamiento salieron bien. |
| Qué escala | A Vision y al CEO, de inmediato: caída, posible fuga entre negocios o pérdida de datos. A Karen: patrones repetidos, para un cambio de corrección. |
| Experiencia que representa | Una persona de soporte de segundo nivel con práctica de guardia de sistemas (operación de plataformas). |
| Referencias | R4 (ITIL 4, gestión de incidentes), spec `calidad` (respaldo diario, simulacro de restauración, defectos después de archivar). Libro *Site Reliability Engineering* de Google: **no verificado en esta consulta.** |
| Modelo | **Ligero** para leer alertas y resultados de la noche. Estándar para el informe de un incidente grave. |
| Autonomía máxima | A3: clasifica, escribe el informe y propone el cambio de corrección a Karen. **No A4.** El sistema manda las alertas. El agente las revisa en sesión. |
| Herramientas | Read, Grep, Glob. Bash de solo lectura sobre registros de errores, B12 y el informe del respaldo. Datos de un negocio: solo con permiso del dueño, y queda en B12. |
| Qué NO puede hacer | Desplegar, volver a una versión anterior, restaurar un respaldo ni borrar. Hablar con dueños (redacta borradores para la persona de soporte). Avisar a una autoridad. |
| Costo por uso | Una sesión corta por día hábil, o por incidencia. Sin medir. Si el uso crece, Edith decide. |
| Cómo se mide | Incidencias con gravedad asignada en menos de un día hábil: 100 %. Respaldos revisados: todos los días. Simulacro de restauración con evidencia: el que fije Vision. Incidencias repetidas sin cambio de corrección: 0. |

---

#### 8 · Evaluador de las conversaciones del Guía

| Campo | Detalle |
|---|---|
| Tipo, nivel, dónde | Interno · N3 · Yizi Solutions |
| Reporta a | Karen. Envía hallazgos de voz a Jarvis y de seguridad a Vision. |
| Momento y prioridad | Al llegar a 143 · Media. Antes, el analista revisa una muestra pequeña. |
| Hueco que cubre | Nuevo. Nadie revisa la calidad de El Guía Yizi en producción. |
| Qué decide | Si una muestra de conversaciones cumple la guía: sin promesas falsas, sin jerga, sin nombres internos, paso a una persona cuando tocaba. |
| Qué escala | A Vision: cualquier intento de inyección de instrucciones o dato de otro negocio en una respuesta. A Karen: flujos que fallan seguido. |
| Experiencia que representa | Una persona de control de calidad de un centro de atención al cliente. |
| Referencias | R2 (OWASP), R9 (NIST), guía de escritura, spec `comunicacion`. |
| Modelo | **Ligero** para marcar casos. Estándar para el informe del mes. |
| Autonomía máxima | A2: lee y reporta. |
| Herramientas | Read y Grep sobre una muestra **sin datos personales** (sin nombres, apodos ni fotos). |
| Qué NO puede hacer | Cambiar flujos ni textos (propone). Ver conversaciones con datos personales. Hablar con dueños. |
| Costo por uso | Una sesión por semana. Sin medir. |
| Cómo se mide | Conversaciones revisadas por semana. Errores graves del Guía por cada 1,000 conversaciones (meta: bajar). Hallazgos convertidos en cambios. |

---

#### 9 · Planificador de campo

| Campo | Detalle |
|---|---|
| Tipo, nivel, dónde | Interno · N3 · Yizi Solutions |
| Reporta a | Karen. Sirve al líder de zona y a los promotores (personas). |
| Momento y prioridad | Al llegar a 143 · Baja. Con un solo promotor, la ruta la decide él. |
| Hueco que cubre | IA-8, ya sin guiones (Jarvis) ni análisis del "no" (analista). |
| Qué decide | Propone rutas por zona y jornadas de alta presencial de al menos 5 negocios. Propone a quién volver a visitar. |
| Qué escala | Al líder de zona: el reparto final de zonas entre personas. |
| Experiencia que representa | Un coordinador de ventas de campo de una distribuidora de consumo masivo. |
| Referencias | Perfil del Promotor (`equipo/perfil-promotor-de-barrio.md`), registro de visitas (T-8), regla de jornadas por zona (flujo, etapa 4). Sin norma externa. |
| Modelo | **Ligero.** Estándar solo para el plan del mes. |
| Autonomía máxima | A3: prepara el plan. |
| Herramientas | Read, Grep, Glob sobre el registro de visitas. Write en la carpeta de campo. |
| Qué NO puede hacer | Contactar a un negocio. Enviar mensajes. Fijar metas a una persona. Evaluar a un promotor. |
| Costo por uso | Una sesión por semana. Sin medir. |
| Cómo se mide | Altas por jornada. Horas de traslado por alta. Visitas repetidas sin resultado. |

### 2.4 Al llegar a 300 negocios

No propongo tipos nuevos de agente. Propongo que el CEO revise estas tres cosas con Ultron y Edith:

1. **Más de una copia de un agente.** Por ejemplo, un analista o un triaje por zona. Es la misma ficha, con más sesiones. Edith mide si cabe en el plan.
2. **Mover al núcleo** el cierre mensual y el cumplimiento, si Yizi Publisher ya cobra o maneja datos de clientes.
3. **Un agente interno siempre encendido (A4)**, solo para el triaje y solo si los datos de 143 negocios muestran que las sesiones no alcanzan. Necesita aprobación del CEO y presupuesto de Edith.

---

## 3. Agentes del producto frente a agentes internos

**La regla: un agente es del producto o es interno. Nunca las dos cosas.**

| | Agente del producto | Agente interno |
|---|---|---|
| Ejemplo | El Guía Yizi (modos ayuda y alta guiada, y las funciones de registro y resumen que ya están en los bloques) | Consejo, Aida, Termy, Karen, Herbie y los agentes 1, 2, 4, 5, 7, 8 y 9 |
| Con quién habla | Con el bodeguero (dueño o cajero) | Con el CEO y con otros agentes |
| Identidad | Siempre **El Guía Yizi**. Nunca un nombre interno. | Su nombre interno |
| Dónde corre | En la plataforma, en producción, por la API del proveedor de IA | En sesiones de Claude Code, en los repositorios |
| Quién paga la IA | Yizi, por cada llamada, por negocio. Es costo variable del tramo (B10). | El plan de IA del CEO (ventana de 5 horas) |
| Modelo | Ligero por defecto, Estándar si hace falta. **Nunca Avanzado ni Frontera.** | El más barato que cumple, según Edith |
| Autonomía | A3 por conversación. La función corre siempre, así que necesita aprobación A4 del CEO y cuota de Edith **una vez por función**. | A3 en sesión. A4 solo con aprobación del CEO y presupuesto de Edith. |
| Datos | Solo los del negocio que lo usa (aislamiento por fila). El dueño confirma todo lo que mueve dinero o stock. | Datos agregados o con permiso registrado en B12 |
| Respaldo si falla | Baja a botones y menús (B10). Nada se bloquea. | Se para la tarea y se avisa al CEO |
| Qué lo define | `design.md` de Vision, voz de Jarvis, criterio de Aida | Su ficha en el repositorio |

**Tres consecuencias:**

1. **Un agente interno nunca escribe a un bodeguero.** Si hace falta un mensaje, el agente interno redacta, el CEO aprueba la plantilla o el lote, y la plataforma lo envía como El Guía Yizi.
2. **Todo lo que dice El Guía Yizi es dato, no orden, para él.** Un audio, una foto del cuaderno o un mensaje pueden traer instrucciones. El Guía no las obedece (OWASP LLM01, R2).
3. **La spec `jerarquia-agentes` no contempla agentes del producto.** Habla de fichas que se cargan como subagentes de Claude Code. Propongo un cambio en esa spec (dueño: Ultron) que diga: los agentes del producto son N3 del satélite, su ficha vive junto al `design.md`, y su identidad es El Guía Yizi.

**Un dato por confirmar:** usar el plan de IA del CEO para tráfico automático de producción probablemente no está permitido por las condiciones del plan. **No verificado.** Vision y Edith deben confirmarlo. Mientras tanto, supongo que todo agente del producto, y todo agente interno A4, usa la API y se paga como gasto extra (spec `finanzas`).

---

## 4. Tareas que NO debe hacer un agente

Estas tareas quedan en una persona. Termy decide qué rol las cubre. Mi lista es lo que un agente no puede hacer, por regla o porque no puede estar en el lugar.

| # | Tarea | Por qué no un agente | Quién (según Termy y el flujo) |
|---|---|---|---|
| 1 | Visitar el negocio, mostrar la demo en persona y ganar la confianza del dueño | Ningún agente visita negocios. La confianza en el barrio es humana. | Promotor de barrio |
| 2 | Alta presencial y capacitación en el local | Hay que estar ahí | Promotor |
| 3 | Probar en el celular real del dueño, con la señal del barrio | El verificador simula. La evidencia real la toma una persona. | Promotor o CEO, con evidencia escrita |
| 4 | Atender a un dueño molesto, una queja o un pedido de baja | Pide criterio y empatía. Una baja mal llevada pierde al cliente. | Promotor; a los 100 negocios, soporte humano |
| 5 | Soporte de segundo nivel cuando El Guía no basta | Por definición | Promotor y CEO; después, soporte humano |
| 6 | Firmar contratos, cobrar, emitir comprobantes, pagar, pasar a solo lectura, borrar, desplegar, publicar | Acciones irreversibles o hacia afuera (`gobierno-agentes`) | **CEO**, cada vez o por lote aprobado (sección 5) |
| 7 | Confirmar que el dinero llegó a la cuenta | Ningún agente tiene acceso al banco (permisos mínimos) | CEO |
| 8 | Dar asesoría legal o tributaria | Un agente no es abogado ni contador | Abogado y contador (externos) |
| 9 | Decidir si se avisa de una fuga de datos a una autoridad o a los afectados | Decisión legal con efectos hacia afuera | CEO con el abogado |
| 10 | Contratar, evaluar y dar retroalimentación a una persona | Termy recomienda; decidir sobre personas es humano | CEO; después, líder de zona |
| 11 | Pedir el consentimiento escrito para un testimonio | Lo da una persona a otra persona | Promotor o CEO |
| 12 | Repartir zonas y fijar metas a los promotores | Afecta el ingreso de una persona | Líder de zona; hoy, CEO |
| 13 | Contactar a los deudores de un bodeguero | Descartado por defecto. Riesgo legal de cobranza (R7). | Nadie. Solo el dueño, si quiere. |

**Para Termy:** las tareas 4 y 5 son el disparador del rol de soporte separado. El agente 3 (Guía en modo ayuda) baja ese volumen, pero **no sabemos cuánto**. Los pilotos lo dicen. Sugiero que Termy use dos señales para su disparador de unos 100 negocios: las horas de soporte humano por semana y el porcentaje que El Guía resuelve solo.

---

## 5. Riesgos y la regla de aprobación por lote

### 5.1 Riesgos

| Riesgo | Qué pasa | Qué propongo |
|---|---|---|
| **Costo de IA del producto** | Cada consulta de ayuda y cada alta gastan llamadas de IA y mensajes. Los supuestos de cuota de Edith no los separan. En el tramo 1, el margen ya es justo. | Escalera de B10 con botones primero. Cuota por negocio. Cada función del producto declara su costo por uso antes de activarse. Edith decide si la ayuda va dentro de la cuota del tramo. |
| **Costo de IA interno** | Más agentes significa más sesiones en el plan del CEO. Las sesiones compiten con el trabajo de construir. | Pocos agentes. Ligero para lo mecánico. Las cifras las calcula un script, no la IA. Sesiones fijas y agrupadas (por ejemplo, el analista los lunes). Edith registra el consumo por agente. |
| **Ventana de 5 horas** | Un cierre de mes o una caída pueden caer en una ventana casi agotada. | El trabajo que no puede esperar (cobro, alerta, respaldo) es del sistema, no de una sesión. Con la ventana justa: primero el triaje de incidentes graves, después lo demás (regla 7). |
| **Autonomía A4** | Los agentes del producto corren siempre. Si algo sale mal, sale mal a todos los negocios a la vez. | Una aprobación A4 del CEO por función, con cuota de Edith, un interruptor para apagar la IA (baja a botones) y revisión mensual. **Ningún agente interno en A4 antes de 143 negocios.** |
| **Inyección de instrucciones** | Un audio, una foto o un texto del cliente intentan dar órdenes al Guía. | El Guía no tiene herramientas que muevan dinero ni datos de otro negocio. Todo lo importante pide confirmación del dueño. El evaluador (agente 8) busca estos casos. |
| **Datos personales de deudores** | Nombres, apodos y fotos de terceros, en manos de agentes. | Los agentes internos trabajan con datos agregados. Todo acceso a un negocio pide permiso y queda en B12. El proveedor de IA no entrena con los datos (por verificar en cada contrato). |
| **Demasiados agentes** | Cada ficha se revisa cada trimestre. Más fichas, más trabajo y más cruces. | 9 agentes en tres momentos, no todos juntos. Tareas de una sola vez, con ejecutores N4. |
| **Independencia del verificador** | Si el verificador depende de Vision, la verificación pierde valor. | Reporta a Ultron. Un desacuerdo con Vision va al CEO. |

### 5.2 La regla de aprobación por plantilla o por lote: mi opinión

**La apoyo.** Sin ella, a 143 negocios el CEO confirma cientos de acciones al mes, y Yizi se detiene. Pero hoy choca con la spec `gobierno-agentes`: "una aprobación no se extiende a otra acción". Por eso necesita un cambio OpenSpec en esa spec. Sugiero tamaño L, porque cambia una regla del núcleo. Ultron decide.

**Ocho condiciones:**

1. **El CEO aprueba por escrito cuatro cosas juntas:** la plantilla, la regla (a quién aplica), un tope (cantidad o monto) y una fecha de fin. Queda en `consejo.md`.
2. **El CEO confirma cada lote**, con la lista y el total. No confirma cada mensaje. Lo que no cumple la regla va aparte, uno por uno.
3. **El borrado de datos nunca va en lote.** Siempre es una confirmación por negocio, después de ofrecer la exportación.
4. **Pasar a solo lectura sí puede ir en lote**, porque se puede deshacer cuando el dueño paga. Pero los primeros casos van uno por uno, para aprender.
5. **Un agente no puede cambiar la plantilla ni la regla.** Cualquier cambio es una aprobación nueva.
6. **Freno automático.** Si el lote se sale de lo normal (por ejemplo, el doble de morosos que el mes anterior), el agente para y avisa. No lo presenta como un lote normal.
7. **Rastro completo.** Cada lote queda registrado: quién lo aprobó, cuándo, qué incluía y qué pasó con cada caso.
8. **En los pilotos no hay lotes.** El CEO confirma cada acción. Así se aprende qué reglas hacen falta.

**Sobre los mensajes dentro de una función ya aprobada** (por ejemplo, el resumen nocturno): estoy de acuerdo con Ultron en que son parte del producto, y no una acción nueva. Con una condición: el `design.md` de la función debe listar cada tipo de mensaje, y el dueño debe haber aceptado recibirlos. Un tipo de mensaje nuevo es una aprobación nueva. El CEO debe confirmar esta lectura por escrito.

---

## 6. Referencias

Fecha de consulta de todas: **2026-11-18.** Fuentes consultadas por Aida en la web. Ninguna reemplaza la opinión del abogado ni del contador.

| # | Referencia | Estado | Fuente |
|---|---|---|---|
| R1 | ISO/IEC 25010:2023, modelo de calidad de producto (9 características). Reemplaza a la edición de 2011. | Verificado: existencia, edición y fecha (15 de noviembre de 2023). Nombres de las 9 características: **no verificado** en la fuente oficial. | [iso.org](https://www.iso.org/standard/78176.html) |
| R2 | OWASP Top 10 para aplicaciones con LLM, edición 2025. LLM01: inyección de instrucciones; LLM10: consumo sin límite. Ya existe una edición 2026. | Verificado (página oficial). La edición 2026 no se revisó. | [genai.owasp.org](https://genai.owasp.org/resource/owasp-top-10-for-llm-applications-2025/) |
| R3 | Anthropic, "Building effective agents" (19 de diciembre de 2024). Recomienda patrones simples y flujos fijos antes que agentes libres. | Verificado | [anthropic.com](https://www.anthropic.com/engineering/building-effective-agents) |
| R4 | ITIL 4, práctica de gestión de incidentes (guía revisada en 2023, PeopleCert y Axelos). | Verificado: existencia y revisión de 2023. El texto de la guía es de pago: **no revisado.** | [peoplecert.org](https://peoplecert.org/news-and-announcements/2023/itil-4-management-practices-2023) |
| R5 | Ley 29733, Ley de Protección de Datos Personales (Perú). | Verificada su existencia. Qué obligaciones aplican a Yizi: **no verificado.** | [gob.pe (ANPD)](https://www.gob.pe/institucion/anpd/normas-legales/6554453-16-2024-jus) |
| R6 | Reglamento de la Ley 29733, D.S. 016-2024-JUS. Publicado el 30 de noviembre de 2024. Vigente desde el 30 o el 31 de marzo de 2025 (las fuentes difieren). Derogó el D.S. 003-2013-JUS. | Verificado (fuentes oficiales y secundarias) | [congreso.gob.pe](https://www.congreso.gob.pe/Docs/DGP/DIDP/files/ds_016-2024-jus.pdf) · [El Peruano](https://www.elperuano.pe/noticia/266995-minjusdh-el-lunes-31-regira-nuevo-reglamento-de-ley) |
| R7 | Ley 29571, Código de Protección y Defensa del Consumidor, artículos 61 y 62 (métodos abusivos de cobranza; por ejemplo, difundir la condición de moroso). | Verificado en fuentes secundarias. Texto oficial vigente: **no revisado.** | [lpderecho.pe](https://lpderecho.pe/prohibir-llamadas-recordatorio-pago-antes-vencimiento-deuda/) · [lacamara.pe](https://lacamara.pe/reglas-basicas-del-codigo-de-consumo/) |
| R8 | SUNAT, R.S. 097-2012/SUNAT (emisión electrónica desde los sistemas del contribuyente) y sus cambios posteriores. | Verificado: existencia y que sigue citada en 2026. Si aplica al RUC 10 del CEO: **no verificado** (lo confirma el contador). | [sunat.gob.pe](https://www.sunat.gob.pe/legislacion/oficios/2016/informe-oficios/i065-2016.pdf) |
| R9 | NIST AI RMF 1.0 (NIST AI 100-1) y su perfil de IA generativa (NIST AI 600-1, julio de 2024). Guía voluntaria, no ley. | Verificado: existencia y fecha. Contenido detallado: **no revisado.** | [nist.gov](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence) |
| — | Política de WhatsApp Business sobre aceptación de mensajes | **No verificado** | — |
| — | Programa ISTQB de nivel básico | **No verificado** | — |
| — | Libro *Site Reliability Engineering* (Google) | **No verificado** en esta consulta | — |
| — | Que el plan de IA del CEO no permita tráfico automático de producción | **No verificado.** Lo confirman Vision y Edith. | — |

---

## 7. Qué sigue

Decisiones para el CEO, por prioridad:

1. **Aprobar o ajustar este mapa.** Es la base de los cambios que siguen.
2. **Elegir los nombres** de los agentes 1, 2 y 3 (los de antes de los pilotos). Deben ser únicos en todo Yizi.
3. **Aprobar que Aida proponga el cambio del verificador independiente** (núcleo, N1 de área). Es el más urgente: sin él no se archiva la Oleada 1.
4. **Pedir que el modo ayuda mínimo y el analista** entren en el cambio `paquete-base-barrio` (Ultron y Karen), en vez de ser cambios aparte.
5. **Aprobar el cambio "completar fichas"** (referencias, costo por uso y herramientas de Vision y Ultron; dueño del Diagnóstico Flash).
6. **Decidir si la regla de aprobación por lote** entra como cambio en `gobierno-agentes`, con las 8 condiciones de la sección 5.2.
7. **Pedir a Vision y a Edith** que confirmen cómo se paga la IA del producto (API o plan) y si la ayuda cabe en la cuota de cada tramo.
