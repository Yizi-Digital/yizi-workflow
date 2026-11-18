---
name: yizi-pendientes
description: Entrega al CEO de Yizi la lista de sus pendientes y la ruta de todos sus documentos, en formato corto y simple. Úsalo cuando el CEO diga "DAME MIS PENDIENTES", "mis pendientes", "qué me falta" o "dónde están mis documentos".
license: Propietaria · Yizi Digital
metadata:
  author: yizi-digital
  version: "1.0"
  nucleo: yizi-workflow
---

Responde con los pendientes del CEO y las rutas de sus documentos.

## Pasos

1. Lee `ceo/pendientes.md` del núcleo (yizi-workflow).
2. Revisa si algo cambió desde la última actualización:
   - pull requests ya fusionados o cerrados;
   - decisiones nuevas en `yizi-solutions/catalogo/decisiones-ceo.md`;
   - documentos nuevos en los repositorios.
3. Si algo cambió, actualiza `ceo/pendientes.md` antes de responder.
4. Responde con este formato, sin texto de más:

```
## Mis pendientes
### Decidir
- …
### Fusionar
- …
### Hacer yo
- …
### Rutina
- …

## Mis documentos
| Qué | Ruta |
```

## Reglas

- Lenguaje simple (guía de escritura del núcleo). Sin explicaciones largas.
- Lo más urgente primero.
- Las rutas son `repositorio/archivo`. Si no está fusionado, indica la rama.
- No inventes pendientes: solo lo que esté en el archivo, en las decisiones o en los pull requests.
