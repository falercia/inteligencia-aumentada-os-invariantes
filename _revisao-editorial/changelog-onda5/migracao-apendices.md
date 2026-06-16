# Changelog — Migração Terminológica: Apêndices (04-apendices/)

**Data:** 2026-06-16
**Escopo:** Pasta `04-apendices/` — 17 arquivos .md
**Operação:** "Princípios" (sistema dos nove) → "Invariantes" em todo o livro
**Editor:** agente (Claude Sonnet 4.6), revisão humana pendente

---

## Resumo executivo

| Métrica | Valor |
|---|---|
| Ocorrências trocadas (sistema dos nove) | ~130 |
| Ocorrências preservadas (genéricas / condutores) | ~27 |
| Arquivos tocados | 12 de 17 |
| Arquivos sem ocorrência (sem mudança) | 5 (APX-D, APX-E, APX-F e arquivos sem "princíp") |
| Fixes pontuais | 2 (DeepSeek Nature + confirmação arXiv Hayes et al.) |

---

## Por arquivo — trocas realizadas

### L1-APX-A-glossario.md
**Trocas:** 18
- Cabeçalho de seção: "I. Princípios e sistema da obra" → "I. Invariantes e sistema da obra"
- Todas as entradas de definição dos nove: "Princípio N:" → "Invariante N:" (Invariantes 1–9)
- Frameworks: "Framework do Princípio N" / "Framework dos Princípios N e M" → "Framework do Invariante N" / "Framework dos Invariantes N e M" (9 entradas)
- "Sistema que opera os princípios" → "Sistema que opera os invariantes"
- "Lost in the Middle. Base do Princípio 2." → "Base do Invariante 2."

**Preservados:**
- "Constitutional AI (CAI). Técnica de alinhamento em que princípios em linguagem natural…" — genérico (princípios da CAI constitution)
- "RLAIF. Variante em que comparação é feita por outro modelo IA seguindo princípios." — genérico

---

### L1-APX-B-mapa-mental.md
**Trocas:** 13
- Subtítulo: "Os Nove Princípios como esqueleto cognitivo" → "Os Nove Invariantes como esqueleto cognitivo"
- Parágrafo de abertura: "a partir dos Nove Princípios" / "é instância de um ou mais princípios" → "Invariantes" / "invariantes"
- ASCII art linha central: "OS NOVE PRINCÍPIOS PERMANENTES" → "OS NOVE INVARIANTES" (alinhamento da moldura │ │ mantido em 61 chars)
- Legenda ASCII: "(princípios duráveis, sistema citável)" → "(invariantes duráveis, sistema citável)"
- Legenda frameworks: "(decisão prática que opera cada princípio)" → "(decisão prática que opera cada invariante)"
- Nota do diagrama: "Os nove princípios têm peso equivalente" → "Os nove invariantes têm peso equivalente"
- Cabeçalhos de seção: "A roda dos Nove Princípios" → "A roda dos Nove Invariantes"; "Princípio × Framework × Capítulo" → "Invariante × Framework × Capítulo"; "Trilha temática × Princípio" → "Trilha temática × Invariante"; "Capítulo × Princípio primário e secundário" → "Capítulo × Invariante primário e secundário"; "Relações críticas entre princípios" → "Relações críticas entre invariantes"
- Cabeçalho de tabela: "| Princípio |" e "| Princípio dominante |" → "| Invariante |" e "| Invariante dominante |"
- Linha introdução capítulo: "Os Nove Princípios | Todos" → "Os Nove Invariantes | Todos"
- Como usar: "Identifique o princípio associado" / "roda dos Nove Princípios" / "qual princípio foi violado" → invariante(s)

**Cabeçalhos renomeados:**
- `## A roda dos Nove Princípios` → `## A roda dos Nove Invariantes`
- `## Princípio × Framework × Capítulo` → `## Invariante × Framework × Capítulo`
- `## Trilha temática × Princípio` → `## Trilha temática × Invariante`
- `## Capítulo × Princípio primário e secundário` → `## Capítulo × Invariante primário e secundário`
- `## Relações críticas entre princípios` → `## Relações críticas entre invariantes`

---

### L1-APX-C-roadmaps.md
**Trocas:** 14
- "Apresentar os Nove Princípios ao primeiro escalão" → "Nove Invariantes"
- "cartaz dos Princípios da empresa" → "dos Invariantes"
- "princípio aplicado ou violado" → "invariante aplicado ou violado"
- "Mapear violações dos Nove Princípios" → "Nove Invariantes"
- "Time aplicando os Princípios como norma" → "os Invariantes"
- "Mentor de outros devs no método dos Princípios" → "dos Invariantes"
- "Produzir entrega usando os Princípios como vocabulário" → "os Invariantes"
- "Workshop dos Nove Princípios para clientes" → "Nove Invariantes"
- "Workshop ou minicurso usando os Princípios" → "os Invariantes"
- "um princípio por semana" / "dos Nove Princípios à audiência" → "um invariante" / "dos Nove Invariantes"
- "com princípio associado" → "com invariante associado"
- "qual princípio explicou o resultado" → "qual invariante"
- "ao menos um dos Nove Princípios" / "citação dos Princípios" → "dos Nove Invariantes" / "dos Invariantes"
- "com métrica, princípio associado" → "invariante associado"
- "cartaz dos Princípios em vista" / "contra os Nove Princípios" → "dos Invariantes" / "dos Nove Invariantes"
- "Aplicação cultural dos Princípios" → "dos Invariantes"

---

### L1-APX-G-papers.md
**Trocas:** 1
- "Base empírica do princípio das extremidades." → "do invariante das extremidades."

---

### L1-APX-H-bibliografia.md
**Trocas:** 3
- "base conceitual do Princípio 9 — Operador" → "do Invariante 9"
- "Inteligência Aumentada — Os Nove Princípios Permanentes" → "Os Nove Invariantes"
- "Os Nove Princípios sintetizam padrões observáveis…" → "Os Nove Invariantes"

**Cabeçalhos renomeados:**
- Seção V: entrada do livro mudou de "Os Nove Princípios Permanentes" para "Os Nove Invariantes"

---

### L1-APX-I-indice-remissivo.md
**Trocas:** 16
- Subtítulo: "Termos, métodos, princípios e casos" → "Termos, métodos, invariantes e casos"
- Todas as entradas de índice: "Princípio N" → "Invariante N" (Invariantes 1, 2, 3, 4, 5, 6, 7, 8, 9)
- "Os Nove Princípios ★" e "Nove Princípios ★" → "Os Nove Invariantes ★" e "Nove Invariantes ★"
- "método derivado do/dos Princípio(s) N" → "Invariante(s)"
- "tabela Princípio × Framework" → "tabela Invariante × Framework"
- "Princípios 4 e 8" → "Invariantes 4 e 8"; "Princípios 2 e 3" → "Invariantes 2 e 3"; "Princípios 4 e 6" → "Invariantes 4 e 6"

---

### L1-APX-J-trilha-do-numero.md
**Trocas:** 1 (terminológica) + 1 (Fix 1)
- "Princípio Três, a Camada Dupla" → "Invariante Três, a Camada Dupla"

**FIX 1 — Atualização DeepSeek Nature:**
- Linha do paper DeepSeek-R1: texto anterior dizia "publicação em periódico revisado por pares não confirmada até a data desta revisão"
- Novo texto: "divulgado via arXiv:2501.12948; publicado em *Nature*, vol. 645, pp. 633–638, 2025 (DOI: 10.1038/s41586-025-09422-z)"
- URL arXiv 2501.12948 mantida.

---

### L1-APX-K-gabaritos.md
**Trocas:** 7
- Nota editorial: "Os Nove Princípios" → "Os Nove Invariantes"
- Cabeçalho de seção: "Introdução — Os Nove Princípios (C00P + C01)" → "Os Nove Invariantes"
- "uma por princípio" → "uma por invariante"
- "com os nove princípios" → "com os nove invariantes"
- "Projeto — Cartaz dos Princípios da empresa" → "Cartaz dos Invariantes da empresa"
- "reconhece os nove princípios" / "princípios copiados" / "nove princípios presentes" → invariante(s)
- "sete princípios em português" → "sete invariantes em português" (×2: Exercício 3 e Rubrica)

**Cabeçalhos renomeados:**
- `## Introdução — Os Nove Princípios (C00P + C01)` → `## Introdução — Os Nove Invariantes (C00P + C01)`
- `### Projeto — Cartaz dos Princípios da empresa` → `### Projeto — Cartaz dos Invariantes da empresa`

---

### L1-APX-L-biblioteca-prompts.md
**Trocas:** 3
- "materializa o Princípio Três, a Camada Dupla" → "Invariante Três"
- "O princípio que cada ficha ilustra é o invariante que vale ler aqui" → "O invariante que cada ficha ilustra é o que vale ler aqui"
- Coluna: "| Princípio ilustrado |" → "| Invariante ilustrado |"

**Preservados:**
- "princípios de engenharia de contexto" (×2, linhas 7 e 13) — genérico, práticas de context engineering
- "que princípio de engenharia de contexto está sendo aplicado aqui?" — idem

---

### L1-APX-M-manifesto-bolso.md
**Trocas:** 9
- Título do arquivo: "Os Nove Princípios em Uma Página" → "Os Nove Invariantes em Uma Página"
- Cabeçalho de seção: "## Os Nove Princípios" → "## Os Nove Invariantes"
- Tabela "Como usar": "Princípio 4/5/6/7/8 e 9/3:" → "Invariante 4/5/6/7/8 e 9/3:" (6 linhas)
- Ressalva: "Os Princípios 1 e 2" / "Os outros sete são princípios de prática" → "Os Invariantes 1 e 2" / "os outros sete são invariantes de prática"
- Atribuição: "Os Nove Princípios Permanentes da Inteligência Artificial" → "Os Nove Invariantes da Inteligência Artificial"

**Cabeçalhos renomeados:**
- `# Apêndice M — Manifesto de Bolso: Os Nove Princípios em Uma Página` → `# Apêndice M — Manifesto de Bolso: Os Nove Invariantes em Uma Página`
- `## Os Nove Princípios` → `## Os Nove Invariantes`

---

### L1-APX-N-metodologico-numeros.md
**Trocas:** 2
- "conforme o Princípio Três e o Framework Nove" → "Invariante Três"
- "Os nove Princípios e as suas mecânicas" → "Os nove Invariantes"

---

### L1-APX-O-caderno-governanca-v1.md
**Trocas:** 9 — arquivo de atenção máxima (dois sentidos de "princípio")
- "os invariantes que o sustentam" (linha 7) — referência ao sistema dos nove
- "materializa o Invariante Três, a Camada Dupla" (linha 11)
- "Princípio Oito, Responsabilidade Indelegável" → "Invariante Oito" (linha 43, tabela de blocos)
- Seção header: "## Os nove princípios que sustentam o caderno" → "## Os nove invariantes que sustentam o caderno"
- "os Nove Princípios da obra" → "os Nove Invariantes da obra" (linha 78)
- "revisitar os princípios em sua versão completa" → "revisitar os invariantes" (linha 78)
- Cabeçalho de tabela: "| Princípio |" → "| Invariante |" (linha 80)
- Quatro linhas da tabela: "Princípio 1 ·", "Princípio 3 ·", "Princípio 6 ·", "Princípio 8 ·" → "Invariante 1 ·", etc.
- "Os outros cinco princípios" → "Os outros cinco invariantes" (linha 87)
- "sem renomear os Nove Princípios da obra" → "os Nove Invariantes da obra" (linha 113)
- "Customização que apaga o Princípio Oito" → "o Invariante Oito" (linha 113)
- "viola o Princípio Oito por omissão estrutural" → "o Invariante Oito" (linha 132)
- "regra fundamental do Princípio Oito" → "do Invariante Oito" (linha 172)

**Preservados (APX-O — detalhado conforme instrução):**
- "os princípios que o sustentam" — substituído → "os invariantes que o sustentam" (já incluído acima)
- "princípios condutores" (linha 17, quadro de orientação) — PRESERVADO: são os princípios condutores customizados da organização
- "| 1. Identificação, escopo e princípios |" (linha 42) — PRESERVADO: nome da seção do caderno operacional
- "quais princípios condutores a organização adota" (linha 42) — PRESERVADO: princípios condutores da org
- "**Princípios condutores customizados ao vocabulário da organização**" (linha 113) — PRESERVADO: título do padrão de adaptação
- "por princípio" (linha 103) — PRESERVADO: expressão idiomática genérica ("regulação setorial sobrescreve governança interna por princípio")
- "customizar a identificação e os princípios na seção 01" (linha 166) — PRESERVADO: refere-se aos princípios condutores da org na seção 01 do caderno
- Arquivo de repo `governance/v1/01-identificacao-escopo-principios.md` (linha 87 e 166) — PRESERVADO: nome de arquivo, não renomear

---

### L1-APX-P-boxes-tecnicos.md
**Trocas:** 3
- Tabela mapa de boxes: "Transversal aos nove Princípios" → "Transversal aos nove Invariantes"
- Cabeçalho de coluna: "| Princípio relacionado |" → "| Invariante relacionado |"
- Nota: "os Princípios (P1 a P9) são definidos no capítulo de abertura" → "os Invariantes (P1 a P9)"

**Preservados:**
- "a clareza dos princípios que orientam a tomada de decisão" (linha 12) — genérico: princípios de arquitetura/design
- "em princípio, ser usada para validar pós-hoc" (linha 319) — expressão idiomática ("in principle")

---

### L1-APX-Q-manual-do-professor.md
**Trocas:** 4
- Tabela 60h: "Discussão em grupo sobre Princípios" → "sobre Invariantes"
- Tabela 40h: "Princípios e Camada Dupla" → "Invariantes e Camada Dupla"
- Tabela 20h: "C00P, Princípios e Camada Dupla" → "C00P, Invariantes e Camada Dupla"
- Ponto de travamento: "Confundir Princípio Um, a plausibilidade" → "Invariante Um"

**Preservados:**
- "princípios de governança, arquitetura RAG" (linha 202) — genérico: princípios de governança organizacional

---

### Arquivos sem ocorrência (inalterados)
- L1-APX-D-ferramentas.md
- L1-APX-E-leituras.md
- L1-APX-F-newsletters.md

---

## Fix 1 — Nota DeepSeek desatualizada (APX-J)

**Arquivo:** `L1-APX-J-trilha-do-numero.md`
**Linha:** tabela de papers (seção 3), entrada DeepSeek-R1

**Antes:** "janeiro de 2025, divulgado por seus autores via arXiv (publicação em periódico revisado por pares não confirmada até a data desta revisão)"

**Depois:** "janeiro de 2025, divulgado via arXiv:2501.12948; publicado em *Nature*, vol. 645, pp. 633–638, 2025 (DOI: 10.1038/s41586-025-09422-z)"

URL arXiv original (arxiv.org/abs/2501.12948) mantida na coluna URL.

---

## Fix 2 — Confirmação arXiv Hayes et al. (APX-J e APX-P)

**Grep executado em:** `04-apendices/L1-APX-J-trilha-do-numero.md` e `04-apendices/L1-APX-P-boxes-tecnicos.md`

**Resultado:**
- APX-J linha 86: `arxiv.org/abs/2410.22884` — CORRETO
- APX-P linha 62: `arxiv.org/abs/2410.22884` — CORRETO (já corrigido em onda anterior)

Nenhuma ocorrência de `2410.10074` nos arquivos de conteúdo editorial da pasta `04-apendices/`. O número errado persiste apenas em backups e changelogs históricos (onde é registro correto de origem).

**Conclusão Fix 2:** nenhuma edição necessária — ambos já citam o número canônico `2410.22884`.

---

## Verificação ASCII art (APX-B)

Linha original:
```
              │      OS NOVE PRINCÍPIOS PERMANENTES         │
```
Caracteres internos (entre │): 45 chars

Linha nova:
```
              │      OS NOVE INVARIANTES                    │
```
Caracteres internos: 45 chars — alinhamento mantido.

Segunda linha (frameworks):
```
              │  (decisão prática que opera cada invariante)│
```
Caracteres internos: 45 chars — alinhamento mantido.

Todas as bordas da moldura permanecem em 61 caracteres.

---

*Changelog gerado em: 2026-06-16. Migração executada no contexto da Onda 5 — revisão editorial.*
