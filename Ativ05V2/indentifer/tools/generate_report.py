from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import (
    PageBreak,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "output" / "pdf" / "relatorio-tecnico-identifier.pdf"

NAVY = colors.HexColor("#17324D")
BLUE = colors.HexColor("#236B8E")
TEAL = colors.HexColor("#2A9D8F")
LIGHT_BLUE = colors.HexColor("#EAF3F7")
LIGHT_GRAY = colors.HexColor("#F5F7F9")
TEXT = colors.HexColor("#263238")


styles = getSampleStyleSheet()
styles.add(
    ParagraphStyle(
        name="ReportTitle",
        parent=styles["Title"],
        fontName="Helvetica-Bold",
        fontSize=26,
        leading=31,
        textColor=NAVY,
        alignment=TA_CENTER,
        spaceAfter=8 * mm,
    )
)
styles.add(
    ParagraphStyle(
        name="ReportSubtitle",
        parent=styles["Normal"],
        fontName="Helvetica",
        fontSize=13,
        leading=18,
        textColor=BLUE,
        alignment=TA_CENTER,
    )
)
styles.add(
    ParagraphStyle(
        name="Section",
        parent=styles["Heading1"],
        fontName="Helvetica-Bold",
        fontSize=15,
        leading=19,
        textColor=NAVY,
        spaceBefore=4 * mm,
        spaceAfter=2.5 * mm,
    )
)
styles.add(
    ParagraphStyle(
        name="Subsection",
        parent=styles["Heading2"],
        fontName="Helvetica-Bold",
        fontSize=11.5,
        leading=15,
        textColor=BLUE,
        spaceBefore=3 * mm,
        spaceAfter=1.5 * mm,
    )
)
styles.add(
    ParagraphStyle(
        name="BodyTextReport",
        parent=styles["BodyText"],
        fontName="Helvetica",
        fontSize=9.4,
        leading=13.2,
        textColor=TEXT,
        alignment=TA_LEFT,
        spaceAfter=2.4 * mm,
    )
)
styles.add(
    ParagraphStyle(
        name="TableText",
        parent=styles["BodyTextReport"],
        fontSize=7.6,
        leading=9.4,
        spaceAfter=0,
    )
)
styles.add(
    ParagraphStyle(
        name="TableHeader",
        parent=styles["TableText"],
        fontName="Helvetica-Bold",
        textColor=colors.white,
        alignment=TA_CENTER,
    )
)
styles.add(
    ParagraphStyle(
        name="CodeText",
        parent=styles["BodyTextReport"],
        fontName="Courier",
        fontSize=8.5,
        leading=11,
        backColor=LIGHT_GRAY,
        borderColor=colors.HexColor("#D9E0E5"),
        borderWidth=0.5,
        borderPadding=7,
    )
)
styles.add(
    ParagraphStyle(
        name="Result",
        parent=styles["BodyTextReport"],
        fontName="Helvetica-Bold",
        fontSize=12,
        leading=16,
        textColor=colors.HexColor("#1B7A62"),
        alignment=TA_CENTER,
        backColor=colors.HexColor("#E8F5F1"),
        borderColor=TEAL,
        borderWidth=1,
        borderPadding=8,
        spaceBefore=3 * mm,
        spaceAfter=4 * mm,
    )
)


def p(text, style="BodyTextReport"):
    return Paragraph(text, styles[style])


def table(rows, widths, alignments=None):
    formatted = []
    for row_index, row in enumerate(rows):
        style = "TableHeader" if row_index == 0 else "TableText"
        formatted.append([p(str(cell), style) for cell in row])

    result = Table(formatted, colWidths=widths, repeatRows=1, hAlign="LEFT")
    commands = [
        ("BACKGROUND", (0, 0), (-1, 0), NAVY),
        ("GRID", (0, 0), (-1, -1), 0.45, colors.HexColor("#BCC9D1")),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 5),
        ("RIGHTPADDING", (0, 0), (-1, -1), 5),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
    ]
    for row_index in range(1, len(rows)):
        if row_index % 2 == 0:
            commands.append(("BACKGROUND", (0, row_index), (-1, row_index), LIGHT_BLUE))
    if alignments:
        for column, alignment in enumerate(alignments):
            commands.append(("ALIGN", (column, 1), (column, -1), alignment))
    result.setStyle(TableStyle(commands))
    return result


def footer(canvas, document):
    canvas.saveState()
    width, _ = A4
    canvas.setStrokeColor(colors.HexColor("#D4DEE4"))
    canvas.setLineWidth(0.5)
    canvas.line(18 * mm, 14 * mm, width - 18 * mm, 14 * mm)
    canvas.setFont("Helvetica", 8)
    canvas.setFillColor(colors.HexColor("#667985"))
    canvas.drawString(18 * mm, 9.5 * mm, "Teste Funcional - Programa Identifier")
    canvas.drawRightString(width - 18 * mm, 9.5 * mm, f"Página {document.page}")
    canvas.restoreState()


def build_story():
    story = [
        Spacer(1, 35 * mm),
        p("RELATÓRIO TÉCNICO", "ReportTitle"),
        p("Teste Funcional e Implementação do Programa Identifier", "ReportSubtitle"),
        Spacer(1, 18 * mm),
        Table(
            [[p("PARTICIONAMENTO EM CLASSES DE EQUIVALÊNCIA", "TableHeader")]],
            colWidths=[145 * mm],
            style=TableStyle(
                [
                    ("BACKGROUND", (0, 0), (-1, -1), BLUE),
                    ("BOX", (0, 0), (-1, -1), 1, BLUE),
                    ("TOPPADDING", (0, 0), (-1, -1), 10),
                    ("BOTTOMPADDING", (0, 0), (-1, -1), 10),
                ]
            ),
        ),
        Spacer(1, 48 * mm),
        p("Java 21 | Maven | JUnit 5", "ReportSubtitle"),
        Spacer(1, 5 * mm),
        p("Relatório acadêmico - 15 de setembro de 2026", "ReportSubtitle"),
        PageBreak(),
        p("1. Objetivo e especificação", "Section"),
        p(
            "O objetivo deste trabalho é implementar e validar o programa <b>Identifier</b> "
            "aplicando o critério funcional de particionamento em classes de equivalência, "
            "complementado pela análise de valor limite."
        ),
        p("Um identificador é considerado válido quando atende simultaneamente às seguintes regras:"),
        p("1. possui de <b>1 a 6 caracteres</b>;<br/>2. começa com uma letra ASCII (<b>A-Z</b> ou <b>a-z</b>);<br/>3. contém, depois do primeiro caractere, somente letras ou dígitos ASCII (<b>0-9</b>)."),
        p(
            "A entrada nula não pertence ao domínio textual da especificação, mas foi incluída "
            "como teste defensivo e deve ser rejeitada."
        ),
        p("2. Lista inicial reconstruída", "Section"),
        p(
            "A lista da aula anterior não foi encontrada nos arquivos fornecidos. Para viabilizar "
            "a comparação solicitada, foi reconstruída a lista intuitiva abaixo, sem aplicação "
            "formal de uma técnica de teste."
        ),
        table(
            [
                ["Caso", "Entrada", "Esperado", "Motivação intuitiva"],
                ["CT-A1", "abc", "Válido", "Exemplo comum"],
                ["CT-A2", "1abc", "Inválido", "Começa com dígito"],
                ["CT-A3", "ab#1", "Inválido", "Possui caractere especial"],
                ["CT-A4", "abcdefg", "Inválido", "Excede o tamanho máximo"],
                ["CT-A5", "String vazia", "Inválido", "Não possui caracteres"],
            ],
            [20 * mm, 31 * mm, 27 * mm, 82 * mm],
            ["CENTER", "CENTER", "CENTER", "LEFT"],
        ),
        Spacer(1, 3 * mm),
        p(
            "A lista cobre regras relevantes, mas não evidencia sistematicamente todas as classes "
            "nem os dois lados dos limites de comprimento."
        ),
        PageBreak(),
        p("3. Passo 1 - Classes de equivalência", "Section"),
        p(
            "Cada classe reúne entradas tratadas de maneira equivalente pelo programa. Uma entrada "
            "representativa de cada classe permite reduzir redundância sem perder cobertura das regras."
        ),
        table(
            [
                ["ID", "Condição", "Classe", "Domínio", "Representante"],
                ["CE-C1", "Comprimento", "Válida", "1 a 6 caracteres", "abc123"],
                ["CE-C2", "Comprimento", "Inválida", "0 caracteres", "String vazia"],
                ["CE-C3", "Comprimento", "Inválida", "7 ou mais", "abcdefg"],
                ["CE-I1", "Inicial", "Válida", "Letra ASCII", "Ab12"],
                ["CE-I2", "Inicial", "Inválida", "Dígito ASCII", "1abc"],
                ["CE-I3", "Inicial", "Inválida", "Símbolo, espaço ou outro", "_abc"],
                ["CE-F1", "Demais", "Válida", "Letras e dígitos ASCII", "a1B2"],
                ["CE-F2", "Demais", "Inválida", "Símbolo, espaço ou outro", "ab#1"],
            ],
            [17 * mm, 28 * mm, 22 * mm, 65 * mm, 28 * mm],
            ["CENTER", "LEFT", "CENTER", "LEFT", "CENTER"],
        ),
        Spacer(1, 4 * mm),
        p(
            "As classes CE-I2 e CE-I3 são separadas porque representam naturezas diferentes de "
            "caractere inicial inválido. CE-F2 cobre qualquer caractere que não seja letra ou dígito."
        ),
        PageBreak(),
        p("4. Passo 2 - Casos derivados", "Section"),
        table(
            [
                ["Caso", "Entrada", "Classes exercitadas", "Esperado"],
                ["CT-E1", "a", "CE-C1, CE-I1", "Válido"],
                ["CT-E2", "abc123", "CE-C1, CE-I1, CE-F1", "Válido"],
                ["CT-E3", "String vazia", "CE-C2", "Inválido"],
                ["CT-E4", "abcdefg", "CE-C3", "Inválido"],
                ["CT-E5", "Ab12", "CE-I1, CE-F1", "Válido"],
                ["CT-E6", "1abc", "CE-I2", "Inválido"],
                ["CT-E7", "_abc", "CE-I3", "Inválido"],
                ["CT-E8", "a1B2", "CE-F1", "Válido"],
                ["CT-E9", "ab#1", "CE-F2", "Inválido"],
                ["CT-E10", "null", "Robustez", "Inválido"],
            ],
            [22 * mm, 40 * mm, 67 * mm, 31 * mm],
            ["CENTER", "CENTER", "LEFT", "CENTER"],
        ),
        p("5. Análise de valor limite", "Section"),
        p(
            "A análise verifica exatamente as fronteiras do intervalo permitido e os valores "
            "imediatamente externos, onde erros de comparação são mais prováveis."
        ),
        table(
            [
                ["Tamanho", "Entrada", "Posição", "Esperado"],
                ["0", "String vazia", "Abaixo do mínimo", "Inválido"],
                ["1", "a", "Mínimo válido", "Válido"],
                ["6", "abc123", "Máximo válido", "Válido"],
                ["7", "abcdefg", "Acima do máximo", "Inválido"],
            ],
            [23 * mm, 42 * mm, 62 * mm, 33 * mm],
            ["CENTER", "CENTER", "LEFT", "CENTER"],
        ),
        PageBreak(),
        p("6. Automação com JUnit 5", "Section"),
        p(
            "Os testes automatizados deixam explícita a estrutura formal solicitada: "
            "<b>Setup</b> cria o validador ou captura a saída padrão; <b>Invocation</b> chama "
            "o método de validação ou a aplicação; e <b>Assessment</b> compara o resultado obtido "
            "com o esperado usando <font name='Courier'>assertEquals</font>."
        ),
        p(
            "Foram executados 14 casos sobre o validador, incluindo classes, valores-limite e "
            "entrada nula, além de 3 casos sobre a interface de linha de comando."
        ),
        p("Comando de execução", "Subsection"),
        p(".\\mvnw.cmd test", "CodeText"),
        p("7. Resultado", "Section"),
        p("17 TESTES APROVADOS - BUILD SUCCESS", "Result"),
        table(
            [
                ["Métrica", "Resultado"],
                ["Testes executados", "17"],
                ["Falhas", "0"],
                ["Erros", "0"],
                ["Ignorados", "0"],
                ["Data da execução", "15/09/2026"],
            ],
            [100 * mm, 60 * mm],
            ["LEFT", "CENTER"],
        ),
        p("8. Conclusão", "Section"),
        p(
            "Todos os representantes selecionados produziram os resultados esperados. As classes "
            "de equivalência tornaram a seleção rastreável em relação à especificação, enquanto "
            "os tamanhos 0, 1, 6 e 7 verificaram precisamente as fronteiras. A aplicação final "
            "atende às regras definidas e sua execução automatizada foi concluída sem falhas."
        ),
        Spacer(1, 4 * mm),
        p("Fonte: especificação da atividade fornecida na pasta <b>docs</b> do projeto."),
    ]
    return story


def main():
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    document = SimpleDocTemplate(
        str(OUTPUT),
        pagesize=A4,
        rightMargin=18 * mm,
        leftMargin=18 * mm,
        topMargin=17 * mm,
        bottomMargin=20 * mm,
        title="Relatório Técnico - Programa Identifier",
        author="Projeto Identifier",
        subject="Particionamento em classes de equivalência e análise de valor limite",
    )
    document.build(build_story(), onFirstPage=footer, onLaterPages=footer)
    print(OUTPUT)


if __name__ == "__main__":
    main()
