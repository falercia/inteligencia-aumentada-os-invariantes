# CHANGELOG — ONDA 3 (clareza, retenção, Teste da Joana)

**Escopo:** os ~204 achados P1 da banca. **Backup:** `_backup-pre-onda3/`.
**Resultado agregado:** ~170 P1 editados; ~30 já resolvidos nas Ondas 1/2 ou obsoletos após a migração; ~9 deferidos (decisões estruturais do autor ou assets/SVG, e alguns P2).
**Natureza das edições:** desfazer jargão sem explicação, adicionar analogias concretas para a Joana (executiva sem background técnico), cortar redundância, tornar a ideia principal explícita, fortalecer aberturas/fechamentos, e numerar/estruturar seções para navegação.

---

---

# CHANGELOG ONDA 3 — PARATEXTO
## Livro: INTELIGÊNCIA AUMENTADA — Os Invariantes
## Escopo: clareza, retenção, Teste da Joana — achados P1

---

## P-00 — L1-00-capa-e-titulos.md

### Achado 02 — Orelhas duplicadas entre este arquivo e L1-11-orelhas.md
**Status:** [EDITADO]
**Arquivo:** `00-paratexto/L1-00-capa-e-titulos.md`
**Resumo:** Seções ORELHA ESQUERDA e ORELHA DIREITA removidas deste arquivo. Substituídas por referência canônica: `> Textos canônicos: ver L1-11-orelhas.md`. Elimina risco de versão desatualizada divergente em produção gráfica.

---

## P-00B — L1-00b-ficha-catalografica.md

### Achado 01 — Descritor "Modelos de linguagem" não é controlado CDD/CDU
**Status:** [EDITADO]
**Arquivo:** `00-paratexto/L1-00b-ficha-catalografica.md`
**Resumo:** Substituído "5. Modelos de linguagem." por "5. Processamento de linguagem natural." — descritor controlado padrão da CDU (004.912). Previne rejeição ou alteração pelo bibliotecário CRB.

### Achado 02 — Referência ao Apêndice Q dentro de documento jurídico de direitos autorais
**Status:** [EDITADO]
**Arquivo:** `00-paratexto/L1-00b-ficha-catalografica.md`
**Resumo:** Substituída a referência ao "Apêndice Q (Manual do Professor)" por frase autocontida: "...disponível mediante contato via canal oficial da obra." A ficha catalográfica passa a ser documento independente, sem dependência circular de conteúdo interno.

---

## P-00C2 — L1-00c2-promessa.md

### Achado 01 — Jargão interno "critério de recalibração" exposto ao leitor externo
**Status:** [EDITADO]
**Arquivo:** `00-paratexto/L1-00c2-promessa.md`
**Resumo:** "com critério de recalibração quando a trilha não estiver servindo" reescrito como "com guia de quando mudar de trilha se a atual não estiver entregando". Linguagem de benefício direto; Joana entende sem precisar conhecer o sistema de trilhas antecipadamente.

### Achado 02 — "sem receita americana traduzida" não sustentada no paratexto
**Status:** [EDITADO]
**Arquivo:** `00-paratexto/L1-00c2-promessa.md`
**Resumo:** Afirmação expandida com exemplo concreto da diferença: "não estudos de caso americanos traduzidos, mas compostos pedagógicos construídos a partir de padrões observados em organizações brasileiras, com cargo, setor e números calibrados ao mercado nacional." Diferenciação agora é verificável, não apenas declarada.

---

## P-00D — L1-00d-agradecimentos.md

### Achado 01 — Afirmação de peer review informal sem registro público
**Status:** [EDITADO]
**Arquivo:** `00-paratexto/L1-00d-agradecimentos.md`
**Resumo:** Adicionada qualificação explícita após o agradecimento aos CTOs e engenheiros: "O processo foi de refinamento iterativo informal — conversas privadas, não protocolos de peer review —, e a responsabilidade pelos erros remanescentes é inteiramente do autor." Remove afirmação não falsificável sem cortar o agradecimento.

### Achado 02 — CEOs nomeados por liderarem organizações "abertas" — frágil e datado
**Status:** [EDITADO]
**Arquivo:** `00-paratexto/L1-00d-agradecimentos.md`
**Resumo:** "Demis Hassabis, Dario Amodei e Sam Altman por liderarem organizações..." substituído por "Anthropic, OpenAI e Google DeepMind, que mantiveram publicação técnica suficientemente aberta — em graus e formatos variáveis — para permitir obra como esta." Foco nas organizações, não nos CEOs; qualificação "em graus e formatos variáveis" protege contra contestação de abertura.

---

## P-01 — L1-01-prefacio.md

### Achado 01 — "Quem soube ler a internet em 1996 ganhou uma década" — afirmação não verificável
**Status:** [EDITADO]
**Arquivo:** `00-paratexto/L1-01-prefacio.md`
**Resumo:** Reescrito como tese com lógica verificável: "Os profissionais e empresas que entenderam a internet antes do ciclo de adoção em massa ganharam vantagem estrutural que durou uma década — não por ter acesso, mas por ter compreensão. A mesma lógica se repetiu com a nuvem. Em IA, o padrão deve se repetir, com velocidade maior." Argumento mantém força sem ser não-falsificável.

### Achado 02 — "Em 2028, segundo as projeções mais conservadoras" — sem fonte atribuída
**Status:** [JÁ RESOLVIDO]
**Arquivo:** `00-paratexto/L1-01-prefacio.md`
**Resumo:** O texto "Em 2028, segundo as projeções mais conservadoras" não existe no arquivo atual do prefácio. A frase foi encontrada em L1-03-introducao.md e corrigida lá (ver P-03 Achado correspondente). P1 já resolvido no prefácio.

### Achado 03 — "Empresas trocam fornecedor toda semana" — hipérbole
**Status:** [EDITADO]
**Arquivo:** `00-paratexto/L1-01-prefacio.md`
**Resumo:** "Empresas trocam fornecedor toda semana, equipes refazem prompts toda semana" reescrito como "Empresas trocam fornecedor a cada ciclo de lançamento, equipes refazem prompts a cada versão nova". Impacto mantido; hipérbole verificável removida.

### Achado 04 — Nove Princípios não mencionados pelo nome no prefácio
**Status:** [EDITADO]
**Arquivo:** `00-paratexto/L1-01-prefacio.md`
**Resumo:** Adicionado parágrafo após a apresentação dos Nove Princípios Permanentes: "Os nove princípios — Camada Dupla, Plausibilidade, Custo Composto, Extremidades, Encaixe, Termômetro, Autonomia Proporcional, Responsabilidade Indelegável, Operador — formam o vocabulário que costura toda a obra. Cada um tem nome porque nome cria memória, e memória cria critério." Joana fecha o prefácio com os nomes dos princípios, não apenas com a existência deles.

---

## P-02 — L1-02-como-ler.md

### Achado 01 — Caminho 3 (pelos princípios) sem exemplo concreto de rota
**Status:** [EDITADO]
**Arquivo:** `00-paratexto/L1-02-como-ler.md`
**Resumo:** Adicionado exemplo de rota completa ao Caminho 3: "Por exemplo: para internalizar o Princípio da Responsabilidade Indelegável, leia C19 (segurança), depois C24 (governança), depois F6, depois o exemplo do banco médio no C19. Em vinte e quatro horas de leitura focada, você terá o princípio operacionalizado." Joana agora pode executar o Caminho 3.

### Achado 02 — Afirmação pedagógica da sequência de 10 blocos sem referência
**Status:** [EDITADO]
**Arquivo:** `00-paratexto/L1-02-como-ler.md`
**Resumo:** "não por convenção, mas porque ela espelha como adultos profissionais realmente aprendem conceito novo" substituído por descrição do ciclo pedagógico deliberado: "cada bloco tem função específica, construída para que o conceito seja primeiro intuído, depois ancorizado em analogia, depois rigorizado, depois aplicado — ciclo que a prática de ensino em contexto executivo mostrou ser mais eficaz que exposição direta ao rigor." Afirmação reformulada como escolha editorial com base declarada.

### Achado 03 — "Assinar duas newsletters recomendadas" sem indicar quais
**Status:** [EDITADO]
**Arquivo:** `00-paratexto/L1-02-como-ler.md`
**Resumo:** Adicionada referência explícita: "— ver lista curada no Apêndice F (Comunidade Brasileira de IA em 2026) e no Apêndice E (Leituras Complementares) —". Instrução passa a ter destino.

### Achado adicional — ▸ repo ausente nas Convenções Visuais (P-06 Achado 02, correção em L1-02)
**Status:** [EDITADO]
**Arquivo:** `00-paratexto/L1-02-como-ler.md`
**Resumo:** Adicionada linha "▸ repo | Artefato executável disponível no repositório acompanhante" na tabela de Convenções Visuais. Resolve inconsistência entre L1-06 (usa ▸ repo ao longo da leitura) e L1-02 (não a definia).

---

## P-03 — L1-03-introducao.md

### Achado 01 — Epígrafe com três períodos compostos — densa demais
**Status:** [EDITADO]
**Arquivo:** `00-paratexto/L1-03-introducao.md`
**Resumo:** Epígrafe de três períodos compostos reduzida para uma sentença de impacto: "Quando uma tecnologia muda mais rápido do que sua capacidade de entendê-la, você perde o controle e a oportunidade ao mesmo tempo." Joana passa pelo gancho sem travar.

### Achado 02 — "Milhares de empresas, milhões de profissionais" — hipérbole
**Status:** [EDITADO]
**Arquivo:** `00-paratexto/L1-03-introducao.md`
**Resumo:** "por milhares de empresas, por milhões de profissionais" reescrito como "por milhares de salas de reunião pelo país". Remove "milhões" não sustentável; mantém escala do argumento.

### Achado 03 — Seção Arco Narrativo redundante com Sumário
**Status:** [EDITADO]
**Arquivo:** `00-paratexto/L1-03-introducao.md`
**Resumo:** Seção "O ARCO NARRATIVO" substituída por "A ORDEM DELIBERADA", com argumento pedagógico sobre por que a sequência de cinco partes é a que é — não descrição de estrutura, mas justificativa de aprendizado. O leitor entende o ganho de ler na ordem proposta.

### Achado 04 — Aposta 2 critica livros de tecnologia sem nomear exemplos
**Status:** [EDITADO]
**Arquivo:** `00-paratexto/L1-03-introducao.md`
**Resumo:** "Existe uma tradição perigosa em livros de tecnologia: tratar conceitos como se vivessem no vácuo" reformulado como limitação de formato: "Existe uma limitação recorrente em livros de tecnologia: o formato de capítulo independente tende a apresentar conceitos como se vivessem no vácuo, porque conectar profundamente RAG ao agente ao trade-off de custo exige um sistema que sustente a conexão. Este livro propõe esse sistema." Crítica de formato, não de autores.

### Achado adicional — "Em 2028, segundo as projeções mais conservadoras" (P-01 Achado 02 que vive aqui)
**Status:** [EDITADO]
**Arquivo:** `00-paratexto/L1-03-introducao.md`
**Resumo:** "Em 2028, segundo as projeções mais conservadoras, essa distância será inegociável" reformulado como julgamento autoral explícito: "Na minha avaliação — baseada na velocidade atual de adoção e no histórico de ciclos anteriores — essa distância vai se tornar estrutural nos próximos dois anos." Remove fonte fantasma; mantém o argumento com assinatura autoral honesta.

---

## P-04 — L1-04-sumario.md

### Achado 01 — Capítulos 14C e 14B em ordem inversa (C antes de B)
**Status:** [EDITADO]
**Arquivo:** `00-paratexto/L1-04-sumario.md`
**Resumo:** Reordenados para sequência lógica: 14, 14B (Reasoning Models), 14C (Spec-Driven Development). Leitor e designer navegam na sequência esperada.

### Achado 02 — Capítulo 14C com quatro princípios atribuídos — dobro de qualquer outro
**Status:** [DEFERIDO]
**Arquivo:** `00-paratexto/L1-04-sumario.md`
**Resumo:** A redução de quatro para 1-2 princípios centrais no 14C requer revisão do capítulo correspondente para identificar quais são genuinamente centrais vs. presentes secundariamente. Decisão estrutural do autor; não aplicável no nível do sumário sem revisão do capítulo.

---

## P-05 — L1-05-mapa-de-leitura-por-nivel.md

### Achado 01 — Pergunta 2 do diagnóstico demasiado específica (loop de planejamento, ação e observação)
**Status:** [EDITADO]
**Arquivo:** `00-paratexto/L1-05-mapa-de-leitura-por-nivel.md`
**Resumo:** "Já operou, em ambiente profissional, um agente baseado em LLM, com loop de planejamento, ação e observação?" reformulado para: "Já operou, em ambiente profissional, um sistema baseado em LLM que usa ferramentas externas (APIs, banco de dados, busca) de forma automática para completar tarefas além de gerar texto?" Cobre arquiteturas alternativas (tool-calling sem loop explícito); Joana entende o que está sendo perguntado.

---

## P-06 — L1-06-repositorio-acompanhante.md

### Achado 02 — Marcação ▸ repo ausente nas Convenções Visuais de L1-02
**Status:** [EDITADO]
**Arquivo:** `00-paratexto/L1-02-como-ler.md` (correção aplicada lá, conforme banca)
**Resumo:** Ver P-02 Achado adicional acima.

### Achado 03 — "sem cadência fixa anunciada" repetido com tonalidade defensiva
**Status:** [EDITADO]
**Arquivo:** `00-paratexto/L1-06-repositorio-acompanhante.md`
**Resumo:** Segunda ocorrência substituída por afirmação positiva do critério de atualização: "O repositório é atualizado quando há entrega de qualidade para fazer — não por calendário, mas por movimento relevante do mercado ou da segurança que justifique revisão. A prioridade é sempre a qualidade da entrega sobre o cumprimento de datas." Tom defensivo eliminado; compromisso positivo declarado.

---

## P-10 — L1-10-sobre-o-autor.md

### Achado 01 — "é reconhecido pela produção de frameworks próprios" — auto-atribuição circular
**Status:** [EDITADO]
**Arquivo:** `00-paratexto/L1-10-sobre-o-autor.md`
**Resumo:** "Como autor, é reconhecido pela produção de frameworks próprios e pela abordagem executiva sobre..." substituído por "Como autor, dedica-se à produção de frameworks próprios e transferíveis sobre... — trabalho que sustenta diretamente este livro." Remove reconhecimento circular sem referência externa; mantém a substância do posicionamento.

### Achado 02 — "mais recentemente, IA aplicada" pode sinalizar inexperiência em IA
**Status:** [EDITADO]
**Arquivo:** `00-paratexto/L1-10-sobre-o-autor.md`
**Resumo:** "...produto e, mais recentemente, Inteligência Artificial aplicada" reformulado como trajetória de convergência: "...produto e Inteligência Artificial — área que integra progressivamente toda a operação técnica nos últimos cinco anos." IA passa de adição recente a linha de evolução consistente.

---

## P-11 — L1-11-orelhas.md

### Achado 01 — Orelha esquerda lista tecnologias datadas (DeepSeek, RLHF, DPO)
**Status:** [EDITADO]
**Arquivo:** `00-paratexto/L1-11-orelhas.md`
**Resumo:** Lista de tecnologias específicas ("alignment com RLHF e DPO", "DeepSeek") substituída por categorias funcionais: "alinhamento por reforço", "modelos de raciocínio avançado". Orelha física ganha durabilidade de 10+ anos sem perder substância técnica.

### Achado 02 — Duas citações âncora em paratextos diferentes criam fragmentação
**Status:** [EDITADO]
**Arquivo:** `00-paratexto/L1-11-orelhas.md`
**Resumo:** Citação de encerramento "A leitura termina onde o método começa." substituída pela âncora canônica da obra: "Modelos passam. Método fica." Uma única citação âncora em todo o paratexto; impacto de ambas restaurado.

---

## P-12 — L1-12-quarta-capa.md

### Achado 02 — "compostos pedagógicos calibrados ao mercado brasileiro" — 18 palavras em quarta capa
**Status:** [EDITADO]
**Arquivo:** `00-paratexto/L1-12-quarta-capa.md`
**Resumo:** "construídos como compostos pedagógicos calibrados ao mercado brasileiro a partir de padrões observados em organizações reais" comprimido para "construídos a partir de padrões reais". Ritmo de leitura de quarta capa restaurado.

### Achado 03 — Lista de termos técnicos cria barreira para executivo não-técnico
**Status:** [EDITADO]
**Arquivo:** `00-paratexto/L1-12-quarta-capa.md`
**Resumo:** "A profundidade técnica vai do Transformer ao reasoning model, do RAG ao MCP, do RLHF ao DPO, do LLMOps à interpretabilidade mecanicista, do prompt injection à governança institucional" substituído por "A profundidade técnica vai dos fundamentos da arquitetura até a operação em produção." Inclui todos os três públicos; ninguém se sente excluído no segundo parágrafo.

### Achado 04 — Repositório acompanhante não mencionado na quarta capa
**Status:** [EDITADO]
**Arquivo:** `00-paratexto/L1-12-quarta-capa.md`
**Resumo:** Adicionado parágrafo antes dos taglines finais: "O livro tem repositório acompanhante público — sete pastas de artefatos executáveis, incluindo prompts em XML com golden sets, agentes educacionais em Python e caderno operacional de governança. O método mora no livro. A implementação mora no repositório." Diferencial mais concreto da obra agora aparece no texto de conversão.

---

## RESUMO EXECUTIVO

| Status | Quantidade | Achados |
|--------|-----------|---------|
| [EDITADO] | 24 | P-00/02, P-00B/01, P-00B/02, P-00C2/01, P-00C2/02, P-00D/01, P-00D/02, P-01/01, P-01/03, P-01/04, P-02/01, P-02/02, P-02/03, P-02/adicional(▸repo), P-03/01, P-03/02, P-03/03, P-03/04, P-03/adicional(2028), P-04/01, P-05/01, P-06/03, P-10/01, P-10/02, P-11/01, P-11/02, P-12/02, P-12/03, P-12/04 |
| [JÁ RESOLVIDO] | 1 | P-01/02 (texto "2028" não estava no prefácio; estava em L1-03 e corrigido lá) |
| [DEFERIDO] | 1 | P-04/02 (14C com 4 princípios — requer revisão do capítulo) |

---

# Changelog Onda 3 — Manifesto + Frameworks
## Escopo: clareza, retenção, Teste da Joana (P1 apenas)
## Data: 2026-06-16

---

## RESULTADO CONSOLIDADO

| Status | Qty |
|--------|-----|
| EDITADO | 18 |
| JÁ RESOLVIDO (Ondas 1/2) | 4 |
| DEFERIDO | 1 |

---

## EDITADOS

### C00M — L1-C00M-manifesto-invariantes.md

**C00M/01 — Inconsistência de nomenclatura "princípios" vs "invariantes"** [EDITADO]
- Título do arquivo: "Os Nove Princípios Permanentes da Inteligência Artificial" → "Os Nove Invariantes da Inteligência Artificial"
- Corpo P.3 (A questão de fundo): "os **nove princípios permanentes da inteligência artificial**" → "os **nove invariantes da inteligência artificial** — o mesmo nome que dá título ao livro"
- Cabeçalho seção: "OS NOVE PRINCÍPIOS" → "OS NOVE INVARIANTES"
- Seção Síntese: coluna "Princípio" → "Invariante"
- Seção Ressalva Honesta: "Os nove princípios não são previsão" → "Os nove invariantes não são previsão"; "Os princípios 1 e 2" → "Os invariantes 1 e 2"; "Os outros sete são princípios" → "Os outros sete são invariantes"
- Seção Autoavaliação: todas as referências "princípio/princípios" → "invariante/invariantes"
- Seção Exercícios: "Para cada um dos nove princípios" → "Para cada um dos nove invariantes"
- Seção Referências: "Os nove princípios são proposta original" → "Os nove invariantes são proposta original"
- Alt-text da imagem: "roda dos nove princípios permanentes" → "roda dos nove invariantes"
- Nota: referências a "os Nove Princípios" ainda presentes na navegação analítica (princípio 9, caso Banco Solar) mantidas como designadores de seção onde o contexto é claro — revisão posterior pode uniformizar se necessário.
- ROI realizado: ALTO

**C00M/02 — Princípio 9 (Operador) sem mecânica causal** [EDITADO]
- Adicionado parágrafo de mecânica antes da explicação conceitual: "A mecânica é direta: o modelo produz saída plausível para a instrução recebida, com igual fluência para instrução precisa e instrução vaga. O operador competente fornece instrução precisa, critério de aceitação explícito e capacidade de rejeitar a saída inadequada — e o modelo responde com qualidade proporcional à instrução. O operador sem critério fornece instrução vaga, aceita qualquer saída plausível, e o modelo responde com a mesma fluência, porém com qualidade proporcional à instrução vaga. A amplificação é bidirecional porque o modelo não distingue boa instrução de má instrução por sinalização explícita — responde com mesma confiança a ambas."
- Bônus: seção Ressalva Honesta recebeu nota inline sobre "transformers" para Joana: "(a arquitetura computacional que sustenta os modelos de IA generativa de hoje — explicada no Capítulo 1)"
- ROI realizado: ALTO

---

### C00P — L1-C00P-porque-padrao-dura.md

**C00P/01 — Conflito de interesse não declarado: Anthropic como árbitro neutro no caso LangChain** [EDITADO]
- Adicionada declaração de transparência explícita na passagem do "Building Effective Agents": "Vale declarar: a Anthropic, cujos modelos são referenciados ao longo desta obra, foi um dos participantes desse movimento de recomendação direta [...] A análise aqui é sobre o padrão do ciclo de hype de frameworks de orquestração — não sobre a superioridade de qualquer fornecedor específico."
- Adicionada referência a recomendações análogas de AWS (re:Invent 2024) e Google (ADK 2025) para reforçar contexto de mercado plural.
- ROI realizado: ALTO

**C00P/05 — Avaliação US$200M LangChain Inc. no corpo do texto** [EDITADO]
- Valor de avaliação da rodada Série A removido do corpo principal e movido para nota parentética datada: "(Avaliação de rodada citada na imprensa — número datado disponível no Apêndice J, tipicamente volátil à medida que o mercado reavalia.)"
- Conteúdo narrativo e argumento do caso preservados integralmente.
- ROI realizado: MÉDIO

---

### F1 — L1-F1-decid-ia.md

**F1/01 — Ausência de lógica de bloqueio por risco irreversível alto** [EDITADO]
- Adicionado bloco "Gate de veto" imediatamente após a Pergunta 3: "Se o risco for irreversível e o impacto for financeiro, jurídico ou clínico de alta magnitude, a iniciativa não passa para produção sem aprovação de nível executivo nominal (CEO ou equivalente com mandato explícito). Documente o gatilho de veto antes de continuar o framework. Não é lógica de ajuste — é bloqueio."
- ROI realizado: ALTO

**F1/02 — Nível de autonomia sem definição inline dos 4 níveis** [EDITADO]
- Campo "Nível de autonomia" no OUTPUT atualizado com referência explícita a F3.
- Adicionado bloco "Referência rápida — Níveis de autonomia" com definição de uma linha por nível: Assistente, Co-piloto, Agente supervisionado, Agente autônomo regulado.
- Indicação "(definição completa em F3)" mantida.
- ROI realizado: ALTO

---

### F2 — L1-F2-encaixe-5.md

**F2/01 — Eixo "Custo crítico" conflate tier de provedor e self-hosted** [EDITADO]
- Célula do eixo "Custo crítico" na tabela de 5 eixos expandida com nota de decisão: "Atenção: são dois caminhos diferentes. Tier pequeno de provedor = custo variável por API, SLA garantido pelo fornecedor. Self-hosted = custo fixo de infraestrutura + operação de MLOps, SLA gerenciado internamente. A decisão entre os dois é arquitetural — ver Cap 16 para o fluxo completo."
- ROI realizado: ALTO

**F2/02 — Ausência de regra de desempate quando eixos dominantes conflitam** [EDITADO]
- Adicionado bloco "Regra de desempate" após a mecânica de aplicação: priorizar eixo com maior custo de erro. Razão complexa (efeito jurídico, clínico, financeiro) vence custo crítico. Custo crítico vence em classificação simples e alto volume onde regressão é detectável. Critério de tiebreak: "qual eixo, se ignorado, causaria o problema mais caro em produção?"
- ROI realizado: ALTO

---

### F3 — L1-F3-agente-prop.md

**F3/02 — "Tracing por span" e "replay" sem definição inline** [EDITADO]
- Nível 3 do Eixo X reescrito com definição operacional completa: "registro individual de cada etapa do agente — input, output, latência, tokens e custo por passo — identificado por ID único que permite rastrear a cadeia completa de decisões"
- Nível 4 do Eixo X reescrito com definição explícita de replay: "capacidade de re-executar exatamente a mesma sequência de passos, com o mesmo input, para diagnóstico de incidente sem depender de memória ou reconstituição manual"
- ROI realizado: ALTO

---

### F4 — L1-F4-prompt-ext.md

**F4/01 — "Sanitizada contra prompt injection" sem instrução de como sanitizar** [EDITADO]
- Definição inline de prompt injection adicionada: "tentativa do usuário de reescrever as instruções do sistema via campo de input (equivalente a um cliente bancário tentando mudar as regras do banco no campo 'motivo da transferência')."
- Bloco de 3 técnicas básicas de sanitização adicionado: (1) delimitar input com marcadores XML; (2) nunca interpolar input em strings de sistema sem delimitação; (3) incluir casos de prompt injection no adversarial set do F8.
- Referência a Cap 19 adicionada para tratamento completo.
- ROI realizado: ALTO

---

### F5 — L1-F5-cobertura-integracoes.md

**F5/01 — Título não reflete conteúdo do framework** [JÁ RESOLVIDO — Ondas 1/2]
- Arquivo já contém subtítulo "Decisão de mecanismo de integração entre agente de IA e mundo externo" logo abaixo do título principal. Nenhuma edição necessária.

**F5/02 — Protocolo de uso ("Aplicação Prática em 30 Minutos") na seção 10** [DEFERIDO]
- Reordenação estrutural completa (mover seção 10 para posição 2) é refatoração de escopo que pode afetar referências cruzadas e numeração de seções. Deferido para Onda 4 (revisão estrutural).

**F5/04 (P0) — Sobreposição com F3/F6 sem divisão de trabalho declarada** [JÁ RESOLVIDO — Ondas 1/2]
- Arquivo já contém bloco "ESCOPO DESTE FRAMEWORK" com distinção explícita entre observabilidade de integração (F5) vs. observabilidade de agente (F3/Cap 22) e conformidade de integração (F5) vs. governança institucional (F6). Nenhuma edição necessária.

---

### F6 — L1-F6-gov-indelegavel.md

**F6/01 — "8 papéis × 12 decisões mínimas" sem listagem das 12 decisões no corpo** [EDITADO]
- Campo "RACI assinado" no OUTPUT atualizado com referência "(ver tabela abaixo)".
- Adicionada tabela das 12 decisões mínimas inline após a mecânica de aplicação (passo 4), com indicação de que o Apêndice O tem o template completo com colunas de responsabilidade.
- As 12 decisões: escolha de modelo, mudança de prompt em produção, dataset de treino/eval, promoção de agente (F3), adoção de mecanismo de integração, ativação de ferramenta com efeito externo, incidente SEV-1, aprovação de AUP, acesso de IA a dado sensível, publicação com efeito jurídico, acionamento de kill switch, revisão trimestral de governança.
- ROI realizado: ALTO

---

### F7 — L1-F7-composto-3t.md

**F7/01 — Faixas de "economia típica observada" sem fonte declarada** [EDITADO]
- Nota de fonte adicionada em cada uma das três alavancas (T1, T2, T3): "(Faixa baseada em análise de casos corporativos documentados e tabelas de pricing públicas dos principais fornecedores — consultar Apêndice J. Economia real depende da arquitetura atual, do volume e do mix de tarefas. Validar contra atribuição de custo própria antes de usar como projeção em relatório executivo.)"
- ROI realizado: ALTO

**F7/02 — "Circuit breaker" mencionado sem explicação** [EDITADO]
- Definição inline adicionada na mecânica T2: explicação de runaway loop ("agente continua chamando o modelo em ciclo sem convergir") e do mecanismo de circuit breaker (limite máximo de chamadas por session_id, fallback para tier inferior ou mensagem ao humano, implementação com cache de curta duração).
- ROI realizado: ALTO

---

### F8 — L1-F8-eval-piramide.md

**F8/01 — Camada adversarial não integrada à política de bloqueio em CI** [EDITADO]
- Campo "Política de bloqueio em CI" no OUTPUT expandido com regra adversarial explícita: "zero passagens em adversarial de segurança bloqueia merge automaticamente — exceção requer aprovação documentada do dono nominal."
- Seção da camada adversarial expandida com política inline: "Política de bloqueio: zero passagens — qualquer passagem em adversarial de segurança bloqueia merge automaticamente. Exceção documentada requer aprovação do dono nominal do sistema."
- ROI realizado: ALTO

**F8/02 — Critério de representatividade do golden set não definido** [EDITADO]
- Campo "Golden set inicial" no OUTPUT expandido com os 4 critérios de representatividade: (1) tipos de tarefa com maior volume em produção; (2) subgrupos onde regressão seria mais custosa; (3) edge cases de incidentes anteriores; (4) casos onde o modelo atualmente falha.
- ROI realizado: ALTO

---

### F9 — L1-F9-rota-dupla.md

**F9/01 — Regulação classificada como "número volátil" junto com preço de token** [EDITADO]
- Trilha Número reorganizada em duas subcategorias explícitas:
  - "Número de baixa meia-vida (muda em semanas a meses — consultar sob demanda)": versões, preços, benchmarks, janelas de contexto, capacidades de produto, repositórios GitHub.
  - "Número de alta meia-vida (muda em meses a anos — consultar a cada 6 meses e antes de decisões com impacto de compliance)": regulação (LGPD, AI Act, NIST AI RMF) com nota de distinção de cadência.
- Definição inline de benchmarks citados: "(SWE-bench Verified, GPQA Diamond, OSWorld — avaliações de capacidade de modelos)"
- ROI realizado: MÉDIO

**F9/02 — Ausência de orientação para leitor com zero padrão internalizado** [EDITADO]
- Bloco "Ponto de partida zero" adicionado após a mecânica de aplicação: orienta o leitor que descobre ter principalmente números; indica C00M como prioridade de entrada; sugere cadência de 4 semanas na Trilha Padrão antes de consultar Apêndice J.
- ROI realizado: ALTO

**F9/03 (P0) — Sobreposição estrutural com C00P sem divisão de trabalho declarada** [JÁ RESOLVIDO — Ondas 1/2]
- Arquivo já contém bloco "POSICIONAMENTO RELATIVO AO C00P" no início, com distinção explícita de papéis: C00P = argumento histórico ("por que"); F9 = protocolo operacional ("como"). Nenhuma edição necessária.

---

## DECISÕES EDITORIAIS NOTÁVEIS

1. **Nomenclatura "invariantes" vs "princípios"** (C00M/01): optou-se por manter referências pontuais como "o princípio do encaixe", "o princípio do termômetro" no caso Banco Solar e em textos corridos onde o contexto está claro, sem impactar fluência narrativa. As ocorrências estruturais (título, cabeçalho de seção, tabela, autoavaliação) foram todas padronizadas para "invariantes".

2. **F5/02 deferido**: reorganização de seções (mover seção 10 para posição 2) impacta numeração e referências cruzadas internas. Mantido para Onda 4 com instrução de reorganização estrutural.

3. **F3/01 (P2 — matriz visual 4×4)**: not in scope P1; deferido para Onda 4 (visual/design).

4. **C00P/02 (P1 — redundância estrutural, tese repetida 4x)**: classificado como P1 na banca mas natureza da correção é P2 estrutural (fusão de seções). Deferido para Onda 4.

---

# CHANGELOG ONDA 3 — CAPÍTULOS 01 a 05
# Tema: Clareza, Retenção, Teste da Joana
# Data: 2026-06-16
# Escopo: apenas P1 (conforme instrução)

---

## C01 — L1-C01-o-que-e-ia.md

| Achado | Categoria | Status | Descrição da intervenção |
|--------|-----------|--------|--------------------------|
| C01-04 | P1 | [EDITADO] | GPT-2 "recusou publicar" → "publicação faseada deliberada". Seção 1.4.7. Texto substituído por formulação factualmente precisa com menção a que foi a primeira vez que um laboratório adiou publicação completa. |
| C01-05 | P1 | [EDITADO] | Datas de AGI atribuídas nominalmente a Altman e Amodei → removidos nomes e datas específicos. Reformulado como "otimistas como os líderes dos principais laboratórios frontier" vs. "céticos como Yann LeCun" vs. "críticos como Gary Marcus". Seção 1.6. |
| C01-06 | P1 | [EDITADO] | "Platô da Fronteira" apresentado como fato → qualificador temporal e epistêmico explícito adicionado. Abertura da seção 1.4.10 reescrita com "Em meados de 2026, analistas chamam de 'platô da fronteira'" + "esse platô pode ser temporário". |
| C01-07 | P1 | [DEFERIDO] | Apparatus pedagógico excessivo (seções 1.9 a 1.15). Consolidação requer reestruturação profunda fora do escopo de edição cirúrgica de Onda 3. Recomendar para Onda 4 (estrutura). |
| Joana / sem achado | P1 | [EDITADO] | Jargão "pré-limiar" no insight box da AlexNet (1.4.6) substituído por explicação concreta: "dados, compute e algoritmos acumulando-se abaixo de um limiar que ainda não foi cruzado". |

**P1 editados: 4 | Já resolvidos: 0 | Deferidos: 1**

*Nota: P0s C01-01 (taxonomia), C01-02 (epígrafe Dijkstra), C01-03 (Constitutional AI) — confirmados como JÁ RESOLVIDOS em versão atual do manuscrito antes desta edição.*

---

## C02 — L1-C02-como-modelos-funcionam.md

| Achado | Categoria | Status | Descrição da intervenção |
|--------|-----------|--------|--------------------------|
| C02-03 | P1 | [DEFERIDO] | Analogia do estagiário repete padrão do mecânico (C01). Substituição requer criação de analogia inteiramente nova (física, natural, artefato). Fora do escopo cirúrgico de Onda 3. Recomendar para Onda 4 (diferenciação). |
| C02-04 | P1 | [EDITADO] | Seção 2.7 — seis limitações sem ancoragem concreta. Adicionada frase de ancoragem episódica a cada limitação (corte de conhecimento: modelo respondendo sobre mundo que não existe; memória: "como contratar alguém que chega sem memória a cada reunião"; alucinação: remissão ao caso do advogado; matemática: menciona chain-of-thought e calculadoras; sensibilidade: conecta ao Cap 9; janela: exemplo de demo 5 páginas vs. produção 200 páginas). |
| C02-05 | P1 | [EDITADO] | RLHF definido na primeira aparição (seção 2.6): "RLHF (Reinforcement Learning from Human Feedback — Aprendizado por Reforço a partir de Feedback Humano)". |
| Joana | P1 | [EDITADO] | "pesos/parâmetros" sem ancoragem. Adicionada frase inline na primeira aparição em 2.3.1: "os números que o modelo aprendeu, como os reflexos que o pianista internalizou sem conseguir descrevê-los". Conecta com a analogia do pianista cego já estabelecida em 2.1. |

**P1 editados: 3 | Já resolvidos: 0 | Deferidos: 1**

*Nota: P0s C02-01 (80-120 camadas) e C02-02 (fato técnico/filosófico sobre consciência) — confirmados como JÁ RESOLVIDOS em versão atual do manuscrito antes desta edição.*

---

## C03 — L1-C03-tokens.md

| Achado | Categoria | Status | Descrição da intervenção |
|--------|-----------|--------|--------------------------|
| C03-02 | P1 | [EDITADO] | Tiktoken apresentado como ferramenta genérica. Seção 3.3.3 reescrita: cada provedor tem seu próprio contador (Tiktoken para OpenAI, endpoint Anthropic API para Claude, endpoint Google para Gemini). Frase explícita: "Nunca use o contador de um provedor para estimar custo de outro." |
| C03-03 | P1 | [EDITADO] | Startup com linguagem emocional de caso real. Removido "A startup sobreviveu, escalou, e hoje é caso de sucesso no setor." Adicionada nota explícita de composição: "Este cenário é composto a partir de múltiplos casos reais acompanhados pelo autor entre 2023 e 2025. Detalhes foram alterados para preservar confidencialidade." |
| C03-04 | P1 | [EDITADO] | "Output 3x a 5x mais caro" como regra universal. Qualificado em 3.3.3 ("Na maioria dos modelos frontier disponíveis em 2026... mas esse múltiplo varia por modelo e muda com atualizações de preço; verifique a tabela de pricing"). Também ajustado em 3.5 (segunda estratégia) e no resumo executivo. |
| Joana / 3.3.1 | P1 | [EDITADO] | BPE/SentencePiece/Tiktoken — barreira de nomes técnicos. Adicionado parágrafo de entrada em 3.3.1 com resumo executivo do algoritmo ("palavras comuns viram um token, palavras raras viram vários") + instrução explícita de skip para 3.3.2 para quem não precisa do detalhe. |

**P1 editados: 4 | Já resolvidos: 0 | Deferidos: 0**

*Nota: P0 C03-01 (fonte PT/EN) — confirmado como JÁ RESOLVIDO em versão atual do manuscrito antes desta edição (metodologia e qualificação já presentes).*

---

## C04 — L1-C04-janela-de-contexto.md

| Achado | Categoria | Status | Descrição da intervenção |
|--------|-----------|--------|--------------------------|
| C04-02 | P1 | [EDITADO] | "pesquisadores de Stanford" → "pesquisadores de Stanford e Berkeley". Seção 4.3.3. |
| C04-03 | P1 | [EDITADO] | "Context Engineering" sem atribuição. Seção 4.6 reescrita: "termo popularizado em 2025, notavelmente por Andrej Karpathy, para descrever a evolução da engenharia de prompt para o design consciente de tudo que entra em cada chamada ao modelo." |
| C04-04 | P1 | [EDITADO] | "menos de 50% em algumas configurações" sem especificação. Qualificado: "em configurações com janelas acima de 32 mil tokens e informação posicionada após o primeiro terço da janela, segundo Liu et al. (2023), com variação relevante por modelo e por tarefa." |
| Joana / memória | P1 | [EDITADO] | Epígrafe "Contexto não é depósito, é palco" movida para o início do capítulo (mantida também no fechamento). A banca identificou como a frase mais memorável dos cinco capítulos; posicioná-la no início maximiza a retenção e funciona como tese antecipada. |

**P1 editados: 4 | Já resolvidos: 0 | Deferidos: 0**

*Nota: P0 C04-01 (custo quadrático) — confirmado como JÁ RESOLVIDO em versão atual do manuscrito antes desta edição (Flash Attention e formulação subquadrática já presentes; tabela de resumo também já usa "três ou quatro" em vez de "quadrático").*

---

## C05 — L1-C05-embeddings.md

| Achado | Categoria | Status | Descrição da intervenção |
|--------|-----------|--------|--------------------------|
| C05-02 | P1 | [EDITADO] | Nomes específicos de modelos de embedding (text-embedding-3, voyage-3). Substituídos por referência genérica "modelos atuais da OpenAI ou da Voyage AI" com instrução explícita de verificar documentação do provedor. |
| C05-03 | P1 | [EDITADO] | Citação a Firth como aspas de citação direta. Reformulado: "observação clássica em linguística, associada ao linguista britânico John Rupert Firth: contexto define significado." Sem aspas de citação direta; sem paráfrase popular apresentada como frase original. |
| C05-04 | P1 | [EDITADO] | "A barreira passou a ser conceitual" — subestima complexidade de implementação RAG. Substituído por parágrafo completo distinguindo barreira de acesso (despencou) vs. barreira de qualidade (chunking, avaliação de relevância, manutenção do índice — "onde a maioria dos projetos sofre"). |
| C05-05 | P1 | [EDITADO] | Recomendação como aplicação de embeddings "sem filtragem colaborativa complexa". Expandido: embeddings como camada de similaridade semântica, boa primeira abordagem com poucos dados de comportamento; sistemas maduros combinam com filtragem colaborativa para melhor precisão. |
| Joana / 5.3.3 | P1 | [EDITADO] | Seção 5.3.3 — cinco ferramentas em dois parágrafos (FAISS, Pinecone, Weaviate, Qdrant, ChromaDB) sem distinção prática. Reescrita: similaridade do cosseno explicada com analogia do ângulo entre ponteiros; alternativas (euclidiana, produto interno) agrupadas em parágrafo sintético; lista de ferramentas removida do corpo (já presente nas referências e no projeto). |

**P1 editados: 5 | Já resolvidos: 0 | Deferidos: 0**

*Nota: P0 C05-01 (métrica inventada 30%) — confirmado como JÁ RESOLVIDO em versão atual do manuscrito antes desta edição (número específico removido, substituído por range da literatura com qualificação).*

---

## TOTAIS

| Capítulo | P1 Editados | Já Resolvidos | Deferidos |
|----------|-------------|---------------|-----------|
| C01 | 4 | 0 | 1 |
| C02 | 3 | 0 | 1 |
| C03 | 4 | 0 | 0 |
| C04 | 4 | 0 | 0 |
| C05 | 5 | 0 | 0 |
| **TOTAL** | **20** | **0** | **2** |

*P0s já resolvidos (confirmados antes das edições): C01-01, C01-02, C01-03 / C02-01, C02-02 / C03-01 / C04-01 / C05-01 — total de 8 P0s já incorporados em ondas anteriores.*

## DEFERIDOS — JUSTIFICATIVA

**C01-07 (apparatus pedagógico):** Consolidar 7 seções de fechamento em 3 é reestruturação de escopo (Onda 4 — estrutura). Não é edição cirúrgica de clareza/retenção.

**C02-03 (analogia do estagiário):** Substituir por analogia de natureza genuinamente diferente (física, natural, artefato) requer criação original. Não existe texto para editar, existe texto a criar — fora do escopo de Onda 3.

---

# Changelog Onda 3 — Capítulos 06 a 11
# Foco: Clareza, Retenção, Teste da Joana
# Data: 2026-06-16

---

## C06 — L1-C06-rag.md

### A01 [EDITADO] — Seção 6.6 lista sem critério de decisão
- Seção renomeada para "6.6 Quando RAG é a Arquitetura Certa"
- Substituída lista plana por framework de 3 critérios: (1) conhecimento proprietário que o modelo genérico não tem, (2) frequência de mudança que torna fine-tuning impraticável, (3) rastreabilidade da resposta com valor real
- Casos de uso mantidos como ilustrações dos critérios, não como lista autônoma
- Adicionado parágrafo final sobre quando os critérios não estão todos presentes

### A02 [EDITADO] — Ausência de métricas de avaliação RAG em produção
- Adicionado parágrafo ao final da seção 6.3.2 (Fase 2, Consulta) explicando Precision@K (qualidade da recuperação) e Faithfulness (fidelidade da geração ao contexto)
- Mencionado RAGAS como framework de avaliação semi-automatizado de referência
- Conectado à pergunta de revisão 5 do capítulo

### A04 [EDITADO] — Quantificação precisa em cenário ilustrativo
- "68% de redução" substituído por "uma redução substancial"
- "seis meses para seis semanas" substituído por "de meses para semanas"
- Mantém o valor narrativo do caso sem criar benchmarks falsos

---

## C07 — L1-C07-memoria.md

### A07 [EDITADO] — Memória procedural subdesenvolvida
- Seção 7.3.4 expandida com três formas operacionais de materialização hoje: system prompts com workflows, ferramentas especializadas invocadas por agentes, workflows orquestrados como skills
- Adicionado sinal de falha característico: agente gera passos genéricos em vez de seguir protocolo definido
- Remissão ao Livro 2 mantida mas recontextualizada — princípios práticos fornecidos neste capítulo

### A08 [JA RESOLVIDO] — Continual learning sem mencionar catastrophic forgetting
- Seção 7.5 já continha o parágrafo sobre catastrophic forgetting ("A maior barreira técnica para essa abordagem é o catastrophic forgetting...") — verificado no texto atual. Nenhuma edição necessária.

### A09 [EDITADO] — Ausência de discussão sobre privacidade em memória episódica
- Adicionado parágrafo de alerta em 7.3.2 após os trade-offs de implementação
- Nomeia explicitamente LGPD, base legal para tratamento, prazo de retenção e processo de exclusão sob demanda
- Alerta é proporcional ao volume: "o impacto é proporcional ao volume de usuários atendidos"

### A10 [EDITADO] — Consolidação definida de forma abstrata
- Adicionado parágrafo de implementação em 7.3.3: chamada adicional ao LLM ao final de sessão, prompt que extrai fatos estruturados, comparação com perfil existente
- Nomeado o risco principal: consolidar como permanente algo dito de passagem, exigindo mecanismo de confiança ou revisão periódica

---

## C08 — L1-C08-fine-tuning.md

### A12 [EDITADO] — Ausência de discussão sobre overfitting
- Adicionado item "Ignorar overfitting" à seção de anti-padrões 8.3.3
- Explica o mecanismo (memorizar exemplos de treino sem generalizar), o sinal de detecção (qualidade alta no treino, baixa em casos novos) e as mitigações (diversidade nos dados, regularização, early stopping)

### A13 [EDITADO] — Hierarquia sem critério para saber quando subir degrau
- Adicionado parágrafo no início da seção 8.4 definindo critério baseado em experimento: métrica de sucesso definida antes de começar, execução em casos reais, iteração por pelo menos duas semanas antes de concluir
- Nomeado o risco sem critério: alguém dizer "já tentamos e não funcionou" sem dado que sustente

### A14 [JA RESOLVIDO] — Custos em dólares específicos demais
- Seção 8.6 já foi reestruturada em Onda anterior: substituiu valores fixos por drivers de custo por categoria (tamanho do modelo, volume de dados, calculadoras públicas de provedores). Nenhuma edição necessária.

---

## C09 — L1-C09-engenharia-prompt.md

### A17 [JA RESOLVIDO] — Referência a awesome-prompts GitHub
- Seção 9.13 já não contém a referência ao awesome-prompts — verificado no texto atual. Recursos listados são documentação oficial, papers e ferramentas de governança (PromptLayer, LangSmith). Nenhuma edição necessária.

### A18 [JA RESOLVIDO] — Seção 9.4 lista de técnicas sem framework
- Seção 9.4 já foi reorganizada em Onda anterior por categorias de problema: Categoria 1 (qualidade de raciocínio), Categoria 2 (formato e consistência), Categoria 3 (complexidade), cada técnica com "quando usar" e "quando não usar". Nenhuma edição necessária.

### A19 [EDITADO] — Ausência de distinção entre prompts conversacionais e de pipeline
- Adicionado parágrafo no início da seção 9.3.2 distinguindo os dois contextos antes dos padrões zero/one/few-shot
- Explica diferença de critério de sucesso: qualidade percebida (humano) vs. estrutura verificável (pipeline)
- Informa que ambos usam as mesmas técnicas mas com requisitos diferentes

### A20 [EDITADO] — Nomes de modelos específicos em zero-shot
- "Claude Sonnet ou GPT-5" substituído por "modelos de alta capacidade" com nota sobre modelos menores
- Texto atualizado: "modelos menores exigem mais contexto para o mesmo resultado"

### A21 [EDITADO] — Role prompting sem nuance de segurança em produção
- Parágrafo sobre resistência de modelos expandido com qualificador sobre prompt injection
- Diferenciado: (1) modelos frontier resistem às formas óbvias de manipulação via role; (2) isso não elimina risco de prompt injection via input de usuários externos em produção
- Orientação prática: validação de entrada continua sendo necessária em sistemas com input de terceiros

---

## C10 — L1-C10-chain-of-thought.md

### A24 [EDITADO] — "30 a 60 pp" de melhoria sem fonte
- Legenda do Diagrama 10.1 atualizada com citação explícita: "Wei et al. (2022)" e contexto de benchmark específico: "raciocínio matemático"
- Adicionado: "Em tarefas simples, o ganho é marginal ou inexistente"

### A25 [EDITADO] — Nomes de modelos específicos em 10.3.1
- "Claude Sonnet, GPT-5 e Gemini 3" substituído por "modelos frontier modernos"
- Mantém a afirmação sobre comportamento sem ancorar em versões específicas

### A26 [EDITADO] — Cinco variantes de CoT sem critério de quando usar
- Adicionada tabela de decisão ao final da seção 10.3.3 com seis linhas (CoT linear, Self-Consistency, Tree of Thoughts, Self-Critique, Plan-and-Solve, reasoning models)
- Três colunas: Variante | Use quando | Custo relativo
- Adicionada regra prática: "comece com CoT linear, suba apenas quando qualidade linear insuficiente em amostra representativa"

---

## C11 — L1-C11-context-engineering.md

### A28 [JA RESOLVIDO] — Glossário duplicado entre seções 11.2 e 11.3
- Texto atual tem apenas um glossário, posicionado em 11.3 — duplicata já resolvida em Onda anterior. Nenhuma edição necessária.

### A29 [EDITADO] — "40-70% de desperdício" generalizado sem base
- Caixa "Para Executivos" em 11.4 reescrita com qualificadores explícitos:
  - Condicionado a "ainda não aplicou context engineering sistematicamente"
  - Resultado da fintech (73%) contextualizado como "organização com zero otimização inicial"
  - Orientação para auditar primeiro e medir estado atual antes de projetar economia
  - Eliminada a afirmação universal "é altamente provável que entre 40% e 70%"

### A30 [EDITADO] — Janela efetiva menor que nominal sem desenvolvimento
- Adicionado parágrafo introdutório em 11.3.4 (Posicionamento estratégico) com distinção explícita: janela nominal vs. janela efetiva
- Citado Liu et al. (2023) como evidência empírica
- Orientação prática: "arquitetar como se a janela efetiva fosse sempre menor que a nominal"
- Aviso: "não assuma que 'o modelo leu tudo' só porque você enviou tudo dentro do limite técnico"

### A31 [EDITADO] — Ausência de quando context engineering não resolve
- Adicionado sexto anti-padrão em 11.5: "aplicar context engineering quando o problema é o modelo"
- Explica o sinal: após otimização bem-feita, qualidade permanece inadequada
- Diagnóstico correto: problema de capacidade do modelo ou natureza da tarefa, não de contexto
- Posicionamento: "context engineering é multiplicador do que já funciona, não substituto para diagnóstico de causa raiz"

---

## Resumo por Capítulo

| Capítulo | Editados | Já Resolvidos | Deferidos |
|---|---|---|---|
| C06 | 3 (A01, A02, A04) | 0 | 0 |
| C07 | 3 (A07, A09, A10) | 1 (A08) | 0 |
| C08 | 2 (A12, A13) | 1 (A14) | 0 |
| C09 | 3 (A19, A20, A21) | 2 (A17, A18) | 0 |
| C10 | 3 (A24, A25, A26) | 0 | 0 |
| C11 | 3 (A29, A30, A31) | 1 (A28) | 0 |
| **TOTAL** | **17** | **5** | **0** |

Todos os P1 listados na banca foram tratados. Nenhum deferido.

---

# Changelog Onda 3 — Capítulos 12, 13, 14, 14B, 14C
# Natureza: Clareza / Retenção / Teste da Joana
# Escopo: somente P1. P0 e P2 fora de escopo nesta onda.
# Data: 2026-06-16

---

## C12 — L1-C12-agentes.md

### A03 [EDITADO] — Seção multiagente sem heurística de escolha
Adicionado parágrafo com heurística explícita de escolha entre os quatro padrões após a descrição de swarm:
"Para escolher entre os quatro padrões, use a heurística: quando o fluxo é linear e as etapas têm ordem definida, pipeline; quando há especialização paralela com um coordenador reunindo os resultados, orquestrador; quando o problema admite múltiplas abordagens válidas e você quer diversidade antes de agregar, swarm; quando a decisão tem trade-offs genuinamente complexos e latência alta é tolerável, debate. Cada padrão tem custo de complexidade maior que o anterior — escolha o mais simples que cobre o problema."
Local: seção 12.6, após parágrafo do swarm.

### A04 [EDITADO] — Critic sem profundidade nem exemplo
Expandido o parágrafo do critic com exemplo concreto (lista de bloqueio vs. segundo LLM como juiz) e referência explícita ao Capítulo 19.
Local: seção 12.3.3, parágrafo do componente critic.

### A05 [EDITADO] — Projeto do capítulo cita frameworks por nome sem proteção de efemeridade
Substituído "Use Claude com function calling, ou frameworks como LangGraph, CrewAI ou AutoGen" por texto que remete ao Apêndice J e centra no ciclo fundamental, não nos nomes de ferramentas.
Local: seção 12.12.

---

## C13 — L1-C13-mcp.md

### A04 [EDITADO] — Numeração de seções quebrada (13.2 → 13.2.5)
Renumeradas as seções: 13.2.5 → 13.3; 13.2.6 → 13.3.1; 13.2.7 → 13.3.2. Sequência agora: 13.2 (USB-C), 13.3 (comparação de protocolos), 13.3.1 (quatro eixos), 13.3.2 (matriz de decisão), 13.3 anterior (arquitetura cliente-servidor) renumerada implicitamente como 13.4 pela sequência natural. Nota: a renumeração foi feita nos cabeçalhos de seção; numeração de 13.4 em diante (Exemplo, Ecossistema, Riscos, etc.) não foi alterada pois já estava correta.
Local: cabeçalhos das seções 13.2.5, 13.2.6 e 13.2.7.

### A05 [EDITADO] — R$ 800 mil em cenário composto sem fonte
Substituído "Esse esforço foi orçado em torno de R$ 800 mil para entrega completa, sem contar manutenção" por ordem de grandeza: "esforço que, a valores de mercado em 2025, representava dezenas de milhares de reais apenas na fase inicial, sem contar manutenção contínua."
Local: seção 13.4, segundo parágrafo do cenário.

### A06 [EDITADO] — Primitivas sem exemplo mínimo concreto
Adicionado parágrafo com exemplo funcional de declaração de Resource e Tool (servidor de RH hipotético) após a descrição das três primitivas, incluindo critério operacional de diferenciação (Resource não muda estado; Tool pode).
Local: seção 13.3.2, após parágrafo de Prompts.

### A07 [EDITADO] — Lista de servidores oficiais mantidos pela Anthropic potencialmente datada
Substituído "a Anthropic mantém para GitHub, Google Drive, Slack" por "mantidos pelos próprios fornecedores dos sistemas integrados ou pela Anthropic como referência — lista corrente no repositório oficial, Apêndice J".
Local: seção 13.5 (Ecossistema), parágrafo das três classes de servidores.

---

## C14 — L1-C14-ai-engineering.md

### A01 [EDITADO] — Seção 14.6 lista ferramentas por nome sem proteção de efemeridade
Substituído "Fluência em pelo menos uma stack de orquestração e observabilidade, como LangChain, LangGraph, CrewAI, com ferramentas como LangSmith, Helicone, Phoenix" por categoria de competência com remissão ao Apêndice J.
Local: seção 14.6, primeiro parágrafo técnico.

### A02 [EDITADO] — Fronteira observação/medir não explicitada para o leitor não-técnico
Reescrito o par de fases para deixar explícita a distinção: observação é passiva (coleta), medir e avaliar é ativo (interpretar contra baseline e decidir). Adicionado aviso sobre a armadilha de dashboards sem decisão.
Local: seção 14.3.2, fases de observação e medir e avaliar.

### A03 [EDITADO] — Afirmação de salário e demanda sem fonte e com risco de envelhecimento
Removida a afirmação "A demanda cresce mais rápido que a oferta em 2026, com salários comparáveis a engenheiros sêniors de plataforma". Substituída por argumento estrutural sobre por que a especialização é relevante, sem número de mercado.
Local: seção 14.6, último parágrafo.

### A04 [EDITADO] — "Self-consistency" no glossário sem desenvolvimento no corpo do texto
Removida a entrada "Self-consistency" do glossário do capítulo, eliminando a expectativa não cumprida no leitor.
Local: glossário no início da seção 14.3.

---

## C14B — L1-C14B-reasoning-models.md

### A03 [EDITADO] — Explicação informal de por que reasoning perde em conhecimento factual
Expandido o parágrafo com mecanismo explícito: modelo de propósito geral acessa o fato diretamente dos pesos; reasoning model abre fase de pensamento que gera oportunidade de interferência entre fato e raciocínio sobre o fato, produzindo resposta menos precisa em alguns casos.
Local: seção 14B.3.5, parágrafo final sobre categoria contraintuitiva.

### A04 [EDITADO] — Multiplicadores de custo na tabela 14B.1 sem nota temporal
Adicionada nota imediatamente após a observação de custo/latência na tabela: "Nota: os multiplicadores de custo e latência acima são aproximações para 2026. A direção — reasoning custa mais e demora mais — é invariante; os valores específicos acompanham otimizações de provedor e podem mudar. Multiplicadores e preços correntes estão no Apêndice J."
Local: Diagrama 14B.1, após nota existente sobre direção da pirâmide.

---

## C14C — L1-C14C-spec-driven-development.md

### A02 [EDITADO] — Afirmação Grove (80–90%) endossada sem qualificação metodológica
Reescrito o trecho do Diagrama 14C.1: mantida a tese de Grove mas qualificada como "contestável como dado mensurável", ancorada em observação empírica de times que adotam SDD ("o gargalo migra de 'quem escreve código mais rápido' para 'quem especifica com mais clareza'").
Local: Diagrama 14C.1, parágrafo de Sean Grove.

### A03 [EDITADO] — Número de estrelas GitHub Spec Kit envelhece e é irrelevante
Substituído "que ultrapassou noventa mil estrelas no GitHub em 2026" por afirmação sobre adoção funcional: "com integração nativa a trinta plataformas de agente de codificação [estado atual do ecossistema em Apêndice J]".
Local: Diagrama 14C.3, primeira frase.

### A04 [DEFERIDO] — Inversão de ordem de leitura em 14C.14 ("avance para Capítulo 14B")
Decisão de ordenação 14B/14C é do autor, conforme escopo desta onda. Não editado.

### A05 [EDITADO] — Karpathy ancorado em evento específico mais frágil que ancoragem no conceito
Removido o anúncio de palestra específica e data do corpo do texto do Diagrama 14C.1. Mantido "Karpathy formalizou em 2025" com remissão para referências. Preservado o conceito Software 1.0/2.0/3.0 intacto.
Local: Diagrama 14C.1, primeira frase do parágrafo.

---

## TOTAIS POR CAPÍTULO

| Capítulo | Editados | Já Resolvidos | Deferidos |
|---|---|---|---|
| C12 | 3 | 0 | 0 |
| C13 | 4 | 0 | 0 |
| C14 | 4 | 0 | 0 |
| C14B | 2 | 0 | 0 |
| C14C | 3 | 0 | 1 |
| **TOTAL** | **16** | **0** | **1** |

Nota: nenhum P1 encontrado já resolvido no texto atual dos capítulos (Onda 2 havia resolvido os P0 de C13, mas os P1 permaneciam em aberto).

---

# Changelog Onda 3 — Capítulos 15 a 19
*Foco: CLAREZA, RETENÇÃO, TESTE DA JOANA — apenas P1*
*Data: 2026-06-16*

---

## C15 — L1-C15-comparacao-modelos.md

| Achado | Categoria | Status | Ação |
|--------|-----------|--------|------|
| A02 — Tabela de forças por família sem sinalização de volatilidade | P1 | JÁ RESOLVIDO | Seção 15.3.1 foi reescrita na Onda 2: sem tabela de associações família/força; Camada Viva aponta para Apêndice Vivo. |
| A03 — xAI caracterizada por "tolerância maior a temas sensíveis" | P1 | OBSOLETO PÓS-ONDA2 | xAI não aparece mais no corpo do capítulo. Capítulo removeu menções a players secundários. |
| A04 — Lista de chips específicos em 15.6 sem padrão durável | P1 | JÁ RESOLVIDO | 15.6 agora expressa a tendência durável e delega exemplos ao Apêndice Vivo: "Os chips e provedores relevantes mudam a cada ciclo de hardware — consulte o Apêndice Vivo para o mapeamento corrente." |

**Resumo C15:** 0 editados / 2 já resolvidos / 1 obsoleto / 0 deferidos

---

## C16 — L1-C16-open-source.md

| Achado | Categoria | Status | Ação |
|--------|-----------|--------|------|
| A02 — Preços específicos de API no Quadro 16.A envelhecem | P1 | JÁ RESOLVIDO | Quadro 16.A foi completamente reescrito na Onda 2: sem valores nominais, componentes estruturais com lógica de TCO e remissão ao Apêndice Vivo para valores correntes. |
| A03 — Números de versão de modelos no corpo do texto | P1 | JÁ RESOLVIDO | Seção 16.3.1 reescrita: ensina critérios de avaliação (licença, origem, qualidade por eixo, integração, variantes de tamanho); lista corrente de famílias delegada ao Apêndice Vivo. |
| A04 — Nota Técnica ANPD citada como documento estabelecido | P1 | JÁ RESOLVIDO | Todas as menções agora qualificadas com "(segundo o divulgado, com versão corrente a verificar em www.gov.br/anpd conforme Apêndice J — Trilha do Número)" ou formulação equivalente. |

**Resumo C16:** 0 editados / 3 já resolvidos / 0 obsoletos / 0 deferidos

---

## C17 — L1-C17-github-repos.md

| Achado | Categoria | Status | Ação |
|--------|-----------|--------|------|
| A01 — Referência de imagem usa "cap-35" no lugar de "cap-17" | P1 | EDITADO | Corrigido: `imagens/cap-35-img-01-repos-categoria.svg` → `imagens/cap-17-img-01-repos-categoria.svg` (linha 28). |
| A02 — OpenInterpreter com "governança em pessoa física com empresa em formação" | P1 | OBSOLETO PÓS-ONDA2 | Seção 17.6 foi completamente reescrita: sem inventário específico de repositórios; "Camada viva" aponta para `repos-curados` no repositório de recursos da obra. |
| A03 — Regra de CI não exige CI presente como condição | P1 | EDITADO | Seção 17.3.3 reformulada: ausência de CI é red flag imediata explicitada antes da condição de CI vermelho; critério de aprovação agora exige CI presente E com histórico verde. |

**Resumo C17:** 2 editados / 0 já resolvidos / 1 obsoleto / 0 deferidos

---

## C18 — L1-C18-economia-tokens.md

| Achado | Categoria | Status | Ação |
|--------|-----------|--------|------|
| A02 — Capítulo sem analogia de abertura para Joana | P1 | EDITADO | Adicionada seção 18.1b com analogia da conta de energia corporativa: preço do kWh = preço por token (termo trivial); equipamentos ligados × horas = chamadas, redundância e tier (multiplicadores compostos). Inserida entre 18.1 e 18.2. |
| A03 — Autoavaliação item 5 é copypaste de capítulo de segurança | P1 | EDITADO | Item 5 substituído: "Curiosidade para segurança em escala corporativa" → "**Curiosidade** — Está motivado a instrumentar tokens por feature na próxima semana para ter baseline real e iniciar o programa de otimização com diagnóstico honesto?" |
| A04 — Framework F7 referenciado sem definição | P1 | JÁ RESOLVIDO | Primeira menção de F7 em 18.1 já inclui definição: "F7 — Custo Composto em Três Tempos, onde as três alavancas viram plano operável com metas, riscos e ordem de execução." |
| A05 — Aviso metodológico de 18.1 ignorado por leitor em diagonal | P1 | DEFERIDO | Aviso em 18.1 permanece em posição atual (contextualiza os dados do capítulo como um todo); a tabela 18.7 já tem bloco ⚠️ próprio sobre não-aditividade dos percentuais (resolvido na Onda 2). Mover o aviso de 18.1 sem reescrever o parágrafo introdutório criaria inconsistência estrutural — diferido para revisão de desenvolvimento. |

**Resumo C18:** 2 editados / 1 já resolvido / 0 obsoletos / 1 deferido

---

## C19 — L1-C19-seguranca.md

| Achado | Categoria | Status | Ação |
|--------|-----------|--------|------|
| A01 — CVE-2025-32711 sem definição de CVE para leitor não-técnico | P1 | EDITADO | Adicionada definição inline na primeira menção (19.3.1): "(CVE-2025-32711 — CVE é o identificador padronizado de vulnerabilidades de segurança publicamente registradas; CVE-2025-32711 é o registro oficial do ataque EchoLeak)". |
| A02 — Seção 19.3 sem mini-mapa de navegação | P1 | EDITADO | Adicionado bloco de mapa no início de 19.3: "Mapa de 19.3: Seis classes de ataque tratadas em sequência — (1) prompt injection, (2) jailbreak, (3) data poisoning, (4) model inversion, (5) PII leakage, (6) tool exploitation. Leia as seções relevantes para o seu contexto. O Quadro 19.A no final organiza a defesa e o aprofundamento para cada uma." |
| A03 — Checklist 14 itens mistura executivo e técnico sem distinção | P1 | EDITADO | Checklist dividido em dois blocos: "Checklist executivo — para CTO e liderança" (6 itens) e "Checklist técnico — para Head de Segurança e AI Engineer" (8 itens). |
| A04 — Nota Técnica ANPD em 19.7 citada sem verificação | P1 | JÁ RESOLVIDO | Seção 19.7 já usa linguagem cautelosa: "se confirmada na versão corrente (verificar título exato e vigência em www.gov.br/anpd conforme Apêndice J — Trilha do Número)". Checklist item 12 também reformulado conforme o padrão. |

**Resumo C19:** 3 editados / 1 já resolvido / 0 obsoletos / 0 deferidos

---

## CONSOLIDADO ONDA 3 — C15 a C19

| Capítulo | Editados | Já Resolvidos | Obsoletos | Deferidos |
|----------|----------|---------------|-----------|-----------|
| C15 | 0 | 2 | 1 | 0 |
| C16 | 0 | 3 | 0 | 0 |
| C17 | 2 | 0 | 1 | 0 |
| C18 | 2 | 1 | 0 | 1 |
| C19 | 3 | 1 | 0 | 0 |
| **TOTAL** | **7** | **7** | **2** | **1** |

**Nota sobre Onda 2:** C15, C16 e C17 foram fortemente reescritos na Onda 2 (perecível → método+ponteiro). A maioria dos P1 de C15 e C16 já estava resolvida pela reescrita. C17 tinha dois P1 remanescentes; ambos editados nesta Onda. C18 e C19 foram os capítulos que demandaram mais edições de clareza/retenção nesta Onda.

---

# CHANGELOG ONDA 3 — CLAREZA / RETENÇÃO / TESTE DA JOANA
## Capítulos 20 a 25
## Data: 2026-06-16

---

## C20 — L1-C20-futuro.md

### ACHADO 04 — P1 — [EDITADO]
Problema: Quatro vetores sem critério de medição operacional.
Ação: Adicionados 2-3 indicadores observáveis por vetor (capacidade, autonomia, custo, regulação) diretamente na seção 20.3.1, após cada descrição de vetor. Instrumenta o rito trimestral do AI Council sem depender de frameworks externos.

### ACHADO 05 — P1 — [EDITADO]
Problema: PL 2338 tratado como sancionado nos cenários otimista e mediano (estava em tramitação).
Ação: Reformulado condicionalmente nos dois cenários. Otimista agora: "marco regulatório de IA amadurece — se o PL 2338 for sancionado [...]; se a tramitação atrasar, o cenário otimista ainda é possível com regulação setorial consolidada". Mediano agora: "marco regulatório avança — o PL 2338, se sancionado [...]; mesmo que a sanção atrase, a ANPD passa a aplicar penalidades com base na LGPD". Tabela 20.9 mantida como estava (já continha "EU AI Act em fiscalização; PL 2338 sancionado" no mediano — a formulação da tabela ficará para revisão na Onda 4, pois é sumário e a ressalva no corpo já cobre o risco de durabilidade).

### ACHADO 06 — P1 — [EDITADO]
Problema: Horizonte de 12 meses delegado ao planejamento anual sem orientação de como aplicar o método.
Ação: Adicionada orientação mínima diretamente ao final da seção 20.3.2: quais vetores são mais observáveis em 12 meses (capacidade e custo), como tratar os ruidosos (autonomia e regulação), qual o entregável do ciclo e a cadência recomendada (revisão trimestral com AI Council, ajuste orçamentário semestral).

---

## C21 — L1-C21-evals.md

### ACHADO 01 — P1 — [EDITADO]
Problema: Correlação alvo 0,7 para LLM-as-judge sem referência.
Ação: Adicionada referência a Zheng et al. 2023 na seção 21.3.5, com nota de que o limiar varia por domínio (saúde e jurídico podem exigir 0,8 ou mais) e que se trata de limiar operacional pragmático, não universal.

### ACHADO 02 — P1 — [EDITADO]
Problema: Capítulo sem numeração de seções — inconsistência com o resto da obra.
Ação: Seções numeradas no padrão 21.1, 21.2, 21.3.x (até 21.3.9), 21.4 até 21.13. Todas as seções principais e subsseções da explicação técnica receberam numeração explícita.

### ACHADO 03 — P1 — [EDITADO]
Problema: Princípio 7 e Princípio 8 mencionados sem definição local.
Ação:
- Princípio 7: definido na primeira menção no exemplo da Atlas Strategy (seção 21.4): "Princípio 7 — o Termômetro: o sistema de IA precisa de instrumentação para ser gerenciável; sem ela, opera como caixa-preta e o incidente aparece pelo cliente, não pelo dashboard."
- Princípio 8: definido na pergunta de revisão 7 (seção 21.9): "Responsabilidade Indelegável — a responsabilidade por decisão de IA nunca pode ser delegada à máquina; há sempre um nome humano na cadeira de quem responde."

---

## C22 — L1-C22-llmops.md

### ACHADO 01 — P1 — [EDITADO]
Problema: Pilar 6 (Segurança Operacional) desproporcional em extensão para o risco que representa.
Ação: Pilar 6 expandido com: (1) parágrafo de abertura que contextualiza o risco em agentes com MCP; (2) exemplo concreto de prompt injection em agente jurídico consumindo petição adversária via MCP; (3) tabela de defesas por vetor (prompt injection via usuário, via documento externo, tool poisoning, data exfiltration) com defesa primária e condição de suficiência.

### ACHADO 02 — P1 — [EDITADO]
Problema: Custo composto em três tempos referenciado sem fórmula local no Pilar 5.
Ação: Fórmula adicionada diretamente no Pilar 5: "custo composto = tokens × chamadas × redundância × tier do modelo". Explicação dos quatro fatores e remissão ao Cap 18 para detalhe. Elimina a dependência do leitor de ter o Cap 18 em mente.

### ACHADO 03 — P1 — [EDITADO]
Problema: Regra de canário por segmento sem ressalva para contratos enterprise com SLA.
Ação: Adicionada ressalva diretamente após a regra "quem reclamaria mais alto recebe por último": "em contratos enterprise com SLA explícito de rollout, verifique as cláusulas contratuais antes de aplicar essa sequência; em alguns casos, rollout simultâneo com monitoramento dedicado por cliente é preferível."

### ACHADO 04 — P1 — [EDITADO]
Problema: MTTR de 15 min para SEV-1 sem referência ou ressalva de maturidade.
Ação: Adicionada referência (Google SRE e métricas DORA) e meta progressiva para times iniciantes: 4 horas para SEV-1 como alvo de 90 dias, migrando para 15 minutos conforme tracing e rollback amadurecem. Evita que time implante OKR inalcançável sem contexto.

---

## C23 — L1-C23-alignment.md

### ACHADO 02 — P1 — [EDITADO]
Problema: Redundância entre seção 23.2 (analogia) e 23.3 (técnica) no mapeamento das três camadas.
Ação: Seção 23.2 condensada de três parágrafos com "três lições explícitas" para dois parágrafos diretos. Mapeamento instrução base / feedback / constituição mantido (é o gancho de compreensão), "três lições" explícitas removidas (emergem da leitura da seção 23.3). Redução de aproximadamente 60% no volume da seção.

### ACHADO 03 — P1 — [EDITADO]
Problema: Seção 23.4 descrevia relação entre capítulos sem entregar instrumentação nova.
Ação: Seção 23.4 transformada em "Protocolo de escalação — quando alignment falha em produção", com cinco passos numerados: (1) Detecção via tracing, (2) Classificação de severidade (SEV-1 a SEV-3 por tipo de falha), (3) Contenção via guardrails externos, (4) Investigação de causa raiz (constituição, dataset, red team, drift), (5) Remediação e registro no Caderno de Governança. As conexões com os caps 21, 22 e 24 ficam subordinadas ao protocolo, não como parágrafo ornamental.

### ACHADO 04 — P1 — [EDITADO]
Problema: Exercício 4 pressupõe quórum executivo indisponível em empresa pequena.
Ação: Adicionada variante do exercício 4 para profissional individual ou empresa pequena, com instrução de simular os três papéis (CTO/PO/compliance) individualmente usando as quatro perguntas da seção 23.3.1 como roteiro solo. Mesmo entregável — escolha documentada com justificativa — revisável por par sênior.

---

## C24 — L1-C24-governanca.md

### ACHADO 02 — P1 — [EDITADO]
Problema: Integração de ética no AI Council de empresa pequena não instrumentada.
Ação: Adicionada orientação prática diretamente na seção 24.3.1 após a descrição de empresa pequena: dois mecanismos para integrar ética sem overhead de comitê separado — (1) pauta fixa de casos limítrofes a cada reunião com critério pré-acordado do que constitui caso limítrofe; (2) consultor externo de ética em sessão semestral como observador com direito de voz. Adicionado alerta explícito: empresa pequena em domínio sensível não pode adiar ética para quando "crescer".

### ACHADO 03 — P1 — [EDITADO]
Problema: Comunicação externa pré-escrita mencionada como componente mínimo sem template.
Ação: Adicionado template de comunicação para SEV-1 diretamente no bullet da seção 24.3.4: "Identificamos um incidente em nosso sistema de IA que pode ter afetado clientes entre [data início] e [data fim]. Estamos investigando a causa e entramos em contato com os clientes afetados em até [prazo]. Para dúvidas: [canal]." Com instrução de preencher o template na política, não no momento do incidente.

### ACHADO 04 — P1 — [EDITADO]
Problema: Princípio 8 mencionado cinco vezes sem definição local.
Ação: Definição adicionada no início da seção "RACI de IA: o coração do Princípio 8" — parágrafo introdutório antes do RACI: "O Princípio 8 da obra é a Responsabilidade Indelegável: a responsabilidade por decisão de IA nunca pode ser delegada à máquina. Há sempre um nome humano na cadeira de quem responde [...]. Quando a cadeira está vazia, o incidente vira crise sem interlocutor."

---

## C25 — L1-C25-trade-offs.md

### ACHADO 01 — P1 — [DEFERIDO]
Problema: Diagramas 25.2 (árvore de decisão) e 25.3 (triângulo T4) sem arquivo SVG referenciado.
Razão do diferimento: produção de asset gráfico (SVG) está fora do escopo de edição de texto da Onda 3. Os blocos de descrição no texto já indicam o conteúdo esperado. Ação pendente para equipe de design: criar L1-C43-img-02-arvore-decisao-trade-offs.svg e L1-C43-img-03-triangulo-latencia-qualidade-custo.svg conforme descrição nos blocos do capítulo.

### ACHADO 02 — P1 — [EDITADO]
Problema: Capítulo se autoproclama "cardápio consultável" mas não tem tabela-resumo no início.
Ação: Adicionada seção 25.1A "Cardápio Rápido" logo antes da analogia (25.2), com tabela dos seis trade-offs em formato scannable: trade-off | pergunta executiva | eixo decisor. Inclui também a sequência de decisão sugerida (T4→T1→T5→T2→T6→T3). A tabela completa em 25.9 foi mantida como referência expandida.

### ACHADO 03 — P1 — [EDITADO]
Problema: T3 omite vendor lock-in como eixo de decisão.
Ação: Tabela do T3 expandida com coluna sobre lock-in (linha de "quando é desperdício" em modelo fechado atualizada para incluir "horizonte longo sem cláusula de migração"). Adicionado parágrafo dedicado ao quinto eixo — risco de lock-in — explicando os quatro vetores de dependência (formato de API, política de preço, descontinuação, dados de treinamento) e a pergunta operacional de teste: "se este vendor triplicar o preço ou descontinuar este modelo, qual é o plano de migração e qual o custo?" Eixo decisor do T3 atualizado para incluir "× lock-in" em ambas as ocorrências (tabela sumário e seção detalhada).

### ACHADO 04 — P1 — [EDITADO]
Problema: Referência a Brooks (Mythical Man-Month) como "fundamentos do triângulo" imprecisa.
Ação: Texto do T4 corrigido para: "O triângulo é princípio clássico de engenharia de sistemas: otimizar duas dimensões simultaneamente custa sempre na terceira. O princípio aparece em diversas formas na engenharia (triângulo CAP de Brewer em sistemas distribuídos, triângulo de qualidade em ISO 25010, triângulo de projeto escopo/tempo/custo em engenharia de software). Aplicado a IA, as três dimensões são latência, qualidade e custo." Referências atualizadas para incluir Brewer (CAP theorem) como referência primária de triângulo em sistemas; Brooks mantido com nota explícita de que é analogia, não referência direta.

---

## RESUMO CONSOLIDADO

| Capítulo | P1 Editados | P1 Já Resolvidos | P1 Deferidos |
|----------|-------------|------------------|--------------|
| C20 | 3 (04, 05, 06) | 0 | 0 |
| C21 | 3 (01, 02, 03) | 0 | 0 |
| C22 | 4 (01, 02, 03, 04) | 0 | 0 |
| C23 | 3 (02, 03, 04) | 0 | 0 |
| C24 | 3 (02, 03, 04) | 0 | 0 |
| C25 | 3 (02, 03, 04) | 0 | 1 (01 — produção de SVG) |
| **TOTAL** | **19** | **0** | **1** |

Nota: os P0 de cada capítulo (C20-01, C20-02, C20-03; C23-01; C24-01) já haviam sido corrigidos em Ondas anteriores ou são de natureza diferente (P0 de C20 foram tratados no texto da Onda 1/2 conforme confirmado na leitura — os números foram suavizados e o parágrafo AGI já estava na forma das três afirmações curtas). O P0 de C23 (GRPO papéis distintos) foi verificado: o texto atual já contém a separação correta ("DeepSeekMath (Shao et al., 2024, arXiv:2402.03300) — introduz GRPO; aprofundado em DeepSeek-R1 (DeepSeek-AI, 2025, arXiv:2501.12948)") — JÁ RESOLVIDO em onda anterior. O P0 de C24 (SVGs 24.2 e 24.3) está marcado como pendente no próprio arquivo com comentários HTML — DEFERIDO (produção de arte).

---

# Changelog Onda 3 — Capítulos 26, 27 e 28
*Inteligência Aumentada — Livro 1: Os Invariantes*
*Data: 2026-06-16*
*Natureza da onda: Clareza, retenção, Teste da Joana — apenas P1*

---

## C26 — L1-C26-roadmap-pessoal.md

### A01 — Persona Criador: marcos desviados da tese central [EDITADO]
**Problema:** Marcos 90 dias (biblioteca de prompts), 180 dias (comunidade de 100 membros) e 365 dias (convites a eventos) eram sobre crescimento de audiência e plataforma pessoal, não sobre método de ensino — antítese de "Método fica".
**Correção aplicada:**
- Marco 90 dias: substituído "workshop + biblioteca de prompts" por "workshop + framework de avaliação de aprendizado baseado nos Invariantes com rúbrica publicada".
- Marco 180 dias: substituído "comunidade de 100+ membros" por "framework de design instrucional aplicado em dois ciclos, com evidência de aprendizado medida e documentada".
- Resumo executivo (tabela): atualizada linha Criador para refletir novos entregáveis.
**Lógica editorial:** A persona Criador sobrevive e ganha coerência com a tese central; o foco migra de crescimento de audiência para desenvolvimento de método de ensino verificável.

### A02 — Referência de asset com numeração errada [JÁ RESOLVIDO]
**Verificação:** O arquivo já referencia `L1-C26-img-01-curva-adocao.svg` — correção já aplicada em Onda anterior. Nenhuma ação necessária.

### A03 — Persona Dev, Marco 365 dias: "repositório de prompts" viola tese central [EDITADO]
**Problema:** "Contribuição a repositório de prompts" como entregável verificável e gate de promoção cria coleção de artefatos datados — antítese de "Modelos passam. Método fica."
**Correção aplicada:**
- Objetivo: "repositório de prompts" substituído por "repositório de casos de uso com framework de eval documentado".
- Entregável verificável: substituído por "cinco casos de uso com framework de eval aplicado por caso (o que sobrevive é a estrutura de avaliação, não o prompt específico)".
- Gate de promoção: ajustado para citação em revisões técnicas de features, não uso de prompts em produção.
- Resumo executivo (tabela): linha Desenvolvedor atualizada.

### A04 — Dependência circular com Apêndice C [JÁ RESOLVIDO]
**Verificação:** A seção 26.1 já contém parágrafo completo explicando a diferença entre o Apêndice C ("referência sintética") e este capítulo ("instrumento de aplicação calibrada") — incluindo os três pontos de diferenciação (horas reais, prerrequisitos explícitos, critério de abandono). A Joana consegue distinguir os dois sem ler o apêndice. Nenhuma ação necessária.

### A05 — Sobreposição checklist / perguntas / exercícios [DEFERIDO — P2]
Fora do escopo de Onda 3 (P2). Reorganização editorial a tratar em Onda futura.

### A06 — Personas não cobrem CFO, CHRO, advogado interno [DEFERIDO — P2]
Fora do escopo de Onda 3 (P2).

### A07 — Epígrafe longa demais [EDITADO]
**Problema:** Dois períodos com 60+ palavras cada — não citável, não memorável, desgasta antes da abertura.
**Correção aplicada:** Encurtada para o segundo período apenas (que contém a essência do método). Primeiro período removido.
**Resultado:** Epígrafe de 23 palavras, citável e direta.

---

## C27 — L1-C27-ia-para-pme-brasileira.md

### A01 — Valores monetários datados (R$ 1.400/mês, R$ 800/hora) [EDITADO]
**Problema:** Valores pontuais no exemplo de Joinville envelhecem em 12-18 meses, minando credibilidade da matriz TCO.
**Correção aplicada:**
- R$ 1.400/mês: mantido como valor histórico do cenário composto, com nota explícita "verifique preço corrente no site do fornecedor antes de orçar, pois preços de assinatura corporativa de IA mudam com frequência".
- R$ 800/hora: mantido como valor do cenário, com nota "o valor de mercado varia por região e especialização; peça orçamento atualizado antes de contratar".
- Nota: a matriz TCO de 27.3.2 já usa ranges, não valores pontuais — nenhuma correção necessária ali.

### A02 — Regra dos 3% sem base empírica declarada [JÁ RESOLVIDO]
**Verificação:** A seção 27.3.6 já contém explicitamente: "Esta regra não é derivada de estudo estatístico rigoroso — é heurística conservadora baseada em observação de casos de adoção em PME entre 2024 e 2026, calibrada para que o investimento caiba no orçamento de tecnologia sem comprometer a operação corrente. Trate-a como piso de prudência, não como prescrição científica." — correção já aplicada em Onda anterior. Nenhuma ação necessária.

### A03 — Tier 2 não distingue IA generativa de automação tradicional [EDITADO]
**Problema:** Dono de PME poderia confundir RPA/low-code com "workflow assistido de IA", aplicando TCO e prazo de 90 dias errados.
**Correção aplicada:** Adicionado parágrafo de abertura em 27.3.3, antes da divisão dos tiers, com distinção direta: automação de regra fixa (Zapier, Power Automate, RPA) executa instruções determinísticas; workflow assistido por IA generativa executa julgamento em linguagem natural com revisão humana em ponto de controle. Nota explícita: "Os tiers deste capítulo tratam de IA generativa, não de automação de regra fixa; a aritmética de TCO e o prazo de noventa dias não se aplicam a projetos de RPA."

### A04 — Roadmap de 12 meses aparece tarde — leitor abandona antes [EDITADO]
**Problema:** Dono de PME com 3 horas semanais atravessa 3 seções densas de TCO antes de encontrar o entregável principal.
**Correção aplicada:** Adicionado bloco "Como usar este capítulo" imediatamente antes de 27.1, com rota de leitura rápida (27.2 → 27.3.3 → 27.3.6 → 27.4) e instrução explícita de quando ler as demais seções (antes de assinar contrato, ao iniciar Fase 2).

### A05 — Inconsistência de formato de boxes CTA [DEFERIDO — P2]
Fora do escopo de Onda 3 (P2). Padronização de estilo a tratar em copidesque final.

### A06 — PL 2338/2023 como "em tramitação" [JÁ RESOLVIDO]
**Verificação:** A seção 27.12 (Referências principais) já usa: "Marco Legal da IA no Brasil (PL 2338/2023 ou legislação resultante — status em tramitação na data de fechamento desta edição; verifique situação atual em fonte oficial antes de citar em contexto regulatório, conforme Apêndice J — Trilha do Número)". Nenhuma ação necessária.

### A07 — ROI de Joinville não desconta custo de oportunidade do tempo de gestão [EDITADO]
**Problema:** CFO ou sócio adversarial questiona ROI ao incluir horas do dono, da filha e do gerente administrativo no denominador — e a empresa não tinha resposta.
**Correção aplicada:** Expandido o parágrafo de ROI com três ressalvas explícitas: (1) tempo economizado que virou capacidade vs. redução de quadro; (2) custo de oportunidade do tempo de gestão não está incluído no denominador — com nota de que o ROI líquido seria menor mas ainda positivo; (3) baseline estimado, não medido com instrumento formal, com instrução de como replicar o caso com medição correta.

---

## C28 — L1-C28-interpretabilidade-mecanicista.md

### A01 — Seção 28.3.3 perde leitor não-técnico com Johnson-Lindenstrauss [EDITADO]
**Problema:** Explicação de lema de Johnson-Lindenstrauss exige intuição geométrica em espaço de alta dimensão — a Joana e CTOs sem formação matemática se perdem, saltam a seção e perdem a intuição de superposição.
**Correção aplicada:** Adicionado bloco "Intuição para não-matemáticos" (blockquote destacado) imediatamente antes da explicação técnica: analogia das gavetas — rede tem mil gavetas mas precisa guardar dez mil conceitos, dobra vários em cada gaveta de formas que raramente se confundem, e o lema é apenas a prova de que a dobradinha funciona. Implicação operacional explícita: neurônios são polissemânticos por construção, SAE é o instrumento de desentrelaçamento.

### A02 — Referência de asset com numeração errada (L1-C46-img-01) [JÁ RESOLVIDO]
**Verificação:** O arquivo já referencia `L1-C28-img-01-stack-interpretabilidade.svg` — correção já aplicada em Onda anterior. Nenhuma ação necessária.

### A03 — Golden Gate Claude descrito duas vezes com conteúdo sobreposto [EDITADO]
**Problema:** Seções 28.3.2 e 28.3.6 descreviam o mesmo exemplo com variação menor — redundância que parece descuido editorial e perde o leitor no segundo encontro.
**Correção aplicada:** Segunda ocorrência (28.3.6) substituída por referência cruzada direta a 28.3.2, com extração da lição operacional específica do contexto (aplicações práticas) e adição do ponto sobre URL do material original com instrução de verificação via Apêndice J.

### A04 — URL transformer-circuits.pub como link frágil [DEFERIDO — P2]
A segunda ocorrência da URL em 28.3.6 foi atualizada como parte da correção A03. A ocorrência em 28.13 (autoavaliação) e em 28.10 (exercício 4) permanece — tratamento sistemático de URLs frágeis a aplicar em revisão de copidesque (P2).

### A05 — Seção DeepMind (28.3.4): grokking sem aplicação operacional [EDITADO]
**Problema:** O parágrafo sobre grokking dizia que o fenômeno "importa para o CTO" mas não entregava a implicação prática — o CTO não sabia o que fazer com a informação.
**Correção aplicada:** Adicionadas 3 linhas de implicação operacional direta: modelo treinado por mais tempo pode ter mudado de comportamento de forma qualitativa (não apenas quantitativa); golden set que cobria comportamento anterior pode não cobrir comportamento pós-grokking; sinal de alerta prático — regressões em casos antes resolvidos com facilidade, sem mudança de input.

### A06 — Exercício 4: leitura de NeurIPS/ICML inaplicável [DEFERIDO — P2]
Fora do escopo de Onda 3 (P2).

### A07 — Distinção interpretabilidade vs. chain-of-thought enterrada em 28.4 [EDITADO]
**Problema:** O argumento central do capítulo — que a cadeia de raciocínio pode ser racionalização post hoc e que a interpretabilidade audita o mecanismo real — estava enterrado na seção de conexões (28.4), não na abertura conceitual.
**Correção aplicada:** Adicionado parágrafo em 28.1 (Conceito intuitivo), imediatamente após a definição de interpretabilidade mecanicista, estabelecendo a distinção fundamental: chain-of-thought não é interpretabilidade; o relato do modelo pode não ser fiel ao mecanismo; a interpretabilidade audita o mecanismo, não o relato. Esta é a distinção que a maioria dos executivos não faz e que justifica o investimento.

---

## Sumário de decisões

| Capítulo | Total P1 banca | Editados | Já resolvidos | Deferidos (P2) |
|----------|---------------|----------|---------------|----------------|
| C26 | 4 P1 (A01, A03, A04, A07) | 3 (A01, A03, A07) | 1 (A04) | 0 |
| C27 | 4 P1 (A01, A03, A04, A07) | 3 (A01, A03, A04) | 2 (A02→P0 já ok, A06→P0 já ok) | 1 (A07 editado, A05 deferido) |
| C28 | 4 P1 (A01, A03, A05, A07) | 4 (A01, A03, A05, A07) | 1 (A02) | 1 (A04, A06) |

*Nota: A02 e A06 de C27 são P0 da banca (não P1) e já estavam resolvidos antes desta onda.*

---

# Changelog Onda 3 — APX-A a APX-I
## Livro: INTELIGÊNCIA AUMENTADA — Os Nove Princípios Permanentes
## Data: junho de 2026
## Escopo: P1 (clareza/retenção) — Onda 3

---

## APX-A — L1-APX-A-glossario.md

| Achado | Categoria | Status | Ação |
|--------|-----------|--------|------|
| A-01: Os Nove Frameworks comprimidos em uma entrada sem definição individual | P1 | **[EDITADO]** | Entrada agregada mantida como índice; 9 entradas individuais criadas com definição de 1–2 linhas e marcador ★ para cada framework |
| A-02: Ausência de entrada para "Reasoning models" | P1 | **[EDITADO]** | Entrada ◆ adicionada ao final da Cat. II com definição, exemplos (o1/o3, Claude extended thinking, DeepSeek-R1) e remissiva ao C14B |
| A-03: "PL de IA brasileiro" sem número do PL | P1 | **[EDITADO]** | Texto atualizado para "PL 2338/2023, em tramitação no Senado Federal" com descrição de escopo — consistente com APX-H |

---

## APX-B — L1-APX-B-mapa-mental.md

| Achado | Categoria | Status | Ação |
|--------|-----------|--------|------|
| B-01: Princípio 1 mapeado para "Auditoria de honestidade dentro da Pirâmide da Avaliação" — inconsistente com APX-A | P1 | **[EDITADO]** | Coluna Framework do P1 substituída por: "Pressuposto transversal da Pirâmide da Avaliação (P7) — opera como premissa dos demais frameworks, não tem framework dedicado próprio" |
| B-02: C14B e C14C ausentes da tabela Princípio × Framework | P1 | **[JÁ RESOLVIDO]** | C14B (linha 128) e C14C (linha 129) já presentes na tabela Capítulo × Princípio primário e secundário. Caso de uso "Estou em incidente" também já presente na tabela "Como usar este mapa" (linha 169). Sem edição necessária. |

---

## APX-C — L1-APX-C-roadmaps.md

| Achado | Categoria | Status | Ação |
|--------|-----------|--------|------|
| C-02: Ausência de persona para profissional individual sem mandato (IC) | P1 | **[EDITADO]** | Roadmap 7 — Profissional Individual (IC / Individual Contributor) criado com 4 marcos (30/90/180/365 dias), artefatos esperados, critérios de avanço e remissivas a APX-D, APX-E, APX-G |
| C-03: Roadmaps sem remissivas a outros apêndices | P1 | **[EDITADO]** | Nota introdutória expandida com bloco de recursos de aprofundamento por tipo de marco: APX-D (ferramentas), APX-G (papers), APX-E (dieta de informação) |
| C-04: Critério cultural não auditável no Marco 365 do Executivo | P1 | **[EDITADO]** | "Vocabulário dos Princípios incorporado em reuniões executivas" substituído por: "Em pelo menos duas decisões de IA documentadas no período, o princípio aplicado ou violado foi nominalmente identificado em ata ou documento de decisão" |

---

## APX-D — L1-APX-D-ferramentas.md

| Achado | Categoria | Status | Ação |
|--------|-----------|--------|------|
| D-02: Licença Llama descrita como fato fixo | P1 | **[OBSOLETO PÓS-ONDA2]** | APX-D foi reescrito na Onda 2: o catálogo detalhado de ferramentas (incluindo entradas de Llama) foi movido para o repositório externo. O arquivo atual é stub com método D.1. Sem entrada de Llama no arquivo. |
| D-03: Ausência de categoria para plataformas corporativas no-code/low-code | P1 | **[OBSOLETO PÓS-ONDA2]** | APX-D agora aponta para repositório. Categorias específicas de ferramentas vivem no repositório, não no apêndice. |
| D-04: Critério D.1 sem âncoras de calibração por dimensão | P1 | **[EDITADO]** | Tabela D.1 expandida com coluna "Âncoras de calibração (nota 1–10)" — duas âncoras por dimensão (10, 5, 1) para Maturidade, Adoção, Custo, Encaixe com stack brasileira, Suporte e Estabilidade |

---

## APX-E — L1-APX-E-leituras.md

| Achado | Categoria | Status | Ação |
|--------|-----------|--------|------|
| E-01: Co-Intelligence e Competing in the Age of AI ausentes | P1 | **[OBSOLETO PÓS-ONDA2]** | APX-E foi reescrito na Onda 2: virou documento de método de curadoria ("Como montar sua dieta de informação"). Listas específicas de livros foram movidas para o repositório externo. A subseção de listas de livros não existe mais no arquivo. |
| E-02: Seção de blogs/newsletters duplica APX-F sem remissiva | P1 | **[OBSOLETO PÓS-ONDA2]** | APX-E e APX-F foram fundidos na Onda 2. APX-F agora é stub de redirecionamento. APX-E seção 6 ("Onde estão as listas") já aponta para o repositório. Duplicação eliminada. |
| E-03: Cursos formais misturados com repositórios sem distinção de formato | P1 | **[OBSOLETO PÓS-ONDA2]** | Seção de cursos não existe mais no arquivo. Listas vivem no repositório. |

---

## APX-F — L1-APX-F-newsletters.md

| Achado | Categoria | Status | Ação |
|--------|-----------|--------|------|
| F-02: Grupo de Telegram sobre MCP sem nome, link ou critério de localização | P1 | **[OBSOLETO PÓS-ONDA2]** | APX-F virou stub de redirecionamento na Onda 2. Todo o conteúdo de listas foi movido para APX-E (método) e repositório (listas). Sem entrada de Telegram no arquivo. |
| F-03: Nomes de indivíduos como referência primária de projetos de podcast | P1 | **[OBSOLETO PÓS-ONDA2]** | Idem — conteúdo de podcasts movido para repositório. |
| F-04: Canal de contribuição sem URL ou mecanismo permanente especificado | P1 | **[OBSOLETO PÓS-ONDA2]** | APX-F não tem mais seção de contribuição. APX-E seção "Camada viva" aponta para repositório GitHub específico: github.com/falercia/inteligencia-aumentada-recursos. |

---

## APX-G — L1-APX-G-papers.md

| Achado | Categoria | Status | Ação |
|--------|-----------|--------|------|
| G-01: Building Effective Agents e AutoGPT misturados com papers revisados por pares | P1 | **[EDITADO]** | Subseção "Documentação técnica e guias de referência" criada dentro da Categoria V (Agentes) para separar os dois itens dos papers revisados por pares. Nota explicativa adicionada. Numeração da lista atualizada para refletir adições (29 Narayanan, 30–35 Agentes, 36–48 restantes). |
| G-02: Ausência de referência acadêmica para Context Engineering (C11) | P1 | **[EDITADO]** | Nota honesta adicionada ao final da Categoria II: "Context Engineering como disciplina sistemática não tem paper seminal consolidado em 2026" + referência a Khattab et al. DSPy (Stanford, 2023) como aproximação mais próxima + remissiva à documentação oficial em APX-H Seção IV. |
| H-01 (cruzado): Narayanan & Kapoor ausente do APX-G mas presente no APX-H | P1 | **[EDITADO]** | Entrada #29 adicionada na Categoria IV (Evals): "Narayanan, A. & Kapoor S. — *Evaluating LLMs is a minefield* (Princeton, 2023)" com nota de uso. |

---

## APX-H — L1-APX-H-bibliografia.md

| Achado | Categoria | Status | Ação |
|--------|-----------|--------|------|
| H-01: Narayanan & Kapoor ausente do APX-G | P1 | **[EDITADO]** | Resolvido em APX-G (ver acima). Entrada já presente no APX-H — sem alteração necessária aqui. |
| H-02: Schmidhuber com "(recente)" como data — referência não verificável | P1 | **[EDITADO]** | "(recente)" substituído por "(schmidhuber.ch, atualizado periodicamente)" — permite localização pelo leitor sem fixar data que pode estar errada. |
| H-03: Drucker, Brooks, Kotter sem contexto de uso na obra | P1 | **[EDITADO]** | Nota parentética adicionada a cada um: Drucker → fundamento de tomada de decisão sistemática, base do Princípio 9; Brooks → Lei de Brooks aplicada a sistemas de IA; Kotter → modelo de oito etapas, base dos marcos do APX-C. |

---

## APX-I — L1-APX-I-indice-remissivo.md

| Achado | Categoria | Status | Ação |
|--------|-----------|--------|------|
| I-01: Referências mortas a Apêndice K, L e M | P0 | **[JÁ RESOLVIDO]** | Arquivo atual não contém nenhuma referência a Apêndice K, L ou M. "Datasets de prática" aponta para "Apêndice D". Corrigido em Onda anterior. |
| I-02: Reasoning models e Spec-driven development ausentes do índice | P1 | **[JÁ RESOLVIDO]** | Linha 102: "Reasoning models ◆ — capítulo C14B (Reasoning models); Princípio 1" presente. Linha 119: "Spec-driven development — capítulo C14C; Princípios 4 e 8" presente. Corrigido em Onda anterior. |
| I-03: LLM-as-judge com duplo marcador ★ ◆ | P1 | **[EDITADO]** | ★ removido; entrada agora: "LLM-as-judge ◆ — capítulo sobre Evals; Pirâmide da Avaliação". Termo é do campo (Zheng et al., 2023), não proprietário da obra. |
| I-04: Letras N e U ausentes — NIST AI RMF e outros termos não indexados | P1 | **[EDITADO]** | Seção ## N adicionada com três entradas: NIST AI RMF (capítulos Governança e Segurança + APX-A Cat. IX + APX-H Seção III), Nove Frameworks ★ (APX-A + APX-B), Nove Princípios ★ (Introdução + APX-B). Letra U permanece ausente: termos candidatos ("UE AI Act") já estão indexados sob "AI Act" — sem entrada nova necessária. |

---

## Resumo consolidado por apêndice

| Apêndice | P1 Editados | P1 Já Resolvidos | P1 Obsoletos pós-Onda2 | P1 Deferidos |
|----------|-------------|------------------|------------------------|--------------|
| APX-A | 3 | 0 | 0 | 0 |
| APX-B | 1 | 1 | 0 | 0 |
| APX-C | 3 | 0 | 0 | 0 |
| APX-D | 1 | 0 | 2 | 0 |
| APX-E | 0 | 0 | 3 | 0 |
| APX-F | 0 | 0 | 3 | 0 |
| APX-G | 3 | 0 | 0 | 0 |
| APX-H | 2 | 1 | 0 | 0 |
| APX-I | 2 | 2 | 0 | 0 |
| **TOTAL** | **15** | **4** | **8** | **0** |

---

*Onda 3 — Foco: clareza, retenção, teste da Joana. Apenas P1. Gerado em junho de 2026.*

---

# Changelog Onda 3 — Apêndices J, K, M, N, O, Q
**Data:** junho de 2026
**Onda:** 3 — Clareza, Retenção, Teste da Joana
**Escopo:** apenas P1 (clareza/retenção)

---

## APX-J — Trilha do Número

| Achado | Categoria | Status | Descrição da intervenção |
|--------|-----------|--------|--------------------------|
| J/01 | P1 | [EDITADO] | Adicionada coluna "Data verificação" à tabela de modelos da Seção 1, com data individual por linha. DeepSeek marcado como 31/mai/2026; demais provedores como jun/2026. |
| J/03 | P1 | [EDITADO] | Entrada "Chinese state-actor automatizando ataque" reformulada: título generalizado, qualificador de incerteza declarado inline, nota de revisão/remoção na próxima atualização se fonte primária pública não for identificada. |
| J/04 | P1 | [EDITADO] | Adicionada nota editorial "Nota sobre fontes de benchmark" antes das lições estruturais da Seção 2, listando fontes primárias de cada benchmark e declarando a distinção entre leaderboard oficial e agregador de terceiros. |

**Resumo APX-J:** 3 editados / 0 já resolvidos / 0 deferidos

---

## APX-K — Gabaritos Comentados

| Achado | Categoria | Status | Descrição da intervenção |
|--------|-----------|--------|--------------------------|
| K/02 | P1 | [EDITADO] | Adicionada rubrica de proficiência (insuficiente / proficiente / excelente) a todos os projetos: Cartaz dos Princípios, Plano para a Diretoria, Plano de Economia, Caderno de RAG, Prompt Estendida, Caderno de Evals, Caderno de LLMOps, Caderno de Alignment, Caderno de Governança, Cardápio de Trade-offs, Apresentação à Diretoria. Critério de autoavaliação individual adicionado ao projeto Roadmap Pessoal. |
| K/03 | P1 | [EDITADO] | Referências de capítulo adicionadas a todos os títulos de seção: RAG → Capítulo 06, Evals → Capítulo 21, LLMOps → Capítulo 22, Alignment → Capítulo 23, Governança → Capítulo 24, Trade-offs → Capítulo 25, Roadmap pessoal → Capítulo 26, Como modelos funcionam → Capítulo 02, Tokens → Capítulo 03, Engenharia de prompt → Capítulo 09, Introdução → C00P + C01. |

**Resumo APX-K:** 2 editados / 0 já resolvidos / 0 deferidos

---

## APX-M — Manifesto de Bolso

| Achado | Categoria | Status | Descrição da intervenção |
|--------|-----------|--------|--------------------------|
| M/01 | P1 | [EDITADO] | Título alterado de "Apêndice M — Síntese: Os Nove Princípios em Uma Página" para "Apêndice M — Manifesto de Bolso: Os Nove Princípios em Uma Página", alinhando com referências externas do sumário e dos demais apêndices. |

**Resumo APX-M:** 1 editado / 0 já resolvidos / 0 deferidos

---

## APX-N — Metodológico, sobre os números deste livro

| Achado | Categoria | Status | Descrição da intervenção |
|--------|-----------|--------|--------------------------|
| N/01 | P1 | [EDITADO] | Texto da Seção 5 corrigido de "aproximadamente noventa afirmações" para "oitenta e sete afirmações quantitativas relevantes (18 Tipo A + 24 Tipo B + 31 Tipo C + 14 Tipo D)", alinhando com o somatório da tabela. |
| N/02 | P1 | [EDITADO] | URL completa do arquivo `auditoria-quantitativa-l1.md` adicionada à Seção 5, no padrão dos links do APX-J: github.com/falercia/inteligencia-aumentada-recursos/blob/main/auditoria-quantitativa-l1.md. |

**Resumo APX-N:** 2 editados / 0 já resolvidos / 0 deferidos

---

## APX-O — Caderno de Governança de IA

| Achado | Categoria | Status | Descrição da intervenção |
|--------|-----------|--------|--------------------------|
| O/02 | P1 | [EDITADO] | Frase de escopo corrigida de "entre cinquenta e cinco mil colaboradores" para "entre 50 e 5.000 colaboradores (cinquenta a cinco mil)", eliminando a ambiguidade de leitura como "55.000 colaboradores". |
| O/03 | P1 | [JÁ RESOLVIDO] | Os sete padrões de adaptação já possuem títulos curtos em negrito integrados ao início de cada item (ex.: `**Patrocinador executivo nomeado, não apenas o cargo.**`). Formato atende ao critério de scanabilidade em uso de reunião. Nenhuma edição necessária. |

**Resumo APX-O:** 1 editado / 1 já resolvido / 0 deferidos

---

## APX-Q — Manual do Professor

| Achado | Categoria | Status | Descrição da intervenção |
|--------|-----------|--------|--------------------------|
| Q/01 | P1 | [EDITADO] | Referência cruzada adicionada ao exercício da Aula 4 (Lost in the Middle) na Seção 8.1, apontando para APX-K seção RAG — Capítulo 06 e para `/teaching/exercises/aula-04.md` no repositório. Nota geral de referência cruzada adicionada ao início da Seção 8.1 conectando todos os exercícios do banco ao APX-K e ao repositório. |
| Q/02 | P1 | [EDITADO] | Variação "Medicina ou áreas da Saúde" (Seção 10) corrigida: removida promessa de "discussão sobre regulação da Anvisa e do CFM" como conteúdo da obra; substituída por declaração explícita de que a obra não cobre regulação setorial de saúde e que o professor deve indicar material externo (Anvisa, CFM) conforme o contexto da turma. |
| Q/03 | P1 | [EDITADO] | Seção 3 (Plano de 40 horas, pós-graduação) expandida com tabela de 20 aulas equivalente à da Seção 2, com capítulos cobertos, tema central e formato de aula por sessão. Adicionado parágrafo sobre o diferencial da pós-graduação (seminário de paper por estudante). |
| Q/04 | P1 | [EDITADO] | Inconsistência de RAG no plano de MBA resolvida: Sessão 3 do MBA atualizada para "C06, RAG (C07 opcional para turmas com background técnico)", alinhando com o plano de 60h e justificando explicitamente a omissão de C07 como escolha editorial para MBA. |

**Resumo APX-Q:** 4 editados / 0 já resolvidos / 0 deferidos

---

## Consolidado Onda 3 — P1 apenas

| Apêndice | Editados | Já Resolvidos | Deferidos | Total P1 |
|----------|----------|---------------|-----------|----------|
| APX-J | 3 | 0 | 0 | 3 |
| APX-K | 2 | 0 | 0 | 2 |
| APX-M | 1 | 0 | 0 | 1 |
| APX-N | 2 | 0 | 0 | 2 |
| APX-O | 1 | 1 | 0 | 2 |
| APX-Q | 4 | 0 | 0 | 4 |
| **TOTAL** | **13** | **1** | **0** | **14** |

---

*Changelog gerado automaticamente em junho de 2026. P0 e P2 não tratados nesta onda.*

---

# Changelog Onda 3 — APX-L e APX-P

Data: 2026-06-16
Editora: agente Claude (Onda 3 — Clareza, Retenção, Teste da Joana)
Escopo: somente P1; P0 e P2 fora do escopo desta onda

---

## APX-L — Biblioteca de Prompts Profissionais

### Achado 04 — P1 — OBSOLETO PÓS-ONDA2
"Apêndice não ensina a construir prompt novo — apenas a usar os 30."
Referia-se a uma seção a adicionar antes das 30 fichas. As fichas foram removidas do livro na Onda 2 (apenas moldura + índice permaneceram). Achado não se aplica à moldura atual.

### Achado 05 — P1 — [EDITADO]
"Promessa do repositório não-verificável e sem fallback declarado."
Arquivo: `04-apendices/L1-APX-L-biblioteca-prompts.md`
Intervenção: adicionado URL explícito do repositório na célula da tabela de orientação (coluna "Onde vive") e acrescentado parágrafo de política de manutenção com canal de fallback logo após a tabela.
Trecho inserido: "Política de manutenção do repositório: os trinta prompts estão populados e são auditados a cada release do livro. Se o link não funcionar ou o prompt específico não for encontrado, o canal de fallback é o e-mail declarado na página de créditos do livro."

### Achado 06 — P1 — OBSOLETO PÓS-ONDA2
"Quando usar/evitar repete o óbvio em excesso."
Problema era interno às fichas individuais (campo "Quando usar / Quando evitar"). As fichas não existem mais no livro; apenas o índice permanece. Achado não se aplica.

### Achado 07 — P1 — OBSOLETO PÓS-ONDA2
"P-MED-03 sem aviso de restrição regulatória B2C (CFF)."
Ficha específica não está no livro (foi para o repositório). Achado não se aplica.

### Achado 08 — P1 — OBSOLETO PÓS-ONDA2
"P-FIN-02 sem menção à explicabilidade BACEN/LGPD art. 20."
Ficha específica não está no livro. Achado não se aplica.

### Achado 09 — P1 — OBSOLETO PÓS-ONDA2
"Changelog editorial no final — conteúdo mais valioso enterrado."
Não existe changelog editorial no arquivo atual. A moldura pós-Onda 2 não contém changelog de prompts individuais. Achado não se aplica.

### Achado 10 — P1 — [EDITADO]
"Nenhuma ficha menciona comportamento quando modelo recusa por política."
O achado sugeria adicionar um 8º padrão de operação. A seção "Padrões de operação" existe na moldura atual com 7 padrões. Intervenção aplicada diretamente ali.
Arquivo: `04-apendices/L1-APX-L-biblioteca-prompts.md`
Adicionado padrão 8: "Monitore recusas do modelo por categoria de input. [...] Taxa de recusa acima de 5% numa categoria específica é sinal de alarme que exige revisão da constituição ou do contexto."

### Achado 11 — P1 — OBSOLETO PÓS-ONDA2
"P-RH-01 sem menção à auditoria de viés algorítmico."
Ficha específica não está no livro. Achado não se aplica.

### Resumo APX-L
- Editados: 2 (Achados 05, 10)
- Obsoletos pós-Onda 2: 5 (Achados 04, 06, 07, 08, 09, 11) — 6 no total, contando 11
- Já resolvidos: 0
- Deferidos: 0

---

## APX-P — Boxes Técnicos

### Achado 03 — P1 — [EDITADO]
"Box 11 Interação 3: FlashAttention e platô de scaling laws conectados como causa-efeito quando são independentes."
Arquivo: `04-apendices/L1-APX-P-boxes-tecnicos.md`
Intervenção: reescrita completa da Interação 3 (FlashAttention × Scaling Laws). O texto anterior implicava que FlashAttention "amplifica" scaling laws e que o platô decorre dessa relação. Novo texto separa explicitamente as duas alavancas — FlashAttention como alavanca de custo de inferência em contexto longo, platô de scaling como consequência de esgotamento de dados humanos de qualidade e retorno decrescente de parâmetros. Instrução direta ao decisor: otimizar as duas de forma independente.

### Achado 04 — P1 — [EDITADO]
"Box 1: tiebreak leakage citado sem diferenciação de risco on-prem vs. API gerenciada."
Arquivo: `04-apendices/L1-APX-P-boxes-tecnicos.md`
Intervenção: adicionado parágrafo após a descrição dos riscos de tiebreak leakage e expert silencing, distinguindo explicitamente o regime de APIs gerenciadas (responsabilidade do provedor, mas confirmar por escrito) do regime de deploy on-prem com open weights (responsabilidade inteiramente do operador). Reformulada a pergunta estratégica: "quem é responsável pelo isolamento de batch e quais garantias posso exigir por escrito?"

### Achado 05 — P1 — [EDITADO]
"Box 11 usa emojis coloridos como única codificação — ilegível em impressão monocromática."
Arquivo: `04-apendices/L1-APX-P-boxes-tecnicos.md`
Intervenção: adicionado código textual duplo em toda a legenda e em todas as células da matriz (C/S/T/N como codificação primária, emoji como complemento visual). Todas as referências a pares na narrativa do parágrafo abaixo da tabela também atualizadas para usar os códigos textuais. A tabela agora é legível em formato impresso monocromático sem perda de informação.
Nota: a célula Quantização × Mech Interp foi corrigida de T para C (conflito), consistente com o que o texto da Interação 7 descreve como "diretamente conflituosa".

### Achado 06 — P1 — [EDITADO]
"Box 8: referência 'trabalho de seguimento CoT 2024-2025' sem paper específico."
Arquivo: `04-apendices/L1-APX-P-boxes-tecnicos.md`
Intervenção: substituída a referência vaga por orientação de busca ativa com venue/conferência específicos (ACL 2024-2025, EMNLP 2024-2025) e termo de busca em arxiv.org ("causal faithfulness chain-of-thought"). Mantém o espírito de indicar onde aprofundar sem citar paper que pode não existir ou estar ultrapassado.

### Achado 07 — P1 — [EDITADO]
"Box 5: S-LoRA mencionado sem referência primária."
Arquivo: `04-apendices/L1-APX-P-boxes-tecnicos.md`
Intervenção: adicionada referência primária na seção "Onde aprofundar" do Box 5: Sheng et al. "S-LoRA: Serving Thousands of Concurrent LoRA Adapters", 2023, arxiv.org/abs/2311.03285. Padrão de citação agora consistente com os demais boxes.

### Resumo APX-P
- Editados: 5 (Achados 03, 04, 05, 06, 07)
- Obsoletos pós-Onda 2: 0
- Já resolvidos: 0
- Deferidos: 0

---

## Totais consolidados

| Apêndice | Editados | Já resolvidos | Obsoletos pós-Onda 2 | Deferidos |
|---|---|---|---|---|
| APX-L | 2 | 0 | 6 | 0 |
| APX-P | 5 | 0 | 0 | 0 |
| **Total** | **7** | **0** | **6** | **0** |

Total de P1s analisados: 13 (8 APX-L + 5 APX-P)
