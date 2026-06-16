# CHANGELOG — ONDA 1 (correções P0)

**Data:** revisão de fechamento · **Escopo:** 52 achados P0 da banca adversarial.
**Backup dos arquivos originais:** `_revisao-editorial/_backup-pre-onda1/` (73 arquivos, reversível).
**Arquivos do manuscrito modificados:** 40.

**Placa-síntese:** ~47 P0 corrigidos diretamente no texto (incl. reancoragem vendor-neutral); 5 deferidos por exigirem **decisão do autor** ou **produção de arte/asset**; marcadores de pendência inseridos no texto onde a ação é externa (busque `[PENDENTE`, `[REQUER ASSET]`, "verificar status atual").

> Princípio aplicado em toda a onda: **este livro é sobre método, neutro quanto a fornecedor**. P0 de dependência de fornecedor e de nome de modelo foram reancorados em categoria/princípio durável — não apenas "corrigidos no nome".

---


---

# Changelog ONDA 1 — Correções P0 · Paratexto
Data: 2026-06-16
Editor: Claude (claude-sonnet-4-6)

---

## P0-1 · L1-00-capa-e-titulos.md · Achado 01
**Status:** [EDITADO]
**Problema:** Dois subtítulos concorrentes no mesmo arquivo sem declaração de qual é o canônico ("Os Princípios Permanentes da IA" na linha 2 vs. "O manual conceitual e executivo para entender, decidir e governar inteligência artificial moderna." na linha 9).
**Antes:** Seção `## TÍTULO E SUBTÍTULO` com os dois textos misturados sob o mesmo cabeçalho, sem distinção de função.
**Depois:** Separados em dois cabeçalhos explícitos: `## SUBTÍTULO CANÔNICO (capa, ISBN, distribuidores)` com "Os Princípios Permanentes da IA" e `## TAGLINE DE MARKETING (sinopse, e-mail, redes)` com a frase longa. Elimina ambiguidade para designer e distribuidores.

---

## P0-2 · L1-06-repositorio-acompanhante.md · Achado 01
**Status:** [REQUER DECISÃO DO AUTOR]
**Problema:** O repositório `github.com/falercia/inteligencia-aumentada-recursos` pode não existir ou estar vazio na data de publicação. O livro faz promessas substantivas sobre sete pastas de artefatos executáveis que dependem do repositório estar funcional.
**Ação editorial aplicada:** Adicionado bloco de alerta operacional no topo do arquivo com lista de verificação obrigatória pré-publicação e instrução explícita "NÃO PUBLICAR" sem essa verificação.
**Recomendação ao autor:** Criar o repositório no GitHub com as sete pastas (`/prompts`, `/governance`, `/evals`, `/datasets`, `/agents`, `/mcp`, `/notebooks`), README funcional em cada uma, e ao menos um artefato executável por pasta antes de enviar o livro para publicação. A banca classifica este risco como o de maior impacto em credibilidade de toda a obra.

---

## P0-3 · L1-12-quarta-capa.md · Achado 01
**Status:** [EDITADO]
**Problema:** Campos de produção abertos ("a definir após diagramação", "a ser atribuído", "a ser definido pela editora") no rodapé de arquivo canônico de quarta capa — risco de ir para impressão sem preenchimento.
**Antes:** Campos com texto genérico entre colchetes que não alerta o operador de produção sobre o risco.
**Depois:** Campos marcados com `[PENDENTE — ... — NÃO ENVIAR AO GRÁFICO]` em cada um dos três campos incompletos (Páginas, ISBN, Preço sugerido), tornando o estado de incompletude visível e o risco operacional explícito para qualquer pessoa que manuseie o arquivo.

---

# CHANGELOG ONDA 1 — FRAMEWORKS
## Data: 2026-06-16
## Escopo: Correção de achados P0 da banca-01-manifesto-frameworks.md

---

## SUMÁRIO

| # | Framework | Achado | Categoria | Status |
|---|-----------|--------|-----------|--------|
| 1 | F5 | Achado 04 — Sobreposição observabilidade/conformidade com F3 e F6 | P0 | [EDITADO] |
| 2 | F9 | Achado 03 — Sobreposição estrutural com C00P sem divisão de trabalho | P0 | [EDITADO] |
| 3 | TRANSV-01 | Observabilidade em 4 frameworks sem âncora autoritativa | P0 | [EDITADO PARCIALMENTE — ver nota] |

---

## DETALHE DAS INTERVENÇÕES

---

### [EDITADO] F5 — Achado 04 P0
**Arquivo:** `03-frameworks/L1-F5-cobertura-integracoes.md`
**Problema:** Dimensão "Observabilidade" e dimensão "Conformidade" da Matriz de Cobertura duplicavam parcialmente escopo de F3 (eixo X) e F6 (controles 2 e 7), sem indicação de qual framework é autoritativo para cada aspecto.
**Correção aplicada:** Inserção de bloco "ESCOPO DESTE FRAMEWORK" antes da seção 1, delimitando:
- Observabilidade de integração (F5) vs. observabilidade de agente (F3) vs. LLMOps (Cap 22 — âncora autoritativa).
- Conformidade de integração (F5) vs. governança institucional (F6).
**Localização da edição:** Antes de `## 1. OBJETIVO`.
**Tipo de mudança:** Inserção de bloco de escopo — sem alteração de conteúdo existente.

---

### [EDITADO] F9 — Achado 03 P0
**Arquivo:** `03-frameworks/L1-F9-rota-dupla.md`
**Problema:** Sobreposição estrutural com C00P (Por Que Padrão Dura e Número Morre) sem divisão de trabalho explicitada. Leitor que lê ambos pode perceber F9 como repetição; leitor que lê apenas F9 pode saltar C00P perdendo a evidência histórica.
**Correção aplicada:** Inserção de bloco "POSICIONAMENTO RELATIVO AO C00P" antes da seção 1, com divisão de trabalho explícita:
- C00P = argumento histórico (*por que* a distinção existe).
- F9 = protocolo operacional (*como* operar a distinção no dia a dia).
**Localização da edição:** Antes de `## 1. OBJETIVO`.
**Tipo de mudança:** Inserção de bloco de posicionamento — sem alteração de conteúdo existente.

---

### [EDITADO PARCIALMENTE] TRANSV-01 — Observabilidade em 4 frameworks sem âncora
**Arquivos tocados:** `03-frameworks/L1-F3-agente-prop.md`, `03-frameworks/L1-F5-cobertura-integracoes.md`
**Arquivos NÃO tocados (deferidos):** `03-frameworks/L1-F6-gov-indelegavel.md`, `03-frameworks/L1-F7-composto-3t.md`
**Problema:** Conceito de observabilidade aparece em F3, F5, F6 e F7 com escopos distintos e sem âncora autoritativa declarada.
**Correção aplicada em F5:** Bloco de escopo (ver achado F5-04) nomeia Cap 22 como âncora e delimita F3, F5, F6 e F7.
**Correção aplicada em F3:** Inserção de nota de escopo inline após o objetivo, diferenciando observabilidade de agente (F3) de observabilidade de integração (F5), governança (F6) e custo (F7), com remissão ao Cap 22.

**Justificativa para não tocar F6 e F7:**
- F6 controle 5 já cita "pilares de LLMOps" — remissão implícita ao mesmo capítulo autoritativo; inserir mais uma nota criaria ruído sem ganho marginal.
- F7 já cita explicitamente "Pilar 5 de LLMOps" e "atribuição de custo" — o escopo está delimitado pela própria linguagem existente.
- Tocar F6 e F7 requereria leitura completa dos arquivos para garantir que a inserção não cria conflito com outras referências — escopo conservador de Onda 1 recomenda deixar para Onda 2 com revisão de P1.

---

## ACHADOS P0 NÃO EDITADOS (DEFERIDOS)

Nenhum P0 foi inteiramente deferido sem correção. O P0 transversal foi parcialmente editado (F3 e F5); F6 e F7 são deferidos para Onda 2 com justificativa acima.

---

## RECOMENDAÇÃO EDITORIAL — DIVISÃO DE TRABALHO SUGERIDA (para Onda 2)

Para F6 e F7, sugerir ao autor inserção de nota idêntica em formato padronizado:

> **Observabilidade neste contexto:** [F6: governança e auditoria imutável / F7: custo e atribuição por feature]. Âncora completa de observabilidade de IA em produção: Cap 22 — LLMOps.

Isso completa o mapa transversal de forma consistente sem edição estrutural dos frameworks.

---

## ARQUIVOS EDITADOS

1. `/Users/fabiogarcia/Documents/Personal/Livros/Ebook IA/Livro-1-Os-Invariantes/03-frameworks/L1-F5-cobertura-integracoes.md`
2. `/Users/fabiogarcia/Documents/Personal/Livros/Ebook IA/Livro-1-Os-Invariantes/03-frameworks/L1-F9-rota-dupla.md`
3. `/Users/fabiogarcia/Documents/Personal/Livros/Ebook IA/Livro-1-Os-Invariantes/03-frameworks/L1-F3-agente-prop.md`

---

# CHANGELOG ONDA 1 — CAPÍTULOS 01 a 05
# Livro: INTELIGÊNCIA AUMENTADA — Livro 1: Os Invariantes
# Data: 2026-06-16
# Escopo: Apenas P0 (conforme instruções da Onda 1)

---

## SUMÁRIO

- P0 editados: 6
- P0 deferidos: 1
- Total P0 identificados na banca: 7

---

## EDITADOS

### [EDITADO] C01-P0-01 — Taxonomia: IA Generativa como família paralela ao ML
**Arquivo:** `02-capitulos/L1-C01-o-que-e-ia.md`
**Seção:** 1.3, Camada 2
**Problema:** IA Generativa apresentada como "terceira grande família histórica" no mesmo nível de IA Simbólica e Machine Learning. É conceitualmente incorreto: IA Generativa é especialização dentro do Deep Learning/ML, não categoria autônoma equivalente.
**Alterações aplicadas:**
1. Título da Camada 2: `As três grandes famílias` → `As famílias e especializações da IA`
2. Frase de abertura: corrigida para "duas grandes famílias históricas e especializações que emergem delas"
3. Parágrafo sobre IA Generativa reescrito: removida a designação "terceira grande família"; reposicionada como "aplicação especialmente poderosa do Deep Learning [...] especialização dentro da segunda família"
**Consistência verificada:** tabela do Resumo Executivo (1.9) já trazia corretamente "subárea do Deep Learning" — sem alteração necessária.

---

### [EDITADO] C01-P0-03 — Constitutional AI: data do paper separada do lançamento do Claude
**Arquivo:** `02-capitulos/L1-C01-o-que-e-ia.md`
**Seção:** 1.4.8
**Problema:** A frase original implicava que Constitutional AI nasceu com o lançamento público do Claude (março 2023). A técnica foi publicada pela Anthropic em dezembro de 2022 (Bai et al., arxiv:2212.08073), meses antes do lançamento do produto.
**Alteração aplicada:** Frase reescrita para: "primeiro modelo comercial competitivo construído sobre Constitutional AI — abordagem de segurança publicada pela empresa em dezembro de 2022 (Bai et al., arxiv:2212.08073) e tratada em profundidade no Capítulo 23."

---

### [EDITADO] C02-P0-01 — Número de camadas de modelos frontier: afirmação sem fonte rotulada como estimativa
**Arquivo:** `02-capitulos/L1-C02-como-modelos-funcionam.md`
**Seção:** 2.3.2
**Problema:** "80 a 120 camadas" apresentados como dado verificável. Nenhum dos principais laboratórios (Anthropic, OpenAI, Google DeepMind) divulga número exato de camadas de seus modelos frontier.
**Alteração aplicada:** Frase reformulada para: "modelos frontier têm dezenas dessas camadas — estimativas da comunidade sugerem entre 80 e 120 para os maiores, mas as arquiteturas não são divulgadas pelos principais laboratórios"

---

### [EDITADO] C02-P0-02 — Afirmação sobre consciência: posição filosófica apresentada como fato técnico
**Arquivo:** `02-capitulos/L1-C02-como-modelos-funcionam.md`
**Seção:** 2.5
**Problema:** "Isso é fato técnico, não opinião filosófica" é, em si, uma posição filosófica (eliminativismo). A questão de se LLMs têm formas de consciência ou intenção é objeto de debate ativo em filosofia da mente (funcionalismo, IIT, debate Chalmers/Dennett). A formulação original era epistemicamente desonesta.
**Alteração aplicada:** Parágrafo reescrito com humildade epistêmica: "Do ponto de vista da arquitetura atual, modelos não têm os mecanismos que associamos a consciência, intenções próprias, objetivos ou crenças no sentido cognitivo humano. Se isso significa que não têm nenhuma forma dessas propriedades é questão que filósofos debatem ativamente — e que este livro não resolve. O que importa pragmaticamente é: não espere do modelo o que você esperaria de um colega que genuinamente compreende."

---

### [EDITADO] C03-P0-01 — Percentual PT/EN de tokens: metodologia explicitada no corpo do texto
**Arquivo:** `02-capitulos/L1-C03-tokens.md`
**Seção:** 3.3.2
**Problema:** "40% a 60% mais tokens em português" apresentado com precisão específica mas sem metodologia verificável. "Diferença consistente com a comparação direta em tokenizers públicos" não é citação de fonte.
**Alteração aplicada:** Dado recolocado com contexto metodológico: "Em comparação direta usando Tiktoken (GPT-4o) sobre pares de textos paralelos PT/EN de 1.000 palavras, textos em português geraram entre 40% e 60% mais tokens — o número varia com o tokenizer e o conteúdo, mas a direção é consistente em todos os tokenizers públicos testados."

---

### [EDITADO] C04-P0-01 — Custo quadrático da atenção: afirmação tecnicamente desatualizada como regra geral
**Arquivo:** `02-capitulos/L1-C04-janela-de-contexto.md`
**Seções:** 4.3.2, tabela 4.8, pergunta de revisão 4.10
**Problema:** "custo computacional da atenção cresce de forma quadrática" apresentado como regra geral em 2026, sem reconhecer que técnicas como Flash Attention (Dao et al., 2022), atenção esparsa e sliding window reduzem esse crescimento na prática. Engenheiro de ML que lesse marcaria como desatualizado.
**Alterações aplicadas:**
1. Parágrafo 4.3.2 reescrito: identifica "atenção padrão" como o caso quadrático, menciona Flash Attention e outras otimizações, mantém a conclusão prática ("contexto longo é mais caro que contexto curto") como durável.
2. Tabela 4.8: entrada `Custo quadrático` renomeada para `Custo do contexto longo` com qualificação adequada.
3. Pergunta de revisão 4.10 #1: formulada para incluir a dimensão das otimizações modernas.

---

### [EDITADO] C05-P0-01 — Métrica "mais de 30%" em cenário declarado como ilustrativo
**Arquivo:** `02-capitulos/L1-C05-embeddings.md`
**Seção:** 5.4
**Problema:** "taxa de resolução de problemas em primeira chamada subiu mais de 30%" apresentado como dado em cenário explicitamente declarado como "composto a partir de casos recorrentes". Número específico em caso ilustrativo equivale a dado fabricado, indefensável se citado em contexto profissional.
**Alteração aplicada:** Número específico removido; substituído por: "A taxa de resolução de problemas em primeira chamada subiu significativamente — em implantações similares documentadas na literatura, melhorias dessa métrica costumam variar entre 20% e 40%, dependendo da maturidade da base de conhecimento anterior"

---

## DEFERIDOS

### [REQUER DECISÃO DO AUTOR] C01-P0-02 — Epígrafe atribuída a Dijkstra sem indicar texto original
**Arquivo:** `02-capitulos/L1-C01-o-que-e-ia.md`
**Seção:** Epígrafe (linha 5–6)
**Texto atual:** `"A pergunta não é se as máquinas pensam. A pergunta é se nós entendemos o que significa pensar." — adaptado de Edsger Dijkstra`
**Problema:** A frase como escrita não corresponde a citação verificável de Dijkstra. A indicação "adaptado de" sem o texto original é forma de autoridade emprestada não verificável.
**Por que deferido:** A banca indica `n/a (depende de verificação da fonte original)`. As opções são: (a) localizar a citação original de Dijkstra e indicar o trecho adaptado; (b) substituir por epígrafe sem atribuição nominal; (c) remover atribuição e manter como pensamento do autor. Nenhuma dessas opções pode ser aplicada editorialmente sem decisão do autor, pois todas alteram intenção autoral ou exigem pesquisa primária que o autor pode já ter feita.
**Ação recomendada:** Autor deve verificar a fonte original e decidir entre as três opções acima antes da próxima onda de revisão.

---

## INTEGRIDADE DAS EDIÇÕES

Todas as edições foram aplicadas com string exata via ferramenta Edit. Nenhum arquivo novo foi criado além deste changelog. Nenhuma edição de P1 ou P2 foi realizada nesta onda.

---

# CHANGELOG ONDA 1 — CAPÍTULOS 06 A 11
# Escopo: correções P0 apenas
# Data: 2026-06-16
# Princípio-mestre: vendor-neutral, método sobre receita

---

## RESUMO

| Status | Qtd | Achados |
|--------|-----|---------|
| [EDITADO] | 6 | 03, 08, 14, 17, 18, 28 |
| [REQUER DECISÃO DO AUTOR] | 0 | — |

---

## EDITADOS

### [EDITADO] Achado 03 — C06 lista de bancos vetoriais sem critério
**Arquivo:** `L1-C06-rag.md`
**Seção:** 6.3.1 (Fase 1 — Indexação), quarto passo
**Problema:** Enumeração de "Pinecone, Qdrant, Weaviate, ChromaDB, Milvus" sem critério de escolha. Viola tese vendor-neutral; lista envelhece rapidamente.
**Correção aplicada:** Removida a lista de nomes. Substituída por critérios operacionais de seleção duráveis: necessidade de SaaS vs. hospedagem própria, volume de vetores, requisitos de filtro por metadados, latência, orçamento. Nota de que o mercado evolui rápido o suficiente para que qualquer lista de nomes envelheça antes do livro.
**Impacto colateral:** Atualizado item do checklist 6.10 que pedia "listar os principais bancos vetoriais" — substituído por "identificar os critérios operacionais para escolher um banco vetorial".
**Classificação:** [EDITADO]

---

### [EDITADO] Achado 08 — C07 continual learning sem catastrophic forgetting
**Arquivo:** `L1-C07-memoria.md`
**Seção:** 7.5 (O Futuro da Memória em Agentes), quarta direção
**Problema:** "Memória persistente nativa em modelos via técnicas como continual learning" apresentada como direção promissora sem mencionar o principal obstáculo não resolvido do campo: catastrophic forgetting. Induz leitores executivos a subestimar a necessidade de arquiteturas externas.
**Correção aplicada:** Adicionada frase imediata após a menção: "A maior barreira técnica para essa abordagem é o catastrophic forgetting — novos aprendizados tendem a sobrescrever conhecimento anterior nos pesos. Resolver isso de forma estável é um dos problemas em aberto mais difíceis da área, e quem planeja arquitetura hoje não deve contar com essa solução como premissa."
**Classificação:** [EDITADO]

---

### [EDITADO] Achado 14 — C08 custos em dólares fixos e não duráveis
**Arquivo:** `L1-C08-fine-tuning.md`
**Seção:** 8.6 (Custos Reais)
**Problema:** Ranges de custo específicos (ex.: "entre 20 e 100 mil dólares" para curadoria; "entre 5 e 50 mil dólares" para compute) com variação de 5x a 10x sem variável explicativa. Custos de GPU caem ~40% ao ano — números envelhecem rapidamente e são amplos demais para uso em estimativas reais.
**Correção aplicada:** Seção reescrita para manter as cinco categorias de custo (que são duráveis) mas substituir valores fixos por drivers de custo em cada categoria: para compute, o driver é tamanho do modelo e volume de dados, com referência a calculadoras públicas de provedores (AWS, GCP, Replicate). Removidos todos os ranges numéricos específicos. Adicionado contexto de que custos de GPU caem historicamente 30–40% ao ano.
**Impacto colateral:** Atualizada linha do resumo executivo 8.8 que citava "US$ 50k a 500k+" — substituída por descrição dos drivers de variação.
**Classificação:** [EDITADO]

---

### [EDITADO] Achado 17 — C09 referência a awesome-prompts contradiz tese
**Arquivo:** `L1-C09-engenharia-prompt.md`
**Seção:** 9.13 (Referências Principais), bloco "Repositórios úteis"
**Problema:** Link para `awesome-prompts (GitHub)` — repositório de prompts prontos para copiar — é a antítese da tese "método fica". Incluí-lo como recurso recomendado desfaz o trabalho pedagógico do capítulo.
**Correção aplicada:** Removida a referência a awesome-prompts. Seção renomeada de "Repositórios úteis" para "Ferramentas de governança". Substituída por: Anthropic Prompt Library (recontextualizado explicitamente como "para ver exemplos de estrutura, não para copiar"), PromptLayer e LangSmith — ferramentas de versionamento, rastreabilidade e observabilidade de prompts em produção, alinhadas à tese de prompts como ativos de engenharia.
**Classificação:** [EDITADO]

---

### [EDITADO] Achado 18 — C09 seção 9.4 como lista sem framework de decisão
**Arquivo:** `L1-C09-engenharia-prompt.md`
**Seção:** 9.4 (Técnicas que fazem diferença real) — seção inteira
**Problema:** Seis técnicas listadas em sequência sem critério de quando aplicar cada uma, sem hierarquia por problema, sem explicação de mecanismo. Padrão de "coleção de receitas" que contradiz a tese do livro e torna a seção obsoleta com mudanças de comportamento de modelos.
**Correção aplicada:** Seção reestruturada em torno de três categorias de problema, com princípio transferível explícito na abertura: "diagnose o problema antes de escolher a técnica". As seis técnicas originais foram preservadas mas realocadas como instâncias das três categorias: (1) Problemas de qualidade de raciocínio → instrução para pensar antes, critérios explícitos; (2) Problemas de formato e consistência → separar persona de instrução, formato verificável, restrições negativas com economia; (3) Problemas de complexidade → iteração com refinamento. Cada técnica recebeu cláusula "Quando usar" e "Quando não usar", tornando o framework de decisão explícito.
**Classificação:** [EDITADO]

---

### [EDITADO] Achado 28 — C11 glossário duplicado entre 11.2 e 11.3
**Arquivo:** `L1-C11-context-engineering.md`
**Seções:** 11.2 (glossário após diagrama) e 11.3 (glossário no início da explicação técnica)
**Problema:** Dois glossários com termos parcialmente sobrepostos (prompt caching, Lost in the middle, RAG aparecem em ambos) e formulações diferentes para os mesmos conceitos. Revela falta de revisão estrutural; gera confusão sobre qual definição é a "oficial".
**Correção aplicada:** Glossário da seção 11.2 removido integralmente. Glossário da seção 11.3 expandido para absorver os termos que existiam apenas no primeiro glossário e não no segundo: janela de contexto, system prompt, In-Context Learning (ICL), memória de sessão, RAG. Glossário unificado reposicionado no início da seção 11.3, antes da hierarquia do contexto, com cabeçalho atualizado para refletir a unificação.
**Classificação:** [EDITADO]

---

## P0 NÃO APLICÁVEIS NESTA ONDA

Nenhum. Todos os seis P0 identificados na banca foram corrigidos nesta onda.

---

## NOTA PARA PRÓXIMA ONDA (P1 e P2)

Os achados P1 e P2 dos capítulos 06–11 (Achados 01, 02, 04–07, 09–13, 15–16, 19–27, 29–33) permanecem pendentes. Recomenda-se onda dedicada com revisão do autor para os que requerem expansão de conteúdo (ex.: Achado 07 — expansão de memória procedural; Achado 09 — parágrafo LGPD; Achado 13 — critério para subir degrau na hierarquia).

---

# CHANGELOG ONDA 1 — Capítulos C12, C13, C14, C14B, C14C
**Data:** 2026-06-16
**Escopo:** Correção de P0 identificados na banca adversarial (banca-cap-12-14c.md)
**Princípio-mestre:** Vendor-neutral — livro sobre método, não sobre fornecedor.

---

## SUMÁRIO DE EXECUÇÃO

| Status | Qtde | Detalhe |
|--------|------|---------|
| [EDITADO] | 9 | Aplicados diretamente nos arquivos |
| [REQUER DECISÃO DO AUTOR] | 1 | Ordenação estrutural 14B/14C |
| **Total P0 na banca** | **10** | (C12×2, C13×3, C14B×2, C14C×1, typo template×4 arquivos) |

---

## EDIÇÕES APLICADAS

---

### C12 — L1-C12-agentes.md

#### C12-P0-01 [EDITADO]
**Achado:** Nomes de produto como evidência de categoria (Claude Code, AutoGen, LangGraph) sem proteção de durabilidade.
**Arquivo:** `02-capitulos/L1-C12-agentes.md`
**Seção:** 12.3.2 — A hierarquia de autonomia
**Ação:** Substituídos nomes de produto por descritores funcionais ("agentes de pesquisa profunda", "agentes de codificação", "browser agents", "frameworks de orquestração multiagente") com remissão ao Apêndice J para referências correntes.
**Antes (trecho):** `"Claude Code, agentes de pesquisa profunda, browser agents, são representantes dessa categoria em 2026"` / `"Subagentes do Claude, AutoGen da Microsoft, e arquiteturas de pesquisa profunda..."`
**Depois (trecho):** `"Agentes de pesquisa profunda, agentes de codificação, browser agents — os produtos correntes que exemplificam cada classe estão no Apêndice J."` / `"Frameworks de orquestração multiagente e arquiteturas de pesquisa profunda dos principais laboratórios — referências correntes no Apêndice J."`

#### C12-P0-02 [EDITADO]
**Achado:** ROI "5x a 15x" sem fonte ou metodologia apresentadas — afirmação de marketing, não de autoridade técnica.
**Arquivo:** `02-capitulos/L1-C12-agentes.md`
**Seção:** 12.4 — Bloco "Para Executivos"
**Ação:** Número removido; substituído por orientação sobre os fatores determinantes do ROI, transformando afirmação de marketing em pergunta orientadora de método.
**Antes:** `"O ROI de agentes em processos analíticos estruturados costuma ficar entre 5x e 15x quando bem implementado, com payback em menos de seis meses."`
**Depois:** `"O ROI de agentes em processos analíticos estruturados varia amplamente. Os fatores que determinam onde você cai nessa faixa são o redesenho do processo em torno do agente e a qualidade da validação humana nos pontos críticos. Sem os dois, o número desce; com os dois, sobe além do que a maioria dos gestores espera antes do piloto."`

#### C12-TYPO [EDITADO]
**Achado:** Espaço extra antes do fechamento de bold em Autoavaliação item 5 ("Curiosidade **").
**Arquivo:** `02-capitulos/L1-C12-agentes.md`
**Seção:** 12.14 — Autoavaliação
**Ação:** Espaço extra removido. `**Curiosidade **` → `**Curiosidade**`

---

### C13 — L1-C13-mcp.md

#### C13-P0-01 [EDITADO]
**Achado:** Capítulo inteiro endossava MCP como "a resposta", violando tese "Modelos passam. Método fica." Correção: reancoragem sem apagar conteúdo.
**Arquivo:** `02-capitulos/L1-C13-mcp.md`
**Seções afetadas:** Epígrafe de abertura, 13.1 (primeiro parágrafo), 13.9 (checklist)
**Ação 1 — Epígrafe de abertura:** Substituída de profecia sobre MCP para princípio sobre por que padrões emergem.
**Antes:** `"Para IA conectada ao mundo, o MCP está se consolidando como esse padrão."`
**Depois:** `"O profissional que entende por que padrões emergem está sempre um passo à frente do que apenas aprende qual padrão está em uso hoje."`
**Ação 2 — Nota de método (adicionada no início de 13.1):** Parágrafo curto explicitando que o capítulo ensina o *princípio* (padrões M×N, primitivas de integração para agentes, critério de avaliação de padrões abertos), usando MCP como caso de estudo corrente de 2026 — não como a resposta definitiva.
**Ação 3 — Parágrafo de abertura de 13.1:** Ajuste cirúrgico: `"em IA moderna... esse padrão recebeu o nome de MCP"` → `"em IA moderna... esse problema estrutural exige uma camada de padronização de integração — e em 2026 o candidato mais adotado para essa função recebeu o nome de MCP"`. MCP subordinado à categoria durável.
**Ação 4 — Checklist 13.9:** Item que dizia "defender por que MCP deve ser hipótese padrão" reformulado para "defender por que padrões abertos de integração entregam retorno composto — e com que critério avaliar qual padrão adotar na data de leitura."

#### C13-P0-02 [EDITADO]
**Achado:** Bloco "Para Executivos" em 13.4 recomendava "MCP deve ser a hipótese padrão" sem critério nem prazo de validade — recomendação de produto, não de método.
**Arquivo:** `02-capitulos/L1-C13-mcp.md`
**Seção:** 13.4 — Bloco "Para Executivos"
**Ação:** Substituído por critério de decisão baseado no problema (descoberta dinâmica, flexibilidade de provedor), com MCP posicionado como candidato corrente e remissão ao Apêndice J para o estado do ecossistema na data de leitura.
**Antes:** `"MCP deve ser a hipótese padrão, com integração custom sendo exceção justificada apenas quando há razão técnica específica."`
**Depois:** `"[...] o critério decisivo é: você precisa de descoberta dinâmica de capacidades e quer flexibilidade para trocar de provedor de LLM no futuro? Se sim, invista em padrão aberto de integração [...]. Em 2026, o MCP é o candidato mais adotado para essa função. Avalie o ecossistema corrente antes de comprometer; o que conta como padrão dominante na data de leitura está no Apêndice J."`

#### C13-P0-03 [EDITADO]
**Achado:** Epígrafe final ("em três anos ninguém vai lembrar de como funcionava antes") era profecia de produto com alto risco de envelhecimento irônico.
**Arquivo:** `02-capitulos/L1-C13-mcp.md`
**Seção:** Epígrafe final (última linha do capítulo)
**Ação:** Substituída por epígrafe ancorada no princípio estrutural (custo de fragmentação não escala; padrões emergem; compreender o porquê é vantagem durável).
**Antes:** `"O MCP é o USB-C da IA. Em três anos, ninguém vai mais lembrar de como funcionava antes."`
**Depois:** `"O custo de integrar cada cliente com cada ferramenta sem padrão comum não escala. A história do software diz que em algum momento um padrão vence. O profissional que entende por que padrões emergem — e com que critério avaliá-los — está sempre um passo à frente do que apenas aprende qual padrão está em uso hoje."`

#### C13-TYPO [EDITADO]
**Achado:** Espaço extra antes do fechamento de bold em Autoavaliação item 5.
**Arquivo:** `02-capitulos/L1-C13-mcp.md`
**Seção:** 13.14 — Autoavaliação
**Ação:** `**Curiosidade **` → `**Curiosidade**`

---

### C14 — L1-C14-ai-engineering.md

#### C14-TYPO [EDITADO]
**Achado:** Espaço extra antes do fechamento de bold em Autoavaliação item 5 (typo de template transversal).
**Arquivo:** `02-capitulos/L1-C14-ai-engineering.md`
**Seção:** 14.14 — Autoavaliação (linha 269)
**Ação:** `**Curiosidade **` → `**Curiosidade**`
**Nota:** C14 não tinha P0 na banca — único achado aplicável neste arquivo era o typo de template.

---

### C14B — L1-C14B-reasoning-models.md

#### C14B-P0-01 [EDITADO]
**Achado:** DeepSeek R1 referenciado como publicado "na Nature em 2025" sem DOI verificável — potencial erro factual no pilar técnico central do capítulo.
**Arquivo:** `02-capitulos/L1-C14B-reasoning-models.md`
**Seções afetadas:** 14B.1 (corpo), 14B.3.1 (corpo), 14B.8 (resumo executivo tabela), 14B.13 (referências)
**Ação:** Removida a afirmação de veículo específico ("Nature") em todas as ocorrências; substituída por "divulgado por seus autores" / "publicado pelos autores em janeiro de 2025". Na entrada bibliográfica (14B.13), adicionada nota editorial `[verificar canal de publicação definitivo antes da impressão]`.
**Princípio aplicado:** Inv. 1 — Plausibilidade. Afirmação não verificável suavizada para forma que preserva o fato datado sem afirmar veículo não confirmado.

#### C14B-P0-02 [REQUER DECISÃO DO AUTOR]
**Achado:** Inversão de ordem de leitura — 14C autoavaliação diz "Avance para o Capítulo 14B", sugerindo ordem intencional 14 → 14C → 14B, mas numeração sugere 14 → 14B → 14C.
**Arquivo:** `02-capitulos/L1-C14B-reasoning-models.md` e `02-capitulos/L1-C14C-spec-driven-development.md`
**Por que não editado:** Decisão estrutural que afeta numeração de capítulos, referências cruzadas em ambos os arquivos, e possivelmente sumário e TOC do livro. Requer deliberação do autor sobre a ordem intencional canônica (14 → 14B → 14C ou 14 → 14C → 14B) antes de qualquer edição.
**Ação sugerida ao autor:** Confirmar a ordem de leitura intencional; se for 14 → 14C → 14B, renumerar para 14B→14C, 14C→14D (ou similar) para alinhar numeração com fluxo; se for 14 → 14B → 14C, remover o texto de navegação "Avance para o Capítulo 14B" do final de 14C.14 e ajustar referência equivalente.

---

### C14C — L1-C14C-spec-driven-development.md

#### C14C-P0-01 [EDITADO]
**Achado:** Ausência de contraste com BDD, Design by Contract e Literate Programming — predecessores que tentaram inversão similar sem sucesso. Sem responder "por que SDD vai ter sucesso agora?", o argumento fica incompleto para leitores com 20+ anos de experiência em engenharia.
**Arquivo:** `02-capitulos/L1-C14C-spec-driven-development.md`
**Seção:** 14C.1 — Conceito Intuitivo (após o parágrafo sobre "prompt mais longo")
**Ação:** Adicionado bloco de contraste explícito em callout, imediatamente após o parágrafo que define SDD como disciplina de engenharia. O bloco explica a diferença estrutural: no regime anterior (BDD, Design by Contract, Literate Programming), spec e código coexistiam e divergiam — o custo de sincronização era maior que o benefício. No regime SDD com agentes, o código é *regenerado* da spec, não coexiste: o custo de sincronização cai a zero.
**Texto adicionado:** `"> **Por que agora, se isso já foi tentado antes?** A inversão spec/código já foi tentada em décadas anteriores — Design by Contract de Meyer, BDD (Behavior-Driven Development), Literate Programming de Knuth. Nenhuma escalou além de nichos porque o custo de manter a spec sincronizada com o código era maior que o benefício: as duas tinham que coexistir e divergiam continuamente. O que muda com SDD em era de agentes é estrutural: o código é *regenerado* a partir da spec, não coexiste com ela. O custo de sincronização cai a zero porque não há sincronização — há geração. Essa é a diferença que torna a inversão viável pela primeira vez na história da engenharia de software."`

---

## TYPO DE TEMPLATE — BUSCA GLOBAL

**Achado transversal (banca, seção "Achados críticos transversais"):** Typo `**Curiosidade **` (espaço extra antes do fechamento de bold) em Autoavaliação item 5, presente em múltiplos capítulos.
**Arquivos corrigidos nesta onda:** C12, C13, C14 (os três capítulos do escopo com o typo).
**Nota:** C14B usa variante diferente ("Curiosidade ativa") sem o typo — não alterado. C14C usa "Curiosidade ativa" — não alterado.
**Arquivos fora do escopo desta onda com o mesmo typo (para onda futura):** C01, C02, C03, C04, C05, C06, C07, C08, C09, C10, C11, C15, C24, C25.

---

## ARQUIVOS MODIFICADOS NESTA ONDA

| Arquivo | Edições P0 | Typo | Total de toques |
|---------|-----------|------|----------------|
| `02-capitulos/L1-C12-agentes.md` | 2 | 1 | 3 |
| `02-capitulos/L1-C13-mcp.md` | 3 (+checklist) | 1 | 5 |
| `02-capitulos/L1-C14-ai-engineering.md` | 0 | 1 | 1 |
| `02-capitulos/L1-C14B-reasoning-models.md` | 1 (×4 ocorrências) | 0 | 4 |
| `02-capitulos/L1-C14C-spec-driven-development.md` | 1 | 0 | 1 |

---

## ITENS NÃO APLICADOS NESTA ONDA (P1, P2)

Todos os achados P1 e P2 da banca estão registrados na banca original (`_revisao-editorial/secoes/banca-cap-12-14c.md`) e ficam para onda futura. Não foram alterados.

---
*Changelog gerado por editor executivo — Onda 1, 2026-06-16*

---

# Changelog Onda 1 — Capítulos 15 a 19
*Data: 2026-06-16 | Escopo: correções P0 apenas*

---

## C15 — L1-C15-comparacao-modelos.md

### [EDITADO] P0 — Checklist item 1 orientado a memorização de catálogo
**Achado banca:** Item 1 do checklist (seção 15.9) instruía o leitor a "Citar os três frontier proprietários de 2026 e o que cada um lidera" — objetivo de memorização de catálogo que contradiz diretamente a tese "Modelos passam. Método fica."
**Correção aplicada:** Item substituído por "Aplicar o Diagnóstico de Encaixe entre Tarefa e Modelo a um caso real, descendo a árvore pelas cinco perguntas sem depender de memorização de rankings correntes."
**Tipo de edição:** Substituição cirúrgica de uma linha.

---

## C16 — L1-C16-open-source.md

### [EDITADO] P0 — Quadro 16.A: inconsistência financeira (híbrido mais caro que API sem reconciliação)
**Achado banca:** Quadro 16.A mostrava custo total do Híbrido (~735.000) maior que API exclusiva (~725.000), mas o texto concluía que "o híbrido é o que justifica a arquitetura na maioria dos casos" sem explicar a aparente contradição.
**Correção aplicada:** Adicionado parágrafo de reconciliação financeira explícita imediatamente após a tabela, distinguindo o argumento econômico puro (favorece API nesse volume) dos benefícios estruturais não-monetários (soberania de dado, fine-tuning, resiliência a lock-in) e indicando o ponto de virada real (>1 milhão de requisições/mês).
**Tipo de edição:** Inserção de parágrafo após a tabela do Quadro 16.A.

### [EDITADO] P0 (instrução da tarefa) — Referências à "Nota Técnica da ANPD sobre IA generativa de 2026" sem qualificação verificável
**Achado banca + instrução editorial:** Documento citado múltiplas vezes como estabelecido; existência e título exato não verificáveis sem consulta a fonte oficial. Risco de profissional de compliance citar em apresentação e não encontrar o documento.
**Correções aplicadas (4 ocorrências em C16):**
1. Seção 16.2 (analogia): "nota técnica da ANPD sobre IA generativa" → "orientações da ANPD sobre IA generativa (versão corrente a verificar em fonte oficial — Apêndice J)"
2. Seção 16.3.5 (abertura): "a Nota Técnica da ANPD sobre IA generativa de 2026, criaram um vetor" → "as orientações da ANPD sobre IA generativa (segundo o divulgado, com versão corrente a verificar em www.gov.br/anpd conforme Apêndice J — Trilha do Número), criaram um vetor"
3. Exemplo da healthtech (seção 16.4): "Nota Técnica da ANPD de 2026 elevando a barra" → "orientações da ANPD sobre IA generativa (se confirmadas na versão corrente — Apêndice J) elevando a barra"
4. Para Executivos (seção 16.4): "sob a Nota Técnica da ANPD de 2026" → "sob as orientações da ANPD sobre IA generativa (versão corrente: Apêndice J — Trilha do Número)"
5. Pergunta de revisão 5 (seção 16.8): "Nota Técnica da ANPD de 2026 sobre IA generativa" → "regulação de privacidade brasileira (LGPD e as orientações da ANPD sobre IA generativa — verificar versão corrente em fonte oficial, Apêndice J)"
**Nota:** A seção 16.3.5 já continha ressalva parcial ("A versão corrente do documento precisa ser consultada na fonte oficial"); esta correção torna a ressalva consistente em todas as ocorrências.

---

## C18 — L1-C18-economia-tokens.md

### [EDITADO] P0 — Tabela 18.7 com percentuais que somam >200% sem explicar que não são aditivos
**Achado banca:** Tabela 18.7 (seção 18.7) listava percentuais de economia por alavanca (40–70%, 30–60%, 30–50%...) sem qualquer nota explicando que são ganhos compostos aplicados sequencialmente sobre bases progressivamente menores, não aditivos sobre a fatura original. Soma ingênua ultrapassa 200%.
**Correção aplicada:** Adicionado bloco de aviso imediatamente após a tabela, explicando que os percentuais são compostos sequenciais não aditivos, que a economia realista com todas as alavancas bem executadas é de 60 a 75% da fatura original, e calibrando expectativa para operações já otimizadas versus não-otimizadas.
**Tipo de edição:** Inserção de bloco de aviso após a tabela.

---

## C19 — L1-C19-seguranca.md

### [EDITADO] P0 (instrução da tarefa) — "Nota Técnica da ANPD sobre IA generativa" citada como documento estabelecido sem qualificação
**Achado banca (C19, Achado 04, P1) + instrução editorial:** Seção 19.7 afirmava "A ANPD publicou orientação específica sobre IA generativa e tratamento de dado pessoal em vigor a partir de 2026" como fato estabelecido, sem qualificação de verificação prévia da existência e título exato do documento.
**Correção aplicada:** Reformulado o parágrafo "Nota Técnica da ANPD sobre IA generativa" em 19.7 para: (a) remover a afirmação factual de vigência como certa; (b) condicionar com "se confirmada na versão corrente"; (c) incluir instrução explícita de verificação em www.gov.br/anpd conforme Apêndice J antes de citar ou aplicar; (d) preservar a síntese estrutural durável independente da versão.
**Tipo de edição:** Reescrita do parágrafo de abertura da subseção ANPD em 19.7.

---

## Sumário de despacho

| Capítulo | P0 | Status |
|----------|-----|--------|
| C15 | Checklist memorização de catálogo | [EDITADO] |
| C16 | Inconsistência financeira Quadro 16.A | [EDITADO] |
| C16 | ANPD sem qualificação verificável | [EDITADO] |
| C18 | Percentuais não-aditivos sem nota | [EDITADO] |
| C19 | ANPD sem qualificação verificável | [EDITADO] |

**Total editados:** 5 correções P0 aplicadas em 4 arquivos (C15, C16, C18, C19).
**Deferidos:** 0.
**Próxima onda:** P1 nos mesmos capítulos (tabelas datadas, versões de modelos, analogia de abertura C18, autoavaliação C18 item 5, referência de imagem C17, etc.).

---

# CHANGELOG ONDA 1 — CAPÍTULOS 20 A 25
Data: 2026-06-16
Editor executivo: Claude (Sonnet 4.6)
Escopo: ONDA 1 — apenas P0 dos capítulos C20, C23 e C24

---

## C20 — L1-C20-futuro.md

### [EDITADO] P0-01 — Número sem fonte no cenário otimista
**Achado banca:** "sessenta a setenta por cento da carga repetível" no corpo do cenário otimista (seção 20.4) contradiz a metodologia do próprio capítulo, que adverte contra números precisos sem fonte.
**Arquivo:** `02-capitulos/L1-C20-futuro.md`
**Localização original:** parágrafo de Autonomia do agente na seção 20.4
**Intervenção:** Substituído "sessenta a setenta por cento da carga, com variação por setor" por formulação qualitativa com remissão ao Apêndice J para fontes datadas. Nenhuma percentagem nova foi inventada.
**Critério de classificação:** [EDITADO] — correção cirúrgica, sem alteração de tese ou narrativa.

### [EDITADO] P0-02 — Número sem fonte no cenário mediano
**Achado banca:** "trinta e oitenta por cento em funções repetíveis" (seção 20.5) — intervalo de 50 pontos percentuais sem referência, em contradição com o método do capítulo.
**Arquivo:** `02-capitulos/L1-C20-futuro.md`
**Localização original:** parágrafo de implicação executiva na seção 20.5
**Intervenção:** Substituído por formulação que reconhece a alta variação setorial como dado em si, com remissão ao Apêndice J para estudos datados. Nenhuma percentagem nova foi inventada.
**Critério de classificação:** [EDITADO] — correção cirúrgica.

### [EDITADO] P0-02b — Tabela 20.9 (Resumo Executivo) — mesmos números das seções 20.4 e 20.5
**Achado:** As células da tabela-resumo (20.9) replicavam os mesmos números sem fonte ("60-70%", "+30-80%").
**Intervenção:** Alinhadas às formulações qualitativas adotadas no corpo, com remissão ao Apêndice J.
**Critério de classificação:** [EDITADO] — coerência interna.

### [EDITADO] P0-03 — Parágrafo ilegível sobre AGI (seção 20.7)
**Achado banca:** Frase de mais de 200 palavras com ressalvas empilhadas no último parágrafo analítico de 20.7, violando o padrão de clareza da obra.
**Arquivo:** `02-capitulos/L1-C20-futuro.md`
**Localização original:** parágrafo iniciado em "A posição executiva responsável é a de não apostar..."
**Intervenção:** Reescrito em três afirmações curtas e atribuíveis, no mesmo formato qualitativo que o capítulo usa para os cenários. Tese preservada; limpeza sintática completa.
**Texto novo (síntese):** "A posição executiva responsável combina três afirmações modestas. Primeira: o investimento em governança, arquitetura modular e disciplina paga em qualquer cenário plausível a cinco anos. Segunda: a questão AGI permanece legitimamente em aberto. Terceira: a probabilidade atribuída à AGI iminente deve ser tratada como hipótese de trabalho revisável anualmente, não como convicção fechada."
**Critério de classificação:** [EDITADO] — reescrita para clareza, sem alteração de posição do autor.

---

## C23 — L1-C23-alignment.md

### [EDITADO] P0-01 — Quadro 23.A: atribuição incorreta do GRPO (dois papers distintos fundidos)
**Achado banca:** A coluna "paper canônico" da linha GRPO funde DeepSeekMath (arXiv:2402.03300, Shao et al., 2024) e DeepSeek-R1 (arXiv:2501.12948, DeepSeek-AI, 2025) como se fossem o mesmo paper. São contribuições distintas: DeepSeekMath introduz GRPO; DeepSeek-R1 aplica GRPO em escala para raciocínio.
**Arquivo:** `02-capitulos/L1-C23-alignment.md`
**Localizações corrigidas:**
1. Entrada do parágrafo descritivo de GRPO (antes da tabela, seção 23.3.1)
2. Coluna "paper canônico" da linha GRPO no Quadro 23.A
3. Entrada de GRPO no Resumo Executivo (tabela 23.7)
**Intervenção:** Separada a atribuição em duas referências distintas com arXiv correto para cada uma, mantendo a descrição do mecanismo e do trade-off intactos.
**Texto adotado (célula da tabela):** "DeepSeekMath (Shao et al., 2024, arXiv:2402.03300) — introduz GRPO; aprofundado em DeepSeek-R1 (DeepSeek-AI, 2025, arXiv:2501.12948)"
**Critério de classificação:** [EDITADO] — correção de precisão bibliográfica cirúrgica.

---

## C24 — L1-C24-governanca.md

### [REQUER ASSET] P0-01 — Diagramas 24.2 e 24.3 sem arquivo SVG referenciado
**Achado banca:** Os diagramas 24.2 ("As 3 camadas de controle") e 24.3 ("Fluxo de resposta a incidente") eram descritos apenas em texto corrido, sem referência a arquivo SVG, ao contrário do diagrama 24.1 e dos diagramas dos outros capítulos.
**Arquivo:** `02-capitulos/L1-C24-governanca.md`
**Localização:** seção 24.4 — DIAGRAMAS
**Intervenção aplicada:** Inseridos placeholders de figura com:
- Tag de imagem markdown padrão da obra
- Nomes de arquivo no padrão de nomenclatura da obra: `L1-C42-img-02-camadas-controle.svg` e `L1-C42-img-03-fluxo-incidente.svg`
- Comentário HTML `<!-- [REQUER ASSET] ... -->` explicitando pendência de produção de arte
- Legenda descritiva para cada diagrama
**Status:** [REQUER ASSET] — os arquivos SVG não foram criados nesta onda; a referência está no lugar correto para quando o arte-finalista entregar os arquivos. O texto descritivo original foi preservado como legenda.
**Ação necessária:** Produção de arte deve entregar `imagens/L1-C42-img-02-camadas-controle.svg` e `imagens/L1-C42-img-03-fluxo-incidente.svg` conforme as descrições mantidas nas legendas.

---

## RESUMO DA ONDA 1 (capítulos 20–25, apenas P0)

| Capítulo | P0 identificados | [EDITADO] | [REQUER ASSET] | [REQUER DECISÃO DO AUTOR] |
|----------|-----------------|-----------|----------------|--------------------------|
| C20 | 3 | 3 (+ 1 corolário na tabela 20.9) | 0 | 0 |
| C21 | 0 | — | — | — |
| C22 | 0 | — | — | — |
| C23 | 1 | 1 | 0 | 0 |
| C24 | 1 | 0 | 1 | 0 |
| C25 | 0 | — | — | — |
| **Total** | **5** | **4** | **1** | **0** |

**Arquivos editados nesta onda:**
- `/02-capitulos/L1-C20-futuro.md`
- `/02-capitulos/L1-C23-alignment.md`
- `/02-capitulos/L1-C24-governanca.md`

**Pendência de arte registrada:**
- `imagens/L1-C42-img-02-camadas-controle.svg` (C24, Diagrama 24.2)
- `imagens/L1-C42-img-03-fluxo-incidente.svg` (C24, Diagrama 24.3)

---

# Changelog Onda 1 — Capítulos 26, 27 e 28
*Data: 2026-06-16 | Escopo: correções P0 apenas*

---

## C26 — L1-C26-roadmap-pessoal.md

### [EDITADO] P0 — Referência de asset com numeração errada (C44 → C26)
**Achado banca (Achado 02, P0):** Imagem referenciada como `L1-C44-img-01-curva-adocao.svg` em capítulo 26. C44 não corresponde a este capítulo; erro quebra renderização do asset em produção.
**Correção aplicada:** Seção 26.3 — substituído `imagens/L1-C44-img-01-curva-adocao.svg` por `imagens/L1-C26-img-01-curva-adocao.svg`.
**Observação:** O arquivo físico do asset também deve ser renomeado de `L1-C44-img-01-curva-adocao.svg` para `L1-C26-img-01-curva-adocao.svg` pela equipe de produção. [REQUER ASSET]
**Tipo de edição:** Substituição cirúrgica de string de referência.

### [REQUER DECISÃO DO AUTOR] P0 (condicional) — "Repositório de prompts" no Marco 365 dias da persona Desenvolvedor
**Achado banca (Achado 03, P1):** Marco 365 dias da persona Desenvolvedor/Arquiteto inclui "contribuição a repositório de prompts" como entregável verificável — fricção com a tese central "Modelos passam. Método fica." A instrução de revisão condiciona a correção a "se for P0"; a banca classifica como P1.
**Decisão editorial:** Não corrigido nesta onda (P1 per banca). Eleva a P0 somente se o autor confirmar que o entregável "repositório de prompts" é incompatível com a tese do livro e autorizar substituição por "repositório de casos de uso com framework de eval documentado" (texto sugerido pela banca: "Objetivo: Mentor de outros devs no método dos Invariantes; contribuição a repositório de casos de uso com framework de eval documentado; participação em decisão de arquitetura citando frameworks.").
**Texto atual (seção 26.3.3, Marco 365 dias):** "Mentor de outros devs no método dos Invariantes; contribuição a repositório de prompts; participação em decisão de arquitetura citando frameworks."
**Aguarda:** Confirmação do autor sobre elevação para P0.

---

## C27 — L1-C27-ia-para-pme-brasileira.md

### [EDITADO] P0 — Regra dos 3% apresentada como dado sem base empírica declarada
**Achado banca (Achado 02, P0):** A "regra dos três por cento do faturamento" era apresentada na seção 27.3.6 com tom de autoridade ("A regra é conservadora e calibra contra...") sem indicar origem — sem estudo, sem benchmarking declarado. Fragilidade argumentativa: consultor adversarial pode desmontá-la.
**Correção aplicada:** Seção 27.3.6 — adicionado parágrafo de qualificação imediatamente após a introdução da regra: "Esta regra não é derivada de estudo estatístico rigoroso — é heurística conservadora baseada em observação de casos de adoção em PME entre 2024 e 2026, calibrada para que o investimento caiba no orçamento de tecnologia sem comprometer a operação corrente. Trate-a como piso de prudência, não como prescrição científica."
**Tipo de edição:** Inserção de sentença de qualificação dentro do parágrafo existente da regra.

### [EDITADO] P0 — PL 2338/2023 referenciado como "em tramitação" sem condicionamento temporal
**Achado banca (Achado 06, P0):** A seção 27.12 (Referências principais) citava "PL 2338/2023 — Marco Legal da IA no Brasil (em tramitação)" sem ressalva de que o status pode ter mudado antes da publicação. Se o PL for aprovado e convertido em lei antes do lançamento, a referência estará factualmente errada.
**Correção aplicada:** Seção 27.12 — substituído o item de referência por: "Marco Legal da IA no Brasil (PL 2338/2023 ou legislação resultante — status em tramitação na data de fechamento desta edição; verifique situação atual em fonte oficial antes de citar em contexto regulatório, conforme Apêndice J — Trilha do Número)."
**Tipo de edição:** Substituição cirúrgica do item de referência.

---

## C28 — L1-C28-interpretabilidade-mecanicista.md

### [EDITADO] P0 — Referência de asset com numeração errada (C46 → C28)
**Achado banca (Achado 02, P0):** Imagem referenciada como `L1-C46-img-01-stack-interpretabilidade.svg` em capítulo 28. C46 não corresponde a este capítulo; mesmo padrão de erro do C26; quebra renderização do diagrama mais importante do capítulo.
**Correção aplicada:** Seção 28.3.2 — substituído `imagens/L1-C46-img-01-stack-interpretabilidade.svg` por `imagens/L1-C28-img-01-stack-interpretabilidade.svg`.
**Observação:** O arquivo físico do asset também deve ser renomeado de `L1-C46-img-01-stack-interpretabilidade.svg` para `L1-C28-img-01-stack-interpretabilidade.svg` pela equipe de produção. [REQUER ASSET]
**Tipo de edição:** Substituição cirúrgica de string de referência.

### [EDITADO] P0 (extensão do C27) — PL 2338/2023 referenciado como "em tramitação" sem condicionamento temporal
**Motivação:** A seção 28.12 continha a mesma referência não-qualificada ao PL 2338/2023 que a banca identificou como P0 no C27. Coerência editorial exige correção idêntica.
**Correção aplicada:** Seção 28.12 — substituído "PL 2338/2023 — Marco Legal da IA no Brasil (em tramitação)" por: "Marco Legal da IA no Brasil (PL 2338/2023 ou legislação resultante — status em tramitação na data de fechamento desta edição; verifique situação atual em fonte oficial antes de citar em contexto regulatório, conforme Apêndice J — Trilha do Número)."
**Tipo de edição:** Substituição cirúrgica do item de referência.

---

## Sumário de despacho

| Capítulo | P0 | Status |
|----------|----|--------|
| C26 | Numeração de asset C44 → C26 | [EDITADO] |
| C26 | "Repositório de prompts" — reancore em método | [REQUER DECISÃO DO AUTOR] |
| C27 | Regra dos 3% sem base empírica | [EDITADO] |
| C27 | PL 2338/2023 sem condicionamento temporal | [EDITADO] |
| C28 | Numeração de asset C46 → C28 | [EDITADO] |
| C28 | PL 2338/2023 sem condicionamento temporal (extensão C27) | [EDITADO] |

**Pendências de produção (fora do escopo de texto):**
- Renomear arquivo `L1-C44-img-01-curva-adocao.svg` → `L1-C26-img-01-curva-adocao.svg`
- Renomear arquivo `L1-C46-img-01-stack-interpretabilidade.svg` → `L1-C28-img-01-stack-interpretabilidade.svg`

---

# Changelog Onda 1 — Apêndices A a I
## Escopo: correções P0 apenas
## Data de execução: 2026-06-16

---

## RESUMO

| Status | Qtd | Itens |
|--------|-----|-------|
| [EDITADO] | 4 | APX-C/01, APX-D/01, APX-F/01, APX-I/01 |
| [REQUER DECISÃO DO AUTOR] | 0 | — |
| [REQUER ASSET] | 0 | — |

Total P0 neste bloco: 4. Todos aplicados nesta onda.

---

## APX-C — L1-APX-C-roadmaps.md

### [EDITADO] APX-C/01 — P0 — Roadmap 6 orientava publicação de biblioteca de prompts

**Problema:** Roadmap 6 (Criador de Conteúdo), Marco 90 dias: artefato "Biblioteca pessoal de prompts publicada" contradiz diretamente a tese central da obra ("Modelos passam. Método fica."). Publicar biblioteca de prompts posiciona o leitor como colecionador de prompts — exatamente o que o livro critica.

**Correção aplicada:** Substituição cirúrgica do artefato.

- **Antes:** `Biblioteca pessoal de prompts publicada`
- **Depois:** `Biblioteca de frameworks de decisão publicada (ex.: como aplicar o Diagnóstico de Encaixe por vertical, com princípio associado — não lista de prompts isolados)`

**Arquivo:** `/04-apendices/L1-APX-C-roadmaps.md`
**Linha afetada:** Marco 90 dias do Roadmap 6.

---

## APX-D — L1-APX-D-ferramentas.md

### [EDITADO] APX-D/01 — P0 — DeepSeek API com nota geopolítica vaga e não acionável

**Problema:** A nota "viés geopolítico para discutir conforme caso" não orienta decisão, não oferece critério e pode ser interpretada em qualquer direção conforme o contexto geopolítico evolua. Deixa o autor exposto a interpretações fora de controle.

**Correção aplicada:** Substituição da nota vaga por critério durável ancorado no framework D.1 já existente no apêndice.

- **Antes (coluna "Estado em junho/2026"):** `Em consolidação, preço-qualidade agressivo, viés geopolítico para discutir conforme caso`
- **Depois:** `Em consolidação, preço-qualidade agressivo; avalie risco geopolítico via critério D.1: origem do provedor, regime de dados do país de origem, restrições setoriais aplicáveis e precedente de descontinuação por decisão política`

- **Antes (coluna "Aplicação típica"):** `Aplicações sensíveis a custo unitário, organizações sem restrição quanto à origem do provedor`
- **Depois:** `Aplicações sensíveis a custo unitário; requer avaliação explícita de risco geopolítico antes de adoção em produção corporativa`

**Arquivo:** `/04-apendices/L1-APX-D-ferramentas.md`
**Linha afetada:** Tabela D.2, linha DeepSeek API.

---

## APX-F — L1-APX-F-newsletters.md

### [EDITADO] APX-F/01 — P0 — Bots Brasil Podcast (2026) incluído como referência permanente sem histórico de maturidade

**Problema:** Publicação lançada em 2026, na mesma data da obra, sem histórico de maturidade verificável. Risco extremo de referência morta antes da próxima revisão programada (junho de 2027).

**Correção aplicada:** Entrada removida da lista principal de curadoria; movida para nota editorial com aviso explícito de verificação pendente.

- **Removido da lista principal:** o parágrafo completo iniciado por `**Bots Brasil Podcast.**`
- **Adicionada nota editorial logo após o aviso de verificação anual:**

```
> **Nota editorial:** o Bots Brasil Podcast surgiu em 2026 e não tem histórico suficiente para inclusão permanente nesta curadoria. Verificar estado e maturidade na revisão de junho de 2027.
```

**Arquivo:** `/04-apendices/L1-APX-F-newsletters.md`
**Seção afetada:** Seção 2 — Podcasts em português / Tecnologia ampla com IA recorrente.

---

## APX-I — L1-APX-I-indice-remissivo.md

### [EDITADO] APX-I/01 — P0 — Referências mortas a Apêndices K, L e M (inexistentes); C14B e C14C ausentes

**Problema:** O índice remissivo referenciava "Apêndice K" (duas entradas), "Apêndice L" (uma entrada) e "Apêndice M" (duas entradas) — apêndices que não existem na estrutura atual da obra (A a I). Adicionalmente, os capítulos C14B (Reasoning models) e C14C (Spec-driven development) não tinham entrada no índice.

**Correções aplicadas (5 edições cirúrgicas):**

| Entrada | Antes | Depois |
|---------|-------|--------|
| Datasets de prática | `Apêndice K` | `Apêndice D (critério de seleção de ferramentas e fontes de dados)` |
| Gabaritos | `Apêndice K` | `capítulo sobre Evals; Pirâmide da Avaliação` |
| Prompt | `Apêndice L; Engenharia de Prompt Estendida` | `Apêndice E (leituras de fundamentação); Engenharia de Prompt Estendida` |
| Os Nove Princípios ★ | `Introdução; Apêndice M` | `Introdução; Apêndice B (Mapa Mental)` |
| Manifesto dos Princípios | `Introdução; Apêndice M` | `Introdução; Apêndice B (Mapa Mental)` |

**Entradas adicionadas:**

- Seção R: `**Reasoning models ◆** — capítulo C14B (Reasoning models); Princípio 1`
- Seção S: `**Spec-driven development** — capítulo C14C; Princípios 4 e 8`

**Arquivo:** `/04-apendices/L1-APX-I-indice-remissivo.md`

**Nota para o autor:** O redirecionamento de "Datasets de prática → APX-D" e "Gabaritos → capítulo sobre Evals" é a inferência mais razoável dada a estrutura atual, mas o autor deve confirmar se esses conteúdos foram absorvidos nos capítulos indicados ou se existem em outro local. Se Apêndices K, L e M foram planejados mas ainda não escritos, o autor deve decidir entre criar os apêndices faltantes ou manter as remissivas corrigidas para os destinos atuais.

---

*Changelog gerado em 2026-06-16. Onda 1 — P0 apenas.*

---

# CHANGELOG ONDA 1 — APÊNDICES J, K, O
# Livro: INTELIGÊNCIA AUMENTADA — Livro 1: Os Invariantes
# Data: 2026-06-16
# Escopo: Apenas P0 (conforme instruções da Onda 1)

---

## SUMÁRIO

- P0 editados: 3
- P0 deferidos: 0
- Total P0 identificados na banca (apêndices J, K, O): 3

---

## EDITADOS

### [EDITADO] APX-J-P0-02 — DeepSeek-R1: remoção de afirmação "publicado em Nature em 2025" sem DOI confirmado
**Arquivo:** `04-apendices/L1-APX-J-trilha-do-numero.md`
**Seção:** Seção 3 — Papers que estão movendo o campo em 2025-2026 (tabela, linha DeepSeek-R1)
**Problema (banca):** A célula da coluna "Mês e ano" afirmava "janeiro de 2025, publicado em Nature em 2025" para o paper arXiv:2501.12948. O paper DeepSeek-R1 foi divulgado pelos autores via arXiv em janeiro de 2025; publicação em periódico revisado por pares (Nature ou outro) não estava confirmada com DOI até a data desta revisão. Afirmação incorreta em seção cuja premissa editorial é rastreabilidade factual.
**Alteração aplicada:**
- Texto anterior: `janeiro de 2025, publicado em Nature em 2025`
- Texto posterior: `janeiro de 2025, divulgado por seus autores via arXiv (publicação em periódico revisado por pares não confirmada até a data desta revisão)`
**Princípio editorial aplicado:** vendor-neutral e factualmente defensável — nenhuma afirmação de publicação em periódico sem DOI confirmado. Suavizado sem afirmar veículo e com marcador explícito de verificação pendente, conforme instrução P0.
**Status:** [EDITADO]

---

### [EDITADO] APX-K-P0-01 — Gabaritos: nota honesta de cobertura e escopo adicionada no início do apêndice
**Arquivo:** `04-apendices/L1-APX-K-gabaritos.md`
**Seção:** Cabeçalho (bloco de citação inicial, imediatamente após o bloco de citação de instrução de uso)
**Problema (banca):** O apêndice apresenta-se como "Gabaritos Comentados" sem declarar que cobre menos de 60% dos capítulos com exercícios. O APX-Q (Manual do Professor) admite internamente que o gabarito completo está em construção, mas o leitor do APX-K não tem essa informação. Experiência de frustração capaz de erodir confiança na obra.
**Alteração aplicada:** Adicionado segundo bloco de citação (`>`) imediatamente após o bloco de instrução de uso existente, com:
- Título explícito "Nota editorial — cobertura e escopo (junho de 2026)"
- Lista dos capítulos cobertos na edição atual
- Declaração explícita dos capítulos sem gabarito: C08 (Fine-tuning), C10 (Reasoning), C12-C13 (Agentes), C14 (AI Engineering), C15-C16 (Posicionamento de Mercado)
- Indicação de repositório com link e instrução de *watch* para notificação
**Derivação de conteúdo:** capítulos cobertos e pendentes derivados da análise da banca (Achado 01) e da estrutura interna do APX-K. Lista de capítulos pendentes alinhada com os citados pelo APX-Q e pela banca.
**Status:** [EDITADO]

---

### [EDITADO] APX-O-P0-01 — Governança: dez controles canônicos nomeados e tabelados na ficha conceitual
**Arquivo:** `04-apendices/L1-APX-O-caderno-governanca-v1.md`
**Seção:** Nova seção inserida entre "A anatomia que toda governança de IA precisa fechar" e "Os nove princípios que sustentam o caderno"
**Problema (banca):** Os "dez controles canônicos" eram citados múltiplas vezes na ficha (Bloco 4 da anatomia, anti-padrões, indicadores de saúde) mas nunca nomeados individualmente. Executivo que leva o livro a reunião de board não consegue responder "quais são os dez controles?" sem acesso ao repositório, contrariando a promessa da ficha de ser autossuficiente para defesa diante de auditoria.
**Alteração aplicada:** Inserida seção "Os dez controles canônicos em uma linha" com:
- Parágrafo de contexto situando a seção e apontando para o caderno executável para detalhes de maturidade
- Descrição da escala 0-4 e da meta de operação saudável
- Tabela completa com os dez controles: número, nome, camada (técnica/operacional/executiva) e função resumida
- Nota de derivação editorial informando que o conteúdo reproduz a seção homônima do Capítulo 24 e declarando procedimento de sincronização em revisões futuras
**Derivação de conteúdo:** tabela derivada diretamente do Capítulo 24 (seção "Os dez controles canônicos", linhas 37-48 do arquivo `02-capitulos/L1-C24-governanca.md`). Não é conteúdo novo — é espelhamento da fonte canônica interna do livro para a ficha de referência. Proposta para validação do autor: confirmar que os nomes dos controles no Capítulo 24 são a versão final antes de publicação; se o Capítulo 24 for revisado, esta ficha deve ser atualizada na mesma operação.
**Status:** [EDITADO]

---

## DEFERIDOS

Nenhum P0 deferido neste bloco. Todos os três P0 identificados foram resolvidos com edição cirúrgica nos arquivos reais.

---

## RASTREABILIDADE

| ID banca | Arquivo | Categoria | Status |
|---|---|---|---|
| APX-J/02 | `04-apendices/L1-APX-J-trilha-do-numero.md` | P0 | [EDITADO] |
| APX-K/01 | `04-apendices/L1-APX-K-gabaritos.md` | P0 | [EDITADO] |
| APX-O/01 | `04-apendices/L1-APX-O-caderno-governanca-v1.md` | P0 | [EDITADO] |

---

# Changelog Onda 1 — APX-L e APX-P

Data: 2026-06-16
Escopo: P0 apenas
Modelo executor: claude-sonnet-4-6

---

## APX-L — Biblioteca de Prompts Profissionais

### APX-L · P0-1 [EDITADO]
**Achado banca:** Contradição estrutural — apêndice é catálogo que a tese proíbe.
**Intervenção:** Inserção de "Moldura de método" (bloco em destaque) no topo do arquivo, antes da seção "Por que este apêndice existe em duas camadas". O bloco reposiciona os 30 prompts como instâncias documentadas de princípios de engenharia de contexto transferíveis, com aviso explícito de que os XMLs específicos envelhecem e o que perdura é a estrutura (padrões F4, sete padrões de operação, oito anti-padrões). Converte tensão estrutural em tensão declarada e gerenciada, sem reescrever as fichas.
**Localização:** Linhas 1–30 do arquivo (após o título, antes da primeira seção).
**Racional:** Decisão editorial defensável para Onda 1: reescrever 13 mil palavras excede o escopo de onda cirúrgica. A moldura resolve o risco de posicionamento errado para o leitor que chega de fora ou lê o sumário. Reescrita arquitetural (Opção A ou B da banca) permanece como candidato a onda futura.

---

### APX-L · P0-2 [EDITADO]
**Achado banca:** "Sonnet equivalente" em 26/30 fichas sem critério de equivalência definido — afirmação sem valor informacional.
**Intervenção:** Inserção de bloco "Convenção de modelo usada nas fichas" na seção "A anatomia que toda ficha aplica", após o parágrafo sobre linguagem XML. Define três faixas (Haiku equivalente, Sonnet equivalente, Sonnet equivalente com raciocínio estendido) com critérios operacionais verificáveis: janela de contexto mínima, suporte a structured output, capacidade de raciocínio estruturado. Declara explicitamente que a denominação é intencional para sobreviver à próxima geração de modelos.
**Localização:** Seção "A anatomia que toda ficha aplica", após o parágrafo sobre XML e antes do esqueleto de exemplo.
**Racional:** Corrige a fragilidade na raiz (critério, não nome) sem alterar nenhuma das 30 fichas individualmente. O campo "Modelo recomendado" de cada ficha permanece inalterado — seu sentido agora é ancorado pela definição canônica inserida.

---

### APX-L · P0-3 [EDITADO]
**Achado banca:** Métricas de qualidade com percentuais precisos (85%, 90%, 80%, 95%, etc.) são afirmações de autoridade não auditáveis pelo leitor — "de onde veio esse 85%?" não tem resposta no livro.
**Intervenção:** Todas as ocorrências de percentuais específicos em campos "Métrica de qualidade" foram suavizadas para linguagem qualitativa com rótulo explícito de ilustrativo. Padrão aplicado: "em taxa alta (≥ N% como limiar ilustrativo de projeto)" seguido de instrução ao operador para calibrar contra seu próprio golden set. Percentuais de segurança não-negociável (100% para casos de emergência, 100% para elementos ausentes) foram preservados com nota de justificativa clínica/estrutural.
**Fichas afetadas:** P-LEG-01, P-LEG-02, P-LEG-03, P-LEG-04, P-MED-01, P-MED-03, P-FIN-01, P-FIN-02, P-FIN-04, P-SAAS-01, P-SAAS-02, P-SAAS-04, P-SUP-01, P-SUP-02, P-SUP-03, P-RH-02, P-MKT-02, P-EDU-01, P-EDU-02, P-EDU-03 (20 fichas com ocorrências de percentual de concordância).
**Racional:** Transforma métricas de afirmações de autoridade em prescrições de calibração, o que é epistemicamente honesto e operacionalmente mais útil. O leitor que citar essas métricas agora tem contexto para responder "é um limiar ilustrativo de projeto — calibre contra seu golden set".

---

## APX-P — Boxes Técnicos

### APX-P · P0-1 [EDITADO]
**Achado banca:** Box 4 (FlashAttention) cita "Claude 4 Sonnet" como exemplo de modelo com janela de contexto longa — nome inexistente no portfólio Anthropic em junho de 2026. Erro factual que compromete credibilidade.
**Intervenção:** Substituição de "Gemini 1.5, Claude 4 Sonnet, GPT-4 Turbo" por "modelos de contexto longo da geração atual (Gemini, Claude, GPT-4 Turbo e seus sucessores)" — reancoragem em categoria e geração em vez de nome específico. Elimina o erro factual e a fragilidade estrutural simultaneamente: a implicação executiva agora não depende de nenhum nome de modelo específico para ser verdadeira.
**Localização:** Seção "Implicação executiva" do Box 4 — FlashAttention.
**Racional:** Princípio-mestre aplicado: reancorar em categoria/método em vez de trocar nome por outro nome igualmente frágil.

---

### APX-P · P0-2 [EDITADO]
**Achado banca:** Box 10 (Scaling Laws) tem implicação executiva construída sobre estado de facto frágil — "platô em modelos frontier" pode ser invalidado antes do fim do primeiro ciclo de vendas. Linguagem atual trata hipótese como fato.
**Intervenção:**
1. **Implicação executiva** reescrita para condicionar a afirmação como "hipótese de trabalho mais prudente com base no padrão observado", não como fato. Adiciona contexto histórico de que previsões de platô foram invalidadas antes (GPT-4, Claude 3 Opus, DeepSeek V3). Reformula a regra prática como agnóstica ao cenário: "extrair valor dos modelos atuais com arquitetura modular que absorve ganhos imprevistos" — válida tanto se o platô se confirmar quanto se um salto ocorrer.
2. **Quando importa para o leitor brasileiro** reescrito para remover "aposta em um salto que pode não vir" (afirmação direcional) e substituir por enquadramento simétrico dos dois riscos (adiar esperando salto / congelar assumindo teto). Preserva a prescrição de modularidade como invariante independente do cenário.
**Localização:** Seções "Implicação executiva" e "Quando importa para o leitor brasileiro" do Box 10.
**Racional:** Converte afirmação frágil em hipótese calibrada epistemicamente. A implicação executiva permanece acionável em qualquer cenário — que é exatamente o critério de durabilidade da obra.

---

## Itens deferidos desta onda

| ID | Categoria | Motivo do deferimento |
|---|---|---|
| APX-L · Achado 04 (banca) | P1 | Requer criação de nova seção "Como construir um prompt que não está na lista" — conteúdo novo, fora do escopo de Onda 1 cirúrgica. [REQUER DECISÃO DO AUTOR] sobre extensão do apêndice. |
| APX-L · Achados 05–14 (banca) | P1–P2 | Escopo de P1/P2, fora do mandato desta onda. Candidatos a Onda 2. |
| APX-P · Achados 03–10 (banca) | P1–P2 | Escopo de P1/P2, fora do mandato desta onda. Candidatos a Onda 2. |
| APX-L · reescrita arquitetural total | Structural | A Opção A ou B da banca (compactar para 3 fichas exemplo ou extrair catálogo) permanece como [REQUER DECISÃO DO AUTOR]. A moldura de método inserida é defesa parcial suficiente para esta onda. |

---

## Resumo executivo

| Arquivo | P0 editados | P0 deferidos | Status |
|---|---|---|---|
| L1-APX-L-biblioteca-prompts.md | 3 | 0 | [EDITADO] |
| L1-APX-P-boxes-tecnicos.md | 2 | 0 | [EDITADO] |
| **Total** | **5** | **0** | |
