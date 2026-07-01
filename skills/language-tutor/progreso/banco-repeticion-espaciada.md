# Banco de Repetición Espaciada — Estado Persistente

> Archivo vivo. Registro operativo de los intervalos definidos en `SKILL.md` Módulo IV. El Tutor de Idiomas **debe leer este archivo al inicio de cada sesión** para saber qué ítems están vencidos hoy, y **añadir/actualizar filas al cierre de cada sesión**. Sin este archivo, los intervalos de repaso (1 día, 3 días, 7 días...) son una fórmula sin ejecución real.

Formato por fila: un ítem (palabra/chunk/estructura gramatical) por línea, con su idioma, la repetición en la que va, y la fecha en que vuelve a tocar.

## Cola de Repaso Activa

| Idioma | Ítem | Tipo (léxico/gramática/pronunciación) | Repetición actual | Última exposición | Próximo repaso (fecha) | Origen (patrón de interferencia / bloque temático) |
|---|---|---|---|---|---|---|
| | | | | | | |

*(Tabla vacía — se puebla en la primera sesión de diagnóstico de cada idioma. Ordenar por "Próximo repaso" ascendente; al inicio de cada sesión, extraer las filas con fecha ≤ hoy como calentamiento de recuperación activa.)*

## Reglas de actualización

- Si el estudiante **recupera correctamente** un ítem sin ayuda: avanzar a la siguiente repetición según la tabla de intervalos de `SKILL.md` §5 (1→3→7→16→35 días, luego doblando)
- Si el estudiante **falla la recuperación**: reiniciar el ítem en la repetición 1 (mismo día), no penalizar más allá de eso
- Ítems que alcancen la repetición 6+ (35 días) sin fallos pasan a **"mantenimiento de largo plazo"**: se revisan solo si el idioma completo entra en modo mantenimiento (ver `ruta-maestra-multilingue.md` §5)
- Cada ítem nuevo se registra con su **codificación elaborativa** (vínculo personal, `SKILL.md` Módulo IV) en la columna Origen cuando aplique, no solo la traducción
