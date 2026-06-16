# F9 — Rota Dupla de Adoção
## Trilha de aprendizado e operação por camada (padrão × número)

## 1. OBJETIVO

Este framework é o **protocolo operacional** do argumento que C00P (Por Que Padrão Dura e Número Morre) demonstra historicamente com quatro casos. A divisão de trabalho é precisa: C00P responde *por que* a distinção existe — evidência histórica com Hadoop, LSTM, fine-tuning, LangChain; argumento para o CTO que resiste à separação. F9 responde *como operar* essa distinção no dia a dia — duas trilhas, cadências, diagnóstico pessoal, protocolo de pré-decisão. Se você leu C00P, F9 é o "como fazer" do que C00P demonstrou ser verdadeiro. Se você não leu C00P, F9 funciona como protocolo standalone — mas C00P entrega a evidência histórica que sustenta o argumento quando o interlocutor é cético.

Orientar o estudo e a operação do leitor distinguindo, em cada peça de conhecimento, o que é **padrão (decora)** do que é **número (consulta)**. Garantir que tempo de aprendizado vá para o que envelhece bem, e que tempo de consulta vá para o que muda — com fonte e data.

## 2. FUNCIONAMENTO

Toda peça de conhecimento sobre IA pertence a **uma de duas trilhas** com cadências distintas de revisitação.

### Trilha Padrão (Padrão durável)

**O que vai aqui.**
- Os 9 Invariantes da IA
- Os 9 Frameworks proprietários (F1-F9)
- Capítulos conceituais (Cap 01, 02, 03, 04, 05, 06, 07, 08, 09, 10, 11, 12, 13, 14)
- Anatomia de eval, LLMOps, Alignment, Governança (Caps 21, 22, 23, 24)
- Tradeoffs canônicos (Cap 25)
- Padrões arquiteturais (RAG, agente, MCP, fine-tuning)

**Cadência de revisitação.** Trimestral para revisão completa. Anual para releitura focada.

**Como armazena.** Cabeça do operador. Cartaz dos Invariantes (Apêndice M) na parede. Caderno do Operador como notas pessoais.

### Trilha Número (Número volátil)

**O que vai aqui.**

*Número de baixa meia-vida (muda em semanas a meses — consultar sob demanda antes de cada decisão):*
- Versões correntes de modelos (Anthropic, OpenAI, Google, open weights)
- Preços por milhão de tokens
- Posições em benchmark da rodada (SWE-bench Verified, GPQA Diamond, OSWorld — avaliações de capacidade de modelos — etc.)
- Limites correntes de janela de contexto
- Capacidades novas de produto (Claude Skills X.Y, Connectors, etc.)
- Lista corrente de repositórios GitHub relevantes

*Número de alta meia-vida (muda em meses a anos — consultar a cada 6 meses e antes de decisões com impacto de compliance):*
- Datas e versões de regulação aplicável (LGPD, AI Act, NIST AI RMF — têm ciclos de 12-24 meses e impacto jurídico; tratar com cadência diferente de preço de token)

**Cadência de revisitação.** Consulta sob demanda, antes de cada decisão que use o número como insumo. Revisão pessoal periódica conforme intensidade do uso de IA na operação.

**Como armazena.** Apêndice J — Trilha do Número, datado, com fonte por linha, mantido como instrumento vivo no repositório acompanhante sem cadência fixa anunciada.

### Mecânica de aplicação

1. **Diagnóstico.** Listar o que se sabe sobre IA hoje. Para cada item, classificar: padrão ou número?
2. **Migração.** Item classificado errado vai para a trilha certa.
3. **Cadência de revisão.** Padrão entra em revisão periódica pessoal, em ritmo que o operador define conforme intensidade de uso. Número fica disponível para consulta sob demanda.
4. **Antes de cada decisão.** Identificar quais padrões e quais números a decisão precisa. Buscar cada um na trilha certa.

> **Ponto de partida zero — para quem o diagnóstico mostra poucos padrões e muitos números:** esse é o estado normal de quem está começando, não sinal de que o framework não se aplica. O caminho de entrada é a Trilha Padrão em ordem linear do livro. Prioridade: internalizar os 9 Invariantes (C00M) antes de qualquer framework específico. Cadência sugerida: dedicar 4 semanas à leitura do corpo do livro antes de consultar qualquer número do Apêndice J para decisão. Os frameworks F1-F9 constroem o mapa de padrão que a decisão depois vai usar.

## 3. OUTPUT

| Campo | Conteúdo |
|-------|----------|
| Mapa pessoal de padrões dominados | Os 9 Invariantes, frameworks F1-F9, conceitos centrais |
| Mapa pessoal de gaps de padrão | O que ainda precisa ser estudado |
| Calendário de revisão de padrão | Trimestral e anual |
| Bookmark do Apêndice J | Para consulta de número |
| Calendário de checagem do Apêndice J | Mensal por padrão; antes de cada decisão crítica |

## 4. EXEMPLO DE USO — CTO QUE PRECISA DECIDIR MODELO

Cenário: CTO de SaaS B2B precisa decidir migração de modelo para feature de copiloto in-product.

**Identificação do que a decisão precisa.**

| Insumo | Trilha | Onde buscar |
|--------|--------|-------------|
| Quais são os eixos relevantes para escolha de modelo? | Padrão | Diagnóstico de Encaixe entre Tarefa e Modelo (Trilha Padrão) |
| Como pontuar a tarefa nos eixos? | Padrão | Cap 15 + F2 |
| Qual a liderança corrente em "razão complexa" e "código"? | Número | Apêndice J — SWE-bench Verified, GPQA |
| Qual o preço por milhão de tokens hoje? | Número | Apêndice J — pricing pages |
| Qual a filosofia de alignment do vendor? | Padrão | Cap 23 (depende pouco da versão) |
| Qual a janela de contexto corrente do modelo X? | Número | Apêndice J |

A decisão é informada por padrão (F2 + Cap 23) e número (Apêndice J). O padrão vive na cabeça do CTO; o número é conferido na semana da decisão.

**Em 6 meses,** a fronteira muda. Versões novas saem. Mas o padrão F2 continua válido. O CTO refaz o exercício, busca o novo número no Apêndice J atualizado, e a decisão é consciente em vez de reativa.

---

### Caso ilustrativo — O custo de confundir número com padrão

> ⚠️ **Cenário composto** a partir de padrões recorrentes observados em empresas de SaaS brasileiro entre 2023 e 2025.

Um Head de Tecnologia de SaaS B2B conduziu, entre 2023 e 2024, três migrações de modelo de linguagem em dezoito meses. Em cada ciclo, o gatilho era o mesmo: um novo lançamento liderava o benchmark da semana. Em cada ciclo, o esforço era o mesmo: três a cinco semanas de engenharia, dois ciclos de validação, comunicação ao time de produto. O resultado acumulado foi R$ 280 mil em custo de migração sem ganho mensurável de qualidade para os usuários.

No quarto ciclo potencial, o Head aplicou o diagnóstico do F9 antes de decidir. O resultado: dos vinte e dois itens de "conhecimento sobre modelos de IA" que ele mantinha na cabeça, vinte eram número (versão, posição em benchmark, preço por token, janela de contexto corrente). Dois eram padrão (eixos de encaixe por tarefa, hierarquia de adoção). O diagnóstico mostrou que as três migrações anteriores tinham sido decididas com fundamento em número sem consulta ao padrão — nenhuma delas passou pelo F2 (encaixe por eixo de tarefa).

A quarta decisão foi diferente: padrão aplicado primeiro (F2 apontou que o eixo dominante da feature era "contexto longo" + "escrita executiva", não "código"), número consultado depois (Apêndice J confirmou qual modelo liderava nesses eixos naquela semana). Resultado: nenhuma migração executada — o modelo em uso já liderava nos eixos que importavam. Custo da quarta "migração": uma sessão de 45 minutos.

## 5. ANTI-PADRÕES

| Anti-padrão | Por que mata |
|-------------|--------------|
| Memorizar versão e benchmark "porque é importante" | Memória vira passivo no próximo release |
| Não memorizar o padrão "porque é teórico" | Sem padrão, decisão fica refém do marketing do vendor |
| Achar que o livro tem tudo | Livro tem o padrão; Apêndice J tem o número |
| Confiar em memória para o número | Modelo X mudou de versão; preço caiu 40%; benchmark líder é outro |
| Ignorar o padrão porque "é óbvio" | Operadores que conhecem o óbvio cometem 80% dos erros do mercado |
| Atualizar o padrão na mesma cadência do número | Tempo gasto reescrevendo o que não mudou |

## 6. CONEXÕES

- 🔗 Manifesto dos Invariantes
- 🔗 Cap 01 — O que é IA
- 🔗 Cap 15 — Comparação de modelos
- 🔗 Apêndice M — Manifesto de bolso
- 🔗 Apêndice B — Mapa Mental Geral
- 🔗 Todos os frameworks F1-F8 (cada um opera um padrão)

---

> *"Decore o padrão, consulte o número. Misturar as duas trilhas é envelhecer junto com o release."*
