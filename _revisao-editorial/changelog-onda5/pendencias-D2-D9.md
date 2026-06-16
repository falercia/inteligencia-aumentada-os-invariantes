# Changelog Onda 5 — Pendências D2, D3, D4, D5, D9
*Data: 2026-06-16 | Executor: Editor Executivo*

---

## D2 — TÍTULO CANÔNICO DO MANIFESTO: "Princípios Permanentes" → "Nove Invariantes"

### Problema
O nome do manifesto (o conjunto dos nove) aparecia em paratexto e manifesto como "Princípios Permanentes", em conflito com o título canônico do arquivo fonte: "Os Nove Invariantes da Inteligência Artificial".

### Decisão
Canônico: **"Os Nove Invariantes da Inteligência Artificial"** (alinhado ao título do livro). Correto apenas onde "Princípios Permanentes" é o nome/título do conjunto — não onde é o subtítulo comercial do livro ("Os Princípios Permanentes da IA").

### Grep completo executado em 00-paratexto/ e 01-manifesto/

**Ocorrências encontradas e classificação:**

| # | Arquivo | Linha | Texto original | Tipo | Ação |
|---|---------|-------|----------------|------|------|
| 1 | `L1-04-sumario.md` | 24 | `## OS NOVE PRINCÍPIOS PERMANENTES` | Nome do conjunto/manifesto | CORRIGIDO |
| 2 | `L1-04-sumario.md` | 28 | `Manifesto — Os Nove Princípios Permanentes da Inteligência Artificial` | Nome do manifesto | CORRIGIDO |
| 3 | `L1-04-sumario.md` | 2 | `## *Inteligência Aumentada · Os Princípios Permanentes da IA*` | Subtítulo comercial do livro | MANTIDO (não é o nome do manifesto) |
| 4 | `L1-05-mapa-de-leitura-por-nivel.md` | 53 | `Manifesto C00M — Os Nove Princípios Permanentes` | Nome do manifesto | CORRIGIDO |
| 5 | `L1-00c2-promessa.md` | 9 | `Os **Nove Princípios Permanentes** que sustentam toda a obra` | Nome do conjunto | CORRIGIDO |
| 6 | `L1-00c2-promessa.md` | 13 | `**Nove Princípios Permanentes** memorizáveis` | Nome do conjunto | CORRIGIDO |
| 7 | `L1-11-orelhas.md` | 9 | `Nove Princípios Permanentes formam a espinha intelectual` | Nome do conjunto | CORRIGIDO |
| 8 | `L1-03-introducao.md` | 46 | `os **Nove Princípios Permanentes da Inteligência Artificial**` | Nome do manifesto | CORRIGIDO |
| 9 | `L1-01-prefacio.md` | 37 | `**Nove Princípios Permanentes da Inteligência Artificial**` | Nome do manifesto | CORRIGIDO |
| 10 | `L1-12-quarta-capa.md` | 11 | `os Nove Princípios Permanentes, costurados` | Nome do conjunto | CORRIGIDO |
| 11 | `L1-12-quarta-capa.md` | 9 | `*Inteligência Aumentada — Os Princípios Permanentes da IA*` | Subtítulo comercial do livro | MANTIDO |
| 12 | `L1-12-quarta-capa.md` | 24 | `### *Os Princípios Permanentes da IA*` | Subtítulo comercial do livro | MANTIDO |
| 13 | `L1-00-capa-e-titulos.md` | 2, 9, 51, 65 | `Os Princípios Permanentes da IA` (várias instâncias) | Subtítulo comercial do livro | MANTIDO (4 instâncias) |
| 14 | `L1-00b-ficha-catalografica.md` | 5 | `*Os Princípios Permanentes da IA*` | Subtítulo comercial do livro | MANTIDO |
| 15 | `L1-10-sobre-o-autor.md` | 10 | `*Inteligência Aumentada — Os Princípios Permanentes da IA*` | Subtítulo comercial do livro | MANTIDO |

**Total de ocorrências corrigidas em paratexto/manifesto: 9**
**Total mantidos (subtítulo comercial do livro, não o manifesto): 6**

### Edições aplicadas (antes → depois)

**L1-04-sumario.md:**
- `## OS NOVE PRINCÍPIOS PERMANENTES` → `## OS NOVE INVARIANTES`
- `Manifesto — Os Nove Princípios Permanentes da Inteligência Artificial` → `Manifesto — Os Nove Invariantes da Inteligência Artificial`

**L1-05-mapa-de-leitura-por-nivel.md:**
- `Manifesto C00M — Os Nove Princípios Permanentes` → `Manifesto C00M — Os Nove Invariantes da Inteligência Artificial`

**L1-00c2-promessa.md:**
- `Os **Nove Princípios Permanentes** que sustentam toda a obra` → `Os **Nove Invariantes** que sustentam toda a obra`
- `**Nove Princípios Permanentes** memorizáveis` → `**Nove Invariantes** memorizáveis`

**L1-11-orelhas.md:**
- `Nove Princípios Permanentes formam a espinha intelectual da obra` → `Nove Invariantes formam a espinha intelectual da obra`

**L1-03-introducao.md:**
- `os **Nove Princípios Permanentes da Inteligência Artificial**` → `os **Nove Invariantes da Inteligência Artificial**`

**L1-01-prefacio.md:**
- `A obra estrutura essa tese em torno de **Nove Princípios Permanentes da Inteligência Artificial**.` → `A obra estrutura essa tese em torno dos **Nove Invariantes da Inteligência Artificial**.`

**L1-12-quarta-capa.md:**
- `os Nove Princípios Permanentes, costurados em rede mútua` → `os Nove Invariantes, costurados em rede mútua`

### Aviso de varredura pendente (body, frameworks, apêndices)
Os diretórios `02-capitulos/`, `03-frameworks/` e `04-apendices/` **não foram editados** nesta rodada. Ocorrências detectadas no grep para referência do autor:

| Arquivo | Linha | Texto | Tipo |
|---------|-------|-------|------|
| `04-apendices/L1-APX-H-bibliografia.md` | 132 | `**Inteligência Aumentada — Os Nove Princípios Permanentes**` | Título bibliográfico — decidir se atualiza para "Os Nove Invariantes" |
| `04-apendices/L1-APX-M-manifesto-bolso.md` | 85 | `Os Nove Princípios Permanentes da Inteligência Artificial` | Nome do manifesto — candidato a correção na varredura do autor |

Verificar também `02-capitulos/` e `03-frameworks/` com grep `"Princípios Permanentes"` — não executado aqui por instrução.

---

## D3 — CONTAGEM DE CAPÍTULOS: "29 capítulos" → "capítulos"

### Problema
`L1-00e-sobre-os-casos.md`, primeira linha do corpo: "ao longo dos 29 capítulos" — contagem frágil (estrutura atual é C01–C28 + C14B + C14C, e pode mudar).

### Ação executada
**Arquivo:** `00-paratexto/L1-00e-sobre-os-casos.md`
**Antes:** `ao longo dos 29 capítulos, mais de trinta exemplos memoráveis`
**Depois:** `ao longo dos capítulos, mais de trinta exemplos memoráveis`

Nenhum outro paratexto continha a contagem numérica de capítulos.

---

## D4 — NOTAS INTERNAS VISÍVEIS NA QUARTA CAPA

### Problema
`L1-12-quarta-capa.md` continha três notas `[PENDENTE — ... — NÃO ENVIAR AO GRÁFICO]` renderizáveis em Markdown (texto literal entre colchetes), que vazariam ao gráfico.

### Ação executada
**Arquivo:** `00-paratexto/L1-12-quarta-capa.md`

Cada nota convertida para comentário HTML `<!-- ... -->` (mesmo padrão já adotado na capa):

| Campo | Antes | Depois |
|-------|-------|--------|
| Páginas | `[PENDENTE — aguardando diagramação final — NÃO ENVIAR AO GRÁFICO]` | `<!-- PENDENTE — aguardando diagramação final — NÃO ENVIAR AO GRÁFICO -->` |
| ISBN | `[PENDENTE — em processo de atribuição — NÃO ENVIAR AO GRÁFICO]` | `<!-- PENDENTE — em processo de atribuição — NÃO ENVIAR AO GRÁFICO -->` |
| Preço sugerido | `[PENDENTE — a ser definido pela editora — NÃO ENVIAR AO GRÁFICO]` | `<!-- PENDENTE — a ser definido pela editora — NÃO ENVIAR AO GRÁFICO -->` |

Conteúdo das notas preservado integralmente; apenas forma alterada para ocultação.

---

## D5 — ORDEM NARRATIVA DOS PRINCÍPIOS NO PREFÁCIO

### Problema
`L1-01-prefacio.md` cita os nove princípios em ordem narrativa (Camada Dupla primeiro, sendo o Princípio 3 canônico), que diverge da numeração do manifesto. Reordenar seria cirúrgico e arriscado.

### Decisão
Inserir frase parentética deixando explícito que a ordem é narrativa, não numérica.

### Ação executada
**Arquivo:** `00-paratexto/L1-01-prefacio.md`

**Antes:**
> Os nove princípios — Camada Dupla, Plausibilidade, Custo Composto, Extremidades, Encaixe, Termômetro, Autonomia Proporcional, Responsabilidade Indelegável, Operador — formam o vocabulário que costura toda a obra.

**Depois:**
> Os nove princípios — Camada Dupla, Plausibilidade, Custo Composto, Extremidades, Encaixe, Termômetro, Autonomia Proporcional, Responsabilidade Indelegável, Operador — formam o vocabulário que costura toda a obra (a ordem aqui é a da história, não a da numeração; os nove estão numerados no manifesto).

---

## D9 — PADRONIZAR "Curiosidade ativa" → "Curiosidade"

### Escopo desta rodada
Paratexto e manifesto apenas. C14B e C14C **não editados** (colisão com outro agente).

### Ocorrências encontradas em 00-paratexto/ e 01-manifesto/

| Arquivo | Linha | Texto | Ação |
|---------|-------|-------|------|
| `01-manifesto/L1-C00P-porque-padrao-dura.md` | 172 | `**Curiosidade ativa** — Está com vontade de entrar...` | CORRIGIDO |

**Ação executada:**
**Antes:** `| 5 | **Curiosidade ativa** — Está com vontade de entrar no Capítulo 1...`
**Depois:** `| 5 | **Curiosidade** — Está com vontade de entrar no Capítulo 1...`

### Pendência delegada (registrada para verificação final)

| Arquivo | Localização | Troca pendente |
|---------|-------------|----------------|
| `02-capitulos/L1-C14B-reasoning-models.md` | Item 5 da autoavaliação | `**Curiosidade ativa**` → `**Curiosidade**` |
| `02-capitulos/L1-C14C-spec-driven-development.md` | Item 5 da autoavaliação | `**Curiosidade ativa**` → `**Curiosidade**` |

Esses dois arquivos estão com edição em andamento por outro agente. Confirmar na verificação final que a troca foi aplicada.

---

## RESUMO EXECUTIVO DAS EDIÇÕES

| ID | Arquivo(s) | Tipo de mudança | Ocorrências | Status |
|----|------------|-----------------|-------------|--------|
| D2 | L1-04-sumario.md, L1-05-mapa-de-leitura-por-nivel.md, L1-00c2-promessa.md, L1-11-orelhas.md, L1-03-introducao.md, L1-01-prefacio.md, L1-12-quarta-capa.md | "Nove Princípios Permanentes" → "Nove Invariantes [da IA]" | 9 corrigidas, 6 mantidas (subtítulo comercial) | FEITO |
| D3 | L1-00e-sobre-os-casos.md | "29 capítulos" → "capítulos" | 1 | FEITO |
| D4 | L1-12-quarta-capa.md | `[PENDENTE...]` → `<!-- PENDENTE... -->` | 3 notas | FEITO |
| D5 | L1-01-prefacio.md | Inserção de parentético sobre ordem narrativa | 1 | FEITO |
| D9 | L1-C00P-porque-padrao-dura.md | "Curiosidade ativa" → "Curiosidade" | 1 em manifesto | FEITO |
| D9 | L1-C14B, L1-C14C | "Curiosidade ativa" → "Curiosidade" | 2 pendentes | DELEGADO — verificar pós-colisão |
