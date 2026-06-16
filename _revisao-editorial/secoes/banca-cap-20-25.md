# BANCA EDITORIAL ADVERSARIAL — CAPÍTULOS 20 A 25
# INTELIGÊNCIA AUMENTADA — "Modelos passam. Método fica."
# Data: 2026-06-16

---

# C20 — L1-C20-futuro.md

## RESUMO EXECUTIVO
Nota: 7/10
Veredito: B

## O QUE FUNCIONA
- A oposição previsão × cenário é articulada com clareza operacional real, não apenas teórica. O CTO que ler entende o que muda no dia seguinte.
- A analogia do piloto com três planos de aproximação é memorável, precisa e proporcional ao conceito. Funciona para público executivo sem background técnico.
- A tabela-resumo do 20.9 sintetiza os três cenários com os quatro vetores e a implicação executiva em formato consultável. É o artefato mais útil do capítulo.
- A seção 20.8 ("Como o CTO Usa Cenários Na Prática") entrega três usos concretos com grau de detalhe que permite ação imediata. Raro em livros de estratégia.
- A posição sobre AGI na seção 20.7 é a mais honesta do mercado: nem aposta contra, nem aposta a favor — trata como pergunta aberta com argumento em ambas as direções. Isso é raro e valioso.
- A decisão de não detalhar cenários de doze meses (remetendo ao processo de planejamento anual) é metodologicamente madura e protege durabilidade.

## O QUE NÃO FUNCIONA
- A última frase do parágrafo sobre AGI (seção 20.7) é ilegível: cláusula sobre cláusula, ressalvas empilhadas, pensamento protegido em excesso que prejudica o argumento.
- O capítulo menciona reiteradamente frameworks internos (F1, F3, F7) sem oferecer ao leitor que está lendo o capítulo de forma isolada qualquer orientação de suficiência. Exige integração que pode não existir no fluxo de leitura.
- Os vetores de mudança (20.3.1) são listados com descrição boa, mas sem critério operacional para medir cada vetor — o executivo sai do capítulo sem saber como, concretamente, "medir capacidade do modelo" em seu contexto.
- O Cenário Otimista declara que agentes verticais cobrem "sessenta a setenta por cento da carga" sem citar qualquer fonte, estudo ou base observacional. É exatamente o tipo de número que o próprio capítulo critica em previsões pontuais.
- O capítulo cita "a literatura corporativa sugere ganhos entre trinta e oitenta por cento em funções repetíveis" (seção 20.5) sem qualquer referência. Intervalo de cinquenta pontos percentuais sem fonte é ruído disfarçado de dado.
- O checklist (20.10) tem nove itens, vários dependentes de outros capítulos da obra. Sem os outros capítulos, o checklist é incompleto como instrumento standalone.

## ACHADOS

### ACHADO 01
Categoria: P0
Problema: Número sem fonte no cenário otimista — "sessenta a setenta por cento da carga repetível" coberta por agentes.
Por que é um problema: O próprio capítulo argumenta que números precisos enganam mais que humildade honesta. Usar número não sustentado aqui é contradição metodológica direta com a tese do capítulo.
Impacto no leitor: CTO cita o número em Conselho; quando questionado sobre a fonte, a credibilidade do capítulo e do autor desce junto.
Correção exata: Ou citar fonte (Epoch AI, McKinsey 2024, estudo setorial verificável) ou reformular para "cobrindo fatia material da carga repetível em domínios específicos" com nota de que estimativas variam amplamente por setor e por definição de 'repetível'.
Texto sugerido: "agentes especializados por função operacional cobrindo fatia material da carga repetível em cada domínio (estimativas setoriais variam entre 40% e 80%, com diferenças significativas por tipo de tarefa e por grau de padronização — ver Apêndice J para fontes datadas)"
ROI: ALTO

### ACHADO 02
Categoria: P0
Problema: "A literatura corporativa sugere ganhos entre trinta e oitenta por cento" — fonte ausente para afirmação quantitativa em seção que deve ser o plano-base.
Por que é um problema: Intervalo de 50 pontos percentuais sem referência é estatisticamente inútil para planejamento. Qualquer número cabe nesse range.
Impacto no leitor: Executivo usa o range para justificar orçamento; quando auditor ou CFO pede a fonte, não há o que apresentar.
Correção exata: Substituir pela referência específica (McKinsey Global Institute 2023, MIT Work of the Future 2024, ou similar) ou reconhecer honestamente que a variância é tão alta que não sustenta planejamento sem análise setorial própria.
Texto sugerido: "A evidência disponível, documentada em estudos como [fonte específica datada], sugere ganhos entre X% e Y% em funções [tipologia específica], com variação alta por setor e por grau de implementação — ver Apêndice J."
ROI: ALTO

### ACHADO 03
Categoria: P0
Problema: Último parágrafo da seção 20.7 é ilegível por acúmulo de ressalvas. A frase que começa em "A evidência disponível em junho de 2026, ainda que limitada..." continua por mais de duzentas palavras sem parar.
Por que é um problema: Qualquer ponto que exija frase de duzentas palavras para ser sustentado não está sustentado — está sendo protegido do escrutínio por complexidade. Viola o padrão de clareza da obra.
Impacto no leitor: Joana para de ler. CTO sente que o autor está se esquivando.
Correção exata: Quebrar em três afirmações curtas e atribuir probabilidade subjetiva qualitativa a cada uma, no mesmo formato que o capítulo usa para os cenários.
Texto sugerido: "A posição executiva responsável combina três afirmações modestas. Primeira: o investimento em governança, arquitetura modular e disciplina paga em qualquer cenário plausível a cinco anos. Segunda: a questão AGI permanece legitimamente em aberto, com argumentos sérios em ambas as direções. Terceira: a probabilidade que você atribui à AGI iminente deve ser tratada como hipótese de trabalho revisável anualmente, não como convicção fechada."
ROI: ALTO

### ACHADO 04
Categoria: P1
Problema: Os quatro vetores (20.3.1) não têm critério operacional de medição. O executivo sabe que precisa medir "capacidade do modelo" mas não sabe como fazer isso em seu contexto específico.
Por que é um problema: Sem critério de medição, o rito trimestral do AI Council (recomendado em 20.8) fica sem instrumentação. A revisão de cenário vira conversa informal, exatamente o que o capítulo adverte contra.
Impacto no leitor: Leitor sai do capítulo motivado a implementar o rito, mas sem saber o que medir em cada reunião trimestral.
Correção exata: Adicionar, para cada vetor, dois ou três indicadores concretos que um time médio consegue medir sem pesquisa primária custosa. Ex.: para "capacidade do modelo" — benchmark interno no golden set próprio, taxa de alucinação em tarefa de domínio, % de tarefas que passaram do prompt para one-shot.
Texto sugerido: n/a (expandir cada vetor com painel de 2-3 indicadores observáveis)
ROI: ALTO

### ACHADO 05
Categoria: P1
Problema: O capítulo menciona PL 2338 como se já estivesse sancionado em ambos os cenários (otimista e mediano), mas o PL estava em tramitação no Senado em 2026. A menção como fato nos cenários introduz imprecisão factual em texto que se propõe a modelar incerteza.
Por que é um problema: Envelhecerá mal dependendo do que acontecer com o PL. O cenário pessimista (20.6) é o único que usa formulação mais cuidadosa sobre o ambiente regulatório brasileiro.
Impacto no leitor: Se o PL for sancionado com texto diferente, ou não for sancionado, o texto fica incorreto em dois dos três cenários.
Correção exata: Reformular nos cenários otimista e mediano para "marco regulatório brasileiro de IA amadurece" ou condicionar explicitamente: "se PL 2338 for sancionado como esperado...".
Texto sugerido: n/a (ajuste de formulação por cenário)
ROI: MÉDIO

### ACHADO 06
Categoria: P1
Problema: O horizonte de doze meses é delegado ao "processo de planejamento anual" mas sem nenhuma orientação sobre como aplicar o método de cenários nesse horizonte. O leitor que mais precisa de ajuda prática fica sem ela.
Por que é um problema: A maioria dos CTOs brasileiros opera em ciclo de doze meses como restrição dura de orçamento. Deixar esse horizonte vago reduz o valor prático imediato do capítulo.
Impacto no leitor: O executivo que quer aplicar o método amanhã, na próxima reunião de orçamento, não tem o ponto de partida.
Correção exata: Adicionar subtópico de meia página (20.3.4 ou sidebar) com orientação mínima para o ciclo de doze meses: quais dos quatro vetores são mais observáveis nesse horizonte, qual é a cadência de revisão recomendada, qual o entregável.
Texto sugerido: n/a (conteúdo novo)
ROI: MÉDIO

### ACHADO 07
Categoria: P2
Problema: A referência à Shell nos anos 1970 (seção 20.1) é o único exemplo histórico do capítulo. O texto menciona que "a Shell tornou o método clássico" mas não cita o paper de Wack (que aparece nas referências em 20.14). A conexão é feita nas referências mas não no corpo.
Por que é um problema: Para o leitor que não vai às referências, a credibilidade da metodologia de cenários fica sem ancora histórica verificável.
Impacto no leitor: Baixo — mas leitores que checam referências ficam com a sensação de que o argumento histórico é ornamento.
Correção exata: Inserir referência parentética a Wack (1985) na menção à Shell no corpo do texto.
Texto sugerido: "A Shell tornou o método clássico ainda nos anos 1970, durante a crise do petróleo (Wack, 1985), e o que ficou na literatura corporativa..."
ROI: BAIXO

## TESTE DA JOANA
Entenderia: SIM (parcial)
O que ela entenderia: A diferença entre previsão e cenário, a analogia do piloto, os três cenários com implicações executivas, o rito trimestral do AI Council.
O que ela NÃO entenderia: Os quatro vetores sem critério de medição (o que, exatamente, ela deveria monitorar na próxima reunião?), as referências a F1, F3, F7 sem explicação local suficiente.
Como corrigir: Adicionar, após os quatro vetores, um painel de "indicadores que qualquer time consegue monitorar" sem depender dos frameworks em outros capítulos.

## TESTE DE DURABILIDADE
Classificação: MÉDIA
2 anos: Bom — o método de cenários é metodologicamente duradouro; os cenários específicos a 36 meses envelhecem conforme a realidade se materializa ou não.
5 anos: Médio — os cenários a 36 meses (escritos em 2026) estarão desatualizados por definição; o método para construir novos cenários permanece.
10 anos: O método dura; os exemplos (PL 2338, custo de inferência a 10x, agentes verticais a 60-70%) serão história datada.
Justificativa: O risco central é a dupla natureza do capítulo — método duradouro + exemplos datados. Os números nos cenários (60-70%, 30-80%, 10x, 3-5x) envelhecem rápido. Recomendado mover todos os números de exemplificação dos cenários para o Apêndice J com data explícita, mantendo o corpo do capítulo em formulação qualitativa.

## TESTE DE DIFERENCIAÇÃO
Classificação: DIFERENCIADO
Justificativa: A combinação de método de cenários aplicado especificamente a IA corporativa, com vetores nomeados, horizontes definidos e probabilidade subjetiva qualitativa explicada contra o instinto de probabilidade numérica do executivo financeiro — isso não está nos livros de referência da régua. O posicionamento sobre AGI (aberto, calibrado, sem tomar partido) é genuinamente raro no mercado.

## TESTE DE MEMORIZAÇÃO
Ideia principal clara? SIM
Qual é a ideia principal (em 1 frase): Em campo de alta turbulência, o CTO competente não prevê o futuro — constrói três planos paralelos e monitora os sinais que o movem entre eles.
Justificativa: A frase-âncora da seção 20.8 ("operamos hoje no cenário mediano, e os sinais que nos moveriam...") é a mais citável do capítulo e merece destaque visual.

## TESTE DE TRANSFORMAÇÃO
Ao terminar, o leitor consegue fazer o que antes não conseguia:
- Estruturar apresentação de IA para Conselho com três cenários em vez de previsão única
- Definir os quatro vetores de mudança e atribuir leitura qualitativa a cada um
- Instituir rito trimestral do AI Council com agenda estruturada e critério de mudança de cenário
- Resistir à pressão do Conselho por probabilidade numérica com argumento técnico sustentável

## NOTA FINAL (0-10 cada eixo)
Estrutura: 8 | Pedagogia: 7 | Clareza: 7 | Autoridade: 7 | Durabilidade: 6 | Diferenciação: 8 | Memorização: 8 | Transformação: 7
**Nota Geral: 7.3**

## DECISÃO EDITORIAL
MANTER COM AJUSTES — Corrigir P0s (remover números sem fonte ou citá-los), quebrar o parágrafo ilegível sobre AGI, adicionar critério de medição para os quatro vetores. Mover números de exemplificação dos cenários para Apêndice J.

---

# C21 — L1-C21-evals.md

## RESUMO EXECUTIVO
Nota: 8/10
Veredito: A

## O QUE FUNCIONA
- A distinção entre eval offline e eval online, com ciclo de retroalimentação, é o melhor mapa operacional do tópico disponível em português. Clara, completa, acionável.
- A Pirâmide de Avaliação com cobertura por camada (100%, 30-80%, 5-15%) e a camada adversarial transversal é um framework visual memorável e operacionalmente correto.
- A tabela de seis tipos de eval com "quando funciona" e "armadilha clássica" é a melhor parte do capítulo — concentra anos de aprendizado operacional em formato consultável.
- A analogia do laboratório clínico é precisa, proporcional e sustentada ao longo do capítulo. Não é enfeite — é ancoragem conceitual que dura.
- O caso Atlas Strategy cumpre a função pedagógica com honestidade metodológica rara: descreve o caso composto, declara o rigor estatístico, nomeia o que o rigor implica.
- A tabela de sete erros típicos com antídoto é citável, direta, sem redundância. É propriedade intelectual do capítulo.
- O quadrante de LLM-as-judge (rubrica específica × risco) é instrumento imediato: o leitor sai com critério de quando confiar e quando não confiar.

## O QUE NÃO FUNCIONA
- O capítulo não numera seções — contraste com o capítulo 23 que numera sistematicamente. A ausência torna difícil referenciar seções específicas em discussão técnica ("a parte sobre LLM-as-judge" é diferente de "seção 21.4").
- "Rigor estatístico do caso" ao final do caso é boa prática, mas a calibração de 0,7 para correlação alvo de LLM-as-judge com humano (seção sobre LLM-as-judge) não tem referência — é número operacional importante que precisa de ancora.
- A relação entre Princípio 7 (Termômetro) e Princípio 8 (Responsabilidade Indelegável) é mencionada nas perguntas de revisão mas não desenvolvida no corpo. Leitores que não leram os princípios não entendem a referência.
- O checklist tem onze itens, alguns compostos (ex.: "Defender a regra de juiz diferente do gerador para LLM-as-judge em mesa técnica"). Itens que contêm "defender" são critérios de proficiência, não de ação — mistura de categorias.
- O capítulo promete "seis tipos canônicos de eval" mas a apresentação no corpo usa texto corrido antes da tabela, gerando redundância desnecessária.

## ACHADOS

### ACHADO 01
Categoria: P1
Problema: Correlação alvo de 0,7 para calibração de LLM-as-judge contra humano sênior não tem referência. É número operacional crítico que determina se um time aceita ou rejeita seu juiz LLM.
Por que é um problema: CTOs usarão este número como critério de aceitação. Se o número estiver errado ou se houver variação significativa por domínio (saúde vs varejo), a decisão baseada nele pode ser inadequada.
Impacto no leitor: Time calibra juiz, atinge 0,68 e conclui que "não passou" — sem saber se 0,7 é limiar universalmente defendível ou convenção operacional do autor.
Correção exata: Citar a referência que suporta 0,7 (Zheng et al. 2023 ou G-Eval Liu et al. 2023, já nas referências), ou explicitar que é limiar operacional pragmático, com nota de que domínios críticos (saúde, jurídico) podem exigir 0,8 ou mais.
Texto sugerido: "calibração contra avaliadores humanos seniores em pelo menos 30 a 50 casos, com correlação alvo acima de 0,7 (Zheng et al., 2023; para domínios de alto risco, considerar 0,8+)"
ROI: ALTO

### ACHADO 02
Categoria: P1
Problema: O capítulo não tem numeração de seções. Isso é inconsistência estrutural com o restante da obra (caps 23 e 24 têm numeração explícita) e prejudica referenciação cruzada.
Por que é um problema: "A seção sobre LLM-as-judge" é diferente de "seção 21.5.3". Em livro técnico com doze perguntas de revisão e onze itens de checklist, a falta de numeração torna discussão entre pares imprecisa.
Impacto no leitor: Profissional que quer citar o capítulo em reunião técnica não tem endereço preciso.
Correção exata: Numerar seções no padrão dos outros capítulos (21.1 Conceito intuitivo, 21.2 Analogia, 21.3 Explicação técnica com 21.3.1 a 21.3.7, etc.).
Texto sugerido: n/a (estrutural)
ROI: MÉDIO

### ACHADO 03
Categoria: P1
Problema: A relação entre Princípio 7 (Termômetro) e Princípio 8 (Responsabilidade Indelegável) é mencionada duas vezes (nas perguntas de revisão e no exemplo) mas nunca explicada no corpo do capítulo. Um leitor que não leu os princípios fundacionais não entende a referência.
Por que é um problema: A obra se propõe a ensinar método, não ferramentas. Os Princípios são o núcleo desse método. Mencioná-los sem ancora local enfraquece a conexão.
Impacto no leitor: Joana vê "Princípio 7" e não sabe o que isso significa. CTO que leu os princípios há três capítulos pode ter esquecido.
Correção exata: Adicionar, na primeira menção ao Princípio 7, lembrete de uma frase: "Princípio 7 (Termômetro) — o sistema de IA precisa de instrumentação para ser gerenciável; sem ela, é caixa-preta". Idem para Princípio 8.
Texto sugerido: n/a (adição contextual)
ROI: MÉDIO

### ACHADO 04
Categoria: P2
Problema: O checklist mistura tipos de itens — alguns são ações verificáveis ("Construir um golden set inicial de 30 a 50 casos") e outros são critérios de proficiência ("Defender a regra de juiz diferente do gerador para LLM-as-judge em mesa técnica"). Checklist útil deve ser homogêneo.
Por que é um problema: Itens de "defender" não são checkáveis. O leitor marca o item quando? Depois de uma defesa bem-sucedida? Nunca? A heterogeneidade confunde o uso do checklist como instrumento de progresso.
Impacto no leitor: Checklist perde função de rastreamento de progresso.
Correção exata: Separar em dois blocos: "O que construir" (ações) e "O que dominar" (proficiências). Ou transformar os itens de proficiência em perguntas de revisão (que já existe e é o lugar certo para eles).
Texto sugerido: n/a (reorganização)
ROI: BAIXO

### ACHADO 05
Categoria: P2
Problema: O texto menciona BERTScore como métrica de similaridade sem contextualizar que ela exige modelo de embedding e tem custo computacional diferente do BLEU. Para equipes pequenas, a equiparação pode ser enganosa.
Por que é um problema: BLEU roda em CPU em milissegundos; BERTScore exige embedding model, tem latência maior e dependência de infraestrutura. Equiparar sem nota cria surpresa na implementação.
Impacto no leitor: Equipe decide usar BERTScore baseada no capítulo e descobre custo de infraestrutura não antecipado.
Correção exata: Adicionar nota "(BERTScore exige modelo de embedding; mais custoso que BLEU mas semanticamente superior)" na tabela de tipos.
Texto sugerido: n/a (adição de nota)
ROI: BAIXO

## TESTE DA JOANA
Entenderia: SIM (alto grau)
O que ela entenderia: O laboratório clínico, a pirâmide, a diferença entre "ficou melhor" e eval real, o caso Atlas com o erro dos dois engenheiros. As três perguntas para fazer ao time técnico no fim do caso são perfeitas para ela.
O que ela NÃO entenderia: A tabela de métricas por tipo de tarefa (F1 ponderada, BERTScore, faithfulness + answer relevance) — o vocabulário técnico sem tradução para o leitor não-técnico cria barreira.
Como corrigir: Adicionar, antes da tabela de métricas, uma frase de orientação: "Esta tabela é referência para o time técnico. Como executivo, o que importa é que cada tipo de tarefa tem sua própria forma de medir — pergunte ao time qual métrica primária usam e o que ela significa."

## TESTE DE DURABILIDADE
Classificação: ALTA
2 anos: Excelente — as estruturas (pirâmide, offline/online, golden set, LLM-as-judge) são metodologicamente estáveis.
5 anos: Bom — as métricas específicas (BLEU, ROUGE, BERTScore) podem ser complementadas por novas, mas a lógica de "métrica por tipo de tarefa" permanece.
10 anos: Médio — os frameworks citados (OpenAI Evals, HELM, inspect-ai) podem não existir, mas a pirâmide e o ciclo offline/online são estruturalmente duráveis.
Justificativa: Este é o capítulo mais durável dos seis. O método de eval não depende de modelo específico, de framework específico nem de preço de token. A tese "engenharia vs fé" é a mais invariante da obra.

## TESTE DE DIFERENCIAÇÃO
Classificação: PROPRIEDADE INTELECTUAL
Justificativa: A combinação de pirâmide com cobertura por camada, quadrante de LLM-as-judge, tabela de sete erros com antídoto e ciclo offline/online com retroalimentação — esse sistema integrado não está nos livros da régua de comparação. É o capítulo mais original dos seis analisados.

## TESTE DE MEMORIZAÇÃO
Ideia principal clara? SIM
Qual é a ideia principal (em 1 frase): Sem golden set versionado e gate em CI, toda decisão de IA é fé disfarçada de engenharia.
Justificativa: A frase de abertura do exemplo ("Eval não é luxo de big tech, é a diferença entre engenharia e fé") é a mais citável da obra. Deve ser destacada visualmente no texto.

## TESTE DE TRANSFORMAÇÃO
Ao terminar, o leitor consegue fazer o que antes não conseguia:
- Distinguir as três camadas da pirâmide e atribuir cobertura realista a cada uma no seu produto
- Construir o golden set inicial com critério (30-50 casos, gabarito anotado por especialista, proporção por classe)
- Definir rubrica de LLM-as-judge com 4-6 critérios objetivos e calibrar contra humano
- Identificar o gate de bloqueio em CI e o critério de rollback
- Fazer três perguntas ao time técnico que revelam o estado real de maturidade de eval da organização

## NOTA FINAL (0-10 cada eixo)
Estrutura: 7 | Pedagogia: 9 | Clareza: 8 | Autoridade: 9 | Durabilidade: 9 | Diferenciação: 9 | Memorização: 9 | Transformação: 9
**Nota Geral: 8.6**

## DECISÃO EDITORIAL
MANTER COM AJUSTES — Adicionar numeração de seções (inconsistência estrutural com o resto da obra), referenciar a correlação alvo 0,7, adicionar ancora local para Princípio 7/8, separar checklist em ações/proficiências.

---

# C22 — L1-C22-llmops.md

## RESUMO EXECUTIVO
Nota: 8/10
Veredito: A

## O QUE FUNCIONA
- A distinção entre LLMOps e MLOps clássico no conceito intuitivo é o melhor argumento de abertura do capítulo: direto, com consequência concreta ("o que se versiona é o prompt, não o modelo"). Resolve de imediato a confusão mais cara do mercado.
- A analogia da sala de controle da usina mapeia cada pilar a um sistema da usina. É proporcional, memorável, e a correspondência é precisa o suficiente para ser útil em explicação executiva.
- Os sete pilares com "pergunta executiva" e "indicador-chave" no resumo (tabela 22) é o artefato mais consultável do capítulo. É o que um CTO imprime e coloca na parede.
- A tabela de recortes por persona (CTO / Arquiteto / Desenvolvedor) com "o que precisa saber", "o que não precisa saber" e "pergunta certa ao fornecedor" é genuinamente diferenciada — a maioria dos livros técnicos não tem isso.
- O caso Pólice.io é o melhor caso dos seis capítulos em termos de concretude: o bug específico (campo de estado civil), o custo específico (R$ 96 mil em chamadas desperdiçadas), o tempo de investigação (onze dias), a correção específica (circuit breaker por usuário, cinco chamadas ao modelo premium por sessão). É ensinável, citável, verificável em estrutura.
- O critério de qualidade do projeto ("outro engenheiro, sem contexto, consegue ler o caderno e responder qualquer das sete perguntas executivas") é o melhor critério de projeto dos seis capítulos.

## O QUE NÃO FUNCIONA
- O capítulo não numera seções, mesmo sendo o mais técnico dos seis. Problema idêntico ao C21.
- O Pilar 6 (Segurança Operacional) é significativamente mais curto que os outros. Prompt injection, tool poisoning e data exfiltration recebem dois parágrafos cada; kill switch recebe três linhas. Em capítulo que trata de agentes com custo real, o pilar de segurança merece paridade com os outros.
- A referência a "custo composto em três tempos" no Pilar 5 remete a outro capítulo (Cap 18) sem orientação suficiente para o leitor que não o leu. A formulação "A ferramenta de redução de custo é esse método" assume que o leitor tem o framework em mente.
- O texto menciona "Karpathy, Software 3.0 (palestra, junho de 2025)" nas referências — data posterior à publicação pretendida do livro se escrito antes de 2025. Requer verificação de consistência de datas.
- A distinção entre canário por percentual e canário por segmento (Pilar 3) é boa, mas a regra "quem reclamaria mais alto recebe por último" não tem nuance para setores regulados onde o cliente enterprise tem obrigações contratuais de SLA que não permitem essa sequência.

## ACHADOS

### ACHADO 01
Categoria: P1
Problema: O Pilar 6 (Segurança Operacional) tem profundidade desproporcional em relação aos outros pilares. É o pilar de maior risco operacional e o mais subestimado em prática, mas é o menor em extensão.
Por que é um problema: Em livro que trata de agentes com MCP, a exposição a prompt injection e tool poisoning é vetor primário de incidente — não secundário. Pilar mais curto para tema de maior risco é inversão da prioridade.
Impacto no leitor: Time técnico conclui que segurança operacional é "coberta" pelo capítulo com menos instrução do que precisa para implementar.
Correção exata: Expandir o Pilar 6 com pelo menos uma tabela de defesas (input → defesa → quando suficiente), equiparando profundidade ao Pilar 1 (que tem subsessões detalhadas sobre o que logar, o que não logar, OpenTelemetry). Adicionar exemplo de prompt injection bem-sucedido e seu impacto em agente com MCP.
Texto sugerido: n/a (expansão de conteúdo)
ROI: ALTO

### ACHADO 02
Categoria: P1
Problema: "A ferramenta de redução de custo é esse método" — referência ao custo composto em três tempos sem definição local. Leitores que pularam ou não lembram o Cap 18 ficam sem o instrumento.
Por que é um problema: O Pilar 5 é o mais diretamente ligado ao caso Pólice.io (o bug de custo). Se o leitor não tem o método de custo, o pilar fica sem instrumentação.
Impacto no leitor: CTO entende que deve monitorar custo por feature mas não tem a fórmula para calcular.
Correção exata: Adicionar a fórmula resumida (tokens × chamadas × redundância × tier de modelo = custo composto) em sidebar ou nota no Pilar 5, com remissão ao Cap 18 para detalhe.
Texto sugerido: "A fórmula de referência é custo composto = tokens × chamadas × redundância × tier — desenvolvida no Cap 18. Sem ela, o pilar 5 fica em 'alarmar quando estoura'."
ROI: ALTO

### ACHADO 03
Categoria: P1
Problema: A regra "quem reclamaria mais alto recebe por último" no canário por segmento não tem ressalva para contratos com SLA de cliente enterprise, que frequentemente exigem paridade ou prioridade em rollout.
Por que é um problema: Em produto B2B com SLA contratual, implementar essa regra pode violar o contrato. O CTO que a aplica cegamente em enterprise pode ter litígio antes de ter feedback.
Impacto no leitor: CTO implanta canário por segmento, começa com free/beta, e cliente enterprise com SLA questiona "por que fomos os últimos a receber a nova versão quando pagamos mais?".
Correção exata: Adicionar nota de ressalva: "Em contratos enterprise com SLA explícito de rollout, verificar cláusulas de atualização antes de aplicar a sequência sugerida. Em alguns casos, rollout simultâneo com monitoramento dedicado é preferível a sequência por risco."
Texto sugerido: n/a (nota de ressalva)
ROI: MÉDIO

### ACHADO 04
Categoria: P1
Problema: O MTTR como métrica institucional (Pilar 4) cita "abaixo de 15 minutos para SEV-1 e abaixo de 1 hora para SEV-2" sem referência. São alvos que o mercado vai questionar.
Por que é um problema: Para SRE experiente, 15 minutos de MTTR para SEV-1 é meta muito agressiva em IA (onde o debug de regressão de prompt pode não ser óbvio mesmo com tracing). Sem referência ou ressalva de "para times maduros com tracing completo", o número pode frustrar times iniciantes.
Impacto no leitor: Time anuncia meta de 15 min de MTTR em OKR, falha consistentemente porque o benchmark é para stack maduro, perde credibilidade internamente.
Correção exata: Adicionar "para equipes com os sete pilares implementados" ou citar fonte (Google SRE, Accelerate/DORA metrics). Sugerir MTTR progressivo: meta inicial de 4 horas para SEV-1, com 15 min como meta de maturidade.
Texto sugerido: n/a (ressalva contextual)
ROI: MÉDIO

### ACHADO 05
Categoria: P2
Problema: A referência "Karpathy, Software 3.0 (palestra, junho de 2025)" tem data que pode ser inconsistente com janela de produção do livro, e "palestra" sem URL ou repositório é referência não-verificável.
Por que é um problema: Referência de palestra sem localização permanente é frágil — o conteúdo muda ou sai do ar.
Impacto no leitor: Leitor vai verificar a referência e não encontra o conteúdo; credibilidade das referências cai.
Correção exata: Converter para referência com URL datada ou YouTube, ou substituir por paper equivalente com DOI ou arXiv.
Texto sugerido: n/a (ajuste bibliográfico)
ROI: BAIXO

## TESTE DA JOANA
Entenderia: SIM (alto grau)
O que ela entenderia: A sala de controle da usina, o caso Pólice.io (especialmente o bug do estado civil que custou R$ 96 mil), as três perguntas para fazer ao time técnico, a tabela de recortes por persona (especialmente a coluna CTO).
O que ela NÃO entenderia: OpenTelemetry GenAI semantic conventions, span/trace/session sem tradução mais explícita, a distinção entre shadow mode e canário sem exemplo operacional.
Como corrigir: A tabela de recortes por persona já faz muito do trabalho para Joana. Adicionar sidebar "Se você é executivo, o que precisa saber de cada pilar em uma frase" seria suficiente.

## TESTE DE DURABILIDADE
Classificação: ALTA
2 anos: Excelente — os sete pilares são estruturais, não dependem de ferramentas específicas.
5 anos: Bom — OpenTelemetry GenAI pode ter evoluído, mas a lógica de span/trace/session é padrão de observabilidade independente de implementação.
10 anos: Os frameworks específicos (LangSmith, Langfuse, Helicone) podem não existir, mas a estrutura dos pilares é metodologicamente duradoura.
Justificativa: Este é o segundo capítulo mais durável dos seis. A metodologia de operação não depende de modelo específico. A exceção são as ferramentas citadas — considerar mover lista de ferramentas para Apêndice J atualizado.

## TESTE DE DIFERENCIAÇÃO
Classificação: PROPRIEDADE INTELECTUAL
Justificativa: A organização em sete pilares com pergunta executiva por pilar, combinada com a tabela de recortes por persona e o caso de custo com valor específico (R$ 96 mil, onze dias, bug específico) não está disponível em nenhum dos livros da régua de comparação.

## TESTE DE MEMORIZAÇÃO
Ideia principal clara? SIM
Qual é a ideia principal (em 1 frase): Autonomia sem observabilidade é loop com cartão de crédito — os sete pilares são o que impede que o orçamento de IA seja destruído por invisibilidade.
Justificativa: A epígrafe do capítulo é a ideia mais citável e está corretamente posicionada.

## TESTE DE TRANSFORMAÇÃO
Ao terminar, o leitor consegue fazer o que antes não conseguia:
- Nomear os sete pilares com a pergunta executiva de cada um e o indicador-chave
- Distinguir o que se versiona em LLMOps (prompt, tool, system prompt, dataset) do que se versiona em MLOps clássico (modelo)
- Calcular o MTTR atual da operação e propor meta de melhoria
- Apresentar os recortes por persona em reunião de tech leadership sem traduzir da documentação

## NOTA FINAL (0-10 cada eixo)
Estrutura: 8 | Pedagogia: 9 | Clareza: 8 | Autoridade: 8 | Durabilidade: 9 | Diferenciação: 9 | Memorização: 9 | Transformação: 8
**Nota Geral: 8.5**

## DECISÃO EDITORIAL
MANTER COM AJUSTES — Expandir Pilar 6 (desproporcional para o risco que representa), adicionar fórmula de custo composto local no Pilar 5, numerar seções, ajustar referência Karpathy.

---

# C23 — L1-C23-alignment.md

## RESUMO EXECUTIVO
Nota: 8/10
Veredito: A

## O QUE FUNCIONA
- A abertura com "modelo não tem valores, tem treinamento" é a tese mais intelectualmente corajosa dos seis capítulos. É verdadeira, vai contra o marketing dos fornecedores, e tem consequência operacional imediata.
- O quadro 23.A com as seis famílias de alignment (RLHF, RLAIF, DPO, KTO, ORPO, GRPO) com paper canônico, arXiv, dado necessário, custo de coleta, quando preferir e trade-off principal é a tabela de referência mais densa de valor dos seis capítulos. É propriedade intelectual real — não existe equivalente em português.
- As quatro perguntas para ler a tabela em decisão real (qual família o fornecedor declara, o trade-off casa com seu domínio, o dado necessário existe, seu time consegue operar a coprodução) são o melhor sequenciamento decisório do livro. Aplicável amanhã.
- A seção sobre faithfulness de chain-of-thought (23.3.4) com referência a Lanham 2023 é altamente diferenciada — é conteúdo que a maioria dos CTOs não conhece e que tem implicação regulatória imediata (LGPD Art. 20 e auditoria regulatória).
- O caso da healthtech com triagem psiquiátrica é o mais complexo dos seis capítulos e cumpre a função: mostra que a escolha de técnica de alignment é decisão executiva com custo, responsável e consequência, não decisão de engenheiro isolada.
- A seção 23.5 para executivos com três perguntas duras é a mais acionável dos seis capítulos para o leitor não-técnico.
- A discussão sobre Constitutional AI como documento operacional auditável é a framing mais útil do conceito para o contexto corporativo brasileiro.

## O QUE NÃO FUNCIONA
- O capítulo é o mais longo dos seis e tem dois momentos de redundância: a analogia do profissional sênior (23.2) e a explicação técnica (23.3) repetem o mapeamento das três camadas com ênfase diferente, mas sem ganho adicional suficiente para justificar a repetição.
- O capítulo promete, no final da seção 23.1, descer "ao detalhe técnico das seis famílias" e "ao detalhe operacional das decisões que cabem ao cliente". A promessa é cumprida, mas a transição entre os dois tipos de detalhe não é sinalizada claramente — o leitor técnico e o executivo acabam nos mesmos parágrafos sem orientação de profundidade esperada.
- GRPO é descrita como "usada no R1" com referência a DeepSeekMath e DeepSeek-R1 — mas o quadro 23.A não inclui o paper de DeepSeekMath (arXiv:2402.03300) na coluna "paper canônico", misturando dois papers distintos com mecanismos distintos. Imprecisão técnica em tabela de referência.
- A seção 23.4 ("Conexão com o Capítulo 19 e com o Capítulo 14B") é correta mas parece inserida como parágrafo de transição, não como seção com substância. O CTO que precisar consultar essa conexão não encontra instrumentação nova — apenas confirmação de que os capítulos se relacionam.
- O exercício 4 ("Mesa de escolha de alignment") é o mais rico dos exercícios mas pressupõe que o leitor tem CTO, product owner e compliance disponíveis para uma sessão. Para empresa menor ou para profissional individual, o exercício não tem ponto de entrada.

## ACHADOS

### ACHADO 01
Categoria: P0
Problema: O quadro 23.A atribui ao GRPO dois papers distintos na coluna "paper canônico" — arXiv:2402.03300 (DeepSeekMath) e arXiv:2501.12948 (DeepSeek-R1) — como se fossem o mesmo paper. São papers com autores parcialmente sobrepostos mas com mecanismos e contribuições distintas.
Por que é um problema: Tabela de referência de nível de auditoria deve ter precisão bibliográfica. Misturar dois papers em uma entrada quebra a credibilidade da tabela para leitor técnico que for verificar.
Impacto no leitor: CTO cita "DeepSeek, 2024 (arXiv:2402.03300)" para GRPO em comitê; colega verifica e encontra que o paper é sobre raciocínio matemático, não o paper do R1. Credibilidade da referência desce.
Correção exata: Separar em duas entradas na coluna paper ou clarificar: "DeepSeekMath (arXiv:2402.03300, 2024) introduz GRPO; DeepSeek-R1 (arXiv:2501.12948, jan/2025) demonstra GRPO em escala para raciocínio".
Texto sugerido: "DeepSeekMath (Shao et al., 2024, arXiv:2402.03300) — introduz GRPO; aprofundado em DeepSeek-R1 (DeepSeek-AI, 2025, arXiv:2501.12948)"
ROI: ALTO

### ACHADO 02
Categoria: P1
Problema: A redundância entre a analogia do profissional sênior (23.2) e a seção de explicação técnica (23.3) aumenta o comprimento sem agregar nova informação. As "três lições" da analogia (23.2) são repetidas implicitamente em 23.3.
Por que é um problema: O capítulo já é o mais longo dos seis. Redundância em texto técnico-executivo custa atenção do leitor.
Impacto no leitor: Joana pula um dos dois blocos; CTO técnico também. O segundo bloco perde leitura porque parece repetição.
Correção exata: Reduzir a analogia (23.2) para um parágrafo de mapeamento direto e eliminar as "três lições" explícitas — elas emergem naturalmente da explicação técnica que se segue.
Texto sugerido: n/a (condensar seção 23.2 de três páginas para um parágrafo)
ROI: MÉDIO

### ACHADO 03
Categoria: P1
Problema: A seção 23.4 ("Alignment não fecha, alignment eleva o piso") é correta conceitualmente mas não entrega instrumentação nova ao leitor. É descrição de relação entre capítulos, não seção com ferramenta ou insight adicional.
Por que é um problema: Em livro que promete método, seção que apenas confirma que capítulos se relacionam é fraca. O leitor já sabe que alignment conecta com segurança, evals e governança — ele esperava saber *como* ativar essa conexão.
Impacto no leitor: CTO sente que a seção é preenchimento de estrutura.
Correção exata: Transformar 23.4 em uma decisão operacional concreta: "Quando alignment falha e segurança precisa agir — o protocolo de escalação". Isso dá instrumentação nova em vez de apenas confirmar conexão existente.
Texto sugerido: n/a (transformar em protocolo)
ROI: MÉDIO

### ACHADO 04
Categoria: P1
Problema: O exercício 4 ("Mesa de escolha de alignment") pressupõe disponibilidade de CTO, product owner e compliance para sessão formal. Profissional em empresa menor, ou individual, não tem esse ponto de entrada.
Por que é um problema: O livro se propõe a alcançar diferentes tamanhos de organização. Exercício que requer quórum executivo exclui parte relevante do público-alvo.
Impacto no leitor: Pequena empresa vê exercício e conclui que alignment é coisa de grande empresa — conclusão que o livro quer combater.
Correção exata: Adicionar variante do exercício 4 para individual ou empresa pequena: "Se você não tem mesa executiva disponível, simule os papéis: liste as restrições de orçamento (CTO), os objetivos de produto (PO) e as obrigações de compliance da sua regulação. Use as quatro perguntas da seção 23.3 como roteiro."
Texto sugerido: n/a (adição de variante)
ROI: MÉDIO

### ACHADO 05
Categoria: P2
Problema: A seção 23.3.5 (Red teaming sistemático) cita "equipes de alignment em Anthropic, OpenAI e DeepMind a partir de 2022" como referência de prática madura. Não cita paper ou documento público verificável — é afirmação de autoridade por associação.
Por que é um problema: O leitor não sabe quais documentos públicos dessas equipes sustentam a descrição das três camadas de red team. A Responsible Scaling Policy da Anthropic (já nas referências) cobre parte disso, mas a conexão não é feita.
Impacto no leitor: CTO quer verificar o claim sobre cadência semanal de red team interno e não sabe onde procurar.
Correção exata: Adicionar referência específica à Responsible Scaling Policy e ao model card de safety da Anthropic para a cadência de red team descrita.
Texto sugerido: n/a (adição de referência)
ROI: BAIXO

## TESTE DA JOANA
Entenderia: SIM (parcial — seções técnicas são densas)
O que ela entenderia: A abertura sobre "modelo não tem valores, tem treinamento", a analogia do profissional sênior, o caso da healthtech (muito bem narrado), as três perguntas para o time técnico na seção 23.5, a ideia de constituição interna como documento que a empresa escreve.
O que ela NÃO entenderia: A tabela das seis famílias com arXiv (não sabe o que é arXiv), DPO/KTO/ORPO/GRPO (abreviações sem ancoragem prévia suficiente para leigo), a seção de faithfulness de chain-of-thought (muito técnica sem tradução executiva).
Como corrigir: Adicionar, antes da tabela das seis famílias, uma frase de orientação para Joana: "Se você é executivo, as quatro perguntas da próxima seção são o que importa. A tabela é referência para o time técnico." Para faithfulness, adicionar implicação executiva em negrito antes da explicação técnica.

## TESTE DE DURABILIDADE
Classificação: ALTA
2 anos: Excelente — RLHF, Constitutional AI, DPO são técnicas estabelecidas; os papers de referência são permanentes.
5 anos: Bom — GRPO e ORPO são mais recentes e podem ser sucedidos, mas o framework de "seis famílias com trade-off" permanece como metodologia de análise.
10 anos: As técnicas específicas podem ter evoluído, mas o princípio de "coprodução de alignment" e as categorias de vício (over-refusal, sycophancy, faithfulness) são estruturalmente duradouros.
Justificativa: O capítulo é metodologicamente maduro. A maior ameaça à durabilidade são as técnicas mais recentes (GRPO, ORPO) que podem ser sucedidas — mas estão corretamente enquadradas como "em uso ativo em 2026", não como permanentes.

## TESTE DE DIFERENCIAÇÃO
Classificação: PROPRIEDADE INTELECTUAL
Justificativa: Nenhum livro da régua de comparação (nem Co-Intelligence, nem Competing in the Age of AI) trata alignment com esse nível de detalhe técnico operacional + implicação regulatória brasileira (LGPD Art. 20) + tabela de referência de seis famílias com arXiv. É conteúdo genuinamente diferenciado para o mercado brasileiro.

## TESTE DE MEMORIZAÇÃO
Ideia principal clara? SIM
Qual é a ideia principal (em 1 frase): Alignment não é entregue pelo fornecedor — é coproduzido pela organização em cada deploy, e a responsabilidade tem nome, data e accountable.
Justificativa: A citação final do caso healthtech ("Alignment não é entregue pelo fornecedor, é coproduzido pela organização") é a mais citável do capítulo e deveria ser destacada visualmente.

## TESTE DE TRANSFORMAÇÃO
Ao terminar, o leitor consegue fazer o que antes não conseguia:
- Identificar, em uma frase, a técnica de alignment do modelo em produção e o trade-off implícito que precisa compensar
- Fazer as quatro perguntas ao fornecedor que revelam o que a documentação de vendas não mostra
- Redigir a constituição interna v0 da organização para produto específico
- Distinguir over-refusal, under-refusal e sycophancy como métricas operacionais distintas, não como conceitos abstratos

## NOTA FINAL (0-10 cada eixo)
Estrutura: 7 | Pedagogia: 8 | Clareza: 8 | Autoridade: 9 | Durabilidade: 9 | Diferenciação: 10 | Memorização: 8 | Transformação: 8
**Nota Geral: 8.4**

## DECISÃO EDITORIAL
MANTER COM AJUSTES — Corrigir P0 na tabela GRPO (dois papers distintos misturados), condensar seção 23.2 (redundância com 23.3), transformar 23.4 em protocolo operacional em vez de confirmação de relação, adicionar variante de exercício 4 para empresa pequena.

---

# C24 — L1-C24-governanca.md

## RESUMO EXECUTIVO
Nota: 8/10
Veredito: A

## O QUE FUNCIONA
- A abertura com "foi o algoritmo que decidiu" é a frase mais potente dos seis capítulos como gancho executivo. Qualquer CEO ou CFO que já viveu incidente com esse enquadramento se conecta imediatamente.
- A tripartição política/processo/prática com a definição precisa de quando cada camada falha é o conceito mais original do capítulo. "Governança que cobre duas é frágil" é afirmação memorável e verificável.
- Os dez controles canônicos com camada (técnica, operacional, executiva) e escala de maturidade 0-4 são o artefato mais acionável do capítulo. Qualquer organização consegue usar como autodiagnóstico amanhã.
- O caso da seguradora com a multa da ANPD é o mais impactante dos seis capítulos para público executivo brasileiro: valor da multa (R$ 4,2 milhões), artigo da LGPD violado (Art. 20), consequências institucionais (substituição do Diretor de Dados, auditoria externa), custo não-financeiro (queda de 0,3 ponto de share). É concreto, local, e inevitável de ler.
- A seção 24.3.1 com critério de quando criar AI Council, Comitê de Ética e Comitê de Riscos por tamanho de organização ("pequena, média, grande") é rara em literatura de governança — a maioria pressupõe enterprise.
- A trilha regulatória com "padrão durável" em vez de texto específico é a decisão editorial mais inteligente do capítulo: protege a durabilidade sem sacrificar a orientação.
- O critério de qualidade do projeto ("outro executivo, sem contexto, lê o caderno e responde sem ambiguidade quem é o Accountable por X") é preciso e testável.

## O QUE NÃO FUNCIONA
- O diagrama 24.2 ("As 3 camadas de controle") não tem arquivo SVG referenciado — a linha do texto menciona apenas "Pirâmide com três níveis verticais — técnica (base), operacional (meio), executiva (topo)" sem o marcador de imagem que os outros capítulos usam. Pode ser erro de formatação ou arquivo pendente.
- O mesmo problema ocorre com o diagrama 24.3 ("Fluxo de resposta a incidente") — texto descritivo sem referência a arquivo SVG.
- A distinção entre AI Council e Comitê de Riscos (24.3.1) é clara, mas a fronteira entre "Comitê de Ética em IA" e "AI Council em pauta ampla" em empresa pequena é vaga. O texto diz "um único AI Council com pauta ampla" mas não explica como integrar ética em pauta de AI Council.
- O Princípio 8 é mencionado por nome múltiplas vezes ("Responsabilidade Indelegável", "Princípio 8") mas o capítulo não define o princípio localmente. Para leitor que chegou ao capítulo 24 sem ler os anteriores, é referência opaca.
- A política de incidentes (24.3.4) menciona "comunicação externa pré-escrita por classe de incidente" sem oferecer exemplo de linguagem ou template. É o item mais urgente em incidente real e o menos instrumentado.

## ACHADOS

### ACHADO 01
Categoria: P0
Problema: Diagramas 24.2 e 24.3 têm conteúdo descrito no texto mas sem arquivo SVG referenciado — ao contrário do diagrama 24.1 e de todos os diagramas dos outros capítulos.
Por que é um problema: Se o livro for publicado sem esses arquivos, dois dos três diagramas do capítulo mais visual (governança) estarão ausentes. O texto que os descreve não substitui o visual.
Impacto no leitor: Capítulo de governança chega ao leitor com lacuna visual justo nos dois diagramas que mapeiam controles e incidente — os mais usados em apresentação executiva.
Correção exata: Criar ou referenciar os SVGs para diagrama 24.2 (pirâmide de controles) e diagrama 24.3 (fluxo de incidente), no padrão de nomenclatura L1-C42-img-02 e L1-C42-img-03.
Texto sugerido: n/a (produção de artefato)
ROI: ALTO

### ACHADO 02
Categoria: P1
Problema: Integração de ética em pauta de AI Council em empresa pequena não é instrumentada. O texto diz "um único AI Council com pauta ampla" mas não diz o que "pauta ampla" significa em prática para ética.
Por que é um problema: Empresa de 50 pessoas que opera IA em saúde ou jurídico precisa de ética integrada à governança, mas o texto não diz como fazer isso em single-body sem criar overhead de comitê separado.
Impacto no leitor: Empresa pequena conclui que ética é assunto de "quando crescer". Essa conclusão é errada e cara.
Correção exata: Adicionar nota operacional: "Para organizações menores, integre ética ao AI Council com dois mecanismos: (1) pauta fixa de casos limítrofes a cada reunião, com critério pré-acordado de o que constitui caso limítrofe; (2) consultor externo de ética em sessão semestral como observador com direito de voz."
Texto sugerido: n/a (adição de parágrafo)
ROI: MÉDIO

### ACHADO 03
Categoria: P1
Problema: A política de incidentes menciona "comunicação externa pré-escrita por classe de incidente" como componente mínimo, mas não oferece exemplo de linguagem, template ou critério de o que vai para fora vs o que fica interno.
Por que é um problema: Em SEV-1 real, o responsável de comunicação começa a escrever do zero enquanto a crise acontece. A recomendação de ter comunicação "pré-escrita" é correta mas não acionável sem ao menos uma estrutura de template.
Impacto no leitor: Time implanta política de incidente, chega ao SEV-1 real e descobre que "comunicação pré-escrita" na política é uma nota sem conteúdo.
Correção exata: Adicionar template de comunicação externa de uma frase para SEV-1 (vítima de decisão automatizada): "Identificamos um incidente em nosso sistema de IA que pode ter afetado clientes entre [data] e [data]. Estamos investigando e entraremos em contato com clientes afetados em até [prazo]. Para dúvidas: [canal]."
Texto sugerido: n/a (adição de template)
ROI: MÉDIO

### ACHADO 04
Categoria: P1
Problema: O Princípio 8 ("Responsabilidade Indelegável") é mencionado cinco vezes no capítulo sem definição local. Para leitor que chegou ao capítulo 24 como ponto de entrada (executivo que recebeu o capítulo específico por recomendação), é referência opaca.
Por que é um problema: Capítulo de governança deve funcionar parcialmente standalone, especialmente para executivos que recebem apenas este capítulo em briefing.
Impacto no leitor: Joana vê "Princípio 8" três vezes e não sabe o que é. Conclude que o livro é "para quem já leu tudo".
Correção exata: Na primeira menção ao Princípio 8, adicionar definição em uma frase: "Princípio 8 da obra — a responsabilidade por decisão de IA nunca pode ser delegada à máquina; há sempre um nome humano na cadeira de quem responde."
Texto sugerido: n/a (adição de definição local)
ROI: MÉDIO

### ACHADO 05
Categoria: P2
Problema: A referência a "ANPD — Notas Técnicas sobre IA generativa (versão corrente verificável em fonte oficial)" é a mais vaga da obra. A ANPD publicou material específico que poderia ser citado com data.
Por que é um problema: Referência vaga ("versão corrente verificável em fonte oficial") não ajuda o leitor a encontrar o documento. É o equivalente de citar "livro disponível em livraria".
Impacto no leitor: Leitor vai ao site da ANPD e encontra vários documentos sem saber qual é o relevante.
Correção exata: Citar o documento específico mais recente disponível na data de fechamento do manuscrito, com URL datada conforme método do Apêndice J.
Texto sugerido: n/a (ajuste bibliográfico)
ROI: BAIXO

## TESTE DA JOANA
Entenderia: SIM (muito bem)
O que ela entenderia: "Foi o algoritmo que decidiu" como frase que não convence ninguém, o caso da seguradora (drama, valor, consequências), a regra do Accountable único, a analogia da linha aérea. O bloco "Para Executivos" com as três perguntas é o melhor gancho de ação imediata do capítulo.
O que ela NÃO entenderia: Os dez controles técnicos (canário, rollback, OpenTelemetry, tracing) sem explicação local, a distinção entre Comitê de Ética e AI Council quando funcionam separados.
Como corrigir: A tabela dos dez controles já tem "o que verifica" — adicionar coluna "explicação em 1 frase" para os seis controles técnicos tornaria a tabela acessível para Joana sem sacrificar a densidade técnica para o CTO.

## TESTE DE DURABILIDADE
Classificação: ALTA
2 anos: Excelente — as três camadas, o RACI, os dez controles, a AUP são independentes de modelo ou tecnologia.
5 anos: Excelente — a estrutura de governança corporativa tem durabilidade institucional análoga ao SRE.
10 anos: A regulação específica (PL 2338, EU AI Act 2024/1689) terá evoluído, mas o padrão durável (classificação por risco, obrigações proporcionais) permanece. Decisão de ensinar padrão em vez de texto é a mais inteligente do livro.
Justificativa: Este é o capítulo de maior durabilidade dos seis. A estrutura de governança não depende de tecnologia. O único envelhecimento previsto é nas regulações específicas — endereçado pela decisão de ensinar padrão.

## TESTE DE DIFERENCIAÇÃO
Classificação: PROPRIEDADE INTELECTUAL
Justificativa: Tripartição política/processo/prática, dez controles com escala de maturidade 0-4, RACI de IA com regra do Accountable único, e o caso da seguradora com ANPD e LGPD Art. 20 em contexto brasileiro não estão em nenhum dos livros da régua.

## TESTE DE MEMORIZAÇÃO
Ideia principal clara? SIM
Qual é a ideia principal (em 1 frase): Governança não é documento publicado — é controle aplicado, e a falta de um Accountable único por decisão de IA não aparece no balanço até aparecer de uma vez.
Justificativa: A citação final ("Governança não é documento publicado. É controle aplicado. Quem confunde descobre na multa, no processo ou na manchete.") é a mais citável do capítulo e deve ter destaque visual.

## TESTE DE TRANSFORMAÇÃO
Ao terminar, o leitor consegue fazer o que antes não conseguia:
- Autodiagnosticar os dez controles em escala 0-4 e identificar os mais frágeis
- Redigir a AUP da organização em quatro páginas ou menos
- Preencher o RACI de IA para cinco decisões reais com Accountable único por decisão
- Conduzir simulado de SEV-1 com time usando o runbook descrito

## NOTA FINAL (0-10 cada eixo)
Estrutura: 8 | Pedagogia: 9 | Clareza: 8 | Autoridade: 9 | Durabilidade: 10 | Diferenciação: 9 | Memorização: 9 | Transformação: 9
**Nota Geral: 8.9**

## DECISÃO EDITORIAL
MANTER COM AJUSTES — Corrigir P0 (criar/referenciar SVGs para diagramas 24.2 e 24.3), instrumentar integração de ética no AI Council de empresa pequena, adicionar template de comunicação externa de SEV-1, definir Princípio 8 localmente.

---

# C25 — L1-C25-trade-offs.md

## RESUMO EXECUTIVO
Nota: 7/10
Veredito: B

## O QUE FUNCIONA
- A analogia da carta do restaurante é a mais simples e mais imediata dos seis capítulos: não exige explicação, escala bem para diferentes públicos, e os três pontos derivados (adequação, consciência, repetibilidade) são pedagogicamente exatos.
- O título de "cardápio executivo de IA" e a promessa de referência consultável antes de qualquer decisão é o posicionamento correto. O capítulo cumpre essa promessa em forma se não completamente em substância.
- A estrutura tabular de cada trade-off (quando faz sentido / quando é desperdício) é clara, consultável e corretamente evita hierarquia entre opções.
- O anti-padrão explícito do T2 ("escolher agente autônomo porque tem N cenários") é o insight mais acionável do capítulo para o leitor que já tomou essa decisão errada.
- O caso do e-commerce com os 27 cenários e a migração para workflow determinístico para 24 + agente para 3 é o mais instrutivo dos seis em termos de precisão da decisão arquitetural descrita. O número (80% para workflow, 20% para agente) é verificável na própria narrativa.
- A árvore de decisão integrada (T4 → T1 → T5 → T2 → T6 → T3) é o artefato mais diferenciado do capítulo — sequência de decisão raramente explicitada em literatura.
- A regra "começar com human-in-the-loop e migrar para automação plena conforme golden set e adversarial madurem" é metodologicamente sólida e alinhada com a tese da obra.

## O QUE NÃO FUNCIONA
- O capítulo é o mais curto dos seis e deixa cada trade-off significativamente underspecified. A tabela "quando faz sentido / quando é desperdício" tem duas linhas por coluna — suficiente para reconhecimento, insuficiente para decisão real em casos limítrofes.
- A árvore de decisão integrada é descrita textualmente ("sequência T4 → T1 → T5 → T2 → T6 → T3") mas o diagrama que a visualiza não tem arquivo SVG referenciado além do diagrama 25.1. Os diagramas 25.2 e 25.3 têm apenas descrição textual sem arquivo.
- O T3 (modelo fechado × open source) não menciona o trade-off de dependência de fornecedor (vendor lock-in) como eixo, mencionando apenas soberania de dado, TCO e ponta de qualidade. Vendor lock-in é o quarto eixo que governa muitas decisões reais.
- O T6 (generalismo × especialização) não aborda o trade-off de latência entre modelo geral e especializado — que pode ser o eixo dominante em aplicações de tempo real.
- O capítulo promete ser "referência consultada antes de qualquer decisão de arquitetura" mas não tem formato indexável: sem numeração de trade-off na seção, sem tabela-resumo que listaria os seis em ordem com eixo decisor em formato scannable antes do conteúdo completo. O leitor que quer consultar rápido precisa navegar pelo texto.
- A referência "Brooks, F. The Mythical Man-Month (1975/1995) — fundamentos do triângulo" aplica ao triângulo escopo/tempo/custo do desenvolvimento de software, não ao triângulo latência/qualidade/custo de IA. A transferência é razoável mas não referenciada no texto de forma que o leitor possa rastreá-la.

## ACHADOS

### ACHADO 01
Categoria: P1
Problema: Diagramas 25.2 (árvore de decisão integrada) e 25.3 (triângulo latência × qualidade × custo) são descritos no texto mas não têm arquivo SVG referenciado — inconsistência com o capítulo 20 e com o capítulo 21 que têm todos os SVGs referenciados.
Por que é um problema: A árvore de decisão integrada é o artefato mais diferenciado do capítulo. Sem visualização, perde metade do valor. O triângulo T4 sem visualização é particularmente problemático porque é o conceito mais usado em reunião executiva.
Impacto no leitor: Leitor chega ao diagrama 25.2 e vê descrição em texto; não tem o visual para usar em apresentação. O capítulo "cardápio executivo" chega ao executivo sem o cardápio visual.
Correção exata: Criar ou referenciar os SVGs para diagrama 25.2 (árvore de decisão) e 25.3 (triângulo), no padrão L1-C43-img-02 e L1-C43-img-03.
Texto sugerido: n/a (produção de artefato)
ROI: ALTO

### ACHADO 02
Categoria: P1
Problema: O capítulo não tem tabela-resumo dos seis trade-offs com eixo decisor em formato scannable antes do conteúdo. O leitor que quer "consultar antes de qualquer decisão" precisa navegar por seis seções.
Por que é um problema: O capítulo se autoproclama "cardápio" e "referência consultável". Cardápio que exige ler três páginas antes de ver os itens não é cardápio — é texto.
Impacto no leitor: O executor que volta ao capítulo para consulta rápida sai frustrado porque não encontra a síntese rápida que precisa.
Correção exata: Mover a tabela de resumo executivo (25.9) para o início do capítulo, logo após a analogia (25.2), como "cardápio rápido" de uma página. Manter a versão completa em 25.9 como referência.
Texto sugerido: n/a (reorganização)
ROI: ALTO

### ACHADO 03
Categoria: P1
Problema: O T3 (modelo fechado × open source) não inclui vendor lock-in como eixo de decisão, mencionando apenas soberania de dado, TCO real, ponta de qualidade e maturidade de ops. Vendor lock-in (dependência de API, formato proprietário, política de preço, descontinuação) é frequentemente o eixo dominante em decisão de arquitectura de longo prazo.
Por que é um problema: Time que decide por modelo fechado "por qualidade" sem considerar vendor lock-in pode descobrir em dezoito meses que o fornecedor mudou preço, formato de API, ou descontinuou o modelo. A omissão do eixo é lacuna estrutural.
Impacto no leitor: CTO opta por modelo fechado com base nos quatro eixos listados; em dezoito meses enfrenta migração forçada que não estava no TCO original.
Correção exata: Adicionar "risco de lock-in" como quinto eixo no T3, com "quando faz sentido" e "quando é desperdício" correspondentes.
Texto sugerido: n/a (expansão de tabela)
ROI: ALTO

### ACHADO 04
Categoria: P1
Problema: A referência a Brooks (Mythical Man-Month) como "fundamentos do triângulo" de latência/qualidade/custo é imprecisa: o triângulo de Brooks é escopo/tempo/custo de projeto, não latência/qualidade/custo de sistema. A transferência analógica é razoável mas não é declarada como analogia — é apresentada como referência direta.
Por que é um problema: Leitor técnico que conhece Brooks verifica a referência e encontra triângulo diferente. A credibilidade das referências cai.
Impacto no leitor: Engenheiro sênior que usa o livro em treinamento interno percebe a imprecisão e a usa para questionar outras referências.
Correção exata: Substituir por referência mais direta ao triângulo CAP (Brewer, 2000) para sistemas distribuídos, ou ao triângulo de qualidade de software (ISO 25010), ou declarar explicitamente: "O princípio clássico de triângulo em engenharia de projeto (Brooks, 1975) se aplica analogamente a IA: [...]".
Texto sugerido: "O triângulo é princípio clássico de engenharia de sistemas: otimizar duas dimensões simultaneamente custa sempre na terceira. Aplicado a IA, as três dimensões são latência, qualidade e custo."
ROI: MÉDIO

### ACHADO 05
Categoria: P2
Problema: O T5 (automação × human-in-the-loop) não menciona o custo de human-in-the-loop em escala. Para produto com volume de milhões de interações/mês, HITL pode ser economicamente inviável mesmo quando regulação o exige, gerando tensão não endereçada.
Por que é um problema: O leitor conclui "domínio sensível → HITL" sem saber o que fazer quando o custo de HITL em escala inviabiliza o produto.
Impacto no leitor: Healthtech ou fintech em escala coloca HITL em tudo que é regulado, descobre que o custo é proibitivo, e corta o HITL sem framework — exatamente o que o capítulo quer evitar.
Correção exata: Adicionar nota no T5: "Em volume alto, HITL pleno pode ser economicamente inviável. A solução arquitetural é HITL por amostra estatística (auditoria periódica em vez de revisão universal), com critério de amostragem explícito e documentado — conforme LGPD e AI Act permitem para sistemas com histórico de qualidade demonstrado."
Texto sugerido: n/a (adição de nota)
ROI: MÉDIO

## TESTE DA JOANA
Entenderia: SIM
O que ela entenderia: A analogia do restaurante, o anti-padrão do agente autônomo para 27 cenários, o caso do e-commerce (muito concreto), as perguntas executivas de cada trade-off, a regra de começar com HITL.
O que ela NÃO entenderia: A árvore de decisão integrada sem o diagrama visual, as diferenças sutis entre T1 (RAG vs fine-tuning vs prompt) sem ter lido os capítulos correspondentes.
Como corrigir: A tabela de resumo executivo no início (como sugerido no achado 02) resolve o problema principal para Joana — ela lê a tabela e identifica qual trade-off é relevante para sua decisão.

## TESTE DE DURABILIDADE
Classificação: ALTA
2 anos: Excelente — os seis trade-offs são estruturais, não dependem de modelo específico.
5 anos: Excelente — RAG vs fine-tuning, agente vs workflow, aberto vs fechado são categorias que permanecem relevantes mesmo que os modelos mudem.
10 anos: Médio — o T3 (fechado vs open source) pode ter estrutura de mercado diferente; os outros cinco são metodologicamente permanentes.
Justificativa: Este é o segundo capítulo de maior durabilidade. A estrutura de trade-off é independente de tecnologia. O único risco é que o mercado de modelos abertos mude a estrutura do T3 de forma que o eixo soberania/TCO/qualidade não capture mais a decisão relevante.

## TESTE DE DIFERENCIAÇÃO
Classificação: DIFERENCIADO
Justificativa: A sequência de decisão T4→T1→T5→T2→T6→T3 e a síntese dos seis trade-offs com pergunta executiva e eixo decisor em formato consultável não estão nos livros da régua. Porém, o conteúdo individual de cada trade-off está mais desenvolvido em capítulos anteriores — este capítulo sintetiza, não adiciona insight novo por trade-off.

## TESTE DE MEMORIZAÇÃO
Ideia principal clara? SIM
Qual é a ideia principal (em 1 frase): Toda decisão de arquitetura de IA se reduz a seis trade-offs canônicos com eixos explícitos — quem domina os eixos decide rápido e correto; quem decide por intuição refaz a decisão a cada trimestre.
Justificativa: A epígrafe ("Não existe decisão de IA sem trade-off. Existe decisão sem consciência do trade-off.") é a mais citável do capítulo.

## TESTE DE TRANSFORMAÇÃO
Ao terminar, o leitor consegue fazer o que antes não conseguia:
- Recitar os seis trade-offs com a pergunta executiva e o eixo decisor de cada um
- Classificar uma proposta de agente autônomo usando o eixo variabilidade × auditabilidade × custo composto do T2
- Defender, em dez minutos para a diretoria, a arquitetura atual com base nos eixos dos trade-offs
- Identificar qual trade-off uma decisão recente da organização "ignorou" e qual a consequência

## NOTA FINAL (0-10 cada eixo)
Estrutura: 7 | Pedagogia: 8 | Clareza: 8 | Autoridade: 7 | Durabilidade: 9 | Diferenciação: 7 | Memorização: 8 | Transformação: 8
**Nota Geral: 7.8**

## DECISÃO EDITORIAL
MANTER COM AJUSTES — Corrigir P1s estruturais (criar SVGs para diagramas 25.2 e 25.3, mover tabela-resumo para o início, adicionar vendor lock-in no T3), corrigir referência Brooks, adicionar nota sobre HITL em escala.

---

## LINHAS-TRACKER

C20|L1-C20-futuro.md|01|P0|ALTO|Número sem fonte: "60-70% da carga repetível" no cenário otimista|Citar fonte verificável ou reformular como estimativa qualitativa com referência ao Apêndice J|MANTER COM AJUSTES
C20|L1-C20-futuro.md|02|P0|ALTO|Número sem fonte: "30-80% de ganhos" no cenário mediano sem referência|Substituir por fonte específica (McKinsey, MIT ou similar) ou declarar variância como inutilizável para planejamento|MANTER COM AJUSTES
C20|L1-C20-futuro.md|03|P0|ALTO|Parágrafo ilegível sobre AGI (seção 20.7): frase de 200+ palavras com ressalvas empilhadas|Quebrar em três afirmações curtas com probabilidade subjetiva qualitativa|MANTER COM AJUSTES
C20|L1-C20-futuro.md|04|P1|ALTO|Quatro vetores sem critério de medição operacional|Adicionar 2-3 indicadores observáveis por vetor para instrumentar rito trimestral do AI Council|MANTER COM AJUSTES
C20|L1-C20-futuro.md|05|P1|MÉDIO|PL 2338 tratado como sancionado em cenários otimista e mediano (estava em tramitação)|Reformular condicionalmente em ambos os cenários|MANTER COM AJUSTES
C20|L1-C20-futuro.md|06|P1|MÉDIO|Horizonte de 12 meses delegado ao planejamento anual sem orientação de como aplicar o método nesse horizonte|Adicionar subtópico com orientação mínima para ciclo de 12 meses|MANTER COM AJUSTES
C20|L1-C20-futuro.md|07|P2|BAIXO|Referência à Shell sem citação de Wack (1985) no corpo do texto|Inserir referência parentética no body|MANTER COM AJUSTES
C21|L1-C21-evals.md|01|P1|ALTO|Correlação alvo 0,7 para LLM-as-judge sem referência|Citar Zheng et al. 2023 ou declarar limiar como operacional com nota de variação por domínio|MANTER COM AJUSTES
C21|L1-C21-evals.md|02|P1|MÉDIO|Capítulo sem numeração de seções — inconsistência com o resto da obra|Numerar seções no padrão 21.1, 21.2, 21.3.x|MANTER COM AJUSTES
C21|L1-C21-evals.md|03|P1|MÉDIO|Princípio 7 e Princípio 8 mencionados sem definição local|Adicionar definição em uma frase na primeira menção de cada princípio|MANTER COM AJUSTES
C21|L1-C21-evals.md|04|P2|BAIXO|Checklist mistura ações verificáveis e critérios de proficiência|Separar em dois blocos: "O que construir" e "O que dominar"|MANTER COM AJUSTES
C21|L1-C21-evals.md|05|P2|BAIXO|BERTScore equiparado a BLEU sem nota de custo computacional distinto|Adicionar nota de custo e dependência de embedding model|MANTER COM AJUSTES
C22|L1-C22-llmops.md|01|P1|ALTO|Pilar 6 (Segurança Operacional) desproporcional em extensão para o risco que representa|Expandir com tabela de defesas e exemplo de prompt injection em agente com MCP|MANTER COM AJUSTES
C22|L1-C22-llmops.md|02|P1|ALTO|Custo composto em três tempos referenciado sem fórmula local no Pilar 5|Adicionar fórmula resumida (tokens × chamadas × redundância × tier) em sidebar|MANTER COM AJUSTES
C22|L1-C22-llmops.md|03|P1|MÉDIO|Regra de canário por segmento sem ressalva para contratos enterprise com SLA|Adicionar nota de verificação de cláusulas contratuais antes de aplicar sequência|MANTER COM AJUSTES
C22|L1-C22-llmops.md|04|P1|MÉDIO|MTTR de 15 min para SEV-1 sem referência ou ressalva de maturidade|Referenciar Google SRE ou DORA; sugerir meta progressiva (4h inicial, 15min em maturidade)|MANTER COM AJUSTES
C22|L1-C22-llmops.md|05|P2|BAIXO|Referência Karpathy "Software 3.0 (palestra, junho 2025)" sem URL verificável|Converter para referência com URL permanente ou substituir por paper equivalente|MANTER COM AJUSTES
C23|L1-C23-alignment.md|01|P0|ALTO|Quadro 23.A mistura dois papers distintos em uma entrada para GRPO (DeepSeekMath e DeepSeek-R1)|Separar em duas referências ou clarificar distinção entre os dois papers na tabela|MANTER COM AJUSTES
C23|L1-C23-alignment.md|02|P1|MÉDIO|Redundância entre seção 23.2 (analogia) e 23.3 (técnica) no mapeamento das três camadas|Condensar seção 23.2 para um parágrafo, eliminar "três lições" explícitas|MANTER COM AJUSTES
C23|L1-C23-alignment.md|03|P1|MÉDIO|Seção 23.4 descreve relação entre capítulos sem entregar instrumentação nova|Transformar em protocolo de escalação quando alignment falha e segurança precisa agir|MANTER COM AJUSTES
C23|L1-C23-alignment.md|04|P1|MÉDIO|Exercício 4 pressupõe quórum executivo indisponível em empresa pequena|Adicionar variante individual/empresa pequena com as quatro perguntas como roteiro solo|MANTER COM AJUSTES
C23|L1-C23-alignment.md|05|P2|BAIXO|Red teaming de Anthropic/OpenAI/DeepMind citado sem referência pública verificável para a cadência|Vincular à Responsible Scaling Policy da Anthropic e ao model card de safety|MANTER COM AJUSTES
C24|L1-C24-governanca.md|01|P0|ALTO|Diagramas 24.2 e 24.3 descritos em texto sem arquivo SVG referenciado|Criar/referenciar SVGs para pirâmide de controles e fluxo de incidente no padrão da obra|MANTER COM AJUSTES
C24|L1-C24-governanca.md|02|P1|MÉDIO|Integração de ética no AI Council de empresa pequena não instrumentada|Adicionar dois mecanismos práticos: pauta fixa de casos limítrofes + consultor externo semestral|MANTER COM AJUSTES
C24|L1-C24-governanca.md|03|P1|MÉDIO|Comunicação externa pré-escrita mencionada como componente mínimo sem template|Adicionar template de comunicação de SEV-1 para decisão automatizada que afetou cliente|MANTER COM AJUSTES
C24|L1-C24-governanca.md|04|P1|MÉDIO|Princípio 8 mencionado cinco vezes sem definição local|Adicionar definição em uma frase na primeira menção|MANTER COM AJUSTES
C24|L1-C24-governanca.md|05|P2|BAIXO|Referência ANPD vaga: "versão corrente verificável em fonte oficial"|Citar documento específico com data e URL|MANTER COM AJUSTES
C25|L1-C25-trade-offs.md|01|P1|ALTO|Diagramas 25.2 (árvore de decisão) e 25.3 (triângulo T4) sem arquivo SVG referenciado|Criar/referenciar SVGs no padrão L1-C43-img-02 e L1-C43-img-03|MANTER COM AJUSTES
C25|L1-C25-trade-offs.md|02|P1|ALTO|Capítulo que se autoproclama "cardápio consultável" não tem tabela-resumo no início|Mover tabela do 25.9 para após a analogia (25.2) como "cardápio rápido de uma página"|MANTER COM AJUSTES
C25|L1-C25-trade-offs.md|03|P1|ALTO|T3 omite vendor lock-in como eixo de decisão — frequentemente o eixo dominante em longo prazo|Adicionar vendor lock-in como quinto eixo no T3 com "quando faz sentido" e "quando é desperdício"|MANTER COM AJUSTES
C25|L1-C25-trade-offs.md|04|P1|MÉDIO|Referência a Brooks (Mythical Man-Month) como "fundamentos do triângulo" imprecisa — triângulo de Brooks é escopo/tempo/custo, não latência/qualidade/custo|Substituir por referência mais direta ou declarar explicitamente como analogia|MANTER COM AJUSTES
C25|L1-C25-trade-offs.md|05|P2|MÉDIO|T5 não aborda HITL em volume de milhões de interações/mês onde HITL pleno é economicamente inviável|Adicionar nota sobre HITL por amostra estatística como solução arquitetural em escala|MANTER COM AJUSTES
