---
title: "Inteligência Aumentada"
lang: pt-BR
---



<div class="page-break"></div>


# CAPÍTULO 43
## TRADE-OFFS CANÔNICOS DA IA

---

> *"Não existe decisão de IA sem trade-off. Existe decisão sem consciência do trade-off. Quem se acomoda na segunda paga preço pela primeira."*

---

> 🧭 **Invariante-mãe:** **Invariante 4 — Encaixe** — *"Escolha pelo padrão da tarefa, nunca pela versão da moda."*
> Invariante secundário: **Inv. 9 — Operador** (consciência do trade-off é função do operador).
> Capítulo-âncora dos frameworks F2, F5, F7. Conecta a Caps 06, 08, 12, 16, 36, 40.

---

## 43.1 — O CONCEITO INTUITIVO

Toda decisão de IA em ambiente corporativo se reduz, no fim, a uma família pequena de **trade-offs canônicos**. Não são novos, não são exóticos, e não vão mudar nos próximos dez anos. RAG ou fine-tuning, ou nenhum dos dois? Agente autônomo ou workflow determinístico? Modelo fechado ou open source self-hosted? Onde sacrificar latência, qualidade ou custo? Automação plena ou human-in-the-loop? Generalismo ou especialização? Cada trade-off tem três a quatro eixos que decidem o lado certo para uma situação específica. Quem domina os eixos decide rápido e correto; quem decide por intuição refaz a decisão a cada trimestre, com custo crescente.

Este capítulo é o **cardápio executivo** de IA. É a referência consultada antes de qualquer decisão de arquitetura, antes de qualquer aprovação de iniciativa, antes de qualquer migração técnica. Não substitui os capítulos que aprofundam cada trade-off — RAG está no Cap 06, fine-tuning no Cap 08, agentes no Cap 12, open source no Cap 16, custo no Cap 36, autonomia no Cap 40 —, e sim sintetiza, num lugar único, a decisão por eixos que cada capítulo desenvolve.

A regra de ouro é não tratar nenhum dos seis trade-offs como **decisão binária**. Cada um é triângulo, raramente dicotomia. RAG e fine-tuning podem coexistir. Agente e workflow podem alternar. Aberto e fechado podem coabitar no mesmo stack. Generalista e especialista podem ser roteados. Quem encara o trade-off como decisão de A ou B perde a flexibilidade arquitetural que torna a operação sustentável.

---

## 43.2 — ANALOGIA: A CARTA DO RESTAURANTE

Pense num restaurante sério. Você não chega pedindo "o melhor prato". Você lê a carta, identifica o que combina com sua fome, seu paladar do dia, seu orçamento, o tempo que tem, o vinho que vai pedir. Há ali, sob cada item, um trade-off explícito — proteína vegetal ou animal, técnica longa ou rápida, sazonalidade, fusão ou tradicional. O chef do bom restaurante não decide pelo cliente; oferece o cardápio honesto e deixa a escolha consciente. O cliente bem informado decide rápido, e a refeição faz sentido.

Trade-offs canônicos de IA são o cardápio do CTO. Você lê os seis itens, identifica o que combina com o caso de uso, o orçamento, a regulação, a maturidade do time. Sob cada item, há eixos honestos. Nenhum item é universalmente melhor; cada um tem situações onde brilha e outras onde é desperdício. O CTO maduro consulta o cardápio antes de cada decisão; o imaturo escolhe pelo que está na moda.

A analogia ilumina três pontos. Primeiro, o trade-off é **decisão de adequação**, não de superioridade. Segundo, o trade-off é **consciente**: ser surpreendido pelo eixo que você não considerou é falha de método. Terceiro, o trade-off é **repetível**: a mesma decisão pode ser revisada quando o contexto mudar, sem culpa.

---

## 43.3 — OS SEIS TRADE-OFFS CANÔNICOS

### Trade-off T1 — RAG × Fine-tuning × Prompt enriquecido

**Pergunta executiva:** *"Quero conhecimento atualizado, comportamento personalizado, ou os dois?"*

| Opção | Quando faz sentido | Quando é desperdício |
|-------|--------------------|-----------------------|
| **RAG** | Conhecimento muda toda semana; corpus grande; rastreabilidade exigida; equipe operando sem time de ML | Conhecimento é estável por anos; corpus pequeno |
| **Fine-tuning** | Comportamento específico (tom, formato, terminologia interna); domínio estável; volume alto que paga o custo de treino | Decisão de prestígio sem caso de uso claro; expectativa de "tirar a censura" |
| **Prompt enriquecido** | Caso simples; contexto curto; operação ainda em prototipagem | Conhecimento volumoso; necessidade de rastreabilidade; volume crescente |

**Eixo decisor:** frequência de mudança do conhecimento × tamanho do corpus × custo aceitável de atualização.

🔗 Aprofundamento: [Cap 06 RAG](L1-C06-rag.md), [Cap 08 Fine-tuning](L1-C08-fine-tuning.md), [Cap 11 Context Engineering](L1-C11-context-engineering.md).

---

### Trade-off T2 — Agente autônomo × Workflow determinístico

**Pergunta executiva:** *"O caminho até a resposta é conhecido, ou descoberto?"*

| Opção | Quando faz sentido | Quando é desperdício |
|-------|--------------------|-----------------------|
| **Agente autônomo** | Variabilidade alta no caminho da resposta; explorar fontes diversas; tarefa de pesquisa ou síntese aberta | Caminho conhecido e padronizado; auditabilidade exigida em cada passo |
| **Workflow determinístico** | Caminho mapeado em 80%+ dos casos; auditoria por passo necessária; reversibilidade exigida; custo composto sob controle | Tarefa exige descoberta; cobertura impossível de exaustivo |

**Eixo decisor:** variabilidade do caminho × auditabilidade exigida × custo composto (F7).

⚠️ **Anti-padrão clássico:** escolher agente autônomo porque "tem N cenários", quando workflow determinístico cobriria os N-1 mais comuns com auditabilidade total a 1/10 do custo composto.

🔗 Aprofundamento: [Cap 12 Agentes](L1-C12-agentes.md), [Cap 40 LLMOps](L1-C40-llmops.md), [F3 AGENTE-PROP](../03-frameworks/L1-F3-agente-prop.md).

---

### Trade-off T3 — Modelo fechado × Open source self-hosted

**Pergunta executiva:** *"Preciso de soberania de dados, controle de custo ou ponta de qualidade?"*

| Opção | Quando faz sentido | Quando é desperdício |
|-------|--------------------|-----------------------|
| **Modelo fechado (vendor)** | Ponta de qualidade em capacidade crítica; sem time dedicado de infra/ML; cadência de release importa | Restrição regulatória sobre saída de dado; volume altíssimo com margem apertada |
| **Open source self-hosted** | Soberania de dado obrigatória; volume permite TCO menor que API; time maduro de ML/ops | Sem time dedicado; sem golden set para sustentar a escolha; cadência de release alta |

**Eixo decisor:** soberania de dado × TCO real × ponta de qualidade × maturidade de ops.

🔗 Aprofundamento: [Cap 16 Open Source](L1-C16-open-source.md), [Cap 15 Comparação de modelos](L1-C15-comparacao-modelos.md).

---

### Trade-off T4 — Latência × Qualidade × Custo (o triângulo)

**Pergunta executiva:** *"Onde está minha restrição dominante?"*

O triângulo é regra clássica de engenharia. Otimizar um canto sempre custa em algum dos outros dois. Não existe "rápido, bom e barato" como combinação livre; existe combinação restrita ao envelope possível em um modelo dado.

| Otimizar | Custa em |
|----------|----------|
| **Latência** | Qualidade (modelo menor, menos passos) ou Custo (caching agressivo, pré-computação) |
| **Qualidade** | Latência (modelo maior, mais passos) ou Custo (modelo premium) |
| **Custo** | Latência (cache + batch) ou Qualidade (modelo pequeno) |

**Eixo decisor:** identificação clara da restrição dominante no caso de uso real. Tarefa de conversação síncrona prioriza latência; tarefa de relatório regulatório prioriza qualidade; tarefa de classificação em volume prioriza custo.

🔗 Aprofundamento: [Cap 36 Economia de Tokens](L1-C36-economia-tokens.md), [F7 COMPOSTO-3T](../03-frameworks/L1-F7-composto-3t.md).

---

### Trade-off T5 — Automação plena × Human-in-the-loop

**Pergunta executiva:** *"Qual o custo de um erro silencioso?"*

| Opção | Quando faz sentido | Quando é desperdício |
|-------|--------------------|-----------------------|
| **Automação plena** | Erro reversível com custo baixo; volume alto; revisão humana inviável em escala | Erro irreversível ou de altíssimo custo; regulação exige revisão humana; domínio sensível |
| **Human-in-the-loop** | Erro irreversível ou caro; regulação exige (LGPD art. 20, AI Act); domínio sensível; operação ainda em maturação | Volume torna revisão humana inviável; erro reversível e barato |

**Eixo decisor:** reversibilidade × frequência × consequência do erro.

A regra prática: começar com human-in-the-loop e migrar para automação plena conforme o golden set, o adversarial e a operação madurem. Não inverter a ordem.

🔗 Aprofundamento: [Cap 39 Evals](L1-C39-evals.md), [Cap 41 Alignment](L1-C41-alignment.md), [Cap 42 Governança](L1-C42-governanca.md), [F3 AGENTE-PROP](../03-frameworks/L1-F3-agente-prop.md).

---

### Trade-off T6 — Generalismo × Especialização

**Pergunta executiva:** *"Modelo geral com prompt forte, ou modelo especializado?"*

| Opção | Quando faz sentido | Quando é desperdício |
|-------|--------------------|-----------------------|
| **Modelo geral + prompt forte** | Domínio estável; volume moderado; sem tempo para construir golden set robusto; necessidade de mover rápido | Domínio nicho com vocabulário próprio; volume altíssimo com margem apertada |
| **Modelo especializado** | Domínio nicho (jurídico, clínico, código); volume justifica custo de treinamento; golden set robusto disponível | Domínio geral; volume pequeno; cadência alta de mudança no domínio |

**Eixo decisor:** volume × estabilidade do domínio × disponibilidade de golden set × custo de treino vs operação.

🔗 Aprofundamento: [Cap 08 Fine-tuning](L1-C08-fine-tuning.md), [Cap 16 Open Source](L1-C16-open-source.md), [F2 ENCAIXE-5](../03-frameworks/L1-F2-encaixe-5.md).

---

## 43.4 — DIAGRAMAS

> 📊 **Diagrama 43.1 — Matriz dos 6 trade-offs canônicos**
>
> *(SVG planejado: `imagens/L1-C43-img-01-matriz-trade-offs.svg`)*
>
> Matriz 6×4 com cada trade-off em uma linha, eixos de decisão nas colunas (pergunta executiva, opção A, opção B, eixo decisor).

> 📊 **Diagrama 43.2 — Árvore de decisão integrada**
>
> *(SVG planejado: `imagens/L1-C43-img-02-arvore-decisao.svg`)*
>
> Fluxograma único que percorre os 6 trade-offs em sequência sugerida (T4 triângulo → T1 → T5 → T2 → T6 → T3), com cada nó conectando ao próximo conforme decisão tomada.

> 📊 **Diagrama 43.3 — Triângulo Latência × Qualidade × Custo**
>
> *(SVG planejado: `imagens/L1-C43-img-03-triangulo.svg`)*
>
> Visualização clássica do triângulo de engenharia aplicada a IA.

---

## 43.5 — EXEMPLO MEMORÁVEL: O E-COMMERCE QUE ESCOLHEU AGENTE QUANDO WORKFLOW BASTAVA

> ⚠️ **Cenário ilustrativo** — composto a partir de padrões observados em e-commerces brasileiros de médio porte durante adoção de IA em atendimento e operação entre 2024 e 2026; números são realistas mas não identificam empresa específica.

E-commerce brasileiro de moda, ~280 colaboradores, ~1,4 milhão de pedidos/ano, operando em 2025. Decisão: automatizar classificação e roteamento de pedidos de reembolso. O time técnico levantou 27 cenários distintos (defeito, tamanho errado, atraso, arrependimento, fraude, troca, devolução parcial, e variações por categoria). A proposta foi um **agente autônomo** que pudesse navegar todos os 27 com flexibilidade e descobrir variantes não previstas.

A diretoria aprovou. Implementação em 8 semanas. Resultado em produção: tempo médio de classificação caiu de 14 minutos (humano) para 3 minutos (agente). Diretoria satisfeita. CFO assinou o investimento.

Três meses depois, três problemas convergiram. Primeiro, **fatura mensal de IA passou de R$ 12 mil para R$ 78 mil**. O agente, em cada classificação, fazia em média 6 chamadas ao modelo, com loops imprevisíveis em casos ambíguos. Segundo, **auditoria do CS revelou inconsistência**: o mesmo cenário, com input ligeiramente diferente, era classificado de formas distintas em 11% dos casos. Terceiro, em uma auditoria regulatória (Procon), o e-commerce não conseguiu reconstruir o caminho exato da decisão em 3 de 5 amostras pedidas, porque o agente não tinha tracing por passo nem rationale explícito.

Uma consultoria foi contratada. A análise revelou o erro estrutural: a empresa tinha caído na armadilha clássica do trade-off T2, escolhendo agente autônomo quando workflow determinístico cobriria a maioria com auditabilidade total. Dos 27 cenários, **24 eram cobertos por regras conhecidas e estáveis** — categoria de produto + motivo declarado + janela de pedido + status atual. Os 3 restantes (ambiguidade, suspeita de fraude, caso multi-categoria) é que justificavam intervenção do agente, sob supervisão humana.

A migração para **workflow determinístico para os 24 cenários estáveis + agente sob supervisão para os 3 ambíguos** levou 6 semanas. Resultado: fatura caiu para R$ 9 mil/mês (abaixo do baseline pré-IA), consistência subiu para 99,2%, tempo médio caiu mais 18% (workflow é mais rápido que agente), auditabilidade ficou total nos 24 cenários e parcial nos 3 restantes (com rationale registrado).

A lição é estrutural. *Em 80%+ dos casos, workflow determinístico bem desenhado é melhor que agente autônomo — mais barato, mais rápido, mais auditável, mais consistente. Agente é a ferramenta certa para descoberta, não para padrão. Quem confunde paga em três frentes ao mesmo tempo: fatura, consistência e auditabilidade.*

> 🎯 **PARA EXECUTIVOS**
> Toda vez que o time técnico propor "agente autônomo" para um caso com N cenários, faça a pergunta: "destes N cenários, quantos são conhecidos e estáveis hoje?". Se a resposta for "80% ou mais", a proposta correta é workflow determinístico para os conhecidos e agente sob supervisão para o restante. Inverter essa ordem custa caro nos três eixos do trade-off T2.

---

## 43.6 — QUANDO USAR / QUANDO EVITAR

**Consultar o cardápio dos 6 trade-offs sempre que:**
- Iniciativa nova de IA está sendo aprovada
- Migração técnica está sendo considerada
- Fornecedor está sendo avaliado
- Arquitetura corrente está sendo revisada
- Decisão de cliente Enterprise depende de defender a arquitetura
- Auditoria interna ou externa está sendo preparada

**Evitar usar como receita rígida** quando o contexto exigir nuance específica. Os trade-offs são bússola, não mapa exato; a decisão final ainda demanda julgamento do operador (Inv. 9).

---

## 43.7 — VANTAGENS E LIMITAÇÕES

| Vantagem | Limitação |
|----------|-----------|
| Acelera decisão de arquitetura com cardápio explícito | Não substitui análise específica do caso de uso |
| Evita decisões por moda e por hype | Requer disciplina de consultar antes de propor |
| Cria vocabulário comum entre tech e diretoria | Em casos limítrofes, eixos não decidem por si só |
| Habilita revisão consciente quando contexto muda | Trade-off lido como dicotomia binária empobrece a decisão |
| Conecta os capítulos anteriores em sistema | Aplicado mecanicamente vira checklist sem força |

---

## 43.8 — CONEXÕES COM OUTROS CAPÍTULOS

- 🔗 Cap 06 RAG (T1), Cap 08 Fine-tuning (T1, T6)
- 🔗 Cap 12 Agentes (T2), Cap 15 Comparação (T3, T6), Cap 16 Open source (T3)
- 🔗 Cap 36 Custo (T4), Cap 40 LLMOps (T2, T5)
- 🔗 Cap 39 Evals (sustenta T5), Cap 41 Alignment (sustenta T5), Cap 42 Governança (regulação no T5)
- 🔗 F2 ENCAIXE-5, F3 AGENTE-PROP, F5 MCP-COBERTURA, F7 COMPOSTO-3T, F8 EVAL-PIRÂMIDE

---

## 43.9 — RESUMO EXECUTIVO

| Trade-off | Pergunta | Eixo decisor |
|-----------|----------|--------------|
| T1 RAG × Fine-tuning × Prompt | Conhecimento atualizado ou comportamento personalizado? | Frequência × corpus × custo |
| T2 Agente × Workflow | Caminho é conhecido? | Variabilidade × auditabilidade × custo composto |
| T3 Fechado × Open source | Soberania, custo ou ponta? | Soberania × TCO × ponta × ops |
| T4 Latência × Qualidade × Custo | Onde está minha restrição? | Triângulo: dois às custas do terceiro |
| T5 Automação × HITL | Custo de erro silencioso? | Reversibilidade × frequência × consequência |
| T6 Generalismo × Especialização | Geral + prompt forte ou especializado? | Volume × estabilidade × eval × custo |

---

## 43.10 — CHECKLIST DO CAPÍTULO

- [ ] Recitar os 6 trade-offs em ordem
- [ ] Citar a pergunta executiva de cada
- [ ] Identificar o eixo decisor dominante de cada trade-off
- [ ] Classificar 3 decisões recentes na minha operação pelos trade-offs
- [ ] Defender por que workflow determinístico vence agente autônomo em 80% dos casos típicos
- [ ] Defender por que automação plena sem HITL é desperdício em domínio sensível
- [ ] Mapear quais trade-offs sua arquitetura corrente "ignorou" sem perceber
- [ ] Apresentar o cardápio à diretoria em 10 minutos
- [ ] Reconhecer, em três frases recentes do time, qual trade-off está sendo violado por intuição

---

## 43.11 — PERGUNTAS DE REVISÃO

1. Por que o trade-off não é dicotomia binária?
2. Em que situação RAG e fine-tuning coexistem com proveito?
3. Qual a armadilha clássica do T2 (agente × workflow)?
4. Por que o T4 (triângulo) é regra clássica de engenharia, não específica de IA?
5. Por que começar com HITL e migrar para automação é melhor que o inverso?
6. Em que situação modelo especializado vence o geral, mesmo com custo maior?
7. Como os trade-offs T1, T3 e T6 se entrelaçam?
8. Por que "ignorou o trade-off T5" é violação direta do Invariante 8?

---

## 43.12 — EXERCÍCIOS PRÁTICOS

**Exercício 1 — Auditoria de decisões.** Liste 6 decisões de arquitetura de IA tomadas na sua organização nos últimos 12 meses. Para cada uma, identifique qual dos 6 trade-offs estava em jogo, qual lado foi escolhido, e qual o eixo decisor. Avalie em retrospecto se a decisão sustentaria o cardápio.

**Exercício 2 — Roteamento por trade-off.** Para uma feature do seu produto, percorra os 6 trade-offs em ordem. Documente a decisão de cada um com justificativa em ≤1 parágrafo. Compare com a arquitetura atual; identifique divergências.

**Exercício 3 — Defesa executiva.** Prepare apresentação de 10 minutos para diretoria explicando os 6 trade-offs e como eles se aplicam à arquitetura atual. Defenda a arquitetura ou proponha mudança fundamentada.

**Exercício 4 — Cardápio adaptado.** Reescreva os 6 trade-offs adaptados à linguagem do seu setor (com vocabulário do seu domínio). Submeta a um par sênior.

---

## 43.13 — PROJETO DO CAPÍTULO

**Construir o Cardápio de Trade-offs do seu produto.** Entregável em 4-6 páginas:

1. Os 6 trade-offs canônicos com a decisão tomada em cada um para a feature principal
2. Justificativa em ≤1 parágrafo por trade-off, conectando ao eixo decisor
3. Plano de revisão (trimestral)
4. Critério de gatilho para revisão antecipada (custo cruza X, volume cresce Y, regulação muda)
5. Apresentação em 10 minutos para a diretoria

**Critério de qualidade.** Outro executivo, lendo o cardápio, consegue defender a arquitetura em reunião externa (cliente Enterprise, conselho, auditor) sem perguntar.

---

## 43.14 — REFERÊNCIAS PRINCIPAIS

📚 **Trade-offs canônicos de engenharia**
- Brooks, F. *The Mythical Man-Month* (1975/1995) — fundamentos do triângulo
- Beck, K. *Extreme Programming Explained* (2000) — trade-offs em produto

📚 **Aplicação em IA**
- a16z. *The Emerging Architectures for LLM Applications* (Bornstein & Radovanovic, 2023)
- Karpathy, A. *Software 3.0* (palestras 2024)
- Anthropic. *Build Effective Agents* (2024)

📚 **Sobre RAG vs Fine-tuning**
- *RAG vs Fine-Tuning: Pipelines, Tradeoffs, and a Case Study on Agriculture* (Balaguer et al., 2024)

📚 **Sobre agentes vs workflows**
- Anthropic. *Building Effective Agents* (Dezembro 2024) — distinção canônica

---

## 43.15 — VALIDAÇÃO UAU

| # | Critério | Você consegue? |
|---|----------|----------------|
| 1 | **Clareza** — Recitar os 6 trade-offs em ordem, com pergunta executiva de cada, em até 3 minutos | ☐ |
| 2 | **Profundidade** — Defender em mesa técnica por que agente autônomo vence workflow determinístico só em casos específicos, e quais | ☐ |
| 3 | **Aplicação** — Classificar, agora, três decisões recentes da sua operação pelos trade-offs e identificar uma onde houve erro | ☐ |
| 4 | **Conexão** — Articular como o Cap 43 amarra os Caps 06, 08, 12, 15, 16, 36, 39, 40, 41 e 42 em sistema de decisão integrado | ☐ |
| 5 | **Curiosidade UAU** — Está com vontade de produzir o Cardápio de Trade-offs do próprio produto na próxima semana | ☐ |

**5 de 5?** Avance. Você tem o cardápio. Use-o.
**3 ou 4?** Releia §43.3 (os 6 trade-offs em profundidade) e §43.5 (o exemplo). É onde a tese se prova.
**Menos de 3?** Releitura completa. Os trade-offs são a costura entre todos os capítulos anteriores.

---

🔗 **Próximo:** [Capítulo 44 — Roadmap pessoal e organizacional de IA](L1-C44-roadmap-pessoal.md)

---

> *"Não existe decisão de IA sem trade-off. Existe decisão sem consciência. Quem se acomoda paga preço pela primeira."*



<div class="page-break"></div>


# CAPÍTULO 44
## ROADMAP PESSOAL E ORGANIZACIONAL DE IA

---

> *"Saber o que fazer amanhã é o que separa o leitor do estudante. Este capítulo é o capítulo de saída — sai da leitura, entra na prática."*

---

> 🧭 **Invariante-mãe:** **Invariante 9 — Operador** — *"A IA multiplica competência e incompetência pelo mesmo fator."*
> Invariante secundário: **Inv. 3 — Camada Dupla** (roadmap separa o que se decora do que se consulta).
> Framework derivado: **F1 — DECID-IA**.

---

## 44.1 — O CONCEITO INTUITIVO

Todo livro técnico bom corre o risco de virar leitura inerte. O leitor termina, fecha, marca a estante. Em três meses, lembra de duas ou três ideias, e na próxima decisão volta a operar pela intuição que o livro queria substituir. A diferença entre o leitor que sai do livro com método novo e o leitor que sai com sensação de leitura concluída está num único movimento: ter **o próximo passo claro** ao virar a última página. Este capítulo existe para garantir esse movimento.

O capítulo 44 é o **capítulo de saída**. Não é resumo nem revisão; é roadmap. Mapeia o que cada persona específica deve fazer nos próximos 30, 90, 180 e 365 dias para que os Invariantes, os frameworks e os capítulos virem prática institucional. Não é genérico — seis personas distintas têm trilhas próprias, cada uma com gates de progresso e Invariantes dominantes em cada marco.

A regra inegociável: roadmap sem **dono nominal** e sem **marco mensurável** é wishlist. O capítulo entrega a estrutura; o leitor preenche o nome e os números. Em três meses, o leitor revisita o roadmap e marca o que cumpriu, o que adiou, o que abandonou — com método.

---

## 44.2 — ANALOGIA: O PROGRAMA DE TREINAMENTO ATLÉTICO

Pense em como um atleta sério sai do estado atual ao estado-meta. Não é "vou treinar mais". É plano com fases — base aeróbica (estabelecer fundamento), força (construir capacidade), especialização (focar no que diferencia em competição), manutenção (sustentar o ganho). Cada fase tem duração, métrica de avanço e gate explícito de passagem para a fase seguinte. Sem o programa, o atleta treina por intuição e estagna em platô; com o programa, evolui com método e revisita o plano periodicamente conforme o corpo responde.

Roadmap de IA opera igual. Quatro marcos (30, 90, 180, 365 dias) por persona. Cada marco com **ações específicas**, **métricas de avanço**, **gate explícito** para próximo. Sem o roadmap, leitor termina o livro e treina IA por intuição até estagnar; com o roadmap, opera com método.

---

## 44.3 — AS SEIS PERSONAS E SEUS EIXOS

| Persona | Eixo principal | Métrica-chave |
|---------|----------------|---------------|
| **Executivo (C-Level)** | Decisão e governança | OKRs de adoção; orçamento de IA; SEV-1 e 2 por trimestre |
| **Gestor / Head** | Time, processo, produto | Cobertura de eval; MTTR; entregas usando IA |
| **Desenvolvedor / Arquiteto** | Construção e integração | Cobertura de tracing; PRs com eval; features instrumentadas |
| **Consultor** | Diagnóstico e implantação para terceiros | Clientes atendidos com cardápio dos 6 trade-offs; cases publicados |
| **Empreendedor / Founder** | Diferenciação e produto | TCO de IA / receita; NPS de feature de IA |
| **Criador de Conteúdo / Educador** | Autoridade e tradução | Material produzido aplicando os Invariantes; alcance |

Cada persona percorre os mesmos quatro marcos (30, 90, 180, 365 dias) com ações específicas ao próprio eixo.

---

## 44.4 — ROADMAP POR PERSONA — DETALHADO

### 44.4.1 — Persona EXECUTIVO (C-Level)

| Marco | Ação | Gate de promoção |
|-------|------|-------------------|
| **30 dias** | Recitar os 9 Invariantes; produzir o Cartaz dos Invariantes da empresa; nomear Accountable por 5 decisões críticas de IA; definir OKRs de adoção | Cartaz publicado; RACI mínimo assinado |
| **90 dias** | Aprovar Caderno de Governança v1; AI Council com mandato; cardápio dos 6 trade-offs aplicado a 3 iniciativas | Caderno aprovado; AI Council com 1ª reunião |
| **180 dias** | Caderno de Evals em produção; LLMOps Pilar 1 (tracing) implementado em 100% das features; orçamento de IA atribuído por feature | Atribuição de custo viva; tracing operante |
| **365 dias** | Maturidade média de 10 controles ≥3; auditoria externa positiva; aplicação dos Invariantes virou cultura | Auditoria externa concluída; 2 simulados de incidente realizados |

### 44.4.2 — Persona GESTOR / HEAD

| Marco | Ação | Gate |
|-------|------|------|
| **30 dias** | Selecionar 1 feature de IA do meu escopo; mapear violações dos Invariantes nessa feature; iniciar golden set de 30 casos | Feature mapeada; golden set v0 |
| **90 dias** | F8 EVAL-PIRÂMIDE base + meio implementados; LLMOps pilares 1, 4 e 7 operantes; cardápio dos 6 trade-offs documentado | Eval em CI; runbook de incidente |
| **180 dias** | Cobertura de tracing 100%; rollback testado mensalmente; orçamento por feature visível | Maturidade técnica média 3+ |
| **365 dias** | Time aplicando Invariantes como norma de revisão de PR; 0 SEV-1 no último trimestre | Cultura aplicada; resultado mensurado |

### 44.4.3 — Persona DESENVOLVEDOR / ARQUITETO

| Marco | Ação | Gate |
|-------|------|------|
| **30 dias** | Aplicar F4 PROMPT-EXT em 1 feature; instrumentar tracing em 1 feature; estudar Caps 39 e 40 | Feature instrumentada |
| **90 dias** | PR com eval em CI virou padrão; tool registry implementado; F3 AGENTE-PROP aplicado em 1 agente | Padrão de PR adotado pelo time |
| **180 dias** | Cobertura de tracing 100% nas features sob minha responsabilidade; participação no Caderno de LLMOps v1 | Caderno de LLMOps publicado |
| **365 dias** | Mentor de outros devs no método dos Invariantes; contribuição a repositório de prompts da empresa; participação em decisão de arquitetura citando frameworks | Reputação interna de quem opera, não usa, IA |

### 44.4.4 — Persona CONSULTOR

| Marco | Ação | Gate |
|-------|------|------|
| **30 dias** | Aplicar cardápio dos 6 trade-offs em 1 cliente; produzir entrega usando os Invariantes como vocabulário | 1 cliente impactado |
| **90 dias** | 3 clientes com cardápio aplicado; 1 case publicado em mídia setorial | 3 cases internos |
| **180 dias** | Workshop dos 9 Invariantes para clientes; framework próprio adaptado ao meu nicho | Workshop em pé |
| **365 dias** | Reputação como referência em método (não em vendor); 10+ clientes operando pelo método | Marca pessoal consolidada |

### 44.4.5 — Persona EMPREENDEDOR / FOUNDER

| Marco | Ação | Gate |
|-------|------|------|
| **30 dias** | Aplicar F1 DECID-IA em cada feature de IA do produto; F7 COMPOSTO-3T para auditar custo atual | Decisão de adoção documentada por feature; baseline de custo |
| **90 dias** | Golden set inicial para feature-chave; canário em produção; eval em CI; circuit breaker de custo | Pirâmide de Evals operante; custo sob controle |
| **180 dias** | F2 ENCAIXE-5 aplicado para escolher modelo certo por feature; LLMOps maduro; AUP publicada | TCO de IA / receita dentro do envelope |
| **365 dias** | Crescimento sustentado com margem; cliente Enterprise compra pela arquitetura defendida | Arquitetura virou diferencial competitivo |

### 44.4.6 — Persona CRIADOR DE CONTEÚDO / EDUCADOR

| Marco | Ação | Gate |
|-------|------|------|
| **30 dias** | 4 posts/vídeos aplicando 1 Invariante por semana; aplicar Cartaz dos Invariantes em audiência | 4 peças publicadas |
| **90 dias** | Workshop ou minicurso usando os Invariantes; biblioteca pessoal de prompts publicada | 1 workshop entregue |
| **180 dias** | Comunidade de Operadores Inteligência Aumentada com 100+ membros engajados | Comunidade ativa |
| **365 dias** | Reconhecimento como referência em IA aplicada em pt-BR; convite a falar em eventos setoriais | Marca consolidada |

---

## 44.5 — DIAGRAMAS

> 📊 **Diagrama 44.1 — Curva de adoção por persona**
>
> *(SVG planejado: `imagens/L1-C44-img-01-curva-adocao.svg`)*
>
> Curva em S mostrando como cada persona avança em maturidade ao longo de 365 dias.

> 📊 **Diagrama 44.2 — Matriz roadmap × persona × marco**
>
> *(SVG planejado: `imagens/L1-C44-img-02-matriz-roadmap.svg`)*
>
> Tabela visual sintética dos 6 personas × 4 marcos com gates explícitos.

---

## 44.6 — EXEMPLO MEMORÁVEL: O CTO DE VAREJO QUE CUMPRIU O ROADMAP

> ⚠️ **Cenário ilustrativo** — composto a partir de padrões observados em CTOs de redes brasileiras de varejo de médio porte que adotaram IA com método estruturado entre 2024 e 2026; números são realistas mas não identificam empresa específica.

CTO de rede brasileira de varejo (~3.500 colaboradores, ~120 lojas, vendas online crescendo a 35% a/a), em 2025. Leu o livro, marcou o Cartaz dos Invariantes na parede do escritório, decidiu cumprir o roadmap de 365 dias da persona Executivo C-Level (sem ser CEO, mas com mandato sobre IA).

**Mês 1.** Recitou os 9 Invariantes em apresentação ao Conselho. Publicou cartaz nas salas de reunião da diretoria. Nomeou Accountable por 5 decisões críticas de IA (modelo de recomendação, prompt do assistente do app, política de uso interno, agente de marketing, fine-tuning). OKRs: cobertura de tracing 100%, MTTR ≤30min, 0 SEV-1.

**Mês 3.** Caderno de Governança v1 aprovado pela diretoria. AI Council instalado com 6 papéis e cadência mensal. Cardápio dos 6 trade-offs aplicado às 3 iniciativas em desenvolvimento (agente de atendimento, classificação de SKU, copiloto de gestor de loja). Decisão de não escalar o agente de marketing para autônomo (T2 + T5 negaram); escolha por modelo Sonnet em vez de Opus para classificação de SKU (T4, F2).

**Mês 6.** Pirâmide de Evals em produção com golden set de 800 casos cobrindo as 3 features. LLMOps Pilar 1 instrumentado em 100%; Pilar 4 (rollback) testado mensalmente; Pilar 7 (governança operacional) com primeiro simulado de incidente SEV-1 executado. Orçamento de IA atribuído por feature, viva em dashboard.

**Mês 12.** Maturidade média dos 10 controles atingiu 3,4 (meta era 3+). Auditoria externa contratada por iniciativa do CTO, recomendada pelo AI Council; saiu positiva. 2 simulados de incidente realizados no ano, ambos com ações corretivas implementadas. Aplicação dos Invariantes virou vocabulário interno — em revisões de PR, em reuniões de diretoria, em apresentações a fornecedores.

Resultado mensurável em ano 2: redução de 41% no custo de atendimento (substituição parcial de Nível 1 + roteamento melhor por F2 e F7), NPS subiu 8 pontos (qualidade percebida), 0 SEV-1 no ano (sem incidente crítico). O CTO foi promovido a Diretor Executivo de Tecnologia em janeiro do ano 3. Apresenta hoje o caso em fóruns setoriais como exemplo de adoção estruturada de IA em varejo brasileiro.

A lição não é sobre o resultado — bom, sim, mas variável caso a caso. A lição é sobre **o método**. *Cumprir o roadmap em 365 dias não é fácil, é estruturado. A diferença entre o CTO que aplica o método e o que opera por intuição vira diferencial competitivo institucional. O livro entrega o método; o leitor entrega o nome e os números.*

---

## 44.7 — QUANDO USAR / QUANDO EVITAR

**Aplicar o roadmap quando:**
- Você reconhece a persona em si mesmo (ou em alguém da sua organização)
- Há mandato para implementar (mesmo informal)
- Há capacidade de revisitar trimestralmente

**Evitar usar como receita rígida** quando:
- Contexto exige customização significativa (sempre exige; o roadmap é estrutura, não script)
- Ambiente não suporta mudança de cultura (nesse caso, primeiro item é mudar o ambiente)

---

## 44.8 — VANTAGENS E LIMITAÇÕES

| Vantagem | Limitação |
|----------|-----------|
| Próximo passo claro ao fechar o livro | Roadmap genérico exige customização para realidade local |
| Gates explícitos facilitam revisão trimestral | Adoção depende de mandato, não só de roadmap |
| Por persona — relevante a quem está lendo | Pode parecer rígido em organizações de cultura experimental |
| Conecta leitura à prática | Sem revisão trimestral, vira documento esquecido |
| Roadmap por persona vira ativo organizacional | Demanda disciplina de revisitar |

---

## 44.9 — CONEXÕES COM OUTROS CAPÍTULOS

- 🔗 **Manifesto e Invariantes** → [Cap 00M](../01-manifesto/L1-C00M-manifesto-invariantes.md)
- 🔗 **F1 DECID-IA** alimenta cada iniciativa do roadmap → [F1](../03-frameworks/L1-F1-decid-ia.md)
- 🔗 **Caps 39, 40, 41, 42** sustentam os marcos técnico-operacionais
- 🔗 **Apêndice C — Roadmaps detalhados** → (Parte 2 desta onda)
- 🔗 **Apêndice K — Gabaritos** → (Parte 2)
- 🔗 **Volume Vivo (L2)** — capítulos de Claude aplicáveis a cada marco

---

## 44.10 — RESUMO EXECUTIVO

| Persona | 30 dias | 90 dias | 180 dias | 365 dias |
|---------|---------|---------|----------|----------|
| Executivo | Cartaz + RACI mínimo | Caderno Governança | Evals + LLMOps | Maturidade 3+ |
| Gestor | Golden v0 | Eval em CI | Tracing 100% | Cultura aplicada |
| Dev/Arquiteto | F4 + tracing | Eval no PR | Caderno LLMOps | Mentor |
| Consultor | 1 cliente | 3 cases | Workshop | Marca |
| Founder | F1 + F7 audit | Eval + canário | F2 + AUP | TCO/receita ok |
| Criador | 4 peças | Workshop | Comunidade 100+ | Referência |

---

## 44.11 — CHECKLIST DO CAPÍTULO

- [ ] Identificar a persona principal entre as 6
- [ ] Marcar no calendário os 4 marcos (30, 90, 180, 365 dias)
- [ ] Preencher Accountable de cada ação por marco
- [ ] Definir métrica numérica de cada gate
- [ ] Marcar a revisão trimestral em agenda recorrente
- [ ] Compartilhar o roadmap com par sênior ou mentor
- [ ] Estabelecer rotina de revisitar este capítulo a cada 90 dias

---

## 44.12 — PERGUNTAS DE REVISÃO

1. Qual a sua persona principal, e por quê?
2. Em qual marco você está hoje, e qual é a sua próxima ação?
3. Que gate de progresso você usaria para validar que está cumprindo?
4. Quem é o Accountable nominal por cada ação?
5. Como o roadmap se conecta com o F1 DECID-IA?

---

## 44.13 — EXERCÍCIOS PRÁTICOS

**Exercício 1 — Roadmap personalizado.** Preencha o roadmap completo da sua persona com nomes, números e datas específicos.

**Exercício 2 — Gargalo dominante.** Identifique o gargalo dominante no marco 30 dias. Defina plano de remediação em 7 dias.

**Exercício 3 — Invariante mais frágil.** Para cada marco, identifique qual Invariante é o mais frágil hoje na sua operação. Documente.

**Exercício 4 — Apresentação à diretoria/sócios.** Construa apresentação de 10 minutos do roadmap para sua diretoria, sócios ou conselho.

---

## 44.14 — PROJETO DO CAPÍTULO

**Apresentar o seu Roadmap dos 365 dias à diretoria/sócios em até 10 minutos.** Entregável:

1. Slide 1 — Persona e tese
2. Slide 2 — Estado atual (Invariante mais frágil)
3. Slide 3 — Marcos 30/90/180/365 com ações
4. Slide 4 — Gates de promoção entre marcos
5. Slide 5 — Métricas de sucesso
6. Slide 6 — Recursos necessários
7. Slide 7 — Pedido específico de mandato

**Critério de qualidade.** Diretoria aprova o roadmap em uma reunião, com mandato formal sobre IA.

---

## 44.15 — REFERÊNCIAS PRINCIPAIS

📚 **Sobre roadmap, OKRs e adoção**
- Doerr, J. *Measure What Matters* (2018) — OKRs como instrumento de adoção
- Kotter, J. *Leading Change* (1996) — fundamentos de mudança organizacional

📚 **Sobre adoção corporativa de IA**
- Davenport, T. *The AI Advantage* (2018)
- MIT Sloan / BCG. *Building the AI-Powered Organization* (relatórios anuais 2019-)

📚 **Inteligência Aumentada — sistema da obra**
- Cap 00M — Manifesto dos Invariantes
- Apêndice C — Roadmaps detalhados (Parte 2)
- Frameworks F1-F9

---

## 44.16 — VALIDAÇÃO UAU

| # | Critério | Você consegue? |
|---|----------|----------------|
| 1 | **Clareza** — Apresentar seu roadmap em 10 minutos a um par sênior sem consulta | ☐ |
| 2 | **Profundidade** — Defender em mesa por que cada marco tem gate explícito de promoção | ☐ |
| 3 | **Aplicação** — Marcar, agora, a primeira ação dos próximos 7 dias do seu roadmap | ☐ |
| 4 | **Conexão** — Articular como o roadmap sustenta os 9 Invariantes e os 9 frameworks da obra | ☐ |
| 5 | **Curiosidade UAU** — Está com vontade de virar a página, abrir os apêndices, e começar | ☐ |

**5 de 5?** Avance. Você passou de leitor a operador. O capítulo seguinte é a sua vida profissional.
**3 ou 4?** Releia §44.4 do seu persona específico. É onde a estrutura vira ação.
**Menos de 3?** Releia o Cap 00M (Manifesto) antes de revisitar este capítulo.

---

🔗 **Apêndices:** [A Glossário](../04-apendices/L1-APX-A-glossario.md) · [B Mapa Mental](../04-apendices/L1-APX-B-mapa-mental.md) · [C Roadmaps por persona](../04-apendices/L1-APX-C-roadmaps.md) · [M Manifesto de Bolso](../04-apendices/L1-APX-M-manifesto-bolso.md)

🔗 **Volume Vivo (L2):** [Cap 17 Entendendo Claude](../../Livro-2-Dominando-Claude/02-capitulos/L2-C17-entendendo-claude.md) · [Apêndice Vivo (J)](../../Livro-2-Dominando-Claude/04-apendices/L2-APX-J-apendice-vivo.md)

---

> *"A leitura termina aqui. O método começa agora. Quem aplicar muda; quem fechar o livro continua igual."*
