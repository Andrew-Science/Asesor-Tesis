# Temario Gramatical Completo — Inglés · Alemán · Francés (A1→C2)

> Complemento de `SKILL.md` (Módulo IV). Este es el **inventario completo de gramática** por idioma y nivel CEFR: la lista de verificación contra la que el tutor garantiza cobertura total — nada se enseña "cuando salga", todo punto tiene su lugar. Cada punto tiene un `id BKT` para registrarse en `motor/bkt_engine.py`: un punto se considera **cubierto** solo cuando su P(dominio) ≥ 0.85 en el motor, no cuando "ya se vio".

**Reglas de uso:**
- El tutor elige el siguiente punto gramatical de este temario según el nivel actual del estudiante y el bloque temático activo (`menu-secuencial-clases.md` §1) — máximo **1 estructura nueva por sesión** (tope de carga cognitiva, `SKILL.md` Módulo I)
- Los puntos no se enseñan como reglas aisladas sino integrados al contenido del bloque (grammaring, Larsen-Freeman)
- Al cerrar cada nivel, auditar cobertura: `python3 motor/bkt_engine.py status` — los puntos del nivel sin registro o con P(L) < 0.85 se reprograman antes de avanzar
- Los patrones de interferencia L1 (tablas de `SKILL.md` Módulo I) tienen prioridad dentro de su nivel

---

## INGLÉS

### A1
| Punto gramatical | id BKT |
|---|---|
| Verbo *to be* (afirmativo, negativo, preguntas) | en_be |
| Pronombres personales y posesivos (my/your/his...) | en_pronombres_posesivos |
| Artículos a/an/the y sustantivos plurales | en_articulos_plural |
| Presente simple + adverbios de frecuencia | en_presente_simple |
| Presente continuo | en_presente_continuo |
| *There is / there are* | en_there_is_are |
| *Can/can't* (habilidad y permiso) | en_can |
| Preposiciones de lugar y tiempo (in/on/at) | en_preposiciones_basicas |
| Imperativo | en_imperativo |
| Genitivo sajón ('s) | en_genitivo_sajon |
| Pronombres demostrativos (this/that/these/those) | en_demostrativos |
| *Like/love/hate* + -ing | en_like_ing |

### A2
| Punto gramatical | id BKT |
|---|---|
| Pasado simple (regulares e irregulares) | en_pasado_simple |
| Pasado continuo | en_pasado_continuo |
| Futuro con *going to* y presente continuo de planes | en_going_to |
| Futuro con *will* (predicciones, decisiones espontáneas) | en_will |
| Comparativos y superlativos | en_comparativos |
| Contables/incontables + some/any/much/many/a lot of | en_contables |
| *Have to / don't have to* (obligación) | en_have_to |
| *Should* (consejo) | en_should |
| Adverbios de modo | en_adverbios_modo |
| Pronombres objeto e indefinidos (someone/anything...) | en_pronombres_objeto |
| Verbos + gerundio o infinitivo (básico: want to, enjoy -ing) | en_gerundio_infinitivo_basico |
| Condicional cero y primer condicional | en_condicional_0_1 |
| Presente perfecto (experiencias: ever/never) | en_presente_perfecto_basico |

### B1
| Punto gramatical | id BKT |
|---|---|
| Presente perfecto vs pasado simple (for/since/just/yet/already) | en_perfecto_vs_pasado |
| Presente perfecto continuo | en_perfecto_continuo |
| Pasado perfecto | en_pasado_perfecto |
| Segundo condicional | en_condicional_2 |
| Voz pasiva (presente y pasado) | en_pasiva_basica |
| Reported speech (afirmaciones y preguntas) | en_reported_basico |
| Cláusulas relativas (defining: who/which/that) | en_relativas_defining |
| Modales de deducción presente (must/might/can't be) | en_modales_deduccion |
| *Used to / would* (hábitos pasados) | en_used_to |
| Question tags | en_question_tags |
| Consistencia de tiempo en narrativa ⚠ *(patrón prioritario del estudiante)* | pasado_narrativo |
| Propósito con *to + infinitivo* ⚠ *(patrón prioritario)* | proposito_to_infinitivo |
| Gerundio tras preposición ⚠ *(patrón prioritario)* | gerundio_tras_preposicion |
| Phrasal verbs de alta frecuencia (separables/inseparables) | en_phrasal_basico |
| *So/such/too/enough* | en_so_such |

### B2
| Punto gramatical | id BKT |
|---|---|
| Tercer condicional ⚠ *(patrón prioritario del estudiante)* | tercer_condicional |
| Condicionales mixtos | en_condicional_mixto |
| Modales de deducción en pasado (must have / can't have) | en_modales_pasado |
| Voz pasiva avanzada (todos los tiempos, con modales, *have something done*) | en_pasiva_avanzada |
| Causativos (have/get something done) | en_causativos |
| Reported speech avanzado (órdenes, sugerencias, verbos de reporte: deny/admit/suggest) | en_reported_avanzado |
| Cláusulas relativas non-defining y con preposición | en_relativas_nondefining |
| *Wish / if only / would rather* | en_wish |
| Futuro perfecto y futuro continuo | en_futuro_perfecto |
| Gerundio vs infinitivo con cambio de significado (stop/remember/try) | en_gerundio_infinitivo_avanzado |
| Conectores formales (however, despite, although, whereas) | en_conectores_formales |
| Verbos + preposición dependiente (depend on, consist of...) | en_preposiciones_dependientes |
| Cuantificadores avanzados (both/either/neither/whole/plenty) | en_cuantificadores |
| Artículos: usos avanzados y omisión | en_articulos_avanzados |

### C1
| Punto gramatical | id BKT |
|---|---|
| Inversión enfática (Never have I..., Not only...) | en_inversion |
| Cleft sentences (What I need is... / It was X who...) | en_cleft |
| Estructuras enfáticas con *do/does/did* | en_enfasis_do |
| Subjuntivo formal (suggest that he be...) | en_subjuntivo |
| Participios como conectores (Having finished..., Seen from...) | en_participios_conectores |
| Elipsis y sustitución (so do I, if so, neither did she) | en_elipsis |
| Nominalización (registro académico) | en_nominalizacion |
| Hedging académico (may suggest, appears to) | en_hedging |
| Modales matizados (shall, ought to, needn't have, dare) | en_modales_matizados |
| Discurso indirecto libre y estilo narrativo | en_discurso_libre |
| Colocaciones y dependencias de registro formal | en_colocaciones_formales |
| Phrasal verbs de registro amplio + verbos preposicionales de 3 partes | en_phrasal_avanzado |

### C2
| Punto gramatical | id BKT |
|---|---|
| Matices modales y de aspecto casi nativos | en_matices_modales |
| Ironía, humor y subtexto gramatical | en_pragmatica |
| Variación dialectal y de registro (formal↔coloquial fluido) | en_variacion_registro |
| Estructuras arcaicas/literarias de reconocimiento | en_literario |

---

## ALEMÁN

### A1
| Punto gramatical | id BKT |
|---|---|
| Géneros y artículos (der/die/das) — estrategia de memorización por sustantivo | de_generos |
| Presente (conjugación regular e irregular: sein, haben, werden) | de_presente |
| Orden V2 en oración principal | de_v2 |
| Nominativo y acusativo (artículos definidos/indefinidos) | de_nom_akk |
| Negación (nicht/kein) | de_negacion |
| Preguntas W- y de sí/no | de_preguntas |
| Modales básicos (können, müssen, wollen, möchten) + verbo al final | de_modales_basico |
| Plurales | de_plurales |
| Posesivos (mein, dein...) | de_posesivos |
| Imperativo | de_imperativo |
| Números, fecha y hora | de_numeros_hora |

### A2
| Punto gramatical | id BKT |
|---|---|
| Dativo (artículos, pronombres, verbos con dativo: helfen, gefallen) | de_dativ |
| Verbos separables ⚠ *(patrón de interferencia L1)* | de_separables |
| Perfekt (haben/sein + participio) | de_perfekt |
| Präteritum de sein/haben/modales | de_praeteritum_basico |
| Preposiciones con acusativo, con dativo, y Wechselpräpositionen | de_preposiciones_casos |
| Subordinadas con *weil/dass/wenn* (verbo al final) ⚠ | de_subordinadas_basico |
| Comparativo y superlativo | de_comparativos |
| Verbos reflexivos | de_reflexivos |
| Futuro con *werden* y presente con valor de futuro | de_futuro |
| Konjunktiv II básico (würde, hätte, könnte — cortesía) | de_konjunktiv2_basico |

### B1
| Punto gramatical | id BKT |
|---|---|
| Declinación completa del adjetivo (con der-/ein-/sin artículo) ⚠ | de_declinacion_adjetivo |
| Genitivo | de_genitiv |
| Präteritum general (narrativa escrita) | de_praeteritum |
| Plusquamperfekt | de_plusquamperfekt |
| Cláusulas relativas (todos los casos) | de_relativas |
| Voz pasiva (Vorgangspassiv, presente y pasado) | de_pasiva_basica |
| Konjunktiv II pleno (hipótesis, irreales del pasado) | de_konjunktiv2 |
| Infinitivo con *zu* y construcciones *um...zu / ohne...zu / statt...zu* | de_infinitiv_zu |
| Conectores dobles (entweder...oder, zwar...aber, je...desto) | de_conectores_dobles |
| Verbos con preposición fija + da-/wo-Komposita | de_verben_praep |
| N-Deklination (der Junge, den Jungen) | de_n_deklination |

### B2
| Punto gramatical | id BKT |
|---|---|
| Konjunktiv I (discurso indirecto, registro periodístico/académico) | de_konjunktiv1 |
| Pasiva con modales y Zustandspassiv | de_pasiva_avanzada |
| Alternativas a la pasiva (man, sich lassen, -bar) | de_pasiva_alternativas |
| Participio I y II como adjetivos y construcciones participiales | de_participios |
| Nominalización (registro formal: das Lesen, die Durchführung) | de_nominalisierung |
| Subjuntores avanzados (obwohl, während, indem, sodass, falls) | de_subjuntores_avanzados |
| Orden de complementos en el Mittelfeld (TeKaMoLo) | de_tekamolo |
| Partículas modales (doch, mal, eben, ja) — comprensión y uso básico | de_partikeln |
| Futur II (suposiciones sobre el pasado) | de_futur2 |
| Preposiciones con genitivo (trotz, während, wegen) | de_praep_genitiv |

### C1
| Punto gramatical | id BKT |
|---|---|
| Construcciones participiales extendidas (das von uns durchgeführte Experiment) | de_partizipialattribute |
| Funktionsverbgefüge (zur Verfügung stellen, in Frage kommen) | de_funktionsverben |
| Estilo nominal vs verbal (registro académico) | de_nominalstil |
| Konjunktiv en todos los registros y matices | de_konjunktiv_matices |
| Partículas modales: dominio pragmático completo | de_partikeln_avanzado |
| Orden de palabras marcado (topicalización, Nachfeld) | de_wortstellung_markiert |

### C2
| Punto gramatical | id BKT |
|---|---|
| Matices casi nativos de partículas, modo y aspecto | de_matices |
| Variación regional y de registro | de_variacion |
| Alemán académico-científico pleno (Wissenschaftssprache) | de_wissenschaftssprache |

---

## FRANCÉS

### A1
| Punto gramatical | id BKT |
|---|---|
| Género y artículos (le/la/les, un/une/des) — sin calcar del español ⚠ | fr_generos |
| Presente de -er, -ir, -re + irregulares clave (être, avoir, aller, faire) | fr_presente |
| Negación *ne...pas* (sin omitir "ne" en registro formal) ⚠ | fr_negacion |
| Preguntas (est-ce que, inversión, entonación) | fr_preguntas |
| Artículos partitivos (du/de la/des) | fr_partitivos |
| Posesivos y demostrativos | fr_posesivos |
| Futur proche (aller + infinitivo) | fr_futur_proche |
| Adjetivos: concordancia y posición (grupo BAGS antepuesto) ⚠ | fr_adjetivos_posicion |
| Números, hora y fecha | fr_numeros |
| *Il y a* | fr_il_y_a |

### A2
| Punto gramatical | id BKT |
|---|---|
| Passé composé (avoir/être, concordancia del participio con être) | fr_passe_compose |
| Imparfait | fr_imparfait |
| Passé composé vs imparfait (aspecto narrativo) | fr_pc_vs_imparfait |
| Verbos reflexivos | fr_reflexivos |
| Pronombres COD y COI (le/la/lui/leur) y su posición | fr_pronombres_od_oi |
| Pronombres *y* / *en* | fr_y_en |
| Futur simple | fr_futur_simple |
| Comparativos y superlativos | fr_comparativos |
| Imperativo con pronombres | fr_imperativo |
| Condicional de cortesía (je voudrais) | fr_condicional_cortesia |

### B1
| Punto gramatical | id BKT |
|---|---|
| Subjuntivo presente (disparadores: il faut que, vouloir que, émotions) ⚠ | fr_subjuntivo_basico |
| Condicional presente y pasado | fr_condicional |
| Hipótesis con *si* (les 3 structures) | fr_hypothese_si |
| Plus-que-parfait | fr_plus_que_parfait |
| Pronombres relativos (qui/que/dont/où) | fr_relativos_basico |
| Discours rapporté (presente y pasado + concordancia de tiempos) | fr_discours_rapporte |
| Doble pronominalización (le lui, m'en...) | fr_doble_pronombre |
| Gérondif (en + participe présent) | fr_gerondif |
| Voz pasiva | fr_pasiva |
| Expresiones de tiempo (depuis, pendant, il y a, dans) | fr_expresiones_tiempo |

### B2
| Punto gramatical | id BKT |
|---|---|
| Subjuntivo pleno (passé, disparadores avanzados, vs indicativo: après que ⚠) | fr_subjuntivo_avanzado |
| Relativos compuestos (lequel, auquel, duquel) | fr_relativos_compuestos |
| Participe présent vs gérondif vs adjectif verbal | fr_participe_present |
| Passé simple (reconocimiento en textos literarios/históricos) | fr_passe_simple |
| Mise en relief (c'est...qui, ce que...c'est) | fr_mise_en_relief |
| Conectores lógicos formales (néanmoins, en revanche, par conséquent) | fr_conectores_formales |
| Nominalización | fr_nominalisation |
| Concordancia del participio con COD antepuesto | fr_accord_participe |
| Futur antérieur | fr_futur_anterieur |

### C1
| Punto gramatical | id BKT |
|---|---|
| Subjuntivo imperfecto/pluscuamperfecto (reconocimiento literario) | fr_subjuntivo_literario |
| Registro soutenu vs courant vs familier (alternancia fluida) | fr_registros |
| Inversión estilística y estructuras enfáticas | fr_inversion |
| Discurso académico (hedging francés: il semblerait que, on pourrait avancer) | fr_hedging |
| Expresiones idiomáticas y colocaciones de alto registro | fr_colocaciones |

### C2
| Punto gramatical | id BKT |
|---|---|
| Matices casi nativos de modo, aspecto y registro | fr_matices |
| Variación regional (Francia/Québec/África) y pragmática cultural | fr_variacion |
| Francés académico-científico pleno | fr_academique |

---

## Auditoría de Cobertura

Al cerrar cada nivel CEFR (hito de la Ruta Maestra), ejecutar:

```
python3 motor/bkt_engine.py status --state progreso/mastery-state.json --lang <idioma>
```

y contrastar contra la tabla del nivel: **todo punto sin registro en el motor o con P(L) < 0.85 se reprograma** en las siguientes sesiones antes de declarar el nivel completado. La cobertura gramatical es un criterio de cierre de nivel, igual que los hitos "can-do" de la Ruta Maestra.
