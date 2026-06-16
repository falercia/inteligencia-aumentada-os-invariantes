# Changelog Onda 2 — Apêndices L, D, E e F
## Durabilidade: enxugamento de conteúdo perecível para MÉTODO + PONTEIRO

**Data:** 2026-06-16
**Editor executivo:** Fabio Garcia
**Operação:** Onda 2 — Durabilidade

---

## APX-L — Biblioteca de Prompts Profissionais

**Arquivo:** `04-apendices/L1-APX-L-biblioteca-prompts.md`

**Antes:** ~13.000 palavras / 1.623 linhas. Conteúdo: Moldura de método + 30 fichas conceituais completas (cada uma com dor, domínio, F4, quando usar/evitar, anti-padrões, modelo recomendado, métrica de qualidade, versão executável) + changelog editorial de 6 prompts.

**Depois:** ~2.000 palavras / 215 linhas.

**O que saiu:**
- As 30 fichas conceituais completas (campos: dor, domínio, F4, quando usar/evitar, anti-padrões, modelo, métrica, versão executável)
- O changelog editorial de 6 prompts (P-LEG-01, P-MED-01, P-FIN-02, P-LEG-03, P-SUP-01, P-EDU-02)

**O que ficou:**
- Moldura de método completa (blockquote de abertura sobre o que cada prompt é e o que não envelhece)
- Seção "Por que este apêndice existe em duas camadas" com quadro de orientação (onde vive o quê)
- Seção "A anatomia que toda ficha aplica" — tabela F4, blocos `<prefill>` e `<self_critique>`, convenção de modelo, exemplo estrutural comentado em XML
- Seção "Padrões de operação" (7 padrões)
- Seção "Anti-padrões transversais de prompt" (tabela de 8 itens)
- Seção "Como ler as fichas" (tabela de 9 campos)
- **NOVO:** Tabela-índice dos 30 prompts (ID, nome, setor, princípio ilustrado, link para pasta no repo)
- Ponteiro canônico para `/prompts` no repositório
- Assinatura de fechamento do apêndice

**Razão:** As fichas completas são conteúdo XML/conceitual com nomes de modelo, benchmarks e detalhes de escopo que envelhecem com cada nova geração de modelo. O invariante — a anatomia F4, os 7 padrões, os 8 anti-padrões, a lógica de camada dupla — permanece. A tabela-índice preserva a navegabilidade para os 30 prompts sem congelar o detalhe no livro.

---

## APX-D — Ferramentas e Stack

**Arquivo:** `04-apendices/L1-APX-D-ferramentas.md`

**Antes:** ~2.500 palavras / 168 linhas. Conteúdo: Framework de seleção (D.0 e D.1 com tabela de 6 dimensões) + catálogo por categoria (D.2 a D.10: plataformas de inferência, modelos open weights, frameworks de agente, bancos vetoriais, observabilidade, evals, MCP, gestão de prompts, cadência de revisão).

**Depois:** ~600 palavras / 38 linhas.

**O que saiu:**
- D.2 — Plataformas de inferência (LLM-as-a-Service): tabela com 6 provedores e critério recomendado
- D.3 — Modelos open weights para self-host: tabela com 6 famílias e critério
- D.4 — Frameworks de agente e orquestração: tabela com 5 frameworks e critério
- D.5 — Bancos vetoriais: tabela com 6 opções e critério
- D.6 — Observabilidade e LLMOps: tabela com 5 ferramentas e critério
- D.7 — Frameworks de evals: tabela com 4 opções e critério
- D.8 — MCP: tabela com 4 itens e critério
- D.9 — Repositórios e gestão de prompts: tabela com 4 opções e critério
- D.10 — Cadência de revisão

**O que ficou:**
- D.0 — Argumento editorial (por que data explícita e critério importam mais que inventário)
- D.1 — Framework de 6 dimensões de seleção (tabela com dimensão, o que avaliar, sinal de risco)
- Ponteiro canônico para `ferramentas` no repositório
- Nota de fechamento descrevendo o que o catálogo cobre

**Razão:** O catálogo de ferramentas datado em junho/2026 é o item mais perecível da obra. Modelos são adquiridos, descontinuados, mudam de licença. O critério de seleção em 6 dimensões é o invariante: serve para avaliar qualquer ferramenta que apareça nos próximos 10 anos.

---

## APX-E — Leituras Complementares → Como montar sua dieta de informação

**Arquivo:** `04-apendices/L1-APX-E-leituras.md`

**Antes:** ~700 palavras / 67 linhas. Conteúdo: Listas de livros (fundamentos de IA, IA aplicada, governança) + blogs e newsletters + cursos.

**Depois:** ~1.100 palavras / 67 linhas (novo conteúdo de método + ponteiro).

**Operação:** Substituição completa do conteúdo. O arquivo foi transformado de lista de leituras em documento de método fundido com APX-F.

**O que saiu:**
- Lista de livros de fundamentos (Russell & Norvig, Bishop, Goodfellow, Murphy)
- Lista de livros de IA aplicada (Karpathy, Engelbart, Christian, Russell)
- Lista de livros de governança (Beyer, Doerr, Allspaw, Davenport)
- Lista de blogs e newsletters (10 itens)
- Lista de cursos (8 itens)

**O que entrou (novo conteúdo de método):**
- Argumento por que a dieta precisa de método (não de lista maior)
- 4 critérios para escolher fontes: especificidade de público, rastreabilidade de origem, cadência sustentável, atualização explícita de erro
- Arquitetura de dieta equilibrada em 3 camadas (fronteira / aplicação / contexto local)
- Tabela de cadência recomendada (blocos semanais com duração e propósito)
- Sinais de qualidade e sinais de alerta
- Como tratar a cena brasileira (uso correto de conteúdo nacional vs. internacional)
- Ponteiro para listas específicas no repositório (`fontes`)

**Incorporação do APX-F:** O conteúdo temático do APX-F (comunidade brasileira, critério de cena local) foi absorvido na seção "Como tratar a cena brasileira" e no argumento de arquitetura de 3 camadas. As listas específicas (newsletters, podcasts, conferências, pesquisadores, empresas) vão para o repositório junto com as listas do APX-E original.

---

## APX-F — Comunidade Brasileira de IA → Stub de redirecionamento

**Arquivo:** `04-apendices/L1-APX-F-newsletters.md`

**Antes:** ~2.300 palavras / 154 linhas. Conteúdo: Argumento da cena brasileira + 8 seções (newsletters, podcasts, conferências, comunidades online, pesquisadores, empresas, crítica honesta da cena, como contribuir).

**Depois:** ~250 palavras / 25 linhas (stub de redirecionamento).

**Operação:** Arquivo preservado (para não quebrar referências existentes) e transformado em stub que redireciona para APX-E e para o repositório.

**O que saiu:**
- As 8 seções de conteúdo (newsletters: 5 fontes com descrição; podcasts: 7 com nota editorial; conferências: 6; comunidades online: 5; pesquisadores: 5 + nota de extensão; empresas: 5 + lista de extensão; crítica honesta; como contribuir)

**O que ficou:**
- Título e nota de redirecionamento explicando a fusão
- Link para APX-E (método)
- Ponteiro canônico para `fontes` no repositório

**Razão:** O arquivo é mantido como stub para não quebrar sumário, índice ou referências cruzadas existentes. O conteúdo migrou para APX-E (método) e repositório (listas).

---

## Resumo de contagem (APX-L, foco do briefing)

| Versão | Palavras aprox. | Linhas |
|---|---|---|
| Antes (Onda 1) | ~13.000 | 1.623 |
| Depois (Onda 2) | ~2.000 | 215 |
| Redução | ~85% | ~87% |
