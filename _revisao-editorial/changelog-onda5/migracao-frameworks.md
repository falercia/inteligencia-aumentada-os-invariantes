# Changelog — Migração Terminológica: Princípios → Invariantes
## Escopo: `03-frameworks/` (9 arquivos)
## Data: 2026-06-16
## Agente responsável: subagente de migração terminológica

---

## TROCADOS (9 ocorrências)

### L1-F1-decid-ia.md

| Linha | Antes | Depois |
|-------|-------|--------|
| 30 | `Sem golden set planejado, a iniciativa pode passar para piloto interno mas não para produção. Princípio 7 manda.` | `... Invariante 7 manda.` |
| 35 | `Sem nome, não passa. Princípio 8 manda.` | `... Invariante 8 manda.` |

### L1-F2-encaixe-5.md

| Linha | Antes | Depois |
|-------|-------|--------|
| 85 | `Viola o Princípio 5 (Custo Composto); em meses, a fatura mostra o erro` | `Viola o Invariante 5 (Custo Composto); ...` |

### L1-F3-agente-prop.md

| Linha | Antes | Depois |
|-------|-------|--------|
| 43 | `Aprovação nominal do dono operacional (Princípio 8)` | `... (Invariante 8)` |
| 96 | `Governança Indelegável (Princípio 8 sustenta o "dono" de cada nível)` | `... (Invariante 8 sustenta o "dono" de cada nível)` |

### L1-F4-prompt-ext.md

| Linha | Antes | Depois |
|-------|-------|--------|
| 6 | `respeitam a física de atenção (Princípio 2) e que separam...do que é número volátil (Princípio 3)` | `... (Invariante 2) ... (Invariante 3)` |
| 114 | `Princípio 2: atenção decai no meio; regra ignorada silenciosamente` | `Invariante 2: atenção decai no meio; ...` |

### L1-F6-gov-indelegavel.md

| Linha | Antes | Depois |
|-------|-------|--------|
| 110 | `Sem nome, ninguém responde. Princípio 8 viola por omissão` | `... Invariante 8 viola por omissão` |

### L1-F7-composto-3t.md

| Linha | Antes | Depois |
|-------|-------|--------|
| 37 | `Exige golden set para mostrar que tier pequeno entrega qualidade equivalente (Princípio 7 sustenta a decisão).` | `... (Invariante 7 sustenta a decisão).` |
| 90 | `Eval que sustenta cada mudança \| Princípio 7 — sem eval, não muda` | `... \| Invariante 7 — sem eval, não muda` |

---

## PRESERVADOS (1 ocorrência)

| Arquivo | Linha | Texto | Motivo |
|---------|-------|-------|--------|
| L1-F6-gov-indelegavel.md | 68 | `AUP + princípios + categorias de safety` | Uso genérico — lista de componentes de política; não refere o sistema dos nove |

---

## ARQUIVOS SEM OCORRÊNCIAS

- L1-F5-cobertura-integracoes.md — zero ocorrências
- L1-F8-eval-piramide.md — zero ocorrências
- L1-F9-rota-dupla.md — zero ocorrências

---

## RESUMO

- Trocados: **9 ocorrências** em 5 arquivos (F1, F2, F3, F4, F6, F7)
- Preservados: **1 ocorrência** em 1 arquivo (F6 l.68 — uso genérico)
- Arquivos não alterados: F5, F8, F9 (sem ocorrências relevantes)
- Arquivos renomeados: nenhum
- Concordância: todos os termos são masculinos — artigos/concordância inalterados em todos os casos
