# Changelog — Migração Terminológica: Manifesto (Onda 5)

**Data:** 2026-06-16  
**Arquivos editados:** `01-manifesto/L1-C00M-manifesto-invariantes.md`, `01-manifesto/L1-C00P-porque-padrao-dura.md`  
**Escopo:** Renomeação do sistema dos nove de "Princípios" → "Invariantes" em toda a pasta `01-manifesto/`.

---

## Totais

| Arquivo | Trocas aplicadas | Ocorrências preservadas (genérico) |
|---------|------------------|------------------------------------|
| C00M | 25 linhas alteradas / ~32 instâncias trocadas | 1 (linha 13: "Quem aprendia os princípios escapava") |
| C00P | 11 linhas alteradas / ~14 instâncias trocadas | 3 (linha 23: "princípio, padrão arquitetural"; linha 93: "A escolha por princípio em vez de por moda"; linha 95: "os princípios derivados dessa literatura") |
| **Total** | **~46 instâncias trocadas** | **4 preservadas** |

---

## Cabeçalhos markdown renomeados

### C00M — `L1-C00M-manifesto-invariantes.md`

| Antes | Depois |
|-------|--------|
| `### Princípio 1 — Plausibilidade` | `### Invariante 1 — Plausibilidade` |
| `### Princípio 2 — Extremidades` | `### Invariante 2 — Extremidades` |
| `### Princípio 3 — Camada Dupla` | `### Invariante 3 — Camada Dupla` |
| `### Princípio 4 — Encaixe` | `### Invariante 4 — Encaixe` |
| `### Princípio 5 — Custo Composto` | `### Invariante 5 — Custo Composto` |
| `### Princípio 6 — Autonomia Proporcional` | `### Invariante 6 — Autonomia Proporcional` |
| `### Princípio 7 — Termômetro` | `### Invariante 7 — Termômetro` |
| `### Princípio 8 — Responsabilidade Indelegável` | `### Invariante 8 — Responsabilidade Indelegável` |
| `### Princípio 9 — Operador` | `### Invariante 9 — Operador` |
| `## QUANDO USAR E QUANDO EVITAR OS PRINCÍPIOS` | `## QUANDO USAR E QUANDO EVITAR OS INVARIANTES` |

### C00P — `L1-C00P-porque-padrao-dura.md`

| Antes | Depois |
|-------|--------|
| `## P.8.5 — NOTA EDITORIAL AO LEITOR ANTES DOS PRINCÍPIOS` | `## P.8.5 — NOTA EDITORIAL AO LEITOR ANTES DOS INVARIANTES` |

---

## Detalhamento das trocas — C00M

- Epígrafe: "Os princípios que decidem se ele funciona" → "Os invariantes que decidem se ele funciona"
- Corpo (§ Questão de Fundo): "ela identifica os princípios que decidem" → "ela identifica os invariantes que decidem"; "Esses princípios estão nomeados" → "Esses invariantes estão nomeados"
- "Cada princípio atende a quatro critérios" → "Cada invariante atende a quatro critérios"
- 9 cabeçalhos `### Princípio N — X` → `### Invariante N — X`
- "é o caso canônico do princípio" → "é o caso canônico do invariante"
- Banco Solar (4 instâncias): "o princípio do encaixe/termômetro/custo composto/responsabilidade indelegável" → "o invariante do ..."
- "Sem princípios, toda migração... Com princípios, a primeira escolha" → "Sem invariantes... Com invariantes..."
- Seção e corpo "QUANDO USAR E QUANDO EVITAR OS PRINCÍPIOS" → "OS INVARIANTES"; "Os princípios funcionam..." → "Os invariantes funcionam..."
- "Os princípios são filtro de decisão... o princípio do termômetro... o princípio combate... cada princípio é amarrado" → variante com invariante
- Tabela vantagens/limitações: "Princípios 1 e 2 dependem" → "Invariantes 1 e 2 dependem"; "pelo princípio violado" → "pelo invariante violado"
- Exercícios: "qual princípio foi respeitado... Reduza cada princípio... Princípio 1 / Princípio 7... o princípio não muda... citando o princípio violado" → invariante
- Referências: "Princípio 9" → "Invariante 9"

## Detalhamento das trocas — C00P

- "terceiro dos Nove Princípios" → "terceiro dos Nove Invariantes"
- "princípio quatro dos Nove" → "invariante quatro dos Nove"
- "princípio nove dos Nove" → "invariante nove dos Nove"
- Seção P.8.5 (cabeçalho): "ANTES DOS PRINCÍPIOS" → "ANTES DOS INVARIANTES"
- "Os Nove Princípios que vêm a seguir" → "Os Nove Invariantes que vêm a seguir"
- "Os Princípios, em contraste" → "Os Invariantes, em contraste"
- "quem segue para os princípios sai armado de prática" → "quem segue para os invariantes..."
- "cada princípio adiante carrega" → "cada invariante adiante carrega"
- "voltar aos princípios sempre que" → "voltar aos invariantes sempre que"
- "deixar os princípios na estante" → "deixar os invariantes na estante"
- "dos Nove Princípios em forma de capítulos" → "dos Nove Invariantes..."
- Link texto: "**Manifesto dos Nove Princípios**" → "**Manifesto dos Nove Invariantes**" (caminho do arquivo preservado)
- Links: "**Princípio 3 — Camada Dupla**" e "**Princípio 4 — Encaixe**" → "**Invariante 3 — ...**" e "**Invariante 4 — ...**"
- Autoavaliação: "ao princípio 3" → "ao invariante 3"

---

## Preservados como genérico

1. **C00M, linha 13**: "Quem aprendia os princípios escapava da obsolescência" — contexto: livros canônicos de engenharia ensinam princípios gerais; não se refere ao sistema dos nove.
2. **C00P, linha 23**: "o operador separa o que dura — **princípio**, padrão arquitetural, mecânica de trade-off..." — listagem de tipos de conteúdo duráveis; "princípio" como categoria genérica de conhecimento, não um dos nove.
3. **C00P, linha 93**: "A escolha por **princípio** em vez de por moda" — expressão idiomática genérica ("agir por princípio").
4. **C00P, linha 95**: "os **princípios** derivados dessa literatura científica" — refere-se a princípios da física, matemática, sistemas distribuídos; não ao sistema dos nove.

---

## Verificações realizadas

- Nenhuma ocorrência de "Invariantes Permanentes" criada.
- Nenhum caminho de arquivo ou link de arquivo alterado (apenas textos de link).
- Concordância gramatical verificada: "o invariante", "os invariantes", "do invariante", "dos invariantes", "cada invariante" — todos masculinos, sem quebra de concordância.
- grep final pós-edição confirma zero ocorrências indevidas de "Princípio N" ou "princípio do [nome do invariante]" remanescentes.
