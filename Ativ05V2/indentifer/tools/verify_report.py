from pathlib import Path

import pymupdf
import pdfplumber
from pypdf import PdfReader


ROOT = Path(__file__).resolve().parents[1]
PDF = ROOT / "output" / "pdf" / "relatorio-tecnico-identifier.pdf"
RENDER_DIR = ROOT / "tmp" / "pdfs" / "render"


def main():
    reader = PdfReader(PDF)
    if len(reader.pages) != 5:
        raise AssertionError(f"Quantidade inesperada de páginas: {len(reader.pages)}")

    with pdfplumber.open(PDF) as document:
        text = "\n".join(page.extract_text() or "" for page in document.pages)

    required = [
        "Classes de equivalência",
        "Análise de valor limite",
        "17 TESTES APROVADOS",
        "BUILD SUCCESS",
        "Setup",
        "Invocation",
        "Assessment",
    ]
    missing = [item for item in required if item not in text]
    if missing:
        raise AssertionError(f"Conteúdo ausente no PDF: {missing}")

    RENDER_DIR.mkdir(parents=True, exist_ok=True)
    for existing_image in RENDER_DIR.glob("pagina-*.png"):
        existing_image.unlink()

    document = pymupdf.open(PDF)
    for index, page in enumerate(document):
        pixmap = page.get_pixmap(matrix=pymupdf.Matrix(1.7, 1.7), alpha=False)
        pixmap.save(RENDER_DIR / f"pagina-{index + 1}.png")

    print(f"paginas={len(reader.pages)}")
    print(f"caracteres_extraidos={len(text)}")
    print(f"arquivos_renderizados={len(list(RENDER_DIR.glob('pagina-*.png')))}")
    print(f"metadata_title={reader.metadata.title}")


if __name__ == "__main__":
    main()
