# Apêndice K — Gabaritos Comentados
## *Soluções estruturadas para exercícios e projetos da obra*

> Este apêndice oferece estruturas de resposta para os exercícios práticos e projetos dos capítulos. Não são respostas únicas. São gabaritos que mostram o método de pensar que cada exercício pretende ativar. Use como referência para autoavaliação, nunca como atalho para pular o esforço.

> **Nota editorial — cobertura e escopo (junho de 2026):** este apêndice cobre, na edição atual, os gabaritos dos exercícios e projetos dos seguintes capítulos: Introdução (Os Nove Princípios), Como Modelos Funcionam, Tokens, RAG, Engenharia de Prompt, Evals, LLMOps, Alignment, Governança, Trade-offs e Roadmap Pessoal. Os capítulos C08 (Fine-tuning), C10 (Reasoning), C12-C13 (Agentes), C14 (AI Engineering) e C15-C16 (Posicionamento de Mercado) não têm gabarito nesta edição. Os gabaritos pendentes serão publicados no repositório acompanhante à medida que forem finalizados — ative *watch* no repositório em [github.com/falercia/inteligencia-aumentada-recursos](https://github.com/falercia/inteligencia-aumentada-recursos) para receber notificação de novas publicações.

---

## Como usar este apêndice

1. Faça o exercício primeiro. Sem isso, o gabarito vira leitura passiva.
2. Compare estrutura, não conteúdo. O gabarito mostra como pensar, não o que pensar.
3. Customize ao seu domínio. Cada gabarito é genérico; sua resposta deve ser específica.
4. Reverifique depois de noventa dias. Gabaritos evoluem com o leitor.

---

## Introdução — Os Nove Princípios (C00P + C01)

### Exercício 1 — Diagnóstico do time
**Estrutura esperada:** lista de nove violações típicas, uma por princípio, com exemplo específico do time. Identificar os três mais críticos com sinal concreto, por exemplo, "regressão silenciosa não detectada nos últimos seis meses" para o Princípio 7.

### Exercício 2 — Auditoria de decisões
**Estrutura esperada:** tabela com três decisões cruzadas com os nove princípios. Marcar respeitado ou violado e descrever o que mudaria.

### Projeto — Cartaz dos Princípios da empresa
**Critério de qualidade:** uma página A3, com violação típica adaptada à linguagem do seu setor. Outro executivo lê e reconhece os nove princípios pela sua versão, sem ambiguidade.
**Rubrica de proficiência:** *Insuficiente* — princípios copiados sem adaptação ao setor ou com menos de seis dos nove presentes. *Proficiente* — todos os nove princípios presentes com violação típica adaptada ao vocabulário real da organização. *Excelente* — cartaz é adotado pelo time, com exemplos de incidentes reais da casa que ilustram cada violação.

---

## Como modelos funcionam — Capítulo 02

### Projeto — Plano para apresentar o transformer à diretoria — Capítulo 02
**Estrutura:** slide um, analogia do estagiário que leu tudo; slide dois, predição de próximo token; slide três, Q/K/V em alto nível, sem fórmula; slide quatro, consequência prática da Plausibilidade; slide cinco, Camada Dupla aplicada à diretoria.
**Rubrica de proficiência:** *Insuficiente* — apresentação com jargão técnico não traduzido ou sem conexão com decisão executiva. *Proficiente* — cinco slides com analogia, consequência prática e Camada Dupla; diretoria entende sem perguntar o que é transformer. *Excelente* — diretoria usa o vocabulário da apresentação em reuniões posteriores sem precisar abrir o livro.

---

## Tokens — Capítulo 03

### Exercício 1 — Auditoria de tokens da operação
**Estrutura:** levantamento de input e output médio por feature; cálculo da fração que é prompt e fração que é resposta; identificação do maior consumidor de tokens.

### Projeto — Plano de economia
**Estrutura:** aplicar o Custo Composto em Três Tempos; identificar tier dominante; identificar redundância; plano em trinta dias.
**Rubrica de proficiência:** *Insuficiente* — plano sem cálculo de custo composto ou com alavanca única identificada. *Proficiente* — três alavancas mapeadas (tier, redundância, arquitetura), com estimativa de economia em percentual e plano de trinta dias. *Excelente* — plano implementado, com leitura de fatura antes e depois validando a estimativa.

---

## RAG — Capítulo 06

### Projeto — Caderno de RAG do produto
**Estrutura:** definição de resposta certa; estratégia de chunking; modelo de embedding; reranking; política de top-k; eval de faithfulness.
**Rubrica de proficiência:** *Insuficiente* — caderno com menos de quatro dos seis elementos ou sem eval de faithfulness. *Proficiente* — todos os seis elementos presentes, com golden set mínimo e precision@5 medida. *Excelente* — caderno em uso em produção, com ciclo de revisão documentado e melhoria mensurável em faithfulness ao longo de um mês.

---

## Engenharia de prompt — Capítulo 09

### Projeto — Aplicar Engenharia de Prompt Estendida em cinco prompts
**Estrutura:** para cada prompt, reescrever nos cinco blocos canônicos. Comparativo de antes e depois, com justificativa por bloco.
**Rubrica de proficiência:** *Insuficiente* — menos de três prompts reescritos ou sem justificativa por bloco. *Proficiente* — cinco prompts reescritos com os cinco blocos canônicos identificados, comparativo antes/depois com melhoria objetiva demonstrada. *Excelente* — prompts reescritos em uso em produção, com medição de diferença de qualidade em golden set de pelo menos dez casos.

---

## Evals — Capítulo 21

### Exercício 1 — Classificação de falhas
**Estrutura:** para cada falha listada, marcar qual camada da pirâmide a teria capturado; identificar a camada mais frágil hoje.

### Projeto — Caderno de Evals v1
**Critério de qualidade:** outro engenheiro lê e roda eval contra mudança nova sem perguntar mais que três coisas. Inclui golden set de trinta a cinquenta itens, LLM-as-judge calibrado com correlação igual ou superior a 0,7 contra humano, adversarial com vinte ou mais casos, política de bloqueio em CI.
**Rubrica de proficiência:** *Insuficiente* — eval sem golden set definido ou sem política de bloqueio em CI. *Proficiente* — golden set de trinta a cinquenta itens, LLM-as-judge com correlação acima de 0,7 contra humano, e política de bloqueio documentada. *Excelente* — eval bloqueou pelo menos uma mudança de prompt ruim em pipeline real, com evidência de postmortem de regressão capturada.

---

## LLMOps — Capítulo 22

### Exercício 1 — Diagnóstico dos sete pilares
**Estrutura:** matriz de sete pilares por cinco níveis de maturidade; identificar os dois mais frágeis; plano de sessenta dias.

### Projeto — Caderno de LLMOps v1
**Critério de qualidade:** outro engenheiro responde sem perguntar qualquer das sete perguntas executivas do capítulo.
**Rubrica de proficiência:** *Insuficiente* — caderno cobre menos de quatro dos sete pilares ou sem evidência de monitoramento em produção. *Proficiente* — todos os sete pilares documentados com status atual e plano de melhoria em sessenta dias. *Excelente* — caderno em uso real, com engenheiro externo capaz de responder qualquer das sete perguntas sem perguntar mais nada.

---

## Alignment — Capítulo 23

### Exercício 3 — Mini-constituição corporativa
**Estrutura:** sete princípios em português, cada um em uma frase, sem jargão. Submetido a par sênior para revisão.

### Projeto — Caderno de Alignment Operacional
**Critério de qualidade:** outro engenheiro sênior responde "como nosso sistema lida com pedido de conselho médico não-supervisionado?" sem precisar perguntar.
**Rubrica de proficiência:** *Insuficiente* — caderno sem política explícita para classe de pedido de alto risco ou sem exemplo concreto da ferramenta adotada. *Proficiente* — mini-constituição com sete princípios em português, exemplo de pedido de alto risco tratado, e critério de revisão por par sênior. *Excelente* — caderno em uso em onboarding de novos engenheiros, com evidência de pelo menos um caso de pedido fora do escopo tratado conforme a política.

---

## Governança — Capítulo 24

### Projeto — Caderno de Governança v1
**Critério de qualidade:** outro executivo responde sem ambiguidade: "quem é o accountable por X?", "qual a maturidade do controle Y?", "quando é o próximo simulado?".
**Rubrica de proficiência:** *Insuficiente* — caderno sem RACI específico ou sem plano de incidente assinado. *Proficiente* — seis blocos preenchidos, RACI com Accountable nominal, AUP com exemplo concreto, e próxima revisão com data marcada. *Excelente* — caderno apresentado à diretoria e aprovado, com data de primeiro simulado agendada e AI Council com mandato escrito.

---

## Trade-offs — Capítulo 25

### Projeto — Cardápio de Trade-offs do produto
**Critério de qualidade:** outro executivo defende a arquitetura em reunião externa, com cliente, conselho ou auditor, sem precisar perguntar.
**Rubrica de proficiência:** *Insuficiente* — cardápio com menos de três trade-offs ou sem justificativa por eixo. *Proficiente* — todos os trade-offs documentados com critério de escolha, alternativa descartada e razão do descarte. *Excelente* — executivo externo usa o cardápio para defender a arquitetura em reunião real sem precisar consultar o autor do documento.

---

## Roadmap pessoal — Capítulo 26

### Projeto — Apresentação à diretoria
**Critério de qualidade:** diretoria aprova o roadmap em uma reunião, com mandato formal sobre IA.
**Rubrica de proficiência:** *Insuficiente* — roadmap sem datas, sem métricas de sucesso ou sem responsável por marco. *Proficiente* — roadmap com três marcos com data, métrica de sucesso por marco, lista de dependências entre eles, e análise de risco por iniciativa. Para autoavaliação individual: os três marcos têm datas fixas, métricas verificáveis, e dependências explícitas. *Excelente* — roadmap aprovado em reunião com mandato formal, ou, em autoestudo, executado com dois marcos concluídos dentro do prazo.
