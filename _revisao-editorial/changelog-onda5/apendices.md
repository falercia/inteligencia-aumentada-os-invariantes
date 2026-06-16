# Changelog Onda 5 — Apêndices (APX-A a APX-Q)

> Onda 5 — GALÉ · Leitura linear dos 17 apêndices
> Executor: Claude (Sonnet 4.6) · Data: 2026-06-16
> Escopo: APX-A através APX-Q (L1-APX-A-glossario.md a L1-APX-Q-manual-do-professor.md)
> Metodologia: leitura 100% de todos os 17 arquivos; lente de consistência de conjunto

---

## EDITADOS (aplicados diretamente)

### APX-H · L1-APX-H-bibliografia.md

**H-001 · Referência obsoleta a "Newsletters" no cabeçalho**
- Linha 4: `"Para curadoria comentada, ver os apêndices de Leituras, Newsletters e Papers."` → `"Para curadoria comentada, ver os apêndices de Leituras (APX-E) e Papers (APX-G)."`
- Motivo: APX-F (Newsletters) foi incorporado ao APX-E na Onda 2. O cabeçalho mantinha referência ao apêndice extinto. Lector que seguisse a referência "Newsletters" não encontraria o destino.
- Risco: baixo (ajuste de ponteiro).

---

### APX-I · L1-APX-I-indice-remissivo.md

**I-001 · Título obsoleto de APX-E na entrada "Prompt"**
- Linha 97: `"Apêndice E (leituras de fundamentação)"` → `"Apêndice E (Como montar sua dieta de informação)"`
- Motivo: APX-E foi renomeado na Onda 2; o título "leituras de fundamentação" não existe mais no documento.
- Risco: baixo.

**I-002 · Nomenclatura inconsistente do APX-M em 3 entradas**
- Ocorrências (linhas 19, 75, 94): `"Manifesto dos Princípios"` → `"Manifesto de Bolso (APX-M)"` (3 substituições via replace_all)
- Motivo: o APX-M se intitula "Manifesto de Bolso: Os Nove Princípios em Uma Página". O índice usava "Manifesto dos Princípios" — termo que o leitor não encontra como título em nenhum apêndice.
- Risco: baixo.

---

### APX-J · L1-APX-J-trilha-do-numero.md

**J-001 · Typo sintático na política editorial**
- Linha 170: `"um calendário que prometido demais"` → `"um calendário que promete demais"`
- Motivo: "que prometido" é erro sintático (faltava o verbo conjugado).
- Risco: nulo.

---

### APX-G · L1-APX-G-papers.md

**G-001 · Duplo separador `---` residual**
- Linhas 101-103: `---\n\n---` → `---` (removido separador duplicado entre seção VIII e "Como ler papers de IA")
- Motivo: duplicação de separador sem propósito; provável artefato de edição anterior.
- Risco: nulo.

---

### APX-L · L1-APX-L-biblioteca-prompts.md

**L-001 · Contagem errada de padrões de operação na moldura**
- Linha 11: `"os sete padrões de operação"` → `"os oito padrões de operação"`
- Linha 13: `"com os sete padrões internalizados"` → `"com os oito padrões internalizados"`
- Motivo: a seção "Padrões de operação" contém 8 itens numerados (1-8). A moldura afirmava "sete", criando contradição interna verificável por qualquer leitor que contasse a lista. O item 8 (monitoramento de recusas) foi provavelmente adicionado depois sem atualizar a moldura.
- Risco: baixo (contagem factual).

---

### APX-P · L1-APX-P-boxes-tecnicos.md

**P-001 · URL do paper Hayes et al. inconsistente com APX-J**
- Box 1, "Onde aprofundar": `"arxiv.org/abs/2410.10074"` → `"arxiv.org/abs/2410.22884"`
- Motivo: o mesmo paper (Hayes et al., "Stealing User Prompts from Mixture of Experts") é citado em APX-J com URL `2410.22884` e em APX-P com `2410.10074`. São dois números arXiv distintos — o APX-J (Trilha do Número, apêndice canônico de referências datadas) é a fonte preferencial da obra. Alinhado APX-P à URL de APX-J.
- Risco: médio — uma das URLs pode estar errada factualmente. PENDENTE verificação manual do autor contra arxiv.org para confirmar qual número está correto antes da impressão.

---

### APX-Q · L1-APX-Q-manual-do-professor.md

**Q-001 · Gabarito da aula 4 apontando para capítulo errado**
- Linha da aula 4 na tabela de exercícios: status `"Disponível — APX-K (C06)"` e pista `"*(Gabarito estruturado completo: APX-K, seção RAG — Capítulo 06; gabarito expandido em /teaching/exercises/aula-04.md no repositório.)*"` → status corrigido para `"Em construção — repositório /teaching/exercises/aula-04.md"` (texto simplificado, referência ao C06 removida)
- Motivo: o exercício da aula 4 reproduz o experimento Lost in the Middle — tema do C04 (Janela de contexto). APX-K não cobre C04; cobre RAG (C06). O status "Disponível — APX-K (C06)" era factualmente errado: o gabarito de Lost in the Middle não existe em APX-K. Verificado: APX-K não contém nenhuma seção de C04.
- Risco: médio — poderia mandar professor adotante procurar gabarito que não existe.

---

## PENDENTE-AUTOR

### APX-N · "F3" como "matriz quatro por quatro"

- APX-N, Tipo C, linha 44: `"matriz quatro por quatro no F3"` — F3 = Escala de Propriedade do Agente (P6).
- Dúvida: a Escala de Propriedade do Agente tem dimensão 4×4? Não é possível confirmar sem acesso ao corpo do capítulo correspondente (capítulo de Agentes). Se a escala tiver cinco níveis (0-4) e uma única dimensão, não é matriz 4×4.
- Ação: autor deve verificar a estrutura exata do F3 no capítulo e corrigir se necessário.

### APX-O · Uso de "Tipo C da taxonomia do APX-N" para descrever padrão conceitual

- APX-O, linha 21: `"materializa, na prática do caderno, o Tipo C da taxonomia do APX-N — padrão durável que vive no livro"`
- Problema: Tipo C em APX-N = números auto-evidentes (ex.: "cinco blocos no F4"). O caderno conceitual não é um "número" — é um framework. A nota equipara padrão conceitual com Tipo C, o que é impreciso e pode confundir leitor técnico que leu APX-N.
- Sugestão: reformular para "esta estrutura de camadas materializa o Princípio Três (Camada Dupla) na prática do caderno", removendo a remissão ao Tipo C que não se encaixa semanticamente.
- Ação: decisão do autor (envolve voz e conceito).

### APX-P · Verificação da URL Hayes et al.

- Como documentado em P-001 acima, uma das duas URLs (APX-J vs APX-P) pode estar errada. Recomenda-se acesso direto ao arxiv.org antes da impressão para confirmar qual número (`2410.22884` ou `2410.10074`) corresponde ao paper correto.
- Se a URL de APX-J estiver errada, corrigir lá também.

### APX-L · Item 8 dos padrões como candidato a fusão ou reposicionamento

- O item 8 ("Monitore recusas do modelo por categoria de input") tem natureza operacional/LLMOps distinta dos 7 primeiros (todos sobre estrutura do prompt). Pode ser mais bem posicionado em seção de "operação em produção" do que dentro da lista de padrões de engenharia de prompt.
- Ação: decisão do autor (envolve arquitetura da seção).

---

## JÁ RESOLVIDO (Ondas anteriores)

- APX-D · Migração de lista de ferramentas para repositório: JÁ RESOLVIDO (Onda 2).
- APX-E · Fusão com APX-F e migração de listas: JÁ RESOLVIDO (Onda 2).
- APX-F · Conversão para página de redirecionamento: JÁ RESOLVIDO (Onda 2).
- APX-L · Migração de XMLs para repositório: JÁ RESOLVIDO (Onda 2).
- APX-O · Migração de caderno executável para repositório: JÁ RESOLVIDO (Onda 2).
- APX-D referência D.1 e critério quantitativo: JÁ RESOLVIDO (presente).
- APX-J política editorial sem cadência fixa: JÁ RESOLVIDO (presente e consistente).
- APX-H referência a APX-E no rodapé (linha 126): JÁ RESOLVIDO (já usa título correto "Como montar sua dieta de informação").
- APX-C referências a APX-E: JÁ RESOLVIDO (usa título correto).

---

## RESUMO

| Categoria | Contagem |
|---|---|
| EDITADOS | 8 edições diretas em 6 arquivos |
| PENDENTE-AUTOR | 4 itens |
| JÁ RESOLVIDO | 9 itens verificados |

**Top achados de referência cruzada:**
1. APX-H cabeçalho referenciava "Newsletters" (APX-F extinto) — corrigido.
2. APX-I usava título antigo de APX-E ("leituras de fundamentação") e nome errado de APX-M ("Manifesto dos Princípios") — corrigidos.
3. APX-Q aula 4 apontava para gabarito inexistente em APX-K (C06 em vez de C04 inexistente) — corrigido.
4. APX-P e APX-J citavam o mesmo paper Hayes et al. com URLs arXiv diferentes — alinhados à URL de APX-J.

**Top achados de consistência interna:**
5. APX-L moldura dizia "sete padrões" mas o corpo tinha 8 — corrigido.
6. APX-J linha 170 tinha typo sintático ("que prometido") — corrigido.
7. APX-G tinha duplo separador `---` residual — corrigido.

**PENDENTE-AUTOR principal:** APX-O equipara o padrão conceitual do caderno com "Tipo C da taxonomia do APX-N" — a remissão é conceitualmente imprecisa e pode confundir leitor técnico que leu ambos os apêndices.
