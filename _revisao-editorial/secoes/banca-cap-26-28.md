# BANCA EDITORIAL ADVERSARIAL — CAPÍTULOS 26, 27 E 28
*Inteligência Aumentada — Livro 1: Os Invariantes*
*Data de revisão: 2026-06-16*

---

# C26 — L1-C26-roadmap-pessoal.md

## RESUMO EXECUTIVO
Nota: 7/10
Veredito: B

## O QUE FUNCIONA
- A estrutura de sete atributos por marco (objetivo, horas, prerrequisitos, recursos, entregável, gate, critério de abandono) é genuinamente original e operacional — não existe assim empacotada em nenhuma obra do benchmarking.
- O "critério de abandono" por marco é a peça mais corajosa e diferenciada do capítulo; quase nenhum livro de roadmap tem coragem de dizer quando desistir, e aqui está em cada célula.
- O exemplo do CTO de varejo (26.6) é denso, longo o suficiente para ser crível, e cobre três pontos reais de quase-abandono — o que o torna memorável e não apenas ilustrativo.
- As seis personas com marcos a 30/90/180/365 dias cobrem o espectro profissional brasileiro de forma coerente com o restante da obra.
- A seção 26.4 (customização por contexto organizacional) é adição legítima — evita que o roadmap vire promessa universal.
- A seção 26.7 (três sinais de abandono) é honesta e rara em books de autoajuda executiva.
- As referências são sólidas e não oportunistas (Tetlock, Newport, Doerr, Kotter, MIT Sloan/BCG).

## O QUE NÃO FUNCIONA
- O capítulo é volumoso demais para a função que exerce: é um apêndice didatizado que cresceu para capítulo, e a densidade de tabelas não compensa a escassez de argumentação original.
- A persona "Criador de Conteúdo / Educador" (26.3.6) é a mais fraca: os marcos dela são sobre crescimento de audiência, não sobre método de IA — desvio da tese central.
- Referências a "Apêndice C" (roadmap sintético) e a "Apêndice K" e "Apêndice O" criam dependência circular sem que o leitor tenha o apêndice em mãos — o capítulo não é autossuficiente.
- A epígrafe de abertura, embora boa, é muito longa (dois períodos densos) para uma epígrafe.
- A imagem referenciada (L1-C44-img-01) tem numeração de capítulo 44, diferente do capítulo 26 — erro de referência de asset.
- A persona Desenvolvedor/Arquiteto no Marco 365 dias inclui "repositório de prompts" como entregável verificável — fratura a tese "Modelos passam. Método fica." ao tangenciar coleção de artefatos datados.
- O checklist (26.9) e as perguntas de revisão (26.10) têm sobreposição de 70% com os exercícios (26.11) — redundância pedagógica que pode ser consolidada.
- Não há critério de abandono do capítulo inteiro para quem não se encaixa em nenhuma das seis personas — lacuna na lógica do próprio método.

---

## ACHADOS

### ACHADO 01
Categoria: P1
Problema: Persona "Criador de Conteúdo / Educador" desvia da tese central.
Por que é um problema: Os marcos 90 dias ("biblioteca pessoal de prompts publicada"), 180 dias ("comunidade de 100 membros") e 365 dias ("convite a eventos setoriais") são sobre crescimento de audiência e construção de plataforma pessoal, não sobre o método de IA da obra. A persona serve à autopromoção, não ao "Método fica". O marco 90 inclui "biblioteca de prompts" — antítese da tese.
Impacto no leitor: Leitor que é educador/criador recebe roadmap de growth de influencer disfarçado de roadmap de método, sem perceber o desvio.
Correção exata: Reorientar os marcos da persona Criador para foco em desenvolvimento de método de ensino e avaliação do aprendizado, removendo "biblioteca de prompts" e "crescimento de audiência" como entregáveis primários. A persona pode sobreviver se o foco migrar para "design instrucional com método".
Texto sugerido: Marco 90 dias da persona Criador: substituir "biblioteca pessoal de prompts publicada" por "framework de avaliação de aprendizado baseado nos Invariantes aplicado em pelo menos um curso ou workshop, com rúbrica publicada". Excluir "biblioteca de prompts" de todos os marcos.
ROI: ALTO

### ACHADO 02
Categoria: P0
Problema: Referência de asset com numeração errada — imagem referenciada como "L1-C44-img-01" em capítulo 26.
Por que é um problema: Erro factual de referência interna que, em produção, quebra a renderização do asset ou aponta para capítulo errado (C44 não existe ou é outro capítulo). Compromete credibilidade editorial.
Impacto no leitor: Imagem não carrega ou carrega imagem errada, quebrando o fluxo visual do capítulo.
Correção exata: Alterar referência da imagem na seção 26.3 de "L1-C44-img-01-curva-adocao.svg" para "L1-C26-img-01-curva-adocao.svg" (e renomear o arquivo correspondente).
Texto sugerido: `![Curva de adoção pessoal — marcos por persona ao longo de 24 meses](imagens/L1-C26-img-01-curva-adocao.svg)`
ROI: ALTO

### ACHADO 03
Categoria: P1
Problema: Persona Desenvolvedor, Marco 365 dias: "repositório de prompts" como entregável verificável viola a tese central.
Por que é um problema: "Contribuição a repositório de prompts" como gate de promoção cria coleção de artefatos datados. Em 12 meses, os prompts estão obsoletos. O método deveria ser o entregável, não os prompts.
Impacto no leitor: Desenvolvedor acredita que acumular prompts é sinal de maturidade do método, quando é antítese dela.
Correção exata: Substituir "repositório de prompts" por "repositório de casos de uso com framework de avaliação aplicado por caso — o que sobrevive é a estrutura de avaliação, não o prompt específico".
Texto sugerido: "Objetivo: Mentor de outros devs no método dos Invariantes; contribuição a repositório de casos de uso com framework de eval documentado; participação em decisão de arquitetura citando frameworks."
ROI: ALTO

### ACHADO 04
Categoria: P1
Problema: Dependência circular com Apêndice C e outros apêndices não disponíveis no momento da leitura.
Por que é um problema: O capítulo menciona "Apêndice C desta obra" como referência sintética complementar (seção 26.1), "Apêndice K — Gabaritos de aplicação" (26.13) e "Apêndice O" (via conexões). O leitor que está no C26 não tem os apêndices em mãos, e o capítulo não é autossuficiente para quem não os leu.
Impacto no leitor: A Joana não sabe o que está no Apêndice C e como ele se distingue do C26 na prática. Ela fica confusa sobre o que usar.
Correção exata: Adicionar, na seção 26.1, parágrafo de 2-3 linhas que resuma o que o Apêndice C entrega de forma que o C26 não entrega, sem exigir que o leitor já o tenha lido.
Texto sugerido: "O Apêndice C apresenta os roadmaps por persona em formato de tabela de referência rápida — uma página por persona, sem a explicação dos atributos e sem os ajustes por contexto que este capítulo desenvolve. Use o Apêndice C como cola de revisão trimestral após ter aplicado o método deste capítulo."
ROI: MÉDIO

### ACHADO 05
Categoria: P2
Problema: Checklist (26.9), perguntas de revisão (26.10) e exercícios (26.11) têm sobreposição excessiva — cerca de 70% dos itens abordam o mesmo conteúdo de formas ligeiramente diferentes.
Por que é um problema: Alonga o capítulo sem adicionar aprendizado incremental. O leitor sente redundância, perde foco.
Impacto no leitor: Fadiga ao final do capítulo; risco de pular tudo depois da tabela-mestra.
Correção exata: Fundir o checklist e os exercícios em um único bloco "Aplicação imediata" com 6-8 itens não redundantes. Manter as perguntas de revisão separadas mas encurtadas para 4 perguntas (de 6).
Texto sugerido: n/a (reorganização editorial)
ROI: MÉDIO

### ACHADO 06
Categoria: P2
Problema: Nenhuma das seis personas cobre o profissional de recursos humanos, jurídico ou financeiro interno — funções que em muitas PMEs e corporations são as primeiras a adotar IA e as que mais precisam de método.
Por que é um problema: A cobertura de personas fica enviesada para perfis de tecnologia e empreendedorismo, sugerindo que IA aplicada é coisa de tech e de negócios, não de funções de suporte que são as maiores usuárias iniciais em muitas organizações.
Impacto no leitor: O CFO, o CHRO ou o advogado interno que lê o livro não se encontra em nenhuma persona e abandona o roadmap.
Correção exata: Adicionar nota na seção 26.1 orientando esses perfis a se classificarem como "Gestor/Head" com ajuste de contexto (solo ou regulado), e adicionar em 26.4.4 (Profissional Solo) referência explícita a essas funções.
Texto sugerido: "Profissionais de funções corporativas (financeiro, jurídico, recursos humanos) que não gerenciam time de IA se classificam, em geral, na persona Gestor ou na persona Profissional Solo, conforme o grau de autonomia da função. A seção 26.4 apresenta os ajustes para cada contexto."
ROI: BAIXO

### ACHADO 07
Categoria: P1
Problema: A epígrafe de abertura é longa demais para cumprir sua função retórica (2 períodos com 60+ palavras cada).
Por que é um problema: Epígrafe longa demais não é citável, não é memorável, e não abre o capítulo com a força que deveria. A epígrafe ideal desta obra tem 1 período de 20-35 palavras.
Impacto no leitor: O leitor passa pela epígrafe sem absorvê-la e chega à Abertura já desgastado.
Correção exata: Encurtar a epígrafe para a segunda sentença apenas: "Roadmap calibrado vira produto, porque assume as horas reais, os prerrequisitos honestos e o critério explícito de abandono."
Texto sugerido: `> *"Roadmap calibrado vira produto, porque assume as horas reais, os prerrequisitos honestos e o critério explícito de abandono. A diferença entre os dois é a diferença entre o leitor que aplicou o método e o leitor que fechou o livro com sensação confortável de ter aprendido."*`
ROI: BAIXO

---

## TESTE DA JOANA
Entenderia: SIM (com esforço considerável)
O que ela entenderia: A lógica de persona, a existência de marcos, a ideia de critério de abandono, e o exemplo do CTO de varejo.
O que ela NÃO entenderia: A diferença entre este capítulo e o Apêndice C; o que fazer se não se encaixar em nenhuma das seis personas; o que é "Escala de Propriedade do Agente (F3)" e "Cardápio dos Seis Trade-offs" sem ter lido os capítulos anteriores; o que é "golden set" sem ter lido C21.
Como corrigir: Cada termo técnico interno à obra citado nas tabelas deveria ter nota de rodapé de 1 linha com definição e referência ao capítulo. Prioridade: "golden set", "Escala de Propriedade", "Circuit Breaker de custo", "AUP".

## TESTE DE DURABILIDADE
Classificação: ALTA
2 anos: Os marcos envelhecem apenas nos recursos específicos (ferramentas nomeadas como Langfuse, Confluence, Notion, Hotmart — referências datadas); o método de sete atributos sobrevive.
5 anos: A estrutura de personas, horas, prerrequisitos e critérios de abandono é durável. Os nomes de ferramentas precisarão ser revisados.
10 anos: O argumento central (roadmap calibrado vs. aspiracional) sobrevive. A Pirâmide de Evals, golden set, eval em CI podem precisar de atualização se o paradigma mudar.
Justificativa: Ferramentas nomeadas em tabelas (Langfuse, Zoom, Hotmart, Udemy, Circle, Discord) envelhecem. Recomendação: substituir nomes de ferramentas por categorias ("ferramenta de observabilidade", "plataforma de hospedagem de workshop", "plataforma de comunidade") com exemplos em parênteses.

## TESTE DE DIFERENCIAÇÃO
Classificação: DIFERENCIADO
Justificativa: O eixo de diferenciação real é o "critério de abandono" por marco e os "sete atributos" por marco. Nenhuma obra do benchmarking apresenta roadmap com esse grau de honestidade operacional e critério de saída explícito. A persona Criador dilui a diferenciação porque seus marcos são indistinguíveis de um guia de growth de influencer. Remover ou corrigir a persona Criador ampliaria a classificação para PROPRIEDADE INTELECTUAL.

## TESTE DE MEMORIZAÇÃO
Ideia principal clara? SIM
Qual é a ideia principal (em 1 frase): Roadmap que funciona tem sete atributos por marco — especialmente horas reais, prerrequisitos honestos e critério de abandono — e é revisado a cada 90 dias.
Justificativa: A ideia é clara, mas enterrada na abertura e não sintetizada como slogan ou como princípio nomeado que o leitor possa carregar. Falta um nome memorável para o método (ex: "Método OPERA" ou "Sete Atributos do Marco").

## TESTE DE TRANSFORMAÇÃO
Ao terminar, o leitor consegue fazer o que antes não conseguia:
- Classificar-se em uma das seis personas com critério objetivo (fração da semana)
- Construir um documento de roadmap com os sete atributos por marco
- Identificar critério de abandono honesto antes de iniciar um marco
- Aplicar ajuste de contexto organizacional ao roadmap padrão
- Conduzir revisão trimestral com pauta estruturada das cinco perguntas

## NOTA FINAL (0-10 cada eixo)
Estrutura: 7 | Pedagogia: 7 | Clareza: 7 | Autoridade: 8 | Durabilidade: 8 | Diferenciação: 7 | Memorização: 6 | Transformação: 8
**Nota Geral: 7.3**

## DECISÃO EDITORIAL
MANTER COM AJUSTES

---

# C27 — L1-C27-ia-para-pme-brasileira.md

## RESUMO EXECUTIVO
Nota: 8/10
Veredito: A

## O QUE FUNCIONA
- Este é o capítulo de maior diferenciação do bloco. A combinação de matriz TCO por faixa de PME + três tiers de adoção + oito perguntas eliminatórias + regra dos 3% e regra dos 90 dias configura PROPRIEDADE INTELECTUAL que não existe assim sistematizada em nenhuma obra do benchmarking.
- A analogia da contratação do contador (27.2) é precisa, durável e culturalmente contextualizada para o Brasil. É a analogia mais forte dos três capítulos avaliados.
- As oito perguntas eliminatórias (27.3.4) são o artefato mais citável do capítulo: concretas, testáveis, com critério de pass/fail explícito. Qualquer dono de PME pode aplicar amanhã.
- Os cinco sinais de armadilha (27.3.5) são complemento cirúrgico das oito perguntas.
- O exemplo de Joinville (27.5) é o mais rico dos três capítulos: detalha ROI calculado (R$ 210k produtividade vs. R$ 56k investimento), cobre os atores internos por nome/função, mostra o processo de descarte das três consultorias via as 8 perguntas — funciona como caso de aula.
- A seção 27.3.7 (SaaS vs. build vs. híbrido) endereça a decisão mais comum mal feita em PME brasileira.
- As referências brasileiras (SEBRAE, BNDES, IBGE, CNI, LGPD, ANPD, PL 2338/2023) são ponto de diferenciação de PI local — raras em obra de IA em português.

## O QUE NÃO FUNCIONA
- A promessa do subtítulo ("roadmap de doze meses para quem não tem time de IA") é cumprida apenas na seção 27.4, que está no final do capítulo — o leitor que veio só pelo roadmap precisa passar por muita aritmética antes.
- Os valores monetários na matriz TCO (27.3.2) são pontuais e datados: R$ 1.400/mês para assinatura corporativa de Claude, R$ 800/hora de consultoria. Envelhecerão em 12-18 meses e perderão credibilidade.
- A "regra dos 3% do faturamento" não tem base empírica declarada — é apresentada como regra prática mas sem citação de origem ou estudo. O leitor crítico vai questionar.
- A seção 27.3.3 (três tiers) é clara, mas a definição de "tier 2" como "workflow assistido" pode gerar confusão com "low-code automation" ou "RPA" — o capítulo não distingue IA de automação tradicional.
- O checklist (27.8) tem 12 itens, dos quais pelo menos 4 repetem literalmente a seção 27.3.4 e o roadmap 27.4 — redundância pedagógica.
- A seção de Perguntas de Revisão (27.9) tem 8 perguntas, algumas com 3-4 sub-questões embutidas — estrutura de prova, não de revisão rápida.

---

## ACHADOS

### ACHADO 01
Categoria: P1
Problema: Valores monetários específicos na matriz TCO (R$ 1.400/mês, R$ 800/hora, R$ 6.400 em consultoria) envelhecerão em 12-18 meses e podem já estar desatualizados no lançamento.
Por que é um problema: Livro com números datados perde credibilidade proporcional ao tempo de prateleira. Preços de ferramentas de IA mudam a cada trimestre.
Impacto no leitor: Leitor em 2027 lê "assinatura de Claude a R$ 1.400/mês" e questiona toda a matriz TCO por inconsistência com o preço atual.
Correção exata: Substituir valores absolutos por ranges relativos ao faturamento e por referência a "preço corrente verificável em [fonte]". Para a assinatura de modelo SaaS, usar "entre 0,2% e 0,8% do orçamento de tecnologia mensal" com nota "verifique preço corrente no site do fornecedor antes de orçar".
Texto sugerido: "A assinatura corporativa de ferramenta SaaS pronta (Claude, ChatGPT, Gemini, equivalente) costuma custar, em plano corporativo com cinco a sete usuários, valor verificável no site do fornecedor — orce pelo preço corrente antes de fechar o T1."
ROI: ALTO

### ACHADO 02
Categoria: P0
Problema: A "regra dos 3% do faturamento" não tem base empírica ou referência declarada.
Por que é um problema: O capítulo apresenta a regra como princípio operacional com tom de autoridade ("A regra é conservadora e calibra contra...") sem indicar de onde veio — sem estudo, sem benchmarking de setor, sem referência da literatura de gestão de PME. Um consultor adversarial vai desmontá-la facilmente.
Impacto no leitor: Dono de PME usa a regra como escudo contratual e o consultor que ela recusa a acredita frágil — a regra sem base perde poder argumentativo no momento em que mais é necessário.
Correção exata: Opção 1: citar benchmarking explícito (ex: "benchmarking de gastos em tecnologia de PME do SEBRAE/FGV, adaptado para IA generativa"). Opção 2: enquadrar a regra honestamente como heurística conservadora do autor, baseada em observação de casos, sem pretensão de base estatística. A segunda opção é mais honesta dado o estado atual da literatura.
Texto sugerido: "A regra dos três por cento não é derivada de estudo estatístico rigoroso — é heurística conservadora baseada em observação de casos de adoção de PME entre 2024 e 2026, calibrada para que o investimento caiba no orçamento de tecnologia sem comprometer a operação corrente. Trate-a como piso de prudência, não como prescição científica."
ROI: ALTO

### ACHADO 03
Categoria: P1
Problema: O tier 2 ("workflow assistido") não distingue IA generativa de automação tradicional (RPA, low-code), criando ambiguidade operacional.
Por que é um problema: Um dono de PME pode confundir configurar um Zapier ou um Power Automate (automação de regra fixa) com "workflow assistido de IA", e aplicar a aritmética TCO errada. A fronteira entre automação e IA generativa importa para o diagnóstico.
Impacto no leitor: Dono aplica a regra dos 3% e o prazo de 90 dias a um projeto de RPA (não de IA generativa), gerando expectativa errada.
Correção exata: Adicionar na abertura da seção 27.3.3 uma distinção de 2-3 linhas entre automação de regra fixa (RPA, low-code) e workflow assistido por IA generativa, com critério simples de distinção.
Texto sugerido: "Diferença entre workflow assistido de IA e automação de regra fixa: a automação de regra fixa (Zapier, Power Automate, RPA tradicional) executa instruções determinísticas sem julgamento; o workflow assistido de IA generativa executa julgamento em linguagem natural sobre inputs não estruturados, com revisão humana em ponto de controle. O tier 2 deste capítulo trata do segundo, não do primeiro."
ROI: MÉDIO

### ACHADO 04
Categoria: P1
Problema: A seção 27.4 (roadmap de 12 meses) aparece tarde no capítulo (após 5 seções densas de aritmética), mas é o entregável mais procurado pelo leitor alvo (dono de PME com 3 horas semanais).
Por que é um problema: O dono de PME com pouco tempo vai chegar ao capítulo procurando o roadmap, encontrar 3 seções densas de TCO e perguntas eliminatórias, e abandonar antes de chegar ao que precisa.
Impacto no leitor: O leitor mais importante do capítulo (dono de PME sem background técnico) não chega ao produto principal.
Correção exata: Adicionar "Como usar este capítulo" na abertura, com orientação explícita: "Se você tem menos de uma hora, leia 27.2 (analogia), 27.3.3 (três tiers), 27.3.6 (duas regras) e 27.4 (roadmap). Volte às demais seções antes de contratar consultoria."
Texto sugerido: "> **Como usar este capítulo:** Dono de PME com pouco tempo — leia nesta ordem: 27.2 (a analogia do contador), 27.3.3 (os três tiers), 27.3.6 (as duas regras), 27.4 (o roadmap). Antes de conversar com consultoria, leia 27.3.4 e 27.3.5. O resto é referência quando precisar."
ROI: ALTO

### ACHADO 05
Categoria: P2
Problema: O box "Para Donos de PME" (27.5, ao final do exemplo) e o box "Para Executivos" no C28 têm formato inconsistente — um usa emoji 🎯 e o outro também. Consistência de formato no livro toda é questão editorial.
Por que é um problema: Inconsistência de formatação entre capítulos sugere falta de revisão de estilo final.
Impacto no leitor: Leitor percebe inconsistência de produção, que afeta percepção de qualidade editorial.
Correção exata: Padronizar todos os boxes de CTA executivo com o mesmo ícone, o mesmo rótulo ("Para [persona]") e a mesma estrutura (3 perguntas duras).
Texto sugerido: n/a (decisão de estilo, implementar no processo de revisão de copidesque)
ROI: BAIXO

### ACHADO 06
Categoria: P0
Problema: O PL 2338/2023 (Marco Legal da IA) é citado como "em tramitação" (27.3.1 e 27.12). Se o livro for publicado após aprovação do PL (que pode ocorrer antes ou durante 2026), a referência estará factualmente errada.
Por que é um problema: Referência a PL "em tramitação" que foi aprovado antes da publicação é erro factual que compromete a credibilidade do capítulo dedicado a regulação.
Impacto no leitor: Leitor busca o PL e encontra que é Lei aprovada, não PL em tramitação — lê o capítulo com desconfiança sobre a atualidade das demais referências regulatórias.
Correção exata: Trocar "PL 2338/2023 — Marco Legal da IA no Brasil (em tramitação)" por "Marco Legal da IA no Brasil (PL 2338/2023 ou Lei resultante — verifique status corrente em fonte oficial antes de citar em contexto regulatório)". Aplicar o mesmo método do Apêndice J — Trilha do Número que o próprio capítulo recomenda.
Texto sugerido: "Marco Legal da IA no Brasil (PL 2338/2023 ou legislação resultante — status em tramitação ou aprovado deve ser verificado em fonte oficial na data de consulta, conforme Apêndice J — Trilha do Número)."
ROI: ALTO

### ACHADO 07
Categoria: P1
Problema: O exemplo de Joinville inclui ROI calculado (R$ 210k vs. R$ 56k) com metodologia simplificada (horas economizadas × custo médio/hora) sem ressalva de que esse cálculo não desconta custo de oportunidade do tempo dos gestores dedicado ao projeto.
Por que é um problema: O ROI apresentado pode ser contestado por leitor sofisticado (CFO, consultor financeiro) que incluiria no denominador as horas do dono, da filha e do gerente administrativo alocadas ao projeto. A própria autora reconhece parte da ressalva ("parte do tempo economizado virou capacidade para tarefas que antes não eram feitas"), mas não fecha a conta.
Impacto no leitor: Dono de PME usa o ROI como argumento interno e é desafiado pelo sócio CFO que inclui as horas dos gestores — e não tem resposta.
Correção exata: Adicionar ao parágrafo de ROI a seguinte ressalva: "O custo de oportunidade do tempo de gestão alocado ao projeto (estimado em X horas do dono, Y horas da filha, Z horas do gerente administrativo, ao custo médio de gerência) não está incluído no denominador acima. Com esse custo incluído, o ROI líquido seria menor — e ainda positivo."
Texto sugerido: n/a (requer estimativa específica para o caso composto)
ROI: MÉDIO

---

## TESTE DA JOANA
Entenderia: SIM (é o capítulo mais acessível dos três para não-técnicos)
O que ela entenderia: A analogia do contador (imediata), as oito perguntas eliminatórias (aplicaria amanhã), os três tiers (clara distinção), as duas regras (3% e 90 dias, lembra bem), o exemplo de Joinville (reconhece o padrão de empresa familiar brasileira).
O que ela NÃO entenderia: A distinção entre "T1, T2, T3 do TCO" sem a introdução do Framework F7 (que está no Cap 18); o termo "golden set" citado no roadmap sem definição local; "AUP" (Acceptable Use Policy) sem expansão da sigla na primeira vez que aparece no roadmap 27.4.
Como corrigir: Expandir siglas na primeira ocorrência local. Adicionar nota de rodapé para "golden set" e "TCO". A sigla "AUP" não é expandida em 27.4 — corrigir para "política de uso aceitável (AUP)".

## TESTE DE DURABILIDADE
Classificação: MÉDIA
2 anos: Os valores monetários específicos (R$ 1.400, R$ 800/hora) envelhecerão. As faixas de PME, os tiers, as oito perguntas e as duas regras sobrevivem.
5 anos: A estrutura conceitual (tiers, perguntas, regras, analogia do contador) sobrevive inteira. A aritmética específica do TCO precisará de revisão.
10 anos: As oito perguntas eliminatórias e a analogia do contador são duráveis por natureza (problema de assimetria de informação em contratação de serviço especializado é invariante). O capítulo pode ser reedição de um livro de 10 anos com ajuste de números.
Justificativa: Valores de produto datam o capítulo. PL 2338/2023 pode estar aprovado e renomeado. Referências a ferramentas específicas (Claude, ChatGPT, Gemini) datam, mas são bem embaladas como exemplos de categoria.

## TESTE DE DIFERENCIAÇÃO
Classificação: PROPRIEDADE INTELECTUAL
Justificativa: C27 é o capítulo mais original da obra em diferenciação local. A combinação de três faixas de PME brasileira (com dados do SEBRAE/BNDES), matriz TCO por faixa, três tiers calibrados para quem não tem time técnico, oito perguntas eliminatórias culturalmente contextualizadas para o cenário de consultoria brasileiro, regra dos 3%/90 dias, e o exemplo de Joinville configura PI local genuíno. Não existe obra em português que entregue essa aritmética com essa especificidade para o mercado brasileiro. A analogia do contador é o elemento mais citável e mais diferenciado da obra inteira.

## TESTE DE MEMORIZAÇÃO
Ideia principal clara? SIM
Qual é a ideia principal (em 1 frase): A PME brasileira não é Enterprise menor — tem aritmética própria, e a proteção do dono começa nas oito perguntas ao consultor e na regra dos 3% do faturamento como teto.
Justificativa: A ideia é memorável, a analogia do contador ancora a memória, as oito perguntas são citáveis. O capítulo é o mais forte em memorização dos três avaliados.

## TESTE DE TRANSFORMAÇÃO
Ao terminar, o leitor consegue fazer o que antes não conseguia:
- Classificar a empresa nas três faixas de PME e saber qual aritmética usar
- Construir matriz TCO de 12 meses somando T1, T2 e T3
- Aplicar as oito perguntas eliminatórias em qualquer conversa com consultoria
- Identificar os cinco sinais de armadilha antes de fechar contrato
- Calcular o teto de 3% do faturamento como envelope de investimento
- Executar o roadmap de 12 meses em três fases calibradas para sua faixa

## NOTA FINAL (0-10 cada eixo)
Estrutura: 8 | Pedagogia: 8 | Clareza: 8 | Autoridade: 9 | Durabilidade: 6 | Diferenciação: 10 | Memorização: 9 | Transformação: 9
**Nota Geral: 8.4**

## DECISÃO EDITORIAL
MANTER COM AJUSTES

---

# C28 — L1-C28-interpretabilidade-mecanicista.md

## RESUMO EXECUTIVO
Nota: 8/10
Veredito: A

## O QUE FUNCIONA
- O capítulo cumpre a promessa de entregar "vocabulário durável" sem virar manual técnico — é a calibração mais difícil de acertar em livro sobre IA, e aqui está bem executada.
- A analogia da anatomia comparada (28.2) é precisa, produtiva e durável. Dela emergem as três lições certas: progressividade da engenharia reversa, necessidade de intervenção causal, e honestidade sobre cobertura parcial.
- A seção 28.3.5 ("limitações brutais") é a peça mais corajosa do capítulo — poucos autores têm a honestidade de dizer "a interpretabilidade está atrasada anos atrás da capacidade" no mesmo capítulo que vende a importância do campo.
- O exemplo do banco e da ANPD (28.5) é o melhor exemplo memorável dos três capítulos: tem cenário crível, pergunta regulatória específica, três camadas de resposta técnica, custo detalhado (R$ 230k decomposto em três componentes), prazo real (D+3 a D+120) e lição estrutural.
- A conexão entre probing e intervenção causal como complementares (não concorrentes) é pedagogicamente sólida.
- As referências incluem os papers canônicos corretos (Olah 2020, Bricken 2023, Templeton 2024, Conmy 2023, Nanda 2023, Belrose 2023) — credibilidade técnica alta.
- A conexão com LGPD Art. 20, ANPD, EU AI Act e NIST AI RMF é o eixo de diferenciação local mais forte do capítulo.
- A seção 28.4 (conexões com outros capítulos) é a mais bem integrada ao sistema da obra dos três capítulos avaliados.

## O QUE NÃO FUNCIONA
- O teste da Joana crítico: a seção 28.3.3 (polissemanticidade, superposição, Johnson-Lindenstrauss) é o único trecho dos três capítulos que provavelmente perde a Joana por completo. O lema de Johnson-Lindenstrauss não é acessível sem matemática de álgebra linear.
- A referência a "transformer-circuits.pub" como fonte de releitura semestral pressupõe que o site continuará disponível — link externo em livro impresso/digital de longa vida é risco.
- O exemplo do Golden Gate Claude é citado duas vezes (28.3.2 e 28.3.6) com sobreposição de conteúdo — a segunda menção poderia ser apenas referência à primeira.
- A seção 28.3.4 (DeepMind) é curta demais para a importância que reivindica ("merecem atenção") — ou expandir com mais detalhes operacionais ou reduzir para parágrafo dentro de 28.3.3.
- A imagem referenciada (L1-C46-img-01) tem numeração C46 em capítulo 28 — mesmo problema de referência de asset que o C26, mas aqui com número diferente.
- O Exercício 4 (28.10) recomenda leitura ativa de NeurIPS e ICML por "responsável nomeado" — subestima o esforço de absorção de conferência técnica para equipe de produto de organização não-acadêmica.

---

## ACHADOS

### ACHADO 01
Categoria: P1
Problema: Seção 28.3.3 (polissemanticidade, superposição, Johnson-Lindenstrauss) perde o leitor não-técnico.
Por que é um problema: O capítulo promete "vocabulário durável" para o CTO sem especialização em interpretabilidade, mas a explicação do lema de Johnson-Lindenstrauss exige intuição geométrica em espaço de alta dimensão. A Joana — e muitos CTOs formados fora de ciência da computação — se perde aqui e pode abandonar o capítulo neste ponto.
Impacto no leitor: Leitor não-matemático pula a seção, perde a intuição de superposição, e não entende por que probing isolado não basta. A consequência é fragilidade na defesa diante de auditor.
Correção exata: Manter a explicação técnica, mas antecedê-la com caixa "Intuição para não-matemáticos" de 4-5 linhas: "A rede descobre que precisa guardar mais coisas do que tem gavetas. Em vez de jogar fora o que não cabe, ela dobra várias coisas na mesma gaveta de formas que raramente se confundem. O lema de Johnson-Lindenstrauss é só a prova matemática de que essa dobradinha funciona."
Texto sugerido: "> **Intuição para não-matemáticos:** Imagine que a rede tem mil gavetas mas precisa guardar dez mil conceitos. Em vez de jogar conceitos fora, ela dobra vários em cada gaveta — de formas cuidadosamente escolhidas para que raramente se confundam. O lema de Johnson-Lindenstrauss é apenas a prova de que essa dobradinha funciona matematicamente. O que importa para o CTO: neurônios individuais são polissemânticos *por construção*, e desentrelaçar essa dobradinha exige SAE."
ROI: ALTO

### ACHADO 02
Categoria: P0
Problema: Referência de asset com numeração errada — imagem referenciada como "L1-C46-img-01" em capítulo 28.
Por que é um problema: Mesmo problema do C26. Erro de referência interna que quebra renderização ou aponta para asset inexistente/errado.
Impacto no leitor: Imagem do stack de interpretabilidade não carrega, perdendo o diagrama mais importante do capítulo.
Correção exata: Alterar de "L1-C46-img-01-stack-interpretabilidade.svg" para "L1-C28-img-01-stack-interpretabilidade.svg" e renomear o arquivo.
Texto sugerido: `![Cinco níveis da interpretabilidade — do comportamento observável à intervenção causal sobre circuits](imagens/L1-C28-img-01-stack-interpretabilidade.svg)`
ROI: ALTO

### ACHADO 03
Categoria: P1
Problema: Golden Gate Claude é descrito duas vezes (28.3.2 e 28.3.6) com conteúdo sobreposto — a segunda instância repete as três "atenções" sem acrescentar perspectiva nova.
Por que é um problema: Redundância que alonga o capítulo sem adicionar aprendizado. O leitor lê o mesmo exemplo duas vezes com pequenas variações.
Impacto no leitor: Perda de credibilidade editorial (parece que o autor não lembrou que já havia discutido). Desatenção do leitor no segundo encontro.
Correção exata: Na seção 28.3.6, substituir a descrição do Golden Gate Claude por referência cruzada: "A demonstração do Golden Gate Claude, descrita em 28.3.2, exemplifica esta frente: a equipe identificou e manipulou feature específica em modelo de fronteira — e o comportamento bizarro resultante (obsessão patológica pela ponte) é, em si, lição operacional sobre cuidado necessário em intervenção."
Texto sugerido: Ver correção acima.
ROI: MÉDIO

### ACHADO 04
Categoria: P2
Problema: Referência a "transformer-circuits.pub" como fonte de releitura semestral é link externo frágil em livro com vida útil longa.
Por que é um problema: URLs mudam. Se a Anthropic reorganizar ou descontinuar o site, a referência de releitura semestral (checklist item 11, exercício 4) fica morta.
Impacto no leitor: Leitor em 2028 clica no link ou o procura e não encontra — desgasta a credibilidade das referências do capítulo.
Correção exata: Substituir URL direta por referência à organização e ao método de busca: "publicações de interpretabilidade da Anthropic (verificar em site oficial da Anthropic em /research ou /interpretability — URL corrente disponível no site oficial)".
Texto sugerido: "publicações de interpretabilidade da Anthropic (disponíveis em transformer-circuits.pub ou equivalente — verifique URL corrente no site oficial da Anthropic, conforme Apêndice J — Trilha do Número)"
ROI: BAIXO

### ACHADO 05
Categoria: P1
Problema: A seção 28.3.4 (DeepMind) promete "merecem atenção" mas entrega parágrafos curtos com contexto insuficiente para o CTO entender por que o grokking importa para ele operacionalmente.
Por que é um problema: O CTO que lê "comportamento aparente do modelo pode esconder transições internas estruturais que interpretabilidade detecta" precisa de um exemplo operacional de quando isso ocorre em produção — e não encontra aqui.
Impacto no leitor: A seção parece apêndice bibliográfico disfarçado de conteúdo. O leitor não sabe o que fazer com a informação.
Correção exata: Adicionar ao parágrafo do grokking uma aplicação prática de 2-3 linhas: "Para o time de produto, o grokking importa porque explica por que um modelo treinado por mais tempo pode ter mudado de comportamento qualitativo, não apenas quantitativo — e a avaliação comportamental padrão pode não detectar a transição. O sinal operacional é: eval que cobria comportamento anterior pode não cobrir comportamento pós-grokking, exigindo revisão do golden set."
Texto sugerido: Ver correção acima.
ROI: MÉDIO

### ACHADO 06
Categoria: P2
Problema: O Exercício 4 (28.10) recomenda leitura ativa de NeurIPS e ICML, subestimando o esforço de absorção para equipe não-acadêmica.
Por que é um problema: NeurIPS e ICML têm papers em quantidade e profundidade que exigem pesquisador treinado para triagem — recomendar ao "responsável nomeado" da equipe de produto, sem orientação de como triagem, é recomendação que não será seguida.
Impacto no leitor: Equipe ignora o exercício por ser inaplicável, e perde o hábito de releitura do campo que o exercício deveria instalar.
Correção exata: Substituir "papers acadêmicos em conferências como NeurIPS e ICML" por "compilações curadas de papers de interpretabilidade (ex: boletins de interpretability no Alignment Forum, Anthropic Alignment Notes, The Gradient — verificar equivalentes correntes)".
Texto sugerido: "Fontes de atualização sugeridas: publicações da Anthropic em interpretabilidade (transformer-circuits.pub ou equivalente), boletins curados de interpretabilidade disponíveis no Alignment Forum e no LessWrong, e sínteses de conferências publicadas por equipes de pesquisa — não os papers brutos de NeurIPS/ICML, mas as sínteses que equipes de produto conseguem absorver."
ROI: BAIXO

### ACHADO 07
Categoria: P1
Problema: O conceito de "faithfulness de chain-of-thought" é mencionado em 28.4 como conexão com Cap. 23, mas o leitor que não leu Cap. 23 não tem a base necessária — e este é um conceito central para entender por que interpretabilidade é diferente de chain-of-thought.
Por que é um problema: A conexão mais importante do capítulo (interpretabilidade como única forma de auditar o "porquê real" do modelo, além do CoT que pode mentir) está enterrada em uma seção de conexões, não destacada como argumento central do capítulo.
Impacto no leitor: Leitor não entende por que interpretabilidade mecanicista é distinta de simplesmente pedir ao modelo que explique seu raciocínio — que é o que a maioria dos executivos faz em prática.
Correção exata: Adicionar no conceito intuitivo (28.1) um parágrafo de 3-4 linhas conectando interpretabilidade com a limitação do chain-of-thought: "O modelo pode produzir cadeia de raciocínio ('decidi assim porque...') que parece transparente mas não reflete o mecanismo real da decisão — a cadeia pode ser racionalizaçãoo post hoc. A interpretabilidade mecanicista é o único instrumento que audita o mecanismo real, não apenas o relato do mecanismo."
Texto sugerido: "A cadeia de raciocínio (chain-of-thought) apresentada pelo modelo pode parecer transparente — mas não é necessariamente fiel ao mecanismo interno que produziu a decisão. A interpretabilidade mecanicista não se contenta com o relato; ela audita o mecanismo. Esta distinção — entre o que o modelo diz que fez e o que ele realmente computou — é o argumento central para o investimento em interpretabilidade em produtos de alto risco."
ROI: ALTO

---

## TESTE DA JOANA
Entenderia: NÃO (parcialmente)
O que ela entenderia: A abertura (28.1) com os três momentos operacionais (auditoria ANPD, jailbreak, processo judicial) — esses ela entende sem dificuldade. A analogia da anatomia comparada (28.2). O exemplo do banco (28.5) — narrativo e concreto o suficiente. As aplicações práticas (28.3.6). A seção de limitações brutais (28.3.5) — a honestidade a conquista.
O que ela NÃO entenderia: Seção 28.3.3 inteira (polissemanticidade, superposição, Johnson-Lindenstrauss) sem a caixa de intuição sugerida no Achado 01. O que é "concept ablation" no exemplo do banco sem definição local. O que é "faithfulness de chain-of-thought" sem o C23 como pré-leitura.
Como corrigir: Caixa de intuição no 28.3.3 (Achado 01). Glossário local de termos técnicos no início do capítulo ou notas de rodapé nas primeiras ocorrências de: "concept ablation", "SAE", "probing", "faithfulness". O capítulo 28 pressupõe leitura anterior de C2 (Transformer) e C5 (Embeddings) — adicionar aviso explícito no início do capítulo.

## TESTE DE DURABILIDADE
Classificação: MÉDIA
2 anos: Os conceitos centrais (feature, circuit, SAE, intervenção causal, superposição) são duráveis. Os papers específicos de 2023-2024 permanecem referência. As referências regulatórias (ANPD, PL 2338/2023) podem ficar desatualizadas.
5 anos: Feature, circuit e intervenção causal são duráveis enquanto a arquitetura Transformer dominar. Se a arquitetura mudar, o vocabulário precisa de revisão. "Claude 3 Sonnet" como referência de modelo datará o capítulo.
10 anos: A postura epistemológica (interpretabilidade como engenharia reversa progressiva, honesta sobre cobertura parcial) é durável. O vocabulário técnico específico pode precisar de atualização dependendo da evolução da arquitetura.
Justificativa: "Claude 3 Sonnet" (28.3.2) datará o capítulo. "Golden Gate Claude" pode ser anedota de curiosidade histórica em 5 anos. A ANPD e o PL 2338/2023 precisarão de atualização conforme evolução regulatória. A referência ao "estado da arte em 2024" em 28.3.5 é datada por construção mas honestamente sinalizada.

## TESTE DE DIFERENCIAÇÃO
Classificação: DIFERENCIADO
Justificativa: O capítulo é diferenciado pela combinação de contexto regulatório brasileiro (ANPD, LGPD Art. 20, cenário de processo judicial brasileiro) com vocabulário técnico de interpretabilidade. A maioria dos textos em inglês sobre o campo não toca em implicações para regulação brasileira. O exemplo do banco com auditoria da ANPD é propriedade intelectual local genuína. Não chega a PI puro porque o conteúdo técnico (feature, circuit, SAE, superposição) é derivação direta da literatura primária (Anthropic, DeepMind) sem nova síntese conceitual — o que é apropriado para um capítulo de divulgação executiva, não de pesquisa.

## TESTE DE MEMORIZAÇÃO
Ideia principal clara? SIM
Qual é a ideia principal (em 1 frase): A pergunta do auditor deslocou-se de "o modelo funciona bem" para "como você sabe que o modelo decidiu como decidiu", e a resposta defensável exige instrumentação de interpretabilidade pronta antes do ofício chegar.
Justificativa: A ideia é clara e está cristalizada na epígrafe e no fechamento do exemplo do banco. É a sentença mais memorável da obra neste bloco. O capítulo termina com a ideia central na última linha — boa escolha editorial.

## TESTE DE TRANSFORMAÇÃO
Ao terminar, o leitor consegue fazer o que antes não conseguia:
- Distinguir interpretabilidade mecanicista de probing leve e de interpretabilidade comportamental em 1 frase
- Nomear os cinco conceitos centrais (feature, SAE, circuit, intervenção causal, probing) com definição operacional
- Explicar por que probing isolado não sustenta defesa regulatória e o que é necessário adicionalmente
- Mapear os produtos da organização por risco de auditoria e identificar quais justificam investimento em interpretabilidade
- Conduzir simulação de pedido regulatório com CTO, DPO e jurídico
- Formular as três perguntas duras ao time técnico sobre instrumentação atual

## NOTA FINAL (0-10 cada eixo)
Estrutura: 8 | Pedagogia: 7 | Clareza: 7 | Autoridade: 9 | Durabilidade: 6 | Diferenciação: 8 | Memorização: 9 | Transformação: 8
**Nota Geral: 7.8**

## DECISÃO EDITORIAL
MANTER COM AJUSTES

---

## LINHAS-TRACKER

C26|L1-C26-roadmap-pessoal.md|01|P1|ALTO|Persona Criador desvia da tese central com marcos de growth de audiência e biblioteca de prompts|Reorientar marcos para design instrucional e avaliação de aprendizado; remover biblioteca de prompts|MANTER COM AJUSTES
C26|L1-C26-roadmap-pessoal.md|02|P0|ALTO|Referência de imagem com numeração errada — L1-C44-img-01 em capítulo 26|Corrigir para L1-C26-img-01 e renomear arquivo de asset|MANTER COM AJUSTES
C26|L1-C26-roadmap-pessoal.md|03|P1|ALTO|Persona Dev Marco 365 inclui repositório de prompts — antítese da tese central|Substituir por repositório de casos de uso com framework de eval documentado|MANTER COM AJUSTES
C26|L1-C26-roadmap-pessoal.md|04|P1|MÉDIO|Dependência circular com Apêndice C e outros apêndices não disponíveis ao leitor do capítulo|Adicionar parágrafo de 2-3 linhas resumindo o que o Apêndice C entrega sem exigir leitura prévia|MANTER COM AJUSTES
C26|L1-C26-roadmap-pessoal.md|05|P2|MÉDIO|Checklist, perguntas de revisão e exercícios com 70% de sobreposição|Fundir em bloco único de aplicação com 6-8 itens não redundantes|MANTER COM AJUSTES
C26|L1-C26-roadmap-pessoal.md|06|P2|BAIXO|Personas não cobrem CFO, CHRO, advogado interno — funções primárias de adoção em muitas organizações|Adicionar nota orientando esses perfis à persona Gestor ou Solo com ajuste de contexto|MANTER COM AJUSTES
C26|L1-C26-roadmap-pessoal.md|07|P1|BAIXO|Epígrafe longa demais — dois períodos de 60+ palavras, não citável nem memorável|Encurtar para segunda sentença apenas|MANTER COM AJUSTES
C27|L1-C27-ia-para-pme-brasileira.md|01|P1|ALTO|Valores monetários específicos (R$ 1.400, R$ 800/hora) envelhecerão em 12-18 meses|Substituir por ranges relativos ao faturamento e referência a preço corrente no site do fornecedor|MANTER COM AJUSTES
C27|L1-C27-ia-para-pme-brasileira.md|02|P0|ALTO|Regra dos 3% sem base empírica ou referência declarada — fragilidade argumentativa|Enquadrar honestamente como heurística conservadora baseada em observação de casos, não em estudo estatístico|MANTER COM AJUSTES
C27|L1-C27-ia-para-pme-brasileira.md|03|P1|MÉDIO|Tier 2 não distingue IA generativa de automação tradicional (RPA, low-code)|Adicionar distinção de 2-3 linhas na abertura de 27.3.3|MANTER COM AJUSTES
C27|L1-C27-ia-para-pme-brasileira.md|04|P1|ALTO|Roadmap de 12 meses (27.4) aparece tarde — leitor alvo abandona antes de chegar|Adicionar "Como usar este capítulo" na abertura com rota de leitura para dono de PME com pouco tempo|MANTER COM AJUSTES
C27|L1-C27-ia-para-pme-brasileira.md|05|P2|BAIXO|Box CTA com formato inconsistente entre C27 e C28|Padronizar ícone, rótulo e estrutura de todos os boxes de CTA executivo|MANTER COM AJUSTES
C27|L1-C27-ia-para-pme-brasileira.md|06|P0|ALTO|PL 2338/2023 referenciado como em tramitação — pode estar aprovado antes da publicação|Substituir por referência dinâmica com instrução de verificar status em fonte oficial|MANTER COM AJUSTES
C27|L1-C27-ia-para-pme-brasileira.md|07|P1|MÉDIO|ROI do exemplo de Joinville não desconta custo de oportunidade do tempo de gestão alocado|Adicionar ressalva explícita com estimativa de custo de gestão no denominador|MANTER COM AJUSTES
C28|L1-C28-interpretabilidade-mecanicista.md|01|P1|ALTO|Seção 28.3.3 perde leitor não-técnico com Johnson-Lindenstrauss sem intuição prévia|Adicionar caixa de intuição para não-matemáticos antes da explicação técnica|MANTER COM AJUSTES
C28|L1-C28-interpretabilidade-mecanicista.md|02|P0|ALTO|Referência de imagem com numeração errada — L1-C46-img-01 em capítulo 28|Corrigir para L1-C28-img-01 e renomear arquivo de asset|MANTER COM AJUSTES
C28|L1-C28-interpretabilidade-mecanicista.md|03|P1|MÉDIO|Golden Gate Claude descrito duas vezes com conteúdo sobreposto em 28.3.2 e 28.3.6|Na segunda ocorrência, substituir por referência cruzada à primeira|MANTER COM AJUSTES
C28|L1-C28-interpretabilidade-mecanicista.md|04|P2|BAIXO|URL transformer-circuits.pub é link externo frágil em livro de longa vida|Substituir por referência à organização e método de busca com instrução de verificar URL corrente|MANTER COM AJUSTES
C28|L1-C28-interpretabilidade-mecanicista.md|05|P1|MÉDIO|Seção DeepMind (28.3.4) promete relevância mas não entrega aplicação operacional do grokking|Adicionar 2-3 linhas com implicação prática: avaliação comportamental pode não detectar transição de grokking|MANTER COM AJUSTES
C28|L1-C28-interpretabilidade-mecanicista.md|06|P2|BAIXO|Exercício 4 recomenda leitura de NeurIPS e ICML — inaplicável para equipe não-acadêmica|Substituir por compilações curadas do Alignment Forum e sínteses de equipes de pesquisa|MANTER COM AJUSTES
C28|L1-C28-interpretabilidade-mecanicista.md|07|P1|ALTO|Distinção interpretabilidade vs. chain-of-thought enterrada em seção de conexões, não no conceito intuitivo|Mover argumento central (modelo pode racionalizar post hoc) para 28.1 como argumento de abertura|MANTER COM AJUSTES
