#!/usr/bin/env python3
"""
Motor de Bayesian Knowledge Tracing (BKT) -- Tutor de Idiomas Neuro-SLA.

A diferencia del motor SM-2 (que agenda repaso de items lexicos puntuales),
este motor mantiene una probabilidad de dominio P(L) por HABILIDAD o PATRON
(ej. "tercer_condicional", "verbos_separables_aleman", "liaison_frances").

Es un modelo probabilistico real: cada observacion (correcto/incorrecto)
actualiza la creencia sobre el dominio del estudiante via regla de Bayes,
y luego aplica una probabilidad de "aprendizaje" entre observaciones.
Este es el mismo tipo de modelo usado en sistemas reales de tutoria
inteligente (Corbett & Anderson, 1994).

Parametros por defecto (ajustables por patron si hay evidencia mejor):
  P(L0) = 0.3   -- probabilidad inicial de dominio antes de observar nada
  P(T)  = 0.15  -- probabilidad de "aprender" el patron entre una observacion y la siguiente
  P(G)  = 0.2   -- probabilidad de acertar por adivinar sin dominar
  P(S)  = 0.1   -- probabilidad de fallar aun dominando (lapsus/despiste)

Uso:
  python3 bkt_engine.py observe --state STATE --lang L --skill "nombre_patron" --correct true|false [--today YYYY-MM-DD]
  python3 bkt_engine.py status  --state STATE [--lang L]
"""
import argparse
import json
import os
from datetime import date

P_L0_DEFAULT = 0.3
P_T_DEFAULT = 0.15
P_G_DEFAULT = 0.2
P_S_DEFAULT = 0.1

MASTERY_THRESHOLD = 0.85  # a partir de aqui se considera "dominado" (Modulo IX / Matriz de Progreso)


def load_state(path):
    if not os.path.exists(path):
        return {"skills": {}}
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def save_state(path, state):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(state, f, ensure_ascii=False, indent=2, sort_keys=True)


def today_str(today_override=None):
    return today_override or date.today().isoformat()


def get_or_init_skill(state, lang, skill):
    key = f"{lang}:{skill}"
    if key not in state["skills"]:
        state["skills"][key] = {
            "lang": lang,
            "skill": skill,
            "p_l": P_L0_DEFAULT,
            "p_t": P_T_DEFAULT,
            "p_g": P_G_DEFAULT,
            "p_s": P_S_DEFAULT,
            "n_observations": 0,
            "history": [],
        }
    return state["skills"][key]


def bayes_update(p_l, correct, p_g, p_s):
    """Posterior P(L | observacion) via regla de Bayes."""
    if correct:
        num = p_l * (1 - p_s)
        den = p_l * (1 - p_s) + (1 - p_l) * p_g
    else:
        num = p_l * p_s
        den = p_l * p_s + (1 - p_l) * (1 - p_g)
    if den == 0:
        return p_l
    return num / den


def apply_learning_transition(p_l_given_obs, p_t):
    """Tras la observacion, el estudiante pudo haber 'aprendido' entre esta y la siguiente."""
    return p_l_given_obs + (1 - p_l_given_obs) * p_t


def observe(state, lang, skill, correct, today):
    s = get_or_init_skill(state, lang, skill)
    p_l_posterior = bayes_update(s["p_l"], correct, s["p_g"], s["p_s"])
    p_l_next = apply_learning_transition(p_l_posterior, s["p_t"])

    s["p_l"] = round(p_l_next, 4)
    s["n_observations"] += 1
    s["history"].append({"date": today, "correct": correct, "p_l_after": s["p_l"]})
    s["mastered"] = s["p_l"] >= MASTERY_THRESHOLD
    return s


def main():
    p = argparse.ArgumentParser(description="Motor BKT de dominio por habilidad/patron")
    sub = p.add_subparsers(dest="cmd", required=True)

    po = sub.add_parser("observe")
    po.add_argument("--state", required=True)
    po.add_argument("--lang", required=True)
    po.add_argument("--skill", required=True)
    po.add_argument("--correct", required=True, choices=["true", "false"])
    po.add_argument("--today", default=None)

    ps = sub.add_parser("status")
    ps.add_argument("--state", required=True)
    ps.add_argument("--lang", default=None)

    args = p.parse_args()
    state = load_state(args.state)

    if args.cmd == "observe":
        today = today_str(args.today)
        s = observe(state, args.lang, args.skill, args.correct == "true", today)
        save_state(args.state, state)
        print(json.dumps(s, ensure_ascii=False, indent=2))

    elif args.cmd == "status":
        skills = [s for s in state["skills"].values() if not args.lang or s["lang"] == args.lang]
        skills.sort(key=lambda s: s["p_l"])
        print(json.dumps(skills, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
