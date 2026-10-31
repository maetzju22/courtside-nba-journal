#!/usr/bin/env python3
"""COURTSIDE – Das NBA-Journal: static site builder.

Reads every data/issues/YYYY-MM-DD.json, renders
  public/index.html                 -> newest issue
  public/ausgabe/<datum>/index.html -> every issue (permalink)
  public/archiv/index.html          -> archive list
Usage: python3 build.py
"""
import json, pathlib, shutil, datetime, hashlib
from jinja2 import Environment, FileSystemLoader, select_autoescape

ROOT = pathlib.Path(__file__).parent
DATA = ROOT / "data" / "issues"
OUT = ROOT / "public"

TEAMS = {
    "ATL": (1610612737, "Atlanta Hawks", "Hawks"),
    "BOS": (1610612738, "Boston Celtics", "Celtics"),
    "CLE": (1610612739, "Cleveland Cavaliers", "Cavaliers"),
    "NOP": (1610612740, "New Orleans Pelicans", "Pelicans"),
    "CHI": (1610612741, "Chicago Bulls", "Bulls"),
    "DAL": (1610612742, "Dallas Mavericks", "Mavericks"),
    "DEN": (1610612743, "Denver Nuggets", "Nuggets"),
    "GSW": (1610612744, "Golden State Warriors", "Warriors"),
    "HOU": (1610612745, "Houston Rockets", "Rockets"),
    "LAC": (1610612746, "LA Clippers", "Clippers"),
    "LAL": (1610612747, "Los Angeles Lakers", "Lakers"),
    "MIA": (1610612748, "Miami Heat", "Heat"),
    "MIL": (1610612749, "Milwaukee Bucks", "Bucks"),
    "MIN": (1610612750, "Minnesota Timberwolves", "Timberwolves"),
    "BKN": (1610612751, "Brooklyn Nets", "Nets"),
    "NYK": (1610612752, "New York Knicks", "Knicks"),
    "ORL": (1610612753, "Orlando Magic", "Magic"),
    "IND": (1610612754, "Indiana Pacers", "Pacers"),
    "PHI": (1610612755, "Philadelphia 76ers", "76ers"),
    "PHX": (1610612756, "Phoenix Suns", "Suns"),
    "POR": (1610612757, "Portland Trail Blazers", "Trail Blazers"),
    "SAC": (1610612758, "Sacramento Kings", "Kings"),
    "SAS": (1610612759, "San Antonio Spurs", "Spurs"),
    "OKC": (1610612760, "Oklahoma City Thunder", "Thunder"),
    "TOR": (1610612761, "Toronto Raptors", "Raptors"),
    "UTA": (1610612762, "Utah Jazz", "Jazz"),
    "MEM": (1610612763, "Memphis Grizzlies", "Grizzlies"),
    "WAS": (1610612764, "Washington Wizards", "Wizards"),
    "DET": (1610612765, "Detroit Pistons", "Pistons"),
    "CHA": (1610612766, "Charlotte Hornets", "Hornets"),
}


def logo(abbr):
    tid = TEAMS[abbr][0]
    return f"https://cdn.nba.com/logos/nba/{tid}/primary/L/logo.svg"


def tname(abbr, short=False):
    t = TEAMS[abbr]
    return t[2] if short else t[1]


def words(issue):
    """Rough word count of all running text, for the reading-time badge."""
    n = 0
    def walk(x):
        nonlocal n
        if isinstance(x, str):
            n += len(x.split())
        elif isinstance(x, list):
            for i in x: walk(i)
        elif isinstance(x, dict):
            for k, v in x.items():
                if k not in ("url", "away", "home", "team", "standings"):
                    walk(v)
    walk(issue)
    return n


def main():
    env = Environment(loader=FileSystemLoader(ROOT / "templates"),
                      autoescape=select_autoescape(["html"]))
    css_v = hashlib.md5((ROOT / 'templates' / 'style.css').read_bytes()).hexdigest()[:8]
    env.globals.update(logo=logo, tname=tname, css_v=css_v)
    issues = []
    for f in sorted(DATA.glob("*.json")):
        d = json.loads(f.read_text(encoding="utf-8"))
        d["_words"] = words(d)
        d["_minutes"] = max(1, round(d["_words"] / 220))
        issues.append(d)
    if not issues:
        raise SystemExit("keine Ausgaben in data/issues")
    issues.sort(key=lambda d: d["date"])

    if OUT.exists():
        shutil.rmtree(OUT)
    (OUT / "archiv").mkdir(parents=True)
    issue_tpl = env.get_template("issue.html")
    for i, d in enumerate(issues):
        prev_d = issues[i - 1]["date"] if i > 0 else None
        next_d = issues[i + 1]["date"] if i < len(issues) - 1 else None
        html = issue_tpl.render(i=d, prev=prev_d, next=next_d, base="../../", is_latest=False)
        p = OUT / "ausgabe" / d["date"]
        p.mkdir(parents=True, exist_ok=True)
        (p / "index.html").write_text(html, encoding="utf-8")
    latest = issues[-1]
    prev_d = issues[-2]["date"] if len(issues) > 1 else None
    (OUT / "index.html").write_text(
        issue_tpl.render(i=latest, prev=prev_d, next=None, base="", is_latest=True), encoding="utf-8")
    (OUT / "archiv" / "index.html").write_text(
        env.get_template("archive.html").render(issues=list(reversed(issues)), base="../"), encoding="utf-8")
    shutil.copy(ROOT / "templates" / "style.css", OUT / "style.css")
    shutil.copytree(ROOT / "templates" / "static", OUT, dirs_exist_ok=True)
    print(f"OK: {len(issues)} Ausgabe(n), neueste {latest['date']} (~{latest['_words']} Wörter, ~{latest['_minutes']} Min.)")


if __name__ == "__main__":
    main()
