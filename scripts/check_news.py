#!/usr/bin/env python3
"""Prüft data/news.json, bevor neue Meldungen veröffentlicht werden.

Aufruf:  python3 scripts/check_news.py [YYYY-MM-DD]
Ohne Datum wird das heutige Datum (Zeitzone Europe/Zurich) erwartet.
Exit-Code 0 = alles in Ordnung, 1 = Fehler gefunden.
"""
import json
import sys
from datetime import datetime, timedelta
from pathlib import Path
from zoneinfo import ZoneInfo

DATEI = Path(__file__).resolve().parent.parent / "data" / "news.json"
TABS = ["gestern", "heute", "demnaechst"]
FELDER = ["datum", "firma", "kategorie", "titel", "text", "quelle"]
ANZAHL = 5


def pruefen(heute: str) -> list[str]:
    fehler = []
    try:
        daten = json.loads(DATEI.read_text(encoding="utf-8"))
    except Exception as e:  # ungültiges JSON oder Datei fehlt
        return [f"news.json kann nicht gelesen werden: {e}"]

    if daten.get("stand") != heute:
        fehler.append(f"'stand' ist {daten.get('stand')!r}, erwartet {heute!r}")

    tage = {t.get("key"): t for t in daten.get("tage", [])}
    gestern = (datetime.fromisoformat(heute) - timedelta(days=1)).date().isoformat()
    erwartet_datum = {"gestern": gestern, "heute": heute, "demnaechst": None}

    for key in TABS:
        tag = tage.get(key)
        if not tag:
            fehler.append(f"Tab '{key}' fehlt")
            continue
        if tag.get("datum") != erwartet_datum[key]:
            fehler.append(f"Tab '{key}': datum ist {tag.get('datum')!r}, erwartet {erwartet_datum[key]!r}")
        items = tag.get("items", [])
        if len(items) != ANZAHL:
            fehler.append(f"Tab '{key}': {len(items)} Meldungen, erwartet {ANZAHL}")
        titel_gesehen = set()
        for i, n in enumerate(items, 1):
            for f in FELDER:
                if not n.get(f):
                    fehler.append(f"Tab '{key}', Meldung {i}: Feld '{f}' fehlt oder ist leer")
            q = n.get("quelle") or {}
            if not str(q.get("url", "")).startswith("https://"):
                fehler.append(f"Tab '{key}', Meldung {i}: Quelle braucht einen https-Link")
            if not q.get("name"):
                fehler.append(f"Tab '{key}', Meldung {i}: Quellenname fehlt")
            if len(n.get("text", "")) > 400:
                fehler.append(f"Tab '{key}', Meldung {i}: Text zu lang (max. 400 Zeichen)")
            t = n.get("titel")
            if t in titel_gesehen:
                fehler.append(f"Tab '{key}': Titel doppelt: {t!r}")
            titel_gesehen.add(t)
    return fehler


if __name__ == "__main__":
    heute = sys.argv[1] if len(sys.argv) > 1 else datetime.now(ZoneInfo("Europe/Zurich")).date().isoformat()
    probleme = pruefen(heute)
    if probleme:
        print("PRÜFUNG FEHLGESCHLAGEN:")
        for p in probleme:
            print(" -", p)
        sys.exit(1)
    print("Prüfung bestanden.")
