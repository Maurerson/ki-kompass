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

1. Eine geplante Aufgabe recherchiert täglich die KI-Neuigkeiten.
2. Sie aktualisiert `data/news.json` und öffnet einen Pull Request.
3. Ein Mensch prüft die Meldungen und gibt den Pull Request frei.
4. GitHub Pages veröffentlicht die neue Version automatisch.

### Regeln für Meldungen

- Je Tag (Gestern, Heute) und für „Demnächst“ genau 5 Meldungen.
- Alle KI-Themen, nicht nur Preise: neue Funktionen, Modelle, Sicherheit, Recht, Arbeitswelt, Termine.
- In eigenen Worten und einfacher Sprache schreiben, keine Sätze aus Artikeln übernehmen.
- Jede Meldung braucht eine Quelle mit Link. Gerüchte klar als Bericht kennzeichnen („laut …“).
- „Demnächst“ enthält nur angekündigte oder bestätigte Termine.

## Hinweise

Preise und Datenschutz-Angaben ohne Gewähr. Vor einem Abschluss immer die Seite des Anbieters prüfen.
