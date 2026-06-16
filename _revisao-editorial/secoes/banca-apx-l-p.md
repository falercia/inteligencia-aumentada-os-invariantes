# APX-L — Biblioteca de Prompts Profissionais

## RESUMO EXECUTIVO
Nota: 6/10
Veredito: B

---

## O QUE FUNCIONA

- **A estratégia de camada dupla (livro + repositório) é intelectualmente honesta.** Separar a ficha conceitual durável do XML executável volátil é a única arquitetura que salva o apêndice de envelhecer com o modelo. A justificativa na introdução é clara e bem argumentada.
- **O Changelog editorial é o melhor trecho do apêndice.** Mostrar iteração real — o que quebrou, por que foi corrigido, qual o impacto no golden set — é raro em livros de negócios e entrega exatamente o que a tese promete: método, não receita. Se houvesse um apêndice inteiro sobre isso, seria superior ao catálogo de fichas.
- **Os sete padrões de operação são transferíveis e duráveis.** Regras como "jamais concatene instrução com dado", "mantenha golden set de 20 casos", "reverifique contra o golden set ao trocar de modelo" — essas sobrevivem à próxima geração porque não dependem de nenhum modelo específico.
- **Os anti-padrões transversais têm alta densidade de utilidade.** São oito padrões de falha observados em campo, com justificativa causal, não apenas lista. Essa seção é citável e memorável.
- **A anatomia comentada do Framework Quatro (F4) é pedagogicamente sólida.** Explicar *por que* cada bloco XML está naquela posição — e não apenas *o que* ele faz — diferencia o conteúdo de um tutorial.
- **Cobertura setorial brasileira é genuinamente diferenciada.** LGPD, CLT, TST, ITR, ANPD, BACEN, ANS — a especificidade regulatória é uma forma real de propriedade intelectual que não existe em equivalentes internacionais do gênero.
- **A cadência de fichas é consistente.** Todos os 30 prompts seguem o mesmo molde de nove campos, o que permite leitura rápida comparada e navegação pontual.

---

## O QUE NÃO FUNCIONA

- **O apêndice é fundamentalmente um catálogo, e a tese do livro proíbe catálogos.** Trinta fichas organizadas por setor (Jurídico, Saúde, Financeiro, SaaS, Suporte, RH, Marketing, Educação, Transversais) com URL de repositório é, formalmente, o tipo de artefato que "Modelos passam. Método fica." deveria rejeitar. A estratégia de camada dupla mitiga o problema, mas não o elimina.
- **"Modelo recomendado: Sonnet equivalente" em 26 das 30 fichas é conteúdo sem informação.** Se 87% das fichas têm a mesma resposta, o campo não está diferenciando nada. É ruído que ocupa espaço conceitual valioso.
- **As métricas de qualidade são afirmações sem sustentação.** "Concordância com advogado sênior em pelo menos 85%" pressupõe golden set calibrado — mas o leitor não tem acesso a ele nem ao critério de seleção do advogado. A métrica parece rigorosa mas é inacessível para verificação.
- **A abertura promete mais do que entrega.** "Trinta fichas que foram desenhados como ativos de produção, com inputs reais, com riscos reais" — mas não há um caso real no apêndice. O único XML é esqueleto genérico. O leitor que veio buscando produção encontra conceito.
- **A estrutura Quando usar / Quando evitar repete padrão óbvio em excesso.** Em muitas fichas, o "Evitar" é trivialmente o inverso do "Usar" (ex: "Usar: triagem preliminar / Evitar: parecer final"). Isso ocupa espaço sem acrescentar discriminação real.
- **O apêndice não ensina o leitor a construir um prompt.** Ele ensina a usar os trinta que já estão no repositório. Isso inverte a lógica de método: o leitor que adaptar um dos 30 sem entender os princípios vai produzir prompt ruim, e o apêndice não o protege disso de forma suficiente.
- **A promessa do repositório é não-verificável no momento da leitura.** O URL aparece 30 vezes, mas se o repositório estiver vazio, com código-stub, ou diferente do prometido, toda a arquitetura colapsa. O leitor não tem como saber isso lendo o livro.

---

## ACHADOS

### ACHADO 01
**Categoria:** P0
**Problema:** Contradição estrutural com a tese central do livro.
**Por que é um problema:** A tese é "Modelos passam. Método fica." e a rubrica instrui a sinalizar explicitamente quando conteúdo transforma o livro em "coleção de prompts". Este apêndice é, na forma, uma coleção de trinta prompts categorizados por setor, com URLs para repositório. A estratégia de camada dupla *mitiga* a contradição mas não a resolve: o leitor que folheia o sumário e chega no Apêndice L vê trinta fichas com nomes como "P-LEG-01", "P-MED-02", "P-FIN-03". Isso é catálogo. A introdução argumenta contra isso, mas o leitor médio não lê introduções de apêndice.
**Impacto no leitor:** Quem chega de fora (resenha, sumário, folhear) conclui que o livro entrega receitas. Isso contradiz o posicionamento de obra de método e autoridade.
**Correção exata:** Duas opções. Opção A (cirúrgica): renomear o apêndice como "Arquitetura de Prompts Profissionais" e transformar a estrutura em três camadas — (1) princípios de design por tipo de tarefa, (2) três fichas completas como exemplos de aplicação, (3) referência para o repositório com os 27 restantes. Opção B (radical): extrair o catálogo inteiro para o repositório e deixar no livro apenas os princípios do Framework Quatro, os sete padrões de operação, os oito anti-padrões transversais e o changelog editorial. O livro ficaria mais coerente com a tese e o repositório ficaria mais completo.
**Texto sugerido:** n/a (intervenção estrutural, não textual)
**ROI:** ALTO

---

### ACHADO 02
**Categoria:** P0
**Problema:** "Modelo recomendado: Sonnet equivalente" em 26/30 fichas é afirmação sem valor informacional.
**Por que é um problema:** Se 87% das fichas têm a mesma resposta, o campo não está discriminando nada. Pior: "Sonnet equivalente" em 2026 pode ser Claude 3.5 Sonnet, GPT-4o, Gemini 1.5 Pro, Mistral Large — sem critério de equivalência definido. O que faz um modelo "equivalente"? Janela de contexto? MMLU? Benchmark jurídico específico? O campo promete especificidade e entrega generalidade.
**Impacto no leitor:** O leitor técnico (que mais usaria essa recomendação) percebe que o campo não foi preenchido com cuidado real. Reduz credibilidade do apêndice inteiro.
**Correção exata:** Ou definir "Sonnet equivalente" com critério operacional verificável na introdução da anatomia (ex: "modelo com contexto mínimo de 100k tokens, desempenho acima de X em benchmark jurídico Y, com suporte a structured output nativo"), ou substituir o campo por "Família de modelo" com três faixas: (1) Haiku equivalente — classificação/triagem de alta volumetria; (2) Sonnet equivalente — raciocínio com estrutura; (3) Sonnet com raciocínio estendido — análise jurídica/médica complexa. Apenas 8 fichas precisariam de nota diferenciada; as 22 restantes seriam "Sonnet equivalente" sem o vazio atual.
**Texto sugerido:** Na seção "A anatomia que toda ficha aplica", após a tabela do F4, adicionar: *"Convenção de modelo: ao longo das fichas, 'Sonnet equivalente' significa modelo com suporte a raciocínio estruturado, janela de contexto de 100k tokens ou mais e structured output nativo. 'Haiku equivalente' significa modelo otimizado para velocidade e custo em tarefas classificatórias de baixa complexidade semântica. A denominação é intencional para sobreviver à próxima geração de modelos — o critério, não o nome."*
**ROI:** MÉDIO

---

### ACHADO 03
**Categoria:** P0
**Problema:** As métricas de qualidade são inacessíveis para verificação independente.
**Por que é um problema:** "Concordância com advogado sênior em pelo menos 85% do golden set" — quem é o advogado sênior? Qual golden set? Com quantos casos? Calibrado como? Em qual modelo? Em que data? A métrica parece rigorosa mas é, na prática, uma afirmação de autoridade não auditável. Em um livro comparado a Superforecasting, onde calibração é central, isso é problema grave.
**Impacto no leitor:** O leitor executivo que citar essa métrica em apresentação interna vai encontrar a primeira pergunta: "de onde veio esse 85%?" e não vai ter resposta. Reduz a autoridade da obra em contexto de uso real.
**Correção exata:** Duas opções. Opção A: tornar as métricas prescrições em vez de afirmações — "Critério de qualidade que você deve exigir: concordância de pelo menos 85% com especialista sênior do domínio em um golden set de 20 casos representativos, com ao menos 5 casos limítrofes". Opção B: referenciar o golden set público no repositório, mostrando que o critério foi aplicado em condições reais documentadas. Se o repositório já tem os 20 casos calibrados, dizer isso explicitamente.
**Texto sugerido:** n/a (depende de qual opção o autor escolhe)
**ROI:** ALTO

---

### ACHADO 04
**Categoria:** P1
**Problema:** O apêndice não ensina a construir um prompt novo — apenas a usar os 30 existentes.
**Por que é um problema:** Um leitor que termina o apêndice sabe identificar qual dos 30 prompts é mais próximo do seu problema e sabe adaptar o conteúdo entre as tags (como o padrão 2 instrui). Mas se o problema do leitor for o prompt 31 — um que não está na lista — ele não sabe construir do zero. Os princípios estão dispersos (F4 na anatomia, padrões de operação, anti-padrões transversais) mas nunca são reunidos em um método explícito de construção.
**Impacto no leitor:** O leitor sai com biblioteca, não com método de biblioteca. A tese exige o contrário.
**Correção exata:** Adicionar, antes das 30 fichas, uma seção "Como construir um prompt que não está nesta lista" com 8 a 10 passos que combinam F4 + padrões de operação + anti-padrões transversais em sequência construtiva. Isso transforma o apêndice de catálogo em método com exemplos.
**Texto sugerido:** n/a (nova seção, conteúdo a criar)
**ROI:** ALTO

---

### ACHADO 05
**Categoria:** P1
**Problema:** A promessa do repositório é o ponto mais frágil do apêndice — e não há fallback declarado.
**Por que é um problema:** O apêndice é projetado como camada 1 de uma arquitetura de duas camadas. Se a camada 2 (repositório) não existir, estiver incompleta ou estiver desatualizada, o leitor que foi instruído a ir ao repositório "para a versão executável" encontra nada. Não há nota de quando o repositório foi populado, qual versão corresponde ao livro, ou o que fazer se o link estiver morto.
**Impacto no leitor:** Um leitor frustrado com repositório vazio ou desatualizado vai revisar a avaliação do livro inteiro para baixo. Em 2026, repositórios GitHub abandonados são comuns.
**Correção exata:** Adicionar no quadro de orientação da introdução uma linha explícita de SLA do repositório — ex: "Política de manutenção: o repositório é mantido ativo e com os 30 prompts populados enquanto o livro estiver em catálogo." E adicionar uma nota em cada ficha com a data de última verificação da versão executável.
**Texto sugerido:** No quadro de orientação, adicionar linha: *"Repositório público: [URL] · Política de manutenção: populado e auditado a cada release do livro. Se o link não funcionar, acesse [email/formulário alternativo]."*
**ROI:** MÉDIO

---

### ACHADO 06
**Categoria:** P1
**Problema:** A estrutura "Quando usar / Quando evitar" repete o óbvio em excesso e ocupa espaço que poderia ser usado para distinção real.
**Por que é um problema:** Em P-LEG-01: "Usar: Triagem de contratos novos / Evitar: Parecer final em litígio." Em P-LEG-02: "Usar: Revisão preliminar / Evitar: Parecer final sobre validade jurídica." Em P-LEG-04: "Usar: Auditoria interna / Evitar: Parecer técnico em contencioso." O padrão geral é "Usar para triagem / Evitar para decisão final" — que é a regra geral de todo prompt bem-desenhado, não uma característica específica de cada prompt. Apenas 8 a 10 fichas têm critérios realmente diferenciadores nessa seção.
**Impacto no leitor:** O leitor aprende a regra geral na segunda ficha e para de ler os quadros. Espaço desperdiçado que poderia ser casos de borda reais.
**Correção exata:** Transformar o campo em "Casos de borda" — situações não óbvias em que o prompt funciona melhor ou pior que o esperado. A regra geral (não use para decisão final) entra na introdução da anatomia uma única vez.
**Texto sugerido:** Substituir o cabeçalho "Quando usar e quando evitar" por "Casos de borda e limites não óbvios", e instrução ao autor para preencher apenas com situações que surpreendem — não com a regra geral.
**ROI:** MÉDIO

---

### ACHADO 07
**Categoria:** P1
**Problema:** P-MED-03 (Alerta de Interação Medicamentosa) tem risco regulatório não declarado que é estruturalmente diferente dos outros prompts de saúde.
**Por que é um problema:** Os prompts P-MED-01 e P-MED-02 são claros sobre seus limites (orientação leiga, fidelidade ao registro). P-MED-03 opera em território de decisão clínica — sinalizar "interação contraindicada" com "necessita validação farmacêutica" pode criar falsa sensação de segurança se usado fora de ambiente hospitalar supervisionado. A ficha não menciona responsabilidade regulatória do operador, CFM, CFF ou CFP, nem distingue uso hospitalar de uso em farmácia de bairro ou app de saúde B2C.
**Impacto no leitor:** Um empreendedor lendo a ficha pode construir um app de verificação de interações para consumidor final, citando o livro como base. Risco real de uso indevido.
**Correção exata:** Adicionar em "Quando evitar": "Uso B2C direto ao consumidor sem supervisão farmacêutica — regulatoriamente restrito no Brasil (CFF). Uso em prescrição pediátrica sem ajuste etário validado por farmacêutico. Ambiente fora de estabelecimento de saúde regulado."
**Texto sugerido:** *"Este prompt é desenhado para uso institucional sob supervisão farmacêutica, não para acesso direto do paciente. O uso em app B2C sem farmacêutico responsável configura, no Brasil, exercício irregular de atividade farmacêutica (CFF)."*
**ROI:** ALTO

---

### ACHADO 08
**Categoria:** P1
**Problema:** P-FIN-02 (Risco de Crédito PF) não menciona a Resolução CMN 4.557/2017 e a necessidade de explicabilidade do modelo de crédito exigida pelo BACEN.
**Por que é um problema:** Em 2026, instituições financeiras sob regulação BACEN precisam de sistemas de crédito com grau explicável de tomada de decisão. O prompt entrega classificação com fatores determinantes, o que é positivo — mas não menciona que o uso do output precisa ser documentado de forma que permita contestação pelo cliente (direito de conhecer a razão de recusa, previsto na LGPD art. 20 e nas normas BACEN). Um DPO lendo a ficha deveria ser alertado disso.
**Impacto no leitor:** O leitor de fintech que adotar o prompt sem essa nota pode estar em não-conformidade regulatória sem saber.
**Correção exata:** Adicionar em "Anti-padrões observados": "Usar o output sem registro auditável do fator determinante — o direito do titular à explicação da decisão de crédito está previsto na LGPD art. 20 e em normas BACEN."
**Texto sugerido:** n/a (adição pontual na lista de anti-padrões)
**ROI:** ALTO

---

### ACHADO 09
**Categoria:** P1
**Problema:** O Changelog editorial trata apenas seis prompts e está no final do apêndice, depois das 30 fichas.
**Por que é um problema:** O Changelog é o conteúdo mais valioso do apêndice do ponto de vista da tese. Ele mostra método de iteração, não produto final. Mas 96% dos leitores nunca vão chegar lá — estão na página 1600 de um apêndice que começa na 1. E os 24 prompts sem changelog aparecem como se tivessem saído prontos, sem cicatriz de iteração.
**Impacto no leitor:** A narrativa implícita dos 24 prompts sem changelog é "este prompt é definitivo". Isso contradiz os padrões de operação (reverifique ao trocar de modelo) e a filosofia do apêndice.
**Correção exata:** Mover o Changelog para a introdução, antes das fichas, como "O que este apêndice aprendeu" — e expandir para 10 a 12 casos. Isso ancora metodologicamente todo o catálogo antes de o leitor entrar nas fichas.
**Texto sugerido:** n/a (reorganização estrutural)
**ROI:** ALTO

---

### ACHADO 10
**Categoria:** P1
**Problema:** Nenhuma ficha menciona o comportamento esperado quando o modelo recusa a tarefa por política de conteúdo.
**Por que é um problema:** Em contextos reais de produção, modelos recusam tarefas. P-MED-03 (interações medicamentosas) e P-LEG-03 (M&A) são exemplos onde provedores como Anthropic ou OpenAI podem inserir recusas não esperadas dependendo de como o input chega. Nenhuma ficha instrui o operador sobre o que fazer quando isso acontece — rewrite do prompt? Fallback para humano? Log de recusa?
**Impacto no leitor:** Em produção, a primeira recusa inesperada quebra o pipeline e o operador não tem guia.
**Correção exata:** Adicionar um oitavo padrão de operação: "Mantenha registro de recusas do modelo por categoria de input. Uma taxa de recusa acima de N% em uma categoria específica indica ou ambiguidade no prompt ou mudança de política do modelo — ambos exigem ação."
**Texto sugerido:** *"8. Monitore recusas por categoria. Quando o modelo recusar a tarefa — seja por policy de conteúdo, seja por input fora do escopo da constituição — registre o motivo literal da recusa, o input que a gerou e o modelo/versão em uso. Taxa de recusa acima de 5% numa categoria específica é sinal de alarme que exige revisão da constituição ou do contexto."*
**ROI:** MÉDIO

---

### ACHADO 11
**Categoria:** P1
**Problema:** P-RH-01 (Triagem de Currículo) não menciona a exigência de auditoria de viés algorítmico que é tendência regulatória clara no Brasil e global.
**Por que é um problema:** Em 2026, recrutamento algorítmico está sob escrutínio crescente da ANPD e de tribunais trabalhistas. O prompt instrui a não usar variáveis vedadas, o que é correto, mas não instrui o operador a manter log de decisões de triagem com auditoria de viés — exigência provável em horizonte de 1 a 2 anos no Brasil, já presente na EU AI Act para sistemas de alto risco em emprego.
**Impacto no leitor:** Uma empresa que usar o prompt sem log auditável pode ter problema regulatório não antecipado.
**Correção exata:** Adicionar em "Anti-padrões observados": "Não manter log auditável de triagens realizadas com variáveis e pontuação registradas — em domínio regulado, auditoria de viés algorítmico exige rastreabilidade completa."
**Texto sugerido:** n/a (adição pontual)
**ROI:** MÉDIO

---

### ACHADO 12
**Categoria:** P2
**Problema:** A introdução usa o verbo "materializa" para descrever o Princípio Três (Camada Dupla), mas o Princípio Três não é identificado em lugar algum no texto com esse número ou nome.
**Por que é um problema:** "Essa separação é deliberada e materializa o Princípio Três, a Camada Dupla." Se o leitor não passou pelo capítulo onde esse princípio é definido — ou se o leitor lê o apêndice isoladamente — a referência flutua sem ancoragem.
**Impacto no leitor:** Leve desorientação. Joana não sabe o que é o Princípio Três.
**Correção exata:** Adicionar entre parênteses ou como nota de rodapé: "(ver Capítulo X)".
**Texto sugerido:** *"...materializa o Princípio Três, a Camada Dupla (Capítulo X)."*
**ROI:** BAIXO

---

### ACHADO 13
**Categoria:** P2
**Problema:** O campo "Versão executável" em cada ficha tem formato de link markdown mas é referência de repositório que pode ou não estar ativa. Em formato impresso ou PDF estático, o link não é clicável e o URL é longo.
**Por que é um problema:** "prompts/P-LEG-01-clausula-nao-concorrencia-clt" — em formato impresso, o leitor precisa digitar a URL base mais o caminho. Nenhum QR code ou URL encurtado é oferecido.
**Impacto no leitor:** Fricção de acesso em formato não-digital.
**Correção exata:** Adicionar uma URL base única ao início do apêndice: "github.com/falercia/inteligencia-aumentada-recursos" e nos campos de versão executável usar apenas o identificador curto: "P-LEG-01".
**Texto sugerido:** n/a (simplificação de formato)
**ROI:** BAIXO

---

### ACHADO 14
**Categoria:** P2
**Problema:** P-MKT-01 (Copy A/B Testável) menciona "Google Ads, Meta Ads, e-mail, LinkedIn, in-app" — todos com limites de caracteres distintos que mudam frequentemente.
**Por que é um problema:** Os limites de caracteres do Google Ads, Meta e LinkedIn são atualizados periodicamente pelas plataformas. Qualquer referência a esses limites no livro impresso envelhece no próximo ciclo de atualização das plataformas.
**Impacto no leitor:** Limite de 30 caracteres no headline do Google Ads hoje pode ser 40 amanhã. O livro fica errado.
**Correção exata:** O campo "Contexto" da ficha já instrui a incluir "limite de caracteres" como variável dinâmica — isso está correto. Mas o texto da ficha não deveria mencionar canais específicos como se fossem estáticos. Substituir a lista por "canais digitais com limite declarado pelo operador".
**Texto sugerido:** *"Domínio: copy para canais digitais com limite de caracteres declarado pelo operador. O prompt recebe o limite como variável dinâmica, sem assumir padrão fixo por plataforma — os limites mudam com frequência e o repositório mantém referência atualizada."*
**ROI:** BAIXO

---

## TESTE DA JOANA
**Entenderia:** PARCIALMENTE
**O que ela entenderia:** A estrutura geral — que existem 30 fichas organizadas por setor, que cada uma diz o que o prompt faz e quando usar. Ela conseguiria ir diretamente à seção de interesse (jurídico, RH) e ler a ficha em 90 segundos como prometido.
**O que ela NÃO entenderia:** O que é o Framework Quatro (F4) e por que importa a ordem das tags XML. A tabela da anatomia (persona, constituição, contexto, tarefa, formato_saida) pressupõe que o leitor já entende o que é um prompt de sistema — Joana pode não saber. A diferença entre "presença com risco" e "ausente" em P-LEG-01 (elementos do TST) é técnico-jurídica sem explicação. A instrução de "verificar contra golden set ao trocar de modelo" não é explicada para quem não sabe o que é regressão automatizada.
**Como corrigir:** Adicionar um glossário de três termos na introdução da anatomia: golden set (o que é, por que importa), constituição do prompt (analogia ao edital — regras que não podem ser violadas), e self-critique (por que o modelo precisa se revisar antes de devolver). Três parágrafos de 3 linhas cada são suficientes.

---

## TESTE DE DURABILIDADE
**Classificação:** MÉDIA
**2 anos:** As fichas conceituais sobrevivem bem. Os padrões de operação e anti-padrões transversais sobrevivem bem. Os campos "Modelo recomendado" envelhecem já em 2026-2027 quando a próxima geração de modelos chegar.
**5 anos:** A estrutura F4 (persona/constituição/contexto/tarefa/formato) é durável enquanto LLMs continuarem operando com system prompt. Se a interface mudar radicalmente (ex: agentes sem prompt estruturado), parte da anatomia fica obsoleta.
**10 anos:** Incerto. Os princípios (separar instrução de dado, manter golden set, versionar) provavelmente sobrevivem. A especificidade regulatória (CLT, TST, LGPD) pode mudar com reformas legislativas.
**Justificativa:** O que mais envelhece: nomes de modelos ("Sonnet equivalente"), referências a plataformas (Google Ads, Meta), número de prompts (trinta — qualquer revisão do livro precisa atualizar este número). O que menos envelhece: a lógica de camada dupla, os sete padrões de operação, o changelog editorial como prática, a anatomia F4.

---

## TESTE DE DIFERENCIAÇÃO
**Classificação:** DIFERENCIADO (com asterisco)
**Justificativa:** A especificidade regulatória brasileira (LGPD, CLT, ITR, ANPD, BACEN, CFF) é genuinamente diferenciadora — não existe equivalente com esse nível de aterramento em publicações de língua inglesa. A estratégia de camada dupla (livro + repositório) também é diferenciadora como arquitetura editorial. O asterisco: na *forma* de catálogo, o apêndice é commodity (listas de prompts por setor existem aos milhares no internet). A diferenciação está na *profundidade* de cada ficha — mas o leitor médio que folheia não percebe a profundidade antes de decidir se o livro é relevante para ele.

---

## TESTE DE MEMORIZAÇÃO
**Ideia principal clara?** NÃO
**Qual é a ideia principal (em 1 frase):** Não é possível responder em 1 frase — o apêndice tem duas ideias em tensão: "aqui está como construir prompts duráveis" (método) e "aqui estão 30 prompts prontos" (catálogo).
**Justificativa:** O leitor que sai do apêndice lembra das fichas, não do método. A ideia mais memorável acaba sendo a estrutura F4 (persona/constituição/contexto/tarefa/formato) — mas ela está enterrada na introdução e não é repetida nas fichas de forma a reforçar o conceito. O Changelog editorial é a segunda coisa mais memorável — e está no final.

---

## TESTE DE TRANSFORMAÇÃO
**Ao terminar, o leitor consegue fazer o que antes não conseguia:**
- Identificar qual dos 30 prompts é mais adequado para um problema específico e adaptar o contexto para o seu cenário
- Estruturar um prompt com os cinco blocos F4 na ordem correta e com separação clara entre instrução e dado
- Montar um golden set básico para testar regressão quando o modelo for atualizado
- Reconhecer os oito anti-padrões transversais na revisão de um prompt existente
- Interpretar o changelog editorial de um prompt como evidência de maturidade operacional, não de falha

**O que o leitor ainda NÃO consegue fazer (problema não resolvido):**
- Construir um prompt novo que não seja adaptação de um dos 30 — o apêndice não ensina design from scratch
- Avaliar se um modelo específico é adequado para uma tarefa específica sem depender do campo "Modelo recomendado" (que é vago)
- Calcular o custo real de operacionalizar um prompt em produção (falta integração com Apêndice J, mencionado no quadro de orientação mas não referenciado em nenhuma ficha individualmente)

---

## NOTA FINAL (0-10 cada eixo)
Estrutura: 7 | Pedagogia: 5 | Clareza: 7 | Autoridade: 6 | Durabilidade: 6 | Diferenciação: 7 | Memorização: 5 | Transformação: 6
**Nota Geral: 6**

## DECISÃO EDITORIAL
**REVISAR PARCIALMENTE**

Prioridade 1: Resolver a contradição com a tese (Achado 01) — seja pela Opção A (compactar para 3 fichas exemplo + repositório) ou pela Opção B (extrair o catálogo, manter o método).
Prioridade 2: Tornar as métricas de qualidade verificáveis ou transformá-las em prescrições (Achado 03).
Prioridade 3: Mover o Changelog para a abertura (Achado 09) — isso custa zero e eleva o apêndice de catálogo para método com cicatriz.
O apêndice tem material genuinamente bom disperso em uma estrutura que o posiciona errado. A revisão não precisa ser de volume — precisa ser de arquitetura.

---

---

# APX-P — Boxes Técnicos

## RESUMO EXECUTIVO
Nota: 8/10
Veredito: A

---

## O QUE FUNCIONA

- **A estrutura de sete blocos por box é exemplarmente consistente e pedagogicamente eficaz.** Por que existe / Conceito intuitivo / Analogia / Mecanismo técnico / Implicação executiva / Quando importa para o leitor brasileiro / Onde aprofundar — essa sequência não foi escolhida por decoração. Ela vai do "preciso me preocupar?" ao "o que isso muda na minha decisão" sem saltar etapas.
- **As analogias são genuinamente boas.** A consultoria com 200 especialistas para MoE, o sócio sênior revisando o estagiário para Speculative Decoding, o auditor com planilha lateral para KV Cache, o cozinheiro com despensa para FlashAttention — cada uma captura a propriedade estruturalmente relevante da técnica sem falsificar a mecânica.
- **A seção "Quando importa para o leitor brasileiro" é propriedade intelectual real.** Nenhum livro em inglês conecta MoE a deploy on-prem em fintechs reguladas brasileiras, FlashAttention a análise de contratos de M&A em português, ou quantização a servidores DGX herdados de datacenters brasileiros. Esse aterramento é diferenciador genuíno.
- **O Box 11 (Matriz de Interações) é o melhor conteúdo técnico do apêndice.** A matriz triangular com os três tipos de relação (sinergia, trade-off, conflito) e os oito pares aprofundados resolve exatamente o problema que o Box 11 identifica: "a decisão real vive nas zonas de fricção entre conceitos". Especialmente as interações 4 (Speculative Decoding × Reasoning Models), 6 (Structured Output × Faithfulness de CoT) e 7 (Mech Interp × Quantização) são conteúdo não encontrável em forma tão acessível na literatura.
- **As referências primárias são precisas e verificáveis.** Os papers citados têm autores, ano, venue e URL de arXiv — padrão comparável a Co-Intelligence e Designing Data-Intensive Applications. Isso constrói autoridade.
- **A precisão técnica é alta para um livro de negócios.** A descrição de grammar-constrained decoding, o algoritmo de speculative sampling com correção de distribuição, a fórmula de crescimento do KV cache, a lógica de superposição em sparse autoencoders — tudo está tecnicamente correto ao nível de profundidade escolhido.
- **O tom "implicação executiva" é calibrado.** Em nenhum momento o apêndice cai no erro oposto de subestimar o leitor — as implicações são concretas, prescritivas e diretamente acionáveis sem ser simplistas.

---

## O QUE NÃO FUNCIONA

- **Box 4 (FlashAttention) menciona "Claude 4 Sonnet" como exemplo de modelo com contexto longo** — nome que não existe no portfólio da Anthropic até a data desta revisão. É erro factual que compromete credibilidade.
- **Box 10 (Scaling Laws) é o mais frágil** porque sua "implicação executiva" central — platô em modelos frontier — é a afirmação mais dependente de data de todos os boxes. Se a próxima geração de modelos produzir salto de qualidade relevante, toda a seção sobre "retorno marginal decrescente" precisa ser reescrita.
- **A Interação 3 (FlashAttention × Scaling Laws) no Box 11 contém um non sequitur**: a lógica salta de "FlashAttention torna viável aumentar contexto" para "scaling laws em platô" como se a segunda fosse consequência da primeira. Não são causalmente conectados da forma que o texto sugere.
- **Box 9 (Interpretabilidade Mecanicista) é ligeiramente mais longo que os outros** sem justificativa pedagógica — o mecanismo técnico tem três frentes (superposição, attribution graphs, monossemanticidade) que poderiam ser comprimidas sem perda para o leitor executivo.
- **O Box 11 usa emojis (🔴🟢🟡⚪) na matriz** — em versão impressa em preto e branco, as cores são invisíveis e a tabela perde toda a informação visual. Não há legenda textual alternativa para impressão monocromática.

---

## ACHADOS

### ACHADO 01
**Categoria:** P0
**Problema:** Box 4 cita "Claude 4 Sonnet" como exemplo de modelo com janela de contexto longa.
**Por que é um problema:** "Claude 4 Sonnet" não é um modelo existente no portfólio da Anthropic em junho de 2026. O portfólio atual inclui Claude 3.5 Sonnet, Claude 3 Opus, Claude 3 Haiku e variantes do Claude 3.5/3.7. Citar um modelo inexistente num livro de autoridade técnica é erro factual que será notado imediatamente por qualquer leitor técnico.
**Impacto no leitor:** Reduz credibilidade de todo o apêndice — se o autor errou o nome de um modelo da Anthropic (a empresa que publica o livro), o que mais pode estar errado?
**Correção exata:** Verificar o portfólio atual da Anthropic, substituir "Claude 4 Sonnet" pelo modelo correto ou remover o nome e usar apenas "Claude (versão atual)" para preservar durabilidade.
**Texto sugerido:** *"...janelas de contexto de duzentos mil a um milhão de tokens, que aparecem como spec sheet em Gemini 1.5, Claude 3.5 Sonnet e GPT-4 Turbo, não foram resultado de uma descoberta teórica..."* (verificar versão correta do Claude antes de publicar)
**ROI:** ALTO

---

### ACHADO 02
**Categoria:** P0
**Problema:** Box 10 (Scaling Laws) tem sua implicação executiva central construída sobre um estado de facto extremamente frágil.
**Por que é um problema:** "A expectativa de que próximas gerações de modelos serão dramaticamente melhores apenas por escala bruta deve ser calibrada para baixo" — essa afirmação estava correta em 2024-2025, mas o campo de IA tem histórico de invalidar conclusões de platô com velocidade surpreendente (GPT-4 apareceu depois de meses de debate sobre limites de GPT-3). O livro está sendo escrito para sobreviver, mas a implicação executiva do Box 10 pode ser invalidada antes do fim do primeiro ciclo de vendas.
**Impacto no leitor:** Um executivo que tomar decisão de stack baseado em "platô de qualidade nos próximos 3 anos" e encontrar GPT-5 ou Claude 4 com salto de qualidade relevante vai associar o livro a conselho errado.
**Correção exata:** Reescrever a implicação executiva para ser epistemicamente honesta sobre a incerteza: "Historicamente, previsões de platô em IA têm sido invalidadas. A regra mais segura é arquitetar para capturar ganhos incrementais certos hoje, enquanto mantém arquitetura suficientemente modular para absorver saltos de qualidade imprevistos. Isso é diferente de apostar em salto — ou em platô."
**Texto sugerido:** *"A regra prática para quem decide em 2026 não é assumir platô nem assumir salto: é desenhar arquitetura que extrai valor dos modelos atuais com elegância e pode ser atualizada com custo baixo quando — não se — a fronteira mover. Os ganhos por geração estão se tornando mais dependentes de inovações em dados e arquitetura do que de escala bruta, mas a velocidade dessas inovações não é previsível com a precisão que uma decisão de investimento exige."*
**ROI:** ALTO

---

### ACHADO 03
**Categoria:** P1
**Problema:** A Interação 3 (FlashAttention × Scaling Laws) no Box 11 conecta causalmente dois fenômenos que são correlatos, não causais.
**Por que é um problema:** O texto afirma que FlashAttention "amplifica scaling laws" e depois conclui que "investir na ponta da escala virou aposta com retorno marginal decrescente". Mas o platô em scaling laws não é causado por FlashAttention — é causado por esgotamento de dados de alta qualidade e pela curva de retorno de parâmetros. FlashAttention e scaling laws são fenômenos independentes que o Box 11 conecta de forma que sugere causalidade onde há apenas co-ocorrência temporal.
**Impacto no leitor:** O leitor técnico que conhece ambos os fenômenos percebe o erro lógico e questiona a qualidade da análise das outras interações.
**Correção exata:** Separar os dois fenômenos. FlashAttention permite contextos longos com custo controlado — isso é sinergia com qualquer escala que use contexto longo. O platô em scaling laws tem causa independente (dados, não compute). Reescrever a interação para refletir isso.
**Texto sugerido:** *"FlashAttention torna economicamente viável o que parecia computacionalmente proibitivo em contextos longos. O platô observado em qualidade de modelos frontier desde 2024, porém, não é consequência de FlashAttention — é consequência do esgotamento de dados humanos de alta qualidade e do retorno decrescente de parâmetros além de certo limiar. Para o decisor, essas são duas alavancas diferentes: FlashAttention reduz custo por token gerado em contextos longos (sinergia com contextos ricos), enquanto a curva de scaling informa que comprar mais parâmetros rende menos por dólar. Otimize as duas de forma independente."*
**ROI:** MÉDIO

---

### ACHADO 04
**Categoria:** P1
**Problema:** Box 1 (MoE) menciona "tiebreak leakage (Hayes et al., outubro de 2024)" como risco de segurança — mas não informa se esse risco foi mitigado nos modelos frontier atuais.
**Por que é um problema:** Em 2026, provedores como Anthropic e OpenAI rodam modelos MoE em ambientes multi-tenant com isolamento. Se o tiebreak leakage foi mitigado nos serving stacks dos provedores principais, mencionar ele sem atualização de status cria alarme desnecessário e pode dissuadir o leitor de adotar MoE por razão que já não existe.
**Impacto no leitor:** Um CISO que leia este box pode bloquear adoção de MoE por risco que já foi mitigado no provedor que estava considerando.
**Correção exata:** Adicionar após a descrição do risco: "Em ambientes de API pública, esses riscos são gerenciados pelos provedores na camada de serving. Para deploys on-prem com modelo open weights, o risco permanece relevante e exige isolamento explícito de batch entre tenants."
**Texto sugerido:** *"Os riscos de tiebreak leakage e expert silencing são relevantes principalmente em deploy on-prem e em ambientes multi-tenant gerenciados diretamente pelo operador. Em APIs gerenciadas pelos provedores frontier, o isolamento de batch e o monitoramento de serving são responsabilidade do provedor — embora valha confirmar com o fornecedor quais salvaguardas estão em vigor antes de processar dados sensíveis em ambiente compartilhado."*
**ROI:** MÉDIO

---

### ACHADO 05
**Categoria:** P1
**Problema:** Box 11 usa emojis coloridos (🔴🟢🟡⚪) como única codificação da matriz de interações. Em impressão monocromática, todos os símbolos ficam visualmente idênticos.
**Por que é um problema:** Um livro técnico sério publicado em versão impressa não pode ter sua informação central (a matriz de interações do Box 11 é o coração do apêndice) depender de renderização colorida para ser legível.
**Impacto no leitor:** Em formato impresso em escala de cinza — como muitas impressões de e-book ou cópia física de baixo custo — a matriz é ilegível.
**Correção exata:** Substituir os emojis por marcadores textuais com legenda dupla. Exemplo: C (conflito), S (sinergia), T (trade-off), N (neutro). Manter os emojis como complemento visual, não como única codificação.
**Texto sugerido:** Substituir cabeçalho da legenda para: "C = conflito / S = sinergia / T = trade-off / N = neutro" e adicionar coluna de legenda equivalente na matriz.
**ROI:** MÉDIO

---

### ACHADO 06
**Categoria:** P1
**Problema:** Box 8 (Faithfulness de CoT) menciona "trabalho de seguimento sobre intervenções causais em CoT, 2024-2025" na seção "Onde aprofundar" sem citar paper específico.
**Por que é um problema:** A seção de referências de todos os outros boxes cita papers com autores, título, venue e URL. A referência vaga "trabalho de seguimento, 2024-2025" quebra o padrão e deixa o leitor sem caminho de aprofundamento real.
**Impacto no leitor:** O leitor técnico que quiser se aprofundar nessa linha específica (que é a mais recente e a mais relevante para aplicação prática) não tem onde ir.
**Correção exata:** Substituir a referência vaga por pelo menos dois papers específicos de 2024-2025 sobre faithfulness de CoT ou causal CoT training. Se nenhum paper específico existir, remover a referência e adicionar: "Esta linha de pesquisa está em desenvolvimento ativo; acompanhe publicações do ACL 2024-2025 e EMNLP 2024."
**Texto sugerido:** n/a (requer pesquisa de papers específicos)
**ROI:** BAIXO

---

### ACHADO 07
**Categoria:** P1
**Problema:** Box 5 (LoRA e PEFT) menciona "S-LoRA" (serving multi-tenant com dezenas de adaptadores) sem citar a referência primária.
**Por que é um problema:** S-LoRA foi formalizado em paper específico (Sheng et al., 2023). Todos os outros conceitos têm referência primária — S-LoRA é citado em passagem de texto sem ancoragem bibliográfica.
**Impacto no leitor:** Leitor que quiser implementar S-LoRA em produção não tem onde começar.
**Correção exata:** Adicionar na seção "Onde aprofundar" do Box 5: "S-LoRA: Sheng et al. *'S-LoRA: Serving Thousands of Concurrent LoRA Adapters'*. 2023. → arxiv.org/abs/2311.03285."
**Texto sugerido:** n/a (adição de referência)
**ROI:** BAIXO

---

### ACHADO 08
**Categoria:** P2
**Problema:** Box 6 (Quantização e Destilação) menciona "Phi-3, da Microsoft" e "Gemini Nano" como exemplos de modelos destilados — mas não menciona DeepSeek-R1-Distill, que é o caso mais relevante de destilação em 2025 e o mais próximo do público-alvo brasileiro (open weights, custo baixo).
**Por que é um problema:** Phi-3 e Gemini Nano são exemplos corretos mas datados. DeepSeek-R1-Distill demonstrou capacidade de reasoning próxima a modelos frontier em modelo destilado de 7B — caso muito mais impactante para a implicação executiva do box.
**Impacto no leitor:** O leitor de fintech ou jurídico que decide entre modelos open weights em 2026 tem DeepSeek como referência primária, não Phi-3.
**Correção exata:** Adicionar DeepSeek-R1-Distill como exemplo na seção de mecanismo técnico e incluir referência correspondente.
**Texto sugerido:** *"...Modelos como Phi-3, da Microsoft, Gemini Nano e a família DeepSeek-R1-Distill são exemplos públicos de modelos pequenos treinados com destilação intensiva a partir de modelos maiores, atingindo qualidade impressionante para seu tamanho — em particular em tarefas de raciocínio estruturado."*
**ROI:** BAIXO

---

### ACHADO 09
**Categoria:** P2
**Problema:** A epígrafe final do apêndice ("Cada um destes boxes existe porque algum executivo, em algum lugar, tomou uma decisão de stack sem saber o que estava escolhendo") é o único momento de voz autoral no texto — e está em formato de nota de rodapé em itálico no final.
**Por que é um problema:** É a frase mais memorável do apêndice inteiro e está enterrada onde ninguém vai encontrá-la.
**Impacto no leitor:** Desperdício de conteúdo. Se essa frase estivesse na abertura, mudaria o enquadramento de como o leitor leria os boxes.
**Correção exata:** Mover essa frase para a abertura do apêndice ("Como usar este apêndice"), como primeira frase ou última frase do primeiro parágrafo.
**Texto sugerido:** Mover como está: *"Cada um destes boxes existe porque algum executivo, em algum lugar, tomou uma decisão de stack sem saber o que estava escolhendo. Que a próxima decisão seja melhor informada."*
**ROI:** BAIXO

---

### ACHADO 10
**Categoria:** P2
**Problema:** O "Mapa de boxes" na tabela inicial referencia princípios como "P5 — Custo Composto" e "P7 — Termômetro" sem que o leitor saiba onde esses princípios estão definidos.
**Por que é um problema:** Um leitor que chega ao Apêndice P sem ter lido os capítulos 1-3 (como a introdução admite que pode acontecer) não sabe o que é "P1 — Plausibilidade" ou "P2 — Extremidades". A tabela assume familiaridade com nomenclatura interna da obra.
**Impacto no leitor:** Joana, lendo o mapa antes dos boxes, não consegue usar a coluna "Princípio relacionado" como orientação.
**Correção exata:** Adicionar nota de rodapé abaixo da tabela: "Os Princípios (P1 a P9) são definidos no Capítulo X e resumidos no Apêndice Y."
**Texto sugerido:** n/a (adição de nota)
**ROI:** BAIXO

---

## TESTE DA JOANA
**Entenderia:** PARCIALMENTE (melhor do que o Apêndice L)
**O que ela entenderia:** As analogias funcionam muito bem para Joana. A consultoria com especialistas (MoE), o sócio revisando o estagiário (Speculative Decoding), o auditor com planilha lateral (KV Cache) — todas são precisas e acessíveis sem background técnico. As implicações executivas são claramente escritas para ela. A seção "Quando importa para o leitor brasileiro" fala diretamente ao seu contexto.
**O que ela NÃO entenderia:** O mecanismo técnico de cada box vai além do que Joana precisa. "Softmax sobre top-K scores", "KL divergence sobre logits suavizados", "SRAM vs HBM" — esses termos aparecem sem glossário. Joana provavelmente pularia a seção de mecanismo técnico de cada box, e isso é aceitável — mas não está explicitamente autorizado no texto. O Box 11 (Matriz) seria difícil para Joana sem guia de leitura.
**Como corrigir:** Adicionar na abertura: "Se você é executivo não-técnico, leia Por que este box existe, Conceito intuitivo, Analogia e Implicação executiva em cada box. Pule o Mecanismo técnico na primeira leitura. Se precisar defender a decisão para um time de engenharia, volte ao mecanismo." Isso é permissão explícita para Joana navegar como precisa.

---

## TESTE DE DURABILIDADE
**Classificação:** ALTA (com ressalva no Box 10)
**2 anos:** Todos os boxes exceto Box 10 (Scaling Laws) sobrevivem bem. Os mecanismos descritos (MoE, speculative decoding, KV cache, FlashAttention, LoRA, quantização, structured output) são suficientemente estáveis para não mudar em dois anos.
**5 anos:** A maioria sobrevive. Risco médio em Box 9 (Interpretabilidade Mecanicista) — se a pesquisa avançar muito, o estado da arte descrito pode estar ultrapassado. Box 4 (FlashAttention) tem risco baixo de ser supersedido por outra técnica de IO-awareness.
**10 anos:** Incerto mas melhor que a média. Os conceitos (atenção, cache, roteamento, quantização) são mais duráveis que nomes de modelos. A questão é se a arquitetura transformer permanecerá dominante — se sim, quase tudo sobrevive.
**Justificativa:** O que mais envelhece: o nome "Claude 4 Sonnet" no Box 4 (já está errado), os exemplos de modelos específicos em Box 6 (Phi-3, Gemini Nano), a análise de platô no Box 10. O que menos envelhece: as analogias (nenhuma depende de modelo), os mecanismos técnicos dos boxes 1-4, a lógica de LoRA, a estrutura da matriz de interações.

---

## TESTE DE DIFERENCIAÇÃO
**Classificação:** PROPRIEDADE INTELECTUAL
**Justificativa:** Box 11 (Matriz de Interações) não existe em nenhuma outra publicação com esse nível de detalhe e aplicabilidade executiva. A combinação de "mecanismo técnico preciso + analogia acessível + implicação executiva brasileira" em cada box é formato que não encontra equivalente em livros de IA de negócios existentes. O apêndice como um todo está mais próximo de Designing Data-Intensive Applications (Kleppmann) em profundidade e aplicabilidade do que de qualquer livro de "IA para executivos" publicado em português.

---

## TESTE DE MEMORIZAÇÃO
**Ideia principal clara?** SIM
**Qual é a ideia principal (em 1 frase):** "Cada técnica arquitetural tem uma implicação executiva específica que muda o que você deve perguntar ao fornecedor antes de decidir o stack."
**Justificativa:** Essa ideia está presente em cada box e no Box 11, e é memorável porque é acionável. O leitor sai com 10 perguntas novas para fazer ao fornecedor — o que é exatamente o que um livro de método deve produzir.

---

## TESTE DE TRANSFORMAÇÃO
**Ao terminar, o leitor consegue fazer o que antes não conseguia:**
- Distinguir parâmetros totais de parâmetros ativos em MoE e fazer a pergunta certa ao comparar modelos
- Exigir do fornecedor informação sobre speculative decoding e avaliar o ganho real de latência
- Dimensionar memória GPU com KV cache em mente, não apenas com tamanho de pesos
- Entender por que contexto longo ficou barato (FlashAttention) e redesenhar arquitetura de RAG em consequência
- Avaliar LoRA como opção de roadmap de produto, não apenas de pesquisa
- Distinguir garantia sintática de garantia semântica em structured output e aplicar a implicação correta
- Tratar chain of thought como narrativa auditável, não como prova de raciocínio
- Planejar capacidade de auditoria não-quantizada quando mech interp for exigida por regulador
- Calibrar expectativa de ganho de qualidade por geração de modelo com base na análise de scaling laws
- Identificar o par dominante de conceitos no próprio produto e otimizar nessa ordem

---

## NOTA FINAL (0-10 cada eixo)
Estrutura: 9 | Pedagogia: 8 | Clareza: 8 | Autoridade: 8 | Durabilidade: 8 | Diferenciação: 9 | Memorização: 8 | Transformação: 9
**Nota Geral: 8**

## DECISÃO EDITORIAL
**MANTER COM AJUSTES**

Prioridade 1: Corrigir "Claude 4 Sonnet" (Achado 01) — erro factual imediato.
Prioridade 2: Reescrever a implicação executiva do Box 10 para ser epistemicamente honesta sobre incerteza de platô (Achado 02).
Prioridade 3: Corrigir a lógica causal da Interação 3 do Box 11 (Achado 03).
O restante são melhorias de detalhe. Este é o conteúdo mais forte dos apêndices revisados — mais próximo do padrão de comparação estabelecido pela rubrica.

---

---

## LINHAS-TRACKER

```
APX-L|L1-APX-L-biblioteca-prompts.md|01|P0|ALTO|Contradição estrutural: apêndice é catálogo que a tese proíbe|Restruturar como método com exemplos ou extrair catálogo para repositório|REVISAR PARCIALMENTE
APX-L|L1-APX-L-biblioteca-prompts.md|02|P0|MÉDIO|"Sonnet equivalente" em 26/30 fichas sem critério de equivalência|Definir critério operacional de equivalência na introdução da anatomia|REVISAR PARCIALMENTE
APX-L|L1-APX-L-biblioteca-prompts.md|03|P0|ALTO|Métricas de qualidade inacessíveis para verificação independente|Transformar em prescrições ou referenciar golden set público no repositório|REVISAR PARCIALMENTE
APX-L|L1-APX-L-biblioteca-prompts.md|04|P1|ALTO|Apêndice não ensina a construir prompt novo — apenas a usar os 30|Adicionar seção "Como construir um prompt que não está nesta lista"|REVISAR PARCIALMENTE
APX-L|L1-APX-L-biblioteca-prompts.md|05|P1|MÉDIO|Promessa do repositório não-verificável e sem fallback declarado|Adicionar política de manutenção e canal alternativo se URL falhar|MANTER COM AJUSTES
APX-L|L1-APX-L-biblioteca-prompts.md|06|P1|MÉDIO|Quando usar/evitar repete o óbvio — regra geral disfarçada de especificidade|Substituir por "Casos de borda e limites não óbvios"|MANTER COM AJUSTES
APX-L|L1-APX-L-biblioteca-prompts.md|07|P1|ALTO|P-MED-03 sem aviso de restrição regulatória B2C (CFF)|Adicionar nota de uso restrito a ambiente institucional supervisionado|MANTER COM AJUSTES
APX-L|L1-APX-L-biblioteca-prompts.md|08|P1|ALTO|P-FIN-02 sem menção à exigência de explicabilidade BACEN/LGPD art. 20|Adicionar anti-padrão: output sem registro auditável do fator determinante|MANTER COM AJUSTES
APX-L|L1-APX-L-biblioteca-prompts.md|09|P1|ALTO|Changelog editorial no final — conteúdo mais valioso enterrado na pág. 1600|Mover Changelog para a abertura, antes das fichas, como âncora metodológica|MANTER COM AJUSTES
APX-L|L1-APX-L-biblioteca-prompts.md|10|P1|MÉDIO|Nenhuma ficha menciona comportamento quando modelo recusa por policy|Adicionar 8º padrão de operação sobre monitoramento de recusas|MANTER COM AJUSTES
APX-L|L1-APX-L-biblioteca-prompts.md|11|P1|MÉDIO|P-RH-01 sem menção à auditoria de viés algorítmico exigida por regulação emergente|Adicionar anti-padrão: ausência de log auditável de triagens com variáveis|MANTER COM AJUSTES
APX-L|L1-APX-L-biblioteca-prompts.md|12|P2|BAIXO|"Princípio Três, a Camada Dupla" sem referência ao capítulo onde é definido|Adicionar "(ver Capítulo X)" na referência|MANTER COM AJUSTES
APX-L|L1-APX-L-biblioteca-prompts.md|13|P2|BAIXO|URL de repositório longa — inacessível em formato impresso|Usar URL base única + identificador curto por ficha|MANTER COM AJUSTES
APX-L|L1-APX-L-biblioteca-prompts.md|14|P2|BAIXO|P-MKT-01 menciona canais com limites de caracteres que mudam com frequência|Substituir por "canais com limite declarado pelo operador" como variável dinâmica|MANTER COM AJUSTES
APX-P|L1-APX-P-boxes-tecnicos.md|01|P0|ALTO|Box 4 cita "Claude 4 Sonnet" — modelo inexistente no portfólio Anthropic|Corrigir para versão atual verificada antes de publicar|MANTER COM AJUSTES
APX-P|L1-APX-P-boxes-tecnicos.md|02|P0|ALTO|Box 10: implicação executiva sobre platô é frágil e pode ser invalidada antes do fim do ciclo de vendas|Reescrever para ser epistemicamente honesto sobre incerteza de platô|MANTER COM AJUSTES
APX-P|L1-APX-P-boxes-tecnicos.md|03|P1|MÉDIO|Box 11 Interação 3: FlashAttention e platô de scaling laws conectados como causa-efeito quando são independentes|Separar os dois fenômenos e corrigir a lógica causal|MANTER COM AJUSTES
APX-P|L1-APX-P-boxes-tecnicos.md|04|P1|MÉDIO|Box 1: tiebreak leakage citado sem atualização de status em APIs gerenciadas|Distinguir risco on-prem vs. risco em API gerenciada pelo provedor|MANTER COM AJUSTES
APX-P|L1-APX-P-boxes-tecnicos.md|05|P1|MÉDIO|Box 11 usa emojis coloridos como única codificação da matriz — ilegível em impressão monocromática|Adicionar codificação textual alternativa (C/S/T/N) com legenda|MANTER COM AJUSTES
APX-P|L1-APX-P-boxes-tecnicos.md|06|P1|BAIXO|Box 8: referência "trabalho de seguimento CoT 2024-2025" sem paper específico|Substituir por referência específica ou orientar leitor para venue/conferência|MANTER COM AJUSTES
APX-P|L1-APX-P-boxes-tecnicos.md|07|P1|BAIXO|Box 5: S-LoRA mencionado sem referência primária|Adicionar: Sheng et al. S-LoRA, 2023, arxiv.org/abs/2311.03285|MANTER COM AJUSTES
APX-P|L1-APX-P-boxes-tecnicos.md|08|P2|BAIXO|Box 6: exemplos de destilação (Phi-3, Gemini Nano) sem DeepSeek-R1-Distill — caso mais relevante em 2026|Adicionar DeepSeek-R1-Distill como exemplo e referência|MANTER COM AJUSTES
APX-P|L1-APX-P-boxes-tecnicos.md|09|P2|BAIXO|Epígrafe final é a frase mais memorável do apêndice — está enterrada no final|Mover para abertura de "Como usar este apêndice"|MANTER COM AJUSTES
APX-P|L1-APX-P-boxes-tecnicos.md|10|P2|BAIXO|Mapa de boxes referencia princípios (P1-P9) sem indicar onde estão definidos|Adicionar nota de rodapé com capítulo/apêndice de referência|MANTER COM AJUSTES
```
