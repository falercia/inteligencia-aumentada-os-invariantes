# Apêndice A — Glossário Completo
## *Vocabulário canônico da obra*

> Glossário organizado por categoria. Termos próprios da obra marcados com **★** (sistema proprietário) ou **◆** (uso técnico canônico). Termos de mercado em uso recorrente sem marcação.

---

## I. Invariantes e sistema da obra (★)

**Camada Dupla.** ★ Invariante 3: separação entre padrão durável (na cabeça) e número volátil (em apêndice datado).

**Custo Composto.** ★ Invariante 5: a multiplicação tokens × chamadas × tier × redundância que escala em produção, não o preço por token isolado.

**Encaixe.** ★ Invariante 4: escolha de modelo por padrão de tarefa em cinco eixos, não por liderança de benchmark da rodada.

**Extremidades.** ★ Invariante 2: regra de que atenção decai no meio do contexto e densidade de relevância vence volume bruto.

**Operador.** ★ Invariante 9: a IA multiplica competência e incompetência pelo mesmo fator.

**Plausibilidade.** ★ Invariante 1: o modelo entrega o plausível, não o verdadeiro.

**Responsabilidade Indelegável.** ★ Invariante 8: toda decisão de IA em produção tem único nome humano accountable.

**Autonomia Proporcional.** ★ Invariante 6: nível de agência é função da capacidade de medir e desfazer.

**Termômetro.** ★ Invariante 7: IA sem eval é fé, não engenharia.

**Autoavaliação.** ★ Critério objetivo de fechamento de cada capítulo da obra, em cinco dimensões.

**Os Nove Frameworks.** ★ Sistema que opera os invariantes na prática. Índice: Método de Decisão para Adotar IA · Diagnóstico de Encaixe entre Tarefa e Modelo · Escala de Propriedade do Agente · Engenharia de Prompt Estendida · Matriz de Cobertura de Integrações · Governança Indelegável · Custo Composto em Três Tempos · Pirâmide da Avaliação · Rota Dupla de Adoção. Ver entradas individuais abaixo.

**Método de Decisão para Adotar IA.** ★ Framework do Invariante 9: sequência de perguntas que separa o problema que a IA resolve do problema que o operador precisa resolver — evita adoção por moda e ancora a decisão em impacto mensurável.

**Diagnóstico de Encaixe entre Tarefa e Modelo.** ★ Framework do Invariante 4: avalia qual modelo serve melhor a uma tarefa específica em cinco eixos (latência, custo, qualidade, contexto, capacidade modal), independente do ranking de benchmark vigente.

**Escala de Propriedade do Agente.** ★ Framework do Invariante 6: gradua o nível de autonomia de um agente em função da capacidade de medir e desfazer cada ação — de execução totalmente supervisionada a agente com aprovação apenas em exceções.

**Engenharia de Prompt Estendida.** ★ Framework dos Invariantes 2 e 3: estrutura que organiza o conteúdo do contexto usando densidade nas extremidades, camada de padrão no system prompt e número volátil em variável — separa o que dura do que muda.

**Matriz de Cobertura de Integrações.** ★ Framework dos Invariantes 6 e 4: mapeia quais ferramentas e fontes de dados um agente ou sistema de IA acessa, com grau de confiança e cobertura por caso de uso — identifica lacunas antes de ir a produção.

**Governança Indelegável.** ★ Framework do Invariante 8: define para cada decisão de IA o nome humano accountable, o mecanismo de rollback e o critério de escalação — torna a responsabilidade auditável, não apenas declarada.

**Custo Composto em Três Tempos.** ★ Framework dos Invariantes 5 e 9: calcula o custo real de uma feature de IA em três horizontes (chamada, mês, produto), multiplicando tokens × chamadas × tier × redundância — evita surpresas de fatura em escala.

**Pirâmide da Avaliação.** ★ Framework do Invariante 7: estrutura de evals em camadas — base determinística, meio com golden set e LLM-as-judge, topo humano, com adversarial transversal. Cada camada detecta o que a anterior não detecta.

**Rota Dupla de Adoção.** ★ Framework do Invariante 3: separa a adoção de IA em duas rotas paralelas — rota de padrão (o que muda lentamente, vai na cabeça ou no CLAUDE.md) e rota de número (o que muda rápido, vai em apêndice datado ou variável de ambiente).

---

## II. Fundamentos de IA

**Agente.** ◆ Sistema de IA que recebe objetivo, decompõe em subtarefas, executa com ciclos de percepção-ação-reflexão, usa tools externas, até cumprir o objetivo. Diferente de chatbot: unidade de operação é a tarefa completa, não a resposta.

**AGI (Artificial General Intelligence).** Sistema de IA com capacidade equivalente a humana em qualquer tarefa cognitiva. Hoje, conceito disputado entre laboratórios.

**ASI (Artificial Superintelligence).** Sistema que excede capacidade humana em todos os domínios cognitivos.

**Atenção (mechanism).** ◆ Operação no transformer que decide quais tokens importam e quanto. Implementada via projeções Query/Key/Value e softmax.

**Benchmark.** Conjunto padronizado para medir capacidade. Exemplos: MMLU, GPQA, SWE-bench, HumanEval, ARC-AGI, OSWorld, Video-MME, HLE.

**Chain of Thought (CoT).** Técnica de prompt que induz o modelo a externalizar raciocínio passo a passo antes da resposta. Sobe acurácia em tarefas multipasso.

**Constitutional AI (CAI).** Técnica de alinhamento em que princípios em linguagem natural ("constituição") são aplicados por outro modelo IA para gerar feedback de treinamento. Formulada originalmente pela Anthropic e adotada com variações por outros laboratórios.

**Context Engineering.** Disciplina que orquestra hierarquicamente o que entra no contexto do modelo (system prompt, memória, RAG, histórico) com caching e medição.

**Deep Learning.** Subcategoria de Machine Learning com redes neurais profundas.

**DPO (Direct Preference Optimization).** Substituto do PPO em RLHF; otimização direta sobre pares de preferência sem modelo de recompensa dedicado.

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

**Prompt engineering.** Disciplina de construir prompts profissionalmente. Ver também Context Engineering, que expande a disciplina para orquestração hierárquica de múltiplas fontes no contexto.

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

**Reasoning model (modelo de raciocínio).** ◆ Modelo treinado para externalizar cadeia de raciocínio longa antes de produzir resposta. A cadeia interna (*thinking*) não é visível ao usuário em todas as implementações. Custo por token é tipicamente mais alto; ganho em tarefas que exigem múltiplos passos lógicos é documentado. Exemplos: OpenAI o1/o3, Claude com extended thinking, DeepSeek-R1. Base do capítulo C14B.

**Zero-shot.** Prompt sem exemplos; só instrução.

---

## III. Avaliação e evals

**Adversarial set.** ◆ Conjunto de casos que sabidamente quebram o sistema (jailbreak, injection, sycophancy, viés).

**Calibração de juiz.** Validação de LLM-as-judge contra humano em ≥30 itens; correlação alvo ≥0,7.

**Faithfulness.** Métrica de quão fiel a saída é a uma fonte (especialmente em RAG).

**Golden set.** ◆ Conjunto fixo de casos com gabarito que serve de referência estável para detectar regressão.

**LLM-as-judge.** ◆ Uso de LLM para avaliar saída de outro LLM segundo rubrica.

**Pirâmide de Evals.** ★ Base determinística, meio com golden set e LLM-as-judge, topo humano, com camada adversarial transversal.

**Regressão silenciosa.** Queda de qualidade que não aparece em métrica agregada mas existe em subgrupo.

**Rubrica.** Critério estruturado para julgamento (humano ou LLM-as-judge).

**Scorecard.** Comparação automatizada baseline × candidato em cada release.

**Vibe-eval.** Anti-padrão: rodar 5 casos manuais e decidir.

---

## IV. LLMOps e operação

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

## V. Alinhamento

**Helpful, Harmless, Honest.** ◆ Trilogia que sintetiza alinhamento, formulada inicialmente pela Anthropic e amplamente referenciada na literatura.

**Interpretabilidade mecanicista.** ◆ Mapeamento dos circuitos internos do modelo que produzem comportamentos específicos.

**Mech Interp.** Abreviação de Interpretabilidade Mecanicista.

**Over-refusal.** Modelo recusa pedidos legítimos por excesso de cautela.

**Red-teaming.** Teste adversarial sistemático de comportamento problemático.

**Sandbagging.** Modelo finge ser menos capaz para escapar de avaliação.

**Sparse Autoencoders.** Técnica para identificar *features* legíveis em ativações.

---

## VI. Governança

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

## VII. Padrões de produto e plataformas

> Padrões de interface e plataforma que afetam arquitetura de produto com IA.

**Agentes de programação assistida.** Categoria de ferramentas tipo CLI, IDE e ambiente integrado para escrita e revisão de código com IA. Exemplos: Claude Code (Anthropic), Cursor, GitHub Copilot, Codex (OpenAI), Gemini Code Assist (Google).

**Connectors / integrações nativas.** Integrações pré-instaladas que ligam o assistente a fontes corporativas. Disponíveis em diferentes formatos nas principais plataformas comerciais.

**MCP (Model Context Protocol).** Padrão aberto, proposto pela Anthropic, para conectar modelos a ferramentas e dados externos. Tem adoção crescente por outros fornecedores.

**Famílias de modelos por tier.** Padrão de mercado em que cada fornecedor oferece três a quatro tiers de capacidade e custo. Exemplos: Haiku, Sonnet e Opus (Anthropic); GPT-4o-mini, GPT-4o e o-series (OpenAI); Gemini Flash, Pro e Ultra (Google); Llama em diferentes tamanhos (Meta).

**Projects / Workspaces.** Ambiente persistente com instruções, arquivos e histórico. Padrão presente em Claude Projects, ChatGPT Projects, Gemini Gems e similares.

**Skills, Subagents, Routines.** Encapsulamentos versionados de comportamento, delegação para agentes especializados e fluxos nomeados. Conceitos canônicos que aparecem com nomes distintos entre fornecedores.

**Scheduled Tasks.** Execução agendada de tarefas por agente, presente em diferentes plataformas comerciais.

---

## VIII. Casos brasileiros da obra (cenários ilustrativos)

**Atlas Strategy.** ★ Consultoria estratégica brasileira; caso de eval por incidente de relatórios.

**Banco Solar.** ★ Fintech brasileira; caso de atendimento híbrido por tier.

**Pólice.io.** ★ Marketplace brasileiro de seguros; caso de loop com cartão de crédito.

**Vianna, Castro e Almeida.** ★ Banca de M&A brasileira; caso de DD assistida.

---

## IX. Regulação e normas

**AI Act.** Regulamentação europeia (UE 2024/1689).

**ANPD.** Autoridade Nacional de Proteção de Dados (Brasil).

**ISO/IEC 42001.** Sistema de gestão de IA (2023).

**LGPD.** Lei Geral de Proteção de Dados (Lei 13.709/2018), especialmente art. 20 (decisão automatizada).

**NIST AI RMF.** AI Risk Management Framework (NIST, 2023).

**PL de IA brasileiro.** PL 2338/2023, em tramitação no Senado Federal. Regime de responsabilidade e requisitos de transparência para sistemas de IA de alto risco.
