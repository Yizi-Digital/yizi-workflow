# Tasks

## 1. Registro y fichas [Viernes]

- [x] 1.1 Renombrar los satélites del registro a `yizi-solutions`, `yizi-growth` y `yizi-talent` (Yizi Solutions, Yizi Growth, Yizi Talent), con líderes aprobados y el repo de Solutions
- [x] 1.2 Quitar el "significado Yizi" de las cinco fichas y actualizar el satélite que patrocina cada directivo
- [x] 1.3 Verificar que no quedan referencias a los nombres antiguos fuera del historial archivado

## 2. Skill y documentación [Ultron, Jarvis]

- [x] 2.1 Actualizar `yizi-satelite` para que el repo remoto sea `Yizi-Digital/<id>` y pida confirmación al CEO
- [x] 2.2 Actualizar `README.md` y `AGENTS.md` con los nombres en inglés y la regla de un repo por satélite
- [x] 2.3 Verificar que el plugin sigue pasando `claude plugin validate`

## 3. Consumo de IA [Edith]

- [x] 3.1 Crear `finanzas/consumo-ia.md` con la tabla mensual y las reglas de la ventana de 5 horas
- [x] 3.2 Añadir la regla de la ventana de 5 horas a la ficha de Edith y a `CLAUDE.md`

## 4. Génesis de Yizi Solutions [Ultron, Vision]

- [x] 4.1 Generar `../yizi-solutions` desde `satelites/plantilla/` sin marcadores pendientes
- [x] 4.2 Inicializar OpenSpec y comprobar con `openspec doctor` que ve el núcleo `yizi-workflow`
- [x] 4.3 Hacer el primer commit del satélite en la rama `main`
- [x] 4.4 Subir a `Yizi-Digital/yizi-solutions` cuando el repositorio exista (requiere al CEO)

## 5. Verificación y archivo [Ultron]

- [x] 5.1 Registrar los veredictos en `consejo.md`
- [x] 5.2 Ejecutar `openspec validate satelites-repos-y-consumo-ia --strict` sin errores
- [x] 5.3 Sincronizar las specs vigentes con el delta (sin archivar) y verificar con `openspec validate --specs --strict`
- [x] 5.4 Cuando 4.4 esté hecha, archivar con `openspec archive satelites-repos-y-consumo-ia --skip-specs` (las specs ya están sincronizadas)
