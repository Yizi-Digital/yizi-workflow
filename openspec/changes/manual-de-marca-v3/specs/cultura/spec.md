# Spec Delta

## MODIFIED Requirements

### Requirement: Misión y visión vigentes
La misión y la visión del grupo SHALL ser las del Manual de Marca v3.0 (`marca/manual-de-marca.md`), y la misión y visión v2.0 SHALL seguir vigentes como las de Yizi Solutions. Los agentes MUST citarlas sin reinterpretarlas:
- Misión del grupo: hacer fácil lo complejo: llevar tecnología, talento y marketing de alto nivel a negocios de todos los tamaños, para que dejen el caos operativo atrás y manejen su operación con sistemas ágiles, automatizados y sencillos de usar.
- Visión del grupo: ser el grupo que impulsa a negocios y mercados a vender más y operar mejor, con soluciones, equipos y productos propios que funcionan con fluidez, sin que el dueño pierda el control de su operación.

#### Scenario: Un agente redacta un documento que menciona la misión
- **WHEN** un agente escribe una propuesta, presentación o documento interno que menciona la misión o la visión
- **THEN** usa el texto vigente de esta spec y no una versión inventada

#### Scenario: Alguien quiere cambiar la misión
- **WHEN** un agente o persona propone modificar la misión o la visión
- **THEN** el cambio se tramita como un cambio OpenSpec de tipo `estrategico` y tamaño `L`
- **AND** solo entra en vigor cuando el CEO lo aprueba

#### Scenario: Documento de Yizi Solutions
- **WHEN** un agente redacta un documento propio de Yizi Solutions
- **THEN** puede usar la misión y visión v2.0, que son las de ese satélite
