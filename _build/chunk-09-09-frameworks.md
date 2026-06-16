---
title: "Inteligência Aumentada"
lang: pt-BR
---



<div class="page-break"></div>


# FRAMEWORK F1 — DECID-IA
## Decisão de adoção de IA por iniciativa

---

> 🧭 **Invariante-mãe:** **Invariante 9 — Operador** — *"A IA multiplica competência e incompetência pelo mesmo fator."*
> Invariante secundário: **Inv. 8 — Responsabilidade Indelegável** (toda iniciativa tem cadeira humana).
> Capítulo-âncora: [Cap 34 (L2) — Claude para Executivos](../../Livro-2-Dominando-Claude/02-capitulos/L2-C34-executivos.md) + [Cap 44 — Roadmap pessoal e organizacional](../02-capitulos/L1-C44-roadmap-pessoal.md).

---

## 1. OBJETIVO

Decidir, em até 30 minutos, se uma iniciativa específica deve usar IA, com qual nível de autonomia, e quem é o dono. Sai com cinco respostas duras e um plano mínimo, ou sai com a recusa documentada da iniciativa por critério explícito.

## 2. FUNCIONAMENTO

Cinco perguntas em ordem rígida. Sair em qualquer uma delas com resposta vaga interrompe o framework: ou se torna específica, ou a iniciativa não passa.

### Pergunta 1 — Tarefa
*"O que exatamente a IA vai fazer?"* Verbo + objeto + critério de sucesso, em uma frase.

Exemplo aceitável: "Classificar tickets de suporte em uma de cinco categorias com F1 mínimo de 0,85 contra rótulo humano". Exemplo não aceitável: "Ajudar o time de suporte com IA".

### Pergunta 2 — Operador
*"Quem opera, com que critério de aceitação?"* Pessoa nominal e regra explícita de quando aceita a saída.

Se a resposta for "ninguém define" ou "o usuário decide", a iniciativa não passa. Voltar à pergunta 1 e estreitar.

### Pergunta 3 — Risco
*"O que acontece se a saída estiver errada? Reversível ou não?"* Tipologia: financeiro, jurídico, reputacional, clínico, operacional. Reversibilidade em escala de quatro: totalmente reversível (idempotente), reversível com custo (compensável), parcialmente reversível, irreversível.

### Pergunta 4 — Linha de medição
*"Como saberemos que está funcionando?"* Métrica primária + golden set inicial + frequência de revisão.

Sem golden set planejado, a iniciativa pode passar para piloto interno mas não para produção. Inv. 7 manda.

### Pergunta 5 — Responsabilidade
*"Quem assina?"* Nome próprio, com cadeira específica, com competência para responder pela decisão.

Sem nome, não passa. Inv. 8 manda.

## 3. OUTPUT

A saída do F1, em uma página, contém:

| Campo | Conteúdo |
|-------|----------|
| Vai / Não-vai | Decisão binária com justificativa em uma frase |
| Nível de autonomia | Assistente · Co-piloto · Agente supervisionado · Agente autônomo regulado (define-se via [F3 AGENTE-PROP](L1-F3-agente-prop.md)) |
| Plano de eval | Golden set inicial, métrica primária, gate de bloqueio (via [F8 EVAL-PIRÂMIDE](L1-F8-eval-piramide.md)) |
| Dono nominal | Nome + cadeira + cláusula de accountability |
| Revisão programada | Quando o framework volta a rodar para reavaliar |

## 4. EXEMPLO DE USO

| Pergunta | Resposta concreta |
|----------|--------------------|
| 1 — Tarefa | Triar currículos em "candidato com fit > 0,7 contra rubrica do hiring manager" (NÃO decisão de contratação) |
| 2 — Operador | Recrutador sênior + hiring manager; aceitação se humano revisa top-15 antes de contato |
| 3 — Risco | Reputacional alto (alegação de discriminação); irreversível em reputação; reversível em decisão |
| 4 — Linha de medição | Golden set de 400 currículos com gabarito de sêniores; viés ≤2% em adversarial de variantes equivalentes; revisão trimestral |
| 5 — Responsabilidade | Diretor de RH + DPO assinam Caderno de Governança da iniciativa |

**Decisão:** vai como **assistente** (humano decide sempre), nunca como decisor único. Eval comportamental mensal (Cap 41). Auditoria de viés trimestral (Cap 42). Política de transparência com candidato.

## 5. ANTI-PADRÕES

| Anti-padrão | Por que mata |
|-------------|--------------|
| Pular a pergunta 2 (operador) | Iniciativa fica sem dono operacional; falha quando precisa iterar |
| Pular a pergunta 5 (responsabilidade) | Falha jurídica e institucional quando der ruim |
| Aceitar "depois a gente decide isso" em qualquer pergunta | Toda dúvida adiada vira incidente |
| Aplicar o framework retroativamente, em iniciativa já em produção, sem corrigir buracos | Vira teatro de processo |

## 6. CONEXÕES

- 🔗 [Manifesto dos Invariantes](../01-manifesto/L1-C00M-manifesto-invariantes.md)
- 🔗 [Cap 39 — Evals](../02-capitulos/L1-C39-evals.md) (linha de medição da Pergunta 4)
- 🔗 [Cap 40 — LLMOps](../02-capitulos/L1-C40-llmops.md) (nível de autonomia da Pergunta 3)
- 🔗 [Cap 42 — Governança](../02-capitulos/L1-C42-governanca.md) (responsabilidade nominal da Pergunta 5)
- 🔗 [F3 — AGENTE-PROP](L1-F3-agente-prop.md) (decide o nível de autonomia)
- 🔗 [F6 — GOV-INDELEGÁVEL](L1-F6-gov-indelegavel.md) (governança da iniciativa)
- 🔗 [F8 — EVAL-PIRÂMIDE](L1-F8-eval-piramide.md) (plano de eval da iniciativa)

---

> *"Vai ou não-vai não é palpite, é resposta a cinco perguntas duras. Quem pula uma delas paga depois."*



<div class="page-break"></div>


# FRAMEWORK F2 — ENCAIXE-5
## Escolha de modelo por 5 eixos de tarefa

---

> 🧭 **Invariante-mãe:** **Invariante 4 — Encaixe** — *"Escolha pelo padrão da tarefa, nunca pela versão da moda."*
> Capítulo-âncora: [Cap 15 — Comparação dos principais modelos](../02-capitulos/L1-C15-comparacao-modelos.md).
> Aplicação Claude: [Cap 18 — Modelos Claude](../../Livro-2-Dominando-Claude/02-capitulos/L2-C18-modelos-claude.md).
> Números correntes: [Apêndice Vivo (J)](../../Livro-2-Dominando-Claude/04-apendices/L2-APX-J-apendice-vivo.md).

---

## 1. OBJETIVO

Decidir qual modelo usar para uma tarefa específica, sem cair em "modelo do mês". A decisão é função do **padrão da tarefa** (durável), não da liderança da semana em benchmark agregado (volátil).

## 2. FUNCIONAMENTO

Pontuar a tarefa de 0 a 5 em cinco eixos canônicos, e aplicar a matriz de perfis de família. Modelo escolhido é o de **melhor encaixe ponderado**, não o de melhor benchmark agregado.

### Os 5 eixos

| Eixo | O que pontuar | Família que tende a vencer |
|------|---------------|----------------------------|
| **Razão complexa** | Tarefas com múltiplos passos, auditoria do percurso, decisão lógica encadeada | Premium dos três frontier; thinking-models open |
| **Código** | Edição de código real, com testes, contexto longo, refatoração | Família Claude (Opus) em SWE-bench Verified, historicamente |
| **Contexto longo** | Análise de documentos extensos, bases volumosas, múltiplos arquivos | Família Gemini Pro (pelo tamanho de janela típico) |
| **Multimodal** | Vídeo, imagem, áudio nativos; OCR, leitura de gráfico | Família Gemini Pro |
| **Custo crítico** | Volume altíssimo, margem apertada, classificação simples em produção | Variantes Flash/Haiku/Mini; open source self-hosted |

### Mecânica de aplicação

1. **Pontuar a tarefa** de 0 a 5 em cada eixo. Notas altas indicam que o eixo importa muito para essa tarefa.
2. **Identificar o eixo dominante** (maior nota). Se houver empate entre dois ou três eixos, marcar todos.
3. **Consultar o Apêndice Vivo** para a família corrente que lidera cada eixo dominante.
4. **Escolher pelo melhor encaixe**, com fallback explícito. Se o eixo dominante é "código" + "razão complexa", o premium da família com força em ambos vence.
5. **Definir critério de reavaliação**: a cada seis meses, a cada lançamento de mesmo eixo, ou conforme custo cruzar limite.

## 3. OUTPUT

| Campo | Conteúdo |
|-------|----------|
| Tarefa pontuada nos 5 eixos | Tabela 5×1 com notas |
| Eixo(s) dominante(s) | 1 a 3 eixos com nota ≥4 |
| Modelo escolhido | Família + tier + variante específica (com link ao Apêndice Vivo) |
| Modelo fallback | Para resiliência ou cost ceiling |
| Critério de reavaliação | Cadência e gatilho |

## 4. EXEMPLOS DE USO

### Exemplo A — Classificação de e-mail em larga escala (5M/mês)

| Eixo | Nota |
|------|------|
| Razão complexa | 1 |
| Código | 0 |
| Contexto longo | 1 |
| Multimodal | 0 |
| Custo crítico | 5 |

Eixo dominante: **custo crítico**. Encaixe: variante pequena (Haiku-like) com prompt enxuto ou fine-tuning leve. Fallback: variante pequena de outro vendor. Reavaliação: trimestral ou quando volume mudar de magnitude.

### Exemplo B — Agente de engenharia para refatoração de código legado

| Eixo | Nota |
|------|------|
| Razão complexa | 5 |
| Código | 5 |
| Contexto longo | 4 |
| Multimodal | 0 |
| Custo crítico | 2 |

Eixos dominantes: **código + razão complexa + contexto longo**. Encaixe: premium da família Claude (Opus) com Claude Code. Fallback: premium concorrente para tarefas onde matemática lidera. Reavaliação: a cada release relevante; teste cego comparado em PRs reais.

### Exemplo C — Análise de relatório técnico com gráficos e tabelas

| Eixo | Nota |
|------|------|
| Razão complexa | 3 |
| Código | 0 |
| Contexto longo | 4 |
| Multimodal | 5 |
| Custo crítico | 2 |

Eixos dominantes: **multimodal + contexto longo**. Encaixe: Gemini Pro pela liderança em multimodal e janela grande. Fallback: variante balanceada de Claude para texto + chamada multimodal específica para o anexo. Reavaliação: semestral.

## 5. ANTI-PADRÕES

| Anti-padrão | Por que mata |
|-------------|--------------|
| "Lançou novo, vou trocar" | Migração sem teste cego na própria carga troca problema conhecido por desconhecido |
| Usar Opus para tudo "porque é o melhor" | Viola Inv. 5; em meses, a fatura mostra o erro |
| Não ter fallback | Vendor outage vira incidente para o cliente final |
| Decidir por benchmark agregado | Esconde força em eixo específico que importa para sua carga |
| Reavaliar só quando "a equipe quiser" | Sem cadência fixa, vira reação ao boato da semana |

## 6. CONEXÕES

- 🔗 [Manifesto dos Invariantes](../01-manifesto/L1-C00M-manifesto-invariantes.md)
- 🔗 [Cap 15 — Comparação de modelos](../02-capitulos/L1-C15-comparacao-modelos.md)
- 🔗 [Cap 18 — Modelos Claude (L2)](../../Livro-2-Dominando-Claude/02-capitulos/L2-C18-modelos-claude.md)
- 🔗 [Apêndice Vivo (J)](../../Livro-2-Dominando-Claude/04-apendices/L2-APX-J-apendice-vivo.md)
- 🔗 [F5 — MCP-COBERTURA](L1-F5-mcp-cobertura.md) (decisão complementar para integração)
- 🔗 [F7 — COMPOSTO-3T](L1-F7-composto-3t.md) (decisão de tier como vetor de custo)

---

> *"Padrão da tarefa não muda toda rodada. Líder da rodada muda toda rodada. Decida pelo que dura."*



<div class="page-break"></div>


# FRAMEWORK F3 — AGENTE-PROP
## Arquitetura de agentes por autonomia proporcional

---

> 🧭 **Invariante-mãe:** **Invariante 6 — Autonomia Proporcional** — *"Só dê ao agente a autonomia que você consegue medir e desfazer."*
> Capítulo-âncora conceitual: [Cap 12 — Agentes de IA](../02-capitulos/L1-C12-agentes.md).
> Capítulo-âncora operacional: [Cap 40 — LLMOps](../02-capitulos/L1-C40-llmops.md).
> Aplicação Claude: [Cap 24 Claude Code](../../Livro-2-Dominando-Claude/02-capitulos/L2-C24-claude-code.md), [Cap 32 Subagents](../../Livro-2-Dominando-Claude/02-capitulos/L2-C32-subagents-workflows.md).

---

## 1. OBJETIVO

Decidir o nível de autonomia que um agente pode receber, em função direta de duas capacidades operacionais: **rastrear** (observabilidade) e **reverter** (rollback). Garantir que autonomia delegada nunca exceda a proporção que o time consegue medir e desfazer.

## 2. FUNCIONAMENTO

Matriz 4×4 cruzando observabilidade × reversibilidade. O quadrante de encontro determina o nível máximo de autonomia permitido na iniciativa.

### Eixos da matriz

**Eixo X — Observabilidade disponível:**
1. Nenhuma (só log de erro)
2. Logs estruturados de input/output
3. Tracing por span (input, output, latência, tokens, custo por passo)
4. Tracing + replay (capacidade de reproduzir a execução completa)

**Eixo Y — Reversibilidade da ação:**
1. Nenhuma (irreversível — envio externo, comunicação a cliente, transação financeira)
2. Compensável (existe ação de desfazer com custo)
3. Totalmente reversível (rollback automático, idempotente)
4. Sem efeito externo (só leitura, simulação)

### Os 4 níveis canônicos de autonomia

| Nível | Quando aplicar | Tipo de ação permitida |
|-------|----------------|-------------------------|
| **Assistente** | Observabilidade 1-2 OU reversibilidade 1 sem rollback | Gera proposta; humano executa |
| **Co-piloto** | Observabilidade 2-3 + reversibilidade 2 | Executa com confirmação a cada passo crítico |
| **Agente supervisionado** | Observabilidade 3 + reversibilidade 3 + humano monitora trace em tempo real | Executa em lote; humano interrompe se algo errado |
| **Agente autônomo regulado** | Observabilidade 4 + reversibilidade 3-4 + eval online + kill switch testado | Executa em produção sem supervisão direta, com gates de promoção |

### Gates de promoção entre níveis

Promoção entre níveis exige:
1. **Métrica de qualidade** estável por N dias (N depende da carga; tipicamente 14-30 dias)
2. **Zero incidentes** SEV-1 ou SEV-2 no período
3. **Custo composto** dentro do envelope acordado
4. **Aprovação nominal** do dono operacional (Inv. 8)
5. **Plano de rollback** testado no nível em questão

Rebaixamento é automático: incidente SEV-1 ou SEV-2 desativa promoção até nova análise.

## 3. OUTPUT

| Campo | Conteúdo |
|-------|----------|
| Nível atual autorizado | Assistente / Co-piloto / Supervisionado / Autônomo regulado |
| Tools permitidas no nível | Lista com permissões (read-only, write com confirmação, write livre) |
| Gates de promoção | Condições explícitas e mensuráveis para subir de nível |
| Critérios de rebaixamento | Triggers que retornam o agente a nível anterior |
| Kill switch | Quem aciona, em quantos segundos, e como testar |
| Plano de rollback | Estado anterior em hot standby; teste mensal documentado |

## 4. EXEMPLO DE USO

**Caso:** agente que envia e-mail externo de boas-vindas em onboarding de cliente B2B.

| Dimensão | Avaliação |
|----------|-----------|
| Observabilidade | Tracing por span existe (3); replay não |
| Reversibilidade da ação | Compensável (e-mail de apologia, escalonamento humano) — nível 2 |
| Quadrante de encontro | Observabilidade 3 + reversibilidade 2 → **Co-piloto** |

**Decisão inicial:** agente opera como co-piloto, com confirmação humana a cada e-mail antes do envio nos primeiros 30 dias.

**Gates de promoção a agente supervisionado:** zero reclamação de cliente em 30 dias, taxa de aprovação humana >95%, eval comportamental sem regressão. Após promoção, humano monitora trace em dashboard mas não confirma cada envio.

**Gate de promoção a agente autônomo regulado:** após mais 60 dias de operação supervisionada sem incidente, implementação de replay completo (atinge observabilidade 4), kill switch testado em simulado mensal.

**Kill switch:** desliga via feature flag em ≤30 segundos. Testado mensalmente em staging com rollback simulado. Dono: VP de Customer Success.

## 5. ANTI-PADRÕES

| Anti-padrão | Por que mata |
|-------------|--------------|
| Agente autônomo com escrita em produção sem tracing | Passivo, não ativo; incidente vira investigação de semanas |
| "A IA é boa, podemos confiar" como justificativa de pular níveis | Quando ela falhar (e vai), não há observabilidade para reconstruir |
| Kill switch teórico (existe no roadmap, nunca foi testado) | Na hora do incidente, descobre-se que não funciona |
| Rollback documentado, nunca exercitado | Rollback que não é testado, na hora não funciona |
| Tratar todos os agentes da empresa no mesmo nível | Ignora variação real de risco entre casos de uso |

## 6. CONEXÕES

- 🔗 [Manifesto dos Invariantes](../01-manifesto/L1-C00M-manifesto-invariantes.md)
- 🔗 [Cap 12 — Agentes](../02-capitulos/L1-C12-agentes.md)
- 🔗 [Cap 40 — LLMOps](../02-capitulos/L1-C40-llmops.md) (os 7 pilares operacionais sustentam o framework)
- 🔗 [Cap 24 — Claude Code (L2)](../../Livro-2-Dominando-Claude/02-capitulos/L2-C24-claude-code.md)
- 🔗 [Cap 32 — Subagents (L2)](../../Livro-2-Dominando-Claude/02-capitulos/L2-C32-subagents-workflows.md)
- 🔗 [F1 — DECID-IA](L1-F1-decid-ia.md) (passo 3 do F1: define o risco; F3 decide o nível)
- 🔗 [F8 — EVAL-PIRÂMIDE](L1-F8-eval-piramide.md) (eval suporta promoção entre níveis)
- 🔗 [F6 — GOV-INDELEGÁVEL](L1-F6-gov-indelegavel.md) (Inv. 8 sustenta o "dono" de cada nível)

---

> *"Autonomia sem rollback testado é passivo no balanço. Não importa que esteja funcionando hoje."*



<div class="page-break"></div>


# FRAMEWORK F4 — PROMPT-EXT
## Engenharia de prompts pelas extremidades

---

> 🧭 **Invariante-mãe:** **Invariante 2 — Extremidades** — *"O meio do contexto é onde a informação vai morrer."*
> Invariante secundário: **Inv. 3 — Camada Dupla** (separa o padrão durável do conteúdo da chamada).
> Capítulos-âncora: [Cap 04 — Janela de contexto](../02-capitulos/L1-C04-janela-de-contexto.md), [Cap 09 — Engenharia de prompt](../02-capitulos/L1-C09-engenharia-prompt.md), [Cap 11 — Context Engineering](../02-capitulos/L1-C11-context-engineering.md).

---

## 1. OBJETIVO

Escrever prompts de produção que respeitam a física de atenção (Inv. 2) e que separam, dentro do prompt, o que é padrão estável do que é número volátil (Inv. 3). Garantir que a regra crítica nunca fique no centro do prompt, e que cada bloco esteja na posição em que será efetivamente seguido.

## 2. FUNCIONAMENTO

Estrutura canônica em **5 blocos**, com regras explícitas de posição.

### Bloco 1 — Persona e missão (topo do prompt)

Curto, claro, ancorado. Diz o que o modelo é e qual o seu objetivo no fluxo. Esta posição recebe a maior parte da atenção do modelo, e por isso carrega a definição que precisa permear toda a resposta.

> *Exemplo:* "Você é o agente de atendimento ao cliente do Banco Solar. Sua missão é resolver o caso do cliente em até três respostas, ou escalar para humano com sumário estruturado."

### Bloco 2 — Constituição (regras invioláveis, imediatamente após persona)

Pequeno, denso, em bullets curtos. Aqui ficam as regras que **nunca podem ser quebradas**, e que precisam estar próximas da persona para receberem peso adequado. É a parte do prompt que sobrevive entre chamadas — versionada, revisada, governada. É a Camada Dupla materializada: padrão estável.

> *Exemplo:*
> *Constituição:*
> *— Nunca afirmar saldo sem consultar a tool `consulta_saldo`.*
> *— Em qualquer suspeita de fraude, escalar imediatamente para humano.*
> *— Nunca prometer ressarcimento; só humano autoriza.*
> *— Comunicação sempre em pt-BR formal, sem expressões coloquiais.*

### Bloco 3 — Contexto da tarefa atual (meio do prompt)

Pode ser maior. Documentos, exemplos, dados, histórico de conversa. Esta é a parte que recebe **menos atenção em prompts longos** — por isso, **nada crítico vai aqui**. Conteúdo do meio é informação de apoio, não regra.

### Bloco 4 — Instrução operacional + formato esperado (imediatamente antes da pergunta viva)

Curto. Posição forte (a segunda mais atendida, depois da abertura). Repete o crítico das regras na linguagem da tarefa específica, e define o formato exato da saída esperada.

> *Exemplo:* "Responda em pt-BR formal, máximo três parágrafos, sem expressões coloquiais. Cite a tool consultada quando aplicável. Se não conseguir resolver, escale para humano com sumário em 3 bullets."

### Bloco 5 — Pergunta viva / input do usuário (última posição)

Sempre na última posição. Sempre. Sanitizada contra prompt injection. Esta é a única parte do prompt que muda em cada chamada — a Camada Dupla materializada: número volátil.

## 3. OUTPUT

O F4 produz um prompt que se lê assim:

```
[BLOCO 1 — PERSONA E MISSÃO]
(curto, 1-3 linhas)

[BLOCO 2 — CONSTITUIÇÃO]
(bullets curtos, 4-8 itens)

[BLOCO 3 — CONTEXTO]
(documentos, exemplos, dados, histórico)

[BLOCO 4 — INSTRUÇÃO OPERACIONAL + FORMATO]
(reitera o crítico, define output)

[BLOCO 5 — PERGUNTA VIVA]
(input do usuário, sanitizado)
```

## 4. EXEMPLO DE USO

**Caso:** agente de revisão de contrato em escritório de advocacia.

```
Você é o agente de revisão de contratos comerciais do escritório Vianna,
Castro e Almeida. Sua missão é identificar cláusulas atípicas, com base
nos padrões da banca, e produzir parecer estruturado em até cinco minutos
de processamento.

[CONSTITUIÇÃO]
- Nunca afirmar cláusula sem citar o trecho literal e a localização (página
  e parágrafo).
- Em qualquer cláusula de mudança de controle, change of control ou MAC,
  marcar como red flag SEV-1 mesmo se redação parecer padrão.
- Nunca recomendar assinatura ou rejeição: produzir parecer; sócio decide.
- Idioma de saída: pt-BR técnico. Citações no idioma original do contrato.

[CONTEXTO]
[Inserir aqui: trechos relevantes do contrato, padrões da banca, casos
similares de DD anteriores, glossário de cláusulas-alvo.]

[INSTRUÇÃO OPERACIONAL]
Produza parecer em três seções: (1) sumário executivo em 5 bullets;
(2) red flags SEV-1 e SEV-2 com citação literal de página/parágrafo;
(3) cláusulas padrão verificadas com nota de "normal" ou "negociar".
Não recomende assinatura. Em qualquer cláusula change of control,
marcar SEV-1 mesmo se redação parecer padrão.

[PERGUNTA VIVA]
[Input do operador: pergunta específica sobre o contrato em análise]
```

A constituição vive em artefato versionado (Skills no L2). O contexto muda
por contrato. A pergunta viva muda por chamada. O bloco 4 reitera as
regras críticas porque, mesmo com a constituição no topo, **a chamada do
modelo termina pelo bloco 4** — daí a redundância deliberada.

## 5. ANTI-PADRÕES

| Anti-padrão | Por que mata |
|-------------|--------------|
| Enterrar regra crítica no parágrafo 40 de prompt longo | Inv. 2: atenção decai no meio; regra ignorada silenciosamente |
| Colocar a pergunta no início, antes do contexto | Modelo responde ao input sem ter visto o contexto |
| Constituição não versionada (string no código) | Sem rastreabilidade de mudança; vira buraco de governança |
| Misturar regra inviolável com sugestão estilística | Modelo perde hierarquia; quebra ambas com a mesma facilidade |
| Não reiterar o crítico no bloco 4 | Em prompts longos, o final domina; sem reiteração, regra do topo enfraquece |
| Não sanitizar a pergunta viva | Prompt injection via input do usuário sobrescreve a constituição |

## 6. CONEXÕES

- 🔗 [Manifesto dos Invariantes](../01-manifesto/L1-C00M-manifesto-invariantes.md)
- 🔗 [Cap 04 — Janela de contexto](../02-capitulos/L1-C04-janela-de-contexto.md)
- 🔗 [Cap 09 — Engenharia de prompt](../02-capitulos/L1-C09-engenharia-prompt.md)
- 🔗 [Cap 11 — Context Engineering](../02-capitulos/L1-C11-context-engineering.md)
- 🔗 [Cap 20 — Projects (L2)](../../Livro-2-Dominando-Claude/02-capitulos/L2-C20-projects.md) — *Projects materializam o bloco de constituição*
- 🔗 [Cap 31 — Skills (L2)](../../Livro-2-Dominando-Claude/02-capitulos/L2-C31-skills.md) — *Skills versionam o bloco de constituição como ativo*
- 🔗 [F8 — EVAL-PIRÂMIDE](L1-F8-eval-piramide.md) — *o adversarial set inclui prompt injection contra a pergunta viva*

---

> *"A regra que importa não vai no meio do prompt. Vai na primeira posição forte e na última. Quem coloca no centro está rezando para a atenção do modelo, e a atenção não está olhando."*



<div class="page-break"></div>


# FRAMEWORK F5 — MCP-COBERTURA
## Decisão de adoção de MCP por quadrante

---

> 🧭 **Invariante-mãe:** **Invariante 6 — Autonomia Proporcional** — *"Só dê ao agente a autonomia que você consegue medir e desfazer."*
> Invariante secundário: **Inv. 4 — Encaixe** (padrão maduro × padrão ad-hoc).
> Capítulos-âncora: [Cap 13 — MCP](../02-capitulos/L1-C13-mcp.md), [Cap 33 (L2) — Claude + MCP](../../Livro-2-Dominando-Claude/02-capitulos/L2-C33-claude-mcp.md).

---

## 1. OBJETIVO

Decidir, por *capability* (capacidade), se vale adotar **MCP existente público**, **MCP self-hosted**, **MCP próprio** ou **tool ad-hoc** — sem cair no extremo de "tudo MCP" (over-engineering) nem no de "nada MCP" (lock-in artesanal). A decisão é função do **padrão maduro disponível** e da **sensibilidade dos dados** envolvidos.

## 2. FUNCIONAMENTO

Matriz 2×2 cruzando padrão maduro × sensibilidade de dados. Cada quadrante dita o tipo de MCP correto.

### Eixos da matriz

**Eixo X — Padrão maduro disponível?**
- **Sim:** existe MCP público bem mantido, com comunidade ativa, governança clara
- **Não:** sem padrão estabelecido; ou existe mas é experimental, abandonado, sem dono claro

**Eixo Y — Sensibilidade dos dados?**
- **Alta:** dados sob LGPD/regulação, segredos comerciais, PII, dados de cliente em produção
- **Baixa:** dados públicos, dados de teste, contexto sem implicação regulatória

### Os 4 quadrantes

| Quadrante | Condição | Decisão | Exemplo típico |
|-----------|----------|---------|----------------|
| **A** | Padrão maduro + dados não sensíveis | **Adotar MCP público** | Calendar, Notion público, GitHub public APIs, Google Search |
| **B** | Padrão maduro + dados sensíveis | **MCP self-hosted ou variante privada** | Slack workspace privado, Salesforce, GitHub enterprise |
| **C** | Sem padrão + dados não sensíveis | **Tool ad-hoc** até virar padrão | API interna nova, integração experimental |
| **D** | Sem padrão + dados sensíveis | **MCP próprio com auditoria completa** | Core bancário, sistemas regulados, PHI/PII em saúde |

### Mecânica de aplicação

1. Listar as *capabilities* (capacidades) que a operação precisa que o agente acesse — leitura, escrita, busca, execução em sistemas terceiros
2. Para cada capability, pontuar os dois eixos
3. Aplicar o quadrante correspondente
4. Documentar: dono nominal por MCP, política de auditoria, política de versionamento, plano de migração se quadrante mudar

## 3. OUTPUT

| Campo | Conteúdo |
|-------|----------|
| Lista de capabilities | O que o agente precisa acessar |
| Quadrante por capability | A/B/C/D justificado |
| Tipo de MCP escolhido | Público / self-hosted / ad-hoc / próprio |
| Dono nominal por MCP | Pessoa responsável + cadeira |
| Política de auditoria | Frequência, escopo, retenção |
| Plano de migração | Quando o quadrante mudar |

## 4. EXEMPLO DE USO — BANCO SOLAR (FINTECH)

Caso composto: fintech BR precisa expor ao agente conjuntos diversos de capability.

| Capability | Eixo X (padrão maduro?) | Eixo Y (sensibilidade?) | Quadrante | Decisão |
|-----------|---------------------------|--------------------------|-----------|---------|
| Calendário do atendente | Sim (Google Calendar MCP) | Baixa | A | MCP público |
| Conhecimento público de produto | Sim (Notion público) | Baixa | A | MCP público |
| Slack workspace interno (notificações) | Sim (Slack MCP) | Alta | B | MCP self-hosted ou variante privada |
| CRM da fintech (Salesforce) | Sim | Alta | B | MCP self-hosted |
| Sistema novo de tickets (lançado mês passado) | Não | Baixa | C | Tool ad-hoc até virar padrão |
| Core bancário (consulta saldo, abre contestação) | Não | Alta | D | MCP próprio com auditoria completa |

**Resultado:** o Banco Solar opera 4 categorias de MCP simultaneamente, com governança específica para cada quadrante. Capability do quadrante D (core bancário) tem dono nominal de área de tecnologia + DPO + Compliance, auditoria a cada release, retenção de log por 5 anos.

## 5. ANTI-PADRÕES

| Anti-padrão | Por que mata |
|-------------|--------------|
| "Tudo MCP" (over-engineering) | Capability nova sem padrão maduro vira projeto de plataforma que atrasa entrega |
| "Nada MCP" (lock-in artesanal) | Toda integração vira tool específica; agente fica frágil; manutenção explode |
| MCP público para dados sensíveis | Risco regulatório e de vendor — o servidor MCP pode logar, vazar, mudar |
| MCP próprio sem auditoria | Cria o falso conforto de "está sob controle" sem sustentar a alegação |
| Não documentar o quadrante por capability | Decisão é refeita por cada engenheiro novo, sem critério |
| Não monitorar quando o quadrante mudou | Capability C que virou padrão maduro precisa migrar para A; ninguém percebe |

## 6. CONEXÕES

- 🔗 [Manifesto dos Invariantes](../01-manifesto/L1-C00M-manifesto-invariantes.md)
- 🔗 [Cap 13 — MCP](../02-capitulos/L1-C13-mcp.md)
- 🔗 [Cap 33 (L2) — Claude + MCP](../../Livro-2-Dominando-Claude/02-capitulos/L2-C33-claude-mcp.md)
- 🔗 [Cap 34b (L2) — Connectors, Dispatch, Routines](../../Livro-2-Dominando-Claude/02-capitulos/L2-C34b-connectors-dispatch-routines.md)
- 🔗 [F3 — AGENTE-PROP](L1-F3-agente-prop.md) (níveis de autonomia limitam permissões por MCP)
- 🔗 [F6 — GOV-INDELEGÁVEL](L1-F6-gov-indelegavel.md) (cada MCP tem dono nominal)

---

> *"Tool ad-hoc é dívida técnica disfarçada. MCP público sem auditoria é risco regulatório disfarçado. MCP próprio sem dono é teatro disfarçado. O quadrante decide qual disfarce você vai vestir."*



<div class="page-break"></div>


# FRAMEWORK F6 — GOV-INDELEGÁVEL
## Governança de IA aplicada — 3 camadas × 10 controles

---

> 🧭 **Invariante-mãe:** **Invariante 8 — Responsabilidade Indelegável** — *"A IA executa; a responsabilidade tem sempre um nome humano."*
> Capítulo-âncora: [Cap 42 — Governança de IA corporativa](../02-capitulos/L1-C42-governanca.md). Aprofundamento: [Cap 37 — Segurança](../02-capitulos/L1-C37-seguranca.md). Aplicação Claude: [Cap 30 (L2) — Enterprise](../../Livro-2-Dominando-Claude/02-capitulos/L2-C30-enterprise.md).

---

## 1. OBJETIVO

Construir governança de IA que **protege o negócio sem virar teatro de compliance**. Saída: Caderno de Governança v1 com política em ≤6 páginas + RACI assinado + plano de incidente testado em simulado + matriz de maturidade dos 10 controles.

## 2. FUNCIONAMENTO

Governança real opera em **três camadas que precisam fechar**, sustentadas por **dez controles canônicos**.

### As 3 camadas

| Camada | O que cobre | Quem responde |
|--------|-------------|----------------|
| **Técnica** | Acesso, auditoria imutável, kill switch, rollback, observability, evals em CI | CTO / Head de tecnologia |
| **Operacional** | RACI, AUP, política de incidentes, runbooks, treinamento, postmortem | Head de operações / VP de produto |
| **Executiva** | AI Council, política pública, accountability nominal, comitê de ética, comunicação com conselho | CEO / Diretor com mandato |

Cada camada tem dono nominal. Sem nome em cada camada, governança não fecha — vira documento publicado sem prática efetiva.

### Os 10 controles canônicos

| # | Controle | Camada |
|---|----------|--------|
| 1 | Controle de acesso por feature, por usuário, por papel | Técnica |
| 2 | Auditoria imutável de cada chamada de IA em produção | Técnica |
| 3 | Kill switch testado por tool, por agente, por modelo, por feature | Técnica |
| 4 | Rollback testado mensalmente em staging | Técnica |
| 5 | Observability com tracing (pilares 1 de LLMOps) | Técnica |
| 6 | Evals em CI com critério de bloqueio explícito | Técnica |
| 7 | RACI de IA assinado pela diretoria | Operacional |
| 8 | Política de Uso Aceitável (AUP) publicada e treinada | Operacional |
| 9 | Política de incidentes testada em simulado trimestral | Operacional |
| 10 | AI Council com mandato e cadência fixa | Executiva |

### Mecânica de aplicação

1. **Diagnóstico de maturidade.** Pontuar cada um dos 10 controles em escala 0-4 (inexistente, declarado, implementado, auditado, melhoria contínua).
2. **Identificação de buracos.** Controles em maturidade ≤1 são prioridade. Maturidade 2 sem auditoria é teatro.
3. **Plano em 90/180/365 dias.** Cada controle com maturidade-alvo, dono, gate de promoção.
4. **Caderno em ≤6 páginas.** Política + RACI + plano de incidente + matriz de maturidade.
5. **Revisão trimestral.** Maturidade atualizada, plano ajustado, incidentes do trimestre integrados.

## 3. OUTPUT

| Campo | Conteúdo |
|-------|----------|
| Política em ≤6 páginas | AUP + princípios + categorias de safety |
| RACI assinado | 8 papéis × 12 decisões mínimas |
| Plano de incidente testado | Severidades, comunicação, postmortem |
| Matriz de maturidade | 10 controles em escala 0-4, com meta de 90/180/365 dias |
| Donos nominais por camada | Técnica, Operacional, Executiva |
| Cadência de revisão | Trimestral, com pauta fixa |

## 4. EXEMPLO DE USO — SEGURADORA APÓS INCIDENTE (CENÁRIO ILUSTRATIVO)

Seguradora BR de médio porte, após multa ANPD por negação automatizada de cobertura sem trilha de auditoria.

**Diagnóstico de maturidade pré-incidente:**

| Controle | Maturidade |
|----------|-----------|
| 1 Acesso | 1 (declarado) |
| 2 Auditoria | 0 |
| 3 Kill switch | 0 |
| 4 Rollback | 1 |
| 5 Observability | 1 |
| 6 Evals em CI | 0 |
| 7 RACI | 0 (implícito, "o time de dados cuida") |
| 8 AUP | 0 |
| 9 Política de incidentes | 1 (documento sem teste) |
| 10 AI Council | 0 |

**Plano após incidente (90 dias):**

- Controle 7 (RACI): assinado pela diretoria com 8 papéis (CTO, Head Dados, DPO, Head Compliance, Diretor Operações, Diretor Comercial, Diretor Jurídico, CEO) × 12 decisões (modelo, prompt, dataset, agente, MCP, tool, incidente SEV-1, política, etc.)
- Controle 8 (AUP): 4 páginas, publicada, treinada em todo o time em ≤30 dias
- Controle 2 (Auditoria): retenção 5 anos para decisão automatizada com efeito jurídico
- Controle 6 (Evals em CI): golden set inicial para classificação de cobertura
- Controle 9 (Incidente): simulado trimestral com cronômetro
- Controle 10 (AI Council): mandato escrito, cadência mensal nos primeiros 6 meses

**Após 7 meses:** matriz com 8 de 10 controles em maturidade ≥3. Multa não voltou. Seguradora apresenta caso em comitê setorial como exemplo de remediação.

## 5. ANTI-PADRÕES

| Anti-padrão | Por que mata |
|-------------|--------------|
| Política publicada, processo inexistente, prática divergente | Governança morta no PDF; quando o incidente vier, o documento será exposto como teatro |
| RACI implícito ("o time X cuida") | Sem nome, ninguém responde. Inv. 8 viola por omissão |
| AI Council sem mandato | Vira reunião de tom sem decisão; conselho fica simbólico |
| Política de incidente nunca testada em simulado | Na hora do incidente, descobre-se que não funciona |
| Auditoria interna sem auditoria externa periódica | Auto-auditoria tende a falsa segurança |
| "Vamos terceirizar o problema" | Compliance terceirizado vira processo terceirizado; accountability não terceiriza |

## 6. CONEXÕES

- 🔗 [Manifesto dos Invariantes](../01-manifesto/L1-C00M-manifesto-invariantes.md)
- 🔗 [Cap 37 — Segurança](../02-capitulos/L1-C37-seguranca.md)
- 🔗 [Cap 41 — Alignment](../02-capitulos/L1-C41-alignment.md) (sustenta safety em produto)
- 🔗 [Cap 42 — Governança](../02-capitulos/L1-C42-governanca.md)
- 🔗 [Cap 29 (L2) — Team](../../Livro-2-Dominando-Claude/02-capitulos/L2-C29-team.md), [Cap 30 (L2) — Enterprise](../../Livro-2-Dominando-Claude/02-capitulos/L2-C30-enterprise.md)
- 🔗 [F1 — DECID-IA](L1-F1-decid-ia.md) (Pergunta 5 — Responsabilidade — alimenta o RACI)
- 🔗 [F3 — AGENTE-PROP](L1-F3-agente-prop.md) (níveis de autonomia precisam de governança proporcional)

---

> *"Governança não é documento publicado, é controle aplicado. Quem confunde, descobre na multa ou no processo."*



<div class="page-break"></div>


# FRAMEWORK F7 — COMPOSTO-3T
## Adoção corporativa pelos 3 vetores arquiteturais de custo composto

---

> 🧭 **Invariante-mãe:** **Invariante 5 — Custo Composto** — *"Trivial é o preço do token; o que quebra o orçamento é quantas vezes você o paga."*
> Invariante secundário: **Inv. 9 — Operador** (operação madura aplica em ordem certa).
> Capítulo-âncora: [Cap 36 — Economia de Tokens em profundidade](../02-capitulos/L1-C36-economia-tokens.md). Fundamento: [Cap 03 — Tokens](../02-capitulos/L1-C03-tokens.md) e [Cap 07 — Memória](../02-capitulos/L1-C07-memoria.md).

---

## 1. OBJETIVO

Atacar o orçamento real de IA na empresa pelo lado certo — **arquitetural** — não pelo lado errado — **textual**. Garantir que esforço de otimização vai onde o termo composto escala, não onde aparece o termo trivial.

## 2. FUNCIONAMENTO

A fórmula do Custo Composto:

```
Custo Total = Σ (tokens_in × preço_in + tokens_out × preço_out)
              × chamadas
              × redundância
              × tier
```

O framework opera em **três alavancas arquiteturais** (os "3T"), em ordem fixa de impacto e de risco.

### T1 — Tier de modelo

**O que é:** rotear cada chamada ao **modelo mais barato suficiente** para a qualidade exigida.

**Mecânica.**
- Classificador leve (Haiku-like) na entrada da pipeline decide rota.
- Tarefas estruturadas, classificação binária, extração de campo → tier pequeno (Haiku).
- Tarefas de razão balanceada, sumarização, resposta em escala → tier balanceado (Sonnet).
- Tarefas críticas de razão profunda, código complexo, escrita executiva → tier premium (Opus).

**Implementação.** 1-3 semanas para versão inicial; classificador é prompt simples ou pequeno modelo dedicado.

**Economia típica observada.** 30% a 60% do gasto total na primeira virada de roteamento, em operações que usavam premium para tudo.

**Risco.** Médio. Exige golden set para mostrar que tier pequeno entrega qualidade equivalente (Invariante 7 sustenta a decisão).

### T2 — Topologia de chamada

**O que é:** reduzir **redundância** dentro do fluxo, sem mexer em tier nem em prompt.

**Mecânica.**
- **Prompt caching** para prefixos estáveis (system prompt, instruções recorrentes).
- **Batching** de chamadas independentes.
- **Eliminação de loops** de agente que reconsultam o mesmo dado.
- **Circuit breaker** contra runaway loops por usuário ou sessão.
- **Tool design** que devolve em uma chamada o contexto que o próximo passo precisa.

**Implementação.** 2-4 semanas para o conjunto inicial; depende do quanto a arquitetura já está modular.

**Economia típica observada.** 20% a 50% adicional, após T1.

**Risco.** Médio-alto. Mudanças em topologia podem introduzir regressão se o pilar 1 de LLMOps (tracing) e o pilar 3 (deploy progressivo) não estiverem maduros.

### T3 — Tamanho de contexto

**O que é:** podar agressivamente o que entra no contexto da chamada.

**Mecânica.**
- **RAG enxuto:** top-k baixo após reranking; chunks compactos; descarte de duplicidade.
- **Compressão de histórico:** sumarização hierárquica de turnos antigos.
- **Expiração de memória:** turnos com idade ou irrelevância vão para sumário ou são descartados.
- **Bibliografia controlada:** evitar inflar context com documentação que não está sendo consultada.

**Implementação.** 1-3 semanas, depende de quanto havia de "carona" no contexto.

**Economia típica observada.** 15% a 40% adicional, após T1 e T2.

**Risco.** Baixo. Exige eval cuidadoso para detectar regressão de qualidade por contexto insuficiente.

### Ordem de aplicação

Mexer em T3 antes de T1 é o erro mais comum, porque T3 é o mais visível ("vamos cortar palavras do prompt"). Visível e marginal. A ordem é T1 → T2 → T3.

## 3. OUTPUT

| Campo | Conteúdo |
|-------|----------|
| Análise atual de custo por feature | Atribuição via Pilar 5 de LLMOps |
| Identificação do componente que mais escala | Tokens, chamadas, redundância ou tier |
| T1 plan | Quais features migrar de tier, em que ordem, com qual golden set |
| T2 plan | Onde implementar caching, batching, circuit breaker |
| T3 plan | RAG enxuto, compressão de histórico, expiração de memória |
| Meta de economia | % por T, por feature, por trimestre |
| Eval que sustenta cada mudança | Inv. 7 — sem eval, não muda |

## 4. EXEMPLO DE USO — PÓLICE.IO PÓS-INCIDENTE

Marketplace BR de seguros, após o incidente do loop com cartão de crédito (Cap 40).

**Diagnóstico inicial.**
- Fatura mensal: R$ 142 mil
- Atribuição por feature: 87% concentrado no agente de cotação
- Componente que mais escala: **redundância** (loop de agente reconsultando 7 seguradoras)
- Tier dominante: 92% das chamadas vão para Opus, mesmo em classificação intermediária

**Plano T1.** Migrar classificação de intent (~38% do volume) para Haiku. Migrar geração de resposta padrão (~24%) para Sonnet. Manter Opus apenas para casos com sinal de complexidade alta (~15%).

**Plano T2.** Prompt caching para system prompt das cotações (eliminar 6.4kb por chamada). Circuit breaker de 5 chamadas Opus por sessão. Reescrita do agente para não reconsultar seguradoras em mudança de campo não-crítico (resolve o bug raiz do incidente).

**Plano T3.** RAG enxuto de documentação de produtos (top-3 chunks após reranking, em vez de top-20). Sumarização hierárquica em sessões com mais de 6 turnos.

**Resultado em 3 meses.** R$ 142 mil → R$ 47 mil, com volume servido maior. Distribuição final: 60% Haiku, 28% Sonnet, 12% Opus.

## 5. ANTI-PADRÕES

| Anti-padrão | Por que mata |
|-------------|--------------|
| Otimizar tamanho do prompt enquanto agente loopa no Opus | Esforço no termo trivial, fatura segue subindo |
| Usar premium para classificação binária "por garantia" | 30-50× o preço para entregar a mesma qualidade do pequeno |
| Começar por T3 porque é visível | T1 entrega ordem de magnitude a mais |
| Migrar tier sem golden set | Sem eval, regressão silenciosa em subgrupo |
| Ignorar atribuição de custo por feature | Sem atribuição, decisão de corte é tiro no escuro |
| Cortar caching para "simplificar" | Caching é o ROI mais alto de T2; descartar é multiplicar fatura |

## 6. CONEXÕES

- 🔗 [Manifesto dos Invariantes](../01-manifesto/L1-C00M-manifesto-invariantes.md)
- 🔗 [Cap 03 — Tokens](../02-capitulos/L1-C03-tokens.md), [Cap 04 — Janela](../02-capitulos/L1-C04-janela-de-contexto.md), [Cap 07 — Memória](../02-capitulos/L1-C07-memoria.md)
- 🔗 [Cap 11 — Context Engineering](../02-capitulos/L1-C11-context-engineering.md)
- 🔗 [Cap 36 — Economia de Tokens](../02-capitulos/L1-C36-economia-tokens.md) (capítulo-âncora completo)
- 🔗 [Cap 40 — LLMOps Pilar 5](../02-capitulos/L1-C40-llmops.md) (atribuição de custo sustenta o framework)
- 🔗 [F2 — ENCAIXE-5](L1-F2-encaixe-5.md) (decisão de tier do F2 alimenta o T1 do F7)
- 🔗 [F8 — EVAL-PIRÂMIDE](L1-F8-eval-piramide.md) (eval sustenta cada virada de T1)

---

> *"Preço por token é o termo trivial da fórmula. Quem otimiza só ali está mexendo onde menos dói. Os 3T mexem onde dói de verdade."*



<div class="page-break"></div>


# FRAMEWORK F8 — EVAL-PIRÂMIDE
## Pirâmide de Evals por criticidade

---

> 🧭 **Invariante-mãe:** **Invariante 7 — Termômetro** — *"IA sem eval é fé, não engenharia."*
> Invariantes secundários: **Inv. 1** (Plausibilidade — eval comportamental detecta o que o modelo finge saber), **Inv. 8** (Responsabilidade — eval sustenta accountability técnica).
> Capítulo-âncora: [Cap 39 — Evals](../02-capitulos/L1-C39-evals.md). Aplicação operacional: [Cap 40 — LLMOps](../02-capitulos/L1-C40-llmops.md). Aplicação comportamental: [Cap 41 — Alignment](../02-capitulos/L1-C41-alignment.md).

---

## 1. OBJETIVO

Decidir **quanto investir em cada camada de eval**, em função do risco da tarefa e do custo de cada camada. Garantir que nenhum sistema entre em produção sem cobertura mínima e que recursos de eval mais caros (humano especialista) sejam alocados onde fazem diferença.

## 2. FUNCIONAMENTO

Hierarquia de três camadas verticais + uma faixa transversal. Cada camada cobre um percentual diferente da carga e tem custo diferente.

### Base — Determinística

**O que mede.** Estrutura da saída, formato, campos críticos, presença de elementos obrigatórios.

**Técnicas.** Schema validation, exact match em campos críticos, regex para padrões obrigatórios, validações estruturais.

**Cobertura.** 100% das chamadas, em CI antes do merge e em produção como primeiro filtro.

**Custo.** Muito baixo. Implementação leva horas a poucos dias.

**Detecta.** Regressões grosseiras (formato quebrado, campo faltante, alucinação estrutural).

### Meio — Golden Set + LLM-as-judge calibrado

**O que mede.** Qualidade semântica contra rubrica explícita, faithfulness, relevância, completude.

**Técnicas.** Golden set fixo com gabarito + LLM-as-judge aplicando rubrica calibrada contra humano em pelo menos 30 itens. Juiz diferente do gerador. Ensemble em decisões críticas.

**Cobertura.** 30% a 80% das chamadas conforme criticidade.

**Custo.** Médio. Implementação leva 1-4 semanas. Manutenção exige revisão do golden set e recalibração mensal do juiz.

**Detecta.** Regressão de qualidade que escapa da base. Cobre tarefas onde exact match não funciona (geração aberta).

### Topo — Rubrica humana especialista

**O que mede.** Nuances específicas de domínio que LLM-as-judge não capta.

**Técnicas.** Revisão de amostra por especialista do domínio, em release crítico, em auditoria mensal ou trimestral, em incidente sob investigação.

**Cobertura.** 5% a 15% da carga, por amostra.

**Custo.** Alto. Demanda especialista do domínio em horas dedicadas.

**Detecta.** Erros sutis específicos do domínio. Calibra o juiz LLM contra o critério humano.

### Transversal — Adversarial e segurança

**O que mede.** Casos que sabidamente quebram o sistema — jailbreak, prompt injection, conteúdo proibido, sycophancy, viés, honestidade de citação, over-refusal, calibração de incerteza.

**Técnicas.** Conjunto adversarial separado, renovado a cada trimestre. Casos vindos de produção (incidentes anteriores) e de literatura (HarmBench, JailbreakBench, BBQ).

**Cadência.** Mensal por padrão. Bloqueia release crítico se regredir.

**Custo.** Médio-alto. Exige curadoria contínua.

**Detecta.** Falhas comportamentais que as camadas verticais não cobrem por design.

## 3. OUTPUT

| Campo | Conteúdo |
|-------|----------|
| Mapa de cobertura por camada | % atual em base, meio, topo, adversarial |
| Mapa-meta em 90 dias | % desejado por camada |
| Golden set inicial | 30-50 casos representativos com gabarito |
| Rubrica de LLM-as-judge calibrada | 4-6 critérios objetivos, com correlação alvo ≥0,7 contra humano |
| Adversarial set inicial | 20+ casos por categoria de segurança crítica |
| Política de bloqueio em CI | Delta que bloqueia merge, delta que alerta, delta que passa |
| Cadência de revisão | Golden set: trimestral. Adversarial: mensal. Calibração de juiz: mensal. |

## 4. EXEMPLO DE USO — ATLAS STRATEGY PÓS-INCIDENTE

Consultoria estratégica BR, após o incidente dos números trocados no relatório (Cap 39).

**Estado anterior.** Vibe-eval (3 sócios na sexta). 0% de cobertura em qualquer camada da pirâmide.

**Plano de pirâmide v1:**

| Camada | Cobertura | Conteúdo |
|--------|-----------|----------|
| Base | 100% | Schema validation do relatório (seções obrigatórias, números formatados, citação presente) |
| Meio | 100% | Golden set de 80 relatórios reais com gabarito de números e tese. LLM-as-judge com rubrica de faithfulness numérico (4 critérios). Juiz = Claude Opus (gerador = Sonnet). Calibrado contra 3 sócios em 30 itens, correlação 0,82 |
| Topo | 10% | Auditoria semanal de partner em release crítico. Trimestralmente, auditoria externa por consultor sênior independente |
| Adversarial | mensal | 30 casos: paciente com sycophancy (cliente forçando conclusão), prompt injection via dado de cliente, números invertidos sutilmente, citação de fonte inexistente, omissão de risco crítico |

**Política de bloqueio.** Faithfulness numérico ≥0,95 (delta máximo 1 ponto contra baseline). Adversarial: zero passagens. Caso falhe, merge bloqueado automaticamente.

**Resultado em 6 meses.** Regressões silenciosas zeraram. Tempo de revisão humana caiu 50% — gate filtra ruído antes de o humano ver.

## 5. ANTI-PADRÕES

| Anti-padrão | Por que mata |
|-------------|--------------|
| Construir o topo da pirâmide sem a base | Humano revisa muito, identifica pouco, time não escala |
| LLM-as-judge sem calibração contra humano | Viés institucionalizado; auto-validação inflada |
| Golden set único, sem renovação | Vira folclore que não bate com produção atual |
| Adversarial só de literatura, sem casos de produção | Cobertura teórica, falhas reais escapam |
| Métrica única agregada (acurácia média) | Esconde regressão por subgrupo crítico |
| "Eval é caro" como justificativa para não fazer | Regressão silenciosa é mais cara, descoberta tarde |

## 6. CONEXÕES

- 🔗 [Manifesto dos Invariantes](../01-manifesto/L1-C00M-manifesto-invariantes.md)
- 🔗 [Cap 06 — RAG](../02-capitulos/L1-C06-rag.md) (RAGAS aplicado ao meio da pirâmide)
- 🔗 [Cap 08 — Fine-tuning](../02-capitulos/L1-C08-fine-tuning.md) (decisão sustentada por golden set)
- 🔗 [Cap 39 — Evals](../02-capitulos/L1-C39-evals.md) (capítulo-âncora completo)
- 🔗 [Cap 40 — LLMOps](../02-capitulos/L1-C40-llmops.md) (pilares 1, 2 e 3 sustentam o framework)
- 🔗 [Cap 41 — Alignment](../02-capitulos/L1-C41-alignment.md) (adversarial cobre 8 safety categories)
- 🔗 [Cap 42 — Governança](../02-capitulos/L1-C42-governanca.md) (eval em CI é controle técnico canônico)
- 🔗 [F1 — DECID-IA](L1-F1-decid-ia.md) (Pergunta 4 — linha de medição — alimenta o plano de pirâmide)
- 🔗 [F3 — AGENTE-PROP](L1-F3-agente-prop.md) (níveis de autonomia exigem cobertura proporcional na pirâmide)

---

> *"A pirâmide é barata na base, cara no topo. Quem inverte paga muito sem cobrir bem. Quem ignora paga em incidente."*



<div class="page-break"></div>


# FRAMEWORK F9 — ROTA-DUPLA
## Trilha de aprendizado e operação por camada (padrão × número)

---

> 🧭 **Invariante-mãe:** **Invariante 3 — Camada Dupla** — *"Decore o padrão, consulte o número."*
> Capítulo-âncora: [Cap 01 — O que é IA](../02-capitulos/L1-C01-o-que-e-ia.md) e o **[Apêndice Vivo (J)](../../Livro-2-Dominando-Claude/04-apendices/L2-APX-J-apendice-vivo.md)**.

---

## 1. OBJETIVO

Orientar o estudo e a operação do leitor distinguindo, em cada peça de conhecimento, o que é **padrão (decora)** do que é **número (consulta)**. Garantir que tempo de aprendizado vá para o que envelhece bem, e que tempo de consulta vá para o que muda — com fonte e data.

## 2. FUNCIONAMENTO

Toda peça de conhecimento sobre IA pertence a **uma de duas trilhas** com cadências distintas de revisitação.

### Trilha Padrão (Padrão durável)

**O que vai aqui.**
- Os 9 Invariantes da IA
- Os 9 Frameworks proprietários (F1-F9)
- Capítulos conceituais (Cap 01, 02, 03, 04, 05, 06, 07, 08, 09, 10, 11, 12, 13, 14)
- Anatomia de eval, LLMOps, Alignment, Governança (Caps 39, 40, 41, 42)
- Tradeoffs canônicos (Cap 43)
- Padrões arquiteturais (RAG, agente, MCP, fine-tuning)

**Cadência de revisitação.** Trimestral para revisão completa. Anual para releitura focada.

**Como armazena.** Cabeça do operador. Cartaz dos Invariantes (Apêndice M) na parede. Caderno do Operador como notas pessoais.

### Trilha Número (Número volátil)

**O que vai aqui.**
- Versões correntes de modelos (Anthropic, OpenAI, Google, open weights)
- Preços por milhão de tokens
- Posições em benchmark da rodada (SWE-bench, GPQA, OSWorld, etc.)
- Limites correntes de janela de contexto
- Capacidades novas de produto (Claude Skills X.Y, Connectors, etc.)
- Lista corrente de repositórios GitHub relevantes
- Datas de regulação aplicável (versões de LGPD, AI Act, NIST AI RMF)

**Cadência de revisitação.** Mensal para conferência. Antes de cada decisão que use o número como insumo.

**Como armazena.** **Apêndice Vivo (J)** no Livro 2, datado, com fonte por linha, atualizado fora do livro.

### Mecânica de aplicação

1. **Diagnóstico.** Listar o que se sabe sobre IA hoje. Para cada item, classificar: padrão ou número?
2. **Migração.** Item classificado errado vai para a trilha certa.
3. **Cadência de revisão.** Padrão entra em revisão trimestral. Número fica disponível para consulta sob demanda.
4. **Antes de cada decisão.** Identificar quais padrões e quais números a decisão precisa. Buscar cada um na trilha certa.

## 3. OUTPUT

| Campo | Conteúdo |
|-------|----------|
| Mapa pessoal de padrões dominados | Os 9 Invariantes, frameworks F1-F9, conceitos centrais |
| Mapa pessoal de gaps de padrão | O que ainda precisa ser estudado |
| Calendário de revisão de padrão | Trimestral e anual |
| Bookmark do Apêndice Vivo | Para consulta de número |
| Calendário de checagem do Apêndice Vivo | Mensal por padrão; antes de cada decisão crítica |

## 4. EXEMPLO DE USO — CTO QUE PRECISA DECIDIR MODELO

Cenário: CTO de SaaS B2B precisa decidir migração de modelo para feature de copiloto in-product.

**Identificação do que a decisão precisa.**

| Insumo | Trilha | Onde buscar |
|--------|--------|-------------|
| Quais são os eixos relevantes para escolha de modelo? | Padrão | F2 ENCAIXE-5 (Trilha Padrão) |
| Como pontuar a tarefa nos eixos? | Padrão | Cap 15 + F2 |
| Qual a liderança corrente em "razão complexa" e "código"? | Número | Apêndice Vivo (J) — SWE-bench Verified, GPQA |
| Qual o preço por milhão de tokens hoje? | Número | Apêndice Vivo (J) — pricing pages |
| Qual a filosofia de alignment do vendor? | Padrão | Cap 41 (depende pouco da versão) |
| Qual a janela de contexto corrente do modelo X? | Número | Apêndice Vivo (J) |

A decisão é informada por padrão (F2 + Cap 41) e número (Apêndice Vivo). O padrão vive na cabeça do CTO; o número é conferido na semana da decisão.

**Em 6 meses,** a fronteira muda. Versões novas saem. Mas o padrão F2 continua válido. O CTO refaz o exercício, busca o novo número no Apêndice Vivo atualizado, e a decisão é consciente em vez de reativa.

## 5. ANTI-PADRÕES

| Anti-padrão | Por que mata |
|-------------|--------------|
| Memorizar versão e benchmark "porque é importante" | Memória vira passivo no próximo release |
| Não memorizar o padrão "porque é teórico" | Sem padrão, decisão fica refém do marketing do vendor |
| Achar que o livro tem tudo | Livro tem o padrão; Apêndice Vivo tem o número |
| Confiar em memória para o número | Modelo X mudou de versão; preço caiu 40%; benchmark líder é outro |
| Ignorar o padrão porque "é óbvio" | Operadores que conhecem o óbvio cometem 80% dos erros do mercado |
| Atualizar o padrão na mesma cadência do número | Tempo gasto reescrevendo o que não mudou |

## 6. CONEXÕES

- 🔗 [Manifesto dos Invariantes](../01-manifesto/L1-C00M-manifesto-invariantes.md)
- 🔗 [Cap 01 — O que é IA](../02-capitulos/L1-C01-o-que-e-ia.md)
- 🔗 [Cap 15 — Comparação de modelos](../02-capitulos/L1-C15-comparacao-modelos.md)
- 🔗 [Apêndice Vivo (J)](../../Livro-2-Dominando-Claude/04-apendices/L2-APX-J-apendice-vivo.md)
- 🔗 [Apêndice M — Manifesto de bolso](../04-apendices/L1-APX-M-manifesto-bolso.md)
- 🔗 [Apêndice B — Mapa Mental Geral](../04-apendices/L1-APX-B-mapa-mental.md)
- 🔗 Todos os frameworks F1-F8 (cada um opera um padrão)

---

> *"Decore o padrão, consulte o número. Misturar as duas trilhas é envelhecer junto com o release."*
