# MAPA DE MIGRAÇÃO — Os Invariantes como horizonte longo
## Cruzamento do manuscrito com os dois repositórios da série

> Objetivo: deixar o **Os Invariantes** 100% método e durável (5–10 anos). Todo conteúdo perecível ou específico de produto sai do papel e vai para a casa que **já existe** na sua série.

---

## 1. A SÉRIE QUE VOCÊ JÁ TEM (4 ativos)

| Ativo | Papel | Meia-vida | Estado |
|---|---|---|---|
| **Livro: Os Invariantes** | método vendor-neutral | 5–10 anos | em revisão (Onda 1 feita) |
| **Repo: inteligencia-aumentada-recursos** | executável do método (prompts, evals, agents, MCP edu, notebooks, governança) | viva | populado e maduro |
| **Livro: Deep Claude** | vertical Claude/Anthropic, mãos à obra | 1–3 anos | existe |
| **Repo: deep-claude** | número que muda + Claude-específico (apêndice vivo de modelos/preços/benchmarks, skills, MCPs, labs) | viva (cadência mensal) | populado, com `apendice-vivo` |

**Conclusão estrutural:** a arquitetura de Camada Dupla que a banca recomendaria já está construída. Não há o que inventar — há o que **realocar**.

---

## 2. ACHADO CONTRA-INTUITIVO: pouco vai para o livro de Claude

O Os Invariantes já é vendor-neutral por design. Portanto a migração **não é** "Os Invariantes → Deep Claude". É majoritariamente **"Os Invariantes → seu próprio companion (recursos)"**, tirando o perecível do papel. O que de fato é Claude-específico no manuscrito é pouco (o capítulo de MCP já foi reancorado como genérico na Onda 1).

---

## 3. MAPA BLOCO A BLOCO

Legenda destino: **R** = repo recursos · **DC** = repo/livro Deep Claude · **LIVRO** = permanece (como método) · **CUT** = remover.

| Bloco no Os Invariantes | O que é | Perecível? | Destino | Já existe lá? | Ação |
|---|---|---|---|---|---|
| **APX-L — 30 prompts (13k palavras)** | fichas de prompt | sim | **R** `/prompts` | ✅ **sim, 33 prompts** | Livro mantém só a *moldura de método*; remover as 30 fichas e apontar para R |
| **C15 — tabelas de comparação/benchmarks** | quem-lidera-o-quê | sim (40 âncoras) | **apêndice vivo** | ❌ falta em R | Livro mantém a *árvore de decisão de avaliação*; números → camada viva (ver §4) |
| **C16 — Quadro 16.A preços / open source** | preços de API | sim | **apêndice vivo** | DC tem `PRECOS.md` | Livro mantém critério *build/buy/host*; preços → camada viva |
| **C17 — lista de repos GitHub** | catálogo de repos | sim (11) | **R** (lista curada) | ❌ criar | Livro mantém *critérios de confiabilidade de repo*; lista → R |
| **C18 — preços de token** | tabela de custos | sim | **apêndice vivo** | DC tem `PRECOS.md` | Livro mantém *mecanismos de custo*; preços → camada viva |
| **C20 — cenários numéricos** | projeções | sim | — | já suavizado Onda 1 | Manter como *método de antecipar*; nada a mover |
| **APX-D — ferramentas** | catálogo (64 itens) | sim | **R** | ❌ criar `/ferramentas` | Livro mantém *critério de seleção*; lista → R |
| **APX-E — leituras** | lista | sim | **R** | parcial | fundir com F; lista → R |
| **APX-F — newsletters** | lista | sim | **R** | ❌ | lista → R; livro mantém "como montar dieta de informação" |
| **APX-G — papers** | bibliografia técnica | baixa | **LIVRO** | — | manter (papers seminais envelhecem devagar) |
| **APX-H — bibliografia** | referências | baixa | **LIVRO** | — | manter |
| **MCP / específico de Claude** | tutoriais de produto | sim | **DC** | ✅ `mcps/`, `skills/` | nada a mover — já está em DC; livro só cita |

---

## 4. A ÚNICA DECISÃO DE ARQUITETURA EM ABERTO

Os números cross-vendor (modelos, preços, benchmarks) que hoje estão dentro de C15/C16/C18 precisam de uma **camada viva única**. Hoje só o `deep-claude/apendice-vivo` existe (cross-vendor, cadência mensal). Três caminhos:

| Opção | Como fica | Vantagem | Custo |
|---|---|---|---|
| **A — Fonte única compartilhada** (recomendada) | Os Invariantes aponta para o `apendice-vivo` do deep-claude como camada de números da série inteira | manutenção em **1 lugar/mês**; escalável | cria dependência do companion neutro no repo da vertical Claude |
| **B — recursos ganha seu próprio apêndice vivo** | duplicar a estrutura de números em recursos, cross-vendor | independência e neutralidade de marca total | manter números em **2 repos/mês** (armadilha de manutenção) |
| **C — Livro sem tabela viva** | livro só ensina a *ler* uma comparação/preço; números por conta do leitor | zero manutenção | perde o ativo "referência viva"; leitor sente falta |

Recomendo **A**: uma fonte única é o que sustenta a cadência mensal sem você manter dois apêndices. A neutralidade do livro se preserva no texto (ensina método); a camada de números é infraestrutura compartilhada da série.

---

## 5. O QUE EU EXECUTO ASSIM QUE VOCÊ DECIDIR

**Onda 2 (durabilidade), no mesmo modelo da Onda 1 (cirúrgico + backup + changelog + verificação):**
1. Enxugar C15, C16, C17, C18 → método + ponteiro para a camada viva escolhida.
2. APX-L: remover as 30 fichas do livro, manter a moldura, apontar para `recursos/prompts`.
3. APX-D/E/F → critério no livro + listas para recursos; fundir E+F.
4. Criar em **recursos** o que falta (`/ferramentas`, lista curada de repos) e, se Opção B, o `apendice-vivo`.
5. Atualizar os ponteiros nos 8 capítulos que já citam o repo, para consistência.

**Não vou escrever nos repos deep-claude/recursos sem seu aval** — são obras separadas. Preciso de duas confirmações abaixo.
