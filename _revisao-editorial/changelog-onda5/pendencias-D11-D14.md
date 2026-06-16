# Changelog — Pendências D11, D12, D14, D6/D9

**Data de execução:** 2026-06-16
**Executor:** Editor Executivo (agente)
**Escopo:** Quatro correções de decisões já aprovadas pelo autor

---

## D11 — Epígrafe Dijkstra (C01)

**Arquivo:** `02-capitulos/L1-C01-o-que-e-ia.md`
**Localização:** Linhas 5–6

**Antes:**
```
> *"A pergunta não é se as máquinas pensam. A pergunta é se nós entendemos o que significa pensar."*
> — adaptado de Edsger Dijkstra
```

**Depois:**
```
> *"A questão de saber se uma máquina pode pensar é tão relevante quanto a questão de saber se um submarino pode nadar."*
> — Edsger W. Dijkstra, "The Threats to Computing Science" (EWD898), 1984
```

**Motivo:** Frase anterior era invenção "adaptada", não citação verificável. Nova epígrafe é a frase real e citável de EWD898 (1984), com atribuição completa sem "adaptado de".

**Impacto no corpo:** Verificado. O primeiro parágrafo da seção 1.1 abre com uma cena de direção para definir inteligência funcionalmente — não referencia a epígrafe antiga nem depende do tema "entender o que significa pensar". A nova epígrafe (a pergunta é mal formulada) flui diretamente para um capítulo que contorna a questão filosófica e vai direto à definição operacional. Nenhum ajuste no corpo necessário.

---

## D12 — Perspectiva proprietária "quando NÃO usar embeddings" (C05)

**Arquivo:** `02-capitulos/L1-C05-embeddings.md`
**Localização:** Final da seção 5.6 (Limitações e Armadilhas), antes do `---` de fechamento

**Antes:** Seção encerrava após a quinta limitação (embeddings ficam obsoletos), sem voz editorial sobre o caso de uso errado.

**Depois:** Adicionados 2 parágrafos após a quinta limitação, antes do separador de seção:

- **Parágrafo 1** introduz a "sexta limitação" — embedding é para similaridade semântica, não para exatidão. Âncora em casos reais: código de produto, número de apólice, cláusula contratual com redação específica, identificador regulatório, decisão judicial por número. Quando usar BM25/match exato/regex: precisão > recall, vocabulário controlado e estreito, custo alto de falso "parecido", exigência de explicabilidade para auditoria.
- **Parágrafo 2** formula o critério durável: confundir similaridade semântica com exatidão é erro de arquitetura, não de modelo. Entrega o critério binário (use embedding quando o valor está na semântica; use léxico quando o texto exato importa) e menciona o padrão maduro de combinar os dois em camadas.

**Tom:** Voz proprietária do autor, sem citar produto específico. Conclusão ancorada em método: embedding é ferramenta, não categoria superior de busca.

---

## D14 — Diversificar exemplo jurídico (C04)

**Arquivo:** `02-capitulos/L1-C04-janela-de-contexto.md`
**Localização:** Seção 4.4 inteira

**Setor substituído:** Escritório de advocacia revisando contratos comerciais → Gestora de recursos revisando relatórios de due diligence de M&A

**Título antes:** "O Contrato Que Não Foi Lido"
**Título depois:** "O Relatório Que Não Foi Lido"

**Mudanças específicas:**
- Operação: escritório de advocacia → gestora de recursos
- Documento: contratos comerciais longos → relatórios de due diligence de M&A (80–120 páginas)
- Usuário: advogado → analista financeiro
- Item perdido: cláusula de penalidade abusiva (pág. 40 de 80) → passivo contingente relevante (pág. 60 de 100)
- Consequência: falha em revisão jurídica → risco financeiro não sinalizado em análise de M&A

**Preservado:** Mecanismo idêntico (informação no meio do contexto sendo perdida), números de taxa de recuperação (60%/100%), arquitetura de solução (chunking em blocos de ~5k tokens com sobreposição), insight final.

**Motivo:** C02 já usa caso jurídico icônico e verificável (Mata v. Avianca — alucinação de advogado em NY). Dois exemplos jurídicos próximos diluíam o impacto e criavam percepção de que o livro trata IA como problema do setor jurídico. Due diligence de M&A é setor diferente, igualmente familiar ao público-alvo executivo, e o mecanismo de "documento longo com informação crítica no meio" mapeia com a mesma precisão.

---

## D6 — Pontes de transição 14B → 14C → 15

### Ponte 14B → 14C

**Arquivo:** `02-capitulos/L1-C14B-reasoning-models.md`
**Localização:** Após o conteúdo final, antes da epígrafe de fechamento

**Adicionado:**
```
---

> **Próximo capítulo:** Reasoning models respondem à pergunta de *como* o modelo pensa. O capítulo seguinte responde à pergunta consequente: se o agente passa a pensar com esse nível de autonomia, *como o trabalho de engenharia precisa se reorganizar* para controlar o que sai do outro lado? Esse é o território do Spec-Driven Development — a disciplina que transforma a especificação no artefato que dá ao operador controle real sobre o que o agente com reasoning entrega.

---
```

**Lógica da ponte:** Liga o eixo "como o modelo pensa" (reasoning) ao eixo "como o operador controla o que o modelo produz" (spec). A ponte é conceitual, não apenas navegacional — frames SDD como resposta operacional ao poder do reasoning.

### Ponte 14C → 15

**Arquivo:** `02-capitulos/L1-C14C-spec-driven-development.md`
**Localização:** Após `🎉 Você acabou de fechar a Parte 3`, antes da epígrafe de fechamento

**Situação antes:** Existia menção de navegação ("Avance para o Capítulo 15") dentro da tabela de autoavaliação, mas não havia ponte narrativa explícita.

**Adicionado:**
```
---

> **Próximo capítulo:** SDD definiu *como* especificar e controlar o que o agente constrói. Mas a spec não existe no vácuo — ela precisa nomear um modelo, calibrar para um provedor, e sobreviver à próxima geração de lançamentos. O Capítulo 15 entrega o critério estruturado para comparar modelos: não por benchmark de marketing, mas pelos eixos que a spec e a operação realmente exigem.

---
```

**Lógica da ponte:** Liga a spec (que nomeia o modelo como parâmetro de entrada) ao capítulo de comparação de modelos (que entrega o critério para essa escolha). Fecha o loop metodológico da Parte 3.

---

## D9 — Padronização "Curiosidade ativa" → "Curiosidade" (item 5 da autoavaliação)

**Arquivos afetados:**
- `02-capitulos/L1-C14B-reasoning-models.md` — linha do item 5 da tabela de autoavaliação (seção 14B.14)
- `02-capitulos/L1-C14C-spec-driven-development.md` — linha do item 5 da tabela de autoavaliação (seção 14C.14)

**Antes (ambos):** `**Curiosidade ativa**`
**Depois (ambos):** `**Curiosidade**`

**Motivo:** Padronização com o restante do livro. Todos os outros capítulos usam "Curiosidade" no item 5 da autoavaliação; C14B e C14C eram os únicos com variante "Curiosidade ativa".

---

*Changelog gerado pelo Editor Executivo. Todas as edições foram aplicadas diretamente nos arquivos de origem.*
