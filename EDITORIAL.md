# COURTSIDE – Redaktionsbriefing

Tägliches, deutschsprachiges NBA-Journal als Onepager im Zeitungsstil.
Erscheint jeden Morgen um 8:00 Uhr Wiener Zeit unter https://courtside.hobiger.cc
Zielgruppe: Maz und seine Freunde – basketballverrückt, aber nicht jeden Tag nah an der NBA dran.
Sie wollen wissen: Was ist passiert, wer ist Favorit, wer hat geliefert, warum ist das wichtig?

## Ablauf einer Ausgabe (für den täglichen Lauf)

1. Repo klonen: `git clone https://github.com/maetzju22/courtside-nba-journal` und dieses Briefing lesen.
   Die letzte Ausgabe in `data/issues/` als Vorlage für Struktur und Ton ansehen.
2. Datum bestimmen (Zeitzone Europe/Vienna). Die Ausgabe heißt `data/issues/JJJJ-MM-TT.json`
   mit dem heutigen Wiener Datum. `issue_no` = Nummer der letzten Ausgabe + 1.
3. Recherche (WebSearch/WebFetch, Sport-Daten-Tool `fetch_sports_data` für Scores, Standings, Spielplan):
   - Alle Spiele der letzten Nacht: Endstand, Bilanz danach, Topscorer beider Teams, Besonderheiten.
   - Aktuelle Tabellen beider Conferences (nach der Nacht).
   - News: Verletzungen, Trades, Sperren, Rekorde, Personalien.
   - Spielplan heute Abend/Nacht und morgen – in Wiener Zeit umrechnen (Achtung Sommerzeit-Unterschiede USA/EU).
   - Europäer der Nacht (siehe Europa-Ecke).
   - Highlight-Videos und Recaps: nur echte URLs aus Suchergebnissen verwenden, nie erfinden.
   Jede Zahl muss aus einer Quelle stammen, die in diesem Lauf abgerufen wurde.
4. JSON schreiben (Schema unten), `python3 build.py` laufen lassen.
5. Prüfen: Build ohne Fehler, Lesezeit-Badge ≤ 6 Min. (Ziel ~1.000–1.300 Wörter; am Wochenende bis ~1.500),
   Ergebnisse gegen Quellen gegengecheckt, Bilanzen konsistent mit der Tabelle, Uhrzeiten plausibel.
6. Commit & Push auf `main` (Commit-Message z. B. `Ausgabe Nr. 7 – 2026-11-06`). Netlify veröffentlicht automatisch.
7. Gab es keine Spiele (All-Star-Pause, Off-Season): kürzere Ausgabe mit Hintergründen, News und Vorschau,
   `games: []` und `rewatch: null` setzen – die Bereiche werden dann ausgeblendet.

## Ton & Stil

- Sportzeitung, locker: fundiert, aber mit Schmäh und Pointen. Kein Fan-Gebrüll, keine Wettempfehlungen.
- Immer einordnen: Warum ist ein Ergebnis wichtig? Was bedeutet es für Tabelle, Cup, Playoff-Rennen, Trades?
- Fachbegriffe beim ersten Auftauchen kurz erklären oder ins Glossar.
- Deutsche Zahlen- und Datumsformate (98:93, 26.668 Punkte), Ergebnisse als Auswärts – Heim.
- Österreich-Bezug darf sein (Wiener Zeit, Pöltl), Wien-Klischees sparsam.
- Urheberrecht: keine Übernahme fremder Formulierungen, keine längeren Zitate, alles in eigenen Worten.

## Kompakt schreiben (seit Ausgabe Nr. 8)

Viele Leser:innen lesen am Handy beim Kaffee. Deshalb gilt: **kurz, dicht, ohne Wiederholungen.**
- Jede Info steht nur einmal auf der Seite. Was in „Alles in 1 Minute“ steht, wird in den Rubriken vertieft, nicht wiederholt.
- Die Seite zeigt vom Aufmacher die ersten 2 Absätze, von Storys und Einordnung nur den ersten Absatz –
  der Rest ist hinter „Weiterlesen“ eingeklappt. Das Wichtigste gehört also immer nach vorne.
- Lieber eine starke Pointe als drei Nebensätze. Absätze max. 3–4 Sätze.

## Rubriken (Reihenfolge = Seitenaufbau)

00. **Die Woche in 1 Minute** (`week`): NUR in der Sonntagsausgabe, steht ganz oben. 5–6 Stichpunkte (je ein Satz,
   fettes Schlagwort) zur Woche Montag–Sonntag: Wer hat dominiert, wer ist abgestürzt, größte Leistung, wichtigste News,
   Pöltl/Deutsche der Woche, Ausblick auf die kommende Woche. Dazu `hot` und `cold` (je 2–3 Teams mit Wochenbilanz als `note`, z. B. „4-0“).
   Wochenbilanzen nur aus den Ergebnissen der Ausgaben der Woche bzw. Quellen ableiten – nichts schätzen.
0. **Alles in 1 Minute** (`minute`): 6–8 Stichpunkte, die die ganze Ausgabe auf das Wichtigste verdichten
   (je ein Satz, beginnend mit fettem Schlagwort). Lesbar in unter einer Minute. Die Ergebnisliste und das
   Spiel des Tages erzeugt die Seite automatisch aus `games` und `upcoming` – nicht in die Stichpunkte kopieren.
1. **Spoilerfreier Re-Watch-Tipp** (`rewatch`): das sehenswerteste Spiel der Nacht für den League Pass.
   Text darf NICHT verraten, wer gewonnen hat oder wie es ausging.
2. **Aufmacher** (`lead`): die wichtigste Geschichte der Nacht, 3–4 kurze Absätze; die ersten zwei müssen allein funktionieren.
3. **Sidebar** (`sidebar`): nur noch „Spieler der Nacht“ (3–4 Einträge). „Die Nacht in 30 Sekunden“ entfällt – das leistet „Alles in 1 Minute“.
4. **Ergebnisse** (`games`): alle Spiele, Topscorer-Zeile (kurz, max. ~20 Wörter), 1–2 Links. Die Zeile ist eingeklappt.
5. **Die Geschichten der Nacht** (`stories`): genau 3 Texte, je 1–2 Absätze (der erste ist sichtbar).
6. **Europa-Ecke** (`europe`): max. 6 Einträge, `text` je ein Satz. Europäer, die gespielt haben. Immer zuerst **Jakob Pöltl** (Österreich), dann die Deutschen
   (Franz Wagner, Moritz Wagner, Tristan da Silva, Dennis Schröder, Isaiah Hartenstein, Daniel Theis u. a. – aktuelle Teams prüfen),
   dann die großen europäischen Stars (Jokić, Dončić, Giannis, Wembanyama …) und Auffälliges (z. B. Niederländer, Schweden).
   Wer nicht gespielt hat, kommt nur rein, wenn es eine News gibt.
7. **Power Ranking** (`power_ranking`): NUR in der Montagsausgabe – alle 30 Teams, je ein Satz, Bewegung zur Vorwoche in `move`.
8. **Einordnung** (`explainer`): 2–3 Absätze, der erste ist der sichtbare Teaser. Ein Erklärstück zu einem Thema, das gerade relevant ist (Regeln, Cup, Trade-Deadline,
   Salary Cap, Playoff-Format, Award-Rennen, Favoritenrolle …). Jeden Tag ein anderes Thema.
9. **News-Ticker** (`news`): 4–6 Meldungen mit Team-Logo, je ein Satz, nichts aus den Rubriken davor wiederholen.
10. **Tabellen** (`standings`): beide Conferences, sortiert nach Platz.
11. **Vorschau** (`upcoming`): heute Abend/Nacht vollständig, dazu morgen (Auswahl). Ein Spiel als `featured` = Spiel des Tages.
12. **Good to know** (`goodtoknow`): 4–5 Trivia/historische Vergleiche/Rekorde, jeweils mit großer Zahl (`big`).
13. **Highlights & Material** (`links`) und **Glossar** (`glossary`, 3–4 Begriffe, möglichst passend zur Ausgabe).
14. **Quellen** (`sources`): alle verwendeten Quellen.

Wochenende (Samstag/Sonntag): `edition_label` „Wochenend-Ausgabe“, etwas mehr Hintergrund. Sonntag zusätzlich `week` (siehe oben).
Montag: „Montagsausgabe mit Power Ranking“.

## JSON-Schema (siehe data/issues für Beispiele)

```
date, issue_no, weekday, date_long ("31. Oktober 2026"), edition_label, tagline, period ("Nacht auf Samstag")
week (nur sonntags): {range ("2.–8. Nov."), items:[html, 5–6], hot:[{team, note}], cold:[{team, note}]}
minute: [html-Stichpunkte, 6–8]
rewatch: {away, home, why}
lead: {kicker, title, teams:[ABK], teaser, body:[html-Absätze]}
sidebar: [{title:"Spieler der Nacht", items:[html]}]
games: [{tag, away, home, away_score, home_score, away_record, home_record, line(html), links:[{label,url}]}]
stories: [{team, kicker, title, body:[html]}]   (genau 3)
europe: [{flag, player, team, stat, text}]
power_ranking (nur montags): [{team, move, text}]  (30 Einträge, Platz 1 zuerst)
explainer: {title, body:[html]}
news: [{team, text(html)}]
standings_note, standings: {east:[[ABK,S,N],...], west:[...]}  (15 je Conference, nach Platz)
upcoming: [{label, games:[{time "HH:MM", away, home, note(html, optional), featured(optional)}]}]
goodtoknow: [{big, title, text}]
links: [{title, src, url, note(optional)}]
glossary: [{term, text}]
sources: [{title, url}]
```

Team-Kürzel (ABK): ATL BOS BKN CHA CHI CLE DAL DEN DET GSW HOU IND LAC LAL MEM MIA MIL MIN NOP NYK OKC ORL PHI PHX POR SAC SAS TOR UTA WAS.
Logos kommen automatisch vom offiziellen NBA-CDN, keine eigenen Bilder einbinden.
HTML in Texten nur `<strong>`, `<em>`, `<br>`.

## KI-Transparenz

Die Seite kennzeichnet im Footer, dass alle Texte KI-generiert sind (Hinweis „KI-generiert“ + Abschnitt „KI-Transparenz“
im Rechtlichen). Diese Kennzeichnung nicht entfernen.

## Sichtbarkeit

COURTSIDE ist nur für Freunde gedacht und soll nicht in Suchmaschinen auftauchen.
Alle Seiten tragen `<meta name="robots" content="noindex, …">` (templates) und Netlify sendet `X-Robots-Tag: noindex` (netlify.toml).
Diese Einträge nicht entfernen. Keine robots.txt mit `Disallow: /` anlegen – sonst sieht Google das noindex nicht.
