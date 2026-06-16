---
title: "Inteligência Aumentada"
lang: pt-BR
---



<div class="page-break"></div>


# APÊNDICE G — PAPERS OBRIGATÓRIOS
## *35 papers que sustentam o estado da arte conceitual em IA generativa*

> Curadoria por categoria. Cada paper com 1-2 linhas explicando por que ler. Versões e papers correntes ficam no [Apêndice Vivo (J)](../../Livro-2-Dominando-Claude/04-apendices/L2-APX-J-apendice-vivo.md).

---

## I. TRANSFORMER E ARQUITETURA

1. **Vaswani et al. — *Attention Is All You Need* (2017).** O paper que mudou a IA moderna. Leitura inegociável.
2. **Devlin et al. — *BERT* (2018).** Pré-treinamento bidirecional. Fundamento de embeddings modernos.
3. **Radford et al. — *GPT* (2018) e *GPT-2* (2019).** Pré-treinamento generativo, escala.
4. **Brown et al. — *Language Models are Few-Shot Learners* (GPT-3, 2020).** Emergência de capacidade por escala.
5. **Touvron et al. — *Llama 2* / *Llama 3* (2023, 2024).** Família open weights de referência.

---

## II. CONTEXTO E ATENÇÃO

6. **Liu et al. — *Lost in the Middle* (2023).** Base empírica do Invariante 2.
7. **Press et al. — *ALiBi: Train Short, Test Long* (2022).** Encoding posicional alternativo.
8. **Su et al. — *RoPE* (2023).** Rotary position embeddings.

---

## III. ALINHAMENTO E RLHF

9. **Christiano et al. — *Deep RL from Human Preferences* (2017).** Primeira formalização moderna do RLHF.
10. **Ouyang et al. — *InstructGPT* (2022).** RLHF aplicado em produção.
11. **Bai et al. — *Constitutional AI* (Anthropic, 2022).** RLAIF e CAI.
12. **Rafailov et al. — *DPO* (2023).** Substituição do PPO no mercado.
13. **Hong et al. — *ORPO* (2024).** Variante recente.
14. **Anthropic — *Collective Constitutional AI* (2023).** CAI com input público.

---

## IV. EVALS E AVALIAÇÃO

15. **Liang et al. — *HELM* (Stanford CRFM, 2022).** Avaliação holística.
16. **Srivastava et al. — *BIG-bench* (2022).** Benchmark colaborativo.
17. **Zheng et al. — *Judging LLM-as-a-Judge* (2023).** Base de LLM-as-judge.
18. **Liu et al. — *G-Eval* (2023).** Eval por LLM alinhada com humano.
19. **Es et al. — *RAGAS* (2023).** Eval específica para RAG.
20. **Mazeika et al. — *HarmBench* (2024).** Adversarial e red-teaming padronizados.

---

## V. AGENTES E TOOL USE

21. **Yao et al. — *ReAct* (2022).** Padrão "raciocinar + agir" canônico.
22. **Schick et al. — *Toolformer* (2023).** Modelos que aprendem a usar tools.
23. **Wang et al. — *Voyager* (2023).** Agente em Minecraft, modelo de descoberta.
24. **Anthropic — *Building Effective Agents* (2024).** Distinção workflow × agente.

---

## VI. INTERPRETABILIDADE MECANICISTA

25. **Olah et al. — *In-context Learning and Induction Heads* (2022).** Circuitos identificados.
26. **Anthropic — *Towards Monosemanticity* (2023).** Sparse autoencoders.
27. **Anthropic — *Scaling Monosemanticity* (2024).** Aplicação em Claude 3 Sonnet.

---

## VII. SEGURANÇA E COMPORTAMENTO

28. **Perez et al. — *Discovering Language Model Behaviors with Model-Written Evals* (2022).** Auto-descoberta de comportamentos problemáticos.
29. **Ganguli et al. — *Red Teaming Language Models* (Anthropic, 2022).** Metodologia de red-teaming.
30. **Sharma et al. — *Towards Understanding Sycophancy* (2023).** Mecânica da bajulação.
31. **Greshake et al. — *Prompt Injection in LLM-Integrated Applications* (2023).** Vetor de ataque dominante.
32. **Bender et al. — *On the Dangers of Stochastic Parrots* (2021).** Crítica fundamentada.

---

## VIII. RAG E RETRIEVAL

33. **Lewis et al. — *RAG: Retrieval-Augmented Generation* (2020).** Paper seminal.
34. **Karpukhin et al. — *Dense Passage Retrieval (DPR)* (2020).** Retrieval moderno.
35. **Reimers, Gurevych — *Sentence-BERT* (2019).** Embeddings para busca semântica.

---

## COMO LER PAPERS DE IA

1. **Abstract + conclusão primeiro.** 60% dos papers basta isso.
2. **Para os 40% que valem mais, leia diagramas e tabelas.**
3. **Equações só onde a matemática realmente sustenta a tese.**
4. **Discussions e limitações** dizem mais que método em muitos casos.
5. **Para citação séria, ler integralmente.**

---

🔗 [Apêndice E Leituras](L1-APX-E-leituras.md) · [Apêndice F Newsletters](L1-APX-F-newsletters.md) · [Apêndice H Bibliografia](L1-APX-H-bibliografia.md)



<div class="page-break"></div>


# APÊNDICE H — BIBLIOGRAFIA COMPLETA
## *Fontes primárias e secundárias citadas na obra*

> Bibliografia consolidada da obra. Para curadoria comentada, ver [Apêndice E (Leituras)](L1-APX-E-leituras.md), [Apêndice F (Newsletters)](L1-APX-F-newsletters.md) e [Apêndice G (Papers)](L1-APX-G-papers.md). Versões correntes de documentação técnica e regulação no [Apêndice Vivo (J)](../../Livro-2-Dominando-Claude/04-apendices/L2-APX-J-apendice-vivo.md).

---

## I. PAPERS SEMINAIS

### Transformer e LLMs
- Vaswani, A. et al. *Attention Is All You Need* (2017)
- Devlin, J. et al. *BERT: Pre-training of Deep Bidirectional Transformers* (2018)
- Brown, T. et al. *Language Models are Few-Shot Learners* (GPT-3) (2020)
- Touvron, H. et al. *LLaMA 2: Open Foundation and Fine-Tuned Chat Models* (2023)
- Anthropic. *The Claude 3 Model Family* (2024)

### Atenção e contexto
- Liu, N. F. et al. *Lost in the Middle: How Language Models Use Long Contexts* (2023)
- Press, O. et al. *Train Short, Test Long: Attention with Linear Biases (ALiBi)* (2022)
- Su, J. et al. *RoFormer: Enhanced Transformer with Rotary Position Embedding (RoPE)* (2023)

### Alinhamento
- Christiano, P. et al. *Deep Reinforcement Learning from Human Preferences* (2017)
- Ouyang, L. et al. *Training language models to follow instructions with human feedback (InstructGPT)* (OpenAI, 2022)
- Bai, Y. et al. *Constitutional AI: Harmlessness from AI Feedback* (Anthropic, 2022)
- Anthropic. *Collective Constitutional AI* (2023)
- Rafailov, R. et al. *Direct Preference Optimization* (2023)
- Hong, J. et al. *ORPO: Monolithic Preference Optimization without Reference Model* (2024)
- Ethayarajh, K. et al. *KTO: Model Alignment as Prospect Theoretic Optimization* (2024)

### Interpretabilidade
- Olah, C. et al. *In-context Learning and Induction Heads* (Anthropic, 2022)
- Anthropic. *Towards Monosemanticity* (2023)
- Anthropic. *Scaling Monosemanticity: Extracting Interpretable Features from Claude 3 Sonnet* (2024)

### Evals
- Liang, P. et al. *HELM: Holistic Evaluation of Language Models* (Stanford CRFM, 2022-)
- Srivastava, A. et al. *BIG-bench: Beyond the Imitation Game Benchmark* (2022)
- Zheng, L. et al. *Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena* (2023)
- Liu, Y. et al. *G-Eval: NLG Evaluation using GPT-4 with Better Human Alignment* (2023)
- Es, S. et al. *RAGAS: Automated Evaluation of Retrieval Augmented Generation* (2023)
- Mazeika, M. et al. *HarmBench: A Standardized Evaluation Framework for Automated Red Teaming and Robust Refusal* (2024)
- Bowman, S. *Evaluating LLMs is a minefield* (palestra, 2023)

### Agentes
- Yao, S. et al. *ReAct: Synergizing Reasoning and Acting in Language Models* (2022)
- Schick, T. et al. *Toolformer: Language Models Can Teach Themselves to Use Tools* (2023)
- Wang, G. et al. *Voyager: An Open-Ended Embodied Agent with Large Language Models* (2023)
- Anthropic. *Building Effective Agents* (2024)

### RAG e retrieval
- Lewis, P. et al. *Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks* (2020)
- Karpukhin, V. et al. *Dense Passage Retrieval for Open-Domain Question Answering* (2020)
- Reimers, N., Gurevych, I. *Sentence-BERT* (2019)

### Segurança e comportamento
- Perez, E. et al. *Discovering Language Model Behaviors with Model-Written Evaluations* (Anthropic, 2022)
- Ganguli, D. et al. *Red Teaming Language Models to Reduce Harms* (Anthropic, 2022)
- Sharma, M. et al. *Towards Understanding Sycophancy in Language Models* (Anthropic, 2023)
- Greshake, K. et al. *Not what you've signed up for: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection* (2023)
- Liu, Y. et al. *Prompt Injection attack against LLM-integrated Applications* (2023)
- Bender, E. et al. *On the Dangers of Stochastic Parrots* (2021)

### Filosofia e fundamento
- Russell, S. *Human Compatible* (2019)
- Christian, B. *The Alignment Problem* (2020)
- Bommasani, R. et al. *On the Opportunities and Risks of Foundation Models* (Stanford CRFM, 2021)

---

## II. LIVROS E REFERÊNCIAS DE FUNDO

- Russell, S. & Norvig, P. *Artificial Intelligence: A Modern Approach* (4ª ed., 2020)
- Bishop, C. & Bishop, H. *Deep Learning: Foundations and Concepts* (2024)
- Goodfellow, I., Bengio, Y., Courville, A. *Deep Learning* (2016)
- Murphy, K. *Probabilistic Machine Learning* (2 vols., 2022 e 2023)
- Engelbart, D. *Augmenting Human Intellect* (1962)
- Drucker, P. *The Effective Executive* (1966)
- Brooks, F. *The Mythical Man-Month* (1975/1995)
- Beyer, B. et al. *Site Reliability Engineering* (Google, 2016) e *The Site Reliability Workbook* (2018)
- Allspaw, J. & Robbins, J. *Web Operations* (2010)
- Doerr, J. *Measure What Matters* (2018)
- Kotter, J. *Leading Change* (1996)
- Davenport, T. *The AI Advantage* (2018)
- Schmidhuber, J. *Annotated History of Modern AI* (recente)

---

## III. NORMAS, REGULAÇÃO, FRAMEWORKS PÚBLICOS

- NIST. *AI Risk Management Framework (AI RMF 1.0)* (2023)
- ISO/IEC 42001 — *Information technology — Artificial intelligence — Management system* (2023)
- OECD AI Principles (2019, revisão 2024)
- EU AI Act (Regulation 2024/1689)
- Brasil — PL 2338/2023 (em tramitação no Senado Federal)
- LGPD — Lei 13.709/2018 (Brasil)
- ANPD — Guias e enunciados sobre IA (2023-2026, ver Apêndice Vivo)
- Anthropic. *Responsible Scaling Policy* (2023, 2024)

---

## IV. DOCUMENTAÇÃO TÉCNICA OFICIAL

- [Anthropic Claude documentation](https://docs.claude.com)
- [OpenAI documentation](https://platform.openai.com/docs)
- [Google AI Studio](https://ai.google.dev)
- [Model Context Protocol specification](https://modelcontextprotocol.io)
- [OpenTelemetry GenAI semantic conventions](https://opentelemetry.io/docs/specs/semconv/gen-ai/)
- [Hugging Face Hub](https://huggingface.co)

---

## V. RECURSOS PEDAGÓGICOS COMENTADOS

Curadoria comentada de cursos, newsletters e canais — ver [Apêndice E](L1-APX-E-leituras.md) e [Apêndice F](L1-APX-F-newsletters.md).

---

## VI. SOBRE ESTA OBRA

**Inteligência Aumentada — Os Invariantes da IA** (Livro 1) e **Inteligência Aumentada — Volume Vivo: Dominando Claude** (Livro 2). Autor: Fabio Garcia. Edição: 1ª. Ano: 2026. Plano editorial inclui Edição Aniversário em 5 anos.

**Os 9 Invariantes da IA** são sistema proprietário desta obra, sintetizando padrões observáveis em literatura técnica, em práticas operacionais e em incidentes documentados. As referências secundárias que mais influenciaram a formulação estão listadas no Cap 00M §00M.14.

---

🔗 [Apêndice E Leituras](L1-APX-E-leituras.md) · [Apêndice F Newsletters](L1-APX-F-newsletters.md) · [Apêndice G Papers obrigatórios](L1-APX-G-papers.md) · [Apêndice Vivo (J)](../../Livro-2-Dominando-Claude/04-apendices/L2-APX-J-apendice-vivo.md)



<div class="page-break"></div>


# APÊNDICE I — ÍNDICE REMISSIVO
## *Termos, frameworks, Invariantes, casos — onde encontrar na obra*

> Índice em ordem alfabética. Cada termo aponta para capítulo(s) ou framework(s) onde é aprofundado. Para vocabulário definido, ver [Apêndice A — Glossário](L1-APX-A-glossario.md). Marcadores: ★ termo proprietário da obra; ◆ termo técnico canônico.

---

## A
- **Accountable** (RACI) — Cap 42 §42.3.3, F6 GOV-INDELEGÁVEL
- **Adversarial set ◆** — Cap 39 §39.3.2, F8 EVAL-PIRÂMIDE
- **Agente ◆** — Cap 12 (conceitual), Cap 40 (operacional), F3 AGENTE-PROP
- **AI Council** — Cap 42 §42.3.4
- **Alignment ★** — Cap 41
- **Apêndice Vivo** — Apêndice J (L2)
- **Artifacts (Claude)** — Cap 21 (L2)
- **Atenção (Q/K/V) ◆** — Cap 02 §2.3.5 (boxe técnico)
- **AUP — Política de Uso Aceitável** — Cap 42 §42.3.5
- **Autonomia Proporcional ★** — Invariante 6, Cap 12, Cap 40, F3

## B
- **Banco Solar (caso)** — EC1, Cap 00M §00M.5
- **Benchmark ◆** — Cap 15 §15.3.3, Apêndice Vivo
- **BPE** — Cap 03

## C
- **Camada Dupla ★** — Invariante 3, Cap 01, F9 ROTA-DUPLA
- **Canário** — Cap 40 §40.3.3
- **Chain of Thought (CoT)** — Cap 10
- **Circuit breaker** — Cap 40 §40.3.5
- **Claude Code** — Cap 24 (L2)
- **Claude Web** — Cap 19 (L2)
- **Constitutional AI** — Cap 41 §41.3.2
- **Context Engineering** — Cap 11
- **Custo Composto ★** — Invariante 5, Cap 36, F7 COMPOSTO-3T

## D
- **Datasets de prática** — Apêndice K, Repositório acompanhante
- **DECID-IA (F1)** — Frameworks/L1-F1
- **DPO (Direct Preference Optimization)** — Cap 41 §41.3.2

## E
- **Embeddings ◆** — Cap 05
- **Encaixe ★** — Invariante 4, Cap 15, F2 ENCAIXE-5
- **Enterprise (Claude)** — Cap 30 (L2)
- **Evals** — Cap 39, F8 EVAL-PIRÂMIDE
- **EVAL-PIRÂMIDE (F8)** — Frameworks/L1-F8
- **Executivos (Claude para)** — Cap 34 (L2)
- **Extremidades ★** — Invariante 2, Cap 04, F4 PROMPT-EXT

## F
- **Faithfulness** — Cap 39, Apêndice A
- **Fine-tuning ◆** — Cap 08, Trade-off T1, T6
- **Frameworks F1-F9** — Frameworks/

## G
- **Gabaritos** — Apêndice K
- **Glossário** — Apêndice A
- **Golden set ★ ◆** — Cap 39 §39.3.4, F8 EVAL-PIRÂMIDE
- **GOV-INDELEGÁVEL (F6)** — Frameworks/L1-F6
- **Governança de IA** — Cap 42, F6

## H
- **Haiku, Sonnet, Opus ◆** — Cap 18 (L2)
- **Helpful, Harmless, Honest** — Cap 41 §41.1

## I
- **Interpretabilidade mecanicista** — Cap 41 §41.3.3
- **Invariantes da IA ★** — Cap 00M (Manifesto), Apêndice M (bolso)

## J
- **Janela de contexto ◆** — Cap 04

## K
- **Kill switch** — Cap 40 §40.3.6

## L
- **LGPD art. 20** — Cap 42 §42.3.6, EC2
- **LLM-as-judge ★ ◆** — Cap 39 §39.3.5, F8
- **LLMOps** — Cap 40
- **Lost in the Middle ◆** — Cap 04, Inv. 2

## M
- **Manifesto dos Invariantes** — Cap 00M, Apêndice M
- **Mapa Mental** — Apêndice B
- **MCP** — Cap 13 (conceitual), Cap 33 (L2), F5 MCP-COBERTURA
- **MCP-COBERTURA (F5)** — Frameworks/L1-F5
- **Memória ◆** — Cap 07
- **Métrica.io (caso)** — EC4
- **MTTR** — Cap 40 §40.3.4

## O
- **Open source (modelos)** — Cap 16, Trade-off T3
- **OpenTelemetry GenAI** — Cap 40 §40.3.1
- **Operador ★** — Invariante 9, Cap 34 (L2), F1
- **Over-refusal** — Cap 41 §41.3.4

## P
- **Plausibilidade ★** — Invariante 1, Cap 41
- **Pólice.io (caso)** — Cap 40 §40.6
- **Postmortem sem culpa** — Cap 42 §42.3.7
- **Projects (Claude)** — Cap 20 (L2)
- **Prompt** — Cap 09, Apêndice L, F4 PROMPT-EXT
- **PROMPT-EXT (F4)** — Frameworks/L1-F4
- **Prompt injection** — Cap 40 §40.3.6

## Q
- **Q/K/V (Query Key Value)** — Cap 02 §2.3.5

## R
- **RACI** — Cap 42 §42.3.3, F6
- **RAG ◆** — Cap 06, Trade-off T1
- **RedeCasa (caso)** — EC2
- **Refusal training** — Cap 41 §41.3.4
- **Repositório acompanhante** — `/_repositorio-acompanhante/`
- **Research (Claude)** — Cap 22 (L2)
- **Responsabilidade Indelegável ★** — Invariante 8, Cap 42, F6
- **Reward hacking** — Cap 41 §41.3.2
- **RLAIF** — Cap 41 §41.3.2
- **RLHF** — Cap 41 §41.3.2
- **Roadmap pessoal** — Cap 44, Apêndice C
- **Rollback** — Cap 40 §40.3.4
- **ROTA-DUPLA (F9)** — Frameworks/L1-F9

## S
- **Sandbagging** — Cap 41 §41.3.4
- **SEV-1 a SEV-4** — Cap 40 §40.3.7, Cap 42 §42.3.7
- **SFT (Supervised Fine-Tuning)** — Cap 41 §41.3.2
- **Shadow mode** — Cap 40 §40.3.3
- **Skills (Claude)** — Cap 31 (L2)
- **Span × Trace × Session** — Cap 40 §40.3.1
- **Sparse Autoencoders** — Cap 41 §41.3.3
- **Subagents** — Cap 32 (L2)
- **Sycophancy** — Cap 41 §41.3.2, Cap 39

## T
- **Team (Claude)** — Cap 29 (L2)
- **Termômetro ★** — Invariante 7, Cap 39, F8
- **Tokens ◆** — Cap 03
- **Tokenizer ◆** — Cap 03 §3.3.1
- **Trade-offs canônicos** — Cap 43
- **Tracing** — Cap 40 §40.3.1
- **Transformer ◆** — Cap 02

## V
- **Validação UAU ★** — Cada capítulo + Apêndice A
- **Versionamento** — Cap 40 §40.3.2
- **Vianna Castro Almeida (caso)** — EC3
- **Vibe-eval** — Cap 39 §39.3.9 (anti-padrão)

## Y, W
- **Workflow determinístico** — Cap 43 §43.3 (T2)

---

🔗 [Apêndice A Glossário](L1-APX-A-glossario.md) · [Apêndice B Mapa mental](L1-APX-B-mapa-mental.md) · [Apêndice M Manifesto de bolso](L1-APX-M-manifesto-bolso.md)



<div class="page-break"></div>


# APÊNDICE K — GABARITOS COMENTADOS
## *Soluções estruturadas para exercícios e projetos da obra*

> Este apêndice oferece **estruturas de resposta** para os exercícios práticos e projetos dos capítulos. Não são respostas únicas; são gabaritos que mostram **o método de pensar** que cada exercício pretende ativar. Use como referência para autoavaliação, nunca como atalho para pular o esforço.

---

## COMO USAR ESTE APÊNDICE

1. **Faça o exercício primeiro.** Sem isso, o gabarito vira leitura passiva.
2. **Compare estrutura, não conteúdo.** O gabarito mostra "como pensar", não "o que pensar".
3. **Customize ao seu domínio.** Cada gabarito é genérico; sua resposta deve ser específica.
4. **Reverifique após 90 dias.** Gabaritos evoluem com o leitor.

---

## CAP 00M — MANIFESTO DOS INVARIANTES

### Exercício 1 — Diagnóstico do time
**Estrutura esperada:** lista de 9 violações típicas (uma por Invariante) com exemplo específico do time. Identificar os 3 mais críticos com sinal (ex: "regressão silenciosa não detectada nos últimos 6 meses" para Inv. 7).

### Exercício 2 — Auditoria de decisões
**Estrutura esperada:** tabela com 3 decisões × 9 Invariantes; marcar respeitado/violado; descrever o que mudaria.

### Projeto — Cartaz dos Invariantes da empresa
**Critério de qualidade:** uma página A3, com violação típica adaptada à linguagem do seu setor. Outro executivo lê e reconhece os 9 Invariantes pela sua versão sem ambiguidade.

---

## CAP 02 — COMO MODELOS FUNCIONAM

### Projeto — Plano para apresentar o transformer à diretoria
**Estrutura:** Slide 1 (analogia do estagiário que leu tudo); Slide 2 (predição de próximo token); Slide 3 (Q/K/V em alto nível, sem fórmula); Slide 4 (consequência prática — Plausibilidade); Slide 5 (Camada Dupla aplicada à diretoria).

---

## CAP 03 — TOKENS

### Exercício 1 — Auditoria de tokens da operação
**Estrutura:** levantamento de input/output médio por feature; cálculo da fração que é prompt vs resposta; identificação do maior consumidor de tokens.

### Projeto — Plano de economia
**Estrutura:** aplicar F7 COMPOSTO-3T; identificar tier dominante; identificar redundância; plano em 30 dias.

---

## CAP 06 — RAG

### Projeto — Caderno de RAG do produto
**Estrutura:** definição de "resposta certa" → estratégia de chunking → modelo de embedding → reranking → política de top-k → eval de faithfulness.

---

## CAP 09 — ENGENHARIA DE PROMPT

### Projeto — Aplicar F4 PROMPT-EXT em 5 prompts
**Estrutura:** para cada prompt, reescrever nos 5 blocos canônicos. Antes/depois com justificativa por bloco.

---

## CAP 39 — EVALS

### Exercício 1 — Classificação de falhas
**Estrutura:** para cada falha listada, marcar qual camada da pirâmide a teria capturado; identificar a camada mais frágil hoje.

### Projeto — Caderno de Evals v1
**Critério de qualidade:** outro engenheiro lê e roda eval contra mudança nova sem perguntar mais que 3 coisas. Inclui golden set 30-50 itens, LLM-as-judge calibrado com correlação ≥0,7 contra humano, adversarial 20+ casos, política de bloqueio em CI.

---

## CAP 40 — LLMOPS

### Exercício 1 — Diagnóstico dos 7 pilares
**Estrutura:** matriz 7×5 (pilar × maturidade 0-4); identificar 2 mais frágeis; plano de 60 dias.

### Projeto — Caderno de LLMOps v1
**Critério de qualidade:** outro engenheiro responde sem perguntar qualquer das 7 perguntas executivas (§40.10).

---

## CAP 41 — ALIGNMENT

### Exercício 3 — Mini-constituição corporativa
**Estrutura:** 7 princípios em pt-BR, cada um em uma frase, sem jargão. Submetido a par sênior para revisão.

### Projeto — Caderno de Alignment Operacional
**Critério de qualidade:** outro engenheiro sênior responde "como nosso sistema lida com pedido de conselho médico não-supervisionado?" sem perguntar.

---

## CAP 42 — GOVERNANÇA

### Projeto — Caderno de Governança v1
**Critério de qualidade:** outro executivo responde sem ambiguidade: "quem é o Accountable por X?", "qual a maturidade do controle Y?", "quando é o próximo simulado?".

---

## CAP 43 — TRADE-OFFS

### Projeto — Cardápio de Trade-offs do produto
**Critério de qualidade:** outro executivo defende a arquitetura em reunião externa (cliente, conselho, auditor) sem perguntar.

---

## CAP 44 — ROADMAP PESSOAL

### Projeto — Apresentação à diretoria
**Critério de qualidade:** diretoria aprova o roadmap em uma reunião, com mandato formal sobre IA.

---

🔗 [Cap 00M](../01-manifesto/L1-C00M-manifesto-invariantes.md) · [Apêndice C Roadmaps](L1-APX-C-roadmaps.md) · [Apêndice L Biblioteca de prompts](L1-APX-L-biblioteca-prompts.md)



<div class="page-break"></div>


# APÊNDICE L — BIBLIOTECA DE PROMPTS TESTADOS
## *Espelho conceitual do `/prompts` no repositório acompanhante*

> Cada prompt aqui segue a estrutura **F4 PROMPT-EXT** (5 blocos posicionais) e é categorizado por caso de uso. A versão rodável vive no [repositório acompanhante](../../_repositorio-acompanhante/prompts/). Esta lista é a referência conceitual; a implementação rodável e atualizada vive fora do livro.

---

## ESTRUTURA CANÔNICA DE TODO PROMPT NA BIBLIOTECA

```
[BLOCO 1 — PERSONA E MISSÃO]
[BLOCO 2 — CONSTITUIÇÃO (regras invioláveis)]
[BLOCO 3 — CONTEXTO]
[BLOCO 4 — INSTRUÇÃO OPERACIONAL + FORMATO]
[BLOCO 5 — PERGUNTA VIVA]
```

---

## CATEGORIAS

### 1. Análise jurídica e DD em M&A (EC3 Vianna Castro)

| Prompt | Função | Eval mínimo |
|--------|--------|-------------|
| `extrair-change-of-control` | Identifica cláusula com citação literal | Golden set 40 contratos + honestidade de citação |
| `red-flag-mac` | Marca Material Adverse Change | Golden set + adversarial de redação ambígua |
| `sumario-categoria-clausula` | Sumário executivo por categoria | LLM-as-judge calibrado |
| `comparar-clausula-padrao` | Compara cláusula contra padrão da banca | Golden set por tipo de operação |

### 2. Escrita executiva

| Prompt | Função | Eval mínimo |
|--------|--------|-------------|
| `memo-para-board` | Memo de 1 página com decisão pedida | Golden set 30 memos + voz padrão |
| `sumario-executivo-relatorio` | Sumário de 5 bullets de relatório técnico | LLM-as-judge calibrado |
| `q-a-para-diretoria` | Roteiro de antecipação de objeções | Adversarial de pergunta hostil |

### 3. Classificação estruturada (EC1 Banco Solar)

| Prompt | Função | Eval mínimo |
|--------|--------|-------------|
| `classificar-tier-ticket` | Classifica ticket em tier 1-4 | Golden set 600 tickets |
| `roteamento-por-intent` | Decide agente apropriado por intent | F1 ponderada por classe |
| `escalonamento-para-humano` | Decide se escalar | Adversarial sycophancy bancário |

### 4. Extração de campos

| Prompt | Função | Eval mínimo |
|--------|--------|-------------|
| `extrair-campos-curriculo` | Extrai sem inferir atributo protegido | Golden + adversarial pareado (EC2) |
| `extrair-numeros-relatorio` | Extrai com faithfulness numérica | LLM-as-judge calibrado (EC6 Atlas) |
| `extrair-stakeholders` | Mapa de stakeholders B2B (EC5 EnterTech) | Golden set 50 briefs |

### 5. Agentes supervisionados

| Prompt | Função | Eval mínimo |
|--------|--------|-------------|
| `agente-cotacao-seguro` | Cotação assistida 7 seguradoras (Pólice.io) | Tracing + circuit breaker + eval de loop |
| `agente-suporte-tier-1` | Atendimento tier 1 (EC1) | Golden + adversarial sycophancy |
| `agente-prospect-research` | Pesquisa de prospect (EC5) | Honestidade de fonte |

### 6. RAG e síntese (EC4 Métrica.io)

| Prompt | Função | Eval mínimo |
|--------|--------|-------------|
| `rag-documentacao-saas` | Resposta de docs com citação | Faithfulness + context precision |
| `explicar-resultado-query` | Explicação de gráfico/tabela | LLM-as-judge calibrado para precisão numérica |
| `sugerir-insight-dados` | Sugestão de insight baseado em dados | Adversarial: ausência de dados → "não tenho como afirmar" |

---

## REGRAS DE USO DA BIBLIOTECA

1. **Não copie cegamente.** Cada prompt é instância de F4; entenda o porquê antes de adaptar.
2. **Customize ao seu domínio.** Os prompts são genéricos; sua aplicação demanda específico.
3. **Inicie com golden set próprio.** Não use o golden set de exemplo em produção; é referência.
4. **Reverifique após mudança de modelo.** Prompt calibrado para X pode regredir em Y.
5. **Mantenha versionado.** Trate prompts como código (LLMOps Pilar 2).

---

## ANTI-PADRÕES NA CONSTRUÇÃO DE PROMPT

| Anti-padrão | Por que mata | Antídoto |
|-------------|--------------|----------|
| Regra crítica no meio do prompt | Inv. 2 — atenção decai no centro | F4: regra na Constituição (logo após persona) |
| Pergunta antes do contexto | Modelo responde sem ver o contexto | F4: Pergunta viva é última |
| Constituição ambígua | Modelo interpreta livremente | Bullets curtos, instruções imperativas |
| Sem reiteração no bloco 4 | Em prompts longos, regra do topo enfraquece | Reiterar o crítico antes da pergunta |
| Sem sanitização do input | Prompt injection sobrescreve a constituição | Sanitizar antes do bloco 5 |
| Prompt como string no código | Sem rastreabilidade | Tratar como artefato versionado |

---

🔗 [Cap 09 Engenharia de Prompt](../02-capitulos/L1-C09-engenharia-prompt.md) · [Cap 11 Context Engineering](../02-capitulos/L1-C11-context-engineering.md) · [F4 PROMPT-EXT](../03-frameworks/L1-F4-prompt-ext.md) · [Repositório acompanhante](../../_repositorio-acompanhante/prompts/)



<div class="page-break"></div>


# APÊNDICE M — MANIFESTO DOS INVARIANTES DA IA
## Versão de bolso · página única destacável

> *Imprima. Cole na parede. Distribua ao time. Leve para a próxima decisão de IA.*

---

## OS 9 INVARIANTES

### 1 — PLAUSIBILIDADE
**"O modelo entrega o plausível, não o verdadeiro — e os dois coincidem, até a hora em que não."**
*Mecânica:* LLM é motor de plausibilidade; calibração de confiança é trabalho do operador, proporcional ao custo do erro.
*Violação típica:* aceitar número jurídico ou financeiro porque "soou certo".
🧭 Cap 02 · Cap 41 · *válido enquanto a arquitetura generativa atual dominar*

### 2 — EXTREMIDADES
**"O meio do contexto é onde a informação vai morrer."**
*Mecânica:* atenção alta nas pontas, diluída no centro; densidade de relevância vence volume.
*Violação típica:* enterrar a regra crítica no parágrafo 40 do prompt.
🧭 Cap 04 · F4 PROMPT-EXT · *válido enquanto a arquitetura transformer atual dominar*

### 3 — CAMADA DUPLA
**"Decore o padrão, consulte o número."**
*Mecânica:* o que muda em semanas vive em apêndice datado; o que dura por anos vive na cabeça.
*Violação típica:* memorizar "modelo X lidera benchmark Y" e ficar obsoleto no próximo release.
🧭 Cap 01 · Apêndice Vivo · F9 ROTA-DUPLA

### 4 — ENCAIXE
**"Escolha pelo padrão da tarefa, nunca pela versão da moda."**
*Mecânica:* decide-se modelo por eixo (código, mate, multimodal, contexto longo, custo), não pelo lançamento da semana.
*Violação típica:* migrar o stack para o release recente sem teste cego na carga real.
🧭 Cap 15 · F2 ENCAIXE-5

### 5 — CUSTO COMPOSTO
**"Trivial é o preço do token; o que quebra o orçamento é quantas vezes você o paga."**
*Mecânica:* custo = tokens × chamadas × tier × redundância; alavancas são arquiteturais.
*Violação típica:* otimizar prompt enquanto um loop de agente dispara 40 chamadas redundantes.
🧭 Cap 36 · F7 COMPOSTO-3T

### 6 — AUTONOMIA PROPORCIONAL
**"Só dê ao agente a autonomia que você consegue medir e desfazer."**
*Mecânica:* nível de agência = função da capacidade de rastrear e reverter.
*Violação típica:* agente com escrita em produção sem tracing nem kill switch.
🧭 Cap 12 · Cap 40 · F3 AGENTE-PROP

### 7 — TERMÔMETRO
**"IA sem eval é fé, não engenharia."**
*Mecânica:* nenhum sistema entra em produção sem detecção de regressão; prompt sem golden set é opinião.
*Violação típica:* trocar prompt "porque ficou melhor" sem dataset que prove que não piorou.
🧭 Cap 39 · F8 EVAL-PIRÂMIDE

### 8 — RESPONSABILIDADE INDELEGÁVEL
**"A IA executa; a responsabilidade tem sempre um nome humano."**
*Mecânica:* toda saída em produção tem dono, controle de acesso, trilha de auditoria, caminho de reversão.
*Violação típica:* "foi a IA que decidiu" como desculpa para decisão que ninguém assume.
🧭 Cap 42 · F6 GOV-INDELEGÁVEL

### 9 — OPERADOR
**"A IA multiplica competência e incompetência pelo mesmo fator."**
*Mecânica:* ganho vem do operador que sabe pedir, rejeitar e validar.
*Violação típica:* esperar que a IA cubra a falta de critério de quem a opera.
🧭 Cap 34 (L2) · Cap 44 · F1 DECID-IA

---

## A FRASE-ÂNCORA

> ## *Modelos passam. Método fica.*

---

## COMO USAR

| Situação | Pergunte-se |
|----------|-------------|
| Vou escolher um modelo | F2 (Inv. 4): qual o **encaixe** por eixo de tarefa? |
| Vou subir um agente | F3 (Inv. 6): tenho tracing e rollback proporcionais? |
| Vou trocar um prompt em produção | F8 (Inv. 7): rodou contra o **golden set**? |
| Vou apresentar a iniciativa à diretoria | F1 (Inv. 9) e F6 (Inv. 8): há **dono** e há **decisão** estruturada? |
| Vou cortar custo de IA | F7 (Inv. 5): mexi nas **3 alavancas arquiteturais**? |
| Vou citar um benchmark | (Inv. 3): conferi o **Apêndice Vivo** com data e fonte? |

---

## NOTA DE HONESTIDADE

Os Invariantes **1** (Plausibilidade) e **2** (Extremidades) dependem da arquitetura generativa atual. Arquiteturas futuras podem mudar a mecânica; os outros sete são princípios de prática e julgamento, independentes de arquitetura.

---

## ATRIBUIÇÃO

**Os 9 Invariantes da IA** — sistema proprietário de *Inteligência Aumentada* (Fabio Garcia, 2026).
Distribuição livre com atribuição. Versão original em [github.com/fabiogarcia/inteligencia-aumentada](https://github.com/fabiogarcia/inteligencia-aumentada) *(URL ilustrativa — confirmar)*.

🔗 **Aprofundamento:** [Cap 00M — Manifesto dos Invariantes](../01-manifesto/L1-C00M-manifesto-invariantes.md)
