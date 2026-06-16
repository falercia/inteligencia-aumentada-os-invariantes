# BANCA EDITORIAL ADVERSARIAL — APÊNDICES A a I
## Livro: INTELIGÊNCIA AUMENTADA — Os Nove Princípios Permanentes
## Data: junho de 2026

---

# APX-A — L1-APX-A-glossario.md

## RESUMO EXECUTIVO
Nota: 8/10
Veredito: A

## O QUE FUNCIONA
- Taxonomia em nove categorias é logicamente coerente: vai de princípios próprios (I) até regulação (IX), cobrindo o mapa completo da obra sem sobreposição óbvia.
- Marcadores ★ / ◆ são diferencial real: comunicam ao leitor o que é propriedade intelectual da obra vs. vocabulário canônico do campo. Decisão editorial acertada.
- Categoria VIII (casos brasileiros) âncora a ficção nos casos concretos da obra — reforça coerência com a promessa de contexto nacional.
- Definição de "Open weights" inclui a distinção crucial vs. open source completo — precisão rara em livros de divulgação.
- Definição de "Agente" é funcional e diferencia de chatbot com clareza operacional.

## O QUE NÃO FUNCIONA
- Categoria VII ("Padrões de produto e plataformas") mistura padrão de protocolo (MCP), padrão de mercado (tiers) e padrão de produto (Projects/Workspaces) sem hierarquia clara — lista heterogênea que força comparação entre incomparáveis.
- "Autoavaliação" (Cat. I) está definida como "critério objetivo de fechamento de cada capítulo" mas não tem marcador ★ consistente com os demais termos proprietários — inconsistência de sistema.
- "Os Nove Frameworks" (Cat. I) lista nove frameworks em uma única entrada de uma linha — a mais importante estrutura operacional da obra merece pelo menos duas linhas por framework, não um parágrafo compactado.
- Falta entrada para "Reasoning models" — o glossário não cobre o capítulo C14B, que é adição ao sumário.
- Entrada de "Prompt engineering" (Cat. II) é vaga: "disciplina de construir prompts profissionalmente" — não diferencia do conceito de Context Engineering, que o livro trata como evolução.
- Regulação (Cat. IX): "PL de IA brasileiro" diz "em tramitação" sem número do PL — inconsistência com a Bibliografia (APX-H), que cita corretamente "PL 2338/2023".

## ACHADOS

### ACHADO 01
Categoria: P1
Problema: "Os Nove Frameworks" comprimidos em uma única entrada sem definição individual de cada framework
Por que é um problema: o leitor que chega ao glossário para relembrar o que é "Diagnóstico de Encaixe entre Tarefa e Modelo" não encontra entrada própria — precisa ler o parágrafo inteiro da entrada "Os Nove Frameworks" e ainda assim não obtém definição
Impacto no leitor: glossário falha em sua função de consulta rápida para o elemento central da obra
Correção exata: criar nove entradas individuais, uma por framework, com definição de 1–2 linhas e marcador ★; remover a entrada agregada ou deixá-la como índice com remissivas
Texto sugerido: ex. "**Diagnóstico de Encaixe entre Tarefa e Modelo.** ★ Framework do Princípio 4: avalia qual modelo serve melhor a uma tarefa específica em cinco eixos (latência, custo, qualidade, contexto, capacidade modal), independente do ranking de benchmark vigente."
ROI: ALTO

### ACHADO 02
Categoria: P1
Problema: ausência de entrada para "Reasoning models" no glossário
Por que é um problema: C14B é capítulo dedicado do livro; o índice remissivo (APX-I) não lista o termo; o glossário não o define — buraco de cobertura em conceito com alta visibilidade de mercado (OpenAI o1, Claude 3.7 Sonnet, DeepSeek-R1)
Impacto no leitor: leitor que chega ao glossário após ler C14B não encontra âncora; leitor que começa pelo glossário não sabe que reasoning models existem como categoria
Correção exata: adicionar entrada em Cat. II com marcador ◆: diferença de chain-of-thought interno vs. resposta final, menção a chain-of-thought "invisível" do modelo
Texto sugerido: "**Reasoning model (modelo de raciocínio).** ◆ Modelo treinado para externalizar cadeia de raciocínio longa antes de produzir resposta. A cadeia interna (thinking) não é visível ao usuário em todas as implementações. Custo por token é tipicamente mais alto; ganho em tarefas que exigem múltiplos passos lógicos é documentado. Base do capítulo C14B."
ROI: ALTO

### ACHADO 03
Categoria: P1
Problema: "PL de IA brasileiro" no glossário sem número de identificação; APX-H cita "PL 2338/2023"
Por que é um problema: inconsistência entre dois apêndices do mesmo livro — leitor que usa os dois documentos percebe descuido
Impacto no leitor: corroe confiança em precisão referencial da obra
Correção exata: unificar para "PL 2338/2023 (em tramitação no Senado Federal)" em ambos os documentos
Texto sugerido: "**PL de IA brasileiro.** PL 2338/2023, em tramitação no Senado Federal. Regime de responsabilidade e requisitos de transparência para sistemas de IA de alto risco."
ROI: MÉDIO

### ACHADO 04
Categoria: P2
Problema: "Prompt engineering" não diferencia de "Context Engineering" — duas entradas adjacentes no glossário que o livro trata como campos distintos
Por que é um problema: a obra posiciona Context Engineering como evolução de Prompt engineering (C11 vs. C09); o glossário não captura essa relação
Impacto no leitor: leitor fica sem clareza sobre hierarquia conceitual
Correção exata: adicionar ao fim de "Prompt engineering": "Ver também Context Engineering, que expande a disciplina para orquestração de múltiplas fontes no contexto."
Texto sugerido: n/a (apenas adicionar remissiva)
ROI: BAIXO

### ACHADO 05
Categoria: P2
Problema: "Autoavaliação" em Cat. I não tem marcador ★ apesar de ser termo proprietário da obra
Por que é um problema: inconsistência do sistema de marcadores — todos os outros termos proprietários têm ★
Impacto no leitor: pequena — leitor pode não perceber que é conceito proprio da obra
Correção exata: adicionar ★ à entrada "Autoavaliação"
Texto sugerido: "**Autoavaliação.** ★ Critério objetivo de fechamento de cada capítulo da obra, em cinco dimensões."
ROI: BAIXO

### ACHADO 06
Categoria: P2
Problema: Categoria VII mistura protocolo (MCP), padrão de mercado (tiers) e conceito de produto (Projects/Workspaces) sem hierarquia
Por que é um problema: leitora Joana não consegue inferir por que esses itens estão juntos; a categoria parece resíduo de organização incompleta
Impacto no leitor: baixa — categoria funciona mesmo sem hierarquia explícita
Correção exata: adicionar nota introdutória de 1 linha: "Padrões de interface e plataforma que afetam arquitetura de produto com IA."
Texto sugerido: n/a
ROI: BAIXO

## TESTE DA JOANA
Entenderia: SIM
O que ela entenderia: vocabulário principal, distinção ★/◆, casos brasileiros como âncoras
O que ela NÃO entenderia: entrada agregada "Os Nove Frameworks" — não consegue recuperar definição de um framework específico; "DPO/PPO/RLAIF" sem analogia (termos ficam opacos)
Como corrigir: desagregar frameworks; adicionar uma linha de analogia para DPO/PPO ("otimização de preferência — como treinar via comparação de opções em vez de nota individual")

## TESTE DE DURABILIDADE
Classificação: ALTA
2 anos: estável — princípios e vocabulário técnico são duráveis
5 anos: estável — Cat. I (princípios) e Cat. II (fundamentos) sobrevivem; Cat. VII (plataformas) pode requerer atualização se MCP for superado por outro padrão
10 anos: Cat. VII e Cat. IX envelhecerão (regulação muda, plataformas mudam); resto sobrevive
Justificativa: o glossário não lista modelos específicos nem preços — escolha editorial acertada que protege durabilidade; PL "em tramitação" pode ser resolvido em 1–2 anos

## TESTE DE DIFERENCIAÇÃO
Classificação: DIFERENCIADO
Justificativa: sistema ★/◆ é diferencial real — não é glossário padrão de divulgação; a inclusão dos frameworks proprietários e casos brasileiros âncora o vocabulário à obra específica

## TESTE DE MEMORIZAÇÃO
Ideia principal clara? SIM
Qual é a ideia principal (em 1 frase): vocabulário canônico que diferencia o que é próprio da obra (★) do que é campo (◆)
Justificativa: sistema de marcadores funciona; categoria I lista os princípios com clareza suficiente

## TESTE DE TRANSFORMAÇÃO
Ao terminar, o leitor consegue fazer o que antes não conseguia:
- Usar vocabulário preciso da obra em conversas profissionais sem ambiguidade
- Distinguir termos proprietários dos canônicos do campo
- Localizar casos brasileiros que correspondem a cada cenário

## NOTA FINAL
Estrutura: 8 | Pedagogia: 7 | Clareza: 8 | Autoridade: 8 | Durabilidade: 9 | Diferenciação: 8 | Memorização: 8 | Transformação: 7
**Nota Geral: 7.9**

## DECISÃO EDITORIAL
MANTER COM AJUSTES

---

## LINHAS-TRACKER
```
APX-A|L1-APX-A-glossario.md|01|P1|ALTO|Nove Frameworks sem entrada individual por framework|Criar 9 entradas individuais com definição e marcador ★|MANTER COM AJUSTES
APX-A|L1-APX-A-glossario.md|02|P1|ALTO|Reasoning models ausente do glossário|Adicionar entrada ◆ com definição e remissiva ao C14B|MANTER COM AJUSTES
APX-A|L1-APX-A-glossario.md|03|P1|MÉDIO|PL de IA sem número; inconsistente com APX-H|Unificar para PL 2338/2023 em ambos os apêndices|MANTER COM AJUSTES
APX-A|L1-APX-A-glossario.md|04|P2|BAIXO|Prompt engineering não diferencia de Context Engineering|Adicionar remissiva cruzada entre as duas entradas|MANTER COM AJUSTES
APX-A|L1-APX-A-glossario.md|05|P2|BAIXO|Autoavaliação sem marcador ★|Adicionar ★ à entrada|MANTER COM AJUSTES
APX-A|L1-APX-A-glossario.md|06|P2|BAIXO|Cat. VII mistura protocolo, padrão de mercado e conceito de produto sem hierarquia|Adicionar nota introdutória de 1 linha à categoria|MANTER COM AJUSTES
```

---

# APX-B — L1-APX-B-mapa-mental.md

## RESUMO EXECUTIVO
Nota: 8/10
Veredito: A

## O QUE FUNCIONA
- Estrutura em três camadas (Tese → Princípios → Frameworks → Capítulos) é o melhor sumário cognitivo da obra — comunica a arquitetura intelectual mais rapidamente do que qualquer outro apêndice.
- A roda dos Nove Princípios em ASCII funciona para ebook: visual sem depender de imagem binária, portável, legível em qualquer renderizador de Markdown.
- Tabela "Capítulo × Princípio primário e secundário" é o artefato mais útil da obra para professor ou facilitador de workshop — permite montar trilha personalizada em 5 minutos.
- Tabela de "Relações críticas entre princípios" (os pares) captura a inteligência da obra de forma citável — especialmente o par 6↔7 ("autonomia sem eval é fé escalada").
- Tabela "Como usar este mapa" por situação é pedagogia aplicada correta: mapeia uso, não estrutura.

## O QUE NÃO FUNCIONA
- A "roda" em ASCII posiciona os princípios de forma assimétrica (P5 e P6 aparecem na base, abaixo do eixo, isolados dos outros 7) sem explicação do critério de posicionamento — parece distribuição aleatória, não arquitetural.
- A tabela "Princípio × Framework × Capítulo" lista "Auditoria de honestidade dentro da Pirâmide da Avaliação" como framework do Princípio 1 — mas no Glossário (APX-A), a "Pirâmide da Avaliação" é listada como framework do Princípio 7, não do Princípio 1. Inconsistência entre apêndices.
- C14B ("Reasoning models") e C14C ("Spec-driven development") aparecem na tabela de capítulos mas não existem como linhas na tabela "Princípio × Framework × Capítulo" — os capítulos adicionados ao sumário não foram integrados ao mapa de frameworks.
- "Como usar este mapa" tem cinco situações mas omite a mais óbvia: "Quero saber qual princípio um incidente violou" (resposta: olhe a tabela de relações críticas).

## ACHADOS

### ACHADO 01
Categoria: P1
Problema: Princípio 1 mapeado para "Auditoria de honestidade dentro da Pirâmide da Avaliação" como framework, mas APX-A lista Pirâmide da Avaliação como framework do Princípio 7
Por que é um problema: inconsistência direta entre APX-B e APX-A no elemento central da arquitetura — leitor que lê os dois apêndices percebe contradição
Impacto no leitor: corrói confiança na coerência do sistema de frameworks
Correção exata: alinhar: ou o Princípio 1 tem seu próprio framework (que precisa ser nomeado explicitamente), ou a tabela deve indicar que P1 opera dentro da Pirâmide de Evals (como sublayer), não como framework próprio
Texto sugerido: na coluna Framework do P1: "Princípio 1 opera como pressuposto transversal da Pirâmide da Avaliação (P7) — não tem framework dedicado; é premissa dos demais"
ROI: ALTO

### ACHADO 02
Categoria: P1
Problema: C14B e C14C presentes na tabela de capítulos mas ausentes da tabela Princípio × Framework × Capítulo
Por que é um problema: as tabelas ficam inconsistentes entre si; leitor que usa o mapa para navegar pelos capítulos C14B e C14C não encontra orientação de qual princípio governa aqueles capítulos
Impacto no leitor: confusão de navegação
Correção exata: adicionar C14B e C14C como linhas na tabela Princípio × Framework
Texto sugerido: C14B já tem linha ("C14B. Reasoning models | 1 | 2 | Raciocínio explícito sob escrutínio"); verificar se essa linha aparece na tabela Princípio × Framework também (atualmente só aparece na tabela Capítulo × Princípio)
ROI: MÉDIO

### ACHADO 03
Categoria: P2
Problema: roda ASCII posiciona P5 e P6 abaixo do eixo central, isolados, sem explicação do critério de layout
Por que é um problema: leitor infere hierarquia onde não existe — parece que P5 e P6 são "menos importantes" ou "derivados" dos outros
Impacto no leitor: confusão conceitual para quem usa a roda como âncora mental
Correção exata: adicionar 1 linha de nota embaixo da roda: "O layout é funcional, não hierárquico — os nove princípios têm peso equivalente; a posição reflete apenas restrições do diagrama em texto."
Texto sugerido: "> Nota: o diagrama acima é representação funcional, não hierárquica. Os nove princípios têm peso equivalente na obra."
ROI: BAIXO

### ACHADO 04
Categoria: P2
Problema: "Como usar este mapa" omite caso de uso "Identifiquei um incidente — quero saber qual princípio foi violado"
Por que é um problema: é o caso de uso mais frequente em produção para gestor ou engenheiro; o próprio APX-I (índice) orienta isso mas o mapa mental, que é mais rico, não o faz
Impacto no leitor: subutilização do mapa em contexto operacional
Correção exata: adicionar linha na tabela "Como usar este mapa": "Estou investigando um incidente de IA | Use a tabela de Relações Críticas para identificar qual princípio foi violado e leia o capítulo correspondente"
Texto sugerido: n/a (inserção direta na tabela)
ROI: BAIXO

## TESTE DA JOANA
Entenderia: SIM (parcialmente)
O que ela entenderia: a hierarquia de três camadas; a tabela de trilhas temáticas; "Como usar este mapa" por situação
O que ela NÃO entenderia: a roda ASCII — o diagrama de conexões bidirecionais com setas e símbolos (◀──▶) não é intuitivo para não-técnica; as abreviações C14B, C14C nas tabelas sem expansão do nome completo
Como corrigir: adicionar título completo dos capítulos na tabela (em vez de apenas C14B, escrever "C14B — Reasoning models"); simplificar a roda ou adicionar legenda de leitura

## TESTE DE DURABILIDADE
Classificação: ALTA
2 anos / 5 anos / 10 anos: altíssima — o mapa mapeia princípios e frameworks, não ferramentas nem modelos; é o apêndice com maior longevidade da obra
Justificativa: nenhuma referência a modelo específico, versão de API ou preço; a estrutura conceitual é estável por design

## TESTE DE DIFERENCIAÇÃO
Classificação: PROPRIEDADE INTELECTUAL
Justificativa: nenhum livro de IA do mercado tem mapa mental deste nível de precisão arquitetural — a tabela de relações críticas entre princípios sozinha já é diferencial citável

## TESTE DE MEMORIZAÇÃO
Ideia principal clara? SIM
Qual é a ideia principal (em 1 frase): os nove princípios são o esqueleto; os frameworks são os músculos; os capítulos são os casos
Justificativa: a estrutura em três camadas comunica a arquitetura da obra de forma direta e memorável

## TESTE DE TRANSFORMAÇÃO
Ao terminar, o leitor consegue fazer o que antes não conseguia:
- Montar trilha de leitura personalizada por perfil (executivo, dev, consultor) usando a tabela de trilhas
- Identificar qual princípio governa uma decisão real em produção
- Apresentar a arquitetura da obra a um time em 10 minutos usando a roda e a tabela de três camadas

## NOTA FINAL
Estrutura: 9 | Pedagogia: 8 | Clareza: 7 | Autoridade: 9 | Durabilidade: 10 | Diferenciação: 9 | Memorização: 9 | Transformação: 8
**Nota Geral: 8.6**

## DECISÃO EDITORIAL
MANTER COM AJUSTES

---

## LINHAS-TRACKER
```
APX-B|L1-APX-B-mapa-mental.md|01|P1|ALTO|Princípio 1 mapeado para framework inconsistente com APX-A|Alinhar: P1 sem framework próprio ou nomear framework distinto|MANTER COM AJUSTES
APX-B|L1-APX-B-mapa-mental.md|02|P1|MÉDIO|C14B e C14C ausentes da tabela Princípio × Framework|Adicionar linhas às duas tabelas afetadas|MANTER COM AJUSTES
APX-B|L1-APX-B-mapa-mental.md|03|P2|BAIXO|Roda ASCII sem nota de que layout não implica hierarquia|Adicionar nota de 1 linha abaixo da roda|MANTER COM AJUSTES
APX-B|L1-APX-B-mapa-mental.md|04|P2|BAIXO|Caso de uso "incidente" ausente da tabela "Como usar este mapa"|Adicionar linha à tabela|MANTER COM AJUSTES
```

---

# APX-C — L1-APX-C-roadmaps.md

## RESUMO EXECUTIVO
Nota: 7/10
Veredito: B

## O QUE FUNCIONA
- Seis personas cobrem o espectro real de leitores da obra — decisão acertada de não usar apenas "técnico vs. não-técnico".
- Estrutura 30/90/180/365 dias com critérios de avanço concretos é o padrão de excelência em livros de transformação (análogo ao modelo de OKRs trimestrais do Doerr); coloca o livro acima da média do gênero.
- Artefatos esperados por marco (deck, RACI, golden set, cartaz) são tangíveis — leitor sabe exatamente o que produzir.
- "Instrumentos comuns a todas as personas" (calendário recorrente + métricas universais) é adição inteligente que evita repetição e reforça coerência entre personas.
- Roadmap do Desenvolvedor (Marco 90 dias) — "PR com eval em CI virou padrão do time" — é critério de avanço defensável e cirúrgico.

## O QUE NÃO FUNCIONA
- Roadmap do Criador de Conteúdo (Persona 6) inclui "Biblioteca pessoal de prompts publicada" como artefato do Marco 90 dias — viola diretamente a tese central ("Modelos passam. Método fica."); publicar biblioteca de prompts incentiva o leitor a se posicionar como colecionador de prompts, não como operador de método.
- Marco 365 dias do Executivo — "Vocabulário dos Princípios incorporado em reuniões executivas" — é critério cultural não auditável; contrasta com a precisão dos outros critérios ("auditoria externa concluída").
- Roadmap 4 (Consultor), Marco 365 dias: "Dez ou mais clientes operando pelo método" é meta absoluta sem baseline — para um consultor solo vs. empresa de consultoria, o número é incomparável.
- Ausência de persona para o perfil "Profissional individual em empresa grande sem mandato de IA" — que é provavelmente o leitor mais frequente da obra; as personas existentes assumem ou mandato (Executivo, Gestor) ou autonomia (Consultor, Founder).
- Nenhum roadmap referencia o APX-D (ferramentas) ou APX-G (papers) como instrumento de aprofundamento — os apêndices existem em silos sem crosslinks.

## ACHADOS

### ACHADO 01
Categoria: P0
Problema: Roadmap 6 (Criador de Conteúdo), Marco 90 dias: "Biblioteca pessoal de prompts publicada" como artefato esperado
Por que é um problema: contradição direta com a tese central da obra — o livro explicitamente ensina método, não prompts; orientar o criador de conteúdo a publicar biblioteca de prompts transforma o leitor em exatamente o tipo de produtor de conteúdo que o livro critica
Impacto no leitor: leitor que aplica o roadmap literalmente produz artefato que contraria o posicionamento da obra; dano de reputação para o autor se citado fora de contexto
Correção exata: substituir "Biblioteca pessoal de prompts publicada" por "Biblioteca de frameworks e critérios de decisão publicados — cada framework com princípio associado, não prompt isolado"
Texto sugerido: "Marco 90 dias, Persona 6: Artefato → Biblioteca de frameworks de decisão publicada (ex.: como aplicar o Diagnóstico de Encaixe por vertical), não lista de prompts"
ROI: ALTO

### ACHADO 02
Categoria: P1
Problema: ausência de persona para "Profissional individual sem mandato de IA em empresa grande"
Por que é um problema: esta é provavelmente a persona modal do livro (analista sênior, especialista funcional, product manager em empresa que ainda não tem estratégia de IA definida); as personas existentes assumem mandato ou autonomia que esta pessoa não tem
Impacto no leitor: leitor mais frequente não encontra caminho aplicável; pode concluir que o livro não é para ele
Correção exata: adicionar Roadmap 7 — "Profissional Individual / IC (Individual Contributor)" com foco em aplicação dentro do escopo próprio sem mandato organizacional; marcos menores, artefatos pessoais, critérios de avanço de competência, não de governança
Texto sugerido: n/a (requer desenvolvimento completo de 4 marcos)
ROI: ALTO

### ACHADO 03
Categoria: P1
Problema: nenhum roadmap cita os outros apêndices como instrumento de aprofundamento
Por que é um problema: o APX-C é o roadmap operacional da obra, mas opera em silo; leitor não sabe que APX-D tem critérios de seleção de ferramentas, APX-G tem papers por tema
Impacto no leitor: subutilização dos apêndices de referência; coerência entre apêndices fica implícita
Correção exata: adicionar coluna "Recursos recomendados" às tabelas de marcos, com remissivas explícitas a APX-D (para marcos técnicos), APX-G (para marcos de aprofundamento), APX-E (para marcos de fundamentação)
Texto sugerido: n/a (ajuste de tabela)
ROI: MÉDIO

### ACHADO 04
Categoria: P1
Problema: Roadmap do Executivo, Marco 365 dias — "Vocabulário dos Princípios incorporado em reuniões executivas" é critério cultural não auditável
Por que é um problema: todos os outros critérios de avanço são verificáveis (auditoria aprovada, dashboard em produção, maturidade nível 3); este critério é impressionístico e não serve como gate
Impacto no leitor: executivo não sabe se avançou ou não
Correção exata: substituir por critério auditável: "Em pelo menos duas decisões de IA documentadas no período, o princípio violado/aplicado foi nominalmente identificado em ata ou documento de decisão"
Texto sugerido: n/a
ROI: MÉDIO

### ACHADO 05
Categoria: P2
Problema: Roadmap 4 (Consultor), Marco 365 dias: "Dez ou mais clientes operando pelo método" sem baseline contextual
Por que é um problema: meta absoluta não calibrada ao contexto (consultor solo, butique, grande empresa)
Impacto no leitor: meta parece arbitrária; pode desanimar consultor solo ou ser trivial para empresa maior
Correção exata: substituir por meta relativa: "Portfólio ativo com pelo menos três clientes aplicando o método como norma, com case documentado por cada um"
Texto sugerido: n/a
ROI: BAIXO

## TESTE DA JOANA
Entenderia: SIM
O que ela entenderia: sua persona (Executivo), os marcos de 30/90/180/365, os artefatos esperados, os critérios de avanço
O que ela NÃO entenderia: "Escala de Propriedade do Agente" no Roadmap do Dev e do Founder sem remissiva ao capítulo; "CI" no roadmap do Dev sem expansão (Continuous Integration)
Como corrigir: expandir siglas e adicionar remissivas ao capítulo correspondente na primeira ocorrência

## TESTE DE DURABILIDADE
Classificação: ALTA
2 anos / 5 anos / 10 anos: alta — roadmaps orientados por princípios e artefatos (RACI, golden set, auditoria) são estruturalmente duráveis; nenhuma referência a ferramenta específica ou versão de modelo
Justificativa: os marcos de 30/90/180/365 são padrão de gestão de mudança, não calendário de produto

## TESTE DE DIFERENCIAÇÃO
Classificação: DIFERENCIADO
Justificativa: roadmaps por persona com critério de avanço auditável são raros em livros de IA; o formato aproxima a obra de um guia de implementação, não apenas de leitura

## TESTE DE MEMORIZAÇÃO
Ideia principal clara? SIM
Qual é a ideia principal (em 1 frase): cada persona tem um caminho de 365 dias para instalar o método na prática
Justificativa: estrutura 30/90/180/365 é memorável e aplicável

## TESTE DE TRANSFORMAÇÃO
Ao terminar, o leitor consegue fazer o que antes não conseguia:
- Montar seu plano de 365 dias baseado na persona mais próxima do seu contexto
- Saber exatamente qual artefato produzir em cada marco
- Auditar seu próprio progresso com critérios objetivos

## NOTA FINAL
Estrutura: 8 | Pedagogia: 8 | Clareza: 8 | Autoridade: 7 | Durabilidade: 9 | Diferenciação: 8 | Memorização: 8 | Transformação: 8
**Nota Geral: 8.0**

## DECISÃO EDITORIAL
MANTER COM AJUSTES

---

## LINHAS-TRACKER
```
APX-C|L1-APX-C-roadmaps.md|01|P0|ALTO|Roadmap 6 orienta publicação de biblioteca de prompts — contradiz tese central|Substituir por biblioteca de frameworks de decisão|MANTER COM AJUSTES
APX-C|L1-APX-C-roadmaps.md|02|P1|ALTO|Ausência de persona para profissional individual sem mandato|Adicionar Roadmap 7 — IC / Profissional Individual|MANTER COM AJUSTES
APX-C|L1-APX-C-roadmaps.md|03|P1|MÉDIO|Roadmaps não referenciam outros apêndices como instrumento de aprofundamento|Adicionar coluna de recursos por marco com remissivas|MANTER COM AJUSTES
APX-C|L1-APX-C-roadmaps.md|04|P1|MÉDIO|Critério cultural não auditável no Marco 365 do Executivo|Substituir por critério verificável em ata ou documento|MANTER COM AJUSTES
APX-C|L1-APX-C-roadmaps.md|05|P2|BAIXO|Meta absoluta de 10 clientes sem baseline contextual no Roadmap do Consultor|Substituir por meta relativa (3 clientes com case)|MANTER COM AJUSTES
```

---

# APX-D — L1-APX-D-ferramentas.md

## RESUMO EXECUTIVO
Nota: 7/10
Veredito: B

## O QUE FUNCIONA
- A decisão de datar explicitamente o apêndice ("Estado: junho de 2026") e declarar que a lista envelhece é a escolha mais inteligente e corajosa do apêndice — pouquíssimos livros técnicos têm esta honestidade.
- D.0 (Por que este apêndice precisa de data e critério) é parágrafo editorial excelente — posiciona o apêndice como anti-padrão da lista descuidada; poderia ser citado em qualquer livro de referência técnica.
- D.1 (Critério quantitativo em seis dimensões) é o ativo principal do apêndice — criterio de "Encaixe com stack brasileira" (LGPD, PIX, pt-BR) diferencia da maioria das listas em inglês; "Sinais de risco" por dimensão é pedagogia aplicada.
- A categoria D.4 (frameworks de agente) inclui nota honesta sobre trade-off framework opinado vs. abstração leve — evita o viés de endorsement.
- D.8 (MCP) tem nota de armadilha correta: "servidor MCP sem governança de versão" e "client sem confirmação humana antes de tool com efeito" são preocupações reais, não genéricas.

## O QUE NÃO FUNCIONA
- ALERTA DE DURABILIDADE ATIVADO: D.2 lista DeepSeek API com nota "viés geopolítico para discutir conforme caso" — fraseamento vago que não orienta decisão; em seis meses, o contexto geopolítico pode ter mudado radicalmente e a frase não dá critério de avaliação.
- D.3 (open weights): Llama 3.3/4 tem nota "licença com restrição de uso comercial em grande escala" — a licença Llama muda a cada geração e já mudou entre Llama 2 e 3; este é o ponto de maior risco de envelhecimento do apêndice.
- D.9 (gestão de prompts): "Pezzo" aparece como "maduro" mas tem histórico de abandono de versões; incluir ferramenta com historico de breaking changes sem nota é risco; adicionalmente, Pezzo não tem escala comparável aos outros itens da lista.
- Falta categoria para "Plataformas de IA corporativa" (ex.: Microsoft Copilot Studio, Google Vertex AI Agent Builder, Amazon Bedrock Agents) — que são as plataformas mais relevantes para o perfil Executivo e Gestor do APX-C; o apêndice tem viés implícito de desenvolvedor.
- D.10 (cadência de revisão) menciona "Editor desta lista: Fabio Garcia" — informação pessoal que não pertence ao corpo do texto de um apêndice; é informação de colofão ou de nota de rodapé.
- A regra "ferramenta abaixo de 6 em qualquer dimensão crítica é candidata duvidosa" em D.1 usa nota 0-10 sem escala explícita — o que é 6 em "Maturidade"? O critério qualitativo é descrito nas colunas mas sem exemplos de pontuação.

## ACHADOS

### ACHADO 01
Categoria: P0
Problema: fraseamento sobre DeepSeek API ("viés geopolítico para discutir conforme caso") não dá critério de avaliação e pode envelhecer mal em qualquer direção
Por que é um problema: "para discutir conforme caso" é instrução vazia — não orienta; e dependendo de quando o leitor lê, o contexto pode ter evoluído para maior restrição ou maior adoção; a frase deixa o autor exposto a interpretações fora de controle
Impacto no leitor: leitor executivo fica sem orientação real sobre risco geopolítico
Correção exata: substituir por critério durável: "Avalie origem geopolítica do provedor como dimensão de risco no D.1 — pergunte: qual o regime de dados do país de origem? Há restrições regulatórias no setor de atuação? Há precedente de descontinuação por decisão política?"
Texto sugerido: na linha do DeepSeek: "Notas: preço-qualidade agressivo; avalie risco geopolítico via critério D.1 (origem do provedor, regime de dados, restrições setoriais) antes da adoção em produção corporativa."
ROI: ALTO

### ACHADO 02
Categoria: P1
Problema: licença da família Llama descrita como fato fixo; a licença Llama muda a cada geração e já mudou entre Llama 2 e 3
Por que é um problema: leitor que adota Llama 4 ou Llama 5 sem verificar licença comete erro legal; o apêndice, ao afirmar estado, cria falsa segurança
Impacto no leitor: decisão legal baseada em informação desatualizada
Correção exata: substituir afirmação de estado por instrução de verificação: "Llama: verificar licença da versão específica em uso em llama.meta.com — a licença muda entre gerações e pode ter restrições de uso comercial em escala"
Texto sugerido: na célula Notas do Llama: "Verificar licença da versão específica; histórico de mudança entre gerações."
ROI: ALTO

### ACHADO 03
Categoria: P1
Problema: ausência de categoria para plataformas de IA corporativa (Copilot Studio, Vertex AI Agent Builder, Bedrock Agents)
Por que é um problema: o perfil Executivo e Gestor do APX-C chega ao APX-D e não encontra referência ao universo de plataformas que provavelmente já usa ou avalia; o apêndice tem viés implícito de desenvolvedor que exclui 2 das 6 personas
Impacto no leitor: executivo e gestor ficam sem orientação de escolha no apêndice mais aplicado da obra
Correção exata: adicionar D.2B — "Plataformas de IA corporativa (no-code / low-code)" com critérios de armadilha específicos (lock-in de ecossistema, custo por assento vs. por uso, governança de dados)
Texto sugerido: n/a (requer nova seção)
ROI: MÉDIO

### ACHADO 04
Categoria: P1
Problema: critério de pontuação D.1 usa nota 0-10 sem escala ou exemplos de calibração por dimensão
Por que é um problema: "nota 0-10 por dimensão" sem âncora de calibração não é critério objetivo — dois avaliadores diferentes darão notas diferentes para a mesma ferramenta; a promessa de objetividade do apêndice não é cumprida
Impacto no leitor: leitor aplica o critério e obtém resultado dependente de interpretação subjetiva
Correção exata: adicionar 1–2 âncoras por dimensão: ex. em "Maturidade" — "10 = LTS declarado, 3+ anos de mercado, menos de 1 breaking change por ano; 5 = produto lançado há 12–24 meses, sem LTS; 1 = lançado há menos de 6 meses, sem versão estável"
Texto sugerido: n/a (requer expansão da tabela D.1)
ROI: MÉDIO

### ACHADO 05
Categoria: P2
Problema: "Editor desta lista: Fabio Garcia. Revisão periódica..." em D.10 é informação de colofão no corpo do apêndice
Por que é um problema: quebra o padrão editorial do livro; informação de autoria pertence ao colofão ou à página de créditos, não ao fim de um apêndice
Impacto no leitor: pequena — mas parece texto de blog, não de obra editada
Correção exata: mover para nota de rodapé ou remover; a informação sobre canal de contribuição já está em D.10 de forma adequada
Texto sugerido: n/a (remoção da última linha de D.10)
ROI: BAIXO

### ACHADO 06
Categoria: P2
Problema: D.9 inclui "Pezzo" como "maduro, open source" sem nota sobre histórico de abandono e atividade recente do projeto
Por que é um problema: Pezzo teve período de baixa atividade no repositório; incluí-lo sem ressalva ao lado de Langfuse (claramente mais ativo) pode induzir adoção de ferramenta que pode ser descontinuada
Impacto no leitor: risco operacional baixo mas real para quem adotar Pezzo em produção
Correção exata: adicionar nota: "Verificar atividade do repositório antes da adoção — histórico de contribuição irregular."
Texto sugerido: na linha Pezzo: "Estado: verificar atividade atual do repositório; adoção menor que Langfuse."
ROI: BAIXO

## TESTE DA JOANA
Entenderia: SIM (com dificuldade)
O que ela entenderia: D.0 e D.1 — a lógica de por que usar critério em vez de lista; os critérios de armadilha por categoria
O que ela NÃO entenderia: D.4 (frameworks de agente) — LangChain, AutoGen, CrewAI, Pydantic AI são nomes sem contexto suficiente para quem nunca viu código; D.5 (bancos vetoriais) — "HNSW, IVF" aparecem sem expansão de sigla
Como corrigir: adicionar 1 linha de analogia por categoria: ex. D.4 "frameworks de agente são como sistemas operacionais para IA — determinam como as peças se conectam, não o que a IA sabe"

## TESTE DE DURABILIDADE
Classificação: MÉDIA
2 anos: médio risco — D.2 (inferência) e D.3 (open weights) têm entrada de estado que pode estar desatualizada em 12 meses
5 anos: alto risco — categorias inteiras podem mudar (D.9 gestão de prompts pode ser absorvida por observabilidade; D.8 MCP pode ser substituído por protocolo de segunda geração)
10 anos: D.1 (critério em 6 dimensões) e D.0 (filosofia do apêndice) sobrevivem; tudo que é estado de ferramenta específico, não
Justificativa: o apêndice reconhece o próprio risco de envelhecimento em D.0 — mérito editorial; mas a solução (data + revisão periódica) não imuniza o texto; a blindagem real é o critério D.1, não a lista

## TESTE DE DIFERENCIAÇÃO
Classificação: DIFERENCIADO
Justificativa: D.1 com critério quantitativo em seis dimensões calibrado para stack brasileira é genuinamente diferenciado; nenhum livro de IA em português faz isso com esta precisão

## TESTE DE MEMORIZAÇÃO
Ideia principal clara? SIM
Qual é a ideia principal (em 1 frase): aplique o critério de seis dimensões antes de adotar qualquer ferramenta; a lista é instância do critério, não substituto
Justificativa: D.0 e D.1 comunicam isso claramente; o risco é que o leitor pule para as listas e ignore o critério

## TESTE DE TRANSFORMAÇÃO
Ao terminar, o leitor consegue fazer o que antes não conseguia:
- Avaliar qualquer ferramenta nova com o critério D.1, independente de qual ferramenta surgir depois da publicação do livro
- Identificar sinais de armadilha por categoria antes de adotar uma ferramenta
- Justificar escolha de ferramenta para stack brasileira com critérios explícitos

## NOTA FINAL
Estrutura: 8 | Pedagogia: 7 | Clareza: 7 | Autoridade: 8 | Durabilidade: 6 | Diferenciação: 8 | Memorização: 7 | Transformação: 8
**Nota Geral: 7.4**

## DECISÃO EDITORIAL
MANTER COM AJUSTES

---

## LINHAS-TRACKER
```
APX-D|L1-APX-D-ferramentas.md|01|P0|ALTO|DeepSeek com "viés geopolítico para discutir conforme caso" sem critério de avaliação|Substituir por critério durável de avaliação de risco geopolítico via D.1|MANTER COM AJUSTES
APX-D|L1-APX-D-ferramentas.md|02|P1|ALTO|Licença Llama descrita como fato fixo; muda a cada geração|Substituir por instrução de verificação na fonte oficial|MANTER COM AJUSTES
APX-D|L1-APX-D-ferramentas.md|03|P1|MÉDIO|Ausência de categoria para plataformas corporativas no-code/low-code|Adicionar D.2B com Copilot Studio, Vertex AI, Bedrock Agents|MANTER COM AJUSTES
APX-D|L1-APX-D-ferramentas.md|04|P1|MÉDIO|Critério D.1 sem âncoras de calibração por dimensão|Adicionar 2 âncoras por dimensão na tabela D.1|MANTER COM AJUSTES
APX-D|L1-APX-D-ferramentas.md|05|P2|BAIXO|"Editor desta lista: Fabio Garcia" no corpo do apêndice|Mover para colofão ou remover|MANTER COM AJUSTES
APX-D|L1-APX-D-ferramentas.md|06|P2|BAIXO|Pezzo listado como maduro sem nota sobre atividade irregular do repositório|Adicionar nota de verificação de atividade|MANTER COM AJUSTES
```

---

# APX-E — L1-APX-E-leituras.md

## RESUMO EXECUTIVO
Nota: 6/10
Veredito: B

## O QUE FUNCIONA
- A estrutura em três blocos (Fundamentos, IA aplicada, Governança/operação) é coerente com a arquitetura da obra — cada bloco tem correspondência direta com as trilhas temáticas do APX-B.
- Engelbart (*Augmenting Human Intellect*, 1962) como origem filosófica da obra é escolha editorial correta e diferenciada — ancora o livro em genealogia intelectual respeitável e não óbvia.
- Beyer et al. (*SRE*) e Allspaw & Robbins (*Web Operations*) como referências de operação madura para LLMOps é uma ponte conceitual acertada — mostra que o problema não é novo, só o substrato muda.
- A nota sobre Karpathy ("Não é livro formal, mas o conjunto vale como referência") é honesta e pedagogicamente útil — o autor não infla o status de um recurso para preencher lista.

## O QUE NÃO FUNCIONA
- O apêndice é curtíssimo para o espaço que ocupa — apenas 29 linhas de conteúdo; não há comentário por entrada, somente título e breve caracterização, o que torna difícil para o leitor decidir o que priorizar.
- A seção "Blogs e newsletters" duplica conteúdo que aparece em detalhamento muito maior no APX-F — a presença dos mesmos itens (Latent Space, Import AI, Karpathy, Simon Willison) em dois apêndices sem remissiva cria redundância e confusão sobre qual apêndice consultar.
- A seção "Cursos" mistura cursos formais (Stanford CS25, MIT 6.5940) com repositórios de exemplos (OpenAI cookbook, Anthropic courses no GitHub) sem distinção de formato ou profundidade — um leitor executivo não consegue inferir qual investimento de tempo cada item exige.
- Davenport (*The AI Advantage*, 2018) é o único livro de gestão corporativa de IA na lista — e é livro de 2018, escrito antes de LLMs dominarem o campo; a ausência de referência mais recente (ex.: *Co-Intelligence* de Mollick, 2024; *Competing in the Age of AI* de Iansiti & Lakhani, 2020) é lacuna séria dado o perfil executivo da obra.
- *Co-Intelligence* e *Competing in the Age of AI* são parte da régua de comparação da rubrica (citados explicitamente) mas não aparecem no APX-E — omissão que enfraquece a autoridade da obra ao não reconhecer seus pares de mercado.

## ACHADOS

### ACHADO 01
Categoria: P1
Problema: *Co-Intelligence* (Mollick, 2024) e *Competing in the Age of AI* (Iansiti & Lakhani, 2020) ausentes do APX-E apesar de constarem na régua de comparação da rubrica da própria obra
Por que é um problema: a obra posiciona-se acima desses títulos — mas não os citar os torna invisíveis para o leitor; pior, deixa a impressão de que o autor desconhece os peers diretos
Impacto no leitor: leitor executivo que pesquisou o tema antes de comprar o livro estranha a ausência; leitor que busca aprofundamento não encontra os títulos mais discutidos em 2024–2026
Correção exata: adicionar subseção "Livros — IA e trabalho do conhecimento" com Mollick, Iansiti & Lakhani e outros peers diretos, com nota curta de diferenciação em relação à obra
Texto sugerido: "**Mollick, E. — *Co-Intelligence: Living and Working with AI* (2024).** Peer direto desta obra no posicionamento de IA para profissional do conhecimento. Foco em uso individual; esta obra complementa com método organizacional e operação em produção."
ROI: ALTO

### ACHADO 02
Categoria: P1
Problema: seção "Blogs e newsletters" duplica conteúdo do APX-F sem remissiva ou distinção de propósito
Por que é um problema: leitor não sabe por que a mesma lista aparece em dois apêndices; o APX-F trata especificamente da cena brasileira e detalha cada fonte; o APX-E apenas lista nomes sem diferenciação de contexto
Impacto no leitor: confusão de navegação; cria sensação de conteúdo de relleno
Correção exata: na seção "Blogs e newsletters" do APX-E, substituir a lista por remissiva direta: "Para curadoria comentada de newsletters e podcasts, ver o Apêndice F. Para fontes técnicas internacionais de referência, as principais são: [manter apenas 3–4 fontes técnicas fundamentais como arXiv, OpenAI blog, Anthropic blog]"
Texto sugerido: "> Para curadoria completa de newsletters, podcasts e comunidades, ver Apêndice F — Comunidade Brasileira de IA. As fontes técnicas primárias internacionais para acompanhamento contínuo são: blog da Anthropic, blog da OpenAI, blog do Google DeepMind e arXiv (cs.CL, cs.AI)."
ROI: MÉDIO

### ACHADO 03
Categoria: P1
Problema: cursos misturados com repositórios de exemplos sem distinção de formato, profundidade ou investimento de tempo
Por que é um problema: "Stanford CS25 Transformers United" exige pré-requisito matemático e ~40 horas; "OpenAI cookbook" é repositório de snippets para dev; colocar os dois na mesma lista sem hierarquia é desorientador
Impacto no leitor: executivo ou gestor pode tentar Stanford CS25 e desistir; desenvolvedor pode subestimar MIT 6.5940
Correção exata: separar em dois blocos — "Cursos estruturados" e "Recursos práticos e repositórios" com nota de pré-requisito por item
Texto sugerido: n/a (reorganização da seção)
ROI: MÉDIO

### ACHADO 04
Categoria: P2
Problema: Davenport (*The AI Advantage*, 2018) como única referência de gestão corporativa de IA — pré-LLM
Por que é um problema: o contexto de 2018 é pré-transformação generativa; o livro não cobre LLMs, agentes, prompt engineering ou qualquer conceito central desta obra; usá-lo como referência de gestão de IA cria descontinuidade conceitual
Impacto no leitor: leitor que ler Davenport em busca de complementação encontrará lacuna enorme
Correção exata: manter Davenport com nota: "Visão pré-LLM, útil para contexto histórico de adoção corporativa; complementar com [Iansiti & Lakhani, 2020] para perspectiva mais recente"
Texto sugerido: adicionar "(contexto pré-LLM — útil para entender adoção corporativa de IA preditiva, base para comparar com o momento atual)" ao lado de Davenport
ROI: BAIXO

## TESTE DA JOANA
Entenderia: SIM (mas sem ajuda de priorização)
O que ela entenderia: os títulos e autores; a estrutura por categoria
O que ela NÃO entenderia: qual livro ler primeiro; qual é mais urgente vs. mais profundo; a diferença entre *Deep Learning* (Goodfellow) e *Deep Learning: Foundations and Concepts* (Bishop) — dois títulos quase idênticos na mesma lista
Como corrigir: adicionar sistema de marcação de prioridade — ex. ● imprescindível, ○ complementar, por perfil de leitor

## TESTE DE DURABILIDADE
Classificação: ALTA
2 anos / 5 anos / 10 anos: alta para livros técnicos clássicos (Goodfellow, Russell & Norvig, SRE); média para IA aplicada (Davenport, Christian, Russell); blogs e cursos são os de maior risco de envelhecimento
Justificativa: livros acadêmicos de fundamento sobrevivem bem; o risco está nos cursos de plataforma (LangChain pode mudar; cursos de produto específico podem ser descontinuados)

## TESTE DE DIFERENCIAÇÃO
Classificação: COMMODITY
Justificativa: lista de leituras semelhante a dezenas de outros livros e posts de blog de IA; o diferencial potencial seria a nota de posicionamento comparativo (por que este livro em relação ao peer), que está ausente

## TESTE DE MEMORIZAÇÃO
Ideia principal clara? NÃO
Qual é a ideia principal (em 1 frase): não há — é lista sem critério de prioridade explícito
Justificativa: o leitor termina sem saber o que ler primeiro ou como sequenciar a leitura

## TESTE DE TRANSFORMAÇÃO
Ao terminar, o leitor consegue fazer o que antes não conseguia:
- Localizar títulos de referência por categoria
- (sem critério de prioridade ou sequência, a transformação é limitada a identificar títulos, não a montar trilha de aprendizado)

## NOTA FINAL
Estrutura: 6 | Pedagogia: 5 | Clareza: 6 | Autoridade: 6 | Durabilidade: 7 | Diferenciação: 4 | Memorização: 5 | Transformação: 5
**Nota Geral: 5.5**

## DECISÃO EDITORIAL
REVISAR PARCIALMENTE

---

## LINHAS-TRACKER
```
APX-E|L1-APX-E-leituras.md|01|P1|ALTO|Co-Intelligence e Competing in the Age of AI ausentes — são peers diretos da obra|Adicionar subseção com peers e nota de diferenciação|REVISAR PARCIALMENTE
APX-E|L1-APX-E-leituras.md|02|P1|MÉDIO|Seção de blogs/newsletters duplica APX-F sem remissiva|Substituir lista por remissiva ao APX-F + 3-4 fontes essenciais|REVISAR PARCIALMENTE
APX-E|L1-APX-E-leituras.md|03|P1|MÉDIO|Cursos formais misturados com repositórios sem distinção de formato|Separar em dois blocos com nota de pré-requisito|REVISAR PARCIALMENTE
APX-E|L1-APX-E-leituras.md|04|P2|BAIXO|Davenport (2018) sem nota de contexto pré-LLM|Adicionar nota de limitação temporal|REVISAR PARCIALMENTE
```

---

# APX-F — L1-APX-F-newsletters.md

## RESUMO EXECUTIVO
Nota: 8/10
Veredito: A

## O QUE FUNCIONA
- A abertura "A profissão de IA no Brasil tem duas vidas paralelas" é o melhor parágrafo de abertura de qualquer apêndice da obra — cita a tensão real entre o fluxo em inglês e a vida profissional em português; citável, memorável, honesto.
- Seção 7 ("Crítica honesta da cena brasileira") é coragem editorial rara — nomear o que falta (newsletter técnica profunda em português, conferência de IA generativa, blog de engenharia público) é mais valioso do que listar o que existe.
- A distinção entre podcasts dedicados a IA (surgidos 2024–2026) e podcasts de tecnologia ampla com IA recorrente é estruturalmente útil — leitor sabe onde está a densidade técnica maior.
- Data declarada ("Atualizado em: junho de 2026") e próxima revisão programada ("junho de 2027") — padrão consistente com APX-D; resolve o problema de envelhecimento de forma honesta.
- Seção 5 (pesquisadores) inclui nota honesta: "a lista é parcial por escolha" e orienta para base Lattes do CNPq — é instrução de pesca, não de peixe.

## O QUE NÃO FUNCIONA
- ALERTA DE DURABILIDADE ATIVADO: newsletters em português têm altíssima volatilidade — "Tecnologia e IA, com Filipe Deschamps", "The Shift" e "Olhar Digital" podem mudar de cadência, encerrar ou ser adquiridos em menos de 12 meses; nomear indivíduos (Filipe Deschamps, Diego Sommer, Helena Ferraz, Marcus Mendes, Fabrício Carraro) cria risco de desatualização acelerada.
- "Bots Brasil Podcast. Lançado em 2026 pela comunidade Bots Brasil no YouTube" — publicação de 2026 em obra de 2026 é risco extremo de envelhecimento: não há histórico de maturidade para avaliar; pode ter sido descontinuado quando o leitor chega ao apêndice.
- "Grupo de Telegram em torno de MCP em português" — referência genérica sem nome, link ou critério de localização; é non-entry: leitor não consegue encontrar o grupo
- Seção 6 (empresas) lista Magazine Luiza / Luizalabs com nota de "cultura interna de engenharia mais aberta do que a média" — afirmação de caráter organizacional sem fonte verificável; em 2026, o contexto da Magazine Luiza mudou significativamente após reestruturações.
- A nota de como contribuir (Seção 8) menciona "canal oficial da obra, divulgado nos materiais de lançamento e nas redes sociais do autor" sem especificar qual é o canal — instrução incompleta; leitor de ebook lido 2 anos depois do lançamento não sabe onde encontrar o canal.

## ACHADOS

### ACHADO 01
Categoria: P0
Problema: "Bots Brasil Podcast. Lançado em 2026" incluído em obra de 2026 sem histórico de maturidade
Por que é um problema: é o caso mais claro de envelhecimento preemptivo do apêndice: uma publicação de menos de 12 meses de existência incluída como referência permanente; se o podcast encerrar em 2027, o apêndice (escrito em 2026 com revisão programada para 2027) não captura o erro a tempo
Impacto no leitor: referência morta ou irrelevante; corrói credibilidade do apêndice como curadoria confiável
Correção exata: remover Bots Brasil Podcast da lista principal; mover para nota de rodapé com aviso: "surgiu em 2026, ainda sem histórico suficiente para curadoria permanente — verificar estado na próxima revisão"
Texto sugerido: "> Nota: o Bots Brasil Podcast surgiu em 2026 e não tem histórico suficiente para inclusão permanente nesta curadoria. Verificar estado na revisão de junho de 2027."
ROI: ALTO

### ACHADO 02
Categoria: P1
Problema: "Grupo de Telegram em torno de MCP em português" sem nome, link ou critério de localização
Por que é um problema: é non-entry — leitor não pode agir com base na referência; a instrução "existe um grupo" sem como encontrá-lo é pior do que não citar
Impacto no leitor: frustração; sensação de referência incompleta
Correção exata: ou nomear o grupo com critério de localização atual, ou remover a referência e generalizar: "comunidades em formação ao redor de MCP podem ser encontradas via Brasil.AI e grupos de Telegram de Python BR"
Texto sugerido: "Comunidades técnicas em formação ao redor de MCP e agentes em português podem ser encontradas via Brasil.AI (Discord) e grupos de Python BR no Telegram — a cena é fluida; confirmar na próxima revisão."
ROI: MÉDIO

### ACHADO 03
Categoria: P1
Problema: nomes de indivíduos (Filipe Deschamps, Diego Sommer, Helena Ferraz, Marcus Mendes, Fabrício Carraro) criam risco de desatualização se os formatos mudarem ou os apresentadores saírem dos projetos
Por que é um problema: um apêndice com "Diego Sommer e Helena Ferraz" como referência perde validade imediata se um dos dois sair do podcast — em contraste com referências de livro (autor não muda) ou paper (publicação não muda)
Impacto no leitor: leitor encontra descrição desatualizada; credibilidade da curadoria cai
Correção exata: citar o nome do projeto como referência primária e o apresentador como nota secundária — inversão da hierarquia atual; adicionar URL ou forma de localização do projeto como critério mais durável que nome de pessoa
Texto sugerido: "**IA Todo Dia** (disponível em plataformas de podcast). Em junho de 2026, produzido por Diego Sommer e Helena Ferraz. O maior podcast brasileiro dedicado exclusivamente a IA em 2026. [verificar estado na próxima revisão]"
ROI: MÉDIO

### ACHADO 04
Categoria: P1
Problema: Seção 8 cita "canal oficial da obra, divulgado nos materiais de lançamento" sem especificar qual é o canal
Por que é um problema: leitor de ebook em 2028 não tem acesso a "materiais de lançamento"; a instrução de contribuição fica inaplicável no tempo
Impacto no leitor: impossibilidade de contribuição para manutenção do apêndice
Correção exata: especificar URL ou mecanismo de contato permanente (e-mail, repositório, site da obra) — se não existir ainda, adicionar quando criado, mas não deixar a instrução vaga
Texto sugerido: substituir "canal oficial da obra, divulgado nos materiais de lançamento" por URL específica ou e-mail do autor quando disponível
ROI: MÉDIO

### ACHADO 05
Categoria: P2
Problema: Magazine Luiza / Luizalabs descrita como tendo "cultura interna de engenharia mais aberta do que a média do setor" sem fonte verificável
Por que é um problema: é afirmação de caráter organizacional sem evidência citável; em 2026, o contexto da Magazine Luiza após reestruturações pode ter mudado
Impacto no leitor: credibilidade baixa para afirmação sobre cultura interna de empresa privada
Correção exata: substituir por afirmação verificável: "Luizalabs com histórico de publicações técnicas públicas [citar blog ou GitHub] e apresentações em TDC e FEBRABAN Tech"
Texto sugerido: "**Magazine Luiza, no time Luizalabs.** IA em e-commerce, busca, recomendação e atendimento, com histórico de apresentações técnicas públicas em TDC e eventos correlatos."
ROI: BAIXO

## TESTE DA JOANA
Entenderia: SIM
O que ela entenderia: a estrutura de duas vidas (inglês vs. português); a diferença entre podcast dedicado e podcast amplo; a crítica honesta da Seção 7
O que ela NÃO entenderia: "PLN" em NeuralMind ("empresa especializada em PLN") sem expansão (Processamento de Linguagem Natural); "R/Brasil em interseção com r/MachineLearning" — Joana provavelmente não usa Reddit
Como corrigir: expandir PLN; remover referência ao Reddit ou contextualizar com uma linha

## TESTE DE DURABILIDADE
Classificação: BAIXA (para a lista) / ALTA (para a análise crítica)
2 anos: alto risco na lista de newsletters, podcasts e comunidades; baixo risco na estrutura analítica (Seção 7)
5 anos: a maioria das entradas específicas estará desatualizada; a Seção 7 e a distinção "dois fluxos" continuarão válidas
10 anos: apenas a estrutura conceitual sobrevive
Justificativa: o apêndice sabe disso e tem mecanismo de revisão — o problema é que a revisão anual pode não acontecer; o conteúdo de análise crítica deveria ter mais peso relativo que a lista

## TESTE DE DIFERENCIAÇÃO
Classificação: DIFERENCIADO
Justificativa: a Seção 7 (crítica honesta da cena brasileira) é genuinamente diferenciada — nenhum livro de IA em português nomeia explicitamente o que falta na cena nacional; a estrutura "o que melhorou / o que ainda falta" é modelo que o mercado deveria adotar

## TESTE DE MEMORIZAÇÃO
Ideia principal clara? SIM
Qual é a ideia principal (em 1 frase): a cena brasileira de IA em 2026 está crescendo mas ainda exige consumo majoritário em inglês para quem quer estar na fronteira
Justificativa: a tensão "duas vidas" é memorável e honesta

## TESTE DE TRANSFORMAÇÃO
Ao terminar, o leitor consegue fazer o que antes não conseguia:
- Selecionar 2–3 fontes em português alinhadas com seu perfil e cadência de consumo
- Entender onde a cena brasileira ainda está aquém e onde avançou
- Saber onde procurar pesquisadores e grupos de pesquisa nacionais

## NOTA FINAL
Estrutura: 8 | Pedagogia: 8 | Clareza: 8 | Autoridade: 7 | Durabilidade: 5 | Diferenciação: 9 | Memorização: 8 | Transformação: 7
**Nota Geral: 7.5**

## DECISÃO EDITORIAL
MANTER COM AJUSTES

---

## LINHAS-TRACKER
```
APX-F|L1-APX-F-newsletters.md|01|P0|ALTO|Bots Brasil Podcast lançado em 2026 incluído como referência permanente sem histórico|Mover para nota de rodapé com aviso de verificação|MANTER COM AJUSTES
APX-F|L1-APX-F-newsletters.md|02|P1|MÉDIO|Grupo de Telegram sobre MCP sem nome, link ou critério de localização|Generalizar para Brasil.AI/Python BR ou remover|MANTER COM AJUSTES
APX-F|L1-APX-F-newsletters.md|03|P1|MÉDIO|Nomes de indivíduos como referência primária de projetos de podcast|Inverter hierarquia: projeto como primário, apresentador como nota|MANTER COM AJUSTES
APX-F|L1-APX-F-newsletters.md|04|P1|MÉDIO|Canal de contribuição sem URL ou mecanismo permanente especificado|Especificar URL/email permanente|MANTER COM AJUSTES
APX-F|L1-APX-F-newsletters.md|05|P2|BAIXO|Afirmação de cultura organizacional da Magazine Luiza sem fonte|Substituir por afirmação verificável com referência a publicações|MANTER COM AJUSTES
```

---

# APX-G — L1-APX-G-papers.md

## RESUMO EXECUTIVO
Nota: 8/10
Veredito: A

## O QUE FUNCIONA
- Curadoria de 46 papers em oito categorias é coerente com a estrutura temática da obra — cada categoria tem correspondência direta com um ou mais capítulos.
- A nota "Como ler papers de IA" (5 passos) no final é adição pedagógica genuína e diferenciada — nenhum livro de divulgação em português faz isso.
- Categoria VI (Interpretabilidade mecanicista) com três papers da Anthropic/DeepMind é curadoria especializada que a maioria dos livros de IA omite — reforça autoridade técnica da obra.
- Nota de uma linha por paper é o formato correto para curadoria de referência — suficiente para decidir se vale ler, insuficiente para substituir o paper.
- Paper #26 (G-Eval) e #27 (RAGAS) lado a lado em Evals mostra distinção útil entre eval genérico e eval específico de RAG.

## O QUE NÃO FUNCIONA
- Paper #32 ("Anthropic — *Building Effective Agents*, 2024") é guia técnico de documentação oficial, não paper de pesquisa — sua inclusão na mesma lista de Vaswani et al. e Ouyang et al. confunde dois tipos de referência (pesquisa vs. documentação de produto).
- Paper #33 ("Significant Gravitas — *AutoGPT technical reports*, 2023") também não é paper revisado por pares — é repositório GitHub com READMEs e relatórios internos; incluir "Significant Gravitas" como referência ao lado do trabalho de Princeton e Meta enfraquece a autoridade da lista.
- Categoria V (Agentes) não inclui nenhum paper sobre multi-agente além de AutoGen (que está no APX-D mas não no APX-G) — lacuna notável dado que C12 e C22 da obra tratam de agentes e LLMOps.
- Não há paper sobre Context Engineering — conceito que tem capítulo próprio na obra (C11) mas sem referência acadêmica correspondente.
- A nota no final ("Como ler papers de IA") aparece solta, sem título de seção hierárquica — no formato Markdown atual, não tem `##` como todas as outras seções.

## ACHADOS

### ACHADO 01
Categoria: P1
Problema: "Building Effective Agents" (Anthropic, 2024) e "AutoGPT technical reports" (Significant Gravitas, 2023) incluídos na lista de papers sem distinção de que não são papers revisados por pares
Por que é um problema: misturar documentação técnica e relatórios de repositório com pesquisa revisada por pares corrói a autoridade da lista; leitor técnico percebe o problema e questiona a curadoria
Impacto no leitor: perda de confiança na qualidade de filtragem editorial
Correção exata: criar subseção separada em cada categoria para "Documentação técnica e guias de referência" — ou mover esses itens para o APX-H (bibliografia) sob "Documentação técnica oficial"
Texto sugerido: "#32 [mover para APX-H, seção IV, Documentação técnica oficial] Anthropic. *Building Effective Agents* (2024) — guia técnico de referência, não paper."
ROI: ALTO

### ACHADO 02
Categoria: P1
Problema: ausência de referência para Context Engineering (C11 da obra) na curadoria de papers
Por que é um problema: Context Engineering tem capítulo próprio mas nenhum paper correspondente — leitor que quer aprofundar não tem ponto de partida acadêmico; isso também sugere que o capítulo da obra pode estar baseado em documentação técnica e prática de campo, não em literatura revisada por pares
Impacto no leitor: ausência de suporte acadêmico para conceito-chave da obra
Correção exata: adicionar em Categoria II (Contexto e atenção) papers sobre orquestração de contexto — ex. o trabalho de Khattab et al. sobre DSPy (Stanford, 2023), que é a referência mais próxima de engenharia sistemática de contexto; ou adicionar nota honesta: "Context Engineering como disciplina não tem paper seminal consolidado — é campo emergente baseado em prática de campo"
Texto sugerido: "> Nota: Context Engineering como disciplina sistemática não tem paper seminal consolidado em 2026 — a fundamentação é baseada em prática documentada (ver documentação de Anthropic e OpenAI) e nos papers de otimização de prompt de Categoria II."
ROI: MÉDIO

### ACHADO 03
Categoria: P2
Problema: "Como ler papers de IA" sem heading `##` — único bloco sem hierarquia no documento
Por que é um problema: inconsistência de formatação; em leitores de Markdown e ebook, o bloco aparece sem destaque ou como corpo corrido
Impacto no leitor: pequena — problema de apresentação
Correção exata: adicionar `## Como ler papers de IA` antes do bloco
Texto sugerido: n/a (adição de heading)
ROI: BAIXO

### ACHADO 04
Categoria: P2
Problema: Categoria V (Agentes) não inclui paper sobre sistemas multi-agente moderno
Por que é um problema: a obra tem capítulo de Agentes (C12) e LLMOps (C22) que discutem sistemas multi-agente; o único paper sobre coordenação é AutoGPT (que é relatório de repositório, não paper) — gap de cobertura em categoria relevante
Impacto no leitor: leitor que quer aprofundar em multi-agente não tem referência acadêmica
Correção exata: adicionar paper sobre multi-agente — ex. "Park et al. — *Generative Agents: Interactive Simulacra of Human Behavior* (Stanford, 2023)" ou "Chen et al. — *AgentVerse* (2023)"; substituir ou complementar a entrada do AutoGPT
Texto sugerido: "#33 Park, J. et al. — *Generative Agents: Interactive Simulacra of Human Behavior* (Stanford, 2023). Arquitetura de agentes com memória, reflexão e planejamento — referência para design de sistemas multi-agente."
ROI: BAIXO

## TESTE DA JOANA
Entenderia: NÃO (como lista de leitura) / SIM (como referência de autoridade)
O que ela entenderia: a estrutura por categoria; a nota "Como ler papers de IA" — especialmente "Abstract e conclusão primeiro" é instrução direta e aplicável
O que ela NÃO entenderia: a maioria dos títulos técnicos (BERT, FlashAttention, DPO, ORPO, KTO, RAGAS) — sem contexto de por que cada um importa para seu trabalho
Como corrigir: a nota por paper (1–2 linhas) deveria ter versão leiga além da nota técnica — ou adicionar coluna "Para quem" por categoria

## TESTE DE DURABILIDADE
Classificação: ALTA
2 anos / 5 anos / 10 anos: os papers seminais são permanentes por definição (Vaswani, 2017; Brown, 2020; Ouyang, 2022 já são canônicos); papers de 2023–2024 têm mais risco de serem superados mas ainda são referência do estado da arte
Justificativa: papers revisados por pares não "envelhecem" como listas de ferramentas — são registros históricos do desenvolvimento do campo; a curadoria é estruturalmente durável

## TESTE DE DIFERENCIAÇÃO
Classificação: DIFERENCIADO
Justificativa: curadoria de 46 papers com nota por item e seção "Como ler papers" em livro de divulgação é diferencial genuíno; repositório equivalente em língua portuguesa não existe como parte de um livro

## TESTE DE MEMORIZAÇÃO
Ideia principal clara? SIM
Qual é a ideia principal (em 1 frase): os papers que fundamentam a IA generativa, organizados por tema, com instrução de como lê-los
Justificativa: a estrutura em categorias temáticas e a nota final de leitura comunicam o propósito com clareza

## TESTE DE TRANSFORMAÇÃO
Ao terminar, o leitor consegue fazer o que antes não conseguia:
- Identificar qual paper ler para aprofundar qualquer tema específico da obra
- Saber como ler um paper de IA em 20–60 minutos sem perder o conteúdo essencial
- Distinguir papers fundacionais (Vaswani, Brown) de papers de aplicação (RAGAS, G-Eval)

## NOTA FINAL
Estrutura: 8 | Pedagogia: 8 | Clareza: 8 | Autoridade: 8 | Durabilidade: 9 | Diferenciação: 9 | Memorização: 8 | Transformação: 8
**Nota Geral: 8.3**

## DECISÃO EDITORIAL
MANTER COM AJUSTES

---

## LINHAS-TRACKER
```
APX-G|L1-APX-G-papers.md|01|P1|ALTO|Building Effective Agents e AutoGPT misturados com papers revisados por pares|Criar subseção de documentação técnica ou mover para APX-H|MANTER COM AJUSTES
APX-G|L1-APX-G-papers.md|02|P1|MÉDIO|Ausência de referência acadêmica para Context Engineering (C11)|Adicionar nota honesta de campo emergente ou paper DSPy|MANTER COM AJUSTES
APX-G|L1-APX-G-papers.md|03|P2|BAIXO|"Como ler papers" sem heading ## — inconsistência de formatação|Adicionar ## Como ler papers de IA|MANTER COM AJUSTES
APX-G|L1-APX-G-papers.md|04|P2|BAIXO|Categoria Agentes sem paper de multi-agente moderno|Adicionar Park et al. Generative Agents (Stanford, 2023)|MANTER COM AJUSTES
```

---

# APX-H — L1-APX-H-bibliografia.md

## RESUMO EXECUTIVO
Nota: 8/10
Veredito: A

## O QUE FUNCIONA
- Organização em seis seções (papers, livros, normas, documentação, pedagógico, sobre a obra) cobre o espectro completo de referências sem sobreposição óbvia.
- Seção III (Normas, regulação e frameworks) é consistente com o glossário (APX-A, Cat. IX) e com o capítulo de Governança — citação do EU AI Act com número do regulamento (2024/1689) é precisão de referência adequada.
- Seção IV (Documentação técnica oficial) lista URLs com formato limpo e sem "verificado em [data]" — decisão consciente de que URLs de documentação oficial são mais estáveis do que datas de acesso.
- A distinção entre APX-H (fontes primárias e secundárias citadas) e APX-E/F/G (curadoria comentada) está declarada na introdução — organização editorial correta.
- "Schmidhuber, J. — *Annotated History of Modern AI* (recente)" na seção II é escolha interessante, mas "recente" como ano é impreciso.

## O QUE NÃO FUNCIONA
- Seção I, subseção "Filosofia e fundamento" lista três itens: Russell (*Human Compatible*), Christian (*The Alignment Problem*) e Bommasani et al. (*On the Opportunities and Risks of Foundation Models*) — os dois primeiros são livros, o terceiro é um technical report de 200+ páginas do Stanford CRFM; a mistura sem indicação de tipo de referência é imprecisa.
- Schmidhuber (*Annotated History of Modern AI*) com "(recente)" como data é referência não verificável — leitor não consegue localizar a edição correta.
- Drucker (*The Effective Executive*, 1966) e Brooks (*The Mythical Man-Month*, 1975/1995) aparecem na seção II sem contexto de como se relacionam com a obra — são referências implícitas que o leitor não consegue ancorar.
- Kotter (*Leading Change*, 1996) também sem contexto de uso na obra — é citado no roadmap (C26/APX-C?) implicitamente, mas sem remissiva.
- Seção V ("Recursos pedagógicos comentados") consiste em uma única linha de remissiva — seção vazia que não agrega valor; poderia ser removida e a remissiva inserida como nota em seção anterior.
- Narayanan & Kapoor (*Evaluating LLMs is a minefield*, Princeton, 2023) aparece na seção de Evals da Seção I mas não aparece no APX-G (papers); inconsistência entre bibliografia completa e curadoria de papers.

## ACHADOS

### ACHADO 01
Categoria: P1
Problema: Narayanan & Kapoor (*Evaluating LLMs is a minefield*) está na seção H de Evals mas ausente do APX-G (papers de Evals)
Por que é um problema: inconsistência entre dois apêndices de referência da mesma obra — leitor que usa o APX-G como guia de papers não encontra esta referência; leitor que usa o APX-H encontra
Impacto no leitor: gap de navegação entre apêndices
Correção exata: adicionar ao APX-G, Categoria IV (Evals): "#28 Narayanan, A. & Kapoor, S. — *Evaluating LLMs is a minefield* (Princeton, 2023). Análise crítica de como benchmarks podem enganar — antídoto necessário para a seção de evals."
Texto sugerido: ver acima
ROI: MÉDIO

### ACHADO 02
Categoria: P1
Problema: Schmidhuber "*Annotated History of Modern AI* (recente)" — "recente" é data não verificável
Por que é um problema: leitor não consegue localizar a edição correta; em 2026, Schmidhuber pode ter publicado versão 2024 ou 2025 — "recente" não discrimina
Impacto no leitor: referência inutilizável como localização; constrangimento para leitor que tenta citar a obra
Correção exata: pesquisar e inserir ano e URL corretos do documento (publicado no site de Schmidhuber e em arXiv); se não houver versão definitiva, indicar: "disponível em schmidhuber.ch, atualizado periodicamente"
Texto sugerido: "Schmidhuber, J. *Annotated History of Modern AI* (schmidhuber.ch, atualizado periodicamente)"
ROI: MÉDIO

### ACHADO 03
Categoria: P1
Problema: Drucker, Brooks e Kotter aparecem na seção II sem contexto de como são usados na obra
Por que é um problema: são referências implícitas — leitor não entende por que *The Effective Executive* (1966) aparece em um livro sobre IA generativa; a ausência de nota mínima de contextualização torna a lista opaca
Impacto no leitor: leitor questiona coerência editorial; pode interpretar como "enchimento de bibliografia para aparentar erudição"
Correção exata: adicionar nota mínima (parentético) de contextualização: ex. "(fundamento de tomada de decisão sob incerteza, base do Princípio 9)" para Drucker; "(lei de Brooks aplicada a sistemas de IA: adicionar agentes não reduz complexidade proporcionalmente)" para Brooks
Texto sugerido: ex. "Drucker, P. *The Effective Executive* (1966). (Fundamento de tomada de decisão sistemática; base conceitual do Princípio 9 — Operador.)"
ROI: MÉDIO

### ACHADO 04
Categoria: P2
Problema: Seção V ("Recursos pedagógicos comentados") é uma linha de remissiva que não agrega valor como seção própria
Por que é um problema: seção com uma linha de conteúdo diminui a autoridade do documento; parece preenchimento de estrutura
Impacto no leitor: pequena — mas corrói percepção de edição cuidadosa
Correção exata: remover Seção V como seção; inserir a remissiva como nota ao final da Seção IV
Texto sugerido: n/a (remoção de seção)
ROI: BAIXO

### ACHADO 05
Categoria: P2
Problema: Bommasani et al. (*On the Opportunities and Risks of Foundation Models*) misturado com livros na subseção "Filosofia e fundamento"
Por que é um problema: é technical report de 200+ páginas, não livro; categorização incorreta
Impacto no leitor: leitor que tenta "ler o livro" encontra documento muito diferente do que esperava
Correção exata: mover Bommasani et al. para Seção I (Papers seminais), nova subseção "Surveys e foundation reports"
Texto sugerido: n/a (reorganização)
ROI: BAIXO

## TESTE DA JOANA
Entenderia: NÃO (como documento de uso independente)
O que ela entenderia: a estrutura em seções; que este é o "índice de fontes" da obra
O que ela NÃO entenderia: para que serve cada seção; por que Drucker aparece em livro de IA; diferença entre paper, technical report e livro
Como corrigir: a nota introdutória "para curadoria comentada, ver apêndices anteriores" é correta mas insuficiente; adicionar uma linha sobre como usar este apêndice: "consulte este apêndice quando quiser localizar a fonte original de uma afirmação ou conceito"

## TESTE DE DURABILIDADE
Classificação: ALTA
2 anos / 5 anos / 10 anos: alta — referências publicadas são permanentes; os papers existem em arXiv e publicações científicas; os livros existem em edições físicas e digitais; as normas têm versão oficial
Justificativa: bibliografia completa é o apêndice com maior durabilidade estrutural da obra — os papéis e livros citados não mudam; apenas a regulação pode ter versão revisada

## TESTE DE DIFERENCIAÇÃO
Classificação: COMMODITY
Justificativa: toda obra técnica tem bibliografia; o diferencial aqui é a organização por tipo (papers / livros / normas / documentação), que é boa prática editorial mas não é propriedade intelectual da obra

## TESTE DE MEMORIZAÇÃO
Ideia principal clara? SIM (mas não é para memorizar — é para consultar)
Qual é a ideia principal (em 1 frase): todas as fontes primárias e secundárias da obra, em um lugar
Justificativa: cumpre o propósito declarado

## TESTE DE TRANSFORMAÇÃO
Ao terminar, o leitor consegue fazer o que antes não conseguia:
- Localizar a fonte original de qualquer afirmação da obra
- Citar a obra em trabalho acadêmico ou relatório profissional com referências verificáveis
- Distinguir o que na obra é interpretação do autor vs. o que é resultado de pesquisa publicada

## NOTA FINAL
Estrutura: 8 | Pedagogia: 6 | Clareza: 7 | Autoridade: 8 | Durabilidade: 9 | Diferenciação: 5 | Memorização: 7 | Transformação: 7
**Nota Geral: 7.1**

## DECISÃO EDITORIAL
MANTER COM AJUSTES

---

## LINHAS-TRACKER
```
APX-H|L1-APX-H-bibliografia.md|01|P1|MÉDIO|Narayanan & Kapoor ausente do APX-G mas presente no APX-H|Adicionar ao APX-G Categoria IV com nota|MANTER COM AJUSTES
APX-H|L1-APX-H-bibliografia.md|02|P1|MÉDIO|Schmidhuber com "(recente)" como data — referência não verificável|Substituir por URL e indicação de atualização periódica|MANTER COM AJUSTES
APX-H|L1-APX-H-bibliografia.md|03|P1|MÉDIO|Drucker, Brooks, Kotter sem contexto de uso na obra|Adicionar nota parentética de contextualização por item|MANTER COM AJUSTES
APX-H|L1-APX-H-bibliografia.md|04|P2|BAIXO|Seção V com uma linha de remissiva — seção vazia|Remover como seção; inserir remissiva como nota em Seção IV|MANTER COM AJUSTES
APX-H|L1-APX-H-bibliografia.md|05|P2|BAIXO|Bommasani et al. categorizado como livro em Filosofia; é technical report|Mover para Seção I em nova subseção de Surveys|MANTER COM AJUSTES
```

---

# APX-I — L1-APX-I-indice-remissivo.md

## RESUMO EXECUTIVO
Nota: 6/10
Veredito: B

## O QUE FUNCIONA
- Estrutura alfabética com remissiva ao capítulo (em vez de número de página) é a escolha correta para ebook — páginas mudam com o tamanho de fonte; capítulos são estáveis.
- Marcadores ★/◆ consistentes com o glossário (APX-A) — coerência de sistema entre apêndices.
- Entrada "Vibe-eval" com nota "como anti-padrão" é achado editorial correto — contextualiza o termo no índice, não apenas localiza.
- Cobertura razoável dos termos técnicos principais: todos os Nove Princípios estão indexados.

## O QUE NÃO FUNCIONA
- "Datasets de prática — Apêndice K" e "Gabaritos — Apêndice K" referenciam um "Apêndice K" que não existe no sumário visível da obra — os apêndices revisados nesta banca vão de A a I; nenhum K aparece nos arquivos fornecidos. Referência morta.
- "Os Nove Princípios ★ — Introdução; Apêndice M" também referencia "Apêndice M" inexistente — mesmo problema.
- "Prompt — capítulo sobre Engenharia de prompt; Apêndice L; Engenharia de Prompt Estendida" referencia "Apêndice L" igualmente inexistente.
- "Manifesto dos Princípios — Introdução; Apêndice M" — terceira referência ao Apêndice M inexistente.
- Ausência de entrada para "Reasoning models" — capítulo C14B não tem entrada no índice; nem "C14B" nem "reasoning" aparecem.
- Ausência de entrada para "Spec-driven development" — capítulo C14C não tem entrada.
- "LLM-as-judge ★ ◆" tem duplo marcador — é incorreto usar ★ (proprietário da obra) e ◆ (canônico do campo) simultaneamente; o termo foi cunhado pelo campo, não pela obra.
- Letra "N" completamente ausente — não há entradas com N; "Narayanan", "NIST AI RMF", "NeuralMind", "Nine Frameworks" deveriam aparecer.
- Letra "U" ausente — não há entradas começando com U; "UE AI Act" ou "União Europeia" poderiam aparecer.
- Letra "X" ausente — esperado em índice de obra técnica incluir "XAI" ou "explicabilidade" se aparecem nos capítulos.

## ACHADOS

### ACHADO 01
Categoria: P0
Problema: referências a "Apêndice K", "Apêndice L" e "Apêndice M" em índice remissivo quando esses apêndices não existem nos arquivos da obra
Por que é um problema: referências mortas no índice remissivo são erro editorial grave — leitor que segue a remissiva não encontra nada; sugere que o índice foi escrito para uma estrutura da obra que mudou (apêndices foram removidos ou renomeados) sem atualização do índice
Impacto no leitor: frustração direta; corrói confiança na qualidade editorial da obra; em ebook com hyperlinks, links quebrados são experiência de leitura degradada
Correção exata: identificar quais apêndices K, L e M existiam no planejamento original; se foram removidos, atualizar as remissivas para o destino correto; se foram renomeados (ex.: K→ alguma letra existente), mapear e corrigir; se o conteúdo foi absorvido em outros capítulos, remissão deve apontar para esses capítulos
Texto sugerido: auditar estrutura de apêndices da obra e substituir K/L/M por letra correta ou por "ver Capítulo X"
ROI: ALTO

### ACHADO 02
Categoria: P1
Problema: "Reasoning models" e "Spec-driven development" ausentes do índice — capítulos C14B e C14C não têm entrada
Por que é um problema: dois capítulos adicionados ao sumário não foram integrados ao índice remissivo — os capítulos ficam órfãos de navegação; leitor que lembra do conceito e quer voltar ao capítulo não encontra pelo índice
Impacto no leitor: impossibilidade de navegação reversa para C14B e C14C
Correção exata: adicionar entradas:
- "Reasoning models ◆ — C14B; Princípio 1"
- "Spec-driven development — C14C; Princípio 4 e 8"
Texto sugerido: inserir em letra R: "**Reasoning models ◆** — capítulo C14B (Reasoning models); Princípio 1" e em letra S: "**Spec-driven development** — capítulo C14C; Princípios 4 e 8"
ROI: ALTO

### ACHADO 03
Categoria: P1
Problema: "LLM-as-judge ★ ◆" com duplo marcador — contraditório
Por que é um problema: ★ indica termo proprietário da obra; ◆ indica termo canônico do campo; um termo não pode ser as duas coisas; "LLM-as-judge" é termo do campo (primeiro uso documentado em Zheng et al., 2023, paper presente no APX-G), não invenção da obra
Impacto no leitor: confusão sobre o sistema de marcadores; corrói a credibilidade do sistema ★/◆ que é um dos diferenciais do glossário
Correção exata: remover ★, manter apenas ◆ em "LLM-as-judge"; auditar o índice e o glossário para verificar se há outros casos de duplo marcador
Texto sugerido: "**LLM-as-judge ◆** — capítulo sobre Evals; Pirâmide da Avaliação"
ROI: MÉDIO

### ACHADO 04
Categoria: P1
Problema: letras N, U ausentes do índice — vários termos importantes não indexados
Por que é um problema: "NIST AI RMF" está no APX-H (bibliografia) e no APX-A (glossário) mas não no índice remissivo; leitor que quer localizar NIST no corpo da obra não consegue pelo índice
Impacto no leitor: navegação incompleta para termos de regulação e governança
Correção exata: auditar o índice contra o glossário (APX-A) — todo termo do glossário deveria ter entrada correspondente no índice; adicionar no mínimo: "NIST AI RMF — capítulo sobre Governança; APX-A; APX-H"
Texto sugerido: adicionar seção ## N com "**NIST AI RMF** — capítulos sobre Governança e Segurança; APX-A (Regulação); APX-H"
ROI: MÉDIO

### ACHADO 05
Categoria: P2
Problema: "Golden set ★ ◆" no índice tem duplo marcador — mesmo problema do LLM-as-judge
Por que é um problema: Golden set é termo do campo de ML (não proprietário da obra); usar ★ é impreciso
Impacto no leitor: mesmo que em APX-I — mas também aparece assim em APX-A, exigindo correção coordenada
Correção exata: remover ★ de "Golden set" — manter apenas ◆; verificar APX-A para consistência
Texto sugerido: "**Golden set ◆** — capítulo sobre Evals; Pirâmide da Avaliação"
ROI: BAIXO

### ACHADO 06
Categoria: P2
Problema: "Atlas Strategy" e "Banco Solar" presentes como casos mas "Pólice.io" e "Vianna, Castro e Almeida" têm entradas inconsistentes — no índice "Pólice.io (caso)" está no índice mas não aparece em "P" com ortografia consistente com APX-A (que usa "Pólice.io")
Por que é um problema: inconsistência ortográfica entre apêndices do mesmo livro
Impacto no leitor: pequena, mas corrói coerência
Correção exata: verificar ortografia de todos os casos brasileiros entre APX-A, APX-I e os capítulos correspondentes
Texto sugerido: n/a (auditoria de consistência)
ROI: BAIXO

## TESTE DA JOANA
Entenderia: SIM (como instrumento de navegação)
O que ela entenderia: que é índice; como usá-lo para encontrar termos; as remissivas ao capítulo
O que ela NÃO entenderia: por que as letras N e U não existem; os marcadores ★ e ◆ sem legenda no próprio índice (a legenda está no glossário, não no índice)
Como corrigir: adicionar nota de rodapé no cabeçalho do índice: "★ = termo proprietário da obra; ◆ = termo técnico canônico do campo"

## TESTE DE DURABILIDADE
Classificação: ALTA (estruturalmente) / BAIXA (para remissivas a apêndices inexistentes)
2 anos / 5 anos / 10 anos: índice remissivo é documento estável se a estrutura da obra não mudar; o problema são as referências mortas a K, L, M que degradam a experiência desde o primeiro dia
Justificativa: o problema de durabilidade aqui não é envelhecimento — é consistência interna atual

## TESTE DE DIFERENCIAÇÃO
Classificação: COMMODITY
Justificativa: todo livro técnico tem índice remissivo; este tem cobertura razoável mas com falhas de consistência; não é diferencial da obra

## TESTE DE MEMORIZAÇÃO
Ideia principal clara? SIM (é instrumento, não conteúdo)
Qual é a ideia principal (em 1 frase): onde encontrar cada conceito na obra
Justificativa: cumpre o propósito com eficácia parcial (falhas de cobertura e remissivas mortas reduzem a utilidade)

## TESTE DE TRANSFORMAÇÃO
Ao terminar, o leitor consegue fazer o que antes não conseguia:
- Localizar onde qualquer conceito principal da obra é aprofundado
- (as remissivas mortas e os capítulos órfãos reduzem a utilidade prática)

## NOTA FINAL
Estrutura: 6 | Pedagogia: 6 | Clareza: 7 | Autoridade: 5 | Durabilidade: 6 | Diferenciação: 4 | Memorização: 7 | Transformação: 6
**Nota Geral: 5.9**

## DECISÃO EDITORIAL
REVISAR PARCIALMENTE

---

## LINHAS-TRACKER
```
APX-I|L1-APX-I-indice-remissivo.md|01|P0|ALTO|Referências mortas a Apêndice K, L e M — apêndices inexistentes|Auditar estrutura de apêndices e corrigir todas as remissivas|REVISAR PARCIALMENTE
APX-I|L1-APX-I-indice-remissivo.md|02|P1|ALTO|Reasoning models e Spec-driven development ausentes do índice|Adicionar entradas para C14B e C14C em letras R e S|REVISAR PARCIALMENTE
APX-I|L1-APX-I-indice-remissivo.md|03|P1|MÉDIO|LLM-as-judge com duplo marcador ★ ◆ — contraditório|Remover ★; manter ◆; auditar outros casos de duplo marcador|REVISAR PARCIALMENTE
APX-I|L1-APX-I-indice-remissivo.md|04|P1|MÉDIO|Letras N e U ausentes — NIST AI RMF e outros termos não indexados|Adicionar seção N com NIST AI RMF e outros termos ausentes|REVISAR PARCIALMENTE
APX-I|L1-APX-I-indice-remissivo.md|05|P2|BAIXO|Golden set com duplo marcador ★ ◆ — mesmo problema do LLM-as-judge|Remover ★; auditar APX-A para consistência|REVISAR PARCIALMENTE
APX-I|L1-APX-I-indice-remissivo.md|06|P2|BAIXO|Inconsistência ortográfica dos casos brasileiros entre apêndices|Auditar todos os casos (Pólice.io, Atlas, Banco Solar, Vianna Castro) entre APX-A e APX-I|REVISAR PARCIALMENTE
```

---

# CONSOLIDADO FINAL — APX-A a APX-I

## Tabela de Totais por Apêndice

| Apêndice | Nota | Veredito | P0 | P1 | P2 | Decisão |
|----------|------|----------|----|----|-----|---------|
| APX-A Glossário | 7.9 | A | 0 | 3 | 3 | MANTER COM AJUSTES |
| APX-B Mapa Mental | 8.6 | A | 0 | 2 | 2 | MANTER COM AJUSTES |
| APX-C Roadmaps | 8.0 | B | 1 | 3 | 1 | MANTER COM AJUSTES |
| APX-D Ferramentas | 7.4 | B | 1 | 3 | 2 | MANTER COM AJUSTES |
| APX-E Leituras | 5.5 | B | 0 | 3 | 1 | REVISAR PARCIALMENTE |
| APX-F Newsletters | 7.5 | A | 1 | 3 | 1 | MANTER COM AJUSTES |
| APX-G Papers | 8.3 | A | 0 | 2 | 2 | MANTER COM AJUSTES |
| APX-H Bibliografia | 7.1 | A | 0 | 3 | 2 | MANTER COM AJUSTES |
| APX-I Índice Remissivo | 5.9 | B | 1 | 3 | 2 | REVISAR PARCIALMENTE |
| **TOTAL** | **7.4** | | **3** | **25** | **16** | |

## Issues Críticos Transversais (afetam múltiplos apêndices)

1. **Apêndices K, L, M referenciados mas inexistentes** (APX-I) — erro estrutural que requer auditoria da arquitetura completa dos apêndices; qual era o plano original? O que foi removido?

2. **C14B (Reasoning models) e C14C (Spec-driven development) não integrados** aos apêndices de mapa mental (APX-B), glossário (APX-A) e índice remissivo (APX-I) — capítulos órfãos que precisam de atualização coordenada nos três apêndices.

3. **Duplicação entre APX-E e APX-F** — a seção de blogs/newsletters do APX-E duplica conteúdo do APX-F sem remissiva; requer decisão editorial sobre qual apêndice é a fonte canônica de cada tipo de referência.

4. **Sistema de marcadores ★/◆ com inconsistências** — "LLM-as-judge" e "Golden set" com duplo marcador em APX-A e APX-I; "Autoavaliação" sem marcador em APX-A; requer auditoria completa do sistema de marcadores.

5. **Tese "Modelos passam. Método fica." violada em APX-C** (Roadmap 6 com biblioteca de prompts) — único P0 com impacto direto na integridade intelectual da obra.

## LINHAS-TRACKER CONSOLIDADO
```
APX-A|L1-APX-A-glossario.md|01|P1|ALTO|Nove Frameworks sem entrada individual por framework|Criar 9 entradas individuais com definição e marcador ★|MANTER COM AJUSTES
APX-A|L1-APX-A-glossario.md|02|P1|ALTO|Reasoning models ausente do glossário|Adicionar entrada ◆ com definição e remissiva ao C14B|MANTER COM AJUSTES
APX-A|L1-APX-A-glossario.md|03|P1|MÉDIO|PL de IA sem número; inconsistente com APX-H|Unificar para PL 2338/2023 em ambos os apêndices|MANTER COM AJUSTES
APX-A|L1-APX-A-glossario.md|04|P2|BAIXO|Prompt engineering não diferencia de Context Engineering|Adicionar remissiva cruzada entre as duas entradas|MANTER COM AJUSTES
APX-A|L1-APX-A-glossario.md|05|P2|BAIXO|Autoavaliação sem marcador ★|Adicionar ★ à entrada|MANTER COM AJUSTES
APX-A|L1-APX-A-glossario.md|06|P2|BAIXO|Cat. VII mistura protocolo, padrão de mercado e conceito de produto sem hierarquia|Adicionar nota introdutória de 1 linha à categoria|MANTER COM AJUSTES
APX-B|L1-APX-B-mapa-mental.md|01|P1|ALTO|Princípio 1 mapeado para framework inconsistente com APX-A|Alinhar: P1 sem framework próprio ou nomear framework distinto|MANTER COM AJUSTES
APX-B|L1-APX-B-mapa-mental.md|02|P1|MÉDIO|C14B e C14C ausentes da tabela Princípio × Framework|Adicionar linhas às duas tabelas afetadas|MANTER COM AJUSTES
APX-B|L1-APX-B-mapa-mental.md|03|P2|BAIXO|Roda ASCII sem nota de que layout não implica hierarquia|Adicionar nota de 1 linha abaixo da roda|MANTER COM AJUSTES
APX-B|L1-APX-B-mapa-mental.md|04|P2|BAIXO|Caso de uso "incidente" ausente da tabela "Como usar este mapa"|Adicionar linha à tabela|MANTER COM AJUSTES
APX-C|L1-APX-C-roadmaps.md|01|P0|ALTO|Roadmap 6 orienta publicação de biblioteca de prompts — contradiz tese central|Substituir por biblioteca de frameworks de decisão|MANTER COM AJUSTES
APX-C|L1-APX-C-roadmaps.md|02|P1|ALTO|Ausência de persona para profissional individual sem mandato|Adicionar Roadmap 7 — IC / Profissional Individual|MANTER COM AJUSTES
APX-C|L1-APX-C-roadmaps.md|03|P1|MÉDIO|Roadmaps não referenciam outros apêndices como instrumento de aprofundamento|Adicionar coluna de recursos por marco com remissivas|MANTER COM AJUSTES
APX-C|L1-APX-C-roadmaps.md|04|P1|MÉDIO|Critério cultural não auditável no Marco 365 do Executivo|Substituir por critério verificável em ata ou documento|MANTER COM AJUSTES
APX-C|L1-APX-C-roadmaps.md|05|P2|BAIXO|Meta absoluta de 10 clientes sem baseline contextual no Roadmap do Consultor|Substituir por meta relativa (3 clientes com case)|MANTER COM AJUSTES
APX-D|L1-APX-D-ferramentas.md|01|P0|ALTO|DeepSeek com "viés geopolítico para discutir conforme caso" sem critério de avaliação|Substituir por critério durável de avaliação de risco geopolítico via D.1|MANTER COM AJUSTES
APX-D|L1-APX-D-ferramentas.md|02|P1|ALTO|Licença Llama descrita como fato fixo; muda a cada geração|Substituir por instrução de verificação na fonte oficial|MANTER COM AJUSTES
APX-D|L1-APX-D-ferramentas.md|03|P1|MÉDIO|Ausência de categoria para plataformas corporativas no-code/low-code|Adicionar D.2B com Copilot Studio, Vertex AI, Bedrock Agents|MANTER COM AJUSTES
APX-D|L1-APX-D-ferramentas.md|04|P1|MÉDIO|Critério D.1 sem âncoras de calibração por dimensão|Adicionar 2 âncoras por dimensão na tabela D.1|MANTER COM AJUSTES
APX-D|L1-APX-D-ferramentas.md|05|P2|BAIXO|"Editor desta lista: Fabio Garcia" no corpo do apêndice|Mover para colofão ou remover|MANTER COM AJUSTES
APX-D|L1-APX-D-ferramentas.md|06|P2|BAIXO|Pezzo listado como maduro sem nota sobre atividade irregular do repositório|Adicionar nota de verificação de atividade|MANTER COM AJUSTES
APX-E|L1-APX-E-leituras.md|01|P1|ALTO|Co-Intelligence e Competing in the Age of AI ausentes — são peers diretos da obra|Adicionar subseção com peers e nota de diferenciação|REVISAR PARCIALMENTE
APX-E|L1-APX-E-leituras.md|02|P1|MÉDIO|Seção de blogs/newsletters duplica APX-F sem remissiva|Substituir lista por remissiva ao APX-F + 3-4 fontes essenciais|REVISAR PARCIALMENTE
APX-E|L1-APX-E-leituras.md|03|P1|MÉDIO|Cursos formais misturados com repositórios sem distinção de formato|Separar em dois blocos com nota de pré-requisito|REVISAR PARCIALMENTE
APX-E|L1-APX-E-leituras.md|04|P2|BAIXO|Davenport (2018) sem nota de contexto pré-LLM|Adicionar nota de limitação temporal|REVISAR PARCIALMENTE
APX-F|L1-APX-F-newsletters.md|01|P0|ALTO|Bots Brasil Podcast lançado em 2026 incluído como referência permanente sem histórico|Mover para nota de rodapé com aviso de verificação|MANTER COM AJUSTES
APX-F|L1-APX-F-newsletters.md|02|P1|MÉDIO|Grupo de Telegram sobre MCP sem nome, link ou critério de localização|Generalizar para Brasil.AI/Python BR ou remover|MANTER COM AJUSTES
APX-F|L1-APX-F-newsletters.md|03|P1|MÉDIO|Nomes de indivíduos como referência primária de projetos de podcast|Inverter hierarquia: projeto como primário, apresentador como nota|MANTER COM AJUSTES
APX-F|L1-APX-F-newsletters.md|04|P1|MÉDIO|Canal de contribuição sem URL ou mecanismo permanente especificado|Especificar URL/email permanente|MANTER COM AJUSTES
APX-F|L1-APX-F-newsletters.md|05|P2|BAIXO|Afirmação de cultura organizacional da Magazine Luiza sem fonte|Substituir por afirmação verificável com referência a publicações|MANTER COM AJUSTES
APX-G|L1-APX-G-papers.md|01|P1|ALTO|Building Effective Agents e AutoGPT misturados com papers revisados por pares|Criar subseção de documentação técnica ou mover para APX-H|MANTER COM AJUSTES
APX-G|L1-APX-G-papers.md|02|P1|MÉDIO|Ausência de referência acadêmica para Context Engineering (C11)|Adicionar nota honesta de campo emergente ou paper DSPy|MANTER COM AJUSTES
APX-G|L1-APX-G-papers.md|03|P2|BAIXO|"Como ler papers" sem heading ## — inconsistência de formatação|Adicionar ## Como ler papers de IA|MANTER COM AJUSTES
APX-G|L1-APX-G-papers.md|04|P2|BAIXO|Categoria Agentes sem paper de multi-agente moderno|Adicionar Park et al. Generative Agents (Stanford, 2023)|MANTER COM AJUSTES
APX-H|L1-APX-H-bibliografia.md|01|P1|MÉDIO|Narayanan & Kapoor ausente do APX-G mas presente no APX-H|Adicionar ao APX-G Categoria IV com nota|MANTER COM AJUSTES
APX-H|L1-APX-H-bibliografia.md|02|P1|MÉDIO|Schmidhuber com "(recente)" como data — referência não verificável|Substituir por URL e indicação de atualização periódica|MANTER COM AJUSTES
APX-H|L1-APX-H-bibliografia.md|03|P1|MÉDIO|Drucker, Brooks, Kotter sem contexto de uso na obra|Adicionar nota parentética de contextualização por item|MANTER COM AJUSTES
APX-H|L1-APX-H-bibliografia.md|04|P2|BAIXO|Seção V com uma linha de remissiva — seção vazia|Remover como seção; inserir remissiva como nota em Seção IV|MANTER COM AJUSTES
APX-H|L1-APX-H-bibliografia.md|05|P2|BAIXO|Bommasani et al. categorizado como livro em Filosofia; é technical report|Mover para Seção I em nova subseção de Surveys|MANTER COM AJUSTES
APX-I|L1-APX-I-indice-remissivo.md|01|P0|ALTO|Referências mortas a Apêndice K, L e M — apêndices inexistentes|Auditar estrutura de apêndices e corrigir todas as remissivas|REVISAR PARCIALMENTE
APX-I|L1-APX-I-indice-remissivo.md|02|P1|ALTO|Reasoning models e Spec-driven development ausentes do índice|Adicionar entradas para C14B e C14C em letras R e S|REVISAR PARCIALMENTE
APX-I|L1-APX-I-indice-remissivo.md|03|P1|MÉDIO|LLM-as-judge com duplo marcador ★ ◆ — contraditório|Remover ★; manter ◆; auditar outros casos de duplo marcador|REVISAR PARCIALMENTE
APX-I|L1-APX-I-indice-remissivo.md|04|P1|MÉDIO|Letras N e U ausentes — NIST AI RMF e outros termos não indexados|Adicionar seção N com NIST AI RMF e outros termos ausentes|REVISAR PARCIALMENTE
APX-I|L1-APX-I-indice-remissivo.md|05|P2|BAIXO|Golden set com duplo marcador ★ ◆ — mesmo problema do LLM-as-judge|Remover ★; auditar APX-A para consistência|REVISAR PARCIALMENTE
APX-I|L1-APX-I-indice-remissivo.md|06|P2|BAIXO|Inconsistência ortográfica dos casos brasileiros entre apêndices|Auditar todos os casos entre APX-A e APX-I|REVISAR PARCIALMENTE
```

