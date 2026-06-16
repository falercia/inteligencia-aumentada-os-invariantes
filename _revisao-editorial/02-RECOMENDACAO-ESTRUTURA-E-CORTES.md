# RECOMENDAÇÃO DE ESTRUTURA, DIVISÃO E CORTES
## Inteligência Aumentada — Livro 1: Os Invariantes

> Documento estratégico, não operacional. Aqui não há correção de texto — há a decisão de **o que pertence a este livro e o que não pertence**. Leitura à luz da sua diretriz: *este livro é sobre método, neutro quanto a fornecedor; profundidade de produto (Claude) vive em outro livro da série.*

---

## 1. O DIAGNÓSTICO EM UMA FRASE

O livro hoje mistura **duas camadas com meias-vidas opostas**, e é essa mistura — não a qualidade — que cria o risco de durabilidade e a fricção com a tese.

| Camada | Meia-vida | Natureza | Exemplos no livro |
|---|---|---|---|
| **Invariante (método)** | 5–10 anos | princípios, frameworks, julgamento, governança | manifesto, F1–F9, fundamentos conceituais, evals, LLMOps, alignment, governança, trade-offs, interpretabilidade |
| **Perecível (campo)** | 6–18 meses | preços, rankings de modelos, repos, ferramentas, prompts | C15, C16, C17, C18, C20, APX-D, APX-E, APX-F, APX-L |

Um livro chamado **"Os Invariantes"** com uma camada perecível embutida é uma **contradição de posicionamento**. Toda página perecível é uma data de validade impressa dentro de um livro que promete durar uma década.

**Princípio de design:** o que muda a cada release de modelo não deve estar em papel. Deve estar no **repositório versionado** ou no **livro de produto (Claude)**. O papel guarda o que sobrevive à próxima geração de modelos.

---

## 2. CLASSIFICAÇÃO DE CADA BLOCO — MANTER / MOVER / CORTAR

Critério: *isso sobrevive à próxima geração de modelos?* Se não, sai do livro-método.

### ✅ NÚCLEO INVARIANTE — fica (é o livro)
Manifesto (C00M, C00P) · Frameworks F1–F9 · C01–C05 (fundamentos conceituais) · C06 RAG · C07 Memória · C08 Fine-tuning (conceito) · C10 Chain-of-Thought · C11 Context Engineering · C12 Agentes · C14 AI Engineering · C14B Reasoning · C14C Spec-Driven · C19 Segurança · C21 Evals · C22 LLMOps · C23 Alignment · C24 Governança · C25 Trade-offs · C27 PME Brasileira (PI local — joia do livro) · C28 Interpretabilidade · APX-A, APX-B, APX-J, APX-M, APX-N, APX-O, APX-Q.

### 🔁 PERECÍVEL → mover para o REPOSITÓRIO VERSIONADO
Conteúdo que é útil mas envelhece e já tem casa natural fora do papel:
- **C15 — Comparação de modelos** → manter no livro só o *método de avaliar um modelo* (a árvore de decisão); a tabela de quem-lidera-o-quê vai para o repo.
- **C16 — Open Source** → manter o *critério de decisão build/buy/host*; preços e quadros vão para o repo.
- **C17 — GitHub Repos** → manter os *critérios de confiabilidade de um repo*; a lista de repos vai para o repo.
- **C18 — Economia de tokens** → manter os *mecanismos* (por que custa, como decompor); números/preços vão para o repo.
- **APX-D Ferramentas · APX-E Leituras · APX-F Newsletters · APX-G Papers · APX-H Bibliografia** → todos são listas datadas. Manter no livro apenas os **critérios de curadoria**; as listas vivem no repo, com data de revisão.

### 📦 VENDOR-DEEP / PROMPTS → mover para o LIVRO DE PRODUTO (Claude)
- **APX-L — Biblioteca de prompts (13 mil palavras)**: é o maior corpo estranho ao "Os Invariantes". A moldura de método que inserimos na Onda 1 é um curativo correto, mas a casa natural deste conteúdo é o **livro de Claude**. No Livro 1, fica apenas a *moldura* (o método de engenharia de prompt como princípio) — os 30 prompts migram.
- Qualquer aprofundamento específico de Claude/MCP/produto que sobrar nos capítulos → citação no Livro 1, desenvolvimento no livro de produto.

### ✂️ AVALIAR CORTE / FUSÃO
- **C20 — Futuro**: capítulo de maior risco (previsões datam). Não cortar, mas **encolher** para princípios de antecipação (como pensar sobre o futuro) em vez de cenários numéricos. Já suavizamos os números na Onda 1.
- **APX-E ↔ APX-F**: duplicação (leituras/newsletters). **Fundir** em um único "como montar sua dieta de informação" baseado em critério.
- **APX-G ↔ APX-H**: papers e bibliografia se sobrepõem. Avaliar fusão.

---

## 3. DUAS OPÇÕES DE ESTRUTURA

### OPÇÃO A — Quarentena (1 livro, baixo risco) · recomendada para a 1ª edição
Mantém um livro só, mas **isola a camada perecível** numa parte final claramente rotulada ("Parte VI — Mapa do Campo, válido na data X, sempre atualizado no repositório") e move o grosso do perecível para o repo. Esforço menor, preserva o projeto atual, resolve 80% da fricção de durabilidade.

**Vantagens:** rápido; não quebra a numeração; entrega já na próxima rodada.
**Risco:** o livro continua grande (~200k+ palavras) e ainda carrega alguma camada perecível.

### OPÇÃO B — Separação em série (2 livros, alto teto) · jogo estratégico
- **Livro 1 — Os Invariantes**: 100% método, vendor-neutral, ~150–170k palavras. Durabilidade de 5–10 anos. É a obra de referência.
- **Livro de Produto (Claude / "Mãos à Obra")**: prompts, ferramentas, comparações, repos, o perecível e o vendor-deep. Edição viva, atualizável, casada com o repositório.

**Vantagens:** posicionamento limpo ("Os Invariantes" cumpre o nome); cada livro tem cadência própria (um dura, o outro se atualiza); cria série e LTV; resolve 100% da fricção com a tese.
**Risco:** mais trabalho editorial; exige decidir o sumário do Livro 2; o Livro 1 fica mais enxuto (o que é uma virtude, mas muda a percepção de "valor por volume").

---

## 4. RECOMENDAÇÃO

**Vá de Opção B no plano, executando por Opção A na prática.** Ou seja: decida agora que a obra é uma **série de dois livros** (porque você já tem o livro de Claude no horizonte — *"lá que deve estar isso"*), e use a quarentena (mover perecível para o repo + marcar a fronteira) como o **passo de transição** que já deixa o Livro 1 limpo sem travar o cronograma. O conteúdo movido para o repo é exatamente o material-semente do Livro 2.

Isso transforma o maior risco do livro (durabilidade desigual) na sua maior alavanca de negócio (uma série com um volume durável e um volume vivo).

---

## 5. TRADE-OFFS E PONTOS CEGOS

| Decisão | Ganho | Custo / risco | Mitigação |
|---|---|---|---|
| Tirar prompts (APX-L) do Livro 1 | coerência com a tese; –13k palavras perecíveis | leitor pode sentir falta do "prático" | manter a *moldura de método* + remeter ao repo/Livro 2 |
| Mover listas para o repo | livro nunca "vence o prazo" | repo precisa existir e ser mantido (hoje é P0 em aberto) | criar e popular o repo **antes** da publicação (ver changelog) |
| Encolher C20 (Futuro) | menos risco de errar previsão | perde apelo de "visão" | trocar previsões por *método de antecipar* |
| Série de 2 livros | posicionamento e LTV | mais esforço editorial | usar o material movido como semente do Livro 2 |

**Ponto cego principal:** o **repositório acompanhante** é hoje o ponto único de falha. Toda a estratégia de durabilidade depende dele existir, estar populado e ser mantido. Enquanto for promessa, é risco. Priorizá-lo é pré-requisito, não acessório.

---

## 6. PRÓXIMOS PASSOS

1. **Decisão sua (1–2 dias):** Opção A, B, ou o híbrido recomendado. É a única decisão que destrava o resto.
2. **Resolver os 5 P0 deferidos** (estão no changelog e na planilha): epígrafe Dijkstra (C01), ordenação 14B/14C, diagramas SVG de C24, repositório acompanhante, e o entregável da persona Desenvolvedor (C26).
3. **Criar e popular o repositório** com a primeira leva de conteúdo perecível movido.
4. **Onda 2** (durabilidade): converter C15–C18 e APX-D–H de catálogo em critério, conforme a classificação acima.
5. **Onda 3** (clareza/Joana) e **Onda 4** (acabamento), já no plano consolidado.

> Se você confirmar a direção, eu executo a Onda 2 no mesmo modelo da Onda 1 (subagentes cirúrgicos + changelog + verificação) e já preparo o **sumário-semente do Livro 2** com o material movido.
