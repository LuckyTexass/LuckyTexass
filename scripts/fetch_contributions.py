"""Pobiera publiczny kalendarz kontrybucji i zapisuje data/contributions.json.

Bez tokenu i bez zależności: ten sam fragment HTML, którego używa strona profilu.
"""
from __future__ import annotations

import json
import re
import sys
import urllib.request
from collections import defaultdict
from pathlib import Path

USER = "LuckyTexass"
URL = f"https://github.com/users/{USER}/contributions"
OUT = Path(__file__).resolve().parent.parent / "data" / "contributions.json"

CELL = re.compile(r"<td\b[^>]*ContributionCalendar-day[^>]*>")
ATTR = re.compile(r'(data-date|data-level|id)="([^"]*)"')
TIP = re.compile(r'<tool-tip\b[^>]*\bfor="([^"]+)"[^>]*>([^<]*)</tool-tip>')
COUNT = re.compile(r"^(\d[\d,]*) contributions?")


def fetch(url: str) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": "profile-art"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        return resp.read().decode("utf-8")


def parse(html: str) -> list[dict]:
    tips = {cell_id: text.strip() for cell_id, text in TIP.findall(html)}
    days = []
    for tag in CELL.findall(html):
        attrs = dict(ATTR.findall(tag))
        if "data-date" not in attrs:
            continue
        m = COUNT.match(tips.get(attrs.get("id", ""), ""))
        days.append({
            "date": attrs["data-date"],
            "level": int(attrs.get("data-level", 0)),
            "count": int(m.group(1).replace(",", "")) if m else 0,
        })
    days.sort(key=lambda d: d["date"])
    return days


def streaks(days: list[dict]) -> tuple[int, int]:
    longest = run = 0
    for d in days:
        run = run + 1 if d["count"] else 0
        longest = max(longest, run)
    current = 0
    for d in reversed(days):
        # dzisiejszy dzień bez kontrybucji jeszcze nie przerywa serii
        if d["count"] == 0 and d["date"] == days[-1]["date"]:
            continue
        if not d["count"]:
            break
        current += 1
    return current, longest


def main() -> int:
    days = parse(fetch(URL))
    if len(days) < 300:
        print(f"Za mało dni w kalendarzu ({len(days)}), GitHub zmienił HTML?", file=sys.stderr)
        return 1

    monthly: dict[str, int] = defaultdict(int)
    for d in days:
        monthly[d["date"][:7]] += d["count"]
    best = max(days, key=lambda d: d["count"])
    current, longest = streaks(days)

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps({
        "user": USER,
        "total": sum(d["count"] for d in days),
        "active_days": sum(1 for d in days if d["count"]),
        "current_streak": current,
        "longest_streak": longest,
        "best_day": {"date": best["date"], "count": best["count"]},
        "monthly": dict(sorted(monthly.items())),
        "days": days,
    }, indent=1, ensure_ascii=False) + "\n")
    print(f"{len(days)} dni, suma {sum(d['count'] for d in days)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
