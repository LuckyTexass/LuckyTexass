"""Rysuje data/contributions.json jako animowany kalendarz w oknie terminala.

Wynik: contrib-heatmap.svg. Animacja (CSS keyframes w samym SVG) odtwarza się raz
i zostaje na ostatniej klatce. STATIC=1 daje zamrożoną klatkę do podglądu.
"""
from __future__ import annotations

import json
import os
from datetime import date, timedelta
from pathlib import Path

from svg_common import FONT, PALETTE, TYPE_SECONDS, plural, terminal_frame

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data" / "contributions.json"
OUT = ROOT / "contrib-heatmap.svg"

MONTHS_FULL = ["styczeń", "luty", "marzec", "kwiecień", "maj", "czerwiec", "lipiec",
               "sierpień", "wrzesień", "październik", "listopad", "grudzień"]
MONTHS = ["sty", "lut", "mar", "kwi", "maj", "cze", "lip", "sie", "wrz", "paź", "lis", "gru"]
DAYS = {1: "pn", 3: "śr", 5: "pt"}  # wiersze liczone od niedzieli, jak u GitHuba

WIDTH = 860
CELL, GAP = 11, 3.4
STEP = CELL + GAP
GRID_X, GRID_Y = 58, 100


def render(data: dict, static: bool) -> str:
    days = data["days"]
    first = date.fromisoformat(days[0]["date"])
    offset = (first.weekday() + 1) % 7  # niedziela = 0

    cells, labels = [], []
    last_month_col = -3
    for i, d in enumerate(days):
        day = first + timedelta(days=i)
        col, row = divmod(i + offset, 7)
        x, y = GRID_X + col * STEP, GRID_Y + row * STEP
        delay = TYPE_SECONDS + 0.3 + (col + row) * 0.035
        style = "" if static else f' style="animation-delay:{delay:.3f}s"'
        title = f'{day.strftime("%d.%m.%Y")}: {d["count"]}'
        cells.append(
            f'<rect class="c" x="{x}" y="{y}" width="{CELL}" height="{CELL}" rx="2" '
            f'fill="{PALETTE[min(d["level"], 4)]}"{style}><title>{title}</title></rect>'
        )
        if day.day <= 7 and row == 0 and col - last_month_col >= 3 and col <= 50:
            labels.append(f'<text class="m" x="{x}" y="{GRID_Y - 8}">{MONTHS[day.month - 1]}</text>')
            last_month_col = col

    for row, name in DAYS.items():
        labels.append(f'<text class="m" x="{GRID_X - 30}" y="{GRID_Y + row * STEP + 10}">{name}</text>')

    grid_bottom = GRID_Y + 7 * STEP
    legend_x = GRID_X + 53 * STEP - GAP - 5 * STEP - 44
    legend = [f'<text class="m" x="{legend_x - 40}" y="{grid_bottom + 26}">mniej</text>']
    for lvl, color in enumerate(PALETTE):
        legend.append(
            f'<rect x="{legend_x + lvl * STEP}" y="{grid_bottom + 16}" width="{CELL}" '
            f'height="{CELL}" rx="2" fill="{color}"/>'
        )
    legend.append(f'<text class="m" x="{legend_x + 5 * STEP + 6}" y="{grid_bottom + 26}">więcej</text>')

    total = data["total"]
    best_month, best_count = max(data["monthly"].items(), key=lambda kv: kv[1])
    best_name = f'{MONTHS_FULL[int(best_month[5:]) - 1]}, {best_count}'
    footer = (
        f'<text class="f" x="{GRID_X - 30}" y="{grid_bottom + 26}">'
        f'<tspan class="hl">{total}</tspan> {plural(total, "kontrybucja", "kontrybucje", "kontrybucji")} '
        f'w ostatnim roku <tspan class="dim">·</tspan> rekord miesiąca: '
        f'<tspan class="hl">{best_name}</tspan></text>'
    )

    css = f"""
      .m {{ font: 11px {FONT}; fill: #7d8590; }}
      .f {{ font: 13px {FONT}; fill: #c9d1d9; }}
      .hl {{ fill: #39d353; font-weight: 700; }}
      .dim {{ fill: #484f58; }}
    """
    if not static:
        css += """
      .c { opacity: 0; transform-box: fill-box; transform-origin: center;
           animation: drop .45s cubic-bezier(.2,.8,.2,1) forwards; }
      @keyframes drop { from { opacity: 0; transform: translateY(-6px) scale(.6); }
                        to { opacity: 1; transform: none; } }
        """

    height = grid_bottom + 48
    body = "\n".join(labels + cells + legend + [footer])
    return terminal_frame(WIDTH, height, "./contributions.sh", css, body, static)


def main() -> None:
    data = json.loads(DATA.read_text())
    OUT.write_text(render(data, os.environ.get("STATIC") == "1"))
    print(f"zapisano {OUT.name}")


if __name__ == "__main__":
    main()
