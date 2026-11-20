# Reuniones por voz con los agentes · Costo de Edith

| Campo | Valor |
|---|---|
| Autora | Edith (CFO) |
| Fecha | 2026-11-20 |
| Base | `agentes/reuniones-por-voz/investigacion-vision.md` (sección 4, precios) |
| Estado | Estimación. Nada se compró ni se construyó. Consumo real: sin medir. |
| Moneda | USD (los precios de origen están en USD; el CEO no fijó otra moneda) |

## 1. Respuesta corta

1. Las opciones 1 y 2 no cuestan nada aparte del plan de IA del CEO. Sí gastan uso del plan y de la ventana de 5 horas.
2. La opción 3 cuesta entre **18 y 37 USD al mes** para 4 reuniones de 30 minutos por semana. Se paga aparte del plan.
3. La opción 4 cuesta lo de la opción 3 más un servidor cuyo precio **no está verificado**.
4. Recomiendo: fase 0 y fase 1 ya, con tope de 0 USD. Piloto de la opción 3 solo después, con tope de 30 USD al mes y 3 USD por reunión.

## 2. Supuestos

Todos son supuestos, no datos medidos. Se corrigen con el piloto.

| # | Supuesto | Valor |
|---|---|---|
| S1 | Reuniones | 4 por semana, 30 minutos cada una. 4,33 semanas por mes = **17 reuniones al mes** (8,5 horas) |
| S2 | El CEO habla | 12 de los 30 minutos (40 %) |
| S3 | Turnos del CEO por reunión | 15 |
| S4 | Agentes que responden por turno | 2 en promedio = **30 respuestas por reunión** |
| S5 | Largo de cada respuesta | 80 palabras (tope del modo reunión), unos 150 tokens y 480 caracteres en español |
| S6 | Voz por reunión | 30 × 480 = **14 400 caracteres** (unos 16 minutos de audio) |
| S7 | Contexto por llamada de agente | 12 000 tokens fijos (ficha + specs, en caché) + 4 000 tokens nuevos (historial de la reunión) |
| S8 | Escrituras de caché | 5 agentes × 2 veces por reunión (la caché vence si un agente calla un rato) = 10 escrituras |
| S9 | Precio de escribir en caché | 1,25 veces el precio de entrada. **No verificado** (Vision no lo leyó; lo confirmo en la página de precios antes del piloto) |
| S10 | Moderador (Ultron) | 1 llamada por turno: 5 000 tokens de entrada, 50 de salida |
| S11 | Acta final | 1 llamada Sonnet 5.5: 10 000 de entrada, 800 de salida |
| S12 | Voz a texto | 0,003 USD por minuto. **No verificado** (Vision da el precio por token de audio, no por minuto) |

## 3. Costo mensual por opción

| Opción | Costo aparte del plan (USD/mes) | Qué consume del plan del CEO | Trabajo para construir |
|---|---|---|---|
| 1 · App de Claude, modo de voz | **0** | Cada reunión cuenta en los límites del plan (fuente: support.claude.com, 2026-11-20) | Ninguno |
| 2 · Claude Code + `/voice` + hook | **0** (dictado sin costo y fuera de `/usage`; voz del sistema operativo gratis. Fuente: code.claude.com/docs/en/voice-dictation, 2026-11-20) | Cada respuesta y cada subagente, igual que hoy. Es la opción que más gasta del plan | Unas horas de un agente (dentro del plan) |
| 3 · App propia | **18 a 37** (detalle abajo) | Nada al usarla. Solo la construcción | 1 a 2 semanas de agentes (dentro del plan) |
| 4 · Tiempo real | **18 a 37 + servidor** (servidor: no verificado) | Nada al usarla. Solo la construcción | 3 a 6 semanas de agentes, más operación continua |

### Detalle de la opción 3 (por reunión)

| Parte | Cálculo | Agentes en Sonnet 5.5 | Agentes en Opus 5.5 |
|---|---|---|---|
| Respuestas de agentes | 30 × (12 000 caché + 4 000 nuevos + 150 salida) | 0,32 | 0,64 |
| Escrituras de caché (S8, S9) | 10 × 12 000 × entrada × 1,25 | 0,30 | 0,60 |
| Moderador en Sonnet 5.5 | 15 × (5 000 entrada + 50 salida) | 0,16 | 0,16 |
| Acta en Sonnet 5.5 | 10 000 entrada + 800 salida | 0,03 | 0,03 |
| **Claude API, subtotal** | | **0,81** | **1,43** |
| Voz a texto (S12) | 12 min × 0,003 | 0,04 | 0,04 |
| Texto a voz, Google Neural2 | 14 400 × 16 / millón | 0,23 | 0,23 |
| **Total por reunión (Google)** | | **1,08** | **1,70** |

Precios de Claude: platform.claude.com/docs/en/about-claude/pricing, verificados por Vision el 2026-11-20. Precios de voz: fuente secundaria (ver sección 4 de Vision).

### Total al mes (17 reuniones)

| Combinación | Claude API | Voz a texto | Texto a voz | **Total USD/mes** |
|---|---|---|---|---|
| Sonnet + Google Chirp 3 HD (245 000 caracteres, dentro del millón gratis) | 13,8 | 0,7 | 0 | **14,5** |
| Sonnet + Google Neural2 | 13,8 | 0,7 | 3,9 | **18,4** |
| Sonnet + ElevenLabs Flash (0,05 por 1000 caracteres) | 13,8 | 0,7 | 12,3 | **26,8** |
| Opus + Google Neural2 | 24,3 | 0,7 | 3,9 | **28,9** |
| Opus + ElevenLabs Flash | 24,3 | 0,7 | 12,3 | **37,3** |

Notas:
1. El gratuito de Chirp 3 HD viene de fuente secundaria. Si no aplica a la cuenta, esa fila sube a unos 21 USD.
2. Si el micrófono queda abierto los 30 minutos, la voz a texto sube a 1,5 USD al mes. No cambia el orden.
3. Falta el hosting de la app (servidor que guarda las claves). Precio: **no verificado**. Muchos servicios tienen capa gratis; Vision lo confirma en el diseño.
4. El consumo real puede salir el doble si las specs pesan más que 12 000 tokens. Por eso el tope lleva margen.

## 4. Qué entra en el plan y qué se paga aparte

| Parte | ¿Dentro del plan del CEO? | Nota |
|---|---|---|
| Modo de voz de la app de Claude | Sí | Cuenta en los límites del plan |
| Dictado `/voice` de Claude Code | Sí, sin gastar uso | No cuenta en `/usage` |
| Respuestas de agentes en Claude Code | Sí | Gastan uso como hoy |
| Voz del sistema operativo (`say`, `espeak`, `piper`) | No aplica | Gratis, corre en el equipo del CEO |
| Construir el hook o la app con agentes | Sí | Gasta uso del plan |
| Claude API (opciones 3 y 4) | **No** | Se cobra por token en la Consola de Claude. Si el plan trae créditos de API: no verificado |
| Voz a texto en la nube (opciones 3 y 4) | **No** | Proveedor externo, pago por uso |
| Texto a voz en la nube (opciones 3 y 4) | **No** | Proveedor externo, pago por uso |
| Servidor de medios (opción 4) | **No** | Precio no verificado |

## 5. Impacto en la ventana de 5 horas

| Opción | Impacto | Cómo lo controlo |
|---|---|---|
| 1 | Medio. Una charla de 30 minutos gasta mensajes del plan. Cifra sin medir | Medir con la página de uso antes y después de 2 reuniones |
| 2 | **Alto.** El modo reunión lanza varios subagentes. Si van en Opus y en paralelo, 2 horas por semana pueden comerse buena parte de una ventana | Agentes en Sonnet en las reuniones. Nada de reuniones en una ventana con trabajo crítico. Medir con `/usage` antes y después |
| 3 y 4 | Ninguno al usarlas (van por API). Solo la construcción gasta plan | Construir fuera de ventanas con trabajo crítico |

Regla 7: si la ventana está cerca del límite, la reunión por voz no es trabajo crítico. Se pospone o se hace con un solo agente.

## 6. Recomendación por fases y topes

| Fase | Qué | Tope de gasto aparte del plan | Condición para pasar a la siguiente |
|---|---|---|---|
| 0 (ya) | `/voice` en Claude Code y app de Claude en el celular | **0 USD** | 2 semanas de uso. Edith registra el uso por reunión en `finanzas/consumo-ia.md` |
| 1 | Hook con voz del sistema operativo, una por firma | **0 USD** | Las reuniones no agotan ventanas. El CEO dice si la calidad de voz alcanza |
| 2 (piloto, 1 mes) | Opción 3: agentes en Sonnet 5.5, moderador en el modelo más ligero que elija bien el turno (probar Haiku 5.5), Google Chirp 3 HD o Neural2 | **30 USD al mes y 3 USD por reunión**, como corte automático en la app. Crédito prepago en la Consola de Claude, sin recarga automática | Costo real medido y el CEO lo usa de verdad (al menos 12 reuniones en el mes) |
| 3 | Opción 4, tiempo real | Se define tras el piloto | Precio del servidor verificado y el piloto muestra que la charla fluida vale la pena |

Reglas del gasto:
1. Opus 5.5 y ElevenLabs solo si Sonnet o Google no dan la calidad. Cada subida la aprueba el CEO.
2. Las decisiones con cifras no se cierran en la reunión por voz. Pasan a una sesión escrita (y la regla 2 sigue: nada se aprueba por voz).
3. Yo preparo la compra del crédito prepago; el CEO la ejecuta. Ninguna clave ni dato de pago va al repositorio.
4. Retorno: es una herramienta interna, sin ingreso directo. Su retorno es tiempo del CEO. Por eso el tope es bajo. La señal de producto para clientes queda con Viernes.

## 7. Veredicto

### Edith · Costo y presupuesto
**Veredicto:** CONDICIONADO
**Costo estimado:** fases 0 y 1: 0 USD aparte del plan. Fase 2: 14 a 37 USD al mes (17 reuniones de 30 minutos), según supuestos S1 a S12.
**Motivos:**
- Las fases 0 y 1 cumplen casi todo el pedido sin gasto extra.
- El riesgo de la opción 2 es la ventana de 5 horas, no el dinero.
- La opción 3 es barata, pero sale de la caja y no tiene retorno directo.
- Dos precios clave están sin verificar: escritura de caché y voz a texto por minuto.
**Condiciones:**
1. Medir el uso del plan en la fase 0 antes de decidir la fase 1.
2. Agentes en Sonnet 5.5 durante las reuniones por voz.
3. Para la fase 2: cambio OpenSpec con Consejo, precios verificados en las páginas oficiales, tope de 30 USD al mes y 3 USD por reunión en el código.
4. La fase 3 queda bloqueada hasta tener datos del piloto.
