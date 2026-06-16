# BANCA EDITORIAL ADVERSARIAL — APÊNDICES J, K, M, N, O, Q
## Inteligência Aumentada — Os Invariantes
**Data da banca:** junho de 2026
**Bancadores:** Editor-Chefe de Aquisição · Editor de Desenvolvimento · Especialista em IA e Fact-Checking · Leitora Joana

---

# APX-J — Trilha do Número

## RESUMO EXECUTIVO
Nota: 8/10
Veredito: A

## O QUE FUNCIONA
- A distinção estrutural entre "padrão que dura" e "número que muda" é aplicada com consistência rigorosa: preços e benchmarks têm data, fonte e url específicas, o que é raro em obras do gênero.
- A política editorial de "instrumento vivo sem cadência fixa" é honesta e defensável: nega o compromisso que não consegue cumprir, o que é mais respeitável que prometer trimestralidade e não entregar.
- Seção 5 (Incidentes) está acima da média: cada caso vem com "por que importa ao CTO BR", o que converte notícia em aprendizado executivo — exatamente o que a obra promete fazer.
- Seção 4 (Regulação) demonstra profundidade técnica rara: a distinção entre prazo original do AI Act (2026-08-02) e o adiamento do Digital Omnibus (2027-12) está correta e é informação que a maioria dos guias de mercado ignora.
- A nota sobre Claude Mythos como "sinal de fronteira próxima, não opção de adoção" é julgamento editorial sofisticado que protege o leitor de superestimar preview.

## O QUE NÃO FUNCIONA
- A tabela de modelos não tem coluna "data de captura" linha a linha — apenas o cabeçalho geral "junho de 2026". Se um provedor atualiza preço em maio e outro em março, o leitor não sabe qual número é mais stale.
- A afirmação "publicado em Nature em 2025" para o paper DeepSeek-R1 (arxiv.org/abs/2501.12948) precisa de verificação — o paper é originalmente arXiv de janeiro 2025 e "publicado em Nature" exige confirmação de DOI.
- URL do SWE-bench Verified no benchmark aponta para "llm-stats.com/benchmarks/swe-bench-verified", site que não é a fonte primária (fonte primária seria o repositório GitHub de SWE-bench); inconsistência metodológica com as outras linhas que citam fontes primárias.
- A tabela de papers não tem coluna de URL para os papers, apenas para o artigo "Stealing User Prompts" — inconsistência que reduz rastreabilidade de alguns itens.
- Seção de incidentes cita "Chinese state-actor automatizando ataque" sem fonte verificável — diferentemente dos outros 6 incidentes, este não tem data precisa (apenas "2025 a 2026") e não tem referência pública. É o único item da tabela que viola a própria política editorial do apêndice.
- A estatística "AI Incident Database registrou 346 casos em 2025" não tem URL da fonte ao final — cita o nome da base mas não o link, quebrando o padrão dos outros dados.

## ACHADOS

### ACHADO 01
Categoria: P1
Problema: Tabela de modelos sem data de captura por linha — apenas data geral do cabeçalho.
Por que é um problema: Se Claude Opus 4.7 foi verificado em março e DeepSeek em 31/mai, o leitor não sabe qual dado é mais confiável hoje. A própria política do apêndice promete "data de captura" por entrada.
Impacto no leitor: Decisão de compra de API com dado stale sem saber que é stale.
Correção exata: Adicionar coluna "Data verificação" na tabela da Seção 1.
Texto sugerido: Adicionar coluna entre "Release / atualização" e "Fonte" com data de cada verificação de preço.
ROI: ALTO

### ACHADO 02
Categoria: P0
Problema: Afirmação "publicado em Nature em 2025" para DeepSeek-R1 sem DOI confirmado.
Por que é um problema: O paper DeepSeek-R1 (2501.12948) foi publicado no arXiv em janeiro 2025; a publicação em Nature não está confirmada publicamente até junho 2026. Se falsa, é erro factual em seção de papers que é central à credibilidade do apêndice.
Impacto no leitor: CTO que citar essa afirmação em apresentação vai parecer desinformado.
Correção exata: Remover "publicado em Nature em 2025" ou substituir por confirmação de DOI. Se sem confirmação: remover referência ao periódico e manter apenas arXiv.
Texto sugerido: "DeepSeek-AI · janeiro de 2025 · arXiv:2501.12948" — sem menção a Nature até que a publicação em periódico seja confirmada com DOI.
ROI: ALTO

### ACHADO 03
Categoria: P1
Problema: Incidente "Chinese state-actor automatizando ataque" sem fonte pública verificável.
Por que é um problema: Os outros 6 incidentes da tabela têm nome de caso, data e origem verificável. Este item viola a política editorial interna do apêndice ao omitir qualquer referência rastreável.
Impacto no leitor: CTO que citar em conselho será questionado sobre fonte e não terá como responder.
Correção exata: Adicionar fonte pública (ex.: relatório Mandiant, CrowdStrike, CISA, ou artigo jornalístico de referência com data) ou remover o incidente até que a fonte seja identificada.
Texto sugerido: n/a até que fonte primária seja localizada.
ROI: ALTO

### ACHADO 04
Categoria: P1
Problema: URLs de benchmark apontam para sites agregadores não-primários (llm-stats.com, benchlm.ai, artificialanalysis.ai) sem nota sobre curadoria.
Por que é um problema: Artificialanalysis.ai e llm-stats.com são sites de terceiros que podem diferir das fontes primárias (papers originais, repositórios GitHub dos benchmarks). A seção promete "URL do leaderboard onde o número pode ser conferido" mas não distingue leaderboard oficial de agregador.
Impacto no leitor: Leitor que verifica e encontra divergência entre o agregador e a fonte primária perde confiança no apêndice inteiro.
Correção exata: Para cada benchmark, indicar também a fonte primária (ex.: arcprize.org para ARC-AGI-2 já está correto; para GPQA Diamond, o GitHub original é o canonical; para SWE-bench, o swebench.com).
Texto sugerido: Adicionar coluna "Fonte primária" ao lado de "Fonte (leaderboard)".
ROI: MÉDIO

### ACHADO 05
Categoria: P2
Problema: Estatística do AI Incident Database (346 casos em 2025) sem URL da base.
Por que é um problema: Todos os outros dados têm URL. Este é o único número sem referência a aiincidentdatabase.com ou ao report específico.
Impacto no leitor: Inconsistência de padronização; facilmente corrigível.
Correção exata: Adicionar "(fonte: incidentdatabase.ai, relatório anual 2025)" ao final da frase.
Texto sugerido: "AI Incident Database registrou 346 casos em 2025, dos quais 179 foram de mídia sintética e 37 de conteúdo violento ou inseguro (fonte: incidentdatabase.ai, relatório anual 2025)."
ROI: BAIXO

### ACHADO 06
Categoria: P2
Problema: A tabela de papers tem URLs para apenas 7 dos 8 itens — a linha do Survey "Towards a Mechanistic Understanding" tem URL mas a linha de "Thoughtology" também tem, porém falta verificação que todos os URLs estão ativos.
Por que é um problema: Problema menor de manutenção; links de arXiv são estáveis mas merecem verificação na próxima revisão.
Impacto no leitor: Mínimo.
Correção exata: Verificar acessibilidade de todos os URLs na próxima revisão semestral.
Texto sugerido: n/a
ROI: BAIXO

## TESTE DA JOANA
Entenderia: SIM (com ressalvas)
O que ela entenderia: A estrutura de cinco seções está clara. A ideia de "número que expira" versus "padrão que fica" é acessível. As notas de contexto após as tabelas traduzem dados em julgamento — isso Joana aprecia.
O que ela NÃO entenderia: "MoE tiebreak leakage", "attribution graphs", "SaaS multi-tenant" sem glossário. A Seção 3 (papers) pressupõe conhecimento de arquitetura que Joana não tem.
Como corrigir: Adicionar 1 linha de "tradução executiva" em cada paper da Seção 3, similar ao campo "Por que importa" já existente — mas escrita para não-técnico.

## TESTE DE DURABILIDADE
Classificação: MÉDIA
2 anos: Alta — estrutura e política editorial sobrevivem; apenas dados mudam.
5 anos: Baixa — todos os números estarão obsoletos; o valor residual é o método de rastreabilidade.
10 anos: Muito baixa — apenas a arquitetura da seção tem valor como modelo.
Justificativa: O próprio apêndice admite isso. O risco é que revisões atrasadas deixem o apêndice com data de "junho 2026" sem atualização visível, o que é pior do que ausência do apêndice.

## TESTE DE DIFERENCIAÇÃO
Classificação: PROPRIEDADE INTELECTUAL
Justificativa: Nenhum outro livro de IA de negócios em português tem apêndice rastreável com data de captura por linha, política editorial declarada, e convite público a contribuições. A combinação de instrumento vivo + log de revisão + repositório público é diferenciador real de PI.

## TESTE DE MEMORIZAÇÃO
Ideia principal clara? SIM
Qual é a ideia principal: "O número tem prazo de validade; aqui está o número com data, fonte e método para você auditá-lo."
Justificativa: A frase do cabeçalho "instrumento vivo" e a estrutura de cinco seções datadas tornam a proposta memorável.

## TESTE DE TRANSFORMAÇÃO
Ao terminar, o leitor consegue fazer o que antes não conseguia:
- Consultar preço de inferência dos 8 principais provedores com data de referência, sem busca no Google.
- Identificar qual benchmark é relevante para qual tipo de tarefa (código, matemática, raciocínio científico).
- Citar incidente de segurança real com nome, data e implicação executiva.
- Entender o estado atual da regulação europeia e brasileira com precisão de datas.

## NOTA FINAL
Estrutura: 9 | Pedagogia: 7 | Clareza: 8 | Autoridade: 8 | Durabilidade: 5 | Diferenciação: 9 | Memorização: 8 | Transformação: 8
**Nota Geral: 8**

## DECISÃO EDITORIAL
MANTER COM AJUSTES

---

## LINHAS-TRACKER
```
APX-J|L1-APX-J-trilha-do-numero.md|01|P1|ALTO|Tabela de modelos sem data de captura por linha|Adicionar coluna Data verificação na tabela da Seção 1|MANTER COM AJUSTES
APX-J|L1-APX-J-trilha-do-numero.md|02|P0|ALTO|Afirmação "publicado em Nature em 2025" para DeepSeek-R1 sem DOI confirmado|Remover referência a Nature ou confirmar com DOI|MANTER COM AJUSTES
APX-J|L1-APX-J-trilha-do-numero.md|03|P1|ALTO|Incidente Chinese state-actor sem fonte pública verificável|Adicionar fonte pública ou remover o incidente|MANTER COM AJUSTES
APX-J|L1-APX-J-trilha-do-numero.md|04|P1|MÉDIO|URLs de benchmark apontam para agregadores sem nota de curadoria|Indicar também fonte primária de cada benchmark|MANTER COM AJUSTES
APX-J|L1-APX-J-trilha-do-numero.md|05|P2|BAIXO|Estatística AI Incident Database sem URL|Adicionar URL da fonte ao final da frase|MANTER COM AJUSTES
APX-J|L1-APX-J-trilha-do-numero.md|06|P2|BAIXO|Links de arXiv não verificados para acessibilidade|Verificar todos os URLs na próxima revisão|MANTER COM AJUSTES
```

---

# APX-K — Gabaritos Comentados

## RESUMO EXECUTIVO
Nota: 5/10
Veredito: C

## O QUE FUNCIONA
- A instrução de uso está correta pedagogicamente: "faça o exercício primeiro", "compare estrutura, não conteúdo", "customize ao seu domínio". Isso é o oposto de atalho e alinha com a tese da obra.
- Os critérios de qualidade dos projetos (ex.: "outro engenheiro lê e roda eval sem perguntar mais que três coisas") são testáveis e específicos — muito acima do padrão de gabaritos genéricos.
- O critério do projeto de LLMOps ("outro engenheiro responde sem perguntar qualquer das sete perguntas executivas") operacionaliza a ideia de transferência de conhecimento de forma verificável.

## O QUE NÃO FUNCIONA
- O apêndice é drasticamente raso: cada "gabarito" tem entre 1 e 5 linhas para exercícios que, segundo o próprio Manual do Professor (APX-Q), exigem "5 a 8 linhas por exercício com critério de correção, armadilhas comuns e pontuação sugerida". O APX-Q admite isso explicitamente ("gabarito completo está em construção"), mas o leitor que comprou o livro hoje recebe algo incompleto.
- Não há referência cruzada explícita entre os gabaritos e os capítulos. O leitor não sabe se "Projeto — Caderno de RAG" corresponde ao capítulo C06 ou C07 sem consultar o sumário.
- Os gabaritos de projetos (vs. exercícios) não têm critério de avaliação — apenas descrevem a estrutura de entrega. Isso diferencia "estrutura do que entregar" de "rubrica de como avaliar", e a rubrica está ausente em todos os projetos.
- Faltam gabaritos para capítulos que têm exercícios nos capítulos: RAG (C06), Fine-tuning (C08), Reasoning (C10), Agentes (C12-13), AI Engineering (C14), Posicionamento de Mercado (C15-16), LLMOps (C22), Alignment (C23). O APX-K cobre no máximo 60% dos capítulos que têm exercícios, sem declarar que o restante não foi incluído.
- A seção de Tokens tem apenas o projeto, sem gabarito do Exercício 1 — que é mencionado no APX-Q como um dos entregáveis intermediários mais importantes (aula 2 do plano de 60h).
- Ausência de gabaritos para exercícios numerados de Agentes, Fine-tuning, Reasoning, Posicionamento — todos com exercícios nos capítulos mas sem solução estruturada aqui.

## ACHADOS

### ACHADO 01
Categoria: P0
Problema: O apêndice é incompleto e não declara isso ao leitor.
Por que é um problema: O APX-Q, escrito pelo mesmo autor, admite que "o gabarito completo está em construção". O leitor do APX-K não sabe disso — o apêndice se apresenta como "Gabaritos Comentados" completos, sem advertência de que cobre menos de 60% dos capítulos com exercícios.
Impacto no leitor: Estudante que tenta usar o apêndice para autoavaliação encontra ausência para metade dos capítulos sem explicação — experiência de frustração que erode confiança na obra.
Correção exata: Adicionar nota editorial no início do apêndice declarando quais capítulos têm gabarito e quais estão pendentes, com link para o repositório onde o restante será publicado.
Texto sugerido: "> **Nota editorial (junho 2026):** este apêndice cobre atualmente os gabaritos dos exercícios e projetos dos capítulos listados abaixo. Gabaritos dos capítulos C08 (Fine-tuning), C10 (Reasoning), C12-C13 (Agentes), C14 (AI Engineering), C15-C16 (Posicionamento), C22 (LLMOps) e C23 (Alignment) estão em construção e serão publicados no repositório acompanhante à medida que forem finalizados. Ative *watch* no repositório para receber notificação."
ROI: ALTO

### ACHADO 02
Categoria: P1
Problema: Gabaritos de projetos descrevem estrutura de entrega mas não rubrica de avaliação.
Por que é um problema: O leitor que está se autoavaliando precisa saber se errou, não apenas o que deveria ter entregado. Um gabarito que diz "critério de qualidade: outro executivo defende a arquitetura" é critério de aprovação, não rubrica de avaliação. Não há escala de proficiência.
Impacto no leitor: Estudante não consegue distinguir entrega medíocre de entrega excelente usando apenas este apêndice.
Correção exata: Para cada projeto, adicionar 3 linhas de rubrica: (a) entrega insuficiente, (b) entrega proficiente, (c) entrega excelente — espelhando a estrutura da rubrica do APX-Q.
Texto sugerido: n/a (requer reescrita projeto a projeto).
ROI: MÉDIO

### ACHADO 03
Categoria: P1
Problema: Ausência de referências cruzadas com capítulos — o leitor não sabe de onde vêm os exercícios.
Por que é um problema: O título de cada seção (ex.: "RAG", "Evals") não inclui o número do capítulo. Em obra com 28 capítulos, isso força navegação desnecessária.
Impacto no leitor: Professor que monta plano de aula tem dificuldade de acoplar APX-K ao plano do APX-Q.
Correção exata: Adicionar referência de capítulo a cada título de seção: "RAG (C06)" em vez de apenas "RAG".
Texto sugerido: Substituir todos os títulos de seção no formato "## RAG" por "## RAG — Capítulo 06".
ROI: BAIXO

### ACHADO 04
Categoria: P2
Problema: Gabarito de "Roadmap pessoal" tem critério ("diretoria aprova o roadmap em uma reunião") que não é auditável por autoavaliação individual.
Por que é um problema: Se o leitor está em autoestudo, não tem diretoria disponível para aprovar o roadmap. O critério externo não funciona para o uso principal do apêndice.
Impacto no leitor: Leitor individual não consegue usar este gabarito para autoavaliação.
Correção exata: Adicionar critério alternativo para autoavaliação: "Ou, para autoestudo: o roadmap tem três marcos com data, métricas de sucesso e dependências explícitas."
Texto sugerido: Adicionar ao final da seção "Roadmap pessoal": "Para autoavaliação individual: o roadmap tem datas fixas, três marcos verificáveis, uma métrica de sucesso por marco, e lista de dependências entre eles."
ROI: BAIXO

## TESTE DA JOANA
Entenderia: NÃO (para a maioria das seções)
O que ela entenderia: A instrução de uso inicial é clara. O critério do projeto de Governança ("outro executivo responde sem ambiguidade") é acessível.
O que ela NÃO entenderia: "LLM-as-judge calibrado com correlação igual ou superior a 0,7 contra humano" (seção Evals) sem o contexto do capítulo é opaco. "Golden set de 30 a 50 itens" sem exemplificação é abstrato demais.
Como corrigir: Adicionar 1 exemplo concreto por seção que traduza o critério técnico em linguagem de negócio.

## TESTE DE DURABILIDADE
Classificação: ALTA
2 anos / 5 anos / 10 anos: Alta em todos os horizontes.
Justificativa: Gabaritos são de método, não de ferramenta. Nenhum item vai envelhecer com lançamentos de modelos. O risco é incompletude, não obsolescência.

## TESTE DE DIFERENCIAÇÃO
Classificação: COMMODITY (no estado atual)
Justificativa: No estado atual, os gabaritos são rasos e cobrem menos da metade dos exercícios. Um gabarito com 3 linhas por projeto é equiparável ao que qualquer outro livro de referência entrega. Se o repositório completar o restante, a classificação sobe para DIFERENCIADO.

## TESTE DE MEMORIZAÇÃO
Ideia principal clara? SIM
Qual é a ideia principal: "O gabarito mostra o método de pensar, não a resposta certa."
Justificativa: A instrução de uso comunica isso bem. O problema é que o conteúdo não honra a promessa — é raso demais para demonstrar o método de pensar em profundidade.

## TESTE DE TRANSFORMAÇÃO
Ao terminar, o leitor consegue fazer o que antes não conseguia:
- Verificar se sua estrutura de resposta segue a arquitetura esperada (para os capítulos cobertos).
- Calibrar se o projeto de Evals atinge o critério mínimo de qualidade.
- Identificar se o caderno de governança tem RACI e patrocinador explícito.
- (Para capítulos não cobertos — Agentes, Fine-tuning, Reasoning — não há transformação mensurável com o apêndice atual.)

## NOTA FINAL
Estrutura: 5 | Pedagogia: 6 | Clareza: 7 | Autoridade: 5 | Durabilidade: 9 | Diferenciação: 4 | Memorização: 7 | Transformação: 5
**Nota Geral: 5**

## DECISÃO EDITORIAL
REVISAR PARCIALMENTE

---

## LINHAS-TRACKER
```
APX-K|L1-APX-K-gabaritos.md|01|P0|ALTO|Apêndice incompleto sem declarar isso ao leitor — cobre menos de 60% dos capítulos com exercícios|Adicionar nota editorial com lista de capítulos cobertos e link para repositório|REVISAR PARCIALMENTE
APX-K|L1-APX-K-gabaritos.md|02|P1|MÉDIO|Gabaritos de projetos sem rubrica de avaliação — apenas critério pass/fail|Adicionar escala de proficiência por projeto (insuficiente/proficiente/excelente)|REVISAR PARCIALMENTE
APX-K|L1-APX-K-gabaritos.md|03|P1|BAIXO|Ausência de referências cruzadas com capítulos nos títulos de seção|Adicionar número do capítulo a cada título de seção|REVISAR PARCIALMENTE
APX-K|L1-APX-K-gabaritos.md|04|P2|BAIXO|Critério de roadmap depende de aprovação por diretoria — inutilizável em autoestudo|Adicionar critério alternativo para autoavaliação individual|MANTER COM AJUSTES
```

---

# APX-M — Síntese: Os Nove Princípios em Uma Página

## RESUMO EXECUTIVO
Nota: 9/10
Veredito: A

## O QUE FUNCIONA
- A síntese em uma página é genuinamente utilizável — o formato com título, mecânica e violação típica por princípio é denso sem ser hermético.
- As frases de cada princípio são citáveis e memoráveis: "O meio do contexto é onde a informação vai morrer" e "IA sem eval é fé, não engenharia" são ao nível da régua de comparação (Thinking Fast and Slow tem frases assim). São candidatas fortes a passar no teste de citabilidade.
- A tabela "Como usar" com situação → princípio é diferenciador real: transforma a síntese de leitura passiva em ferramenta de checklist situacional. Executivo que imprime e usa em reunião vai notar que a tabela é o ativo mais útil do apêndice.
- A ressalva sobre Princípios 1 e 2 (dependência de arquitetura generativa atual) é intelectualmente honesta e rara: o autor sinaliza onde a própria obra pode envelhecer.
- "Distribuição livre com atribuição" é decisão estratégica inteligente — aumenta alcance viral do conteúdo.

## O QUE NÃO FUNCIONA
- O manifesto não tem título explícito "Manifesto" — o título é "Síntese: Os Nove Princípios em Uma Página". O apêndice é referenciado no sumário e em outros apêndices como "manifesto" e "manifesto de bolso", mas o documento não usa essa palavra internamente. Inconsistência de nomenclatura.
- O Princípio 4 (Encaixe) tem mecânica com problema sintático: "o modelo decide-se por eixo, código, matemática, multimodal, contexto longo, custo, não pelo lançamento da semana" — a lista não diferencia claramente que "custo" é eixo transversal enquanto os outros são domínios de tarefa. Isso pode confundir ao ser lido isoladamente do capítulo.
- A frase-síntese "Modelos passam. Método fica." aparece em destaque de heading (`## *Modelos passam. Método fica.*`), mas o Manifesto é o único lugar na obra onde seria natural uma versão estendida de 3-4 linhas do argumento central — e isso está ausente. A frase sozinha é correta mas deixa de aproveitar o momento.
- A instrução "Imprima. Cole na parede. Distribua ao time." no subtítulo sugere uso em papel, mas o apêndice não vem formatado para impressão A4 ou A3 — a tabela "Como usar" com 6 linhas pode quebrar em impressão de formato padrão.

## ACHADOS

### ACHADO 01
Categoria: P1
Problema: Inconsistência de nomenclatura entre "Síntese" (título interno) e "Manifesto de Bolso" (referência nos outros apêndices e sumário).
Por que é um problema: Leitor que busca o "manifesto" pode não associar imediatamente ao apêndice M. Piora a navegabilidade da obra.
Impacto no leitor: Confusão em leitura não linear (que é o modo dominante de ebooks executivos).
Correção exata: Ajustar o subtítulo ou o título para incluir "Manifesto" como termo-âncora.
Texto sugerido: "# Apêndice M — Manifesto de Bolso: Os Nove Princípios em Uma Página"
ROI: MÉDIO

### ACHADO 02
Categoria: P2
Problema: Mecânica do Princípio 4 mistura eixos de tarefa com eixo de custo sem distinção.
Por que é um problema: Lido isoladamente do capítulo, o leitor pode entender que "custo" é mais um eixo de domínio como código ou matemática — mas custo é transversal, não domínio.
Impacto no leitor: Uso incorreto do princípio na prática de seleção de modelo.
Correção exata: Separar custo dos eixos de domínio: "o modelo decide-se por eixo de tarefa (código, matemática, multimodal, contexto longo) e por custo agregado, nunca pelo lançamento da semana."
Texto sugerido: *Mecânica:* o modelo decide-se por eixo de tarefa — código, matemática, multimodal, contexto longo — ponderado por custo composto, nunca pelo lançamento da semana.
ROI: BAIXO

### ACHADO 03
Categoria: P2
Problema: Frase-síntese apresentada isolada sem versão estendida — oportunidade desperdiçada no momento de maior impacto emocional do apêndice.
Por que é um problema: Em livros da régua de comparação (Thinking Fast and Slow, Superforecasting), a frase central tem expansão de 2-3 linhas que ancora o leitor. Aqui, a frase está solta.
Impacto no leitor: Momento de fechamento que poderia ser memorável é subaproveitado.
Correção exata: Adicionar 2-3 linhas de expansão abaixo da frase-síntese.
Texto sugerido: > *Modelos passam. Método fica.*
>
> O modelo que lidera hoje o benchmark será ultrapassado no próximo trimestre. A capacidade de escolher com critério, avaliar com método, governar com responsabilidade e aprender continuamente — essa não envelhece. É o que a obra inteira treina.
ROI: MÉDIO

## TESTE DA JOANA
Entenderia: SIM
O que ela entenderia: Cada princípio com sua frase, mecânica e violação típica é acessível. A tabela "Como usar" é exatamente o nível de diretividade que Joana precisa.
O que ela NÃO entenderia: "Q/K/V" referenciado no APX-K (mas não aqui). Neste apêndice especificamente, Joana entende tudo — é o melhor apêndice do ponto de vista de acessibilidade executiva.
Como corrigir: Nenhuma ação necessária para Joana neste apêndice.

## TESTE DE DURABILIDADE
Classificação: ALTA
2 anos / 5 anos / 10 anos: Alta em todos os horizontes.
Justificativa: A ressalva do próprio apêndice é correta — Princípios 1 e 2 dependem de arquitetura generativa e podem mudar. Os outros sete são de prática profissional e duram indefinidamente. Nenhum número, nome de modelo ou preço aparece aqui.

## TESTE DE DIFERENCIAÇÃO
Classificação: PROPRIEDADE INTELECTUAL
Justificativa: A combinação de nove princípios com frases memoráveis, mecânica operacional e violação típica, em uma única página, é o destilado da voz autoral da obra. Não existe equivalente em livros concorrentes no mercado brasileiro. Tem potencial de virar citação em apresentações de diretoria — que é exatamente o que propriedade intelectual faz.

## TESTE DE MEMORIZAÇÃO
Ideia principal clara? SIM
Qual é a ideia principal: "Nove princípios que governam a prática profissional em IA — imprimíveis, verificáveis, duráveis."
Justificativa: A seleção de 9 (nem 7, nem 12) princípios, com frase única por princípio, otimiza para memorização por limitação cognitiva intencional.

## TESTE DE TRANSFORMAÇÃO
Ao terminar, o leitor consegue fazer o que antes não conseguia:
- Passar de leitura da obra inteira para referência rápida de checklist situacional.
- Usar a tabela "Como usar" como protocolo de decisão em reunião de IA sem abrir o livro.
- Distribuir o apêndice ao time como vocabulário comum sem precisar fazer apresentação completa da obra.
- Identificar qual princípio está sendo violado em uma situação concreta, em 30 segundos.

## NOTA FINAL
Estrutura: 9 | Pedagogia: 9 | Clareza: 9 | Autoridade: 9 | Durabilidade: 10 | Diferenciação: 9 | Memorização: 10 | Transformação: 9
**Nota Geral: 9**

## DECISÃO EDITORIAL
MANTER COM AJUSTES

---

## LINHAS-TRACKER
```
APX-M|L1-APX-M-manifesto-bolso.md|01|P1|MÉDIO|Inconsistência de nomenclatura entre Síntese (título interno) e Manifesto de Bolso (referências externas)|Ajustar título para incluir "Manifesto de Bolso" como termo-âncora|MANTER COM AJUSTES
APX-M|L1-APX-M-manifesto-bolso.md|02|P2|BAIXO|Mecânica do Princípio 4 mistura eixos de tarefa com custo sem distinção clara|Separar custo dos eixos de domínio na descrição da mecânica|MANTER COM AJUSTES
APX-M|L1-APX-M-manifesto-bolso.md|03|P2|MÉDIO|Frase-síntese sem expansão no momento de maior impacto emocional do apêndice|Adicionar 2-3 linhas de expansão da tese central abaixo da frase|MANTER COM AJUSTES
```

---

# APX-N — Metodológico, sobre os números deste livro

## RESUMO EXECUTIVO
Nota: 8/10
Veredito: A

## O QUE FUNCIONA
- A taxonomia de quatro tipos (A — Fonte necessária, B — Exemplo composto, C — Auto-evidente, D — Estimativa honesta) é metodologicamente rigorosa e original. É o tipo de estrutura que separa obra acadêmica de obra de divulgação — e esta obra escolhe operar com rigor acadêmico de forma executivamente legível.
- A declaração explícita de que "Nenhuma afirmação de validação por NDA até que efetivamente exista NDA com cliente real" (Tipo B) é incomum em honestidade — a maioria dos livros de negócios inventa case studies sem essa ressalva.
- A tabela de cadência de revisão (Seção 4) é artefato de gestão editorial útil e publicável — raramente se vê isso em obra técnica. Eleva a credibilidade da obra como instrumento gerenciado.
- A distinção entre "50-5000 colaboradores" e "operação em setor criticamente regulado" como critério de escopo para uso do caderno (APX-O) tem aqui sua justificativa metodológica — os dois apêndices se reforçam bem.
- A referência ao repositório "auditoria-quantitativa-l1.md" como artefato público de auditoria linha a linha é diferenciador real.

## O QUE NÃO FUNCIONA
- A Seção 5 afirma que "foram identificadas aproximadamente noventa afirmações quantitativas relevantes" e lista contagem por tipo (18+24+31+14=87, não 90). A inconsistência entre "aproximadamente noventa" e o somatório de 87 é pequena mas capturável por crítico.
- O repositório referenciado como "auditoria-quantitativa-l1.md" não tem URL neste apêndice — em contraste com o APX-J que cita repositório com URL completo. Inconsistência de padrão.
- A Seção 6 argumenta por que o livro não cita fonte inline em todos os números — argumento válido mas que ficaria mais forte se listasse os "15 a 20 casos" de nota de rodapé existentes em forma de tabela de referência rápida, em vez de apenas declarar que eles existem.
- A "próxima revisão: anual" declarada no header conflita com a "revisão programada: junho de 2027" do footer — são consistentes em conteúdo (anual a partir de junho 2026 = junho 2027) mas a apresentação redundante cria a impressão de duas políticas.
- A Seção 2 usa a expressão "o livro inteiro opera sobre os Nove Princípios da obra" indiretamente — mas não há referência explícita a qual Framework governa a Camada Dupla epistemológica. O leitor que leu o APX-N antes do corpo do livro não tem âncora.

## ACHADOS

### ACHADO 01
Categoria: P1
Problema: Inconsistência entre "aproximadamente noventa afirmações" (texto) e soma de 87 na tabela da Seção 5.
Por que é um problema: Pequena mas detectável por qualquer leitor que some as colunas. Erode credibilidade precisamente no apêndice que trata de rigor quantitativo.
Impacto no leitor: Especialista em IA ou fact-checker que lê este apêndice primeiro e encontra essa inconsistência vai questionar a acurácia de todo o restante.
Correção exata: Ajustar o texto de "aproximadamente noventa" para "aproximadamente oitenta e sete" ou revisar a tabela para chegar a 90 com mais precisão.
Texto sugerido: "A varredura identificou oitenta e sete afirmações quantitativas relevantes no corpo dos capítulos, frameworks e apêndices (18 Tipo A + 24 Tipo B + 31 Tipo C + 14 Tipo D)."
ROI: ALTO

### ACHADO 02
Categoria: P1
Problema: Repositório "auditoria-quantitativa-l1.md" sem URL — inconsistência com o padrão do APX-J que cita URLs completos.
Por que é um problema: Leitor que quer auditar não tem como chegar ao artefato sem ir ao repositório raiz e procurar o arquivo manualmente.
Impacto no leitor: Proposta de transparência fica incompleta. O diferenciador da obra (auditabilidade pública) não funciona sem o link.
Correção exata: Adicionar URL completo ao arquivo de auditoria no repositório, no formato dos outros links da obra.
Texto sugerido: "...pode consultar o documento `auditoria-quantitativa-l1.md` no repositório em [github.com/falercia/inteligencia-aumentada-recursos/blob/main/auditoria-quantitativa-l1.md](https://github.com/falercia/inteligencia-aumentada-recursos/blob/main/auditoria-quantitativa-l1.md), atualizado a cada revisão do manuscrito."
ROI: MÉDIO

### ACHADO 03
Categoria: P2
Problema: Header e footer com declarações de revisão redundantes e potencialmente confusas.
Por que é um problema: Header diz "Próxima revisão: anual"; footer diz "Próxima revisão programada: junho de 2027". São equivalentes mas o leitor tem que fazer a conta. Para leitor em 2028 que encontra o apêndice, a data "junho de 2027" no footer vai parecer revisão atrasada.
Impacto no leitor: Ambiguidade sobre se a revisão ocorreu ou não.
Correção exata: Unificar em um único campo: "Atualizado em: junho de 2026. Próxima revisão programada: junho de 2027."
Texto sugerido: Remover a linha do footer e manter apenas o header com data atualizada a cada revisão.
ROI: BAIXO

### ACHADO 04
Categoria: P2
Problema: Seção 6 declara existência de "15 a 20 casos" de nota de rodapé sem listá-los — oportunidade de ancoragem que não é aproveitada.
Por que é um problema: Leitor que acabou de ler a justificativa de por que existem notas de rodapé quer saber quais são. Sem a lista, a declaração é autocertificação sem verificabilidade.
Impacto no leitor: Leitor não consegue verificar se os 15-20 casos anunciados realmente existem, ou se estão todos presentes.
Correção exata: Adicionar tabela de referência rápida dos 15-20 casos de Tipo A com nota de rodapé: capítulo, afirmação e link.
Texto sugerido: "Ver tabela completa em `auditoria-quantitativa-l1.md` no repositório — coluna 'Tipo A com nota de rodapé'."
ROI: BAIXO

## TESTE DA JOANA
Entenderia: SIM (parcialmente)
O que ela entenderia: A distinção entre Tipo A, B, C e D com os exemplos. A ideia de "número que expira" vs. "padrão que dura". A tabela de cadência de revisão.
O que ela NÃO entenderia: "Postura epistemológica", "piso epistemológico", "afirmação categórica que sustenta tese estrutural" — linguagem acadêmica que não é traduzida para o executivo. Joana pode pular a Seção 2 sem perder valor prático.
Como corrigir: Adicionar linha de "tradução executiva" no início da Seção 2: "Em linguagem direta: explicamos aqui de onde vieram os números do livro e como cada um deve ser lido."

## TESTE DE DURABILIDADE
Classificação: ALTA
2 anos / 5 anos / 10 anos: Alta em todos os horizontes.
Justificativa: O apêndice é sobre metodologia de rastreamento, não sobre o conteúdo rastreado. A metodologia de quatro tipos não envelhece. A tabela de cadência de revisão pode ser expandida em edições futuras sem reescrever a estrutura.

## TESTE DE DIFERENCIAÇÃO
Classificação: PROPRIEDADE INTELECTUAL
Justificativa: Nenhum livro de IA de negócios em português tem apêndice metodológico declarando postura epistemológica, taxonomia de afirmações e cadência de revisão por número. Isso é procedimento científico aplicado ao livro de negócios — diferenciador real de PI que a obra deve explorar em marketing.

## TESTE DE MEMORIZAÇÃO
Ideia principal clara? SIM
Qual é a ideia principal: "Saiba de onde veio cada número e como ele envelhece — a metodologia está aqui, auditável."
Justificativa: A taxonomia de quatro tipos é memorável como estrutura. O leitor que a internalizou vai aplicá-la para avaliar outros livros de IA.

## TESTE DE TRANSFORMAÇÃO
Ao terminar, o leitor consegue fazer o que antes não conseguia:
- Classificar qualquer afirmação quantitativa em uma das quatro categorias (A, B, C, D) e saber qual tratamento editorial esperar.
- Identificar que número do livro exige verificação antes de citar em apresentação (Tipo A com link) vs. qual é estrutural e não precisa (Tipo C).
- Auditar a cadência de revisão dos números mais voláteis da obra.
- Avaliar outros livros de IA pela mesma metodologia — transferência de competência genuína.

## NOTA FINAL
Estrutura: 9 | Pedagogia: 8 | Clareza: 7 | Autoridade: 9 | Durabilidade: 10 | Diferenciação: 9 | Memorização: 8 | Transformação: 8
**Nota Geral: 8**

## DECISÃO EDITORIAL
MANTER COM AJUSTES

---

## LINHAS-TRACKER
```
APX-N|L1-APX-N-metodologico-numeros.md|01|P1|ALTO|Inconsistência entre "aproximadamente noventa" no texto e soma de 87 na tabela da Seção 5|Corrigir texto para 87 ou revisar tabela para totalizar 90|MANTER COM AJUSTES
APX-N|L1-APX-N-metodologico-numeros.md|02|P1|MÉDIO|Repositório auditoria-quantitativa-l1.md sem URL completo — inconsistência com padrão do APX-J|Adicionar URL completo para o arquivo de auditoria no repositório|MANTER COM AJUSTES
APX-N|L1-APX-N-metodologico-numeros.md|03|P2|BAIXO|Header e footer com declarações de revisão redundantes e potencialmente confusas|Unificar em campo único no header com data atualizada a cada revisão|MANTER COM AJUSTES
APX-N|L1-APX-N-metodologico-numeros.md|04|P2|BAIXO|Seção 6 declara 15-20 notas de rodapé sem listá-las — autocertificação sem verificabilidade|Adicionar referência à tabela de Tipo A no repositório|MANTER COM AJUSTES
```

---

# APX-O — Caderno de Governança de IA

## RESUMO EXECUTIVO
Nota: 9/10
Veredito: A+

## O QUE FUNCIONA
- A separação explícita entre "ficha conceitual no livro" e "caderno executável no repositório" é a decisão arquitetural mais inteligente da obra inteira. Materializa o Princípio 3 (Camada Dupla) no próprio artefato que ensina o Princípio 3. É recursividade intelectual que vai além do que a maioria dos livros de gestão consegue.
- A anatomia de seis blocos com justificativa de posição é superior à média de frameworks de governança publicados. A frase "sem RACI específico não há decisão rastreável, e sem plano de incidente assinado não há resposta calibrada" é nível de precisão executiva que a régua de comparação exige.
- Os dez anti-padrões da tabela são concretos, verificáveis e cirúrgicos. "Teatro de compliance" versus "ausência declarada de governança" é distinção que a maioria dos frameworks de mercado evita fazer — este apêndice a faz com clareza.
- Os sete indicadores quantitativos de "caderno vivo versus caderno morto" são o activo de maior valor de PI do apêndice: "12 atas no ano, sem ausência maior que 45 dias", "crescimento mínimo de 0,5 ponto na escala de 0 a 4 por ano até atingir 3,0 médio". São métricas de gestão operacionalizáveis que nenhum framework concorrente (NIST AI RMF, ISO 42001, EU AI Act) entrega em linguagem executiva.
- A tabela "Quando adotar vs. quando exige adendo" é artefato de navegação raramente encontrado em frameworks de governança — resolve um problema real de "isso é para mim?" com precisão de critérios.
- Os sete padrões de adaptação são concretos sem serem prescritivos demais. "AUP com exemplo de ferramenta real" vs. "AUP genérica que não orienta" é julgamento editorial que vai contra o padrão do mercado de templates genéricos.

## O QUE NÃO FUNCIONA
- O quadro de orientação "onde vive o quê" cita três camadas de conhecimento mas não alinha explicitamente com a taxonomia do APX-N. Leitor que leu o APX-N antes espera ver "Tipo A / B / C / D" — a terminologia diverge sem motivo aparente.
- O número de "dez controles canônicos" é citado múltiplas vezes (no Bloco 4 da anatomia, nos anti-padrões, nos indicadores) mas os controles nunca são nomeados ou numerados na ficha conceitual. O leitor que não tem acesso ao repositório no momento da leitura não sabe quais são os dez controles.
- O "repositório acompanhante" (github.com/falercia/inteligencia-aumentada-recursos/tree/main/governance/v1) é citado três vezes com URL completo — redundância benign mas que ocupa espaço que poderia ser usado para listar ao menos os nomes dos dez controles.
- A frase "caderno de cerca de seis páginas" no final da seção de anatomia é a única estimativa de tamanho do artefato — e pode criar expectativa errada se o caderno executável tiver divergido.
- O critério "cinquenta e cinco mil colaboradores" na seção "Quando adotar" é ambiguamente escrito — "entre cinquenta e cinco mil" sem vírgula pode ser lido como "entre 55 mil" ou "entre 50 e 5000". O texto clarifica na tabela ("50 e 5000") mas a frase de abertura é um erro tipográfico potencial.
- Os sete padrões de adaptação numerados de 1 a 7 não têm título curto — são textos corridos. Para uma ficha de referência que o executivo vai usar em reunião, títulos curtos melhorariam scanabilidade (ex.: "1. Patrocinador nominal", "2. Princípios com vocabulário próprio").

## ACHADOS

### ACHADO 01
Categoria: P0
Problema: Os "dez controles canônicos" são citados repetidamente mas nunca nomeados na ficha conceitual — leitor sem acesso ao repositório não sabe quais são.
Por que é um problema: A ficha promete ser suficiente para "entender o método" e "defender a estrutura diante de auditoria externa". Sem saber quais são os dez controles, o executivo não consegue defender o caderno — precisa do repositório, que a ficha diz ser opcional.
Impacto no leitor: Executivo que leva o livro a uma reunião de board e é perguntado "quais são os dez controles?" não tem resposta sem o laptop aberto no repositório.
Correção exata: Adicionar tabela com os nomes dos dez controles na ficha conceitual, sem o detalhe de cada um (que fica no repositório), mas com nome e função em uma linha cada.
Texto sugerido: Adicionar seção "Os dez controles em uma linha" entre a anatomia dos seis blocos e os nove princípios, com tabela de nome do controle e função resumida.
ROI: ALTO

### ACHADO 02
Categoria: P1
Problema: Ambiguidade tipográfica "cinquenta e cinco mil" vs. "entre cinquenta e cinco mil colaboradores" na seção de escopo.
Por que é um problema: Na frase de abertura da seção "Quando adotar este modelo", o texto diz "para organização brasileira entre cinquenta e cinco mil colaboradores" — sem vírgula, lê-se "55.000 colaboradores" em vez de "50 a 5.000 colaboradores". A tabela abaixo corrige mas a frase é a primeira que o leitor lê.
Impacto no leitor: Empresa de 500 colaboradores que lê a frase e interpreta "55 mil" acha que o caderno não é para ela e pula o apêndice.
Correção exata: Adicionar vírgula ou reformular: "para organização brasileira entre cinquenta e cinco mil colaboradores".
Texto sugerido: "O caderno foi calibrado para organização brasileira entre 50 e 5.000 colaboradores (ou, por extenso: entre cinquenta e cinco mil colaboradores), com uso de IA em produção em pelo menos um caso de uso material."
ROI: ALTO

### ACHADO 03
Categoria: P1
Problema: Os sete padrões de adaptação numerados sem título curto — reduz scanabilidade para uso em reunião.
Por que é um problema: A ficha é descrita como instrumento de uso em reunião e auditoria. Padrões sem título curto forçam leitura linear quando o executivo precisa de referência rápida.
Impacto no leitor: Em uso real de referência rápida, executivo não consegue encontrar o padrão 5 sem ler os quatro anteriores.
Correção exata: Adicionar título curto em negrito antes de cada padrão (o primeiro já tem: "Patrocinador executivo nomeado, não apenas o cargo" — é quase um título mas está no corpo da frase).
Texto sugerido: Reformatar cada padrão como "**TÍTULO CURTO.** Descrição completa." — ex.: "**1. Patrocinador nominal.** O caderno exige nome próprio na linha de patrocinador..."
ROI: MÉDIO

### ACHADO 04
Categoria: P2
Problema: O quadro de orientação "onde vive o quê" não alinha com a taxonomia do APX-N (Tipos A, B, C, D).
Por que é um problema: Para leitor que leu o APX-N, a terminologia "camada do conhecimento" aqui diverge sem motivo. A integração entre os dois apêndices ficaria mais forte com referência explícita.
Impacto no leitor: Leitor que tenta integrar os dois apêndices tem trabalho adicional de mapeamento mental.
Correção exata: Adicionar nota ao pé do quadro: "Esta estrutura de camadas materializa o Tipo C (padrão durável no livro) e o Tipo A (número datado no repositório) da taxonomia do Apêndice N."
Texto sugerido: n/a (nota de rodapé de uma linha é suficiente).
ROI: BAIXO

### ACHADO 05
Categoria: P2
Problema: URL do repositório citado três vezes no mesmo apêndice — redundância que ocupa espaço.
Por que é um problema: Problema cosmético; o espaço poderia ser usado para listar os nomes dos dez controles (Achado 01).
Impacto no leitor: Mínimo.
Correção exata: Na segunda e terceira citação do URL, substituir por referência interna: "o repositório mencionado acima" ou simplesmente `governance/v1`.
Texto sugerido: n/a
ROI: BAIXO

## TESTE DA JOANA
Entenderia: SIM (para a maioria)
O que ela entenderia: A distinção entre "caderno vivo" e "caderno morto". Os sete indicadores de saúde do caderno. A anatomia dos seis blocos com justificativa de posição. Os dez anti-padrões.
O que ela NÃO entenderia: "DPO efetivo previamente nomeado" sem glosa. "CMN 4658/2018" como referência bare sem explicação do que é (Resolução do CMN sobre governança de TI em bancos). "HRAIS" no APX-J sem estar definido no APX-O.
Como corrigir: Adicionar glosa de 4-5 palavras após "DPO" e "CMN 4658/2018" na tabela de adendo setorial.

## TESTE DE DURABILIDADE
Classificação: ALTA
2 anos / 5 anos / 10 anos: Alta em todos os horizontes para a ficha conceitual; o conteúdo do repositório envelhece conforme regulação evolui.
Justificativa: A anatomia de seis blocos, os sete padrões de adaptação e os dez anti-padrões são estruturais — independentes de modelo de IA, de provedor, de legislação específica. Apenas a seção de adendo setorial vai exigir atualização quando PL 2338 for aprovado e regulamentado.

## TESTE DE DIFERENCIAÇÃO
Classificação: PROPRIEDADE INTELECTUAL
Justificativa: A combinação de (1) ficha conceitual no livro + (2) caderno executável no repositório + (3) métricas quantitativas de saúde do caderno + (4) anti-padrões nomeados não existe em nenhum framework concorrente (NIST AI RMF, ISO 42001, EU AI Act) com este nível de acessibilidade executiva em português. É o ativo de PI mais forte dos seis apêndices avaliados.

## TESTE DE MEMORIZAÇÃO
Ideia principal clara? SIM
Qual é a ideia principal: "Governança de IA não é documento — é prática viva medida por sete indicadores. Se vier um incidente e você não sabe de quem é a cadeira em cinco minutos, você não tem governança."
Justificativa: A frase final ("a organização precisa saber em até cinco minutos de quem é a cadeira") é a mais memorável dos seis apêndices. Tem potencial de citar em conselho de administração.

## TESTE DE TRANSFORMAÇÃO
Ao terminar, o leitor consegue fazer o que antes não conseguia:
- Distinguir teatro de compliance de governança ativa com critério operacional.
- Identificar em qual dos seis blocos o caderno da sua organização está fraco.
- Verificar se o caderno está vivo usando os sete indicadores quantitativos.
- Decidir se precisa de adendo setorial antes de adotar o modelo base.
- Defender a estrutura diante de auditoria externa com os argumentos da ficha conceitual.

## NOTA FINAL
Estrutura: 10 | Pedagogia: 9 | Clareza: 8 | Autoridade: 10 | Durabilidade: 9 | Diferenciação: 10 | Memorização: 9 | Transformação: 10
**Nota Geral: 9**

## DECISÃO EDITORIAL
MANTER COM AJUSTES

---

## LINHAS-TRACKER
```
APX-O|L1-APX-O-caderno-governanca-v1.md|01|P0|ALTO|Dez controles canônicos citados mas nunca nomeados na ficha conceitual|Adicionar tabela com nomes e funções dos dez controles na ficha|MANTER COM AJUSTES
APX-O|L1-APX-O-caderno-governanca-v1.md|02|P1|ALTO|Ambiguidade tipográfica "cinquenta e cinco mil" lida como 55.000 em vez de 50 a 5.000|Reformular frase de escopo com número e extenso inequívocos|MANTER COM AJUSTES
APX-O|L1-APX-O-caderno-governanca-v1.md|03|P1|MÉDIO|Sete padrões de adaptação sem título curto — reduz scanabilidade em uso de reunião|Reformatar cada padrão com título curto em negrito antes da descrição|MANTER COM AJUSTES
APX-O|L1-APX-O-caderno-governanca-v1.md|04|P2|BAIXO|Quadro de orientação não alinha com taxonomia do APX-N (Tipos A B C D)|Adicionar nota de rodapé de alinhamento entre os dois apêndices|MANTER COM AJUSTES
APX-O|L1-APX-O-caderno-governanca-v1.md|05|P2|BAIXO|URL do repositório citado três vezes — redundância que ocupa espaço|Na segunda e terceira citação substituir por referência interna|MANTER COM AJUSTES
```

---

# APX-Q — Manual do Professor

## RESUMO EXECUTIVO
Nota: 8/10
Veredito: A

## O QUE FUNCIONA
- A cobertura de cinco públicos distintos com planos de curso diferenciados (60h, 40h, 20h, 16h, autoestudo) é excepcional para material de adoção acadêmica e demonstra maturidade pedagógica real. Nenhum outro livro de IA de negócios em português oferece equivalente.
- A tabela de 20 aulas com capítulos, tema central e atividade prática é artefato executável — um professor pode adotar o livro amanhã usando apenas essa tabela.
- A estrutura interna de aula em quatro blocos (30+60+60+30 min) tem justificativa pedagógica explícita e é defensável contra os dois extremos identificados ("100% palestra que adormece" / "100% prática que dispersa").
- Os cinco pontos onde estudantes travam e os três erros conceituais comuns são informação de uso imediato para o professor adotante — vêm de experiência real e são mais valiosos que qualquer teoria pedagógica.
- Os quatro debates fecundos para sala são escolhidos com critério: open source vs. fechado, construir vs. comprar, autonomia de agente, regulação brasileira. Cada um tem tensão genuína, o que gera discussão produtiva.
- O projeto final em três entregas escalonadas (aula 8, 14, 19) é estruturalmente inteligente e resolve o problema clássico de "estudante que descobre na semana de prova que não entendeu nada".

## O QUE NÃO FUNCIONA
- A seção 4 (MBA Executivo) lista as sessões com capítulos "C06, RAG" em Sessão 3, mas a tabela da Seção 2 mostra RAG nos capítulos C06+C07. A seção 4 omite C07 sem explicação — inconsistência com o plano de 60h.
- O banco de 20 exercícios (Seção 8.1) é o achado mais problemático: vários exercícios têm pistas de gabarito que contradizem ou complementam o APX-K (Gabaritos), mas sem referência cruzada. Por exemplo, o exercício da aula 4 ("reproduza Lost in the Middle") tem gabarito de 3 linhas aqui, mas não está no APX-K. O APX-K e o APX-Q foram escritos em paralelo sem sincronização suficiente.
- A seção 8 admite honestamente que "o dataset público de exercícios está em construção em junho de 2026" — mas não declara quais exercícios do banco de 20 já têm gabarito completo no repositório e quais estão pendentes. O leitor não sabe o que está disponível hoje.
- A rubrica da Seção 7 tem problema de alinhamento: a dimensão "Profundidade Técnica" menciona "vai além do capítulo, cita paper do Apêndice G" como critério de excelência — mas o Apêndice G não está entre os seis apêndices avaliados aqui e não há verificação se essa promessa é cumprida no estado atual da obra.
- As variações por curso (Seção 10) para Medicina/Saúde mencionam "regulação da Anvisa e do CFM" como conteúdo de discussão — mas a obra não tem capítulo nem apêndice específico sobre regulação de saúde. É promessa de conteúdo que não existe no livro.
- O plano de 40h (pós-graduação) é significativamente mais raso que os outros — apenas dois parágrafos sem tabela de aulas. Para o público que provavelmente mais vai usar o livro como livro-texto (pós-graduação em Ciência de Dados, Gestão de Tecnologia), a orientação é a mais fraca.

## ACHADOS

### ACHADO 01
Categoria: P1
Problema: APX-K e APX-Q têm gabaritos paralelos e não sincronizados — exercício da aula 4 (Lost in the Middle) tem gabarito de 3 linhas no APX-Q mas não está no APX-K.
Por que é um problema: Professor que usa os dois apêndices recebe informação inconsistente. Estudante que procura gabarito no APX-K não encontra para esse exercício central.
Impacto no leitor: Confusão e necessidade de triangular entre dois apêndices para completar a informação.
Correção exata: Sincronizar APX-K e APX-Q: ou mover os gabaritos das pistas do APX-Q para o APX-K, ou adicionar referência cruzada explícita em cada exercício do APX-Q para a entrada correspondente no APX-K.
Texto sugerido: Adicionar ao final de cada exercício no APX-Q: "(gabarito estruturado: APX-K, Capítulo XX)" ou "gabarito completo em repositório `/teaching/exercises/aula-04.md`".
ROI: ALTO

### ACHADO 02
Categoria: P1
Problema: Variação para Medicina/Saúde promete discussão de "regulação Anvisa e CFM" que não existe como conteúdo nos capítulos ou apêndices.
Por que é um problema: Professor de medicina que adota o livro com base nessa seção vai descobrir que o conteúdo prometido não existe. É promessa não cumprida.
Impacto no leitor: Descredibiliza o Manual do Professor como guia confiável para adoção em cursos específicos.
Correção exata: Remover "discussão sobre regulação da Anvisa e do CFM" ou qualificá-la como "discussão aberta com material externo indicado pelo professor, uma vez que a obra não cobre regulação setorial de saúde".
Texto sugerido: "...complementada por discussão sobre aplicação clínica responsável e uso ético, com material regulatório externo (Anvisa, CFM) indicado pelo professor conforme contexto — a obra não cobre regulação setorial de saúde."
ROI: ALTO

### ACHADO 03
Categoria: P1
Problema: Plano de 40h (pós-graduação) é drasticamente mais raso que os outros quatro planos — dois parágrafos sem tabela de aulas para o público que mais vai usar o livro academicamente.
Por que é um problema: Pós-graduação em IA e Ciência de Dados é o canal de adoção acadêmica mais provável para a obra. O plano mais fraco para o público mais relevante é inversão de prioridades editorial.
Impacto no leitor: Professor de pós-graduação que acessa o APX-Q para avaliar adoção vai encontrar orientação insuficiente e pode optar por obra concorrente com material mais estruturado.
Correção exata: Expandir a seção 3 com tabela de 20 sessões equivalente à da seção 2, adaptada ao ritmo de pós-graduação com seminários de papers.
Texto sugerido: n/a (requer reescrita da seção 3 com tabela).
ROI: ALTO

### ACHADO 04
Categoria: P1
Problema: Inconsistência entre os capítulos de RAG no plano de MBA (Sessão 3 = apenas C06) e no plano de 60h (Aula 4 = C06+C07) sem justificativa.
Por que é um problema: Menor problema de consistência, mas sinaliza que os planos foram escritos sem sincronização final.
Impacto no leitor: Professor que usa os dois planos como referência cruzada encontra inconsistência que pode confundir o que está em C07 versus C06.
Correção exata: Ou justificar a omissão de C07 no MBA ("C07 é capítulo de detalhamento técnico — MBA foca em C06 como capítulo executivo de RAG") ou incluir C07 na sessão 3 do MBA.
Texto sugerido: "Sessão 3 | C06 (RAG executivo — C07 opcional para turmas com background técnico) | Encomendar projeto de RAG com método"
ROI: MÉDIO

### ACHADO 05
Categoria: P2
Problema: Seção 8 declara que dataset está em construção mas não especifica quais dos 20 exercícios têm gabarito completo disponível hoje.
Por que é um problema: Professor que quer adotar hoje não sabe o que está pronto vs. o que está prometido. A honestidade da declaração é correta, mas a falta de status por exercício impede uso imediato.
Impacto no leitor: Professor não consegue planejar com precisão quais exercícios incluir no plano de curso hoje.
Correção exata: Adicionar coluna "Status do gabarito" na tabela de 20 exercícios (Disponível / Em construção / No repositório).
Texto sugerido: Adicionar coluna na tabela da Seção 8.1: "| Aula | Exercício | Nível | Pista de gabarito | **Status** |"
ROI: MÉDIO

### ACHADO 06
Categoria: P2
Problema: A rubrica da Seção 7 menciona "cita paper do Apêndice G" como critério de excelência sem verificar se o Apêndice G existe e entrega o prometido.
Por que é um problema: Critério de avaliação que depende de apêndice não avaliado nesta banca pode introduzir inconsistência se o APX-G estiver incompleto.
Impacto no leitor: Se APX-G estiver incompleto, o critério de excelência da rubrica fica sem base.
Correção exata: Verificar estado do APX-G antes de publicação. Se completo, manter. Se em construção, adicionar nota: "(o Apêndice G está em construção; professor pode substituir por papers indicados pelo próprio professor)".
Texto sugerido: n/a até verificação do APX-G.
ROI: MÉDIO

## TESTE DA JOANA
Entenderia: SIM (Joana como executiva que avalia adoção para programa corporativo)
O que ela entenderia: Os cinco públicos-alvo, a carga horária por curso, os quatro módulos corporativos. A estrutura interna de aula de quatro blocos é clara.
O que ela NÃO entenderia: "Precision@5", "CoT", "similaridade coseno", "LLM-as-judge" nos exercícios do banco da Seção 8.1 sem tradução. Mas Joana não é o público primário deste apêndice — é professor ou coordenador de curso.
Como corrigir: Para uso corporativo (coordenador que avalia adoção para capacitação), adicionar na Seção 5 (Plano de Capacitação Corporativa) um parágrafo em linguagem de negócio sobre o que o participante consegue fazer ao final de cada módulo.

## TESTE DE DURABILIDADE
Classificação: MÉDIA-ALTA
2 anos: Alta — planos de curso, rubrica e estrutura pedagógica não dependem de modelo específico.
5 anos: Média — os exercícios técnicos que citam modelos específicos (Llama 3.x, Claude) vão exigir atualização de referências.
10 anos: Baixa para os exercícios técnicos; alta para a estrutura pedagógica.
Justificativa: A estrutura de quatro blocos de aula, a rubrica de cinco dimensões e os cinco pontos de trava de estudantes são independentes de modelo. Os exercícios que citam modelos específicos (exercício aula 9: "Llama 3.x", exercício aula 8: "reasoning model") vão envelhecer com os modelos.

## TESTE DE DIFERENCIAÇÃO
Classificação: PROPRIEDADE INTELECTUAL
Justificativa: Manual do professor com planos diferenciados por cinco públicos, banco de exercícios calibrados, rubrica de cinco dimensões e estrutura interna de aula — nenhum livro de IA de negócios em português oferece isso. É ativo de adoção acadêmica que cria barreira de entrada real para concorrentes: quem adota este livro recebe infraestrutura de curso que demora meses para replicar.

## TESTE DE MEMORIZAÇÃO
Ideia principal clara? SIM
Qual é a ideia principal: "Este livro tem infraestrutura completa para virar livro-texto — plano de aula, rubrica e banco de exercícios incluídos."
Justificativa: A promessa é clara. A entrega parcial (banco em construção, plano de pós-graduação raso) reduz a força da promessa, mas a estrutura geral é memorável como proposta de valor para professor adotante.

## TESTE DE TRANSFORMAÇÃO
Ao terminar, o leitor (professor adotante) consegue fazer o que antes não conseguia:
- Montar plano de curso de 60h com tabela de 20 aulas em menos de 2 horas de trabalho.
- Estruturar cada aula de 3h com os quatro blocos calibrados.
- Avaliar projetos finais com rubrica de cinco dimensões em vez de avaliação subjetiva.
- Identificar antecipadamente os cinco pontos onde estudantes vão travar.
- Adaptar o curso para graduação, pós, MBA, corporativo ou escola técnica com orientação diferenciada.

## NOTA FINAL
Estrutura: 8 | Pedagogia: 9 | Clareza: 8 | Autoridade: 8 | Durabilidade: 7 | Diferenciação: 9 | Memorização: 8 | Transformação: 9
**Nota Geral: 8**

## DECISÃO EDITORIAL
MANTER COM AJUSTES

---

## LINHAS-TRACKER
```
APX-Q|L1-APX-Q-manual-do-professor.md|01|P1|ALTO|APX-K e APX-Q com gabaritos paralelos e não sincronizados — exercício aula 4 no APX-Q sem correspondente no APX-K|Sincronizar os dois apêndices com referências cruzadas explícitas|MANTER COM AJUSTES
APX-Q|L1-APX-Q-manual-do-professor.md|02|P1|ALTO|Variação para Medicina promete conteúdo de regulação Anvisa/CFM que não existe na obra|Qualificar como material externo indicado pelo professor ou remover|MANTER COM AJUSTES
APX-Q|L1-APX-Q-manual-do-professor.md|03|P1|ALTO|Plano de pós-graduação (40h) drasticamente mais raso que outros quatro planos — dois parágrafos sem tabela|Expandir seção 3 com tabela de aulas equivalente à da seção 2|MANTER COM AJUSTES
APX-Q|L1-APX-Q-manual-do-professor.md|04|P1|MÉDIO|Inconsistência de capítulos entre plano de MBA (C06 apenas) e plano de 60h (C06+C07) para RAG|Alinhar ou justificar explicitamente a omissão de C07 no MBA|MANTER COM AJUSTES
APX-Q|L1-APX-Q-manual-do-professor.md|05|P2|MÉDIO|Banco de exercícios sem status por exercício — professor não sabe o que está disponível hoje|Adicionar coluna de status na tabela de 20 exercícios|MANTER COM AJUSTES
APX-Q|L1-APX-Q-manual-do-professor.md|06|P2|MÉDIO|Critério de excelência da rubrica cita APX-G sem verificação do estado atual do apêndice|Verificar APX-G; se incompleto, adicionar nota de substituição|MANTER COM AJUSTES
```

---

# CONSOLIDADO — TOTAIS POR APÊNDICE

| Apêndice | P0 | P1 | P2 | Total | Nota | Decisão |
|---|---|---|---|---|---|---|
| APX-J — Trilha do Número | 1 | 3 | 2 | 6 | 8/10 | MANTER COM AJUSTES |
| APX-K — Gabaritos Comentados | 1 | 2 | 1 | 4 | 5/10 | REVISAR PARCIALMENTE |
| APX-M — Manifesto de Bolso | 0 | 1 | 2 | 3 | 9/10 | MANTER COM AJUSTES |
| APX-N — Metodológico Números | 0 | 2 | 2 | 4 | 8/10 | MANTER COM AJUSTES |
| APX-O — Caderno de Governança | 1 | 2 | 2 | 5 | 9/10 | MANTER COM AJUSTES |
| APX-Q — Manual do Professor | 0 | 4 | 2 | 6 | 8/10 | MANTER COM AJUSTES |
| **TOTAL** | **3** | **14** | **11** | **28** | | |

## PRIORIDADES EDITORIAIS POR IMPACTO

**P0 — 3 achados críticos:**
1. APX-J/02: Afirmação "DeepSeek-R1 publicado em Nature" sem DOI confirmado — risco de erro factual em seção central de credibilidade.
2. APX-K/01: Apêndice de gabaritos incompleto sem declarar isso ao leitor — erode confiança na obra em primeiro uso.
3. APX-O/01: Dez controles canônicos nunca nomeados na ficha conceitual — executivo não consegue defender o caderno sem o repositório aberto.

**P1 com ROI ALTO — ações imediatas recomendadas:**
- APX-J/01: Tabela de modelos sem data de captura por linha.
- APX-J/03: Incidente Chinese state-actor sem fonte verificável.
- APX-Q/01: APX-K e APX-Q com gabaritos não sincronizados.
- APX-Q/02: Variação Medicina promete conteúdo inexistente na obra.
- APX-Q/03: Plano de pós-graduação sem tabela de aulas.
- APX-O/02: Ambiguidade tipográfica "55 mil vs. 50-5.000 colaboradores".
- APX-N/01: Inconsistência "90 afirmações" no texto vs. 87 na tabela.

---

## LINHAS-TRACKER CONSOLIDADO

```
APX-J|L1-APX-J-trilha-do-numero.md|01|P1|ALTO|Tabela de modelos sem data de captura por linha|Adicionar coluna Data verificação na tabela da Seção 1|MANTER COM AJUSTES
APX-J|L1-APX-J-trilha-do-numero.md|02|P0|ALTO|Afirmação "publicado em Nature em 2025" para DeepSeek-R1 sem DOI confirmado|Remover referência a Nature ou confirmar com DOI|MANTER COM AJUSTES
APX-J|L1-APX-J-trilha-do-numero.md|03|P1|ALTO|Incidente Chinese state-actor sem fonte pública verificável|Adicionar fonte pública ou remover o incidente|MANTER COM AJUSTES
APX-J|L1-APX-J-trilha-do-numero.md|04|P1|MÉDIO|URLs de benchmark apontam para agregadores sem nota de curadoria|Indicar também fonte primária de cada benchmark|MANTER COM AJUSTES
APX-J|L1-APX-J-trilha-do-numero.md|05|P2|BAIXO|Estatística AI Incident Database sem URL|Adicionar URL da fonte ao final da frase|MANTER COM AJUSTES
APX-J|L1-APX-J-trilha-do-numero.md|06|P2|BAIXO|Links de arXiv não verificados para acessibilidade|Verificar todos os URLs na próxima revisão|MANTER COM AJUSTES
APX-K|L1-APX-K-gabaritos.md|01|P0|ALTO|Apêndice incompleto sem declarar isso ao leitor — cobre menos de 60% dos capítulos com exercícios|Adicionar nota editorial com lista de capítulos cobertos e link para repositório|REVISAR PARCIALMENTE
APX-K|L1-APX-K-gabaritos.md|02|P1|MÉDIO|Gabaritos de projetos sem rubrica de avaliação — apenas critério pass/fail|Adicionar escala de proficiência por projeto (insuficiente/proficiente/excelente)|REVISAR PARCIALMENTE
APX-K|L1-APX-K-gabaritos.md|03|P1|BAIXO|Ausência de referências cruzadas com capítulos nos títulos de seção|Adicionar número do capítulo a cada título de seção|REVISAR PARCIALMENTE
APX-K|L1-APX-K-gabaritos.md|04|P2|BAIXO|Critério de roadmap depende de aprovação por diretoria — inutilizável em autoestudo|Adicionar critério alternativo para autoavaliação individual|MANTER COM AJUSTES
APX-M|L1-APX-M-manifesto-bolso.md|01|P1|MÉDIO|Inconsistência de nomenclatura entre Síntese (título interno) e Manifesto de Bolso (referências externas)|Ajustar título para incluir "Manifesto de Bolso" como termo-âncora|MANTER COM AJUSTES
APX-M|L1-APX-M-manifesto-bolso.md|02|P2|BAIXO|Mecânica do Princípio 4 mistura eixos de tarefa com custo sem distinção clara|Separar custo dos eixos de domínio na descrição da mecânica|MANTER COM AJUSTES
APX-M|L1-APX-M-manifesto-bolso.md|03|P2|MÉDIO|Frase-síntese sem expansão no momento de maior impacto emocional do apêndice|Adicionar 2-3 linhas de expansão da tese central abaixo da frase|MANTER COM AJUSTES
APX-N|L1-APX-N-metodologico-numeros.md|01|P1|ALTO|Inconsistência entre "aproximadamente noventa" no texto e soma de 87 na tabela da Seção 5|Corrigir texto para 87 ou revisar tabela para totalizar 90|MANTER COM AJUSTES
APX-N|L1-APX-N-metodologico-numeros.md|02|P1|MÉDIO|Repositório auditoria-quantitativa-l1.md sem URL completo — inconsistência com padrão do APX-J|Adicionar URL completo para o arquivo de auditoria no repositório|MANTER COM AJUSTES
APX-N|L1-APX-N-metodologico-numeros.md|03|P2|BAIXO|Header e footer com declarações de revisão redundantes e potencialmente confusas|Unificar em campo único no header com data atualizada a cada revisão|MANTER COM AJUSTES
APX-N|L1-APX-N-metodologico-numeros.md|04|P2|BAIXO|Seção 6 declara 15-20 notas de rodapé sem listá-las — autocertificação sem verificabilidade|Adicionar referência à tabela de Tipo A no repositório|MANTER COM AJUSTES
APX-O|L1-APX-O-caderno-governanca-v1.md|01|P0|ALTO|Dez controles canônicos citados mas nunca nomeados na ficha conceitual|Adicionar tabela com nomes e funções dos dez controles na ficha|MANTER COM AJUSTES
APX-O|L1-APX-O-caderno-governanca-v1.md|02|P1|ALTO|Ambiguidade tipográfica "cinquenta e cinco mil" lida como 55.000 em vez de 50 a 5.000|Reformular frase de escopo com número e extenso inequívocos|MANTER COM AJUSTES
APX-O|L1-APX-O-caderno-governanca-v1.md|03|P1|MÉDIO|Sete padrões de adaptação sem título curto — reduz scanabilidade em uso de reunião|Reformatar cada padrão com título curto em negrito antes da descrição|MANTER COM AJUSTES
APX-O|L1-APX-O-caderno-governanca-v1.md|04|P2|BAIXO|Quadro de orientação não alinha com taxonomia do APX-N (Tipos A B C D)|Adicionar nota de rodapé de alinhamento entre os dois apêndices|MANTER COM AJUSTES
APX-O|L1-APX-O-caderno-governanca-v1.md|05|P2|BAIXO|URL do repositório citado três vezes — redundância que ocupa espaço|Na segunda e terceira citação substituir por referência interna|MANTER COM AJUSTES
APX-Q|L1-APX-Q-manual-do-professor.md|01|P1|ALTO|APX-K e APX-Q com gabaritos paralelos e não sincronizados — exercício aula 4 no APX-Q sem correspondente no APX-K|Sincronizar os dois apêndices com referências cruzadas explícitas|MANTER COM AJUSTES
APX-Q|L1-APX-Q-manual-do-professor.md|02|P1|ALTO|Variação para Medicina promete conteúdo de regulação Anvisa/CFM que não existe na obra|Qualificar como material externo indicado pelo professor ou remover|MANTER COM AJUSTES
APX-Q|L1-APX-Q-manual-do-professor.md|03|P1|ALTO|Plano de pós-graduação (40h) drasticamente mais raso que outros quatro planos — dois parágrafos sem tabela|Expandir seção 3 com tabela de aulas equivalente à da seção 2|MANTER COM AJUSTES
APX-Q|L1-APX-Q-manual-do-professor.md|04|P1|MÉDIO|Inconsistência de capítulos entre plano de MBA (C06 apenas) e plano de 60h (C06+C07) para RAG|Alinhar ou justificar explicitamente a omissão de C07 no MBA|MANTER COM AJUSTES
APX-Q|L1-APX-Q-manual-do-professor.md|05|P2|MÉDIO|Banco de exercícios sem status por exercício — professor não sabe o que está disponível hoje|Adicionar coluna de status na tabela de 20 exercícios|MANTER COM AJUSTES
APX-Q|L1-APX-Q-manual-do-professor.md|06|P2|MÉDIO|Critério de excelência da rubrica cita APX-G sem verificação do estado atual do apêndice|Verificar APX-G; se incompleto, adicionar nota de substituição|MANTER COM AJUSTES
```
