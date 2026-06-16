# Changelog Onda 1 — Apêndices A a I
## Escopo: correções P0 apenas
## Data de execução: 2026-06-16

---

## RESUMO

| Status | Qtd | Itens |
|--------|-----|-------|
| [EDITADO] | 4 | APX-C/01, APX-D/01, APX-F/01, APX-I/01 |
| [REQUER DECISÃO DO AUTOR] | 0 | — |
| [REQUER ASSET] | 0 | — |

Total P0 neste bloco: 4. Todos aplicados nesta onda.

---

## APX-C — L1-APX-C-roadmaps.md

### [EDITADO] APX-C/01 — P0 — Roadmap 6 orientava publicação de biblioteca de prompts

**Problema:** Roadmap 6 (Criador de Conteúdo), Marco 90 dias: artefato "Biblioteca pessoal de prompts publicada" contradiz diretamente a tese central da obra ("Modelos passam. Método fica."). Publicar biblioteca de prompts posiciona o leitor como colecionador de prompts — exatamente o que o livro critica.

**Correção aplicada:** Substituição cirúrgica do artefato.

- **Antes:** `Biblioteca pessoal de prompts publicada`
- **Depois:** `Biblioteca de frameworks de decisão publicada (ex.: como aplicar o Diagnóstico de Encaixe por vertical, com princípio associado — não lista de prompts isolados)`

**Arquivo:** `/04-apendices/L1-APX-C-roadmaps.md`
**Linha afetada:** Marco 90 dias do Roadmap 6.

---

## APX-D — L1-APX-D-ferramentas.md

### [EDITADO] APX-D/01 — P0 — DeepSeek API com nota geopolítica vaga e não acionável

**Problema:** A nota "viés geopolítico para discutir conforme caso" não orienta decisão, não oferece critério e pode ser interpretada em qualquer direção conforme o contexto geopolítico evolua. Deixa o autor exposto a interpretações fora de controle.

**Correção aplicada:** Substituição da nota vaga por critério durável ancorado no framework D.1 já existente no apêndice.

- **Antes (coluna "Estado em junho/2026"):** `Em consolidação, preço-qualidade agressivo, viés geopolítico para discutir conforme caso`
- **Depois:** `Em consolidação, preço-qualidade agressivo; avalie risco geopolítico via critério D.1: origem do provedor, regime de dados do país de origem, restrições setoriais aplicáveis e precedente de descontinuação por decisão política`

- **Antes (coluna "Aplicação típica"):** `Aplicações sensíveis a custo unitário, organizações sem restrição quanto à origem do provedor`
- **Depois:** `Aplicações sensíveis a custo unitário; requer avaliação explícita de risco geopolítico antes de adoção em produção corporativa`

**Arquivo:** `/04-apendices/L1-APX-D-ferramentas.md`
**Linha afetada:** Tabela D.2, linha DeepSeek API.

---

## APX-F — L1-APX-F-newsletters.md

### [EDITADO] APX-F/01 — P0 — Bots Brasil Podcast (2026) incluído como referência permanente sem histórico de maturidade

**Problema:** Publicação lançada em 2026, na mesma data da obra, sem histórico de maturidade verificável. Risco extremo de referência morta antes da próxima revisão programada (junho de 2027).

**Correção aplicada:** Entrada removida da lista principal de curadoria; movida para nota editorial com aviso explícito de verificação pendente.

- **Removido da lista principal:** o parágrafo completo iniciado por `**Bots Brasil Podcast.**`
- **Adicionada nota editorial logo após o aviso de verificação anual:**

```
> **Nota editorial:** o Bots Brasil Podcast surgiu em 2026 e não tem histórico suficiente para inclusão permanente nesta curadoria. Verificar estado e maturidade na revisão de junho de 2027.
```

**Arquivo:** `/04-apendices/L1-APX-F-newsletters.md`
**Seção afetada:** Seção 2 — Podcasts em português / Tecnologia ampla com IA recorrente.

---

## APX-I — L1-APX-I-indice-remissivo.md

### [EDITADO] APX-I/01 — P0 — Referências mortas a Apêndices K, L e M (inexistentes); C14B e C14C ausentes

**Problema:** O índice remissivo referenciava "Apêndice K" (duas entradas), "Apêndice L" (uma entrada) e "Apêndice M" (duas entradas) — apêndices que não existem na estrutura atual da obra (A a I). Adicionalmente, os capítulos C14B (Reasoning models) e C14C (Spec-driven development) não tinham entrada no índice.

**Correções aplicadas (5 edições cirúrgicas):**

| Entrada | Antes | Depois |
|---------|-------|--------|
| Datasets de prática | `Apêndice K` | `Apêndice D (critério de seleção de ferramentas e fontes de dados)` |
| Gabaritos | `Apêndice K` | `capítulo sobre Evals; Pirâmide da Avaliação` |
| Prompt | `Apêndice L; Engenharia de Prompt Estendida` | `Apêndice E (leituras de fundamentação); Engenharia de Prompt Estendida` |
| Os Nove Princípios ★ | `Introdução; Apêndice M` | `Introdução; Apêndice B (Mapa Mental)` |
| Manifesto dos Princípios | `Introdução; Apêndice M` | `Introdução; Apêndice B (Mapa Mental)` |

**Entradas adicionadas:**

- Seção R: `**Reasoning models ◆** — capítulo C14B (Reasoning models); Princípio 1`
- Seção S: `**Spec-driven development** — capítulo C14C; Princípios 4 e 8`

**Arquivo:** `/04-apendices/L1-APX-I-indice-remissivo.md`

**Nota para o autor:** O redirecionamento de "Datasets de prática → APX-D" e "Gabaritos → capítulo sobre Evals" é a inferência mais razoável dada a estrutura atual, mas o autor deve confirmar se esses conteúdos foram absorvidos nos capítulos indicados ou se existem em outro local. Se Apêndices K, L e M foram planejados mas ainda não escritos, o autor deve decidir entre criar os apêndices faltantes ou manter as remissivas corrigidas para os destinos atuais.

---

*Changelog gerado em 2026-06-16. Onda 1 — P0 apenas.*
