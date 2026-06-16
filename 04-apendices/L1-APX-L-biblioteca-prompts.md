# Apêndice L — Biblioteca de Prompts Profissionais

> **Moldura de método — leia antes das fichas**
>
> Este apêndice reúne trinta prompts profissionais. Antes de entrar nas fichas, um aviso necessário sobre o que você está lendo e o que não está.
>
> **O que cada prompt é:** uma instância documentada de princípios de engenharia de contexto — não uma receita definitiva. Cada ficha existe para tornar visível uma estrutura que funciona: como separar instrução de dado, como ancorar persona antes de tarefa, como forçar self-critique em outputs de alto risco, como delimitar escopo sem ambiguidade. Esses princípios são transferíveis. Os prompts específicos que os instanciam, não.
>
> **O que envelhece:** o XML executável, os nomes de modelo em campos de recomendação, os números de benchmarks citados, os limites de plataforma, os textos de exemplo. Tudo isso está sujeito a iteração. O repositório acompanhante ([github.com/falercia/inteligencia-aumentada-recursos](https://github.com/falercia/inteligencia-aumentada-recursos)) existe exatamente para absorver essa evolução sem congelar o conhecimento no livro.
>
> **O que não envelhece:** a lógica de camada dupla (separar o durável do volátil), os oito padrões de operação, os oito anti-padrões transversais, a anatomia F4 (persona → constituição → contexto → tarefa → formato), e a prática de manter golden set com regressão a cada troca de modelo. Esses são os invariantes. As fichas a seguir são exemplos de como eles se materializam em domínios reais — não o produto final do método, mas sua evidência.
>
> **Como usar:** leia cada ficha perguntando "que princípio de engenharia de contexto está sendo aplicado aqui?" em vez de "posso copiar este prompt?". O leitor que sair do apêndice com os oito padrões internalizados tem mais do que o leitor que decorou os trinta XMLs. Modelos passam. Método fica.

---

## Por que este apêndice existe em duas camadas

A biblioteca que este apêndice apresenta reúne trinta prompts profissionais que foram desenhados como ativos de produção, no sentido estrito de que cada um foi pensado para entrar em pipelines reais, com inputs reais, com riscos reais, e com necessidade de versionamento, auditoria e regressão automatizada. A construção desses ativos exige duas peças que se complementam, e a obra trata cada uma delas no andar certo.

A primeira peça é o padrão durável, e ela vive aqui no livro, na forma de trinta fichas conceituais. Cada ficha entrega a dor que o prompt resolve, o escopo do domínio, o que esperar como saída, a anatomia da estrutura sob o Framework Quatro, os anti-padrões observados em prática, o critério explícito de quando usar e quando evitar, o modelo recomendado e a métrica de qualidade. A ficha é o que o operador maduro precisa entender para adaptar o prompt ao próprio contexto, e para construir biblioteca interna calibrada para o tráfego real da sua operação.

A segunda peça é o número volátil, e ela vive no repositório acompanhante público em [github.com/falercia/inteligencia-aumentada-recursos](https://github.com/falercia/inteligencia-aumentada-recursos), em pasta dedicada por prompt, com o XML completo do ativo, o golden set de vinte casos calibrados pelo autor, o changelog público datado, os anti-padrões em detalhe e o script de regressão executável. Quem chega à ficha do livro com clareza conceitual encontra no repositório o artefato pronto para clonar, adaptar e colocar em CI, sem ter que reescrever cada estrutura do zero.

Essa separação é deliberada e materializa o Invariante Três, a Camada Dupla (definido no capítulo de abertura "Os Nove Invariantes"). O padrão dura porque a estrutura conceitual sobrevive à próxima geração de modelo, ao próximo provedor, à próxima moda de framework. O número muda porque o XML específico vai sofrer iteração mensal, o golden set vai crescer com calibração de especialistas externos, e a métrica de qualidade vai ser refinada a cada release. Manter as duas no mesmo arquivo, como faziam as primeiras versões deste apêndice, congelava o XML em mídia impressa e impedia a evolução contínua do ativo. O leitor que entendeu o método vai ao repositório quando precisa do executável, e fica com a ficha quando precisa do método.

### Quadro de orientação — onde vive o quê

| Camada do conhecimento | Onde vive | Cadência de revisão |
|---|---|---|
| Dor que o prompt resolve, anatomia sob Framework Quatro, critério de quando usar e quando evitar, anti-padrões estruturais, métrica de qualidade | **LIVRO · ficha conceitual** | Anual, junto com a próxima edição |
| XML executável completo, golden set de vinte casos calibrados, prefill, self-critique, changelog datado, script de regressão, anti-padrões em detalhe | **REPO · `/prompts/<dominio>/<id>/`** · [github.com/falercia/inteligencia-aumentada-recursos](https://github.com/falercia/inteligencia-aumentada-recursos) | Sem cadência fixa, conforme evolução real do ativo |
| Resultado de execução em modelo da rodada, custo médio por chamada, posição em benchmark de qualidade aplicado | **APÊNDICE J · Trilha do Número** | Sem cadência fixa, conforme movimento relevante de mercado |

O leitor com pressa que precisa apenas decidir se adota um prompt resolve a decisão na ficha conceitual. O leitor que vai operar o prompt em produção desce ao repositório. O leitor que precisa justificar custo ou comparar com alternativa em ata de comitê consulta o Apêndice J. Os três artefatos são desenhados para serem usados em conjunto, jamais como substitutos um do outro.

> **Política de manutenção do repositório:** os trinta prompts estão populados e são auditados a cada release do livro. Se o link não funcionar ou o prompt específico não for encontrado, o canal de fallback é o e-mail declarado na página de créditos do livro — o objetivo é que nenhum leitor fique sem acesso ao artefato executável por razão técnica.

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

**Convenção de modelo usada nas fichas.** As fichas empregam três faixas de família de modelo, intencionalmente sem nomear versões específicas para preservar durabilidade:

- *Haiku equivalente* — modelo otimizado para velocidade e custo em tarefas classificatórias de baixa complexidade semântica (triagem em volume, roteamento, extração simples).
- *Sonnet equivalente* — modelo com suporte a raciocínio estruturado, janela de contexto de 100 mil tokens ou mais e structured output nativo. Adequado para análise jurídica, médica ou financeira com saída estruturada e regras complexas.
- *Sonnet equivalente com raciocínio estendido* — mesmo perfil anterior, com capacidade de extended thinking ou chain-of-thought longo ativado, para casos que exigem decomposição de problema antes do output final.

O critério é funcional, não de marca. Ao trocar de modelo ou de provedor, verifique contra essas propriedades, não contra o nome. A denominação não cita modelos específicos porque eles envelhecem; o critério operacional, não.

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
8. **Monitore recusas do modelo por categoria de input.** Quando o modelo recusar a tarefa — seja por política de conteúdo, seja por input fora do escopo da constituição — registre o motivo literal da recusa, o input que a gerou e o modelo/versão em uso. Taxa de recusa acima de 5% numa categoria específica é sinal de alarme que exige revisão da constituição ou do contexto: pode indicar ambiguidade no prompt ou mudança silenciosa de política do provedor, e ambos exigem ação antes de afetar o pipeline em produção.

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

## Índice dos 30 prompts

A tabela a seguir é a entrada do apêndice para cada prompt. O invariante que cada ficha ilustra é o que vale ler aqui; a ficha executável completa — XML, golden set, changelog, script de regressão — vive no repositório.

| ID | Nome | Setor | Invariante ilustrado | Repositório |
|---|---|---|---|---|
| P-LEG-01 | Revisão de Cláusula de Não-Concorrência CLT | Jurídico | Constituição estrita + citação literal obrigatória | [/prompts/P-LEG-01](https://github.com/falercia/inteligencia-aumentada-recursos/tree/main/prompts/P-LEG-01-clausula-nao-concorrencia-clt) |
| P-LEG-02 | Análise de NDA Brasileiro LGPD-Compliant | Jurídico | Escopo fechado + sinalização de lacuna | [/prompts/P-LEG-02](https://github.com/falercia/inteligencia-aumentada-recursos/tree/main/prompts/P-LEG-02-nda-lgpd-compliant) |
| P-LEG-03 | Red Flags em Contrato M&A | Jurídico | Classificação em níveis estáveis + JSON fechado | [/prompts/P-LEG-03](https://github.com/falercia/inteligencia-aumentada-recursos/tree/main/prompts/P-LEG-03-red-flags-contrato-ma) |
| P-LEG-04 | Parecer sobre Compliance LGPD em Processamento de Dados | Jurídico | Indeterminado explícito quando falta evidência | [/prompts/P-LEG-04](https://github.com/falercia/inteligencia-aumentada-recursos/tree/main/prompts/P-LEG-04-parecer-compliance-lgpd) |
| P-MED-01 | Triagem de Sintomas com Recusa por Escopo | Saúde | Conservadorismo em dúvida + recusa estruturada | [/prompts/P-MED-01](https://github.com/falercia/inteligencia-aumentada-recursos/tree/main/prompts/P-MED-01-triagem-sintomas) |
| P-MED-02 | Súmula de Prontuário | Saúde | Fidelidade ao registro + marcação de ambiguidade | [/prompts/P-MED-02](https://github.com/falercia/inteligencia-aumentada-recursos/tree/main/prompts/P-MED-02-sumula-prontuario) |
| P-MED-03 | Alerta de Interação Medicamentosa | Saúde | Self-critique para segurança clínica + fallback humano | [/prompts/P-MED-03](https://github.com/falercia/inteligencia-aumentada-recursos/tree/main/prompts/P-MED-03-interacao-medicamentosa) |
| P-FIN-01 | Detecção de Anomalia em Extrato | Financeiro | Justificativa observável + sem inferir identidade | [/prompts/P-FIN-01](https://github.com/falercia/inteligencia-aumentada-recursos/tree/main/prompts/P-FIN-01-anomalia-extrato) |
| P-FIN-02 | Classificação de Risco de Crédito PF | Financeiro | Variável vedada explícita na constituição | [/prompts/P-FIN-02](https://github.com/falercia/inteligencia-aumentada-recursos/tree/main/prompts/P-FIN-02-risco-credito-pf) |
| P-FIN-03 | Súmula de Relatório Trimestral ITR | Financeiro | Fidelidade numérica + sem recomendação implícita | [/prompts/P-FIN-03](https://github.com/falercia/inteligencia-aumentada-recursos/tree/main/prompts/P-FIN-03-sumula-itr) |
| P-FIN-04 | Análise de Carteira Recomendada | Financeiro | Descritivo vs. recomendação: fronteira explícita | [/prompts/P-FIN-04](https://github.com/falercia/inteligencia-aumentada-recursos/tree/main/prompts/P-FIN-04-analise-carteira) |
| P-SAAS-01 | Classificação de Feature Request por Persona | SaaS/Produto | Sem prometer entrega + citação literal como evidência | [/prompts/P-SAAS-01](https://github.com/falercia/inteligencia-aumentada-recursos/tree/main/prompts/P-SAAS-01-feature-request) |
| P-SAAS-02 | Súmula de NPS Qualitativo | SaaS/Produto | Sinal fraco vs. tema dominante: distinção estrutural | [/prompts/P-SAAS-02](https://github.com/falercia/inteligencia-aumentada-recursos/tree/main/prompts/P-SAAS-02-sumula-nps) |
| P-SAAS-03 | Geração de Release Notes | SaaS/Produto | Apenas mudanças listadas + breaking change em destaque | [/prompts/P-SAAS-03](https://github.com/falercia/inteligencia-aumentada-recursos/tree/main/prompts/P-SAAS-03-release-notes) |
| P-SAAS-04 | Análise de Churn Signal | SaaS/Produto | Plano dentro do alcance do operador + prazo declarado | [/prompts/P-SAAS-04](https://github.com/falercia/inteligencia-aumentada-recursos/tree/main/prompts/P-SAAS-04-churn-signal) |
| P-SUP-01 | Classificação de Ticket em Severidade | Suporte | Critério técnico vs. tom emocional na constituição | [/prompts/P-SUP-01](https://github.com/falercia/inteligencia-aumentada-recursos/tree/main/prompts/P-SUP-01-severidade-ticket) |
| P-SUP-02 | Resposta Empática a Reclamação | Suporte | Empatia real vs. fórmula vazia: regra na constituição | [/prompts/P-SUP-02](https://github.com/falercia/inteligencia-aumentada-recursos/tree/main/prompts/P-SUP-02-resposta-empatica) |
| P-SUP-03 | Decisão sobre Escalonamento | Suporte | Critério literal auditável + ação intermediária em limítrofes | [/prompts/P-SUP-03](https://github.com/falercia/inteligencia-aumentada-recursos/tree/main/prompts/P-SUP-03-escalonamento) |
| P-RH-01 | Triagem de Currículo com Fit | RH | Variável vedada explícita + aprofundamento humano obrigatório | [/prompts/P-RH-01](https://github.com/falercia/inteligencia-aumentada-recursos/tree/main/prompts/P-RH-01-triagem-curriculo) |
| P-RH-02 | Análise de Feedback 360 | RH | Preservação de anonimato + equilíbrio sem inflar | [/prompts/P-RH-02](https://github.com/falercia/inteligencia-aumentada-recursos/tree/main/prompts/P-RH-02-feedback-360) |
| P-RH-03 | Descritivo de Vaga em Linguagem Inclusiva | RH | Bloqueio de requisito discriminatório na constituição | [/prompts/P-RH-03](https://github.com/falercia/inteligencia-aumentada-recursos/tree/main/prompts/P-RH-03-descritivo-vaga) |
| P-MKT-01 | Geração de Copy A/B Testável | Marketing | Hipóteses semanticamente distintas + compliance declarado | [/prompts/P-MKT-01](https://github.com/falercia/inteligencia-aumentada-recursos/tree/main/prompts/P-MKT-01-copy-ab) |
| P-MKT-02 | Análise de Brand Voice | Marketing | Diagnóstico estruturado vs. juízo estético | [/prompts/P-MKT-02](https://github.com/falercia/inteligencia-aumentada-recursos/tree/main/prompts/P-MKT-02-brand-voice) |
| P-MKT-03 | Súmula de Pesquisa de Mercado | Marketing | Ressalvas metodológicas em destaque + sem extrapolar amostra | [/prompts/P-MKT-03](https://github.com/falercia/inteligencia-aumentada-recursos/tree/main/prompts/P-MKT-03-sumula-pesquisa) |
| P-EDU-01 | Geração de Plano de Aula | Educação | Soma de tempos coerente + sem prometer resultado | [/prompts/P-EDU-01](https://github.com/falercia/inteligencia-aumentada-recursos/tree/main/prompts/P-EDU-01-plano-aula) |
| P-EDU-02 | Avaliação Rubrica-Baseada | Educação | Critério primeiro, consolidado depois: ordem como invariante | [/prompts/P-EDU-02](https://github.com/falercia/inteligencia-aumentada-recursos/tree/main/prompts/P-EDU-02-avaliacao-rubrica) |
| P-EDU-03 | Resposta Socrática a Dúvida do Aluno | Educação | Sem entregar resposta em conteúdo construído + pista progressiva | [/prompts/P-EDU-03](https://github.com/falercia/inteligencia-aumentada-recursos/tree/main/prompts/P-EDU-03-resposta-socratica) |
| P-TR-01 | Extração Estruturada com Schema JSON | Transversal | Null explícito + sem conversão sem instrução | [/prompts/P-TR-01](https://github.com/falercia/inteligencia-aumentada-recursos/tree/main/prompts/P-TR-01-extracao-json) |
| P-TR-02 | Classificação Multi-Label | Transversal | Fallback indeterminado + evidência textual obrigatória | [/prompts/P-TR-02](https://github.com/falercia/inteligencia-aumentada-recursos/tree/main/prompts/P-TR-02-multi-label) |
| P-TR-03 | Recusa Estruturada com Fallback | Transversal | Recusa integral + sem revelar prompt interno | [/prompts/P-TR-03](https://github.com/falercia/inteligencia-aumentada-recursos/tree/main/prompts/P-TR-03-recusa-fallback) |

---

**Camada viva.** O método está aqui; os artefatos/listas que mudam vivem no repositório de recursos da obra ([github.com/falercia/inteligencia-aumentada-recursos](https://github.com/falercia/inteligencia-aumentada-recursos) → `/prompts`), atualizados continuamente.

---

*Apêndice L · Biblioteca de Prompts Profissionais. Versão executável em [github.com/falercia/inteligencia-aumentada-recursos](https://github.com/falercia/inteligencia-aumentada-recursos). Política editorial: instrumento vivo, sem cadência fixa anunciada.*
