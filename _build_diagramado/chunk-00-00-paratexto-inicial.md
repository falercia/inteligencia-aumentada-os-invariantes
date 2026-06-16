---
title: "Inteligência Aumentada"
lang: pt-BR
---



<section class="paratexto-inicial">
<div class="abertura-paratexto">

# Dedicatória

A quem aprende a ler o padrão por trás do número,
e ensina o próximo a fazer o mesmo.

A quem teve paciência com minhas ausências
enquanto este livro foi escrito.

Ao leitor que vai usar este conhecimento para construir,
não apenas para opinar.

</div>
</section>



<section class="paratexto-inicial">
<div class="abertura-paratexto">

# Por que este livro

> *Modelos passam. Método fica.*

---

## O que você vai dominar até a última página

Este não é um livro de "como usar IA". É um livro de **como pensar em IA**, com método transferível para o próximo modelo, para o próximo provedor, para a próxima onda regulatória. Os **Nove Princípios Permanentes** que sustentam toda a obra sobrevivem à troca de Claude, GPT, Gemini ou qualquer fronteira que ainda não foi lançada.

Ao terminar, você sai com:

- **Nove Princípios Permanentes** memorizáveis, que viram critério de decisão em reunião executiva, em revisão técnica e em conversa com fornecedor
- **Nove Frameworks operacionais** (F1 a F9): método de decisão para adotar IA, encaixe modelo×tarefa, escala de propriedade de agente, engenharia de prompt estendida, cobertura de integrações, governança indelegável, custo composto, pirâmide de avaliação, rota dupla de adoção
- **Vocabulário técnico profundo** sobre tokens, contexto, embeddings, RAG, memória, fine-tuning, agentes, MCP, reasoning models, evals, LLMOps, alignment, interpretabilidade mecanicista
- **Trinta exemplos memoráveis brasileiros** calibrados ao mercado nacional, com cargo, setor, números e desfecho que materializam decisão local, sem receita americana traduzida. O pacto editorial sobre a construção desses casos está declarado em *Sobre os Casos*, logo a seguir.
- **Trilhas de leitura por perfil** (Iniciante, Intermediário, Avançado, Express Executivo), com critério de recalibração quando a trilha não estiver servindo
- **Roadmap pessoal por persona** com horas semanais reais e critério de abandono explícito

---

## O que vive junto com este livro (executável e público)

O método mora no livro. O número e os artefatos vivem em **repositório acompanhante público**, com licença permissiva para uso comercial, atualizações públicas no repositório, sem cadência fixa anunciada, e contrato editorial declarado. O detalhamento aparece logo após o Mapa de Leitura. As sete pastas disponíveis hoje:

| Pasta | O que entrega |
|---|---|
| **`/prompts`** | 30 prompts profissionais em XML, com constituição, contexto, tarefa, formato, prefill e self-critique versionados, golden set por prompt e anti-padrões, prontos para clonar para o seu repositório interno |
| **`/governance`** | Caderno de Governança v1 em 6 seções fatiadas + caderno único de 6 páginas para imprimir e assinar + modelos clonáveis dos 6 anexos operacionais |
| **`/evals`** | `eval_runner.py` executável, `compile_golden_sets.py`, judges integrados, gate de CI e relatórios timestampados, para validar prompt contra golden set antes de cada release |
| **`/datasets`** | Golden sets em JSONL compilados a partir dos YAMLs originais, prontos para CI |
| **`/agents`** | Quatro agentes educacionais executáveis em Python puro (ReAct, Escala de Propriedade, Orquestrador-Especialistas e Multiagente Debate), com tools simuladas seguras, tracing local, gates e kill switch testável |
| **`/mcp`** | Servidores MCP educacionais (Hello World e Biblioteca Interna), com cliente de teste local e config-exemplo para Claude Desktop |
| **`/notebooks`** | 4 notebooks fundacionais executáveis — tokenização, *Lost in the Middle*, embeddings com busca semântica e prompt caching |

A combinação de livro + repositório é o que separa decisão informada de decisão de moda.

---

## Quem se reconhece nestas três promessas vai aproveitar a leitura

| Se você é... | Você sai daqui com... |
|---|---|
| **Executivo C-level / CTO / Head de Tecnologia** | Critério de decisão sobre adoção, custo, fornecedor e governança; caderno operacional pronto para o Conselho; arquitetura de defesa em camadas para conversar com auditor |
| **AI Engineer / Desenvolvedor / Arquiteto** | Stack técnica completa de AI Engineering em português, com engenharia de prompt profissional, agentes, MCP, evals e LLMOps; motor de avaliação executável para colocar em CI |
| **Profissional de outra área (advogado, médico, RH, professor)** | Vocabulário técnico genuíno sem diluição, frameworks de decisão aplicáveis ao seu domínio, prompts profissionais para clonar e adaptar |

---

## A diferença em uma frase

Quem só lê este livro sai com **método** que dura. Quem usa o repositório acompanhante acrescenta **ativos executáveis** prontos para produção. Quem opera só com o repositório sem ler o livro **opera no escuro**, porque não vai entender por que cada peça está naquela posição.

Boa leitura.

</div>
</section>



<section class="paratexto-inicial">
<div class="abertura-paratexto">

# Sobre os Casos desta Obra
## Pacto editorial de transparência

Esta obra usa, ao longo dos 29 capítulos, mais de 30 exemplos memoráveis como instrumento pedagógico, todos eles construídos como **compostos pedagógicos** a partir de padrões observados em organizações brasileiras reais, sem identificar a organização original. Estes casos aparecem em capítulos centrais como a engenharia de contexto da fintech, a stack de AI Engineering da seguradora, a operação de LLMOps da Pólice.io, a governança da seguradora em diálogo com a ANPD, os trade-offs do e-commerce de moda, o roadmap pessoal do CTO de varejo, o caso da indústria de embalagens de Joinville, a auditoria do banco médio em interpretabilidade mecanicista, e diversos outros. Os exemplos têm cargo, setor, números e desfecho calibrados ao mercado nacional, e foram desenhados para virar referência operacional do leitor. Nenhum deles é caso atribuído nominalmente nesta edição, e o quadro a seguir declara, sem rodeio, a categoria de cada um.

---

## Os três tipos de caso nesta edição

A obra opera com três tipos de caso, em proporções diferentes nesta primeira edição. O quadro abaixo declara qual é qual, e o que cada um permite ao leitor crítico.

| Tipo | O que é | Quantidade nesta edição | O que o leitor pode verificar |
|---|---|---|---|
| **Composto pedagógico** | Padrão observado em ≥2 organizações reais, com cargos, números e desfecho calibrados ao mercado BR. Não identifica a organização original. | **30+ casos · todos os memoráveis desta edição** | Plausibilidade do padrão. Não verifica número específico. |
| **Caso atribuído público** | Organização nomeada, com permissão explícita, número auditável, selo editorial específico. | **0 nesta edição. Sugestão de evolução: 3-5 em edição futura, conforme contribuições especialistas chegarem.** | Tudo: nome, número, desfecho, contato pós-publicação. |
| **Estudo ficcional declarado** | Caso explicitamente sintético usado para ilustração de conceito (ex: cenários adversariais). | Pontual, sempre marcado como tal | Apenas a lógica conceitual; não pretende ser real. |

---

## Por que esta edição usa compostos pedagógicos em vez de casos atribuídos

A escolha tem três razões, declaradas em ordem de peso.

| # | Razão | O que significa |
|---|---|---|
| 1 | **Proteção contratual** | Profissionais que compartilharam aprendizados em conversas privadas, consultorias ou sessões de revisão operam, em sua maioria, sob acordos de confidencialidade vigentes. Publicação nominal violaria compromissos legítimos. |
| 2 | **Proteção competitiva das organizações fonte** | Empresas brasileiras estão em estágio inicial de maturidade pública sobre IA. Expor decisões específicas, números reais e arquiteturas internas pode comprometer vantagem competitiva ou estratégia. |
| 3 | **Proteção de dados pessoais de envolvidos** | Muitos casos derivam de discussões com cargos identificáveis. Anonimizar o padrão preserva a privacidade dos profissionais que confiaram em conversa não-pública. |

---

## O custo da escolha, declarado

A escolha tem custo, e o custo é declarado: o leitor crítico não pode verificar diretamente cada número, cada decisão, cada resultado. Esse limite é fragilidade real, e a fragilidade não deve ser disfarçada.

O Apêndice N — Postura Metodológica trata, com mais profundidade, da classificação epistemológica dos números desta obra, em quatro classes (A, B, C, D), com critérios explícitos para cada classe e exemplos do que pertence a cada uma.

---

## Convite à atribuição em edições futuras

> **Caminho proposto, não compromisso vinculante.** Edições futuras desta obra poderão atribuir nominalmente entre **três e cinco casos memoráveis**, conforme empresas brasileiras se dispuserem a publicar artefato operacional sob selo editorial específico. O instrumento de adoção existe em documento interno do projeto, com critérios de elegibilidade, minuta de termo de autorização e questionário de coleta padronizado. A execução depende do interesse de empresas dispostas a publicar.

### Como participar, se você é executivo de empresa brasileira

Empresas brasileiras dispostas a publicar um caso real são convidadas, com seriedade e respeito ao tempo do leitor executivo, a contatar o autor via canal oficial da obra. Artefatos elegíveis incluem:

- Caderno de Governança aplicado, com decisões e maturidade declaradas
- Eval Harness em produção, com cobertura e cadência de revisão
- Pipeline de LLMOps instrumentado, com métricas de SLA real
- Decisão de adoção documentada, com critério explícito e resultado pós-12 meses
- Postmortem público de incidente material, com aprendizado consolidado
- Outro artefato operacional que demonstre o método em uso

Edições futuras poderão destacar casos atribuídos com selo editorial específico, com permissão explícita da organização e com cumprimento integral dos requisitos de LGPD e dos termos contratuais aplicáveis.

---

## Por que esta nota existe

Esta nota existe porque o pacto editorial precisa declarar com honestidade onde está a verificabilidade direta e onde está a fidelidade pedagógica. O leitor merece o pacto explícito, e o autor merece a responsabilidade de cumpri-lo.


</div>
</section>



<section class="paratexto-inicial">
<div class="abertura-paratexto">

# Prefácio

Liderando tecnologia há mais de quinze anos em empresas brasileiras, atravessei algumas ondas. Vi a nuvem deixar de ser controvérsia, vi mobile reorganizar canais inteiros, vi big data ser anunciado como revolução e absorvido sem barulho na operação. Cada onda chegou prometendo permanência, e cada uma, dentro de um intervalo previsível, foi substituída por outra que reivindicava a mesma permanência. O que ficou foram os princípios que cada ciclo revelou, raramente as ferramentas que ele trouxe.

A inteligência artificial chegou usando o mesmo manual de marketing, e por isso muita gente está cometendo com ela os mesmos erros de leitura. Confundindo velocidade com profundidade, adoção com competência, presença com domínio. Gastando muito mais tempo escolhendo qual modelo usar do que entendendo por que usar.

Mas a IA não é igual às outras ondas, e é o motivo direto deste livro existir.

## A diferença que muda tudo

A internet amplificou comunicação. O ERP amplificou processo. A nuvem amplificou infraestrutura. Cada uma reorganizou empresas e mercados, mas nenhuma amplificou diretamente aquilo que distingue um profissional do outro, uma decisão acertada de uma equivocada.

A IA amplifica julgamento. Amplifica capacidade de raciocínio. Amplifica, em quem sabe usar, a própria competência cognitiva, e amplifica, em quem não sabe, a própria mediocridade. É a primeira onda da minha carreira em que a ferramenta opera na mesma camada da competência humana mais cara, a de pensar. Por isso as analogias que vinham funcionando para explicar transformação tecnológica passam a falhar.

Em ondas anteriores, o que diferenciava as empresas era a capacidade de implementar. Em IA, o que diferencia é a capacidade de pensar antes de implementar. A vantagem migrou da execução para a interpretação. Quem entende isso reorganiza times, repensa governança, redesenha decisão. Quem não entende continua tratando IA como mais um sistema a contratar, e descobre, com atraso, que comprou tecnologia sem comprar critério.

## O erro que o mercado está cometendo

O erro mais comum cabe em uma frase. O mercado está estudando produtos quando deveria estar estudando princípios.

A obsessão é com benchmarks, rankings, versões, lançamentos. Empresas trocam fornecedor toda semana, equipes refazem prompts toda semana, dirigentes pedem estratégia de IA em reunião sem saber o que pediram. É um erro de categoria.

Em qualquer área madura, os profissionais mais respeitados são aqueles que dominam fundamentos, não ferramentas. Um arquiteto que entende estruturas sobrevive a qualquer software de cálculo. Um médico que entende fisiologia sobrevive a qualquer protocolo. Em tecnologia, cultivamos por décadas a ilusão de que dominar a ferramenta da moda é dominar a profissão. Conheciam o como, não conheciam o porquê. Quando o framework mudava, voltavam ao começo.

A obsessão por ferramentas produz dependência intelectual. Quem não tem critério próprio sempre precisa de alguém para dizer qual é a melhor ferramenta da semana. Quem tem critério escolhe sozinho, escolhe melhor, e revisa a escolha quando o cenário muda, sem precisar começar de novo a cada ciclo.

Em IA, essa diferença vai separar duas categorias de profissionais, e duas categorias de empresas, pelos próximos dez anos.

## Por que escrevi este livro

Podia ter feito o caminho fácil. Catálogo de prompts, tutorial de ferramentas, guia de adoção corporativa. Conteúdo desse tipo se publica em três meses, vende razoavelmente, e expira em outros três.

Recusei essa opção desde o primeiro rascunho. Os livros que sobrevivem na minha estante são os que ensinam a pensar, não os que ensinam a operar. O princípio dobra a década. A versão dura um trimestre.

A tese central deste livro cabe em quatro palavras. **Modelos passam, método fica.**

A obra estrutura essa tese em torno de **Nove Princípios Permanentes da Inteligência Artificial**. Nada na tecnologia é permanente no sentido absoluto, mas há padrões de pensamento que sobreviveram a múltiplas ondas e que provavelmente vão sobreviver a esta. São o que chamo de invariantes. O conjunto de critérios que permite ao profissional manter capacidade de julgamento mesmo quando o cenário muda completamente.

Construir um livro sobre invariantes, em uma época em que o mercado paga por novidade, é uma declaração editorial. Este livro decidiu não competir no eixo da velocidade, porque quem quer notícia tem newsletter, podcast, post, vídeo. Decidiu competir no eixo da profundidade. Tudo que envelhece em três meses não merece ser livro. Livro deve ser aquilo que ainda vai estar de pé dez anos depois.

Há ainda uma convicção que orientou cada decisão editorial. Quis escrever um livro que respeitasse o leitor brasileiro. Que não diluísse. Que assumisse que profissional brasileiro lê texto técnico denso quando o texto é honesto, e que iniciante brasileiro merece a mesma profundidade conceitual oferecida a iniciante americano.

## O que está em jogo

Vantagem competitiva real raramente vem do acesso à ferramenta nova. Quase sempre, vem da capacidade de compreender, mais cedo, com mais profundidade e com mais clareza, o que aquela ferramenta significa.

Acesso democratiza. Compreensão diferencia.

Quem soube ler a internet em 1996 ganhou uma década. Quem soube ler a nuvem em 2008 ganhou uma década. Quem souber ler a IA agora vai ganhar a próxima. Não por ter acesso, porque acesso, hoje, é commodity. Vai ganhar por compreender, mais profundamente que os outros, o que essa onda específica está reorganizando no mundo.

Compreender, em ambiente saturado de informação rasa, é um ato de disciplina. É o exercício deliberado de buscar o princípio quando todos correm atrás da versão. É a teimosia intelectual de aprender o que dura, em um mercado que insiste em ensinar o que passa.

As próximas páginas são, antes de tudo, um convite a esse exercício. Não é leitura confortável, nem rápida, nem que se esgota em uma viagem de avião. Se em algum momento o texto pedir demais, é porque está fazendo a parte dele do contrato.

Modelos vão continuar passando. Quem dominar o método vai continuar de pé.

Compreender, no fim das contas, sempre foi a vantagem competitiva mais subestimada da história da tecnologia. E sempre foi a única que durou.

Boa leitura.

</div>
</section>



<section class="paratexto-inicial">
<div class="abertura-paratexto">

# Como Ler Este Livro

---

## A obra opera com três caminhos de leitura

Esta obra foi projetada para servir leitores em estágios e contextos diferentes. Cada caminho responde a uma intenção distinta, e quem usa o livro mais de uma vez tende a percorrer todos eles em ordens diferentes.

**Caminho 1 — Linear.** Comece pela Introdução e siga até o último capítulo. A ordem foi pensada em curva de aprendizado deliberada, com cada conceito construindo sobre o anterior. É o caminho recomendado para quem está começando.

**Caminho 2 — Por interesse.** Cada capítulo é autocontido o suficiente para ser lido isoladamente, e o leitor que aterriza no meio do livro vai encontrar as referências de que precisa. As trilhas temáticas estão organizadas no Mapa de Leitura por Nível, a seguir.

**Caminho 3 — Pelos princípios.** Este é o caminho que mais diferencia o uso profissional do livro. Em vez de ler em ordem de página, leia pela camada-mãe. Parta de um dos nove princípios, percorra o capítulo onde ele é tratado em profundidade, depois os capítulos que o instanciam em outros temas, depois o framework derivado, depois o exemplo correspondente. É a forma mais rápida de internalizar o vocabulário que dá nome ao livro.

> **A escolha por nível de experiência, as horas estimadas, os roteiros por orçamento de tempo e o critério de recalibração estão no Mapa de Leitura por Nível, logo após o Sumário.**

---

## Como cada capítulo funciona

Os capítulos seguem uma arquitetura pedagógica recorrente, não por convenção, mas porque ela espelha como adultos profissionais realmente aprendem conceito novo. A anatomia de cada capítulo, em quadro de bolso:

| Bloco | O que faz | Por que está aí |
|---|---|---|
| Abertura | Provoca, ancora o porquê | Engajamento antes de carga cognitiva |
| Conceito intuitivo | Estabelece a ideia central em linguagem simples | Modelo mental antes do rigor |
| Analogia | Conecta o novo com o conhecido | Transferência de conhecimento prévio |
| Explicação técnica | Aprofunda com rigor controlado | Profundidade sob a intuição |
| Diagrama | Visualiza o que palavras não conseguem | Compressão cognitiva |
| Exemplo brasileiro | Materializa em composto pedagógico calibrado ao mercado BR (ver *Sobre os Casos*) | Plausibilidade local |
| Quando usar / quando evitar | Constrói framework de decisão | Regra prática operacional |
| Resumo executivo | Síntese de 30 segundos | Recuperação rápida em consulta |
| Checklist + revisão + exercícios | Fixação ativa | Aprendizado durável |
| Autoavaliação | Filtro objetivo de "estou pronto?" | Honestidade pedagógica |

Não pule as perguntas de revisão, os exercícios e a autoavaliação. São onde o conhecimento se fixa.

---

## Convenções visuais

Algumas marcas pontuais atravessam toda a obra. Cada uma tem função única e a obra é consistente no uso.

| Marca | Função |
|---|---|
| **Citação destacada** | Frase-chave memorável, recortável para post ou citação |
| **▲ Alerta** | Armadilha comum ou cenário ilustrativo de risco |
| **✸ Insight** | Sacada conceitual importante que merece pausa |
| **Para Executivos** | Conexão direta com decisão de negócio |
| **Na Prática** | Aplicação imediata na operação |
| **Diagrama** | Visualização densa que sintetiza relações |
| **Referência** | Fonte primária externa, com URL ou DOI quando aplicável |

---

## O que fazer ao terminar

Terminar o livro não é o fim do aprendizado, é o início da operação. A lista abaixo é o protocolo de consolidação, em ordem de retorno.

1. **Refazer os exercícios** dos capítulos que sentiu mais difíceis. Repetição espaçada vale mais que releitura passiva.
2. **Voltar ao mapa mental** nos apêndices e explicar cada nó em voz alta. Se travar, releia o capítulo correspondente.
3. **Executar o roadmap por persona** para consolidar prática em ciclo curto.
4. **Identificar três áreas** de aprofundamento e buscar os papers indicados nos apêndices.
5. **Assinar duas newsletters** recomendadas e criar hábito de manutenção semanal.
6. **Consultar a documentação atualizada** dos fornecedores periodicamente para reajustar decisões à fronteira atual.

---

> *A leitura não termina o aprendizado. Ela começa.* A diferença real entre quem leu e quem domina está na aplicação dos princípios na próxima decisão.

</div>
</section>



<section class="paratexto-inicial">
<div class="abertura-paratexto">

# INTRODUÇÃO
## Por que este livro existe

---

> *"Quando uma tecnologia muda mais rápido do que sua capacidade de entendê-la, você perde duas coisas ao mesmo tempo: o controle e a oportunidade. Quando uma obra técnica envelhece junto com a tecnologia que documenta, o leitor que confiou nela perde a terceira: o instrumento que escolheu para se proteger."*

---

## A CENA QUE SE REPETE

Você provavelmente já viveu, ou viu alguém viver, esta cena que tem se repetido em milhares de reuniões executivas pelo país nos últimos dois anos. Uma sala com diretoria sentada, slide projetado com o título "Estratégia de IA para 2026", e o diretor de tecnologia apresentando uma arquitetura cheia de siglas — LLM, RAG, MCP, fine-tuning, embeddings, agentes — com setas conectando caixas que ninguém na sala consegue explicar em profundidade. A diretoria assente, faz perguntas educadas sobre cronograma e orçamento, evita perguntas técnicas para não parecer desinformada, e em vinte minutos decisões de milhões de reais são tomadas com base em entendimento superficial do que está sendo proposto.

Saindo da reunião, dois executivos no corredor, sem testemunhas. Um pergunta baixinho, "você entendeu de verdade o que ele propôs?". O outro responde, "mais ou menos, mas pareceu sólido, vamos seguir". Multiplique essa cena por milhares de empresas, por milhões de profissionais, e está pintado o retrato de uma geração inteira tomando decisões sobre IA sem ter o modelo mental necessário para validar essas decisões. Esse é o problema que este livro existe para resolver.

---

## A LACUNA QUE NINGUÉM ASSUME

Vale ser direto sobre algo desconfortável que tem implicações sérias para quem trabalha com tecnologia em 2026. A maior parte dos profissionais, incluindo muitos seniores com salários generosos e currículos respeitáveis, opera com entendimento bastante superficial de IA moderna. Sabe usar ChatGPT, sabe escrever prompts decentes, talvez tenha brincado com uma API em algum projeto paralelo. Mas quando a conversa desce um nível, a coisa muda.

Por que tokens custam mais em modelos diferentes? O que exatamente acontece dentro de uma janela de contexto, em termos arquiteturais? Como embeddings transformam significado em geometria, e por que isso permite busca semântica? Por que RAG existe como padrão arquitetural, em quais situações ele falha, e o que fazer quando falha? O que diferencia tecnicamente um agente de um chatbot com retrieval? Como MCP muda a arquitetura de sistemas, e por que esse padrão está se consolidando como referência? Quando fine-tuning é desperdício de dinheiro, e em quais situações específicas ele é necessário? Como se mede um sistema de IA antes de soltar em produção? Como se opera IA em produção sem que ela vire incidente? Quem responde quando algo dá errado? A resposta para essas perguntas, na maioria dos casos que aparecem em campo, é silêncio constrangido ou explicação rasa que não sobrevive a uma segunda pergunta.

Não é culpa do profissional. É culpa de uma lacuna na literatura, que em português ainda não foi preenchida. Em inglês existem obras profundas; em vídeo, canais excelentes; em fóruns, discussões ricas. Em português, ainda em 2026, não há uma obra que cubra tudo isso com profundidade real, em linguagem executiva, conectando conceito a prática a impacto de negócio. Esta é a tentativa de fechar essa lacuna, com a aposta de que o leitor brasileiro está pronto para esse nível de conteúdo desde que ele seja oferecido com clareza, sem academicismo nem condescendência.

---

## AS QUATRO APOSTAS DESTE LIVRO

### Aposta 1 — Conceitos sobre ferramentas

Modelos mudam a cada três meses, plataformas mudam a cada seis, frameworks vêm e vão. Mas os conceitos — token, contexto, embedding, atenção, raciocínio, agência, custo composto, eval, autonomia proporcional — permanecem, e são o esqueleto sobre o qual toda nova ferramenta é construída. Investir tempo em conceitos é investir em fundação que não envelhece; investir tempo apenas em ferramentas é correr atrás de algo que sempre vai mudar de lugar antes de ser dominado.

### Aposta 2 — Mas conceitos sem aplicação são abstração morta

Existe uma tradição perigosa em livros de tecnologia: tratar conceitos como se vivessem no vácuo. O autor explica RAG no abstrato, agentes no abstrato, MCP no abstrato, e o leitor termina sabendo definir cada termo, mas sem ter visto um único exemplo profundo em produção real. Quando vai aplicar, descobre que a teoria não basta.

A aposta desta obra é diferente: cada conceito é apresentado com aplicação imediata, compostos pedagógicos calibrados ao mercado brasileiro a partir de padrões observados em organizações reais, e exemplos extraídos do uso profissional dos modelos comerciais atuais — GPT, Claude, Gemini, Llama —, sem que nenhum deles vire fundamento. Os fornecedores aparecem para ilustrar, não para sustentar. O pacto editorial sobre verificabilidade dos casos está declarado em *Sobre os Casos*, antes da introdução.

### Aposta 3 — Profundidade sobre cobertura rasa

Existe uma tentação editorial recorrente: cobrir tudo superficialmente, com promessas como "100 ferramentas de IA em 100 páginas". Esse formato vende bem, mas não forma profissional. A aposta aqui é oposta: menos temas tratados em mais profundidade, e cada capítulo aprofunda até o ponto em que o conceito fica realmente assentado, não apenas memorizado.

### Aposta 4 — Sistema citável próprio

Esta é a aposta mais ambiciosa do livro, e a que mais o distingue da literatura existente. Em vez de simplesmente cobrir os tópicos com excelência, a obra propõe um sistema citável que costura tudo: os **nove princípios permanentes da inteligência artificial**. São os princípios que decidem se a IA funciona, independentemente do modelo da semana. Cada princípio tem regra, mecânica e violação típica. Cada capítulo declara, na primeira página, qual princípio instancia. Cada framework proprietário deriva de um princípio. Cada estudo de caso ilustra um conjunto deles em decisão real.

Quem termina o livro não sai sabendo apenas o vocabulário técnico. Sai com um sistema de decisão que pode ser invocado em reunião — "estamos violando o princípio do encaixe nessa migração", "essa proposta passa pelo termômetro?", "quem é o nome humano que responde pela indelegabilidade?" — e que continua válido enquanto a função da IA for amplificar trabalho humano.

---

## O ARCO NARRATIVO

Você vai percorrer cinco grandes territórios. A introdução apresenta os nove princípios como sistema citável que costura toda a obra. Os fundamentos cobrem o que é IA, como modelos funcionam, tokens, contexto, embeddings, RAG, memória e fine-tuning. Em seguida, prompts e raciocínio — engenharia de prompt, chain of thought, engenharia de contexto. Depois, agentes e IA moderna — agentes, MCP, AI Engineering. Adiante, modelos — comparação por encaixe e modelos open source. A última parte traz os temas avançados e definitivos: economia de tokens, segurança e riscos, futuro, avaliações, operação em produção, alinhamento, governança, trade-offs canônicos e roadmap pessoal e organizacional.

Cada parte é uma camada de competência, e cada capítulo é uma peça que se encaixa no quadro maior. A ordem é deliberada. Ainda que cada capítulo seja autocontido o suficiente, ler na sequência produz aprendizado mais robusto do que pular para o que parece imediatamente útil.

---

## A PROMESSA

Ao terminar este livro, o leitor deve ser capaz de fazer dez coisas específicas que separam quem entende de quem só usa. Vale registrar de forma direta para que a obra possa ser cobrada ao final.

1. Recitar os nove princípios, descrever a mecânica de cada um, e identificar a violação típica em sua própria operação.
2. Explicar IA moderna em três níveis de profundidade — leigo, gestor, técnico —, usando analogias e exemplos.
3. Avaliar criticamente uma proposta de arquitetura de IA, saber quais perguntas fazer, e reconhecer quando algo não bate.
4. Decidir com critério entre RAG, fine-tuning, engenharia de prompt ou nenhuma das anteriores, para um problema concreto.
5. Construir prompts profissionais que produzem resultados consistentes, com método e estrutura pelas extremidades.
6. Entender agentes como classe de software, sabendo quando usá-los, quando evitá-los, e qual nível de autonomia é proporcional à observabilidade disponível.
7. Medir sistema de IA com golden set, LLM-as-judge calibrado e regressão em CI.
8. Operar IA em produção com tracing, versionamento, deploy progressivo, rollback testado e gestão de custo composto.
9. Governar IA corporativa com RACI assinado, política de incidente testada, accountability nominal e controles canônicos.
10. Tomar decisões de carreira e de negócio com base em entendimento real e sistema próprio, não em discurso de fornecedor.

---

## UMA ÚLTIMA COISA ANTES DE COMEÇAR

A IA não vai esperar ninguém se atualizar. Essa é uma realidade dura que vale internalizar antes de virar a próxima página. A cada mês que passa sem investimento em entendimento, a distância entre quem domina e quem apenas usa cresce. Em 2026 essa distância já é visível em conversas executivas, em decisões de carreira, em quem é convidado para projetos estratégicos. Em 2028, segundo as projeções mais conservadoras, essa distância será inegociável.

Há duas opções. A primeira é continuar usando IA como ferramenta de consulta esporádica, aceitando que outras pessoas vão entender mais do que você sobre algo que vai redefinir profundamente sua carreira nos próximos anos. A segunda é investir entre trinta e cinco e cinquenta horas neste livro, e sair com base sólida que vai diferenciar pelos próximos dez anos. Se a escolha é a segunda, vire a página.

Os nove princípios começam na próxima.

</div>
</section>



<section class="paratexto-inicial">
<div class="abertura-paratexto">

# SUMÁRIO
## *Inteligência Aumentada · Os Princípios Permanentes da IA*

---

## PARATEXTO INICIAL

| Seção | pg |
|---|---:|
| Dedicatória | ii |
| Por que este livro — proposta de valor e ganhos por perfil | iii |
| Sobre os Casos desta Obra — pacto editorial | vi |
| Prefácio | xi |
| Como Ler Este Livro | xv |
| Introdução | xxi |
| Sumário (este) | xxvii |
| Mapa de Leitura por Nível | xxxiii |
| Repositório Acompanhante | xlii |

---

## OS NOVE PRINCÍPIOS PERMANENTES

| Seção | pg |
|---|---:|
| Manifesto — Os Nove Princípios Permanentes da Inteligência Artificial | 1 |
| Por que Padrão Dura e Número Morre — fundação intelectual da Camada Dupla | 22 |

---

## PARTE 1 — FUNDAMENTOS DA INTELIGÊNCIA ARTIFICIAL · pg 34

| # | Capítulo | Princípio central |
|---|----------|-------------------|
| 1 | O Que É Inteligência Artificial | Camada Dupla |
| 2 | Como os Modelos de IA Funcionam | Plausibilidade |
| 3 | Tokens | Custo Composto |
| 4 | Janela de Contexto | Extremidades |
| 5 | Embeddings | Camada Dupla, Custo Composto |
| 6 | RAG — Retrieval Augmented Generation | Camada Dupla, Termômetro |
| 7 | Memória em IA | Custo Composto |
| 8 | Fine-Tuning | Termômetro |

---

## PARTE 2 — ENGENHARIA DE PROMPT E RACIOCÍNIO · pg 146

| # | Capítulo | Princípio central |
|---|----------|-------------------|
| 9 | Engenharia de Prompt | Extremidades, Termômetro |
| 10 | Chain of Thought e Raciocínio | Plausibilidade, Extremidades |
| 11 | Context Engineering | Extremidades, Camada Dupla |

---

## PARTE 3 — AGENTES E IA MODERNA · pg 187

| # | Capítulo | Princípio central |
|---|----------|-------------------|
| 12 | Agentes de IA | Autonomia Proporcional |
| 13 | MCP — Model Context Protocol | Encaixe, Autonomia Proporcional |
| 14 | AI Engineering | Termômetro, Autonomia Proporcional |
| 14C | Spec-Driven Development | Operador, Camada Dupla, Autonomia Proporcional, Responsabilidade Indelegável |
| 14B | Reasoning Models | Plausibilidade, Extremidades, Custo Composto |

---

## PARTE 4 — MODELOS DE IA · pg 259

| # | Capítulo | Princípio central |
|---|----------|-------------------|
| 15 | Comparação dos Principais Modelos | Encaixe |
| 16 | Modelos Open Source | Encaixe, Custo Composto |

---

## PARTE 5 — TÓPICOS AVANÇADOS · pg 298

| # | Capítulo | Princípio central |
|---|----------|-------------------|
| 17 | Repositórios GitHub — método de auditoria em 30 minutos | Termômetro, Operador |
| 18 | Economia de Tokens em Profundidade | Custo Composto |
| 19 | Segurança em IA — anatomia de ataque, arquitetura de defesa | Responsabilidade Indelegável, Plausibilidade |
| 20 | O Futuro da IA em Cenários Estruturados | Camada Dupla |
| 21 | Avaliações — A Engenharia de Medir IA | Termômetro |
| 22 | LLMOps — Operação de IA em Produção | Autonomia Proporcional |
| 23 | Alinhamento — Mito, técnica e prática | Responsabilidade Indelegável, Plausibilidade |
| 24 | Governança de IA Corporativa | Responsabilidade Indelegável |
| 25 | Trade-offs Canônicos da IA | Encaixe, Operador |
| 26 | Roadmap Pessoal de IA — horas, prerrequisitos e critério de abandono | Operador |
| 27 | IA para PME Brasileira | Operador, Custo Composto, Encaixe |
| 28 | Interpretabilidade Mecanicista | Plausibilidade, Responsabilidade Indelegável |

---

## FRAMEWORKS DA OBRA

| Framework | Princípio central | pg |
|-----------|-------------------|---:|
| F1 — Método de Decisão para Adotar IA | Operador | 630 |
| F2 — Diagnóstico de Encaixe entre Tarefa e Modelo | Encaixe | 634 |
| F3 — Escala de Propriedade do Agente | Autonomia Proporcional | 639 |
| F4 — Engenharia de Prompt Estendida | Extremidades, Camada Dupla | 644 |
| F5 — Matriz de Cobertura de Integrações | Autonomia Proporcional, Encaixe | 649 |
| F6 — Governança Indelegável | Responsabilidade Indelegável | 660 |
| F7 — Custo Composto em Três Tempos | Custo Composto, Operador | 665 |
| F8 — Pirâmide da Avaliação | Termômetro | 670 |
| F9 — Rota Dupla de Adoção | Camada Dupla | 676 |

---

## APÊNDICES

| ID | Apêndice | pg |
|----|----------|---:|
| A | Glossário Completo | 681 |
| B | Mapa Mental Geral | 689 |
| C | Roadmaps Detalhados por Persona | 698 |
| D | Ferramentas e Stack — curadoria datada | 706 |
| E | Leituras Complementares | 718 |
| F | Comunidade Brasileira de IA em 2026 | 721 |
| G | Papers Fundamentais | 730 |
| H | Bibliografia Completa | 735 |
| I | Índice Remissivo | 741 |
| J | Trilha do Número — versões, preços, benchmarks, papers, regulação datados | 746 |
| K | Gabaritos Comentados | 762 |
| L | Biblioteca de Prompts Profissionais — 30 fichas | 767 |
| M | Manifesto de Bolso — Os Nove Princípios em Uma Página | 825 |
| N | Postura Metodológica sobre os Números desta Obra | 829 |
| O | Caderno de Governança v1 | 837 |
| P | Boxes Técnicos — 11 boxes técnicos | 849 |
| Q | Manual do Professor — planos de curso, projeto final, rubrica | 882 |

---

**Após os apêndices:** Sobre o Autor.

</div>
</section>



<section class="paratexto-inicial">
<div class="abertura-paratexto">

# MAPA DE LEITURA POR NÍVEL
## A partir de onde você está

A maior parte dos livros técnicos densos cobra do leitor um preço alto quando ele tenta ler linearmente sem reconhecer o próprio ponto de partida. O iniciante absoluto trava em capítulos avançados e abandona; o profissional experiente perde tempo nos capítulos iniciais e desiste na metade; o cientista de dados pula direto para a profundidade técnica e perde a costura conceitual que sustenta o sistema. Esta nota existe para evitar os três destinos.

A obra é desenhada para três níveis de leitor, e cada nível tem trilha recomendada de leitura, com volume horário estimado e capítulos prioritários. O leitor honesto faz primeiro o diagnóstico de cinco perguntas abaixo, identifica o próprio nível, e segue a trilha correspondente. As trilhas por nível são subsets enxutos: quem quiser leitura integral encontra o roteiro de cinquenta horas mais adiante, na seção *Roteiros de leitura por orçamento de tempo*.

---

## Diagnóstico em cinco perguntas

Responda sim ou não para cada uma, com honestidade.

| # | Pergunta | Sim | Não |
|---|---|:---:|:---:|
| 1 | Sabe explicar, com analogia ou linguagem técnica, o que é um *embedding* e por que ele importa em sistemas modernos de IA? | ☐ | ☐ |
| 2 | Já operou, em ambiente profissional, um *agente* baseado em LLM, com loop de planejamento, ação e observação? | ☐ | ☐ |
| 3 | Lê papers técnicos no arXiv ou em conferências (NeurIPS, ICML, ACL, ICLR) com regularidade suficiente para reconhecer trabalhos recentes do campo? | ☐ | ☐ |
| 4 | Consegue explicar, em pelo menos linguagem intermediária, como funciona o mecanismo de *attention* em arquiteturas Transformer? | ☐ | ☐ |
| 5 | Já conduziu, em produção ou em projeto-piloto sério, processo de *fine-tuning* ou de *engenharia de prompt* em escala, com métrica de qualidade auditável? | ☐ | ☐ |

### Sua trilha pela contagem de "sim"

| Sim | Seu nível | Trilha recomendada |
|:---:|---|---|
| **0-2** | Iniciante absoluto | Trilha INICIANTE (12h em 4 semanas) |
| **3-4** | Intermediário | Trilha INTERMEDIÁRIO (30h em 6-8 semanas) |
| **5** | Avançado ou especialista | Trilha AVANÇADO (18h focadas + leitura cruzada) |

### Fluxo entre trilhas

| Trilha atual | Avança quando | Recua quando |
|---|---|---|
| **Iniciante** | Consolida C5 (embeddings) + C9 (engenharia de prompt) com autoavaliação ≥ 4/5 em três capítulos seguidos | — |
| **Intermediário** | Opera C11 (context) + C14 (AI engineering) + C21 (evals) em produção, com critério explícito | Três autoavaliações seguidas < 3/5 → volta para Iniciante |
| **Avançado** | — | Três autoavaliações seguidas < 3/5 em capítulo avançado → volta para Intermediário |

Voltar uma trilha é movimento normal, não custo de orgulho. Avançar acontece naturalmente conforme a base consolida.

---

## Trilha do leitor INICIANTE ABSOLUTO

**Pressupostos:** nunca operou IA generativa regularmente em ambiente profissional, não domina vocabulário básico (prompt, token, modelo, fine-tuning, embedding), entrou na obra para construir base sólida.

**Volume estimado:** cerca de doze horas de leitura ativa, em quatro semanas.

**Capítulos prioritários, em ordem de leitura:**

| Ordem | Item | Por que vir agora |
|---|---|---|
| 1 | Manifesto C00P — Por que padrão dura e número morre | Fundação intelectual; lê em qualquer nível |
| 2 | Manifesto C00M — Os Nove Princípios Permanentes | Espinha da obra; lê com calma |
| 3 | C1 — O que é IA | Contexto histórico e conceitual mínimo |
| 4 | C2 — Como modelos funcionam | Versão intuitiva da arquitetura |
| 5 | C3 — Tokens | Conceito que abre tudo o resto |
| 6 | C4 — Janela de contexto | Limite prático que estrutura uso real |
| 7 | C5 — Embeddings | Conceito fundamental para entender RAG |
| 8 | C9 — Engenharia de prompt | Habilidade prática imediata |
| 9 | C26 — Roadmap pessoal | Define o próximo passo para seu caso |
| 10 | Apêndices A (glossário) e B (mapa mental) | Consulta permanente |

**Pular nesta primeira passada:** C11, C14, C21, C22, C28, todos os frameworks F3 a F9, Apêndices L, P, O. Voltar a eles quando o vocabulário e os fundamentos estiverem consolidados.

---

## Trilha do leitor INTERMEDIÁRIO

**Pressupostos:** usa IA generativa regularmente, opera prompts profissionais, conhece vocabulário básico, busca sistematizar conhecimento, ampliar profundidade técnica e instalar disciplina executiva.

**Volume estimado:** cerca de trinta horas de leitura ativa, em seis a oito semanas.

**Trilha completa, com prioridades:**

| Prioridade | Capítulos e Frameworks |
|---|---|
| **Alta** | C00P, C00M, C6 (RAG), C7 (memória), C9, C10 (chain of thought), C11 (context engineering), C12 (agentes), C13 (MCP), C14 (AI Engineering), C18 (economia de tokens), C24 (governança), C25 (trade-offs), C26 (roadmap), C27 (PME se for fundador) |
| **Frameworks essenciais** | F1 (decisão), F2 (encaixe), F4 (prompt estendido), F6 (governança), F7 (custo), F8 (avaliação) |
| **Apêndices essenciais** | L (biblioteca de prompts), J (trilha do número), O (caderno de governança), D (ferramentas) |
| **Média** | C8 (fine-tuning), C15 (comparação), C16 (open source), C19 (segurança), C20 (futuro), C21 (evals), C22 (LLMOps), C23 (alignment) |
| **Frameworks médios** | F3 (agente), F5 (cobertura), F9 (rota dupla) |
| **Apêndices médios** | M (síntese), N (metodológico), P (boxes técnicos) |

**Pular nesta primeira passada:** C14B (reasoning models — voltar quando estiver operando reasoning em produção), C28 (interpretabilidade mecanicista — voltar quando enfrentar caso regulatório real), C17 (auditoria de repositórios — usar como referência operacional). Apêndice Q (Manual do Professor) somente se for docente.

---

## Trilha do leitor AVANÇADO ou ESPECIALISTA

**Pressupostos:** trabalha com IA em produção, lê papers, opera evals e LLMOps, busca sistema próprio coeso, profundidade técnica em pontos centrais e diferenciação intelectual da obra.

**Volume estimado:** cerca de dezoito horas focadas em capítulos centrais, com leitura cruzada do restante.

**Trilha prioritária:**

| Bloco | Capítulos e itens |
|---|---|
| **Sistema intelectual** | C00P, C00M, F3, F8, F9 |
| **Núcleo técnico** | C11 (context engineering), C14 (AI Engineering), C14B (reasoning models), C21 (evals), C22 (LLMOps), C23 (alignment) |
| **Fronteira técnica** | C28 (interpretabilidade), Apêndice P (boxes técnicos), Apêndice J (trilha do número) |
| **Operação rigorosa** | C19 (segurança), C24 (governança), C25 (trade-offs), Apêndice O (caderno) |
| **Diferenciação** | Apêndice N (postura metodológica), F6 (governança indelegável) |

**Apêndices de referência permanente:** N, P, J, O, L.

**Não precisa ler na primeira passada:** C1 a C4 (revisão de fundamentos — pode pular ou ler em diagonal), C27 (PME — só se for atuar em consultoria neste segmento), Apêndice Q (somente se for docente).

---

## Bandeira por capítulo

Para o leitor que quiser identificar rapidamente o público primário de cada capítulo, a obra mantém a seguinte classificação:

| Nível primário | Capítulos |
|---|---|
| **Iniciante** | C1, C2, C3, C4, C9 |
| **Iniciante + Intermediário** | C5, C6, C7, C8 |
| **Intermediário** | C10, C11, C12, C13, C15, C16, C18, C24, C25, C26, C27 |
| **Intermediário + Avançado** | C14, C19, C20, C21, C22 |
| **Avançado / Especialista** | C14B, C17, C23, C28 |
| **Todos os níveis (fundação)** | Manifesto C00P, Manifesto C00M |

Frameworks (F1 a F9) e Apêndices são consulta permanente, não leitura sequencial obrigatória.

---

## Roteiros de leitura por orçamento de tempo

**8 horas (executivo com agenda apertada):**
C00P → C00M → F1 (Método de Decisão) → C24 (governança) → C25 (trade-offs) → C26 (roadmap pessoal) → Apêndice O (caderno) → Apêndice M (síntese de bolso).

**20 horas (intermediário em primeira passada):**
Manifestos C00P e C00M → C1 a C9 em ritmo regular → C11, C12, C13 com profundidade → C18, C24, C25, C26 → frameworks F1, F4, F6, F7 → apêndices L, J, O.

**50 horas (leitura completa para construir referência interna):**
Leitura sequencial integral com pausa em cada Autoavaliação. Aplicação dos exercícios numerados ao longo dos capítulos. Construção do roadmap pessoal (C26). Aplicação do Caderno de Governança v1 no contexto do leitor (Apêndice O). Revisão da Trilha do Número (Apêndice J) e da Biblioteca de Prompts (Apêndice L) como instrumentos diários.

---

## Como saber se a trilha está funcionando

Cada capítulo termina com Autoavaliação em tabela de cinco critérios. A regra prática de recalibração:

| Sinal observado | O que fazer |
|---|---|
| 3 capítulos seguidos com Autoavaliação ≥ 4/5 | Considerar avançar uma trilha |
| 3 capítulos seguidos com Autoavaliação ≤ 2/5 | Voltar uma trilha |
| 1-2 capítulos com nota baixa entre vários ≥ 3/5 | Reler o capítulo específico, não mudar trilha |
| Autoavaliação inconsistente entre temas | Trilha mista provável — seguir por interesse, não por nível |

A leitura honesta deste mapa, antes do primeiro capítulo, economiza horas de esforço mal direcionado. A leitura desonesta cobra o preço típico do leitor que escolhe a trilha que aspira ser, em vez da trilha que efetivamente serve agora.

</div>
</section>



<section class="paratexto-inicial">
<div class="abertura-paratexto">

# Repositório Acompanhante

> *O padrão dura no livro. O número muda no repositório.*

---

Este livro tem um companheiro executável público que carrega o que muda mais rápido do que a tinta no papel. Enquanto o livro entrega o método que sobrevive à próxima geração de modelo — os princípios, os frameworks, a anatomia das decisões, os anti-padrões observáveis — o repositório carrega o número datado: prompts em XML versionado, golden sets executáveis, scripts de regressão, caderno operacional de governança em arquivos editáveis, changelog público versionado.

A combinação dos dois materializa o Princípio Três da obra, **Camada Dupla**. Quem só lê o livro sai com método e precisa montar os artefatos do zero. Quem opera só com o repositório sem ler o livro opera no escuro, porque não vai entender por que cada peça está naquela posição. Quem usa os dois sai com modelo mental sólido e ativos prontos para entrar em pipeline.

---

## Endereço

**[github.com/falercia/inteligencia-aumentada-recursos](https://github.com/falercia/inteligencia-aumentada-recursos)**

Licenças: MIT para código, CC-BY 4.0 para conteúdo editorial. Uso comercial permitido com atribuição.

---

## O que vive lá agora

| Pasta | Conteúdo | Capítulos relacionados |
|---|---|---|
| `/prompts` | 30 prompts profissionais em XML, com golden set, prefill, self-critique, anti-padrões e métrica de qualidade por prompt | C9 · F4 · Apêndice L |
| `/governance` | Caderno de Governança v1.0 em 6 seções fatiadas, modelo de 6 páginas para imprimir e assinar, modelos clonáveis dos 6 anexos | C24 · F6 · Apêndice O |
| `/evals` | `eval_runner.py` executável, `compile_golden_sets.py`, judges integrados (substring, regex, json_schema, classification), gate de CI | C21 · F8 |
| `/datasets` | Golden sets em JSONL compilados a partir dos YAMLs originais, prontos para CI | C21 · C23 |
| `/agents` | Quatro agentes educacionais executáveis em Python puro — A01 (ReAct Simples), A02 (Escala de Propriedade nos 4 níveis F3 lado a lado), A03 (Orquestrador-Especialistas, multiagente cooperativo em estrela reusando `/prompts`) e A04 (Multiagente Debate, adversarial com juiz integrável a `/evals`). Todos com tools simuladas seguras, tracing local em JSONL, gates, kill switch testável e exemplos rodáveis | C12 · C14C · C21 · C25 · F3 · F8 |
| `/mcp` | Servidores MCP educacionais — M01 (Hello World com Resource, Tool e Prompt mínimos) e M02 (Biblioteca Interna que expõe os prompts de `/prompts` e o caderno de governança como Resources para qualquer cliente MCP), com cliente de teste local e config-exemplo para Claude Desktop | C13 · F5 |
| `/notebooks` | 4 notebooks fundacionais executáveis com narrativa didática célula a célula — tokenização com `tiktoken`, reprodução do experimento *Lost in the Middle*, embeddings com visualização 2D e busca semântica, e demonstração quantitativa de prompt caching | C3 · C4 · C5 · C18 |

## Cada pasta tem o seu próprio README

Cada pasta com conteúdo tem `README.md` próprio com instruções específicas, ficha técnica do que entrega, padrões de uso, exemplos rodáveis e conexão com os capítulos do livro. Antes de clonar artefato isolado, vale ler o README da pasta correspondente — quinze minutos de leitura economizam horas de tentativa-e-erro.

Quem identifica lacuna, anti-padrão útil para a obra, ou caso de uso não coberto pelas estruturas atuais, é convidado a abrir issue no repositório com o template correspondente. Contribuições qualificadas com fonte primária ou validação por especialista entram nas revisões seguintes, com atribuição quando o contribuidor autoriza.

---

## Como começar

Três caminhos, conforme a intenção:

1. **Quero entender antes de usar.** Abra `prompts/P-LEG-01/` e leia o `README.md` da pasta, depois compare com a ficha conceitual correspondente no Apêndice L. Em quinze minutos você terá o mapa mental completo de como livro e repositório se costuram.

2. **Quero colocar em produção rápido.** Pegue o prompt mais próximo do seu domínio, copie o diretório inteiro para o seu repositório interno, adapte a constituição ao seu contexto, construa seu golden set próprio com pelo menos vinte casos representativos do seu tráfego real, rode `eval_runner.py` antes de cada release.

3. **Quero contribuir.** Leia `CONTRATO.md` e abra issue com a categoria sugerida. Contribuições qualificadas com fonte primária são incorporadas nas revisões seguintes, com atribuição quando o contribuidor autoriza.

---

## Política de evolução

O repositório evolui de forma incremental, sem cadência fixa anunciada, com prioridade para a qualidade da entrega sobre o cumprimento de calendário. Releases recebem tag semântica e `CHANGELOG.md` versionado, indicando mudança item por item, motivo da mudança, e impacto observado em golden set ou em produção. A política editorial é simples e dura: nenhuma promessa de release que não esteja pronta para ser cumprida, e nenhum release publicado sem ter passado pela mesma disciplina de revisão que o livro exige de qualquer artefato sério.

O que separa repositório acompanhante vivo de folheto promocional não é cadência declarada, é entrega consistente sob crítica pública. O leitor que clona o repositório pode ativar *watch* no GitHub para receber notificação de novos releases, e o autor compromete-se apenas com a verdade do que foi entregue, jamais com data futura que não dependa só dele.

---

## Conexão capítulo a capítulo

Ao longo da leitura, cada vez que aparecer a marcação **▸ repo** ou a referência a um caminho `pasta/arquivo`, trata-se de artefato executável que vive no repositório. Quem está com pressa pode anotar o caminho e visitar depois; quem quer ver o instrumento em mãos pode abrir em outra aba enquanto lê.

> *Quem só lê o livro sai com método. Quem usa este repositório acrescenta implementação. Quem opera só com este repositório sem ler o livro opera no escuro.*

</div>
</section>
