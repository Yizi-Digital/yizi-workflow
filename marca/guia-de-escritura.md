# Guía de escritura de Yizi

| Campo | Valor |
|---|---|
| Versión | 1.0 |
| Fecha | 2026-11-17 |
| Dueño | Área de marca (Jarvis) |
| Aplica a | Todos los agentes y las personas de Yizi, en el núcleo y en los satélites |
| Base | ASD-STE100 (Simplified Technical English), adaptado al español |

Todos los textos de Yizi usan un **lenguaje natural, humano y simplificado**. El objetivo es que cualquier persona entienda el texto la primera vez que lo lee, aunque tenga prisa.

ASD-STE100 es una norma para escribir inglés técnico simple. Yizi usa sus reglas principales y las aplica al español.

## 1. Las 12 reglas

### Palabras
1. **Usa palabras comunes.** Escribe "usar" y no "utilizar"; "ayudar" y no "coadyuvar".
2. **Una palabra, un significado.** Si llamas "cliente" al dueño de la bodega, no uses "cliente" para la persona que compra en la bodega. Usa "comprador".
3. **Usa siempre el mismo término para la misma cosa.** No alternes "paquete", "plan" y "kit" para lo mismo.
4. **Explica la palabra técnica la primera vez.** Ejemplo: "IGV (el impuesto a las ventas)". Si una palabra simple sirve, no uses la técnica.

### Frases
5. **Frases cortas.** Máximo 20 palabras en una instrucción. Máximo 25 palabras en una explicación.
6. **Una idea por frase.** Una instrucción por frase.
7. **Voz activa.** Escribe "Edith valida el precio" y no "el precio es validado por Edith".
8. **Di quién hace qué.** Escribe "Tú apruebas" y no "se aprueba".

### Párrafos y estructura
9. **Párrafos cortos.** Máximo 6 frases por párrafo.
10. **Lo importante, primero.** Empieza por la respuesta o la decisión. Después explica.
11. **Usa listas y tablas** para pasos, opciones y comparaciones. Numera los pasos en orden.
12. **Advertencias antes de la acción.** Escribe el riesgo antes del paso que lo causa.

## 2. Tono

- **Natural y humano.** Escribe como una persona que habla con respeto y cercanía. No escribas como un robot ni como un contrato.
- **Directo y sobrio.** Sin relleno, sin adornos, sin exageraciones.
- **Cercano.** Usa "tú" con el CEO y con los dueños de negocio, salvo que pidan "usted".
- **Honesto.** Si no sabes algo, dilo. Marca lo que no está verificado.

## 3. Ejemplos

| No escribas | Escribe |
|---|---|
| "Se procederá a la implementación de la solución una vez que se haya obtenido la aprobación correspondiente." | "Empezamos a construir cuando tú lo apruebes." |
| "Optimizamos el renderizado del menú." | "Tu menú carga al instante." |
| "La utilización de la API conlleva costos variables asociados a la mensajería." | "Cada mensaje de WhatsApp tiene un costo. Lo pagamos por mensaje." |
| "Es recomendable considerar la posibilidad de validar con el contador." | "Pregúntale a tu contador antes de firmar." |

## 4. Excepciones

- **Specs de OpenSpec:** usan las mismas reglas, pero los encabezados de estructura y las palabras SHALL y MUST quedan en inglés.
- **Código y comandos:** se escriben tal como son. Explica qué hacen en una frase simple.
- **Textos legales y tributarios:** cita el texto oficial tal como es. Después explícalo en lenguaje simple.

## 5. Revisión rápida antes de enviar

- [ ] ¿La primera frase dice lo más importante?
- [ ] ¿Alguna frase tiene más de 25 palabras?
- [ ] ¿Hay voz pasiva o "se hace" sin decir quién?
- [ ] ¿Hay palabras difíciles que puedo cambiar por palabras comunes?
- [ ] ¿Uso el mismo término para la misma cosa en todo el texto?
