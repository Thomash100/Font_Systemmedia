from fontTools.fontBuilder import FontBuilder
from fontTools.pens.ttGlyphPen import TTGlyphPen
from fontTools.ttLib import TTFont
import math
import os
import re


GLYPHS = {
    "A": {"w": 100, "p": ["M14 106 L47 16 Q50 9 53 16 L86 106", "M29 76 L71 76"]},
    "B": {"w": 92, "p": ["M18 14 L62 14 Q82 14 82 36 Q82 55 62 55 L18 55", "M18 55 L66 55 Q84 55 84 80 Q84 106 62 106 L18 106 L18 14"]},
    "C": {"w": 94, "p": ["M82 18 L31 18 Q14 18 14 38 L14 82 Q14 102 31 102 L82 102"]},
    "D": {"w": 94, "p": ["M18 14 L62 14 Q84 14 84 40 L84 80 Q84 106 62 106 L18 106 L18 14"]},
    "E": {"w": 90, "p": ["M80 16 L18 16 L18 104 L80 104", "M18 60 L70 60"]},
    "F": {"w": 86, "p": ["M78 16 L18 16 L18 104", "M18 60 L68 60"]},
    "G": {"w": 98, "p": ["M84 18 L32 18 Q14 18 14 38 L14 82 Q14 102 32 102 L84 102 L84 66 L56 66"]},
    "H": {"w": 96, "p": ["M18 16 L18 104", "M78 16 L78 104", "M18 60 L78 60"]},
    "I": {"w": 46, "p": ["M23 16 L23 104"]},
    "J": {"w": 78, "p": ["M60 16 L60 82 Q60 104 37 104 L14 104"]},
    "K": {"w": 92, "p": ["M18 16 L18 104", "M78 16 L34 60 L80 104"]},
    "L": {"w": 82, "p": ["M18 16 L18 104 L74 104"]},
    "M": {"w": 116, "p": ["M16 104 L16 18 Q16 10 23 17 L58 56 L93 17 Q100 10 100 18 L100 104"]},
    "N": {"w": 102, "p": ["M18 104 L18 18 Q18 10 25 18 L84 104", "M84 104 L84 16"]},
    "O": {"w": 100, "p": ["M34 16 L66 16 Q86 16 86 38 L86 82 Q86 104 66 104 L34 104 Q14 104 14 82 L14 38 Q14 16 34 16"]},
    "P": {"w": 90, "p": ["M18 104 L18 16 L64 16 Q82 16 82 40 Q82 62 64 62 L18 62"]},
    "Q": {"w": 104, "p": ["M34 16 L66 16 Q86 16 86 38 L86 82 Q86 104 66 104 L34 104 Q14 104 14 82 L14 38 Q14 16 34 16", "M62 82 L90 108"]},
    "R": {"w": 94, "p": ["M18 104 L18 16 L64 16 Q82 16 82 40 Q82 62 64 62 L18 62", "M56 62 L84 104"]},
    "S": {"w": 92, "p": ["M80 17 L30 17 Q14 17 14 38 Q14 58 32 58 L62 58 Q80 58 80 80 Q80 103 62 103 L14 103"]},
    "T": {"w": 92, "p": ["M12 16 L80 16", "M46 16 L46 104"]},
    "U": {"w": 98, "p": ["M18 16 L18 76 Q18 104 49 104 Q80 104 80 76 L80 16"]},
    "V": {"w": 98, "p": ["M14 16 L48 104 Q50 110 52 104 L86 16"]},
    "W": {"w": 128, "p": ["M14 16 L34 104 Q36 110 40 102 L64 50 L88 102 Q92 110 94 104 L114 16"]},
    "X": {"w": 96, "p": ["M16 16 L80 104", "M80 16 L16 104"]},
    "Y": {"w": 96, "p": ["M14 16 L48 58 L82 16", "M48 58 L48 104"]},
    "Z": {"w": 90, "p": ["M14 16 L78 16 L14 104 L80 104"]},
    "0": {"w": 96, "p": ["M32 16 L64 16 Q82 16 82 38 L82 82 Q82 104 64 104 L32 104 Q14 104 14 82 L14 38 Q14 16 32 16", "M68 28 L28 92"]},
    "1": {"w": 58, "p": ["M30 104 L30 16 L14 32"]},
    "2": {"w": 88, "p": ["M14 34 Q14 16 36 16 L60 16 Q78 16 78 38 Q78 56 58 68 L16 104 L80 104"]},
    "3": {"w": 88, "p": ["M16 16 L60 16 Q78 16 78 38 Q78 58 58 58", "M58 58 Q80 58 80 80 Q80 104 58 104 L14 104"]},
    "4": {"w": 92, "p": ["M72 104 L72 16", "M72 64 L14 64 L58 16"]},
    "5": {"w": 88, "p": ["M78 16 L20 16 L20 56 L58 56 Q80 56 80 80 Q80 104 58 104 L16 104"]},
    "6": {"w": 90, "p": ["M76 16 L34 16 Q16 16 16 40 L16 82 Q16 104 38 104 L58 104 Q80 104 80 80 Q80 58 58 58 L16 58"]},
    "7": {"w": 84, "p": ["M12 16 L76 16 L34 104"]},
    "8": {"w": 92, "p": ["M34 16 L58 16 Q78 16 78 38 Q78 58 58 58 L34 58 Q14 58 14 38 Q14 16 34 16", "M34 58 L60 58 Q82 58 82 80 Q82 104 60 104 L32 104 Q12 104 12 80 Q12 58 34 58"]},
    "9": {"w": 90, "p": ["M74 62 L34 62 Q14 62 14 40 Q14 16 36 16 L56 16 Q76 16 76 40 L76 80 Q76 104 54 104 L18 104"]},
    "-": {"w": 62, "p": ["M14 60 L48 60"]},
    ".": {"w": 38, "p": ["M20 100 L21 100"]},
    "/": {"w": 72, "p": ["M58 16 L14 104"]},
    " ": {"w": 48, "p": []},
}

LAYER_STROKES = {
    "Outer": 180,
    "Channel": 95,
    "Accent": 38,
}

SCALE = 8
TOP = 960
TRACKING = 13 * SCALE
UNITS_PER_EM = 1000


def glyph_name(char):
    names = {" ": "space", "-": "hyphen", ".": "period", "/": "slash"}
    if char in names:
        return names[char]
    if char.isdigit():
        return "zero one two three four five six seven eight nine".split()[int(char)]
    return char


def transform(point):
    x, y = point
    return (x * SCALE, TOP - y * SCALE)


def parse_path(path):
    tokens = re.findall(r"[MLQ]|-?\d+(?:\.\d+)?", path)
    index = 0
    current = None
    points = []
    while index < len(tokens):
        command = tokens[index]
        index += 1
        if command == "M":
            current = (float(tokens[index]), float(tokens[index + 1]))
            index += 2
            points.append(current)
        elif command == "L":
            current = (float(tokens[index]), float(tokens[index + 1]))
            index += 2
            points.append(current)
        elif command == "Q":
            control = (float(tokens[index]), float(tokens[index + 1]))
            end = (float(tokens[index + 2]), float(tokens[index + 3]))
            index += 4
            start = current
            for step in range(1, 13):
                t = step / 12
                x = (1 - t) ** 2 * start[0] + 2 * (1 - t) * t * control[0] + t**2 * end[0]
                y = (1 - t) ** 2 * start[1] + 2 * (1 - t) * t * control[1] + t**2 * end[1]
                points.append((x, y))
            current = end
    return [transform(point) for point in points]


def add_polygon(pen, points):
    if len(points) < 3:
        return
    pen.moveTo((round(points[0][0]), round(points[0][1])))
    for point in points[1:]:
        pen.lineTo((round(point[0]), round(point[1])))
    pen.closePath()


def add_circle(pen, center, radius, segments=18):
    cx, cy = center
    points = []
    for index in range(segments):
        angle = math.tau * index / segments
        points.append((cx + math.cos(angle) * radius, cy + math.sin(angle) * radius))
    add_polygon(pen, points)


def add_capsule(pen, start, end, radius):
    x1, y1 = start
    x2, y2 = end
    dx = x2 - x1
    dy = y2 - y1
    length = math.hypot(dx, dy)
    if length < 1:
        add_circle(pen, start, radius)
        return
    nx = -dy / length * radius
    ny = dx / length * radius
    add_polygon(pen, [(x1 + nx, y1 + ny), (x2 + nx, y2 + ny), (x2 - nx, y2 - ny), (x1 - nx, y1 - ny)])
    add_circle(pen, start, radius)
    add_circle(pen, end, radius)


def build_glyph(char, stroke_width):
    pen = TTGlyphPen(None)
    if char != " ":
        radius = stroke_width / 2
        for path in GLYPHS[char]["p"]:
            points = parse_path(path)
            for index in range(len(points) - 1):
                add_capsule(pen, points[index], points[index + 1], radius)
    return pen.glyph()


def make_font(layer, stroke_width, output_dir):
    family = f"SYSTEMMEDIA {layer}"
    glyph_order = [".notdef"] + [glyph_name(char) for char in GLYPHS.keys()]
    char_to_name = {char: glyph_name(char) for char in GLYPHS.keys()}
    glyphs = {".notdef": TTGlyphPen(None).glyph()}
    metrics = {".notdef": (600, 0)}
    cmap = {}

    for char, data in GLYPHS.items():
        name = char_to_name[char]
        glyphs[name] = build_glyph(char, stroke_width)
        metrics[name] = (int(data["w"] * SCALE + TRACKING), 0)
        cmap[ord(char)] = name

    builder = FontBuilder(UNITS_PER_EM, isTTF=True)
    builder.setupGlyphOrder(glyph_order)
    builder.setupCharacterMap(cmap)
    builder.setupGlyf(glyphs)
    builder.setupHorizontalMetrics(metrics)
    builder.setupHorizontalHeader(ascent=900, descent=-200)
    builder.setupOS2(
        sTypoAscender=900,
        sTypoDescender=-200,
        usWinAscent=1050,
        usWinDescent=250,
        fsSelection=0x40,
    )
    builder.setupNameTable(
        {
            "familyName": family,
            "styleName": "Regular",
            "uniqueFontIdentifier": f"SYSTEMMEDIA {layer} Regular",
            "fullName": f"SYSTEMMEDIA {layer} Regular",
            "psName": f"SYSTEMMEDIA-{layer}",
            "version": "Version 1.000",
        }
    )
    builder.setupPost()
    builder.setupMaxp()
    font = builder.font

    ttf_path = os.path.join(output_dir, f"SYSTEMMEDIA-{layer}.ttf")
    woff_path = os.path.join(output_dir, f"SYSTEMMEDIA-{layer}.woff")
    font.save(ttf_path)

    webfont = TTFont(ttf_path)
    webfont.flavor = "woff"
    webfont.save(woff_path)
    return ttf_path, woff_path


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    output_dir = os.path.join(here, "dist", "fonts")
    os.makedirs(output_dir, exist_ok=True)
    for layer, stroke_width in LAYER_STROKES.items():
        ttf_path, woff_path = make_font(layer, stroke_width, output_dir)
        print(f"built {ttf_path}")
        print(f"built {woff_path}")


if __name__ == "__main__":
    main()
