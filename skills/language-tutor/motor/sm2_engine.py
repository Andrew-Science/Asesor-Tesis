#!/usr/bin/env python3
"""
Motor de Repeticion Espaciada (SM-2) -- Tutor de Idiomas Neuro-SLA.

Implementacion real del algoritmo SM-2 (SuperMemo-2, Wozniak 1987).
Cada item (palabra/chunk/estructura) tiene un estado que se actualiza
con cada revision segun la calidad de la respuesta (0-5). El "easiness
factor" (EF) es el parametro que hace este motor adaptativo: sube o baja
por item segun el desempeno real del estudiante, no una tabla fija.

Uso:
  python3 sm2_engine.py add     --state STATE --lang L --id ID --text "..." [--origin "..."]
  python3 sm2_engine.py review  --state STATE --lang L --id ID --quality 0-5 [--today YYYY-MM-DD]
  python3 sm2_engine.py due     --state STATE --lang L [--today YYYY-MM-DD]
  python3 sm2_engine.py list    --state STATE [--lang L]
"""
import argparse
import json
import os
from datetime import date, timedelta

MIN_EF = 1.3
INITIAL_EF = 2.5


def load_state(path):
    if not os.path.exists(path):
        return {"items": {}}
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def save_state(path, state):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(state, f, ensure_ascii=False, indent=2, sort_keys=True)


def today_str(today_override=None):
    if today_override:
        return today_override
    return date.today().isoformat()


def add_item(state, lang, item_id, text, origin, today):
    key = f"{lang}:{item_id}"
    state["items"][key] = {
        "lang": lang,
        "id": item_id,
        "text": text,
        "origin": origin or "",
        "ef": INITIAL_EF,
        "n": 0,
        "interval": 0,
        "last_review": None,
        "next_review": today,
        "history": [],
    }
    return state["items"][key]


def review_item(state, lang, item_id, quality, today):
    """SM-2: quality is 0-5 (0=blackout, 5=perfect recall)."""
    key = f"{lang}:{item_id}"
    if key not in state["items"]:
        raise SystemExit(f"Item no encontrado: {key}. Usa 'add' primero.")
    item = state["items"][key]

    ef = item["ef"]
    n = item["n"]

    if quality < 3:
        # Fallo de recuperacion: reiniciar repeticiones, no penalizar EF mas alla de la formula
        n = 0
        interval = 1
    else:
        if n == 0:
            interval = 1
        elif n == 1:
            interval = 6
        else:
            interval = round(item["interval"] * ef)
        n += 1

    ef = ef + (0.1 - (5 - quality) * (0.08 + (5 - quality) * 0.02))
    ef = max(MIN_EF, ef)

    next_review = (date.fromisoformat(today) + timedelta(days=interval)).isoformat()

    item["ef"] = round(ef, 3)
    item["n"] = n
    item["interval"] = interval
    item["last_review"] = today
    item["next_review"] = next_review
    item["history"].append({"date": today, "quality": quality})

    return item


def due_items(state, lang, today):
    out = []
    for key, item in state["items"].items():
        if lang and item["lang"] != lang:
            continue
        if item["next_review"] <= today:
            out.append(item)
    out.sort(key=lambda i: i["next_review"])
    return out


def main():
    p = argparse.ArgumentParser(description="Motor SM-2 de repeticion espaciada")
    sub = p.add_subparsers(dest="cmd", required=True)

    pa = sub.add_parser("add")
    pa.add_argument("--state", required=True)
    pa.add_argument("--lang", required=True)
    pa.add_argument("--id", required=True)
    pa.add_argument("--text", required=True)
    pa.add_argument("--origin", default="")
    pa.add_argument("--today", default=None)

    pr = sub.add_parser("review")
    pr.add_argument("--state", required=True)
    pr.add_argument("--lang", required=True)
    pr.add_argument("--id", required=True)
    pr.add_argument("--quality", type=int, required=True, choices=range(0, 6))
    pr.add_argument("--today", default=None)

    pd = sub.add_parser("due")
    pd.add_argument("--state", required=True)
    pd.add_argument("--lang", default=None)
    pd.add_argument("--today", default=None)

    pl = sub.add_parser("list")
    pl.add_argument("--state", required=True)
    pl.add_argument("--lang", default=None)

    args = p.parse_args()
    state = load_state(args.state)

    if args.cmd == "add":
        today = today_str(args.today)
        item = add_item(state, args.lang, args.id, args.text, args.origin, today)
        save_state(args.state, state)
        print(json.dumps(item, ensure_ascii=False, indent=2))

    elif args.cmd == "review":
        today = today_str(args.today)
        item = review_item(state, args.lang, args.id, args.quality, today)
        save_state(args.state, state)
        print(json.dumps(item, ensure_ascii=False, indent=2))

    elif args.cmd == "due":
        today = today_str(args.today)
        items = due_items(state, args.lang, today)
        print(json.dumps(items, ensure_ascii=False, indent=2))

    elif args.cmd == "list":
        items = [i for i in state["items"].values() if not args.lang or i["lang"] == args.lang]
        print(json.dumps(items, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
