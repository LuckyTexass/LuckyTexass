"""Wspólna rama okna terminala dla wszystkich SVG profilu."""
from __future__ import annotations

from html import escape

FONT = "ui-monospace, SFMono-Regular, Menlo, Consolas, 'Liberation Mono', monospace"
PROMPT = "gracjan@github ~ $"
BG, BAR, BORDER = "#0d1117", "#161b22", "#30363d"
PALETTE = ["#161b22", "#0e4429", "#006d32", "#26a641", "#39d353"]
TYPE_SECONDS = 0.9  # tyle trwa wpisywanie komendy, potem rusza zawartość


def plural(n: int, one: str, few: str, many: str) -> str:
    if n == 1:
        return one
    if n % 10 in (2, 3, 4) and n % 100 not in (12, 13, 14):
        return few
    return many


def terminal_frame(width: int, height: int, command: str, css: str, body: str, static: bool) -> str:
    """Okno z paskiem tytułu i linią promptu, w której komenda „wpisuje się" sama."""
    prompt_w = (len(PROMPT) + 1) * 8.4  # 14px monospace ≈ 8.4px na znak
    cmd_w = len(command) * 8.4 + 4
    typing = ""
    if not static:
        typing = f"""
      .cmd {{ clip-path: inset(0 100% 0 0); animation: type {TYPE_SECONDS}s steps({len(command)}) .2s forwards; }}
      @keyframes type {{ to {{ clip-path: inset(0 0 0 0); }} }}
      .cur {{ animation: blink 1s steps(1) infinite; }}
      @keyframes blink {{ 50% {{ opacity: 0; }} }}
        """
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-label="{escape(command)}">
  <style>
      .p {{ font: 14px {FONT}; fill: #39d353; }}
      .k {{ font: 14px {FONT}; fill: #e6edf3; }}
      .t {{ font: 12px {FONT}; fill: #7d8590; }}{typing}{css}
  </style>
  <rect x=".5" y=".5" width="{width - 1}" height="{height - 1}" rx="10" fill="{BG}" stroke="{BORDER}"/>
  <path d="M.5 34 V10.5 a10 10 0 0 1 10 -10 H{width - 10.5} a10 10 0 0 1 10 10 V34 Z" fill="{BAR}"/>
  <line x1="1" y1="34" x2="{width - 1}" y2="34" stroke="{BORDER}"/>
  <circle cx="20" cy="17" r="6" fill="#ff5f57"/>
  <circle cx="40" cy="17" r="6" fill="#febc2e"/>
  <circle cx="60" cy="17" r="6" fill="#28c840"/>
  <text class="t" x="{width / 2}" y="21" text-anchor="middle">gracjan@github: ~</text>
  <text class="p" x="22" y="62">{PROMPT}</text>
  <text class="k cmd" x="{22 + prompt_w:.1f}" y="62">{escape(command)}</text>
  <rect class="cur" x="{22 + prompt_w + cmd_w:.1f}" y="50" width="8" height="15" fill="#e6edf3" opacity=".8"/>
{body}
</svg>
"""
