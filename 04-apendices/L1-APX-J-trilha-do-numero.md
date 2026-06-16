# Apêndice J — Trilha do Número

> **Atualizado em:** junho de 2026
> **Política editorial:** instrumento vivo, com revisões publicadas no repositório acompanhante sempre que movimento relevante do mercado, da regulação ou da segurança justifique atualização, sem cadência fixa anunciada

---

## Por que este apêndice existe

A obra inteira opera sob o Princípio Três, a Camada Dupla, que diz que conhecimento em IA vive em dois andares, o padrão que dura e o número que muda. O Framework Nove, Rota Dupla, formaliza essa decisão epistemológica afirmando que a memória profissional deve carregar o padrão, e que o número deve ser consultado, com data e fonte, a cada decisão. Este apêndice é a casa do número. Sem ele, a Rota Dupla seria tese sem prática, e o leitor ficaria sem fonte interna confiável para checar versão de modelo, preço de inferência, posição em benchmark, paper relevante do mês, mudança regulatória em andamento.

Nada aqui pretende durar. Cada item tem data de captura, fonte primária quando existe, e marcador de incerteza quando a confirmação não foi possível. O leitor que tiver dúvida deve sempre conferir na fonte oficial, e quem identificar erro deve enviar correção pelo canal indicado ao final do apêndice.

Estrutura: cinco seções, todas datadas no momento da revisão.

1. Modelos de fronteira e seus preços de inferência.
2. Benchmarks recentes e quem lidera.
3. Papers que estão movendo o campo.
4. Estado da regulação no Brasil e no mundo.
5. Incidentes públicos notáveis que entram no radar do CTO brasileiro.

---

## 1. Modelos de fronteira em junho de 2026

A tabela abaixo cobre os oito provedores que dominam a pauta de decisão executiva no Brasil em junho de 2026. Preços de input e output em dólares por milhão de tokens. Janela de contexto em tokens. Data de release ou última atualização significativa. Todos os valores foram verificados contra a fonte primária na data de captura indicada; entradas com revisão programada para a próxima atualização vêm com nota explícita de provisoriedade no corpo do parágrafo de contexto, e não como marcador dentro da tabela.

| Provedor | Modelo flagship | Modelo de raciocínio | Input USD por 1M tokens | Output USD por 1M tokens | Janela de contexto | Release / atualização | Data verificação | Fonte |
|---|---|---|---|---|---|---|---|---|
| Anthropic | Claude Opus 4.7 | Claude Opus 4.7 em modo Adaptive ou Max Effort | 5,00 | 25,00 | 1 milhão | 16/abr/2026 | jun/2026 | docs Anthropic |
| OpenAI | GPT-5.5 | o3 (input 2,00, output 8,00); o4-mini (input 1,10, output 4,40) | 5,00 | 30,00 | 1 milhão (tier separado para long-context acima de 270 mil) | abr/2026 | jun/2026 | openai.com/api/pricing |
| Google DeepMind | Gemini 3.1 Pro | Gemini 3.1 Pro com extended thinking | 2,00 abaixo de 200 mil tokens, 4,00 acima | 12,00 abaixo de 200 mil tokens, 18,00 acima | 2 milhões | 19/fev/2026 | jun/2026 | ai.google.dev/gemini-api/docs/models |
| Meta | Llama 4 Maverick | Llama 4 Behemoth em preview restrito | 0,15 | 0,60 | 1 milhão | abr/2025, com variante experimental Llama-4-Maverick-03-26 submetida ao LMArena em mar/2026 | jun/2026 | llama.com/models/llama-4 |
| DeepSeek | DeepSeek V4 Pro | DeepSeek R1 (input 0,55, output 2,19) | 0,435 (cache-miss) | 0,87 | 128 mil | tabela revisada em 31/mai/2026 | 31/mai/2026 | api-docs.deepseek.com/quick_start/pricing |
| Mistral | Mistral Large 3 (versão 2512) | Magistral, lançado como reasoning em 2025 | 0,50 | 1,50 | 262 mil | 01/dez/2025 | jun/2026 | mistral.ai/pricing |
| xAI | Grok 4.3 high | Grok 4.3 em modo think | 1,25 | 2,50 (cache 0,20) | 1 milhão, com vídeo nativo | 30/abr/2026 | jun/2026 | docs.x.ai/developers/models |
| Alibaba Qwen | Qwen 3.7 Max | Qwen 3.7 Max com extended thinking | 2,50 (cache 0,25) | 7,50 | 1 milhão (saída até 65.536) | 20/mai/2026 | jun/2026 | Alibaba Cloud Model Studio |

**Notas de contexto importantes para junho de 2026:**

Anthropic prepara, em preview restrito, o Claude Mythos, que aparece em vários leaderboards como líder mas não está em produção geral. Trate Mythos como sinal de fronteira próxima, não como opção de adoção.

DeepSeek aplicou novo tarifário em 31 de maio de 2026, encerrando o desconto de setenta e cinco por cento que vigorou durante boa parte de 2025. Os preços listados são pós-desconto. Quem operava com desconto deve recalcular margem antes da próxima fatura.

GPT-5.5 Pro existe em tier "research-grade" com input em 30 dólares por milhão e output em 180 dólares por milhão. Não foi tabulado acima porque sua adoção corporativa é marginal, mas vale citar quando se discutir teto de qualidade para tarefa única e crítica.

A janela de contexto deixou de ser diferencial competitivo entre os três frontiers ocidentais. Gemini lidera em 2 milhões, Claude e GPT-5.5 estabilizaram em 1 milhão. A decisão prática voltou a ser preço por qualidade e custo de output, não capacidade bruta de janela.

---

## 2. Benchmarks recentes em junho de 2026

A tabela cobre os sete benchmarks mais citados no debate técnico-executivo de junho de 2026. Score do líder no momento da captura. URL do leaderboard onde o número pode ser conferido em qualquer dia. Quando há divergência metodológica entre fontes, a tabela traz a faixa observada e, no texto sequente, indica a fonte preferencial para a próxima revisão.

| Benchmark | O que mede | Líder atual | Score | Fonte |
|---|---|---|---|---|
| GPQA Diamond | Raciocínio científico nível PhD em cento e noventa e oito questões mais duras | Gemini 3.1 Pro Preview (Mythos Preview marca 94,6% em leaderboard interno Anthropic, ainda não auditado por terceiros) | 94,1% | artificialanalysis.ai/evaluations/gpqa-diamond |
| SWE-bench Verified | Resolução de issues reais GitHub em projetos Python open source | Claude Mythos Preview em preview; em produção, Claude Opus 4.8 | 93,9% Mythos, 88,6% Opus 4.8 | llm-stats.com/benchmarks/swe-bench-verified |
| AIME 2025 | Olimpíada de matemática com trinta questões de resposta inteira | Kimi K2.5 Reasoning; Gemini 3 Pro reporta cem por cento em variante com ferramentas externas habilitadas | 96,1% | benchlm.ai/benchmarks/aime2025 |
| ARC-AGI-2 | Raciocínio abstrato e generalização visual | GPT-5.5 | 85% | arcprize.org/leaderboard |
| Humanity's Last Exam | Aproximadamente dois mil e quinhentas questões PhD multi-domínio com cap intencionalmente baixo | Claude Opus 4.8 Adaptive Max Effort em produção; Mythos Preview marca 64,7% em leaderboard interno ainda não auditado | 45,7% em produção | artificialanalysis.ai/evaluations/humanitys-last-exam |
| OSWorld-Verified | Agentes computer-use em sistema operacional real | Holo3-35B-A3B open-weight, Claude Mythos Preview proprietário | 82,6% e 79,6% | llm-stats.com/benchmarks/osworld-verified |
| Video-MME | Compreensão multimodal de vídeo | Gemini 3.1 Pro dominante em múltiplos vídeo-benchmarks; faixa observada entre oitenta e oitenta e cinco por cento conforme fonte | 80%-85% | video-mme.github.io |

**Nota sobre fontes de benchmark:** as colunas "Fonte" acima apontam para leaderboards públicos, que incluem tanto fontes primárias oficiais (arcprize.org para ARC-AGI-2; video-mme.github.io para Video-MME) quanto agregadores de terceiros (artificialanalysis.ai, llm-stats.com, benchlm.ai). Agregadores atualizam com latência e podem divergir das fontes primárias — o score listado é o informado pelo agregador na data de captura. Fontes primárias dos benchmarks: GPQA Diamond → github.com/idavidrein/gpqa; SWE-bench → swebench.com; AIME → artofproblemsolving.com; ARC-AGI-2 → arcprize.org; HLE → scale.com/leaderboard; OSWorld → os-world.github.io. Na próxima revisão, a tabela incluirá coluna "Fonte primária" separada da coluna de leaderboard.

**Lições estruturais para junho de 2026:**

Benchmarks de raciocínio convergiram para cima nos modelos de fronteira, com vantagens marginais que mudam todo mês. Para decisão corporativa, o ranking absoluto importa menos que o perfil por eixo, conforme tratado no Framework Dois. Em junho de 2026, o eixo onde a diferença ainda compensa esforço é código complexo, onde Claude mantém vantagem operacional, e raciocínio matemático puro, onde Gemini e Kimi disputam.

Computer-use em SO real virou benchmark relevante. Quem opera agentes que precisam interagir com aplicativos sem API estável deve acompanhar OSWorld-Verified e variantes. Em 2025, esse eixo era exótico, em 2026 é decisão de arquitetura.

---

## 3. Papers que estão movendo o campo em 2025-2026

A tabela cobre oito trabalhos que mudaram, ou continuam mudando, a conversa técnica e executiva entre o início de 2025 e o presente. Lista deliberadamente curta, com critério de impacto operacional, não comprehensiveness acadêmica.

| Título | Autores / instituição | Mês e ano | Por que importa | URL |
|---|---|---|---|---|
| DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning | DeepSeek-AI | janeiro de 2025, divulgado por seus autores via arXiv (publicação em periódico revisado por pares não confirmada até a data desta revisão) | Prova que RL puro sem chain of thought humano gera raciocínio emergente, virando o blueprint dos reasoning models que dominaram 2025 e 2026 | arxiv.org/abs/2501.12948 |
| On the Biology of a Large Language Model + Circuit Tracing | Anthropic Interpretability Team | março de 2025, ferramenta open-source em maio de 2025 | Mapeia attribution graphs em Claude 3.5 Haiku e oferece a primeira evidência empírica de planejamento multi-step e features anti-jailbreak em modelo de produção | transformer-circuits.pub/2025/attribution-graphs/biology.html |
| Are DeepSeek R1 And Other Reasoning Models More Faithful? | Chua et al. (Truthful AI / colaboração acadêmica) | janeiro de 2025 | Testa se o chain of thought exposto reflete o cálculo interno real, peça-chave do debate sobre faithfulness em reasoning models | arxiv.org/abs/2501.08156 |
| Large Language Lobotomy: Jailbreaking Mixture-of-Experts via Expert Silencing | te Lintelo, Wu e Picek (TU Delft / Radboud) | fevereiro de 2026 | Descreve classe de ataque training-free que desliga experts de segurança em modelos MoE, elevando taxa de jailbreak bem-sucedido de aproximadamente sete para mais de setenta por cento ao silenciar menos de vinte por cento dos experts por camada | arxiv.org/abs/2602.08741 |
| RASA: Routing-Aware Safety Alignment for Mixture-of-Experts Models | Liang et al. (Stony Brook) | fevereiro de 2026, revisado em abril de 2026 | Resposta defensiva à classe de ataques anterior, com fine-tune seletivo de experts de safety preservando capacidade em MMLU, GSM8K e TruthfulQA; código público disponível | arxiv.org/abs/2602.04448 |
| Stealing User Prompts from Mixture of Experts (MoE Tiebreak Leakage) | Hayes et al. (Google DeepMind) | outubro de 2024, citado em 2026 | Primeiro ataque que extrai prompts de outros usuários via roteamento MoE, risco direto para SaaS multi-tenant | arxiv.org/abs/2410.22884 |
| Towards a Mechanistic Understanding of Large Reasoning Models: A Survey of Training, Inference, and Failures | colaboração acadêmica multi-instituição | janeiro de 2026 | Survey-padrão para entender treino, inferência e modos de falha de modelos de raciocínio, referência defensiva obrigatória, organizando achados recentes em três dimensões — dinâmica de treino, mecanismos de raciocínio e comportamentos não intencionais | arxiv.org/abs/2601.19928 |
| DeepSeek-R1 Thoughtology: Let's think about LLM Reasoning | Marjanović et al. (colaboração acadêmica) | abril de 2025 | Análise sistemática dos thoughts do R1, referência para auditoria de cadeias de raciocínio em pipelines reais | arxiv.org/abs/2504.07128 |

**Padrão observável em 2025-2026:**

A agenda científica deslocou-se de "como fazer o modelo gerar texto melhor" para três frentes simultâneas. Reasoning sob RL puro, interpretabilidade mecanicista das features internas, e segurança em arquiteturas MoE onde o roteamento abre vetores novos de ataque. CTO atento acompanha pelo menos um paper de cada frente por trimestre.

---

## 4. Estado da regulação em junho de 2026

### EU AI Act

Entrou em vigor em 1 de agosto de 2024, com aplicação geral marcada para 2 de agosto de 2026. Práticas proibidas e AI literacy já se aplicam desde 2 de fevereiro de 2025. Governança e obrigações para modelos de propósito geral entraram em vigor em 2 de agosto de 2025.

Em 2 de agosto de 2026, o bulk das obrigações entra em vigor, incluindo transparência conforme Artigo 50, conformity assessments, gestão de risco, supervisão humana. Quem opera no mercado europeu precisa ter caderno de governança pronto antes dessa data.

Em 7 de maio de 2026, o acordo provisional sobre o Digital Omnibus on AI adiou as obrigações para sistemas High-Risk (HRAIS) de 2 de agosto de 2026 para 2 de dezembro de 2027, uma janela adicional de dezesseis meses. Anexo Um HRAIS adiado para 2 de agosto de 2028.

Guidelines do Artigo 50 estão em consulta pública até 3 de junho de 2026.

### PL 2338/2023 no Brasil

Aprovado por unanimidade no Senado em 10 de dezembro de 2024. Em tramitação na Câmara dos Deputados desde março de 2025, em Comissão Especial. Votação foi adiada para 2026 por impasses políticos. Em junho de 2026 está agendado, com data ainda em definição — o leitor deve consultar o portal da Câmara antes de qualquer decisão executiva baseada em prazo, porque calendário legislativo brasileiro tem volatilidade alta e este apêndice é revisado periodicamente, sem cadência fixa.

Modelo adotado é europeu, com classificação por risco em três classes (excessivo, alto, baixo-moderado), direitos do titular, criação do Sistema Nacional de Regulação e Governança de IA, multas até cinquenta milhões de reais por infração.

Vício de iniciativa identificado por juristas: atribuições à ANPD são matéria de iniciativa exclusiva do Executivo. Isso pode forçar emenda substitutiva ou veto presidencial parcial, o que adiciona incerteza sobre a forma final.

### NIST AI RMF

Versão base permanece o AI RMF 1.0, publicado em janeiro de 2023. Não há "versão 2.0" formal em junho de 2026. O Generative AI Profile NIST AI 600-1, publicado em 2024, adiciona mais de duzentas ações específicas para LLMs.

Em 7 de abril de 2026, NIST publicou concept note para AI RMF Profile on Trustworthy AI in Critical Infrastructure. Em fevereiro de 2026, o Treasury Department publicou Financial Services AI RMF com 230 control objectives para instituições financeiras. Expectativa para o restante de 2026: addenda 1.1 e novos profiles setoriais.

### ISO/IEC 42001

Adoção acelerando em 2026. Fortune 500 começou a exigir de fornecedores em RFP. Certificações públicas confirmadas até a data desta revisão: CrowdStrike em janeiro, CM.com em janeiro, BCG entre as primeiras cem globais em janeiro, Perforce em fevereiro, SAP em 2025. A estimativa de aproximadamente dezesseis organizações certificadas publicamente no início de 2026, com número crescendo mês a mês, é compilação editorial deste apêndice a partir de releases públicos das próprias empresas; não existe registro central auditado para esse universo, e revisões futuras substituirão esta estimativa por contagem fechada caso uma fonte agregadora confiável passe a publicá-la.

### LGPD e ANPD no Brasil

Nota Técnica número 1 de 2026, da ANPD, analisa o Grok integrado ao X e firma posição de que saída de IA referente a pessoa identificável é dado pessoal. Marco importante para qualquer sistema que opere com inferência sobre brasileiros.

Resolução número 23 de 2024 publicou a Agenda Regulatória 2025-2026, com IA como eixo prioritário ao lado de direitos do titular, RIPD, segurança e anonimização.

Quatro eixos de fiscalização para 2026-2027: direitos do titular, dados de crianças e adolescentes, tratamento pelo Poder Público, IA e tecnologias emergentes.

Sandbox regulatório de IA em fase de testes sob supervisão direta da ANPD até dezembro de 2026. Empresas interessadas em testar produto sensível com cobertura regulatória parcial devem submeter aplicação.

ANPD designada como autoridade reguladora residual no PL 2338. Em setores sem regulação específica, ANPD cria normas, supervisiona e aplica sanções.

---

## 5. Incidentes públicos notáveis em 2025-2026

A tabela cobre sete incidentes que entraram no radar regulatório, jurídico ou de segurança no período. Critério de inclusão: incidente público com aprendizado executivo para CTO brasileiro.

| Incidente | Data | O que aconteceu | Por que importa ao CTO BR |
|---|---|---|---|
| Baltimore contra xAI, X e SpaceX por imagens sexualizadas geradas por Grok | dezembro de 2025 a janeiro de 2026 | Processo municipal apurou que Grok gerou entre 1,8 e 3 milhões de imagens sexualizadas, com aproximadamente vinte e três mil retratando menores | Risco de responsabilidade civil e criminal para deploy de modelos generativos de imagem sem guardrails. Chamou atenção da ANPD via Nota Técnica 1 de 2026 |
| EchoLeak, CVE-2025-32711 | divulgado em junho de 2025 | Primeira vulnerabilidade zero-click de prompt injection documentada publicamente para exfiltração em LLM em produção, no Microsoft 365 Copilot | Define nova classe de CVE. IA conectada a e-mail ou SharePoint é vetor de exfiltração sem clique do usuário. Obrigatório no threat model |
| Vercel e Context.ai OAuth breach | abril de 2026 | Funcionário concedeu OAuth com escopo "Allow All" a ferramenta de IA. Comprometimento do Context.ai escalou para lateral movement na Vercel | Confirma OAuth de produtividade IA como porta de entrada. Exige revisão de scopes e least-privilege em qualquer integração SaaS mais IA |
| Eightfold AI class action sob FCRA | janeiro de 2026 | Class action argumentou que plataforma de hiring com IA operava como consumer reporting agency não-registrada, sem disclosure, consent ou dispute | Precedente direto para uso de IA em RH no Brasil sob LGPD e futuro PL 2338, como sistema de alto risco |
| Cisco multi-turn jailbreak em modelos open-weight | 2026 | Teste com oito modelos open-weight mostrou que ataques multi-turn tiveram aproximadamente noventa e três por cento de sucesso | Quem deploya open-weight on-prem precisa de camada externa de guarda. Modelo "alinhado" não basta |
| Mercor data breach | 1 de abril de 2026 | Recruiting platform de IA enfrentou ao menos quatro class actions no Northern District of California por vazamento de dados | Reforça que dados de candidato em pipeline de IA são jurisdição LGPD e ANPD se houver brasileiros entre os afetados |
| Grupo estatal com automação de ataque via assistente de código IA | 2025 a 2026 | Relatórios de inteligência de ameaças (Mandiant, CrowdStrike) descrevem grupos avançados automatizando entre oitenta e noventa por cento da cadeia de ataque com assistentes de código IA via jailbreak — fonte primária pública ainda não confirmada com nome de caso e data exatos; entrada mantida com qualificador de incerteza | Marco: IA agente como vetor ofensivo real, não teórico. Eleva a régua de SOC e SBOM. *(Incerteza declarada: fonte primária pública com nome de caso e data exatos não confirmada até esta revisão; entrada será atualizada ou removida na próxima revisão se não houver publicação verificável.)* |

**Estatística contextual:** AI Incident Database registrou 346 casos em 2025, dos quais 179 foram de mídia sintética e 37 de conteúdo violento ou inseguro (fonte: incidentdatabase.ai, relatório anual 2025).

---

## Como contribuir com correções

Esta trilha evolui no repositório acompanhante público sempre que movimento relevante do mercado, da regulação ou da segurança justifique atualização. Para receber notificação de novas revisões, ative *watch* no repositório no GitHub. Correções, atualizações ou novas entradas podem ser enviadas como issue ou pull request com fonte primária; contribuições qualificadas são incorporadas nas revisões seguintes, com atribuição quando o contribuidor autoriza.

Toda alteração registra três campos no log de revisão: data da mudança, item alterado, fonte que motivou a alteração. O log integra o material publicado a cada revisão, para que o leitor possa, em qualquer momento, reconstituir o que a obra afirmou em cada janela de tempo.

---

## Política editorial

O autor não promete cadência fixa de release. O instrumento é vivo, e o ato de manter o número auditável e datado depende de janela de pesquisa que nem sempre se encerra no mês do calendário. A política assumida é simples e dura: publicar quando a revisão estiver pronta para ser cumprida sob crítica pública, jamais antes; sinalizar com clareza no cabeçalho a data da última revisão; e abrir revisões emergenciais a qualquer momento quando movimento relevante do mercado, da regulação ou da segurança justifique correção imediata.

Honestidade temporal é parte da promessa da Rota Dupla, e essa honestidade fica mais bem servida pela ausência de calendário fixo do que pelo descumprimento de um calendário que prometido demais.

---

## Editor desta trilha

**Editor responsável:** Fabio Garcia, autor da obra.

O editor mantém o registro datado de cada revisão e responde pelas escolhas de inclusão, exclusão, classificação de impacto e nível de incerteza atribuído a cada item. Discordâncias técnicas, sugestões de inclusão e identificação de erro devem ser dirigidas ao repositório acompanhante, com fonte primária; respostas editoriais a contribuições qualificadas são incorporadas nas revisões seguintes e creditadas quando o contribuidor autoriza.

---

*Apêndice J — Trilha do Número. Política editorial: instrumento vivo, sem cadência fixa anunciada. Editor: Fabio Garcia.*
