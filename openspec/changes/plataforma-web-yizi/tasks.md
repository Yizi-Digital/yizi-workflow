# Tasks

> Reglas de todo el cambio:
> - Nada se construye sin la aprobación del CEO de este plan (regla 1). Nada se publica, fusiona en `main` ni se paga sin su confirmación (regla 2).
> - Cada tarea dura como máximo medio día. Formato: `[dueño · modelo]`. Modelos: Sonnet (Estándar) para construir, Haiku (Ligero) para lo mecánico. Nunca Fable.
> - Quien construye no verifica: verifica Lince al cerrar cada fase.
> - Si la ventana de 5 horas está justa, trabaja un agente a la vez.
> - **Regla de pausa:** si el CEO pierde horas de los pilotos de Solutions, la web se pausa.
> - Las fases 1 a 3 son la primera versión publicable. Si el CEO elige la opción B, solo se hacen 3.1 a 3.3 y 3.6.
> - Todo texto legal va marcado "requiere revisión de abogado colegiado".

## 0. Preparación del CEO

- [ ] 0.1 Decidir el alcance: A (sitio de 9 páginas por fases) o B (una página) [CEO]
- [ ] 0.2 Elegir y comprar el dominio .com, comparando 2 o 3 registradores por renovación [CEO, Edith asesora]
- [ ] 0.3 Crear el repo `Yizi-Digital/yizi-web` (público o privado) y el equipo de Vercel [CEO]
- [ ] 0.4 Elegir el WhatsApp Business y el correo del negocio, con alias [CEO]
- [ ] 0.5 Decidir qué busca de los inversionistas y si hay inglés [CEO]
- [ ] 0.6 Aprobar Astro como desviación del stack (D2) [CEO]
- [ ] 0.7 Confirmar el tope de gasto con cotizaciones reales [CEO, Edith · Haiku]
- [ ] 0.8 Registrar las decisiones en `ceo/estado-actual.md` [Ultron · Haiku]
- [ ] 0.9 Verificar la fase 0 [Lince · Sonnet]

## 1. Base técnica

- [ ] 1.1 Crear el proyecto Astro con una página de prueba, `AGENTS.md` y `CLAUDE.md` cortos que apuntan al núcleo [Vision · Sonnet]
- [ ] 1.2 Configurar la CI: Lighthouse CI con presupuestos, axe, prueba sin JavaScript, gitleaks y `npm audit` [Vision · Sonnet]
- [ ] 1.3 Poner las cabeceras de seguridad en `vercel.json` y medir con HTTP Observatory [Vision · Sonnet]
- [ ] 1.4 Proteger `main` y activar Dependabot [CEO, con la guía de Vision]
- [ ] 1.5 Corregir la sección 6.4 del manual de marca con un cambio de marca aparte (proyectos MACRO y nombre público) [Jarvis · Sonnet]
- [ ] 1.6 Verificar la fase 1 con evidencia de CI y vista previa [Lince · Sonnet]

## 2. Sistema de diseño

- [ ] 2.1 Ajustar la narrativa: nombre "Productos propios de Yizi", sin `[dato pendiente]` abiertos y sin nombres internos [Jarvis · Sonnet]
- [ ] 2.2 Escribir `tokens.css` con colores, tipografías alojadas y la regla del Ámbar [Vision · Sonnet]
- [ ] 2.3 Construir los componentes: botones, tarjetas, navegación y etiquetas de estado [Vision · Sonnet]
- [ ] 2.4 Añadir animaciones con CSS y la regla de movimiento reducido [Vision · Sonnet]
- [ ] 2.5 Hacer la página de componentes y pasar axe y la lista manual [Vision · Sonnet]
- [ ] 2.6 Revisar marca: colores, tipografías, logo y maquetas marcadas [Jarvis · Sonnet]
- [ ] 2.7 Verificar la fase 2 [Lince · Sonnet]

## 3. Páginas en español (primera versión publicable)

- [ ] 3.1 Inicio con las 7 pantallas, voz cliente e inversionista según la narrativa [Vision construye, Jarvis textos · Sonnet]
- [ ] 3.2 Página de Yizi Solutions, sin precios, con la invitación al Diagnóstico Flash [Vision, Jarvis · Sonnet]
- [ ] 3.3 Etiquetas de estado leídas de `satelites/registro.yaml` [Vision · Sonnet]
- [ ] 3.4 Páginas de Publisher, Productos propios y Talent, con "Próximamente" y sin oferta [Vision, Jarvis · Sonnet]
- [ ] 3.5 Páginas Nosotros e Inversionistas, sin cifras ni montos [Vision, Jarvis · Sonnet]
- [ ] 3.6 Contacto con WhatsApp y correo del negocio, y página de Privacidad en borrador [Vision, Jarvis · Sonnet]
- [ ] 3.7 Revisar cada texto contra "Qué NO se dice" y la lista de datos pendientes [Jarvis · Haiku]
- [ ] 3.8 Revisar la regla 6 y el encuadre para inversionistas [Viernes · Sonnet]
- [ ] 3.9 Confirmar costos reales de dominio, correo y Vercel [Edith · Haiku]
- [ ] 3.10 Probar en celular real con red lenta y guardar pasos, resultado y fecha [Vision · Sonnet]
- [ ] 3.11 Verificar la fase 3 [Lince · Sonnet]

## 4. Formulario y analítica

- [ ] 4.1 Construir la función del formulario con validación, consentimiento y respaldo por WhatsApp [Vision · Sonnet]
- [ ] 4.2 Añadir anti-spam: campo trampa, tiempo mínimo y límite por red [Vision · Sonnet]
- [ ] 4.3 Probar envío con y sin JavaScript, error del proveedor, casilla sin marcar y campo trampa [Vision · Haiku]
- [ ] 4.4 Activar Vercel Web Analytics sin eventos con datos personales [Vision · Haiku]
- [ ] 4.5 Cotizar el proveedor de correo [Edith · Haiku]
- [ ] 4.6 Revisar consentimiento, flujo de datos fuera del Perú e inscripción del banco de datos [Abogado]
- [ ] 4.7 Verificar la fase 4 [Lince · Sonnet]

## 5. Inglés (opcional)

- [ ] 5.1 Preparar los textos en inglés de las páginas que elija el CEO [Jarvis · Sonnet]
- [ ] 5.2 Construir `/en/` con `hreflang` y las mismas metas [Vision · Sonnet]
- [ ] 5.3 Revisión humana de la traducción [Jarvis]
- [ ] 5.4 Verificar la fase 5 [Lince · Sonnet]

## 6. Producción

- [ ] 6.1 Abogado: revisar datos del proveedor, privacidad, Libro de Reclamaciones, texto de inversionistas, aviso de IA y promesas [Abogado]
- [ ] 6.2 Revisar la marca "Yizi" ante Indecopi [Viernes con el abogado]
- [ ] 6.3 Lista final firmada: metas, seguridad, textos aprobados y aviso revisado [Lince · Sonnet]
- [ ] 6.4 El CEO fusiona en `main` y conecta el dominio, cada paso con su confirmación [CEO]
- [ ] 6.5 Revisar producción después de publicar y registrar el resultado [Lince · Sonnet]
- [ ] 6.6 Actualizar `ceo/estado-actual.md` y `ceo/pendientes.md` [Ultron · Haiku]
- [ ] 6.7 Medir 3 señales: consultas de clientes, consultas de inversionistas y tiempo hasta la primera venta [Jarvis, Edith · Haiku]
