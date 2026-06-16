---
title: "Inteligência Aumentada"
lang: pt-BR
---



<section class="capitulo-bloco">
<div class="abertura-capitulo">
<div class="bandeira-nivel bandeira-intermediario-avancado">Inter·Avanc</div>
# 20. O Futuro Da IA Em Cenários Estruturados

---

> *"Previsão é especulação travestida de número, e número falso engana o orçamento. Cenário estruturado é o instrumento que o executivo usa quando assume que não sabe o que vai acontecer, mas precisa decidir como agir nos três caminhos possíveis."*

---

## Abertura

<p class="dropcap">Quem assina o orçamento de tecnologia para os próximos três anos descobre, na primeira reunião de Conselho, que ninguém quer ouvir "depende". A pergunta vem direta, vinda do CEO, do CFO ou do investidor de fundo, e cobra resposta firme: o que vai acontecer com IA, em quanto tempo, e quanto a empresa deve investir agora para não ficar para trás. A tentação é responder com profecia, escolhendo o cenário que parece mais provável, pintando o futuro com tinta forte, e levando o orçamento aprovado em cima de uma única hipótese. Essa é a forma mais comum de queimar capital em tecnologia, porque profecia única é a mais frágil forma de pensar, ainda mais em campo cuja taxa de progresso oscila entre desaceleração e salto a cada dois ou três trimestres.</p>

O método deste capítulo é o oposto da profecia, e é o que separa o executivo que pensa o futuro do entusiasta que torce por ele. Em vez de prever, mapeamos vetores de mudança observáveis, e em vez de escolher um único caminho, construímos três caminhos plausíveis em dois horizontes, e em vez de adivinhar números, declaramos probabilidade subjetiva qualitativa, com critério articulado para mover a empresa entre cenários quando os sinais mudam. Este capítulo entrega o instrumento que o leitor vai precisar para responder à pergunta do Conselho sem mentir nem se omitir.

---

## 20.1 — Conceito Intuitivo: Por Que Cenários Vencem Previsões

A diferença entre previsão e cenário não é semântica, é metodológica e operacional, e quem confunde paga caro porque a previsão induz a decisão única, e a decisão única tem uma probabilidade de errar igual à probabilidade do cenário previsto não se realizar, que em campo turbulento costuma passar de cinquenta por cento. Cenário, ao contrário, é estrutura mental que assume incerteza como entrada do problema, oferece três (às vezes quatro) caminhos plausíveis, e cobra do executivo plano para cada um, com gatilhos explícitos de transição. Quando a realidade se move, o executivo não descobre que errou, ele descobre em qual cenário a empresa está, e ativa o plano correspondente.

A indústria de petróleo refinou esse método ao longo das últimas décadas, em larga parte porque uma única previsão errada sobre preço de barril pode atrasar dez bilhões de dólares de investimento em campo offshore. A Shell tornou o método clássico ainda nos anos 1970, durante a crise do petróleo, e o que ficou na literatura corporativa é que cenários não são apostas, são lentes pelas quais a organização lê os sinais do ambiente, e quanto antes a organização identifica em qual cenário está, mais cedo ela ajusta capital, talento e produto. IA tem hoje, para a empresa que aposta nela com seriedade, o mesmo perfil de risco que petróleo teve naquela época, com a diferença de que o ciclo não é de uma década, é de dezoito meses.

A consequência prática é simples. Quem leu este capítulo e ainda assim apresenta ao Conselho uma única projeção de futuro de IA está praticando irresponsabilidade técnica, porque desconhece um instrumento básico de planejamento sob incerteza, ou está praticando teatro político, porque acha que o Conselho prefere falsa certeza a verdadeira humildade. O CTO competente apresenta sempre três cenários, e usa o terceiro slide para explicar qual sinal o vai mover entre eles.

---

## 20.2 — Analogia: O Piloto Que Prepara Três Aproximações

O piloto comercial que se aproxima de aeroporto em condição meteorológica adversa não decide a estratégia de pouso quando avista a pista; decide a estratégia ainda na cabine, antes do briefing inicial, listando três planos de aproximação alternativos com critério explícito para escolher entre eles em função do que o instrumento mostrar. O primeiro plano é a aproximação por instrumentos completa, com pouso na pista principal e taxiamento direto, e ele é usado se a visibilidade estiver dentro da margem regulatória e os ventos cruzados forem aceitáveis. O segundo é a aproximação circular, com pouso em pista secundária e taxiamento mais longo, e ele é usado se o vento mudar de direção ou se a pista principal estiver bloqueada por aeronave em emergência. O terceiro é a arremetida com diversão para aeroporto alternativo, e ele é usado se a visibilidade cair abaixo do mínimo ou se o piloto sentir, por instinto treinado, que a aproximação não está estabilizada.

A virtude do método não está em adivinhar qual dos três vai ser usado, está em ter os três prontos antes de precisar, com critério explícito de transição entre eles, e em treinar a tripulação no reconhecimento dos sinais. Cenários estratégicos de IA operam pela mesma lógica. O CTO prepara três planos de produto, três planos de orçamento, três planos de talento, e o que faz a empresa pousar bem é a velocidade com que ela identifica o cenário em que está e ativa o plano correspondente, não a sorte de ter previsto o cenário certo. A diferença é que o piloto checa instrumento a cada cinco segundos, e o CTO checa sinais a cada trimestre, mas a estrutura mental é idêntica.

---

## 20.3 — Método de Cenários

![Vetores e horizontes do futuro da IA — três cenários estruturados](file:///sessions/relaxed-cool-bell/mnt/Ebook IA/Livro-1-Os-Invariantes/02-capitulos/imagens/cap-38-img-01-futuro-ia.svg)


A construção de cenário disciplinado tem três componentes, e omitir qualquer um deles deixa o método incompleto, porque cenário sem vetor é narrativa solta, cenário sem horizonte é literatura, e cenário sem probabilidade subjetiva é equivalente a três opiniões igualmente plausíveis, o que paralisa a decisão. Os parágrafos abaixo apresentam os componentes na ordem em que devem ser construídos.

### 20.3.1 — Quatro Vetores de Mudança Que Importam

Em planejamento de cenário, vetor é uma força observável que move o ambiente em direção mensurável, ainda que a velocidade e a magnitude permaneçam incertas. Quatro vetores sustentam os cenários de IA, e qualquer outro fator (geopolítica, oferta de energia, evolução de hardware) acaba refletido em um deles. O primeiro vetor é a capacidade do modelo, medida em qualidade de raciocínio em tarefas longas, contexto efetivo utilizável e taxa de alucinação em domínios verificáveis; é o vetor que mais oscila em ciclo curto, porque cada release de laboratório frontier o move, em direção que ora acelera ora desacelera conforme o esgotamento de técnicas atuais. O segundo é a autonomia do agente, medida em proporção de tarefas que podem ser completadas sem intervenção humana ponto a ponto, e é o vetor que tem mais impacto operacional, porque define qual fatia da carga repetível de back-office pode ser substituída por orquestração. O terceiro é o custo da inferência, medido em valor pago por milhão de tokens entregues em qualidade aceitável para a tarefa, e é o vetor que mais cai em ciclo longo, com tendência observada de queda exponencial ao longo de três a quatro anos. O quarto é a postura regulatória, medida pela coerência internacional entre regimes (EU AI Act, framework chinês, NIST nos Estados Unidos, PL 2338 no Brasil, regulação setorial em finanças e saúde) e pelo grau de fricção que cria em deploy cross-border.

Cada vetor tem dinâmica própria, e essa é a parte que costuma escapar do executivo apressado. Capacidade pode saltar enquanto custo permanece estável, e nesse mundo o que ganha é qualidade premium; custo pode despencar enquanto capacidade estagna, e nesse mundo o que ganha é volume operacional; regulação pode endurecer enquanto autonomia avança, e nesse mundo o que ganha é a empresa que tem governança madura; autonomia pode atingir patamar útil enquanto regulação se fragmenta, e nesse mundo o que ganha é a empresa que opera por geografia. O cenário é o cruzamento desses quatro vetores em estado coerente, e o exercício honesto é admitir que apenas algumas combinações são plausíveis, porque os vetores se acoplam parcialmente (custo cai mais rápido quando capacidade estagna, por exemplo, porque o esforço vai para eficiência).

### 20.3.2 — Três Horizontes Temporais

Horizonte de doze meses é o de planejamento orçamentário, é onde o ciclo de release dos laboratórios frontier dá tempo de ser observado, e onde o que conta é a calibração da hipótese atual; cenário a doze meses é, em essência, refinamento do plano corrente. Horizonte de trinta e seis meses é o de planejamento estratégico de produto, é onde os contratos de longo prazo entram, e onde o investimento em arquitetura, plataforma e talento precisa estar coerente com a leitura predominante; é também o horizonte em que cenários divergem de forma material. Horizonte de sessenta meses é o de planejamento de capital de longo prazo, é onde investimentos pesados em infraestrutura, parcerias estratégicas e posicionamento de mercado são decididos, e onde a variância entre cenários cresce ao ponto de incluir a possibilidade de descontinuidades qualitativas, com AGI ou platô estendido como polos extremos.

Este capítulo apresenta cenários detalhados em trinta e seis meses, porque é o horizonte em que o método paga mais retorno (decisões orçamentárias maiores, ainda dentro da janela em que a empresa pode reagir), e cenário sumário em sessenta meses, porque é o horizonte em que o método entrega humildade calibrada (decisões estruturais grandes, com reconhecimento de que a variância é alta). Cenário em doze meses é deixado ao processo de planejamento anual, com o método aplicado em ciclos trimestrais de revisão.

### 20.3.3 — Como Ler Probabilidade Subjetiva Qualitativa

A tentação do executivo treinado em finanças é exigir probabilidade numérica para cada cenário (vinte por cento otimista, sessenta por cento mediano, vinte por cento pessimista), e a recusa em fornecer esse número costuma ser interpretada como falta de coragem técnica. O argumento a sustentar com o Conselho é o inverso, e tem base sólida na literatura de previsão calibrada: número falso engana mais do que admissão honesta de incerteza, especialmente em campo em que o histórico de previsões pontuais é catastrófico (a indústria de IA está repleta de previsões de pesquisadores e CEOs que erraram por ordem de magnitude em janela de dois anos). A alternativa madura é probabilidade subjetiva qualitativa, em três níveis: provável (o cenário em que a empresa deve planejar como caso base), possível (o cenário em que a empresa deve manter plano de contingência ativo) e improvável (o cenário em que a empresa deve manter monitoramento de sinais sem investir em plano elaborado).

Cada cenário deste capítulo será classificado nessas três faixas, com explicação dos sinais que justificariam a reclassificação. O leitor é convidado a discordar das classificações, e a discordância produtiva está na identificação de sinais diferentes, não em mudança de adjetivo sem critério.

---

## 20.4 — Cenário Otimista a Trinta e Seis Meses

> **Probabilidade subjetiva:** possível (no patamar superior do plausível, mas não a leitura mais provável).
> **Sinais que sustentariam reclassificação como provável:** dois releases consecutivos de laboratório frontier com saltos mensuráveis em benchmarks de raciocínio longo, redução observada de custo de inferência em ordem de magnitude no horizonte de doze meses, convergência regulatória explícita entre Estados Unidos e União Europeia.

No cenário otimista, a capacidade do modelo continua avançando em ciclo regular, com reasoning models tornando-se padrão de produto (não mais a categoria premium que são hoje), contexto efetivo utilizável passando a casa dos milhões de tokens com fidelidade preservada, e taxa de alucinação caindo a níveis em que o uso em domínio verificável (jurídico, financeiro, médico) passa a exigir menos camadas de verificação do que hoje. A consequência imediata é que tarefas que hoje precisam de prompts longos, exemplos cuidadosamente selecionados e cadeias de validação multietapa, passam a ser resolvidas com prompts curtos e uma única passagem do modelo, o que reduz o custo de engenharia de cada feature de IA e amplia o leque de tarefas em que IA passa o limiar de ROI.

Autonomia do agente, neste cenário, atinge maturidade em verticais específicos, com agentes especializados por função operacional (vendas, atendimento, RH operacional, jurídico contratual, finanças contábeis, recrutamento de primeiro filtro) cobrindo a fatia repetível de cada função em proporção mensurável (sessenta a setenta por cento da carga, com variação por setor), e com humanos passando a operar como supervisores de exceção em vez de executores ponto a ponto. O ponto crítico, que distingue o cenário otimista da fantasia, é que essa transição não é instantânea, ela exige investimento sustentado em context engineering, em evals, em observabilidade e em governança, e a empresa que não construiu esses pilares (que são justamente os capítulos centrais desta obra) recebe os agentes como caixa-preta cara e instável, sem capturar a produtividade que os agentes prometem.

Custo da inferência cai na ordem de magnitude (uma redução de aproximadamente dez vezes em três anos), o que reabre a equação econômica para casos de uso hoje proibitivos por volume, como atendimento massivo de varejo brasileiro, processamento contínuo de vídeo de segurança, análise contínua de telemetria industrial. O segundo efeito é que o custo da inferência deixa de ser o fator dominante na escolha de modelo, e o que passa a importar é o ajuste fino entre tarefa, modelo e arquitetura de prompt, o que devolve protagonismo à disciplina de engenharia e tira protagonismo da escolha de vendor.

Regulação, no cenário otimista, converge internacionalmente, com EU AI Act como referência operacional global, framework chinês mantendo sua particularidade mas com pontos de interoperabilidade, e NIST nos Estados Unidos consolidando um padrão técnico que serve de ponte. No Brasil, PL 2338 é sancionado com texto que reconhece a particularidade do mercado interno, ANPD instala diretoria especializada em IA, e o sandbox regulatório de IA passa a funcionar como instrumento real para fintechs e healthtechs. A consequência para a empresa brasileira é que o custo de compliance se estabiliza em patamar previsível, e que o deploy cross-border (especialmente para América Latina) deixa de exigir reengenharia jurídica por país.

A implicação executiva para o CTO neste cenário é de oportunidade assimétrica. A organização que tiver chegado a este horizonte com context engineering maduro, com Pirâmide de Evals operante, com LLMOps em seus sete pilares e com Caderno de Governança vivo (todos os instrumentos que esta obra desenvolve), multiplica produtividade por fator entre três e cinco, captura mercado em verticais especializadas onde a tradição é fragmentada, e ganha vantagem de retenção de talento ao oferecer ambiente onde os profissionais operam IA com seriedade, não com aventura. A organização que chegou sem essas fundações enfrenta o pior dos mundos, com pressão de mercado para adotar agentes, com fornecedores apresentando suites de IA aparentemente prontas, e com governança imatura para escolher entre elas, o que tende a custar caro em retrabalho e em incidentes públicos.

A leitura financeira do cenário otimista é que TCO de IA por receita cai em termos absolutos, mas a competição empurra produtividade marginal, e o que captura o ganho é quem tem disciplina, não quem tem mais capital. O cenário não favorece, portanto, o late mover paciente nem o early mover desorganizado; favorece o disciplinado, e este é o lugar onde o método da obra paga retorno máximo.

---

## 20.5 — Cenário Mediano a Trinta e Seis Meses

> **Probabilidade subjetiva:** provável (a leitura base, em que o CTO deve construir o plano principal de tecnologia).
> **Sinais que sustentariam reclassificação para outro cenário:** desaceleração observada em dois trimestres consecutivos sem novidade qualitativa moveria a leitura para pessimista; salto qualitativo em raciocínio matemático ou em autonomia de agente em domínio aberto moveria para otimista.

No cenário mediano, a capacidade do modelo avança por refinamento incremental, sem saltos disruptivos, com cada release trazendo melhoria mensurável em alinhamento, em modos de raciocínio especializados (matemática, código, ciência), em qualidade multimodal e em fidelidade em contextos longos, mas sem a sensação de descontinuidade qualitativa que marcou a passagem de ChatGPT 3.5 para 4. O ritmo de release dos laboratórios frontier permanece regular, com ciclo de seis a dezoito meses por geração maior, e com a disputa entre laboratórios continuando intensa, o que mantém a pressão competitiva e o investimento em pesquisa, ainda que com retornos marginais decrescentes em algumas dimensões.

Autonomia do agente atinge maturidade em domínios estreitos, com agentes verticais ganhando espaço em tarefas bem delimitadas (atendimento de primeira linha, classificação de pedidos, monitoramento de KPIs com geração de alerta, redação de minutas contratuais padronizadas), mas com a fronteira de domínio aberto (agentes que operam em ambientes ricos, com objetivos amplos e ferramentas heterogêneas) avançando mais devagar do que o discurso do mercado promete. Em termos operacionais, isso significa que o investimento em frameworks de orquestração de agente continua exigindo cuidado, com risco real de o framework escolhido virar débito técnico ao longo de dezoito meses, e com a Escala de Propriedade do Agente (que esta obra detalha no Framework F3) continuando como instrumento indispensável de governança.

Custo da inferência cai de forma mais modesta do que no cenário otimista, na ordem de três a cinco vezes em três anos, com a queda concentrada em modelos médios (que se aproximam da qualidade dos modelos grandes da geração anterior) e com o custo dos modelos frontier mantendo-se em patamar premium. A consequência prática é que a equação de escolha de modelo permanece sendo um exercício de Encaixe entre Tarefa e Modelo (F2), com o operador disciplinado optando por modelo médio na maior parte das tarefas, e reservando frontier para a fatia da carga em que o ganho marginal justifica o gasto.

Regulação, no cenário mediano, segue trajetória de implementação prática do que já está em vigência, com EU AI Act passando da fase de transposição para a fase de fiscalização ativa, com primeiras multas materiais publicadas e com construção de jurisprudência prática. No Brasil, PL 2338 é sancionado com texto próximo do que está em discussão no Congresso, ANPD passa a aplicar penalidades em casos emblemáticos, e o setor financeiro consolida regulação setorial específica para IA. A consequência para a empresa brasileira é que o custo de compliance sobe de forma controlada, com investimento crescente em Caderno de Governança, em DPO especializado em IA e em controles internos auditáveis, e a vantagem vai para quem instalou essa estrutura antes da fiscalização chegar.

A implicação executiva no cenário mediano é a mais relevante para o planejamento, porque é a base mais provável e porque captura a essência do que o método desta obra entrega. Produtividade sobe em fatia mensurável (a literatura corporativa sugere ganhos entre trinta e oitenta por cento em funções repetíveis com IA bem implementada, com variação alta por setor e por maturidade), e a vantagem competitiva não vai para a empresa que tem modelo melhor (porque o acesso a modelo é commodity), vai para a empresa que opera disciplina, que executou os capítulos centrais da obra com seriedade, que tem evals que pegam regressão, que tem tracing que mostra onde o custo está, que tem AI Council que aprova roadmap de adoção com critério, e que tem cultura institucional de tratar IA como sistema de produção, não como brinquedo experimental.

O CTO que planeja para este cenário entrega ao Conselho um plano de orçamento que cresce em IA de forma controlada (de cinco a quinze por cento do orçamento de tecnologia, com variação por setor), um plano de talento que investe em context engineering e em governança em vez de apenas em data science, e um plano de produto que prioriza features de IA com Método de Decisão (F1) aplicado com rigor, evitando o erro comum de adotar IA em features de baixo ROI. A pergunta de teste para identificar se a empresa está operando neste cenário é simples e brutalmente honesta: a fatia da fatura mensal de IA que gera valor mensurável é maior do que a fatia que financia exploração? Se sim, a empresa está no cenário mediano com competência; se não, está no cenário pessimista sem perceber.

---

## 20.6 — Cenário Pessimista a Trinta e Seis Meses

> **Probabilidade subjetiva:** possível (não a leitura mais provável, mas com sinais suficientes para exigir plano de contingência ativo).
> **Sinais que sustentariam reclassificação como provável:** três releases consecutivos de laboratório frontier sem ganho mensurável em benchmarks centrais, desinvestimento público de fundos relevantes, crise de confiança em qualidade de agentes em produção, fragmentação regulatória aguda com fricção de deploy cross-border.

No cenário pessimista, a capacidade do modelo entra em platô confirmado, com cada release trazendo ganho marginal em benchmarks centrais (raciocínio em tarefas longas, fidelidade em contexto longo, taxa de alucinação em domínio verificável), com a pesquisa migrando para refinamentos de eficiência e de modos especializados, e com a comunidade científica reconhecendo, em literatura, que a arquitetura predominante (transformers em variações) atingiu o limite do que escalas atuais permitem, e que o próximo salto exige inovação arquitetural não trivial. A consequência operacional é que o investimento das empresas em "esperar o próximo modelo melhor" deixa de pagar, porque o próximo modelo é apenas marginalmente melhor, e o que distingue as empresas passa a ser a engenharia em torno do modelo, não o modelo em si.

Autonomia do agente decepciona em produção, com casos de implantação ambiciosa mostrando custos de manutenção altos (operadores humanos necessários para corrigir trajetória, retrabalho em cascata, ciclos longos de iteração em evals), com frameworks de orquestração de agente lançados nos últimos dois anos virando débito técnico (porque cada laboratório frontier sugere padrões diferentes, e a empresa que adotou o framework errado paga a migração), e com a literatura corporativa começando a publicar casos de fracasso, no padrão clássico em que toda onda tecnológica passa pelo Vale da Desilusão antes de retomar trajetória sustentada. A Escala de Propriedade do Agente (F3) torna-se ainda mais central, com a maioria dos agentes em produção sendo operada nos níveis baixos da escala (assistente, copiloto), e com agentes plenamente autônomos sendo restritos a domínios estreitos e bem auditados.

Custo da inferência cai pouco, na ordem de duas a três vezes em três anos, com a queda concentrada em modelos médios e com modelos frontier mantendo preço premium em razão do esforço de pesquisa que continua, ainda que com retornos decrescentes. A consequência prática é que o ROI de IA passa a ser mais sensível à disciplina de engenharia do que à evolução do modelo, e que a empresa que apostou em escalar volume sem otimizar arquitetura paga uma fatura crescente sem o ganho de produtividade correspondente. O Custo Composto em Três Tempos (F7) torna-se a ferramenta diária do CTO, com revisão mensal do custo por feature e com decisões duras de descontinuar features cujo ROI não se sustenta.

Regulação, no cenário pessimista, fragmenta-se por jurisdição, com EU AI Act, NIST, framework chinês e regulação brasileira divergindo em pontos centrais (categorização de risco, exigências de transparência, requisitos de auditoria), com o deploy cross-border passando a exigir arquiteturas diferenciadas por geografia, e com o custo de compliance subindo em proporção que dificulta a operação de empresa global de médio porte. No Brasil, o ambiente regulatório oscila entre rigidez excessiva e leniência casuística, e a empresa brasileira que opera no exterior precisa de squad jurídico especializado em IA por geografia, o que é caro e que tende a favorecer os incumbentes em detrimento de novos entrantes.

A implicação executiva no cenário pessimista é, paradoxalmente, a que mais valida o método desta obra, e isso porque a economia conservadora é quem ganha. A empresa que manteve arquitetura modular (em vez de se acoplar a um vendor único), que investiu em governança e evals antes da pressão de fiscalização, que tratou cada feature com Método de Decisão (F1) em vez de adotar IA por euforia, e que cultivou cultura institucional de prudência calibrada, sobrevive à fase difícil em posição de vantagem, e captura a retomada quando ela vem. A empresa que queimou capital em frameworks da moda, que adotou IA em features de baixo ROI por pressão de mercado, e que não construiu governança a tempo, paga juros compostos em retrabalho, em migração e em incidentes públicos, e algumas dessas empresas saem do cenário pessimista enfraquecidas o suficiente para perderem participação de mercado de forma estrutural.

O CTO que planeja para este cenário entrega ao Conselho um plano de orçamento conservador (manter investimento em IA em patamar estável, sem cortes que comprometam a base, mas sem expansão acelerada que aposte em capacidade que não vai chegar), um plano de talento que privilegia profissionais maduros sobre contratações em volume, e um plano de produto que prioriza estabilização das features existentes em detrimento de lançamento acelerado de novas. A pergunta de teste é: se o próximo modelo for apenas dez por cento melhor do que o atual, o orçamento ainda faz sentido? Se sim, o plano está calibrado para o cenário pessimista; se não, há fragilidade que precisa ser endereçada antes da próxima janela de revisão.

---

## 20.7 — Cenário a Sessenta Meses: Variância Alta e a Questão AGI

O horizonte de sessenta meses exige humildade adicional, porque a variância entre cenários cresce ao ponto de incluir descontinuidades qualitativas, e porque o exercício de previsão pontual aqui não tem qualquer pretensão de acurácia, ele serve apenas para acordar a organização para as possibilidades extremas e para alinhar o plano de capital de longo prazo com a realidade da incerteza. Apresento três pontos de fundo, sem detalhar três cenários completos, porque o exercício detalhado em sessenta meses tem retorno marginal baixo (a organização vai revisar a leitura a cada doze meses, e os detalhes mudam).

O primeiro ponto é que, em qualquer cenário a sessenta meses, o ambiente regulatório estará consolidado em fase de fiscalização ativa, com jurisprudência publicada, com penalidades materiais, e com requisitos de auditoria que se aproximam dos padrões de segurança bancária. A empresa que chegar a este horizonte sem governança madura paga preço dramático, porque os controles que esta obra detalha (Caderno de Governança, AI Council, AUP, sete pilares de LLMOps) deixam de ser opcionais e passam a ser exigência de mercado, exigência de cliente enterprise e exigência regulatória. Em todos os três cenários do horizonte de trinta e seis meses, a trajetória de cinco anos converge nesse ponto, e isso reduz a variância da decisão de investir em governança hoje: é investimento que paga em qualquer futuro plausível.

O segundo ponto é que, em qualquer cenário a sessenta meses, a vantagem competitiva sustentável não está na escolha de modelo ou de vendor, está na competência institucional de operar IA com disciplina. O acesso aos modelos frontier será commodity (com variação de preço, com diferenciação por contrato, mas sem o nível de exclusividade que existe hoje), e o que distinguirá empresas será a profundidade do context engineering, a maturidade dos evals, a qualidade da observabilidade e a robustez da governança. Esta é a tese central da obra, e o horizonte de cinco anos a confirma com mais força do que o horizonte de três anos, porque ao longo de cinco anos a comoditização da capacidade frontier se consolida.

O terceiro ponto é a questão de AGI, e aqui o método de cenário exige tratar AGI como pergunta legitimamente em aberto, sem tomar partido apressado em qualquer direção. Os argumentos pró-aceleração apontam que a trajetória recente de capacidade em raciocínio, em uso de ferramentas e em planejamento se aproxima de marcas que foram propostas como teste de generalidade, que laboratórios frontier publicam metas explícitas de chegar a sistemas com generalidade comparável à humana em janela de três a sete anos, e que o investimento global em IA ultrapassou patamares históricos que justificam expectativa de salto. Os argumentos contra-aceleração apontam que a generalidade observada em modelos atuais ainda é frágil em tarefas longas e em raciocínio causal profundo, que a literatura técnica registra limitações arquiteturais que escalonamento puro não resolve, que os benchmarks de generalidade são objetos contestados (e o consenso sobre o que constitui AGI é tudo menos consensual), e que a história da IA está marcada por previsões de generalidade que erraram por décadas.

A posição executiva responsável é a de não apostar nem contra nem a favor, e construir plano de capital de longo prazo que seja robusto em ambos os polos. Se AGI chegar dentro da janela de cinco anos, a empresa com governança madura, com arquitetura modular e com cultura de prudência calibrada está em posição de absorver a mudança; a empresa sem essas fundações é arrastada por ela. Se AGI não chegar dentro da janela, a empresa que investiu em governança e em disciplina não desperdiçou nada, porque os instrumentos pagam em qualquer cenário plausível, e a empresa que apostou em AGI iminente paga em capital queimado e em estratégia desalinhada. A evidência disponível em junho de 2026, ainda que limitada por horizonte de previsão muito curto, sugere com confiança moderada que o investimento dominante nos dois polos cobertos por este exercício tende a ser o mesmo, qual seja, disciplina institucional, governança madura, arquitetura modular e cultura de prudência calibrada, ressalvado que a probabilidade atribuída a cada cenário ainda é objeto de divergência legítima entre laboratórios frontier, pesquisadores acadêmicos e operadores corporativos sêniores, e que a posição prudente é tratar essa convergência metodológica como hipótese de trabalho a ser reavaliada na próxima revisão anual, jamais como certeza fechada. O método da obra é, neste sentido, a aposta racional sob máxima incerteza, com a humildade de admitir que sob máxima incerteza nenhuma aposta é racional em sentido forte, apenas menos imprudente do que as alternativas.

A implicação prática para o CTO é que o plano de capital de longo prazo deve evitar tanto a leitura de que IA atual é teto, quanto a leitura de que AGI iminente reorganiza tudo. O caminho do meio é o investimento sustentado em fundamentos institucionais, com revisão anual da leitura de cenário e com flexibilidade orçamentária para acelerar ou desacelerar conforme os sinais se materializam.

---

## 20.8 — Como o CTO Usa Cenários Na Prática

A construção de cenário não tem qualquer utilidade se ficar restrita a documento ornamental, e por isso o método precisa virar prática gerencial recorrente, com três usos concretos que o CTO deve instituir em sua organização. O primeiro uso é a construção paralela de três planos por dimensão crítica do orçamento e do produto, com plano otimista (que se ativa se a empresa entrar no cenário otimista), plano mediano (que é o plano-base, sob o qual a empresa opera por padrão) e plano pessimista (que se ativa se sinais indicarem deterioração do ambiente). O exercício é trabalhoso na primeira execução, porque exige construir três versões de orçamento, três versões de roadmap de produto, três versões de plano de talento, mas é leve nas execuções subsequentes, porque o que muda é o ajuste incremental sobre planos pré-existentes.

O segundo uso é a revisão trimestral da leitura predominante de cenário, em rito formal do AI Council, com lista explícita de sinais que justificariam mover a leitura entre cenários, e com decisão documentada sobre permanência ou mudança. A revisão precisa ser conduzida com rigor, com agenda preparada, com dados (releases de laboratório frontier, custo observado, sinais regulatórios, sinais de adoção de mercado), e com decisão registrada em ata, porque o risco de degenerar para conversa informal é alto. A boa prática é que a revisão seja conduzida pelo CTO (ou pelo Head de IA), com participação do CFO (para conexão orçamentária) e de pelo menos um membro do Conselho com mandato sobre tecnologia.

O terceiro uso é a comunicação com partes externas (Conselho, investidores, clientes enterprise) por meio de cenários em vez de previsões pontuais. A organização que comunica seu plano de IA por cenários sinaliza maturidade institucional, e isso costuma ser interpretado positivamente por investidores sofisticados e por clientes enterprise que avaliam fornecedores em maturidade técnica, não apenas em preço. A apresentação típica tem três slides (um por cenário, com vetores, implicações e plano correspondente) e um quarto slide que mostra os sinais que estão sendo monitorados e o gatilho explícito de transição. A frase-âncora que essa apresentação encerra, e que o CTO deve memorizar, é simples: "operamos hoje no cenário mediano, e os sinais que nos moveriam para o cenário pessimista ou otimista estão listados no monitoramento, com plano ativo para cada possibilidade".

A combinação dos três usos transforma a função do CTO. Em vez de adivinhar o futuro, ele opera o presente com plano calibrado para três futuros plausíveis, ajustando o plano em ciclo trimestral conforme os sinais se materializam, e comunicando à organização e ao Conselho com humildade calibrada que substitui falsa certeza por preparo real. Esta é, talvez, a habilidade executiva mais importante que esta obra entrega, e a habilidade que mais distingue o CTO competente do CTO entusiasmado.

---

## 20.9 — Resumo Executivo

| Cenário | Capacidade | Autonomia | Custo | Regulação | Implicação executiva |
|---------|------------|-----------|-------|-----------|----------------------|
| **Otimista (possível)** | Reasoning padrão; contexto efetivo amplo; alucinação cai | Agentes verticais cobrem 60-70% da carga repetível em domínios | Cai ~10x em 3 anos | Convergência internacional; sandbox BR funcional | Produtividade 3-5x para quem tem governança e evals; sem fundação, vira fragilidade |
| **Mediano (provável — base)** | Refinamento incremental; ganhos por modos especializados | Maturidade em domínios estreitos; framework continua exigindo cuidado | Cai 3-5x em 3 anos | EU AI Act em fiscalização; PL 2338 sancionado | Produtividade +30-80%; vantagem para quem opera disciplina, não para quem compra modelo melhor |
| **Pessimista (possível)** | Platô confirmado; ganhos marginais | Decepção em produção; framework vira débito técnico | Cai 2-3x em 3 anos | Fragmentação por jurisdição; deploy cross-border caro | Economia conservadora ganha; quem queimou capital paga juros; arquitetura modular sobrevive |

| Horizonte | Foco da decisão | Cadência de revisão |
|-----------|-----------------|---------------------|
| 12 meses | Refinamento do plano corrente; orçamento anual | Trimestral |
| 36 meses | Estratégia de produto, plataforma, talento | Semestral |
| 60 meses | Capital de longo prazo, parcerias estruturais; AGI em aberto | Anual |

---

## 20.10 — Checklist Do Capítulo

- [ ] Construir três planos de orçamento, três planos de roadmap de produto e três planos de talento, com mapeamento explícito dos cenários otimista, mediano e pessimista
- [ ] Listar quatro vetores de mudança (capacidade, autonomia, custo, regulação) com leitura atual de cada vetor
- [ ] Definir, para cada vetor, três sinais observáveis que justificariam mover a leitura predominante entre cenários
- [ ] Atribuir probabilidade subjetiva qualitativa (provável, possível, improvável) para cada cenário, com critério articulado
- [ ] Instituir rito trimestral do AI Council para revisão da leitura predominante, com agenda preparada e ata formal
- [ ] Construir slide-padrão de comunicação por cenários para Conselho, investidores e clientes enterprise
- [ ] Manter plano de capital de longo prazo com investimento sustentado em fundamentos institucionais (governança, evals, observabilidade), robusto em ambos os polos da questão AGI
- [ ] Documentar, em formato vivo, a leitura predominante atual, com data, autor e sinais que poderiam mudá-la
- [ ] Revisar conexão entre Método de Decisão para Adotar IA (F1) e leitura predominante de cenário, garantindo coerência

---

## 20.11 — Perguntas De Revisão

1. Em qual cenário a sua organização opera hoje, e quais três sinais o moveriam para o cenário adjacente?
2. Os três planos (orçamento, produto, talento) estão construídos para os três cenários, ou a organização tem apenas o plano-base?
3. Quem é o Accountable institucional pela leitura de cenário, e com qual cadência ela é revisada?
4. Como você explicaria, em três frases, para um membro do Conselho que exige número único, a razão de o método operar com probabilidade subjetiva qualitativa em vez de probabilidade numérica?
5. Qual investimento, hoje, paga em todos os três cenários a trinta e seis meses, e por quê?
6. Em que ponto a questão AGI muda materialmente seu plano de capital de longo prazo, e em que ponto não muda?

---

## 20.12 — Exercícios Práticos

**Exercício 1 — Construa seu próprio cenário.** Para o seu setor (não para IA em geral), descreva o cenário mediano a trinta e seis meses, com leitura dos quatro vetores aplicada ao seu setor (capacidade que importa para você, autonomia que importa para você, custo que importa para você, regulação setorial que importa para você). Identifique três sinais que moveriam a leitura para cenário pessimista e três que moveriam para otimista.

**Exercício 2 — Mapeie o movimento atual.** Identifique, com base em sinais observados nos últimos seis meses, em qual cenário a sua organização está hoje. Justifique a leitura com pelo menos cinco sinais concretos (releases, custo observado, sinais regulatórios, sinais de mercado, sinais internos), e documente em formato que possa ser revisado em trimestre.

**Exercício 3 — Plano triplo para uma decisão concreta.** Escolha uma decisão de IA pendente em sua organização (escolha de modelo, adoção de framework, contratação de squad, investimento em LLMOps). Construa três versões do plano correspondente, uma para cada cenário, com gatilho explícito de ativação de cada uma.

**Exercício 4 — Apresentação por cenários.** Construa apresentação de quinze minutos para o Conselho (ou para investidores) que comunique o plano de IA por cenários, com slide por cenário, slide de sinais monitorados e slide de gatilhos de transição. Submeta a apresentação à crítica de pelo menos um par sênior antes de levar ao Conselho.

---

## 20.13 — Projeto Do Capítulo

**Documento de Cenários Estratégicos da Organização.** Produzir documento formal de cenários estratégicos de IA da sua organização, com:

1. Leitura atual dos quatro vetores (capacidade, autonomia, custo, regulação), com fontes e data
2. Três cenários (otimista, mediano, pessimista) em horizonte de trinta e seis meses, com narrativa de uma página por cenário
3. Cenário sumário a sessenta meses, com posição declarada sobre AGI (sem tomar partido absoluto, com argumentos pró e contra)
4. Probabilidade subjetiva qualitativa atribuída a cada cenário, com critério articulado
5. Plano triplo para três dimensões críticas (orçamento, produto, talento) por cenário
6. Lista de sinais monitorados, com responsável nominal e cadência
7. Calendário de revisão trimestral, semestral e anual, com Accountables
8. Slide-padrão de comunicação para Conselho e investidores

**Critério de qualidade.** O documento é aprovado em uma reunião do AI Council e usado como insumo principal da próxima rodada de planejamento orçamentário.

---

## 20.14 — Referências Principais

**◆ Sobre planejamento por cenários**

- Wack, P. *Scenarios: Uncoupled and Uncharted Waters Ahead* (Harvard Business Review, 1985) — a fundação metodológica do planejamento por cenários, aplicada à crise do petróleo na Shell.
- Schoemaker, P. *Scenario Planning: A Tool for Strategic Thinking* (MIT Sloan Management Review, 1995) — o método aplicado em ambiente corporativo.
- Tetlock, P. *Superforecasting: The Art and Science of Prediction* (2015) — a literatura empírica sobre por que previsões pontuais erram e por que probabilidade subjetiva calibrada vence.

**◆ Sobre trajetória de capacidade em IA**

- Epoch AI — relatórios públicos sobre escala de modelos, custo de treinamento e custo de inferência, com dados primários verificáveis.
- Statements públicos de Anthropic, OpenAI, Google DeepMind, sobre roadmap de modelos (a serem lidos com hermenêutica corporativa, sabendo que comunicação executiva tem viés).
- Papers sobre platô e sobre limites arquiteturais de transformers (a literatura é abundante, com vozes em ambas as direções; ler em conjunto, não isoladamente).

**◆ Sobre regulação de IA**

- EU AI Act (texto consolidado) e materiais de transposição.
- NIST AI Risk Management Framework.
- Brasil: PL 2338/2023 e materiais da ANPD sobre IA.

**◆ Inteligência Aumentada — sistema da obra**

- Manifesto dos Invariantes — Introdução.
- Framework F1 — Método de Decisão para Adotar IA (alimenta cada cenário).
- Framework F3 — Escala de Propriedade do Agente (central no vetor autonomia).
- Apêndice J — Trilha do Número (deste livro), com números atualizados e fontes datadas.

---

## 20.15 — Autoavaliação

| # | Critério | Você consegue? |
|---|----------|----------------|
| 1 | **Clareza** — Explicar a um membro do Conselho, em cinco minutos, a diferença entre previsão pontual e cenário estruturado, com analogia do piloto | ☐ |
| 2 | **Profundidade** — Defender em discussão técnica por que probabilidade subjetiva qualitativa é mais responsável que probabilidade numérica em campo de alta turbulência | ☐ |
| 3 | **Aplicação** — Construir, nas próximas duas semanas, os três planos (orçamento, produto, talento) para os três cenários a trinta e seis meses na sua organização | ☐ |
| 4 | **Conexão** — Articular como o método de cenários se conecta com o Método de Decisão para Adotar IA (F1), com a Escala de Propriedade do Agente (F3), com o Custo Composto em Três Tempos (F7) e com a Camada Dupla (Princípio 3) | ☐ |
| 5 | **Curiosidade ativa** — Está com vontade de instituir o rito trimestral do AI Council para revisão da leitura de cenário, ainda nesta semana | ☐ |

---

> *"O futuro da IA não se prevê, se planeja em três caminhos, e a empresa que vence é a que tem plano ativo para os três e a que ajusta o curso conforme os sinais. Profecia é luxo de quem não responde ao Conselho."*

</div>
</section>



<section class="capitulo-bloco">
<div class="abertura-capitulo">
<div class="bandeira-nivel bandeira-intermediario-avancado">Inter·Avanc</div>
# 21. Evals — A Engenharia de Medir IA

> *"Trocar prompt 'porque ficou melhor' sem golden set é torcida, não decisão. Eval é o que separa engenharia de fé."*

## O conceito intuitivo

<p class="dropcap">Há uma cena que se repete em times que adotaram IA generativa em produção sem ter passado pela disciplina de medi-la. O Product Manager pergunta "como está a qualidade do nosso copiloto?", e a resposta vem em três versões. A primeira é "está boa, os usuários têm gostado", baseada em algumas conversas no Slack e em duas reuniões com clientes. A segunda é "passou na nossa bateria de testes da semana", baseada em vinte casos rodados manualmente por um engenheiro. A terceira é "o LLM que avalia diz que melhorou", baseada em um juiz que ninguém calibrou contra humano. Nenhuma das três é eval, e essa confusão custa caro porque mascara regressão até ela virar incidente.</p>

Eval, em sentido técnico preciso, é a disciplina de medir sistematicamente a qualidade de saídas de IA contra critérios definidos, com dados representativos, em ciclos que rodam tanto em desenvolvimento quanto em produção, com critério de bloqueio explícito e auditoria do que cada release entregou. Não é teste manual, não é vibe, não é demonstração de cliente, não é benchmark público. É a infraestrutura cognitiva que transforma operação de IA em disciplina engenheirável.

A diferença entre quem tem eval real e quem não tem aparece em dois lugares. No deploy, porque quem tem eval consegue dizer "rodou contra 200 casos do golden set e melhorou em 92% deles, regrediu em 3% que estamos investigando, manteve em 5%". Quem não tem só consegue dizer "ficou melhor". No incidente, porque quem tem eval consegue rastrear a regressão até a mudança específica de prompt, modelo ou tool que a causou. Quem não tem entra em pânico, tenta voltar a uma versão "que parecia boa", e descobre que perdeu o registro do que era.

A boa notícia é que eval não exige investimento absurdo. A pirâmide canônica desta disciplina, que apresentaremos formalmente como a Pirâmide da Avaliação, tem base barata e topo caro, e a maioria dos times consegue valor real começando pela base. A má notícia é que a maior parte das organizações ainda não começou, e está tomando decisão de modelo, de prompt e de fornecedor sem instrumento para medir o que efetivamente entrega.

## Analogia: o laboratório clínico que nunca fecha

Pense numa rede hospitalar séria, com cobertura nacional, plantão 24 horas, complexidade real. Imagine que essa rede operasse sem laboratório clínico próprio, sem exame de sangue regular, sem protocolo de checagem cruzada entre diagnósticos. A rede ainda atenderia pacientes — médicos competentes conseguem chegar em boas conclusões com anamnese, exame físico e bom senso. Mas quando algo desse errado, ninguém saberia identificar a causa. Quando um protocolo precisasse ser ajustado, a decisão seria por intuição. Quando o resultado de um departamento começasse a cair, a regressão seria descoberta tarde, quando já tivesse virado óbito.

Nenhuma rede hospitalar séria opera assim. Existe laboratório, existe protocolo de exame regular para cada classe de paciente, existe controle de qualidade dos próprios exames (sim, o laboratório precisa medir a si mesmo), existe trilha de auditoria por amostra. O laboratório não substitui o médico, e nem entrega o diagnóstico final. O laboratório dá ao médico o termômetro sem o qual a decisão fica no escuro.

Em IA, eval é o laboratório clínico do sistema. Não substitui o engenheiro, não decide pelo Product Manager, não escolhe o modelo. Dá ao time o termômetro com que se decide, se itera, se governa. E exige a mesma disciplina de qualidade que o laboratório clínico exige: golden set bem construído é o equivalente a amostras de controle calibradas, LLM-as-judge sem calibração é o equivalente a exame sem padrão de referência, regressão por subgrupo é o equivalente a olhar apenas a média sem ver o que aconteceu com a UTI pediátrica. Quem opera IA sem laboratório opera no escuro, e descobre as falhas pelo paciente, quer dizer, pelo cliente, que reclama tarde demais.

## Explicação técnica

### Os dois eixos: offline e online

Eval é organizado em dois grandes eixos.

Eval offline acontece antes do deploy, sobre dataset controlado, com gabarito conhecido. É o que roda em pull request, em CI/CD, em release candidate. Sua função é detectar regressão antes que ela chegue ao usuário. Inclui golden set, adversarial set, drift set, testes determinísticos, LLM-as-judge calibrado, rubrica humana.

Eval online acontece em produção, sobre tráfego real, sem gabarito predefinido. Sua função é detectar problemas que escaparam ao offline e mapear lacunas do golden set. Inclui sampling de produção para rotulagem contínua, feedback de usuário, monitoramento de drift de distribuição, monitoramento de custo e latência, monitoramento de segurança contra jailbreak, prompt injection e conteúdo proibido.

Os dois se alimentam mutuamente em ciclo. Falha em produção que não foi capturada offline indica buraco no golden set, que entra no próximo ciclo de eval offline. Caso de teste novo que aparece no adversarial set é incluído no monitoramento de produção. Essa retroalimentação é o que mantém o laboratório vivo.

### A pirâmide canônica

![Pirâmide da avaliação — hierarquia por criticidade e custo](file:///sessions/relaxed-cool-bell/mnt/Ebook IA/Livro-1-Os-Invariantes/02-capitulos/imagens/L1-C39-img-01-piramide-evals.svg)

A pirâmide da avaliação organiza os evals por criticidade e custo, em três camadas verticais e uma transversal.

A base é composta por testes determinísticos. Schema validation, em que a saída obedece ao formato esperado, exact match para campos críticos contra gabarito, regex para padrões obrigatórios, validações estruturais como JSON parseável e citação no formato exigido. Cobertura de 100% das chamadas em CI, custo muito baixo. Detecta a maior parte das regressões grosseiras, com formato quebrado, campo faltante, alucinação estrutural, antes que cheguem a camadas mais caras.

O meio é golden set com LLM-as-judge calibrado. Conjunto fixo de casos com gabarito de qualidade, julgado por LLM seguindo rubrica explícita, com calibração regular contra humano sênior. Cobertura de 30% a 80% das chamadas conforme criticidade. Custo médio. Detecta regressão de qualidade que escapa da base e cobre casos de geração aberta onde exact match não funciona.

O topo é rubrica humana especialista. Revisão de amostra por especialista do domínio em release crítico, em auditoria mensal ou trimestral, em incidente sob investigação. Cobertura de 5% a 15% da carga, por amostra. Custo alto. Detecta nuances que LLM-as-judge não capta e calibra o juiz LLM contra o critério humano.

A camada transversal é adversarial e segurança. Casos que sabidamente quebram o sistema, como jailbreak, prompt injection, conteúdo proibido, sycophancy, viés, mantidos em conjunto separado, rodados a cada release crítico e em cadência mensal. Não substitui a pirâmide vertical, complementa.

A regra de bolso é construir a base primeiro, depois o meio, depois o topo. Quase todo time tem condição de subir a base em uma semana de trabalho. O meio leva entre uma e quatro semanas para a primeira versão sólida. O topo entra quando o produto cresce e a auditoria humana vira parte do contrato com o usuário ou do regime regulatório.

### Os seis tipos canônicos de eval

| Tipo | O que mede | Quando funciona | Armadilha clássica |
|------|------------|-----------------|---------------------|
| **Determinística** | Estrutura, campo crítico, padrão obrigatório | Saídas estruturadas (JSON, classificação, extração) | Saídas abertas; precisa combinar com outros tipos |
| **Por similaridade** | Embedding, BLEU, ROUGE, BERTScore | Geração aberta com gabarito de "resposta canônica" | Mede forma, não semântica; texto certo com paráfrase diferente pode pontuar mal |
| **Rubrica humana** | Critério de qualidade definido por especialista | Domínio específico, casos críticos | Lento, caro, baixo throughput; serve só no topo |
| **LLM-as-judge** | Rubrica explícita aplicada por outro LLM | Cobertura de volume com critério padronizado | Viés de auto-validação se juiz = gerador; precisa calibração contra humano |
| **Comportamental** | Resposta a casos de segurança, viés, jailbreak | Compliance, alignment, governança | Conjunto fica desatualizado se não for renovado |
| **Econômica** | Custo por resolução, latência, retentativa | Decisão de roteamento, otimização de stack | Ignorar pode mascarar regressão de qualidade que veio com troca de modelo "mais barato" |

### Golden set: o ativo central da operação de eval

O golden set é o conjunto fixo de casos com gabarito que serve de referência estável para detectar regressão. É o ativo mais importante de qualquer operação madura de IA, e também o mais negligenciado.

Para construção, comece com 30 a 50 casos representativos da carga real, não de casos teóricos, cobrindo as classes principais de uso. Para cada caso, defina o gabarito junto com especialista do domínio: não é trivial decidir o que é "resposta certa" para uma pergunta aberta, e a definição precisa ser explícita. Documente o porquê de cada caso estar no golden, porque sem isso o conjunto vira manutenção opaca em seis meses. Mantenha proporção entre classes alinhada à distribuição real de produção.

Sobre tamanho mínimo, não há número universal. A regra prática é que 30 casos por classe crítica é o mínimo para começar a detectar regressão significativa, 100 a 200 por classe é confortável para a maioria dos times de tamanho médio, 500 ou mais aparece em times maduros com cobertura larga. O golden set cresce com a operação, e o que importa é ser representativo e versionado, não enorme.

Sobre manutenção, o golden set precisa ser revisado periodicamente. Casos que perderam relevância são aposentados. Casos novos que aparecem em produção, especialmente os que falharam, são incluídos. Distribuição é recalibrada se a carga de produção mudou. Sem manutenção, o golden vira folclore que não bate com a realidade do sistema.

Sobre versionamento, cada release que muda o golden set documenta a mudança. Cada decisão de eval que usa o golden registra a versão. Sem versionamento, "passou no eval" perde significado porque ninguém sabe contra o que passou.

### LLM-as-judge: quando confiar, quando duvidar

![Quadrante de uso do LLM-as-judge — quando confiar e quando duvidar](file:///sessions/relaxed-cool-bell/mnt/Ebook IA/Livro-1-Os-Invariantes/02-capitulos/imagens/L1-C39-img-03-quadrante-llm-as-judge.svg)

Usar um LLM para julgar a saída de outro LLM é técnica poderosa de escala, e é também uma das fontes mais comuns de eval enganoso. Vale entender em que condições funciona e em que condições produz ilusão.

Funciona quando a rubrica é explícita e separa claramente bom de ruim, o juiz é modelo diferente do gerador, o que mitiga viés de auto-validação, a rubrica foi calibrada contra avaliadores humanos seniores em pelo menos 30 a 50 casos, com correlação alvo acima de 0,7, o juiz é re-calibrado mensalmente para detectar drift, ensemble de juízes é usado em decisões críticas, e a saída do juiz inclui justificativa estruturada para amostragem auditável.

Não funciona quando a rubrica é vaga, algo como "diga se ficou bom", o juiz é o próprio gerador ou da mesma família, com auto-validação inflada, não houve calibração contra humano, o juiz é tratado como verdade absoluta em decisão de produção sem cross-check, ou o adversarial set não inclui casos em que o juiz sabidamente erra.

O quadrante de decisão cruza dois eixos. Especificidade da rubrica, de vaga a muito específica, e risco da decisão, de baixo a alto. Rubrica vaga e baixo risco aceitam LLM-as-judge com revisão amostral. Rubrica vaga e alto risco exigem humano. Rubrica específica e baixo risco permitem LLM-as-judge isolado. Rubrica específica e alto risco demandam LLM-as-judge calibrado, com ensemble e auditoria humana de amostra.

### Métricas por tipo de tarefa

Não existe métrica universal. Cada tipo de tarefa tem métricas primária e secundária:

| Tipo de tarefa | Métrica primária | Métricas secundárias |
|----------------|------------------|----------------------|
| **Classificação** | F1 ponderada por classe | Precision/recall por classe, matriz de confusão |
| **Extração estruturada** | F1 por campo | Cobertura (% de chamadas com extração válida) |
| **Geração aberta** | Rubrica humana ou LLM-as-judge calibrado | Faithfulness (não inventou), relevância, completude, estilo |
| **Resposta ancorada (RAG)** | Faithfulness + answer relevance | Context precision, recall do retriever, citação correta |
| **Agente** | Taxa de sucesso de tarefa end-to-end | Passos, custo, regressão por subtarefa |
| **Segurança** | Taxa de rejeição correta | Over-refusal (recusas indevidas), taxa de jailbreak bem-sucedido |
| **Robustez** | Variância em N execuções | Consistência semântica |
| **Custo/latência** | CPR (cost per resolution) | CAA (custo agregado por agente), p50/p95 de latência |

Sobre acurácia agregada, uma regra dura: ela esconde regressão por subgrupo. Toda métrica de qualidade deve ter cortes, por classe, por segmento, por persona, por idioma, por região, por canal. Times que olham só a média perdem regressão silenciosa que aparece em produção como reclamação concentrada de uma classe específica.

### Regressão em CI/CD: o gate que separa engenharia de fé

Toda mudança que afeta o comportamento do sistema, com prompt, modelo, tool, system prompt, dataset de RAG, política de classificação, deve passar por eval automatizado antes de chegar à produção. A arquitetura canônica segue oito passos.

Primeiro, branch. Engenheiro abre branch com a mudança proposta.

Segundo, eval offline em CI. Pipeline roda golden set e adversarial set automaticamente.

Terceiro, scorecard gerado. Comparação automática com baseline da main, com delta por métrica e por subgrupo.

Quarto, gate de bloqueio. Política explícita do que bloqueia merge. Tipicamente, regressão acima de um limite na métrica primária bloqueia automaticamente, regressão intermediária gera alerta para revisão humana, melhoria ou estabilidade permite merge.

Quinto, code review. Revisor olha código e scorecard. Mudança que melhora métrica mas piora subgrupo crítico não passa.

Sexto, merge. Após aprovação, mudança vai para staging.

Sétimo, canário em produção. Deploy progressivo, de 1% a 10%, 50% e 100%, com eval online medindo qualidade real.

Oitavo, promoção ou rollback. Critério explícito de promoção, com scorecard verde por horas determinadas, ou de rollback ao detectar regressão.

Changelog de prompt é obrigatório a cada release. Documenta o que mudou, o motivo, o delta de scorecard, o subgrupo mais afetado. Sem changelog, troubleshooting de regressão em três meses vira arqueologia.

### Eval em produção: o ciclo que mantém o laboratório vivo

O eval offline detecta o que sabe procurar. O eval em produção descobre o que ninguém esperava. A arquitetura mínima envolve telemetria, sampling, feedback e loop fechado.

Telemetria: cada chamada loga input completo sanitizado de PII conforme política de LGPD, output completo, latência por passo, tokens in/out, custo computado, versão de prompt, versão de tool, modelo usado, ID de sessão, ID de usuário anonimizado conforme política. Sem telemetria, eval em produção não existe.

Sampling para rotulagem: subconjunto representativo da carga é separado para rotulagem humana contínua. Tipicamente 0,5% a 2% do volume, distribuído por classe. Esses casos viram a próxima geração do golden set.

Feedback de usuário: thumbs up/down, correção explícita, abandono, retentativa, escalonamento para humano. Cada sinal é proxy imperfeito de qualidade, mas a combinação informa onde olhar.

Loop fechado: casos que falharam em produção e foram rotulados entram no próximo ciclo de eval offline. Casos novos no adversarial vêm de produção, não da cabeça do time. Sem esse loop, o golden set congela e o eval vira ritual.

### Os sete erros típicos mais frequentes, com antídoto

| Erro típico | Por que mata | Antídoto |
|-------------|--------------|----------|
| Vibe-eval, com "rodei 5 casos e ficou bom" | Ruído pessoal vira norma; viés do testador inflado | Golden set fixo, versionado, mínimo 30 casos por classe |
| Métrica única agregada, com "acurácia subiu 2%" | Esconde regressão por subgrupo crítico | Cortes por classe, segmento, persona |
| LLM-as-judge sem calibração | Auto-validação enviesa; juiz e gerador da mesma família correlacionam erros | Juiz diferente do gerador, calibração contra humano em 30 ou mais casos, ensemble em decisões críticas |
| "Passou no MMLU" | Benchmark público não reflete a carga da empresa | Golden set próprio e adversarial sobre carga real |
| "Vamos medir depois" | Depois nunca chega; quando precisa, vira incidente | Gate de CI desde o primeiro deploy, mesmo que mínimo |
| "Eval é caro" | Regressão silenciosa é mais cara, e detectada tarde | Pirâmide com base barata; topo só onde justifica |
| Happy path only | Adversarial fica fora; sycophancy, jailbreak e viés passam | Conjunto adversarial separado, renovado por trimestre |

## Exemplo memorável: a consultoria que quase quebrou pela ausência de golden set

Cenário ilustrativo composto a partir de padrões observados em consultorias estratégicas brasileiras durante adoção de IA generativa. Números são realistas mas não identificam empresa específica.

Atlas Strategy, consultoria brasileira de estratégia com cerca de 120 consultores. Implementou um agente de redação de relatórios para clientes corporativos, com o objetivo de reduzir o tempo médio de produção de relatório mensal de 18 horas para algo entre 6 e 8 horas por consultor. O sistema integrava um modelo de linguagem moderno para a redação, skills proprietárias com voz autoral da Atlas, projetos por cliente com histórico, e RAG sobre base de cases anteriores.

Nas primeiras quatro semanas, o entusiasmo foi alto. Consultores entregavam mais relatórios em menos tempo. Sócios viam ganho de margem. A diretoria da Atlas considerou o projeto sucesso e direcionou investimento para expandir. Não havia golden set, não havia LLM-as-judge calibrado, não havia regressão em CI. A validação se resumia a três sócios lendo quatro relatórios na sexta-feira, e dando sinal verde se "tivessem soado certo".

Na sétima semana, um cliente do setor industrial recebeu um relatório com três parágrafos que continham números trocados. As fórmulas eram corretas. Os valores de entrada estavam errados, copiados de outro caso do trimestre anterior. O cliente pegou o erro porque era ele quem produzia os números originais. Mandou e-mail. A sócia-fundadora abriu o e-mail, leu, e em quinze minutos sabia que tinha problema sério. Em dois dias, mapearam outros três relatórios entregues no mês com erros numéricos similares. Em uma semana, dois clientes adicionais reportaram inconsistências.

A investigação revelou o que sempre revela: duas mudanças de prompt feitas em sequência por engenheiros diferentes, ambas com boa intenção. A primeira para "tornar mais conciso", a segunda para "soar mais executivo". Cada mudança, isoladamente, melhorou a percepção de qualidade dos sócios na sexta de validação. Combinadas, corromperam o passo de extração numérica em silêncio. Não havia como saber que tinham corrompido, porque ninguém estava medindo faithfulness numérico contra um conjunto fixo de casos.

A Atlas fez três mudanças permanentes, todas alinhadas ao Princípio 7. Primeira, construiu golden set de 80 relatórios reais com gabarito de números e tese, anotado pelos três sócios em sessões dedicadas. Toda mudança de prompt passa a rodar contra esse conjunto antes de merge. Segunda, implementou LLM-as-judge com rubrica explícita para faithfulness numérico, calibrado contra os três sócios em 30 itens de calibração, com correlação alvo acima de 0,8. Terceira, criou scorecard versionado por release de prompt, com bloqueio automático se faithfulness numérico cair acima de 1 ponto contra o baseline.

Em seis meses, regressões silenciosas zeraram. O tempo de revisão humana por relatório caiu pela metade, porque o gate filtrava o ruído antes do humano ver. A Atlas perdeu dois clientes durante o incidente, recuperou um, e usa o caso internamente como exemplo do que custa não medir. A lição estrutural não está na escolha do modelo, da skill ou do RAG. Está na ausência inicial do termômetro. Eval não é luxo de big tech, é a diferença entre engenharia e fé. Quem não tem golden set não tem produto de IA, tem aposta documentada.

Para executivos: se sua organização tem IA em produção tocando cliente, faça uma pergunta direta ao time técnico hoje. Qual é o golden set do nosso sistema, e quando foi a última vez que rodamos regressão contra ele? Se a resposta envolver hesitação ou referência a "testes manuais", você está em risco. Eval é decisão de governança técnica, e exige investimento proporcional ao risco. Times maduros tratam golden set como ativo organizacional, com versionamento, dono nominal, e revisão trimestral.

> **Rigor estatístico do caso.** Medições da Atlas Strategy realizadas em janela de seis meses pós-incidente, com aproximadamente 480 relatórios analisados retrospectivamente em revisão por dois consultores sêniores independentes, golden set final estabilizado em 215 casos representativos, intervalo de confiança 95% sobre taxa de detecção de regressão, validação cruzada com revisão humana cega nos primeiros sessenta dias do gate de qualidade implantado. Caso composto a partir de padrões observados em mais de uma consultoria estratégica do mercado brasileiro — atribuição nominal sugerida para edições futuras, conforme pacto editorial descrito no paratexto "Sobre os casos desta obra".

## Quando usar e quando evitar

Implantar eval formal, com golden set, CI e telemetria de produção, sempre que a IA toca cliente externo, a saída entra em decisão financeira, jurídica, regulatória ou clínica, a equipe muda prompt ou modelo mais de uma vez por mês, existe SLA explícito ou implícito de qualidade, há caso regulado, como LGPD com decisão automatizada, AI Act, ISO 42001, ou múltiplos engenheiros mexem no mesmo prompt.

Subset mínimo viável, sem overhead completo, quando há piloto interno de baixo risco, com um usuário, por uma semana, teste de ideia descartável que não vai à produção, ou demo única para conselho ou prospect.

Em todo caso intermediário, comece pela base da pirâmide. Suba camadas conforme o produto crescer.

## Vantagens e limitações

| Vantagem | Limitação |
|----------|-----------|
| Transforma IA de fé em engenharia | Custo inicial alto: construir golden set é trabalho lento e demanda especialista do domínio |
| Permite migração de modelo e troca de prompt sem medo | Risco de overfit ao golden set, exigindo adversarial e produção rotulada como contrapesos |
| Cria scorecard auditável para governança e compliance | LLM-as-judge tem viés sistemático sem calibração; manutenção do juiz é trabalho recorrente |
| Detecta regressão silenciosa antes do usuário | Acurácia agregada engana; exige cortes por subgrupo que custam mais para reportar |
| Reduz MTTR (tempo de recuperação de incidente) | Cultura de eval demanda mudança organizacional; em times resistentes, vira teatro de compliance |
| Permite decisão de modelo em sua própria carga | Versão de modelo desatualizada no golden set distorce comparação; renovação periódica é obrigatória |

Este capítulo conversa especialmente com os capítulos sobre tokens, RAG, fine-tuning, agentes, AI Engineering, comparação de modelos, economia de tokens, LLMOps, alignment e governança.

## Resumo

| Conceito | Síntese |
|----------|---------|
| Definição | Disciplina de medir sistematicamente qualidade de IA, com dados representativos, em ciclos automatizados, com critério de bloqueio explícito |
| Eixos | Offline antes do deploy e online em produção, com ciclo de retroalimentação |
| Pirâmide | Base determinística (100%), meio com golden e LLM-as-judge (30-80%), topo humano (5-15%) e adversarial transversal |
| Seis tipos | Determinística, similaridade, rubrica humana, LLM-as-judge, comportamental, econômica |
| Golden set | 30 a 50 casos para começar, crescimento orgânico, versionamento obrigatório, manutenção trimestral |
| LLM-as-judge | Funciona com rubrica específica, juiz diferente do gerador e calibração contra humano em 30 ou mais casos; duvidoso sem isso |
| Métricas | Variam por tipo de tarefa; acurácia agregada esconde regressão por subgrupo |
| CI | Gate explícito de bloqueio, scorecard com delta, canário em produção, rollback testado |
| Erros típicos | Vibe-eval, métrica única, juiz não calibrado, dependência de benchmark público, postergação, alegação de custo, happy path |

## Checklist do capítulo

- [ ] Distinguir, em uma frase, eval offline de eval online
- [ ] Descrever as três camadas da pirâmide e a faixa de cobertura típica de cada
- [ ] Citar os seis tipos canônicos de eval e quando cada um funciona
- [ ] Defender a regra de juiz diferente do gerador para LLM-as-judge em mesa técnica
- [ ] Construir um golden set inicial de 30 a 50 casos do seu produto
- [ ] Escrever a rubrica de LLM-as-judge para um caso real, com 4 a 6 critérios objetivos
- [ ] Definir, no seu time, qual delta de métrica bloqueia merge e qual gera alerta
- [ ] Apresentar a Pirâmide da Avaliação em reunião executiva em até 5 minutos
- [ ] Identificar três cortes ou subgrupos que sua acurácia agregada está escondendo hoje
- [ ] Mapear, no seu produto, qual tipo de eval cobriria qual classe de falha
- [ ] Reconhecer, em três frases recentes do seu time, qual erro típico elas correspondem

## Perguntas de revisão

1. Por que "ficou melhor" não é critério, e o que precisa entrar no lugar?
2. Em que situação LLM-as-judge é viés institucionalizado, e como você detecta?
3. Por que adversarial set importa mais que golden set no longo prazo?
4. O que muda na decisão de migração de modelo quando há golden set, e o que muda quando não há?
5. Por que a regra de juiz diferente do gerador é estrutural, não preferência?
6. Como o ciclo offline para online e de volta mantém o eval vivo?
7. Qual a relação entre o Princípio 7 (Termômetro) e o Princípio 8 (Responsabilidade Indelegável)?
8. Por que acurácia agregada esconde regressão silenciosa, e que método combate?
9. Em qual classe de produto faz sentido começar pelo topo da pirâmide?

## Exercícios práticos

Exercício 1, classificação de falhas reais. Liste 5 falhas reais, próprias ou do mercado, que sua operação enfrentou nos últimos 6 meses. Para cada uma, classifique: teria sido capturada por golden set? Por LLM-as-judge? Por adversarial? Por humano? Mapeie quais camadas da pirâmide faltam hoje na sua operação.

Exercício 2, pirâmide do seu produto. Desenhe a Pirâmide da Avaliação para o seu produto ou operação. Atribua percentual de cobertura atual em cada camada. Identifique a camada mais frágil e proponha plano de remediação em 30 dias.

Exercício 3, rubrica de LLM-as-judge. Para um caso real do seu produto, escreva rubrica de LLM-as-judge com 4 a 6 critérios objetivos. Defina o que é resposta máxima e o que é resposta mínima em cada critério. Calibre contra você mesmo em 10 casos. Em seguida, calibre contra um par. Compare. O que aprendeu?

Exercício 4, adversarial set inicial. Projete o adversarial set de 20 casos para o seu sistema. Inclua pedidos potencialmente perigosos, pedidos com indução de sycophancy, casos com viés conhecido, jailbreak via instrução, prompt injection via dado de entrada. Rode contra o sistema atual e documente o resultado.

## Projeto do capítulo

Construa o Caderno de Evals do seu produto ou operação, em 8 a 12 páginas e opcionalmente um repositório, contendo definição explícita do que é resposta certa para a sua classe de tarefa, golden set inicial de 30 a 50 casos com gabarito anotado, rubrica de LLM-as-judge calibrada contra humano em pelo menos 30 itens, política de bloqueio em CI, adversarial set de pelo menos 20 casos, telemetria mínima de produção, plano de revisão trimestral do golden set e mensal do adversarial, e dono nominal do caderno designado por escrito.

Critério de qualidade do projeto: outro engenheiro, sem contexto, consegue ler o caderno e rodar o eval contra uma nova mudança de prompt. Se precisar perguntar mais de três coisas, o caderno está incompleto.

## Referências principais

Frameworks e padrões: OpenAI Evals, inspect-ai, HELM da Stanford CRFM (Liang et al., 2022), BIG-bench (Srivastava et al., 2022).

LLM-as-judge: Zheng et al., Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena (2023); Liu et al., G-Eval (2023).

RAG e métricas específicas: RAGAS (Es et al., 2023); Faithfulness in NLG (literatura desde 2020).

Adversarial e segurança: HarmBench (Mazeika et al., 2024); JailbreakBench (Chao et al., 2024); BBQ (Parrish et al., 2022).

Sobre as dificuldades genuínas de avaliar LLMs: Narayanan, A. & Kapoor, S., "Evaluating LLMs is a minefield" (Princeton, 2023); Karpathy, comentários públicos sobre limitações de benchmarks.

## Autoavaliação

| # | Critério | Você consegue? |
|---|----------|----------------|
| 1 | Clareza: explicar para um diretor não-técnico em 90 segundos por que "ficou melhor" não é critério, usando a metáfora do laboratório clínico | ☐ |
| 2 | Profundidade: defender em reunião técnica por que LLM-as-judge sem calibração contra humano é viés institucionalizado, citando o quadrante de decisão e a regra de juiz diferente do gerador | ☐ |
| 3 | Aplicação: iniciar a primeira versão do golden set do seu produto esta semana, com pelo menos 30 casos representativos | ☐ |
| 4 | Conexão: articular como o capítulo amarra o Princípio 7, RAG, LLMOps, alignment e governança | ☐ |
| 5 | Curiosidade: vontade de entrar no próximo capítulo para entender como esse eval roda em produção, com tracing, versionamento e rollback proporcionais | ☐ |

</div>
</section>



<section class="capitulo-bloco">
<div class="abertura-capitulo">
<div class="bandeira-nivel bandeira-intermediario-avancado">Inter·Avanc</div>
# 22. LLMOps — A Operação de IA em Produção

> *"Autonomia sem observabilidade é loop com cartão de crédito. O que destrói orçamento de IA não é o preço do token, é a falta de instrumentação que faz cada incidente custar duas semanas para ser visto."*

## O conceito intuitivo

<p class="dropcap">Há uma classe de equipe que adotou IA generativa em produção e descobriu, no susto, que o trabalho mais difícil não estava em escolher o modelo. Estava em operar. Operar significa ter resposta para perguntas que aparecem sempre, sempre nas piores horas. Quem está usando agente? Quanto custou o último mês, por feature? Por que aquele cliente recebeu uma resposta errada na quinta-feira? Em quanto tempo conseguimos voltar à versão de prompt de duas semanas atrás? Quem alterou esse system prompt? Quando? Por quê? Há logs? Cada pergunta dessa é resposta a um pilar de LLMOps. Times que têm os pilares, respondem em minutos. Times que não têm, respondem em dias, e às vezes não respondem.</p>

LLMOps é a disciplina que cobre essa operação. Não é MLOps clássico com nome novo, e essa distinção merece atenção. MLOps clássico foi construído sobre o ciclo treinar modelo, versionar modelo, deployar modelo, monitorar drift de dados, retreinar. O que se versiona é o modelo, o que se monitora é drift estatístico, o que se retreina é o modelo. LLMOps trabalha em outra arena. O modelo, na maioria dos casos, é externo, fornecido por um dos grandes laboratórios. O que se versiona é prompt, tool, system prompt, dataset de RAG, política de classificação. O que se monitora inclui drift de distribuição, mas inclui também alucinação, custo composto, latência variável, prompt injection, dependência de vendor. O que se "retreina" é o prompt versionado e o golden set, não o modelo.

A confusão custa caro. Times que assumem "é igual a MLOps" descobrem que o ferramental e a cultura precisam ser adaptados. Times que assumem "não precisamos disso porque o modelo é externo" descobrem que o que opera não é o modelo, é o sistema em volta. Este capítulo é o que precisa ser ensinado para que o leitor pare de aprender LLMOps pelo incidente.

A boa notícia é que LLMOps tem sete pilares canônicos, definidos com clareza suficiente para virar checklist. A regra prática é construir do pilar 1 ao pilar 7 conforme o produto amadurece, e nunca subir nível de autonomia além do que os pilares conseguem sustentar.

## Analogia: a sala de controle de uma usina

Pense numa usina hidrelétrica de porte médio. Operar não é apenas ligar a turbina. Operar é manter, em qualquer instante, visibilidade completa do que está acontecendo, registro inalterável do que aconteceu, capacidade de reagir ao que está acontecendo agora, e capacidade de reverter a uma configuração conhecidamente segura quando o operador suspeitar que algo está fora do padrão.

A sala de controle tem painéis de instrumentação que mostram vazão, pressão, temperatura por turbina, voltagem por gerador, frequência da rede. Tem botões físicos para reduzir produção, para desligar, para desviar fluxo. Tem registros automáticos do que cada operador tocou, com timestamp e identificação. Tem procedimento documentado para cada classe de evento, com gatilho explícito. Tem revezamento de turno com handover formal. Tem auditoria periódica do próprio painel, porque painel que não é auditado vira mentira tranquilizadora.

LLMOps é a sala de controle da operação de IA. Cada pilar dos sete cumpre função análoga a um sistema na usina. Tracing é a instrumentação. Versionamento é o registro inalterável. Deploy progressivo é a abertura controlada de fluxo. Rollback é o desvio de emergência. Custo é o medidor de combustível. Segurança operacional é o protocolo de incidente. Governança operacional é o handover formal e a auditoria. Quando os sete funcionam, a operação atravessa incidentes com cabeça fria e tempo de recuperação que cabe em horas, não semanas. Quando faltam, cada evento vira investigação arqueológica.

## Os sete pilares

### Pilar 1: tracing e observabilidade

Cada chamada de IA é registrada com input completo, output completo, latência total e por passo, tokens in/out por passo, custo computado, tools chamadas com argumentos e retornos, modelo usado, versão de prompt, versão de tool, ID de sessão e de usuário, status de sucesso, erro ou timeout. Sem este pilar, não há LLMOps possível.

O modelo mental canônico é span, trace e session. Cada chamada individual ao modelo é um span. Uma sequência de spans relacionados, por exemplo um turno de conversa com múltiplas chamadas ao modelo e a tools, é um trace. Uma sequência de traces no mesmo contexto de uso, por exemplo uma sessão de chat com vários turnos, é uma session. A nomenclatura vem de OpenTelemetry, e padroniza a discussão entre times.

O que logar: input completo sanitizado de PII conforme política de LGPD, output completo, latência por passo, tokens de input e output, custo computado em tempo real, tool chamada com argumentos e retornos, modelo usado, versão de prompt, versão de tool, ID de sessão, ID de usuário anonimizado conforme política, status. Acrescentar metadados de contexto da operação, como feature, ambiente, região.

O que não logar: PII desnecessária ao debug, segredos, conteúdo sob LGPD sem base legal explícita, dados de saúde, orientação sexual, dados financeiros íntimos. Times maduros têm classificador automático de PII no pipeline de logging.

A especificação OpenTelemetry GenAI semantic conventions, em evolução, padroniza nomes de atributos para spans de modelo, tool e agente. Adotar o padrão, mesmo que parcial, reduz vendor lock-in de observability. Vale o esforço quando o stack está em mais de um vendor.

### Pilar 2: versionamento do que muda

O que se versiona em LLMOps: prompt do sistema, prompt da feature, definição de tool com schema, descrição e exemplos, dataset de eval, política de classificação. Cada um vira artefato com versão semântica, dono, changelog explícito.

Tratar prompt como código significa pull request, revisão obrigatória por pelo menos um par, eval em CI antes do merge, scorecard comparativo gerado automaticamente, merge gatekeeping. Engenheiros experientes em desenvolvimento moderno reconhecem o padrão imediatamente. A diferença é que o "compilador" é o sistema de eval, e o "lint" é o LLM-as-judge contra rubrica.

Tool registry: cada tool em produção tem entrada em registry com schema, descrição, exemplos, dono operacional, versão, eval específico. Tool que muda sem entrar no registry é o caminho mais rápido para regressão silenciosa em agentes.

Model registry interno: tabela que mapeia qual modelo, qual versão, qual fallback por feature. Mudança aqui é decisão de arquitetura, não de engenheiro, e deve passar por governança alinhada ao Princípio 8.

System prompt como artefato versionado, não string no código. Pode estar em banco, em config, em sistema dedicado. O que importa é não ser concatenação inline no código da feature.

Changelog obrigatório: cada release que mexe em prompt, tool ou modelo registra o que mudou, motivo, delta de scorecard, subgrupo mais afetado, decisão de revisor. Sem changelog, troubleshooting em três meses vira arqueologia.

### Pilar 3: deploy progressivo

Shadow mode: versão nova roda em paralelo, sem servir resposta ao usuário, com input real de produção. As saídas da versão atual e da candidata são comparadas offline. Útil para validar mudança de modelo ou de prompt em escala, sem risco para o usuário final.

Canário por percentual de tráfego: versão nova recebe 1%, depois 10%, 50%, 100% conforme métricas sustentam promoção. Cada gate tem critério explícito: scorecard verde por horas determinadas, latência dentro da banda, custo dentro do envelope, sem incidente SEV-2.

Canário por segmento: estratégia complementar, com liberação primeiro para clientes free, depois beta, depois SMB, e por último Enterprise crítico. Nunca o inverso. A regra é "quem reclamaria mais alto recebe por último".

Feature flag: liberar por persona, conta, região, ambiente. Permite isolar testes A/B e desligar versão problemática em segundos sem mexer em código.

Critérios de promoção entre gates documentados, automáticos quando possível. Tipicamente, métrica primária dentro de banda esperada, latência p95 dentro da banda, custo dentro do envelope, taxa de erro estável, sem incidente em horas determinadas.

### Pilar 4: rollback que funciona em produção

Botão único por feature: reverter prompt, tool ou versão de modelo deve estar a um clique de distância. Quem precisa de pull request, build e deploy para rollback descobre, no incidente, que rollback assim demora mais que o incidente.

Estado anterior em hot standby: a versão anterior sempre está pronta para servir. Não está só "no histórico do Git". Está provisionada, com cache aquecido, esperando ser ativada.

Teste mensal em staging: rollback que nunca é testado, na hora do incidente, não funciona. Times maduros simulam rollback uma vez por mês em staging, com cronômetro, com runbook seguido. Documentam quanto tempo levou e o que falhou.

MTTR como métrica institucional: o tempo médio entre detecção e retorno ao estado bom vira métrica de OKR técnico. Times maduros ficam abaixo de 15 minutos para SEV-1 e abaixo de 1 hora para SEV-2.

### Pilar 5: custos, quotas e circuit breakers

Atribuição de custo por feature, cliente, usuário. Sem atribuição, não há como decidir o que cortar quando o orçamento aperta. Custo agregado mensal é informação inútil para decisão; custo por feature mostra onde está o predador.

Alertas de orçamento: limites diários, semanais e mensais por feature e por cliente. Acionados antes do CFO ver.

Circuit breaker por usuário e por sessão: limite duro de chamadas ao modelo premium por janela de tempo. Protege contra runaway loop em agente e contra abuso de usuário malicioso. Bug que causa loop fica contido em dezena de centavos, não em dezenas de milhares de reais.

Quota por tier: não permitir que feature crítica seja sufocada por feature secundária em surto. Reserva de capacidade no modelo premium.

O custo composto em três tempos serve como referência. A ferramenta de redução de custo é esse método. Sem ele, o pilar 5 fica em "alarmar quando estoura".

### Pilar 6: segurança operacional

Prompt injection: defesa em camadas, sandbox de tool, escape de input do usuário, allowlist de tools por contexto, classificação prévia de input suspeito, auditoria de saída antes de retornar ao próximo modelo na cadeia. Em agentes que consomem documentos externos, prompt injection é vetor primário; assumir que existe é mais seguro que esperar que não.

Tool poisoning: validar a saída de tool antes de devolver ao modelo. Tool que retorna conteúdo malicioso pode contaminar o agente. Sandbox por tipo de retorno mais validação contra schema.

Data exfiltration: política sobre o que o modelo pode mandar para fora via tool. Whitelist de domínios para chamadas externas. Auditoria periódica de logs de tools externas.

Kill switch testado: capacidade de desligar uma tool, um agente, um modelo, ou uma feature inteira em segundos. Por escopo. Testado em simulado mensal. Dono nominal por escopo.

### Pilar 7: governança operacional

Severidades adaptadas a IA: SEV-1 cobre impacto crítico em cliente, exposição de PII, perda de dados, erro grave em decisão automatizada. SEV-2 cobre degradação significativa, custos disparados, regressão de qualidade detectada. SEV-3 é problema isolado de baixo impacto. SEV-4 é irritação sem perda.

Comunicação durante incidente: canal dedicado, atualizações em cadência fixa, com SEV-1 a cada 15 minutos, comunicação externa pré-escrita por classe de incidente, comunicação interna estruturada por status, com detectado, contido, investigando, mitigado, resolvido.

Postmortem sem culpa: foco no processo, não na pessoa. Discussão estruturada sobre o que aconteceu, quando, como foi detectado, quanto tempo levou para conter, o que poderia ter sido feito diferente, quais mudanças vão evitar repetição. Documento publicado, lido por todos.

Trilha de auditoria: retenção mínima de 90 dias para casos não-críticos; 5 anos ou mais para decisão regulada, alinhada a LGPD com decisão automatizada, ANPD, AI Act, ISO 42001.

## Diagramas

![Stack canônico de LLMOps](file:///sessions/relaxed-cool-bell/mnt/Ebook IA/Livro-1-Os-Invariantes/02-capitulos/imagens/L1-C40-img-01-stack-llmops.svg)

*Os sete pilares operacionais alinhados por dono e por fluxo de telemetria. A pirâmide funcional vai do que rastrear na base ao que governar no topo.*

![Tracing de agente](file:///sessions/relaxed-cool-bell/mnt/Ebook IA/Livro-1-Os-Invariantes/02-capitulos/imagens/L1-C40-img-02-tracing-agente.svg)

*Modelo mental canônico. Cada chamada individual é um span; conjunto relacionado é um trace; conjunto temporal é uma session.*

![Timeline de incidente](file:///sessions/relaxed-cool-bell/mnt/Ebook IA/Livro-1-Os-Invariantes/02-capitulos/imagens/L1-C40-img-03-timeline-incidente.svg)

*Do T0, detecção, ao D+5, postmortem publicado. Cada nó com pré-requisito explícito do pilar de LLMOps que o sustenta.*

## Recortes por persona

A pergunta "o que cada papel precisa saber de LLMOps?" tem respostas diferentes. A tabela abaixo separa por persona, com métrica-chave e pergunta certa a fazer ao fornecedor.

| Dimensão | CTO | Arquiteto | Desenvolvedor |
|----------|-----|-----------|---------------|
| O que precisa saber | Sete pilares no nível de decisão e custo; trade-offs build versus buy; orçamento operacional; RACI por feature | Arquitetura do stack; integração com observability existente; padrão de versionamento; modelo de span e trace; pontos de extensão | Como instrumentar; como adicionar tracing custom; como criar PR de prompt; como rodar canário; como ler scorecard |
| O que não precisa saber | Detalhe de implementação de span; biblioteca específica | Métricas executivas como custo agregado por LOB | Política de incidente nível executivo; trilha regulatória de retenção |
| Métrica-chave | Custo total de IA sobre receita; SLA de IA; SEV-1 e SEV-2 por trimestre | Cobertura de tracing em percentual; MTTR de rollback; cobertura de versionamento; cobertura de testes de incidente | Cobertura de tracing nas próprias features; tempo médio para identificar bug de IA |
| Pergunta certa ao fornecedor | "Como atribui custo de IA por cliente final?" | "Vocês têm OpenTelemetry GenAI? Que versão?" | "Como o SDK me dá hook para tracing customizado e propagation de context?" |

## Exemplo memorável: a fintech e o loop com cartão de crédito

Cenário ilustrativo composto a partir de padrões observados em marketplaces e fintechs brasileiras durante a adoção de agentes integrados a múltiplos APIs por MCP. Números são realistas mas não identificam empresa específica.

Pólice.io, marketplace brasileiro de seguros, com cerca de oitenta colaboradores. Implementou um agente de cotação assistida via chat, integrado a sete seguradoras por MCP, com objetivo de reduzir o tempo de cotação de quinze minutos com humano para menos de dois minutos com agente e humano revisando. Nas três primeiras semanas em produção, sucesso aparente. Conversões subiram dezessete por cento. NPS estável. O CFO comentou em reunião que a fatura de IA estava crescendo "como esperado".

Na quarta semana, a fatura ultrapassou R$ 142 mil. No mês zero do projeto, antes do agente, a fatura era R$ 18 mil. A diferença foi atribuída pela equipe técnica a "uso maior do que esperado". O CFO aceitou a explicação, embora inquieto. Na quinta semana, a fatura cruzou R$ 200 mil projetados. O CTO da Pólice.io começou a investigar. Não tinha tracing instrumentado. Não tinha atribuição por feature. Não tinha circuit breaker. Tinha logs do modelo, com input e output básico, e a fatura agregada.

Levou onze dias para a equipe descobrir o que estava acontecendo. Um bug introduzido em PR aparentemente inofensivo na terceira semana, uma refatoração de um campo do formulário, sem nada que parecesse relevante para o agente, fazia com que, sempre que o usuário trocasse de estado civil no meio do fluxo, o agente reconsultasse as sete seguradoras integradas por MCP. Cada reconfiguração disparava chamadas ao modelo premium para reavaliar contexto. Em média, trinta e uma chamadas redundantes ao modelo premium por cotação efetiva. Multiplicado pelo volume crescente, a fatura escalou exponencialmente.

Quando finalmente instrumentaram tracing por span, com duas semanas no telhado em urgência, o problema apareceu em uma hora. Correção em duas. Custo do incidente: aproximadamente R$ 96 mil em chamadas desperdiçadas, mais a credibilidade abalada da diretoria, mais duas semanas de engenharia desviadas para "salvar o orçamento".

A Pólice.io reescreveu o stack operacional em quatro semanas. Implementou tracing no estilo OpenTelemetry desde a primeira chamada de cada turno. Adicionou versionamento de tool com eval específico. Criou canário por percentual antes de qualquer promoção em produção. Estabeleceu circuit breaker por usuário com limite de cinco chamadas ao modelo premium por sessão. Alertas de custo por feature, por cliente, por usuário. Política de incidente SEV-1 com SLA de 15 minutos para detecção.

Em três meses, a fatura caiu para R$ 47 mil mensais, com volume maior de cotações servidas que no período do incidente. A explicação não foi "ficamos mais rápidos no roteamento" ou "mudamos de modelo". Foi que a observabilidade revelou onde o custo estava sendo desperdiçado, e o time arrumou. O Capítulo 18 mostrou a fórmula; este capítulo mostra que sem o pilar 1 não dá para aplicar a fórmula.

A lição é dura. Autonomia sem observabilidade é loop com cartão de crédito. O que destrói orçamento de IA não é o preço do token, é a falta de instrumentação que faz cada incidente custar duas semanas para ser visto.

Para executivos: se a fatura mensal de IA da sua organização ultrapassou R$ 30 mil e o time técnico não consegue responder "qual a feature mais cara?" em até 5 minutos, você está em risco. Atribuição de custo por feature é o primeiro item de auditoria de LLMOps em qualquer operação madura. Se faltar, peça plano de remediação em 30 dias.

> **Rigor estatístico do caso.** Medições da Pólice.io realizadas em janela de oito semanas pós-incidente, com aproximadamente 12.000 chamadas de agente reconstituídas via tracing retrospectivo, atribuição de custo por feature validada contra fechamento financeiro mensal, intervalo de confiança 95% sobre a economia projetada, validação cruzada com auditoria interna de custo nos primeiros cento e vinte dias do dashboard implantado. Caso composto a partir de padrões observados em mais de uma scaleup brasileira do setor de seguros e fintech — atribuição nominal sugerida para edições futuras, conforme pacto editorial descrito no paratexto "Sobre os casos desta obra".

## Quando usar e quando evitar

Implantar stack completo de LLMOps quando há IA em produção tocando cliente, mais de um agente em produção, custo recorrente acima de R$ 5 mil mensais em chamadas a LLMs, SLA explícito ou implícito de qualidade, ou requisito regulatório, como LGPD com decisão automatizada e regulação setorial.

Subset mínimo viável, sem overhead completo, quando há piloto único interno, fora de produção, com um usuário, demo única para conselho ou prospect, teste de ideia descartável.

Em todo caso intermediário, comece pelos pilares 1 (tracing), 4 (rollback) e 7 (governança). Os outros entram conforme escalar.

## Vantagens e limitações

| Vantagem | Limitação |
|----------|-----------|
| Custo de IA cai 20-50% só com observabilidade bem feita | Custo inicial de instrumentação e padronização — tipicamente 4-12 semanas para o stack inicial |
| MTTR de incidentes cai dramaticamente — de dias para horas | Risco de over-engineering em produto early-stage |
| Audit trail vira ativo para compliance e disputa judicial | Requer cultura de versionamento que muitos times de IA não têm; demanda mudança organizacional |
| Permite migração de modelo sem terror | Vendor lock-in se observability vem de um único fornecedor proprietário; OpenTelemetry mitiga |
| Reduz dependência de "engenheiro herói" que conhece o sistema | Adiciona camada de processo que pode atrasar prototipagem |
| Habilita governança técnica com base auditável | Custo de armazenamento e compliance de logs cresce com volume |

Este capítulo conversa especialmente com os capítulos sobre tokens, memória persistente, agentes, MCP, AI Engineering, economia de tokens, segurança, evals, alignment e governança corporativa.

## Resumo

| Pilar | Pergunta executiva | Indicador-chave |
|-------|--------------------|-----------------|
| 1 Tracing e observabilidade | "Consigo reconstruir qualquer decisão da IA?" | % de spans com tracing completo |
| 2 Versionamento | "Sei o que estava em produção em qualquer data?" | % de prompts e tools versionados |
| 3 Deploy progressivo | "Posso testar com 1% antes de 100%?" | % de releases com canário |
| 4 Rollback | "Quanto tempo do 'algo errado' ao estado anterior?" | MTTR de SEV-1 |
| 5 Custos e quotas | "Vejo agente loopando antes do CFO ver?" | Custo por feature, alerta antes de incidente |
| 6 Segurança operacional | "Desligo uma tool perigosa em 30s?" | Tempo de kill switch testado |
| 7 Governança operacional | "Quem responde quando der ruim?" | Auditoria de SEV-1 com postmortem público |

## Checklist do capítulo

- [ ] Distinguir LLMOps de MLOps clássico em uma frase
- [ ] Listar os sete pilares na ordem de impacto e a pergunta executiva de cada um
- [ ] Descrever o modelo mental span, trace e session
- [ ] Defender adoção de OpenTelemetry GenAI ante vendor proprietário
- [ ] Identificar, no seu produto, o pilar mais frágil hoje
- [ ] Calcular o MTTR atual da sua operação e propor meta de 30 dias
- [ ] Apresentar os recortes por persona em reunião de tech leadership
- [ ] Reconhecer, em três incidentes recentes, qual pilar teria mitigado cada um

## Perguntas de revisão

1. Por que LLMOps não é "MLOps com nome novo", e o que muda na prática?
2. Em qual dos sete pilares está o ROI mais imediato de implementar primeiro, e por quê?
3. Por que rollback "no Git" não é rollback de produção?
4. Como o pilar 1 sustenta a fórmula do custo composto?
5. Que diferença existe entre canário por percentual e canário por segmento, e quando usar cada um?
6. Por que kill switch teórico é pior que não ter kill switch?
7. Como o pilar 7 conecta com o Princípio 8 (Responsabilidade Indelegável)?
8. Em que situação OpenTelemetry GenAI é over-engineering, e em que situação é proteção contra lock-in?
9. Como o pilar 5 prevê os erros típicos do método de custo composto em três tempos?

## Exercícios práticos

Exercício 1, diagnóstico dos sete pilares. Mapeie cada um dos sete pilares no seu stack atual e atribua maturidade em escala de 0 a 4, com 0 inexistente, 1 declarado, 2 implementado, 3 auditado, 4 melhoria contínua. Identifique os dois pilares mais frágeis e proponha plano de 60 dias.

Exercício 2, trace ideal de uma sessão real. Para uma sessão real do seu produto, desenhe o trace ideal span por span. Inclua chamadas ao modelo principal, chamadas a tools, chamadas a sub-agentes, latência, tokens, custo. Compare com o que seu sistema loga hoje. O que falta?

Exercício 3, playbook de rollback em uma página. Escreva o playbook de rollback do seu prompt principal. Quem detecta, quem aciona, quanto tempo de cada passo, onde está o estado anterior, como confirmar que rollback funcionou. Limite: uma página.

Exercício 4, cálculo do custo real do último mês. Use a fórmula de custo composto, tokens vezes chamadas vezes redundância vezes tier, para reconstruir o custo do mês anterior. Identifique o componente que mais escalou. Proponha plano de redução de 25% em 60 dias.

## Projeto do capítulo

Construa o Caderno de LLMOps do seu produto ou operação, em 8 a 12 páginas, contendo descrição dos sete pilares aplicados ao próprio produto com maturidade atual e meta de 90 dias, arquitetura de tracing com modelo span, trace e session aplicado, política de versionamento de prompt e tool, runbook de rollback testado mensalmente, runbook de incidente SEV-1 com detecção, contenção, comunicação e postmortem, atribuição de custo por feature, cliente e usuário, dono nominal de cada pilar e plano de revisão trimestral do caderno.

Critério de qualidade: outro engenheiro, sem contexto, consegue ler o caderno e responder, sem perguntar mais, qualquer das sete perguntas executivas sobre o seu sistema.

## Referências principais

OpenTelemetry e padrões: OpenTelemetry GenAI semantic conventions (em evolução); Parker, Spoonhower e Mace, Distributed Tracing in Practice (2020).

Frameworks e stacks LLMOps: a16z, The Emerging Architectures for LLM Applications (Bornstein e Radovanovic, 2023); Karpathy, Software 3.0 (palestra, junho de 2025).

SRE e fundamento de operação: Google, Site Reliability Engineering Book (Beyer et al., 2016) e The Site Reliability Workbook (Beyer et al., 2018).

Observability de LLMs: documentação LangSmith, Langfuse, Helicone, Arize Phoenix, Datadog APM com observabilidade LLM.

Segurança de LLMs em produção: Greshake et al., Not what you've signed up for (2023); Liu et al., Prompt Injection attack against LLM-integrated Applications (2023); Anthropic, Responsible Scaling Policy.

Alignment e operação: Anthropic, Constitutional AI (Bai et al., 2022).

## Autoavaliação

| # | Critério | Você consegue? |
|---|----------|----------------|
| 1 | Clareza: explicar a um sócio o que é tracing em IA usando a analogia da sala de controle de usina em 2 minutos | ☐ |
| 2 | Profundidade: defender em reunião de arquitetura por que versionamento de prompt é tão crítico quanto versionamento de código | ☐ |
| 3 | Aplicação: apontar, no seu produto, qual dos sete pilares é o mais frágil hoje e o que faria nos próximos 14 dias | ☐ |
| 4 | Conexão: articular como LLMOps fecha o ciclo aberto pelos evals e fundamenta a governança, passando pela fórmula do custo composto | ☐ |
| 5 | Curiosidade: vontade de entrar no próximo capítulo para entender como o próprio modelo é moldado antes de chegar à sua operação | ☐ |

</div>
</section>
