---
title: "Inteligência Aumentada"
lang: pt-BR
---



<div class="page-break"></div>


# APÊNDICE A — GLOSSÁRIO COMPLETO
## *Vocabulário canônico de Inteligência Aumentada*

> Glossário organizado por categoria. Termos próprios da obra marcados com **★** (sistema proprietário) ou **◆** (uso técnico canônico). Termos de mercado em uso recorrente sem marcação.

---

## I. INVARIANTES E SISTEMA DA OBRA (★)

**Camada-mãe.** ★ Os 9 Invariantes da IA, princípios duráveis que sustentam toda a obra.

**Camada Dupla.** ★ Invariante 3: separação entre padrão durável (na cabeça) e número volátil (em apêndice datado).

**Custo Composto.** ★ Invariante 5: a multiplicação tokens × chamadas × tier × redundância que escala em produção, não o preço por token isolado.

**Encaixe.** ★ Invariante 4: escolha de modelo por padrão de tarefa (5 eixos), não por liderança de benchmark da rodada.

**Extremidades.** ★ Invariante 2: regra de que atenção decai no meio do contexto e densidade de relevância vence volume bruto.

**Frame derivado.** ★ Framework prático (F1-F9) que opera um Invariante específico.

**Operador.** ★ Invariante 9: a IA multiplica competência e incompetência pelo mesmo fator.

**Plausibilidade.** ★ Invariante 1: o modelo entrega o plausível, não o verdadeiro.

**Responsabilidade Indelegável.** ★ Invariante 8: toda decisão de IA em produção tem único nome humano accountable.

**Autonomia Proporcional.** ★ Invariante 6: nível de agência é função da capacidade de medir e desfazer.

**Termômetro.** ★ Invariante 7: IA sem eval é fé, não engenharia.

**Validação UAU.** ★ Critério objetivo de fechamento de cada capítulo da obra; 5 dimensões.

**Frameworks F1-F9.** ★ Sistema proprietário de 9 frameworks derivados dos Invariantes:
- F1 DECID-IA (Inv. 9), F2 ENCAIXE-5 (Inv. 4), F3 AGENTE-PROP (Inv. 6), F4 PROMPT-EXT (Inv. 2+3), F5 MCP-COBERTURA (Inv. 6+4), F6 GOV-INDELEGÁVEL (Inv. 8), F7 COMPOSTO-3T (Inv. 5+9), F8 EVAL-PIRÂMIDE (Inv. 7), F9 ROTA-DUPLA (Inv. 3).

---

## II. FUNDAMENTOS DE IA

**Agente.** ◆ Sistema de IA que recebe objetivo, decompõe em subtarefas, executa com ciclos de percepção-ação-reflexão, usa tools externas, até cumprir o objetivo. Diferente de chatbot: unidade de operação é a tarefa completa, não a resposta.

**AGI (Artificial General Intelligence).** Sistema de IA com capacidade equivalente a humana em qualquer tarefa cognitiva. Hoje, conceito disputado entre laboratórios.

**ASI (Artificial Superintelligence).** Sistema que excede capacidade humana em todos os domínios cognitivos.

**Atenção (mechanism).** ◆ Operação no transformer que decide quais tokens importam e quanto. Implementada via projeções Query/Key/Value e softmax.

**Benchmark.** Conjunto padronizado para medir capacidade. Exemplos: MMLU, GPQA, SWE-bench, HumanEval, ARC-AGI, OSWorld, Video-MME, HLE. Status corrente no Apêndice Vivo.

**Chain of Thought (CoT).** Técnica de prompt que induz o modelo a externalizar raciocínio passo a passo antes da resposta. Sobe acurácia em tarefas multipasso.

**Constitutional AI (CAI).** Técnica de alinhamento da Anthropic em que princípios em linguagem natural ("constituição") são aplicados por outro modelo IA para gerar feedback de treinamento.

**Context Engineering.** Disciplina que orquestra hierarquicamente o que entra no contexto do modelo (system prompt, memória, RAG, histórico) com caching e medição.

**Deep Learning.** Subcategoria de Machine Learning com redes neurais profundas.

**DPO (Direct Preference Optimization).** Substituto do PPO em RLHF; otimização direta sobre pares de preferência sem RM dedicado. Padrão de mercado em 2025-2026.

**Embedding.** ◆ Vetor numérico que representa significado em espaço contínuo. Permite busca semântica e RAG.

**Few-shot.** Técnica de prompt com poucos exemplos de input/output esperado.

**Fine-tuning.** Continuar treinando modelo pré-existente com dados específicos.

**Fundação (modelo).** Modelo base de larga escala usado como ponto de partida para aplicações.

**Hallucination.** Saída plausível mas factualmente incorreta. Decorre da arquitetura geradora.

**Instruction Tuning (SFT).** Fine-tuning supervisionado com pares (instrução, resposta) para ensinar o modelo a seguir instruções.

**Janela de contexto.** ◆ Limite de tokens que o modelo processa simultaneamente em uma chamada.

**LLM (Large Language Model).** Grande modelo de linguagem baseado em transformer e treinado em corpus massivo.

**Lost in the Middle.** ◆ Fenômeno documentado: atenção decai no meio de contextos longos. Base do Invariante 2.

**Multimodal.** Modelo que processa texto + imagem + áudio + vídeo nativamente.

**One-shot.** Prompt com um único exemplo.

**Open weights.** Modelo com pesos disponíveis para download (não confundir com open source completo, que inclui código e dados).

**Pré-treinamento.** Treinamento inicial do modelo em corpus não-rotulado.

**PPO (Proximal Policy Optimization).** Algoritmo clássico de RL usado no RLHF original; em substituição por DPO.

**Prompt.** Entrada de texto enviada ao modelo.

**Prompt engineering.** Disciplina de construir prompts profissionalmente.

**Prompt injection.** Ataque que insere instruções maliciosas via input ou dado de tool.

**RAG (Retrieval-Augmented Generation).** ◆ Arquitetura que combina recuperação externa de conhecimento com geração. Reduz alucinação, atualiza conhecimento sem retreinar.

**Reward Hacking.** Modelo aprende a soar bom para o RM, não a ser bom.

**RLHF (Reinforcement Learning from Human Feedback).** ◆ Alinhamento via comparação humana → modelo de recompensa → RL contra o RM.

**RLAIF.** Variante em que comparação é feita por outro modelo IA seguindo princípios.

**Sycophancy.** Modelo concorda com usuário porque foi premiado por isso em treinamento.

**System prompt.** Bloco persistente que precede inputs do usuário; define persona, regras, formato.

**Token.** ◆ Unidade fundamental que o modelo processa. Pode ser palavra, sub-palavra ou caractere.

**Tokenizer.** Sistema que converte texto em tokens.

**Transformer.** ◆ Arquitetura introduzida em 2017 (*Attention Is All You Need*) que mudou a IA moderna.

**Zero-shot.** Prompt sem exemplos; só instrução.

---

## III. EVALS (do Cap 39)

**Adversarial set.** ◆ Conjunto de casos que sabidamente quebram o sistema (jailbreak, injection, sycophancy, viés).

**Calibração de juiz.** Validação de LLM-as-judge contra humano em ≥30 itens; correlação alvo ≥0,7.

**Faithfulness.** Métrica de quão fiel a saída é a uma fonte (especialmente em RAG).

**Golden set.** ◆ Conjunto fixo de casos com gabarito que serve de referência estável para detectar regressão.

**LLM-as-judge.** ◆ Uso de LLM para avaliar saída de outro LLM segundo rubrica.

**Pirâmide de Evals.** ★ Framework F8: Base determinística + Meio com golden set e LLM-as-judge + Topo humano + Adversarial transversal.

**Regressão silenciosa.** Queda de qualidade que não aparece em métrica agregada mas existe em subgrupo.

**Rubrica.** Critério estruturado para julgamento (humano ou LLM-as-judge).

**Scorecard.** Comparação automatizada baseline × candidato em cada release.

**Vibe-eval.** Anti-padrão: rodar 5 casos manuais e decidir.

---

## IV. LLMOPS (do Cap 40)

**Canário.** ◆ Liberação progressiva de versão nova (1% → 10% → 50% → 100%) com gates.

**Circuit breaker.** Limite duro que para chamadas em condições anômalas (loop, custo, latência).

**Kill switch.** ◆ Capacidade de desligar tool/agente/modelo/feature em segundos.

**LLMOps.** ◆ Disciplina de operar IA em produção; difere de MLOps clássico.

**MTTR (Mean Time To Recovery).** Tempo médio entre detecção e retorno ao estado bom.

**OpenTelemetry GenAI.** Convenção semântica de OpenTelemetry para LLMs.

**Promptware como código.** Tratamento de prompt com PR, revisão, eval em CI.

**Rollback.** Reversão a estado conhecido seguro.

**SEV-1 a SEV-4.** Severidades de incidente, adaptadas a IA.

**Shadow mode.** Versão nova roda em paralelo, sem servir, para comparar com atual.

**Span × Trace × Session.** ◆ Modelo mental de observabilidade: span = chamada individual; trace = sequência relacionada; session = uso temporal.

**Tracing.** Instrumentação que registra cada chamada com input, output, latência, tokens, custo, tools.

**Versionamento de prompt.** Cada mudança de prompt vira release versionado com changelog.

---

## V. ALIGNMENT (do Cap 41)

**Helpful, Harmless, Honest.** ◆ Trilogia que sintetiza alinhamento (Anthropic).

**Interpretabilidade mecanicista.** ◆ Mapeamento dos circuitos internos do modelo que produzem comportamentos específicos.

**Mech Interp.** Abreviação de Interpretabilidade Mecanicista.

**Over-refusal.** Modelo recusa pedidos legítimos por excesso de cautela.

**Red-teaming.** Teste adversarial sistemático de comportamento problemático.

**Sandbagging.** Modelo finge ser menos capaz para escapar de avaliação.

**Sparse Autoencoders.** Técnica para identificar *features* legíveis em ativações.

---

## VI. GOVERNANÇA (do Cap 42)

**Accountable.** No RACI, quem responde pela decisão. Único nominal.

**AI Council.** Órgão executivo de governança de IA.

**AUP (Acceptable Use Policy).** Política de uso aceitável interna.

**Camadas de governança.** Técnica, Operacional, Executiva.

**Maturidade dos controles.** Escala 0-4 (inexistente, declarado, implementado, auditado, melhoria contínua).

**Política × Processo × Prática.** Três camadas que precisam fechar para governança não ser teatro.

**Postmortem sem culpa.** Investigação de incidente focada em processo, não em pessoa.

**RACI.** Matriz Responsible / Accountable / Consulted / Informed.

**Simulado.** Exercício programado de resposta a incidente, em staging.

---

## VII. ECOSSISTEMA CLAUDE (do Volume Vivo)

**Artifacts.** Painel lateral do Claude Web para conteúdo renderizado (código, documentos, diagramas).

**Claude Code.** Agente de programação CLI da Anthropic.

**Connectors.** Integrações nativas pré-instaladas no Claude.

**Constitutional AI.** Ver seção II.

**Cowork Mode.** Modo do Claude Desktop para colaboração assistida (research preview).

**Dispatch.** Mecanismo de invocação de workflows a partir de triggers externos.

**Haiku, Sonnet, Opus.** ◆ Três tiers canônicos da família Claude por encaixe.

**MCP (Model Context Protocol).** Padrão aberto para conectar modelos a tools e dados externos.

**Mythos Preview.** Linha experimental da Anthropic.

**Projects.** Workspace persistente do Claude com instruções, arquivos e histórico.

**Research.** Capacidade de pesquisa profunda multi-fonte do Claude.

**Routines.** Fluxos repetitivos nomeados no Claude Code.

**Scheduled Tasks.** Tarefas agendadas no Claude.

**Skills.** Comportamentos reutilizáveis e versionados encapsulados.

**Subagents.** Agentes especializados delegados por agente coordenador.

---

## VIII. CASOS BRASILEIROS DA OBRA (cenários ilustrativos)

**Atlas Strategy.** ★ Consultoria estratégica BR; caso de eval por incidente de relatórios (Cap 39, EC6).

**Banco Solar.** ★ Fintech BR; caso de atendimento híbrido por tier (EC1).

**EnterTech BR.** ★ Vendor B2B; caso de pré-vendas com Research (EC5).

**Instituto Norte.** ★ Educação executiva BR; caso de programa formativo (EC7).

**Métrica.io.** ★ SaaS BR de BI; caso de copiloto in-product (EC4).

**Pólice.io.** ★ Marketplace BR de seguros; caso de loop com cartão de crédito (Cap 40).

**RedeCasa.** ★ Varejo BR; caso de triagem de currículos com mitigação de viés (EC2).

**Triagem.Br.** ★ Healthtech BR; caso de alignment fraco em saúde (Cap 41).

**Vianna, Castro e Almeida.** ★ Banca de M&A BR; caso de DD assistida (EC3).

---

## IX. REGULAÇÃO E NORMAS

**AI Act.** Regulamentação europeia (UE 2024/1689).

**ANPD.** Autoridade Nacional de Proteção de Dados (Brasil).

**ISO/IEC 42001.** Sistema de gestão de IA (2023).

**LGPD.** Lei Geral de Proteção de Dados (Lei 13.709/2018), especialmente art. 20 (decisão automatizada).

**NIST AI RMF.** AI Risk Management Framework (NIST, 2023).

**PL de IA brasileiro.** Projeto de Lei sobre uso de IA, em tramitação. Status corrente no Apêndice Vivo.

---

🔗 [Apêndice B Mapa Mental](L1-APX-B-mapa-mental.md) · [Apêndice M Manifesto de bolso](L1-APX-M-manifesto-bolso.md) · [Apêndice Vivo (J)](../../Livro-2-Dominando-Claude/04-apendices/L2-APX-J-apendice-vivo.md)



<div class="page-break"></div>


# APÊNDICE B — MAPA MENTAL GERAL
## *Os 9 Invariantes da IA como esqueleto cognitivo da obra*

---

> Este mapa mental tem propósito específico. Não é índice (que é o sumário), nem é resumo (que é por capítulo). É a representação visual de como a obra se organiza **a partir dos Invariantes**, mostrando que cada capítulo, cada framework e cada estudo de caso é instância de um ou mais princípios da camada-mãe.

---

## ESTRUTURA EM CAMADAS

```
                    ┌────────────────────────────────┐
                    │   MODELOS PASSAM. MÉTODO FICA. │
                    └────────────────┬───────────────┘
                                     │
              ┌──────────────────────┴──────────────────────┐
              │      CAMADA-MÃE: OS 9 INVARIANTES           │
              │  (princípios duráveis, sistema citável)     │
              └──────────────────────┬──────────────────────┘
                                     │
              ┌──────────────────────┴──────────────────────┐
              │  CAMADA OPERACIONAL: 9 FRAMEWORKS (F1-F9)   │
              │  (decisão prática derivada de cada princípio) │
              └──────────────────────┬──────────────────────┘
                                     │
              ┌──────────────────────┴──────────────────────┐
              │  CAMADA APLICADA: CAPÍTULOS E ESTUDOS       │
              │  (instâncias técnicas e casos brasileiros)  │
              └─────────────────────────────────────────────┘
```

---

## A RODA DOS 9 INVARIANTES

```
                              ┌─────────────────────┐
                              │ 1. PLAUSIBILIDADE   │
                              │ "Plausível ≠ verdade"│
                              └──────────┬──────────┘
                                         │
       ┌─────────────────────┐           │           ┌─────────────────────┐
       │ 9. OPERADOR         │◀──────────┼──────────▶│ 2. EXTREMIDADES     │
       │ "Multiplica os dois"│           │           │ "Meio morre"        │
       └──────────┬──────────┘           │           └──────────┬──────────┘
                  │                      │                      │
                  │              ┌───────┴────────┐             │
                  │              │   FRASE-ÂNCORA │             │
                  │              │ "Modelos passam│             │
                  │              │  Método fica"  │             │
                  │              └───────┬────────┘             │
                  │                      │                      │
       ┌──────────┴──────────┐           │           ┌──────────┴──────────┐
       │ 8. RESPONSABILIDADE │◀──────────┼──────────▶│ 3. CAMADA DUPLA     │
       │ "Nome humano"        │           │           │ "Padrão × número"   │
       └──────────┬──────────┘           │           └──────────┬──────────┘
                  │                      │                      │
                  │                      │                      │
       ┌──────────┴──────────┐           │           ┌──────────┴──────────┐
       │ 7. TERMÔMETRO       │◀──────────┼──────────▶│ 4. ENCAIXE          │
       │ "Eval ou fé"        │           │           │ "Padrão da tarefa"  │
       └──────────┬──────────┘           │           └──────────┬──────────┘
                  │                      │                      │
                  └──────────────────────┼──────────────────────┘
                              ┌──────────┴──────────┐
                              │ 6. AUTONOMIA PROP.  │
                              └──────────┬──────────┘
                                         │
                              ┌──────────┴──────────┐
                              │ 5. CUSTO COMPOSTO   │
                              │ "Vezes que paga"    │
                              └─────────────────────┘
```

> 📊 **Diagrama B.1 — A Roda dos 9 Invariantes (versão SVG canônica)**
>
> *(SVG a produzir: `imagens/L1-APX-B-img-01-roda-invariantes-grande.svg`)*
>
> Versão de referência em alta arte, distribuível, com licença explícita.

---

## INVARIANTE × FRAMEWORK × CAPÍTULO-ÂNCORA

| Invariante | Framework derivado | Capítulo-âncora L1 | Aplicação L2 (Claude) | Estudo de caso L2 |
|-----------|---------------------|---------------------|------------------------|-------------------|
| 1 — Plausibilidade | Auditoria de honestidade no F8 | Cap 02, Cap 41 | Cap 22 Research, Cap 23 Web Search | EC2, EC3 |
| 2 — Extremidades | F4 PROMPT-EXT | Cap 04 | Cap 20 Projects, Cap 31 Skills | EC4, EC6 |
| 3 — Camada Dupla | F9 ROTA-DUPLA | Cap 01 + Apêndice Vivo (J) | Cap 31 Skills, Cap 17 Entendendo Claude | EC6 |
| 4 — Encaixe | F2 ENCAIXE-5 | Cap 15 | Cap 18 Modelos Claude | EC5 |
| 5 — Custo Composto | F7 COMPOSTO-3T | Cap 36 | Cap 18 Modelos, Cap 32 Subagents, Cap 34b Connectors | EC1 |
| 6 — Autonomia Proporcional | F3 AGENTE-PROP | Cap 12 + Cap 40 | Cap 24 Claude Code, Cap 28 Scheduled, Cap 32 Subagents, Cap 33 MCP | EC1, EC4 |
| 7 — Termômetro | F8 EVAL-PIRÂMIDE | Cap 39 | Cap 34 Executivos (OKRs) | EC4, EC7 |
| 8 — Responsabilidade Indelegável | F6 GOV-INDELEGÁVEL | Cap 42 + Cap 37 | Cap 29 Team, Cap 30 Enterprise, Cap 34 Executivos | EC1, EC2, EC3 |
| 9 — Operador | F1 DECID-IA | Cap 34 (L2) + Cap 44 | Toda a Parte 5 do Volume Vivo | Todos os EC |

---

## TRILHA TEMÁTICA × INVARIANTE

| Trilha | Invariante dominante | Capítulos sugeridos |
|--------|----------------------|---------------------|
| Entender LLMs profundamente | 1, 2, 3 | 02, 03, 04, 05, 09, 10, 11 |
| Decidir arquitetura de IA | 3, 4 | 06, 08, 13, 14, 15, 16, 43 |
| Construir agentes com critério | 6, 7 | 12, 32 (L2), 39, 40 |
| Medir e operar IA em produção | 6, 7, 8 | 14, 39, 40 |
| Governar IA corporativa | 8, 1 | 37, 41, 42 |
| Otimizar custo composto | 5 | 03, 04, 11, 36 |
| Liderar adoção executiva | 8, 9 | 15, 16, 34 (L2), 42, 43, 44 |
| Roadmap de longo prazo | 3, 9 | 38, 44 |

---

## CAPÍTULO × INVARIANTE PRIMÁRIO E SECUNDÁRIO

| Capítulo | Inv. primário | Inv. secundário | Função no esqueleto |
|----------|--------------|------------------|---------------------|
| 00M Manifesto | Todos | — | Capítulo-mãe declarativo |
| 01 O que é IA | 3 | — | Plantio da Camada Dupla |
| 02 Como modelos funcionam | 1 | — | Mecânica da Plausibilidade |
| 03 Tokens | 5 | — | Unidade do Custo Composto |
| 04 Janela de contexto | 2 | — | Capítulo-âncora das Extremidades |
| 05 Embeddings | 3 | 5 | Geometria do significado |
| 06 RAG | 3 | 7 | Camada Dupla aplicada |
| 07 Memória | 5 | — | Custo de retenção |
| 08 Fine-tuning | 7 | — | Decisão sem eval é especulação |
| 09 Engenharia de prompt | 2 | 7 | Estrutura pelas extremidades |
| 10 Chain of Thought | 1 | 2 | Raciocínio aparente, não real |
| 11 Context Engineering | 2 | 3 | Orquestração das pontas |
| 12 Agentes | 6 | — | Capítulo-âncora conceitual da Autonomia |
| 13 MCP | 4 | 6 | Padrão de encaixe + autonomia |
| 14 AI Engineering | 7 | 6 | Portal para Evals e LLMOps |
| 15 Comparação de modelos | 4 | — | Capítulo-âncora do Encaixe |
| 16 Open source | 4 | 5 | Decisão estratégica de encaixe |
| 17-34b (Volume Vivo) | 4-9 | Vários | Aplicação Claude por capacidade |
| 35 GitHub repos | 3 | — | Critérios duráveis, lista volátil |
| 36 Economia de tokens | 5 | — | Capítulo-âncora do Custo Composto |
| 37 Segurança e riscos | 8 | 1 | Mapeamento de risco com dono |
| 38 Futuro da IA | 3 | — | Vetores de mudança duráveis |
| 39 Evals | 7 | 1, 3, 8 | Capítulo definitivo do Termômetro |
| 40 LLMOps | 6 | 5, 7, 8 | Operação da Autonomia Proporcional |
| 41 Alignment | 1 | 8, 4 | Mecânica do alinhamento |
| 42 Governança | 8 | 6 | Aplicação da Responsabilidade |
| 43 Trade-offs canônicos | 4 | 9 | Cardápio de decisão |
| 44 Roadmap pessoal | 9 | 3 | Plano de aplicação |

---

## RELAÇÕES CRÍTICAS ENTRE INVARIANTES (não-óbvias)

| Par | Relação | Onde aparece |
|-----|---------|--------------|
| 1 ↔ 7 | Plausibilidade exige Termômetro: eval comportamental é antídoto à confiança injustificada | Caps 39, 41 |
| 2 ↔ 5 | Extremidades + Custo Composto: posição importa, mas volume mal arquitetado paga juros | Caps 11, 36 |
| 3 ↔ 4 | Camada Dupla + Encaixe: o padrão da escolha de modelo dura; o ranking da rodada não | Caps 15, 18 |
| 6 ↔ 7 | Autonomia Proporcional só existe com Termômetro: sem eval, autonomia é fé escalada | Caps 12, 32, 39, 40 |
| 6 ↔ 8 | Autonomia delegada precisa de Responsabilidade nominal: a IA executa, alguém assina | Caps 30, 40, 42 |
| 8 ↔ 9 | Responsabilidade Indelegável e Operador: governança precisa de operadores competentes | Caps 34, 42, 44 |
| 1 ↔ 8 | Plausibilidade + Responsabilidade: o erro plausível tem dono humano, sempre | Caps 02, 37, 42 |
| 3 ↔ 9 | Camada Dupla + Operador: padrão na cabeça do operador, número em apêndice datado | Cap 00M + Apêndice J |

---

## COMO USAR ESTE MAPA

| Situação | Como o mapa ajuda |
|----------|---------------------|
| Estou em decisão de adoção | Olhe o Invariante associado à decisão e siga ao framework e capítulo-âncora |
| Quero estudar por trilha temática | Use a tabela "Trilha × Invariante" para escolher o caminho |
| Vou apresentar a obra a um time | Use a Roda dos 9 Invariantes como abertura |
| Estou em incidente | Identifique qual Invariante foi violado e leia o capítulo-âncora |
| Quero ensinar um par sênior | Comece pelo Manifesto (Cap 00M) e este mapa em paralelo |

---

🔗 **Próximo:** [Apêndice C — Roadmaps por persona](L1-APX-C-roadmaps.md)
🔗 **Manifesto completo:** [Cap 00M](../01-manifesto/L1-C00M-manifesto-invariantes.md)
🔗 **Versão de bolso:** [Apêndice M](L1-APX-M-manifesto-bolso.md)



<div class="page-break"></div>


# APÊNDICE C — ROADMAPS POR PERSONA
## *Versão detalhada do Cap 44, com checklists semanais e métricas por marco*

> Este apêndice expande o Cap 44. Cada roadmap aqui traz, por marco (30/90/180/365 dias), **ações semanais sugeridas**, **métricas com referência numérica**, **artefatos esperados** e **gates de promoção**. Use como bússola e como acompanhamento de progresso real.

---

## ROADMAP 1 — EXECUTIVO (C-Level)

### Marco 30 dias
**Tese:** instalar o vocabulário e o nome humano por trás de cada decisão crítica.

| Semana | Ação | Artefato |
|--------|------|----------|
| 1 | Recitar os 9 Invariantes em apresentação ao seu primeiro escalão | Slide-deck dos Invariantes |
| 2 | Listar 5 decisões críticas de IA na organização hoje + identificar Accountable de cada uma | Tabela RACI mínima |
| 3 | Definir OKRs de adoção de IA (3 a 5) | Documento de OKRs |
| 4 | Produzir o Cartaz dos Invariantes da empresa (Cap 00M projeto) | Cartaz em A3 |

**Gate de promoção:** cartaz publicado + RACI mínimo de 5 decisões assinado + OKRs aprovados.

### Marco 90 dias
**Tese:** instalar governança de IA viva.

- Caderno de Governança v1 aprovado pela diretoria
- AI Council com mandato e primeira reunião realizada
- Cardápio dos 6 trade-offs aplicado a 3 iniciativas atuais
- Caderno de Evals v1 em construção (responsabilidade do CTO)

**Gate:** Caderno de Governança aprovado + AI Council ata pública.

### Marco 180 dias
**Tese:** instalar instrumentação técnica e financeira.

- LLMOps Pilar 1 (tracing) em 100% das features em produção
- Atribuição de custo de IA por feature em dashboard executivo
- Pirâmide de Evals em 50%+ de cobertura
- Primeiro simulado de incidente SEV-1 realizado

**Gate:** dashboard de custo viva + tracing 100%.

### Marco 365 dias
**Tese:** virar cultura.

- Maturidade média dos 10 controles de governança ≥ 3
- Auditoria externa positiva
- Aplicação dos Invariantes virou vocabulário interno (auditoria amostral em reuniões)
- 2 simulados de incidente realizados no ano

**Gate:** auditoria externa concluída.

---

## ROADMAP 2 — GESTOR / HEAD

### Marco 30 dias
- Selecionar 1 feature de IA sob seu escopo
- Mapear violações dos 9 Invariantes nessa feature (use a checklist do Cap 00M)
- Iniciar golden set de 30 casos representativos

**Gate:** feature mapeada + golden set v0.

### Marco 90 dias
- F8 EVAL-PIRÂMIDE base + meio implementados (eval em CI)
- LLMOps Pilares 1, 4 e 7 operantes
- Cardápio dos 6 trade-offs documentado para a feature

**Gate:** eval em CI bloqueando merge + runbook de incidente.

### Marco 180 dias
- Cobertura de tracing 100% nas features sob responsabilidade
- Rollback testado mensalmente
- Orçamento por feature visível

**Gate:** maturidade técnica média ≥ 3.

### Marco 365 dias
- Time aplicando Invariantes como norma de revisão de PR
- 0 SEV-1 no último trimestre
- Cultura aplicada e medida

**Gate:** cultura confirmada por auditoria amostral.

---

## ROADMAP 3 — DESENVOLVEDOR / ARQUITETO

### Marco 30 dias
- Aplicar F4 PROMPT-EXT em 1 feature
- Instrumentar tracing em 1 feature
- Estudar Caps 39 (Evals) e 40 (LLMOps)

**Gate:** 1 feature instrumentada.

### Marco 90 dias
- PR com eval em CI virou padrão do time
- Tool registry implementado
- F3 AGENTE-PROP aplicado em 1 agente

**Gate:** padrão de PR com eval adotado pelo time.

### Marco 180 dias
- Cobertura de tracing 100% nas features sob responsabilidade
- Participação no Caderno de LLMOps v1

**Gate:** Caderno de LLMOps publicado.

### Marco 365 dias
- Mentor de outros devs no método dos Invariantes
- Contribuição ao repositório de prompts da empresa
- Participação em decisão de arquitetura citando frameworks

**Gate:** reputação interna confirmada por feedback de pares.

---

## ROADMAP 4 — CONSULTOR

### Marco 30 dias
- Aplicar o cardápio dos 6 trade-offs em 1 cliente
- Produzir entrega usando os Invariantes como vocabulário

**Gate:** 1 cliente impactado.

### Marco 90 dias
- 3 clientes com cardápio aplicado
- 1 case publicado em mídia setorial

**Gate:** 3 cases internos documentados.

### Marco 180 dias
- Workshop dos 9 Invariantes para clientes
- Framework próprio adaptado ao seu nicho

**Gate:** workshop em pé.

### Marco 365 dias
- Reputação como referência em método (não em vendor)
- 10+ clientes operando pelo método

**Gate:** marca pessoal consolidada.

---

## ROADMAP 5 — EMPREENDEDOR / FOUNDER

### Marco 30 dias
- Aplicar F1 DECID-IA em cada feature de IA do produto
- F7 COMPOSTO-3T para auditar custo atual

**Gate:** decisão de adoção documentada por feature + baseline de custo.

### Marco 90 dias
- Golden set inicial para feature-chave
- Canário em produção
- Eval em CI
- Circuit breaker de custo

**Gate:** Pirâmide de Evals operante.

### Marco 180 dias
- F2 ENCAIXE-5 aplicado para escolher modelo por feature
- LLMOps maduro
- AUP publicada

**Gate:** TCO de IA / receita dentro do envelope.

### Marco 365 dias
- Crescimento sustentado com margem
- Cliente Enterprise compra pela arquitetura defendida

**Gate:** arquitetura virou diferencial competitivo.

---

## ROADMAP 6 — CRIADOR DE CONTEÚDO / EDUCADOR

### Marco 30 dias
- 4 posts/vídeos aplicando 1 Invariante por semana
- Distribuir versão de bolso (Apêndice M) à audiência

**Gate:** 4 peças publicadas.

### Marco 90 dias
- Workshop ou minicurso usando os Invariantes
- Biblioteca pessoal de prompts publicada

**Gate:** 1 workshop entregue.

### Marco 180 dias
- Comunidade de Operadores Inteligência Aumentada com 100+ membros engajados

**Gate:** comunidade ativa.

### Marco 365 dias
- Reconhecimento como referência em IA aplicada em pt-BR
- Convite a falar em eventos setoriais

**Gate:** marca consolidada.

---

## INSTRUMENTOS COMUNS A TODAS AS PERSONAS

### Calendário recorrente sugerido

| Cadência | Atividade |
|----------|-----------|
| Diária | 30 min com o Cartaz dos Invariantes em vista; auto-pergunta antes de cada decisão de IA |
| Semanal | Revisão dos artefatos da semana contra os 9 Invariantes |
| Mensal | Atualização do Apêndice Vivo (J) na sua área; revisão de métricas-chave |
| Trimestral | Revisão do roadmap; gates de promoção; ajuste de plano |
| Anual | Edição completa de todos os Cadernos (Governança, Evals, LLMOps); auditoria externa |

### Métricas universais

| Métrica | Cadência |
|---------|----------|
| Cobertura de tracing | Mensal |
| MTTR de SEV-1 e SEV-2 | Mensal |
| Custo de IA / receita | Mensal |
| Maturidade dos 10 controles (média) | Trimestral |
| Aplicação cultural dos Invariantes (auditoria amostral) | Semestral |

---

🔗 [Cap 44 Roadmap pessoal e organizacional](../02-capitulos/L1-C44-roadmap-pessoal.md) · [Cap 00M Manifesto](../01-manifesto/L1-C00M-manifesto-invariantes.md) · [Apêndice K Gabaritos](L1-APX-K-gabaritos.md)



<div class="page-break"></div>


# APÊNDICE D — FERRAMENTAS RECOMENDADAS
## *Curadoria por categoria, com critério de seleção*

> Lista corrente; aplicam-se os 6 critérios de seleção do [Cap 35 §35.1.5](../02-capitulos/L1-C35-github-repos.md). Versões e líderes correntes ficam no [Apêndice Vivo (J)](../../Livro-2-Dominando-Claude/04-apendices/L2-APX-J-apendice-vivo.md).

---

## CATEGORIAS

### Desenvolvimento e SDK
- Anthropic SDK (Python, TypeScript)
- OpenAI SDK
- Google Generative AI SDK
- Vercel AI SDK

### Eval e qualidade
- promptfoo (testes de prompt)
- deepeval (eval em Python)
- RAGAS (eval específica para RAG)
- inspect-ai (Anthropic, eval framework)
- Braintrust (parcial open)

### Observabilidade e LLMOps
- LangSmith (LangChain)
- Langfuse (open)
- Helicone
- Arize Phoenix (open)
- Datadog APM (LLM observability)
- New Relic AI observability

### MCP (servidores e clientes)
- `modelcontextprotocol/servers` (oficial)
- MCP Python SDK / TypeScript SDK
- `punkpeye/awesome-mcp-servers` (comunidade)

### Agentes
- Anthropic Claude Code (oficial)
- LangGraph (orquestração)
- crewAI (multi-agente)
- AutoGen (Microsoft)

### RAG
- LangChain / LlamaIndex (frameworks)
- Chroma, Qdrant, Pinecone, Weaviate (bancos vetoriais)
- Cohere Rerank, voyage-ai (reranking)

### Modelos open weights
- Hugging Face Hub (registry)
- vLLM, llama.cpp (inferência)
- Ollama (local)

### Notebooks e exploração
- Jupyter / Google Colab
- Claude Code para análise

---

## CRITÉRIO DE ESCOLHA

Antes de adotar qualquer ferramenta, aplicar os **6 critérios** do Cap 35 §35.1.5:
1. Mantenedor com governança clara
2. Último commit relevante
3. Comunidade ativa
4. Documentação completa
5. Compatibilidade declarada
6. Ecossistema reconhece

Ranking corrente entre concorrentes diretos no [Apêndice Vivo (J)](../../Livro-2-Dominando-Claude/04-apendices/L2-APX-J-apendice-vivo.md).

---

🔗 [Cap 35 GitHub Repos](../02-capitulos/L1-C35-github-repos.md) · [Apêndice E Leituras](L1-APX-E-leituras.md) · [Apêndice G Papers](L1-APX-G-papers.md)



<div class="page-break"></div>


# APÊNDICE E — LEITURAS COMPLEMENTARES
## *Livros, blogs e cursos comentados para aprofundar*

---

## LIVROS — FUNDAMENTOS DE IA

**Russell, S. & Norvig, P. — *Artificial Intelligence: A Modern Approach* (4ª ed., 2020).** Referência canônica do campo. Denso. Para quem quer fundamento acadêmico.

**Bishop, C. & Bishop, H. — *Deep Learning: Foundations and Concepts* (2024).** Fundamentos matemáticos modernos. Para profissional técnico que quer ir além do uso.

**Goodfellow, I., Bengio, Y. & Courville, A. — *Deep Learning* (2016).** Clássico. Algumas partes desatualizadas; a estrutura conceitual segue válida.

**Murphy, K. — *Probabilistic Machine Learning* (2 vols., 2022, 2023).** Fundamentos probabilísticos.

---

## LIVROS — IA APLICADA

**Karpathy, A. — coleção de palestras públicas e o blog `karpathy.ai`.** Não é livro formal, mas o conjunto vale como referência de pensamento técnico atual.

**Engelbart, D. — *Augmenting Human Intellect* (1962).** O conceito original de "inteligência aumentada". Origem filosófica da obra.

**Christian, B. — *The Alignment Problem* (2020).** Visão geral acessível.

**Russell, S. — *Human Compatible* (2019).** Fundamento filosófico do alinhamento.

---

## LIVROS — GOVERNANÇA E OPERAÇÃO

**Beyer, B. et al. — *Site Reliability Engineering* (Google, 2016) e *The Site Reliability Workbook* (2018).** Fundamento de operação madura aplicável a LLMOps.

**Doerr, J. — *Measure What Matters* (2018).** OKRs como instrumento de adoção.

**Allspaw, J. & Robbins, J. — *Web Operations* (2010).** Fundamentos de cultura blameless.

**Davenport, T. — *The AI Advantage* (2018).** Visão executiva de adoção.

---

## BLOGS E NEWSLETTERS

- **Anthropic blog** (`anthropic.com/news`) — releases, research, perspectivas
- **OpenAI blog** (`openai.com/news`)
- **Google DeepMind blog**
- **Karpathy** (`karpathy.ai`)
- **Simon Willison** (`simonwillison.net`)
- **Latent Space** (newsletter sobre IA aplicada)
- **The Batch** (deeplearning.ai)
- **Import AI** (Jack Clark)
- **Marble Block** (em PT-BR, em desenvolvimento)

---

## CURSOS

- **DeepLearning.AI** — curso de Andrew Ng + curadoria de cursos curtos sobre temas específicos (RAG, agentes, LangChain, etc.)
- **Hugging Face Course** — open source, prático
- **Anthropic courses** (`github.com/anthropics/courses`)
- **MIT 6.5940 (TinyML)** — para quem vai para hardware especializado
- **Stanford CS25 (Transformers United)** — fundamentos avançados

---

🔗 [Apêndice F Newsletters](L1-APX-F-newsletters.md) · [Apêndice G Papers](L1-APX-G-papers.md) · [Apêndice H Bibliografia](L1-APX-H-bibliografia.md)



<div class="page-break"></div>


# APÊNDICE F — NEWSLETTERS E CANAIS
## *Curadoria comentada para manutenção do conhecimento*

> Manter atualização é parte do método dos Invariantes (F9 ROTA-DUPLA): a Trilha Número exige fontes confiáveis e periódicas. Esta lista é a curadoria de manutenção.

---

## EM INGLÊS — ALTA PRIORIDADE

**Latent Space (`latent.space`).** Podcast e newsletter sobre IA aplicada em produção. Excelente para profissional que opera, não só estuda.

**Import AI (Jack Clark).** Semanal. Análise de papers, releases e mercado. Conciso.

**The Batch (deeplearning.ai).** Semanal. Andrew Ng e time. Visão executiva.

**Ben's Bites.** Diária, curta. Para acompanhar a frequência alta de releases.

**Simon Willison weekly notes.** Foco em IA aplicada, ferramentas, prompts.

**One Useful Thing (Ethan Mollick).** Pesquisa em adoção organizacional de IA.

---

## EM INGLÊS — APROFUNDAMENTO

**The Gradient.** Análise técnica, papers comentados.

**Last Week in AI.** Resumo semanal mais técnico que Ben's Bites.

**AI Snake Oil (Sayash Kapoor, Arvind Narayanan).** Princeton. Crítica fundamentada ao hype.

**The Pragmatic Engineer** (Gergely Orosz) — não é só IA, mas tem cobertura de LLMOps e adoção corporativa.

---

## EM PT-BR

> Curadoria em formação. A obra *Inteligência Aumentada* pretende contribuir para fechar essa lacuna.

A serem incluídas conforme a comunidade brasileira de IA aplicada amadurecer.

---

## PODCASTS

**No Priors** (Sarah Guo, Elad Gil).
**Lex Fridman Podcast** (técnico + entrevistas).
**Latent Space podcast**.
**Hard Fork** (Kevin Roose, Casey Newton — NYT).

---

## CANAIS ANTHROPIC

**Anthropic news** (`anthropic.com/news`).
**Anthropic Research** (papers e relatórios).
**Anthropic courses** (treinamento estruturado).
**Claude Code release notes**.

---

## FREQUÊNCIA RECOMENDADA DE LEITURA

| Persona | Cadência |
|---------|----------|
| Executivo | 1 newsletter executiva (Batch ou One Useful Thing) semanal |
| Gestor/Head | + 1 newsletter técnica (Latent Space ou Import AI) semanal |
| Dev/Arquiteto | + papers seminais quinzenal + Simon Willison |
| Empreendedor | Todas as acima + News executive (a16z, Bessemer) |

---

🔗 [Apêndice E Leituras](L1-APX-E-leituras.md) · [Apêndice G Papers](L1-APX-G-papers.md) · [F9 ROTA-DUPLA](../03-frameworks/L1-F9-rota-dupla.md)
