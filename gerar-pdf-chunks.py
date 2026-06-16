#!/usr/bin/env python3
"""
Gerador do PDF do Livro 1 em CHUNKS — necessário para escapar timeout de 45s
do bash do ambiente. Cada chunk gera ~150 páginas (~10-30s).

ORDEM ATUALIZADA (junho/2026, pós-fechamento editorial do L1):
- 70 arquivos no total
- 14 chunks balanceados (cada um deve completar em <30s)
- Inclui todos os capítulos novos (C00P, C14B, C45, C46), apêndices novos
  (J, N, O, P, Q), F5 reescrito (cobertura-integracoes), 8 paratextos editoriais
  novos (ficha catalográfica, dedicatória, agradecimentos, pacto sobre casos,
  mapa de leitura por nível, sobre o autor, orelhas, quarta capa).

Uso:
    python3 gerar-pdf-chunks.py prepare        # consolida MD, gera HTML e CSS
    python3 gerar-pdf-chunks.py chunk N        # gera PDF do chunk N (0..N-1)
    python3 gerar-pdf-chunks.py capas          # gera PDFs das capas
    python3 gerar-pdf-chunks.py merge          # mescla todos os PDFs
"""
import subprocess
import os
import re
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parent
ROOT = BASE.parent

# ---------- ORDEM CANÔNICA (70 arquivos) ----------
ORDEM = [
    # PARATEXTO INICIAL (10 arquivos)
    ("00-paratexto/L1-00-capa-e-titulos.md",         "Capa e Títulos"),
    ("00-paratexto/L1-00b-ficha-catalografica.md",   "Ficha Catalográfica"),
    ("00-paratexto/L1-00c-dedicatoria.md",           "Dedicatória"),
    ("00-paratexto/L1-00d-agradecimentos.md",        "Agradecimentos"),
    ("00-paratexto/L1-00e-sobre-os-casos.md",        "Sobre os Casos"),
    ("00-paratexto/L1-01-prefacio.md",               "Prefácio"),
    ("00-paratexto/L1-02-como-ler.md",               "Como Ler"),
    ("00-paratexto/L1-03-introducao.md",             "Introdução"),
    ("00-paratexto/L1-04-sumario.md",                "Sumário"),
    ("00-paratexto/L1-05-mapa-de-leitura-por-nivel.md", "Mapa de Leitura"),

    # MANIFESTO (2 arquivos)
    ("01-manifesto/L1-C00M-manifesto-invariantes.md", "Manifesto"),
    ("01-manifesto/L1-C00P-porque-padrao-dura.md",   "Por quê"),

    # PARTE 1 — FUNDAMENTOS (8 capítulos)
    ("02-capitulos/L1-C01-o-que-e-ia.md",            "Cap 01"),
    ("02-capitulos/L1-C02-como-modelos-funcionam.md", "Cap 02"),
    ("02-capitulos/L1-C03-tokens.md",                "Cap 03"),
    ("02-capitulos/L1-C04-janela-de-contexto.md",    "Cap 04"),
    ("02-capitulos/L1-C05-embeddings.md",            "Cap 05"),
    ("02-capitulos/L1-C06-rag.md",                   "Cap 06"),
    ("02-capitulos/L1-C07-memoria.md",               "Cap 07"),
    ("02-capitulos/L1-C08-fine-tuning.md",           "Cap 08"),

    # PARTE 2 — PROMPT E RACIOCÍNIO (3 capítulos)
    ("02-capitulos/L1-C09-engenharia-prompt.md",     "Cap 09"),
    ("02-capitulos/L1-C10-chain-of-thought.md",      "Cap 10"),
    ("02-capitulos/L1-C11-context-engineering.md",   "Cap 11"),

    # PARTE 3 — AGENTES (4 capítulos, incluindo C14B novo)
    ("02-capitulos/L1-C12-agentes.md",               "Cap 12"),
    ("02-capitulos/L1-C13-mcp.md",                   "Cap 13"),
    ("02-capitulos/L1-C14-ai-engineering.md",        "Cap 14"),
    ("02-capitulos/L1-C14B-reasoning-models.md",     "Cap 14B"),

    # PARTE 4 — MODELOS (2 capítulos)
    ("02-capitulos/L1-C15-comparacao-modelos.md",    "Cap 15"),
    ("02-capitulos/L1-C16-open-source.md",           "Cap 16"),

    # PARTE 5 — AVANÇADO (12 capítulos, incluindo C41, C45, C46 novos)
    ("02-capitulos/L1-C35-github-repos.md",          "Cap 35"),
    ("02-capitulos/L1-C36-economia-tokens.md",       "Cap 36"),
    ("02-capitulos/L1-C37-seguranca.md",             "Cap 37"),
    ("02-capitulos/L1-C38-futuro.md",                "Cap 38"),
    ("02-capitulos/L1-C39-evals.md",                 "Cap 39"),
    ("02-capitulos/L1-C40-llmops.md",                "Cap 40"),
    ("02-capitulos/L1-C41-alignment.md",             "Cap 41"),
    ("02-capitulos/L1-C42-governanca.md",            "Cap 42"),
    ("02-capitulos/L1-C43-trade-offs.md",            "Cap 43"),
    ("02-capitulos/L1-C44-roadmap-pessoal.md",       "Cap 44"),
    ("02-capitulos/L1-C45-ia-para-pme-brasileira.md", "Cap 45"),
    ("02-capitulos/L1-C46-interpretabilidade-mecanicista.md", "Cap 46"),

    # FRAMEWORKS (9 arquivos, F5 com nome novo neutro)
    ("03-frameworks/L1-F1-decid-ia.md",              "F1 Decisão"),
    ("03-frameworks/L1-F2-encaixe-5.md",             "F2 Encaixe"),
    ("03-frameworks/L1-F3-agente-prop.md",           "F3 Agente"),
    ("03-frameworks/L1-F4-prompt-ext.md",            "F4 Prompt Estendido"),
    ("03-frameworks/L1-F5-cobertura-integracoes.md", "F5 Cobertura"),
    ("03-frameworks/L1-F6-gov-indelegavel.md",       "F6 Governança"),
    ("03-frameworks/L1-F7-composto-3t.md",           "F7 Custo Composto"),
    ("03-frameworks/L1-F8-eval-piramide.md",         "F8 Pirâmide"),
    ("03-frameworks/L1-F9-rota-dupla.md",            "F9 Rota Dupla"),

    # APÊNDICES (17 arquivos, A a Q)
    ("04-apendices/L1-APX-A-glossario.md",           "Apêndice A"),
    ("04-apendices/L1-APX-B-mapa-mental.md",         "Apêndice B"),
    ("04-apendices/L1-APX-C-roadmaps.md",            "Apêndice C"),
    ("04-apendices/L1-APX-D-ferramentas.md",         "Apêndice D"),
    ("04-apendices/L1-APX-E-leituras.md",            "Apêndice E"),
    ("04-apendices/L1-APX-F-newsletters.md",         "Apêndice F"),
    ("04-apendices/L1-APX-G-papers.md",              "Apêndice G"),
    ("04-apendices/L1-APX-H-bibliografia.md",        "Apêndice H"),
    ("04-apendices/L1-APX-I-indice-remissivo.md",    "Apêndice I"),
    ("04-apendices/L1-APX-J-trilha-do-numero.md",    "Apêndice J"),
    ("04-apendices/L1-APX-K-gabaritos.md",           "Apêndice K"),
    ("04-apendices/L1-APX-L-biblioteca-prompts.md",  "Apêndice L"),
    ("04-apendices/L1-APX-M-manifesto-bolso.md",     "Apêndice M"),
    ("04-apendices/L1-APX-N-metodologico-numeros.md", "Apêndice N"),
    ("04-apendices/L1-APX-O-caderno-governanca-v1.md", "Apêndice O"),
    ("04-apendices/L1-APX-P-boxes-tecnicos.md",      "Apêndice P"),
    ("04-apendices/L1-APX-Q-manual-do-professor.md", "Apêndice Q"),

    # PARATEXTO FINAL (3 arquivos)
    ("00-paratexto/L1-10-sobre-o-autor.md",          "Sobre o Autor"),
    ("00-paratexto/L1-11-orelhas.md",                "Orelhas"),
    ("00-paratexto/L1-12-quarta-capa.md",            "Quarta Capa"),
]

# ---------- CHUNKS (índices da ORDEM, fim exclusivo) ----------
# Cada chunk deve gerar em <30s para caber no timeout de 45s do bash MCP.
# APX-L tem ~126KB e fica em chunk próprio para evitar timeout.
CHUNKS = [
    ("00-paratexto-inicial",     0,  10),   # 10 paratextos iniciais
    ("01-manifesto",             10, 12),   # C00M + C00P
    ("02-fundamentos-1",         12, 16),   # C01-C04
    ("03-fundamentos-2",         16, 20),   # C05-C08
    ("04-prompt-cot-contexto",   20, 23),   # C09-C11
    ("05-agentes-mcp",           23, 27),   # C12, C13, C14, C14B
    ("06-modelos",               27, 29),   # C15-C16
    ("07-praticas-35-38",        29, 33),   # C35-C38
    ("08-evals-llmops-align",    33, 36),   # C39, C40, C41
    ("09-gov-trade-roadmap",     36, 40),   # C42, C43, C44, C45
    ("10-interp-frameworks",     40, 50),   # C46 + F1-F9
    ("11-apendices-A-G",         50, 57),   # APX-A a APX-G
    ("12-apendices-H-K",         57, 61),   # APX-H, I, J, K
    ("13-apendice-L",            61, 62),   # APX-L sozinho (gigante)
    ("14-apendices-M-Q",         62, 67),   # APX-M, N, O, P, Q
    ("15-paratexto-final",       67, 70),   # Sobre o autor, orelhas, quarta capa
]

CSS = """
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

body {
    font-family: "Lora", "Liberation Serif", "DejaVu Serif", Georgia, serif;
    font-size: 11pt;
    line-height: 1.55;
    color: #0d1b2a;
    text-align: justify;
    hyphens: auto;
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

h3 { font-size: 13pt; color: #1b263b; margin-top: 18pt; margin-bottom: 8pt; font-weight: 700; }
h4 { font-size: 11.5pt; color: #1b263b; margin-top: 14pt; font-weight: 700; }

p { margin-top: 0; margin-bottom: 9pt; orphans: 3; widows: 3; }

blockquote {
    margin: 14pt 0;
    padding: 10pt 14pt;
    border-left: 3pt solid #E97451;
    background-color: #fefce8;
    font-style: italic;
    color: #1b263b;
    page-break-inside: avoid;
}

blockquote p { margin: 4pt 0; }

ul, ol { margin: 8pt 0 12pt 0; padding-left: 22pt; }
li { margin-bottom: 4pt; }

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

td { padding: 5pt 8pt; border-bottom: 0.5pt solid #d1d5db; vertical-align: top; }
tr:nth-child(even) td { background-color: #fafafa; }

code {
    font-family: 'Liberation Mono', 'DejaVu Sans Mono', monospace;
    font-size: 9.5pt;
    background-color: #f3f4f6;
    padding: 1pt 4pt;
    color: #0d1b2a;
}

pre {
    background-color: #0d1b2a;
    color: #fef3c7;
    padding: 12pt;
    overflow-x: auto;
    font-size: 9pt;
    line-height: 1.45;
    page-break-inside: avoid;
    margin: 12pt 0;
}

pre code { background-color: transparent; color: #fef3c7; padding: 0; }

img { max-width: 100%; height: auto; display: block; margin: 14pt auto; page-break-inside: avoid; }
a { color: #D97706; text-decoration: none; }
.page-break { page-break-after: always; }
strong { color: #0d1b2a; font-weight: 700; }
em { color: #1b263b; }
hr { border: none; border-top: 1pt solid #E97451; margin: 18pt auto; width: 60%; opacity: 0.6; }
"""


def ajustar_paths_de_imagem(conteudo, arquivo_origem):
    dir_origem = arquivo_origem.parent
    def substituir(match):
        link = match.group(2)
        if link.startswith(('http://', 'https://', 'file://', 'data:')):
            return match.group(0)
        caminho_abs = (dir_origem / link).resolve()
        if caminho_abs.exists():
            return f'![{match.group(1)}](file://{caminho_abs})'
        return match.group(0)
    return re.sub(r'!\[([^\]]*)\]\(([^)]+)\)', substituir, conteudo)


def consolidar_chunk(chunk_idx):
    nome, ini, fim = CHUNKS[chunk_idx]
    saida = ["---", 'title: "Inteligência Aumentada"', 'lang: pt-BR', "---", ""]
    for i in range(ini, fim):
        caminho_rel, nome_sec = ORDEM[i]
        caminho = BASE / caminho_rel
        if not caminho.exists():
            print(f"  ✗ FALTA: {caminho_rel}", file=sys.stderr)
            continue
        conteudo = caminho.read_text(encoding='utf-8')
        conteudo = ajustar_paths_de_imagem(conteudo, caminho)
        saida.append('\n\n<div class="page-break"></div>\n\n')
        saida.append(conteudo)
    return "\n".join(saida)


def cmd_prepare():
    print(f"Preparando build... ({len(CHUNKS)} chunks, {len(ORDEM)} arquivos)")
    build = BASE / "_build"
    build.mkdir(exist_ok=True)
    (build / "style.css").write_text(CSS, encoding='utf-8')
    print(f"  CSS escrito em {build/'style.css'}")

    # Validar que todos os arquivos da ORDEM existem
    faltantes = []
    for caminho_rel, nome in ORDEM:
        if not (BASE / caminho_rel).exists():
            faltantes.append(caminho_rel)
    if faltantes:
        print(f"  ✗ {len(faltantes)} arquivos faltam:")
        for f in faltantes:
            print(f"      {f}")
        sys.exit(1)
    print(f"  ✓ Todos os {len(ORDEM)} arquivos da ORDEM existem")

    # Consolidar cada chunk em MD
    for idx, (nome, ini, fim) in enumerate(CHUNKS):
        md = consolidar_chunk(idx)
        (build / f"chunk-{idx:02d}-{nome}.md").write_text(md, encoding='utf-8')
        print(f"  ✓ chunk {idx:02d} ({nome}): {fim-ini} itens, {len(md)//1024} KB")

    # Consolidado completo (para revisão e auditoria)
    completo = ["---", 'title: "Inteligência Aumentada"',
                'subtitle: "Os Invariantes da IA"',
                'author: "Fabio Garcia"', 'date: "2026"', 'lang: pt-BR', "---", ""]
    for caminho_rel, nome_sec in ORDEM:
        caminho = BASE / caminho_rel
        if not caminho.exists():
            continue
        conteudo = caminho.read_text(encoding='utf-8')
        conteudo = ajustar_paths_de_imagem(conteudo, caminho)
        completo.append('\n\n<div class="page-break"></div>\n\n')
        completo.append(conteudo)
    consolidado_path = build / "L1-consolidado.md"
    consolidado_path.write_text("\n".join(completo), encoding='utf-8')
    print(f"  ✓ L1-consolidado.md: {consolidado_path.stat().st_size//1024} KB")
    print("Pronto.")


def cmd_chunk(idx):
    build = BASE / "_build"
    md_path = build / sorted([p for p in build.glob(f"chunk-{idx:02d}-*.md")])[0].name
    html_path = build / md_path.name.replace(".md", ".html")
    pdf_path = build / md_path.name.replace(".md", ".pdf")
    print(f"Chunk {idx}: {md_path.name}")
    subprocess.run([
        'pandoc', str(md_path),
        '-f', 'markdown+raw_html+definition_lists+fenced_code_blocks+pipe_tables',
        '-t', 'html5', '--standalone', '-o', str(html_path),
        '--metadata=title:Inteligência Aumentada', '--metadata=lang:pt-BR',
    ], check=True)
    print(f"  HTML: {html_path.name}")
    import weasyprint
    css = weasyprint.CSS(filename=str(build / "style.css"))
    weasyprint.HTML(filename=str(html_path), base_url=str(BASE)).write_pdf(
        str(pdf_path), stylesheets=[css]
    )
    print(f"  PDF: {pdf_path.name} ({pdf_path.stat().st_size//1024} KB)")


def cmd_capas():
    """Gera PDFs separados da capa frontal e quarta capa."""
    import weasyprint
    build = BASE / "_build"
    for tag, svg_name in [("capa-frontal", "L1-capa-frontal.svg"),
                          ("quarta-capa", "L1-quarta-capa.svg")]:
        svg = ROOT / "assets" / "capas" / "L1" / svg_name
        if not svg.exists():
            print(f"  ✗ FALTA: {svg}")
            continue
        html = f"""<!DOCTYPE html><html><head><style>
@page {{ size: 16cm 24cm; margin: 0; }}
body {{ margin: 0; padding: 0; }}
img {{ width: 16cm; height: 24cm; display: block; }}
</style></head><body>
<img src="file://{svg.resolve()}"/>
</body></html>"""
        html_path = build / f"{tag}.html"
        html_path.write_text(html)
        pdf_path = build / f"{tag}.pdf"
        weasyprint.HTML(filename=str(html_path)).write_pdf(str(pdf_path))
        print(f"  ✓ {tag}.pdf ({pdf_path.stat().st_size//1024} KB)")


def cmd_merge():
    from pypdf import PdfWriter
    build = BASE / "_build"
    final = BASE / "Inteligencia-Aumentada-Livro-1-Os-Invariantes.pdf"
    writer = PdfWriter()
    # Capa frontal
    capa = build / "capa-frontal.pdf"
    if capa.exists():
        writer.append(str(capa))
        print(f"  + capa-frontal.pdf")
    # Chunks em ordem
    for idx in range(len(CHUNKS)):
        candidatos = sorted(build.glob(f"chunk-{idx:02d}-*.pdf"))
        if not candidatos:
            print(f"  ✗ FALTA: chunk {idx:02d}")
            continue
        writer.append(str(candidatos[0]))
        print(f"  + {candidatos[0].name}")
    # Quarta capa
    quarta = build / "quarta-capa.pdf"
    if quarta.exists():
        writer.append(str(quarta))
        print(f"  + quarta-capa.pdf")
    writer.write(str(final))
    writer.close()
    tamanho = final.stat().st_size / (1024 * 1024)
    print(f"\n✓ PDF final: {final.name} ({tamanho:.2f} MB)")


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    cmd = sys.argv[1]
    if cmd == "prepare":
        cmd_prepare()
    elif cmd == "chunk":
        cmd_chunk(int(sys.argv[2]))
    elif cmd == "capas":
        cmd_capas()
    elif cmd == "merge":
        cmd_merge()
    else:
        print(f"Comando desconhecido: {cmd}")
        sys.exit(1)


if __name__ == "__main__":
    main()
