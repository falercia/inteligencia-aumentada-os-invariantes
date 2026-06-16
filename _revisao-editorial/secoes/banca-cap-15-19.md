# BANCA EDITORIAL ADVERSARIAL — CAPÍTULOS 15 a 19
*Livro: INTELIGÊNCIA AUMENTADA | Tese: "Modelos passam. Método fica."*
*Leitura integral realizada em 16/06/2026*

---

# C15 — L1-C15-comparacao-modelos.md

## RESUMO EXECUTIVO
Nota: 7/10
Veredito: B

## O QUE FUNCIONA
- A analogia da frota de veículos é memorável, correta e escalonável mentalmente.
- A árvore de decisão (cinco perguntas sequenciais) é o coração durável do capítulo; sobrevive a qualquer rotação de modelos porque ancora em padrão de tarefa, não em lançamento.
- A seção 15.3.3 sobre benchmarks funciona bem: explica o que cada benchmark mede em vez de citar pontuação, o que é o movimento metodicamente correto.
- A delegação de números voláteis para o Apêndice J (Trilha do Número) é a decisão editorial mais acertada do capítulo.
- O exemplo da fintech com roteamento (15.5) está bem construído, com aviso de "cenário ilustrativo" explícito, números realistas e lição estrutural separada dos detalhes.
- A seção de Tendências (15.6) está correta e durável: comoditização, modelos especializados, integração com hardware.

## O QUE NÃO FUNCIONA
- O checklist (15.9) instrui o leitor a "citar os três frontier proprietários de 2026 e o que cada um lidera" — isso é exatamente o que o livro deveria evitar; instrução de memorização de catálogo.
- A tabela de forças relativas (seção 15.4) nomeia famílias específicas como "vencedoras" por eixo; ao lado da ressalva correta de que "padrões mudam pouco entre gerações", ainda convida o leitor a memorizar associações que podem ser falsas em 18 meses.
- O texto menciona "xAI" e "Z.AI (modelos GLM)" como actores relevantes sem o mesmo cuidado epistêmico aplicado às três grandes; esses players têm probabilidade alta de serem irrelevantes ou transformados em 2 anos.
- Referência a "Trainium da AWS, Tensor Processing Units do Google, e silicon proprietário da Apple" em 15.6 é lista de produtos que envelhece rápido sem entregar método.
- A autoavaliação final (15.14) tem traço de "Curiosidade " com espaço extra no final — erro tipográfico menor mas indica ausência de revisão.

---

## ACHADOS

### ACHADO 01
Categoria: P0
Problema: O checklist item 1 instrui o leitor a "Citar os três frontier proprietários de 2026 e o que cada um lidera" — objetivo de aprendizagem orientado a memorização de catálogo de nomes e associações.
Por que é um problema: Contradição direta com a tese da obra. O livro declara "Modelos passam. Método fica." mas o primeiro item do checklist pede que o leitor grave qual família lidera qual eixo em 2026. Em 18 meses, o item estará errado.
Impacto no leitor: Joana aprende que deve saber de cor "Claude = código, GPT = matemática, Gemini = multimodal", e usa isso como critério permanente quando deveria usar a árvore de decisão.
Correção exata: Substituir "Citar os três frontier proprietários de 2026 e o que cada um lidera" por "Aplicar o Framework Diagnóstico de Encaixe em um caso real, sem recorrer a memória de qual modelo lidera qual eixo".
Texto sugerido: `- [ ] Aplicar o Diagnóstico de Encaixe entre Tarefa e Modelo a um caso real, descendo a árvore pelas cinco perguntas sem depender de memorização de rankings correntes`
ROI: ALTO

### ACHADO 02
Categoria: P1
Problema: A tabela de "Pontos Fortes" por família (seção 15.3.1 e repetida na tabela do 15.4) fixa associações com nomes de famílias específicas ("Claude Opus em SWE-bench Verified, historicamente") sem sinalização adequada de volatilidade.
Por que é um problema: O leitor que ler em 2027 vai encontrar afirmações provavelmente incorretas apresentadas como padrão estrutural. A ressalva "esses padrões mudam pouco entre gerações" é insuficiente — mudam sim, e o próprio texto mostra isso ao citar que o DeepSeek reorganizou o mercado.
Impacto no leitor: Executivo usa a tabela como referência permanente em vez de consultá-la como snapshot datado.
Correção exata: Adicionar cabeçalho de aviso na tabela: "Estado observado em 2026 — consulte Apêndice J para atualização. Leia os padrões, não os nomes."
Texto sugerido: `> ⚠️ **Tabela datada (2026)** — Os padrões estruturais (código, multimodal, custo) tendem a ser estáveis; as famílias que lideram cada eixo mudam. Use esta tabela para entender os eixos, consulte o Apêndice J para saber quem lidera hoje.`
ROI: ALTO

### ACHADO 03
Categoria: P1
Problema: xAI e Z.AI (GLM) são mencionados sem cuidado epistemológico equivalente ao dos três grandes. A xAI é caracterizada por "tolerância maior a temas sensíveis" como se isso fosse vantagem estável — definição que pode ser interpretada como endosso de menor alinhamento.
Por que é um problema: Em livro que tem capítulo de Alignment (C23), endossar "tolerância maior a temas sensíveis" como característica neutra de produto é inconsistente filosoficamente e potencialmente embaraçoso.
Impacto no leitor: Joana pode inferir que escolher xAI é recomendação do livro para casos em que se quer menos restrição de segurança.
Correção exata: Reescrever a caracterização da xAI para ser factual sem conotação de endorsement, e adicionar nota sobre implicações de alinhamento.
Texto sugerido: `A **xAI** opera o Grok, com acesso em tempo real ao X e posicionamento em monitoramento de tendências de rede social. O menor filtro por padrão versus os três grandes é diferença arquitetural que pode ser vantagem em contextos específicos de análise e risco regulatório em outros — avalie conforme o Capítulo 23 (Alignment).`
ROI: MÉDIO

### ACHADO 04
Categoria: P1
Problema: A seção 15.6 cita "Trainium da AWS, Tensor Processing Units do Google, e silicon proprietário da Apple" como exemplos de integração com hardware. É uma lista de produtos que envelhece em 2 anos sem entregar o padrão durável.
Por que é um problema: Em 2027, a lista de chips mudou (AWS Trainium 3, novo silicon da Apple, concorrentes), e o leitor que leu a lista decorou nomes errados.
Impacto no leitor: Confunde sinal de curto prazo (esses chips específicos) com tendência durável (inferência especializada em hardware específico reduz custo).
Correção exata: Reescrever o parágrafo para expressar o padrão durável e colocar os exemplos entre parênteses com marcação de snapshot.
Texto sugerido: `A tendência durável é que chips dedicados de inferência (como Trainium da AWS, TPUs do Google e silicon da Apple — exemplos de 2026, ver Apêndice J) estão mudando a economia de inferência de forma estrutural. O padrão a acompanhar é: custo de inferência em hardware especializado cai mais rápido que custo de hardware genérico, o que desloca a fronteira do self-hosting continuamente.`
ROI: MÉDIO

### ACHADO 05
Categoria: P2
Problema: Erro tipográfico em 15.14 — "**Curiosidade **" com espaço antes do fechamento do negrito. Sinal de ausência de revisão de copydeck.
Por que é um problema: Pequeno mas sinal de que a seção de autoavaliação não passou por revisão final.
Impacto no leitor: Mínimo, mas prejudica a credibilidade de atenção ao detalhe.
Correção exata: Remover espaço extra: `**Curiosidade**`
Texto sugerido: `| 5 | **Curiosidade** — Está com vontade de entender em profundidade o ecossistema open source, suas vantagens reais e suas armadilhas | ☐ |`
ROI: BAIXO

### ACHADO 06
Categoria: P2
Problema: A pergunta de revisão 3 (seção 15.10) pede que o leitor decida entre "Claude Opus e o frontier GPT para sistema de agentes autônomos" — pergunta orientada a nomes de produtos específicos, não a critérios.
Por que é um problema: Reforça a memória de produto em vez do método de decisão.
Impacto no leitor: O leitor pratica responder com nomes de modelos em vez de com lógica de encaixe.
Correção exata: Reformular como: "Como você decidiria entre um modelo premium centrado em código e um modelo premium centrado em computer use para um sistema de agentes? Quais perguntas do Diagnóstico de Encaixe guiariam a decisão?"
Texto sugerido: n/a (reformulação estrutural da pergunta)
ROI: BAIXO

---

## TESTE DA JOANA
Entenderia: SIM (parcialmente)
O que ela entenderia: A analogia da frota é excelente — Joana vai lembrar dela. A árvore de cinco perguntas é clara. O exemplo da fintech com economia de US$ 380 mil é concreto e motivador.
O que ela NÃO entenderia: A menção a "MCP" em 15.3.1 sem definição no capítulo (referencia Cap 13, mas quem está lendo fora de ordem não tem contexto). A distinção entre "frontier proprietário" e "open source" aparece sem o cuidado de 15.3.1 ter sido introduzido — ela pode confundir "open source" com "gratuito".
Como corrigir: Adicionar uma linha de definição de "MCP" inline na primeira menção, ou remover da seção e deixar apenas a referência ao capítulo.

## TESTE DE DURABILIDADE
Classificação: MÉDIA
2 anos: O framework de decisão (árvore de perguntas) sobrevive bem. As associações de família-força (Claude = código, GPT = matemática, Gemini = multimodal) provavelmente são parcialmente incorretas em 2028.
5 anos: A analogia da frota sobrevive. Os nomes de família e benchmarks específicos (ARC-AGI-2, Humanity's Last Exam) provavelmente foram superados.
10 anos: O método de roteamento por categoria de complexidade sobrevive. Tudo com nome de produto específico está obsoleto.
Justificativa: O capítulo se salva por delegar os números ao Apêndice J, mas os nomes de família no corpo do texto criam risco de leitura desatualizada por leitor que não for ao apêndice.

## TESTE DE DIFERENCIAÇÃO
Classificação: DIFERENCIADO
Justificativa: A estrutura de árvore de decisão com critério explícito (não "qual é o melhor" mas "qual passa nos critérios") é genuinamente pedagógica e não é comum em livros de IA executivos. A maioria dos concorrentes faz catálogo. Este capítulo não faz catálogo — faz método. Exceção: as tabelas de força por família são commodity.

## TESTE DE MEMORIZAÇÃO
Ideia principal clara? SIM
Qual é a ideia principal: "Não existe melhor modelo universal; existe roteamento inteligente por categoria de tarefa, com frota gerenciada em vez de escolha única."
Justificativa: A mensagem emerge clara da analogia e é repetida na epígrafe de fechamento.

## TESTE DE TRANSFORMAÇÃO
Ao terminar, o leitor consegue fazer o que antes não conseguia:
- Responder em reunião "não existe melhor modelo" com argumento estruturado, não opinião.
- Aplicar árvore de decisão de cinco perguntas para rotear tarefas entre tiers de modelo.
- Estimar potencial de economia de roteamento em operação existente.
- Distinguir qual benchmark é relevante para o seu caso de uso.
- Não confiar em ranking único como decisão de fundação.

## NOTA FINAL
Estrutura: 8 | Pedagogia: 8 | Clareza: 7 | Autoridade: 7 | Durabilidade: 6 | Diferenciação: 7 | Memorização: 8 | Transformação: 8
**Nota Geral: 7.4**

## DECISÃO EDITORIAL
MANTER COM AJUSTES
*Correções prioritárias: reformular checklist item 1 (P0), adicionar aviso datado às tabelas de força por família (P1), revisar caracterização da xAI (P1). O método é sólido; o catálogo residual no corpo do texto é o risco principal.*

---
---

# C16 — L1-C16-open-source.md

## RESUMO EXECUTIVO
Nota: 8/10
Veredito: A

## O QUE FUNCIONA
- A distinção "open weights × open source estrito" (16.3.2) é pedagogicamente precisa e rara em livros executivos — entrega valor real ao leitor.
- A seção de quantização (16.3.3) é técnica sem ser inacessível para Joana e entrega a implicação prática (PME rodando 70B em uma GPU) de forma concreta.
- A matriz de TCO em 12 meses (Quadro 16.A) é um artefato executivo genuíno: combina componentes que a maioria dos guias omite (time especializado, atualização, contingência).
- O caso da healthtech (16.4) é o mais completo dos exemplos dos cinco capítulos: tem vetor de pressão, processo de decisão, resultado quantificado, lição estrutural, e a ressalva de "cenário composto" explícita.
- Os seis critérios (16.5) são claros, ordenados e duráveis — esta é a parte mais Invariante do capítulo.
- A referência ao PL 2338 com ressalva de "em tramitação" e delegação ao Apêndice J é modelo de como citar legislação em evolução.

## O QUE NÃO FUNCIONA
- O capítulo cita "Nota Técnica da ANPD sobre IA generativa de 2026" em múltiplos pontos como documento estabelecido, mas o próprio texto ressalva que precisa ser verificado. A repetição sem marcação datada clara dá impressão de autoridade que pode não existir na data de leitura.
- A tabela do Quadro 16.A tem célula com "~600.000 (~50.000/mês para 100k req/dia média)" — esse número envelhece em meses. Preços de API da Anthropic (Claude Sonnet) mudaram múltiplas vezes em 18 meses.
- A seção 16.3.1 lista famílias com nomes de versão específicos (DeepSeek V3.1, Qwen 2.5 e Qwen 3, Llama 3.3 e 4) — inventário que terá versões novas antes do livro ir à gráfica.
- A referência ao Phi 4 como "14B" pode estar desatualizada — a família Phi evoluiu para Phi 4.5 e outras variantes.
- O Quadro 16.A descreve o híbrido com "~735.000" sendo mais caro que API exclusiva "~725.000" mas afirma que o híbrido é o padrão maduro — a lógica financeira parece inconsistente sem explicação mais clara de quando o híbrido ganha.

---

## ACHADOS

### ACHADO 01
Categoria: P0
Problema: O Quadro 16.A mostra custo total do Híbrido (~735.000) maior que API exclusiva (~725.000) mas o texto conclui que "o híbrido é o que justifica a arquitetura na maioria dos casos". A inconsistência não é explicada: se o híbrido custa mais, por que é o padrão maduro economicamente?
Por que é um problema: O leitor executivo (especialmente o CFO de Joana) vai notar que o argumento econômico não sustenta a recomendação. A defesa do híbrido precisa estar nos "benefícios não-monetários" — mas a tabela não os destaca.
Impacto no leitor: Mina a credibilidade do argumento TCO. O CFO diz "os números mostram que API é mais barata" e o argumento do híbrido colapsa.
Correção exata: Adicionar coluna "Benefício não-monetário" na tabela, OU adicionar parágrafo de reconciliação explícita: "No exemplo acima, o híbrido custa marginalmente mais que API exclusiva — o argumento econômico puro favorece API. O híbrido se justifica pelos benefícios estruturais não capturados na fatura: soberania de dado sensível em 97% do volume, capacidade de fine-tuning, e resiliência ao lock-in. Se esses três não têm valor para a organização, API exclusiva é a resposta certa nesse volume."
Texto sugerido: (parágrafo acima como inserção após a tabela)
ROI: ALTO

### ACHADO 02
Categoria: P1
Problema: O Quadro 16.A usa preço de API específico ("~600.000 para Claude Sonnet, ~50k/mês para 100k req/dia média") — dado que envelhece em ciclos de meses conforme a Anthropic ajusta preços.
Por que é um problema: Em 12 meses, os preços de Sonnet podem ser 30-50% diferentes; o leitor que usar a tabela para decisão terá premissa errada.
Impacto no leitor: Cálculo de TCO errado → decisão arquitetural errada.
Correção exata: Substituir o valor específico de API por "custo corrente de API (verificar Apêndice J)" e transformar a tabela em template com células marcadas como "preencher com valor corrente do provedor escolhido".
Texto sugerido: Cabeçalho da tabela: `| Componente | API exclusiva (preencher com preço atual — Apêndice J) | Self-hosting | Híbrido |`
ROI: ALTO

### ACHADO 03
Categoria: P1
Problema: A seção 16.3.1 lista "DeepSeek V3.1", "Qwen 2.5 e Qwen 3", "Llama 3.3 e 4", "Phi 4" como inventário específico de versões. Esse nível de especificidade envelhece antes da impressão.
Por que é um problema: O capítulo inteiro tem a tese de que a decisão é sobre método, não catálogo. A própria seção 16.3.1 contraria essa tese ao fazer exatamente o catálogo que o capítulo deveria evitar.
Impacto no leitor: Em 2027, o leitor encontra versões defasadas e perde confiança no resto do capítulo.
Correção exata: Manter os nomes de família (DeepSeek, Meta Llama, Mistral, Qwen, Phi, Gemma) mas remover números de versão do corpo do texto e delegar para o Apêndice J. Adicionar instrução de consulta: "versão corrente em Apêndice J."
Texto sugerido: `**DeepSeek (laboratório chinês).** Família em licença MIT com foco em raciocínio, código e multilíngue. Versão corrente no Apêndice J. Qualidade de fronteira open weights em várias tarefas corporativas...`
ROI: MÉDIO

### ACHADO 04
Categoria: P1
Problema: "Nota Técnica da ANPD sobre IA generativa de 2026" é citada múltiplas vezes como se fosse documento estabelecido e bem-definido, mas a própria referência ao final do capítulo instrui "verificar versão corrente em fonte oficial datada". A citação no corpo do texto sem data específica e sem nota de rodapé cria falsa autoridade.
Por que é um problema: A Nota Técnica pode ter sido revisada, substituída, ou pode nem ter sido publicada com esse título exato. O leitor que tentar verificar pode não encontrar o documento nomeado.
Impacto no leitor: Profissional de compliance usa a referência em apresentação interna, não encontra o documento exato, perde credibilidade.
Correção exata: Em toda menção à Nota Técnica da ANPD, adicionar marcação "(verificar versão corrente em Apêndice J — Trilha do Número)" explicitamente, ou criar nota de rodapé padrão para o capítulo.
Texto sugerido: `...a Nota Técnica da ANPD sobre IA generativa (versão corrente: Apêndice J — Trilha do Número)...`
ROI: MÉDIO

### ACHADO 05
Categoria: P2
Problema: A analogia da frota corporativa (16.2) é boa mas longa. Quatro parágrafos para estabelecer a analogia antes de descer ao técnico. Em um livro de executivos, a analogia poderia ser comprimida em dois parágrafos sem perda de conteúdo.
Por que é um problema: Ritmo lento na entrada do capítulo pode fazer Joana pular para 16.3, perdendo a estrutura narrativa que o livro usa.
Impacto no leitor: Menor — mas analogia longa demais perde força.
Correção exata: Comprimir 16.2 de quatro para dois parágrafos, mantendo os quatro pontos de analogia mas de forma mais densa.
Texto sugerido: n/a (reescrita de compressão)
ROI: BAIXO

### ACHADO 06
Categoria: P2
Problema: A pergunta de revisão 5 cita "Nota Técnica da ANPD de 2026" como dado de fact — instrução de memorização que cria o mesmo problema de durabilidade.
Por que é um problema: Em 2027, o leitor não vai saber se a nota de 2026 ainda é a vigente.
Impacto no leitor: Leitor memora "2026" como referência correta quando deveria aprender a verificar a versão corrente.
Correção exata: Reformular: "Como a regulação de privacidade brasileira (atualmente LGPD + orientações da ANPD — verificar versão corrente) desloca a fronteira em favor de operação em território nacional?"
Texto sugerido: n/a
ROI: BAIXO

---

## TESTE DA JOANA
Entenderia: SIM
O que ela entenderia: A analogia da frota é acessível. O conceito de "API vs self-hosting" tem paralelo imediato com "terceirizar vs fazer em casa". A Quadro 16.A com valores em reais é diretamente utilizável por ela em conversa com CFO.
O que ela NÃO entenderia: "Quantização INT4 com AWQ" — o texto explica o que é INT4 mas AWQ fica como sigla sem desdobramento suficiente para quem não é técnico. "vLLM como engine de inferência" — não há definição do que é uma engine de inferência para não-técnico.
Como corrigir: Adicionar glossário inline para AWQ: "(AWQ — método de quantização que preserva melhor a qualidade; detalhes técnicos desnecessários para decisão executiva)".

## TESTE DE DURABILIDADE
Classificação: MÉDIA
2 anos: Os seis critérios de decisão (16.5), a distinção open weights × open source estrito, a lógica de TCO honesto — tudo isso sobrevive. As versões de modelo, os preços específicos e a referência à "Nota Técnica da ANPD de 2026" ficam desatualizados.
5 anos: O método de TCO honesto sobrevive. O Quadro 16.A precisa ser refaturado com novos números.
10 anos: Os princípios de soberania de dados, TCO composto e arquitetura híbrida sobrevivem. Os nomes de provedor (Magalu Cloud, etc.) podem não existir mais.
Justificativa: Capítulo bem construído com separação razoável entre método durável e exemplos datados. O risco principal são os números de preço e os números de versão.

## TESTE DE DIFERENCIAÇÃO
Classificação: DIFERENCIADO
Justificativa: A matriz de TCO com os cinco componentes (hardware, time, energia, atualização, contingência) é mais completa que qualquer framework equivalente em livros de gestão de IA disponíveis no mercado brasileiro. A distinção open weights × open source estrito é rara e precisa. O posicionamento de soberania de dados como driver estratégico, não apenas técnico, é genuíno.

## TESTE DE MEMORIZAÇÃO
Ideia principal clara? SIM
Qual é a ideia principal: "A decisão de 2026 não é 'open source ou API' — é arquitetura híbrida com classificador, calibrada por TCO honesto e soberania de dado."
Justificativa: A frase é repetida várias vezes e a epígrafe de fechamento a cristaliza bem.

## TESTE DE TRANSFORMAÇÃO
Ao terminar, o leitor consegue fazer o que antes não conseguia:
- Calcular TCO honesto de 12 meses com os cinco componentes (não apenas fatura de API).
- Distinguir open weights de open source estrito e saber que quase nenhum modelo grande é open source estrito.
- Identificar o ponto de virada econômico (volume mensal) para avaliar se self-hosting se justifica.
- Saber quais perguntas fazer ao DPO sobre soberania de dados sensíveis.
- Propor arquitetura híbrida com classificador como alternativa ao binário "API ou on-prem".

## NOTA FINAL
Estrutura: 9 | Pedagogia: 8 | Clareza: 7 | Autoridade: 8 | Durabilidade: 6 | Diferenciação: 9 | Memorização: 8 | Transformação: 9
**Nota Geral: 8.0**

## DECISÃO EDITORIAL
MANTER COM AJUSTES
*Correções prioritárias: resolver inconsistência do Quadro 16.A onde híbrido custa mais que API mas é recomendado (P0); transformar preços específicos em template com remissão ao Apêndice J (P1); remover números de versão de modelos do corpo (P1).*

---
---

# C17 — L1-C17-github-repos.md

## RESUMO EXECUTIVO
Nota: 9/10
Veredito: A+

## O QUE FUNCIONA
- Este é o capítulo mais autorreferente e metodologicamente consistente dos cinco. A epígrafe que abre, a analogia do imóvel, o protocolo de 30 minutos, o anti-padrão das estrelas — tudo é internamente coerente e genuinamente durável.
- A analogia do corretor de imóvel em trinta minutos é a mais precisa e útil dos cinco capítulos: tem seis blocos, cada um com lição direta, e o padrão de "cada bloco é trivialmente auditável em cinco minutos" é imediatamente aplicável.
- O Quadro 17.A (tabela do protocolo) é o melhor artefato operacional dos cinco capítulos: colunas claras, decisão binária, três saídas. Executável sem contexto adicional.
- A seção de anti-padrões (17.4) é pedagógica: as quatro armadilhas com o sinal real versus performático são precisas e não requerem atualização.
- O ciclo de vida do repositório (17.3.7) com cinco fases e quatro sinais cada é framework durável que sobrevive a qualquer rotação do ecossistema.
- A seção 17.6 tem a consciência editorial mais honesta de todo o livro: declara explicitamente que a lista vai envelhecer, que serve apenas como exercício de aplicação, e convida o leitor a comparar com sua própria auditoria. Isso é exatamente como o capítulo deveria se comportar.
- O exemplo da fintech (17.5) é concreto, realista, com números plausíveis e lição estrutural clara.

## O QUE NÃO FUNCIONA
- O capítulo referencia "imagens/cap-35-img-01-repos-categoria.svg" com código de capítulo (cap-35) diferente do número do capítulo (17). Erro de referência de arquivo que indica inconsistência na numeração interna.
- A seção 17.6 declara que lista oito repositórios mas a caracterização inclui "Weights & Biases" com "componente proprietário dominante" — confunde a ferramenta open source (SDK W&B) com o produto comercial. A distinção importa para o Critério 6 (encaixe).
- O texto menciona "OpenInterpreter" com "governança em pessoa física com empresa em formação" — informação de alta perecibilidade que contradiz a filosofia do capítulo.
- A regra "CI vermelho na branch principal" em 17.3.3 é apresentada como red flag absoluta, mas CI verde é trivialmente falsificável (basta não ter CI). A regra deveria ser CI presente e verde, não apenas "verde".

---

## ACHADOS

### ACHADO 01
Categoria: P1
Problema: Referência de imagem usa "imagens/cap-35-img-01-repos-categoria.svg" — cap-35 quando o capítulo é o 17. Inconsistência de numeração interna.
Por que é um problema: Indica que o arquivo de imagem pode não existir no caminho correto, ou que houve renumeração de capítulos sem atualização das referências.
Impacto no leitor: Imagem quebrada na versão digital; ilustração ausente na versão impressa.
Correção exata: Verificar o caminho correto do arquivo SVG e corrigir para "imagens/cap-17-img-01-repos-categoria.svg" (ou o padrão adotado pelo livro).
Texto sugerido: `![Mapa de categorias de repositórios relevantes no ecossistema de IA](imagens/cap-17-img-01-repos-categoria.svg)`
ROI: ALTO

### ACHADO 02
Categoria: P1
Problema: A caracterização do "OpenInterpreter" inclui "governança em pessoa física com empresa em formação" — informação extremamente perecível que contradiz a filosofia de método durável que o capítulo defende.
Por que é um problema: Se o livro instrui a não confiar em blog posts e README de marketing por envelhecerem, o próprio livro não pode fazer exatamente isso ao caracterizar a governança de um projeto pelo estado corrente da empresa do mantenedor.
Impacto no leitor: Em 6 meses, a informação estará desatualizada; o leitor perde confiança no método exatamente no capítulo que deveria defender o método.
Correção exata: Substituir "governança em pessoa física com empresa em formação" por observação sobre o critério que o leitor deve verificar: "verifique a fase do ciclo de vida conforme protocolo — em meados de 2026 estava em adoção real com sinais de transição, mas esse diagnóstico é exercício, não inventário."
Texto sugerido: `**OpenInterpreter.** Fase variável — audite conforme protocolo. Em meados de 2026: adoção real com sinais de transição, encaixe limitado em produção corporativa, natural em sandbox e uso individual. Leia a governança corrente no repositório ao aplicar Critério 5.`
ROI: MÉDIO

### ACHADO 03
Categoria: P1
Problema: A regra de CI (17.3.3) diz "CI vermelho na branch principal é red flag" mas não exige CI presente como condição. CI ausente é mais grave que CI vermelho, mas a formulação da regra não captura isso.
Por que é um problema: Projeto sem CI passa no critério (por não ter CI vermelho) mas deveria falhar.
Impacto no leitor: Adota projeto que passou no critério 3 sem ter CI algum.
Correção exata: Reformular: "A ausência de CI é red flag imediata em qualquer projeto que se apresenta como pronto para produção. CI presente e vermelho é sinal de descuido ou de quebra ativa — igualmente problemático."
Texto sugerido: `**CI/CD ativo.** A ausência de pipeline de integração contínua é red flag imediata para uso em produção. CI presente com status vermelho na branch principal indica quebra ativa ou descuido — ambos são red flag. Passes em CI com histórico verde nos últimos commits é o critério de aprovação.`
ROI: MÉDIO

### ACHADO 04
Categoria: P2
Problema: A seção de Weights & Biases (17.6) descreve "componente proprietário dominante" e "modelo de negócio em camada hospedada" mas não aprofunda o que isso significa para o Critério 6 (encaixe) — especificamente para a organização com restrição de operação totalmente self-hosted.
Por que é um problema: É o único dos oito repositórios em que a questão de licença e encaixe é relevante o suficiente para merecer destaque mas o texto não destaca.
Impacto no leitor: Organização com restrição regulatória de self-hosting total adota W&B sem perceber que a funcionalidade principal requer a camada cloud.
Correção exata: Adicionar frase explícita: "Para organização com restrição de self-hosting total por regulação, verifique se a funcionalidade requerida está no SDK open source ou exige a camada hospedada — essa verificação entra no Critério 6."
Texto sugerido: (adicionar ao final da linha sobre W&B)
ROI: BAIXO

### ACHADO 05
Categoria: P2
Problema: O exemplo (17.5) descreve sessão com "dois engenheiros sêniores e o tech lead da plataforma de IA" tomando "dez horas totais distribuídas em três tardes" — mas o protocolo diz 30 minutos por repositório. Vinte repositórios × 30 minutos = 10 horas, o que fecha. Mas o leitor pode interpretar que cada pessoa gastou 10 horas (30 horas totais) em vez de que a sessão total foi 10 horas. A ambiguidade é pequena mas real.
Por que é um problema: Leitor pode perceber que três pessoas dedicaram 10 horas cada = 30 horas para auditar 20 repositórios, o que não valida o protocolo de 30 min/repo.
Impacto no leitor: Questionamento sobre se o protocolo é realmente de 30 minutos.
Correção exata: Clarificar: "...dez horas totais de sessão coletiva (média de trinta minutos por repositório aplicada em trio), distribuídas em três tardes."
Texto sugerido: n/a (pequeno ajuste de clareza)
ROI: BAIXO

---

## TESTE DA JOANA
Entenderia: SIM
O que ela entenderia: A analogia do corretor de imóvel é o melhor ponto de entrada dos cinco capítulos para Joana. O Quadro 17.A é imediatamente utilizável por ela como checklist para perguntar ao time. Os quatro anti-padrões são reconhecíveis e memoráveis.
O que ela NÃO entenderia: "SemVer" sem definição inline (ela sabe o que é "versionamento semântico" pela explicação, mas o acrônimo SemVer aparece sem apresentação). "Bus factor de um" — jargão técnico não explicado.
Como corrigir: Definir bus factor inline: "(bus factor de um: risco de o projeto parar se uma única pessoa chave sair)".

## TESTE DE DURABILIDADE
Classificação: ALTA
2 anos: O protocolo de seis critérios, o ciclo de vida, os anti-padrões — tudo sobrevive. A lista de oito repositórios em 17.6 provavelmente está parcialmente desatualizada.
5 anos: O método sobrevive inteiramente. Os oito exemplos são exercício de aplicação, não inventário — o capítulo resiste.
10 anos: Este é o capítulo com maior durabilidade dos cinco. A analogia do imóvel e o protocolo de 30 minutos descrevem lógica de avaliação de qualidade de software que não tem data de validade.
Justificativa: O capítulo pratica o que prega — não faz catálogo, faz método. A seção 17.6 tem a maior consciência editorial sobre durabilidade de qualquer seção dos cinco capítulos.

## TESTE DE DIFERENCIAÇÃO
Classificação: PROPRIEDADE INTELECTUAL
Justificativa: O protocolo de 30 minutos com seis critérios duráveis, o ciclo de vida com quatro sinais por fase, os quatro anti-padrões com o mecanismo de sinal performático — em conjunto, isso é framework genuinamente novo que não existe em formato equivalente em nenhum livro de IA executivo do mercado. Este capítulo justifica o livro por si só para qualquer CTO que já perdeu tempo com repositório abandonado.

## TESTE DE MEMORIZAÇÃO
Ideia principal clara? SIM
Qual é a ideia principal: "Inventário envelhece em seis meses; método de auditoria dura uma carreira — e o método cabe em trinta minutos por repositório, com seis critérios e a coragem de descartar catorze de cada vinte."
Justificativa: A epígrafe inicial e a epígrafe final repetem a mesma ideia em formulações levemente diferentes. Memorável.

## TESTE DE TRANSFORMAÇÃO
Ao terminar, o leitor consegue fazer o que antes não conseguia:
- Auditar qualquer repositório GitHub em 30 minutos com critério explícito e decisão documentada.
- Reconhecer as quatro armadilhas (estrelas, README, demo, blog post) antes de tomá-las como sinal real.
- Classificar repositório em uma das cinco fases do ciclo de vida e tomar decisão proporcional.
- Estabelecer planilha estruturada de auditoria como padrão da casa.
- Proteger a organização de "lista de conferência" sem método de validação.

## NOTA FINAL
Estrutura: 9 | Pedagogia: 10 | Clareza: 9 | Autoridade: 9 | Durabilidade: 9 | Diferenciação: 10 | Memorização: 9 | Transformação: 10
**Nota Geral: 9.4**

## DECISÃO EDITORIAL
MANTER COM AJUSTES
*Apenas dois ajustes prioritários: corrigir referência de imagem com número de capítulo errado (P1) e reformular a caracterização de OpenInterpreter para não infringir a filosofia do próprio capítulo (P1). O resto é excelente — este é o capítulo mais alinhado com a tese do livro.*

---
---

# C18 — L1-C18-economia-tokens.md

## RESUMO EXECUTIVO
Nota: 7/10
Veredito: B

## O QUE FUNCIONA
- A fórmula do custo composto (18.2.1) com os quatro termos explícitos (tokens×preço, chamadas, redundância, tier) é o melhor artefato conceitual do capítulo — diferente do que se encontra nos guias de otimização típicos que tratam apenas o preço por token.
- A regra de ordem de implementação (T1 antes T2 antes T3) é contraintuitiva e valiosa: a maioria dos times começa por poda de contexto (T3) enquanto o maior impacto está em roteamento de tier (T1).
- O exemplo da SaaS (18.5) é limpo e convincente: comprova a regra de ordem com um caso real de "equipe otimizou o termo trivial enquanto a sangria estava no termo composto".
- O Quadro 18.A é util como referência rápida.
- A seção 18.6 (quando aprofundar e quando parar) é rara em guias de otimização e entrega valor genuíno — saber quando parar é tão importante quanto saber quando começar.

## O QUE NÃO FUNCIONA
- O capítulo é o mais curto dos cinco em extensão de análise e o menos desenvolvido em framework. Não tem analogia de abertura (a rubrica espera "CONCEITO INTUITIVO + ANALOGIA" mas aqui só há conceito). A seção 18.2 vai direto para a fórmula matemática sem rampa de acesso.
- A tabela 18.7 apresenta percentuais de economia "40-70%, 30-60%, 30-50%..." que se somam a mais de 100% sem explicação de que são ganhos compostos não-aditivos. Um CFO vai perguntar "isso dá 200% de economia total?" e a resposta não está no texto.
- A seção 18.1 tem o aviso metodológico sobre "ordens de grandeza observadas" — bom — mas o aviso aparece no topo antes de qualquer contexto, o que o torna invisível ao leitor que lê por diagonal.
- A referência ao Framework F7 é repetida 3 vezes mas o framework não está no capítulo. O leitor não sabe o que é F7 sem navegar para fora do capítulo.
- O capítulo não tem analogia. Para um tema de finanças corporativas, uma analogia de otimização financeira (ex: análise de Pareto em gastos operacionais) tornaria a entrada muito mais acessível para Joana.
- Perguntas de revisão (18.8) têm apenas 5 itens — todos os outros capítulos têm 7-8. Indica desenvolvimento incompleto.
- A autoavaliação (18.12) tem item 5 sobre "Curiosidade para segurança em escala corporativa" — que não tem relação com o capítulo de economia de tokens. Parece copypaste de outro capítulo.

---

## ACHADOS

### ACHADO 01
Categoria: P0
Problema: A tabela 18.7 lista percentuais de economia por alavanca (40-70%, 30-60%, etc.) sem explicar que são ganhos compostos aplicados a bases progressivamente menores, não aditivos sobre a fatura original. A soma ingênua ultrapassa 200%.
Por que é um problema: CFO ou analista financeiro vai somar as percentagens e perguntar "nossa fatura vai para zero?" — destruindo a credibilidade do autor.
Impacto no leitor: Decisão de investimento em otimização baseada em expectativa inflada. Descredita o capítulo para leitores com mentalidade quantitativa.
Correção exata: Adicionar nota de rodapé ou parágrafo após a tabela explicando: "Os percentuais são aplicados sequencialmente sobre o resíduo — não são aditivos. Aplicar todas as sete alavancas pode resultar em economia de 60-75% do total original, não na soma dos intervalos."
Texto sugerido: `> ⚠️ **Os percentuais não somam.** Cada alavanca é aplicada sobre o custo residual após as anteriores. Prompt caching de 40-70% reduz a base; roteamento de 30-60% incide sobre o que sobrou. A economia composta realista com todas as sete alavancas bem executadas é de 60 a 75% da fatura original — não a soma dos intervalos acima.`
ROI: ALTO

### ACHADO 02
Categoria: P1
Problema: O capítulo não tem analogia de abertura. A entrada vai direto para a fórmula matemática, o que é inacessível para Joana e para executivos financeiros sem background técnico.
Por que é um problema: A rubrica do livro exige Conceito Intuitivo + Analogia. Este capítulo pula a analogia, tornando a fórmula do custo composto mais difícil de internalizar do que precisa ser.
Impacto no leitor: Joana para na fórmula, lê o exemplo da SaaS e entende a mensagem, mas perde a estrutura analítica que permitiria aplicar em outras situações.
Correção exata: Adicionar analogia entre 18.1 e 18.2. Sugestão: "Pense em conta de energia elétrica corporativa. O preço do kWh aparece na fatura, mas o que explode a conta é a soma de equipamentos ligados × horas × quantidade de unidades. Cortar o preço do kWh em 5% via negociação com a distribuidora entrega menos que desligar equipamentos em stand-by que ninguém auditou. Tokens funcionam da mesma forma: preço por token é o kWh; chamadas, redundância e tier são os equipamentos esquecidos ligados."
Texto sugerido: (parágrafo acima como Seção 18.2 de analogia antes da fórmula)
ROI: ALTO

### ACHADO 03
Categoria: P1
Problema: A autoavaliação (18.12) item 5 diz "Curiosidade para segurança em escala corporativa" — completamente desconectado do tema do capítulo (economia de tokens). Claramente é texto de outro capítulo copiado sem ajuste.
Por que é um problema: Erro editorial básico que sinaliza que a seção de autoavaliação foi produzida por template sem revisão de conteúdo.
Impacto no leitor: Perde confiança na qualidade editorial; pode confundir o leitor sobre o que o capítulo cobre.
Correção exata: Substituir pelo critério correto de curiosidade para economia de tokens: "Curiosidade — Está motivado a instrumentar tokens por feature na sua operação nas próximas duas semanas para ter baseline real antes de iniciar o programa de otimização?"
Texto sugerido: `| 5 | **Curiosidade** — Está motivado a instrumentar tokens por feature na próxima semana para ter baseline real e iniciar o programa de otimização com diagnóstico honesto? | ☐ |`
ROI: ALTO

### ACHADO 04
Categoria: P1
Problema: O Framework F7 é referenciado três vezes no capítulo mas nunca definido. O leitor que lê o capítulo isoladamente não sabe o que é F7.
Por que é um problema: Referência circular sem âncora no texto cria sensação de que o capítulo está incompleto — como se a parte "real" estivesse em outro lugar.
Impacto no leitor: Leitor que não tem acesso ao framework completo não consegue aplicar T1/T2/T3 sistematicamente.
Correção exata: Adicionar mini-descrição do F7 na primeira menção: "Framework F7 — Custo Composto em Três Tempos: o plano operável das três alavancas (T1=tier, T2=topologia, T3=contexto) com metas, riscos e ordem de execução detalhados no módulo de Frameworks do livro."
Texto sugerido: n/a (inline na primeira menção de F7)
ROI: MÉDIO

### ACHADO 05
Categoria: P1
Problema: O aviso metodológico de 18.1 ("As reduções percentuais apresentadas... são ordens de grandeza observadas... não médias estatísticas de pesquisa peer-reviewed") está no início do capítulo antes de qualquer contexto, tornando-o invisível. O leitor que lê em diagonal vai ao título, à fórmula e ao exemplo — e nunca vê o aviso.
Por que é um problema: Os percentuais são usados por executivos em apresentações ao conselho sem a ressalva metodológica, criando expectativas incorretas.
Impacto no leitor: "O livro diz que economizamos 70%" → promessa não cumprida → descredita o autor.
Correção exata: Mover o aviso para próximo à tabela 18.7, onde os percentuais aparecem, em vez de no início do texto onde é ignorado.
Texto sugerido: Mover o parágrafo de ressalva de 18.1 para um bloco de rodapé da tabela 18.7.
ROI: MÉDIO

### ACHADO 06
Categoria: P2
Problema: Os preços de tier mencionados no Quadro 18.A ("30 a 50 vezes o preço do modelo pequeno") são afirmações de magnitude que envelhecem conforme os fornecedores ajustam pricing.
Por que é um problema: Em 18 meses, a razão premium/pequeno pode ser 10x ou 100x dependendo dos lançamentos.
Impacto no leitor: Leitor usa "30-50x" como dado firme em análise financeira.
Correção exata: Adicionar remissão: "(magnitude observada em 2026; confirmar razão atual nas fichas dos fornecedores — Apêndice J)".
Texto sugerido: n/a (inline na menção)
ROI: BAIXO

---

## TESTE DA JOANA
Entenderia: NÃO (sem a analogia)
O que ela entenderia: O exemplo da SaaS (18.5) é excelente para Joana — concreto, em reais, com narrativa de descoberta. A seção "Para executivos" inline em 18.2.3 é útil.
O que ela NÃO entenderia: A fórmula matemática em 18.2.1 (Σ, tokens_in, tokens_out) — não há rampa de acesso. Os percentuais da tabela 18.7 sem a explicação de que não são aditivos vão confundi-la ou fazê-la ignorar a tabela.
Como corrigir: A analogia da conta de energia proposta no Achado 02 resolve o problema de entrada para Joana.

## TESTE DE DURABILIDADE
Classificação: ALTA
2 anos: A fórmula do custo composto com quatro termos, a ordem de implementação T1>T2>T3, o exemplo estrutural da SaaS — tudo sobrevive.
5 anos: O framework sobrevive. Os percentuais específicos ficam como referência histórica.
10 anos: Os princípios de custo composto (multiplicadores, não termos isolados) são durávéis. Este capítulo tem a segunda maior durabilidade depois do C17.
Justificativa: A fórmula e a lógica de ordem de implementação são independentes de qualquer fornecedor ou modelo específico.

## TESTE DE DIFERENCIAÇÃO
Classificação: DIFERENCIADO
Justificativa: A fórmula explícita do custo composto com os quatro termos é genuinamente original na literatura de gestão de IA. A maioria dos guias trata apenas "preço por token" como variável de otimização. A instrução contraintuitiva de atacar tier antes de contexto é diferencial.

## TESTE DE MEMORIZAÇÃO
Ideia principal clara? SIM (mas com atrito)
Qual é a ideia principal: "O preço por token é o termo trivial; o custo real escala pelos multiplicadores de chamadas, redundância e tier — e otimizá-los nessa ordem entrega 60-75% de economia."
Justificativa: A ideia está clara mas exige que o leitor chegue ao exemplo (18.5) para cristalizar. Sem a analogia, muitos leitores vão perder a estrutura da fórmula.

## TESTE DE TRANSFORMAÇÃO
Ao terminar, o leitor consegue fazer o que antes não conseguia:
- Decompor fatura de IA nos quatro termos e identificar qual está sangrando.
- Defender para o time técnico por que começar por roteamento de tier (não por poda de prompt) é a ordem correta.
- Montar o golden set mínimo para validar migração de tier.
- Propor sequência de 8 semanas de otimização estruturada.
- Saber quando parar (quando ganho marginal não paga o tempo de engenharia).

## NOTA FINAL
Estrutura: 6 | Pedagogia: 6 | Clareza: 6 | Autoridade: 7 | Durabilidade: 8 | Diferenciação: 8 | Memorização: 7 | Transformação: 7
**Nota Geral: 6.9**

## DECISÃO EDITORIAL
REVISAR PARCIALMENTE
*Correções críticas: resolver a tabela de percentuais não-aditivos (P0); adicionar analogia de abertura (P1); corrigir item 5 da autoavaliação que é copypaste de outro capítulo (P1); mover aviso metodológico para próximo aos percentuais (P1). O capítulo tem estrutura conceitual sólida mas está incompleto no desenvolvimento pedagógico — é o menos acabado dos cinco.*

---
---

# C19 — L1-C19-seguranca.md

## RESUMO EXECUTIVO
Nota: 8/10
Veredito: A

## O QUE FUNCIONA
- A taxonomia de prompt injection em quatro famílias (direta, indireta via contexto, indireta via tool, multi-turn) é precisa, atualizada com referências a CVE-2025-32711 e ao ataque Crescendo da Microsoft, e durável enquanto arquitetura de LLM não mudar radicalmente.
- A analogia do sistema imune em camadas é a mais tecnicamente precisa das cinco analogias dos capítulos — mapeia de forma justa (cada camada falha em fração de eventos; robustez vem de redundância).
- O Quadro 19.A (OWASP LLM Top 10 com definição, defesa e capítulo de aprofundamento em uma linha cada) é artefato de referência genuinamente útil — o CTO que tiver o quadro na parede vai usá-lo como mapa de decisão de investimento em segurança.
- A seção de red team sistemático (19.5) com as três métricas (taxa de bypass, severidade ponderada, tempo de detecção) é framework concreto que falta em quase todos os livros de IA corporativa.
- O caso do banco (19.6) é o mais rico em detalhe técnico dos cinco capítulos: vetor de ataque identificado (prompt injection indireta via PDF), três falhas de arquitetura compostas, remediação em quatro semanas, custo total do incidente, resultado regulatório. É um caso real-ish que vai ser citado em apresentações.
- A seção de conformidade (19.7) usa a Camada Dupla corretamente: apresenta o padrão durável (classificação por risco, trilha de auditoria, direito à explicação) e delega o texto específico para o Apêndice J.
- A seção 19.8 sobre contratar consultoria é pedagogicamente honesta: lista red flags explícitos que distinguem consultoria séria de teatro.

## O QUE NÃO FUNCIONA
- A referência à ANPD "Nota Técnica de 2026" aparece novamente (como em C16) como documento estabelecido sem data específica ou fonte verificável inline.
- O capítulo é longo (350+ linhas) sem resumo intermediário em cada subseção de 19.3. O leitor que perde o fio em 19.3.4 (model inversion) precisa rolar muito para voltar ao contexto.
- A menção a "EchoLeak (CVE-2025-32711)" como caso público é boa, mas o texto não explica o que é CVE para Joana, e essa é a única referência a CVE no capítulo.
- O checklist (19.10) tem 14 itens — o mais longo dos cinco capítulos. Para Joana, é intimidante. Para o CTO, é útil mas poderia ser dividido em "checklist executivo" (6 itens) e "checklist técnico" (8 itens).
- A frase de abertura da seção 19.3.6 descreve "EchoLeak (CVE-2025-32711)" sem contexto de que CVE é um identificador padronizado de vulnerabilidade. Leitor não-técnico pode não saber o que significa.

---

## ACHADOS

### ACHADO 01
Categoria: P1
Problema: CVE-2025-32711 (EchoLeak) é referenciado como "a CVE pública" sem explicação do que é CVE para o leitor não-técnico. Joana vai ler "CVE-2025-32711" e não saber se é um regulamento, um ataque, um produto ou um padrão.
Por que é um problema: O capítulo é explicitamente voltado para CTO, Head de Segurança E Head de Engenharia — o Head de Engenharia sabe o que é CVE, o CTO de fundo comercial provavelmente não.
Impacto no leitor: Joana (e CTOs não-técnicos) perdem a força do exemplo porque não entendem o que é CVE.
Correção exata: Adicionar definição inline na primeira menção: "(CVE — Common Vulnerabilities and Exposures: identificador público padronizado de vulnerabilidade de segurança; CVE-2025-32711 é o registro oficial do ataque EchoLeak)".
Texto sugerido: `...com o caso público de EchoLeak (CVE-2025-32711 — identificador padronizado de vulnerabilidade pública) ilustrando a classe em ambiente corporativo.`
ROI: MÉDIO

### ACHADO 02
Categoria: P1
Problema: O capítulo tem 350+ linhas de seção técnica (19.3) sem cabeçalhos de resumo intermediário ou "regra prática" no final de cada subseção. O leitor que chega em 19.3.4 (model inversion) depois de ter lido 19.3.1, 2 e 3 está sem âncora de onde está no mapa.
Por que é um problema: A seção 19.3 cobre seis classes de ataque diferentes. Um leitor não-especialista que pausar a leitura vai ter dificuldade de retomar no ponto correto.
Impacto no leitor: Joana lê 19.3.1 (prompt injection) com atenção, chega em 19.3.5 (PII leakage) com fadiga, e para. O capítulo perde a metade mais operacional.
Correção exata: Adicionar "Regra prática para [classe de ataque]:" ao final de cada subseção de 19.3 (como 19.3.1 já tem para as subseções de injeção, mas 19.3.4 e 19.3.5 são mais longas e se beneficiariam). Alternativamente, adicionar mini-sumário no início de 19.3: "Seis classes de ataque, de 19.3.1 a 19.3.6. Leia as que são mais relevantes para o seu contexto — o Quadro 19.A ao final organiza a defesa para cada uma."
Texto sugerido: `> **Mapa de 19.3:** Seis classes de ataque tratadas em sequência: (1) prompt injection, (2) jailbreak, (3) data poisoning, (4) model inversion, (5) PII leakage, (6) tool exploitation. O Quadro 19.A no final do capítulo organiza defesa e aprofundamento para cada uma.`
ROI: MÉDIO

### ACHADO 03
Categoria: P1
Problema: O checklist (19.10) tem 14 itens sem distinção entre itens executivos e itens técnicos. Para um Head de Segurança, 14 itens é gerenciável. Para um CEO ou CFO, é um muro.
Por que é um problema: A rubrica orienta que o capítulo serve para CTO, Head de Segurança e Head de Engenharia — mas a mistura de itens técnicos ("Listar as tools de cada agente e classificá-las em leitura segura ou escrita com efeito") com itens executivos ("Apontar o Accountable nomeado por ativação do kill switch") não diferencia bem os dois públicos.
Impacto no leitor: Executivos descartam o checklist por extensão; técnicos perdem os itens mais estratégicos no meio dos operacionais.
Correção exata: Dividir o checklist em dois blocos: "Checklist executivo (6 itens — para CTO e liderança)" e "Checklist técnico (8 itens — para Head de Segurança e AI Engineer)".
Texto sugerido: n/a (reorganização de estrutura)
ROI: MÉDIO

### ACHADO 04
Categoria: P1
Problema: A "Nota Técnica da ANPD sobre IA generativa" é referenciada em 19.7 como documento estabelecido ("A ANPD publicou orientação específica sobre IA generativa e tratamento de dado pessoal em vigor a partir de 2026") sem data específica ou verificação de que o documento existe exatamente com esse nome e vigência.
Por que é um problema: Igual ao problema em C16 — profissional de compliance que tentar citar o documento pode não encontrá-lo com esse nome exato.
Impacto no leitor: Perde credibilidade em apresentação ao DPO.
Correção exata: Adicionar marcação de verificação: "(Nota Técnica da ANPD — verificar versão corrente e título exato em www.gov.br/anpd conforme Apêndice J — Trilha do Número)"
Texto sugerido: n/a (inline na menção)
ROI: MÉDIO

### ACHADO 05
Categoria: P2
Problema: A regra "cadência mínima viável é trimestral" para red team (19.5) é apresentada como absoluta, mas não considera que organizações em fase inicial sem red team algum têm horizonte diferente de organizações com red team maduro. A regra de "se o último red team foi há mais de noventa dias, a organização não tem red team, tem auditoria pontual antiga" é implacável mas não oferece rota de construção progressiva.
Por que é um problema: Organização em fase inicial lê "não tem red team" e se sente paralisada sem saber como começar.
Impacto no leitor: Paralisia de excelência — "se não posso fazer trimestral, não faço nada".
Correção exata: Adicionar parágrafo de "rota de entrada para organizações sem red team": "Para organizações que nunca fizeram red team, o primeiro objetivo é conduzir a primeira sessão em 90 dias, com suite de 20 casos cobrindo as cinco categorias de maior risco do OWASP LLM Top 10 para o contexto específico. A cadência trimestral é o regime maduro; chegar a ele é processo de dois a três ciclos."
Texto sugerido: (parágrafo acima como inserção após a regra de 90 dias)
ROI: BAIXO

### ACHADO 06
Categoria: P2
Problema: A seção de PII leakage (19.3.5) menciona "Microsoft Presidio" como ferramenta padrão para redaction de PII, sem notar que é uma dependência externa com seu próprio ciclo de vida (o protocolo do capítulo anterior exigiria auditar o repositório do Presidio antes de depender dele).
Por que é um problema: Contradição leve com o método de C17 — o livro recomenda uma ferramenta específica sem aplicar o próprio protocolo de avaliação a ela.
Impacto no leitor: Menor — mas leitores atentos que acabaram de ler C17 vão notar a inconsistência.
Correção exata: Adicionar nota: "(Microsoft Presidio — referência comum em 2026; antes de adotar, aplique o protocolo de trinta minutos do Cap 17 para verificar fase do ciclo de vida)".
Texto sugerido: n/a (inline)
ROI: BAIXO

---

## TESTE DA JOANA
Entenderia: SIM (com atrito em 19.3)
O que ela entenderia: A analogia do sistema imune é imediatamente compreensível. O caso do banco (19.6) vai ser a parte que ela mais lembra — é concreto, tem resolução, tem custo. As perguntas para o time técnico no bloco "Para Executivos" são diretamente usáveis por ela.
O que ela NÃO entenderia: "Differential privacy", "adversarial embedding", "rate limiting por sessão" — termos técnicos que aparecem sem definição suficiente para executivo não-técnico. "CVE-2025-32711" sem explicação do que é CVE.
Como corrigir: Glossário inline para os termos mais técnicos; o Achado 01 já propõe a solução para CVE. Para "differential privacy", uma linha basta: "(técnica que adiciona ruído matemático ao treino para que nenhuma amostra individual do dataset possa ser extraída do modelo)".

## TESTE DE DURABILIDADE
Classificação: ALTA
2 anos: A taxonomia de prompt injection, a arquitetura de defesa em camadas, o Quadro 19.A do OWASP LLM Top 10 — tudo sobrevive. O OWASP vai ter versão 2026 e o capítulo faz isso correto ao referenciar "versão 2025" com data.
5 anos: O modelo do queijo suíço, os seis ataques como classes, a lógica de red team sistemático — todos duráveis. Nomes específicos de ferramentas (Lakera, NeMo Guardrails) podem mudar.
10 anos: Os princípios de defesa em camadas e da separação instrução/dado são duráveis enquanto modelos de linguagem operarem por processamento de tokens. Isso é estrutural.
Justificativa: Este é o capítulo com segunda maior durabilidade depois de C17. A taxonomia de ataques é independente de modelo específico; a arquitetura de defesa é independente de fornecedor.

## TESTE DE DIFERENCIAÇÃO
Classificação: DIFERENCIADO
Justificativa: A combinação de taxonomia de ataques + arquitetura de defesa em sete camadas + framework de red team com três métricas + caso de incidente com custos reais + guia de contratação de consultoria com red flags explícitos — esse pacote não existe em formato equivalente no mercado de livros de gestão de IA. É mais completo que Co-Intelligence (Mollick) e mais aplicado que Competing in the Age of AI (Iansiti/Lakhani).

## TESTE DE MEMORIZAÇÃO
Ideia principal clara? SIM
Qual é a ideia principal: "Defesa de IA mora fora do modelo — em sete camadas externas. A diferença entre incidente contornado e manchete de capa é o tempo de detecção e a maturidade do playbook, construídos antes do ataque."
Justificativa: A epígrafe, a analogia do sistema imune e a lição do caso do banco repetem a mesma ideia em registros diferentes. Memorável.

## TESTE DE TRANSFORMAÇÃO
Ao terminar, o leitor consegue fazer o que antes não conseguia:
- Distinguir prompt injection direta de indireta e saber por que a segunda é mais difícil de defender.
- Mapear o stack de IA da organização contra as dez categorias do OWASP LLM Top 10.
- Estruturar um programa de red team com cadência, composição de equipe e três métricas.
- Redigir o playbook de SEV-1 para vazamento de PII com Accountable nomeado.
- Distinguir consultoria de segurança séria de teatro de pentest tradicional.
- Fazer as três perguntas duras ao time técnico no dia seguinte à leitura.

## NOTA FINAL
Estrutura: 8 | Pedagogia: 7 | Clareza: 7 | Autoridade: 9 | Durabilidade: 9 | Diferenciação: 9 | Memorização: 8 | Transformação: 9
**Nota Geral: 8.3**

## DECISÃO EDITORIAL
MANTER COM AJUSTES
*Correções prioritárias: dividir checklist em executivo + técnico (P1); adicionar mini-mapa de navegação em 19.3 para capítulo longo (P1); definir CVE inline (P1); adicionar marcação de verificação à referência da Nota Técnica da ANPD (P1). O capítulo é sólido — as correções são de acessibilidade, não de conteúdo.*

---
---

# ALERTA DE DURABILIDADE CRUZADO (capítulos 15-19)

## Risco sistêmico detectado

**Catálogos residuais em C15 e C16:** Ambos os capítulos resistem razoavelmente à tese "Modelos passam. Método fica." mas carregam catálogo residual em tabelas de força por família (C15) e em versões específicas de modelos (C16). O risco não é fatal mas requer marcação datada consistente em todas as tabelas com nomes de produto.

**Preços de API em C16 e C18:** Os valores específicos de custo de inferência (Quadro 16.A e referências em C18) são os componentes de maior risco de obsolescência rápida. Em 18 meses, os preços de Claude Sonnet, GPT-4 e Gemini podem ter variado 30-60%. Recomendação: transformar todos os valores específicos de preço em templates com remissão ao Apêndice J.

**"Nota Técnica da ANPD sobre IA generativa de 2026":** Citada em C16 e C19 como documento estabelecido. Risco de o documento não existir com esse nome exato, ter sido revisado, ou ainda estar em consulta pública. Recomendação: verificar a existência e título exato do documento; adicionar marcação de "verificar versão corrente" em toda citação.

**C17 é o modelo correto:** O protocolo de 30 minutos de C17, por ser método puro sem inventário de nomes específicos, é o benchmark editorial que os outros capítulos deveriam aspirar. C15 e C16 ficam abaixo desse padrão por carregarem mais catálogo que necessário.

---

## LINHAS-TRACKER

```
C15|L1-C15-comparacao-modelos.md|01|P0|ALTO|Checklist item 1 instrui memorização de catálogo contradizendo tese do livro|Reformular item para aplicação do framework de decisão sem memorização de família|MANTER COM AJUSTES
C15|L1-C15-comparacao-modelos.md|02|P1|ALTO|Tabela de forças por família fixa associações sem sinalização de volatilidade|Adicionar cabeçalho de aviso datado e instrução de consulta ao Apêndice J|MANTER COM AJUSTES
C15|L1-C15-comparacao-modelos.md|03|P1|MÉDIO|xAI caracterizada por "tolerância maior a temas sensíveis" como vantagem neutra|Reescrever com nota sobre implicações de alignment conforme C23|MANTER COM AJUSTES
C15|L1-C15-comparacao-modelos.md|04|P1|MÉDIO|Lista de chips específicos em 15.6 envelhece sem entregar padrão durável|Reescrever para expressar tendência; colocar exemplos entre parênteses com marcação de snapshot|MANTER COM AJUSTES
C15|L1-C15-comparacao-modelos.md|05|P2|BAIXO|Erro tipográfico "Curiosidade " com espaço antes do fechamento de negrito em 15.14|Remover espaço extra|MANTER COM AJUSTES
C15|L1-C15-comparacao-modelos.md|06|P2|BAIXO|Pergunta de revisão 3 orientada a nomes de produtos específicos|Reformular para perguntar por critérios de encaixe sem nomear modelos|MANTER COM AJUSTES
C16|L1-C16-open-source.md|01|P0|ALTO|Quadro 16.A mostra Híbrido mais caro que API mas recomenda híbrido sem reconciliar|Adicionar explicação de que benefícios não-monetários justificam o custo marginalmente maior|MANTER COM AJUSTES
C16|L1-C16-open-source.md|02|P1|ALTO|Preços específicos de API no Quadro 16.A envelhecem em meses|Transformar em template com remissão ao Apêndice J|MANTER COM AJUSTES
C16|L1-C16-open-source.md|03|P1|MÉDIO|Números de versão de modelos no corpo do texto envelhecem antes da impressão|Remover números de versão do corpo; manter nomes de família com remissão ao Apêndice J|MANTER COM AJUSTES
C16|L1-C16-open-source.md|04|P1|MÉDIO|Nota Técnica ANPD citada como documento estabelecido sem data específica ou verificação|Adicionar marcação de verificação em toda citação|MANTER COM AJUSTES
C16|L1-C16-open-source.md|05|P2|BAIXO|Analogia da frota (16.2) longa demais para ritmo de livro executivo|Comprimir de quatro para dois parágrafos mantendo os quatro pontos|MANTER COM AJUSTES
C16|L1-C16-open-source.md|06|P2|BAIXO|Pergunta de revisão 5 cita "Nota Técnica ANPD de 2026" como dado memorável|Reformular para perguntar pelo padrão regulatório durável não pela data específica|MANTER COM AJUSTES
C17|L1-C17-github-repos.md|01|P1|ALTO|Referência de imagem usa cap-35 sendo o capítulo 17|Corrigir para cap-17 no caminho do arquivo SVG|MANTER COM AJUSTES
C17|L1-C17-github-repos.md|02|P1|MÉDIO|OpenInterpreter caracterizado com "governança em pessoa física com empresa em formação" — informação perecível que contradiz a filosofia do capítulo|Substituir por observação sobre aplicação do protocolo de verificação|MANTER COM AJUSTES
C17|L1-C17-github-repos.md|03|P1|MÉDIO|Regra de CI não exige CI presente — projeto sem CI passa no critério|Reformular para exigir CI presente E verde como critério de aprovação|MANTER COM AJUSTES
C17|L1-C17-github-repos.md|04|P2|BAIXO|W&B descrito sem destaque para implicação de self-hosting restrito|Adicionar frase sobre verificação de encaixe para organizações com restrição regulatória|MANTER COM AJUSTES
C17|L1-C17-github-repos.md|05|P2|BAIXO|Exemplo de 10 horas com 3 pessoas é ambíguo sobre se é 10h total ou por pessoa|Clarificar que é 10h total de sessão coletiva|MANTER COM AJUSTES
C18|L1-C18-economia-tokens.md|01|P0|ALTO|Tabela 18.7 com percentuais não-aditivos que somam mais de 200% sem explicação|Adicionar nota explícita de que os percentuais são compostos sequenciais não aditivos|REVISAR PARCIALMENTE
C18|L1-C18-economia-tokens.md|02|P1|ALTO|Capítulo não tem analogia de abertura para Joana — entra direto na fórmula matemática|Adicionar analogia de conta de energia com quatro termos como 18.2 introdutória|REVISAR PARCIALMENTE
C18|L1-C18-economia-tokens.md|03|P1|ALTO|Autoavaliação item 5 é copypaste de outro capítulo sobre segurança — não tem relação com economia de tokens|Substituir por critério de curiosidade relevante ao capítulo|REVISAR PARCIALMENTE
C18|L1-C18-economia-tokens.md|04|P1|MÉDIO|Framework F7 referenciado três vezes sem definição no capítulo|Adicionar mini-descrição inline na primeira menção|REVISAR PARCIALMENTE
C18|L1-C18-economia-tokens.md|05|P1|MÉDIO|Aviso metodológico de 18.1 está no início do capítulo onde é ignorado|Mover para próximo à tabela de percentuais onde os números aparecem|REVISAR PARCIALMENTE
C18|L1-C18-economia-tokens.md|06|P2|BAIXO|Razão premium/pequeno de "30 a 50 vezes" pode envelhecer com ajustes de pricing|Adicionar remissão ao Apêndice J inline|REVISAR PARCIALMENTE
C19|L1-C19-seguranca.md|01|P1|MÉDIO|CVE-2025-32711 referenciado sem explicação do que é CVE para leitor não-técnico|Adicionar definição inline de CVE na primeira menção|MANTER COM AJUSTES
C19|L1-C19-seguranca.md|02|P1|MÉDIO|Seção 19.3 com 6 classes de ataque sem mini-mapa de navegação intermediário|Adicionar mapa de navegação no início de 19.3 e regras práticas ao final de subseções longas|MANTER COM AJUSTES
C19|L1-C19-seguranca.md|03|P1|MÉDIO|Checklist com 14 itens mistura executivo e técnico sem distinção de público|Dividir em checklist executivo (6 itens) e checklist técnico (8 itens)|MANTER COM AJUSTES
C19|L1-C19-seguranca.md|04|P1|MÉDIO|Nota Técnica ANPD em 19.7 citada como documento estabelecido sem verificação|Adicionar marcação de verificação em toda citação da nota ANPD|MANTER COM AJUSTES
C19|L1-C19-seguranca.md|05|P2|BAIXO|Regra de cadência trimestral de red team sem rota de entrada para organização sem red team|Adicionar parágrafo de construção progressiva para fase inicial|MANTER COM AJUSTES
C19|L1-C19-seguranca.md|06|P2|BAIXO|Microsoft Presidio recomendado sem instrução de aplicar o protocolo de C17|Adicionar nota de verificação conforme protocolo de C17|MANTER COM AJUSTES
```
