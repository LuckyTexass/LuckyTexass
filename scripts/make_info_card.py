"""Karta w stylu neofetch: monogram ASCII po lewej, dane po prawej.

Wynik: info-card.svg. Treść zmienia się rzadko, więc skrypt odpala się ręcznie.
STATIC=1 daje zamrożoną klatkę do podglądu.
"""
from __future__ import annotations

import os
from html import escape
from pathlib import Path

from svg_common import FONT, TYPE_SECONDS, terminal_frame

OUT = Path(__file__).resolve().parent.parent / "info-card.svg"

LOGO = [
    " ██████╗ ███████╗",
    "██╔════╝ ██╔════╝",
    "██║  ███╗███████╗",
    "██║   ██║╚════██║",
    "╚██████╔╝███████║",
    " ╚═════╝ ╚══════╝",
]
LOGO_COLORS = ["#69f0a0", "#39d353", "#39d353", "#26a641", "#26a641", "#006d32"]

INFO = [
    ("Rola", "Full-Stack Engineer, produkty od zera do produkcji"),
    ("Produkty", "Roadence, Matura Ustna AI, CWave Workspace, Vento Profit"),
    ("Działka", "agregatory, systemy rezerwacyjne, SaaS, marketplace"),
    ("Frontend", "React, Next.js, TypeScript, Tailwind, PWA"),
    ("Backend", "Node.js, PostgreSQL / Supabase, Python, REST API"),
    ("Infra", "Linux / VPS, Vercel, CI/CD, webhooki i crony"),
    ("Integracje", "Stripe, Meta CAPI, Google Ads API, IdoSell"),
    ("AI", "LLM w produkcie, ocena odpowiedzi, guardrails"),
    ("Kontakt", "gracjan@pxlmedia.pl"),
]
SWATCHES = ["#ff7b72", "#ffa657", "#d29922", "#39d353", "#79c0ff", "#d2a8ff", "#e6edf3"]

WIDTH = 860
LOGO_SIZE = 17
LOGO_LINE = 20  # znaki ramek w Menlo mają ~1.17em, więc linie się stykają bez przerw
LOGO_X, LOGO_Y = 40, 196
INFO_X, VALUE_X, INFO_Y, INFO_LINE = 300, 404, 100, 24


def main() -> None:
    static = os.environ.get("STATIC") == "1"
    start = TYPE_SECONDS + 0.3
    parts = []

    for i, (row, color) in enumerate(zip(LOGO, LOGO_COLORS)):
        style = "" if static else f' style="animation-delay:{start + i * 0.12:.2f}s"'
        parts.append(
            f'<text class="logo wipe" x="{LOGO_X}" y="{LOGO_Y + i * LOGO_LINE}" fill="{color}"'
            f'{style}>{escape(row)}</text>'
        )

    lines = [
        '<tspan class="u">gracjan</tspan><tspan class="v">@</tspan><tspan class="u">github</tspan>',
        '<tspan class="d">' + "-" * 14 + "</tspan>",
    ]
    lines += [
        f'<tspan class="key">{escape(k)}:</tspan><tspan class="v" x="{VALUE_X}">{escape(v)}</tspan>'
        for k, v in INFO
    ]
    info_start = start + 0.4
    for i, line in enumerate(lines):
        style = "" if static else f' style="animation-delay:{info_start + i * 0.08:.2f}s"'
        parts.append(f'<text class="row" x="{INFO_X}" y="{INFO_Y + 12 + i * INFO_LINE}"{style}>{line}</text>')

    sw_y = INFO_Y + 12 + len(lines) * INFO_LINE - 8
    sw_delay = info_start + len(lines) * 0.08
    for i, color in enumerate(SWATCHES):
        style = "" if static else f' style="animation-delay:{sw_delay + i * 0.05:.2f}s"'
        parts.append(
            f'<rect class="row" x="{INFO_X + i * 28}" y="{sw_y}" width="24" height="14" rx="3" '
            f'fill="{color}"{style}/>'
        )

    css = f"""
      .logo {{ font: 700 {LOGO_SIZE}px/1 {FONT}; white-space: pre; }}
      .row {{ font: 13px {FONT}; }}
      .u {{ fill: #39d353; font-weight: 700; }}
      .d {{ fill: #c9d1d9; }}
      .key {{ fill: #79c0ff; font-weight: 700; }}
      .v {{ fill: #c9d1d9; }}
    """
    if not static:
        css += """
      .wipe { clip-path: inset(0 100% 0 0); animation: wipe .5s steps(17) forwards; }
      @keyframes wipe { to { clip-path: inset(0 0 0 0); } }
      .row { opacity: 0; animation: rise .45s ease-out forwards; }
      @keyframes rise { from { opacity: 0; transform: translateX(-10px); } to { opacity: 1; transform: none; } }
        """

    height = sw_y + 44
    OUT.write_text(terminal_frame(WIDTH, height, "neofetch", css, "\n".join(parts), static))
    print(f"zapisano {OUT.name}")


if __name__ == "__main__":
    main()
