# KI-Kompass

Deutschsprachige Übersicht über KI-Assistenten: welcher Anbieter passt zu wem, was kostet er, wo werden die Daten verarbeitet und was ist gerade neu. Für Privatpersonen und Firmen in der Schweiz.

## Aufbau

| Datei | Inhalt |
|---|---|
| `index.html` | Die ganze Seite: Layout, Anbieter-Profile, Entscheidungshilfe |
| `data/news.json` | Meldungen für „Gestern“, „Heute“ und „Demnächst“ (wird täglich aktualisiert) |

Die Seite braucht keinen Build-Schritt. GitHub Pages veröffentlicht sie direkt aus dem Branch `main`.

## Lokal ansehen

Weil die Seite `data/news.json` nachlädt, braucht es einen kleinen lokalen Webserver (ein Doppelklick auf `index.html` reicht nicht):

```bash
python3 -m http.server 8000
```

Danach im Browser `http://localhost:8000` öffnen.

## Tägliche Aktualisierung

1. **Kurz vor 8 Uhr** recherchiert eine geplante Aufgabe die KI-Neuigkeiten, aktualisiert `data/news.json` auf einem Branch `news/JJJJ-MM-TT` und schickt eine Benachrichtigung.
2. **Freigeben:** Branch selbst in `main` mergen (Pull Request erstellen und mergen).
3. **Stoppen:** Branch auf GitHub löschen. Dann wird an diesem Tag nichts veröffentlicht.
4. **Keine Reaktion:** Eine zweite Aufgabe 30 Minuten später prüft die Datei mit `scripts/check_news.py` und merged den Branch automatisch, wenn die Prüfung besteht.
5. GitHub Pages veröffentlicht die neue Version.

Prüfung manuell starten: `python3 scripts/check_news.py`

### Regeln für Meldungen

- Je Tag (Gestern, Heute) und für „Demnächst“ genau 5 Meldungen.
- Alle KI-Themen, nicht nur Preise: neue Funktionen, Modelle, Sicherheit, Recht, Arbeitswelt, Termine.
- In eigenen Worten und einfacher Sprache schreiben, keine Sätze aus Artikeln übernehmen.
- Jede Meldung braucht eine Quelle mit Link. Gerüchte klar als Bericht kennzeichnen („laut …“).
- „Demnächst“ enthält nur angekündigte oder bestätigte Termine.

## Hinweise

Preise und Datenschutz-Angaben ohne Gewähr. Vor einem Abschluss immer die Seite des Anbieters prüfen.
