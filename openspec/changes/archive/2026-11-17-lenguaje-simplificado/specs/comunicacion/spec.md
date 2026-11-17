# Spec Delta

## ADDED Requirements

### Requirement: Lenguaje natural y simplificado
Todo texto de un agente o de una persona de Yizi SHALL seguir la Guía de escritura (`marca/guia-de-escritura.md`), basada en ASD-STE100 y adaptada al español: lenguaje natural y humano, palabras comunes, un término por concepto, frases cortas en voz activa, lo importante primero y listas para pasos y opciones. Los textos que no cumplan la guía MUST corregirse antes de enviarse.

#### Scenario: Respuesta de un agente al CEO
- **WHEN** un agente responde al CEO
- **THEN** la primera frase dice la respuesta o la decisión
- **AND** ninguna frase pasa de 25 palabras

#### Scenario: Texto con voz pasiva
- **WHEN** un borrador dice "el precio será validado"
- **THEN** el agente lo reescribe como "Edith valida el precio"

#### Scenario: Término técnico
- **WHEN** un texto usa una palabra técnica por primera vez
- **THEN** la explica en palabras simples o la cambia por una palabra común
