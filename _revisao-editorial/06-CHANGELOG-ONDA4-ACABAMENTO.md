# CHANGELOG — ONDA 4 (acabamento / P2)

**Escopo:** os ~122 achados P2 (otimizações de experiência). **Backup:** `_backup-pre-onda4/`.
**Resultado:** ~100 P2 editados; restante já resolvido nas Ondas 1-3 ou obsoleto após a migração; poucos deferidos (assets/diagramas e decisões de estilo global).
**Natureza:** consistência de formato, microcópia, referências de fonte estáveis, navegação, eliminação de redundância residual, padronização de boxes/rubricas.

---

# CHANGELOG ONDA 4 — PARATEXTO
## Categoria: P2 (otimizações de experiência)
## Data: 2026-06-16

---

## EDITADOS (17 achados aplicados em 13 arquivos)

---

### P-00/03 — L1-00-capa-e-titulos.md
**Problema:** "Linha curta para canais digitais" era tag interna de briefing exposta no arquivo de produto.
**Aplicado:** Movida para comentário HTML `<!-- -->`. Não aparecerá em arquivo enviado ao designer ou distribuidor.

---

### P-00/04 — L1-00-capa-e-titulos.md
**Problema:** Campos ISBN e Ficha CIP marcados como "a obter"/"a produzir" sem data-limite ou responsável.
**Aplicado:** Substituídos por `[PENDENTE — responsável: X — prazo: Y]` com responsável e prazo explícitos para cada campo.

---

### P-00B/03 — L1-00b-ficha-catalografica.md
**Problema:** "canal oficial da obra, divulgado pelo autor em sua presença profissional pública" — linguagem evasiva em contexto jurídico.
**Aplicado:** Substituído por URL explícito: `linkedin.com/in/falercia (perfil profissional do autor)`.

---

### P-00C/01 — L1-00c-dedicatoria.md
**Problema:** Segunda estrofe era clichê de dedicatória técnica ("A quem teve paciência com minhas ausências enquanto este livro foi escrito").
**Aplicado:** Reescrita com detalhe específico do processo deste livro: "A quem conviveu com as madrugadas em que o método ainda estava errado, e com as manhãs em que ficou certo."

---

### P-00C/02 — L1-00c-dedicatoria.md
**Problema:** Primeira estrofe abstrata demais sem contexto da obra ("A quem aprende a ler o padrão por trás do número").
**Aplicado:** Ancorada na tese central: "A quem escolhe aprender o que dura em vez do que vende, e ensina o próximo a fazer o mesmo."

---

### P-00C2/03 — L1-00c2-promessa.md
**Problema:** "Trinta exemplos memoráveis" repetido 3× no paratexto sem variação de enquadramento.
**Status:** JÁ RESOLVIDO em Onda anterior. Cada arquivo já tem ângulo distinto: promessa (quantidade + explicação de compostos), orelha (profundidade + instrumento operacional), quarta capa (padrões reais + prática). Nenhuma ação necessária.

---

### P-00C2/04 — L1-00c2-promessa.md
**Problema:** Lista F1-F9 não conectava frameworks a perfis de leitor.
**Aplicado:** Adicionado ao final da entrada de frameworks: "— os mais relevantes por perfil estão mapeados na tabela abaixo", criando referência direta à tabela de promessas por perfil existente no mesmo arquivo.

---

### P-00D/03 — L1-00d-agradecimentos.md
**Problema:** Parágrafo sobre família genérico e intercambiável.
**Status:** DEFERIDO. Banca indica "personalizar com detalhe específico ou aceitar a convenção" — texto sugerido = n/a. O parágrafo atual já inclui "a leitura paciente dos primeiros rascunhos cheios de erros", que adiciona especificidade mínima. Decisão de personalização adicional fica com o autor; alteração sem texto sugerido extrapola escopo P2 cirúrgico.

---

### P-00E/01 — L1-00e-sobre-os-casos.md
**Problema:** "mais de 30 exemplos" (intro) vs. "30+ casos" (tabela) — inconsistência de formulação.
**Aplicado:** Padronizado para "Mais de 30 compostos pedagógicos" na célula da tabela, alinhando com a formulação da introdução e com o padrão declarado no resto do paratexto.

---

### P-00E/02 — L1-00e-sobre-os-casos.md
**Problema:** "Postmortem público de incidente material" como critério de elegibilidade criava barreira implícita.
**Aplicado:** Substituído por "Postmortem documentado de incidente material, com aprendizado consolidado e disposição para publicação parcial sob revisão editorial" — reduz barreira sem abrir mão de rigor.

---

### P-00E/03 — L1-00e-sobre-os-casos.md
**Problema:** "sem rodeio" locução redundante em texto já direto.
**Aplicado:** Removido. Frase corre sozinha: "o quadro a seguir declara a categoria de cada um."

---

### P-01/05 — L1-01-prefacio.md
**Problema:** Seções "A diferença que muda tudo" e "Por que escrevi este livro" duplicavam argumento ferramentas vs. princípios sem escalada.
**Aplicado:** Adicionado pivô editorial no início de "Por que escrevi" que distingue explicitamente o diagnóstico da resposta autoral: "não porque o mercado não precise de execução, mas porque o mercado já tem execução em abundância. O que falta é critério." Elimina a sobreposição sem reescrever nenhuma das duas seções.

---

### P-02/04 — L1-02-como-ler.md
**Problema:** "Consultar a documentação atualizada dos fornecedores periodicamente" — instrução sem periodicidade.
**Aplicado:** Substituído por "Consultar as release notes dos seus dois ou três fornecedores principais a cada trimestre — ou quando lançarem versão principal —". Periodicidade clara e ancorada a gatilho.

---

### P-02/05 — L1-02-como-ler.md
**Problema:** Nenhuma das três trilhas de leitura mencionava duração estimada neste arquivo.
**Aplicado:** Adicionadas estimativas em itálico após o nome de cada caminho:
- Caminho 1: *(~50h com exercícios; ~20h em leitura seletiva)*
- Caminho 2: *(~8–30h, conforme capítulos selecionados)*
- Caminho 3: *(~2–4h por princípio)*

---

### P-03/05 — L1-03-introducao.md
**Problema:** "35-50 horas" ambíguo — não especificava se incluía exercícios ou qual trilha.
**Aplicado:** Expandido para "trinta e cinco e cinquenta horas de leitura ativa com os exercícios — ou vinte a trinta horas para a trilha de leitura seletiva descrita no Mapa de Leitura por Nível". Escopo das horas declarado; referência ao Mapa fornecida.

---

### P-03/06 — L1-03-introducao.md
**Problema:** "estrutura pelas extremidades" é jargão do Princípio 4 (P4 — Extremidades), não explicado ainda na introdução.
**Aplicado:** Substituído por "estrutura na abertura e no fechamento da instrução" — linguagem descritiva que o leitor entende sem referência ao princípio.

---

### P-04/03 — L1-04-sumario.md
**Problema:** Numeração de página por capítulo ausente — sumário sem função de índice de navegação.
**Aplicado:** Adicionada nota editorial logo após o cabeçalho da Parte 1: *"Numeração de página por capítulo: a definir após diagramação final. As páginas das Partes são estimativas de produção."* Marca o pendente operacional sem criar falsa precisão.

---

### P-04/04 — L1-04-sumario.md
**Problema:** Mescla de numeração romana (paratexto) e arábica (corpo) sem transição explícita — risco de indexação em ebook.
**Aplicado:** Adicionada nota entre parênteses antes da tabela do paratexto: *(Paginação romana no paratexto; paginação arábica a partir de p. 1 no corpo da obra.)*

---

### P-05/02 — L1-05-mapa-de-leitura-por-nivel.md
**Problema:** Trilha AVANÇADO instrui começar por C00P e C00M sem opção de pular para quem já os leu.
**Aplicado:** Entrada do bloco "Sistema intelectual" reescrita com condicional: "C00P e C00M *(se ainda não leu, comece aqui; se já leu, pule direto para o Núcleo técnico)*".

---

### P-05/03 — L1-05-mapa-de-leitura-por-nivel.md
**Problema:** "A leitura desonesta cobra o preço típico" — tom moralizante para leitor executivo.
**Aplicado:** Reformulado em linguagem de consequência, sem julgamento moral: "Escolher a trilha que você aspira ser, em vez da que efetivamente serve agora, produz o resultado típico: abandono nos capítulos errados por frustração ou tédio."

---

### P-06/04 — L1-06-repositorio-acompanhante.md
**Problema:** "O que separa repositório acompanhante vivo de folheto promocional não é cadência declarada, é entrega consistente sob crítica pública" — frase auto-referencial defensiva que criava a crítica ao tentar refutá-la.
**Aplicado:** Substituído por princípio positivo: "A política editorial é simples: nenhum release publicado sem ter passado pela mesma disciplina de revisão que o livro exige de qualquer artefato sério."

---

### P-10/03 — L1-10-sobre-o-autor.md
**Problema:** Setores de atuação listados sem empresa ou resultado verificável.
**Status:** DEFERIDO. Banca indica "n/a — depende do que o autor está disposto a revelar." Sem texto sugerido. Decisão de adicionar âncora fica com o autor.

---

### P-10/04 — L1-10-sobre-o-autor.md
**Problema:** Parágrafo de abertura para contato duplicava informações já presentes em outros paratextos, estendendo a bio além do necessário.
**Aplicado:** Reduzido para sentença única: "Está aberto ao contato de leitores, pares e organizações via canal oficial da obra."

---

### P-11/03 — L1-11-orelhas.md
**Problema:** "é reconhecido pela produção de frameworks proprietários transferíveis" — auto-atribuição não verificável repetida em dois documentos canônicos (bio + orelha).
**Aplicado:** Substituído por afirmação de prática verificável: "É reconhecido pela prática de instalar disciplina operacional em áreas técnicas e por construir frameworks que sobrevivem à saída do autor."

---

### P-12/05 — L1-12-quarta-capa.md
**Problema:** "caderno de governança em seis páginas" e "trade-off em seis dimensões" eram números sem âncora para leitor de livraria.
**Status:** JÁ RESOLVIDO em Onda anterior. O texto atual da quarta capa já diz "A profundidade executiva vai do método de decisão ao caderno de governança, do roadmap pessoal ao critério de abandono de projeto." — os números específicos foram removidos. Nenhuma ação necessária.

---

## RESUMO FINAL

| Status | Quantidade | Arquivos afetados |
|--------|-----------|-------------------|
| **Editados** | 20 achados | 13 arquivos |
| **Já resolvidos** | 2 achados | L1-00c2-promessa.md, L1-12-quarta-capa.md |
| **Deferidos** | 2 achados | L1-00d-agradecimentos.md (P-00D/03), L1-10-sobre-o-autor.md (P-10/03) |
| **Total P2** | 24 achados | — |

**Deferidos — motivo:** ambos têm texto sugerido "n/a" na banca e dependem de decisão autoral sobre informação pessoal ou privacidade corporativa. Fora do escopo de edição cirúrgica Onda 4.

---

# CHANGELOG ONDA 4 — Manifesto + Frameworks
## Escopo: P2 da banca-01-manifesto-frameworks.md
## Data: 2026-06-16

---

## RESUMO

| Status | Quantidade |
|--------|-----------|
| EDITADO | 15 |
| JÁ RESOLVIDO (ondas anteriores) | 0 |
| DEFERIDO | 2 |

---

## EDITADOS

### C00M-03 — Analogia navegação condensada para 1 parágrafo
- **Arquivo:** L1-C00M-manifesto-invariantes.md
- **Seção:** A NAVEGAÇÃO COMO ANALOGIA
- **Ação:** Reduzido de 3 parágrafos densos para 1 parágrafo enxuto. O núcleo da analogia e a ponte com os invariantes foram preservados; os exemplos detalhados do barco (madeira→aço, vento→nuclear) foram condensados na abertura do parágrafo único.

### C00M-04 — Drucker e Engelbart com ponte para IA generativa
- **Arquivo:** L1-C00M-manifesto-invariantes.md
- **Seção:** REFERÊNCIAS PRINCIPAIS — Sobre o operador como multiplicador
- **Ação:** Adicionadas 1-2 frases de ponte explícita para cada referência, conectando o argumento original (Drucker: método > talento; Engelbart: ferramenta amplifica na proporção da habilidade) ao Princípio 9 (amplificação bidirecional da instrução).

### C00M-05 — Exercício versão de bolso com exemplos concretos
- **Arquivo:** L1-C00M-manifesto-invariantes.md
- **Seção:** EXERCÍCIOS — Versão de bolso para o time
- **Ação:** Adicionado bloco de exemplo após o exercício, demonstrando a transformação para dois princípios (Plausibilidade e Termômetro): linguagem técnica → linguagem operacional da empresa.

### C00P-03 — Seção P.9 reduzida (repetia P.8.5)
- **Arquivo:** L1-C00P-porque-padrao-dura.md
- **Seção:** P.9 — CONVITE AO LIVRO
- **Ação:** Seção reduzida de 3 parágrafos longos para 2 parágrafos curtos. Eliminadas repetições de instrução metodológica que P.8.5 já cobria com mais elegância. Mantido o remate com a lista dos quatro ciclos históricos.

### C00P-04 — Preços de fine-tuning movidos para nota datada
- **Arquivo:** L1-C00P-porque-padrao-dura.md
- **Seção:** P.4 — CASO HISTÓRICO 3
- **Ação:** "US$ 100.000 e US$ 500.000" substituído por "ticket de seis dígitos em dólares" com nota entre parênteses remetendo ao Apêndice J e reconhecendo autocontradição metodológica (o próprio capítulo prega separar número de padrão).

### F1-03 — Campo Revisão Programada com cadência-padrão
- **Arquivo:** L1-F1-decid-ia.md
- **Seção:** 3. OUTPUT — tabela de campos
- **Ação:** Campo "Revisão programada" expandido com cadência-padrão sugerida por nível de autonomia: 90 dias (piloto interno), 6 meses (Assistente/Co-piloto em produção), 3 meses (Agente Supervisionado/Autônomo Regulado).

### F2-03 — Benchmarks de código com glossário inline
- **Arquivo:** L1-F2-encaixe-5.md
- **Seção:** 2. FUNCIONAMENTO — eixo Código
- **Ação:** SWE-bench Verified, HumanEval e LiveCodeBench receberam definições inline entre parênteses explicando o que cada benchmark mede, com referência ao Apêndice J para posições correntes.

### F3-03 — Critério de N dias com guia de calibração
- **Arquivo:** L1-F3-agente-prop.md
- **Seção:** 2. FUNCIONAMENTO — Gates de promoção
- **Ação:** "N dias (tipicamente 14-30)" substituído por tabela de calibração explícita: 14 dias (reversível, impacto interno), 30 dias (efeito externo), 60 dias ou mais (irreversível, alto impacto). Exigência de justificativa para N abaixo do padrão.

### F4-02 — Cobertura de prompts multimodais
- **Arquivo:** L1-F4-prompt-ext.md
- **Seção:** 2. FUNCIONAMENTO — Bloco 3
- **Ação:** Adicionada nota sobre prompts multimodais: input visual vai no Bloco 3; a Constituição (Bloco 2) deve cobrir explicitamente o tratamento de conteúdo visual.

### F4-03 — Instrução para manejo do Bloco 3 quando cresce além do limite
- **Arquivo:** L1-F4-prompt-ext.md
- **Seção:** 2. FUNCIONAMENTO — Bloco 3
- **Ação:** Adicionada regra de posição inegociável: Bloco 3 cresce até o ponto em que Bloco 4 ainda está na posição forte. Referência explícita a T3 do F7 como protocolo de compressão.

### F5-03 — Subseção "Quando Migrar de Mecanismo Existente"
- **Arquivo:** L1-F5-cobertura-integracoes.md
- **Seção:** Nova seção 7 (seções 8-11 renumeradas de 8-10 para 9-11)
- **Ação:** Adicionada subseção com critérios que justificam migração (custo de manutenção, requisito não atendível, incidente recorrente) e critérios que não justificam (moda, conferência, SDK novo do fornecedor).

### F6-02 — Anti-padrão terceirização com distinção legítima/ilegítima
- **Arquivo:** L1-F6-gov-indelegavel.md
- **Seção:** 5. ANTI-PADRÕES
- **Ação:** Anti-padrão "Vamos terceirizar o problema" reformulado para distinguir: accountability não terceiriza (nome interno obrigatório); execução especializada terceirizada (auditoria externa, DPIA, certificação ISO) é legítima e recomendada.

### F6-03 — AI Council com cadência-padrão generalizada
- **Arquivo:** L1-F6-gov-indelegavel.md
- **Seção:** 2. FUNCIONAMENTO — Os 10 controles, controle 10
- **Ação:** Controle 10 expandido com cadência mínima generalizada: mensal nos primeiros 12 meses, trimestral após revisão de maturidade no primeiro ano; permanece mensal em setores regulados.

### F7-03 — Diagnóstico de pré-requisito antes das alavancas
- **Arquivo:** L1-F7-composto-3t.md
- **Seção:** 2. FUNCIONAMENTO — antes de "Ordem de aplicação"
- **Ação:** Adicionada subseção "Diagnóstico de pré-requisito" com dois caminhos: (1) com atribuição de custo instalada (Pilar 5 LLMOps) → decisão por dado; (2) sem atribuição → estimativa inicial por sintoma (volume premium > 70%, loops visíveis, contexto > 50%).

### F8-03 — Guia de construção de adversarial set por domínio
- **Arquivo:** L1-F8-eval-piramide.md
- **Seção:** 2. FUNCIONAMENTO — Transversal adversarial e segurança
- **Ação:** Adicionado parágrafo "Construção por domínio" com três fontes (incidentes anteriores, literatura de segurança, brainstorm adversarial) e exemplos de categorias dominantes por setor (RH, financeiro, clínico, consultoria).

### TRANSV-01 — Notas de escopo de observabilidade em F6 e F7
- **Arquivos:** L1-F6-gov-indelegavel.md, L1-F7-composto-3t.md
- **Seção:** 1. OBJETIVO (bloco de escopo adicionado ao início)
- **Ação:** F3 e F5 já tinham nota de escopo de ondas anteriores. F6 e F7 receberam nota equivalente declarando âncora autoritativa (Cap 22) e escopo restrito de cada framework (F6 = governança/auditoria; F7 = custo). Completa o achado transversal P0.

---

## DEFERIDOS

### F3-01 — Matriz visual 4×4
- **Arquivo:** L1-F3-agente-prop.md
- **Motivo:** Requer diagrama gráfico. Não implementável via edição de texto Markdown.

### F9-04 — F9 sem exemplo memorável com números reais
- **Arquivo:** L1-F9-rota-dupla.md
- **Status:** EDITADO (reclassificado de DEFERIDO para EDITADO durante execução)
- **Ação:** Adicionado caso ilustrativo composto "O custo de confundir número com padrão" — Head de Tecnologia de SaaS B2B, três migrações em 18 meses, R$ 280 mil em custo acumulado, quarta decisão resolvida em 45 minutos com aplicação do F2 + Apêndice J.

---

## NOTA DE RECONCILIAÇÃO

O item F9-04 foi inicialmente marcado como DEFERIDO mas foi executado durante a onda. Portanto:

| Status | Quantidade |
|--------|-----------|
| EDITADO | 16 |
| JÁ RESOLVIDO (ondas anteriores) | 0 |
| DEFERIDO | 1 (F3-01 — matriz visual) |

---

# CHANGELOG — ONDA 4 / P2 — C01 a C11
# Data: 2026-06-16
# Escopo: apenas itens P2 (Achados 08, 09, 06, 05, 05, 06, 07, 05, 06, 11, 15, 16, 22, 23, 27, 32, 33)

---

## C01 — L1-C01-o-que-e-ia.md
**Achado 08 [EDITADO]** — Narrativa Minsky/Papert simplificada
- Parágrafo em 1.4.2 expandido: substituída a frase "O livro foi lido... o dano de percepção estava feito" por versão qualificada que reconhece múltiplas causas do primeiro inverno (cortes orçamentários independentes), cita a historiografia mais recente, e preserva o papel simbólico do livro sem exagerar causalidade.

**Achado 09 [EDITADO]** — XCON economizou US$40M sem fonte citada
- Referência adicionada entre parênteses: "segundo estudos da época documentados em McDermott, 1982, e citados em Russell & Norvig, *Artificial Intelligence: A Modern Approach*".

**Achado sistêmico [EDITADO]** — Espaço duplo em "Curiosidade  **" na autoavaliação
- Corrigido de `**Curiosidade ** —` para `**Curiosidade** —` (erro tipográfico de template).

---

## C02 — L1-C02-como-modelos-funcionam.md
**Achado 06 [EDITADO]** — Custo de treino "50 a 500 milhões" sem fonte, range de 10x
- Frase expandida com nota de que são estimativas externas de analistas (SemiAnalysis, Epoch AI), não dados divulgados pelos laboratórios.

**Achado sistêmico [EDITADO]** — Espaço duplo em autoavaliação (ver C01).

---

## C03 — L1-C03-tokens.md
**Achado 05 [EDITADO]** — Epígrafe levemente condescendente
- Epígrafe reescrita de "Toda vez que você esquece essa diferença, você gasta dinheiro à toa" para "Quem entende essa diferença constrói sistemas que escalam; quem ignora paga para descobrir." — tom de par desafiando executivo, não de professor repreendendo aluno.

**Achado sistêmico [EDITADO]** — Espaço duplo em autoavaliação (ver C01).

---

## C04 — L1-C04-janela-de-contexto.md
**Achado 05 [EDITADO]** — Números de janela por modelo são os dados mais perecíveis do livro
- Seção 4.3.1 reformulada: removida lista de modelos com valores específicos (Claude 200k, Gemini 1-2M, GPT 128k-400k), substituída por princípio durável com instrução de consultar documentação do provedor; mantida apenas a referência de grandeza (200k ≈ livro de 350-400 páginas).
- Tabela de resumo executivo (4.8) atualizada para refletir a nova redação ("consulte o provedor para o dado atual").

**Achado sistêmico [EDITADO]** — Espaço duplo em autoavaliação (ver C01).

---

## C05 — L1-C05-embeddings.md
**Achado 06 [DEFERIDO]** — Capítulo é commodity; falta perspectiva proprietária do autor
- Requer contribuição original do autor sobre quando NÃO usar embeddings (casos de precisão > recall, domínios estreitos). Não editável sem voz do autor. Sinalizado para revisão autoral na Onda 5 ou edição posterior.

**Achado 07 [EDITADO]** — Exercícios dependem de ferramentas específicas que podem ser descontinuadas
- Exercício 1: reformulado para indicar "ferramentas de visualização disponíveis no momento" com remissão ao material suplementar do livro, em vez de citar TensorFlow Embedding Projector por nome.
- Exercício 2: reformulado para "API do seu provedor de preferência (verifique documentação do provedor para o modelo atual)".
- Projeto do Capítulo (5.12): referência a "OpenAI text-embedding-3-small ou similar" substituída por instrução genérica de verificar documentação do provedor.

**Achado sistêmico [EDITADO]** — Espaço duplo em autoavaliação (ver C01).

---

## C06 — L1-C06-rag.md
**Achado 05 [EDITADO]** — Nome de modelo específico ("voyage-multilingual") em cenário ilustrativo
- Substituído por "modelo de embedding com suporte multilingual" em 6.5, removendo dependência de versão/produto específico.

**Achado 06 [EDITADO]** — Espaço duplo sistêmico antes do checkbox na autoavaliação
- Corrigido `**Curiosidade **` → `**Curiosidade**` (ver C01).

---

## C07 — L1-C07-memoria.md
**Achado 11 [EDITADO]** — URL Anthropic Memory volátil nas referências
- `[Anthropic — Memory in Claude](https://www.anthropic.com/news/memory)` substituído por `[Anthropic — Documentação de funcionalidades de memória em Claude](https://docs.anthropic.com)` — referência estável ao domínio de documentação oficial.

**Achado sistêmico [EDITADO]** — Espaço duplo em autoavaliação (ver C01).

---

## C08 — L1-C08-fine-tuning.md
**Achado 15 [EDITADO]** — "modelo grande genérico" como definição datada
- Substituído por "modelo frontier comercial" em 8.3.2 — terminologia mais estável que não depende da percepção de tamanho relativo de cada geração.

**Achado 16 [EDITADO]** — URL específica de documentação Anthropic volátil nas referências
- Link com URL específica removido; substituído por referência textual com instrução de consultar docs.anthropic.com para versão atual.

**Achado sistêmico [EDITADO]** — Espaço duplo em autoavaliação (ver C01).

---

## C09 — L1-C09-engenharia-prompt.md
**Achado 22 [EDITADO]** — Anthropic Prompt Library borderline com coleção de prompts
- Referência recontextualizada explicitamente: "útil para ver exemplos de estrutura e anatomia de prompt; use como referência de formato, não como repositório de prompts prontos para copiar". Mantida na seção de referências com essa ressalva.

**Achado 23 [EDITADO]** — Inconsistência de moeda entre capítulos (reais em C09 vs dólares em C08)
- Valor em reais mantido como âncora para empresa brasileira do exemplo, com conversão aproximada adicionada entre parênteses: "cerca de 520 mil reais por ano (aproximadamente 100 mil dólares, ao câmbio do período)".

**Achado sistêmico [EDITADO]** — Espaço duplo em autoavaliação (ver C01).

---

## C10 — L1-C10-chain-of-thought.md
**Achado 27 [EDITADO]** — Ausência de discussão sobre CoT e latência em aplicações com SLA apertado
- Terceira limitação em 10.5 expandida: adicionado parágrafo específico sobre trade-off latência/qualidade em aplicações com SLA de 2-3 segundos (atendimento ao cliente, assistentes em tempo real), com orientação para reasoning models nativos nesses casos e critério de aplicar CoT apenas em fluxos onde latência maior é tolerada.

**Achado sistêmico [EDITADO]** — Espaço duplo em autoavaliação (ver C01).

---

## C11 — L1-C11-context-engineering.md
**Achado 32 [EDITADO]** — Referência a threads de X/Twitter de Karpathy não é estável
- Substituído por referência mais estável: "publicações e apresentações sobre 'context engineering' como disciplina emergente (2024–2025; consulte karpathy.ai ou o canal do autor para referências atualizadas)" — remove dependência de URL de rede social.

**Achado 33 [EDITADO]** — "Configuração leva 30 minutos" é afirmação arriscada
- Legenda do Diagrama 11.3 substituída por: "Configuração técnica é direta para aplicações bem estruturadas. O investimento real é em reorganizar o prompt para que o conteúdo estável venha antes do variável." — elimina promessa de tempo específico que varia por stack.

**Achado sistêmico [EDITADO]** — Espaço duplo em autoavaliação (ver C01).

---

## TOTALIZADOR POR CAPÍTULO

| Cap | Editados | Já Resolvidos | Deferidos |
|-----|----------|---------------|-----------|
| C01 | 3 (A08, A09, sistêmico) | 0 | 0 |
| C02 | 2 (A06, sistêmico) | 0 | 0 |
| C03 | 2 (A05, sistêmico) | 0 | 0 |
| C04 | 2 (A05, sistêmico) | 0 | 0 |
| C05 | 2 (A07, sistêmico) | 0 | 1 (A06) |
| C06 | 2 (A05, A06/sistêmico) | 0 | 0 |
| C07 | 2 (A11, sistêmico) | 0 | 0 |
| C08 | 3 (A15, A16, sistêmico) | 0 | 0 |
| C09 | 3 (A22, A23, sistêmico) | 0 | 0 |
| C10 | 2 (A27, sistêmico) | 0 | 0 |
| C11 | 3 (A32, A33, sistêmico) | 0 | 0 |
| **Total** | **26** | **0** | **1** |

## NOTA: Achado sistêmico (A06-C06 espaço duplo)
O espaço duplo em `**Curiosidade **` foi identificado como erro de template que afeta todos os capítulos C01–C11. Corrigido em todos os 11 arquivos como parte deste lote P2.

---

# CHANGELOG ONDA 4 — ACABAMENTO (P2)
# Capítulos C12 a C19
# Data: 2026-06-16

---

## SUMÁRIO POR CAPÍTULO

| Cap | Arquivo | Editados | Já Resolvidos | Obsoletos | Deferidos |
|-----|---------|----------|---------------|-----------|-----------|
| C12 | L1-C12-agentes.md | 0 | 1 | 0 | 0 |
| C13 | L1-C13-mcp.md | 0 | 1 | 0 | 0 |
| C14 | L1-C14-ai-engineering.md | 1 | 1 | 0 | 0 |
| C14B | L1-C14B-reasoning-models.md | 1 | 0 | 0 | 1 |
| C14C | L1-C14C-spec-driven-development.md | 2 | 0 | 0 | 0 |
| C15 | L1-C15-comparacao-modelos.md | 1 | 1 | 0 | 0 |
| C16 | L1-C16-open-source.md | 0 | 2 | 0 | 0 |
| C17 | L1-C17-github-repos.md | 0 | 1 | 1 | 0 |
| C18 | L1-C18-economia-tokens.md | 1 | 0 | 0 | 0 |
| C19 | L1-C19-seguranca.md | 2 | 0 | 0 | 0 |
| **TOTAL** | | **8** | **7** | **1** | **1** |

---

## DETALHAMENTO POR CAPÍTULO

---

### C12 — L1-C12-agentes.md

#### P2-06 — Typo "Curiosidade **" em 12.14 item 5
**Status: [JÁ RESOLVIDO]**
O arquivo atual já contém `**Curiosidade**` sem espaço extra. Correção aplicada em onda anterior ou no texto original.

---

### C13 — L1-C13-mcp.md

#### P2-08 — Typo "Curiosidade **" em 13.14 item 5
**Status: [JÁ RESOLVIDO]**
O arquivo atual já contém `**Curiosidade**` sem espaço extra.

---

### C14 — L1-C14-ai-engineering.md

#### P2-05 — Lista de ferramentas de observabilidade sem nota de durabilidade
**Status: [EDITADO]**
**Localização:** Seção 14.3.3, parágrafo de ferramentas de observabilidade.
**Antes:** `...Ferramentas como LangSmith, Helicone, Phoenix Arize, Langfuse, e Datadog com integração IA, estão consolidando esse espaço.`
**Depois:** `...Ferramentas como LangSmith, Helicone, Phoenix Arize, Langfuse, e Datadog com integração IA estão consolidando esse espaço (exemplos correntes — Apêndice J para lista atualizada).`

#### P2-06 — Typo "Curiosidade **" em 14.14 item 5
**Status: [JÁ RESOLVIDO]**
O arquivo atual já contém `**Curiosidade**` sem espaço extra.

---

### C14B — L1-C14B-reasoning-models.md

#### P2-05 — Referência a "Lanham e colegas" sem ano inline na primeira citação
**Status: [EDITADO]**
**Localização:** Parágrafo de introdução à faithfulness (14B.1, terceiro parágrafo do capítulo).
**Antes:** `com nomes como Lanham e colegas conduzindo experimentos sistemáticos`
**Depois:** `com nomes como Lanham et al. (2023) conduzindo experimentos sistemáticos`

#### P2-06 — Inconsistência de template: "Curiosidade ativa" vs "Curiosidade" nos demais
**Status: [DEFERIDO]**
C14B e C14C usam consistentemente "Curiosidade ativa" entre si. O padrão diverge de C12–C13–C14 que usam apenas "Curiosidade". A banca classifica como "decisão de estilo" (ROI BAIXO). Deferido para decisão de padronização global de template — fora do escopo da Onda 4.

---

### C14C — L1-C14C-spec-driven-development.md

#### P2-06 — Checklist com 8 itens — o mais longo do bloco
**Status: [EDITADO]**
**Localização:** Seção 14C.9 — CHECKLIST DO CAPÍTULO.
**Antes:** Itens 7 e 8 separados:
```
- [ ] Articular como SDD instancia os Invariantes 9 (Operador), 3 (Camada Dupla), 6 (Autonomia Proporcional) e 8 (Responsabilidade Indelegável)
- [ ] Esboçar um piloto de quatro semanas em uma squad pequena, com critério de sucesso explícito antes de começar
```
**Depois:** Fundidos em item único marcado como avançado:
```
- [ ] *(Avançado)* Articular como SDD instancia os Invariantes 9 (Operador), 3 (Camada Dupla), 6 (Autonomia Proporcional) e 8 (Responsabilidade Indelegável), e esboçar um piloto de quatro semanas com critério de sucesso explícito antes de começar
```
O checklist passa de 8 para 7 itens, com o último marcado como avançado para diferenciar do núcleo.

#### P2-07 — "Kiro" e "Forge" na lista de integrações sem contexto para leitor brasileiro
**Status: [EDITADO]**
**Localização:** Seção 14C.3.7, parágrafo do GitHub Spec Kit.
**Antes:** `(Copilot, Claude Code, Cursor, Codex, Gemini, Windsurf, Kiro, Forge e outras)`
**Depois:** `(Copilot, Claude Code, Cursor, Codex, Gemini, Windsurf, Kiro da AWS, Forge e outras)`
Adicionado contexto mínimo para Kiro. Forge mantido sem contexto (projeto de codificação com suficiente reconhecimento técnico no segmento).

---

### C15 — L1-C15-comparacao-modelos.md

#### P2-05 — Typo "Curiosidade **" em 15.14 item 5
**Status: [EDITADO]**
**Localização:** Seção 15.14 — Autoavaliação, item 5.
**Antes:** `| 5 | **Curiosidade ** — Está com vontade de entender em profundidade o ecossistema open source...`
**Depois:** `| 5 | **Curiosidade** — Está com vontade de entender em profundidade o ecossistema open source...`
Espaço extra antes do fechamento do negrito removido.

#### P2-06 — Pergunta de revisão 3 orientada a nomes de produtos específicos
**Status: [JÁ RESOLVIDO]**
O arquivo atual já contém a pergunta reformulada: "Como você decidiria entre o frontier premium centrado em código e o frontier com força em agência para um sistema de agentes autônomos? Quais perguntas do Diagnóstico de Encaixe entre Tarefa e Modelo você usaria?" — orientada a critérios, sem nomear modelos específicos.

---

### C16 — L1-C16-open-source.md

#### P2-05 — Analogia da frota (16.2) longa demais
**Status: [JÁ RESOLVIDO]**
A seção 16.2 no arquivo atual já contém dois parágrafos substantivos mais uma frase de transição — estrutura já comprimida conforme recomendação da banca.

#### P2-06 — Pergunta de revisão 5 cita "Nota Técnica ANPD de 2026" como dado memorável
**Status: [JÁ RESOLVIDO]**
A pergunta 5 da seção 16.8 já foi reformulada: "Como a regulação de privacidade brasileira (LGPD e as orientações da ANPD sobre IA generativa — verificar versão corrente em fonte oficial, Apêndice J) desloca a fronteira em favor de operação em território nacional...". Perguntas pelo padrão regulatório durável, não pela data específica.

---

### C17 — L1-C17-github-repos.md

#### P2-04 — W&B descrito sem destaque para implicação de self-hosting restrito
**Status: [OBSOLETO]**
A seção 17.6 foi completamente reestruturada na Onda 2. O capítulo não contém mais lista específica de oito repositórios — foi substituída por referência ao Apêndice Vivo (repositório de recursos da obra). A discussão de W&B e suas implicações de self-hosting não existe mais no corpo do capítulo. Achado obsoleto pela reescrita estrutural da seção.

#### P2-05 — Exemplo de 10 horas com 3 pessoas é ambíguo
**Status: [JÁ RESOLVIDO]**
O texto atual (seção 17.5) já diz "dez horas totais distribuídas em três tardes", o que deixa claro que são 10 horas de sessão coletiva, não por pessoa.

---

### C18 — L1-C18-economia-tokens.md

#### P2-06 — Razão premium/pequeno de "30 a 50 vezes" pode envelhecer com ajustes de pricing
**Status: [EDITADO]**
**Localização 1:** Parágrafo sobre Tier no corpo do texto.
**Antes:** `...paga 30 a 50 vezes o preço do modelo pequeno para entregar a mesma qualidade. Tier mal escolhido...`
**Depois:** `...paga 30 a 50 vezes o preço do modelo pequeno para entregar a mesma qualidade (magnitude observada em 2026; confirmar razão atual nas fichas dos fornecedores — Apêndice J). Tier mal escolhido...`

**Localização 2:** Quadro 18.A, linha do Tier.
**Antes:** `30-50× por chamada mal roteada`
**Depois:** `30-50× por chamada mal roteada (2026 — Apêndice J)`

---

### C19 — L1-C19-seguranca.md

#### P2-05 — Regra de cadência trimestral sem rota de entrada para organização sem red team
**Status: [EDITADO]**
**Localização:** Seção 19.5 — Red teaming sistemático, bloco "Cadência".
**Antes:** `A regra prática: se o último red team foi há mais de noventa dias, a organização não tem red team, tem auditoria pontual antiga.`
**Depois:** `A regra prática: se o último red team foi há mais de noventa dias, a organização não tem red team, tem auditoria pontual antiga. Para organizações sem red team instalado, o objetivo inicial não é chegar logo à cadência trimestral — é conduzir a primeira sessão em até noventa dias, com suite de vinte casos cobrindo as cinco categorias de maior risco do OWASP LLM Top 10 para o contexto específico. A cadência trimestral é o regime maduro; chegar a ele tipicamente leva dois a três ciclos.`

#### P2-06 — Microsoft Presidio recomendado sem instrução de aplicar o protocolo de C17
**Status: [EDITADO]**
**Localização:** Seção 19.3.5 (PII leakage), bloco "Redaction de entrada".
**Antes:** `Ferramentas comuns: Microsoft Presidio em pipeline de pré-processamento, com customização para entidades brasileiras.`
**Depois:** `Ferramentas comuns: Microsoft Presidio em pipeline de pré-processamento, com customização para entidades brasileiras (referência comum em 2026 — antes de adotar, aplique o protocolo de trinta minutos do Cap 17 para verificar a fase corrente do ciclo de vida).`

---

## TOTAIS CONSOLIDADOS

| Status | Quantidade |
|--------|-----------|
| EDITADO | 8 |
| JÁ RESOLVIDO | 7 |
| OBSOLETO | 1 |
| DEFERIDO | 1 |
| **TOTAL P2 processados** | **17** |

---

*Onda 4 — P2 concluída. Arquivos alterados: L1-C14-ai-engineering.md, L1-C14B-reasoning-models.md, L1-C14C-spec-driven-development.md, L1-C15-comparacao-modelos.md, L1-C18-economia-tokens.md, L1-C19-seguranca.md.*

---

# CHANGELOG ONDA 4 — ACABAMENTO P2
# Capítulos C20 a C28
# Data: 2026-06-16

---

## C20 — L1-C20-futuro.md

| Achado | Categoria | Status | Descrição |
|--------|-----------|--------|-----------|
| 07 | P2 | [EDITADO] | Inserida referência parentética "(Wack, 1985)" na menção à Shell em 20.1, conectando o corpo do texto às referências de 20.14. |

**Resumo C20:** 1 editado / 0 já resolvido / 0 deferido

---

## C21 — L1-C21-evals.md

| Achado | Categoria | Status | Descrição |
|--------|-----------|--------|-----------|
| 04 | P2 | [EDITADO] | Checklist 21.8 reestruturado em dois blocos: "O que construir" (ações verificáveis com entregável) e "O que dominar" (proficiências verificadas nas perguntas de revisão). Elimina heterogeneidade que tornava o checklist não-rastreável como instrumento de progresso. |
| 05 | P2 | [EDITADO] | Nota de custo e dependência de infraestrutura adicionada ao BERTScore na tabela de tipos (21.3.3): "(BERTScore exige modelo de embedding — mais custoso que BLEU, mas semanticamente superior; avaliar viabilidade de infraestrutura antes de adotar em equipe pequena)". |

**Resumo C21:** 2 editados / 0 já resolvido / 0 deferido

---

## C22 — L1-C22-llmops.md

| Achado | Categoria | Status | Descrição |
|--------|-----------|--------|-----------|
| 05 | P2 | [EDITADO] | Referência Karpathy expandida para incluir instrução de verificar URL corrente e nota de que palestra sem repositório permanente é referência frágil; orientação para Apêndice J. |

**Resumo C22:** 1 editado / 0 já resolvido / 0 deferido

---

## C23 — L1-C23-alignment.md

| Achado | Categoria | Status | Descrição |
|--------|-----------|--------|-----------|
| 05 | P2 | [EDITADO] | Red teaming em 23.3.5 agora cita documentos públicos verificáveis: "conforme documentada publicamente por equipes de alignment em Anthropic (Responsible Scaling Policy, 2023/2024; Constitutional AI, Bai et al., 2022), OpenAI e DeepMind a partir de 2022". Elimina afirmação de autoridade por associação sem ancora verificável. |

**Resumo C23:** 1 editado / 0 já resolvido / 0 deferido

---

## C24 — L1-C24-governanca.md

| Achado | Categoria | Status | Descrição |
|--------|-----------|--------|-----------|
| 05 | P2 | [EDITADO] | Referência ANPD em 24.14 substituída por documento específico: "Guia Orientativo de Proteção de Dados no uso de IA Generativa (2024) e demais notas técnicas sobre IA (verificar lista atualizada em www.gov.br/anpd — conforme Apêndice J — Trilha do Número)". Elimina a referência vaga "versão corrente verificável em fonte oficial". |

**Resumo C24:** 1 editado / 0 já resolvido / 0 deferido

---

## C25 — L1-C25-trade-offs.md

| Achado | Categoria | Status | Descrição |
|--------|-----------|--------|-----------|
| 05 | P2 | [EDITADO] | Adicionada nota sobre HITL em volume ao Trade-off T5: instrução explícita sobre HITL por amostra estatística como solução arquitetural para produtos com milhões de interações mensais, com referência a LGPD e AI Act e instrução de registrar critério de amostragem no Caderno de Governança. |

**Resumo C25:** 1 editado / 0 já resolvido / 0 deferido

---

## C26 — L1-C26-roadmap-pessoal.md

| Achado | Categoria | Status | Descrição |
|--------|-----------|--------|-----------|
| 05 | P2 | [EDITADO] | Seções 26.9, 26.10 e 26.11 reestruturadas: checklist e exercícios fundidos em bloco único "26.9 — Aplicação Imediata" com 8 itens acionáveis não-redundantes; perguntas de revisão encurtadas para 4 (de 6); exercício integrador unificado em 26.11 com critérios de revisão por par. Elimina sobreposição de ~70% entre os três blocos. |
| 06 | P2 | [EDITADO] | Adicionada nota em 26.1 orientando profissionais de funções corporativas (CFO, CHRO, advogado interno, controller) a se classificarem como persona Gestor ou Profissional Solo, com referência à seção 26.4 para ajustes por contexto. |

**Resumo C26:** 2 editados / 0 já resolvido / 0 deferido

---

## C27 — L1-C27-ia-para-pme-brasileira.md

| Achado | Categoria | Status | Descrição |
|--------|-----------|--------|-----------|
| 05 | P2 | [JÁ RESOLVIDO] | Boxes de CTA verificados: C27 usa "🎯 **PARA DONOS DE PME**" com 3 perguntas duras; C28 usa "🎯 **PARA EXECUTIVOS**" com 3 perguntas duras. Mesmo ícone, mesma estrutura, rótulo diferenciado por persona — consistência mantida intencionalmente. Nenhuma ação necessária. |

**Resumo C27:** 0 editados / 1 já resolvido / 0 deferido

---

## C28 — L1-C28-interpretabilidade-mecanicista.md

| Achado | Categoria | Status | Descrição |
|--------|-----------|--------|-----------|
| 04 | P2 | [JÁ RESOLVIDO] | Referência a transformer-circuits.pub no corpo do texto (linha 98) já continha instrução "verifique URL corrente no site oficial da Anthropic, conforme Apêndice J — Trilha do Número". Problema da banca endereçado em onda anterior. |
| 06 | P2 | [EDITADO] | Exercício 4 (28.10) atualizado: substituído "papers acadêmicos em conferências como NeurIPS e ICML" por fontes curadas acessíveis a equipe de produto (Alignment Forum, LessWrong, sínteses de equipes de pesquisa), com nota explícita de que papers brutos de NeurIPS/ICML exigem pesquisador treinado para triagem. |

**Resumo C28:** 1 editado / 1 já resolvido / 0 deferido

---

## CONSOLIDADO ONDA 4 — P2 — C20 a C28

| Capítulo | Editados | Já Resolvidos | Deferidos |
|----------|----------|---------------|-----------|
| C20 | 1 | 0 | 0 |
| C21 | 2 | 0 | 0 |
| C22 | 1 | 0 | 0 |
| C23 | 1 | 0 | 0 |
| C24 | 1 | 0 | 0 |
| C25 | 1 | 0 | 0 |
| C26 | 2 | 0 | 0 |
| C27 | 0 | 1 | 0 |
| C28 | 1 | 1 | 0 |
| **TOTAL** | **10** | **2** | **0** |

---

*Notas: C22 e C24 não tinham P2 próprios além dos registrados acima. C21, C23, C25 não fazem parte do lote primário indicado pelo usuário (C20, C25, C26, C28 com P2 confirmados), mas foram incluídos porque a banca os lista com P2. Nenhum deferido — todos os P2 eram de baixo risco e cirurgicamente corrigíveis sem reescrever conteúdo de P0/P1.*

---

# Changelog Onda 4 — Apêndices A–I
## Onda 4 / P2 / data: 2026-06-16

---

## APX-A — L1-APX-A-glossario.md

| # | Status | Descrição |
|---|--------|-----------|
| A-04 | [EDITADO] | Adicionada remissiva cruzada ao fim de "Prompt engineering": "Ver também Context Engineering, que expande a disciplina para orquestração hierárquica de múltiplas fontes no contexto." |
| A-05 | [JÁ RESOLVIDO] | "Autoavaliação" já continha marcador ★ no arquivo atual — item resolvido em onda anterior. |
| A-06 | [EDITADO] | Adicionada nota introdutória `> Padrões de interface e plataforma que afetam arquitetura de produto com IA.` logo após o cabeçalho `## VII. Padrões de produto e plataformas`. |

---

## APX-B — L1-APX-B-mapa-mental.md

| # | Status | Descrição |
|---|--------|-----------|
| B-03 | [EDITADO] | Adicionada nota `> Nota: o diagrama acima é representação funcional, não hierárquica. Os nove princípios têm peso equivalente na obra; a posição reflete apenas restrições do diagrama em texto.` após o bloco ASCII da roda dos Nove Princípios. |
| B-04 | [JÁ RESOLVIDO] | Linha "Estou em incidente" já estava presente na tabela "Como usar este mapa" — item resolvido em onda anterior. |

---

## APX-C — L1-APX-C-roadmaps.md

| # | Status | Descrição |
|---|--------|-----------|
| C-05 | [EDITADO] | Substituído "Dez ou mais clientes operando pelo método" por "Portfólio ativo com pelo menos três clientes aplicando o método como norma, com case documentado por cada um" no Marco 365 do Roadmap 4 (Consultor). Meta agora é relativa ao contexto, não absoluta. |

---

## APX-D — L1-APX-D-ferramentas.md

| # | Status | Descrição |
|---|--------|-----------|
| D-05 | [OBSOLETO] | APX-D foi reescrito na Onda 2. O arquivo atual não contém "Editor desta lista: Fabio Garcia" nem nenhuma lista de ferramentas no corpo — o catálogo foi movido ao repositório externo. Item inexistente no texto atual. |
| D-06 | [OBSOLETO] | APX-D foi reescrito na Onda 2. "Pezzo" não aparece no arquivo atual. Item inexistente no texto atual. |

---

## APX-E — L1-APX-E-leituras.md

| # | Status | Descrição |
|---|--------|-----------|
| E-04 | [OBSOLETO] | APX-E foi reescrito na Onda 2 como documento de método de curadoria ("Como montar sua dieta de informação"). Não há lista de leituras com entrada de Davenport (2018) no arquivo atual. Item inexistente no texto atual. |

---

## APX-F — L1-APX-F-newsletters.md

| # | Status | Descrição |
|---|--------|-----------|
| F-05 | [OBSOLETO] | APX-F foi reescrito na Onda 2 como página de redirecionamento para APX-E. Não há conteúdo sobre Magazine Luiza nem qualquer lista de empresas no arquivo atual. Item inexistente no texto atual. |

---

## APX-G — L1-APX-G-papers.md

| # | Status | Descrição |
|---|--------|-----------|
| G-03 | [EDITADO] | Adicionado separador `---` e confirmado heading `## Como ler papers de IA` — o heading já existia mas sem separador visual antes do bloco; adicionado `---` para consistência de formatação com as demais seções. |
| G-04 | [JÁ RESOLVIDO] | Park et al. — *Generative Agents* (Stanford, 2023) já estava presente na Categoria V como linha 33 do arquivo atual — item resolvido em onda anterior. |

---

## APX-H — L1-APX-H-bibliografia.md

| # | Status | Descrição |
|---|--------|-----------|
| H-04 | [EDITADO] | Seção V ("Recursos pedagógicos comentados") removida como seção própria. Conteúdo substituído por nota blockquote `> Para curadoria comentada de leituras, cursos e fontes de acompanhamento, ver Apêndice E — Como montar sua dieta de informação.` inserida ao final da Seção IV. O que era "Seção VI — Sobre esta obra" passou a ser "Seção V — Sobre esta obra". |
| H-05 | [JÁ RESOLVIDO] | Bommasani et al. já está posicionado dentro de "## I. Papers seminais" na subseção "Filosofia e fundamento" — não está misturado com livros em seção separada. Item resolvido em onda anterior. |

---

## APX-I — L1-APX-I-indice-remissivo.md

| # | Status | Descrição |
|---|--------|-----------|
| I-05 | [EDITADO] | Removido marcador ★ de "Golden set ★ ◆" — corrigido para "Golden set ◆". Golden set é termo canônico do campo (◆), não propriedade da obra (★). |
| I-06 | [EDITADO] | Corrigida ortografia de "Vianna Castro Almeida (caso)" para "Vianna, Castro e Almeida (caso)", alinhando com a grafia canônica do APX-A (Cat. VIII). Pólice.io verificado: grafia consistente entre APX-A e APX-I. |

---

## Totais por apêndice

| Apêndice | Editados | Já Resolvidos | Obsoletos | Deferidos |
|----------|----------|---------------|-----------|-----------|
| APX-A | 2 | 1 | 0 | 0 |
| APX-B | 1 | 1 | 0 | 0 |
| APX-C | 1 | 0 | 0 | 0 |
| APX-D | 0 | 0 | 2 | 0 |
| APX-E | 0 | 0 | 1 | 0 |
| APX-F | 0 | 0 | 1 | 0 |
| APX-G | 1 | 1 | 0 | 0 |
| APX-H | 1 | 1 | 0 | 0 |
| APX-I | 2 | 0 | 0 | 0 |
| **TOTAL** | **8** | **4** | **4** | **0** |

---

# Changelog — Onda 4 (Acabamento P2) — Apêndices J, K, M, N, O, Q
**Data:** junho de 2026
**Escopo:** apenas achados P2 da banca adversarial

---

## APX-J — Trilha do Número
**Arquivo:** `04-apendices/L1-APX-J-trilha-do-numero.md`

| Achado | Status | Descrição da ação |
|---|---|---|
| J/05 | [EDITADO] | Adicionada referência "(fonte: incidentdatabase.ai, relatório anual 2025)" ao final da estatística do AI Incident Database na Seção 5. |
| J/06 | [DEFERIDO] | Verificação de acessibilidade de todos os URLs de arXiv. Ação de manutenção sem texto a editar — deferida para próxima revisão semestral conforme política do apêndice. |

---

## APX-K — Gabaritos Comentados
**Arquivo:** `04-apendices/L1-APX-K-gabaritos.md`

| Achado | Status | Descrição da ação |
|---|---|---|
| K/04 | [JÁ RESOLVIDO] | O arquivo já contém, na seção "Roadmap pessoal — Capítulo 26", rubrica de proficiência completa com critério alternativo explícito para autoavaliação individual ("Para autoavaliação individual: os três marcos têm datas fixas, métricas verificáveis, e dependências explícitas"). Nenhuma edição necessária. |

---

## APX-M — Manifesto de Bolso
**Arquivo:** `04-apendices/L1-APX-M-manifesto-bolso.md`

| Achado | Status | Descrição da ação |
|---|---|---|
| M/02 | [EDITADO] | Mecânica do Princípio 4 corrigida: separado "eixo de tarefa" (código, matemática, multimodal, contexto longo) de "custo composto" como ponderador transversal, eliminando ambiguidade entre domínios e eixo de custo. |
| M/03 | [EDITADO] | Adicionados 3 parágrafos de expansão abaixo da frase-síntese "Modelos passam. Método fica.", ancorada na tese central da obra — capacidade de escolher, avaliar, governar e aprender como o que não envelhece. |

---

## APX-N — Metodológico, sobre os números deste livro
**Arquivo:** `04-apendices/L1-APX-N-metodologico-numeros.md`

| Achado | Status | Descrição da ação |
|---|---|---|
| N/03 | [EDITADO] | Footer unificado: "Atualizado em: junho de 2026. Próxima revisão programada: junho de 2027." — eliminando a aparência de duas políticas de revisão independentes. O header mantém a política geral ("anual ou sob mudança relevante"); o footer passa a conter a data específica, tornando a informação complementar em vez de redundante. |
| N/04 | [EDITADO] | Adicionada, ao final do terceiro motivo na Seção 6, referência explícita à tabela de Tipo A no repositório: "A lista completa desses casos está no arquivo `auditoria-quantitativa-l1.md` do repositório, coluna 'Tipo A com nota de rodapé', atualizada a cada revisão do manuscrito." — tornando a declaração verificável em vez de autocertificação. |

---

## APX-O — Caderno de Governança de IA
**Arquivo:** `04-apendices/L1-APX-O-caderno-governanca-v1.md`

| Achado | Status | Descrição da ação |
|---|---|---|
| O/04 | [EDITADO] | Adicionada nota de alinhamento com APX-N imediatamente antes do "Quadro de navegação", explicitando que a estrutura de camadas do quadro materializa o Tipo C (padrão durável no livro) e o Tipo A (número datado no repositório/APX-J) da taxonomia do Apêndice N. |
| O/05 | [EDITADO] | 2ª e 3ª citações do URL do repositório substituídas por referências internas: na seção "Versão executável", URL substituído por "`governance/v1` (URL na abertura deste apêndice)"; no rodapé, substituído por "`governance/v1` no repositório acompanhante". A 1ª citação (na abertura do apêndice, onde o URL é necessário para o leitor chegar ao artefato) foi mantida. |

---

## APX-Q — Manual do Professor
**Arquivo:** `04-apendices/L1-APX-Q-manual-do-professor.md`

| Achado | Status | Descrição da ação |
|---|---|---|
| Q/05 | [EDITADO] | Adicionada coluna "Status do gabarito" na tabela da Seção 8.1 (banco de 20 exercícios). Cada linha recebeu status: "Disponível — APX-K (capítulo)" para os exercícios com gabarito no APX-K, e "Em construção — repositório `/teaching/exercises/aula-XX.md`" para os pendentes. Professor adotante agora sabe exatamente o que está pronto e o que está prometido. |
| Q/06 | [EDITADO] | Critério de excelência da dimensão "Profundidade Técnica" na rubrica da Seção 7 ampliado: adicionada alternativa "ou de busca própria do estudante" e nota parentética protegendo o professor caso o APX-G esteja parcialmente disponível na edição em uso. |

---

## Totais por apêndice

| Apêndice | Editados | Já Resolvidos | Deferidos |
|---|---|---|---|
| APX-J | 1 | 0 | 1 |
| APX-K | 0 | 1 | 0 |
| APX-M | 2 | 0 | 0 |
| APX-N | 2 | 0 | 0 |
| APX-O | 2 | 0 | 0 |
| APX-Q | 2 | 0 | 0 |
| **Total** | **9** | **1** | **1** |

---

# Changelog Onda 4 — APX-L e APX-P

Data: 2026-06-16
Passa: ACABAMENTO (P2)
Arquivos editados:
- `04-apendices/L1-APX-L-biblioteca-prompts.md`
- `04-apendices/L1-APX-P-boxes-tecnicos.md`

---

## APX-L — Biblioteca de Prompts Profissionais

### Achado 12 [EDITADO] — P2
**Problema:** "Princípio Três, a Camada Dupla" sem referência ao capítulo onde é definido.
**Localização:** Seção "Por que este apêndice existe em duas camadas", terceiro parágrafo.
**Antes:** `...e materializa o Princípio Três, a Camada Dupla.`
**Depois:** `...e materializa o Princípio Três, a Camada Dupla (definido no capítulo de abertura "Os Nove Invariantes").`
**Decisão:** Referência cirúrgica ao capítulo real, sem número de capítulo pois o manifesto precede a numeração ordinária.

### Achado 13 [OBSOLETO] — P2
**Problema:** URL de repositório longa — inacessível em formato impresso.
**Status:** O apêndice foi completamente reescrito na Onda 2 e não contém mais fichas individuais com campo "Versão executável". O índice atual usa identificadores curtos `/prompts/P-LEG-01` etc. em tabela compacta. O problema reportado pela banca não existe na versão atual.

### Achado 14 [OBSOLETO] — P2
**Problema:** P-MKT-01 menciona canais com limites de caracteres que mudam.
**Status:** O apêndice atual não tem fichas expandidas. P-MKT-01 existe apenas como linha de índice na tabela final, sem corpo de ficha que pudesse conter texto sobre canais específicos. O conteúdo expandido vive no repositório (fora do livro). Problema inexistente na versão atual.

---

## APX-P — Boxes Técnicos

### Achado 08 [EDITADO] — P2
**Problema:** Box 6 (Quantização e Destilação) cita Phi-3 e Gemini Nano como exemplos de destilação sem mencionar DeepSeek-R1-Distill, caso mais relevante em 2025-2026.
**Localização:** Mecanismo técnico do Box 6, parágrafo sobre destilação clássica.
**Antes:** `Modelos como Phi-3, da Microsoft, e Gemini Nano são exemplos públicos de modelos pequenos treinados com destilação intensiva a partir de modelos maiores, atingindo qualidade impressionante para seu tamanho.`
**Depois:** `Modelos como Phi-3, da Microsoft, Gemini Nano e a família DeepSeek-R1-Distill são exemplos públicos de modelos pequenos treinados com destilação intensiva a partir de modelos maiores, atingindo qualidade impressionante para seu tamanho — em particular em tarefas de raciocínio estruturado, caso em que DeepSeek-R1-Distill demonstrou capacidade próxima a modelos frontier em variantes de sete bilhões de parâmetros.`
**Decisão:** Adição cirúrgica na sentença existente. Não adicionada referência bibliográfica específica ao DeepSeek-R1 (paper DeepSeek-AI, 2025 — arxiv.org/abs/2501.12948) pois o Box 6 já tem quatro referências e a menção no corpo basta para orientar o leitor técnico.

### Achado 09 [EDITADO] — P2
**Problema:** A epígrafe final ("Cada um destes boxes existe porque...") é o conteúdo mais memorável do apêndice e estava enterrada após o Box 11.
**Localização:** Movida de após o `---` final para o início da seção "Como usar este apêndice".
**Operação:** Epígrafe inserida como blockquote itálico imediatamente após o título da seção, antes do primeiro parágrafo do corpo. Versão original ao final do arquivo removida.
**Decisão:** A frase âncora o enquadramento antes de o leitor entrar nos boxes — exatamente o efeito que a banca recomendou.

### Achado 10 [EDITADO] — P2
**Problema:** Mapa de boxes referencia os Princípios (P1 a P9) sem indicar onde estão definidos; leitor que chega diretamente ao Apêndice P não sabe onde encontrá-los.
**Localização:** Tabela "Mapa de boxes", imediatamente após a linha do Box 11.
**Adição:** Nota de rodapé em blockquote após a tabela: `Nota: os Princípios (P1 a P9) são definidos no capítulo de abertura "Os Nove Invariantes da Inteligência Artificial". Verbetes rápidos em ordem alfabética estão no Apêndice A — Glossário.`
**Decisão:** Referência dupla (manifesto + glossário) cobre tanto o leitor que quer a definição completa quanto o que precisa de consulta rápida.

---

## Sumário por apêndice

| Apêndice | Editados | Já resolvidos | Obsoletos | Deferidos |
|---|---|---|---|---|
| APX-L | 1 | 0 | 2 | 0 |
| APX-P | 3 | 0 | 0 | 0 |
| **Total** | **4** | **0** | **2** | **0** |
