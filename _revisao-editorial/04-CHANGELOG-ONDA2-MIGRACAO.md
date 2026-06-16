# CHANGELOG — ONDA 2 (durabilidade + migração para a série)

**Objetivo:** transformar o *Os Invariantes* no volume de horizonte longo da série, tirando o perecível do papel para os companions que já existem.
**Backups:** manuscrito em `_backup-pre-onda2/`; repo recursos em `_backup-repos-pre-migracao/recursos/`.

## Placar
- **~14 mil palavras de conteúdo perecível removidas do livro** (APX-L −78%, APX-D, APX-F).
- **17 blocos perecíveis** (tabelas de modelos, benchmarks, preços, listas de repos) convertidos em **método + ponteiro** em C15/C16/C17/C18.
- **7 ponteiros "Camada viva"** inseridos no manuscrito.
- **Repo recursos** ganhou 4 áreas novas (`apendice-vivo`, `ferramentas`, `repos-curados`, `fontes`) + README atualizado.
- **deep-claude/apendice-vivo** declarado fonte única cross-vendor da série (cross-link).

## Arquitetura da camada viva (decisão)
Fonte ÚNICA de números cross-vendor = `deep-claude/apendice-vivo` (cadência mensal já existente). O recursos tem um `apendice-vivo/README.md` que é **ponteiro + método de leitura**, não dataset duplicado. Os Invariantes aponta para o companion recursos. Resultado: um só dataset para manter por mês.

---


---

# Changelog ONDA 2 — Durabilidade | Capítulos 15 a 18

**Princípio aplicado:** o que muda a cada release de modelo não fica no papel. Preço, ranking de modelo, benchmark numérico e nome de produto saem do texto; o método de avaliar e decidir fica. Cada bloco removido ganhou ponteiro para a camada viva.

**Ponteiro canônico inserido:**
> **Camada viva.** Esta seção ensina o método; os números que mudam (modelos, preços, benchmarks) vivem no **Apêndice Vivo da série**, atualizado mensalmente no repositório de recursos da obra (github.com/falercia/inteligencia-aumentada-recursos → `apendice-vivo`). Consulte lá a versão corrente antes de decidir.

---

## L1-C15-comparacao-modelos.md

### O que saiu (8 blocos perecíveis movidos para o Apêndice Vivo)

1. **Seção 15.3.1 — Panorama por padrão de especialização (completa):** nomes de modelos com versão (Claude Opus/Sonnet/Haiku, GPT premium/mini/nano, Gemini Pro/Flash, Grok, DeepSeek V3/R1, Z.AI GLM, Mistral, Llama), forças relativas atribuídas a cada família, data de criação do padrão MCP. Substituídos por: critérios duráveis de avaliação de família (tier premium/balanceado/compacto, eixo de especialização, licença) + ponteiro ao Apêndice Vivo.

2. **Seção 15.3.2 — Dimensão capacidade:** menção explícita de "Claude Opus, GPT premium, Gemini Pro" como os três frontier, e atribuição de força relativa específica a cada um. Substituída por: framing genérico de famílias frontier com eixos de especialização sem nomear versões.

3. **Seção 15.3.3 — Benchmarks (título e conteúdo):** "MMLU saturou perto de 90%", "Humanity's Last Exam — atualmente o benchmark mais difícil, nenhum modelo atinge metade da pontuação no momento desta edição". Substituídos por: categorias duráveis de benchmark (raciocínio científico, engenharia de software, matemática formal, raciocínio visual, agência em software, multimodalidade temporal, fronteira geral) com exemplos de referência rotulados + ponteiro ao Apêndice Vivo para líderes correntes e scores.

4. **Seção 15.4 — Framework de Decisão (perguntas e tabela):** nomes de modelos específicos como "Flash, Haiku, Mini", "GPT premium", "Gemini Pro", "Claude + Claude Code", "Claude Opus em SWE-bench Verified, historicamente". Coluna "Família que tende a vencer" substituída por "Como identificar o líder" + ponteiro ao Apêndice Vivo.

5. **Seção 15.5 — Exemplo memorável:** "Claude Haiku" como classificador; "modelo pequeno (Haiku)", "modelo balanceado (Sonnet)", "frontier multimodal (família Gemini Pro)". Substituídos por: "tier compacto", "tier balanceado", "frontier com força em multimodalidade" — denominações funcionais sem nomear versão.

6. **Seção 15.6 — Tendências:** "em 2026 já há paridade em muitas tarefas comuns"; chips específicos "Trainium da AWS, Tensor Processing Units do Google, silicon proprietário da Apple" + ponteiro ao Apêndice Vivo para chips e provedores relevantes no momento.

7. **Resumo executivo 15.8:** linhas "Família Claude", "Família GPT", "Família Gemini" com forças específicas; "Custo-benefício no frontier: Gemini premium, com flutuação por rodada". Substituídas por: forças descritas como eixos sem nomear família + ponteiro ao Apêndice Vivo.

8. **Checklist 15.9 e Exercício 15.11:** âncora temporal "em 2026"; nomes de modelos específicos no Exercício 2 ("Claude", "GPT", "Flash"). Substituídos por: linguagem de categoria + ponteiro ao Apêndice Vivo para versões pontuais.

### O que ficou (método preservado)

- Epígrafe e enquadramento do platô da fronteira (invariante)
- Analogia da frota de veículos (durável)
- Estrutura de três dimensões de comparação: capacidade, economia, alinhamento e segurança
- Framework Diagnóstico de Encaixe entre Tarefa e Modelo: 5 perguntas em árvore (sensibilidade → custo → multimodal → agência → default balanceado)
- Tabela de eixos de especialização com coluna de método de identificação do líder
- Exemplo memorável de roteamento com economia de US$ 380 mil (padrão ilustrativo, não ranking)
- Princípio de roteamento como arquitetura vs. decisão pontual
- Tendências estruturais: comoditização, especialização, hardware
- Conexões, perguntas de revisão, exercícios, projeto, autoavaliação

---

## L1-C16-open-source.md

### O que saiu (7 blocos perecíveis movidos para o Apêndice Vivo)

1. **Seção 16.3.1 — Família competitiva (completa):** lista detalhada de seis famílias com versões específicas (DeepSeek V3 671B MoE 37B ativos, DeepSeek R1, DeepSeek V3.1, Llama 3.3 e 4 com variantes 8B/70B/405B, Mistral Large 2/Mixtral 8x22B/Nemo/Codestral, Qwen 2.5 e 3 de 0.5B a 235B, Phi 4 14B, Gemma 3 2B/9B/27B) com detalhes de licença e integração específicos a cada família. Substituída por: cinco critérios duráveis de avaliação de qualquer família (licença, origem/jurisdição, qualidade por eixo/força em PT-BR, integração com engines de inferência, variantes de tamanho) + ponteiro ao Apêndice Vivo para a lista corrente.

2. **Seção 16.3.2 — Quantização (preço de GPU):** "custo de aluguel de aproximadamente 2 a 4 dólares por hora em provedor de nuvem com GPU dedicada". Substituído por: afirmação estrutural de viabilidade para PME + ponteiro ao Apêndice Vivo para preços correntes de hardware.

3. **Seção 16.3.6 — Aritmética de TCO (valores nominais):** "4.000 e 8.000 reais por mês" (GPU), "25.000 e 50.000 reais" (time sênior), limiares de requisições com valores nominais. Substituídos por: estrutura de componentes sem valores nominais + ponteiro ao Apêndice Vivo para aritmética corrente.

4. **Quadro 16.A — Matriz de TCO em 12 meses:** tabela completa com valores em reais (API ~600k, self-hosting ~530k, híbrido ~735k) e modelos específicos ("Claude Sonnet", "DeepSeek V3 INT4 em H100"). Substituída por: tabela de componentes estruturais (sem valores nominais) + lógica de qual cenário favorece cada rota + ponteiro ao Apêndice Vivo.

5. **Seção 16.4 — Exemplo memorável:** valores específicos em reais ("90.000 reais mensais", "180.000", "24.000"), modelos específicos ("GPT-4o", "DeepSeek V3"), provedor específico ("Magalu Cloud"). Substituídos por: padrão estrutural da migração com economia de 73% preservada como ordem de grandeza, denominações funcionais (modelo open source de fronteira, provedor com presença nacional).

6. **Resumo executivo 16.6:** linha "Família competitiva 2026: DeepSeek (MIT), Llama 3.3-4, Mistral (mista), Qwen (Apache), Phi (MIT), Gemma (restrita)". Substituída por: "Múltiplas famílias com licenças variadas — lista corrente no Apêndice Vivo".

7. **Epílogo:** âncoras temporais "em 2026" e "mapa de 2022". Substituídas por: formulação relativa sem data absoluta.

### O que ficou (método preservado)

- Conceito intuitivo da virada estrutural (narrativa de três janelas temporais com eventos nomeados onde necessário para contexto histórico)
- Analogia da frota corporativa (durável)
- Distinção open weights × open source no sentido estrito da OSI (definição estrutural)
- Técnicas de quantização: INT8, INT4, AWQ, GPTQ com trade-offs de qualidade (método durável)
- Distilação clássica e distilação de raciocínio como técnicas (método durável)
- Soberania de dados: LGPD, ANPD, driver brasileiro (estrutural, com ponteiro para versão corrente)
- Cinco componentes do TCO honesto: hardware, time, energia, atualização, risco operacional
- Seis critérios de decisão: volume, sensibilidade, qualidade de fronteira, maturidade do time, fine-tuning, portfolio
- Exemplo memorável: padrão de migração healthtech com resultados estruturais preservados
- Conexões, checklist, perguntas de revisão, exercícios, projeto, autoavaliação

---

## L1-C17-github-repos.md

### O que saiu (1 bloco perecível movido para repos-curados)

1. **Seção 17.6 — Lista corrente (completa):** oito repositórios com descrição de estado em "meados de 2026" (LangChain, LlamaIndex, vLLM, Ollama, OpenInterpreter, LiteLLM, MLflow, Weights & Biases), com fase do ciclo de vida, notas de encaixe e comparativos específicos. Substituídos por: instrução de como usar a lista viva + ponteiro ao repositório de recursos (github.com/falercia/inteligencia-aumentada-recursos → `repos-curados`) + protocolo de como comparar a leitura própria com a anotação da camada viva.

2. **Seção 17.12 — Referências:** "Repositórios usados como exercício de aplicação (estado observado em meados de 2026): LangChain, LlamaIndex, vLLM, Ollama, OpenInterpreter, LiteLLM, MLflow, Weights & Biases". Substituído por: ponteiro ao `repos-curados`.

### O que ficou (método preservado)

- Conceito intuitivo: inventário envelhece, método dura (durável)
- Analogia da auditoria de imóvel comercial em 30 minutos (durável)
- Seis critérios duráveis completos: sinais de vida, maturidade de release, qualidade de código, documentação operacional, padrão de governança, encaixe com o contexto
- Protocolo 30 minutos (Quadro 17.A): tabela com onde olhar, sinal de passa e sinal de falha por critério
- Ciclo de vida do repositório: cinco fases (hype, adoção real, maturidade, manutenção, abandono) com quatro sinais cada
- Quatro anti-padrões: estrelas, README de marketing, demonstração, post de blog
- Exemplo memorável: fintech que auditou 20 repositórios e descartou 14 (método, não lista)
- Conexões, checklist, perguntas de revisão, exercícios, projeto, autoavaliação

---

## L1-C18-economia-tokens.md

### O que saiu (1 bloco perecível reforçado com ponteiro)

1. **Seção 18.11 — Referências:** menção genérica a "Anthropic, OpenAI, Google" como provedores de onde verificar preços. Reforçada com ponteiro explícito ao Apêndice Vivo para tabela de preços por tier e por provedor atualizada mensalmente.

### Nota sobre o capítulo

O C18 estava substancialmente durável antes da intervenção. Não contém tabelas de preço por token, não cita versões específicas de modelo e não faz rankings. Os valores em reais no exemplo memorável (R$ 70 mil, R$ 180 mil etc.) são parte do padrão ilustrativo de um cenário composto — não são preços de API — e foram mantidos, pois o capítulo já os rotula como "cenário ilustrativo composto". A fórmula de custo composto, as três alavancas (T1/T2/T3), as sete alavancas em ordem de impacto e o processo estruturado de otimização são todos duráveis.

### O que ficou (método preservado — integralmente)

- Fórmula explícita de custo composto: tokens × preço × chamadas × redundância × tier
- As três alavancas arquiteturais: tier de modelo (T1), topologia de chamada (T2), tamanho de contexto (T3)
- As sete alavancas em ordem de impacto com economia típica em percentual
- Processo de otimização estruturada em oito semanas
- Exemplo memorável: SaaS que corrigiu erro de tier e reduziu custo de R$ 180 mil para R$ 60 mil
- Conexões com Princípio 5 (Custo Composto) e Framework F7

---

## Resumo consolidado

| Capítulo | Blocos perecíveis movidos | Método preservado |
|----------|--------------------------|-------------------|
| C15 — Comparação de Modelos | 8 | Sim — framework de decisão em 5 perguntas, eixos de especialização, roteamento como arquitetura |
| C16 — Open Source | 7 | Sim — critérios de avaliação, TCO estrutural, soberania LGPD, arquitetura híbrida |
| C17 — GitHub Repos | 1 (lista de 8 repos + referência) | Sim — 6 critérios, protocolo 30 min, ciclo de vida, anti-padrões |
| C18 — Economia de Tokens | 1 (reforço de ponteiro) | Sim — fórmula, alavancas, processo de otimização |
| **Total** | **17 blocos** | **Método integralmente preservado nos 4 capítulos** |

**Ponteiros inseridos:**
- `apendice-vivo` (github.com/falercia/inteligencia-aumentada-recursos → `apendice-vivo`): C15 (×4), C16 (×5), C18 (×1)
- `repos-curados` (github.com/falercia/inteligencia-aumentada-recursos → `repos-curados`): C17 (×2)

---

# Changelog Onda 2 — Apêndices L, D, E e F
## Durabilidade: enxugamento de conteúdo perecível para MÉTODO + PONTEIRO

**Data:** 2026-06-16
**Editor executivo:** Fabio Garcia
**Operação:** Onda 2 — Durabilidade

---

## APX-L — Biblioteca de Prompts Profissionais

**Arquivo:** `04-apendices/L1-APX-L-biblioteca-prompts.md`

**Antes:** ~13.000 palavras / 1.623 linhas. Conteúdo: Moldura de método + 30 fichas conceituais completas (cada uma com dor, domínio, F4, quando usar/evitar, anti-padrões, modelo recomendado, métrica de qualidade, versão executável) + changelog editorial de 6 prompts.

**Depois:** ~2.000 palavras / 215 linhas.

**O que saiu:**
- As 30 fichas conceituais completas (campos: dor, domínio, F4, quando usar/evitar, anti-padrões, modelo, métrica, versão executável)
- O changelog editorial de 6 prompts (P-LEG-01, P-MED-01, P-FIN-02, P-LEG-03, P-SUP-01, P-EDU-02)

**O que ficou:**
- Moldura de método completa (blockquote de abertura sobre o que cada prompt é e o que não envelhece)
- Seção "Por que este apêndice existe em duas camadas" com quadro de orientação (onde vive o quê)
- Seção "A anatomia que toda ficha aplica" — tabela F4, blocos `<prefill>` e `<self_critique>`, convenção de modelo, exemplo estrutural comentado em XML
- Seção "Padrões de operação" (7 padrões)
- Seção "Anti-padrões transversais de prompt" (tabela de 8 itens)
- Seção "Como ler as fichas" (tabela de 9 campos)
- **NOVO:** Tabela-índice dos 30 prompts (ID, nome, setor, princípio ilustrado, link para pasta no repo)
- Ponteiro canônico para `/prompts` no repositório
- Assinatura de fechamento do apêndice

**Razão:** As fichas completas são conteúdo XML/conceitual com nomes de modelo, benchmarks e detalhes de escopo que envelhecem com cada nova geração de modelo. O invariante — a anatomia F4, os 7 padrões, os 8 anti-padrões, a lógica de camada dupla — permanece. A tabela-índice preserva a navegabilidade para os 30 prompts sem congelar o detalhe no livro.

---

## APX-D — Ferramentas e Stack

**Arquivo:** `04-apendices/L1-APX-D-ferramentas.md`

**Antes:** ~2.500 palavras / 168 linhas. Conteúdo: Framework de seleção (D.0 e D.1 com tabela de 6 dimensões) + catálogo por categoria (D.2 a D.10: plataformas de inferência, modelos open weights, frameworks de agente, bancos vetoriais, observabilidade, evals, MCP, gestão de prompts, cadência de revisão).

**Depois:** ~600 palavras / 38 linhas.

**O que saiu:**
- D.2 — Plataformas de inferência (LLM-as-a-Service): tabela com 6 provedores e critério recomendado
- D.3 — Modelos open weights para self-host: tabela com 6 famílias e critério
- D.4 — Frameworks de agente e orquestração: tabela com 5 frameworks e critério
- D.5 — Bancos vetoriais: tabela com 6 opções e critério
- D.6 — Observabilidade e LLMOps: tabela com 5 ferramentas e critério
- D.7 — Frameworks de evals: tabela com 4 opções e critério
- D.8 — MCP: tabela com 4 itens e critério
- D.9 — Repositórios e gestão de prompts: tabela com 4 opções e critério
- D.10 — Cadência de revisão

**O que ficou:**
- D.0 — Argumento editorial (por que data explícita e critério importam mais que inventário)
- D.1 — Framework de 6 dimensões de seleção (tabela com dimensão, o que avaliar, sinal de risco)
- Ponteiro canônico para `ferramentas` no repositório
- Nota de fechamento descrevendo o que o catálogo cobre

**Razão:** O catálogo de ferramentas datado em junho/2026 é o item mais perecível da obra. Modelos são adquiridos, descontinuados, mudam de licença. O critério de seleção em 6 dimensões é o invariante: serve para avaliar qualquer ferramenta que apareça nos próximos 10 anos.

---

## APX-E — Leituras Complementares → Como montar sua dieta de informação

**Arquivo:** `04-apendices/L1-APX-E-leituras.md`

**Antes:** ~700 palavras / 67 linhas. Conteúdo: Listas de livros (fundamentos de IA, IA aplicada, governança) + blogs e newsletters + cursos.

**Depois:** ~1.100 palavras / 67 linhas (novo conteúdo de método + ponteiro).

**Operação:** Substituição completa do conteúdo. O arquivo foi transformado de lista de leituras em documento de método fundido com APX-F.

**O que saiu:**
- Lista de livros de fundamentos (Russell & Norvig, Bishop, Goodfellow, Murphy)
- Lista de livros de IA aplicada (Karpathy, Engelbart, Christian, Russell)
- Lista de livros de governança (Beyer, Doerr, Allspaw, Davenport)
- Lista de blogs e newsletters (10 itens)
- Lista de cursos (8 itens)

**O que entrou (novo conteúdo de método):**
- Argumento por que a dieta precisa de método (não de lista maior)
- 4 critérios para escolher fontes: especificidade de público, rastreabilidade de origem, cadência sustentável, atualização explícita de erro
- Arquitetura de dieta equilibrada em 3 camadas (fronteira / aplicação / contexto local)
- Tabela de cadência recomendada (blocos semanais com duração e propósito)
- Sinais de qualidade e sinais de alerta
- Como tratar a cena brasileira (uso correto de conteúdo nacional vs. internacional)
- Ponteiro para listas específicas no repositório (`fontes`)

**Incorporação do APX-F:** O conteúdo temático do APX-F (comunidade brasileira, critério de cena local) foi absorvido na seção "Como tratar a cena brasileira" e no argumento de arquitetura de 3 camadas. As listas específicas (newsletters, podcasts, conferências, pesquisadores, empresas) vão para o repositório junto com as listas do APX-E original.

---

## APX-F — Comunidade Brasileira de IA → Stub de redirecionamento

**Arquivo:** `04-apendices/L1-APX-F-newsletters.md`

**Antes:** ~2.300 palavras / 154 linhas. Conteúdo: Argumento da cena brasileira + 8 seções (newsletters, podcasts, conferências, comunidades online, pesquisadores, empresas, crítica honesta da cena, como contribuir).

**Depois:** ~250 palavras / 25 linhas (stub de redirecionamento).

**Operação:** Arquivo preservado (para não quebrar referências existentes) e transformado em stub que redireciona para APX-E e para o repositório.

**O que saiu:**
- As 8 seções de conteúdo (newsletters: 5 fontes com descrição; podcasts: 7 com nota editorial; conferências: 6; comunidades online: 5; pesquisadores: 5 + nota de extensão; empresas: 5 + lista de extensão; crítica honesta; como contribuir)

**O que ficou:**
- Título e nota de redirecionamento explicando a fusão
- Link para APX-E (método)
- Ponteiro canônico para `fontes` no repositório

**Razão:** O arquivo é mantido como stub para não quebrar sumário, índice ou referências cruzadas existentes. O conteúdo migrou para APX-E (método) e repositório (listas).

---

## Resumo de contagem (APX-L, foco do briefing)

| Versão | Palavras aprox. | Linhas |
|---|---|---|
| Antes (Onda 1) | ~13.000 | 1.623 |
| Depois (Onda 2) | ~2.000 | 215 |
| Redução | ~85% | ~87% |

---

# Migração de Conteúdo Perecível → Repo Recursos

> Data: 2026-06-16
> Operação: população do repositório COMPANION `inteligencia-aumentada-recursos` com conteúdo extraído do livro

---

## Arquivos criados no repositório recursos

**Repositório:** `github.com/falercia/inteligencia-aumentada-recursos`
**Caminho host base:** `/Users/fabiogarcia/Documents/Repositorios/Github falercia/inteligencia-aumentada-recursos/`

### 1. `apendice-vivo/README.md`
**Criado em:** 2026-06-16
**Conteúdo:** Ponteiro para a fonte única de números cross-vendor da série (modelos, preços, benchmarks, janelas de contexto) mantida no repositório `deep-claude/apendice-vivo`. Não duplica dados — explica a decisão editorial de fonte única (Camada Dupla, Princípio Três) e entrega o método vendor-neutral de ler comparações de modelo e preço de token: o que olhar, como normalizar, por que não memorizar ranking. Inclui tabela de estrutura do Apêndice Vivo do deep-claude, cadência de atualização mensal e capítulos relacionados do livro.
**Fonte primária:** APX-J (Trilha do Número), `deep-claude/apendice-vivo/README.md`

### 2. `ferramentas/README.md`
**Criado em:** 2026-06-16
**Conteúdo:** Catálogo completo de ferramentas e stack extraído do APX-D do livro. Cobre oito categorias: plataformas de inferência (D.2), modelos open weights para self-host (D.3), frameworks de agente e orquestração (D.4), bancos vetoriais (D.5), observabilidade e LLMOps (D.6), frameworks de evals (D.7), MCP (D.8) e gestão de prompts (D.9). A coluna de critério de seleção em seis dimensões (Maturidade, Adoção, Custo, Encaixe com stack brasileira, Suporte, Estabilidade) foi preservada como cabeçalho do catálogo. Estado de cada ferramenta referenciado como "junho/2026". Nota de data e cadência de revisão no cabeçalho. Tom vendor-neutral.
**Fonte primária:** `_backup-pre-onda2/04-apendices/L1-APX-D-ferramentas.md`

### 3. `repos-curados/README.md`
**Criado em:** 2026-06-16
**Conteúdo:** Lista de repositórios GitHub extraída do Cap 17 do livro (seção 17.6 "Lista corrente como exercício de aplicação"). Estruturada com o Protocolo de 30 Minutos (tabela dos seis critérios duráveis com onde olhar, sinal de passa e sinal de falha) e as quatro armadilhas clássicas (estrelas, README de marketing, demonstração, post de blog) como cabeçalho antes da lista — para que o método apareça antes do inventário. Inclui descrição do ciclo de vida do repositório (cinco fases com sinais). Data de observação junho/2026 declarada com aviso explícito de que a lista envelhece e o método não.
**Fonte primária:** `_backup-pre-onda2/02-capitulos/L1-C17-github-repos.md`

### 4. `fontes/README.md`
**Criado em:** 2026-06-16
**Conteúdo:** Fusão do APX-E (Leituras Complementares) e APX-F (Comunidade Brasileira de IA em 2026) em arquivo único, organizados por tipo: livros de fundamento técnico, livros de IA aplicada, livros de governança e operação, blogs e newsletters em inglês (divididos em fonte de provedor vs. análise independente), cursos e recursos de aprendizado, newsletters brasileiras, podcasts brasileiros (divididos em dedicados a IA vs. tecnologia ampla), comunidades online, conferências brasileiras e crítica honesta da cena brasileira. Critérios de curadoria declarados no cabeçalho (profundidade sobre divulgação, fonte primária verificável, validade temporal declarada). Data de revisão no cabeçalho; revisão anual para a seção de comunidade brasileira.
**Fonte primária:** `_backup-pre-onda2/04-apendices/L1-APX-E-leituras.md` e `L1-APX-F-newsletters.md`

---

## Arquivo editado no repositório recursos

### 5. `README.md` (raiz do repositório) — edição aditiva
**Editado em:** 2026-06-16
**O que mudou:** Adicionadas quatro novas linhas na tabela "O que vive aqui" (`/apendice-vivo`, `/ferramentas`, `/repos-curados`, `/fontes`) e quatro novas linhas na tabela de status "Outras pastas" (seção "Estado atual"). Nenhuma linha existente foi removida ou alterada.

---

## Decisões editoriais registradas

- **Não duplicar números.** O `apendice-vivo/README.md` é ponteiro, não cópia. A decisão de manter modelos, preços e benchmarks exclusivamente no `deep-claude/apendice-vivo` evita inconsistência quando os números mudarem.
- **Critério antes da lista.** Em `repos-curados/README.md` e `ferramentas/README.md`, o critério de avaliação aparece antes do inventário — aplicação direta do que o Cap 17 prega sobre postura epistêmica.
- **Fusão APX-E + APX-F.** As duas fontes foram fundidas em `fontes/README.md` porque são complementares e o leitor que busca "onde aprender" ou "onde encontrar comunidade" não deveria precisar navegar para dois arquivos separados.
- **Backups estáveis como fonte.** Todo conteúdo foi extraído dos arquivos em `_backup-pre-onda2`, não dos arquivos vivos do livro, para estabilidade da base.
