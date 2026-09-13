"""Create the vector PDF export corresponding to figures/ps1_teaser.drawio."""

from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor


OUT = "figures/ps1_teaser.pdf"
PAGE_W, PAGE_H = 506.0, 150.7458
SX, SY = PAGE_W / 960.0, PAGE_H / 286.0
INK = HexColor("#18324A")
BLUE = HexColor("#315EFB")
TEAL = HexColor("#14877D")


def x(value):
    return value * SX


def y(value):
    return PAGE_H - value * SY


def label(c, text, cx, baseline, size, color=INK, bold=False):
    c.setFillColor(color)
    c.setFont("Helvetica-Bold" if bold else "Helvetica", size * SY)
    c.drawCentredString(x(cx), y(baseline), text)


def arrow(c, x1, y1, x2, y2, color, dashed=False):
    c.setStrokeColor(color)
    c.setFillColor(color)
    c.setLineWidth(1.6 * SX)
    c.setDash(4 * SX, 3 * SX) if dashed else c.setDash()
    c.line(x(x1), y(y1), x(x2), y(y2))
    c.setDash()
    if abs(x2 - x1) >= abs(y2 - y1):
        c.wedge(x(x2 - 7), y(y2 + 4), x(x2 + 1), y(y2 - 4), 0, 360, fill=1, stroke=0)
    else:
        c.wedge(x(x2 - 4), y(y2 - 1), x(x2 + 4), y(y2 + 7), 0, 360, fill=1, stroke=0)


def main():
    c = canvas.Canvas(OUT, pagesize=(PAGE_W, PAGE_H))

    label(c, "Economics", 150, 19, 20, bold=True)
    label(c, "Harsanyi (1968); Crawford & Sobel (1982)", 150, 45, 13)
    label(c, "Computer science", 480, 19, 20, bold=True)
    label(c, "Watkins & Dayan (1992); Leung et al. (2026)", 480, 45, 13)
    label(c, "Behavioral science", 810, 19, 20, bold=True)
    label(c, "Sommerfeld et al. (2007)", 810, 45, 15)

    c.setStrokeColor(BLUE)
    c.setLineWidth(1.6 * SX)
    c.rect(x(66), y(121), x(170), (121 - 63) * SY, fill=0, stroke=1)
    c.line(x(66), y(92), x(236), y(92))
    c.line(x(151), y(63), x(151), y(121))
    for text, cx, by in [("3, 3", 108.5, 83), ("0, 4", 193.5, 83), ("4, 0", 108.5, 112), ("1, 1", 193.5, 112)]:
        label(c, text, cx, by, 18)

    for left, text in [(347, "None"), (435, "Report"), (523, "Verify")]:
        c.rect(x(left), y(118), x(70), (118 - 65) * SY, fill=0, stroke=1)
        label(c, text, left + 35, 95, 16)
    arrow(c, 418, 91, 432, 91, BLUE)
    arrow(c, 506, 91, 520, 91, BLUE)

    c.setStrokeColor(TEAL)
    c.setLineWidth(1.6 * SX)
    for cx in (731, 831):
        c.circle(x(cx), y(78), x(13), fill=0, stroke=1)
        c.line(x(cx), y(96), x(cx), y(113))
        c.line(x(cx), y(100), x(cx - 21), y(112))
        c.line(x(cx), y(100), x(cx + 21), y(112))
    arrow(c, 764, 91, 807, 91, TEAL)

    label(c, "Truthful reporting + defection", 150, 151, 17)
    label(c, "Vary rewards, costs, and sanctions", 150, 178, 14, TEAL)
    label(c, "Epsilon-greedy Q-learning", 480, 151, 18)
    label(c, "No report / strategic / verified", 480, 178, 14, TEAL)
    label(c, "Calibrated trust vs payoff learning", 810, 151, 15)
    label(c, "Compare report use and cooperation", 810, 178, 14, TEAL)

    for cx in (150, 480, 810):
        arrow(c, cx, 187, cx, 207, TEAL, dashed=True)
    c.setStrokeColor(TEAL)
    c.setLineWidth(1.6 * SX)
    c.rect(x(55), y(260), x(850), (260 - 207) * SY, fill=0, stroke=1)
    label(c, "When does third-party information sustain cooperation?", 480, 228, 20, bold=True)
    label(c, "Honesty | report use | cooperation | exploitation | welfare", 480, 252, 16)
    label(c, "Dashed arrows = interdisciplinary test; all reported outcomes are simulated.", 480, 281, 14)

    c.showPage()
    c.save()


if __name__ == "__main__":
    main()
