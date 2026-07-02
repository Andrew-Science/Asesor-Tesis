# Banco de Repetición Espaciada — Estado Persistente

> Archivo de referencia legible para humanos. **La fuente de verdad real es `progreso/srs-state.json`**, gestionada por el motor `motor/sm2_engine.py` (algoritmo SM-2 real, no una tabla fija). Este archivo se regenera como resumen después de cada sesión — no editar directamente los intervalos aquí, editar vía el motor.

## Cómo funciona el motor (SM-2, Wozniak 1987)

Cada ítem tiene un **easiness factor (EF)** individual que empieza en 2.5 y sube o baja según el desempeño real del estudiante en cada revisión (calidad 0-5, donde <3 = fallo). El intervalo hasta el próximo repaso se calcula como `intervalo_anterior × EF`, no con una tabla fija de días — dos estudiantes (o dos ítems distintos del mismo estudiante) divergen con el tiempo según su dificultad real. Esto es lo que hace el sistema adaptativo en vez de estático.

```
# Agregar un ítem nuevo detectado en sesión
python3 motor/sm2_engine.py add --state progreso/srs-state.json --lang ingles \
  --id "tercer_condicional_doble_aux" --text "If I had studied... (no had have)" \
  --origin "interferencia L1 - hipercorrección"

# Registrar una revisión (quality: 0=falló completamente, 3=correcto con esfuerzo, 5=perfecto)
python3 motor/sm2_engine.py review --state progreso/srs-state.json --lang ingles \
  --id "tercer_condicional_doble_aux" --quality 4

# Ver qué está vencido hoy (calentamiento de la sesión)
python3 motor/sm2_engine.py due --state progreso/srs-state.json --lang ingles
```

## Reglas de uso durante la sesión

- Al **inicio de sesión**: ejecutar `due` para el idioma activo — esos ítems son el calentamiento de recuperación activa obligatorio (Módulo VII)
- Cada vez que se detecta un ítem nuevo (vocabulario, patrón de error, estructura): `add` inmediatamente, con la **codificación elaborativa** (Módulo IV) en `--origin`
- Cada vez que se revisa un ítem existente en la sesión (el estudiante lo recupera con o sin éxito): `review` con la calidad observada — esto es lo que hace que el modelo "aprenda" tu curva de olvido real, ítem por ítem
- Al **cierre de sesión**: regenerar el resumen humano abajo a partir de `srs-state.json` (vía `list`) para que quede legible sin tener que parsear JSON

## Resumen legible (regenerar al cierre de cada sesión)

*(Vacío hasta la primera sesión — se llena con la salida de `python3 motor/sm2_engine.py due --state progreso/srs-state.json`)*

| Idioma | Ítem | EF actual | Próximo repaso |
|---|---|---|---|
