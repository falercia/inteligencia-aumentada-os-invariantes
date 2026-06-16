#!/usr/bin/env python3
"""
Pipeline de DIAGRAMAÇÃO PROFISSIONAL do Livro 1 — Inteligência Aumentada.

Implementa todas as especificações do briefing _PROJETO/BRIEFING-DIAGRAMACAO-L1.md:
  - Paleta oficial (#E97451 laranja queimado, #0d1b2a navy escuro, etc.)
  - Tipografia serif (texto) + sans (títulos) + monospace (código)
  - Hierarquia H1-H4 com borda lateral em laranja
  - Capítulos abrindo em página ímpar com número grande + drop cap 3 linhas
  - Cabeçalho par/ímpar diferenciado (capítulo / seção)
  - Numeração romana minúscula para paratexto inicial, decimal para o resto
  - Boxes especiais: PARA EXECUTIVOS (badge navy), ALERTA (laranja), DICA (lâmpada),
    TÉCNICO (chave), INSIGHT
  - Bandeira lateral indicando nível primário do capítulo
  - Bookmarks navegáveis no PDF
  - Frameworks e apêndices visualmente diferenciados do corpo
  - Tabelas com cabeçalho navy + texto off-white
  - Code blocks navy escuro
  - Separadores laranja

Uso:
    python3 diagramacao_pipeline.py prepare      # consolida MD, gera HTML+CSS
    python3 diagramacao_pipeline.py chunk N      # gera PDF do chunk N
    python3 diagramacao_pipeline.py capas        # PDFs das capas
    python3 diagramacao_pipeline.py merge        # mescla tudo
    python3 diagramacao_pipeline.py all          # roda tudo em sequência
"""
import subprocess
import os
import re
import sys
import json
from pathlib import Path

BASE = Path(__file__).resolve().parent
ROOT = BASE.parent
BUILD = BASE / "_build_diagramado"
BUILD.mkdir(exist_ok=True)

# ============================================================================
# 1) ORDEM CANÔNICA + CLASSIFICAÇÃO DE SEÇÕES
# ============================================================================
# Cada entrada: (path_relativo, titulo_curto, tipo, level_opcional)
#   tipo ∈ {paratexto-inicial, manifesto, capitulo, framework, apendice, paratexto-final}
#   level ∈ {iniciante, intermediario, avancado, fundacao, referencia} — só para capitulos/frameworks/apendices

ORDEM = [
    # PARATEXTO INICIAL — numeração romana
    # NOTA: L1-00-capa-e-titulos.md é briefing editorial, NÃO entra no PDF.
    # A capa frontal vem da arte SVG (assets/capas/L1/).
    # NOTA: L1-00b-ficha-catalografica.md NÃO entra no miolo (decisão editorial 2026-06-02).
    #       Ficha catalográfica oficial será produzida por bibliotecário registrado no CRB
    #       antes do depósito legal e aparecerá apenas como página de copyright minimalista.
    ("00-paratexto/L1-00c-dedicatoria.md",           "Dedicatória",             "paratexto-inicial"),
    # NOTA: L1-00d-agradecimentos.md REMOVIDO do miolo (decisão editorial 2026-06-02).
    ("00-paratexto/L1-00c2-promessa.md",             "Por que este livro",      "paratexto-inicial"),
    ("00-paratexto/L1-00e-sobre-os-casos.md",        "Sobre os Casos",          "paratexto-inicial"),
    ("00-paratexto/L1-01-prefacio.md",               "Prefácio",                "paratexto-inicial"),
    ("00-paratexto/L1-02-como-ler.md",               "Como Ler Este Livro",     "paratexto-inicial"),
    ("00-paratexto/L1-03-introducao.md",             "Introdução",              "paratexto-inicial"),
    ("00-paratexto/L1-04-sumario.md",                "Sumário",                 "paratexto-inicial"),
    ("00-paratexto/L1-05-mapa-de-leitura-por-nivel.md", "Mapa de Leitura",      "paratexto-inicial"),
    ("00-paratexto/L1-06-repositorio-acompanhante.md", "Repositório Acompanhante", "paratexto-inicial"),

    # MANIFESTO — primeira página decimal (reset counter)
    ("01-manifesto/L1-C00M-manifesto-invariantes.md", "Manifesto",              "manifesto",  "fundacao"),
    ("01-manifesto/L1-C00P-porque-padrao-dura.md",   "Por quê",                 "manifesto",  "fundacao"),

    # FUNDAMENTOS
    ("02-capitulos/L1-C01-o-que-e-ia.md",            "1 · O Que É IA",          "capitulo",   "iniciante"),
    ("02-capitulos/L1-C02-como-modelos-funcionam.md", "2 · Como Modelos Funcionam", "capitulo", "iniciante"),
    ("02-capitulos/L1-C03-tokens.md",                "3 · Tokens",              "capitulo",   "iniciante"),
    ("02-capitulos/L1-C04-janela-de-contexto.md",    "4 · Janela de Contexto",  "capitulo",   "iniciante"),
    ("02-capitulos/L1-C05-embeddings.md",            "5 · Embeddings",          "capitulo",   "iniciante-intermediario"),
    ("02-capitulos/L1-C06-rag.md",                   "6 · RAG",                 "capitulo",   "iniciante-intermediario"),
    ("02-capitulos/L1-C07-memoria.md",               "7 · Memória",             "capitulo",   "iniciante-intermediario"),
    ("02-capitulos/L1-C08-fine-tuning.md",           "8 · Fine-Tuning",         "capitulo",   "iniciante-intermediario"),

    # PROMPT E RACIOCÍNIO
    ("02-capitulos/L1-C09-engenharia-prompt.md",     "9 · Engenharia de Prompt", "capitulo",  "iniciante"),
    ("02-capitulos/L1-C10-chain-of-thought.md",      "10 · Chain of Thought",   "capitulo",   "intermediario"),
    ("02-capitulos/L1-C11-context-engineering.md",   "11 · Context Engineering", "capitulo",  "intermediario"),

    # AGENTES
    ("02-capitulos/L1-C12-agentes.md",               "12 · Agentes",            "capitulo",   "intermediario"),
    ("02-capitulos/L1-C13-mcp.md",                   "13 · MCP",                "capitulo",   "intermediario"),
    ("02-capitulos/L1-C14-ai-engineering.md",        "14 · AI Engineering",     "capitulo",   "intermediario-avancado"),
    ("02-capitulos/L1-C14C-spec-driven-development.md", "14C · Spec-Driven Development", "capitulo", "intermediario-avancado"),
    ("02-capitulos/L1-C14B-reasoning-models.md",     "14B · Reasoning Models",  "capitulo",   "avancado"),

    # MODELOS
    ("02-capitulos/L1-C15-comparacao-modelos.md",    "15 · Comparação de Modelos", "capitulo", "intermediario"),
    ("02-capitulos/L1-C16-open-source.md",           "16 · Open Source",        "capitulo",   "intermediario"),

    # AVANÇADO (renumerados em 2026-06-02 de C35-C46 para C17-C28, sequencial)
    ("02-capitulos/L1-C17-github-repos.md",          "17 · GitHub Repos",       "capitulo",   "avancado"),
    ("02-capitulos/L1-C18-economia-tokens.md",       "18 · Economia de Tokens", "capitulo",   "intermediario"),
    ("02-capitulos/L1-C19-seguranca.md",             "19 · Segurança",          "capitulo",   "intermediario-avancado"),
    ("02-capitulos/L1-C20-futuro.md",                "20 · Futuro",             "capitulo",   "intermediario-avancado"),
    ("02-capitulos/L1-C21-evals.md",                 "21 · Evals",              "capitulo",   "intermediario-avancado"),
    ("02-capitulos/L1-C22-llmops.md",                "22 · LLMOps",             "capitulo",   "intermediario-avancado"),
    ("02-capitulos/L1-C23-alignment.md",             "23 · Alignment",          "capitulo",   "avancado"),
    ("02-capitulos/L1-C24-governanca.md",            "24 · Governança",         "capitulo",   "intermediario"),
    ("02-capitulos/L1-C25-trade-offs.md",            "25 · Trade-offs",         "capitulo",   "intermediario"),
    ("02-capitulos/L1-C26-roadmap-pessoal.md",       "26 · Roadmap Pessoal",    "capitulo",   "intermediario"),
    ("02-capitulos/L1-C27-ia-para-pme-brasileira.md", "27 · IA para PME BR",    "capitulo",   "intermediario"),
    ("02-capitulos/L1-C28-interpretabilidade-mecanicista.md", "28 · Interpretabilidade", "capitulo", "avancado"),

    # FRAMEWORKS
    ("03-frameworks/L1-F1-decid-ia.md",              "F1 · Método de Decisão",  "framework",  "referencia"),
    ("03-frameworks/L1-F2-encaixe-5.md",             "F2 · Diagnóstico de Encaixe", "framework", "referencia"),
    ("03-frameworks/L1-F3-agente-prop.md",           "F3 · Escala de Propriedade", "framework", "referencia"),
    ("03-frameworks/L1-F4-prompt-ext.md",            "F4 · Prompt Estendido",   "framework",  "referencia"),
    ("03-frameworks/L1-F5-cobertura-integracoes.md", "F5 · Cobertura de Integrações", "framework", "referencia"),
    ("03-frameworks/L1-F6-gov-indelegavel.md",       "F6 · Governança Indelegável", "framework", "referencia"),
    ("03-frameworks/L1-F7-composto-3t.md",           "F7 · Custo Composto",     "framework",  "referencia"),
    ("03-frameworks/L1-F8-eval-piramide.md",         "F8 · Pirâmide da Avaliação", "framework", "referencia"),
    ("03-frameworks/L1-F9-rota-dupla.md",            "F9 · Rota Dupla",         "framework",  "referencia"),

    # APÊNDICES
    ("04-apendices/L1-APX-A-glossario.md",           "Apêndice A · Glossário",            "apendice", "referencia"),
    ("04-apendices/L1-APX-B-mapa-mental.md",         "Apêndice B · Mapa Mental",          "apendice", "referencia"),
    ("04-apendices/L1-APX-C-roadmaps.md",            "Apêndice C · Roadmaps",             "apendice", "referencia"),
    ("04-apendices/L1-APX-D-ferramentas.md",         "Apêndice D · Ferramentas",          "apendice", "referencia"),
    ("04-apendices/L1-APX-E-leituras.md",            "Apêndice E · Leituras",             "apendice", "referencia"),
    ("04-apendices/L1-APX-F-newsletters.md",         "Apêndice F · Newsletters",          "apendice", "referencia"),
    ("04-apendices/L1-APX-G-papers.md",              "Apêndice G · Papers",               "apendice", "referencia"),
    ("04-apendices/L1-APX-H-bibliografia.md",        "Apêndice H · Bibliografia",         "apendice", "referencia"),
    ("04-apendices/L1-APX-I-indice-remissivo.md",    "Apêndice I · Índice Remissivo",     "apendice", "referencia"),
    ("04-apendices/L1-APX-J-trilha-do-numero.md",    "Apêndice J · Trilha do Número",     "apendice", "referencia"),
    ("04-apendices/L1-APX-K-gabaritos.md",           "Apêndice K · Gabaritos",            "apendice", "referencia"),
    ("04-apendices/L1-APX-L-biblioteca-prompts.md",  "Apêndice L · Biblioteca de Prompts", "apendice", "referencia"),
    ("04-apendices/L1-APX-M-manifesto-bolso.md",     "Apêndice M · Síntese de Bolso",     "apendice", "referencia"),
    ("04-apendices/L1-APX-N-metodologico-numeros.md", "Apêndice N · Metodológico",        "apendice", "referencia"),
    ("04-apendices/L1-APX-O-caderno-governanca-v1.md", "Apêndice O · Caderno de Governança", "apendice", "referencia"),
    ("04-apendices/L1-APX-P-boxes-tecnicos.md",      "Apêndice P · Boxes Técnicos",       "apendice", "referencia"),
    ("04-apendices/L1-APX-Q-manual-do-professor.md", "Apêndice Q · Manual do Professor",  "apendice", "referencia"),

    # PARATEXTO FINAL — decimal continuada
    # NOTA: L1-11-orelhas.md vai na orelha física da brochura (não miolo).
    #       L1-12-quarta-capa.md vai na quarta capa (já em SVG, anexada no merge).
    ("00-paratexto/L1-10-sobre-o-autor.md",          "Sobre o Autor",           "paratexto-final"),
]

# Chunks balanceados (cada um < 30s no weasyprint)
# Índices reajustados após remoção de L1-00, L1-11, L1-12 da ORDEM.
CHUNKS = [
    ("00-paratexto-inicial",     0,  9),    # 9 paratextos
    ("01-manifesto",             9,  11),
    ("02-fundamentos-1",        11, 15),
    ("03-fundamentos-2",        15, 19),
    ("04-prompt-cot-contexto",  19, 22),
    ("05-agentes-mcp",          22, 26),
    ("06-modelos",              26, 28),
    ("07-praticas-35-38",       28, 32),
    ("08-evals-llmops-align",   32, 35),
    ("09-gov-trade-roadmap",    35, 39),
    ("10-interp-frameworks",    39, 49),
    ("11-apendices-A-G",        49, 56),
    ("12-apendices-H-K",        56, 60),
    ("13-apendice-L",           60, 61),
    ("14-apendices-M-Q",        61, 66),
    ("15-paratexto-final",      66, 67),    # só Sobre o Autor
]


# ============================================================================
# 2) CSS — DIAGRAMAÇÃO COMPLETA CONFORME BRIEFING
# ============================================================================

CSS = r"""
/* ==========================================================================
   PALETA OFICIAL
   - #E97451  Laranja queimado (acentos, separadores, destaques)
   - #0d1b2a  Navy escuro (cabeçalhos, texto institucional)
   - #1b263b  Navy médio (subcabeçalhos)
   - #fefce8  Amarelo claro (boxes destacados)
   - #fafafa  Cinza claro (alternância de linhas)
   - #6b7280  Cinza médio (paginação, rodapé)
   - #D97706  Âmbar (links)
   ========================================================================== */

/* --------------------- FONTES (web font fallback chain) --------------------- */
@font-face {
    font-family: 'Charter';
    src: local('Charter'), local('Bitstream Charter'), local('DejaVu Serif');
}

/* --------------------- @PAGE: paratexto inicial (romanos) ------------------ */
@page paratexto-inicial {
    size: 16cm 24cm;
    margin: 1.8cm 1.7cm 1.9cm 1.5cm;
    @bottom-center {
        content: counter(page, lower-roman);
        font-family: "DejaVu Sans", sans-serif;
        font-size: 9pt;
        color: #6b7280;
    }
}

/* --------------------- @PAGE: corpo principal (arábica) -------------------- */
@page principal {
    size: 16cm 24cm;
    margin: 1.8cm 1.7cm 1.9cm 1.5cm;
    @top-left {
        content: string(chap-title);
        font-family: "DejaVu Sans", sans-serif;
        font-size: 8pt;
        font-style: italic;
        color: #9ca3af;
    }
    @top-right {
        content: string(sect-title);
        font-family: "DejaVu Sans", sans-serif;
        font-size: 8pt;
        font-style: italic;
        color: #9ca3af;
    }
    @bottom-center {
        content: counter(page);
        font-family: "DejaVu Sans", sans-serif;
        font-size: 9pt;
        color: #6b7280;
    }
}

/* --------------------- @PAGE: abertura de capítulo ------------------------- */
@page abertura-capitulo {
    size: 16cm 24cm;
    margin: 1.8cm 1.7cm 1.9cm 1.5cm;
    @top-left { content: none; }
    @top-right { content: none; }
    @bottom-center {
        content: counter(page);
        font-family: "DejaVu Sans", sans-serif;
        font-size: 9pt;
        color: #6b7280;
    }
}

/* --------------------- HTML/BODY base -------------------------------------- */
html { font-size: 10pt; }

body {
    font-family: 'Charter', 'Bitstream Charter', 'DejaVu Serif', Georgia, serif;
    font-size: 10pt;
    line-height: 1.32;
    color: #0d1b2a;
    text-align: justify;
    hyphens: auto;
    -webkit-hyphens: auto;
}

/* Default page por chunk: chunk 0 = paratexto, restante = principal */
body.chunk-paratexto-inicial { page: paratexto-inicial; }
body.chunk-principal { page: principal; }

/* --------------------- Blocos de seção principais -------------------------- */
.paratexto-inicial { page: paratexto-inicial; }

.corpo-principal,
.manifesto-bloco,
.capitulo-bloco,
.framework-bloco,
.apendice-bloco,
.paratexto-final-bloco {
    page: principal;
}

/* Reset de contador de páginas no início do corpo principal (Manifesto C00M) */
.reset-arabica {
    counter-reset: page 0;
}

/* --------------------- Abertura de seção (capítulo/framework/apêndice) ---- */
.abertura-capitulo,
.abertura-framework,
.abertura-apendice,
.abertura-manifesto,
.abertura-paratexto-final {
    page: abertura-capitulo;
    page-break-before: always; /* nova página, sem forçar ímpar (economiza páginas em branco) */
    padding-top: 0;
}

/* Para o paratexto inicial: cada seção começa em página nova */
.abertura-paratexto {
    page-break-before: always;
}

/* --------------------- TÍTULOS (hierarquia) -------------------------------- */
h1, h2, h3, h4, h5, h6 {
    font-family: 'Charter', 'Bitstream Charter', 'DejaVu Serif', Georgia, serif;
    font-weight: 700;
    color: #0d1b2a;
    page-break-after: avoid;
    text-align: left;
}

/* H1 = abertura de capítulo: número grande à direita, título, linha laranja */
h1 {
    font-size: 30pt;
    line-height: 1.15;
    color: #0d1b2a;
    margin: 0 0 0.6cm 0;
    padding-bottom: 12pt;
    border-bottom: 3pt solid #E97451;
    string-set: chap-title content(), sect-title content();
    bookmark-level: 1;
    bookmark-state: open;
    letter-spacing: -0.5pt;
    font-weight: 800;
}

/* H1 dentro de abertura de capítulo recebe número grande antes do texto via JS pré-processado */
.abertura-capitulo h1 {
    margin-top: 0;
    font-size: 28pt;
}

/* Em paratexto inicial sem capítulo numerado, H1 é mais sóbrio */
.paratexto-inicial h1 {
    font-size: 22pt;
    border-bottom-width: 2pt;
}

/* H2 = seções X.1, X.2: borda lateral laranja */
h2 {
    font-size: 15pt;
    color: #1b263b;
    margin: 14pt 0 8pt 0;
    padding-left: 12pt;
    border-left: 4pt solid #E97451;
    line-height: 1.22;
    string-set: sect-title content();
    bookmark-level: 2;
}

h3 {
    font-size: 12pt;
    color: #1b263b;
    margin: 10pt 0 4pt 0;
    font-weight: 700;
    bookmark-level: 3;
}

h4 {
    font-size: 10.5pt;
    color: #1b263b;
    margin: 8pt 0 3pt 0;
    font-weight: 700;
    font-style: italic;
    bookmark-level: 4;
}

h5, h6 {
    font-size: 10pt;
    color: #1b263b;
    margin: 8pt 0 3pt 0;
    font-weight: 700;
}

/* --------------------- PARÁGRAFOS ------------------------------------------ */
p {
    margin: 0 0 0.1em 0;
    text-indent: 1.2em;
    orphans: 3;
    widows: 3;
}

/* Ficha catalográfica: campos Autor/Categoria/ISBN sem indentação, com pausa */
.ficha-dados p {
    text-indent: 0;
    margin: 0 0 0.5em 0;
}

/* Parágrafos com cara de "linha de dados" (Autor: X, Categoria: Y) recebem
   espaçamento extra para não grudarem em parede de texto. */
p > strong:first-child {
    /* nada visual no strong, mas o parágrafo que o contém merece pausa */
}

/* Primeiro parágrafo após título não tem recuo */
h1 + p, h2 + p, h3 + p, h4 + p, h5 + p, h6 + p,
blockquote + p.dropcap,
.epigrafe + p,
.linha-decorativa + p {
    text-indent: 0;
}

/* Espaçamento entre parágrafos para densidade legível */
p + p { margin-top: 0; }

/* --------------------- DROP CAP -------------------------------------------
   WeasyPrint tem bug com float:left em ::first-letter combinado com outros
   floats em árvore complexa. Usamos initial-letter (CSS Inline Layout Module
   Level 3), suportado pelo WeasyPrint 60+. Fallback: ::first-letter maior. */
p.dropcap {
    text-indent: 0;
}

p.dropcap::first-letter {
    font-family: 'Charter', 'Bitstream Charter', 'DejaVu Serif', Georgia, serif;
    initial-letter: 3 2;
    font-weight: 800;
    color: #0d1b2a;
    padding-right: 6pt;
}

/* --------------------- EPÍGRAFE (citação sob título do capítulo) ---------- */
.epigrafe {
    margin: 14pt 18pt 24pt 18pt;
    padding: 0;
    border: none;
    background: none;
    font-style: italic;
    color: #1b263b;
    font-size: 11pt;
    text-align: right;
    line-height: 1.4;
}
.epigrafe::before { content: "❝ "; color: #E97451; font-size: 14pt; }
.epigrafe::after { content: " ❞"; color: #E97451; font-size: 14pt; }
.epigrafe cite, .epigrafe .autor {
    display: block;
    font-style: normal;
    font-size: 9pt;
    color: #6b7280;
    margin-top: 6pt;
    letter-spacing: 0.5pt;
}

/* --------------------- BLOCKQUOTES (padrão) -------------------------------- */
blockquote {
    margin: 8pt 0;
    padding: 8pt 12pt;
    border-left: 3pt solid #E97451;
    background-color: #fefce8;
    font-style: italic;
    color: #1b263b;
    page-break-inside: avoid;
}
blockquote p { margin: 4pt 0; text-indent: 0; }

/* --------------------- BOX PARA EXECUTIVOS (🎯) --------------------------- */
.box-executivos {
    margin: 10pt 0;
    padding: 10pt 14pt 10pt 14pt;
    background-color: #fefce8;
    border-left: 4pt solid #0d1b2a;
    page-break-inside: avoid;
    position: relative;
    font-style: normal;
    color: #1b263b;
}
.box-executivos::before {
    content: "PARA EXECUTIVOS";
    display: block;
    background-color: #0d1b2a;
    color: #fef3c7;
    font-family: "DejaVu Sans", sans-serif;
    font-size: 8pt;
    font-weight: 700;
    letter-spacing: 1.2pt;
    padding: 3pt 8pt;
    margin: -10pt -14pt 8pt -14pt;
    text-align: left;
}
.box-executivos p { margin: 4pt 0; text-indent: 0; font-style: normal; }

/* --------------------- BOX ALERTA (⚠) ------------------------------------- */
.box-alerta {
    margin: 8pt 0;
    padding: 8pt 12pt 8pt 36pt;
    background-color: #fef3c7;
    border-left: 4pt solid #E97451;
    page-break-inside: avoid;
    position: relative;
    color: #1b263b;
}
.box-alerta::before {
    content: "▲";
    position: absolute;
    left: 14pt;
    top: 10pt;
    color: #E97451;
    font-size: 16pt;
    font-weight: 700;
    line-height: 1;
}
.box-alerta p { margin: 3pt 0; text-indent: 0; }
.box-alerta strong:first-child {
    display: block;
    font-family: "DejaVu Sans", sans-serif;
    font-size: 8.5pt;
    letter-spacing: 1pt;
    color: #E97451;
    margin-bottom: 4pt;
}

/* --------------------- BOX DICA / INSIGHT (💡) ---------------------------- */
.box-dica,
.box-insight {
    margin: 8pt 0;
    padding: 8pt 12pt 8pt 36pt;
    background-color: #f3f4f6;
    border-left: 4pt solid #D97706;
    page-break-inside: avoid;
    position: relative;
    color: #1b263b;
}
.box-dica::before,
.box-insight::before {
    content: "✸";
    position: absolute;
    left: 14pt;
    top: 10pt;
    color: #D97706;
    font-size: 14pt;
    line-height: 1;
}
.box-dica p, .box-insight p { margin: 3pt 0; text-indent: 0; }
.box-dica strong:first-child,
.box-insight strong:first-child {
    display: block;
    font-family: "DejaVu Sans", sans-serif;
    font-size: 8.5pt;
    letter-spacing: 1pt;
    color: #D97706;
    margin-bottom: 4pt;
}

/* --------------------- BOX TÉCNICO (🔧) ------------------------------------ */
.box-tecnico {
    margin: 8pt 0;
    padding: 8pt 12pt 8pt 36pt;
    background-color: #eff6ff;
    border-left: 4pt solid #1b263b;
    page-break-inside: avoid;
    position: relative;
    font-size: 10pt;
    color: #1b263b;
}
.box-tecnico::before {
    content: "⚙";
    position: absolute;
    left: 14pt;
    top: 10pt;
    color: #1b263b;
    font-size: 14pt;
    line-height: 1;
}
.box-tecnico p { margin: 3pt 0; text-indent: 0; }
.box-tecnico strong:first-child {
    display: block;
    font-family: "DejaVu Sans", sans-serif;
    font-size: 8.5pt;
    letter-spacing: 1pt;
    color: #1b263b;
    margin-bottom: 4pt;
}

/* --------------------- LISTAS --------------------------------------------- */
ul, ol {
    margin: 6pt 0 8pt 0;
    padding-left: 22pt;
}
li {
    margin-bottom: 2pt;
    line-height: 1.32;
}
li p { text-indent: 0; margin: 0; } /* parágrafo dentro de item: sem indent */
ul li::marker { color: #E97451; }
ol li::marker {
    font-family: "DejaVu Sans", sans-serif;
    font-weight: 700;
    color: #0d1b2a;
}

/* --------------------- TASK LIST (checklist com checkboxes) --------------- */
/* Pandoc converte "- [ ] item" em <ul class="task-list"><li><input ...></li></ul>.
   No HTML do pandoc, depois do <input> vem o texto direto, mas o <p> implícito
   do markdown bloco-nível joga o texto para linha de baixo. Solução robusta:
   forçar tudo dentro de <li> a renderizar inline + tirar o marker. */
ul.task-list {
    list-style: none;
    padding-left: 0;
    margin: 6pt 0 8pt 0;
}
ul.task-list > li {
    display: block;
    padding-left: 16pt;
    text-indent: -16pt;
    margin-bottom: 3pt;
    line-height: 1.32;
}
ul.task-list > li::marker,
ul.task-list > li::before { content: none !important; display: none !important; }
ul.task-list input[type="checkbox"] {
    display: inline-block;
    width: 8pt;
    height: 8pt;
    margin: 0 6pt 0 0;
    padding: 0;
    vertical-align: -1pt;
    border: 0.8pt solid #6b7280;
}
/* Caso pandoc envolva o texto em <p> dentro do <li>, força inline */
ul.task-list > li > p {
    display: inline;
    text-indent: 0;
    margin: 0;
}

/* --------------------- TABELAS -------------------------------------------- */
/* Tabelas precisam NUNCA quebrar palavras letra-por-letra (acontece quando o
   text-align: justify do body se combina com hyphens: auto e células estreitas).
   Forçamos text-align: left, word-spacing normal e quebra apenas em fronteiras
   reais de palavra para evitar o efeito "Q u a n t i z a ç ã o" vertical. */
table {
    width: 100%;
    border-collapse: collapse;
    margin: 10pt 0;
    font-size: 9pt;
    page-break-inside: auto; /* tabelas longas podem quebrar entre linhas */
    table-layout: auto;
    text-align: left;
    word-spacing: normal;
    hyphens: manual;
    -webkit-hyphens: manual;
}
th {
    background-color: #0d1b2a;
    color: #fef3c7;
    padding: 5pt 8pt;
    text-align: left;
    font-family: "DejaVu Sans", sans-serif;
    font-weight: 700;
    font-size: 8.5pt;
    letter-spacing: 0.3pt;
    vertical-align: middle;
    hyphens: manual;
    -webkit-hyphens: manual;
    word-break: normal;
    overflow-wrap: normal;
}
td {
    padding: 4pt 8pt;
    border-bottom: 0.5pt solid #d1d5db;
    vertical-align: top;
    line-height: 1.3;
    text-align: left;
    hyphens: manual;
    -webkit-hyphens: manual;
    word-break: normal;
    overflow-wrap: break-word;
    word-spacing: normal;
}
tr:nth-child(even) td { background-color: #fafafa; }
table p { text-indent: 0; margin: 0; text-align: left; word-spacing: normal; }

/* Tabelas curtas (4 ou menos linhas) podem ficar inteiras na página */
table.compacta { page-break-inside: avoid; }

/* Em tabelas longas, cabeçalho se repete entre páginas */
thead { display: table-header-group; }
tbody { display: table-row-group; }
tr { page-break-inside: avoid; }

/* --------------------- CÓDIGO --------------------------------------------- */
code {
    font-family: 'DejaVu Sans Mono', monospace;
    font-size: 9.5pt;
    background-color: #f3f4f6;
    padding: 1pt 4pt;
    color: #0d1b2a;
    border-radius: 2pt;
}
pre {
    background-color: #0d1b2a;
    color: #fef3c7;
    padding: 10pt 12pt;
    overflow: visible;
    font-size: 7.5pt;
    line-height: 1.3;
    page-break-inside: avoid;
    margin: 10pt 0;
    border-radius: 2pt;
    max-width: 100%;
    white-space: pre;
    word-wrap: normal;
    hyphens: none;
    -webkit-hyphens: none;
    word-spacing: normal;
}
pre code {
    background-color: transparent;
    color: #fef3c7;
    padding: 0;
    font-size: 7.5pt;
    white-space: pre;
    word-spacing: normal;
}

/* --------------------- IMAGENS / SVG / FIGURAS ---------------------------- */
img, svg {
    max-width: 100%;
    height: auto;
    display: block;
    margin: 14pt auto;
    page-break-inside: avoid;
}
figure {
    margin: 16pt 0;
    text-align: center;
    page-break-inside: avoid;
}
figcaption {
    font-family: "DejaVu Sans", sans-serif;
    font-size: 9pt;
    color: #6b7280;
    margin-top: 6pt;
    font-style: italic;
}
/* Figura placeholder discreta: só uma linha em itálico, sem caixa pesada */
.figura-placeholder { margin: 10pt 0; }
.figura-caixa {
    display: none; /* não mostra a caixa visual feia */
}
.figura-placeholder figcaption {
    font-style: italic;
    color: #6b7280;
    font-size: 9pt;
    text-align: center;
    border-top: 0.5pt solid #e5e7eb;
    border-bottom: 0.5pt solid #e5e7eb;
    padding: 4pt 0;
}

/* --------------------- LINKS ---------------------------------------------- */
a, a:link, a:visited {
    color: #D97706;
    text-decoration: none;
}

/* --------------------- SEPARADORES (---) ---------------------------------- */
hr {
    border: none;
    border-top: 1pt solid #E97451;
    margin: 18pt auto;
    width: 60%;
    opacity: 0.6;
    page-break-after: avoid;
}

/* --------------------- ÊNFASES -------------------------------------------- */
strong { color: #0d1b2a; font-weight: 700; }
em { color: #1b263b; font-style: italic; }

/* --------------------- ABERTURA DE CAPÍTULO (cabeçalho dedicado) ---------- */
.abertura-capitulo-header {
    padding-top: 1.5cm;
    margin-bottom: 1cm;
}
.abertura-capitulo-numero {
    font-family: 'Charter', 'DejaVu Serif', Georgia, serif;
    font-size: 80pt;
    font-weight: 800;
    color: #0d1b2a;
    line-height: 1;
    text-align: right;
    margin: 0;
    letter-spacing: -3pt;
}
.abertura-capitulo-numero .pequeno {
    font-size: 22pt;
    color: #6b7280;
    font-weight: 400;
    display: block;
    letter-spacing: 2pt;
    margin-bottom: 4pt;
}
.abertura-capitulo-titulo {
    font-family: 'Charter', 'DejaVu Serif', Georgia, serif;
    font-size: 24pt;
    font-weight: 700;
    color: #0d1b2a;
    line-height: 1.2;
    margin: 10pt 0 0 0;
    text-align: left;
}
.abertura-capitulo-linha {
    border: none;
    border-top: 3pt solid #E97451;
    width: 40%;
    margin: 20pt 0 24pt 0;
    opacity: 1;
}

/* --------------------- BANDEIRA DE NÍVEL (faixa no topo) ----------------- */
/* Faixa horizontal no topo da página de abertura (WeasyPrint não suporta
   bem position:absolute sangrando para fora do bloco, então usamos faixa). */
.bandeira-nivel {
    display: inline-block;
    background-color: #E97451;
    color: #fff;
    font-family: "DejaVu Sans", sans-serif;
    font-size: 8pt;
    font-weight: 700;
    letter-spacing: 1.5pt;
    padding: 4pt 14pt;
    text-transform: uppercase;
    margin: 0 0 14pt 0;
}
.bandeira-iniciante { background-color: #16a34a; }
.bandeira-iniciante-intermediario { background-color: #ca8a04; }
.bandeira-intermediario { background-color: #D97706; }
.bandeira-intermediario-avancado { background-color: #c2410c; }
.bandeira-avancado { background-color: #b91c1c; }
.bandeira-referencia { background-color: #1b263b; }
.bandeira-fundacao { background-color: #0d1b2a; }

/* --------------------- FRAMEWORK / APÊNDICE (selo dedicado) --------------- */
.selo-framework, .selo-apendice {
    display: inline-block;
    font-family: "DejaVu Sans", sans-serif;
    font-size: 9pt;
    font-weight: 700;
    letter-spacing: 2pt;
    color: #fef3c7;
    background-color: #0d1b2a;
    padding: 4pt 12pt;
    margin-bottom: 16pt;
    text-transform: uppercase;
    white-space: nowrap;
    hyphens: none;
    -webkit-hyphens: none;
}
.selo-apendice { background-color: #E97451; color: #fff; }

/* --------------------- AVOID PAGE BREAKS DENTRO DE ELEMENTOS CRÍTICOS ---- */
pre, blockquote, .box-executivos, .box-alerta, .box-dica, .box-tecnico { page-break-inside: avoid; }
/* Tabelas: longas podem quebrar, curtas (classe .compacta) ficam inteiras */
h1, h2, h3, h4 { page-break-after: avoid; }
/* Headers nunca ficam órfãos no fim da página: o conteúdo seguinte vem junto */
h2 + p, h2 + ul, h2 + ol, h2 + table, h2 + pre, h2 + blockquote,
h3 + p, h3 + ul, h3 + ol, h3 + table, h3 + pre, h3 + blockquote,
h4 + p, h4 + ul, h4 + ol, h4 + table, h4 + pre, h4 + blockquote {
    page-break-before: avoid;
}

/* --------------------- PARATEXTO INICIAL: sem text-indent --------------- */
/* Paratexto (dedicatória, prefácio, como ler, sumário, mapa de leitura) usa
   prosa curta. Identar primeira linha de cada parágrafo distrai mais do que
   ajuda, e produz o efeito "A quem teve paciência..." indentado no print 1. */
.paratexto-inicial p { text-indent: 0; }
.paratexto-inicial h1 + p,
.paratexto-inicial h2 + p,
.paratexto-inicial h3 + p { text-indent: 0; }

/* --------------------- AJUSTES FINOS DE DENSIDADE ------------------------- */
.paratexto-inicial { font-size: 10.5pt; line-height: 1.5; }
.framework-bloco { font-size: 10.5pt; line-height: 1.5; }
.apendice-bloco { font-size: 10pt; line-height: 1.45; }

/* Sumário e Mapa: tabelas mais compactas */
.paratexto-inicial table { font-size: 9pt; }
.paratexto-inicial td { padding: 4pt 6pt; }
"""


# ============================================================================
# 3) PRÉ-PROCESSAMENTO DE MARKDOWN
# ============================================================================

def ajustar_paths_de_imagem(conteudo, arquivo_origem):
    """Converte caminhos relativos de imagem para file://absoluto.

    Se a imagem não existir, substitui por uma legenda placeholder editorial
    (evita travar WeasyPrint com referências quebradas).
    """
    dir_origem = arquivo_origem.parent
    def substituir(match):
        alt = match.group(1)
        link = match.group(2)
        if link.startswith(('http://', 'https://', 'file://', 'data:')):
            return match.group(0)
        caminho_abs = (dir_origem / link).resolve()
        if caminho_abs.exists():
            return f'![{alt}](file://{caminho_abs})'
        # Imagem ausente: substitui por placeholder editorial em prosa
        legenda = alt if alt else Path(link).stem.replace('-', ' ').replace('_', ' ')
        return (f'\n\n<figure class="figura-placeholder">\n'
                f'<div class="figura-caixa">[ Figura: {legenda} ]</div>\n'
                f'<figcaption>{legenda}</figcaption>\n'
                f'</figure>\n')
    return re.sub(r'!\[([^\]]*)\]\(([^)]+)\)', substituir, conteudo)


def higienizar_editorial(conteudo, slug=None):
    """Remove resíduos de meta-briefing e placeholders editoriais.

    Aplicado antes de qualquer outra transformação. Cobre:
      - Placeholders [a ser atribuído], [a ser definido]
      - Linhas com colchetes ainda não preenchidos pela editora
      - Seções com TÍTULO 'XXX EDITORIAL' / 'ORELHA ESQUERDA' / etc.
      - Emojis funcionais inline (📚, 🔗, 📊) substituídos por marcadores
        tipográficos discretos.
    """
    # 1) Limpa placeholders entre colchetes que não devem ir ao livro
    conteudo = re.sub(r'\[a ser atribuído[^\]]*\]', '—', conteudo, flags=re.IGNORECASE)
    conteudo = re.sub(r'\[a ser definido[^\]]*\]', '—', conteudo, flags=re.IGNORECASE)
    conteudo = re.sub(r'\[a ser preenchido[^\]]*\]', '—', conteudo, flags=re.IGNORECASE)
    conteudo = re.sub(r'\[editora\]', 'Edição do Autor', conteudo)
    conteudo = re.sub(r'\[N\] p\.', '— p.', conteudo)

    # 2) Higieniza ficha catalográfica: remove seção "Impressão e distribuição"
    if slug == 'L1-00b-ficha-catalografica':
        conteudo = re.sub(
            r'## Impressão e distribuição.*?(?=\n##|\n\*Impresso)',
            '', conteudo, flags=re.DOTALL
        )
        # Remove "Páginas" e "ISBN" com placeholder, deixa apenas "Edição"
        conteudo = re.sub(r'\*\*Páginas:\*\*\s*—\s*\n?', '', conteudo)
        conteudo = re.sub(r'\*\*ISBN \(impresso\):\*\*\s*—\s*\n?', '**ISBN (impresso):** *Em processo de atribuição*\n', conteudo)
        conteudo = re.sub(r'\*\*ISBN \(digital\):\*\*\s*—\s*\n?', '**ISBN (digital):** *Em processo de atribuição*\n', conteudo)
        # Limpa CIP com "[N] p" → "— p"
        conteudo = re.sub(r'\[N\]', '—', conteudo)
        conteudo = re.sub(r'ISBN —', 'ISBN: Em atribuição', conteudo)

        # 2.1) Envolve o bloco contíguo de campos "**Campo:** valor" em <div class="ficha-dados">
        #      para que o CSS aplique text-indent:0 + margin-bottom:0.5em, evitando
        #      o efeito de parede de texto que apareceu na primeira diagramação.
        linhas = conteudo.split('\n')
        saida_ficha = []
        em_bloco = False
        for l in linhas:
            if re.match(r'^\*\*[^*]+:\*\*', l):
                if not em_bloco:
                    saida_ficha.append('<div class="ficha-dados">')
                    em_bloco = True
                saida_ficha.append(l)
            elif em_bloco and l.strip() == '':
                saida_ficha.append(l)
            else:
                if em_bloco:
                    saida_ficha.append('</div>')
                    em_bloco = False
                saida_ficha.append(l)
        if em_bloco:
            saida_ficha.append('</div>')
        conteudo = '\n'.join(saida_ficha)

    # 3) Limpa título do sumário: remove referência a "Orelhas" e "Quarta Capa"
    if slug == 'L1-04-sumario':
        conteudo = re.sub(r'\n- Orelhas\n', '\n', conteudo)
        conteudo = re.sub(r'\n- Quarta Capa\n', '\n', conteudo)

    # 4) Substitui emojis funcionais inline por marcadores tipográficos
    #    (apenas onde NÃO está em blockquote — blockquotes viram boxes especiais)
    linhas = conteudo.split('\n')
    saida = []
    for linha in linhas:
        if linha.startswith('>'):
            saida.append(linha)
            continue
        # Linhas tipo "📚 **Livros**" → "**◆ Livros**"
        l = linha
        l = re.sub(r'^📚\s*\*\*([^*]+)\*\*\s*$', r'**◆ \1**', l)
        l = re.sub(r'^🔗\s*\*\*([^*]+)\*\*\s*$', r'**▸ \1**', l)
        l = re.sub(r'^📊\s*\*\*([^*]+)\*\*\s*$', r'**▸ \1**', l)
        l = re.sub(r'^🎯\s*\*\*([^*]+)\*\*\s*$', r'**▸ \1**', l)
        # Emojis isolados em prosa: remover (e dar espaço duplo)
        l = re.sub(r'📚 ', '', l)
        l = re.sub(r'📊 ', '', l)
        l = re.sub(r'🔗 ', '', l)
        l = re.sub(r'🎯 ', '', l)
        l = re.sub(r'⚙️ ', '', l)
        saida.append(l)
    return '\n'.join(saida)


def converter_boxes_especiais(conteudo):
    """Converte blockquotes começando com emoji editorial em divs com classes.

    Padrões reconhecidos:
      > 🎯 **PARA EXECUTIVOS**\n> ...    → <div class="box-executivos">
      > ⚠️ **ALERTA**\n> ...             → <div class="box-alerta">
      > ⚠ **ALERTA**\n> ...
      > 💡 **DICA**\n> ...                → <div class="box-dica">
      > 💡 **INSIGHT**\n> ...             → <div class="box-insight">
      > 🔧 **TÉCNICO**\n> ...             → <div class="box-tecnico">
    """
    BOXES = [
        (r'🎯\s*\*\*PARA EXECUTIVOS\*\*', 'box-executivos', 'Para Executivos'),
        (r'⚠️?\s*\*\*ALERTA[^*]*\*\*',    'box-alerta',     'Alerta'),
        (r'💡\s*\*\*INSIGHT\*\*',          'box-insight',    'Insight'),
        (r'💡\s*\*\*DICA\*\*',             'box-dica',       'Dica'),
        (r'🔧\s*\*\*TÉCNICO[^*]*\*\*',     'box-tecnico',    'Técnico'),
        (r'🔧\s*\*\*BOX TÉCNICO[^*]*\*\*', 'box-tecnico',    'Técnico'),
    ]

    linhas = conteudo.split('\n')
    saida = []
    i = 0
    while i < len(linhas):
        linha = linhas[i]
        matched = False

        for padrao, classe, titulo in BOXES:
            # Procurar linha de blockquote começando com o emoji+rótulo
            m = re.match(r'^>\s*(' + padrao + r')\s*$', linha)
            if not m:
                continue
            # Coletar todas as linhas seguintes que sejam blockquote
            bloco = []
            i += 1
            while i < len(linhas) and (linhas[i].startswith('>') or linhas[i].strip() == ''):
                if linhas[i].startswith('>'):
                    bloco.append(re.sub(r'^>\s?', '', linhas[i]))
                    i += 1
                elif linhas[i].strip() == '' and i + 1 < len(linhas) and linhas[i+1].startswith('>'):
                    bloco.append('')
                    i += 1
                else:
                    break
            # Montar HTML do box (sem repetir o título — badge CSS já mostra)
            corpo_md = '\n'.join(bloco).strip()
            saida.append('')
            saida.append(f'<div class="{classe}">')
            saida.append('')
            saida.append(corpo_md)
            saida.append('')
            saida.append('</div>')
            saida.append('')
            matched = True
            break

        if not matched:
            saida.append(linha)
            i += 1

    return '\n'.join(saida)


def envolver_arquivo(conteudo, titulo, tipo, level=None, slug=None):
    """Envolve o conteúdo Markdown em um <section> com classes apropriadas.

    Adiciona:
      - section.tipo-bloco com page apropriada
      - section.abertura-tipo para forçar página ímpar
      - bandeira de nível (capítulos)
      - selo (frameworks, apêndices)
      - dropcap no primeiro parágrafo de capítulo
    """
    # Marca de reset de contador no Manifesto (primeira ocorrência arábica)
    reset_arabica = ' reset-arabica' if slug == 'L1-C00M-manifesto-invariantes' else ''

    # Bandeira de nível (apenas em capítulos)
    bandeira_html = ''
    if tipo == 'capitulo' and level:
        rotulo = {
            'iniciante': 'Iniciante',
            'iniciante-intermediario': 'Inic·Inter',
            'intermediario': 'Intermediário',
            'intermediario-avancado': 'Inter·Avanc',
            'avancado': 'Avançado',
            'fundacao': 'Fundação',
            'referencia': 'Referência',
        }.get(level, level.capitalize())
        bandeira_html = f'<div class="bandeira-nivel bandeira-{level}">{rotulo}</div>'

    # Selo para frameworks e apêndices
    selo_html = ''
    if tipo == 'framework':
        selo_html = '<div class="selo-framework">Framework</div>\n\n'
    elif tipo == 'apendice':
        selo_html = '<div class="selo-apendice">Apêndice</div>\n\n'

    # Classe da abertura conforme tipo
    classe_abertura = {
        'paratexto-inicial':  'abertura-paratexto',
        'paratexto-final':    'abertura-paratexto-final',
        'manifesto':          'abertura-manifesto',
        'capitulo':           'abertura-capitulo',
        'framework':          'abertura-framework',
        'apendice':           'abertura-apendice',
    }[tipo]

    # Classe do bloco
    classe_bloco = {
        'paratexto-inicial':  'paratexto-inicial',
        'paratexto-final':    'paratexto-final-bloco',
        'manifesto':          'manifesto-bloco',
        'capitulo':           'capitulo-bloco',
        'framework':          'framework-bloco',
        'apendice':           'apendice-bloco',
    }[tipo]

    # Marcar drop cap no primeiro parágrafo real (após linhas de título/HR/blockquote)
    # Estratégia simples: usar marcador raw HTML que pandoc preserva
    conteudo_processado = aplicar_drop_cap(conteudo) if tipo in ('capitulo', 'manifesto') else conteudo

    abre = (
        f'\n\n<section class="{classe_bloco}{reset_arabica}">\n'
        f'<div class="{classe_abertura}">\n'
        f'{bandeira_html}\n'
        f'{selo_html}'
    )
    fecha = '\n</div>\n</section>\n'

    return abre + conteudo_processado + fecha


def aplicar_drop_cap(conteudo):
    """Marca o primeiro parágrafo substancial após o título principal como dropcap.

    Insere um marcador HTML que sobrevive ao pandoc: parágrafo prefixado com
    <span class="dropcap-mark"></span> que CSS pega via :has() ou via classe.
    Como WeasyPrint não suporta :has(), usamos uma estratégia: wrappar com
    <div class="dropcap-wrap"><p class="dropcap">...</p></div> direto.
    """
    linhas = conteudo.split('\n')
    saida = []
    em_blockquote = False
    drop_aplicado = False
    pulou_titulo = False

    for idx, linha in enumerate(linhas):
        if not drop_aplicado and pulou_titulo:
            stripped = linha.strip()
            # Primeiro parágrafo substancial: não vazio, não título, não lista, não tabela, não HR, não blockquote, não imagem, não HTML
            if (stripped
                and not stripped.startswith(('#', '>', '-', '*', '|', '!', '<', '```', '---'))
                and not re.match(r'^\d+\.\s', stripped)):
                # Marca como dropcap via HTML inline para pandoc preservar
                saida.append('<p class="dropcap">' + stripped + '</p>')
                drop_aplicado = True
                continue

        if linha.startswith('# ') and not pulou_titulo:
            pulou_titulo = True

        saida.append(linha)

    return '\n'.join(saida)


# ============================================================================
# 4) CONSOLIDAÇÃO POR CHUNK
# ============================================================================

def consolidar_chunk(chunk_idx):
    nome, ini, fim = CHUNKS[chunk_idx]
    saida = ["---", 'title: "Inteligência Aumentada"', 'lang: pt-BR', "---", ""]
    for i in range(ini, fim):
        entry = ORDEM[i]
        caminho_rel, titulo, tipo = entry[0], entry[1], entry[2]
        level = entry[3] if len(entry) > 3 else None
        slug = Path(caminho_rel).stem
        caminho = BASE / caminho_rel
        if not caminho.exists():
            print(f"  ✗ FALTA: {caminho_rel}", file=sys.stderr)
            continue
        conteudo = caminho.read_text(encoding='utf-8')
        conteudo = higienizar_editorial(conteudo, slug=Path(caminho_rel).stem)
        conteudo = ajustar_paths_de_imagem(conteudo, caminho)
        conteudo = converter_boxes_especiais(conteudo)
        conteudo = envolver_arquivo(conteudo, titulo, tipo, level, Path(caminho_rel).stem)
        saida.append(conteudo)
    return "\n".join(saida)


# ============================================================================
# 5) COMANDOS
# ============================================================================

def cmd_prepare():
    print(f"Preparando build... ({len(CHUNKS)} chunks, {len(ORDEM)} arquivos)")
    (BUILD / "style.css").write_text(CSS, encoding='utf-8')
    print(f"  CSS escrito em {BUILD/'style.css'}")

    # Validar
    faltantes = []
    for entry in ORDEM:
        caminho_rel = entry[0]
        if not (BASE / caminho_rel).exists():
            faltantes.append(caminho_rel)
    if faltantes:
        print(f"  ✗ {len(faltantes)} arquivos faltam:")
        for f in faltantes:
            print(f"      {f}")
        sys.exit(1)
    print(f"  ✓ Todos os {len(ORDEM)} arquivos da ORDEM existem")

    for idx, (nome, ini, fim) in enumerate(CHUNKS):
        md = consolidar_chunk(idx)
        (BUILD / f"chunk-{idx:02d}-{nome}.md").write_text(md, encoding='utf-8')
        print(f"  ✓ chunk {idx:02d} ({nome}): {fim-ini} itens, {len(md)//1024} KB")
    print("Pronto.")


def cmd_chunk(idx, offset=None):
    """Gera o PDF de um chunk.

    Se `offset` é dado, injeta CSS para resetar counter(page) ao valor offset,
    de modo que a primeira página renderize como offset+1. Isso permite que o
    PDF final, mesclado com pdfunite, tenha numeração contínua.
    """
    md_path = sorted(BUILD.glob(f"chunk-{idx:02d}-*.md"))[0]
    html_path = BUILD / md_path.name.replace(".md", ".html")
    pdf_path = BUILD / md_path.name.replace(".md", ".pdf")
    print(f"Chunk {idx}: {md_path.name}" + (f" [offset={offset}]" if offset is not None else ""))
    # Gera HTML fragmento (sem --standalone) para evitar header com title automático
    pandoc_proc = subprocess.run([
        'pandoc', str(md_path),
        '-f', 'markdown+raw_html+definition_lists+fenced_code_blocks+pipe_tables+yaml_metadata_block',
        '-t', 'html5',
        '--wrap=preserve',
    ], check=True, capture_output=True, text=True)
    fragmento = pandoc_proc.stdout
    # Detecta se é o chunk 0 (paratexto-inicial) para escolher body class
    body_class = "chunk-paratexto-inicial" if idx == 0 else "chunk-principal"
    # Wrapper HTML mínimo
    html_full = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<title>Inteligência Aumentada</title>
</head>
<body class="{body_class}">
{fragmento}
</body>
</html>"""
    html_path.write_text(html_full, encoding='utf-8')
    print(f"  HTML: {html_path.name} ({html_path.stat().st_size//1024} KB)")
    import weasyprint
    stylesheets = [weasyprint.CSS(filename=str(BUILD / "style.css"))]
    if offset is not None:
        # Reset do contador de página: aplicado na primeira página de
        # qualquer tipo (@page :first). Isso faz a primeira página
        # renderizar como offset+1 e as subsequentes continuarem.
        offset_css = f"""
            @page :first {{ counter-reset: page {offset}; }}
            html {{ counter-reset: page {offset}; }}
        """
        stylesheets.append(weasyprint.CSS(string=offset_css))
    weasyprint.HTML(filename=str(html_path), base_url=str(BASE)).write_pdf(
        str(pdf_path), stylesheets=stylesheets
    )
    print(f"  PDF: {pdf_path.name} ({pdf_path.stat().st_size//1024} KB)")


# OFFSETS = valor que counter-reset deve receber, igual ao número da PRIMEIRA
# página do chunk (a auto-incrementação acontece DEPOIS do render no WeasyPrint).
# chunk 0 = paratexto, numeração romana, sem offset.
# Valores recalibrados após higienização editorial.
OFFSETS = {
    0: None,
    1: 1,
    2: 34,
    3: 98,
    4: 146,
    5: 187,
    6: 259,
    7: 298,
    8: 377,
    9: 435,
    10: 531,
    11: 605,
    12: 659,
    13: 691,
    14: 748,
    15: 816,
}


def cmd_capas():
    """Gera PDFs das capas a partir dos SVGs."""
    import weasyprint
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
        html_path = BUILD / f"{tag}.html"
        html_path.write_text(html)
        pdf_path = BUILD / f"{tag}.pdf"
        weasyprint.HTML(filename=str(html_path)).write_pdf(str(pdf_path))
        print(f"  ✓ {tag}.pdf ({pdf_path.stat().st_size//1024} KB)")


def cmd_merge():
    """Merge final usando pikepdf (10-30x mais rápido que pypdf para livros longos).
    pikepdf preserva os bookmarks/outline de cada chunk quando estendido via pages.extend."""
    import pikepdf
    final = BASE / "Inteligencia-Aumentada-L1-DIAGRAMADO.pdf"
    out = pikepdf.Pdf.new()
    capa = BUILD / "capa-frontal.pdf"
    if capa.exists():
        with pikepdf.open(str(capa)) as src:
            out.pages.extend(src.pages)
        print(f"  + capa-frontal.pdf")
    for idx in range(len(CHUNKS)):
        candidatos = sorted(BUILD.glob(f"chunk-{idx:02d}-*.pdf"))
        if not candidatos:
            print(f"  ✗ FALTA: chunk {idx:02d}")
            continue
        with pikepdf.open(str(candidatos[0])) as src:
            out.pages.extend(src.pages)
        print(f"  + {candidatos[0].name}")
    quarta = BUILD / "quarta-capa.pdf"
    if quarta.exists():
        with pikepdf.open(str(quarta)) as src:
            out.pages.extend(src.pages)
        print(f"  + quarta-capa.pdf")
    out.save(str(final))
    out.close()
    tamanho = final.stat().st_size / (1024 * 1024)
    print(f"\n✓ PDF final: {final.name} ({tamanho:.2f} MB)")


def cmd_all():
    cmd_prepare()
    cmd_capas()
    for idx in range(len(CHUNKS)):
        cmd_chunk(idx)
    cmd_merge()


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    cmd = sys.argv[1]
    if cmd == "prepare":  cmd_prepare()
    elif cmd == "chunk":
        idx = int(sys.argv[2])
        if "--offset" in sys.argv:
            off = int(sys.argv[sys.argv.index("--offset")+1])
            cmd_chunk(idx, offset=off)
        elif "--use-offsets" in sys.argv:
            cmd_chunk(idx, offset=OFFSETS.get(idx))
        else:
            cmd_chunk(idx)
    elif cmd == "capas":  cmd_capas()
    elif cmd == "merge":  cmd_merge()
    elif cmd == "all":    cmd_all()
    else:
        print(f"Comando desconhecido: {cmd}")
        sys.exit(1)


if __name__ == "__main__":
    main()
