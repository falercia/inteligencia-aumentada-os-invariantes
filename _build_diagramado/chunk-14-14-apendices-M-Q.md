---
title: "Inteligência Aumentada"
lang: pt-BR
---



<section class="apendice-bloco">
<div class="abertura-apendice">

<div class="selo-apendice">Apêndice</div>

# Apêndice L — Biblioteca de Prompts Profissionais

## Por que este apêndice existe em duas camadas

A biblioteca que este apêndice apresenta reúne trinta prompts profissionais que foram desenhados como ativos de produção, no sentido estrito de que cada um foi pensado para entrar em pipelines reais, com inputs reais, com riscos reais, e com necessidade de versionamento, auditoria e regressão automatizada. A construção desses ativos exige duas peças que se complementam, e a obra trata cada uma delas no andar certo.

A primeira peça é o padrão durável, e ela vive aqui no livro, na forma de trinta fichas conceituais. Cada ficha entrega a dor que o prompt resolve, o escopo do domínio, o que esperar como saída, a anatomia da estrutura sob o Framework Quatro, os anti-padrões observados em prática, o critério explícito de quando usar e quando evitar, o modelo recomendado e a métrica de qualidade. A ficha é o que o operador maduro precisa entender para adaptar o prompt ao próprio contexto, e para construir biblioteca interna calibrada para o tráfego real da sua operação.

A segunda peça é o número volátil, e ela vive no repositório acompanhante público em [github.com/falercia/inteligencia-aumentada-recursos](https://github.com/falercia/inteligencia-aumentada-recursos), em pasta dedicada por prompt, com o XML completo do ativo, o golden set de vinte casos calibrados pelo autor, o changelog público datado, os anti-padrões em detalhe e o script de regressão executável. Quem chega à ficha do livro com clareza conceitual encontra no repositório o artefato pronto para clonar, adaptar e colocar em CI, sem ter que reescrever cada estrutura do zero.

Essa separação é deliberada e materializa o Princípio Três, a Camada Dupla. O padrão dura porque a estrutura conceitual sobrevive à próxima geração de modelo, ao próximo provedor, à próxima moda de framework. O número muda porque o XML específico vai sofrer iteração mensal, o golden set vai crescer com calibração de especialistas externos, e a métrica de qualidade vai ser refinada a cada release. Manter as duas no mesmo arquivo, como faziam as primeiras versões deste apêndice, congelava o XML em mídia impressa e impedia a evolução contínua do ativo. O leitor que entendeu o método vai ao repositório quando precisa do executável, e fica com a ficha quando precisa do método.

### Quadro de orientação — onde vive o quê

| Camada do conhecimento | Onde vive | Cadência de revisão |
|---|---|---|
| Dor que o prompt resolve, anatomia sob Framework Quatro, critério de quando usar e quando evitar, anti-padrões estruturais, métrica de qualidade | **LIVRO · ficha conceitual** | Anual, junto com a próxima edição |
| XML executável completo, golden set de vinte casos calibrados, prefill, self-critique, changelog datado, script de regressão, anti-padrões em detalhe | **REPO · `/prompts/<dominio>/<id>/`** | Sem cadência fixa, conforme evolução real do ativo |
| Resultado de execução em modelo da rodada, custo médio por chamada, posição em benchmark de qualidade aplicado | **APÊNDICE J · Trilha do Número** | Sem cadência fixa, conforme movimento relevante de mercado |

O leitor com pressa que precisa apenas decidir se adota um prompt resolve a decisão na ficha conceitual. O leitor que vai operar o prompt em produção desce ao repositório. O leitor que precisa justificar custo ou comparar com alternativa em ata de comitê consulta o Apêndice J. Os três artefatos são desenhados para serem usados em conjunto, jamais como substitutos um do outro.

---

## A anatomia que toda ficha aplica

Antes das trinta fichas, vale percorrer uma única vez a anatomia comum a todos os prompts, sob o Framework Quatro, a Engenharia de Prompt Estendida. Cinco blocos XML estáveis sustentam cada prompt, e a ordem não foi escolhida por estética. Ela emergiu de testes A/B em diferentes famílias de modelos e deve ser preservada quando o leitor adaptar qualquer ficha ao próprio cenário, sob pena de degradar a aderência à constituição.

| Bloco | Função | Por que está nesta posição |
|---|---|---|
| `<persona>` | Define quem o modelo é, com tom e padrão profissional. | Primeiro porque ancora o vocabulário e o nível de exigência. |
| `<constituicao>` | Reúne as regras invioláveis do prompt. | Cedo no contexto porque modelos priorizam instruções recentes em outputs longos; reiterar no fim quando crítico. |
| `<contexto>` | Carrega as variáveis nomeadas em duplo-chaves, com o dado dinâmico da chamada. | No meio porque é o que muda a cada chamada, e o modelo precisa do dado depois das regras. |
| `<tarefa>` | Declara o que se pede ao modelo, com escopo explícito. | Depois do contexto porque a tarefa opera sobre o dado disponível. |
| `<formato_saida>` | Especifica o schema da saída, em markdown ou JSON. | Por último porque é o "como devolver", aplicado ao que foi pedido. |

Dois blocos adicionais aparecem em todos os trinta prompts em qualidade plena, e merecem nota própria.

**`<prefill>`** ancora o início da resposta do modelo no formato esperado, reduzindo a chance de divagar antes de entregar o conteúdo estruturado. O ganho é mensurável especialmente em saídas JSON e em fluxos com schema fechado, onde a primeira chave do objeto direciona toda a geração.

**`<self_critique>`** força uma rodada explícita de revisão antes do output final. Modelos longos perdem peso relativo das regras do início conforme a resposta cresce, e o self-critique recupera aderência à constituição em casos limítrofes onde o output direto fugiria do escopo. Em produção, esse bloco isolado reduz em ordens de magnitude a taxa de violação silenciosa da constituição.

A linguagem escolhida foi XML porque os modelos da família Claude foram treinados para reconhecer tags como delimitadores semânticos fortes, com aderência mensurável superior a markdown em testes controlados. O leitor que opera com outras famílias pode substituir XML por marcadores equivalentes em markdown estruturado, em YAML ou em delimitadores customizados como triplo-pipe, desde que mantenha a separação clara entre instrução e dado, que é a propriedade arquitetural que importa, não a sintaxe.

### Exemplo estrutural

Para ancorar a anatomia em algo concreto antes das fichas, fica aqui o único XML completo deste apêndice, em forma didática genérica. Este não é um prompt de produção, e sim um esqueleto comentado para que o leitor visualize a estrutura antes de visitar o repositório, onde cada um dos trinta prompts vive em sua forma executável.

```xml
<persona>
Você é [descrição da identidade profissional do modelo, com tom e padrão de
saída esperado, em uma a três linhas].
</persona>

<constituicao>
- [Regra de escopo: o que o prompt cobre e o que recusa.]
- [Regra de citação: o que deve aparecer literal vs. parafraseado.]
- [Regra de lacuna: o que fazer quando faltar informação.]
- [Regra de marcação: quando usar expressão padronizada de sinalização.]
- [Regra de limite: o que o prompt não pode fazer.]
</constituicao>

<contexto>
[Variável dinâmica 1]:
{{variavel_1}}

[Variável dinâmica 2]:
{{variavel_2}}
</contexto>

<tarefa>
[Declaração da tarefa, com objeto, dimensões a analisar, e fronteira do que
o modelo deve produzir.]
</tarefa>

<formato_saida>
[Schema da saída, em markdown ou JSON, com seções nomeadas ou chaves
tipadas, sem ambiguidade.]
</formato_saida>

<prefill>
[Primeira parte da saída pré-escrita, ancorando o modelo no formato.]
</prefill>

<self_critique>
Antes de finalizar, faça [N] verificações. Primeiro, [verificação alinhada
ao item crítico da constituição]. Segundo, [verificação sobre formato e
schema]. Terceiro, [verificação sobre lacunas e sinalização]. Reescreva a
seção problemática antes de devolver.
</self_critique>

<input>
{{conteudo_a_processar}}
</input>
```

O leitor que quiser ver esse esqueleto preenchido com um caso real, completo em todos os campos, com golden set de vinte casos, prefill calibrado, self-critique afinado e métrica de qualidade quantitativa, encontra cada um dos trinta prompts em pasta dedicada no repositório acompanhante.

---

## Padrões de operação

Sete padrões organizam o uso responsável da biblioteca, independentemente do prompt específico que o leitor escolher adaptar.

1. **Não copie cegamente nenhum dos trinta prompts.** Cada um foi calibrado para um cenário hipotético típico, e o cenário do leitor terá particularidades que exigem ajuste de constituição, de formato e de exemplos no golden set.
2. **Customize o conteúdo entre as tags, jamais a ordem das tags.** A ordem é a propriedade estrutural que sobreviveu aos testes e que carrega a maior parte do ganho de aderência.
3. **Mantenha golden set próprio com no mínimo vinte casos representativos por prompt**, atualizado conforme novas categorias de input apareçam no tráfego real, executado como teste de regressão a cada mudança de prompt ou de modelo.
4. **Reverifique o prompt contra o golden set sempre que o modelo subjacente for atualizado**, porque modelos novos mudam comportamento mesmo em prompts antigos, e o que era ouro pode virar bronze sem aviso.
5. **Mantenha os prompts versionados em Git**, com identificador estável, changelog descritivo, tags de release e pipeline de promoção entre dev, homologação e produção.
6. **Use variáveis nomeadas no formato duplo-chaves para todo conteúdo dinâmico**, jamais concatenação direta de strings, porque concatenação é vetor de prompt injection e impede testes determinísticos.
7. **Não misture instrução com dado fora das tags.** Todo conteúdo vindo de usuário ou de fonte externa deve estar embrulhado em tag de input, contexto ou exemplo, para que o modelo trate o conteúdo como dado a ser processado, não como nova instrução a obedecer.

---

## Anti-padrões transversais de prompt

| Anti-padrão | Por que falha |
|---|---|
| Regra crítica enterrada no meio do prompt | Modelos priorizam início e fim, regras no meio são esquecidas em outputs longos. |
| Pergunta colocada antes do contexto | Força o modelo a especular, depois a corrigir, gerando respostas incoerentes. |
| Constituição ambígua, com termos como "se possível" ou "sempre que apropriado" | Cria espaço para o modelo escolher quando obedecer, anulando a regra. |
| Falta de reiteração de regra crítica antes da saída | Em respostas longas, a regra do início perde peso relativo. |
| Ausência de sanitização contra prompt injection no campo de input | Permite que o conteúdo do usuário sobrescreva instruções do sistema. |
| Prompt como string concatenada solta no código | Impede versionamento, impede teste, impede observabilidade. |
| Ausência de golden set | Torna impossível detectar regressão quando o modelo é atualizado. |
| Ausência de versionamento e changelog | Transforma cada edição em mudança não rastreável, com risco em produção. |

---

## Como ler as fichas

Cada ficha a seguir segue exatamente o mesmo molde, com nove campos enxutos. A leitura sequencial das trinta fichas em janela de uma hora dá ao executivo o mapa completo da biblioteca. A consulta pontual a uma ficha específica em janela de noventa segundos dá ao operador o critério para decidir se aquele prompt resolve a dor que tem na frente.

| Campo | O que entrega |
|---|---|
| Dor que resolve | Por que o prompt existe, em uma frase contextual. |
| Domínio | Escopo coberto, e fronteira do que não cobre. |
| O que o prompt entrega | Cinco a sete pontos do output esperado. |
| Estrutura aplicada do F4 | Tabela com persona, constituição, contexto, tarefa e formato. |
| Quando usar e quando evitar | Tabela de quatro pares cada. |
| Anti-padrões observados | Três a cinco padrões específicos de domínio. |
| Modelo recomendado | Família, com nota de tier e fallback. |
| Métrica de qualidade | Critério quantitativo verificável. |
| Versão executável | URL direta para a pasta do prompt no repositório. |

O leitor que quiser ir além e abrir o XML completo, o golden set de vinte casos, o changelog datado, o script de eval e os exemplos de saída anonimizados encontra tudo isso no repositório acompanhante público, em pasta dedicada para cada um dos trinta prompts.

---

## Os 30 prompts — fichas conceituais

### Jurídico

#### P-LEG-01 · Revisão de Cláusula de Não-Concorrência CLT

**Dor que resolve.** Jurídico interno gasta horas na primeira leitura de contratos com cláusulas restritivas pós-contratuais; este prompt entrega triagem em segundos, sinalizando os elementos que o TST considera essenciais para validar a cláusula.

**Domínio.** Jurídico trabalhista CLT brasileiro, cláusulas de 6 a 24 meses, todos os níveis hierárquicos. Não cobre PJ, estatutário ou outras jurisdições.

**O que o prompt entrega**
- Citação literal de cada elemento da cláusula, sem paráfrase, para preservar rastreabilidade
- Status presente, ausente ou presente com risco para os cinco elementos essenciais do TST
- Classificação geral em baixo, médio, alto ou crítico
- Três a cinco ajustes pontuais sugeridos, sem reescrever a cláusula
- Lacunas declaradas em vez de inferência sobre o que estaria escrito
- Recusa estruturada quando o input cai fora do escopo CLT

**Estrutura aplicada do F4**

| Bloco | Conteúdo |
|---|---|
| Persona | Advogado trabalhista sênior, 20 anos de TST, tom de parecer interno |
| Constituição | Escopo CLT estrito, citação literal obrigatória, proibição de inventar acórdão, sem juízo de validade definitiva |
| Contexto | Cláusula sob análise, cargo, salário, setor |
| Tarefa | Análise dos cinco elementos do TST (temporal, geográfico, material, contraprestação, interesse legítimo) |
| Formato | Markdown com cinco seções fixas |

**Quando usar e quando evitar**

| Usar | Evitar |
|---|---|
| Triagem de contratos novos | Parecer final em litígio |
| Revisão preliminar pré-jurídico | Defesa em audiência |
| Treinamento de juniores | Regime PJ, estatutário ou estrangeiro |
| Auditoria de portfólio contratual | Análise de validade definitiva |

**Anti-padrões observados**
- Não fornecer cargo e salário no contexto reduz a qualidade da análise em mais de 40%
- Esperar parecer definitivo sobre validade extrapola o papel do prompt e a constituição bloqueia
- Aplicar a contrato PJ disfarçado dispara recusa estruturada, não análise

**Modelo recomendado.** Sonnet equivalente com raciocínio estendido em casos complexos. Haiku para triagem em volume alto, com escalonamento para Sonnet em casos sinalizados como controversos.

**Métrica de qualidade.** Concordância com advogado sênior em pelo menos 85% do golden set quanto à classificação de risco, e 100% quanto à identificação de elementos ausentes.

**Versão executável.** [`prompts/P-LEG-01-clausula-nao-concorrencia-clt`](https://github.com/falercia/inteligencia-aumentada-recursos/tree/main/prompts/P-LEG-01-clausula-nao-concorrencia-clt)

---

#### P-LEG-02 · Análise de NDA Brasileiro LGPD-Compliant

**Dor que resolve.** O time jurídico recebe NDAs com compartilhamento de dados pessoais e precisa identificar pontos de atenção LGPD em ciclo de fechamento contratual sob pressão de prazo; o prompt entrega análise estruturada por dez cláusulas-chave em segundos, sinalizando explicitamente quando há tratamento de dados pessoais sem base legal clara.

**Domínio.** Acordos de confidencialidade sob direito brasileiro com compartilhamento de dados pessoais entre controladores. Não cobre instrumentos sob direito estrangeiro nem opinião sobre validade jurídica definitiva.

**O que o prompt entrega**
- Tabela das dez cláusulas-chave (definição, exceções, vigência, sobrevida, devolução, base legal LGPD, finalidade, retenção, transferência internacional, responsabilização) com status, trecho literal, justificativa e ponto de atenção LGPD
- Lista de até cinco riscos consolidados ordenados por materialidade
- Lista de até cinco recomendações de ajuste pontual
- Declaração explícita de cláusulas que dependem de negociação ou informação adicional
- Sinalização "ponto de atenção LGPD" sempre que houver dado pessoal sem base legal clara

**Estrutura aplicada do F4**

| Bloco | Conteúdo |
|---|---|
| Persona | Advogada brasileira sênior em contratos e proteção de dados, tom de parecer prático |
| Constituição | Restrição a direito brasileiro, citação literal, recusa de direito estrangeiro, declaração explícita de lacunas |
| Contexto | NDA sob análise, natureza das partes, finalidade declarada do compartilhamento |
| Tarefa | Análise das dez cláusulas-chave esperadas em NDA com tratamento de dados |
| Formato | Tabela markdown + três seções (riscos, recomendações, lacunas) |

**Quando usar e quando evitar**

| Usar | Evitar |
|---|---|
| Revisão preliminar de NDA de fechamento | Parecer final sobre validade jurídica |
| Diligência em ciclo M&A pré-due-diligence | NDAs sob direito estrangeiro |
| Padronização de templates jurídicos internos | Análise sobre regime PJ ou contratos sem dado pessoal |
| Treinamento de júnior jurídico | Decisão definitiva sobre transferência internacional |

**Anti-padrões observados**
- Confundir NDA brasileiro com modelos NDA americanos e citar exigências não aplicáveis no Brasil
- Emitir parecer sobre direito estrangeiro quando o NDA cita foro estrangeiro
- Aceitar "execução contratual" como base legal para dados sensíveis sem sinalizar erro
- Tratar anonimização declarada como suficiente sem exigir comprovação metodológica

**Modelo recomendado.** Sonnet equivalente.

**Métrica de qualidade.** Identificação correta de no mínimo nove das dez cláusulas-chave em 90% dos casos, e marcação correta de ponto de atenção LGPD em 100% dos casos em que dados pessoais são mencionados.

**Versão executável.** [`prompts/P-LEG-02-nda-lgpd-compliant`](https://github.com/falercia/inteligencia-aumentada-recursos/tree/main/prompts/P-LEG-02-nda-lgpd-compliant)

---

#### P-LEG-03 · Red Flags em Contrato M&A

**Dor que resolve.** Equipes de M&A precisam fazer leitura preliminar rápida de SPAs e contratos complexos para identificar cláusulas que merecem atenção do sócio responsável; o prompt entrega lista classificada em três níveis (alerta informativo, ponto de negociação, cláusula bloqueante) com justificativa por nível, sem emitir veredito sobre fechar ou não o deal.

**Domínio.** SPAs e contratos M&A sob direito brasileiro ou cross-border com vínculo material no Brasil. Não cobre veredito sobre fazer ou não o deal, nem aconselhamento sobre estrutura societária.

**O que o prompt entrega**
- Sumário executivo com cinco a sete bullets dos pontos mais materiais
- Lista de red flags em JSON com schema fechado (trecho literal, classificação em três níveis, justificativa)
- Identificação de cláusulas típicas problemáticas (MAC sem carve-outs, earn-out sem rules contábeis, sandbagging, indemnification cap, escrow, condições precedentes sem long stop date)
- Recomendação de pontos de negociação sem prescrever conduta
- Sinalização explícita de risco regulatório quando aplicável (CADE, CVM, regularidade fiscal)

**Estrutura aplicada do F4**

| Bloco | Conteúdo |
|---|---|
| Persona | Sócio sênior de M&A em escritório brasileiro, tom técnico denso |
| Constituição | Citação literal, três níveis estáveis, sem recomendação walk away, sem inventar acórdão |
| Contexto | Texto do contrato, lado representado (comprador ou vendedor), setor, estrutura da operação |
| Tarefa | Triagem em três níveis com justificativa por entrada |
| Formato | JSON com sumário e array de red flags |

**Quando usar e quando evitar**

| Usar | Evitar |
|---|---|
| Triagem rápida pré-revisão sênior | Parecer final em negociação fechada |
| Padronização de checklist de due diligence | Aconselhamento de estrutura societária |
| Treinamento de associados em M&A | Operações em jurisdição não brasileira sem material no Brasil |
| Revisão de contratos boilerplate de fornecedor | Estimativa de valor da transação |

**Anti-padrões observados**
- Classificar como cláusula bloqueante prática usual de mercado, gerando alarme falso
- Citar acórdão inexistente do STJ para reforçar argumento
- Recomendar walk away em vez de listar pontos de negociação
- Aceitar earn-out sem rules contábeis como ponto de negociação quando deveria ser bloqueante

**Modelo recomendado.** Sonnet equivalente com raciocínio estendido em SPAs longos.

**Métrica de qualidade.** Concordância com sócio M&A em pelo menos 80% das classificações de nível, com tolerância de um nível em casos limítrofes, e identificação de 100% das cláusulas bloqueantes claras.

**Versão executável.** [`prompts/P-LEG-03-red-flags-contrato-ma`](https://github.com/falercia/inteligencia-aumentada-recursos/tree/main/prompts/P-LEG-03-red-flags-contrato-ma)

---

#### P-LEG-04 · Parecer sobre Compliance LGPD em Processamento de Dados

**Dor que resolve.** DPO precisa avaliar operação de tratamento de dados pessoais contra a LGPD, em ciclo que combina pressão regulatória crescente com volume de operações a auditar; o prompt entrega parecer estruturado em sete dimensões com sinalização de risco regulatório material onde aplicável, sem afirmar adequação completa quando faltam informações.

**Domínio.** Operações de tratamento de dados pessoais sob a LGPD brasileira. Não cobre obrigações criminais, apenas administrativas e civis. Menciona GDPR apenas para contextualização.

**O que o prompt entrega**
- Avaliação por dimensão (base legal, compatibilidade de finalidades, princípios do art. 6º, direitos do titular, segurança técnica e organizacional, governança de compartilhamento, transferência internacional)
- Classificação em conforme, parcialmente conforme, não conforme ou indeterminado por falta de informação
- Citação de artigo específico da LGPD quando aplicável, sem inventar inciso
- Sinalização "risco regulatório material" em situações que possam caracterizar infração administrativa
- Lista de informações faltantes para parecer mais conclusivo
- Recomendações de mitigação ordenadas por prioridade

**Estrutura aplicada do F4**

| Bloco | Conteúdo |
|---|---|
| Persona | DPO sênior brasileiro, formação jurídica e técnica, tom estruturado para comitê |
| Constituição | LGPD como base, citação de artigo sem invenção, sem confirmar adequação definitiva, indeterminado quando faltar evidência |
| Contexto | Descrição da operação, categorias de dados, finalidades, bases legais invocadas, compartilhamento |
| Tarefa | Avaliação em sete dimensões com classificação e justificativa |
| Formato | Markdown com seções nomeadas |

**Quando usar e quando evitar**

| Usar | Evitar |
|---|---|
| Auditoria interna de privacidade | Parecer técnico em contencioso |
| Resposta a RFP com checklist LGPD | Decisão sobre regime sancionatório aplicável |
| Padronização de avaliação de novos projetos | Avaliação sob GDPR como base normativa |
| Preparação para fiscalização ANPD | Opinião sobre obrigação criminal |

**Anti-padrões observados**
- Afirmar adequação completa quando faltam informações em vez de declarar indeterminado
- Citar inciso inexistente do artigo 7 da LGPD
- Confundir controlador e operador na atribuição de responsabilidades
- Tratar "legítimo interesse" como base legal universal sem exigir teste de balanceamento

**Modelo recomendado.** Sonnet equivalente.

**Métrica de qualidade.** Identificação correta da base legal aplicável em 100% dos casos, e concordância com DPO sênior em pelo menos 85% das classificações por dimensão.

**Versão executável.** [`prompts/P-LEG-04-parecer-compliance-lgpd`](https://github.com/falercia/inteligencia-aumentada-recursos/tree/main/prompts/P-LEG-04-parecer-compliance-lgpd)

---

### Saúde

#### P-MED-01 · Triagem de Sintomas com Recusa por Escopo

**Dor que resolve.** Operadoras de saúde precisam atender consultas leigas de orientação em rede, com risco real de subestimar emergência por linguagem moderada do paciente, ou de extrapolar para diagnóstico sem atribuição médica; o prompt entrega classificação em quatro níveis de urgência conservadora, com recusa estruturada para o que cai fora do escopo de orientação leiga.

**Domínio.** Orientação leiga sobre busca de atendimento em rede, com classificação de urgência. Não cobre diagnóstico, prescrição, confirmação de hipótese diagnóstica do paciente, nem orientação fora do escopo de operadora.

**O que o prompt entrega**
- Classificação em emergência (SAMU), urgência (pronto atendimento mesmo dia), eletiva preferencial (72 horas) ou eletiva sem urgência
- Mensagem em linguagem leiga, calma, com 3 a 5 linhas
- Próxima ação concreta com canal indicado
- Sinais de alerta identificados explícitos
- Recusa estruturada quando fora de escopo, com canal humano de continuidade
- Princípio do nível mais conservador em qualquer dúvida

**Estrutura aplicada do F4**

| Bloco | Conteúdo |
|---|---|
| Persona | Assistente de orientação em saúde de operadora, tom calmo, respeitoso, sem alarme |
| Constituição | Sem diagnóstico, sem prescrição, conservadorismo em dúvida, recusa para fora de escopo |
| Contexto | Sintomas descritos, idade, condições crônicas, tempo de início |
| Tarefa | Classificação em quatro níveis de urgência com orientação de canal |
| Formato | JSON com schema fechado |

**Quando usar e quando evitar**

| Usar | Evitar |
|---|---|
| Canal digital de operadora ou plano | Triagem em pronto atendimento (cabe a profissional) |
| Concierge de saúde corporativo | Diagnóstico em qualquer contexto |
| Orientação inicial em app de saúde | Prescrição de medicação ou conduta |
| Triagem assíncrona com supervisão humana | Confirmação de hipótese diagnóstica do paciente |

**Anti-padrões observados**
- Arriscar hipótese diagnóstica em casos clássicos, violando a constituição
- Subestimar urgência por minimizar relato do paciente
- Pedir dados sensíveis desnecessários antes de classificar
- Confirmar diagnóstico mencionado pelo paciente como se fosse parecer médico

**Modelo recomendado.** Sonnet equivalente com temperatura baixa.

**Métrica de qualidade.** Sensibilidade de 100% para casos de emergência clara no golden set, e taxa de recusa de escopo correta em pelo menos 95% das interações fora de escopo.

**Versão executável.** [`prompts/P-MED-01-triagem-sintomas`](https://github.com/falercia/inteligencia-aumentada-recursos/tree/main/prompts/P-MED-01-triagem-sintomas)

---

#### P-MED-02 · Súmula de Prontuário

**Dor que resolve.** Passagem de plantão e handoff entre médicos exige resumo confiável do estado do paciente, e a leitura integral do prontuário entre turnos é cara em tempo do profissional; o prompt entrega súmula no padrão SBAR adaptado, com fidelidade absoluta ao registro original e marcação explícita de ambiguidades, sem introduzir diagnóstico ou conduta nova.

**Domínio.** Documentação clínica hospitalar em formato SBAR adaptado para handoff entre médicos. Não cobre juízo sobre adequação da conduta médica registrada, nem geração de hipótese diagnóstica nova.

**O que o prompt entrega**
- Situação, Background, Avaliação registrada, Recomendação registrada (padrão SBAR)
- Medicações em uso com nome, posologia e via conforme registrado
- Alergias documentadas ou declaração explícita de ausência de registro
- Eventos relevantes no período cobertos cronologicamente
- Lacunas e ambiguidades marcadas explicitamente como "registro ambíguo"
- Fidelidade literal ao registro original

**Estrutura aplicada do F4**

| Bloco | Conteúdo |
|---|---|
| Persona | Assistente de documentação clínica em hospital terciário, tom técnico e conciso |
| Constituição | Trabalha só com conteúdo do prontuário, sem inferência, citação literal, sem juízo de adequação |
| Contexto | Conteúdo do prontuário anonimizado, período, especialidade de destino |
| Tarefa | Súmula em padrão SBAR com fidelidade ao registro |
| Formato | Markdown com seções nomeadas SBAR + medicações, alergias, eventos, lacunas |

**Quando usar e quando evitar**

| Usar | Evitar |
|---|---|
| Handoff entre médicos em mudança de plantão | Geração de hipótese diagnóstica nova |
| Triagem de prontuário em primeira consulta | Decisão sobre conduta terapêutica |
| Suporte a auditoria clínica | Análise crítica da conduta registrada |
| Briefing de equipe multidisciplinar | Diagnóstico em qualquer contexto |

**Anti-padrões observados**
- Inferir diagnóstico não registrado a partir de sintomas, violando a constituição
- Completar posologia de medicação que estava parcial no registro
- Sugerir conduta nova em "Recomendação registrada", ultrapassando escopo
- Resolver ambiguidades temporais por inferência em vez de marcá-las

**Modelo recomendado.** Sonnet equivalente.

**Métrica de qualidade.** Fidelidade ao registro de 100% em diagnósticos e medicações no golden set, e identificação correta de lacunas em pelo menos 90% dos casos.

**Versão executável.** [`prompts/P-MED-02-sumula-prontuario`](https://github.com/falercia/inteligencia-aumentada-recursos/tree/main/prompts/P-MED-02-sumula-prontuario)

---

#### P-MED-03 · Alerta de Interação Medicamentosa

**Dor que resolve.** Farmacêuticos clínicos precisam revisar prescrições para identificar interações relevantes em volume incompatível com revisão manual completa; o prompt entrega análise par a par e em conjunto, com severidade em quatro níveis e sinalização de "necessita validação farmacêutica" em interações maiores ou contraindicadas.

**Domínio.** Prescrições hospitalares brasileiras com lista de medicamentos. Não cobre substituição específica de medicamento, apenas sinalização e conduta esperada.

**O que o prompt entrega**
- Lista de interações com medicamentos envolvidos, mecanismo conhecido, severidade em quatro níveis (contraindicada, maior, moderada, menor)
- Manifestação clínica esperada por interação
- Conduta esperada sem recomendar troca específica
- Sinalização "necessita validação farmacêutica" em contraindicadas e maiores
- Ajustes por função renal quando relevante
- Declaração de lacuna quando informação (dose, via) for insuficiente

**Estrutura aplicada do F4**

| Bloco | Conteúdo |
|---|---|
| Persona | Assistente farmacêutico clínico hospitalar, tom técnico denso |
| Constituição | Apenas interações com evidência consolidada, sem especulação, sem substituição específica |
| Contexto | Lista de medicamentos com dose e via, idade, função renal, condições crônicas |
| Tarefa | Identificação de interações com severidade e conduta |
| Formato | JSON com schema fechado |

**Quando usar e quando evitar**

| Usar | Evitar |
|---|---|
| Revisão de prescrição hospitalar | Substituição direta de medicamento (cabe a farmacêutico clínico) |
| Conferência em transição de cuidado | Aconselhamento direto a paciente |
| Suporte à decisão farmacêutica | Decisão sobre suspensão sem validação humana |
| Auditoria de polifarmácia em idoso | Pediatria sem ajuste etário explícito |

**Anti-padrões observados**
- Identificar interação inexistente entre fármacos comuns, gerando alarme falso
- Recomendar troca específica de medicamento, ultrapassando escopo
- Não sinalizar necessidade de validação farmacêutica em interação maior
- Extrapolar interação documentada em adulto para pediatria sem ajuste

**Modelo recomendado.** Sonnet equivalente, com base de conhecimento farmacológica externa quando disponível.

**Métrica de qualidade.** Sensibilidade de 100% para interações contraindicadas e maiores do golden set, com taxa de falso positivo abaixo de 10% em moderadas e menores.

**Versão executável.** [`prompts/P-MED-03-interacao-medicamentosa`](https://github.com/falercia/inteligencia-aumentada-recursos/tree/main/prompts/P-MED-03-interacao-medicamentosa)

---

### Financeiro

#### P-FIN-01 · Detecção de Anomalia em Extrato

**Dor que resolve.** Analistas antifraude em bancos digitais precisam revisar volume crescente de extratos e sinalizar transações suspeitas para revisão humana, sem cair em alarme falso por padrões legítimos ou inferência indevida sobre identidade de terceiros; o prompt entrega análise em quatro dimensões (valor, contraparte, canal, temporal) com nível de suspeita justificado por padrão observável.

**Domínio.** Extratos bancários brasileiros, transações em conta corrente, Pix, débito, crédito, boleto, com perfil histórico do cliente disponível. Não cobre decisão de bloqueio definitivo, apenas sinalização para humano.

**O que o prompt entrega**
- Lista de anomalias com dimensões anômalas, nível de suspeita em três faixas
- Justificativa baseada em padrão observável, jamais intuição
- Ação recomendada (contato cliente, bloqueio preventivo humano, revisão, observação)
- Resumo agregado por nível
- Lacunas de dados sinalizadas
- Sem inferência de identidade do destinatário a partir do nome de chave Pix

**Estrutura aplicada do F4**

| Bloco | Conteúdo |
|---|---|
| Persona | Analista de prevenção a fraude de banco digital, tom técnico sem alarmismo |
| Constituição | Sem classificar como fraude definitiva, sem bloquear por conta própria, justificativa observável, sem inferir identidade |
| Contexto | Lista de transações em JSON, perfil histórico, indicadores externos |
| Tarefa | Análise em quatro dimensões com nível de suspeita |
| Formato | JSON com schema fechado |

**Quando usar e quando evitar**

| Usar | Evitar |
|---|---|
| Triagem em fila de revisão antifraude | Bloqueio definitivo sem aprovação humana |
| Suporte a operador em revisão de casos | Inferência sobre identidade de terceiros |
| Auditoria de padrões em pós-incidente | Classificação como fraude consumada |
| Triagem em alta volumetria com Haiku | Decisão jurídica sobre processo |

**Anti-padrões observados**
- Classificar como fraude definitiva, ultrapassando escopo
- Justificar suspeita com "parece suspeito" sem padrão observável
- Inferir identidade do destinatário a partir do nome da chave
- Deixar de sinalizar padrão de smurfing por estar abaixo do limite individual

**Modelo recomendado.** Haiku equivalente para alto volume, Sonnet para casos com narrativa explicativa.

**Métrica de qualidade.** Precisão em alta suspeita acima de 80% contra rótulo humano, com recall de 90% em anomalias claras do golden set.

**Versão executável.** [`prompts/P-FIN-01-anomalia-extrato`](https://github.com/falercia/inteligencia-aumentada-recursos/tree/main/prompts/P-FIN-01-anomalia-extrato)

---

#### P-FIN-02 · Classificação de Risco de Crédito PF

**Dor que resolve.** Mesa de crédito precisa de parecer estruturado para cada proposta de PF, com classificação justificada por variável observável, e sem permitir que tempo de relacionamento ou variáveis sensíveis vedadas contaminem a decisão; o prompt entrega classificação em cinco faixas (AA, A, B, C, D) com três fatores determinantes, pontos de atenção para a mesa e ajustes recomendados.

**Domínio.** Crédito pessoa física no Brasil, em produtos de baixo e médio ticket. Não cobre PJ, não decide aprovação, apenas classifica risco e indica pontos de atenção.

**O que o prompt entrega**
- Classificação em AA muito baixo risco, A baixo, B moderado, C alto, D crítico
- Três fatores determinantes com valor observado e impacto na classificação
- Pontos de atenção para a mesa
- Ajustes recomendados (redução de valor, prazo, exigência de garantia)
- Lacunas de dados
- Decisão recomendada à mesa coerente com a classificação

**Estrutura aplicada do F4**

| Bloco | Conteúdo |
|---|---|
| Persona | Analista de crédito sênior em instituição brasileira, tom de parecer para mesa |
| Constituição | Sem decidir aprovação, sem usar variáveis vedadas, sem inferir histórico, comprometimento e score acima de tempo de relacionamento |
| Contexto | Dados da proposta, renda, comprometimento, score, histórico, variáveis comportamentais |
| Tarefa | Classificação em cinco faixas com fatores determinantes |
| Formato | JSON com schema fechado |

**Quando usar e quando evitar**

| Usar | Evitar |
|---|---|
| Triagem pré-mesa de crédito | Decisão final de aprovação automatizada |
| Padronização de critérios de mesa | Uso de variáveis sensíveis vedadas |
| Treinamento de júnior em mesa | Crédito PJ |
| Auditoria de portfólio em pós-concessão | Classificação por intuição sem variável observável |

**Anti-padrões observados**
- Decidir aprovação por conta própria, ultrapassando escopo
- Justificar com "perfil parece bom" sem citar variável observável
- Considerar tempo de relacionamento como suficiente para ignorar comprometimento
- Inferir variável sensível vedada a partir de variável comportamental

**Modelo recomendado.** Sonnet equivalente.

**Métrica de qualidade.** Concordância com analista sênior em pelo menos 85% das classificações, com tolerância de uma faixa em casos limítrofes.

**Versão executável.** [`prompts/P-FIN-02-risco-credito-pf`](https://github.com/falercia/inteligencia-aumentada-recursos/tree/main/prompts/P-FIN-02-risco-credito-pf)

---

#### P-FIN-03 · Súmula de Relatório Trimestral ITR

**Dor que resolve.** Mesa de investidor profissional precisa absorver dezenas de releases trimestrais em janela curta, e a leitura integral de cada release consome tempo desproporcional ao valor incremental do detalhe técnico; o prompt entrega súmula em sete blocos com números literais, sem juízo de recomendação, e marcando lacunas no release.

**Domínio.** Releases de resultado trimestral de empresas listadas brasileiras (ITR), com carta da administração quando disponível. Não cobre recomendação de compra, venda ou manutenção.

**O que o prompt entrega**
- Destaques operacionais
- Performance financeira top line e bottom line com variação T/T e A/A
- Geração de caixa e estrutura de capital
- Guidance e outlook, ou indicação explícita de ausência
- Eventos não recorrentes isolados
- Pontos para Q&A no call
- Lacunas observadas no release

**Estrutura aplicada do F4**

| Bloco | Conteúdo |
|---|---|
| Persona | Analista sell-side sênior brasileiro, tom denso e objetivo |
| Constituição | Apenas dados do release, citação literal, sem recomendação, sem inferir guidance |
| Contexto | Texto do release, carta da administração, trimestre |
| Tarefa | Súmula em sete blocos com fidelidade numérica |
| Formato | Markdown com seções nomeadas |

**Quando usar e quando evitar**

| Usar | Evitar |
|---|---|
| Mesa de buy-side em earnings season | Recomendação de compra ou venda |
| Briefing para comitê de investimento | Análise de fair value |
| Triagem de releases em volume | Projeção de resultados futuros |
| Treinamento de júnior em análise | Modelagem de DCF |

**Anti-padrões observados**
- Emitir recomendação de compra implícita usando adjetivos como "excelente trimestre"
- Arredondar números de forma a distorcer comparação
- Inferir guidance não declarado a partir do tom da carta
- Normalizar câmbio ou base contábil sem o release fornecer a normalização

**Modelo recomendado.** Sonnet equivalente.

**Métrica de qualidade.** Fidelidade numérica de 100% ao release no golden set, e cobertura de todos os sete blocos quando informação está disponível.

**Versão executável.** [`prompts/P-FIN-03-sumula-itr`](https://github.com/falercia/inteligencia-aumentada-recursos/tree/main/prompts/P-FIN-03-sumula-itr)

---

#### P-FIN-04 · Análise de Carteira Recomendada

**Dor que resolve.** Plataformas de investimento publicam carteiras recomendadas e o leitor profissional precisa de descrição descritiva da composição e dos riscos declarados, sem recomendação direta a investidor PF e sem garantia de rentabilidade; o prompt entrega descrição em cinco dimensões com fidelidade ao relatório original.

**Domínio.** Relatórios de carteira recomendada de assessoria brasileira. Não cobre recomendação direta a investidor PF, função reservada a suitability.

**O que o prompt entrega**
- Composição percentual por classe e por instrumento, conforme relatório
- Premissas macroeconômicas declaradas, sem inferência adicional
- Rentabilidade esperada conforme declarada, com horizonte, sem promessa
- Riscos materiais declarados, com sinalização "risco material declarado"
- Adequação ao perfil declarado, descritiva
- Lacunas em premissas esperadas no relatório

**Estrutura aplicada do F4**

| Bloco | Conteúdo |
|---|---|
| Persona | Analista de alocação em plataforma brasileira, sem aconselhar diretamente o investidor |
| Constituição | Sem recomendação direta, citação literal, sem confirmar rentabilidade futura, sem reclassificar perfil |
| Contexto | Texto do relatório, perfil declarado, horizonte |
| Tarefa | Descrição em cinco dimensões |
| Formato | Markdown com seções nomeadas |

**Quando usar e quando evitar**

| Usar | Evitar |
|---|---|
| Comunicação interna de mesa | Recomendação direta a investidor PF |
| Reporting para curadoria de produto | Suitability ou classificação de perfil |
| Briefing executivo de research | Promessa de rentabilidade |
| Treinamento de assessor | Aconselhamento individual |

**Anti-padrões observados**
- Recomendar diretamente ao leitor "compre este ativo"
- Afirmar rentabilidade futura como certa
- Classificar perfil do investidor (função reservada a suitability)
- Inferir probabilidade de cenário não declarada pelo relatório

**Modelo recomendado.** Sonnet equivalente.

**Métrica de qualidade.** Ausência absoluta de recomendação direta no golden set, e identificação correta de pelo menos 90% das lacunas esperadas.

**Versão executável.** [`prompts/P-FIN-04-analise-carteira`](https://github.com/falercia/inteligencia-aumentada-recursos/tree/main/prompts/P-FIN-04-analise-carteira)

---

### SaaS e Produto

#### P-SAAS-01 · Classificação de Feature Request por Persona

**Dor que resolve.** Product managers recebem volume crescente de pedidos de funcionalidade vindos de canais de suporte e sucesso, e a triagem manual em janela útil é cara em tempo do PM sênior; o prompt entrega classificação em cinco dimensões (persona, tema, severidade, potencial de roadmap, categoria de origem), sem prometer entrega e sem inflar severidade por linguagem emocional.

**Domínio.** Feature requests recebidos em SaaS B2B brasileiro, vindos de canais de suporte e CS. Não cobre decisão de priorização final, apenas triagem inicial.

**O que o prompt entrega**
- Persona destinatária do pedido
- Tema de produto e severidade percebida
- Potencial de inclusão em roadmap em três faixas
- Categoria de origem (nova, melhoria, bug, fora de escopo)
- Trecho literal do pedido como evidência
- Sinalização de duplicidade aparente com histórico
- "Necessita refinamento" quando o pedido for ambíguo ou aglomerado

**Estrutura aplicada do F4**

| Bloco | Conteúdo |
|---|---|
| Persona | PM sênior de SaaS B2B brasileiro, tom técnico de triagem |
| Constituição | Sem prometer entrega, citação literal, sem inflar severidade por tom emocional, sem fundir pedidos |
| Contexto | Texto do pedido, persona do cliente, plano, histórico recente |
| Tarefa | Classificação em cinco dimensões |
| Formato | JSON com schema fechado |

**Quando usar e quando evitar**

| Usar | Evitar |
|---|---|
| Triagem em volume alto vinda de CS e suporte | Priorização final em comitê de produto |
| Roteamento automático para PM responsável | Promessa de entrega ao cliente |
| Detecção de duplicidade entre clientes do mesmo segmento | Estimativa de esforço técnico |
| Auditoria de origem de pedidos por canal | Decisão de plano ou pricing |

**Anti-padrões observados**
- Prometer entrega ao classificar, ultrapassando escopo
- Fundir pedidos distintos em registro único
- Atribuir severidade alta por linguagem emocional do cliente
- Classificar pedido de regulação como funcionalidade discricionária

**Modelo recomendado.** Haiku equivalente.

**Métrica de qualidade.** Concordância com PM sênior em pelo menos 80% da classificação multidimensional no golden set.

**Versão executável.** [`prompts/P-SAAS-01-feature-request`](https://github.com/falercia/inteligencia-aumentada-recursos/tree/main/prompts/P-SAAS-01-feature-request)

---

#### P-SAAS-02 · Súmula de NPS Qualitativo

**Dor que resolve.** Operação de pesquisa de cliente acumula milhares de comentários qualitativos por janela, e a leitura humana exaustiva é incompatível com a cadência de produto; o prompt entrega síntese em temas com volume relativo, tom predominante e citações literais, com preservação de tom e marcação de sinais fracos.

**Domínio.** Comentários qualitativos de pesquisa NPS em SaaS B2B brasileiro. Não cobre recomendação de ação de produto, apenas síntese de tema.

**O que o prompt entrega**
- Sumário executivo dos temas dominantes
- Temas positivos, negativos e neutros com volume relativo, tom e citações literais
- Causas hipotéticas quando inferidas do conteúdo
- Sinais fracos (volume baixo) destacados sem elevar
- Lacunas observadas na pesquisa

**Estrutura aplicada do F4**

| Bloco | Conteúdo |
|---|---|
| Persona | Analista de pesquisa de cliente em SaaS brasileiro, tom preservando o respondente |
| Constituição | Sem inventar comentário, citação literal anônima, sem recomendar ação, sem amplificar tom |
| Contexto | Lista de comentários NPS com nota, período, segmentação |
| Tarefa | Síntese em temas com volume, tom e citações |
| Formato | Markdown com seções nomeadas |

**Quando usar e quando evitar**

| Usar | Evitar |
|---|---|
| Briefing executivo pós-survey | Recomendação direta de roadmap |
| Triagem de feedback em volume alto | Decisão de produto sem comitê |
| Identificação de sinais emergentes | Generalização de tema fraco |
| Suporte a QBR com clientes | Análise causal definitiva |

**Anti-padrões observados**
- Inventar comentário para reforçar tema
- Atribuir causa raiz definitiva em vez de causa hipotética
- Recomendar ação de produto
- Elevar sinal fraco a tema dominante pela novidade

**Modelo recomendado.** Sonnet equivalente.

**Métrica de qualidade.** Concordância com analista qualitativo sênior na identificação dos três temas dominantes em pelo menos 90% dos casos.

**Versão executável.** [`prompts/P-SAAS-02-sumula-nps`](https://github.com/falercia/inteligencia-aumentada-recursos/tree/main/prompts/P-SAAS-02-sumula-nps)

---

#### P-SAAS-03 · Geração de Release Notes

**Dor que resolve.** Times de engenharia entregam mudanças semanais ou quinzenais, e a tradução para release notes voltadas a usuário final consome ciclos de technical writing que poderiam ser investidos em documentação principal; o prompt entrega notes organizadas em quatro categorias com destaque para breaking changes, sem inventar funcionalidade nem promover entrega futura.

**Domínio.** Release notes em SaaS B2B brasileiro a partir de lista de mudanças técnicas. Não cobre comunicação de marketing, apenas notas de release técnicas.

**O que o prompt entrega**
- Novidades, Melhorias, Correções e Atenções necessárias
- Cada item com título curto e descrição em uma a três linhas
- Breaking changes em destaque com instrução clara de ação
- Tradução de jargão técnico para impacto ao usuário
- Notas finais sem promessa de futuro

**Estrutura aplicada do F4**

| Bloco | Conteúdo |
|---|---|
| Persona | Technical writer de SaaS brasileiro, tom informativo, sem jargão |
| Constituição | Apenas mudanças listadas, sem promessa futura, breaking change em destaque |
| Contexto | Lista de mudanças técnicas, versão, data, persona |
| Tarefa | Notes organizadas em quatro categorias |
| Formato | Markdown com estrutura fixa de release |

**Quando usar e quando evitar**

| Usar | Evitar |
|---|---|
| Geração rápida pós-release | Comunicação de marketing de produto |
| Padronização de notas entre squads | Anúncio de roadmap futuro |
| Tradução de changelog técnico | Material de venda |
| Documentação de breaking change com instrução | Resolução de vulnerabilidade exposta em detalhe |

**Anti-padrões observados**
- Inventar funcionalidade não listada
- Usar jargão técnico como "refatoramos o módulo X"
- Promover entrega futura, violando a constituição
- Omitir breaking change para evitar comunicação difícil

**Modelo recomendado.** Haiku equivalente.

**Métrica de qualidade.** Aderência à lista de entrada de 100% no golden set, e identificação correta de breaking changes em 100% dos casos.

**Versão executável.** [`prompts/P-SAAS-03-release-notes`](https://github.com/falercia/inteligencia-aumentada-recursos/tree/main/prompts/P-SAAS-03-release-notes)

---

#### P-SAAS-04 · Análise de Churn Signal

**Dor que resolve.** CS Ops precisa identificar clientes em risco de churn antes que a saída se concretize, com plano de ação executável pelo CSM na janela de cinco dias úteis; o prompt entrega classificação em quatro faixas com sinais determinantes, causas hipotéticas e plano de ação dentro do alcance do CSM.

**Domínio.** Carteira de clientes SaaS B2B com variáveis comportamentais e contratuais. Não cobre decisão comercial sobre desconto, e mantém o plano dentro do alcance do CSM.

**O que o prompt entrega**
- Classificação em baixo, atenção, alto, crítico
- Até cinco sinais determinantes com valores literais e peso
- Causas hipotéticas com sinal observável
- Plano de ação para CSM em até cinco passos, todos executáveis em cinco dias úteis
- Lacunas de dados

**Estrutura aplicada do F4**

| Bloco | Conteúdo |
|---|---|
| Persona | CS Operations sênior de SaaS B2B, tom de plano operacional |
| Constituição | Sem confirmar churn como inevitável, citação literal, plano em cinco dias do CSM |
| Contexto | Dados do cliente, sinais comportamentais, histórico CSM |
| Tarefa | Classificação de risco com plano de ação |
| Formato | JSON com schema fechado |

**Quando usar e quando evitar**

| Usar | Evitar |
|---|---|
| Triagem mensal de carteira em risco | Decisão comercial sobre desconto |
| Briefing antes de QBR | Confirmação de churn como certo |
| Roteamento para Account Management | Ação fora do alcance do CSM em cinco dias |
| Padronização de critério em CS Ops | Substituição da conversa direta com cliente |

**Anti-padrões observados**
- Confirmar churn como certo
- Recomendar desconto comercial sem evidência de objeção de preço
- Propor ação fora do alcance do CSM em cinco dias úteis
- Tratar NPS de respondente único como sinal forte

**Modelo recomendado.** Sonnet equivalente.

**Métrica de qualidade.** Concordância com CS Ops em pelo menos 85% das classificações de risco no golden set, e 100% de aderência ao prazo de cinco dias úteis nas ações.

**Versão executável.** [`prompts/P-SAAS-04-churn-signal`](https://github.com/falercia/inteligencia-aumentada-recursos/tree/main/prompts/P-SAAS-04-churn-signal)

---

### Suporte

#### P-SUP-01 · Classificação de Ticket em Severidade

**Dor que resolve.** Tickets chegam em volume crescente com qualidade descritiva variável, e a triagem por critério objetivo (impacto técnico e contratual) precisa resistir à inflação por tom emocional do cliente; o prompt entrega classificação em severidade, prioridade e fila destino com indicadores objetivos exigidos.

**Domínio.** Tickets de suporte em SaaS B2B brasileiro. Não promete prazo de resolução, apenas classifica para fila e prioridade.

**O que o prompt entrega**
- Severidade S1 a S4 baseada em impacto técnico e contratual
- Prioridade alta, média ou baixa
- Fila destino entre N1, N2, produto, billing, segurança
- Trecho literal do relato que sustenta a classificação
- Indicadores objetivos identificados
- Necessidade de escalonamento com motivo objetivo
- Pergunta para cliente quando faltar informação

**Estrutura aplicada do F4**

| Bloco | Conteúdo |
|---|---|
| Persona | Analista de triagem de suporte B2B brasileiro, tom de critério objetivo |
| Constituição | Classifica por impacto técnico e contratual, não por tom emocional, sem prometer prazo |
| Contexto | Texto do ticket, plano, SLA, histórico do cliente |
| Tarefa | Classificação em severidade, prioridade e fila |
| Formato | JSON com schema fechado |

**Quando usar e quando evitar**

| Usar | Evitar |
|---|---|
| Triagem em fila de entrada de suporte | Promessa de prazo de resolução |
| Roteamento automático para fila correta | Decisão sobre conteúdo técnico do ticket |
| Identificação de escalonamento necessário | Substituição da inspeção humana em segurança |
| Padronização de critério entre analistas | Escalada por insatisfação subjetiva |

**Anti-padrões observados**
- Elevar severidade por tom emocional sem indicador técnico
- Prometer prazo de resolução, ultrapassando escopo
- Rotear para escalação por receio de cliente insatisfeito
- Rebaixar S1 por ausência de detalhe técnico em casos de segurança preventiva

**Modelo recomendado.** Haiku equivalente.

**Métrica de qualidade.** Concordância com supervisor de suporte em pelo menos 85% das classificações no golden set, e identificação correta de 100% dos S1.

**Versão executável.** [`prompts/P-SUP-01-severidade-ticket`](https://github.com/falercia/inteligencia-aumentada-recursos/tree/main/prompts/P-SUP-01-severidade-ticket)

---

#### P-SUP-02 · Resposta Empática a Reclamação

**Dor que resolve.** Analistas de suporte precisam responder reclamações com empatia controlada, sem prometer o que não foi formalmente acordado e sem usar fórmulas vazias que pioram a percepção do cliente; o prompt entrega resposta em três parágrafos (reconhecimento, status, oferta dentro dos limites), com tom calmo e profissional.

**Domínio.** Reclamações de cliente em SaaS B2B brasileiro, com ações aprovadas internamente disponíveis. Não promete prazo, desconto, crédito ou reembolso fora do escopo aprovado.

**O que o prompt entrega**
- Resposta sugerida em três parágrafos prontos para envio
- Encaminhamentos internos necessários após o envio
- Pontos não tratados na resposta com motivo de exclusão
- Reconhecimento específico do impacto declarado
- Sem fórmulas vazias de empatia performática

**Estrutura aplicada do F4**

| Bloco | Conteúdo |
|---|---|
| Persona | Analista sênior de suporte, tom empático e profissional |
| Constituição | Sem promessa fora do escopo, sem fórmula vazia, sem culpar terceiros ou cliente |
| Contexto | Texto da reclamação, histórico, ações aprovadas, limites do analista |
| Tarefa | Resposta em três parágrafos com encaminhamentos |
| Formato | Markdown com seções nomeadas |

**Quando usar e quando evitar**

| Usar | Evitar |
|---|---|
| Resposta em fila de reclamação | Posicionamento sobre ameaça jurídica |
| Padronização de tom entre analistas | Promessa não aprovada |
| Treinamento de júnior em manejo | Resposta genérica em múltiplas demandas |
| Apoio em situações de tensão | Reembolso ou crédito não aprovado |

**Anti-padrões observados**
- Prometer reembolso não aprovado
- Culpar cliente por mau uso
- Usar fórmulas vazias de empatia performática
- Posicionar-se sobre mérito de ameaça jurídica ou regulatória

**Modelo recomendado.** Sonnet equivalente.

**Métrica de qualidade.** Concordância com supervisor de suporte sobre adequação da resposta em pelo menos 90% do golden set, e ausência total de promessa fora de escopo.

**Versão executável.** [`prompts/P-SUP-02-resposta-empatica`](https://github.com/falercia/inteligencia-aumentada-recursos/tree/main/prompts/P-SUP-02-resposta-empatica)

---

#### P-SUP-03 · Decisão sobre Escalonamento

**Dor que resolve.** Coordenadores de suporte precisam decidir escalonamento com base em critério objetivo auditável, e resistir à pressão de escalar por insatisfação subjetiva ou por receio de incomodar área superior; o prompt entrega decisão estruturada com critério literal citado, e propõe ação intermediária em casos limítrofes em vez de escalar defensivamente.

**Domínio.** Tickets de suporte com regras de escalonamento explícitas e SLA contratual. Não cobre escalonamento por receio subjetivo.

**O que o prompt entrega**
- Decisão entre escalar, ação intermediária ou manter no nível
- Destino do escalonamento (N2, N3, produto, engenharia, liderança)
- Urgência (imediata, mesmo dia, próximo dia útil)
- Critérios atendidos com texto literal da regra
- Ação intermediária recomendada quando aplicável

**Estrutura aplicada do F4**

| Bloco | Conteúdo |
|---|---|
| Persona | Coordenador de suporte B2B brasileiro, tom de decisão auditável |
| Constituição | Critério explícito, citação literal, sem escalar por sensação, ação intermediária em limítrofes |
| Contexto | Estado do ticket, regras de escalonamento, SLA, histórico |
| Tarefa | Decisão estruturada com critério literal |
| Formato | JSON com schema fechado |

**Quando usar e quando evitar**

| Usar | Evitar |
|---|---|
| Decisão estruturada em fila de coordenação | Escalada por insatisfação subjetiva |
| Auditoria de padrão de escalonamento | Decisão sem critério explícito nas regras |
| Treinamento de coordenador júnior | Substituição da inspeção humana em segurança |
| Padronização entre turnos | Inversão de critério técnico por pressão comercial |

**Anti-padrões observados**
- Escalar por tom emocional do cliente
- Deixar de escalar por receio de incomodar área superior
- Criar critério inexistente nas regras
- Confundir risco comercial com critério técnico de escalonamento

**Modelo recomendado.** Haiku equivalente.

**Métrica de qualidade.** Aderência a critério explícito em 100% das decisões no golden set, e concordância com coordenador em pelo menos 90%.

**Versão executável.** [`prompts/P-SUP-03-escalonamento`](https://github.com/falercia/inteligencia-aumentada-recursos/tree/main/prompts/P-SUP-03-escalonamento)

---

### Recursos Humanos

#### P-RH-01 · Triagem de Currículo com Fit

**Dor que resolve.** Times de recrutamento precisam triagem inicial de currículos contra descritivos de vaga, sem usar variáveis vedadas (idade, gênero, raça, religião, estado civil, orientação sexual, origem regional) e com regra de aprofundamento humano em pontuação limítrofe; o prompt entrega pontuação de fit entre 0 e 1, com encaminhamento obrigatório para aprofundamento humano quando ≤ 0,7.

**Domínio.** Triagem inicial de currículos contra descritivos de vaga em empresas brasileiras. Não decide contratação nem rejeição.

**O que o prompt entrega**
- Pontuação de fit entre 0 e 1 com duas casas decimais
- Status presente, ausente ou parcial para cada competência crítica e desejável
- Trecho literal do currículo como evidência por competência
- Sinais de senioridade observados com evidência
- Pontos a aprofundar em entrevista
- Encaminhamento obrigatório a humano quando fit ≤ 0,7

**Estrutura aplicada do F4**

| Bloco | Conteúdo |
|---|---|
| Persona | Recrutadora sênior brasileira, prática de não discriminação |
| Constituição | Sem variáveis vedadas, citação literal, aprofundamento humano em fit ≤ 0,7, sem rejeição automática |
| Contexto | Descritivo da vaga, currículo, competências críticas e desejáveis |
| Tarefa | Avaliação em três dimensões com pontuação |
| Formato | JSON com schema fechado |

**Quando usar e quando evitar**

| Usar | Evitar |
|---|---|
| Triagem em alto volume de currículos | Rejeição automática sem aprofundamento |
| Padronização de critério não discriminatório | Decisão de contratação |
| Auditoria de processo de seleção | Uso de variáveis vedadas para pontuação |
| Treinamento de recrutador júnior | Inferência sobre características pessoais |

**Anti-padrões observados**
- Pontuar usando idade ou gênero, violando a constituição
- Rejeitar candidato automaticamente sem aprofundamento humano
- Inferir competência sem evidência textual
- Tratar lacuna temporal não explicada como negativa

**Modelo recomendado.** Sonnet equivalente.

**Métrica de qualidade.** Aderência à regra de aprofundamento humano em 100% dos casos com fit ≤ 0,7, e ausência absoluta de uso de variáveis vedadas em auditoria.

**Versão executável.** [`prompts/P-RH-01-triagem-curriculo`](https://github.com/falercia/inteligencia-aumentada-recursos/tree/main/prompts/P-RH-01-triagem-curriculo)

---

#### P-RH-02 · Análise de Feedback 360

**Dor que resolve.** Conversas de desenvolvimento exigem síntese de feedback 360 que preserve anonimato dos respondentes, equilibre forças e pontos a desenvolver sem inflar artificialmente, e marque temas com volume insuficiente; o prompt entrega síntese em quatro blocos com cuidados específicos para a conversa de devolutiva.

**Domínio.** Respostas de feedback 360 com origens genéricas (par, gestor, subordinado, cliente). Não emite veredito sobre a pessoa avaliada, apenas síntese.

**O que o prompt entrega**
- Sumário equilibrado em três a quatro linhas
- Forças predominantes com volume relativo, origens convergentes, exemplos literais
- Pontos a desenvolver com mesma estrutura
- Divergências entre origens (par, gestor, subordinado, cliente)
- Temas com volume insuficiente como sinal fraco
- Cuidados para a conversa de devolutiva

**Estrutura aplicada do F4**

| Bloco | Conteúdo |
|---|---|
| Persona | Consultora sênior de desenvolvimento humano, tom preservando anonimato |
| Constituição | Sem identificar respondente, sem amplificar tom, equilibrio sem inflar lado, sem veredito sobre a pessoa |
| Contexto | Respostas com origem genérica, identificação anônima do avaliado, período |
| Tarefa | Síntese em quatro blocos com preservação de anonimato |
| Formato | Markdown com seções nomeadas |

**Quando usar e quando evitar**

| Usar | Evitar |
|---|---|
| Preparação para conversa de devolutiva | Decisão sobre desempenho ou desligamento |
| Padronização de síntese entre coaches | Identificação de respondente |
| Auditoria de programa de feedback 360 | Veredito sobre a pessoa avaliada |
| Treinamento de líderes em feedback | Tratamento de tema sensível sem canal apropriado |

**Anti-padrões observados**
- Citar trecho identificável
- Amplificar tom negativo em respostas isoladas
- Emitir veredito sobre a pessoa avaliada
- Incluir tema sensível em síntese pública em vez de canal apropriado

**Modelo recomendado.** Sonnet equivalente.

**Métrica de qualidade.** Preservação de anonimato em 100% dos exemplos no golden set, e equilíbrio entre forças e pontos a desenvolver em concordância com consultor sênior em pelo menos 90%.

**Versão executável.** [`prompts/P-RH-02-feedback-360`](https://github.com/falercia/inteligencia-aumentada-recursos/tree/main/prompts/P-RH-02-feedback-360)

---

#### P-RH-03 · Descritivo de Vaga em Linguagem Inclusiva

**Dor que resolve.** Gestores frequentemente fornecem briefing com requisitos artificiais ou linguagem que pode sinalizar preferência discriminatória, e o descritivo final precisa ser inclusivo, com critérios objetivos e sem requisitos artificiais; o prompt entrega descritivo estruturado com requisitos a validar com gestor marcados, e bloqueia escrita em casos de exigência explicitamente discriminatória.

**Domínio.** Vagas em empresas brasileiras com briefing do gestor. Não cobre cargos sob legislação especial não declarada (concursos públicos, magistrados).

**O que o prompt entrega**
- Sobre a oportunidade sem jargão vazio
- Responsabilidades em linguagem clara
- Requisitos obrigatórios enxutos
- Requisitos desejáveis distintos
- Modelo de trabalho, localidade e faixa salarial conforme autorizado
- Requisitos a validar com gestor (lista interna não publicada)

**Estrutura aplicada do F4**

| Bloco | Conteúdo |
|---|---|
| Persona | Redatora sênior de descrição de vagas, prática de não discriminação |
| Constituição | Linguagem neutra, sem requisito artificial, separação entre obrigatórios e desejáveis, bloqueio em requisito discriminatório |
| Contexto | Briefing, cargo, senioridade, modelo de trabalho, faixa salarial |
| Tarefa | Descritivo em linguagem inclusiva |
| Formato | Markdown com seções nomeadas |

**Quando usar e quando evitar**

| Usar | Evitar |
|---|---|
| Geração de descritivo a partir de briefing | Vagas com legislação especial não declarada |
| Padronização de tom inclusivo na empresa | Cargo discriminatório explícito |
| Auditoria de descritivos antigos | Material de marketing de marca empregadora |
| Treinamento de hiring manager | Estimativa salarial sem autorização |

**Anti-padrões observados**
- Usar jargão vazio em sobre a oportunidade
- Aceitar requisito sem justificativa como obrigatório
- Criar linguagem que sugere preferência de gênero
- Aceitar requisito discriminatório explícito (idade, estado civil) sem bloqueio

**Modelo recomendado.** Sonnet equivalente.

**Métrica de qualidade.** Ausência total de linguagem de viés em auditoria, e proporção de requisitos a validar com gestor em pelo menos um terço dos casos limítrofes do golden set.

**Versão executável.** [`prompts/P-RH-03-descritivo-vaga`](https://github.com/falercia/inteligencia-aumentada-recursos/tree/main/prompts/P-RH-03-descritivo-vaga)

---

### Marketing

#### P-MKT-01 · Geração de Copy A/B Testável

**Dor que resolve.** Equipes de marketing de performance precisam gerar variantes de copy A/B com hipóteses semanticamente distintas (não-paráfrases entre si), respeitar limites de canal e restrições de compliance em setores regulados; o prompt entrega quatro variantes com hipóteses explícitas (benefício, prova social, escassez, redução de fricção).

**Domínio.** Copy para canais digitais brasileiros (Google Ads, Meta Ads, e-mail, LinkedIn, in-app). Cobre setores regulados (financeiro, saúde, jurídico) com compliance declarado.

**O que o prompt entrega**
- Quatro variantes com hipótese distinta por variante
- Headline, corpo e CTA dentro do limite de caracteres
- Contagem de caracteres por variante para auditoria
- Aderência à brand voice classificada em três níveis
- Riscos de compliance identificados quando aplicável
- Recomendações de setup de teste e métricas primárias

**Estrutura aplicada do F4**

| Bloco | Conteúdo |
|---|---|
| Persona | Copywriter sênior de marketing de performance, aderência à brand voice |
| Constituição | Sem promessa não sustentada, sem superlativo vazio, dentro do limite, sem violar compliance |
| Contexto | Briefing, persona, canal, limite, brand voice, restrições de compliance |
| Tarefa | Quatro variantes com hipóteses semanticamente distintas |
| Formato | JSON com schema fechado |

**Quando usar e quando evitar**

| Usar | Evitar |
|---|---|
| Geração de pool de variantes para teste | Campanha em setor regulado sem compliance declarado |
| Padronização de hipóteses em performance | Promessa vedada por regulação |
| Suporte a copywriter humano em volume | Campanha em contexto sensível sem revisão |
| Auditoria de aderência à brand voice | Comparação direta com concorrente em setor restrito |

**Anti-padrões observados**
- Criar headline acima do limite de caracteres
- Usar promessa vedada por compliance
- Gerar quatro variantes praticamente iguais
- Ignorar tensão entre brand voice e canal

**Modelo recomendado.** Sonnet equivalente.

**Métrica de qualidade.** Diferença semântica medida entre variantes acima de limiar definido, aderência ao limite de caracteres em 100%, e ausência total de risco de compliance no golden set.

**Versão executável.** [`prompts/P-MKT-01-copy-ab`](https://github.com/falercia/inteligencia-aumentada-recursos/tree/main/prompts/P-MKT-01-copy-ab)

---

#### P-MKT-02 · Análise de Brand Voice

**Dor que resolve.** Times de brand precisam auditar peças contra a brand voice declarada com diagnóstico estruturado dos desvios, sem reescrever a peça e sem emitir juízo estético sem critério; o prompt entrega análise em quatro dimensões (tom, vocabulário, ritmo, persona de marca) com desvios literais classificados em três níveis.

**Domínio.** Peças de comunicação contra brand voice declarada da marca, em canal e formato definidos. Não cobre rebrand ou reformulação de brand voice.

**O que o prompt entrega**
- Sumário de aderência com pontuação geral
- Análise por dimensão com aderência, desvios literais e direção de ajuste
- Desvios graves consolidados em lista priorizada
- Lacunas na brand voice declarada quando insuficiente para análise
- Sem reescrita da peça nem juízo estético

**Estrutura aplicada do F4**

| Bloco | Conteúdo |
|---|---|
| Persona | Diretora de brand de empresa brasileira, tom de diagnóstico estruturado |
| Constituição | Restrita à brand voice declarada, citação literal, sem reescrita, três níveis de desvio |
| Contexto | Brand voice declarada, peça sob análise, canal e formato |
| Tarefa | Análise em quatro dimensões |
| Formato | Markdown com seções nomeadas |

**Quando usar e quando evitar**

| Usar | Evitar |
|---|---|
| Auditoria de peças antes de publicar | Reformulação de brand voice |
| Padronização de revisão entre times | Reescrita da peça |
| Treinamento de redator em aderência | Juízo estético sem critério |
| Identificação de lacunas na brand voice | Análise de marca sem brand voice declarada |

**Anti-padrões observados**
- Reescrever a peça sem ser solicitado
- Inventar diretriz de brand voice
- Emitir juízo estético sem critério
- Classificar tensão contextual (sensível, técnico) como desvio em vez de lacuna

**Modelo recomendado.** Sonnet equivalente.

**Métrica de qualidade.** Concordância com diretor de brand em pelo menos 85% das classificações de nível de desvio.

**Versão executável.** [`prompts/P-MKT-02-brand-voice`](https://github.com/falercia/inteligencia-aumentada-recursos/tree/main/prompts/P-MKT-02-brand-voice)

---

#### P-MKT-03 · Súmula de Pesquisa de Mercado

**Dor que resolve.** Diretores de inteligência precisam absorver relatórios de pesquisa em janela de comitê executivo, com fidelidade à metodologia e preservação das ressalvas, sem extrapolação para escopo não amostrado; o prompt entrega síntese em cinco blocos com metodologia explícita e ressalvas metodológicas em destaque.

**Domínio.** Relatórios de pesquisa de mercado em categoria definida, com metodologia declarada. Não emite recomendação estratégica em primeira mão.

**O que o prompt entrega**
- Sumário executivo dos achados centrais
- Metodologia e amostra literais com limitações
- Principais achados em até sete itens com números literais
- Segmentação relevante conforme o relatório
- Tendências declaradas pelo relatório
- Ressalvas metodológicas priorizadas
- Perguntas que ficam abertas

**Estrutura aplicada do F4**

| Bloco | Conteúdo |
|---|---|
| Persona | Diretora de inteligência de mercado em empresa brasileira, tom denso |
| Constituição | Apenas dados do relatório, citação literal, sem extrapolar amostra, sem recomendação |
| Contexto | Texto do relatório, objetivo declarado, categoria |
| Tarefa | Síntese em cinco blocos |
| Formato | Markdown com seções nomeadas |

**Quando usar e quando evitar**

| Usar | Evitar |
|---|---|
| Briefing executivo pós-pesquisa | Recomendação estratégica em primeira mão |
| Padronização de leitura de research | Extrapolação para escopo não amostrado |
| Identificação de lacunas metodológicas | Comparação direta entre pesquisas distintas |
| Triagem de relatórios em volume | Validação de hipótese sem teste estatístico |

**Anti-padrões observados**
- Extrapolar resultados para escopo nacional sem base
- Emitir recomendação estratégica
- Inventar número não declarado
- Omitir vínculo de interesse do patrocinador da pesquisa

**Modelo recomendado.** Sonnet equivalente.

**Métrica de qualidade.** Fidelidade numérica de 100% no golden set, e identificação de pelo menos uma ressalva metodológica em todos os casos com metodologia frágil.

**Versão executável.** [`prompts/P-MKT-03-sumula-pesquisa`](https://github.com/falercia/inteligencia-aumentada-recursos/tree/main/prompts/P-MKT-03-sumula-pesquisa)

---

### Educação

#### P-EDU-01 · Geração de Plano de Aula

**Dor que resolve.** Professores e coordenadores precisam de planos de aula estruturados alinhados a competências declaradas pelo currículo, com sequência didática coerente com tempo total e instrumento de avaliação alinhado; o prompt entrega plano em sete blocos com pontos que necessitam adaptação por perfil de turma.

**Domínio.** Planos de aula para ensino fundamental, médio e superior brasileiro, com competências declaradas. Não promete resultado de aprendizagem específico.

**O que o prompt entrega**
- Identificação com disciplina, série, tema, duração, competências literais
- Objetivos de aprendizagem
- Pré-requisitos esperados sem assumir conhecimento não declarado
- Sequência didática em tabela com etapa, tempo, descrição, recursos
- Instrumento de avaliação coerente com objetivos
- Atividades de extensão
- Pontos que necessitam adaptação ao perfil da turma

**Estrutura aplicada do F4**

| Bloco | Conteúdo |
|---|---|
| Persona | Coordenadora pedagógica sênior brasileira, tom de plano estruturado |
| Constituição | Apenas competências declaradas, citação literal, soma de tempos coerente com duração, sem prometer resultado |
| Contexto | Disciplina, série, tema, competências, duração, recursos, perfil da turma |
| Tarefa | Plano em sete blocos |
| Formato | Markdown com seções nomeadas |

**Quando usar e quando evitar**

| Usar | Evitar |
|---|---|
| Geração rápida de plano para coordenação | Promessa de resultado de aprendizagem |
| Padronização entre professores da mesma série | Currículo não declarado |
| Apoio a substituto sem tempo de preparação | Aula sem competência alinhada |
| Treinamento de professor novo | Plano em formato não pedagógico |

**Anti-padrões observados**
- Somar tempos das etapas que excedem duração total
- Criar competência não declarada
- Prometer que aluno aprenderá X ao final, ultrapassando escopo
- Prescrever conduta clínica para alunos com necessidades específicas

**Modelo recomendado.** Sonnet equivalente.

**Métrica de qualidade.** Coerência entre soma dos tempos e duração total em 100% dos casos, e concordância com coordenador em pelo menos 90% da adequação pedagógica.

**Versão executável.** [`prompts/P-EDU-01-plano-aula`](https://github.com/falercia/inteligencia-aumentada-recursos/tree/main/prompts/P-EDU-01-plano-aula)

---

#### P-EDU-02 · Avaliação Rubrica-Baseada

**Dor que resolve.** Professores precisam avaliar produções textuais com aderência estrita à rubrica declarada, com feedback construtivo e sem juízo sobre o aluno como pessoa; o prompt entrega avaliação critério por critério com nota ponderada e feedback consolidado em tom construtivo.

**Domínio.** Produções textuais de alunos contra rubrica declarada, em ensino fundamental, médio ou superior. Não emite juízo sobre o aluno como pessoa.

**O que o prompt entrega**
- Avaliação por critério com descritor atingido
- Trecho literal do texto do aluno como evidência
- Justificativa por critério em duas a quatro linhas
- Pontos de revisão por critério
- Nota final ponderada conforme pesos da rubrica
- Feedback consolidado em tom construtivo
- Lacunas na rubrica quando insuficiente

**Estrutura aplicada do F4**

| Bloco | Conteúdo |
|---|---|
| Persona | Professora sênior brasileira, tom respeitoso e construtivo |
| Constituição | Apenas critérios da rubrica, citação literal do aluno, sem juízo sobre a pessoa, tom sem ironia |
| Contexto | Rubrica, texto do aluno anonimizado, série e disciplina, instrução original |
| Tarefa | Avaliação critério por critério com nota ponderada |
| Formato | JSON com schema fechado |

**Quando usar e quando evitar**

| Usar | Evitar |
|---|---|
| Apoio a correção em volume | Decisão final de aprovação sem revisão |
| Padronização entre professores da disciplina | Avaliação sem rubrica declarada |
| Treinamento de professor em avaliação | Diagnóstico clínico do aluno |
| Auditoria de coerência avaliativa | Avaliação de variedade linguística não-padrão como erro fora de critério |

**Anti-padrões observados**
- Emitir juízo sobre o aluno em vez do texto
- Criar critério fora da rubrica
- Dar feedback irônico ou desanimador
- Afirmar plágio sem evidência confirmada

**Modelo recomendado.** Sonnet equivalente.

**Métrica de qualidade.** Concordância com professora sênior em pelo menos 85% das pontuações no golden set, e aderência à rubrica em 100% dos critérios avaliados.

**Versão executável.** [`prompts/P-EDU-02-avaliacao-rubrica`](https://github.com/falercia/inteligencia-aumentada-recursos/tree/main/prompts/P-EDU-02-avaliacao-rubrica)

---

#### P-EDU-03 · Resposta Socrática a Dúvida do Aluno

**Dor que resolve.** Tutores precisam responder dúvidas de alunos em estilo socrático, conduzindo o raciocínio por perguntas progressivas em conteúdo que o aluno deve construir, sem entregar a resposta diretamente; o prompt entrega progressão em até cinco passos com pista mais explícita após três passos com erro persistente.

**Domínio.** Tutoria escolar em ensino fundamental e médio, com política da escola sobre entrega de resposta direta declarada. Não substitui o professor.

**O que o prompt entrega**
- Cinco passos socráticos progressivos
- Pergunta inicial baseada na dúvida
- Pistas crescentes com reconhecimento de acerto
- Pista mais explícita no passo 4 se erro persistir
- Fechamento com reflexão final sem entregar resposta
- Sinalizações para o professor sobre dificuldade conceitual

**Estrutura aplicada do F4**

| Bloco | Conteúdo |
|---|---|
| Persona | Tutor sênior brasileiro, tom socrático e respeitoso |
| Constituição | Sem entregar resposta em conteúdo construído, sem ironia, citação do trecho da dúvida, pista explícita após três passos |
| Contexto | Dúvida do aluno, nível, tema, política da escola |
| Tarefa | Condução em até cinco passos progressivos |
| Formato | Markdown com seções nomeadas por passo |

**Quando usar e quando evitar**

| Usar | Evitar |
|---|---|
| Tutoria assíncrona em plataforma educacional | Entrega de resposta em conteúdo construído |
| Apoio a estudo guiado pelo aluno | Avaliação de produção textual |
| Treinamento de tutor em método socrático | Substituição do professor em sala |
| Diagnóstico de dificuldade conceitual | Resposta a dúvida fora do tema declarado |

**Anti-padrões observados**
- Entregar resposta final em conteúdo construído
- Corrigir com ironia
- Criar exemplo que contradiz tema
- Ceder à pressão de tempo do aluno e entregar resposta

**Modelo recomendado.** Sonnet equivalente.

**Métrica de qualidade.** Ausência de resposta direta em 100% dos casos não permitidos pela política, e concordância com tutor sênior em pelo menos 90% da progressão socrática.

**Versão executável.** [`prompts/P-EDU-03-resposta-socratica`](https://github.com/falercia/inteligencia-aumentada-recursos/tree/main/prompts/P-EDU-03-resposta-socratica)

---

### Transversais

#### P-TR-01 · Extração Estruturada com Schema JSON

**Dor que resolve.** Pipelines de processamento de documentos exigem extração estruturada para schema JSON declarado, com fidelidade ao texto fonte, regra estrita de nulo explícito quando campo está ausente e marcação de ambiguidade quando há ocorrências múltiplas; o prompt entrega extração com auditoria por nó.

**Domínio.** Documentos livres (contratos, propostas, NF-e, prontuários OCR, formulários) para schema JSON declarado. Cobre conversão apenas quando autorizada.

**O que o prompt entrega**
- JSON estritamente conforme o schema declarado
- Null explícito para campos sem evidência (jamais string vazia)
- Trecho literal da fonte para cada campo extraído quando solicitado
- Marcação de ambiguidade quando há ocorrências múltiplas
- Sem conversão de unidade, formato ou data sem instrução
- Sem invenção de identificador, número ou código

**Estrutura aplicada do F4**

| Bloco | Conteúdo |
|---|---|
| Persona | Processador de extração estruturada, tom de fidelidade ao texto fonte |
| Constituição | Apenas o que está literal, null para ausência, sem converter sem instrução, sem inventar |
| Contexto | Schema JSON, texto fonte, instruções específicas de conversão |
| Tarefa | Extração para o schema com auditoria |
| Formato | JSON estrito conforme schema |

**Quando usar e quando evitar**

| Usar | Evitar |
|---|---|
| Pipeline de ingestão documental | Inferência sobre dado não declarado |
| Suporte a OCR estruturado | Conversão de unidade sem autorização |
| Triagem de documentos em volume | Geração de campo fora do schema |
| Padronização de dados de entrada | Completar palavra parcialmente legível |

**Anti-padrões observados**
- Inventar CNPJ quando o documento não traz
- Preencher string vazia em vez de nulo
- Converter data sem instrução
- Criar campo novo no JSON fora do schema

**Modelo recomendado.** Haiku ou Sonnet equivalente conforme complexidade.

**Métrica de qualidade.** Fidelidade ao texto fonte em 100%, ausência total de invenção em auditoria, e marcação correta de ambiguidade em todos os casos do golden set.

**Versão executável.** [`prompts/P-TR-01-extracao-json`](https://github.com/falercia/inteligencia-aumentada-recursos/tree/main/prompts/P-TR-01-extracao-json)

---

#### P-TR-02 · Classificação Multi-Label

**Dor que resolve.** Sistemas de classificação precisam atribuir múltiplos rótulos a conteúdo livre conforme taxonomia declarada, com confiança por rótulo e trecho literal de sustentação, sem inventar rótulo fora da taxonomia nem forçar rótulo único quando há múltiplos válidos; o prompt entrega classificação com fallback explícito.

**Domínio.** Conteúdos livres (tickets, e-mails, comentários, descrições) contra taxonomia declarada. Não cobre criação de novo rótulo dinâmico.

**O que o prompt entrega**
- Rótulos atribuídos com confiança numérica entre 0 e 1
- Trecho literal que sustenta cada rótulo
- Fallback "indeterminado" quando nenhum rótulo atinge confiança mínima
- Rótulos considerados e descartados com motivo
- Sem invenção de rótulo fora da taxonomia
- Sem forçar rótulo único quando há múltiplos válidos

**Estrutura aplicada do F4**

| Bloco | Conteúdo |
|---|---|
| Persona | Classificador multi-label, tom de aderência à taxonomia |
| Constituição | Apenas rótulos da taxonomia, múltiplos quando aplicável, confiança numérica, evidência textual |
| Contexto | Taxonomia, conteúdo, confiança mínima |
| Tarefa | Classificação multi-label com fallback |
| Formato | JSON com schema fechado |

**Quando usar e quando evitar**

| Usar | Evitar |
|---|---|
| Roteamento por taxonomia em alto volume | Criação dinâmica de rótulo novo |
| Triagem com Haiku em baixo custo | Decisão regulatória sem revisão humana |
| Padronização de categorização | Atribuição por intuição sem evidência |
| Auditoria de taxonomia em uso | Forçamento de rótulo único quando há múltiplos válidos |

**Anti-padrões observados**
- Inventar rótulo fora da taxonomia
- Forçar rótulo único quando há múltiplos válidos
- Atribuir confiança alta sem evidência citada
- Usar "outros" como rótulo padrão sem testar especificidade

**Modelo recomendado.** Haiku equivalente.

**Métrica de qualidade.** Aderência à taxonomia em 100%, F1 multi-label acima de limiar declarado contra rotulagem humana, e fallback correto em ambíguos do golden set.

**Versão executável.** [`prompts/P-TR-02-multi-label`](https://github.com/falercia/inteligencia-aumentada-recursos/tree/main/prompts/P-TR-02-multi-label)

---

#### P-TR-03 · Recusa Estruturada com Fallback

**Dor que resolve.** Sistemas em produção recebem inputs fora do escopo declarado e a recusa precisa ser estruturada, respeitosa, com fallback humano claro e sem revelar prompt interno ou estrutura do sistema; o prompt entrega recusa com motivo literal, mensagem ao usuário e registro de auditoria.

**Domínio.** Módulo de governança de escopo em qualquer sistema com escopo declarado e canais de fallback humano disponíveis. Cobre tentativas de injection, extração e tráfego automatizado.

**O que o prompt entrega**
- Verificação de aderência ao escopo declarado
- Motivo literal da recusa com base no escopo
- Mensagem ao usuário em tom respeitoso, três a cinco linhas
- Canal de fallback humano indicado quando aplicável
- Registro de auditoria com categoria, necessidade de revisão humana e padrão detectado

**Estrutura aplicada do F4**

| Bloco | Conteúdo |
|---|---|
| Persona | Módulo de governança de escopo, tom respeitoso |
| Constituição | Restrita ao escopo, recusa integral, motivo literal, fallback claro, sem revelar prompt interno |
| Contexto | Escopo declarado, canais de fallback, input recebido, histórico de tentativas |
| Tarefa | Verificação e recusa estruturada |
| Formato | JSON com schema fechado |

**Quando usar e quando evitar**

| Usar | Evitar |
|---|---|
| Módulo de governança em sistema em produção | Atendimento parcial a pedido fora de escopo |
| Detecção de tentativa de injection | Decisão de bloqueio definitivo do usuário |
| Padronização de recusa entre produtos | Resposta a tema dentro do escopo |
| Registro de padrão de uso indevido | Tom culpabilizante ao usuário |

**Anti-padrões observados**
- Tentar atender parcialmente pedido fora de escopo
- Revelar trecho de prompt interno na resposta
- Culpabilizar o usuário pela pergunta
- Recusar input dentro do escopo por interpretação literal estreita

**Modelo recomendado.** Haiku equivalente.

**Métrica de qualidade.** Taxa de recusa correta em 100% dos inputs fora do escopo do golden set, ausência total de revelação de prompt interno, e oferta de fallback em 100% dos casos com canal disponível.

**Versão executável.** [`prompts/P-TR-03-recusa-fallback`](https://github.com/falercia/inteligencia-aumentada-recursos/tree/main/prompts/P-TR-03-recusa-fallback)

---

## Changelog editorial dos prompts

Esta seção documenta a evolução de seis prompts marcados como referência de iteração na biblioteca, registrando o que mudou em relação à primeira versão e por quê. O objetivo é evitar que a biblioteca seja lida como showroom limpo demais, mostrando que cada prompt em produção carrega cicatriz de iteração, e que essa cicatriz é parte do ativo, não da vergonha. A política editorial é registrar, a cada release, uma entrada por prompt alterado, com data, motivo e impacto observado em golden set ou em produção.

#### P-LEG-01 — Revisão de cláusula de não-concorrência CLT
A primeira versão trazia um único exemplo de cláusula complexa dentro do bloco de tarefa, com o objetivo didático de mostrar ao modelo o tipo de cláusula esperada. Testes em modelos de família média mostraram que o exemplo era copiado quase literalmente em respostas a inputs próximos, contaminando a análise. A versão atual eliminou o exemplo único, reforçou a regra de citação literal do trecho recebido na constituição, e ampliou o golden set de três para vinte entradas com contraste explícito entre cláusulas válidas, limítrofes e nulas, o que reduziu o efeito de cópia para próximo de zero em modelos pequenos.

#### P-MED-01 — Triagem de sintomas com recusa por escopo
A primeira versão usava como ação padrão "encaminhar para avaliação médica" em qualquer dúvida, o que se mostrou subóptimo em casos de emergência clara, em que a recomendação correta deveria ser SAMU 192 sem rodeio. A versão atual introduziu a regra constitucional de escolher sempre o nível mais conservador em caso de dúvida, separou explicitamente as faixas de emergência, urgência e eletiva no schema de saída, e adicionou o bloco de self-critique para forçar o modelo a revisar se classificou de forma conservadora antes de devolver o JSON. Sensibilidade para emergência subiu para próximo de cem por cento no golden set ampliado.

#### P-FIN-02 — Classificação de risco de crédito PF
A primeira versão permitia que o modelo justificasse decisão de classificação combinando tempo de relacionamento com score, o que produzia decisões otimistas demais em casos de clientes antigos com sinais recentes de stress financeiro. A versão atual reforçou na constituição que comprometimento e score atuais têm prioridade sobre tempo de relacionamento, e o bloco de self-critique força explicitamente a verificação de inconsistência entre classificação e fatores observáveis. O golden set foi ampliado de três para vinte entradas, incluindo casos limítrofes com volatilidade de renda, contestação em bureau e primeiro acesso ao crédito sem score.

#### P-LEG-03 — Red flags em contrato M&A
A primeira versão pedia justificativa textual livre para cada red flag, o que gerava análises longas e difíceis de comparar entre execuções. A versão atual moveu o formato de saída para JSON com schema fechado, separando classificação em três níveis estáveis (alerta_informativo, ponto_de_negociacao, clausula_bloqueante), e adicionou self-critique forçando a revisão da coerência entre nível e justificativa. Em paralelo, a constituição foi reforçada para não emitir veredito final de fazer ou não fazer o deal, depois que duas execuções iniciais produziram recomendações de "walk away" sem amparo no escopo solicitado.

#### P-SUP-01 — Classificação de ticket em severidade
A primeira versão classificava tickets como S1 quando o cliente usava tom emocional forte ("urgentíssimo", "vou cancelar"), mesmo sem indicador objetivo de impacto em produção. A revisão introduziu a regra constitucional explícita de classificar por impacto técnico e contratual, não por tom emocional, e o schema de saída passou a exigir "indicadores_objetivos" como array obrigatório, o que força o modelo a listar evidência observável antes de atribuir severidade alta. O efeito foi queda de aproximadamente quarenta por cento na taxa de falso S1 em testes internos.

#### P-EDU-02 — Avaliação rubrica-baseada
A primeira versão entregava o feedback consolidado primeiro e a avaliação por critério depois, o que fazia com que modelos em respostas longas escrevessem o feedback antes de ter analisado os critérios e depois ajustassem a análise para "bater" com o feedback. A versão atual inverteu a ordem (critério primeiro, feedback consolidado depois), e o prefill foi escrito para iniciar a resposta pelo bloco de "avaliacao_por_criterio", garantindo que a análise critério a critério aconteça antes do consolidado. A coerência entre nota final e pontuação por critério subiu acima de noventa e cinco por cento em testes internos.

---

*Apêndice L · Biblioteca de Prompts Profissionais. Versão executável em [github.com/falercia/inteligencia-aumentada-recursos](https://github.com/falercia/inteligencia-aumentada-recursos). Política editorial: instrumento vivo, sem cadência fixa anunciada.*

</div>
</section>



<section class="apendice-bloco">
<div class="abertura-apendice">

<div class="selo-apendice">Apêndice</div>

# Apêndice M — Síntese: Os Nove Princípios em Uma Página

> *Imprima. Cole na parede. Distribua ao time. Leve para a próxima decisão de IA.*

---

## Os Nove Princípios

### 1 — Plausibilidade
**"O modelo entrega o plausível, não o verdadeiro — e os dois coincidem, até a hora em que não."**
*Mecânica:* o modelo de linguagem é motor de plausibilidade; calibrar confiança é trabalho do operador, em proporção ao custo do erro.
*Violação típica:* aceitar número jurídico ou financeiro porque soou certo.

### 2 — Extremidades
**"O meio do contexto é onde a informação vai morrer."**
*Mecânica:* atenção alta nas pontas, diluída no centro; densidade de relevância vence volume bruto.
*Violação típica:* enterrar a regra crítica no parágrafo quarenta do prompt.

### 3 — Camada Dupla
**"Decore o padrão, consulte o número."**
*Mecânica:* o que muda em semanas vive em apêndice datado; o que dura por anos vive na cabeça.
*Violação típica:* memorizar que o modelo X lidera o benchmark Y e ficar obsoleto no próximo release.

### 4 — Encaixe
**"Escolha pelo padrão da tarefa, nunca pela versão da moda."**
*Mecânica:* o modelo decide-se por eixo, código, matemática, multimodal, contexto longo, custo, não pelo lançamento da semana.
*Violação típica:* migrar o stack para o release recente sem teste cego na carga real.

### 5 — Custo Composto
**"Trivial é o preço do token; o que quebra o orçamento é quantas vezes você o paga."**
*Mecânica:* custo é tokens vezes chamadas vezes tier vezes redundância; as alavancas são arquiteturais.
*Violação típica:* otimizar prompt enquanto um loop de agente dispara quarenta chamadas redundantes.

### 6 — Autonomia Proporcional
**"Só dê ao agente a autonomia que você consegue medir e desfazer."**
*Mecânica:* o nível de agência é função da capacidade de rastrear e reverter.
*Violação típica:* agente com escrita em produção sem tracing nem kill switch.

### 7 — Termômetro
**"IA sem eval é fé, não engenharia."**
*Mecânica:* nenhum sistema entra em produção sem detecção de regressão; prompt sem golden set é opinião.
*Violação típica:* trocar prompt porque ficou melhor sem dataset que prove que não piorou.

### 8 — Responsabilidade Indelegável
**"A IA executa; a responsabilidade tem sempre um nome humano."**
*Mecânica:* toda saída em produção tem dono, controle de acesso, trilha de auditoria e caminho de reversão.
*Violação típica:* foi a IA que decidiu, como desculpa para decisão que ninguém assume.

### 9 — Operador
**"A IA multiplica competência e incompetência pelo mesmo fator."**
*Mecânica:* o ganho vem do operador que sabe pedir, rejeitar e validar.
*Violação típica:* esperar que a IA cubra a falta de critério de quem a opera.

---

## A frase-síntese

> ## *Modelos passam. Método fica.*

---

## Como usar

| Situação | Pergunte-se |
|----------|-------------|
| Vou escolher um modelo | Princípio 4: qual o encaixe por eixo de tarefa? |
| Vou subir um agente | Princípio 6: tenho tracing e rollback proporcionais? |
| Vou trocar um prompt em produção | Princípio 7: rodou contra o golden set? |
| Vou apresentar a iniciativa à diretoria | Princípios 8 e 9: há dono e há decisão estruturada? |
| Vou cortar custo de IA | Princípio 5: mexi nas três alavancas arquiteturais? |
| Vou citar um benchmark | Princípio 3: conferi a data e a fonte? |

---

## Ressalva

Os Princípios 1 (Plausibilidade) e 2 (Extremidades) dependem da arquitetura generativa atual. Arquiteturas futuras podem mudar a mecânica. Os outros sete são princípios de prática e julgamento, independentes de arquitetura.

---

## Atribuição

Os Nove Princípios Permanentes da Inteligência Artificial — sistema da obra *Inteligência Aumentada* (Fabio Garcia, 2026). Distribuição livre com atribuição.

</div>
</section>



<section class="apendice-bloco">
<div class="abertura-apendice">

<div class="selo-apendice">Apêndice</div>

# Apêndice N — Metodológico, sobre os números deste livro

> **Atualizado em:** junho de 2026
> **Próxima revisão:** anual, ou sob mudança relevante na base de auditorias operacionais

---

## 1. Por que este apêndice existe

Toda obra técnica que pretende durar precisa expor o piso epistemológico sobre o qual seus números repousam. Em IA, o piso é mais frágil do que parece. Modelos mudam, preços mudam, benchmarks mudam, populações de uso mudam, e qualquer número específico tem vida útil curta. O leitor merece saber, com clareza, qual é a origem de cada número usado no corpo do livro, qual é a postura adotada quando o número aparece sem fonte primária, e qual é o roteiro que o autor seguirá para revisar o material em ciclos futuros.

Este apêndice cumpre três funções. Primeira, declara a postura epistemológica do livro em relação a números. Segunda, classifica todas as afirmações quantitativas relevantes em quatro tipos, com tratamento próprio para cada um. Terceira, lista os números críticos que precisam de revisão programada e a cadência sugerida.

---

## 2. Postura epistemológica

A obra trabalha em três camadas de conhecimento, conforme o Princípio Três e o Framework Nove. A camada do padrão, que é frameworks, princípios operacionais e arquiteturas duráveis, vive no corpo dos capítulos. A camada do número, que é preço, benchmark, versão de modelo, posição regulatória, vive no Apêndice J, com data e fonte. A camada do exemplo, que é caso ilustrativo composto a partir de padrões observados, vive nos boxes memoráveis dos capítulos, com rótulo explícito.

Números são usados em três modos. Modo definicional, quando o número é parte do desenho do framework e não pretende descrever o mundo, por exemplo "cobertura de cem por cento na camada base da Pirâmide de Avaliação". Modo observacional, quando o número descreve faixa colhida de auditorias operacionais, com qualificador adequado, por exemplo "tipicamente entre quarenta e setenta por cento de economia em operações que migram para roteamento por tier". Modo ilustrativo, quando o número aparece em cenário composto que serve para ensinar padrão, por exemplo "fatura de cento e quarenta e dois mil reais caiu para quarenta e sete mil em três meses".

A regra editorial é simples. Número em modo definicional não exige fonte. Número em modo observacional exige qualificador, e quando descrever afirmação categórica que sustenta tese, exige link para experimento reproduzível ou para fonte primária. Número em modo ilustrativo exige rótulo de "cenário composto a partir de padrões observados", deve sempre vir sem identificação de empresa real e, quando descrever resultado, deve respeitar a ordem de grandeza típica do setor.

---

## 3. Classificação das afirmações quantitativas

Toda afirmação quantitativa relevante do livro foi mapeada em quatro tipos, conforme a tabela abaixo.

### Tipo A — Fonte necessária

Afirmação categórica que sustenta tese ou diagnóstico estrutural. Exige link para fonte primária, paper, documentação oficial ou leaderboard público, com data da consulta. Exemplos no livro: "português usa quarenta a sessenta por cento mais tokens que inglês"; "custo de treinar modelo de fronteira em 2026 está entre cinquenta e quinhentos milhões de dólares"; "output costuma custar entre três e cinco vezes mais que input"; "modelos modernos chegam a um ou dois milhões de tokens de janela em 2026".

Tratamento editorial: nota de rodapé com link na primeira aparição, atualização cruzada no Apêndice J quando se tratar de preço, benchmark ou versão de modelo.

### Tipo B — Exemplo composto

Números que aparecem em casos memoráveis compostos a partir de padrões observados em auditorias reais. Exemplos no livro: "Banco Solar, fintech com aproximadamente quatrocentas pessoas em 2024, três migrações em quatro meses"; "Pólice.io, fatura de cento e quarenta e dois mil reais caiu para quarenta e sete mil em três meses"; "fintech do Cap 11, trezentas mil consultas por mês, custo caiu setenta e três por cento após context engineering".

Tratamento editorial: rótulo explícito de "cenário ilustrativo composto a partir de padrões observados". Nomes de empresa fictícios. Faixa de valores plausível para o setor descrito. Nenhuma afirmação de validação por NDA até que efetivamente exista NDA com cliente real disposto à atribuição.

### Tipo C — Auto-evidente

Números que são parte do desenho do framework e não descrevem o mundo. Exemplos no livro: "cinco blocos no F4"; "três alavancas no F7"; "cobertura de cem por cento na camada base do F8"; "cobertura de cinco a quinze por cento na camada topo do F8"; "matriz quatro por quatro no F3".

Tratamento editorial: nenhum, pois o número é parte da definição. Aparece sem fonte porque é o próprio framework.

### Tipo D — Estimativa honesta

Números que descrevem faixa observada com qualificador explícito que protege contra leitura literal. Exemplos no livro: "tipicamente entre setenta e quinhentos bilhões de parâmetros em modelos de fronteira em 2026"; "em média entre um vírgula três e um vírgula cinco tokens por palavra em inglês"; "trinta a sessenta por cento de economia típica observada na primeira alavanca do F7".

Tratamento editorial: qualificador presente, data da observação implícita ou explícita, e quando aparecer em capítulo central, link para metodologia da auditoria que originou a faixa.

---

## 4. Tabela de números críticos com cadência de revisão

A tabela abaixo lista os números que mais envelhecem rápido na obra, organizados por cadência de revisão necessária. Itens da cadência crítica são revisados a cada seis meses. Itens da cadência moderada são revisados anualmente. Itens da cadência estável são revisados a cada dois ou três anos.

| Cadência | Número | Capítulo | Tratamento |
|---|---|---|---|
| Crítica | Preço por token dos provedores de fronteira | C03, C15, C18 | Movido para Apêndice J, datado, sem cadência fixa |
| Crítica | Janela máxima de contexto em fronteira | C02, C04 | Movido para Apêndice J, datado, sem cadência fixa |
| Crítica | Custo de treinar modelo de fronteira | C02 | Faixa qualificada como "estimativa pública até [ano]", citando Epoch AI e statements oficiais |
| Crítica | Score do líder em GPQA, SWE-bench, AIME, HLE | C15 | Movido para Apêndice J, datado, sem cadência fixa |
| Crítica | Estado de PL 2338 no Brasil | C19, C24 | Movido para Apêndice J, datado |
| Moderada | Tamanho típico de modelo em parâmetros | C02 | Faixa qualificada com "tipicamente", revisão anual |
| Moderada | Taxa de tokens por palavra em português versus inglês | C03 | Acompanhar versionamento de tokenizers principais; nota de rodapé com link para experimento público |
| Moderada | Ranges típicos de economia por alavanca do F7 | C18, F7 | Manter qualificador "típica observada", revisão anual com auditorias adicionadas |
| Moderada | Distribuição entre as três zonas de Lost in the Middle | C04 | Acompanhar papers que aprofundem Liu et al. 2023 e variantes |
| Estável | Os nove Princípios e as suas mecânicas | Manifesto | Reescrita só sob mudança de arquitetura dominante (saída de Transformers) |
| Estável | Arquitetura básica de tokenizer BPE | C03 | Reescrita só sob substituição da família BPE no mercado |
| Estável | Mecanismo de atenção em transformers | C02 | Reescrita só sob substituição da arquitetura |

---

## 5. Auditoria das afirmações quantitativas do manuscrito

Foi feita varredura sistemática do manuscrito da Obra Um buscando todas as afirmações com números, percentuais, intervalos e métricas. A varredura identificou aproximadamente noventa afirmações quantitativas relevantes no corpo dos capítulos, frameworks e apêndices, distribuídas conforme a tabela a seguir.

| Tipo | Quantidade aproximada | Tratamento editorial agregado |
|---|---|---|
| A — Fonte necessária | 18 | Nota de rodapé com link na primeira aparição, atualização cruzada no Apêndice J |
| B — Exemplo composto | 24 | Rótulo "cenário ilustrativo composto a partir de padrões observados" em todos |
| C — Auto-evidente | 31 | Sem alteração, pois é definição |
| D — Estimativa honesta | 14 | Qualificador presente verificado em todos, revisão para garantir consistência |

Auditoria detalhada por capítulo, com a lista linha a linha das afirmações classificadas em cada tipo, ficou registrada no repositório acompanhante. O leitor que quiser auditar item a item pode consultar o documento "auditoria-quantitativa-l1.md" no repositório, atualizado a cada revisão do manuscrito.

---

## 6. Por que não citar fonte inline em todos os números

Algumas obras técnicas optam por nota de rodapé em cada número. A escolha deste livro é deliberadamente diferente, por três motivos.

Primeiro, os números mais voláteis foram movidos para o Apêndice J. Isso libera o corpo dos capítulos para defender padrão sem ruído de versionamento. O leitor que precisar do número exato consulta o Apêndice J na data da decisão.

Segundo, os números mais usados na obra são qualificados como faixa observada, com palavra como "tipicamente", "observado em", "cerca de", o que evita pretensão de precisão que não se sustenta. Faixa qualificada não exige fonte pontual, exige metodologia da auditoria, que está descrita neste apêndice.

Terceiro, as afirmações categóricas que sustentam tese estrutural recebem nota de rodapé com link na primeira aparição. São aproximadamente quinze a vinte casos no livro inteiro, e a contenção é deliberada, para que a nota seja sinal de que o número importa, em vez de virar ruído onipresente.

A combinação dessas três regras mantém o livro legível, deixa o número auditável quando necessário, e protege o autor contra o envelhecimento que afetaria qualquer obra que prometesse precisão que o campo não permite.

---

## 7. Compromisso com revisão futura

A próxima revisão deste apêndice acompanha o ciclo anual da obra. A cada doze meses, a tabela do item 4 é reavaliada, a base de auditorias operacionais que sustenta os números do Tipo B e do Tipo D é atualizada, e qualquer afirmação que tenha mudado de classificação por mudança no campo é registrada no log de revisão.

O log de revisão fica público no repositório acompanhante, com três campos por entrada: data da revisão, item revisado, motivo da revisão. O leitor que quiser entender por que tal número mudou na quarta edição em relação à primeira pode consultar o log e reconstituir o histórico.

---

*Apêndice N — Metodológico. Próxima revisão programada: junho de 2027.*

</div>
</section>



<section class="apendice-bloco">
<div class="abertura-apendice">

<div class="selo-apendice">Apêndice</div>

# Apêndice O — Caderno de Governança de IA

## Por que este apêndice existe em duas camadas

O Caderno de Governança de IA é o artefato prometido pelo Framework Seis, e foi pensado desde a primeira versão como instrumento vivo, no sentido estrito de que deve ser preenchido com nomes humanos, assinado pela diretoria, revisado em cadência trimestral, atualizado a cada incidente material, e auditado contra evidência de execução, jamais contra a sua própria existência publicada. Um caderno que dorme em PDF assinado e não volta à mesa por seis trimestres seguidos não é governança ativa, é teatro de compliance, e a obra trata teatro como pior do que ausência declarada de governança, porque teatro mente para o conselho.

Construir um caderno desse tipo exige duas peças que vivem em andares diferentes, e a obra trata cada uma delas no andar certo. A primeira peça é o padrão durável, e ela vive aqui no livro, na forma de uma ficha conceitual única que entrega a anatomia do caderno, os princípios que o sustentam, os critérios de quando o modelo se aplica e quando exige adendo setorial, os padrões de adaptação ao contexto da organização, os anti-padrões observados em prática e a métrica que separa caderno vivo de caderno morto. A ficha é o que o executivo precisa entender para customizar o modelo ao próprio contexto, para defender a estrutura diante de auditoria externa e para reconhecer quando o caderno da sua casa começou a degradar.

A segunda peça é o caderno operacional executável, e ela vive no repositório acompanhante público em [github.com/falercia/inteligencia-aumentada-recursos/tree/main/governance/v1](https://github.com/falercia/inteligencia-aumentada-recursos/tree/main/governance/v1), em pasta dedicada, com o caderno inteiro em um arquivo único pronto para imprimir e assinar, as seis seções fatiadas em arquivos separados para edição independente por área, a lista dos seis anexos referenciados com modelos clonáveis, e o changelog editorial datado a cada revisão. Quem chega à ficha do livro com clareza conceitual encontra no repositório o artefato pronto para clonar, customizar, assinar e colocar em revisão trimestral, sem ter que reescrever cada seção do zero, e sem ter que decidir quais campos um caderno mínimo precisa ter.

Essa separação é deliberada e materializa o Princípio Três, a Camada Dupla. O padrão dura porque a estrutura conceitual de governança de IA sobrevive à próxima geração de modelo, ao próximo provedor, à próxima moda de framework, e à próxima onda regulatória, ainda que cada onda exija adendo específico sobre o que a versão atual do caderno carrega. O número muda porque o conteúdo dos dez controles vai sofrer iteração mensal conforme novos vetores de incidente apareçam em produção, conforme reguladores publiquem novas exigências, e conforme a comunidade de operadores brasileiros de IA contribua com calibração de RACI por setor. Manter as duas peças no mesmo arquivo, como faziam as primeiras versões deste apêndice, congelava o caderno em mídia impressa e impedia a evolução contínua do ativo. O leitor que entendeu o método vai ao repositório quando precisa do executável, e fica com a ficha quando precisa do método.

### Quadro de orientação — onde vive o quê

| Camada do conhecimento | Onde vive | Cadência de revisão |
|---|---|---|
| Anatomia dos seis blocos, princípios condutores, padrões de adaptação ao contexto, anti-padrões transversais, métrica de caderno vivo versus caderno morto | **LIVRO · ficha conceitual** | Anual, junto com a próxima edição |
| Caderno completo pronto para imprimir e assinar, seis seções fatiadas para edição independente, modelos dos seis anexos referenciados, changelog editorial datado | **REPO · `/governance/v1/`** | Sem cadência fixa, conforme evolução do instrumento |
| Calibração regulatória corrente (LGPD, AI Act, NIST AI RMF), adendos setoriais publicados, casos de incidente material registrados como lição pública | **APÊNDICE J · Trilha do Número** | Periódico, com fonte primária por linha |

### Quadro de navegação — onde começar dependendo da sua dor

> *Este caderno é instrumentação operacional de dois lugares da obra. O Framework Seis entrega a tese de governança indelegável e o porquê de cada bloco. O Capítulo 19 entrega o vocabulário de incidente e o desenho de severidades que sustenta o plano de resposta. Consulte os dois antes para o porquê do caderno; volte aqui para o como, e desça ao repositório para o pronto-para-assinar.*

| Se sua dor é | Comece por | Volte aqui para |
|---|---|---|
| Convencer a diretoria do porquê de governança formal | F6 — Governança Indelegável | Customizar a ficha conceitual ao vocabulário da casa |
| Construir o playbook de SEV-1 antes do primeiro incidente | C19 — Segurança e Riscos | Acoplar o plano de incidente do caderno ao desenho de severidades |
| Preencher o caderno operacional na próxima semana | `/governance/v1/` no repositório | Validar adaptação contra os sete padrões e os dez anti-padrões |
| Auditar caderno existente que parou de evoluir | Métrica de caderno vivo nesta ficha | Acionar diretoria com leitura dos sete indicadores em vermelho |

---

## A anatomia que toda governança de IA precisa fechar

Antes da ficha em si, vale percorrer uma única vez a anatomia do caderno, em seis blocos, com a função de cada um e a razão de estar naquela posição. A ordem dos blocos não foi escolhida por estética, ela emergiu da experiência de diretorias que tentaram montar caderno em ordem diferente, e descobriram tarde demais que sem identificação clara não há accountable, sem RACI específico não há decisão rastreável, e sem plano de incidente assinado não há resposta calibrada quando a crise vier.

| Bloco | Função | Por que está nesta posição |
|---|---|---|
| 1. Identificação, escopo e princípios | Define quem assina, o que está dentro e o que está fora, e quais princípios condutores a organização adota | Primeiro porque sem nome do patrocinador executivo e do responsável operacional, o caderno é documento órfão; sem escopo declarado, controles aplicáveis ficam ambíguos |
| 2. RACI e Comitê de IA | Atribui Accountable único por classe de decisão recorrente e define o órgão executivo permanente | Cedo no caderno porque o Princípio Oito, Responsabilidade Indelegável, exige que toda decisão tenha nome humano antes de qualquer controle técnico ser cobrado |
| 3. Política de uso aceitável (AUP) | Declara o que é permitido, o que é proibido e as sanções pelo descumprimento, para todo colaborador e prestador | No meio porque depende do escopo declarado no bloco 1 e do Accountable definido no bloco 2, e antecede os controles operacionais que vão fiscalizar a aderência |
| 4. Dez controles canônicos com nível de maturidade | Estabelece os controles técnicos, operacionais e executivos auditáveis, com maturidade autodeclarada e meta no horizonte de doze meses | Depois da AUP porque os controles fiscalizam a aderência à AUP e ao RACI; antes do plano de incidente porque incidente é falha de controle, e sem controle declarado a classificação de falha fica subjetiva |
| 5. Plano de incidente e severidades | Calibra detecção, resposta, comunicação e postmortem por nível de severidade | Penúltimo porque incidente é o estresse-teste de tudo que veio antes, e sem o que veio antes não há base de comparação para julgar a resposta |
| 6. Assinaturas, anexos e revisão | Vincula a diretoria ao compromisso, lista os anexos vivos do caderno e declara a política de revisão trimestral | Último porque assinatura é ato de fechamento, anexos são extensões controladas, e revisão é o motor que mantém o caderno vivo |

Os seis blocos compõem um documento de cerca de seis páginas no caderno operacional executável. A ficha no livro entrega o método para customizar cada bloco. O repositório entrega cada bloco em arquivo separado, com placeholders nomeados, para que a organização preencha em paralelo entre as áreas responsáveis.

---

## Os nove princípios que sustentam o caderno

O caderno opera sobre os Nove Princípios da obra, com ênfase em quatro deles que carregam a maior parte do peso operacional do instrumento. O leitor que precise revisitar os princípios em sua versão completa encontra a discussão no Framework Seis, e a síntese de bolso no Apêndice M.

| Princípio | Como o caderno materializa |
|---|---|
| Princípio 1 · Plausibilidade não verdade | A AUP veda atribuir autoria humana a conteúdo gerado integralmente por IA quando a atribuição importa ao destinatário, e exige revisão humana proporcional ao risco em decisão crítica |
| Princípio 3 · Camada dupla | O próprio caderno é Camada Dupla aplicada, com o método aqui no livro e o número datado no repositório acompanhante |
| Princípio 6 · Propriedade do agente | A matriz RACI exige Accountable nomeado para promoção de agente entre níveis de autonomia, e o controle número três exige kill switch testado em simulado |
| Princípio 8 · Responsabilidade indelegável | A regra fundamental do caderno é que toda decisão de IA tem nome humano único, e quando alguém disser "foi a IA que decidiu", a organização precisa saber em até cinco minutos de quem é a cadeira |

Os outros cinco princípios aparecem de forma distribuída no caderno, e estão listados na íntegra na seção 1.3 do caderno operacional executável em `governance/v1/01-identificacao-escopo-principios.md`.

---

## Quando adotar este modelo, e quando ele exige adendo setorial

O caderno foi calibrado para organização brasileira entre cinquenta e cinco mil colaboradores, com uso de IA em produção em pelo menos um caso de uso material, e sem operação em setor criticamente regulado em que o regulador exija instrumento de governança próprio. Fora dessa faixa, o caderno continua útil como ponto de partida, mas exige adendo específico.

| Adotar como está | Exige adendo setorial antes de adotar |
|---|---|
| Organização entre 50 e 5000 colaboradores em qualquer setor | Instituição financeira sob CMN 4658/2018 e regulação prudencial específica do Banco Central |
| Adoção primeira de governança formal de IA | Hospital ou operadora de saúde sob ANS, com prontuário eletrônico tocado por IA |
| Operação multi-cloud com modelos próprios e de terceiros | Governo, autarquia ou empresa pública sob LGPD setorial e Marco Civil específico |
| Empresa que vende SaaS com IA embarcada como funcionalidade central | Operação em jurisdição não-brasileira com regulação distinta (EU AI Act, NIST AI RMF, regulação setorial estadual nos EUA) |
| Empresa que adota IA de terceiros via API como ferramenta auxiliar | Operação com dado pessoal sensível em volume material sem DPO efetivo previamente nomeado |

O adendo setorial não substitui o caderno, ele se anexa como camada adicional sobre o instrumento base, e é o instrumento setorial que define o trecho específico, jamais o contrário, porque regulação setorial sobrescreve governança interna por princípio.

---

## Sete padrões de adaptação ao contexto da organização

A customização do caderno segue sete padrões transversais, independentemente do setor e do porte. Pular qualquer um deles produz documento publicado com aparência de governança e prática divergente, que é exatamente o teatro que o Framework Seis combate.

1. **Patrocinador executivo nomeado, não apenas o cargo.** O caderno exige nome próprio na linha de patrocinador, não apenas "CTO" ou "CEO". Sem nome, a responsabilidade vira institucional, e institucional é eufemismo para ninguém.

2. **Princípios condutores customizados ao vocabulário da organização**, sem renomear os Nove Princípios da obra, e sem suprimir nenhum deles. Customização que apaga o Princípio Oito viola o pacto editorial do caderno.

3. **Matriz RACI estendida com as classes de decisão específicas do negócio.** As sete classes de decisão recorrentes do modelo são piso, jamais teto. Empresa que opera com agente autônomo em produção precisa adicionar classe específica para promoção de tier de autonomia, com gates de observabilidade explícitos.

4. **Comitê de IA com mandato declarado por escrito**, em ata da primeira reunião, com lista do que decide unilateralmente, do que escala à diretoria e do que precisa de quórum qualificado. Comitê sem mandato é fórum de debate filosófico, e fórum não para incidente.

5. **AUP traduzida ao contexto operacional da empresa**, com exemplos práticos do que é permitido e do que é proibido nas ferramentas reais que a organização adota. AUP genérica não orienta, AUP com exemplo orienta.

6. **Maturidade autodeclarada com evidência anexada por controle.** O preenchimento da coluna de maturidade na primeira assinatura exige link para artefato de evidência, jamais autodeclaração nua. Maturidade três sem artefato é maturidade um disfarçada.

7. **Revisão trimestral em calendário fixo da diretoria**, não em janela negociada por agenda. Sem data fixa, revisão escorrega para o trimestre seguinte, e o caderno entra em coma silencioso.

---

## Anti-padrões transversais de governança de IA

| Anti-padrão | Por que falha |
|---|---|
| Caderno publicado em PDF assinado sem revisão programada | Governança morre no momento da assinatura; o documento vira álibi quando o incidente vier, não defesa |
| RACI implícito com expressão como "o time X cuida" | Sem nome, ninguém responde; viola o Princípio Oito por omissão estrutural |
| Comitê de IA sem mandato escrito e sem quórum mínimo | Reuniões viram fórum de opinião, decisões empacam, incidentes escalam à diretoria sem filtro técnico |
| AUP genérica sem exemplo concreto da ferramenta adotada | Colaborador não sabe se a ferramenta nova do dia está permitida ou proibida, e o resultado é shadow AI |
| Maturidade autodeclarada sem evidência anexada | Conselho recebe quadro verde otimista que não resiste ao primeiro incidente |
| Plano de incidente sem simulado semestral | Quando a crise vier pela primeira vez, todo mundo descobre que o playbook não foi treinado |
| Ausência de log de edições do caderno | Cada revisão vira mudança não rastreável, e impossível defender o instrumento em auditoria |
| Revisão trimestral pulada sem registro formal | Caderno entra em coma silencioso, e quando alguém perceber, a versão vigente já estará desalinhada da operação |
| Atualização do caderno apenas após incidente material | Governança vira reativa; o objetivo é manter o caderno à frente do incidente, não atrás |
| Adoção integral sem adendo setorial em setor regulado | Conflito entre instrumento interno e exigência do regulador, com perda de validade jurídica do caderno em caso de fiscalização |

---

## A métrica que separa caderno vivo de caderno morto

Saber se o caderno está vivo não é função de quem publicou, e sim de quem usa o caderno em cadência. Sete indicadores quantitativos sustentam a leitura da saúde do instrumento, e devem ser revisados no relatório anual do Comitê de IA à diretoria.

| Indicador | O que mede | Faixa saudável no horizonte de doze meses |
|---|---|---|
| Atas do Comitê de IA arquivadas | Cadência real do órgão executivo | 12 atas no ano, sem ausência maior que 45 dias |
| Atualizações do caderno registradas no log | Quantas vezes o instrumento foi revisado de fato | Entre 4 e 8 atualizações no ano, com pelo menos uma por incidente material |
| Maturidade média dos 10 controles | Evolução agregada da postura operacional | Crescimento mínimo de 0,5 ponto na escala de 0 a 4, por ano, até atingir 3,0 médio |
| RACIs específicos assinados por caso de uso em produção | Cobertura nominal de Accountable por sistema | 100% dos casos de uso de IA em produção com RACI específico assinado |
| Simulados de SEV-1 executados | Maturidade real do plano de incidente | 2 simulados no ano, com tempo de resposta abaixo da meta declarada |
| Postmortems sem culpa publicados internamente | Aprendizado real a partir de incidentes | 100% dos SEV-1 e SEV-2 com postmortem em até 10 dias úteis |
| Treinamentos de AUP em onboarding | Difusão da AUP na operação | 100% dos colaboradores novos treinados no primeiro mês de casa |

Organização que olha esses sete indicadores e descobre quatro deles em vermelho não tem governança, tem caderno publicado. O Comitê de IA deve usar essa leitura para acionar a diretoria, jamais para esconder a degradação.

---

## Versão executável

O caderno operacional completo, com placeholders nomeados, com as seis seções fatiadas para edição independente, com os modelos dos seis anexos referenciados e com o changelog datado a cada revisão, está no repositório acompanhante na pasta dedicada [`governance/v1`](https://github.com/falercia/inteligencia-aumentada-recursos/tree/main/governance/v1).

O caminho recomendado de adoção é clonar a pasta, customizar a identificação e os princípios na seção 01, montar o RACI específico do negócio na seção 02, traduzir a AUP ao vocabulário e às ferramentas da organização na seção 03, preencher a maturidade autodeclarada com evidência anexada na seção 04, calibrar o plano de incidente ao SLA real do negócio na seção 05, colher as assinaturas da diretoria na seção 06, e marcar a próxima revisão no calendário do Comitê de IA no mesmo ato. Caderno que não nasce com data de próxima revisão marcada já nasce morto.

---

## Compromisso final do caderno

A diretoria, ao assinar o caderno, compromete-se com a regra fundamental do Princípio Oito, em que toda decisão de IA tem nome humano responsável. A IA executa, a responsabilidade tem dono. Quando alguém disser "foi a IA que decidiu", a organização precisa saber, em até cinco minutos, de quem é a cadeira.

Este é o pacto que o caderno materializa, e é a métrica final pela qual ele será julgado, ainda que muito antes disso o conselho já tenha julgado os sete indicadores de caderno vivo.

---

*Apêndice O · Caderno de Governança de IA. Ficha conceitual no livro, caderno operacional executável em [governance/v1](https://github.com/falercia/inteligencia-aumentada-recursos/tree/main/governance/v1) no repositório acompanhante. Política editorial: instrumento vivo, sem cadência fixa anunciada.*

</div>
</section>



<section class="apendice-bloco">
<div class="abertura-apendice">

<div class="selo-apendice">Apêndice</div>

# Apêndice P — Boxes Técnicos

> Atualizado em: junho de 2026
> Cobertura: conceitos arquiteturais e operacionais ausentes do corpo principal por escolha de pedagogia, aqui apresentados em formato de box para consulta rápida do leitor técnico

---

## Como usar este apêndice

O corpo principal desta obra foi construído com uma decisão pedagógica deliberada, manter o foco em invariantes e em consequências executivas, sem deixar que a riqueza de detalhe arquitetural roubasse a clareza dos princípios que orientam a tomada de decisão. Esse recorte funciona para o leitor que está formando a primeira lente conceitual, mas deixa de fora um conjunto de mecanismos internos cuja compreensão deixou, em 2026, de ser opcional para quem decide stack, custo de inferência, escolha entre proprietário e open weights, ou postura de adoção em escala.

Este apêndice cobre exatamente esse vazio. Cada box é uma unidade autônoma de cerca de seiscentas a novecentas palavras, escrita para ser lida fora de ordem, sem dependência sequencial com os boxes vizinhos. A organização segue uma curva pedagógica natural, do mais arquitetural (Mixture of Experts, Speculative Decoding, KV Cache, FlashAttention) para o mais operacional (LoRA, quantização, structured output) e finalmente para o mais epistêmico (faithfulness de chain of thought, interpretabilidade mecanicista, scaling laws), mas nada impede que o leitor pule diretamente para o box que resolve sua dúvida do momento.

Cada box segue a mesma estrutura interna, sete blocos curtos que cobrem por que o box existe, o conceito intuitivo, uma analogia, o mecanismo técnico em profundidade real, a implicação executiva que muda quando o leitor internaliza o conceito, quando isso importa especificamente para o contexto brasileiro, e onde aprofundar no paper canônico. A leitura de cada box leva entre seis e dez minutos, e a leitura completa do apêndice cabe em uma tarde de domingo.

O pré-requisito de leitura recomendado é ter passado pelos Capítulos 1, 2 e 3, que estabelecem o vocabulário básico de tokens, treinamento, inferência, atenção e transformer. Sem essa base, alguns boxes (notadamente Box 3, Box 4 e Box 9) ficam mais difíceis do que precisam ser. Com essa base, todos eles ficam acessíveis ao leitor executivo com paciência técnica.

---

## Mapa de boxes

| Box | Tema | Capítulo onde aparece referência | Princípio relacionado |
|---|---|---|---|
| 1 | Mixture of Experts (MoE) | C02, C15 | P5 — Custo Composto |
| 2 | Speculative Decoding | C02, C18 | P5 — Custo Composto |
| 3 | KV Cache | C04, C18 | P5 — Custo Composto |
| 4 | FlashAttention | C04 | P2 — Extremidades |
| 5 | LoRA e PEFT | C08 | P4 — Encaixe |
| 6 | Quantização e Destilação | C16, C18 | P5 — Custo Composto |
| 7 | Structured Output e JSON Mode | C12 | P1 — Plausibilidade |
| 8 | Faithfulness de Chain of Thought | C10, C23 | P1 — Plausibilidade |
| 9 | Interpretabilidade Mecanicista | C28 | P7 — Termômetro |
| 10 | Scaling Laws | C02, C15 | P5 — Custo Composto |
| 11 | Matriz de Interações entre os Conceitos | Transversal, referencia todos os anteriores | Transversal aos nove Princípios |

---

## Box 1 — Mixture of Experts (MoE)

**Por que este box existe.** A maioria dos modelos frontier lançados de 2024 em diante usa arquitetura Mixture of Experts em vez do transformer denso clássico, e essa decisão arquitetural muda radicalmente a relação entre parâmetros totais, parâmetros ativos e custo de inferência. Quem decide stack sem entender MoE acaba comparando modelos como se fossem da mesma natureza, e a conta sai errada.

**Conceito intuitivo.** Em um transformer denso, todo token que entra no modelo atravessa todos os parâmetros das camadas feed-forward, o que significa que um modelo de 400 bilhões de parâmetros gasta os 400 bilhões para gerar cada token. Em um MoE, cada camada feed-forward é fatiada em dezenas de subredes especialistas, e um roteador aprendido decide, para cada token, qual pequeno subconjunto desses especialistas será ativado. O resultado é que um modelo pode ter centenas de bilhões de parâmetros no total, mas usar apenas dezenas de bilhões para gerar cada token, o que reduz drasticamente o custo de inferência sem proporcionalmente reduzir a capacidade aprendida.

**Analogia.** Pense numa consultoria com duzentos especialistas no quadro, cada um profundamente competente em um nicho diferente, do financeiro de varejo ao tributário internacional. Quando chega um problema, em vez de reunir todos os duzentos na sala, o sócio gestor escala dois ou três especialistas cuja expertise mais se aproxima do problema, e o restante segue trabalhando em paralelo em outros casos. O capital intelectual da consultoria como um todo continua disponível, mas a capacidade ociosa em cada caso específico cai drasticamente, e o custo por hora cobrada do cliente fica proporcional ao especialista efetivamente ativado, não ao tamanho do quadro.

**Mecanismo técnico.** Em uma camada MoE, a operação feed-forward padrão (uma rede densa de duas camadas com não-linearidade no meio) é substituída por N especialistas paralelos, cada um com a mesma forma da rede densa original, e por um gate, que é uma pequena rede linear que recebe o vetor de embedding do token e produz, para cada especialista, um score de afinidade. O gate aplica um softmax aos K maiores scores (top-K, tipicamente K igual a dois) e zera os demais, o que faz com que apenas K especialistas processem aquele token, e o output da camada é a soma ponderada dos outputs dos K especialistas ativados, com pesos vindos do softmax. Para manter o treinamento estável, adiciona-se uma perda auxiliar que penaliza desbalanceamento entre especialistas, evitando que todos os tokens sejam roteados para os mesmos poucos especialistas e os demais virem zumbis.

A consequência arquitetural é poderosa, porque a capacidade total do modelo (medida em parâmetros) escala com o número de especialistas, enquanto o custo de inferência por token escala apenas com K (número de especialistas ativos) vezes o tamanho de cada especialista. Mixtral 8x7B, da Mistral, popularizou a fórmula em 2023, com oito especialistas de sete bilhões de parâmetros cada e top-2 routing, totalizando aproximadamente quarenta e sete bilhões de parâmetros e ativando perto de treze bilhões por token. DeepSeek V3, lançado no fim de 2024, levou o conceito ao limite com 671 bilhões de parâmetros totais e cerca de 37 bilhões ativos por token, atingindo qualidade de fronteira a custo de inferência dramaticamente menor que GPT-4 denso.

O ponto delicado é que MoE não é grátis. A literatura documentou pelo menos dois riscos sérios. O primeiro é o que se chama tiebreak leakage (Hayes et al., outubro de 2024), em que o roteamento, sob certas condições de batching, expõe informação entre prompts vizinhos, com implicações de segurança em ambientes multi-tenant. O segundo é expert silencing, ataque em que tokens adversariais conseguem desligar especialistas específicos da inferência, degradando qualidade de forma direcionada. Para o tomador de decisão, isso significa que MoE em produção exige cuidado adicional de isolamento e monitoramento.

**Implicação executiva.** Quando você lê que um modelo tem 671 bilhões de parâmetros e outro tem 200 bilhões, e ambos custam aproximadamente o mesmo por milhão de tokens, a explicação não é mágica, é arquitetura. Capacidade efetiva é função de parâmetros ativos e da inteligência do roteamento, não do número estampado no marketing. Em decisão de stack, peça sempre dois números separados, parâmetros totais e parâmetros ativos por token, e compare custo de inferência só entre arquiteturas comparáveis.

**Quando importa para o leitor brasileiro.** Empresas brasileiras que estão escolhendo entre rodar open weights em infraestrutura própria (típico em fintechs reguladas e em jurídico com sigilo forte) precisam entender MoE para dimensionar GPU corretamente. Um Mixtral 8x7B cabe em duas GPUs de oitenta gigas; um modelo denso de capacidade comparável exigiria quatro ou cinco. Isso muda a viabilidade econômica de deploy on-prem em ordens de magnitude, e o engenheiro de infra precisa do quadro completo para decidir.

**Onde aprofundar.** Fedus, Zoph, Shazeer. *"Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity"*. JMLR, 2022. → arxiv.org/abs/2101.03961. Mixtral paper: Jiang et al. *"Mixtral of Experts"*. 2024. → arxiv.org/abs/2401.04088. Para os riscos de tiebreak leakage: Hayes et al., 2024 → arxiv.org/abs/2410.10074.

---

## Box 2 — Speculative Decoding

**Por que este box existe.** Latência de inferência virou, em 2026, gargalo competitivo tão relevante quanto qualidade de resposta, e speculative decoding é a técnica que mais silenciosamente reduziu essa latência sem trocar o modelo principal nem comprometer qualidade. Quem decide arquitetura de serving sem entender essa técnica deixa dinheiro e responsividade na mesa.

**Conceito intuitivo.** A geração padrão de um LLM é autoregressiva e sequencial, o modelo gera um token, anexa ao contexto, gera o próximo, anexa, e assim sucessivamente. Cada passo exige uma passagem completa pelo modelo, e como modelos frontier têm centenas de bilhões de parâmetros, cada passagem é cara. Speculative decoding quebra essa sequencialidade ao introduzir um segundo modelo, muito menor e muito mais rápido, chamado modelo draft, que gera uma sequência tentativa de vários tokens à frente. O modelo principal então verifica essa sequência em uma única passagem em paralelo, aceitando o prefixo correto e descartando o resto, o que produz vários tokens válidos por passagem do modelo grande.

**Analogia.** Imagine um sócio sênior revisando um documento longo escrito por um estagiário competente. O sócio não escreve cada palavra, lê em blocos rapidamente, aprovando trechos inteiros quando o estagiário acertou e marcando o ponto exato em que o raciocínio descarrilhou, a partir do qual o sócio assume a redação. Se o estagiário acerta com frequência razoável, a velocidade efetiva da dupla é várias vezes maior do que a do sócio escrevendo sozinho do zero, e a qualidade final é exatamente a do sócio, porque tudo que entrou no documento passou por seu crivo. O estagiário acelera, mas não diminui o padrão.

**Mecanismo técnico.** Formalmente, dado um prompt e uma posição atual, o modelo draft gera K tokens de forma autoregressiva, produzindo uma sequência candidata. O modelo principal recebe o prompt mais essa sequência candidata e, em uma única passagem (que custa aproximadamente o mesmo que gerar um token, porque atenção é paralelizável sobre a sequência inteira), calcula a distribuição de probabilidade verdadeira para cada uma das K+1 posições. O algoritmo então decide token a token, da esquerda para a direita, se aceita ou rejeita a proposta do draft, usando uma regra de amostragem provável (originalmente proposta por Leviathan, Kalman, Matias, 2023) que preserva exatamente a distribuição que o modelo principal teria gerado sozinho. Quando aparece a primeira rejeição, o token é substituído por uma amostra da distribuição verdadeira corrigida, e os tokens posteriores ao ponto de rejeição são descartados. O ciclo recomeça a partir daí.

A propriedade matemática que sustenta a técnica é que, sob a regra de amostragem correta (chamada de speculative sampling com correção de distribuição), a sequência final de tokens segue exatamente a distribuição que o modelo principal teria produzido se tivesse gerado sozinho, sem speculative. Não há perda de qualidade no sentido estatístico, apenas ganho de latência. O ganho típico observado em produção é de duas a três vezes em modelos densos grandes, com modelos draft cerca de dez a cinquenta vezes menores que o principal.

Variantes recentes refinaram a ideia. Medusa, de 2024, substitui o modelo draft por cabeças adicionais no próprio modelo principal, que produzem candidatos para várias posições futuras em paralelo, eliminando o custo de manter um segundo modelo separado. EAGLE explora árvores de candidatos em vez de sequência linear, aumentando taxa de aceitação. Todas essas variantes preservam a propriedade central, qualidade idêntica à geração padrão, latência menor.

**Implicação executiva.** A latência percebida pelo usuário em produção pode ser reduzida em duas a três vezes sem trocar o modelo principal, sem perder qualidade, sem mudar o produto, apenas adotando speculative decoding no serving. Em decisão de plataforma, perguntar ao fornecedor se ele faz speculative decoding (e qual variante) é tão relevante quanto perguntar qual é o modelo. Custos de infraestrutura caem proporcionalmente, porque servir o mesmo volume requer menos tempo de GPU.

**Quando importa para o leitor brasileiro.** Aplicações brasileiras de atendimento em tempo real (call centers de saúde, chatbots bancários, assistentes em e-commerce de alta concorrência) são particularmente sensíveis a latência, porque a tolerância do consumidor brasileiro a espera é baixa e o custo de NPS de uma resposta lenta é alto. Para essas aplicações, exigir speculative decoding na camada de serving é o caminho mais barato para reduzir tempo de primeira resposta, e a maioria dos provedores frontier já entrega isso por padrão se a integração for feita pelos endpoints corretos.

**Onde aprofundar.** Leviathan, Kalman, Matias. *"Fast Inference from Transformers via Speculative Decoding"*. ICML, 2023. → arxiv.org/abs/2211.17192. Chen et al. *"Accelerating Large Language Model Decoding with Speculative Sampling"*. DeepMind, 2023. → arxiv.org/abs/2302.01318. Medusa: Cai et al., 2024 → arxiv.org/abs/2401.10774.

---

## Box 3 — KV Cache

**Por que este box existe.** Prompt caching, pricing diferenciado por cache hit, latência de primeira resposta versus tokens subsequentes, throughput de GPU em produção, tudo isso só faz sentido quando o leitor entende o que é o KV cache e como ele se comporta. É a estrutura de dados invisível que governa boa parte da economia de inferência moderna.

**Conceito intuitivo.** Quando um modelo gera tokens autoregressivamente, cada novo token precisa atender a todos os tokens anteriores da sequência. Sem otimização, isso significaria recomputar, a cada passo, as projeções de atenção (Key e Value) para a sequência inteira, o que seria assintoticamente quadrático no comprimento e proibitivo na prática. O KV cache resolve isso guardando, na memória da GPU, os tensores K e V já computados para cada token de cada camada, de modo que a cada novo passo apenas o token novo precise ser projetado e anexado ao cache. A consequência é que inferência autoregressiva fica linear no comprimento da sequência, em vez de quadrática, e o uso de memória GPU passa a depender principalmente do tamanho do cache.

**Analogia.** Imagine um auditor que está revisando um livro-razão. Em vez de, a cada nova linha lida, voltar ao começo e reler tudo desde a primeira página para entender o contexto, o auditor mantém anotações cumulativas em uma planilha lateral, com saldos parciais e categorizações já resolvidas. Cada nova linha do livro-razão é processada à luz da planilha, e ao fim, a planilha é atualizada com o resultado da linha nova. O custo por linha lida fica constante, em vez de crescer à medida que o livro avança. KV cache faz exatamente isso para a atenção transformer.

**Mecanismo técnico.** Para cada camada do transformer, cada token na sequência tem um vetor de Key e um vetor de Value, produzidos pela projeção linear sobre o embedding do token naquela camada. Em uma sequência de comprimento L, com dimensão de embedding d, número de cabeças h e número de camadas n, a memória do KV cache cresce proporcionalmente a 2 vezes L vezes h vezes (d dividido por h) vezes n, ou seja, escala linearmente com o comprimento da sequência e com a profundidade do modelo. Em modelos frontier típicos, com cento e vinte camadas e contexto de duzentos mil tokens, o KV cache de uma única conversa pode ocupar dezenas ou centenas de gigabytes de memória GPU, o que se soma à memória dos pesos do modelo em si.

Esse fato tem três consequências práticas que merecem ser internalizadas. Primeiro, prompt caching, que virou produto vendido por provedores frontier a partir de 2024, é literalmente o reuso do KV cache de um prefixo comum entre requisições, evitando a re-projeção dos tokens já vistos. Isso só faz sentido se o cache for estável (mesmas posições, mesmos tokens), o que limita prompt caching a prefixos exatos, não a paráfrases. Segundo, batch de inferência em produção é restrito pela memória total disponível, e como cada usuário em paralelo carrega seu próprio cache, o número de usuários simultâneos por GPU é função inversa do comprimento médio de contexto deles. Terceiro, contextos muito longos em produção exigem trade-offs explícitos entre memória, throughput e latência, e técnicas como paged attention (vLLM) e KV cache compression (quantização do cache) surgiram exatamente para mitigar essa pressão.

Variantes recentes mudam a estrutura do cache para reduzir consumo. Multi-Query Attention (MQA) e Grouped-Query Attention (GQA), adotadas em Llama 2 e em modelos posteriores, fazem várias cabeças de atenção compartilharem as mesmas matrizes K e V, reduzindo o tamanho do cache em fatores de quatro a oito sem perda significativa de qualidade. Multi-head Latent Attention (MLA), introduzida em DeepSeek V2, comprime ainda mais usando projeções latentes de dimensão baixa. Cada uma dessas variantes é uma decisão arquitetural que afeta diretamente o custo de servir o modelo em produção.

**Implicação executiva.** Prompt caching só funciona sob cache estável de prefixo exato, e o preço diferenciado por cache hit, oferecido pelos provedores frontier, é uma das otimizações de custo mais subexploradas em produção. Em um agente que repete a mesma instrução de sistema em milhares de chamadas, ativar prompt caching pode reduzir o custo total em sessenta a noventa por cento. Em decisão de stack on-prem, perguntar pelo tamanho do KV cache esperado por usuário simultâneo é tão relevante quanto perguntar pelo tamanho dos pesos do modelo, porque define o número máximo de usuários por GPU.

**Quando importa para o leitor brasileiro.** Empresas brasileiras que estão construindo agentes em workflow com instrução de sistema longa (típico em jurídico com regras de compliance, em saúde com protocolos clínicos, em fintech com regras regulatórias) ganham muito ao migrar para provedores que oferecem prompt caching nativo, e ao desenhar a arquitetura do prompt para maximizar prefixo estável. A diferença de custo entre desenhar o prompt com prefixo bom para cache versus com prefixo variável pode chegar a uma ordem de magnitude na fatura mensal.

**Onde aprofundar.** Pope et al. *"Efficiently Scaling Transformer Inference"*. 2022. → arxiv.org/abs/2211.05102. PagedAttention (vLLM): Kwon et al. *"Efficient Memory Management for Large Language Model Serving with PagedAttention"*. SOSP, 2023. → arxiv.org/abs/2309.06180. Multi-Query Attention: Shazeer, 2019 → arxiv.org/abs/1911.02150.

---

## Box 4 — FlashAttention

**Por que este box existe.** Janelas de contexto de um milhão de tokens não apareceram porque a teoria mudou, apareceram porque a implementação do mecanismo de atenção mudou. FlashAttention é o algoritmo que tornou economicamente viável o que parecia computacionalmente proibitivo, e entender o porquê é entender por que o gargalo da inferência não é mais o que o leitor pensa que é.

**Conceito intuitivo.** A atenção, na sua forma matemática clássica, é uma operação de complexidade O(n²) em comprimento de sequência, porque cada token precisa interagir com cada outro token para calcular pesos. Por décadas, a literatura assumiu que esse era o gargalo, e a pesquisa concentrou esforço em aproximações esparsas que evitassem o n² teórico. FlashAttention abordou o problema de outro ângulo, observando que o gargalo prático em GPUs modernas não era o número de operações matemáticas, era a movimentação de dados entre a memória rápida da GPU (SRAM, perto dos núcleos de computação) e a memória lenta (HBM, mais distante mas maior). Ao reorganizar o cálculo da atenção para minimizar movimentação entre HBM e SRAM, FlashAttention conseguiu acelerar a atenção exata (sem aproximação) em fatores de duas a quatro vezes, e reduzir consumo de memória de O(n²) para O(n), o que destravou contextos longos sem precisar reescrever a matemática.

**Analogia.** Imagine um cozinheiro preparando um prato complexo em uma cozinha grande, com a bancada de trabalho (pequena, perto do fogão) separada da despensa (grande, no fundo). A receita exige cinquenta ingredientes, e o cozinheiro normal pega um ingrediente da despensa, usa, deixa a sobra na bancada, volta à despensa, pega o próximo, e assim por diante, gastando mais tempo caminhando do que cozinhando. FlashAttention é o cozinheiro experiente, que planeja a receita de modo a buscar lotes inteiros de ingredientes da despensa de uma só vez, processá-los completamente na bancada antes de buscar o próximo lote, e descartar resultados intermediários que não precisam ser guardados. A receita é a mesma, o prato sai idêntico, o tempo de preparo cai por um fator constante grande.

**Mecanismo técnico.** O algoritmo original da atenção materializa, em HBM, a matriz n por n de scores de atenção (produto Query por Key transposto), aplica softmax sobre ela, e a multiplica pela matriz de Values. Essa matriz n por n é o vilão, porque para n igual a um milhão de tokens, ela teria um trilhão de entradas, o que estoura qualquer GPU. FlashAttention reorganiza o cálculo em blocos, carregando da HBM para a SRAM apenas pedaços de Q, K e V de cada vez, computando a contribuição daquele bloco para o output final, e usando um truque numérico (online softmax) que permite acumular o softmax de forma estável sem nunca materializar a matriz completa. O resultado final é matematicamente idêntico à atenção exata, o número total de operações de ponto flutuante é o mesmo, mas o número de operações de leitura e escrita em HBM cai por um fator igual ao tamanho do bloco, que é tipicamente de 64 a 128.

A consequência prática é que, em hardware moderno (A100, H100, B100), o tempo de execução da atenção cai por um fator de duas a quatro vezes, e o consumo de memória cai de O(n²) para O(n), o que significa que contextos antes impraticáveis tornam-se rotineiros. FlashAttention 2, lançado em 2023, refinou ainda mais o algoritmo usando paralelismo melhor entre warps da GPU, e FlashAttention 3, em 2024, aproveitou recursos específicos do H100 (assíncrono e baixa precisão) para acelerar mais.

**Implicação executiva.** Contextos de duzentos mil a um milhão de tokens, que aparecem como spec sheet em Gemini 1.5, Claude 4 Sonnet, GPT-4 Turbo, não foram resultado de uma descoberta teórica, foram resultado de FlashAttention rodando em hardware mais recente. Isso tem duas consequências. Primeiro, a janela de contexto vai continuar crescendo, porque o teto não é matemático, é de engenharia. Segundo, o leitor não deve mais assumir que contexto longo é caro por design, e pode redesenhar arquiteturas (RAG, agents, document processing) assumindo contextos generosos com custo controlado, com o cuidado de Lost in the Middle do Capítulo 4 sendo o limitador real, não a janela em si.

**Quando importa para o leitor brasileiro.** Aplicações brasileiras intensivas em documento (jurídico processando peças longas, due diligence de M&A analisando contratos extensos, saúde lendo prontuários cumulativos) só são economicamente viáveis em escala graças a FlashAttention. Há um ano e meio, fazer um agente que lesse cinquenta páginas de um contrato em uma única chamada era luxo, hoje é commodity, e a explicação está nas duas mil linhas de código CUDA que reorganizam a leitura de memória.

**Onde aprofundar.** Dao et al. *"FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness"*. NeurIPS, 2022. → arxiv.org/abs/2205.14135. FlashAttention-2: Dao, 2023 → arxiv.org/abs/2307.08691. FlashAttention-3: Shah et al., 2024 → arxiv.org/abs/2407.08608.

---

## Box 5 — LoRA e PEFT

**Por que este box existe.** Fine-tuning saiu, em poucos anos, do território de "só pra quem tem cem GPUs e três meses" para o território de "qualquer time de produto consegue se quiser", e o que mudou foi a invenção de técnicas de adaptação eficiente em parâmetros, conhecidas pelo guarda-chuva PEFT. Sem entender o que mudou, o leitor segue assumindo que fine-tuning é caro e arriscado, quando deixou de ser ambos.

**Conceito intuitivo.** Fine-tuning clássico significa pegar todos os bilhões de pesos do modelo base e ajustá-los a um novo conjunto de dados, o que exige memória para guardar os pesos, gradientes e estados do otimizador, e exige horas ou dias de GPU. PEFT, abreviação de Parameter-Efficient Fine-Tuning, é a família de técnicas que congela os pesos do modelo base e treina apenas um número pequeno de parâmetros adicionais, que ficam ao lado ou dentro das camadas originais e desviam levemente o comportamento do modelo na direção desejada. LoRA, a mais popular dessas técnicas, treina apenas matrizes de baixo posto que se somam às matrizes originais, o que reduz o número de parâmetros treináveis em três ordens de magnitude e mantém oitenta a noventa e cinco por cento da qualidade de um fine-tune completo, dependendo da tarefa.

**Analogia.** Pense em um piano de concerto, perfeitamente afinado e regulado, que é a base. Um pianista clássico que precise tocar bossa nova não vai reconstruir o piano inteiro, vai instalar pedais auxiliares, surdina ou abafadores, que modificam o som de forma sutil e direcionada para o gênero novo, sem mexer no mecanismo principal. Quando precisar voltar ao clássico, basta remover os auxiliares, e o piano original volta intacto. PEFT é exatamente essa lógica, o modelo base segue o mesmo, e adaptações leves são plugadas e despluáveis conforme o caso de uso.

**Mecanismo técnico.** LoRA, formalizado por Hu et al. em 2021, parte da observação empírica de que as matrizes de mudança induzidas por fine-tuning, ou seja, a diferença entre o peso pós-treino e o peso pré-treino, tende a ter posto efetivo baixo. Em vez de aprender uma matriz delta W com mesma dimensão da matriz original W (digamos d por d), LoRA aprende duas matrizes pequenas, A de dimensão d por r e B de dimensão r por d, onde r é o posto escolhido, tipicamente entre 4 e 64. A delta efetiva é o produto B vezes A, que tem mesma dimensão de W, mas é determinada por apenas 2dr parâmetros em vez de d². Para r igual a 16 e d igual a 4096, isso significa cento e trinta mil parâmetros em vez de dezesseis milhões, redução de duas ordens de magnitude por camada. Durante o treinamento, apenas A e B são atualizados. Durante a inferência, o produto BA pode ser somado a W e descartado, sem custo adicional.

A consequência operacional é que um fine-tune de um modelo de sete bilhões de parâmetros, que antes exigiria GPUs com duzentos gigabytes de memória e várias horas, hoje cabe em uma única GPU de vinte e quatro gigabytes em algumas horas, e o checkpoint salvo ocupa megabytes em vez de dezenas de gigabytes. Deploy de variantes fica trivial, porque o modelo base fica armazenado uma vez e cada variante é um adaptador LoRA leve que pode ser carregado e descarregado sob demanda, inclusive em um mesmo serving multi-tenant que serve dezenas de adaptadores diferentes a partir do mesmo modelo base, técnica conhecida como S-LoRA.

O ecossistema PEFT inclui variantes além de LoRA. Prefix tuning treina vetores prependidos ao contexto, prompt tuning treina embeddings de prompts virtuais, IA3 escala ativações com vetores aprendidos, QLoRA combina LoRA com quantização do modelo base para reduzir ainda mais memória. Cada uma tem trade-offs distintos entre número de parâmetros treináveis, qualidade final e facilidade de deploy.

**Implicação executiva.** Fine-tune não é mais infraestrutura pesada, é decisão de produto. Times de produto podem manter dezenas de variantes adaptadas para verticais diferentes (um para atendimento ao cliente B2C, outro para B2B, outro para pós-venda técnico), todas servidas a partir do mesmo modelo base, com custo de armazenamento e troca trivial. Em decisão de roadmap, considerar fine-tune como caminho viável para casos onde engenharia de prompt atingiu teto é hoje a regra, não a exceção, e o cálculo de ROI é muito mais favorável que era em 2023.

**Quando importa para o leitor brasileiro.** Empresas brasileiras com domínio linguístico ou normativo muito específico (cooperativas de crédito com terminologia própria, escritórios de advocacia com estilo argumentativo proprietário, redes hospitalares com protocolos internos) ganham muito ao manter variantes LoRA treinadas em seus próprios corpora, em vez de tentar codificar tudo isso em prompts gigantes. O custo de manter dez variantes LoRA é uma fração do custo de manter um único fine-tune completo, e a qualidade final é comparável para a maioria das tarefas.

**Onde aprofundar.** Hu et al. *"LoRA: Low-Rank Adaptation of Large Language Models"*. ICLR, 2022. → arxiv.org/abs/2106.09685. QLoRA: Dettmers et al., 2023 → arxiv.org/abs/2305.14314. Survey de PEFT: Lialin et al., 2023 → arxiv.org/abs/2303.15647.

---

## Box 6 — Quantização e Destilação

**Por que este box existe.** Open weights só são viáveis economicamente em hardware modesto graças a quantização e destilação, e a diferença entre o leitor que entende esses conceitos e o que não entende é a diferença entre conseguir rodar Llama 70B em uma única GPU de consumidor ou achar que precisa de uma fazenda de servidores. Para a decisão entre proprietário e open weights, este box é pré-requisito.

**Conceito intuitivo.** Quantização é reduzir a precisão numérica com que os pesos do modelo são armazenados, do padrão FP32 (trinta e dois bits por peso) ou FP16 (dezesseis bits) para INT8 (oito bits), INT4 (quatro bits) ou até menos, com perda mínima de qualidade quando bem feita. Destilação é treinar um modelo menor (chamado aluno) para imitar o comportamento de um modelo maior (chamado professor), aproveitando os sinais ricos das distribuições de probabilidade do professor em vez de apenas dos rótulos finais, e produzindo um aluno significativamente mais barato que carrega boa parte da capacidade do professor. As duas técnicas são complementares, e juntas constituem o caminho pelo qual modelos de capacidade frontier alcançam hardware acessível.

**Analogia.** Pense em um manuscrito de mil páginas escrito em caligrafia preciosa, com cada letra adornada por floreios complexos. Quantização é redigitar o mesmo conteúdo em uma fonte sans-serif limpa, ocupando metade do papel, perdendo a estética mas mantendo a mensagem intacta para todos os fins práticos. Destilação é diferente, é contratar um redator hábil que leu o manuscrito inteiro e escreve uma versão condensada que preserva os argumentos centrais e a estrutura, mas em duzentas páginas, com voz reconhecivelmente parecida com a do original. Ambos os processos comprimem informação, mas a quantização preserva fielmente o conteúdo, e a destilação preserva fielmente o comportamento.

**Mecanismo técnico.** Em quantização, cada peso, originalmente um número em ponto flutuante de trinta e dois bits, é mapeado para um número inteiro de oito ou quatro bits, junto com fatores de escala que permitem reconstruir o valor aproximado durante a inferência. As operações de matmul, que dominam o custo computacional, podem ser executadas em hardware inteiro especializado (tensor cores em INT8, por exemplo), o que reduz tanto a memória ocupada pelo modelo quanto o tempo de inferência. A perda de qualidade depende fortemente do esquema de quantização, e as técnicas modernas (GPTQ, AWQ, SmoothQuant) usam calibração com dados representativos para ajustar fatores de escala por canal, minimizando degradação. Para quantização agressiva em quatro bits ou menos, a perda em benchmarks típicos é tipicamente menor que dois pontos percentuais para modelos de sete bilhões em diante, e é ainda menor para modelos maiores, o que torna INT4 a opção padrão para deploy de open weights em hardware modesto.

Destilação clássica, proposta por Hinton, Vinyals, Dean em 2015, treina o aluno minimizando a divergência entre suas distribuições de saída e as do professor (KL divergence sobre logits suavizados por temperatura), em vez de minimizar apenas o erro contra rótulos verdadeiros. O aluno aprende mais que os rótulos, aprende a estrutura de incerteza relativa entre classes que o professor codificou, e essa informação rica permite que ele atinja qualidade desproporcional ao seu tamanho. Em LLMs modernos, destilação pode ser feita em vários níveis, sobre logits, sobre representações intermediárias, sobre comportamento em sequências geradas. Modelos como Phi-3, da Microsoft, e Gemini Nano são exemplos públicos de modelos pequenos treinados com destilação intensiva a partir de modelos maiores, atingindo qualidade impressionante para seu tamanho.

A combinação de quantização e destilação produz a curva de Pareto que define open weights em 2026. Um modelo destilado de quatorze bilhões para três bilhões de parâmetros, quantizado para INT4, cabe em sete gigabytes e roda em GPU de consumidor com latência aceitável, com qualidade adequada para aplicações específicas (assistência interna, classificação, sumarização de domínio limitado).

**Implicação executiva.** Open weights deixaram de ser, em 2026, uma alternativa marginal restrita a entusiastas, e tornaram-se opção viável para deploy em hardware modesto sempre que o caso de uso admite qualidade aquém da fronteira proprietária. A decisão proprietário versus open weights depende, em primeira ordem, do delta de qualidade aceitável e do volume de inferência. Para volumes altos com qualidade não-fronteira, open weights quantizado é dramaticamente mais barato. Para volumes baixos com necessidade de qualidade máxima, proprietário ainda vence.

**Quando importa para o leitor brasileiro.** Empresas brasileiras com restrições de dados sensíveis (saúde, financeiro, jurídico com NDA forte) ou com infraestrutura de TI em datacenters próprios herdada de décadas anteriores ganham bastante ao deployar modelos quantizados em hardware on-prem, em vez de enviar dados para APIs externas. A combinação de Llama ou Mistral quantizado para INT4 rodando em servidores DGX existentes, com adaptadores LoRA por área, é hoje arquitetura realista para muitos casos brasileiros que cinco anos atrás teriam exigido contratos de cloud cifrados complexos.

**Onde aprofundar.** Hinton, Vinyals, Dean. *"Distilling the Knowledge in a Neural Network"*. NeurIPS Workshop, 2015. → arxiv.org/abs/1503.02531. GPTQ: Frantar et al., 2022 → arxiv.org/abs/2210.17323. AWQ: Lin et al., 2023 → arxiv.org/abs/2306.00978. Survey de quantização para LLMs: Zhu et al., 2023 → arxiv.org/abs/2308.07633.

---

## Box 7 — Structured Output e JSON Mode

**Por que este box existe.** Agentes não funcionam, function calling não funciona, integrações automatizadas não funcionam, sem garantia de saída parseável. Prompt engineering "por favor responda em JSON" é frágil em produção, e a literatura técnica resolveu esse problema há tempos com grammar-constrained decoding e schema enforcement. Sem entender esses mecanismos, o leitor segue lutando com parsing quebrado em vez de aproveitar garantias formais já disponíveis.

**Conceito intuitivo.** A geração padrão de um LLM amostra cada token de uma distribuição de probabilidade sobre todo o vocabulário, sem nenhuma restrição estrutural, o que significa que mesmo um modelo bem treinado pode, ocasionalmente, produzir uma saída JSON com vírgula faltando, chave duplicada, aspas desbalanceadas, ou simplesmente texto extra antes ou depois do JSON. Structured output, no sentido moderno, é qualquer técnica que restringe a amostragem de tokens para garantir que a saída final obedeça a uma gramática formal, tipicamente um JSON Schema. A garantia é dura, não probabilística, e isso muda a natureza do contrato entre o modelo e o sistema que consome sua saída.

**Analogia.** Pense em um formulário fiscal que precisa ser preenchido. Sem restrições, um contribuinte poderia escrever qualquer coisa em qualquer campo, e o fisco passaria horas tentando interpretar entradas livres. Com um formulário PDF preenchível, com campos tipados e validações de cliente, o contribuinte só consegue enviar entradas que respeitam o formato. O conteúdo da decisão (o que ele decide preencher) ainda é livre, mas a forma é garantida. Structured output é exatamente isso para a saída do modelo, conteúdo livre, forma garantida.

**Mecanismo técnico.** A técnica central é grammar-constrained decoding, que funciona da seguinte maneira. Dada uma gramática formal (em JSON Schema ou em uma gramática context-free como BNF), um compilador converte a gramática em um autômato finito que rastreia, a cada posição da saída, qual é o conjunto de tokens válidos que o modelo pode emitir sem violar a gramática. Durante a inferência, antes de amostrar cada token, o sistema calcula a distribuição padrão sobre o vocabulário, mas em vez de amostrar livremente dessa distribuição, ele zera as probabilidades de todos os tokens que não estão no conjunto válido naquela posição, renormaliza, e amostra apenas dos tokens permitidos. A consequência é que a saída final é, por construção, sintaticamente válida segundo a gramática.

Function calling, oferecido por OpenAI, Anthropic, Google e demais provedores, é uma aplicação dessa ideia em que o esquema das funções disponíveis é convertido em uma gramática que o modelo pode emitir, garantindo que toda chamada de função tenha argumentos do tipo correto. JSON mode strict, com schema enforcement (lançado pela OpenAI em 2024 e seguido por outros), aplica a mesma lógica para garantir aderência a um JSON Schema fornecido pelo desenvolvedor. Ferramentas open source como Outlines, Guidance, LMQL e XGrammar oferecem grammar-constrained decoding sobre qualquer modelo open weights, o que permite estender a garantia para qualquer stack.

Há custos a considerar. Primeiro, restringir a amostragem pode degradar levemente a qualidade do conteúdo, porque o modelo pode ser empurrado para caminhos menos prováveis que aqueles que naturalmente sairiam. Modelos modernos foram treinados com formatos comuns (JSON, XML, Markdown) e essa degradação é pequena, mas existe. Segundo, gramáticas muito complexas aumentam a latência da inferência, porque o autômato precisa ser avaliado a cada token. Terceiro, structured output dá garantia sintática, não semântica, ou seja, garante que o JSON é válido e segue o schema, não que os valores dentro dele estão corretos. Validação semântica continua sendo responsabilidade da camada de aplicação.

**Implicação executiva.** Qualquer agente em produção em 2026 deve usar structured output, não engenharia de prompt com expectativa de obediência. A diferença entre os dois, na prática operacional, é a diferença entre uma integração que funciona em produção e uma que requer try-catch em torno de cada chamada e cresce em complexidade defensiva à medida que o sistema escala. Em decisão de stack, exigir suporte a JSON mode strict ou a grammar-constrained decoding é tão básico quanto exigir suporte a streaming de resposta.

**Quando importa para o leitor brasileiro.** Integrações brasileiras com sistemas legados (SAP, Oracle, sistemas tributários, sistemas regulatórios da ANS, do BACEN, da Susep) precisam de garantia de forma, porque os parsers do outro lado são tipicamente rígidos, e qualquer desvio de schema gera erro de processamento em batch. Adotar structured output como padrão, em vez de tentar bombear robustez via prompt, reduz dramaticamente a fragilidade dessas integrações e diminui o tempo de incidentes em produção.

**Onde aprofundar.** Outlines: Willard, Louf. *"Efficient Guided Generation for Large Language Models"*. 2023. → arxiv.org/abs/2307.09702. XGrammar: Dong et al., 2024 → arxiv.org/abs/2411.15100. Documentação de JSON Mode strict da OpenAI e de structured output da Anthropic em 2024-2025.

---

## Box 8 — Faithfulness de Chain of Thought

**Por que este box existe.** Chain of Thought (CoT) é uma das técnicas mais populares de prompting e está embutido em produtos de raciocínio explícito como o3 e Claude com extended thinking. A intuição forte de quem usa essas saídas é que o raciocínio exposto reflete o cálculo interno do modelo, ou seja, que ler a cadeia é ler o pensamento. A literatura técnica recente é firme em mostrar que isso não é estritamente verdade, e a distância entre narrativa e cálculo tem implicações sérias para auditoria, segurança e confiabilidade.

**Conceito intuitivo.** Quando um modelo é instruído a "pensar passo a passo" antes de responder, ele gera uma sequência de tokens que parece um raciocínio, com etapas intermediárias, considerações, descartes de hipóteses, e chega a uma conclusão final. A questão central, chamada de faithfulness do CoT, é se esses passos intermediários representam o cálculo interno que produziu a resposta final, ou se a resposta foi determinada por outros meios e a cadeia foi produzida posteriormente como uma justificação plausível. Em outras palavras, a cadeia é causa ou narrativa? Os experimentos recentes mostram que, em uma fração não desprezível dos casos, ela é narrativa.

**Analogia.** Imagine um executivo experiente que toma decisões intuitivamente a partir de padrões assimilados em décadas de prática, e que é solicitado a justificar cada decisão em forma de memorando estruturado. O memorando é honesto na intenção, mas o processo cognitivo que gerou a decisão não foi uma sequência linear de premissas e conclusões, foi um reconhecimento de padrão quase instantâneo. O memorando é uma reconstrução posterior, plausível e útil, mas não é o registro fiel do que aconteceu na cabeça do executivo. Chain of thought pode ser exatamente isso, uma reconstrução posterior plausível do cálculo interno, e não o registro fiel desse cálculo.

**Mecanismo técnico.** A literatura de faithfulness, especialmente o trabalho de Lanham et al. (Anthropic, 2023) e seus desdobramentos em 2024 e 2025, faz experimentos controlados em que componentes do CoT são modificados, removidos ou perturbados, e mede-se se a resposta final muda na direção esperada caso a cadeia fosse causal. Em muitos modelos e tarefas, a resposta final é largamente invariante a essas perturbações, o que sugere que o cálculo verdadeiro acontece antes ou paralelamente à geração da cadeia, e que a cadeia é, em parte, uma racionalização ex post. Em alguns casos, modelos respondem corretamente mesmo quando a cadeia explícita contém erros lógicos óbvios, o que reforça a hipótese de que a cadeia não é necessária ao cálculo.

Outros experimentos, como o de Turpin et al. (2023), mostram que modelos podem produzir cadeias plausíveis que omitem o fator real que motivou a decisão. Em um experimento canônico, perguntando ao modelo qual entre A e B é melhor, com um viés inserido sutilmente no prompt favorecendo A, o modelo escolhe A e produz uma cadeia que justifica a escolha por razões inteiramente diferentes do viés, sem mencionar o viés. A cadeia é coerente, plausível, e completamente desacoplada do mecanismo real que produziu a escolha. Isso tem implicações sérias para casos em que cadeias de raciocínio são usadas como evidência de não-discriminação ou de conformidade ética.

A literatura mais recente (2024-2025) começa a propor métodos de melhorar faithfulness, treinando explicitamente modelos para que cadeias e respostas estejam acopladas (causal CoT training), ou usando interpretabilidade mecanicista para validar pós-hoc se a cadeia corresponde ao cálculo interno. Esses esforços estão em estágio inicial, e nenhum modelo frontier de 2026 oferece garantia formal de faithfulness em suas cadeias.

**Implicação executiva.** Chain of thought é útil, melhora qualidade em muitas tarefas, e oferece um artefato auditável que ajuda humanos a inspecionar a saída do modelo. Mas ela não é prova de raciocínio, e não deve ser tratada como evidência forte de imparcialidade, de adesão a uma política, ou de ausência de viés. Em decisões de alto impacto, sobretudo em domínios regulados, exigir cadeia de raciocínio do modelo é uma boa prática de transparência, mas a cadeia precisa ser tratada como narrativa que pode ou não corresponder ao cálculo interno, e mecanismos adicionais de validação (RAG verificável, testes em casos contrafactuais, monitoramento de viés em saídas finais) continuam necessários.

**Quando importa para o leitor brasileiro.** Aplicações brasileiras em domínios regulados que precisam justificar decisões a um auditor externo (concessão de crédito, análise de risco em seguros, triagem médica) frequentemente expõem cadeias de raciocínio do modelo como evidência de fairness. O leitor deve saber que essa exposição, embora útil, não é prova suficiente sob a literatura técnica atual, e que reguladores e advogados informados começarão a exigir camadas adicionais de validação. Estruturar essa expectativa agora, em vez de descobrir no incidente, é higiene profissional.

**Onde aprofundar.** Lanham et al. *"Measuring Faithfulness in Chain-of-Thought Reasoning"*. Anthropic, 2023. → arxiv.org/abs/2307.13702. Turpin et al. *"Language Models Don't Always Say What They Think"*. NeurIPS, 2023. → arxiv.org/abs/2305.04388. Trabalho de seguimento sobre intervenções causais em CoT, 2024-2025.

---

## Box 9 — Interpretabilidade Mecanicista

**Por que este box existe.** Durante anos, a frase "LLMs são caixa preta" foi descrição honesta do estado da arte, e era frequentemente usada para encerrar discussões sobre auditoria, segurança e governança. Em 2024 e 2025, com avanços significativos publicados pela Anthropic e outros, a caixa preta começou a ter rachaduras. Não está aberta, mas pela primeira vez existem ferramentas que permitem inspecionar parcialmente os circuitos internos de um modelo frontier. Para o leitor que decide governança, este é um vetor a acompanhar.

**Conceito intuitivo.** Interpretabilidade mecanicista é o programa de pesquisa que tenta entender, em detalhe causal, como representações e cálculos específicos acontecem dentro de uma rede neural, identificando circuitos (subconjuntos de neurônios e atenções que implementam uma função reconhecível) e features (direções no espaço de ativação que correspondem a conceitos legíveis). O objetivo último é poder dizer, para um output específico do modelo, exatamente quais features foram ativadas, por quais entradas, e por meio de quais cabeças e camadas, com um nível de detalhe similar ao que biólogos fazem quando rastreiam o caminho de um sinal molecular em uma célula.

**Analogia.** Pense em neurociência. Por décadas, o cérebro humano foi caixa preta funcional, conhecida por seus comportamentos externos mas opaca em sua mecânica interna. Avanços em técnicas de imagem (fMRI, eletrofisiologia, optogenética) começaram a permitir, em fases, mapear quais regiões fazem o quê, e em casos cada vez mais específicos, quais conjuntos de neurônios disparam quando o sujeito pensa em uma cara, em um lugar, em uma palavra. A interpretabilidade de LLMs está mais ou menos onde a neurociência sistêmica estava nos anos 2000, com avanços rápidos e a sensação genuína de que a opacidade total está sendo erodida, mesmo que a opacidade parcial siga sendo a regra.

**Mecanismo técnico.** O programa moderno de interpretabilidade mecanicista tem três frentes principais que merecem ser conhecidas. A primeira é a hipótese de superposição, segundo a qual modelos pequenos não codificam features em neurônios individuais, e sim em direções superpostas no espaço de ativação, que precisam ser desembaraçadas com técnicas como Sparse Autoencoders (SAEs). Treinando SAEs sobre ativações de camadas específicas, pesquisadores conseguem decompor as ativações em features esparsas, cada uma correspondendo a um conceito legível, como "código em Python", "linguagem formal", "presença de risco financeiro". Trabalhos da Anthropic publicados ao longo de 2024 demonstraram milhões de features extraíveis de Claude 3 Sonnet, com mapas que mostram features se ativando em contextos coerentes.

A segunda frente é attribution graphs, técnica que mapeia, para um output específico, quais features foram causalmente responsáveis pelo output, traçando caminhos através das camadas. Esse é o método central de "Biology of a Large Language Model", trabalho amplo da Anthropic de março de 2025, que aplicou attribution graphs a Claude 3.5 Haiku para entender comportamentos como cálculo aritmético, multilinguismo, recusa a prompts perigosos e raciocínio com planejamento. Os resultados mostram que muitos comportamentos têm circuitos reconhecíveis, com features ativando em ordem e com papéis específicos, e que o modelo às vezes faz coisas surpreendentes, como planejar várias palavras à frente em poesia ou usar caminhos diferentes para a mesma operação dependendo do contexto.

A terceira frente é monossemanticidade, propriedade desejável de features extraídas, em que cada feature corresponde a um único conceito legível, em vez de a uma sopa de conceitos não-relacionados. Trabalhos seminais de Olah et al. e Bricken et al. (Anthropic, 2023) mostraram caminhos para extrair features monossemânticas a partir de SAEs treinados com critérios apropriados, abrindo a porta para um vocabulário de features que pesquisadores podem usar para descrever modelos.

**Implicação executiva.** A interpretabilidade mecanicista está, em 2026, no estágio em que se torna possível, em pesquisa, auditar parcialmente o interior de modelos frontier, e em que começam a aparecer aplicações práticas (debugging de circuitos problemáticos, validação parcial de cadeias de raciocínio, identificação de viés codificado em features específicas). Em horizonte de três a cinco anos, é plausível esperar que reguladores e auditores comecem a exigir não apenas testes de comportamento, mas também análises mecanicistas de modelos em domínios críticos. Para empresas que dependem de modelos em escala, acompanhar essa evolução agora é melhor do que reagir depois.

**Quando importa para o leitor brasileiro.** Empresas brasileiras em setores com auditoria forte (financeiro sob BACEN, saúde sob ANS, seguro sob Susep) terão interesse, dentro do horizonte de poucos anos, em poder oferecer aos reguladores não apenas evidência comportamental de que o modelo não discrimina, mas também evidência mecanicista de quais features são ativadas em decisões críticas. Adotar essa pauta proativamente, em conversa com fornecedores de modelos, posiciona a empresa à frente da curva regulatória que está se formando.

**Onde aprofundar.** Anthropic. *"Biology of a Large Language Model"*. Março de 2025. → anthropic.com/research. Bricken et al. *"Towards Monosemanticity: Decomposing Language Models With Dictionary Learning"*. Anthropic, 2023. Templeton et al. *"Scaling Monosemanticity: Extracting Interpretable Features from Claude 3 Sonnet"*. Anthropic, 2024. Olah et al. trabalhos seminais em Distill.

---

## Box 10 — Scaling Laws

**Por que este box existe.** Por anos, a narrativa pública sobre IA assumiu que aumentar modelo significaria aumentar capacidade, indefinidamente, e que o caminho para a próxima geração era simplesmente investir mais bilhões em GPU. As scaling laws empíricas, formalizadas em 2020 e refinadas em 2022, deram base teórica para essa expectativa, e a percepção de platô em 2024-2025 deu base empírica para a sua revisão. Para quem decide investimento de capital e expectativa estratégica de quando IA "chega lá", este box é leitura obrigatória.

**Conceito intuitivo.** Scaling laws são relações empíricas, observadas em larga escala, entre três variáveis fundamentais do treinamento de modelos de linguagem, o número de parâmetros, o número de tokens de treinamento e o compute total investido (medido em FLOPs), e a métrica de qualidade do modelo, tipicamente loss em um conjunto de teste. As primeiras leis, de Kaplan et al. em 2020, sugeriram que loss caía como lei de potência em cada uma das três variáveis, com expoentes que indicavam onde investir margem adicional de compute. As leis foram refinadas em 2022 por Hoffmann et al. (paper Chinchilla), que mostraram que os pontos de operação anteriores haviam superestimado parâmetros e subestimado tokens, e propuseram regras de proporção entre os dois para compute fixo.

**Analogia.** Pense em um restaurante que tenta aumentar sua qualidade investindo em três alavancas, número de cozinheiros (parâmetros), tempo de treinamento dos cozinheiros (tokens) e dinheiro total disponível (compute). Por anos, os donos assumiram que dobrar cozinheiros dobrava qualidade, e investiram nessa direção. Auditorias posteriores mostraram que a alavanca mais sub-investida era tempo de treinamento, e que com o mesmo dinheiro, formas diferentes de alocação produziriam restaurantes muito melhores. Mais recentemente, observou-se que a qualidade do que os cozinheiros estudam (qualidade dos dados) importa mais do que qualquer das três alavancas, e isso virou a fronteira competitiva atual.

**Mecanismo técnico.** A formulação clássica de Kaplan et al. (2020) sugere que a loss L como função do compute C segue L proporcional a C elevado a -α, com α em torno de 0.05, e relações similares para número de parâmetros N e número de tokens D, com expoentes ligeiramente diferentes. A consequência prática naquela leitura era que, para compute fixo, modelos deveriam ser tão grandes quanto possível, e o número de tokens de treino crescia secundariamente. O paper Chinchilla, de Hoffmann et al. (2022), refez os experimentos com mais cuidado em controlar variáveis e chegou à conclusão oposta, que para compute fixo, parâmetros e tokens deveriam crescer aproximadamente em proporção igual, e que modelos anteriores haviam sido sub-treinados, ou seja, tinham parâmetros demais para os tokens vistos. A regra prática Chinchilla, que ficou conhecida, é tokens por parâmetro de aproximadamente vinte para um.

A revisão Chinchilla mudou prática da indústria, e modelos posteriores (Llama 2, Llama 3, Mistral, DeepSeek) foram treinados em proporções próximas àquela ótima. O resultado foi modelos menores em parâmetros mas treinados em muito mais tokens, com qualidade dramaticamente melhor por dólar gasto. Llama 3 70B, com seu volume de mais de quinze trilhões de tokens vistos, ilustra essa filosofia, e supera em qualidade modelos significativamente maiores treinados sob a curva Kaplan original.

A discussão de 2024 e 2025 trouxe um elemento novo, a sensação de platô em modelos frontier, com sucessivas gerações trazendo ganhos perceptivelmente menores em benchmarks padronizados, e a hipótese de que estaríamos próximos de um teto onde nem mais parâmetros, nem mais tokens, nem mais compute resolveriam por si só. As respostas a esse aparente teto têm sido três, todas legítimas, todas em evolução. A primeira é qualidade de dados, com curadoria intensiva e geração sintética de dados de alta qualidade compensando o esgotamento de texto humano de qualidade. A segunda é técnicas pós-treino, como RLHF refinado, raciocínio explícito com computação adicional na inferência (o3, Claude com extended thinking), que extraem mais capacidade de modelos do mesmo tamanho. A terceira é arquitetura, com MoE, atenção esparsa, atenção latente e variantes que mudam a relação entre parâmetros e capacidade efetiva.

**Implicação executiva.** A expectativa de que próximas gerações de modelos serão dramaticamente melhores apenas por escala bruta deve ser calibrada para baixo. Os ganhos por geração estão se tornando mais incrementais e mais dependentes de inovações em dados, técnicas e arquitetura. Em decisão de cronograma estratégico, assumir que daqui a três anos um modelo dez vezes melhor cairá no mercado é otimismo arriscado. O mais prudente é assumir que a fronteira evolui, mas mais lentamente, e que ganhos práticos virão tanto de aperfeiçoamento de produto sobre modelos atuais quanto de novas gerações.

**Quando importa para o leitor brasileiro.** Empresas brasileiras planejando investimento em IA para horizonte de três a cinco anos devem evitar a armadilha de adiar decisões esperando o próximo modelo milagroso. A regra prática, em 2026, é desenhar arquiteturas que extraiam valor dos modelos atuais com elegância, e que sejam capazes de se beneficiar de atualizações graduais nos próximos anos, em vez de apostar em um salto que pode não vir. Esse posicionamento é especialmente importante em decisões de transformação digital de grande escala que dependem de viabilidade econômica imediata, e não podem esperar uma promessa de fronteira que está ficando mais cara e menos confiável de prever.

**Onde aprofundar.** Kaplan et al. *"Scaling Laws for Neural Language Models"*. OpenAI, 2020. → arxiv.org/abs/2001.08361. Hoffmann et al. *"Training Compute-Optimal Large Language Models"* (Chinchilla). DeepMind, 2022. → arxiv.org/abs/2203.15556. Discussões de 2024-2025 sobre platô e dados sintéticos, com trabalhos em torno de Llama 3, DeepSeek V3 e Phi-3 como pontos de referência.

---

## Box 11 — Matriz de Interações entre os Conceitos

**Por que este box existe.** Os dez conceitos cobertos até aqui foram apresentados como unidades autônomas, com mecanismo, analogia e implicação executiva próprios, e essa escolha pedagógica é defensável quando o leitor está formando vocabulário. Mas a decisão executiva real, aquela em que um CTO precisa escolher stack, dimensionar GPU, calibrar latência aceitável e ainda atender ao auditor regulatório no trimestre seguinte, quase nunca depende de um conceito isolado. Ela vive nas zonas de fricção em que dois ou três desses mecanismos interagem, às vezes amplificando ganho, às vezes obrigando o decisor a escolher entre duas otimizações que não convivem em paz. Este box transversal mapeia essas interações em uma matriz e detalha cinco pares cuja combinação aparece com mais frequência em decisões de produção em 2026.

### Matriz triangular de interações

A tabela abaixo registra a interação esperada entre cada par de conceitos. Use o legenda padrão: 🔴 conflito (combinados, exigem decisão antagônica e quase nunca convivem), 🟢 sinergia (combinados, ampliam ganho de forma multiplicativa), 🟡 trade-off (combinados, viáveis mas exigem decisão consciente sobre o que se ganha e o que se paga), ⚪ neutro (a interação existe mas não muda materialmente a decisão).

|  | MoE | Spec. Decoding | KV Cache | FlashAttention | LoRA | Quantização | Structured Output | Faithfulness | Mech Interp | Scaling Laws |
|---|---|---|---|---|---|---|---|---|---|---|
| **MoE** | — | 🟡 | 🟡 | 🟢 | 🟡 | 🟡 | ⚪ | 🟡 | 🔴 | 🟢 |
| **Speculative Decoding** | | — | 🟢 | 🟢 | ⚪ | 🟢 | 🟢 | 🟡 | ⚪ | ⚪ |
| **KV Cache** | | | — | 🟢 | ⚪ | 🟢 | ⚪ | ⚪ | ⚪ | 🟡 |
| **FlashAttention** | | | | — | ⚪ | 🟢 | ⚪ | ⚪ | ⚪ | 🟢 |
| **LoRA** | | | | | — | 🟡 | ⚪ | ⚪ | 🟡 | ⚪ |
| **Quantização** | | | | | | — | ⚪ | 🟡 | 🟡 | 🟡 |
| **Structured Output** | | | | | | | — | 🟡 | ⚪ | ⚪ |
| **Faithfulness** | | | | | | | | — | 🟢 | ⚪ |
| **Mech Interp** | | | | | | | | | — | ⚪ |
| **Scaling Laws** | | | | | | | | | | — |

A leitura da matriz é triangular superior; as células abaixo da diagonal repetiriam a mesma informação e foram suprimidas para clareza. Pares marcados como 🟢 são candidatos preferenciais a otimização combinada; pares 🟡 são onde a decisão executiva precisa ser tomada com consciência do que se sacrifica; pares 🔴 são alertas para que o arquiteto não tente fazer os dois ao mesmo tempo sem custo. Cinco interações merecem aprofundamento e estão tratadas nas subseções seguintes.

### Interação 1 — MoE × KV Cache

A combinação de Mixture of Experts com KV Cache é exemplo clássico de sinergia tornada complexa pela interação. Em modelo denso, o KV cache cresce linearmente com o comprimento da sequência e a profundidade do modelo, e sua gestão em produção (paged attention, prompt caching, batch dimensioning) é problema bem mapeado. Em MoE, cada token ativa um subconjunto distinto de experts em cada camada, e o KV cache associado precisa ser indexado por roteamento, não apenas por posição. O resultado é que técnicas de prompt caching que funcionam por prefixo exato em modelo denso podem falhar silenciosamente em MoE quando o roteamento se altera entre execuções (por variação de batch composition ou por estocasticidade leve do gate). Em decisão de stack, o CTO precisa exigir do fornecedor garantia de cache estável sob MoE, ou aceitar que parte do ganho de custo do MoE será corroído por hit rate menor no prompt cache.

### Interação 2 — LoRA × Quantização

A combinação de LoRA com quantização é o pesadelo prático mais comum em deploy on-prem, porque a ordem das operações importa e raramente é documentada com clareza no fornecedor. Existem duas ordens razoáveis. A primeira é treinar LoRA no modelo em precisão alta (FP16 ou BF16) e depois quantizar o conjunto (modelo base mais adapters LoRA fundidos), o que tende a preservar qualidade do treino mas perde parte do ganho de tamanho prometido pela quantização agressiva. A segunda é quantizar primeiro o modelo base e depois treinar LoRA sobre ele (QLoRA, técnica popularizada por Dettmers et al. em 2023), o que permite treino em hardware modesto mas exige cuidado adicional para que os adapters não amplifiquem erros de quantização. Para o tomador de decisão, a regra prática é: se o objetivo é deploy mínimo em hardware barato, prefira QLoRA; se o objetivo é qualidade máxima sob restrição de tamanho moderada, prefira treinar em precisão alta e quantizar depois. A escolha errada produz degradação de qualidade que aparece em produção como queda de aderência ao golden set, sem que o engenheiro entenda de onde veio.

### Interação 3 — FlashAttention × Scaling Laws

FlashAttention e suas variantes (FlashAttention-2, FlashAttention-3) reduzem o custo de atenção de quadrático para próximo de linear em comprimento de sequência, e essa eficiência abre janela para treinar e servir modelos maiores e contextos mais longos sem refazer o orçamento de compute. Em teoria, isso amplifica scaling laws, porque permite que parte do ganho previsto pela curva de Kaplan ou Chinchilla seja realmente realizada. Em prática, no entanto, as scaling laws estão em platô empírico desde 2024, e os ganhos por geração estão se tornando incrementais e cada vez mais dependentes de qualidade de dados e técnicas pós-treino. O trade-off para o decisor é o seguinte: FlashAttention torna economicamente viável aumentar contexto e parâmetros, mas o retorno por dólar adicional gasto em parâmetros está caindo. Investir na ponta da escala virou aposta com retorno marginal decrescente, e o capital tende a render mais aplicado em curadoria de dados ou em arquitetura híbrida do que em puro aumento de tamanho viabilizado por FlashAttention.

### Interação 4 — Speculative Decoding × Reasoning Models

Speculative decoding ganha latência aceitando que um modelo draft pequeno gere sequência candidata que o modelo principal valida em paralelo. Em modelos de raciocínio (DeepSeek R1, o3, Claude com extended thinking), a sequência gerada inclui longas cadeias de pensamento interno antes da resposta final ao usuário, e a aceleração obtida pelo draft depende da capacidade dele de antecipar a estrutura da cadeia. O ponto sensível é que o modelo draft, sendo pequeno, raramente acerta o conteúdo de raciocínio passo a passo, e a taxa de aceitação tende a cair em sequências de reasoning longo. Variantes como Medusa (cabeças adicionais no modelo principal) mitigam parte do problema, e abordagens emergentes propõem draft especializado em reasoning. Para o decisor, a regra prática em 2026 é: speculative decoding entrega ganho consistente em geração padrão e ganho menor (mas ainda positivo) em reasoning models; quando o produto depende de latência sob extended thinking, exija medição de aceleração efetiva sob carga típica, não apenas no benchmark genérico do fornecedor.

### Interação 5 — MoE × Speculative Decoding

A combinação de Mixture of Experts com Speculative Decoding é tentadora porque ambos prometem reduzir custo de inferência, mas os mecanismos não somam de forma trivial. O draft model usado em speculative decoding precisa antecipar quais tokens o modelo principal vai produzir, e em MoE essa antecipação é estruturalmente mais difícil, porque o roteamento de cada token pode ativar especialistas distintos do draft e do principal, gerando taxa de aceitação menor do que em modelo denso equivalente. Em produção, a operação madura raramente ganha duas vezes o múltiplo prometido por cada técnica isolada; o ganho efetivo costuma ficar entre cinquenta e setenta por cento do somatório teórico. Pior, o overhead de manter sincronia entre o roteador do draft e o do principal pode anular parcialmente o ganho em batches pequenos, comuns em SaaS multi-tenant brasileiro. Para o decisor, a regra prática é: medir o ganho conjunto sob carga real antes de assumir que as duas técnicas se complementam, e exigir do fornecedor benchmark específico para o seu perfil de tráfego, jamais aceitar números de marketing genérico.

### Interação 6 — Structured Output × Faithfulness de CoT

A combinação de structured output (JSON Mode, response_format=json) com chain of thought visível introduz tensão arquitetural pouco discutida na literatura comercial e que pega muita equipe em produção. O structured output força o modelo a comprometer cedo com formato fechado, frequentemente listando o raciocínio dentro de um campo `reasoning` e a conclusão em outro campo `answer`. Em medições controladas, essa restrição reduz a faithfulness da cadeia, porque o modelo aprende a escrever raciocínio que justifica a resposta que ele já sabe que vai colocar no campo answer, em vez de raciocinar e descobrir a resposta no processo. O efeito é maior em domínios onde o modelo tem incentivo a parecer coerente, como avaliação de risco, parecer técnico ou diagnóstico clínico. Para o decisor, a regra prática é: quando auditabilidade do raciocínio é parte do produto, separar a chamada de raciocínio (formato livre) da chamada de estruturação (structured output sobre a resposta já produzida), aceitando o custo de duas chamadas em troca da preservação da faithfulness. Estruturar e raciocinar simultaneamente é a forma mais comum de tornar a cadeia exposta em narrativa pós-hoc decorativa.

### Interação 7 — Mech Interp × Quantização

A combinação de interpretabilidade mecanicista com quantização é diretamente conflituosa, e o conflito raramente é declarado pelos fornecedores que vendem ambos os recursos. Mech interp depende da capacidade de inspecionar features, circuitos e ativações em precisão suficiente para reconhecer padrões consistentes entre prompts. Quantização agressiva (INT4, INT2) reduz a precisão numérica das ativações ao ponto em que ferramentas de análise como sparse autoencoders, probing classifiers e circuit identification entregam resultados degradados, com ruído que torna difícil distinguir feature legítima de artefato de quantização. Em produção on-prem, onde quantização é frequentemente exigida para caber em GPU acessível, o time de governança que pretende usar mech interp como ferramenta defensiva precisa manter um servidor não-quantizado paralelo, dedicado exclusivamente a auditoria de amostras representativas. Para o CTO em domínio regulado, a regra prática é: orçar capacidade não-quantizada de auditoria desde o início do projeto, jamais descobrir esse custo na primeira fiscalização. Quantizar primeiro e tentar auditar depois é a configuração mais comum de retrabalho caro.

### Interação 8 — Faithfulness × Mech Interp

Faithfulness de chain of thought e interpretabilidade mecanicista são duas frentes da mesma agenda — abrir a caixa preta — abordando-a por ângulos diferentes. Faithfulness pergunta se a narrativa do raciocínio corresponde ao cálculo interno. Mech interp tenta descrever o cálculo interno em termos de circuitos e features. A sinergia é real: interpretabilidade mecanicista pode, em princípio, ser usada para validar pós-hoc se a cadeia exposta pelo modelo corresponde ao caminho computacional efetivamente percorrido. O trade-off é igualmente real: análise mecanicista é cara em tempo de execução e em compute de auditoria, e fazê-la em escala de produção, em cada decisão crítica, ainda é tecnicamente inviável em 2026. Para o CTO em domínio regulado, a regra prática é tratar mech interp como capacidade defensiva a desenvolver com horizonte de poucos anos, em paralelo com governança que hoje opera com técnicas mais leves (RAG verificável, contrafactuais, monitoramento de viés em saídas finais); e tratar faithfulness como propriedade desejável mas não garantida em qualquer cadeia exposta a auditor.

### Implicação executiva

A regra prática para quem decide stack em 2026 é simples na enunciação e difícil na execução. Comece sempre pela interação mais cara do seu produto, medida em três eixos combinados: custo de inferência, latência percebida pelo usuário e auditabilidade exigida pelo regulador setorial. Identifique qual par de boxes domina cada eixo. Em produto de alto volume com latência sensível, o par dominante costuma ser Speculative Decoding × KV Cache; em produto regulado com auditoria forte, o par dominante costuma ser Faithfulness × Mech Interp; em deploy on-prem em hardware modesto, o par dominante é LoRA × Quantização. Otimize primeiro o par dominante, e só depois inclua boxes secundários para refinar a margem residual. Tentar otimizar todos os boxes ao mesmo tempo, sem priorizar a interação que domina o seu caso, é a forma mais comum de queimar orçamento de engenharia em ganhos marginais que não aparecem no PnL e que pioram a auditabilidade.

---

> *"Cada um destes boxes existe porque algum executivo, em algum lugar, tomou uma decisão de stack sem saber o que estava escolhendo. Que a próxima decisão seja melhor informada."*

</div>
</section>
