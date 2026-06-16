# F4 — Engenharia de Prompt Estendida
## Engenharia de prompts pelas extremidades

## 1. OBJETIVO

Escrever prompts de produção que respeitam a física de atenção (Invariante 2) e que separam, dentro do prompt, o que é padrão estável do que é número volátil (Invariante 3). Garantir que a regra crítica nunca fique no centro do prompt, e que cada bloco esteja na posição em que será efetivamente seguido.

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

**Prompts multimodais:** input visual (imagem, PDF, tabela, gráfico) vai no Bloco 3, junto ao contexto textual, nunca no Bloco 5 (que é exclusivo do texto do usuário). A Constituição no Bloco 2 deve cobrir explicitamente como tratar o conteúdo visual — ex.: "Citar sempre página e número de figura ao referenciar dados de documento."

**Quando o Bloco 3 cresce demais:** aplicar T3 do F7 (RAG enxuto, compressão de histórico, expiração de memória). A regra de posição é inegociável: o Bloco 3 cresce até o ponto em que o Bloco 4 ainda está na posição forte de atenção. Se o Bloco 4 migrar para o meio do prompt por crescimento do Bloco 3, a estrutura quebrou — comprimir o Bloco 3 antes de adicionar contexto.

### Bloco 4 — Instrução operacional + formato esperado (imediatamente antes da pergunta viva)

Curto. Posição forte (a segunda mais atendida, depois da abertura). Repete o crítico das regras na linguagem da tarefa específica, e define o formato exato da saída esperada.

> *Exemplo:* "Responda em pt-BR formal, máximo três parágrafos, sem expressões coloquiais. Cite a tool consultada quando aplicável. Se não conseguir resolver, escale para humano com sumário em 3 bullets."

### Bloco 5 — Pergunta viva / input do usuário (última posição)

Sempre na última posição. Sempre. Sanitizada contra prompt injection — tentativa do usuário de reescrever as instruções do sistema via campo de input (equivalente a um cliente bancário tentando mudar as regras do banco no campo "motivo da transferência").

**Técnicas básicas de sanitização:** (1) delimitar o input do usuário com marcadores XML fixos reconhecidos pela constituição, ex: `<pergunta_usuario>...</pergunta_usuario>`; (2) nunca interpolar input do usuário diretamente em strings de sistema sem delimitação; (3) incluir no adversarial set do F8 casos de prompt injection via input do usuário. Ver Cap 19 para tratamento completo de segurança em prompt.

Esta é a única parte do prompt que muda em cada chamada — a Camada Dupla materializada: número volátil.

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
| Enterrar regra crítica no parágrafo 40 de prompt longo | Invariante 2: atenção decai no meio; regra ignorada silenciosamente |
| Colocar a pergunta no início, antes do contexto | Modelo responde ao input sem ter visto o contexto |
| Constituição não versionada (string no código) | Sem rastreabilidade de mudança; vira buraco de governança |
| Misturar regra inviolável com sugestão estilística | Modelo perde hierarquia; quebra ambas com a mesma facilidade |
| Não reiterar o crítico no bloco 4 | Em prompts longos, o final domina; sem reiteração, regra do topo enfraquece |
| Não sanitizar a pergunta viva | Prompt injection via input do usuário sobrescreve a constituição |

## 6. CONEXÕES

- 🔗 Manifesto dos Invariantes
- 🔗 Cap 04 — Janela de contexto
- 🔗 Cap 09 — Engenharia de prompt
- 🔗 Cap 11 — Context Engineering
- 🔗 Cap 20 — Projects (L2) — *Projects materializam o bloco de constituição*
- 🔗 Cap 31 — Skills (L2) — *Skills versionam o bloco de constituição como ativo*
- 🔗 Pirâmide da Avaliação — *o adversarial set inclui prompt injection contra a pergunta viva*

---

> *"A regra que importa não vai no meio do prompt. Vai na primeira posição forte e na última. Quem coloca no centro está rezando para a atenção do modelo, e a atenção não está olhando."*
