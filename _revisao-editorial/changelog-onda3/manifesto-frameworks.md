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
