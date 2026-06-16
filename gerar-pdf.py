#!/usr/bin/env python3
"""
Gerador do PDF final do Livro 1 — Inteligência Aumentada · Os Invariantes da IA.

Consolida todos os arquivos MD na ordem correta, ajusta paths de imagens para
absolutos, converte para HTML via pandoc e renderiza PDF via WeasyPrint.
"""
import subprocess
import os
import re
from pathlib import Path

BASE = Path(__file__).resolve().parent
ROOT = BASE.parent  # Ebook IA/

# Ordem canônica do Livro 1
ORDEM = [
    # PARATEXTO
    ("00-paratexto/L1-00-capa-e-titulos.md", "Capa e Títulos"),
    ("00-paratexto/L1-01-prefacio.md", "Prefácio"),
    ("00-paratexto/L1-02-como-ler.md", "Como Ler"),
    ("00-paratexto/L1-03-introducao.md", "Introdução"),
    ("00-paratexto/L1-04-sumario.md", "Sumário"),
    # MANIFESTO
    ("01-manifesto/L1-C00M-manifesto-invariantes.md", "Manifesto dos Invariantes"),
    # CAPÍTULOS PARTE 1
    ("02-capitulos/L1-C01-o-que-e-ia.md", "Cap 01"),
    ("02-capitulos/L1-C02-como-modelos-funcionam.md", "Cap 02"),
    ("02-capitulos/L1-C03-tokens.md", "Cap 03"),
    ("02-capitulos/L1-C04-janela-de-contexto.md", "Cap 04"),
    ("02-capitulos/L1-C05-embeddings.md", "Cap 05"),
    ("02-capitulos/L1-C06-rag.md", "Cap 06"),
    ("02-capitulos/L1-C07-memoria.md", "Cap 07"),
    ("02-capitulos/L1-C08-fine-tuning.md", "Cap 08"),
    # PARTE 2
    ("02-capitulos/L1-C09-engenharia-prompt.md", "Cap 09"),
    ("02-capitulos/L1-C10-chain-of-thought.md", "Cap 10"),
    ("02-capitulos/L1-C11-context-engineering.md", "Cap 11"),
    # PARTE 3
    ("02-capitulos/L1-C12-agentes.md", "Cap 12"),
    ("02-capitulos/L1-C13-mcp.md", "Cap 13"),
    ("02-capitulos/L1-C14-ai-engineering.md", "Cap 14"),
    # PARTE 4
    ("02-capitulos/L1-C15-comparacao-modelos.md", "Cap 15"),
    ("02-capitulos/L1-C16-open-source.md", "Cap 16"),
    # PARTE 6 (Caps 35-44)
    ("02-capitulos/L1-C35-github-repos.md", "Cap 35"),
    ("02-capitulos/L1-C36-economia-tokens.md", "Cap 36"),
    ("02-capitulos/L1-C37-seguranca.md", "Cap 37"),
    ("02-capitulos/L1-C38-futuro.md", "Cap 38"),
    ("02-capitulos/L1-C39-evals.md", "Cap 39"),
    ("02-capitulos/L1-C40-llmops.md", "Cap 40"),
    ("02-capitulos/L1-C41-alignment.md", "Cap 41"),
    ("02-capitulos/L1-C42-governanca.md", "Cap 42"),
    ("02-capitulos/L1-C43-trade-offs.md", "Cap 43"),
    ("02-capitulos/L1-C44-roadmap-pessoal.md", "Cap 44"),
    # FRAMEWORKS
    ("03-frameworks/L1-F1-decid-ia.md", "F1 DECID-IA"),
    ("03-frameworks/L1-F2-encaixe-5.md", "F2 ENCAIXE-5"),
    ("03-frameworks/L1-F3-agente-prop.md", "F3 AGENTE-PROP"),
    ("03-frameworks/L1-F4-prompt-ext.md", "F4 PROMPT-EXT"),
    ("03-frameworks/L1-F5-mcp-cobertura.md", "F5 MCP-COBERTURA"),
    ("03-frameworks/L1-F6-gov-indelegavel.md", "F6 GOV-INDELEGÁVEL"),
    ("03-frameworks/L1-F7-composto-3t.md", "F7 COMPOSTO-3T"),
    ("03-frameworks/L1-F8-eval-piramide.md", "F8 EVAL-PIRÂMIDE"),
    ("03-frameworks/L1-F9-rota-dupla.md", "F9 ROTA-DUPLA"),
    # APÊNDICES
    ("04-apendices/L1-APX-A-glossario.md", "Apêndice A — Glossário"),
    ("04-apendices/L1-APX-B-mapa-mental.md", "Apêndice B — Mapa Mental"),
    ("04-apendices/L1-APX-C-roadmaps.md", "Apêndice C — Roadmaps"),
    ("04-apendices/L1-APX-D-ferramentas.md", "Apêndice D — Ferramentas"),
    ("04-apendices/L1-APX-E-leituras.md", "Apêndice E — Leituras"),
    ("04-apendices/L1-APX-F-newsletters.md", "Apêndice F — Newsletters"),
    ("04-apendices/L1-APX-G-papers.md", "Apêndice G — Papers"),
    ("04-apendices/L1-APX-H-bibliografia.md", "Apêndice H — Bibliografia"),
    ("04-apendices/L1-APX-I-indice-remissivo.md", "Apêndice I — Índice Remissivo"),
    ("04-apendices/L1-APX-K-gabaritos.md", "Apêndice K — Gabaritos"),
    ("04-apendices/L1-APX-L-biblioteca-prompts.md", "Apêndice L — Biblioteca de Prompts"),
    ("04-apendices/L1-APX-M-manifesto-bolso.md", "Apêndice M — Manifesto de Bolso"),
]


def ajustar_paths_de_imagem(conteudo: str, arquivo_origem: Path) -> str:
    """Converte paths de imagem relativos para absolutos (file://)."""
    dir_origem = arquivo_origem.parent

    def substituir(match):
        link = match.group(1)
        if link.startswith(('http://', 'https://', 'file://', 'data:')):
            return match.group(0)
        # Resolve relativo ao arquivo de origem
        caminho_abs = (dir_origem / link).resolve()
        if caminho_abs.exists():
            return f'![{match.group(0).split("[")[1].split("]")[0]}](file://{caminho_abs})'
        return match.group(0)

    # Padrão: ![alt](path)
    return re.sub(r'!\[([^\]]*)\]\(([^)]+)\)', substituir, conteudo)


def consolidar():
    print("Consolidando MDs...")
    saida = []

    # Frontmatter pandoc com título
    saida.append("---")
    saida.append('title: "Inteligência Aumentada"')
    saida.append('subtitle: "Os Invariantes da IA"')
    saida.append('author: "Fabio Garcia"')
    saida.append('date: "2026"')
    saida.append('lang: pt-BR')
    saida.append("---")
    saida.append("")

    # CAPA FRONTAL (SVG embutida como primeira página)
    capa_svg = ROOT / "assets" / "capas" / "L1" / "L1-capa-frontal.svg"
    if capa_svg.exists():
        saida.append('<div class="cover-page">')
        saida.append(f'<img src="file://{capa_svg.resolve()}" alt="Capa" class="cover-image"/>')
        saida.append('</div>')
        saida.append("")
        print("  ✓ Capa frontal embutida")

    for caminho_rel, nome in ORDEM:
        caminho = BASE / caminho_rel
        if not caminho.exists():
            print(f"  ✗ FALTA: {caminho_rel}")
            continue
        conteudo = caminho.read_text(encoding='utf-8')
        conteudo = ajustar_paths_de_imagem(conteudo, caminho)
        # Quebra de página entre seções principais
        saida.append('\n\n<div class="page-break"></div>\n\n')
        saida.append(conteudo)
        print(f"  ✓ {nome}")

    consolidado = BASE / "_build" / "L1-consolidado.md"
    consolidado.parent.mkdir(exist_ok=True)
    consolidado.write_text("\n".join(saida), encoding='utf-8')
    print(f"\nConsolidado em {consolidado}")
    return consolidado


def gerar_css():
    """CSS para formatação profissional do PDF."""
    css = """
@page {
    size: 16cm 24cm;
    margin: 2cm 1.8cm;
    @bottom-center {
        content: counter(page);
        font-family: "Liberation Sans", "DejaVu Sans", sans-serif;
        font-size: 9pt;
        color: #6b7280;
    }
    @top-left {
        content: string(chapter);
        font-family: "Liberation Sans", "DejaVu Sans", sans-serif;
        font-size: 8pt;
        color: #9ca3af;
        font-style: italic;
    }
}

@page cover {
    size: 16cm 24cm;
    margin: 0;
    @bottom-center { content: none; }
    @top-left { content: none; }
}

@page :first {
    @bottom-center { content: none; }
    @top-left { content: none; }
    margin: 0;
}

body {
    font-family: "Lora", "Liberation Serif", "DejaVu Serif", Georgia, serif;
    font-size: 11pt;
    line-height: 1.55;
    color: #0d1b2a;
    text-align: justify;
    hyphens: auto;
}

/* Capa */
.cover-page {
    page: cover;
    width: 16cm;
    height: 24cm;
    margin: 0;
    padding: 0;
    page-break-after: always;
}

.cover-image {
    width: 16cm;
    height: 24cm;
    margin: 0;
    padding: 0;
    display: block;
}

h1, h2, h3, h4, h5, h6 {
    font-family: "Lora", "Liberation Serif", "DejaVu Serif", Georgia, serif;
    font-weight: 600;
    color: #0d1b2a;
    string-set: chapter content();
    page-break-after: avoid;
}

h1 {
    font-size: 26pt;
    color: #0d1b2a;
    border-bottom: 2pt solid #E97451;
    padding-bottom: 8pt;
    margin-top: 0;
    page-break-before: always;
    letter-spacing: -0.5pt;
}

h2 {
    font-size: 18pt;
    color: #1b263b;
    margin-top: 24pt;
    margin-bottom: 12pt;
    border-left: 3pt solid #E97451;
    padding-left: 10pt;
}

h3 {
    font-size: 13pt;
    color: #1b263b;
    margin-top: 18pt;
    margin-bottom: 8pt;
    font-weight: 700;
}

h4 {
    font-size: 11.5pt;
    color: #1b263b;
    margin-top: 14pt;
    font-weight: 700;
}

p {
    margin-top: 0;
    margin-bottom: 9pt;
    text-indent: 0;
    orphans: 3;
    widows: 3;
}

/* Blockquote (selo Invariante, citações) */
blockquote {
    margin: 14pt 0;
    padding: 10pt 14pt;
    border-left: 3pt solid #E97451;
    background-color: #fefce8;
    font-style: italic;
    color: #1b263b;
    page-break-inside: avoid;
}

blockquote p {
    margin: 4pt 0;
}

/* Listas */
ul, ol {
    margin: 8pt 0 12pt 0;
    padding-left: 22pt;
}

li {
    margin-bottom: 4pt;
}

/* Tabelas */
table {
    width: 100%;
    border-collapse: collapse;
    margin: 14pt 0;
    font-size: 9.5pt;
    page-break-inside: avoid;
}

th {
    background-color: #0d1b2a;
    color: #fef3c7;
    padding: 6pt 8pt;
    text-align: left;
    font-family: "Liberation Sans", "DejaVu Sans", sans-serif;
    font-weight: 700;
    font-size: 8.5pt;
    letter-spacing: 0.3pt;
}

td {
    padding: 5pt 8pt;
    border-bottom: 0.5pt solid #d1d5db;
    vertical-align: top;
}

tr:nth-child(even) td {
    background-color: #fafafa;
}

/* Código inline */
code {
    font-family: 'Courier New', monospace;
    font-size: 9.5pt;
    background-color: #f3f4f6;
    padding: 1pt 4pt;
    border-radius: 2pt;
    color: #0d1b2a;
}

pre {
    background-color: #0d1b2a;
    color: #fef3c7;
    padding: 12pt;
    border-radius: 4pt;
    overflow-x: auto;
    font-size: 9pt;
    line-height: 1.45;
    page-break-inside: avoid;
    margin: 12pt 0;
}

pre code {
    background-color: transparent;
    color: #fef3c7;
    padding: 0;
}

/* Imagens */
img {
    max-width: 100%;
    height: auto;
    display: block;
    margin: 14pt auto;
    page-break-inside: avoid;
}

/* Links */
a {
    color: #D97706;
    text-decoration: none;
}

/* Quebra de página explícita */
.page-break {
    page-break-after: always;
}

/* Strong / em */
strong {
    color: #0d1b2a;
    font-weight: 700;
}

em {
    color: #1b263b;
}

/* Divisores */
hr {
    border: none;
    border-top: 1pt solid #E97451;
    margin: 18pt auto;
    width: 60%;
    opacity: 0.6;
}

/* Validação UAU (tabela específica de fim de capítulo) */
table:last-of-type tr td:first-child {
    font-weight: 700;
    color: #E97451;
}
"""
    css_path = BASE / "_build" / "style.css"
    css_path.parent.mkdir(exist_ok=True)
    css_path.write_text(css, encoding='utf-8')
    return css_path


def md_para_html(md_path: Path) -> Path:
    html_path = BASE / "_build" / "L1-consolidado.html"
    print(f"\nConvertendo MD → HTML via pandoc...")
    subprocess.run([
        'pandoc',
        str(md_path),
        '-f', 'markdown+raw_html+definition_lists+fenced_code_blocks+pipe_tables',
        '-t', 'html5',
        '--standalone',
        '-o', str(html_path),
        '--metadata=title:Inteligência Aumentada',
        '--metadata=lang:pt-BR',
    ], check=True)
    print(f"  HTML em {html_path}")
    return html_path


def html_para_pdf(html_path: Path, css_path: Path) -> Path:
    print(f"\nConvertendo HTML → PDF via WeasyPrint...")
    import weasyprint
    pdf_path = BASE / "Inteligencia-Aumentada-Livro-1-Os-Invariantes.pdf"
    html = weasyprint.HTML(filename=str(html_path), base_url=str(BASE))
    css = weasyprint.CSS(filename=str(css_path))
    html.write_pdf(str(pdf_path), stylesheets=[css])
    print(f"  PDF em {pdf_path}")
    return pdf_path


def adicionar_quarta_capa_pdf(pdf_path: Path) -> Path:
    """Anexa a quarta capa como última página, se SVG existir."""
    capa_back = ROOT / "assets" / "capas" / "L1" / "L1-quarta-capa.svg"
    if not capa_back.exists():
        return pdf_path
    print("\nAnexando quarta capa...")
    import weasyprint
    # Gera PDF só da quarta capa
    quarta_html = f"""<!DOCTYPE html>
<html><head><style>
@page {{ size: 16cm 24cm; margin: 0; }}
body {{ margin: 0; padding: 0; }}
img {{ width: 16cm; height: 24cm; display: block; }}
</style></head><body>
<img src="file://{capa_back.resolve()}"/>
</body></html>"""
    quarta_html_path = BASE / "_build" / "L1-quarta-capa.html"
    quarta_html_path.write_text(quarta_html)
    quarta_pdf = BASE / "_build" / "L1-quarta-capa.pdf"
    weasyprint.HTML(filename=str(quarta_html_path)).write_pdf(str(quarta_pdf))

    # Mescla via pypdf
    try:
        from pypdf import PdfWriter
        writer = PdfWriter()
        writer.append(str(pdf_path))
        writer.append(str(quarta_pdf))
        writer.write(str(pdf_path))
        writer.close()
        print(f"  Quarta capa anexada")
    except ImportError:
        print("  pypdf não disponível, pulando merge da quarta capa")
    return pdf_path


def main():
    md = consolidar()
    css = gerar_css()
    html = md_para_html(md)
    pdf = html_para_pdf(html, css)
    pdf = adicionar_quarta_capa_pdf(pdf)
    tamanho_mb = pdf.stat().st_size / (1024 * 1024)
    print(f"\n✓ PDF final: {pdf}")
    print(f"  Tamanho: {tamanho_mb:.2f} MB")


if __name__ == "__main__":
    main()
