"""Hand-built pixel playbill art for Mark Jayson Martinez Farol's GitHub profile.

SVGs are SMIL-only: no scripts, no style blocks, no external images.
GitHub keeps declarative animation and drops CSS and JavaScript inside
images, so every motion here is an <animate> or <animateTransform> child
of the element it moves.
"""

from __future__ import annotations

import html
from pathlib import Path

GLYPH_W = 5
GLYPH_H = 7

# Original 5x7 glyphs. "#" is ink, "." is empty.
FONT = {
    "A": [" ### ", "#   #", "#   #", "#####", "#   #", "#   #", "#   #"],
    "B": ["#### ", "#   #", "#   #", "#### ", "#   #", "#   #", "#### "],
    "C": [" ####", "#    ", "#    ", "#    ", "#    ", "#    ", " ####"],
    "D": ["#### ", "#   #", "#   #", "#   #", "#   #", "#   #", "#### "],
    "E": ["#####", "#    ", "#    ", "#### ", "#    ", "#    ", "#####"],
    "F": ["#####", "#    ", "#    ", "#### ", "#    ", "#    ", "#    "],
    "G": [" ####", "#    ", "#    ", "# ###", "#   #", "#   #", " ####"],
    "H": ["#   #", "#   #", "#   #", "#####", "#   #", "#   #", "#   #"],
    "I": ["#####", "  #  ", "  #  ", "  #  ", "  #  ", "  #  ", "#####"],
    "J": ["  ###", "   # ", "   # ", "   # ", "#  # ", "#  # ", " ##  "],
    "K": ["#   #", "#  # ", "# #  ", "##   ", "# #  ", "#  # ", "#   #"],
    "L": ["#    ", "#    ", "#    ", "#    ", "#    ", "#    ", "#####"],
    "M": ["#   #", "## ##", "# # #", "#   #", "#   #", "#   #", "#   #"],
    "N": ["#   #", "##  #", "# # #", "#  ##", "#   #", "#   #", "#   #"],
    "O": [" ### ", "#   #", "#   #", "#   #", "#   #", "#   #", " ### "],
    "P": ["#### ", "#   #", "#   #", "#### ", "#    ", "#    ", "#    "],
    "Q": [" ### ", "#   #", "#   #", "#   #", "# # #", "#  # ", " ## #"],
    "R": ["#### ", "#   #", "#   #", "#### ", "# #  ", "#  # ", "#   #"],
    "S": [" ####", "#    ", "#    ", " ### ", "    #", "    #", "#### "],
    "T": ["#####", "  #  ", "  #  ", "  #  ", "  #  ", "  #  ", "  #  "],
    "U": ["#   #", "#   #", "#   #", "#   #", "#   #", "#   #", " ### "],
    "V": ["#   #", "#   #", "#   #", "#   #", "#   #", " # # ", "  #  "],
    "W": ["#   #", "#   #", "#   #", "#   #", "# # #", "## ##", "#   #"],
    "X": ["#   #", "#   #", " # # ", "  #  ", " # # ", "#   #", "#   #"],
    "Y": ["#   #", "#   #", " # # ", "  #  ", "  #  ", "  #  ", "  #  "],
    "Z": ["#####", "    #", "   # ", "  #  ", " #   ", "#    ", "#####"],
    "0": [" ### ", "#   #", "#  ##", "# # #", "##  #", "#   #", " ### "],
    "1": ["  #  ", " ##  ", "  #  ", "  #  ", "  #  ", "  #  ", " ### "],
    "2": [" ### ", "#   #", "    #", "  ## ", " #   ", "#    ", "#####"],
    "3": ["#### ", "    #", "    #", " ### ", "    #", "    #", "#### "],
    "4": ["#   #", "#   #", "#   #", "#####", "    #", "    #", "    #"],
    "5": ["#####", "#    ", "#### ", "    #", "    #", "#   #", " ### "],
    "6": [" ### ", "#    ", "#    ", "#### ", "#   #", "#   #", " ### "],
    "7": ["#####", "    #", "   # ", "  #  ", " #   ", " #   ", " #   "],
    "8": [" ### ", "#   #", "#   #", " ### ", "#   #", "#   #", " ### "],
    "9": [" ### ", "#   #", "#   #", " ####", "    #", "    #", " ### "],
    ".": ["     ", "     ", "     ", "     ", "     ", " ##  ", " ##  "],
    ",": ["     ", "     ", "     ", "     ", " ##  ", " ##  ", " #   "],
    "-": ["     ", "     ", "     ", "#####", "     ", "     ", "     "],
    "/": ["    #", "   # ", "   # ", "  #  ", " #   ", " #   ", "#    "],
    "+": ["     ", "  #  ", "  #  ", "#####", "  #  ", "  #  ", "     "],
    "'": [" ##  ", " ##  ", " #   ", "     ", "     ", "     ", "     "],
    ":": ["     ", " ##  ", " ##  ", "     ", " ##  ", " ##  ", "     "],
    "!": ["  #  ", "  #  ", "  #  ", "  #  ", "  #  ", "     ", "  #  "],
    "?": [" ### ", "#   #", "   # ", "  #  ", "  #  ", "     ", "  #  "],
    "(": ["  ## ", " #   ", "#    ", "#    ", "#    ", " #   ", "  ## "],
    ")": [" ##  ", "   # ", "    #", "    #", "    #", "   # ", " ##  "],
}

# Colors and the front grid are copied cell for cell from the attached sprite.
# J is the flat green backdrop and is not drawn.
EXACT_COLORS = {
    "A": "#156E20",
    "B": "#212020",
    "C": "#3D2F30",
    "D": "#433F34",
    "E": "#545047",
    "F": "#734610",
    "G": "#833301",
    "H": "#8C8F3B",
    "I": "#8F8500",
    "K": "#955E1A",
    "L": "#A45F00",
    "M": "#A6FC00",
    "N": "#BDAC00",
    "O": "#DEA900",
    "P": "#F9FB00",
    "Q": "#FCFBFA",
    "R": "#FED650",
    # White suit. S is the fold that used to be E, W is the cloth that used to be D.
    "S": "#D9D3C8",
    "W": "#F7F4EE",
}

FRONT_GRID = """
JJJJJJJJJJCCCJJJJJJJJJJ
JJJJJJJJJCPPRCJJJJJJJJJ
JJJJJJJJCLPPRLCJJJJJJJJ
JJJJJJJCOPPRROOCJJJJJJJ
JJJJJJCLPPPPRRRLCJJJJJJ
JJJJJJCPPPPPPRRRCJJJJJJ
JJJJJCOPPPPPPRRROCJJJJJ
JJJJJCPPPPPPPRRRRCJJJJJ
JJJJCOPPPPPPPRRRROCJJJJ
JJJJCPPPPPPPPRRRRRCJJJJ
JJJJCPQCCQPPPQCCQRCJJJJ
JJJJCPPPPPLPLRRRRRCJJJJ
JJJJCOPPPPCPCRRRROCJJJJ
JJJJJCPPPPLPLRRRRCJJJJJ
JJJJJCOPPPOLORRROCJJJJJ
JJJJJJCPPPPORRRRCJJJJJJ
JJJJJBDCOPPRRROCDBJJJJJ
JJJJBCEECCOROCCDDCBJJJJ
JJJBEBEEEDCCCDDDDBDBJJJ
CCCEDBDEEEECDDDAABDDCCC
CPPRCBBDEEEEEAAABJCRRRC
CCCPCIGIDEAMMADDBHCPCCC
JJJCCNGGAAMMADDBHHCCJJJ
JJJBKINICCCBCCDBHHHHJJJ
JJBKFFBBCDBHBDDBHHHHJJJ
JJBFFBHBCEBHBEDBHHHHJJJ
JJBBBHHBCCBHBCCBHHHJJJJ
JJJJJHHHBBHHHBBHHHJJJJJ
JJJJJJJHHHHHHHHHJJJJJJJ
""".strip("\n").splitlines()

def _white_suit(grid: list[str]) -> list[str]:
    """Same sprite, same pose. Only the charcoal suit becomes white."""
    return [row.replace("E", "S").replace("D", "W") for row in grid]


WHITE_GRID = _white_suit(FRONT_GRID)


def _check_grids() -> None:
    allowed = set(EXACT_COLORS) | {"J"}
    for name, grid in (("front", FRONT_GRID), ("white", WHITE_GRID)):
        if len(grid) != 29 or any(len(row) != 23 for row in grid):
            raise ValueError(f"bad {name} grid")
        bad = {ch for row in grid for ch in row if ch not in allowed}
        if bad:
            raise ValueError(f"{name} grid has {sorted(bad)}")
        if name == "white" and any("D" in row or "E" in row for row in grid):
            raise ValueError("white suit still has charcoal pixels")


_check_grids()

# Tiny icons, 9 columns, used on scene cards.
ICONS = {
    "lemon": """
...KKK...
..KYYYK..
.KYYYYYK.
KYYYYYYYK
KYYYYYYYK
.KYYYYYK.
..KYYYK..
...KKK...
.........
""".strip("\n"),
    "riff": """
KK....KK.
KKK..KKK.
.KKKKKK..
..KKKK...
.KKKKKK..
KKK..KKK.
KK....KK.
.........
.........
""".strip("\n"),
    "grid": """
KKKKKKKKK
K.K.K.K.K
KKKKKKKKK
K.K.K.K.K
KKKKKKKKK
K.K.K.K.K
KKKKKKKKK
K.K.K.K.K
KKKKKKKKK
""".strip("\n"),
    "coins": """
..KKKKK..
.KYYYYYK.
.KYYYYYK.
..KKKKK..
..KKKKK..
.KYYYYYK.
.KYYYYYK.
..KKKKK..
.........
""".strip("\n"),
    "link": """
.KKK.KKK.
K..K.K..K
K..KKK..K
.K.....K.
..K...K..
...K.K...
....K....
.........
.........
""".strip("\n"),
    "stack": """
.KKKKKKK.
.K.....K.
KKKKKKKKK
K.......K
KKKKKKKKK
K.......K
KKKKKKKKK
K.......K
KKKKKKKKK
""".strip("\n"),
    "scroll": """
KKKKKKK..
K.....KK.
K.KKK.K..
K.KKK.K..
K.KKK.K..
K.....K..
KKKKKKK..
.........
.........
""".strip("\n"),
    "house": """
....K....
...KKK...
..KKKKK..
.KKKKKKK.
..K.K.K..
..KK.KK..
..KK.KK..
..KK.KK..
..KK.KK..
""".strip("\n"),
    "mask": """
.KKKKKKK.
KYYYYYYYK
KYY.Y.YYK
KYYYYYYYK
.KYYYYYK.
..KYYYK..
...KKK...
....K....
.........
""".strip("\n"),
}


def _validate_font() -> None:
    for ch, rows in FONT.items():
        if len(rows) != GLYPH_H or any(len(row) != GLYPH_W or set(row) - set("#. ") for row in rows):
            raise ValueError(f"bad glyph {ch!r}")


_validate_font()


LIGHT = {
    "bg": "#7ED4FF",
    "bg_deep": "#C8EFFF",
    "cloud": "#FFFFFF",
    "hill": "#3CB85A",
    "hill_hi": "#8BE56E",
    "hill_dark": "#1F8A3C",
    "night": False,
    "ink": "#2A160E",
    "muted": "#6B4A32",
    "curtain": "#C4314A",
    "curtain_dark": "#861832",
    "curtain_hi": "#FF8B98",
    "gold": "#E2A31A",
    "gold_hi": "#FFE38A",
    "gold_dim": "#A67416",
    "lemon": "#FFE14A",
    "lemon_hi": "#FFF4AE",
    "lemon_shade": "#E6A820",
    "leaf": "#2F9E55",
    "stage": "#7A4A28",
    "stage_hi": "#C4844A",
    "stage_dark": "#4E2E18",
    "cream": "#FFFAF0",
    "pink": "#FF6B9D",
    "mint": "#1F9D6B",
    "grape": "#6C3BB8",
    "ticket": "#FFF8E4",
    "ticket_ink": "#2A160E",
    "marquee": "#2A160E",
    "role": "#861832",
    "rotator": "#2A160E",
    "plaque": "#6C3BB8",
    "q0": "#F3E0BC",
    "q1": "#FFE08A",
    "q2": "#F0B429",
    "q3": "#E07A14",
    "q4": "#C4511A",
    "accents": ["#C4314A", "#146848", "#6C3BB8", "#7A4A00", "#A33D10", "#1D6A8C"],
}

DARK = {
    "bg": "#1A1244",
    "bg_deep": "#26185A",
    "cloud": "#3A2E70",
    "hill": "#1C5C38",
    "hill_hi": "#2E8A50",
    "hill_dark": "#0E3320",
    "night": True,
    "ink": "#FFF1C9",
    "muted": "#E4C98A",
    "curtain": "#E23B5C",
    "curtain_dark": "#7C1434",
    "curtain_hi": "#FF9AAB",
    "gold": "#FFC44D",
    "gold_hi": "#FFF0B8",
    "gold_dim": "#A67420",
    "lemon": "#FFE566",
    "lemon_hi": "#FFF7C2",
    "lemon_shade": "#E6A817",
    "leaf": "#3DCC74",
    "stage": "#3A2416",
    "stage_hi": "#8A5A32",
    "stage_dark": "#24140C",
    "cream": "#FFF6DF",
    "pink": "#FF8EC4",
    "mint": "#5EECC0",
    "grape": "#C4A6FF",
    "ticket": "#2C2158",
    "ticket_ink": "#FFF1C9",
    "marquee": "#FFE7A0",
    "role": "#FF8EC4",
    "rotator": "#FFF1C9",
    "plaque": "#5EECC0",
    "q0": "#2A2044",
    "q1": "#6A5018",
    "q2": "#C4922A",
    "q3": "#FFC44D",
    "q4": "#FFF1A8",
    "accents": ["#FF8EC4", "#5EECC0", "#C4A6FF", "#FFC44D", "#FFB070", "#9FD4FF"],
}

# The lead uses the same costume in both shows so he stays recognizable.
SPRITE_COLORS = {
    "K": "#1A100C",
    "Y": "#FFE14A",
    "H": "#FFF4AE",
    "N": "#E6A820",
    "B": "#1A100C",
    "D": "#3C3A44",
    "G": "#6A6674",
    "P": "#FF4D88",
    "L": "#3CAA62",
    "T": "#6B3E22",
}

NIGHT_CARD = "#241436"
NIGHT_INK = "#FFF1C9"
NIGHT_MUTED = "#E4C98A"
NIGHT_GOLD = "#FFC44D"


# System faces only. A style block or a web font would be stripped when GitHub
# serves the SVG as an image, and the pixel alphabet was too small to read.
SANS = "ui-sans-serif, system-ui, -apple-system, 'Segoe UI', Helvetica, Arial, sans-serif"


def rect_tag(x: int, y: int, w: int, h: int, fill: str, inner: str = "") -> str:
    if w <= 0 or h <= 0:
        return ""
    attrs = f'x="{x}" y="{y}" width="{w}" height="{h}" fill="{fill}"'
    if inner:
        return f"<rect {attrs}>{inner}</rect>"
    return f"<rect {attrs}/>"


def compress(pixels: dict[tuple[int, int], str]) -> list[str]:
    """Pack a pixel map into as few rectangles as possible."""
    if not pixels:
        return []
    rows: dict[int, list[tuple[int, str]]] = {}
    for (x, y), color in pixels.items():
        rows.setdefault(y, []).append((x, color))
    horiz: list[tuple[int, int, int, str]] = []
    for y in sorted(rows):
        cells = sorted(rows[y])
        run_x, run_color, run_w = cells[0][0], cells[0][1], 1
        for x, color in cells[1:]:
            if color == run_color and x == run_x + run_w:
                run_w += 1
            else:
                horiz.append((run_x, y, run_w, run_color))
                run_x, run_color, run_w = x, color, 1
        horiz.append((run_x, y, run_w, run_color))
    horiz.sort(key=lambda item: (item[0], item[2], item[3], item[1]))
    merged: list[tuple[int, int, int, int, str]] = []
    for x, y, w, color in horiz:
        if (
            merged
            and merged[-1][0] == x
            and merged[-1][2] == w
            and merged[-1][4] == color
            and merged[-1][1] + merged[-1][3] == y
        ):
            px, py, pw, ph, pc = merged[-1]
            merged[-1] = (px, py, pw, ph + 1, pc)
        else:
            merged.append((x, y, w, 1, color))
    merged.sort(key=lambda item: (item[1], item[0]))
    return [rect_tag(x, y, w, h, color) for x, y, w, h, color in merged]


def parse_art(art: str) -> list[str]:
    rows = art.strip("\n").splitlines()
    width = max(len(row) for row in rows)
    return [row.ljust(width, ".") for row in rows]


def blit(target: dict[tuple[int, int], str], rows: list[str], cmap: dict[str, str], ox: int, oy: int, scale: int) -> None:
    for gy, row in enumerate(rows):
        for gx, ch in enumerate(row):
            color = cmap.get(ch)
            if not color:
                continue
            for dy in range(scale):
                for dx in range(scale):
                    target[(ox + gx * scale + dx, oy + gy * scale + dy)] = color


def measure(text: str, scale: int, spacing: int | None = None) -> int:
    if spacing is None:
        spacing = scale
    cursor = 0
    chars = text.upper()
    for i, ch in enumerate(chars):
        cursor += 3 * scale if ch == " " else GLYPH_W * scale
        if i != len(chars) - 1:
            cursor += spacing
    return cursor


def blit_text(
    target: dict[tuple[int, int], str],
    text: str,
    x: int,
    y: int,
    scale: int,
    fill: str,
    spacing: int | None = None,
) -> int:
    if spacing is None:
        spacing = scale
    cursor = x
    chars = text.upper()
    for i, ch in enumerate(chars):
        if ch == " ":
            cursor += 3 * scale
        else:
            try:
                glyph = FONT[ch]
            except KeyError as exc:
                raise KeyError(f"no glyph for {ch!r} in {text!r}") from exc
            for gy, row in enumerate(glyph):
                for gx, bit in enumerate(row):
                    if bit != "#":
                        continue
                    for dy in range(scale):
                        for dx in range(scale):
                            target[(cursor + gx * scale + dx, y + gy * scale + dy)] = fill
            cursor += GLYPH_W * scale
        if i != len(chars) - 1:
            cursor += spacing
    return cursor - x


def char_edges(text: str, scale: int, spacing: int | None = None) -> list[int]:
    """Width of the line after each character, used to type one glyph at a time."""
    if spacing is None:
        spacing = scale
    cursor = 0
    edges: list[int] = []
    chars = text.upper()
    for i, ch in enumerate(chars):
        cursor += 3 * scale if ch == " " else GLYPH_W * scale
        edges.append(cursor)
        if i != len(chars) - 1:
            cursor += spacing
            edges[-1] = cursor
    return edges


class Scene:
    def __init__(self, w: int, h: int, bg: str | None):
        self.w = w
        self.h = h
        self.bg = bg
        self.parts: list[list[str]] = []
        self.bag: dict[tuple[int, int], str] = {}
        self.defs: list[str] = []
        self._seq = 0

    def _flush(self) -> None:
        if self.bag:
            self.parts.append(compress(self.bag))
            self.bag = {}

    def rect(self, x: int, y: int, w: int, h: int, fill: str, inner: str = "") -> None:
        self._flush()
        tag = rect_tag(int(x), int(y), int(w), int(h), fill, inner)
        if tag:
            self.parts.append([tag])

    def xml(self, snippet: str) -> None:
        self._flush()
        self.parts.append([snippet])

    def define(self, snippet: str) -> None:
        self.defs.append(snippet)

    def next_id(self, prefix: str) -> str:
        self._seq += 1
        return f"{prefix}{self._seq}"

    def draw_text(self, text: str, x: int, y: int, scale: int, fill: str, spacing: int | None = None) -> int:
        width = measure(text, scale, spacing)
        height = GLYPH_H * scale
        if x < 0 or y < 0 or x + width > self.w or y + height > self.h:
            raise SystemExit(
                f"text overflow {text!r} at ({x},{y}) size {width}x{height} canvas {self.w}x{self.h}"
            )
        return blit_text(self.bag, text, x, y, scale, fill, spacing)

    def draw_text_centered(self, text: str, cx: int, y: int, scale: int, fill: str, spacing: int | None = None) -> int:
        width = measure(text, scale, spacing)
        return self.draw_text(text, int(cx - width / 2), y, scale, fill, spacing)

    def text(
        self,
        content: str,
        x: int,
        y: int,
        size: int,
        fill: str,
        weight: int = 600,
        anchor: str = "middle",
        spacing: str = "0",
        opacity: str | None = None,
        inner: str = "",
    ) -> None:
        op = f' opacity="{opacity}"' if opacity is not None else ""
        self.xml(
            f'<text x="{int(x)}" y="{int(y)}" text-anchor="{anchor}" '
            f'font-family="{SANS}" font-size="{size}" font-weight="{weight}" fill="{fill}" '
            f'letter-spacing="{spacing}"{op} '
            'shape-rendering="geometricPrecision" text-rendering="geometricPrecision">'
            f"{inner}{html.escape(content)}</text>"
        )

    def blit_art(self, art: str, cmap: dict[str, str], ox: int, oy: int, scale: int) -> tuple[int, int]:
        rows = parse_art(art)
        blit(self.bag, rows, cmap, ox, oy, scale)
        return len(rows[0]) * scale, len(rows) * scale

    def to_svg(self, title: str, desc: str) -> str:
        self._flush()
        body: list[str] = []
        if self.bg:
            body.append(rect_tag(0, 0, self.w, self.h, self.bg))
        if self.defs:
            body.append("<defs>" + "".join(self.defs) + "</defs>")
        for part in self.parts:
            body.extend(part)
        inner = "\n".join(body)
        return (
            '<?xml version="1.0" encoding="UTF-8"?>\n'
            f'<svg xmlns="http://www.w3.org/2000/svg" width="{self.w}" height="{self.h}" '
            f'viewBox="0 0 {self.w} {self.h}" role="img" shape-rendering="crispEdges">\n'
            f"<title>{html.escape(title)}</title>\n"
            f"<desc>{html.escape(desc)}</desc>\n"
            f"{inner}\n"
            "</svg>\n"
        )


def save_svg(path: Path | str, scene: Scene, title: str, desc: str) -> None:
    destination = Path(path)
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(scene.to_svg(title, desc), encoding="utf-8")
    print(f"wrote {destination} ({destination.stat().st_size} bytes)")


def _sway(values: str, dur: str, begin: str = "0s") -> str:
    return (
        '<animateTransform attributeName="transform" attributeType="XML" type="translate" '
        f'dur="{dur}" begin="{begin}" repeatCount="indefinite" calcMode="discrete" values="{values}"/>'
    )


def _curtain_group(palette: dict, x: int, y: int, height: int, sway: str, begin: str) -> str:
    colors = [
        palette["curtain_dark"],
        palette["curtain"],
        palette["curtain_hi"],
        palette["curtain"],
        palette["curtain_dark"],
    ]
    stripe = 5
    parts = [_sway(sway, "4.8s", begin)]
    for i in range(8):
        parts.append(rect_tag(x + i * stripe, y, stripe, height, colors[i % 5]))
    # A darker inner hem so the drape reads as folded cloth.
    hem_x = x + 8 * stripe - 3 if begin == "0s" else x
    parts.append(rect_tag(hem_x, y, 3, height, palette["curtain_dark"]))
    return "<g>" + "".join(parts) + "</g>"


def _valance(scene: Scene, palette: dict, x: int, y: int, width: int) -> None:
    colors = [palette["curtain"], palette["curtain_dark"], palette["curtain_hi"]]
    scallop = 18
    cx = x
    index = 0
    while cx < x + width:
        w = min(scallop, x + width - cx)
        color = colors[index % 3]
        scene.rect(cx, y, w, 5, color)
        if w > 10:
            scene.rect(cx + 3, y + 5, w - 6, 4, color)
            scene.rect(cx + 6, y + 9, w - 12, 3, palette["curtain_dark"])
        cx += scallop
        index += 1


def _bulbs(scene: Scene, palette: dict, y: int) -> None:
    left, right = 22, scene.w - 22
    count = 22
    span = right - left
    step = span / (count - 1)
    for i in range(count):
        x = int(left + i * step) - 6
        scene.rect(x, y, 12, 12, palette["ink"])
        delay = f"{(i % 6) * 0.18:.2f}s"
        pulse = (
            f'<animate attributeName="fill" dur="2.4s" begin="{delay}" repeatCount="indefinite" '
            f'calcMode="discrete" values="{palette["gold"]};{palette["gold_hi"]};{palette["gold"]}" '
            'keyTimes="0;0.5;1"/>'
        )
        scene.rect(x + 2, y + 2, 8, 8, palette["gold"], pulse)


def _ellipse(scene: Scene, cx: int, cy: int, rx: int, ry: int, color: str) -> None:
    for dy in range(-ry, ry + 1):
        span = int(rx * (1 - (dy * dy) / (ry * ry)) ** 0.5)
        if span > 0:
            scene.rect(cx - span, cy + dy, span * 2, 1, color)


def _frame(scene: Scene, color: str, thickness: int = 5) -> None:
    w, h, t = scene.w, scene.h, thickness
    scene.rect(0, 0, w, t, color)
    scene.rect(0, h - t, w, t, color)
    scene.rect(0, 0, t, h, color)
    scene.rect(w - t, 0, t, h, color)


def candy_frame(scene: Scene) -> None:
    """Pink and lemon stripe, the candy border used across the page."""
    w, h = scene.w, scene.h
    scene.rect(0, 0, w, 5, "#FF5C93")
    scene.rect(0, h - 5, w, 5, "#FF5C93")
    scene.rect(0, 0, 5, h, "#FF5C93")
    scene.rect(w - 5, 0, 5, h, "#FF5C93")
    scene.rect(5, 5, w - 10, 3, "#FFE14A")
    scene.rect(5, h - 8, w - 10, 3, "#FFE14A")
    scene.rect(5, 5, 3, h - 10, "#FFE14A")
    scene.rect(w - 8, 5, 3, h - 10, "#FFE14A")


def _bob(begin: str) -> str:
    return (
        '<animateTransform attributeName="transform" attributeType="XML" type="translate" '
        f'dur="1.8s" begin="{begin}" repeatCount="indefinite" calcMode="discrete" '
        'values="0,0;0,-6;0,0;0,-6;0,0"/>'
    )


def sprite_group(grid: list[str], ox: int, oy: int, scale: int, begin: str) -> str:
    parts = [_bob(begin)]
    for gy, row in enumerate(grid):
        for gx, ch in enumerate(row):
            color = EXACT_COLORS.get(ch)
            if not color:
                continue
            parts.append(rect_tag(ox + gx * scale, oy + gy * scale, scale, scale, color))
    return "<g>" + "".join(parts) + "</g>"


def _cloud(scene: Scene, x: int, y: int, color: str) -> None:
    scene.rect(x + 8, y, 22, 8, color)
    scene.rect(x, y + 6, 40, 12, color)
    scene.rect(x + 10, y + 16, 20, 6, color)


def _spark(scene: Scene, x: int, y: int, color: str, begin: str) -> None:
    pulse = (
        f'<animate attributeName="fill-opacity" dur="2.4s" begin="{begin}" '
        'repeatCount="indefinite" calcMode="discrete" values="1;0.25;1" keyTimes="0;0.5;1"/>'
    )
    scene.rect(x + 2, y, 2, 6, color, pulse)
    scene.rect(x, y + 2, 6, 2, color)


def _lemon_tower(scene: Scene, x: int, top: int, height: int) -> None:
    yellow, shade, outline = "#F9FB00", "#DEA900", "#3D2F30"
    scene.rect(x + 16, top, 10, 6, outline)
    scene.rect(x + 18, top + 2, 6, 4, yellow)
    scene.rect(x + 8, top + 6, 26, 14, yellow)
    scene.rect(x + 10, top + 8, 6, 10, shade)
    scene.rect(x + 2, top + 18, 38, height - 28, yellow)
    scene.rect(x + 4, top + 22, 8, height - 40, shade)
    scene.rect(x + 16, top + height // 2, 10, 12, outline)
    scene.rect(x + 18, top + height // 2 + 2, 6, 8, "#7ED4FF")
    scene.rect(x, top + height - 8, 42, 8, outline)


def _typing_line(scene: Scene, text: str, y: int, scale: int, fill: str, slot: int, slots: int, cursor: str) -> None:
    width = measure(text, scale)
    x = int((scene.w - width) / 2)
    height = GLYPH_H * scale
    if x < 8 or x + width > scene.w - 8 or y + height > scene.h:
        raise SystemExit(f"rotator overflow {text!r}")
    bag: dict[tuple[int, int], str] = {}
    blit_text(bag, text, x, y, scale, fill)
    rects = compress(bag)
    clip_id = scene.next_id("type")
    edges = char_edges(text, scale)
    full = edges[-1]
    start = slot / slots
    reveal = start + 0.10
    # Line one is already on stage at t=0, so a first paint and a paused
    # viewer still read a complete sentence. The other lines type on.
    if slot == 0:
        values = [full, full]
        times = [0, 1]
    else:
        values = [0, 0, *edges, full]
        times = [0, start]
        steps = len(edges)
        for i in range(steps):
            times.append(start + (reveal - start) * ((i + 1) / steps))
        times.append(1)
    # Keep keyTimes monotonic and closed on [0, 1].
    cleaned = [0.0]
    for stamp in times[1:-1]:
        cleaned.append(max(cleaned[-1], round(stamp, 4)))
    cleaned.append(1.0)
    if len(cleaned) != len(values):
        raise SystemExit(f"keyframe mismatch for {text!r}: {len(values)} values, {len(cleaned)} times")
    value_attr = ";".join(str(int(v)) for v in values)
    time_attr = ";".join("0" if t == 0 else "1" if t == 1 else f"{t:.4f}".rstrip("0") for t in cleaned)
    scene.define(
        f'<clipPath id="{clip_id}"><rect x="{x}" y="{y}" width="{full}" height="{height}">'
        f'<animate attributeName="width" dur="20s" repeatCount="indefinite" calcMode="linear" '
        f'values="{value_attr}" keyTimes="{time_attr}"/>'
        "</rect></clipPath>"
    )
    opacity_values = ["0"] * slots
    opacity_values[slot] = "1"
    # Base opacity matches the first frame so a viewer without SMIL still reads line one.
    base = "1" if slot == 0 else "0"
    keys = ";".join(str(i / slots) for i in range(slots)) + ";1"
    vals = ";".join(opacity_values) + f";{opacity_values[0]}"
    blink = (
        f'<rect x="{x + width + scale}" y="{y}" width="{scale * 2}" height="{height}" fill="{cursor}" fill-opacity="1">'
        '<animate attributeName="fill-opacity" dur="1.1s" repeatCount="indefinite" calcMode="discrete" '
        'values="1;1;0;0" keyTimes="0;0.49;0.5;1"/>'
        "</rect>"
    )
    # The cursor sits outside the reveal clip, or the clip cuts it off
    # for the whole line. Opacity still hides it on the other lines.
    group = (
        f'<g opacity="{base}">'
        f'<animate attributeName="opacity" dur="20s" repeatCount="indefinite" calcMode="discrete" '
        f'values="{vals}" keyTimes="{keys}"/>'
        f'<g clip-path="url(#{clip_id})">'
        + "".join(rects)
        + "</g>"
        + blink
        + "</g>"
    )
    scene.xml(group)


def _crossfade(scene: Scene, lines: list[str], x: int, y: int, size: int, fill: str) -> None:
    """Swap complete lines. A type-on clip left the sentence unreadable mid-cycle."""
    slots = len(lines)
    keys = ";".join(str(i / slots) for i in range(slots)) + ";1"
    for index, line in enumerate(lines):
        values = ["0"] * slots
        values[index] = "1"
        vals = ";".join(values) + f";{values[0]}"
        animate = (
            '<animate attributeName="opacity" dur="20s" repeatCount="indefinite" calcMode="discrete" '
            f'values="{vals}" keyTimes="{keys}"/>'
        )
        scene.text(line, x, y, size, fill, weight=560, spacing="0.2", opacity="1" if index == 0 else "0", inner=animate)


def build_hero(palette: dict) -> Scene:
    """Daytime or twilight header. Pixel landscape, modern type, two Lemongrab twins."""
    w, h = 920, 460
    scene = Scene(w, h, palette["bg"])
    night = palette["night"]
    if night:
        for sx, sy in (
            (36, 22), (110, 36), (188, 18), (760, 24),
            (820, 40), (870, 16), (250, 28), (680, 20),
        ):
            scene.rect(sx, sy, 3, 3, "#FFF6C2")
        _spark(scene, 150, 26, "#FFF6C2", "0s")
        _spark(scene, 790, 30, "#FFE14A", "0.6s")
    else:
        for cx, cy in ((24, 12), (168, 18), (748, 14), (820, 20)):
            _cloud(scene, cx, cy, palette["cloud"])
        _spark(scene, 140, 24, "#FFFFFF", "0s")
        _spark(scene, 700, 22, "#FFE14A", "0.7s")

    _lemon_tower(scene, 28, 150, 230)
    _lemon_tower(scene, 112, 198, 170)
    _lemon_tower(scene, 768, 180, 190)
    _lemon_tower(scene, 850, 140, 240)

    hill_y = 372
    scene.rect(0, hill_y, w, h - hill_y, palette["hill"])
    _ellipse(scene, 180, hill_y, 200, 34, palette["hill_hi"])
    _ellipse(scene, 480, hill_y + 6, 240, 40, palette["hill"])
    _ellipse(scene, 780, hill_y, 190, 32, palette["hill_dark"])
    for gx, gy in ((70, hill_y - 8), (240, hill_y - 4), (520, hill_y - 10), (700, hill_y - 6), (860, hill_y - 8)):
        scene.rect(gx + 2, gy, 4, 10, palette["hill_dark"])
        scene.rect(gx, gy + 4, 10, 6, palette["hill_hi"])

    scene.text("Mark Jayson Martinez Farol", w // 2, 74, 40, palette["marquee"], weight=700, spacing="-0.4")
    scene.rect(w // 2 - 28, 92, 40, 4, "#FFE14A")
    scene.rect(w // 2 + 16, 92, 12, 4, "#FF5C93")
    scene.text("Quantitative economist  ·  Las Vegas", w // 2, 120, 18, palette["role"], weight=560, spacing="0.3")
    _crossfade(
        scene,
        [
            "Research-grade panels",
            "147,782 × 2,676 IPEDS file",
            "A 39-check acceptance audit",
            "IPEDS, 2004–2024",
            "Open to economist roles",
        ],
        w // 2,
        152,
        18,
        palette["rotator"],
    )

    scale = 6
    sprite_h = 29 * scale
    sprite_w = 23 * scale
    gap = 28
    pair = sprite_w * 2 + gap
    left = (w - pair) // 2
    top = hill_y - sprite_h + 18
    scene.xml(sprite_group(WHITE_GRID, left, top, scale, "0s"))
    scene.xml(sprite_group(FRONT_GRID, left + sprite_w + gap, top, scale, "0.45s"))

    candy_frame(scene)
    return scene


def build_stats(palette: dict) -> Scene:
    w, h = 900, 248
    scene = Scene(w, h, palette["bg"])
    cards = [
        ("147,782", "rows × 2,676 columns", "2004–2024 IPEDS", 0),
        ("141,711", "rows × 2,721 columns", "Labeled release v1", 1),
        ("39", "acceptance checks", "Audit", 2),
        ("25+ years", "Title IV volume", "Federal Student Aid", 3),
        ("200+", "students", "Each term", 4),
        ("10", "researchers", "Mentored", 5),
    ]
    margin, gap = 12, 12
    card_w = (w - margin * 2 - gap * 2) // 3
    card_h = 104
    for index, (big, mid, small, accent_i) in enumerate(cards):
        col, row = index % 3, index // 3
        x = margin + col * (card_w + gap)
        y = margin + row * (card_h + gap)
        accent = palette["accents"][accent_i]
        scene.rect(x, y, card_w, card_h, palette["gold"])
        scene.rect(x + 3, y + 3, card_w - 6, card_h - 6, palette["ticket"])
        scene.rect(x + 3, y + 3, 8, card_h - 6, accent)
        for hole_y in (y + 18, y + card_h // 2 - 3, y + card_h - 24):
            scene.rect(x + 5, hole_y, 5, 5, palette["bg"])
        cx = x + 18 + (card_w - 28) // 2
        scene.text(big, cx, y + 48, 28, accent, weight=720, spacing="-0.4")
        scene.text(mid, cx, y + 72, 14, palette["ticket_ink"], weight=600)
        scene.text(small, cx, y + 90, 13, palette["muted"], weight=500)
    candy_frame(scene)
    return scene


def build_divider() -> Scene:
    w, h = 920, 40
    scene = Scene(w, h, None)
    for x in range(16, w - 16, 16):
        scene.rect(x, 18, 10, 4, "#FF5C93" if (x // 16) % 2 == 0 else "#FFE14A")
    # Lemon drops and grass tufts.
    for x, color in ((48, "#F9FB00"), (120, "#FF5C93"), (800, "#5EECC0"), (860, "#F9FB00")):
        scene.rect(x, 8, 14, 10, color)
        scene.rect(x + 4, 4, 6, 6, color)
        scene.rect(x + 2, 16, 10, 4, "#3D2F30")
    for x in (200, 460, 680):
        scene.rect(x + 3, 8, 4, 12, "#1F8A3C")
        scene.rect(x, 14, 12, 6, "#8BE56E")
    return scene


def build_pipeline(palette: dict) -> Scene:
    w, h = 900, 236
    scene = Scene(w, h, palette["bg"])
    headers = ["Sources", "Pipelines", "Output"]
    columns = [
        ["NCES / IPEDS", "Student aid", "FRED, BEA, BLS", "Census and World Bank"],
        ["mdb-tools", "DuckDB and SQL", "Harmonize", "QA / QC gate"],
        ["Year panels", "Macro by Mark", "Working papers", "Replication"],
    ]
    box_w, box_h = 250, 168
    gap = 46
    origin_x, origin_y = 20, 44
    scene.text("From the archive to the stage", w // 2, 28, 16, palette["marquee"], weight=650)
    for index, (header, lines) in enumerate(zip(headers, columns)):
        x = origin_x + index * (box_w + gap)
        scene.rect(x, origin_y, box_w, box_h, palette["gold"])
        scene.rect(x + 3, origin_y + 3, box_w - 6, box_h - 6, palette["ticket"])
        pulse = (
            '<animate attributeName="fill" dur="3.6s" repeatCount="indefinite" calcMode="discrete" '
            f'begin="{index * 0.45:.2f}s" values="{palette["gold"]};{palette["gold_hi"]};{palette["gold"]};{palette["gold"]}" '
            'keyTimes="0;0.2;0.4;1"/>'
        )
        scene.rect(x + 3, origin_y + 3, box_w - 6, 32, palette["gold"], pulse)
        scene.text(header, x + box_w // 2, origin_y + 25, 15, "#1B140F", weight=700)
        line_y = origin_y + 58
        for line in lines:
            scene.text(line, x + box_w // 2, line_y, 15, palette["ticket_ink"], weight=560)
            line_y += 26
        if index < 2:
            ax = x + box_w + 8
            ay = origin_y + box_h // 2
            scene.rect(ax, ay, gap - 18, 4, palette["gold"])
            scene.rect(ax + gap - 22, ay - 5, 4, 14, palette["gold"])
            scene.rect(ax + gap - 18, ay - 2, 4, 8, palette["gold_hi"])
    candy_frame(scene)
    return scene


def build_footer(palette: dict) -> Scene:
    w, h = 920, 148
    scene = Scene(w, h, palette["bg"])
    hill_y = 108
    scene.rect(0, hill_y, w, h - hill_y, palette["hill"])
    _ellipse(scene, 160, hill_y, 140, 22, palette["hill_hi"])
    _ellipse(scene, 760, hill_y, 150, 22, palette["hill_dark"])
    scale = 3
    top = h - 10 - 29 * scale
    scene.xml(sprite_group(WHITE_GRID, 18, top, scale, "0.2s"))
    scene.xml(sprite_group(FRONT_GRID, w - 18 - 23 * scale, top, scale, "0.7s"))
    scene.text("Mark Jayson Martinez Farol", w // 2, 42, 26, palette["marquee"], weight=700, spacing="-0.3")
    scene.text("Las Vegas", w // 2, 70, 16, palette["role"], weight=560, spacing="0.4")
    candy_frame(scene)
    return scene


def _icon_colors(accent: str) -> dict[str, str]:
    return {"K": "#2A160E", "Y": accent, "B": "#1A100C", "P": "#FF4D88", "L": "#3CAA62", ".": ""}


def build_poster(title: str, subtitle: str, accent: str, icon: str) -> Scene:
    w, h = 880, 96
    scene = Scene(w, h, "#FFF8E6")
    scene.rect(0, 0, w, h, "#FF5C93")
    scene.rect(5, 5, w - 10, h - 10, "#FFE566")
    scene.rect(9, 9, w - 18, h - 18, "#FFF8E6")
    scene.rect(9, 9, 8, h - 18, accent)
    rows = parse_art(ICONS[icon])
    blit(scene.bag, rows, _icon_colors(accent), 28, 28, 4)
    scene.text(title, 112, 42, 22, "#1B140F", weight=700, anchor="start", spacing="-0.2")
    scene.text(subtitle, 112, 68, 15, "#5C4636", weight=500, anchor="start")
    chevron = ["#..", "##.", "###", "##.", "#.."]
    ox, oy = w - 42, 30
    bag = scene.bag
    for gy, row in enumerate(chevron):
        for gx, bit in enumerate(row):
            if bit == "#":
                for dy in range(3):
                    for dx in range(3):
                        bag[(ox + gx * 3 + dx, oy + gy * 3 + dy)] = "#FF5C93"
    return scene


def build_link(label: str, accent: str) -> Scene:
    # Generous width so a system face never clips the label.
    w = max(148, 28 + len(label) * 11)
    h = 48
    scene = Scene(w, h, "#FFF8E6")
    scene.rect(0, 0, w, h, accent)
    scene.rect(4, 4, w - 8, h - 8, "#FFF8E6")
    scene.text(label, w // 2, 31, 16, "#1B140F", weight=650, spacing="0.2")
    return scene


def contribution_level(count: int, maximum: int) -> int:
    if count <= 0 or maximum <= 0:
        return 0
    ratio = count / maximum
    if ratio <= 0.25:
        return 1
    if ratio <= 0.5:
        return 2
    if ratio <= 0.75:
        return 3
    return 4


def build_quest(palette: dict, weeks: list[list[tuple[str, int]]], total: int, start_label: str, end_label: str) -> Scene:
    w = 900
    step, cell = 15, 12
    cols = max(len(weeks), 1)
    grid_w = cols * step
    left = (w - grid_w) // 2
    top = 88
    h = top + 7 * step + 42
    scene = Scene(w, h, palette["bg"])
    scene.text("This season", 28, 36, 26, palette["marquee"], weight=700, anchor="start", spacing="-0.3")
    span = f"{start_label} – {end_label}"
    scene.text(span, 28, 62, 15, palette["muted"], weight=500, anchor="start")
    total_text = f"{total:,}"
    scene.text(total_text, w - 28, 38, 30, palette["marquee"], weight=720, anchor="end", spacing="-0.4")
    scene.text("Public contributions", w - 28, 62, 14, palette["muted"], weight=500, anchor="end")

    counts = [count for week in weeks for _, count in week]
    maximum = max(counts) if counts else 0
    colors = [palette["q0"], palette["q1"], palette["q2"], palette["q3"], palette["q4"]]
    import datetime

    for col, week in enumerate(weeks):
        for date, count in week:
            day = datetime.date.fromisoformat(date)
            row = (day.weekday() + 1) % 7
            color = colors[contribution_level(count, maximum)]
            scene.rect(left + col * step, top + row * step, cell, cell, color)

    legend_y = top + 7 * step + 10
    scene.text("Quiet", 28, legend_y + 11, 13, palette["muted"], weight=560, anchor="start")
    lx = 84
    for level in range(5):
        scene.rect(lx + level * 18, legend_y, 12, 12, colors[level])
    scene.text("Busy", lx + 5 * 18 + 8, legend_y + 11, 13, palette["muted"], weight=560, anchor="start")
    candy_frame(scene)
    return scene


def build_font_proof() -> Scene:
    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.,-/+':!?"
    scale = 4
    scene = Scene(760, 220, "#FFF6DC")
    x, y = 12, 12
    for ch in chars:
        scene.draw_text(ch, x, y, scale, "#2A160E")
        x += 36
        if x > 720:
            x = 12
            y += 40
    return scene
