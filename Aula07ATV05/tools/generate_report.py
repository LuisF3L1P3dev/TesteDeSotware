from __future__ import annotations

import html
import re
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.platypus import (
    KeepTogether,
    PageBreak,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)


ACTIVITY_DIR = Path(__file__).resolve().parents[1]
REPOSITORY_DIR = ACTIVITY_DIR.parent
SOURCE_PATH = ACTIVITY_DIR / "relatorio-tecnico-identifier.md"
OUTPUT_PATH = REPOSITORY_DIR / "output" / "pdf" / "relatorio-tecnico-identifier.pdf"


def register_fonts() -> tuple[str, str, str]:
    regular = Path("C:/Windows/Fonts/arial.ttf")
    bold = Path("C:/Windows/Fonts/arialbd.ttf")
    mono = Path("C:/Windows/Fonts/consola.ttf")
    if regular.exists() and bold.exists() and mono.exists():
        pdfmetrics.registerFont(TTFont("ReportRegular", regular))
        pdfmetrics.registerFont(TTFont("ReportBold", bold))
        pdfmetrics.registerFont(TTFont("ReportMono", mono))
        return "ReportRegular", "ReportBold", "ReportMono"
    return "Helvetica", "Helvetica-Bold", "Courier"


REGULAR_FONT, BOLD_FONT, MONO_FONT = register_fonts()


def inline_markup(value: str) -> str:
    value = html.escape(value.strip())
    value = re.sub(
        r"`([^`]+)`",
        lambda match: f'<font name="{MONO_FONT}" size="7.3">{match.group(1)}</font>',
        value,
    )
    value = re.sub(r"\*\*([^*]+)\*\*", r"<b>\1</b>", value)
    return value


def build_styles():
    styles = getSampleStyleSheet()
    styles.add(
        ParagraphStyle(
            name="ReportTitle",
            fontName=BOLD_FONT,
            fontSize=20,
            leading=24,
            textColor=colors.HexColor("#17365D"),
            alignment=TA_CENTER,
            spaceAfter=10,
        )
    )
    styles.add(
        ParagraphStyle(
            name="ReportSubtitle",
            fontName=REGULAR_FONT,
            fontSize=11,
            leading=15,
            textColor=colors.HexColor("#44546A"),
            alignment=TA_CENTER,
            spaceAfter=8,
        )
    )
    styles.add(
        ParagraphStyle(
            name="ReportH2",
            fontName=BOLD_FONT,
            fontSize=14,
            leading=18,
            textColor=colors.HexColor("#17365D"),
            spaceBefore=12,
            spaceAfter=7,
        )
    )
    styles.add(
        ParagraphStyle(
            name="ReportH3",
            fontName=BOLD_FONT,
            fontSize=11.5,
            leading=15,
            textColor=colors.HexColor("#2F5597"),
            spaceBefore=9,
            spaceAfter=5,
        )
    )
    styles.add(
        ParagraphStyle(
            name="ReportBody",
            fontName=REGULAR_FONT,
            fontSize=9.5,
            leading=13.5,
            alignment=TA_JUSTIFY,
            textColor=colors.HexColor("#222222"),
            spaceAfter=6,
        )
    )
    styles.add(
        ParagraphStyle(
            name="ReportBullet",
            parent=styles["ReportBody"],
            leftIndent=13,
            firstLineIndent=-7,
            bulletIndent=4,
            spaceAfter=3,
        )
    )
    styles.add(
        ParagraphStyle(
            name="TableHeader",
            fontName=BOLD_FONT,
            fontSize=7.2,
            leading=9,
            alignment=TA_LEFT,
            textColor=colors.white,
        )
    )
    styles.add(
        ParagraphStyle(
            name="TableCell",
            fontName=REGULAR_FONT,
            fontSize=7.1,
            leading=9,
            alignment=TA_LEFT,
            textColor=colors.HexColor("#222222"),
        )
    )
    return styles


STYLES = build_styles()


def column_widths(
    column_count: int, available_width: float, header_line: str
) -> list[float]:
    if column_count == 5 and "Suíte" in header_line:
        proportions = [0.19, 0.32, 0.19, 0.15, 0.15]
        return [available_width * proportion for proportion in proportions]
    proportions = {
        2: [0.24, 0.76],
        4: [0.13, 0.31, 0.30, 0.26],
        5: [0.08, 0.18, 0.35, 0.18, 0.21],
    }.get(column_count)
    if proportions is None:
        proportions = [1 / column_count] * column_count
    return [available_width * proportion for proportion in proportions]


def markdown_table(lines: list[str], available_width: float) -> Table:
    rows = []
    for index, line in enumerate(lines):
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if index == 1 and all(re.fullmatch(r":?-{3,}:?", cell) for cell in cells):
            continue
        style_name = "TableHeader" if not rows else "TableCell"
        rows.append([Paragraph(inline_markup(cell), STYLES[style_name]) for cell in cells])

    table = Table(
        rows,
        colWidths=column_widths(len(rows[0]), available_width, lines[0]),
        repeatRows=1,
        hAlign="LEFT",
    )
    table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#2F5597")),
                ("GRID", (0, 0), (-1, -1), 0.35, colors.HexColor("#A6A6A6")),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 4),
                ("RIGHTPADDING", (0, 0), (-1, -1), 4),
                ("TOPPADDING", (0, 0), (-1, -1), 4),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
            ]
        )
    )
    for row_index in range(1, len(rows)):
        if row_index % 2 == 0:
            table.setStyle(
                TableStyle(
                    [("BACKGROUND", (0, row_index), (-1, row_index), colors.HexColor("#EAF0F8"))]
                )
            )
    return table


def parse_markdown(source: str, available_width: float) -> list:
    lines = source.splitlines()
    story = []
    index = 0
    title_seen = False

    while index < len(lines):
        line = lines[index].rstrip()
        stripped = line.strip()

        if not stripped:
            index += 1
            continue
        if stripped == r"\newpage":
            story.append(PageBreak())
            index += 1
            continue
        if stripped.startswith("|"):
            table_lines = []
            while index < len(lines) and lines[index].strip().startswith("|"):
                table_lines.append(lines[index].strip())
                index += 1
            story.extend([markdown_table(table_lines, available_width), Spacer(1, 7)])
            continue
        if stripped.startswith("# "):
            story.append(Paragraph(inline_markup(stripped[2:]), STYLES["ReportTitle"]))
            title_seen = True
        elif stripped.startswith("## "):
            story.append(Paragraph(inline_markup(stripped[3:]), STYLES["ReportH2"]))
        elif stripped.startswith("### "):
            story.append(Paragraph(inline_markup(stripped[4:]), STYLES["ReportH3"]))
        elif stripped.startswith("- "):
            story.append(
                Paragraph(inline_markup(stripped[2:]), STYLES["ReportBullet"], bulletText="•")
            )
        else:
            style = "ReportSubtitle" if title_seen and len(story) == 1 else "ReportBody"
            story.append(Paragraph(inline_markup(stripped), STYLES[style]))
        index += 1

    return story


def draw_page(canvas, document) -> None:
    canvas.saveState()
    width, height = A4
    canvas.setStrokeColor(colors.HexColor("#D9E2F3"))
    canvas.setLineWidth(0.5)
    canvas.line(2 * cm, height - 1.35 * cm, width - 2 * cm, height - 1.35 * cm)
    canvas.setFont("Helvetica", 7.5)
    canvas.setFillColor(colors.HexColor("#666666"))
    canvas.drawString(2 * cm, height - 1.1 * cm, "Programa Identifier - Relatorio tecnico")
    canvas.drawRightString(width - 2 * cm, 1.05 * cm, f"Pagina {document.page}")
    canvas.restoreState()


def main() -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    page_width, _ = A4
    left_margin = right_margin = 2 * cm
    document = SimpleDocTemplate(
        str(OUTPUT_PATH),
        pagesize=A4,
        leftMargin=left_margin,
        rightMargin=right_margin,
        topMargin=1.7 * cm,
        bottomMargin=1.6 * cm,
        title="Relatório Técnico - Programa Identifier",
        author="",
        subject="Teste funcional por classes de equivalência e valores limite",
    )
    source = SOURCE_PATH.read_text(encoding="utf-8")
    story = parse_markdown(source, page_width - left_margin - right_margin)
    document.build(story, onFirstPage=draw_page, onLaterPages=draw_page)
    print(OUTPUT_PATH)


if __name__ == "__main__":
    main()
