# INTELIGÊNCIA AUMENTADA — Banca Editorial Adversarial
## Sumário Executivo + Plano de Ação Consolidado

**Escopo:** 73 arquivos `.md` lidos integralmente (sem amostragem) — 15 paratextos, 2 manifestos, 9 frameworks, 30 capítulos, 17 apêndices. ~231 mil palavras.
**Método:** banca de 4 papéis adversariais (Aquisição, Desenvolvimento, IA/Fact-checking, Leitora Joana) + 5 testes (Joana, Durabilidade, Diferenciação, Memorização, Transformação) por arquivo.
**Régua:** não é a média dos livros de IA — é *Thinking Fast and Slow*, *Superforecasting*, *Competing in the Age of AI*, *Designing Data-Intensive Applications*, *Accelerate*.

---

## 1. VEREDITO GERAL

A obra está num patamar **claramente acima da média do mercado brasileiro de IA** e a tese central — *"Modelos passam. Método fica."* — é defensável e diferenciadora. O problema não é qualidade média; é **inconsistência de durabilidade e alguns pontos de fricção com a própria tese**. O livro já contém ilhas de propriedade intelectual real (frameworks F3 e F8, capítulos C14B, C17, C27, apêndices M e O). O risco não é o livro ser fraco — é ele **envelhecer mal** e **se contradizer** em pontos específicos que um leitor executivo exigente vai notar.

**Total de achados: 378** (após deduplicação)

| Prioridade | Qtd | Significado |
|---|---|---|
| **P0 — Crítico** | 52 | Compromete credibilidade, autoridade ou coerência. Resolver antes de publicar. |
| **P1 — Importante** | 204 | Reduz clareza, retenção e transformação do leitor. |
| **P2 — Melhoria** | 122 | Otimização de experiência. |

**Arquivos que exigem mais que ajuste pontual (REVISAR PARCIALMENTE):**
C05 (embeddings), C09 (engenharia de prompt), C13 (MCP), C18 (economia de tokens), F5 (cobertura/integrações), APX-E (leituras), APX-I (índice remissivo), APX-K (gabaritos), APX-L (biblioteca de prompts).

---

## 2. OS 5 TEMAS TRANSVERSAIS (resolva a causa, não o sintoma)

Os 378 achados se condensam em cinco padrões de causa-raiz. Atacar estes cinco resolve a maior parte dos problemas individuais.

### TEMA 1 — Fricção com a própria tese (12 ocorrências) · **MAIOR RISCO REPUTACIONAL**
O livro promete "método, não catálogo de prompts/ferramentas", mas tropeça nisso em pontos concretos:
- **C09** referencia `awesome-prompts` e estrutura a seção 9.4 como lista de receitas sem framework de decisão.
- **APX-L** é, formalmente, a "biblioteca de prompts" que a tese proíbe.
- **APX-C** (Roadmap 6) e **C26** orientam o leitor a publicar uma "biblioteca de prompts".
- **C13 (MCP)** endossa um protocolo de fornecedor como referência — exatamente o tipo de aposta que "modelos passam" deveria evitar ancorar.
> **Decisão editorial necessária:** ou estes elementos são **reancorados em método** (ex.: "biblioteca de *frameworks de decisão*", prompts apresentados como *instâncias de um princípio transferível*), ou a tese perde força. Não dá para ter as duas coisas.

### TEMA 2 — Números e afirmações sem fonte rastreável (15 ocorrências) · **RISCO DE AUTORIDADE**
Vários números aparecem como fato sem rastreabilidade (percentuais PT/EN de tokenização em C03; "30%" ilustrativo tratado como dado em C05; cenários do C20; "85% de concordância com advogado sênior" em APX-L; economias de tokens que somam >200% em C18). O livro tem um *apêndice metodológico de números* (APX-N) e uma *trilha do número* (APX-J) — mas nem todos os números citados estão amarrados a eles. **Toda estatística precisa de origem ou de rótulo explícito "ilustrativo".**

### TEMA 3 — Durabilidade desigual (26 ocorrências) · **RISCO DE 2 ANOS**
Capítulos-método (Evals, LLMOps, Alignment, Governança, Trade-offs) têm ALTA durabilidade. Mas capítulos-catálogo envelhecem em 12–18 meses: preços de API (C16, C18), comparação de modelos (C15), nomes de modelos específicos (inclusive um modelo **inexistente** citado como exemplo em APX-P), repos do GitHub (C17 — mitigado por bom enquadramento), ferramentas (APX-D) e newsletters (APX-F). **Solução durável: substituir listas fixas por critérios de seleção** ("como avaliar um modelo" > "qual modelo é melhor hoje").

### TEMA 4 — Erros factuais técnicos pontuais (a corrigir antes da gráfica) · **RISCO DE CREDIBILIDADE**
Itens que um especialista detecta na primeira leitura e que custam autoridade:
- **"Claude 4 Sonnet"** (modelo inexistente) citado como exemplo em APX-P.
- **"DeepSeek-R1 publicado na Nature"** afirmado sem DOI em C14B e APX-J.
- Quadro 23.A funde dois papers distintos na entrada GRPO (DeepSeekMath ≠ DeepSeek-R1).
- Taxonomia de C01 posiciona "IA Generativa" como família paralela ao ML (incorreto).
- Custo quadrático da atenção apresentado como regra geral, ignorando Flash Attention (C04).

### TEMA 5 — Consistência interna e assets de produção (19 ocorrências) · **RISCO OPERACIONAL**
Numeração de assets trocada (C44/C46 em vez de C26/C28); diagramas descritos em texto sem SVG referenciado (C24); índice remissivo (APX-I) aponta para apêndices K/L/M como se não existissem e ignora C14B/C14C; orelhas duplicadas e divergentes; campos de produção (ISBN, ficha CIP) abertos em arquivos canônicos; repositório acompanhante que pode estar vazio na publicação.

---

## 3. OS 52 ACHADOS P0 — onde concentrar a primeira semana

Os P0 estão na aba **"P0 Criticos"** da planilha `Tracker-Achados-Banca-Editorial.xlsx`, prontos para atribuir responsável e prazo. Concentração de criticidade:

| Arquivo | P0 | Natureza |
|---|---|---|
| C01 — O que é IA | 3 | taxonomia, epígrafe, data de Constitutional AI |
| C13 — MCP | 3 | dependência de protocolo de fornecedor vs. tese |
| C20 — Futuro | 3 | números sem fonte + trecho ilegível sobre AGI |
| APX-L — Biblioteca de prompts | 3 | contradiz tese + métricas não-verificáveis |
| C02, C09, C12, C14B, C27, APX-P | 2 cada | erros factuais e fricção com tese |
| ~30 outros arquivos | 1 cada | ver planilha |

---

## 4. PLANO DE AÇÃO EM 4 ONDAS

### ONDA 1 — Blindagem de credibilidade (antes de qualquer diagramação final) · ~1 semana
Resolver os **52 P0**, priorizando os 5 erros factuais do Tema 4 e os 12 pontos de fricção com a tese (Tema 1). Sem isso, um resenhista técnico derruba a autoridade do livro no primeiro capítulo.
**Critério de pronto:** zero afirmação factual incorreta; zero número sem fonte ou rótulo "ilustrativo"; nenhum elemento que contradiga "Modelos passam. Método fica." sem reancoragem explícita.

### ONDA 2 — Durabilidade (decisão estratégica) · ~1–2 semanas
Converter capítulos-catálogo em capítulos-método (Tema 3). Para cada lista de preços/modelos/ferramentas/repos, adicionar a pergunta durável que a gera ("o que torna um repo confiável", "como ler um preço de token", "como avaliar um modelo") e mover os exemplos datados para o repositório acompanhante versionado.
**Critério de pronto:** nenhum capítulo perde validade se um modelo novo for lançado amanhã.

### ONDA 3 — Clareza e Joana (retenção) · ~2 semanas
Atacar os 204 P1, com foco nos capítulos técnicos onde a Joana se perde (C05 embeddings, C28 interpretabilidade) e na padronização de aberturas/encerramentos pedagógicos.
**Critério de pronto:** cada capítulo passa no teste "qual foi a ideia principal?" em uma frase.

### ONDA 4 — Acabamento e consistência (pré-gráfica) · ~1 semana
Assets, numeração, índice remissivo, paratextos, repositório (Temas 5). Mais os 122 P2.
**Critério de pronto:** nenhum placeholder visível; índice e referências cruzadas 100% consistentes; repositório acompanhante populado.

---

## 5. COMO USAR ESTES ENTREGÁVEIS

- **`Tracker-Achados-Banca-Editorial.xlsx`** — controle item a item. Aba *Dashboard* (visão geral), *Achados* (378, ordenados por prioridade e ROI, com colunas Status/Responsável/Prazo prontas), *P0 Criticos* (os 52 críticos isolados).
- **Este documento** — leitura executiva + plano.
- **`secoes/`** — a banca completa, arquivo por arquivo, no formato integral (notas por eixo, 5 testes, achados detalhados, decisão editorial). A íntegra das 11 seções segue abaixo, neste mesmo arquivo, para leitura corrida.

---
---

# BANCA COMPLETA — ÍNTEGRA POR ARQUIVO

> As seções abaixo são a avaliação detalhada de cada arquivo, no formato adversarial completo. Use a planilha para executar; use esta íntegra para entender o *porquê* de cada achado.


---

# BANCA EDITORIAL ADVERSARIAL — PARATEXTO COMPLETO
## Livro: INTELIGÊNCIA AUMENTADA — Os Princípios Permanentes da IA
## Revisado por: Banca de 4 especialistas (Editor-Chefe, Editor de Desenvolvimento, Especialista IA/Fact-checking, Leitora Joana)

---

# [P-00] — L1-00-capa-e-titulos.md

## RESUMO EXECUTIVO
Nota: 7/10
Veredito: B

## O QUE FUNCIONA
- O posicionamento "manual conceitual e executivo" é preciso e defensável: diferencia de tutorial e de livro acadêmico sem prometer o impossível.
- A linha curta "O livro que separa o padrão do botão" é memorável e citável — funciona em capa de e-mail e em thumbnail.
- A tabela de posicionamento entrega os cinco elementos que um briefing de capa precisa, em formato digerível para o designer.
- A escolha de Conceito A (minimalista executivo) com justificativa é decisão editorial, não indecisão — isso é positivo.
- A frase âncora da orelha esquerda ("Modelos passam. Método fica. Decore o padrão, consulte o número.") é a síntese mais compacta e memorável de toda a proposta do livro.

## O QUE NÃO FUNCIONA
- O subtítulo da capa oscila entre duas versões sem que o arquivo declare qual é a canônica: linha 2 diz "Os Princípios Permanentes da IA" (subordinada ao título principal), mas linha 9 diz "O manual conceitual e executivo para entender, decidir e governar inteligência artificial moderna." — são dois subtítulos diferentes. Isso vai confundir o designer e o distribuidor.
- "Linha curta para canais digitais" na linha 11 é uma tag interna de produção que não deveria estar em arquivo de capa — parece lembrete de briefing, não elemento editorial.
- O ISBN e a Ficha CIP como "a obter" / "a produzir" são estado de incompletude aceitável em produção, mas a tabela de copyright mistura campos finalizados com campos pendentes sem marcação clara (ex: "a obter" vs campo já preenchido). Isso é risco operacional: campo vazio em PDF de impressão.
- A seção de Orelha Esquerda duplica conteúdo que aparece no L1-11-orelhas.md — dois arquivos para o mesmo elemento, risco de versão desatualizada divergir.
- A seção de Orelha Direita neste arquivo é mais esquemática (tabela de trilhas) do que a versão expandida que aparece em L1-05 e L1-02 — inconsistência de profundidade entre o que o leitor vê na capa física vs. o interior do livro.

## ACHADOS

### ACHADO 01
Categoria: P0
Problema: Dois subtítulos concorrentes no mesmo arquivo sem declaração de qual é o canônico.
Por que é um problema: O subtítulo aparece em ISBN, cadastro de distribuidores, metadados de e-book, capa impressa e material de divulgação. Divergência entre "Os Princípios Permanentes da IA" (linha 2) e "O manual conceitual e executivo para entender, decidir e governar inteligência artificial moderna" (linha 9) vai gerar erro em pelo menos um canal.
Impacto no leitor: Confusão na descoberta orgânica; metadados incorretos reduzem indexação.
Correção exata: Declarar explicitamente qual é o subtítulo canônico para capa/ISBN ("Os Princípios Permanentes da IA") e qual é o tagline de marketing (a linha longa). Separar com cabeçalho distinto.
Texto sugerido: `## SUBTÍTULO CANÔNICO (capa, ISBN, distribuidores)\n*Os Princípios Permanentes da IA*\n\n## TAGLINE DE MARKETING (sinopse, e-mail, redes)\n*O manual conceitual e executivo para entender, decidir e governar inteligência artificial moderna.*`
ROI: ALTO

### ACHADO 02
Categoria: P1
Problema: Seção de Orelha Esquerda duplicada entre este arquivo e L1-11-orelhas.md, com conteúdo diferente entre os dois.
Por que é um problema: Em produção gráfica, o designer vai escolher um dos dois. Se escolher o errado, a versão de menor qualidade vai para impressão.
Impacto no leitor: Não diretamente — mas risco operacional alto de erro de produção.
Correção exata: Remover as seções de orelha deste arquivo e manter apenas referência: "Ver L1-11-orelhas.md (versão canônica)" — como já foi feito para a quarta capa.
Texto sugerido: `## ORELHAS\n> Textos canônicos: ver \`L1-11-orelhas.md\`.`
ROI: ALTO

### ACHADO 03
Categoria: P2
Problema: "Linha curta para canais digitais" é tag interna de briefing editorial exposta em arquivo de produto.
Por que é um problema: Se este arquivo for enviado ao designer ou ao distribuidor, a tag interna aparece como conteúdo.
Impacto no leitor: Zero direto — risco operacional.
Correção exata: Mover para comentário HTML `<!-- -->` ou para seção de notas internas separada.
Texto sugerido: n/a
ROI: BAIXO

### ACHADO 04
Categoria: P2
Problema: Campos de ISBN e Ficha CIP marcados como "a obter"/"a produzir" sem data-limite ou responsável.
Por que é um problema: Em produção de livro, esses campos têm prazo regulatório (depósito legal exige ISBN antes da impressão). Sem data-limite, o pendente fica invisível.
Impacto no leitor: Nenhum até impressão. Após impressão sem ISBN: problema de distribuição.
Correção exata: Adicionar `[PENDENTE — responsável: X — prazo: Y]` em cada campo incompleto.
Texto sugerido: n/a
ROI: MÉDIO

## TESTE DA JOANA
Entenderia: SIM
O que ela entenderia: O posicionamento do livro, o tom, para quem é.
O que ela NÃO entenderia: A diferença entre subtítulo canônico e tagline — mas isso é problema de produção, não de leitura.
Como corrigir: Separar subtítulo de tagline com cabeçalhos explícitos.

## TESTE DE DURABILIDADE
Classificação: ALTA
2 anos / 5 anos / 10 anos: Arquivo de capa não envelhece — é estrutural. A cor navy+laranja não tem data de validade editorial.
Justificativa: Nenhum elemento datado. Os conceitos visuais recomendados são atemporais.

## TESTE DE DIFERENCIAÇÃO
Classificação: DIFERENCIADO
Justificativa: "O livro que separa o padrão do botão" é diferenciador real no mercado de livros de IA em português. A maioria dos concorrentes empurha o botão.

## TESTE DE MEMORIZAÇÃO
Ideia principal clara? SIM
Qual é a ideia principal (em 1 frase): Livro de método, não de ferramenta — "Modelos passam. Método fica."
Justificativa: A frase âncora da orelha esquerda faz o trabalho de memorização sem apoio adicional.

## TESTE DE TRANSFORMAÇÃO
Ao terminar, o leitor consegue fazer o que antes não conseguia:
- Não se aplica diretamente a arquivo de capa. O arquivo cumpre sua função estrutural de orientar produção gráfica.

## NOTA FINAL
Estrutura: 7 | Pedagogia: n/a | Clareza: 6 | Autoridade: 8 | Durabilidade: 9 | Diferenciação: 8 | Memorização: 8 | Transformação: n/a
**Nota Geral: 7**

## DECISÃO EDITORIAL
MANTER COM AJUSTES (resolver conflito de subtítulo e remover duplicação de orelhas)

---

# [P-00B] — L1-00b-ficha-catalografica.md

## RESUMO EXECUTIVO
Nota: 7/10
Veredito: B

## O QUE FUNCIONA
- A nota sobre o ecossistema de IA é honesta e tecnicamente correta: data os dados com "junho de 2026" e explica onde vivem as atualizações (repositório acompanhante).
- A cláusula de errata e contribuições com política de creditação no changelog é prática recomendável e rara em livros técnicos brasileiros.
- A ressalva sobre bibliotecário registrado (CRB) para ficha CIP está correta juridicamente (Lei 4.084/1962).
- A seção de marcas registradas é adequada e cobre os principais provedores mencionados.

## O QUE NÃO FUNCIONA
- A ficha CIP inclui "5. Modelos de linguagem" como descritor — esse termo não é descritor controlado padrão da CDD/CDU brasileira. Bibliotecário CRB vai rejeitar ou alterar.
- O "Apêndice Q (Manual do Professor)" é citado na seção de direitos autorais como referência para "política específica de uso em contexto educacional" — mas a ficha catalográfica é elemento de pré-impressão que não deve referenciar apêndices internos. Cria dependência circular.
- "canal oficial da obra, divulgado pelo autor em sua presença profissional pública" é eufemismo para LinkedIn. Nomeie o canal ou coloque URL. Linguagem vaga em documento jurídico é problema.
- ISBN duplo (impresso + digital) com "Em processo de atribuição" em ambos — aceitável como estado, mas o arquivo deveria ter campo de data de atribuição esperada para controle de produção.
- CDD: 006.3 está correto para IA. CDU: 004.8 está correto. Sem problema aqui.

## ACHADOS

### ACHADO 01
Categoria: P1
Problema: Descritor "5. Modelos de linguagem" não é descritor controlado padrão do sistema CDD/CDU para catalogação brasileira.
Por que é um problema: Bibliotecário CRB vai alterar ou rejeitar, gerando retrabalho. "Processamento de linguagem natural" (CDU 004.912) é o descritor correto.
Impacto no leitor: Reduz indexação em bibliotecas e sistemas acadêmicos que consultam ficha CIP.
Correção exata: Substituir "5. Modelos de linguagem" por "5. Processamento de linguagem natural" ou "5. Redes neurais artificiais".
Texto sugerido: `5. Processamento de linguagem natural.`
ROI: MÉDIO

### ACHADO 02
Categoria: P1
Problema: Referência ao "Apêndice Q (Manual do Professor)" dentro da ficha catalográfica/direitos autorais — documento jurídico referenciando conteúdo interno.
Por que é um problema: Ficha catalográfica é documento independente, deve ser autocontida. Referência interna cria ambiguidade sobre o que a política de direitos autorais realmente diz.
Impacto no leitor: Confusão para quem usa o livro em contexto educacional e não encontra o apêndice referenciado de imediato.
Correção exata: Substituir a referência ao Apêndice Q por uma frase autocontida com a política essencial, ou redirecionar para o canal oficial.
Texto sugerido: `Qualquer adaptação para curso, palestra, treinamento corporativo ou material derivado exige autorização específica e por escrito do autor, disponível mediante contato via canal oficial da obra.`
ROI: MÉDIO

### ACHADO 03
Categoria: P2
Problema: "canal oficial da obra, divulgado pelo autor em sua presença profissional pública" — linguagem evasiva em contexto jurídico.
Por que é um problema: Em caso de disputa de direitos autorais, "presença profissional pública" não é endereço verificável.
Impacto no leitor: Leitor que quer contato legítimo não sabe onde ir.
Correção exata: Inserir URL ou e-mail de contato, mesmo que seja o LinkedIn com URL completo.
Texto sugerido: n/a — depende de decisão do autor sobre canal oficial.
ROI: MÉDIO

## TESTE DA JOANA
Entenderia: SIM. Documento padrão, linguagem clara. A nota sobre ecossistema de IA é particularmente bem escrita para leigo.
O que ela NÃO entenderia: A diferença entre CDD e CDU — mas não precisa entender.
Como corrigir: n/a.

## TESTE DE DURABILIDADE
Classificação: ALTA
Justificativa: Ficha catalográfica é atemporal por definição. A nota sobre atualização do repositório é bem calibrada — não promete data, apenas promete entrega.

## TESTE DE DIFERENCIAÇÃO
Classificação: COMMODITY
Justificativa: Ficha catalográfica é elemento regulatório padrão. A nota sobre ecossistema é diferenciada mas está no lugar certo.

## TESTE DE MEMORIZAÇÃO
Ideia principal clara? SIM — documento funcional, não precisa ser memorável.
Qual é a ideia principal (em 1 frase): Este livro tem direitos reservados, dados datados de junho/2026, e atualizações vivem no repositório.
Justificativa: Cumpre função regulatória adequadamente.

## TESTE DE TRANSFORMAÇÃO
Ao terminar, o leitor consegue fazer o que antes não conseguia:
- Não aplicável — documento regulatório.

## NOTA FINAL
Estrutura: 8 | Pedagogia: n/a | Clareza: 7 | Autoridade: 7 | Durabilidade: 9 | Diferenciação: 5 | Memorização: n/a | Transformação: n/a
**Nota Geral: 7**

## DECISÃO EDITORIAL
MANTER COM AJUSTES (corrigir descritor CIP, remover referência ao Apêndice Q, especificar canal de contato)

---

# [P-00C] — L1-00c-dedicatoria.md

## RESUMO EXECUTIVO
Nota: 6/10
Veredito: B

## O QUE FUNCIONA
- A terceira estrofe ("Ao leitor que vai usar este conhecimento para construir, não apenas para opinar") está diretamente alinhada com a tese da obra e com o tagline da quarta capa — coerência rara em dedicatórias.
- O tom é seco, sem sentimentalismo excessivo — adequado para um livro técnico-executivo.

## O QUE NÃO FUNCIONA
- A primeira estrofe ("A quem aprende a ler o padrão por trás do número") é abstrata a ponto de ser genérica — poderia estar em qualquer livro de método ou de estratégia. Não ancora na identidade específica desta obra.
- A segunda estrofe ("A quem teve paciência com minhas ausências") é convencional ao ponto do clichê. Toda dedicatória de não-ficção técnica escrita com seriedade tem uma variação desta frase. Não agrega nada específico.
- A dedicatória não menciona a tese central ("Modelos passam. Método fica.") nem o conceito dos Nove Princípios — oportunidade perdida de fazer o paratexto reforçar a espinha intelectual do livro.

## ACHADOS

### ACHADO 01
Categoria: P2
Problema: Segunda estrofe é clichê de dedicatória técnica ("A quem teve paciência com minhas ausências").
Por que é um problema: Não diferencia esta obra de milhares de outras. Dedicatória que poderia existir em dezenas de outros livros = baixa originalidade.
Impacto no leitor: Impressão de que o autor não investiu esforço criativo neste elemento.
Correção exata: Reescrever para ancorar a ausência em algo específico da construção deste livro, ou cortar a estrofe e deixar as outras duas.
Texto sugerido: `A quem conviveu com as madrugadas em que o método ainda estava errado, e com as manhãs em que ficou certo.`
ROI: BAIXO

### ACHADO 02
Categoria: P2
Problema: Primeira estrofe ("A quem aprende a ler o padrão por trás do número") é abstrata demais para ser âncora de dedicatória.
Por que é um problema: O leitor que abre a dedicatória antes de ler o livro não tem referência para "padrão" vs. "número" — a Camada Dupla ainda não foi apresentada.
Impacto no leitor: Passa sem marcar.
Correção exata: Ou adicionar uma palavra que ancora ("A quem escolhe o princípio sobre a versão") ou manter e aceitar que a dedicatória funciona retroativamente, após a leitura.
Texto sugerido: `A quem escolhe aprender o que dura em vez do que vende.`
ROI: BAIXO

## TESTE DA JOANA
Entenderia: SIM. Curta, direta. A terceira estrofe vai ressoar especialmente.
O que ela NÃO entenderia: "ler o padrão por trás do número" sem contexto prévio.
Como corrigir: Âncora mais concreta na primeira estrofe.

## TESTE DE DURABILIDADE
Classificação: ALTA — dedicatórias não envelhecem.

## TESTE DE DIFERENCIAÇÃO
Classificação: COMMODITY — exceto a terceira estrofe.

## TESTE DE MEMORIZAÇÃO
Ideia principal clara? SIM
Qual é a ideia principal (em 1 frase): Este livro é para quem constrói com o conhecimento, não apenas opina.
Justificativa: Terceira estrofe carrega toda a carga.

## TESTE DE TRANSFORMAÇÃO
Ao terminar, o leitor consegue fazer o que antes não conseguia: Não aplicável.

## NOTA FINAL
Estrutura: 6 | Pedagogia: n/a | Clareza: 7 | Autoridade: 6 | Durabilidade: 9 | Diferenciação: 5 | Memorização: 6 | Transformação: n/a
**Nota Geral: 6**

## DECISÃO EDITORIAL
MANTER COM AJUSTES (reescrever segunda estrofe; considerar ancoragem mais específica na primeira)

---

# [P-00C2] — L1-00c2-promessa.md

## RESUMO EXECUTIVO
Nota: 8/10
Veredito: A

## O QUE FUNCIONA
- A estrutura é clara e honesta: separa o que o livro entrega, o que o repositório entrega, e o que a combinação dos dois entrega. Essa distinção tripla é rara e útil.
- A tabela de promessas por perfil (C-level / AI Engineer / Profissional de outra área) é precisa — cada linha entrega promessa específica e verificável, não genérica.
- A frase final "Quem opera só com o repositório sem ler o livro opera no escuro" é memorável, honesta e corajosa — desincentiva uso incompleto sem ser arrogante.
- A lista de sete pastas do repositório com descrição funcional é substancial e útil — o leitor que vê isso antes de comprar entende exatamente o que está comprando além do livro.
- "Vocabulário técnico profundo" com lista de termos específicos (tokens, RAG, MCP, reasoning models, evals, LLMOps, alignment, interpretabilidade mecanicista) é promessa auditável, não vaga.

## O QUE NÃO FUNCIONA
- A lista de "Nove Frameworks operacionais (F1 a F9)" na linha 14 nomeia os frameworks sem descrever o que cada um entrega em uma palavra — para quem ainda não sabe o que é F3, "escala de propriedade de agente" não diz nada operacional. A tabela de promessas por perfil não conecta os frameworks aos perfis.
- "Trinta exemplos memoráveis brasileiros" é afirmação que se repete em pelo menos três lugares no paratexto (aqui, na orelha esquerda, e na quarta capa). A repetição em paratexto curto dilui o impacto — o leitor começa a ignorar a afirmação.
- "com critério de recalibração quando a trilha não estiver servindo" na lista de entregas é jargão interno de produto que não comunica benefício ao leitor externo. Parece nota de rascunho.
- A afirmação "sem receita americana traduzida" (linha 16) é uma declaração de diferenciação que não está sustentada neste arquivo — o leitor precisa confiar na palavra do autor. Seria mais forte com um exemplo concreto do que "diferente" significa aqui.

## ACHADOS

### ACHADO 01
Categoria: P1
Problema: "com critério de recalibração quando a trilha não estiver servindo" na lista de entregas é jargão interno exposto ao leitor.
Por que é um problema: Leitor externo não sabe o que "trilha" significa ainda (o sistema de trilhas é apresentado mais à frente). A frase parece nota de produção vascada.
Impacto no leitor: Joana vai travar aqui. Não entende o que está sendo prometido.
Correção exata: Reescrever em linguagem de benefício direto.
Texto sugerido: `Trilhas de leitura por perfil (Iniciante, Intermediário, Avançado, Express Executivo), com guia de quando mudar de trilha se a atual não estiver entregando`
ROI: MÉDIO

### ACHADO 02
Categoria: P1
Problema: "sem receita americana traduzida" é afirmação não sustentada no paratexto.
Por que é um problema: É afirmação de diferenciação que o leitor não pode verificar com o texto disponível. Pode soar como marketing vazio.
Impacto no leitor: Leitor cético vai ignorar. Leitor ingênuo vai aceitar sem base.
Correção exata: Adicionar um exemplo concreto: o que seria "receita americana traduzida" vs. o que o livro faz diferente.
Texto sugerido: `Trinta exemplos memoráveis brasileiros — não estudos de caso americanos traduzidos, mas compostos pedagógicos construídos a partir de padrões observados em organizações brasileiras, com cargo, setor e números calibrados ao mercado nacional.`
ROI: MÉDIO

### ACHADO 03
Categoria: P2
Problema: "Trinta exemplos memoráveis brasileiros" repetido três vezes no paratexto (aqui, orelha esquerda, quarta capa) sem variação de enquadramento.
Por que é um problema: Repetição sem variação = o leitor para de processar a informação na segunda ocorrência.
Impacto no leitor: Reduz o impacto da afirmação em cada uma das três aparições.
Correção exata: Variar o ângulo em cada aparição. Aqui: foco na quantidade. Na orelha: foco na profundidade. Na quarta capa: foco no desfecho verificável.
Texto sugerido: n/a — depende de revisão coordenada dos três arquivos.
ROI: MÉDIO

### ACHADO 04
Categoria: P2
Problema: A lista de frameworks F1-F9 na seção de entregas não conecta frameworks a perfis de leitor.
Por que é um problema: O C-level não sabe quais frameworks são relevantes para ele vs. o AI Engineer. Lista não diferenciada = lista ignorada.
Impacto no leitor: Joana ignora a lista inteira de frameworks porque nenhum nome faz sentido para ela ainda.
Correção exata: Adicionar coluna de "perfil primário" na lista de frameworks, ou integrar à tabela de promessas por perfil.
Texto sugerido: n/a
ROI: BAIXO

## TESTE DA JOANA
Entenderia: SIM (maioria). A tabela de promessas por perfil é o ponto mais forte para ela.
O que ela entenderia: O que ela vai ganhar como executiva C-level. A diferença entre livro e repositório.
O que ela NÃO entenderia: "escala de propriedade de agente", "engenharia de prompt estendida", "cobertura de integrações" — terminologia técnica prematura na lista de frameworks.
Como corrigir: Reescrever os nomes dos frameworks na lista de entregas com linguagem de benefício, não de label técnico.

## TESTE DE DURABILIDADE
Classificação: MÉDIA
2 anos / 5 anos / 10 anos: As promessas de vocabulário técnico específico (MCP, reasoning models, LLMOps) são termos correntes em 2026 mas podem ser substituídos por terminologia nova. Os frameworks e o método são duráveis. A lista de pastas do repositório envelhece junto com o repositório.
Justificativa: O método da promessa é durável. Os substantivos específicos (MCP, RAG, LLMOps) têm vida útil de 3-5 anos como termos dominantes.

## TESTE DE DIFERENCIAÇÃO
Classificação: DIFERENCIADO
Justificativa: A estrutura tripla (livro = método / repositório = número / combinação = vantagem) é genuinamente diferenciada. Poucos livros técnicos têm repositório acompanhante com essa profundidade declarada.

## TESTE DE MEMORIZAÇÃO
Ideia principal clara? SIM
Qual é a ideia principal (em 1 frase): O livro dá o método; o repositório dá os artefatos executáveis; sem os dois juntos o leitor opera incompleto.
Justificativa: A frase "Quem opera só com o repositório sem ler o livro opera no escuro" faz o trabalho de memorização.

## TESTE DE TRANSFORMAÇÃO
Ao terminar, o leitor consegue fazer o que antes não conseguia:
- Entender exatamente o que está comprando antes de abrir o primeiro capítulo.
- Decidir qual trilha de leitura é a sua antes de começar.
- Saber que o repositório existe e para que serve.

## NOTA FINAL
Estrutura: 8 | Pedagogia: 8 | Clareza: 7 | Autoridade: 8 | Durabilidade: 7 | Diferenciação: 9 | Memorização: 8 | Transformação: 8
**Nota Geral: 8**

## DECISÃO EDITORIAL
MANTER COM AJUSTES (corrigir jargão interno, sustentar afirmação diferenciadora, variar enquadramento dos exemplos brasileiros)

---

# [P-00D] — L1-00d-agradecimentos.md

## RESUMO EXECUTIVO
Nota: 8/10
Veredito: A

## O QUE FUNCIONA
- O parágrafo sobre a comunidade brasileira de IA é genuíno e específico — nomeia categorias concretas (professores universitários, newsletters técnicas, fundadores, organizadores de meetups) sem listar nomes que envelhecem.
- A frase "onde acertei, acertamos juntos; onde errei, errei sozinho" é memorável, honesta e calibrada — clássico de agradecimentos bem escritos, mas funciona porque é verdadeiro para o contexto.
- A menção às referências intelectuais com justificativa específica por autor (Mollick, Huyen, Karpathy, LeCun, Hassabis, Amodei, Altman) é rara e substancial — cada menção tem razão explícita, não é name-dropping vazio.
- A distinção entre "pares nomeados na bibliografia" e "pares que preferiram anonimato" é eticamente correta e editorialmente honesta.

## O QUE NÃO FUNCIONA
- O parágrafo sobre CTOs e heads de tecnologia que "sentaram em sessões longas para validar exemplos" cria implicitamente uma promessa de peer review que não é cumprida formalmente — o livro não tem revisores nomeados, apenas informais. Isso pode ser questionado por leitor crítico que perguntar "quem são os CTOs que validaram?".
- "Demis Hassabis, Dario Amodei e Sam Altman por liderarem organizações que mantêm publicação técnica suficientemente aberta" — esta frase pode envelhecer mal se qualquer um deles deixar o cargo ou se o status de abertura das publicações mudar (OpenAI em particular tem histórico de menos abertura ao longo do tempo).
- O parágrafo sobre família é o mais genérico do texto — "madrugadas, renúncias de finais de semana, conversas interrompidas" é o conjunto padrão de todo agradecimento de não-ficção. Não é errado, mas é a parte mais fraca do arquivo.
- O arquivo não menciona Anthropic como provedor do modelo que aparentemente foi usado na produção — se foi, omitir é inconsistência ética; se não foi, então não é problema.

## ACHADOS

### ACHADO 01
Categoria: P1
Problema: A afirmação de que CTOs e heads de tecnologia validaram exemplos e "desafiaram generalizações cômodas" implica peer review informal sem registro público.
Por que é um problema: Leitor que questionar a metodologia vai perguntar "quem?" e a resposta é "anônimos". Isso pode ser usado para desacreditar a obra por quem tiver interesse.
Impacto no leitor: Leitor técnico avançado pode perceber como afirmação não falsificável.
Correção exata: Ou nomear pelo menos 2-3 revisores com permissão, ou reformular para deixar claro que foi processo de refinamento iterativo informal, não peer review formal.
Texto sugerido: `...evitaram que erros conceituais grandes chegassem à versão final. O processo de revisão foi informal — conversas privadas, não protocolos de peer review — e a responsabilidade pelos erros remanescentes é inteiramente do autor.`
ROI: MÉDIO

### ACHADO 02
Categoria: P1
Problema: "Demis Hassabis, Dario Amodei e Sam Altman por liderarem organizações que mantêm publicação técnica suficientemente aberta" — afirmação datada e frágil.
Por que é um problema: OpenAI em 2024-2026 reduziu progressivamente abertura técnica. A afirmação pode ser factualmente incorreta já na publicação e certamente vai envelhecer. Se Altman ou Hassabis deixarem seus cargos, a frase perde sentido.
Impacto no leitor: Leitor técnico vai contestar a caracterização da OpenAI como "suficientemente aberta".
Correção exata: Reformular para focar na organização, não no CEO, e qualificar "aberta" com especificidade.
Texto sugerido: `...Anthropic, OpenAI e Google DeepMind, que mantiveram publicação técnica suficientemente aberta — em graus e formatos variáveis — para permitir obra como esta.`
ROI: MÉDIO

### ACHADO 03
Categoria: P2
Problema: Parágrafo sobre família é o mais genérico e intercambiável do arquivo.
Por que é um problema: Baixa originalidade. Poderia existir em qualquer livro de não-ficção.
Impacto no leitor: Passa sem marcar. Não subtrai, mas não acrescenta.
Correção exata: Personalizar com um detalhe específico do processo de escrita deste livro, ou manter como está e aceitar a convenção.
Texto sugerido: n/a
ROI: BAIXO

## TESTE DA JOANA
Entenderia: SIM. O texto é fluente e acessível. Os nomes de referência (Mollick, Karpathy, LeCun) são reconhecíveis para ela se tiver acompanhado o debate.
O que ela NÃO entenderia: Por que Karpathy e LeCun têm posições distintas sobre IA — mas não precisa entender aqui.
Como corrigir: n/a.

## TESTE DE DURABILIDADE
Classificação: MÉDIA
Justificativa: A menção a CEOs pelo nome (Hassabis, Amodei, Altman) é o único elemento que pode envelhecer mal. Os demais são duráveis — autores de livros e comunidades não mudam de cargo.

## TESTE DE DIFERENCIAÇÃO
Classificação: DIFERENCIADO
Justificativa: Agradecimentos com justificativa específica por autor referenciado são raros em livros técnicos brasileiros.

## TESTE DE MEMORIZAÇÃO
Ideia principal clara? SIM
Qual é a ideia principal (em 1 frase): Este livro existe sobre ombros da comunidade brasileira de IA e de referências intelectuais internacionais específicas.
Justificativa: O parágrafo inicial e o de referências intelectuais carregam a memória.

## TESTE DE TRANSFORMAÇÃO
Ao terminar, o leitor consegue fazer o que antes não conseguia: Não aplicável diretamente — mas o contexto de onde o livro veio aumenta credibilidade da obra.

## NOTA FINAL
Estrutura: 8 | Pedagogia: n/a | Clareza: 9 | Autoridade: 8 | Durabilidade: 7 | Diferenciação: 8 | Memorização: 7 | Transformação: n/a
**Nota Geral: 8**

## DECISÃO EDITORIAL
MANTER COM AJUSTES (reformular afirmação sobre peer review e sobre abertura da OpenAI)

---

# [P-00E] — L1-00e-sobre-os-casos.md

## RESUMO EXECUTIVO
Nota: 9/10
Veredito: A+

## O QUE FUNCIONA
- Este é o arquivo mais intelectualmente honesto do paratexto inteiro. A declaração explícita de que os casos são "compostos pedagógicos" e que "o leitor crítico não pode verificar diretamente cada número" é corajosa e rara.
- A tabela de três tipos de caso (composto pedagógico / caso atribuído público / estudo ficcional) com contagem por tipo é modelo de transparência editorial — deveria ser copiado por outros autores de não-ficção técnica brasileira.
- "A escolha tem custo, e o custo é declarado" é a frase que define o padrão editorial desta obra. Ponto mais forte de todo o paratexto.
- A seção de "Convite à atribuição em edições futuras" com critérios específicos de elegibilidade (caderno de governança, eval harness, postmortem público) não é promessa vaga — é protocolo verificável.
- A nota explicando "Por que esta nota existe" encerra com precisão: "o pacto editorial precisa declarar com honestidade onde está a verificabilidade direta e onde está a fidelidade pedagógica."

## O QUE NÃO FUNCIONA
- "mais de 30 exemplos" na introdução e "30+ casos" na tabela são afirmações ligeiramente diferentes — se a contagem exata é relevante (e é, porque o livro usa "trinta exemplos memoráveis" como ponto de diferenciação), a inconsistência de "30+" vs. "mais de 30" é trivial mas perceptível.
- A seção "Como participar, se você é executivo de empresa brasileira" funciona bem como convite, mas os critérios de elegibilidade ("Postmortem público de incidente material") podem intimidar empresas que tenham postmortems relevantes mas nunca os tornaram públicos — criar barreira implícita onde havia abertura declarada.
- O "Apêndice N — Postura Metodológica" é referenciado como tratamento mais profundo da classificação epistemológica dos números, mas o leitor que lê este arquivo antes de abrir o livro não tem como acessar o Apêndice N. A referência cria promessa sem entrega imediata.
- "sem rodeio" na frase "declara, sem rodeio, a categoria de cada um" — esta locução é redundante em texto que já é direto. Soa como anúncio de direteza que não precisa de anúncio.

## ACHADOS

### ACHADO 01
Categoria: P2
Problema: "mais de 30 exemplos" vs. "30+ casos" — inconsistência de formulação para a mesma afirmação.
Por que é um problema: O livro usa "trinta exemplos memoráveis" como ponto de diferenciação. Variação na contagem (30, 30+, mais de 30) reduz credibilidade da afirmação.
Impacto no leitor: Leitor atento percebe imprecisão no exato dado que o livro usa como credencial.
Correção exata: Padronizar para "mais de 30" em todo o paratexto, ou declarar o número exato se conhecido.
Texto sugerido: `mais de 30 compostos pedagógicos` (uniforme em todos os arquivos)
ROI: BAIXO

### ACHADO 02
Categoria: P2
Problema: "Postmortem público de incidente material" como critério de elegibilidade para caso atribuído cria barreira implícita.
Por que é um problema: Empresas que têm postmortems relevantes raramente os tornaram públicos. O critério "público" elimina candidatos que poderiam participar com atribuição nominal de caso não-incidente.
Impacto no leitor: Não há impacto direto na leitura — mas reduz o pool de futuros colaboradores.
Correção exata: Reformular para "postmortem documentado" (com opção de publicação parcial mediante revisão editorial).
Texto sugerido: `Postmortem documentado de incidente material, com aprendizado consolidado e disposição para publicação parcial sob revisão editorial`
ROI: BAIXO

### ACHADO 03
Categoria: P2
Problema: "sem rodeio" é locução redundante em texto que já é direto.
Por que é um problema: Anunciar que vai ser direto antes de ser direto é sinal de texto que ainda não confia em si mesmo.
Impacto no leitor: Pequeno — mas o leitor técnico percebe.
Correção exata: Remover "sem rodeio" e deixar a frase andar sozinha.
Texto sugerido: `declara a categoria de cada um.`
ROI: BAIXO

## TESTE DA JOANA
Entenderia: SIM. A tabela de três tipos de caso é clara mesmo para não-técnico.
O que ela entenderia: Por que os casos não têm nome de empresa. Que é uma escolha honesta, não um problema.
O que ela NÃO entenderia: "classificação epistemológica" no penúltimo parágrafo — jargão desnecessário aqui.
Como corrigir: Substituir "classificação epistemológica" por "classificação de confiabilidade dos números".

## TESTE DE DURABILIDADE
Classificação: ALTA
Justificativa: A política de transparência é estrutural, não datada. Os critérios de elegibilidade para casos atribuídos são duráveis.

## TESTE DE DIFERENCIAÇÃO
Classificação: PROPRIEDADE INTELECTUAL
Justificativa: Nenhum outro livro técnico de IA em português (e poucos em inglês) declara explicitamente a metodologia e os limites de verificabilidade dos seus casos. Isso é diferencial real de integridade editorial.

## TESTE DE MEMORIZAÇÃO
Ideia principal clara? SIM
Qual é a ideia principal (em 1 frase): Os casos são pedagógicos, não atribuídos — a escolha tem custo declarado e o autor assume esse custo.
Justificativa: "A escolha tem custo, e o custo é declarado" é a frase mais citável do paratexto inteiro.

## TESTE DE TRANSFORMAÇÃO
Ao terminar, o leitor consegue fazer o que antes não conseguia:
- Avaliar os exemplos do livro com o critério correto (plausibilidade do padrão, não verificabilidade do número específico).
- Distinguir entre os três tipos de evidência que o livro usa.

## NOTA FINAL
Estrutura: 9 | Pedagogia: 9 | Clareza: 9 | Autoridade: 10 | Durabilidade: 9 | Diferenciação: 10 | Memorização: 9 | Transformação: 8
**Nota Geral: 9**

## DECISÃO EDITORIAL
MANTER (ajustes menores de consistência e remoção de jargão pontual)

---

# [P-01] — L1-01-prefacio.md

## RESUMO EXECUTIVO
Nota: 8/10
Veredito: A

## O QUE FUNCIONA
- A abertura com analogia de ondas tecnológicas (nuvem → mobile → big data → IA) é bem calibrada — ancora o argumento em experiência profissional real antes de fazer a afirmação central.
- "A IA amplifica julgamento" é a formulação mais poderosa do prefácio e provavelmente a mais citável de todo o paratexto. É genuinamente original como enquadramento.
- "A vantagem migrou da execução para a interpretação" é a segunda afirmação mais forte — diferencia esta obra da maioria dos livros de adoção de IA que focam em execução.
- A estrutura em quatro seções (diferença / erro / por que escrevi / o que está em jogo) é clássica de prefácio bem construído — cada seção tem papel claro.
- "Podia ter feito o caminho fácil. Catálogo de prompts, tutorial de ferramentas, guia de adoção corporativa. Conteúdo desse tipo se publica em três meses, vende razoavelmente, e expira em outros três." — honestidade editorial rara e eficaz.
- A frase final é forte: "Compreender, no fim das contas, sempre foi a vantagem competitiva mais subestimada da história da tecnologia."

## O QUE NÃO FUNCIONA
- "Quem soube ler a internet em 1996 ganhou uma década. Quem soube ler a nuvem em 2008 ganhou uma década." — essas afirmações são não-verificáveis como enunciadas. Quem é o "quem"? Ganhou uma década em qual métrica? O argumento é retoricamente poderoso mas epistemicamente fraco. Especialista em IA e fact-checker vai marcar isso.
- "Em 2028, segundo as projeções mais conservadoras, essa distância será inegociável" — "projeções mais conservadoras" de quem? Este é o tipo de afirmação que envelhece em 24 meses e pode parecer errado ou certeiro por acidente. Sem fonte, é argumento de autoridade sem autoridade.
- "A obsessão é com benchmarks, rankings, versões, lançamentos. Empresas trocam fornecedor toda semana" — hipérbole que o leitor técnico reconhece como tal. "toda semana" não é literal e soa como exagero retórico, reduzindo credibilidade da afirmação mais abrangente.
- O prefácio não menciona os Nove Princípios Permanentes pelo nome — menciona apenas "Nove Princípios Permanentes da Inteligência Artificial" sem listá-los ou criar curiosidade sobre o sistema. Para um prefácio que é o primeiro contato substantivo do leitor com o livro, essa omissão é oportunidade perdida.
- A seção "Por que escrevi este livro" duplica parte do argumento de "A diferença que muda tudo" — especialmente a dicotomia ferramentas vs. princípios, que aparece em ambas as seções sem escalada de argumento.

## ACHADOS

### ACHADO 01
Categoria: P1
Problema: "Quem soube ler a internet em 1996 ganhou uma década" — afirmação não verificável como enunciada.
Por que é um problema: É o tipo de afirmação retórica que o leitor técnico percebe como retórica. Reduz credibilidade do argumento analítico que o cerca.
Impacto no leitor: Editor de aquisição vai sinalizar. Especialista técnico vai marcar como não-falsificável.
Correção exata: Qualificar com especificidade ou reformular como tese, não como fato histórico.
Texto sugerido: `Os profissionais e empresas que entenderam a internet antes do ciclo de adoção em massa ganharam vantagem estrutural que durou uma década — não por ter acesso, mas por ter compreensão. A mesma lógica se repetiu com a nuvem. Em IA, o padrão deve se repetir, com velocidade maior.`
ROI: MÉDIO

### ACHADO 02
Categoria: P1
Problema: "Em 2028, segundo as projeções mais conservadoras, essa distância será inegociável" — afirmação sem fonte, com qualificador não atribuído.
Por que é um problema: "Projeções mais conservadoras" de quem? Esta frase vai envelhecer ou como acerto fortuito ou como erro verificável. Sem fonte, é argumento de autoridade sem autoridade — o que contradiz o padrão intelectual do restante do livro.
Impacto no leitor: Leitor técnico descredencia a afirmação inteira. Leitor ingênuo aceita como fato.
Correção exata: Ou atribuir a fonte específica, ou reformular como julgamento autoral explícito.
Texto sugerido: `Na minha avaliação — baseada na velocidade atual de adoção e no histórico de ciclos anteriores — essa distância vai se tornar estrutural nos próximos dois anos.`
ROI: MÉDIO

### ACHADO 03
Categoria: P1
Problema: "Empresas trocam fornecedor toda semana" — hipérbole que reduz credibilidade do argumento.
Por que é um problema: O argumento sobre obsessão com velocidade é válido e importante. A hipérbole "toda semana" abre flanco para que o leitor descarte o argumento inteiro como exagero.
Impacto no leitor: Leitor técnico para de processar o argumento e foca no exagero.
Correção exata: Reformular com precisão que mantém o impacto sem hipérbole verificável.
Texto sugerido: `Empresas trocam fornecedor a cada ciclo de lançamento, equipes refazem prompts a cada versão nova, dirigentes pedem estratégia de IA em reunião sem saber o que pediram.`
ROI: MÉDIO

### ACHADO 04
Categoria: P1
Problema: Os Nove Princípios Permanentes não são mencionados pelo nome nem listados no prefácio — o primeiro contato substantivo do leitor com o sistema central do livro é perdido.
Por que é um problema: O prefácio é onde o leitor decide se vai continuar. Não nomear o sistema central deixa a proposta de valor incompleta.
Impacto no leitor: Joana fecha o prefácio sabendo que existe um "sistema de nove princípios" mas sem nenhuma ideia do que são — oportunidade de gancho perdida.
Correção exata: Adicionar parágrafo de um a dois períodos que listam os nomes dos nove princípios ou ao menos cria curiosidade específica sobre eles.
Texto sugerido: `Os nove princípios — Camada Dupla, Plausibilidade, Custo Composto, Extremidades, Encaixe, Termômetro, Autonomia Proporcional, Responsabilidade Indelegável, Operador — formam o vocabulário que costura toda a obra. Cada um tem nome porque nome cria memória, e memória cria critério.`
ROI: ALTO

### ACHADO 05
Categoria: P2
Problema: Seções "A diferença que muda tudo" e "Por que escrevi este livro" duplicam o argumento ferramentas vs. princípios sem escalada.
Por que é um problema: O leitor de não-ficção técnica percebe repetição sem progressão e começa a pular parágrafos.
Impacto no leitor: Ritmo do prefácio perde velocidade na segunda metade.
Correção exata: Distinguir claramente: a primeira seção é o diagnóstico (o que a IA faz de diferente); a segunda deve ser a resposta editorial (por que este livro específico, não qualquer livro de princípios). Eliminar sobreposição.
Texto sugerido: n/a — requer revisão estrutural das duas seções.
ROI: MÉDIO

## TESTE DA JOANA
Entenderia: SIM. O prefácio é um dos textos mais acessíveis do paratexto.
O que ela entenderia: Por que IA é diferente das outras ondas tecnológicas. Por que este livro é diferente de guias de ferramentas.
O que ela NÃO entenderia: "Projeções mais conservadoras" — vai querer saber de quem. "Benchmarks" — pode precisar de explicação, mas é termo que ela provavelmente conhece.
Como corrigir: Atribuir a afirmação de 2028 ou reformular como julgamento autoral explícito.

## TESTE DE DURABILIDADE
Classificação: ALTA
2 anos / 5 anos / 10 anos: O argumento central (IA amplifica julgamento, vantagem migrou da execução para a interpretação) é durável. A afirmação sobre 2028 é o único elemento datado e já está qualificada como estimativa.
Justificativa: Prefácios que argumentam por princípio envelhecem melhor que prefácios que argumentam por dado. Este é majoritariamente de princípio.

## TESTE DE DIFERENCIAÇÃO
Classificação: DIFERENCIADO
Justificativa: "A IA amplifica julgamento" é formulação original e diferenciada. Não aparece assim em nenhum dos livros da régua de comparação.

## TESTE DE MEMORIZAÇÃO
Ideia principal clara? SIM
Qual é a ideia principal (em 1 frase): IA amplifica julgamento — e por isso estudar princípios vale mais que estudar ferramentas.
Justificativa: A seção "A diferença que muda tudo" entrega essa ideia com clareza.

## TESTE DE TRANSFORMAÇÃO
Ao terminar, o leitor consegue fazer o que antes não conseguia:
- Articular por que IA é diferente das outras ondas tecnológicas (amplifica a camada cognitiva, não operacional).
- Reconhecer o erro de categoria entre estudar ferramentas vs. estudar princípios.

## NOTA FINAL
Estrutura: 8 | Pedagogia: 7 | Clareza: 8 | Autoridade: 7 | Durabilidade: 8 | Diferenciação: 9 | Memorização: 9 | Transformação: 8
**Nota Geral: 8**

## DECISÃO EDITORIAL
MANTER COM AJUSTES (atribuir afirmação de 2028, cortar hipérbole "toda semana", adicionar gancho dos nove princípios, distinguir as duas seções que se sobrepõem)

---

# [P-02] — L1-02-como-ler.md

## RESUMO EXECUTIVO
Nota: 7/10
Veredito: B

## O QUE FUNCIONA
- A anatomia de capítulo em tabela (10 blocos com função explícita de cada um) é ferramenta pedagógica genuinamente útil — o leitor que entende a estrutura antes de começar vai absorver melhor cada elemento.
- As convenções visuais em tabela (▲ Alerta, ✸ Insight, Para Executivos, Na Prática) são claras e funcionais — o leitor sabe o que esperar de cada marcação.
- A seção "O que fazer ao terminar" com protocolo de consolidação em 6 passos é o tipo de instrução pós-leitura que livros técnicos raramente fornecem e que aumenta retenção real.
- Os três caminhos de leitura estão descritos com clareza suficiente para que o leitor escolha o seu sem precisar de ajuda externa.

## O QUE NÃO FUNCIONA
- O "Caminho 3 — Pelos princípios" (leia pela camada-mãe, depois o capítulo em profundidade, depois os frameworks, depois o exemplo) é descrito de forma abstrata demais para ser seguido sem exemplo concreto. Nenhum dos nove princípios é mencionado, nenhuma rota específica é demonstrada.
- A frase "não por convenção, mas porque ela espelha como adultos profissionais realmente aprendem conceito novo" é afirmação pedagógica não sustentada. Qual teoria de aprendizagem de adultos sustenta essa sequência específica? Referência a Bloom, Kolb, ou qualquer framework de andragogia tornaria a afirmação defensável. Sem referência, é opinião vestida de fato.
- A seção "O que fazer ao terminar" descreve "Assinar duas newsletters recomendadas" sem indicar quais newsletters ou onde encontrá-las. Instrução sem destino.
- "Consultar a documentação atualizada dos fornecedores periodicamente" — qual periodicidade? "Periodicamente" é não-instrução.
- O arquivo não menciona a duração estimada de leitura para nenhuma das três trilhas — essa informação vem apenas no Mapa de Leitura por Nível, que o leitor ainda não leu quando encontra este arquivo.

## ACHADOS

### ACHADO 01
Categoria: P1
Problema: "Caminho 3 — Pelos princípios" é descrito sem exemplo concreto de rota.
Por que é um problema: É o caminho mais diferenciado e mais difícil de seguir. Sem exemplo — "parta do Princípio X, leia o capítulo Y, depois o framework F3, depois o exemplo E7" — o leitor não consegue executar a instrução.
Impacto no leitor: Joana vai ler o Caminho 3 e não saber como começar. Vai default para o Caminho 1.
Correção exata: Adicionar um exemplo de rota completa para um princípio, com capítulos e frameworks específicos.
Texto sugerido: `Por exemplo: para internalizar o Princípio da Responsabilidade Indelegável, leia C19 (segurança), depois C24 (governança), depois F6, depois o exemplo do banco médio no C28. Em vinte e quatro horas de leitura focada, você terá o princípio operacionalizado.`
ROI: ALTO

### ACHADO 02
Categoria: P1
Problema: "não por convenção, mas porque ela espelha como adultos profissionais realmente aprendem conceito novo" — afirmação pedagógica sem referência.
Por que é um problema: A afirmação implica que a sequência de 10 blocos foi derivada de teoria de aprendizagem. Se não foi, é afirmação de autoridade sem base. Se foi, deve citar a fonte.
Impacto no leitor: Leitor com background em educação ou design instrucional vai questionar.
Correção exata: Ou referenciar a base pedagógica (ex: "baseada no ciclo experiencial de Kolb e na taxonomia de Bloom") ou reformular como escolha editorial explícita.
Texto sugerido: `Esta obra foi projetada com sequência deliberada: cada bloco tem função específica, construída para que o conceito seja primeiro intuído, depois ancorizado em analogia, depois rigorizado, depois aplicado — ciclo que a prática de ensino em contexto executivo mostrou ser mais eficaz que exposição direta ao rigor.`
ROI: MÉDIO

### ACHADO 03
Categoria: P1
Problema: "Assinar duas newsletters recomendadas" sem indicar quais ou onde encontrar a lista.
Por que é um problema: É instrução sem destino. O leitor que quer seguir o protocolo de consolidação fica parado neste passo.
Impacto no leitor: Frustração. A instrução perde credibilidade.
Correção exata: Adicionar referência ao apêndice que tem a lista, ou nomear 2-3 newsletters diretamente aqui.
Texto sugerido: `Assinar duas newsletters recomendadas — ver lista curada no Apêndice F (Comunidade Brasileira de IA em 2026) e no Apêndice E (Leituras Complementares).`
ROI: MÉDIO

### ACHADO 04
Categoria: P2
Problema: "Consultar a documentação atualizada dos fornecedores periodicamente" — instrução sem periodicidade.
Por que é um problema: "Periodicamente" é não-instrução. O leitor não sabe se é semanal, mensal, trimestral.
Impacto no leitor: A instrução é ignorada por falta de especificidade.
Correção exata: Definir periodicidade ou vincular a gatilho.
Texto sugerido: `Consultar a documentação de release notes dos seus dois ou três fornecedores principais a cada trimestre, ou quando lançarem versão principal.`
ROI: BAIXO

### ACHADO 05
Categoria: P2
Problema: Nenhuma das três trilhas de leitura menciona duração estimada neste arquivo.
Por que é um problema: O leitor que encontra "Como Ler Este Livro" antes de chegar ao Mapa de Leitura não tem informação de tempo para escolher trilha.
Impacto no leitor: Escolha de trilha sem critério de orçamento de tempo = escolha mal informada.
Correção exata: Adicionar estimativa de horas entre parênteses ao lado de cada caminho, com referência ao Mapa para detalhamento.
Texto sugerido: `**Caminho 1 — Linear** (~50h para leitura completa; ~20h para leitura seletiva)`
ROI: BAIXO

## TESTE DA JOANA
Entenderia: SIM, majoritariamente. A tabela de blocos pedagógicos é muito útil para ela.
O que ela entenderia: Como o livro está organizado, o que cada elemento visual significa, o que fazer depois de terminar.
O que ela NÃO entenderia: O Caminho 3 sem exemplo concreto. Como encontrar as newsletters recomendadas.
Como corrigir: Exemplo concreto no Caminho 3. Referência explícita para newsletters.

## TESTE DE DURABILIDADE
Classificação: ALTA
Justificativa: Instruções de leitura são atemporais. As convenções visuais não envelhecem. A única vulnerabilidade é "documentação dos fornecedores" — que é instrução correta mas com URLs que mudam.

## TESTE DE DIFERENCIAÇÃO
Classificação: DIFERENCIADO
Justificativa: A anatomia explícita de capítulo em tabela e o protocolo de consolidação pós-leitura são diferenciais reais. A maioria dos livros técnicos não tem instrução explícita de como consolidar após a leitura.

## TESTE DE MEMORIZAÇÃO
Ideia principal clara? SIM
Qual é a ideia principal (em 1 frase): Este livro tem três caminhos de leitura e uma estrutura pedagógica explícita — use o que serve ao seu nível e objetivo.
Justificativa: A tabela de blocos e os três caminhos são estrutura memorável.

## TESTE DE TRANSFORMAÇÃO
Ao terminar, o leitor consegue fazer o que antes não conseguia:
- Escolher conscientemente como ler o livro, em vez de ler por padrão linear.
- Reconhecer o papel de cada elemento pedagógico quando encontrar na leitura.
- Saber o que fazer com o conhecimento depois de terminar o livro.

## NOTA FINAL
Estrutura: 8 | Pedagogia: 7 | Clareza: 7 | Autoridade: 7 | Durabilidade: 9 | Diferenciação: 8 | Memorização: 7 | Transformação: 8
**Nota Geral: 7**

## DECISÃO EDITORIAL
MANTER COM AJUSTES (exemplo concreto no Caminho 3, referência para newsletters, atribuição pedagógica da sequência de blocos)

---

# [P-03] — L1-03-introducao.md

## RESUMO EXECUTIVO
Nota: 8/10
Veredito: A

## O QUE FUNCIONA
- A cena de abertura (sala de diretoria, slides cheios de siglas, dois executivos no corredor) é o melhor parágrafo de todo o paratexto em termos de identificação do leitor. É concreta, específica e cinematográfica sem ser melodramática.
- "Por que tokens custam mais em modelos diferentes?" seguido por lista de perguntas técnicas específicas é excelente diagnóstico da lacuna — o leitor que não sabe responder nenhuma delas sente a necessidade do livro imediatamente.
- As quatro apostas estão bem estruturadas e cada uma tem argumento próprio. A progressão (conceitos → aplicação → profundidade → sistema citável) é lógica e escalada.
- A lista de "dez coisas específicas que separam quem entende de quem só usa" na seção A Promessa é auditável — o leitor pode voltar ao final e verificar se o livro cumpriu.
- "Em português, ainda em 2026, não há uma obra que cubra tudo isso com profundidade real" — afirmação audaciosa, provavelmente verdadeira, e verificável pelo leitor que fizer a busca.

## O QUE NÃO FUNCIONA
- A epígrafe de abertura ("Quando uma tecnologia muda mais rápido do que sua capacidade de entendê-la...") é longa demais para epígrafe — três períodos compostos. Epígrafe eficaz tem no máximo dois períodos curtos. A densidade cognitiva na abertura antes do primeiro parágrafo é excessiva.
- "Multiplique essa cena por milhares de empresas, por milhões de profissionais" — a escalada de "milhares" para "milhões" é hipérbole retórica não sustentada. No Brasil em 2026, o número de profissionais em posição de tomar decisões de IA em reunião executiva é significativamente menor que "milhões".
- A Aposta 2 ("conceitos sem aplicação são abstração morta") começa com crítica a "uma tradição perigosa em livros de tecnologia" sem nomear exemplos — afirmação de categoria que pode ser percebida como ataque velado a concorrentes sem evidência.
- O Arco Narrativo (seção que descreve as cinco partes) é a seção mais fraca da introdução — é descrição de tabela de conteúdo em prosa, não argumento. Duplica o Sumário sem acrescentar perspectiva.
- A promessa de "entre trinta e cinco e cinquenta horas" para ler o livro aparece na última seção sem contexto — são horas de leitura ativa, leitura total, ou leitura com exercícios? A ambiguidade na estimativa de tempo pode criar frustração em leitores mais lentos ou mais rápidos.

## ACHADOS

### ACHADO 01
Categoria: P1
Problema: Epígrafe de abertura tem três períodos compostos — excessivamente densa para função de epígrafe.
Por que é um problema: Epígrafe é gancho, não argumento. Leitor que trava na epígrafe chega ao primeiro parágrafo já cansado cognitivamente.
Impacto no leitor: Joana vai reler a epígrafe duas vezes e ainda não vai ter certeza do que significa.
Correção exata: Reduzir para uma sentença de impacto, ou substituir por uma das afirmações mais cirúrgicas do prefácio.
Texto sugerido: `"Quando uma tecnologia muda mais rápido do que sua capacidade de entendê-la, você perde o controle e a oportunidade ao mesmo tempo."`
ROI: MÉDIO

### ACHADO 02
Categoria: P1
Problema: "Multiplique essa cena por milhares de empresas, por milhões de profissionais" — hipérbole não sustentada.
Por que é um problema: O leitor técnico sabe que o universo de profissionais em posição de tomar decisões executivas de IA no Brasil não é "milhões". A hipérbole abre flanco crítico.
Impacto no leitor: Leitor cético para de confiar no argumento analítico do parágrafo.
Correção exata: Reformular com estimativa defensável ou generalizar sem número.
Texto sugerido: `Multiplique essa cena por milhares de salas de reunião pelo país, e está pintado o retrato de uma geração inteira...`
ROI: MÉDIO

### ACHADO 03
Categoria: P1
Problema: A seção "O Arco Narrativo" é redundante com o Sumário — descrição de estrutura em prosa sem argumento adicional.
Por que é um problema: O leitor que já leu o Sumário (que vem antes na ordem do paratexto) vai pular esta seção. O leitor que não leu vai preferir o Sumário formatado.
Impacto no leitor: Seção ignorada. Perde ritmo da introdução.
Correção exata: Substituir descrição estrutural por argumento sobre por que a ordem das cinco partes é a que é — o que o leitor ganha ao percorrer o arco na sequência proposta.
Texto sugerido: Reescrever como "A ordem deliberada: por que começar pelos fundamentos antes de chegar à governança" — argumento pedagógico, não descrição.
ROI: MÉDIO

### ACHADO 04
Categoria: P1
Problema: Aposta 2 critica "livros de tecnologia" que tratam conceitos no vácuo sem nomear exemplos — pode ser percebida como ataque implícito a concorrentes.
Por que é um problema: Afirmação de categoria sobre "livros de tecnologia" sem exemplos é ou difamação implícita ou afirmação não verificável. Nenhum dos dois serve bem ao livro.
Impacto no leitor: Leitor que ama algum desses livros vai se defender em vez de concordar.
Correção exata: Reformular como limitação de formato, não como crítica a autores.
Texto sugerido: `Existe uma limitação recorrente em livros de tecnologia: o formato de capítulo independente tende a apresentar conceitos como se vivessem no vácuo, porque conectar profundamente RAG ao agente ao trade-off de custo exige um sistema que sustente a conexão. Este livro propõe esse sistema.`
ROI: MÉDIO

### ACHADO 05
Categoria: P2
Problema: "entre trinta e cinco e cinquenta horas" é estimativa de tempo ambígua — não especifica se inclui exercícios, revisão e roadmap pessoal.
Por que é um problema: Leitor que só lê o texto pode terminar em 20 horas. Leitor que faz todos os exercícios pode levar 60. A ambiguidade cria expectativa incorreta.
Impacto no leitor: Frustração ou surpresa desagradável ao descobrir que "50 horas" incluía exercícios não opcionais.
Correção exata: Especificar o que conta nas horas estimadas.
Texto sugerido: `entre trinta e cinco e cinquenta horas de leitura ativa com os exercícios — ou vinte a trinta horas para a trilha de leitura seletiva descrita no Mapa de Leitura por Nível`
ROI: BAIXO

### ACHADO 06
Categoria: P2
Problema: Item 5 da lista de promessas — "Construir prompts profissionais que produzem resultados consistentes, com método e estrutura pelas extremidades" — usa "pelas extremidades" como jargão interno não explicado ainda.
Por que é um problema: "Extremidades" é o Princípio 4 (P4 — Extremidades), que ainda não foi apresentado. O leitor da introdução não tem referência.
Impacto no leitor: Joana vai travar na frase e passar sem entender.
Correção exata: Substituir por linguagem descritiva ou adicionar referência.
Texto sugerido: `Construir prompts profissionais que produzem resultados consistentes, com método e estrutura na abertura e no fechamento da instrução`
ROI: BAIXO

## TESTE DA JOANA
Entenderia: SIM (maioria). A cena de abertura e a lista de perguntas técnicas são especialmente eficazes para ela.
O que ela entenderia: Por que o livro existe. O que vai aprender. Que o problema descrito é real e ela já viveu.
O que ela NÃO entenderia: A epígrafe na primeira leitura. "Estrutura pelas extremidades" sem contexto. O Arco Narrativo (vai pular).
Como corrigir: Simplificar epígrafe. Substituir jargão interno na lista de promessas.

## TESTE DE DURABILIDADE
Classificação: ALTA
2 anos / 5 anos / 10 anos: O diagnóstico da lacuna (falta de obra técnica profunda em português) pode se tornar falso se outros livros forem publicados. A cena da sala de diretoria pode perder ressonância se o nível de conhecimento executivo sobre IA aumentar significativamente.
Justificativa: O argumento central (princípios > ferramentas) é durável. Os exemplos específicos de perguntas técnicas (RAG, MCP, agentes) podem precisar de atualização em 5+ anos se a terminologia mudar.

## TESTE DE DIFERENCIAÇÃO
Classificação: DIFERENCIADO
Justificativa: A lista de dez promessas auditáveis ao final é genuinamente diferenciada — a maioria das introduções faz promessas vagas. Aqui, o leitor tem critério de avaliação explícito.

## TESTE DE MEMORIZAÇÃO
Ideia principal clara? SIM
Qual é a ideia principal (em 1 frase): O livro existe para fechar a lacuna de obra técnica profunda sobre IA em português, com sistema próprio de nove princípios que sobrevive à troca de modelos.
Justificativa: As Quatro Apostas entregam a ideia com clareza progressiva.

## TESTE DE TRANSFORMAÇÃO
Ao terminar, o leitor consegue fazer o que antes não conseguia:
- Articular exatamente quais lacunas de conhecimento técnico precisa fechar.
- Ter critério explícito para avaliar se o livro cumpriu o que prometeu.
- Reconhecer a cena da sala de diretoria e nomear o problema.

## NOTA FINAL
Estrutura: 8 | Pedagogia: 8 | Clareza: 7 | Autoridade: 8 | Durabilidade: 8 | Diferenciação: 9 | Memorização: 8 | Transformação: 9
**Nota Geral: 8**

## DECISÃO EDITORIAL
MANTER COM AJUSTES (simplificar epígrafe, cortar hipérbole numérica, substituir Arco Narrativo por argumento pedagógico, remover jargão interno da lista de promessas)

---

# [P-04] — L1-04-sumario.md

## RESUMO EXECUTIVO
Nota: 7/10
Veredito: B

## O QUE FUNCIONA
- A coluna "Princípio central" no sumário de capítulos é diferencial editorial genuíno — o leitor que conhece os nove princípios pode navegar por princípio, não apenas por capítulo. Nenhum sumário equivalente em livros de IA faz isso.
- A separação clara entre Frameworks (F1-F9), Apêndices (A-Q) e Capítulos cria três camadas de referência que o leitor pode usar de formas diferentes.
- A contagem de apêndices (A até Q = 17 apêndices) é substancial e sinaliza obra de referência, não apenas de leitura linear.

## O QUE NÃO FUNCIONA
- O capítulo 14C ("Spec-Driven Development") tem quatro princípios atribuídos (Operador, Camada Dupla, Autonomia Proporcional, Responsabilidade Indelegável) — o dobro de qualquer outro capítulo. Isso sinaliza ou que o capítulo está tentando cobrir demais, ou que a atribuição de princípios precisa de curadoria.
- A numeração de capítulos é inconsistente: existe 14, 14C e 14B — dois sub-capítulos do 14, mas numerados fora de ordem (14C antes de 14B na listagem). Esta ordem vai confundir o leitor que procura pelo número.
- As páginas do paratexto inicial usam numeração romana (ii, iii, vi, xi, xv, xxi, xxvii, xxxiii, xlii), mas os Frameworks começam em 630 e os Apêndices em 681 — o gap entre o último capítulo e os frameworks não está representado. Onde ficam os capítulos 17-28 no mapa de páginas?
- O Sumário não indica quais capítulos têm "Autoavaliação", "Checklist" ou "Exercícios" — elementos que o arquivo "Como Ler" descreve como essenciais. Leitor que usa o sumário como índice de navegação não encontra esses elementos.
- O capítulo 28 (Interpretabilidade Mecanicista) aparece listado mas sem número explícito — há "28" implícito na sequência, mas a tabela da Parte 5 para em "28" sem que haja indicação de que 28 é o último capítulo.

## ACHADOS

### ACHADO 01
Categoria: P1
Problema: Capítulos 14C e 14B aparecem nessa ordem (C antes de B) na listagem do Sumário — numeração fora de sequência lógica.
Por que é um problema: Leitor que procura "14B" vai encontrá-lo depois de "14C" na tabela, o que é contraintuitivo. Em ebook com links de navegação, a ordem vai confundir.
Impacto no leitor: Frustração na navegação. Impressão de erro editorial.
Correção exata: Reordenar para 14, 14B, 14C na listagem, ou renumerar os sub-capítulos para 14A, 14B, 14C em ordem lógica.
Texto sugerido: n/a — depende da numeração canônica do manuscrito.
ROI: ALTO

### ACHADO 02
Categoria: P1
Problema: Capítulo 14C tem quatro princípios atribuídos — o dobro de qualquer outro. Sinaliza sobrecarga temática.
Por que é um problema: Ou o capítulo está tentando cobrir mais do que um capítulo suporta, ou a atribuição de princípios está errada. Em ambos os casos, o sumário sinaliza problema no capítulo correspondente.
Impacto no leitor: Expectativa de capítulo excessivamente denso ou difuso.
Correção exata: Revisar a atribuição de princípios do 14C — capítulos devem ter 1-2 princípios centrais, não 4.
Texto sugerido: n/a — requer revisão do capítulo.
ROI: MÉDIO

### ACHADO 03
Categoria: P2
Problema: Numeração de páginas dos capítulos 1-28 não aparece no sumário — apenas as páginas das Partes (pg 34, pg 146, pg 187, pg 259, pg 298) estão indicadas.
Por que é um problema: Sumário sem numeração de página por capítulo é sumário incompleto. O leitor não consegue ir diretamente ao capítulo 19, por exemplo.
Impacto no leitor: Sumário perde função de índice de navegação.
Correção exata: Adicionar coluna de página por capítulo, mesmo que seja com marcador de "a definir após diagramação".
Texto sugerido: n/a — depende da diagramação final.
ROI: ALTO

### ACHADO 04
Categoria: P2
Problema: Paratexto usa numeração romana (ii, iii...) mas a tabela do sumário mescla romano e arábico sem transição explícita.
Por que é um problema: Em ebook, a numeração dupla pode criar indexação inconsistente se o motor de navegação não suportar mistura.
Impacto no leitor: Problema técnico de navegação em ebook.
Correção exata: Adicionar nota "(paginação romana no paratexto; arábica a partir da p. 1 no corpo da obra)" na entrada do sumário.
Texto sugerido: n/a
ROI: BAIXO

## TESTE DA JOANA
Entenderia: SIM — a estrutura em cinco partes é clara. A coluna de princípios vai intrigar positivamente.
O que ela NÃO entenderia: A diferença entre "14", "14C" e "14B". Por que a ordem é 14, 14C, 14B.
Como corrigir: Reordenar e renomear os sub-capítulos.

## TESTE DE DURABILIDADE
Classificação: ALTA — sumário é elemento estrutural, não datado.

## TESTE DE DIFERENCIAÇÃO
Classificação: DIFERENCIADO — coluna de Princípio central por capítulo é formato único.

## TESTE DE MEMORIZAÇÃO
Ideia principal clara? SIM — cinco partes, 28 capítulos, 9 frameworks, 17 apêndices.
Qual é a ideia principal (em 1 frase): Obra de referência estruturada em camadas de competência crescente, navegável por capítulo ou por princípio.
Justificativa: A arquitetura do sumário comunica a ambição da obra.

## TESTE DE TRANSFORMAÇÃO
Ao terminar, o leitor consegue fazer o que antes não conseguia: Não aplicável — elemento de navegação.

## NOTA FINAL
Estrutura: 6 | Pedagogia: 7 | Clareza: 6 | Autoridade: 8 | Durabilidade: 9 | Diferenciação: 9 | Memorização: 7 | Transformação: n/a
**Nota Geral: 7**

## DECISÃO EDITORIAL
MANTER COM AJUSTES (corrigir ordem 14B/14C, revisar atribuição quádrupla de princípios no 14C, adicionar numeração de página por capítulo)

---

# [P-05] — L1-05-mapa-de-leitura-por-nivel.md

## RESUMO EXECUTIVO
Nota: 9/10
Veredito: A+

## O QUE FUNCIONA
- O diagnóstico em cinco perguntas com contagem de "sim" para definir trilha é mecanismo pedagógico elegante e honesto — força o leitor a se posicionar antes de começar.
- A tabela de fluxo entre trilhas (avança quando / recua quando) é genuinamente diferenciada — poucos livros técnicos têm critério explícito de recalibração de trilha. É operacionalizável imediatamente.
- A frase "Voltar uma trilha é movimento normal, não custo de orgulho" desfaz a resistência psicológica ao downgrade de trilha — intervenção comportamental discreta e eficaz.
- Os roteiros de tempo (8h / 20h / 50h) com sequência explícita de capítulos são o nível de especificidade que Joana precisa para decidir como vai ler.
- A tabela de bandeiras por capítulo (Iniciante / Iniciante+Intermediário / etc.) com lista de capítulos por nível é referência operacional de alta utilidade.
- A seção "Como saber se a trilha está funcionando" com tabela de sinais observados e ações correspondentes é design instrucional sólido.

## O QUE NÃO FUNCIONA
- O diagnóstico usa "operou, em ambiente profissional, um agente baseado em LLM, com loop de planejamento, ação e observação" — a exigência de "loop de planejamento, ação e observação" é altamente específica e pode classificar erroneamente profissionais que operaram agentes com arquitetura diferente (ex: agentes baseados em tool-calling sem loop explícito de observação). A pergunta vai subcategorizar incorretamente.
- A Trilha Avançado lista "C00P" e "C00M" como primeira prioridade do "Sistema intelectual" — mas esses capítulos são o Manifesto, que o leitor avançado provavelmente já leu ou vai pular. A instrução de "comece pelos manifestos" para o leitor avançado é contraintuitiva.
- O roteiro de 8 horas inclui "F1 (Método de Decisão)" sem mencionar que F1 está no Apêndice de Frameworks — leitor que segue o roteiro linear pode não saber onde procurar F1.
- A afirmação "A leitura desonesta cobra o preço típico do leitor que escolhe a trilha que aspira ser, em vez da trilha que efetivamente serve agora" é válida mas tem tom levemente moralizante que pode ser percebido como condescendente para o leitor executivo que paga pelo livro.

## ACHADOS

### ACHADO 01
Categoria: P1
Problema: Pergunta 2 do diagnóstico é demasiado específica — "com loop de planejamento, ação e observação" pode subcategorizar incorretamente profissionais que operam agentes com arquitetura diferente.
Por que é um problema: Profissional que usa LangChain com tool-calling mas sem "loop de observação" explícito pode responder "não" e ser classificado como Iniciante, quando tem nível Intermediário.
Impacto no leitor: Classificação incorreta de trilha → subutilização do livro ou abandono por tédio.
Correção exata: Reformular para incluir arquiteturas alternativas.
Texto sugerido: `Já operou, em ambiente profissional, um sistema baseado em LLM que usa ferramentas externas (APIs, banco de dados, busca) de forma automática para completar tarefas além de gerar texto?`
ROI: MÉDIO

### ACHADO 02
Categoria: P2
Problema: Trilha Avançado instrui começar por C00P e C00M, mas leitor avançado provavelmente já os leu ou vai pular.
Por que é um problema: Instrução óbvia para o leitor que já está avançado. Reduz utilidade do mapa para esse perfil.
Impacto no leitor: Leitor avançado ignora a instrução de "começo" e começa onde quiser de qualquer forma.
Correção exata: Reformular como "se não leu, comece por C00P e C00M; se leu, pule diretamente para o Núcleo técnico."
Texto sugerido: n/a
ROI: BAIXO

### ACHADO 03
Categoria: P2
Problema: "A leitura desonesta cobra o preço típico do leitor que escolhe a trilha que aspira ser" — tom levemente condescendente.
Por que é um problema: O leitor executivo sênior que paga R$150 por um livro não quer ser chamado de "desonesto" na leitura, mesmo que indiretamente.
Impacto no leitor: Resistência. Alguns leitores vão reagir negativamente ao enquadramento.
Correção exata: Reformular em linguagem de consequência, não de julgamento moral.
Texto sugerido: `Escolher a trilha que você aspira ser, em vez da que efetivamente serve agora, produz o resultado típico: abandono nos capítulos errados por frustração ou tédio.`
ROI: BAIXO

## TESTE DA JOANA
Entenderia: SIM. O diagnóstico em cinco perguntas vai funcionar bem para ela.
O que ela entenderia: Que tem uma trilha pensada para o seu nível. Que pode e deve mudar de trilha.
O que ela NÃO entenderia: A Pergunta 2 do diagnóstico (loop de planejamento, ação e observação) — vai precisar adivinhar.
Como corrigir: Reformular Pergunta 2 com linguagem mais acessível.

## TESTE DE DURABILIDADE
Classificação: ALTA
Justificativa: O mecanismo de diagnóstico e trilhas é estrutural e atemporal. Os capítulos listados são referências internas ao livro.

## TESTE DE DIFERENCIAÇÃO
Classificação: PROPRIEDADE INTELECTUAL
Justificativa: Diagnóstico com contagem de "sim" + critério de recalibração de trilha + tabela de sinais observados é o conjunto de design instrucional mais sofisticado deste paratexto. Não existe equivalente nos livros da régua de comparação.

## TESTE DE MEMORIZAÇÃO
Ideia principal clara? SIM
Qual é a ideia principal (em 1 frase): Existe trilha de leitura para seu nível — diagnose, escolha, e recalibre quando necessário.
Justificativa: O diagnóstico de cinco perguntas é a ideia mais memorável e acionável do paratexto inteiro.

## TESTE DE TRANSFORMAÇÃO
Ao terminar, o leitor consegue fazer o que antes não conseguia:
- Identificar seu nível real de conhecimento em IA generativa com critério objetivo.
- Escolher trilha de leitura com base no diagnóstico, não em aspiração.
- Saber quando mudar de trilha ao longo da leitura.

## NOTA FINAL
Estrutura: 9 | Pedagogia: 10 | Clareza: 8 | Autoridade: 9 | Durabilidade: 9 | Diferenciação: 10 | Memorização: 9 | Transformação: 10
**Nota Geral: 9**

## DECISÃO EDITORIAL
MANTER COM AJUSTES MÍNIMOS (reformular Pergunta 2 do diagnóstico, suavizar tom condescendente na frase final)

---

# [P-06] — L1-06-repositorio-acompanhante.md

## RESUMO EXECUTIVO
Nota: 8/10
Veredito: A

## O QUE FUNCIONA
- A distinção "padrão dura no livro / número muda no repositório" na epígrafe é a melhor instanciação do Princípio Camada Dupla em qualquer paratexto — concreta, operacional, e vincula o repositório ao sistema intelectual da obra.
- O endereço do repositório é dado logo no início, sem deixar o leitor esperar — `github.com/falercia/inteligencia-aumentada-recursos` está na linha 15, onde deveria estar.
- A tabela de pastas com coluna de "Capítulos relacionados" é excelente — o leitor que leu o C9 sabe que `/prompts` é o seu próximo passo.
- A seção "Política de evolução" com "nenhuma promessa de release que não esteja pronta para ser cumprida" é declaração de responsabilidade editorial rara e credível.
- Os três caminhos de início (entender antes de usar / colocar em produção rápido / contribuir) são distintos e acionáveis — atendem aos três perfis principais do livro.
- A descrição dos agentes educacionais (/agents) com nomes específicos (A01 ReAct, A02 Escala de Propriedade, A03 Orquestrador-Especialistas, A04 Multiagente Debate) e características técnicas (tools simuladas, kill switch testável) é substantiva — o leitor técnico sabe exatamente o que vai encontrar.

## O QUE NÃO FUNCIONA
- "sem cadência fixa anunciada" aparece duas vezes no arquivo (linha 17 e implícito na política de evolução) — a repetição não agrega e pode ser interpretada como desculpa antecipada para não entregar.
- "Quem identifica lacuna, anti-padrão útil para a obra, ou caso de uso não coberto pelas estruturas atuais, é convidado a abrir issue no repositório com o template correspondente" — onde está o template? O repositório existe? A URL é real? Em junho de 2026 quando o livro for publicado, o repositório precisa estar disponível e funcional, não apenas prometido.
- A seção "Cada pasta tem o seu próprio README" é instrução de uso do repositório, não conteúdo que pertence ao paratexto do livro. Seria melhor no README raiz do repositório.
- A frase "O que separa repositório acompanhante vivo de folheto promocional não é cadência declarada, é entrega consistente sob crítica pública" é auto-referencial de forma levemente defensiva — o autor está se defendendo de uma crítica que o leitor ainda não fez.
- A marcação "▸ repo" mencionada como convenção ao longo do livro não foi introduzida nas convenções visuais de "Como Ler Este Livro" (L1-02) — inconsistência entre os dois arquivos.

## ACHADOS

### ACHADO 01
Categoria: P0
Problema: O repositório `github.com/falercia/inteligencia-aumentada-recursos` pode não existir no momento da publicação ou pode estar vazio — o livro faz promessas substantivas sobre o conteúdo do repositório.
Por que é um problema: Se o repositório não estiver funcional na data de publicação (junho 2026), todas as promessas do livro sobre artefatos executáveis se tornam vazias. Isso compromete credibilidade central da obra.
Impacto no leitor: Leitor que compra o livro por causa do repositório e encontra repositório vazio vai devolver o livro e publicar review negativo.
Correção exata: Verificar que o repositório existe, tem as sete pastas listadas, e tem README funcional em cada uma antes de publicar. Adicionar nota: "Repositório disponível desde [data]."
Texto sugerido: n/a — requer ação operacional, não editorial.
ROI: ALTO

### ACHADO 02
Categoria: P1
Problema: A marcação "▸ repo" mencionada como convenção visual não está listada em L1-02-como-ler.md nas convenções visuais.
Por que é um problema: Inconsistência entre dois arquivos de paratexto. O leitor que leu "Como Ler" e chegar ao texto "▸ repo" não vai saber o que significa.
Impacto no leitor: Confusão de navegação.
Correção exata: Adicionar "▸ repo" na tabela de Convenções Visuais de L1-02, com descrição "Artefato executável disponível no repositório acompanhante".
Texto sugerido: n/a — correção em L1-02, não neste arquivo.
ROI: MÉDIO

### ACHADO 03
Categoria: P1
Problema: "sem cadência fixa anunciada" aparece duas vezes com tonalidade defensiva — pode ser interpretado como desculpa preventiva para atrasos.
Por que é um problema: Leitor que paga pelo livro e pelo repositório vai interpretar "sem cadência fixa" como "não se compromete com atualização". Corrói confiança no ativo.
Impacto no leitor: Reduz percepção de valor do repositório como ativo vivo.
Correção exata: Substituir a segunda ocorrência por afirmação positiva sobre o critério de atualização.
Texto sugerido: `O repositório é atualizado quando há entrega de qualidade para fazer — não por calendário, mas por movimento relevante do mercado ou da segurança que justifique revisão.`
ROI: MÉDIO

### ACHADO 04
Categoria: P2
Problema: "O que separa repositório acompanhante vivo de folheto promocional" é auto-referencial defensivo.
Por que é um problema: O autor está respondendo a uma crítica que o leitor não fez. Cria a crítica ao tentar preventivamente refutá-la.
Impacto no leitor: Leitor que não havia pensado "isso pode ser folheto" vai pensar depois de ler a frase.
Correção exata: Remover a frase ou reformular como princípio positivo.
Texto sugerido: `A política editorial é simples: nenhum release publicado sem ter passado pela mesma disciplina de revisão que o livro exige de qualquer artefato sério.`
ROI: BAIXO

## TESTE DA JOANA
Entenderia: SIM — a tabela de pastas com descrição funcional é acessível.
O que ela entenderia: O que o repositório contém e como começar.
O que ela NÃO entenderia: "gate de CI", "JSONL", "tracing local em JSONL" — terminologia técnica não traduzida para executivos.
Como corrigir: Adicionar coluna "Para executivos" na tabela de pastas, ou nota entre parênteses.

## TESTE DE DURABILIDADE
Classificação: MÉDIA
2 anos / 5 anos / 10 anos: A existência do repositório é durável. O conteúdo específico (MCP servers, agentes em Python, notebooks) pode envelhecer conforme as ferramentas evoluem.
Justificativa: A política de atualização sem cadência fixa é sensata mas cria risco de abandono silencioso se o autor não mantiver a disciplina.

## TESTE DE DIFERENCIAÇÃO
Classificação: PROPRIEDADE INTELECTUAL
Justificativa: Repositório acompanhante com sete pastas de artefatos executáveis — prompts em XML com golden sets, agentes educacionais com kill switch, caderno de governança em arquivos editáveis — não existe em nenhum livro de IA em português e é raro em inglês.

## TESTE DE MEMORIZAÇÃO
Ideia principal clara? SIM
Qual é a ideia principal (em 1 frase): O repositório carrega o número que muda; o livro carrega o método que dura — usar os dois é mais que a soma das partes.
Justificativa: A epígrafe entrega com precisão.

## TESTE DE TRANSFORMAÇÃO
Ao terminar, o leitor consegue fazer o que antes não conseguia:
- Saber que o repositório existe e o que tem nele antes de começar o livro.
- Escolher um dos três caminhos de início no repositório.
- Entender a diferença funcional entre livro e repositório.

## NOTA FINAL
Estrutura: 8 | Pedagogia: 8 | Clareza: 7 | Autoridade: 8 | Durabilidade: 7 | Diferenciação: 10 | Memorização: 9 | Transformação: 8
**Nota Geral: 8**

## DECISÃO EDITORIAL
MANTER COM AJUSTES (verificar repositório funcional antes de publicar, adicionar ▸ repo em L1-02, reformular tom defensivo)

---

# [P-10] — L1-10-sobre-o-autor.md

## RESUMO EXECUTIVO
Nota: 7/10
Veredito: B

## O QUE FUNCIONA
- A "dupla cadeira" (executivo que responde por orçamento E operador que lê código) é o diferencial de credibilidade mais forte da bio — específico, verificável e raro.
- As três marcas declaradas (disciplina operacional / frameworks transferíveis / desenvolvimento de pessoas) são concretas e distinguem o autor de coaches genéricos de liderança.
- A menção ao segundo livro planejado (*Deep Claude*) com descrição funcional é posicionamento de série, não apenas de título único — aumenta percepção de sistema.
- O parágrafo final ("se um leitor brasileiro fechar este livro e operar IA de forma mais clara...") é missão declarada com critério de sucesso explícito — raro e honesto.

## O QUE NÃO FUNCIONA
- "Como autor, é reconhecido pela produção de frameworks próprios e pela abordagem executiva sobre Inteligência Artificial" — "reconhecido" por quem? Sem referência a publicação prévia, prêmio, ou comunidade específica, essa afirmação é circular. O livro que está sendo vendido não pode ser sua própria credencial no texto da bio.
- Os setores de atuação (logística, supply chain, transporte, operações industriais, plataformas B2B SaaS) são mencionados mas sem empresa ou resultado específico — é o tipo de credencial que o leitor técnico sênior quer verificar e não consegue.
- "mais recentemente, Inteligência Artificial aplicada" no primeiro parágrafo sinaliza que IA é a área mais nova, o que pode ser lido como "ainda aprendendo" para o leitor crítico.
- O texto usa "é reconhecido" e "mantém presença ativa" em terceira pessoa, que é convencional para bio de orelha mas cria distância desnecessária dado o tom autoral direto do resto do livro.
- O parágrafo sobre abertura para contato (leitores, pesquisa, adoção institucional) duplica informações que já aparecem em outros paratextos — especialmente o canal oficial da obra.

## ACHADOS

### ACHADO 01
Categoria: P1
Problema: "Como autor, é reconhecido pela produção de frameworks próprios" — auto-atribuição de reconhecimento sem referência externa.
Por que é um problema: "Reconhecido" implica reconhecimento externo. Se não há publicação anterior, prêmio, ou comunidade que atribua esse reconhecimento, a afirmação é não-verificável.
Impacto no leitor: Leitor técnico sênior vai buscar "Fabio Garcia frameworks IA" e encontrar apenas este livro. Credencial circular.
Correção exata: Ou substituir por afirmação factual ("desenvolveu frameworks proprietários adotados por times de tecnologia em..."), ou remover e deixar as três marcas declaradas falarem por si.
Texto sugerido: `Como autor, dedica-se à produção de frameworks próprios e transferíveis sobre Inteligência Artificial, engenharia de software, governança e produtividade de times — trabalho que sustenta diretamente este livro.`
ROI: MÉDIO

### ACHADO 02
Categoria: P1
Problema: "mais recentemente, Inteligência Artificial aplicada" pode ser lido como reconhecimento de inexperiência em IA.
Por que é um problema: O livro posiciona o autor como especialista em IA. "Mais recentemente" sinaliza que IA é sua área mais nova, não sua área de profundidade histórica.
Impacto no leitor: Leitor técnico vai questionar a profundidade da experiência em IA.
Correção exata: Reformular para mostrar trajetória de convergência, não de adição tardia.
Texto sugerido: `...com responsabilidade direta sobre engenharia, dados, produto e Inteligência Artificial — área que integra progressivamente toda a operação técnica nos últimos cinco anos.`
ROI: MÉDIO

### ACHADO 03
Categoria: P2
Problema: Setores de atuação listados sem empresa ou resultado verificável.
Por que é um problema: O leitor técnico sênior quer saber "onde?" e "com que resultado?". Lista de setores sem âncora não constrói credibilidade.
Impacto no leitor: Bio lida como genérica por leitores que comparecem com alto nível de escrutínio.
Correção exata: Adicionar pelo menos uma âncora verificável — porte de equipe liderada, receita gerenciada, ou resultado específico.
Texto sugerido: n/a — depende do que o autor está disposto a revelar.
ROI: MÉDIO

### ACHADO 04
Categoria: P2
Problema: Parágrafo de abertura para contato duplica informações de outros paratextos.
Por que é um problema: Redundância. O leitor de bio não precisa de instrução completa de como contribuir — isso está no L1-00e e em outros locais.
Impacto no leitor: Bio se estende além do necessário.
Correção exata: Reduzir para uma sentença com referência ao canal oficial.
Texto sugerido: `Está aberto ao contato de leitores, pares e organizações via canal oficial da obra.`
ROI: BAIXO

## TESTE DA JOANA
Entenderia: SIM. A bio é clara e acessível.
O que ela entenderia: Quem é o autor, de onde vem a autoridade, para onde vai a série.
O que ela NÃO entenderia: Por que "mais recentemente IA" pode ser fraqueza de credencial — ela não vai questionar isso.
Como corrigir: O problema é para o leitor técnico sênior, não para Joana.

## TESTE DE DURABILIDADE
Classificação: ALTA
Justificativa: Bio baseada em trajetória e marcas de liderança não envelhece. Referência ao segundo livro (*Deep Claude*) pode precisar de atualização se o título ou escopo mudar.

## TESTE DE DIFERENCIAÇÃO
Classificação: DIFERENCIADO
Justificativa: A "dupla cadeira" (executivo + operador técnico) é diferencial real e raro no mercado de autores de livros de IA em português.

## TESTE DE MEMORIZAÇÃO
Ideia principal clara? SIM
Qual é a ideia principal (em 1 frase): O autor é o executivo que também lê código — e essa dupla cadeira é a fonte de autoridade de todo o livro.
Justificativa: "É dessa dupla cadeira que nasce a voz desta obra" é a frase mais forte da bio.

## TESTE DE TRANSFORMAÇÃO
Ao terminar, o leitor consegue fazer o que antes não conseguia: Não aplicável — bio de autor.

## NOTA FINAL
Estrutura: 7 | Pedagogia: n/a | Clareza: 8 | Autoridade: 7 | Durabilidade: 8 | Diferenciação: 8 | Memorização: 8 | Transformação: n/a
**Nota Geral: 7**

## DECISÃO EDITORIAL
MANTER COM AJUSTES (remover auto-atribuição de reconhecimento, reformular "mais recentemente IA", adicionar âncora de resultado verificável)

---

# [P-11] — L1-11-orelhas.md

## RESUMO EXECUTIVO
Nota: 7/10
Veredito: B

## O QUE FUNCIONA
- A orelha esquerda abre com a dicotomia "inventário de ferramentas / filosofia distante" e declara que o livro "recusa as duas armadilhas e propõe sistema" — posicionamento editorial preciso em uma sentença.
- A lista dos nove frameworks com verbos de ação ("como decidir", "como diagnosticar", "como construir", "como engenharar", "como projetar", "como instituir", "como contabilizar", "como erguer", "como construir") é a forma mais compacta e acionável de descrever F1-F9.
- A frase final da orelha esquerda ("Para o profissional que quer construir, não apenas opinar") é tagline eficaz e consistente com a quarta capa.
- A orelha direita sobre o autor é enxuta — três períodos que dizem tudo o que precisa ser dito em espaço físico de orelha.

## O QUE NÃO FUNCIONA
- A orelha esquerda lista tecnologias específicas datadas: "DeepSeek", "RLHF e DPO", "interpretabilidade mecanicista", "prompt injection". Estas menções são plenamente corretas em 2026, mas em uma orelha física que vai durar 10 anos na estante, a datação é risco.
- "nove frameworks acionáveis traduzem cada Princípio em decisão concreta" — mas na listagem dos frameworks em prosa, o penúltimo framework ("como erguer a pirâmide da avaliação") e o último ("como construir a rota dupla de adoção") são descritos com metáforas que precisam de referência para fazer sentido ("pirâmide da avaliação", "rota dupla"). O leitor da orelha não tem essa referência.
- A frase de encerramento do arquivo (`> *"A leitura termina onde o método começa."*`) é uma citação isolada sem contexto de autoria — quem disse? É do autor? É nova? Diferente da frase âncora do arquivo de capa ("Modelos passam. Método fica."). Duas citações âncora em paratextos diferentes criam fragmentação de mensagem.
- A orelha direita repete "é reconhecido pela produção de frameworks proprietários transferíveis" — mesma afirmação problemática da bio (L1-10), agora em dois lugares.

## ACHADOS

### ACHADO 01
Categoria: P1
Problema: Orelha esquerda lista tecnologias datadas (DeepSeek, RLHF, DPO, prompt injection) que podem envelhece em orelha física.
Por que é um problema: Orelha de livro impresso tem vida de 10-15 anos. Menção a "DeepSeek" em 2026 pode parecer arqueológica em 2031.
Impacto no leitor: Leitor de segunda mão em 2030 vai ver as menções como datadas.
Correção exata: Opção A — remover menções específicas de tecnologia da orelha e manter no corpo do livro. Opção B — reformular para mencionar categorias em vez de marcas ("modelos de raciocínio avançado" em vez de "DeepSeek").
Texto sugerido: `A obra cobre o estado da arte em 2026 em profundidade técnica: arquitetura de large language models, retrieval-augmented generation, agentes e integração via protocolo, modelos de raciocínio, alinhamento por reforço, interpretabilidade, operação em produção, segurança e governança institucional.`
ROI: MÉDIO

### ACHADO 02
Categoria: P1
Problema: Duas citações âncora em paratextos diferentes — "Modelos passam. Método fica." (capa/orelha esquerda do L1-00) vs. "A leitura termina onde o método começa." (fim do L1-11).
Por que é um problema: Dois slogans âncora criam fragmentação de mensagem. O leitor não sabe qual é o tagline da obra.
Impacto no leitor: Reduz impacto memorável de ambas as frases.
Correção exata: Escolher uma como âncora principal da obra. Sugestão: "Modelos passam. Método fica." é superior — mais simples, mais contrastante. A segunda pode aparecer como variação interna, não como citação de encerramento de arquivo canônico.
Texto sugerido: n/a — depende de decisão editorial sobre hierarquia de slogans.
ROI: ALTO

### ACHADO 03
Categoria: P2
Problema: "é reconhecido pela produção de frameworks proprietários transferíveis" repete auto-atribuição problemática da bio (L1-10).
Por que é um problema: Dois documentos canônicos com a mesma afirmação não-verificável dobram o problema.
Impacto no leitor: Leitor que leu a bio antes da orelha percebe a repetição e a desacredita.
Correção exata: Substituir por afirmação factual verificável na orelha — mesmo que seja simples como "com mais de quinze anos de prática em liderança técnica".
Texto sugerido: `É reconhecido pela prática de instalar disciplina operacional em áreas técnicas e por construir frameworks que sobrevivem à saída do autor.`
ROI: MÉDIO

## TESTE DA JOANA
Entenderia: SIM. A orelha esquerda é provavelmente o melhor texto de paratexto para ela — denso mas acessível.
O que ela entenderia: O que o livro é (sistema, não inventário), o que os frameworks fazem (traduzir em decisão), quem é o autor.
O que ela NÃO entenderia: "RLHF e DPO", "interpretabilidade mecanicista". Vai passar por esses termos sem ancorar.
Como corrigir: Substituir por categorias funcionais em vez de siglas técnicas.

## TESTE DE DURABILIDADE
Classificação: MÉDIA
Justificativa: A estrutura das orelhas é sólida mas as menções de tecnologia específica reduzem durabilidade para uma orelha física.

## TESTE DE DIFERENCIAÇÃO
Classificação: DIFERENCIADO
Justificativa: "Recusa as duas armadilhas e propõe sistema" é posicionamento preciso e diferenciado no mercado de livros de IA em português.

## TESTE DE MEMORIZAÇÃO
Ideia principal clara? SIM
Qual é a ideia principal (em 1 frase): Este é o livro que tem sistema próprio — não inventário de ferramentas, não filosofia distante.
Justificativa: A dicotomia de abertura da orelha esquerda é eficaz e memorável.

## TESTE DE TRANSFORMAÇÃO
Ao terminar, o leitor consegue fazer o que antes não conseguia:
- Não aplicável — paratexto de orelha.
- Porém: a orelha deve fazer o leitor querer abrir o livro, e cumpre essa função.

## NOTA FINAL
Estrutura: 8 | Pedagogia: n/a | Clareza: 7 | Autoridade: 7 | Durabilidade: 6 | Diferenciação: 8 | Memorização: 7 | Transformação: n/a
**Nota Geral: 7**

## DECISÃO EDITORIAL
MANTER COM AJUSTES (escolher citação âncora única, reformular menções de tecnologia datada, substituir auto-atribuição de reconhecimento)

---

# [P-12] — L1-12-quarta-capa.md

## RESUMO EXECUTIVO
Nota: 8/10
Veredito: A

## O QUE FUNCIONA
- A frase de abertura em destaque é a mais forte da quarta capa e provavelmente da obra toda: "A diferença entre quem dominará a Inteligência Artificial e quem será dominado por ela não é tecnológica. É de método." — circular, binária, memorizável.
- A estrutura do texto central (nove princípios → nove frameworks → exemplos) é descrição de proposta de valor em escada lógica — cada elemento constrói sobre o anterior.
- Os três taglines finais em bold ("Para o profissional brasileiro que quer construir, não apenas opinar. / Para o executivo que quer decidir, não apenas reagir. / Para o operador que quer durar, não apenas surfar.") são os melhores taglines do paratexto inteiro — três públicos distintos, três verbos de contraste, três promessas específicas.
- O texto cumpre sua função de quarta capa em menos de 200 palavras com densidade suficiente para vender o livro.

## O QUE NÃO FUNCIONA
- Os campos "[a definir após diagramação]" e "[a ser atribuído]" e "[a ser definido pela editora]" no rodapé da quarta capa são estados de produção que não deveriam aparecer em arquivo canônico — se este arquivo for enviado ao gráfico sem revisão, esses campos vão para impressão.
- "construídos como compostos pedagógicos calibrados ao mercado brasileiro a partir de padrões observados em organizações reais" é a frase mais longa e mais técnica da quarta capa — quebraria o ritmo de leitura de um leitor que pega o livro na livraria.
- "Do Transformer ao reasoning model, do RAG ao MCP, do RLHF ao DPO, do LLMOps à interpretabilidade mecanicista, do prompt injection à governança institucional" — lista de pares de termos técnicos é substancial mas cria barreira de entrada para o executivo não-técnico que é exatamente o terceiro público-alvo da obra.
- A quarta capa não menciona o repositório acompanhante — que é um diferencial real e único da obra. Oportunidade perdida de diferenciação.
- "A profundidade executiva vai do método de decisão ao caderno de governança em seis páginas, do trade-off em seis dimensões ao roadmap pessoal por persona com horas reais e critério de abandono" — "em seis páginas", "em seis dimensões", "horas reais e critério de abandono" são especificidades de marketing interno, não de quarta capa.

## ACHADOS

### ACHADO 01
Categoria: P0
Problema: Campos de produção abertos ("[a definir após diagramação]", "[a ser atribuído]", "[a ser definido pela editora]") no rodapé de arquivo canônico de quarta capa.
Por que é um problema: Se este arquivo for o arquivo de produção gráfica, esses placeholders vão para impressão. É o erro de produção mais óbvio de todo o paratexto.
Impacto no leitor: Livro impresso com placeholder visível na quarta capa = embarrassment editorial imediato.
Correção exata: Marcar claramente como "PENDENTE — NÃO ENVIAR AO GRÁFICO" ou substituir por valores reais assim que disponíveis.
Texto sugerido: `**Páginas:** [PENDENTE — aguardando diagramação final — NÃO ENVIAR AO GRÁFICO]`
ROI: ALTO

### ACHADO 02
Categoria: P1
Problema: "construídos como compostos pedagógicos calibrados ao mercado brasileiro a partir de padrões observados em organizações reais" — frase técnico-editorial de 18 palavras em texto de quarta capa.
Por que é um problema: Quarta capa é texto de conversão, não de disclosure. O leitor na livraria lê em 30 segundos. Esta frase vai paralisar a leitura.
Impacto no leitor: Joana abandona a leitura neste ponto e coloca o livro de volta na prateleira.
Correção exata: Comprimir para o essencial da promessa.
Texto sugerido: `Mais de trinta exemplos memoráveis, construídos a partir de padrões brasileiros reais, transformam abstração em prática.`
ROI: ALTO

### ACHADO 03
Categoria: P1
Problema: Lista de pares de termos técnicos ("do Transformer ao reasoning model, do RAG ao MCP...") cria barreira de entrada para o executivo não-técnico.
Por que é um problema: O terceiro tagline ("Para o operador que quer durar") sugere público técnico, mas os dois primeiros ("profissional brasileiro / executivo") sugerem público com menos tecnicidade. A lista de termos serve apenas ao terceiro público.
Impacto no leitor: Executivo não-técnico se sente excluído no segundo parágrafo da quarta capa.
Correção exata: Reformular a profundidade técnica em linguagem de resultado, não de vocabulário.
Texto sugerido: `A profundidade técnica vai dos fundamentos da arquitetura até a operação em produção. A profundidade executiva vai do método de decisão ao caderno de governança, do roadmap pessoal ao critério de abandono de projeto.`
ROI: MÉDIO

### ACHADO 04
Categoria: P1
Problema: O repositório acompanhante não é mencionado na quarta capa.
Por que é um problema: O repositório é o diferencial mais concreto e verificável da obra. A quarta capa que não o menciona perde o argumento mais forte de conversão para o leitor técnico.
Impacto no leitor: Leitor técnico que estava indeciso não recebe o argumento decisivo.
Correção exata: Adicionar menção ao repositório na última seção do texto, antes dos taglines.
Texto sugerido: `O livro tem repositório acompanhante público — sete pastas de artefatos executáveis, incluindo prompts em XML com golden sets, agentes educacionais em Python e caderno operacional de governança. O método mora no livro. A implementação mora no repositório.`
ROI: ALTO

### ACHADO 05
Categoria: P2
Problema: "caderno de governança em seis páginas" e "trade-off em seis dimensões" são especificidades de marketing interno sem contexto para o leitor de livraria.
Por que é um problema: "Seis páginas" e "seis dimensões" são números sem âncora — o leitor não sabe se seis é muito ou pouco.
Impacto no leitor: Os números passam sem marcar.
Correção exata: Substituir os números por descrição de benefício.
Texto sugerido: `da governança que cabe em uma reunião de conselho ao roadmap pessoal com horas reais e critério explícito de quando parar`
ROI: BAIXO

## TESTE DA JOANA
Entenderia: SIM (maioria). A frase de abertura e os três taglines finais são os pontos mais fortes para ela.
O que ela entenderia: Por que o livro existe. Para quem é. Que tem profundidade técnica e executiva.
O que ela NÃO entenderia: A lista de termos técnicos no segundo parágrafo. "Compostos pedagógicos calibrados ao mercado brasileiro".
Como corrigir: Simplificar o segundo parágrafo. Adicionar repositório antes dos taglines.

## TESTE DE DURABILIDADE
Classificação: ALTA (texto principal) / BAIXA (lista de termos técnicos)
Justificativa: A frase de abertura e os três taglines são atemporais. A lista de tecnologias específicas (MCP, reasoning model, interpretabilidade mecanicista) vai envelhecer em 5-7 anos.

## TESTE DE DIFERENCIAÇÃO
Classificação: PROPRIEDADE INTELECTUAL
Justificativa: "A diferença entre quem dominará a IA e quem será dominado por ela não é tecnológica. É de método." é a afirmação de posicionamento mais forte e mais diferenciada de toda a obra. Nenhum concorrente faz essa afirmação desta forma.

## TESTE DE MEMORIZAÇÃO
Ideia principal clara? SIM
Qual é a ideia principal (em 1 frase): Quem tem método domina a IA; quem não tem, é dominado por ela.
Justificativa: A frase de abertura é a ideia mais memorável de todo o paratexto. Cabe em tweet, em slide, em conversa de corredor.

## TESTE DE TRANSFORMAÇÃO
Ao terminar, o leitor consegue fazer o que antes não conseguia:
- Não aplicável — texto de conversão.
- Porém: a quarta capa deve converter leitores indecisos, e os três taglines finais fazem esse trabalho com eficácia.

## NOTA FINAL
Estrutura: 8 | Pedagogia: n/a | Clareza: 7 | Autoridade: 9 | Durabilidade: 7 | Diferenciação: 10 | Memorização: 10 | Transformação: n/a
**Nota Geral: 8**

## DECISÃO EDITORIAL
MANTER COM AJUSTES (marcar campos pendentes, simplificar frase de compostos pedagógicos, simplificar lista de termos técnicos, adicionar menção ao repositório)

---

## LINHAS-TRACKER

`CODIGO|ARQUIVO|ACHADO_ID|CATEGORIA|ROI|PROBLEMA_CURTO|CORRECAO_CURTA|DECISAO_CAP`
`P-00|L1-00-capa-e-titulos.md|01|P0|ALTO|Dois subtítulos concorrentes sem declaração do canônico|Declarar subtítulo canônico vs. tagline de marketing com cabeçalhos distintos|MANTER COM AJUSTES`
`P-00|L1-00-capa-e-titulos.md|02|P1|ALTO|Orelhas duplicadas entre este arquivo e L1-11 com conteúdo divergente|Remover orelhas deste arquivo, manter apenas referência a L1-11|MANTER COM AJUSTES`
`P-00|L1-00-capa-e-titulos.md|03|P2|BAIXO|Tag interna de briefing exposta no arquivo de produto|Mover para comentário HTML ou seção de notas internas|MANTER COM AJUSTES`
`P-00|L1-00-capa-e-titulos.md|04|P2|MÉDIO|Campos ISBN e Ficha CIP pendentes sem data-limite ou responsável|Adicionar responsável e prazo em cada campo incompleto|MANTER COM AJUSTES`
`P-00B|L1-00b-ficha-catalografica.md|01|P1|MÉDIO|Descritor "Modelos de linguagem" não é controlado CDD/CDU|Substituir por "Processamento de linguagem natural"|MANTER COM AJUSTES`
`P-00B|L1-00b-ficha-catalografica.md|02|P1|MÉDIO|Referência ao Apêndice Q dentro de documento jurídico de direitos autorais|Substituir por frase autocontida com a política essencial|MANTER COM AJUSTES`
`P-00B|L1-00b-ficha-catalografica.md|03|P2|MÉDIO|Canal de contato descrito com linguagem evasiva em contexto jurídico|Inserir URL ou e-mail de contato explícito|MANTER COM AJUSTES`
`P-00C|L1-00c-dedicatoria.md|01|P2|BAIXO|Segunda estrofe é clichê de dedicatória técnica|Reescrever com detalhe específico deste livro ou cortar|MANTER COM AJUSTES`
`P-00C|L1-00c-dedicatoria.md|02|P2|BAIXO|Primeira estrofe abstrata demais sem contexto da obra|Ancorar com linguagem mais específica ao método do livro|MANTER COM AJUSTES`
`P-00C2|L1-00c2-promessa.md|01|P1|MÉDIO|Jargão interno "critério de recalibração" exposto ao leitor externo|Reescrever em linguagem de benefício direto|MANTER COM AJUSTES`
`P-00C2|L1-00c2-promessa.md|02|P1|MÉDIO|Afirmação "sem receita americana traduzida" não sustentada no paratexto|Adicionar exemplo concreto da diferença|MANTER COM AJUSTES`
`P-00C2|L1-00c2-promessa.md|03|P2|MÉDIO|"Trinta exemplos memoráveis" repetido 3x sem variação de enquadramento|Variar o ângulo em cada aparição|MANTER COM AJUSTES`
`P-00C2|L1-00c2-promessa.md|04|P2|BAIXO|Lista de frameworks F1-F9 não conecta frameworks a perfis de leitor|Adicionar coluna de perfil primário ou integrar à tabela de promessas|MANTER COM AJUSTES`
`P-00D|L1-00d-agradecimentos.md|01|P1|MÉDIO|Afirmação de peer review informal não nomeado pode ser questionada|Reformular como refinamento iterativo informal, não peer review formal|MANTER COM AJUSTES`
`P-00D|L1-00d-agradecimentos.md|02|P1|MÉDIO|CEOs nomeados (Hassabis, Amodei, Altman) por liderarem organizações "abertas" — frágil e datado|Reformular focando na organização, não no CEO; qualificar "aberta"|MANTER COM AJUSTES`
`P-00D|L1-00d-agradecimentos.md|03|P2|BAIXO|Parágrafo sobre família é o mais genérico e intercambiável do arquivo|Personalizar com detalhe específico ou aceitar a convenção|MANTER COM AJUSTES`
`P-00E|L1-00e-sobre-os-casos.md|01|P2|BAIXO|"mais de 30 exemplos" vs. "30+ casos" — inconsistência de formulação|Padronizar para "mais de 30" em todo o paratexto|MANTER`
`P-00E|L1-00e-sobre-os-casos.md|02|P2|BAIXO|"Postmortem público" como critério cria barreira implícita|Reformular como "postmortem documentado" com opção de publicação parcial|MANTER`
`P-00E|L1-00e-sobre-os-casos.md|03|P2|BAIXO|"sem rodeio" é locução redundante em texto já direto|Remover|MANTER`
`P-01|L1-01-prefacio.md|01|P1|MÉDIO|"Quem soube ler a internet em 1996 ganhou uma década" — afirmação não verificável|Qualificar como tese, não como fato histórico|MANTER COM AJUSTES`
`P-01|L1-01-prefacio.md|02|P1|MÉDIO|"Em 2028, segundo as projeções mais conservadoras" — sem fonte atribuída|Reformular como julgamento autoral explícito|MANTER COM AJUSTES`
`P-01|L1-01-prefacio.md|03|P1|MÉDIO|"Empresas trocam fornecedor toda semana" — hipérbole que abre flanco crítico|Reformular com precisão que mantém o impacto|MANTER COM AJUSTES`
`P-01|L1-01-prefacio.md|04|P1|ALTO|Nove Princípios não mencionados pelo nome no prefácio — gancho perdido|Adicionar parágrafo com nomes dos nove princípios|MANTER COM AJUSTES`
`P-01|L1-01-prefacio.md|05|P2|MÉDIO|Seções "A diferença" e "Por que escrevi" duplicam argumento sem escalada|Distinguir diagnóstico de resposta editorial; eliminar sobreposição|MANTER COM AJUSTES`
`P-02|L1-02-como-ler.md|01|P1|ALTO|Caminho 3 (pelos princípios) descrito sem exemplo concreto de rota|Adicionar exemplo com capítulos e frameworks específicos|MANTER COM AJUSTES`
`P-02|L1-02-como-ler.md|02|P1|MÉDIO|Afirmação pedagógica da sequência de 10 blocos sem referência à teoria|Referenciar base pedagógica ou reformular como escolha editorial|MANTER COM AJUSTES`
`P-02|L1-02-como-ler.md|03|P1|MÉDIO|"Assinar duas newsletters recomendadas" sem indicar quais|Adicionar referência ao apêndice ou nomear 2-3 diretamente|MANTER COM AJUSTES`
`P-02|L1-02-como-ler.md|04|P2|BAIXO|"Consultar documentação dos fornecedores periodicamente" sem periodicidade|Definir periodicidade ou vincular a gatilho|MANTER COM AJUSTES`
`P-02|L1-02-como-ler.md|05|P2|BAIXO|Nenhuma das trilhas menciona duração estimada neste arquivo|Adicionar estimativa de horas ao lado de cada caminho|MANTER COM AJUSTES`
`P-03|L1-03-introducao.md|01|P1|MÉDIO|Epígrafe de abertura tem três períodos compostos — densa demais para epígrafe|Reduzir para uma sentença de impacto|MANTER COM AJUSTES`
`P-03|L1-03-introducao.md|02|P1|MÉDIO|"Milhares de empresas, milhões de profissionais" — hipérbole não sustentada|Reformular com estimativa defensável|MANTER COM AJUSTES`
`P-03|L1-03-introducao.md|03|P1|MÉDIO|Seção Arco Narrativo é redundante com Sumário sem argumento adicional|Substituir por argumento sobre por que a ordem das partes é a que é|MANTER COM AJUSTES`
`P-03|L1-03-introducao.md|04|P1|MÉDIO|Aposta 2 critica livros de tecnologia sem nomear exemplos — ataque implícito|Reformular como limitação de formato, não crítica a autores|MANTER COM AJUSTES`
`P-03|L1-03-introducao.md|05|P2|BAIXO|"35-50 horas" ambíguo — não especifica se inclui exercícios|Especificar o que conta nas horas|MANTER COM AJUSTES`
`P-03|L1-03-introducao.md|06|P2|BAIXO|"estrutura pelas extremidades" é jargão interno não explicado ainda|Substituir por linguagem descritiva|MANTER COM AJUSTES`
`P-04|L1-04-sumario.md|01|P1|ALTO|Capítulos 14C e 14B em ordem inversa (C antes de B)|Reordenar para 14, 14B, 14C|MANTER COM AJUSTES`
`P-04|L1-04-sumario.md|02|P1|MÉDIO|Capítulo 14C com quatro princípios — dobro de qualquer outro|Revisar atribuição de princípios do 14C|MANTER COM AJUSTES`
`P-04|L1-04-sumario.md|03|P2|ALTO|Numeração de páginas por capítulo ausente — sumário sem função de índice|Adicionar coluna de página por capítulo|MANTER COM AJUSTES`
`P-04|L1-04-sumario.md|04|P2|BAIXO|Mescla de numeração romana e arábica sem transição explícita|Adicionar nota sobre sistema de paginação duplo|MANTER COM AJUSTES`
`P-05|L1-05-mapa-de-leitura-por-nivel.md|01|P1|MÉDIO|Pergunta 2 do diagnóstico demasiado específica — subcategoriza agentes com arquitetura diferente|Reformular para incluir arquiteturas alternativas|MANTER COM AJUSTES`
`P-05|L1-05-mapa-de-leitura-por-nivel.md|02|P2|BAIXO|Trilha Avançado instrui começar por C00P/C00M sem opção de pular para quem já leu|Reformular como condicional: se não leu, comece; se leu, pule|MANTER COM AJUSTES`
`P-05|L1-05-mapa-de-leitura-por-nivel.md|03|P2|BAIXO|"Leitura desonesta" tem tom moralizante para leitor executivo|Reformular em linguagem de consequência, não de julgamento|MANTER COM AJUSTES`
`P-06|L1-06-repositorio-acompanhante.md|01|P0|ALTO|Repositório pode não existir ou estar vazio na publicação|Verificar funcionalidade antes de publicar e adicionar nota de disponibilidade|MANTER COM AJUSTES`
`P-06|L1-06-repositorio-acompanhante.md|02|P1|MÉDIO|Marcação ▸ repo não está listada nas Convenções Visuais de L1-02|Adicionar ▸ repo na tabela de Convenções Visuais de L1-02|MANTER COM AJUSTES`
`P-06|L1-06-repositorio-acompanhante.md|03|P1|MÉDIO|"sem cadência fixa anunciada" repetido com tonalidade defensiva|Substituir segunda ocorrência por afirmação positiva do critério de atualização|MANTER COM AJUSTES`
`P-06|L1-06-repositorio-acompanhante.md|04|P2|BAIXO|"O que separa repositório vivo de folheto promocional" é auto-referencial defensivo|Remover ou reformular como princípio positivo|MANTER COM AJUSTES`
`P-10|L1-10-sobre-o-autor.md|01|P1|MÉDIO|"é reconhecido pela produção de frameworks próprios" — auto-atribuição circular|Substituir por afirmação factual verificável|MANTER COM AJUSTES`
`P-10|L1-10-sobre-o-autor.md|02|P1|MÉDIO|"mais recentemente, IA aplicada" pode sinalizar inexperiência em IA|Reformular como trajetória de convergência, não adição tardia|MANTER COM AJUSTES`
`P-10|L1-10-sobre-o-autor.md|03|P2|MÉDIO|Setores de atuação sem empresa ou resultado verificável|Adicionar âncora de resultado concreto|MANTER COM AJUSTES`
`P-10|L1-10-sobre-o-autor.md|04|P2|BAIXO|Parágrafo de abertura para contato duplica informações de outros paratextos|Reduzir para uma sentença com referência ao canal oficial|MANTER COM AJUSTES`
`P-11|L1-11-orelhas.md|01|P1|MÉDIO|Orelha esquerda lista tecnologias datadas (DeepSeek, RLHF, DPO) em texto físico de longa vida|Substituir por categorias funcionais em vez de marcas e siglas|MANTER COM AJUSTES`
`P-11|L1-11-orelhas.md|02|P1|ALTO|Duas citações âncora em paratextos diferentes criam fragmentação de mensagem|Escolher "Modelos passam. Método fica." como âncora única da obra|MANTER COM AJUSTES`
`P-11|L1-11-orelhas.md|03|P2|MÉDIO|"é reconhecido pela produção de frameworks" repete auto-atribuição problemática da bio|Substituir por afirmação factual verificável|MANTER COM AJUSTES`
`P-12|L1-12-quarta-capa.md|01|P0|ALTO|Campos de produção abertos no rodapé de arquivo canônico de quarta capa|Marcar claramente como pendente e não enviar ao gráfico sem preenchimento|MANTER COM AJUSTES`
`P-12|L1-12-quarta-capa.md|02|P1|ALTO|"Compostos pedagógicos calibrados ao mercado brasileiro" — 18 palavras em texto de quarta capa|Comprimir para frase de benefício direto|MANTER COM AJUSTES`
`P-12|L1-12-quarta-capa.md|03|P1|MÉDIO|Lista de termos técnicos cria barreira de entrada para executivo não-técnico|Reformular em linguagem de resultado, não de vocabulário|MANTER COM AJUSTES`
`P-12|L1-12-quarta-capa.md|04|P1|ALTO|Repositório acompanhante não mencionado na quarta capa — diferencial perdido|Adicionar menção ao repositório antes dos taglines finais|MANTER COM AJUSTES`
`P-12|L1-12-quarta-capa.md|05|P2|BAIXO|"caderno em seis páginas" e "trade-off em seis dimensões" são números sem âncora|Substituir por descrição de benefício|MANTER COM AJUSTES`

---

# BANCA EDITORIAL ADVERSARIAL — MANIFESTO + FRAMEWORKS
## Livro: INTELIGÊNCIA AUMENTADA
## Arquivos revisados: L1-C00M, L1-C00P, F1–F9

---

# L1-C00M — manifesto-invariantes.md

## RESUMO EXECUTIVO
Nota: 8/10
Veredito: A

## O QUE FUNCIONA
- Os nove princípios são distintivos, nomeados, citáveis. "Termômetro", "Camada Dupla", "Operador" são rótulos memoráveis que funcionam como vocabulário compartilhado.
- A estrutura interna de cada princípio (regra + mecânica + violação típica) é pedagogicamente sólida e consistente ao longo dos nove.
- A ressalva honesta sobre os princípios 1 e 2 dependerem da arquitetura transformer atual é rara em livros do gênero — aumenta credibilidade.
- O caso Banco Solar é bem construído como exemplo memorável e ancora os princípios em decisão executiva concreta.
- A tabela de síntese final é excelente material de referência rápida.
- A seção "Quando usar e quando evitar" é didaticamente útil e raras vezes aparece em frameworks análogos.

## O QUE NÃO FUNCIONA
- O título do arquivo/capítulo é "Os Nove Princípios Permanentes" mas a tese central do livro os chama de "invariantes". Há inconsistência de nomenclatura com o título do próprio livro ("Os Invariantes").
- O Princípio 9 (Operador) não tem mecânica técnica equivalente aos outros oito — é mais aforismo motivacional do que princípio com causalidade identificável.
- A analogia da navegação (seção 2) é eficaz mas longa demais para um manifesto — ocupa espaço que poderia ir para profundidade dos princípios.
- O exercício "Versão de bolso para o time" pede redução a 12 palavras mas não há exemplo de como fazê-lo — fica como instrução abstrata.
- Referências sobre "operador como multiplicador" citam Drucker (1966) e Engelbart (1962) mas a ponte entre esses trabalhos e IA generativa não é explicitada no texto. Parece credencial de biblioteca, não argumento.

## ACHADOS

### ACHADO 01
Categoria: P1
Problema: Inconsistência de nomenclatura — "princípios permanentes" vs. "invariantes"
Por que é um problema: O título do livro é "Os Invariantes". O capítulo os chama de "princípios permanentes". O manifesto os chama de "nove princípios". Três nomes para o mesmo conceito enfraquecem a ancoragem de marca intelectual.
Impacto no leitor: Confusão sobre o que é o produto intelectual central do livro. Dificulta citação e recomendação boca-a-boca.
Correção exata: Escolher um nome e padronizar: "Os Nove Invariantes" ou "Os Nove Princípios Permanentes" — não ambos. Recomendação: "Invariantes" ganha em memorabilidade e diferenciação (o nome do livro os ancora).
Texto sugerido: n/a (decisão editorial de nomenclatura)
ROI: ALTO

### ACHADO 02
Categoria: P1
Problema: Princípio 9 (Operador) carece de mecânica causal identificável
Por que é um problema: Os princípios 1-8 têm mecânica técnica explicável ("o softmax em contexto longo", "custo = chamadas × redundância × tier", etc.). O Princípio 9 afirma que "IA multiplica" mas não explica o mecanismo pelo qual isso ocorre — é assertiva, não princípio com causalidade.
Impacto no leitor: O leitor técnico questiona a paridade dos nove. O leitor executivo aceita mas não consegue defender em mesa técnica.
Correção exata: Adicionar a mecânica: a IA amplifica porque o output plausível do modelo é função da qualidade do input do operador (especificidade da tarefa, critério de aceitação, capacidade de rejeitar saída ruim). A amplificação é bidirecional porque o modelo não distingue boa instrução de má instrução por sinalização explícita — responde com mesma fluência a ambas.
Texto sugerido: "A mecânica é direta: o modelo produz saída plausível para a instrução recebida, com igual fluência para instrução precisa e instrução vaga. O operador competente fornece instrução precisa, critério de aceitação explícito e capacidade de rejeitar a saída inadequada — e o modelo responde com qualidade proporcional. O operador sem critério fornece instrução vaga, aceita qualquer saída plausível, e o modelo responde com qualidade proporcional à instrução. O fator de multiplicação é real; o sinal que determina a direção é a qualidade da operação."
ROI: ALTO

### ACHADO 03
Categoria: P2
Problema: Analogia da navegação (seção 2) é longa para um manifesto — 2 parágrafos densos antes dos princípios propriamente
Por que é um problema: O leitor quer chegar nos nove princípios. A analogia da navegação é eficaz para a tese mas poderia ser condensada em 50% sem perder força.
Impacto no leitor: Joana se perde antes de chegar nos princípios.
Correção exata: Reduzir a analogia para 1 parágrafo enxuto; mover o segundo parágrafo para nota de rodapé ou apêndice de contexto.
Texto sugerido: n/a
ROI: MÉDIO

### ACHADO 04
Categoria: P2
Problema: Citação de Drucker e Engelbart no Princípio 9 sem ponte explicada
Por que é um problema: Citar "The Effective Executive" (1966) e "Augmenting Human Intellect" (1962) como referência do Princípio 9 parece credencial de erudição sem argumento — a conexão com IA generativa não é explicitada.
Impacto no leitor: Leitor técnico questiona a relevância. Leitora Joana ignora.
Correção exata: Ou explicitar a ponte em 1-2 frases no corpo do texto, ou remover as referências da seção de princípios e mantê-las apenas nas referências finais do capítulo correspondente.
Texto sugerido: n/a
ROI: BAIXO

### ACHADO 05
Categoria: P2
Problema: Exercício "Versão de bolso" sem exemplo concreto
Por que é um problema: Pede que o leitor reduza cada princípio a 12 palavras "adaptadas à linguagem da sua empresa" sem mostrar o que isso significa na prática.
Impacto no leitor: Exercício atraente mas incompleto — o leitor não sabe o que é uma versão de bolso bem-feita vs. mal-feita.
Correção exata: Adicionar um exemplo de versão de bolso para dois dos nove princípios, mostrando a transformação de linguagem técnica para linguagem operacional.
Texto sugerido: n/a
ROI: MÉDIO

## TESTE DA JOANA
Entenderia: SIM (geral)
O que ela entenderia: Os nove nomes, a regra de cada um, o caso Banco Solar, a tabela de síntese.
O que ela NÃO entenderia: A mecânica técnica de Princípio 2 (softmax, encoding posicional) sem contexto prévio. A referência a "transformers" sem definição anterior (o manifesto é o primeiro capítulo substantivo).
Como corrigir: Adicionar uma nota de rodapé ou parêntese: "(Transformers são a arquitetura computacional que sustenta os modelos de IA generativa atuais — explicada no Capítulo 1)" para que Joana continue sem precisar sair do texto.

## TESTE DE DURABILIDADE
Classificação: ALTA
2 anos: Todos os nove princípios permanecem válidos. Banco Solar pode precisar de revisão se fintech específica se tornar identificável.
5 anos: Princípios 3–9 permanecem. Princípio 2 (Extremidades) pode precisar de revisão se arquitetura transformer for substituída — o próprio texto já ressalva isso.
10 anos: Princípios 1, 3, 4, 5, 6, 7, 8, 9 são independentes de arquitetura e tendem a durar.
Justificativa: A ressalva do autor sobre dependência arquitetural (seção final) é a proteção intelectual correta.

## TESTE DE DIFERENCIAÇÃO
Classificação: PROPRIEDADE INTELECTUAL
Justificativa: Os nove princípios com nomenclatura própria, mecânica interna padronizada e violação típica formam um sistema coerente que não existe em nenhum dos livros da régua de comparação. "Camada Dupla", "Termômetro", "Operador como multiplicador" são rótulos originais com definições operacionais. O risco é de enfraquecimento se a inconsistência "princípios vs. invariantes" não for resolvida.

## TESTE DE MEMORIZAÇÃO
Ideia principal clara? SIM
Qual é a ideia principal: Existe um conjunto de nove princípios que governam operação eficaz de IA independentemente do modelo do trimestre — dominá-los protege contra a obsolescência.
Justificativa: A tabela de síntese e o caso Banco Solar tornam a ideia concreta e citável.

## TESTE DE TRANSFORMAÇÃO
Ao terminar, o leitor consegue fazer o que antes não conseguia:
- Nomear os nove princípios e recitar a regra de pelo menos cinco
- Identificar qual princípio foi violado em uma decisão de IA passada
- Usar o vocabulário dos princípios em reunião executiva com autoridade
- Diagnosticar a violação típica de cada princípio quando ela aparece no time

## NOTA FINAL
Estrutura: 9 | Pedagogia: 8 | Clareza: 7 | Autoridade: 9 | Durabilidade: 8 | Diferenciação: 9 | Memorização: 9 | Transformação: 8
**Nota Geral: 8.4**

## DECISÃO EDITORIAL
MANTER COM AJUSTES

---

# L1-C00P — porque-padrao-dura.md

## RESUMO EXECUTIVO
Nota: 8/10
Veredito: A

## O QUE FUNCIONA
- Os quatro casos históricos (Hadoop, LSTM, fine-tuning, LangChain) são verificáveis, bem documentados e progressivamente mais recentes — excelente construção de evidência.
- A distinção padrão × número é clara e operacional; a tabela "O que mantenho na cabeça × O que consulto no Apêndice J" é uma das melhores peças do livro.
- A implicação executiva (P.8) é concreta, com metáfora de juros compostos bem executada.
- A seção P.8.5 (Nota Editorial ao Leitor) é pedagogicamente corajosa — o autor diz explicitamente o que o capítulo entrega vs. o que os princípios entregam, sem inflar expectativas.
- As referências são específicas (datas, conferências, nomes de papers), o que aumenta credibilidade.

## O QUE NÃO FUNCIONA
- O capítulo é longo (aprox. 3.500 palavras) e repete a tese principal em pelo menos quatro lugares diferentes (P.1, P.6, P.7, P.8). A redundância pedagógica é intencional mas pode ser podada em 20% sem perder força.
- A seção P.6 ("Por Que o Padrão Dura") é genérica demais — afirma que padrões sobrevivem porque "operam no nível da decisão e do trade-off", mas não adiciona nenhum mecanismo novo além do que os quatro casos já demonstraram.
- O caso LangChain (P.5) menciona a publicação "Building Effective Agents" da Anthropic (dezembro 2024) como acelerador da reavaliação do mercado. Em um livro que defende neutralidade e durabilidade, citar a própria editora como árbitro da maturidade do mercado é conflito de interesse não sinalizados.
- A seção P.9 ("Convite ao Livro") é repetitiva com o que a nota P.8.5 já fez de forma mais elegante.
- O título "Por Que Padrão Dura e Número Morre" é funcional mas menos memorável que os títulos dos princípios. Poderia ganhar com subtítulo.

## ACHADOS

### ACHADO 01
Categoria: P1
Problema: Conflito de interesse não declarado no caso LangChain — Anthropic citada como árbitro de maturidade
Por que é um problema: O capítulo cita "Building Effective Agents" (Anthropic, 2024) como documento que "acelerou a reavaliação do mercado" em relação ao LangChain — ou seja, um documento da editora do livro (Anthropic é o modelo base; a obra tem relação explícita com o ecossistema Anthropic) é apresentado como evidência neutra de uma mudança de mercado. Isso não é declarado e pode ser percebido como publicidade disfarçada.
Impacto no leitor: Leitor técnico com background em LLMs questiona a neutralidade da análise. Corrói autoridade do capítulo inteiro se percebido.
Correção exata: Adicionar frase de transparência: "Vale declarar: a Anthropic, cujos modelos são referenciados ao longo desta obra, foi um dos participantes desse movimento. A análise aqui é sobre o padrão do ciclo de hype de frameworks — não sobre a superioridade de qualquer fornecedor específico." Ou, alternativamente, adicionar a posição de outros fornecedores (AWS, Google, OpenAI) que fizeram recomendações similares no mesmo período.
Texto sugerido: n/a
ROI: ALTO

### ACHADO 02
Categoria: P1
Problema: Redundância estrutural — tese repetida quatro vezes sem adição de camada
Por que é um problema: P.1, P.6, P.7 e P.8 repetem a mesma assertiva ("padrão dura, número morre") com palavras diferentes mas sem adicionar mecanismo ou evidência novos. P.6 em particular é inteiramente dispensável — os quatro casos já demonstraram o argumento.
Impacto no leitor: Leitor com ritmo de leitura executivo (rápida, seletiva) percebe a repetição e desacelera a confiança no rigor editorial.
Correção exata: Fundir P.6 com P.7 em uma seção única ("Por Que Padrão Dura e Número Morre") de 300 palavras. Eliminar as repetições da tese em P.1 e P.8 mantendo apenas a aplicação executiva.
Texto sugerido: n/a
ROI: MÉDIO

### ACHADO 03
Categoria: P2
Problema: Seção P.9 ("Convite ao Livro") repete o que P.8.5 já fez com mais elegância
Por que é um problema: P.8.5 já posiciona o capítulo vs. os princípios com clareza. P.9 repete as mesmas instruções de leitura com menos precisão.
Impacto no leitor: Final do capítulo perde energia — termina com repetição em vez de remate forte.
Correção exata: Eliminar P.9 ou reduzir a 2 parágrafos máximo. Terminar o capítulo com a citação final ("Modelo passa, framework passa...") diretamente após P.8.
Texto sugerido: n/a
ROI: MÉDIO

### ACHADO 04
Categoria: P2
Problema: Caso fine-tuning (P.4) afirma que projetos custaram "US$ 100.000 a US$ 500.000" — número volátil no corpo do texto
Por que é um problema: O próprio capítulo argumenta que números pertencem ao Apêndice J, não ao corpo. Preços de projetos de consultoria de 2022-2023 são exatamente o tipo de número que envelhece.
Impacto no leitor: Autocontradição metodológica — o capítulo prega separação de padrão e número e pratica mistura.
Correção exata: Mover o número de preço para nota de rodapé com data explícita, ou reformular: "projetos de fine-tuning corporativo com tickets de seis dígitos em dólares, conforme tabelas de preço de boutiques especializadas da época — valores datados de 2022-2023 disponíveis no Apêndice J".
Texto sugerido: n/a
ROI: ALTO

### ACHADO 05
Categoria: P1
Problema: Caso LangChain menciona avaliação de US$ 200 milhões da LangChain Inc. — número volátil no corpo principal, e a relevância do número para o argumento não é clara
Por que é um problema: A avaliação da rodada Série A não contribui para o argumento de que LangChain é número (ciclo de hype), apenas adiciona drama corporativo. E é exatamente o tipo de dado que envelhece — a avaliação pode ter sido revisada.
Impacto no leitor: Distração do argumento central. Segunda autocontradição metodológica.
Correção exata: Remover a avaliação de US$ 200 milhões do corpo ou mover para nota de rodapé datada. O argumento sobre hype funciona sem ele.
Texto sugerido: n/a
ROI: MÉDIO

## TESTE DA JOANA
Entenderia: SIM (geral)
O que ela entenderia: Os quatro casos (Hadoop, LSTM, fine-tuning, LangChain), a distinção padrão × número, a tabela de síntese, a implicação para carreira de CTO.
O que ela NÃO entenderia: A seção P.3 (LSTM) pressupõe familiaridade com arquiteturas de redes neurais — BLEU score, encoder-decoder, Bi-LSTM não são explicados. Joana pode se perder nos dois parágrafos mais técnicos.
Como corrigir: Adicionar uma linha de contextualização: "LSTM eram a arquitetura dominante para tarefas de linguagem — pense nelas como o 'motor' que as empresas treinavam para entender texto antes do ChatGPT existir."

## TESTE DE DURABILIDADE
Classificação: ALTA
2 anos: Os quatro casos continuam válidos como história documentada.
5 anos: Os casos podem precisar de um quinto caso com o próximo ciclo de hype (2025-2027). A estrutura sobrevive.
10 anos: Sólido como evidência histórica. Os padrões derivados dos casos são independentes de tecnologia específica.
Justificativa: O capítulo pratica o que prega — argumenta com padrão, não com número. As autocontradições (números no corpo) são exceções pontuais, não estruturais.

## TESTE DE DIFERENCIAÇÃO
Classificação: DIFERENCIADO
Justificativa: A combinação de casos históricos verificáveis com a distinção operacional padrão × número é diferenciada. Porém não é PROPRIEDADE INTELECTUAL sozinho — a ideia de "aprender princípios, não ferramentas" existe em outros livros (Thinking Fast and Slow tem analogia com System 1/2; Superforecasting tem disciplina epistêmica similar). A diferenciação real vem do contexto específico de IA e da ponte com os frameworks proprietários.

## TESTE DE MEMORIZAÇÃO
Ideia principal clara? SIM
Qual é a ideia principal: Toda vez que um número virou ortodoxia em tecnologia, ele morreu em janela curta; o padrão derivado sobreviveu três gerações — decorar padrão, consultar número.
Justificativa: Os quatro casos são a âncora mnemônica. A tabela de síntese consolida.

## TESTE DE TRANSFORMAÇÃO
Ao terminar, o leitor consegue fazer o que antes não conseguia:
- Classificar qualquer peça de conhecimento sobre IA em "padrão" ou "número"
- Identificar autocontradição quando memoriza versão de modelo como se fosse durável
- Usar os quatro casos históricos como evidência em debate com CTO que resiste à separação padrão × número
- Montar a tabela pessoal de O que mantenho na cabeça × O que consulto no Apêndice J

## NOTA FINAL
Estrutura: 7 | Pedagogia: 8 | Clareza: 8 | Autoridade: 9 | Durabilidade: 8 | Diferenciação: 7 | Memorização: 9 | Transformação: 8
**Nota Geral: 8.0**

## DECISÃO EDITORIAL
MANTER COM AJUSTES

---

# L1-F1 — decid-ia.md

## RESUMO EXECUTIVO
Nota: 8/10
Veredito: A

## O QUE FUNCIONA
- Cinco perguntas em ordem rígida com lógica de bloqueio é um design elegante e aplicável imediatamente.
- O output em uma página com decisão binária e campos obrigatórios é excelente — elimina o vício de iniciativas sem dono e sem critério.
- O exemplo de uso (triagem de currículos) é bem escolhido: alto risco reputacional, sem ser caso de ficção.
- A anti-padrão "Aceitar 'depois a gente decide isso'" é preciso e reconhecível.
- A conexão explícita com Princípios 7 e 8 (Termômetro e Responsabilidade Indelegável) ancora o framework na espinha dorsal do livro.

## O QUE NÃO FUNCIONA
- O framework não trata o caso em que a resposta à Pergunta 3 (risco irreversível) deveria ser "não vai" automático — a lógica de bloqueio não inclui gatilho de veto por risco.
- "Nível de autonomia: Assistente · Co-piloto · Agente supervisionado · Agente autônomo regulado" é referenciado mas não definido aqui — leitor sem F3 não sabe o que significa, e a conexão com F3 está só nas conexões ao final.
- O campo "Revisão programada" no output é vago — quando o framework volta a rodar? Sem cadência sugerida, fica à decisão do leitor (que provavelmente não fará).

## ACHADOS

### ACHADO 01
Categoria: P1
Problema: Ausência de lógica de bloqueio por risco irreversível alto
Por que é um problema: A Pergunta 3 pede a avaliação de risco, mas a lógica do framework não especifica que risco irreversível + impacto crítico deve gerar bloqueio automático (não apenas ajuste de nível de autonomia). Um usuário pode avaliar risco como "irreversível em reputação" e ainda assim continuar o fluxo sem sinalização especial.
Impacto no leitor: Executa o framework como ritual sem entender que há casos onde a resposta correta é "não vai", independentemente das outras quatro perguntas.
Correção exata: Adicionar após a Pergunta 3: "Se o risco for irreversível E o impacto for financeiro, jurídico ou clínico de alta magnitude, a iniciativa não passa sem aprovação de nível executivo nominal (CEO ou equivalente com mandato). Documente o gatilho de veto explicitamente."
Texto sugerido: n/a
ROI: ALTO

### ACHADO 02
Categoria: P1
Problema: Nível de autonomia definido por referência cruzada sem explicação mínima inline
Por que é um problema: O leitor que encontra o F1 antes de ler F3 não tem como preencher o campo "Nível de autonomia" com critério — apenas com palpite.
Impacto no leitor: O campo mais importante do output (nível de autonomia) fica sem guia de preenchimento.
Correção exata: Adicionar caixa de referência rápida inline com a definição dos quatro níveis em uma linha cada, com indicação "detalhado em F3".
Texto sugerido: "Assistente: humano executa sempre / Co-piloto: executa com confirmação por passo crítico / Agente supervisionado: executa em lote com humano monitorando / Agente autônomo regulado: executa sem supervisão direta com observabilidade completa e kill switch testado. Definição completa em F3."
ROI: ALTO

### ACHADO 03
Categoria: P2
Problema: Campo "Revisão programada" sem cadência sugerida
Por que é um problema: Sem orientação de cadência, o campo será preenchido com "quando necessário" — que é equivalente a nunca.
Impacto no leitor: O framework perde seu mecanismo de autocorreção ao longo do tempo.
Correção exata: Adicionar orientação padrão: "Cadência padrão sugerida: 90 dias para piloto interno, 6 meses para produção com nível Assistente ou Co-piloto, 3 meses para Agente Supervisionado ou Autônomo."
Texto sugerido: n/a
ROI: MÉDIO

## TESTE DA JOANA
Entenderia: SIM
O que ela entenderia: As cinco perguntas, o exemplo de currículos, a decisão binária.
O que ela NÃO entenderia: O campo "nível de autonomia" sem definição inline (veja Achado 02).
Como corrigir: Adicionar a caixa de referência rápida do Achado 02.

## TESTE DE DURABILIDADE
Classificação: ALTA
2 anos / 5 anos / 10 anos: As cinco perguntas são independentes de tecnologia — funcionam para qualquer sistema de decisão automatizada, não apenas IA generativa.
Justificativa: Nenhum número, versão ou produto específico no corpo do framework.

## TESTE DE DIFERENCIAÇÃO
Classificação: PROPRIEDADE INTELECTUAL
Justificativa: A combinação de cinco perguntas com lógica de bloqueio + output em uma página + conexão explícita com princípios de governança é original. Não existe equivalente nos livros da régua de comparação.

## TESTE DE MEMORIZAÇÃO
Ideia principal clara? SIM
Qual é a ideia principal: Toda iniciativa de IA precisa responder cinco perguntas duras antes de ir para produção — ou não vai.
Justificativa: As cinco perguntas são memorizáveis; a lógica de bloqueio ("sem resposta específica, não passa") é incomum e marcante.

## TESTE DE TRANSFORMAÇÃO
Ao terminar, o leitor consegue fazer o que antes não conseguia:
- Conduzir uma sessão de 30 minutos que resulta em decisão documentada de vai/não-vai para qualquer iniciativa de IA
- Identificar quando uma iniciativa está passando sem operador nominal ou sem linha de medição
- Preencher o output de uma página com decisão fundamentada em critério, não em entusiasmo

## NOTA FINAL
Estrutura: 9 | Pedagogia: 8 | Clareza: 8 | Autoridade: 9 | Durabilidade: 9 | Diferenciação: 9 | Memorização: 8 | Transformação: 9
**Nota Geral: 8.6**

## DECISÃO EDITORIAL
MANTER COM AJUSTES

---

# L1-F2 — encaixe-5.md

## RESUMO EXECUTIVO
Nota: 7/10
Veredito: B

## O QUE FUNCIONA
- Os cinco eixos são distintos, coerentes e colocam o critério de escolha no padrão da tarefa, não no benchmark do mês.
- A mecânica de pontuação 0-5 por eixo é simples o suficiente para ser usada em 30 minutos.
- Os três exemplos (classificação de e-mail, agente de código, análise com gráficos) cobrem perfis de tarefa bem diferentes e são realistas.
- O anti-padrão "Lançou novo, vou trocar" é o mais importante do framework e está bem posicionado na primeira linha da tabela.
- A instrução explícita de "teste cego na carga real" é concreta e rara em livros do gênero.

## O QUE NÃO FUNCIONA
- O eixo "Custo crítico" mistura conceito de tier com conceito de auto-hospedagem (open weights self-hosted) sem explicar quando usar cada um — são decisões arquiteturais distintas.
- Não há orientação sobre o que fazer quando dois eixos empatam em notas altas mas apontam para modelos diferentes (ex: "razão complexa" aponta para premium proprietário mas "custo crítico" aponta para open weights).
- O framework pressupõe que o leitor sabe o que é "SWE-bench Verified", "GPQA Diamond", "HumanEval" — termos não definidos inline.
- A instrução "Consultar o Apêndice J" aparece duas vezes no corpo (eixos multimodal e contexto longo) mas não há orientação de como calibrar a decisão quando o Apêndice J mostra empate técnico entre dois modelos.

## ACHADOS

### ACHADO 01
Categoria: P1
Problema: Eixo "Custo crítico" conflate tier e arquitetura de hospedagem
Por que é um problema: O eixo diz "variante econômica do tier (Haiku, Mini, Flash) ou modelo open weights self-hosted (Llama, Mistral, DeepSeek, Qwen, Phi)". São duas decisões com trade-offs radicalmente diferentes — tier pequeno do fornecedor tem SLA mas custo variável; self-hosted tem custo fixo mas exige operação de infraestrutura, equipe MLOps, latência gerenciada internamente. Um leitor que pontua "5" em custo crítico não sabe qual caminho tomar.
Impacto no leitor: Decisão de arquitetura de hospedagem confundida com decisão de tier — consequências operacionais completamente diferentes.
Correção exata: Separar o eixo em dois subeixos ou adicionar nota de decisão: "Se custo crítico aponta para tier pequeno com provedor, o trade-off é API paga vs. volume; se aponta para self-hosted, o trade-off é custo de infraestrutura + operação vs. custo variável de API. A decisão entre os dois é arquitetural — ver Cap 16 para o fluxo completo."
Texto sugerido: n/a
ROI: ALTO

### ACHADO 02
Categoria: P1
Problema: Ausência de lógica de desempate quando dois eixos dominantes apontam para modelos diferentes
Por que é um problema: O Exemplo B (agente de código) tem três eixos dominantes (código, razão complexa, contexto longo) que apontam para o mesmo modelo. Na prática, casos reais frequentemente têm eixo de custo crítico em tensão com razão complexa — o framework não diz o que fazer.
Impacto no leitor: Em decisão real de conflito, o leitor volta ao critério de "modelo do mês" por falta de regra de desempate.
Correção exata: Adicionar regra de desempate: "Quando eixos dominantes apontam para modelos distintos, priorizar o eixo de maior custo de erro. Se razão complexa (alto custo de erro) conflita com custo crítico (baixo custo de erro), o eixo de razão complexa vence para tarefas com efeito jurídico, clínico ou financeiro. Custo crítico vence em tarefas de classificação simples e alto volume onde regressão é detectável."
Texto sugerido: n/a
ROI: ALTO

### ACHADO 03
Categoria: P2
Problema: Benchmarks citados sem glossário mínimo inline
Por que é um problema: "SWE-bench Verified", "HumanEval", "LiveCodeBench" são mencionados como critérios de escolha mas não são explicados. Joana e o executivo não-técnico não sabem o que medem.
Impacto no leitor: Termos opacos criam distância onde o framework deveria criar clareza.
Correção exata: Adicionar nota de rodapé ou parêntese inline: "(SWE-bench Verified mede resolução de bugs reais em repositórios open source — é o padrão mais próximo de engenharia real em 2025/2026; consultar Apêndice J para posições correntes)".
Texto sugerido: n/a
ROI: MÉDIO

## TESTE DA JOANA
Entenderia: SIM (parcialmente)
O que ela entenderia: Os cinco eixos, a mecânica de pontuação, os três exemplos.
O que ela NÃO entenderia: O eixo "Custo crítico" com a bifurcação tier/self-hosted; os benchmarks citados.
Como corrigir: Aplicar Achados 01 e 03.

## TESTE DE DURABILIDADE
Classificação: ALTA
2 anos / 5 anos / 10 anos: Os cinco eixos de tarefa são independentes de fornecedor e versão. A instrução de "consultar Apêndice J" para os números garante que o corpo do framework não envelhece.
Justificativa: Um framework do gênero de 2015 ainda seria aplicável hoje — os eixos de tarefa (razão, código, contexto, multimodal, custo) são categorias estáveis.

## TESTE DE DIFERENCIAÇÃO
Classificação: PROPRIEDADE INTELECTUAL
Justificativa: A matriz de cinco eixos com pontuação e critério de encaixe é original. "Escolha pelo padrão da tarefa, nunca pela versão da moda" é citável e diferente da abordagem de comparação de benchmarks dominante no mercado.

## TESTE DE MEMORIZAÇÃO
Ideia principal clara? SIM
Qual é a ideia principal: Pontuação em cinco eixos da tarefa → modelo de melhor encaixe; benchmark agregado é irrelevante.
Justificativa: Os cinco eixos são memorizáveis como lista; a regra de pontuação é simples.

## TESTE DE TRANSFORMAÇÃO
Ao terminar, o leitor consegue fazer o que antes não conseguia:
- Pontuar qualquer tarefa nos cinco eixos em 10 minutos
- Justificar a escolha de modelo com critério de tarefa, não com "é o mais novo"
- Definir critério de reavaliação com cadência e gatilho explícitos

## NOTA FINAL
Estrutura: 8 | Pedagogia: 7 | Clareza: 7 | Autoridade: 8 | Durabilidade: 9 | Diferenciação: 9 | Memorização: 8 | Transformação: 8
**Nota Geral: 8.0**

## DECISÃO EDITORIAL
MANTER COM AJUSTES

---

# L1-F3 — agente-prop.md

## RESUMO EXECUTIVO
Nota: 9/10
Veredito: A+

## O QUE FUNCIONA
- A matriz 4×4 de observabilidade × reversibilidade é o mecanismo mais rigoroso do livro inteiro — decisão de autonomia ancorada em duas capacidades mensuráveis, não em confiança ou entusiasmo.
- Os quatro níveis canônicos são bem nomeados e distintos — Assistente, Co-piloto, Agente supervisionado, Agente autônomo regulado cobrem o espectro real de deployment.
- Os gates de promoção com critérios explícitos (N dias sem incidente SEV-1/2, custo dentro do envelope, aprovação nominal, rollback testado) são operacionalmente aplicáveis imediatamente.
- O rebaixamento automático por incidente SEV-1/2 é mecanismo crítico raramente articulado em outros frameworks — distingue isso de confiança de mercado.
- O exemplo (agente de e-mail de boas-vindas) é bem escolhido: consequência moderada, reversibilidade parcial, progressão realista de níveis.
- Anti-padrão "Kill switch teórico (existe no roadmap, nunca foi testado)" é preciso e reconhecível — aparece em 80% das implementações reais.

## O QUE NÃO FUNCIONA
- O eixo X (Observabilidade) usa termos técnicos sem definição inline: "Tracing por span", "replay". Joana não sabe o que é span.
- A matriz 4×4 não é mostrada visualmente — é descrita textualmente. Uma matriz gráfica 4×4 tornaria o framework radicalmente mais usável.
- "N dias (N depende da carga; tipicamente 14-30 dias)" — a variabilidade de N sem critério de como decidir o N correto deixa a regra de promoção incompleta.

## ACHADOS

### ACHADO 01
Categoria: P2
Problema: Ausência de matriz visual 4×4 — o framework mais visual do livro está descrito em texto
Por que é um problema: Uma matriz 4×4 com os quadrantes preenchidos seria o artefato mais fácil de imprimir e colar na parede de qualquer time de engenharia. A descrição textual funciona mas desperdiça o potencial visual do framework.
Impacto no leitor: Memorabilidade e usabilidade reduzidas — o leitor precisa reconstruir a matriz mentalmente.
Correção exata: Adicionar tabela/diagrama com Observabilidade (1-4) no eixo X e Reversibilidade (1-4) no eixo Y, com os quatro quadrantes de autonomia preenchidos.
Texto sugerido: n/a (requer diagrama)
ROI: ALTO

### ACHADO 02
Categoria: P1
Problema: "Tracing por span" e "replay" sem definição inline
Por que é um problema: Os critérios de promoção de nível dependem de o time entender o que é "tracing por span" e "capacidade de reproduzir a execução completa". Sem definição, o leitor não técnico avalia o próprio sistema incorretamente.
Impacto no leitor: Risco real: time avalia que tem "observabilidade 3" quando tem apenas "observabilidade 2 com logs não estruturados".
Correção exata: Adicionar definição inline: "Tracing por span: registro individual de cada etapa do agente (input, output, latência, tokens e custo por passo), identificado por ID único que permite rastrear a cadeia completa de decisões. Replay: capacidade de re-executar exatamente a mesma sequência de passos, com o mesmo input, para diagnóstico de incidente."
Texto sugerido: (acima)
ROI: ALTO

### ACHADO 03
Categoria: P2
Problema: Critério de N dias para promoção sem guia de como calibrar N
Por que é um problema: "Tipicamente 14-30 dias" é vago o suficiente para que times agressivos justifiquem N=14 dias para qualquer caso.
Impacto no leitor: Gates de promoção perdem rigor — N vira negociação em vez de critério.
Correção exata: Adicionar orientação: "N = 14 dias para carga de baixo risco (ação reversível, impacto interno). N = 30 dias para ação com efeito externo (e-mail, mensagem, transação). N = 60 dias ou mais para ação irreversível de alto impacto (financeiro, jurídico, clínico). Justificar explicitamente qualquer N abaixo do padrão."
Texto sugerido: n/a
ROI: MÉDIO

## TESTE DA JOANA
Entenderia: SIM (parcialmente)
O que ela entenderia: Os quatro níveis de autonomia, o exemplo do e-mail de boas-vindas, o kill switch.
O que ela NÃO entenderia: Tracing por span, replay, a lógica da matriz 4×4 sem visualização.
Como corrigir: Aplicar Achados 01 e 02.

## TESTE DE DURABILIDADE
Classificação: ALTA
2 anos / 5 anos / 10 anos: Observabilidade e reversibilidade como critérios de autonomia são princípios de engenharia de sistemas que antecedem IA e sobrevivem a qualquer mudança de modelo.
Justificativa: O framework poderia ter sido escrito para automação de processos em 2005 e seria igualmente válido. A ancoragem em IA generativa é contextual, não estrutural.

## TESTE DE DIFERENCIAÇÃO
Classificação: PROPRIEDADE INTELECTUAL
Justificativa: A matriz observabilidade × reversibilidade como determinante de autonomia é original e operacionalizável. Não encontrei equivalente nos livros da régua de comparação. O mecanismo de rebaixamento automático por incidente é especialmente distintivo.

## TESTE DE MEMORIZAÇÃO
Ideia principal clara? SIM
Qual é a ideia principal: Autonomia do agente = função direta de quanto você consegue rastrear e desfazer — nunca mais que isso.
Justificativa: A regra é simples, contraintuitiva para quem quer deploy rápido, e memorável.

## TESTE DE TRANSFORMAÇÃO
Ao terminar, o leitor consegue fazer o que antes não conseguia:
- Avaliar qualquer agente nos dois eixos da matriz e determinar o nível máximo de autonomia permitido
- Definir gates de promoção com critérios mensuráveis, não com "quando a equipe sentir que está pronto"
- Implementar mecanismo de rebaixamento automático por incidente
- Testar kill switch mensalmente com protocolo documentado

## NOTA FINAL
Estrutura: 9 | Pedagogia: 8 | Clareza: 8 | Autoridade: 10 | Durabilidade: 10 | Diferenciação: 10 | Memorização: 9 | Transformação: 9
**Nota Geral: 9.1**

## DECISÃO EDITORIAL
MANTER COM AJUSTES MENORES

---

# L1-F4 — prompt-ext.md

## RESUMO EXECUTIVO
Nota: 8/10
Veredito: A

## O QUE FUNCIONA
- A estrutura de 5 blocos com regras de posição é clara, aplicável e diretamente derivada do Princípio 2 (Extremidades) — a ponte teórico-prática é explícita e bem executada.
- O conceito de "Constituição" como bloco versionado e governado é um contribuição original importante — nomeia e formaliza uma prática que times avançados fazem informalmente.
- O anti-padrão "Não sanitizar a pergunta viva" é importante e raramente documentado em livros de prompt engineering.
- O exemplo do escritório de advocacia é bem escolhido — risco alto, regras invioláveis identificáveis, formato de saída estruturado.
- A redundância deliberada do bloco 4 (reiterar regra crítica antes do input) é mecanismo contra-intuitivo bem explicado.

## O QUE NÃO FUNCIONA
- O framework não cobre o caso de prompts multimodais (imagem/PDF + texto) — apenas text-in/text-out. Em 2026, esse é um gap real.
- "Sanitizada contra prompt injection" aparece como instrução no Bloco 5 mas não explica como sanitizar — a instrução é incompleta como guia operacional.
- O framework não menciona o limite prático de tokens do Bloco 3 (contexto) — quando o contexto cresce demais, qual é a estratégia de poda? F7 (T3) cobre isso mas a conexão não é explícita aqui.

## ACHADOS

### ACHADO 01
Categoria: P1
Problema: "Sanitizada contra prompt injection" sem instrução de como sanitizar
Por que é um problema: A instrução de sanitizar o input do usuário é correta mas incompleta. O leitor que não tem background em segurança não sabe o que fazer operacionalmente.
Impacto no leitor: Anti-padrão documentado ("Não sanitizar a pergunta viva") mas sem remédio ensinado.
Correção exata: Adicionar 3-4 linhas de guia operacional: "Técnicas básicas de sanitização: (1) delimitar o input do usuário com marcadores XML fixos que a constituição reconhece; (2) nunca interpolar input diretamente em strings de sistema sem delimitação; (3) incluir no adversarial set (F8) casos de prompt injection via input do usuário. Ver Cap 19 para tratamento completo."
Texto sugerido: n/a
ROI: ALTO

### ACHADO 02
Categoria: P2
Problema: Ausência de cobertura de prompts multimodais
Por que é um problema: Em 2026, uma fração significativa dos casos de uso corporativos envolve análise de imagem, PDF, tabela ou vídeo. O framework de 5 blocos foi desenhado para text-only e não orienta sobre onde o input multimodal entra na estrutura.
Impacto no leitor: Leitor com caso de uso multimodal não sabe adaptar o framework.
Correção exata: Adicionar nota ao Bloco 3: "Para prompts multimodais, o input visual (imagem, PDF, tabela) vai no Bloco 3, junto ao contexto textual, nunca no Bloco 5 (onde só vai o texto do usuário). As regras de constituição no Bloco 2 devem explicitamente cobrir como tratar o conteúdo visual — ex.: 'Cite sempre página e número de figura ao referenciar dados do documento.'".
Texto sugerido: n/a
ROI: MÉDIO

### ACHADO 03
Categoria: P2
Problema: Sem instrução de como manejar Bloco 3 quando cresce além do limite prático
Por que é um problema: O framework diz que o Bloco 3 "pode ser maior" mas não orienta sobre o que fazer quando o contexto do Bloco 3 ameaça superar o limite da janela ou degradar a atenção nas extremidades.
Impacto no leitor: Em prompts longos reais, o leitor enfrenta o problema sem guia e pode comprometer as extremidades para acomodar o contexto.
Correção exata: Adicionar: "Quando o Bloco 3 cresce demais: aplicar T3 do F7 (RAG enxuto, compressão de histórico, expiração de memória). A regra é: o Bloco 3 cresce até o ponto em que o Bloco 4 ainda está na posição forte de atenção. Se o Bloco 4 vai para o meio do prompt, a estrutura quebrou — comprimir o Bloco 3 antes."
Texto sugerido: n/a
ROI: MÉDIO

## TESTE DA JOANA
Entenderia: SIM
O que ela entenderia: Os 5 blocos, o exemplo do escritório de advocacia, a lógica de "regra crítica nas extremidades".
O que ela NÃO entenderia: "Prompt injection", "sanitização" sem explicação do que são.
Como corrigir: Aplicar Achado 01 e adicionar uma linha de definição: "Prompt injection: tentativa do usuário de reescrever as instruções do sistema dentro do campo de input — o equivalente digital de um cliente bancário tentando mudar as regras do banco no campo 'motivo da transferência'."

## TESTE DE DURABILIDADE
Classificação: ALTA
2 anos / 5 anos / 10 anos: A física de atenção nas extremidades é derivada da arquitetura transformer — pode precisar de revisão com nova arquitetura. A estrutura de 5 blocos como princípio de composição é durável independentemente da física específica.
Justificativa: O framework sobrevive porque opera no nível de design de prompt (o que vai onde), não no nível de implementação de atenção.

## TESTE DE DIFERENCIAÇÃO
Classificação: PROPRIEDADE INTELECTUAL
Justificativa: O conceito de "Constituição" como bloco versionado e governado, a regra de posição das extremidades e a redundância deliberada do Bloco 4 formam um sistema original. Não existe equivalente consolidado na literatura de prompt engineering.

## TESTE DE MEMORIZAÇÃO
Ideia principal clara? SIM
Qual é a ideia principal: Prompts de produção têm 5 blocos com posições fixas; o crítico vai nas extremidades e nunca no meio.
Justificativa: A estrutura numerada com nomes é memorizável; "extremidades" é âncora mnemônica direta do Princípio 2.

## TESTE DE TRANSFORMAÇÃO
Ao terminar, o leitor consegue fazer o que antes não conseguia:
- Estruturar qualquer prompt de produção nos 5 blocos com posicionamento correto
- Identificar quando um prompt em produção tem regra crítica enterrada no meio
- Versionar a constituição como ativo de governança separado do contexto dinâmico
- Reiterar deliberadamente o crítico no Bloco 4 para reforçar atenção nas extremidades

## NOTA FINAL
Estrutura: 9 | Pedagogia: 8 | Clareza: 8 | Autoridade: 9 | Durabilidade: 8 | Diferenciação: 9 | Memorização: 9 | Transformação: 9
**Nota Geral: 8.6**

## DECISÃO EDITORIAL
MANTER COM AJUSTES

---

# L1-F5 — cobertura-integracoes.md

## RESUMO EXECUTIVO
Nota: 7/10
Veredito: B

## O QUE FUNCIONA
- A nota editorial de neutralidade (seção 2) é rara e corajosa — explicitar que MCP é projeto da Anthropic e ainda assim tratá-lo com igualdade analítica aumenta credibilidade.
- Os seis mecanismos com "quando é a escolha errada" (seção 6) é a parte mais valiosa do framework — a simetria analítica diferencia de tutoriais de MCP.
- O exemplo da telecom (seção 8) é o mais concreto do livro em termos de números — R$ 800 mil vs. R$ 280 mil, sete semanas, trinta por cento de redução no tempo de atendimento. O rigor estatístico declarado ao final do caso é boa prática.
- A matriz de cinco dimensões (leitura, ação, autenticação, observabilidade, conformidade) é aplicável a qualquer integração e age como checklist de produção.

## O QUE NÃO FUNCIONA
- O framework é o mais longo dos nove (aprox. 2.000 palavras) — tem seções que poderiam ser comprimidas sem perda (seção 3 e seção 5 se sobrepõem parcialmente).
- A seção 10 ("Aplicação Prática em 30 Minutos") deveria ser a seção 2 — o leitor que quer usar o framework imediatamente encontra o protocolo de uso apenas no final.
- O título "Matriz de Cobertura de Integrações" não reflete bem o conteúdo principal, que é a decisão de mecanismo por capability — o título sugere uma checklist de cobertura, não um framework de decisão de arquitetura.
- O framework não orienta quando migrar de um mecanismo para outro — apenas quando cada um é a escolha certa inicial. Organizações que já têm REST consolidado não sabem quando vale investir em MCP.

## ACHADOS

### ACHADO 01
Categoria: P1
Problema: Título não reflete o conteúdo principal do framework
Por que é um problema: "Matriz de Cobertura de Integrações" evoca uma checklist de coverage (como F8 evoca a pirâmide). O conteúdo real é um framework de decisão de mecanismo de integração por capability — mais análogo ao F2 (que decide modelo) do que a uma matriz de cobertura.
Impacto no leitor: Expectativa errada antes de abrir o framework; dificulta recuperação por referência cruzada.
Correção exata: Renomear para "F5 — Decisão de Mecanismo de Integração" ou "F5 — Escolha de Integração por Capability". Manter "Matriz de Cobertura" como nome da ferramenta de cinco dimensões dentro do framework, não como nome do framework inteiro.
Texto sugerido: n/a
ROI: MÉDIO

### ACHADO 02
Categoria: P1
Problema: Protocolo de uso ("Aplicação Prática em 30 Minutos") está na seção 10, no final
Por que é um problema: O leitor que quer aplicar o framework imediatamente precisa ler 1.800 palavras antes de encontrar o protocolo de uso. Todos os outros frameworks (F1, F2, F3) colocam o funcionamento operacional no início.
Impacto no leitor: Atrito de uso — o framework mais longo do livro é também o que mais demora para chegar ao "como usar agora".
Correção exata: Mover a seção 10 para seção 2 (logo após o objetivo). Reorganizar para: 1. Objetivo → 2. Como aplicar em 30 minutos → 3. Os seis mecanismos → 4. As cinco dimensões → 5. Exemplos.
Texto sugerido: n/a
ROI: ALTO

### ACHADO 03
Categoria: P2
Problema: Ausência de orientação sobre migração de mecanismo existente
Por que é um problema: A maioria dos leitores não está escolhendo integração do zero — está avaliando se deve migrar de REST para MCP, ou de tool ad-hoc para MCP. O framework não orienta esse caso.
Impacto no leitor: O leitor com REST consolidado não encontra resposta para "quando vale migrar?".
Correção exata: Adicionar subseção "Quando Migrar de Mecanismo": "Critérios que justificam migração: (1) o mecanismo atual impõe custo de manutenção recorrente maior que o custo de migração; (2) novo requisito (descoberta dinâmica, portabilidade entre provedores) não é atendível com o mecanismo atual sem adaptação significativa; (3) incidente recorrente rastreável ao mecanismo. Critérios que não justificam: moda, conferência, o fornecedor lançou SDK novo."
Texto sugerido: n/a
ROI: MÉDIO

### ACHADO 04
Categoria: P0
Problema: Sobreposição temática com F3 e F6 em governança de integração
Por que é um problema: A dimensão "Conformidade" da Matriz de Cobertura (LGPD, AI Act, DPIA) duplica parcialmente o controle 2 (Auditoria) e controle 7 (RACI) do F6. A dimensão "Observabilidade" duplica parcialmente a observabilidade do F3 (eixo X da matriz). Sem indicação explícita de qual framework é autoritativo para cada aspecto, o leitor fica sem saber onde aplicar cada ferramenta.
Impacto no leitor: Risco de aplicar F5 como substituto de F3 e F6 em decisões de governança e autonomia, perdendo a especificidade de cada um.
Correção exata: Adicionar nota de escopo ao início do F5: "Este framework decide o mecanismo de integração (como o agente se conecta ao mundo). Observabilidade de integração aqui trata de visibilidade da chamada de integração — não da observabilidade do agente, que é coberta por F3. Conformidade de integração aqui trata de requisitos de dado na chamada — governança de IA como prática institucional é coberta por F6."
Texto sugerido: n/a
ROI: ALTO

## TESTE DA JOANA
Entenderia: SIM (parcialmente)
O que ela entenderia: Os seis mecanismos na tabela, o exemplo da telecom, a lógica de "cada mecanismo tem seu caso de uso".
O que ela NÃO entenderia: gRPC, Protobuf, event sourcing, OpenTelemetry — termos não definidos inline.
Como corrigir: Adicionar definições em parênteses para os termos mais opacos nas tabelas.

## TESTE DE DURABILIDADE
Classificação: MÉDIA
2 anos: MCP pode ter mudado significativamente como padrão. "Ecossistema em consolidação rápida" é exatamente o tipo de afirmação que envelhece.
5 anos: Os seis mecanismos podem ter sido reduzidos a quatro (se MCP absorver tool ad-hoc) ou expandidos (se novos protocolos emergirem).
10 anos: A estrutura de cinco dimensões (leitura, ação, autenticação, observabilidade, conformidade) é durável — os mecanismos específicos são número.
Justificativa: O framework tem durabilidade ALTA nas dimensões e BAIXA na lista de mecanismos — a separação não está clara o suficiente no texto atual.

## TESTE DE DIFERENCIAÇÃO
Classificação: DIFERENCIADO
Justificativa: A abordagem de igualdade analítica entre seis mecanismos (incluindo MCP) é diferenciada do mercado, que em 2025/2026 trata MCP como resposta universal. Mas o framework é menos original que F1, F3 e F8 — a ideia de "usar a ferramenta certa para cada problema" existe em livros de arquitetura de software.

## TESTE DE MEMORIZAÇÃO
Ideia principal clara? SIM
Qual é a ideia principal: Não existe mecanismo de integração universal — cada capability pede um mecanismo específico; arquitetura madura usa quatro a cinco em paralelo.
Justificativa: O anti-padrão de adoção doutrinária é a âncora memorável.

## TESTE DE TRANSFORMAÇÃO
Ao terminar, o leitor consegue fazer o que antes não conseguia:
- Aplicar a matriz de cinco dimensões a qualquer integração em 30 minutos
- Identificar quando MCP é a escolha errada (latência crítica, REST consolidado, conformidade específica)
- Evitar adoção doutrinária de mecanismo único

## NOTA FINAL
Estrutura: 6 | Pedagogia: 7 | Clareza: 7 | Autoridade: 8 | Durabilidade: 6 | Diferenciação: 7 | Memorização: 7 | Transformação: 8
**Nota Geral: 7.0**

## DECISÃO EDITORIAL
REVISAR PARCIALMENTE

---

# L1-F6 — gov-indelegavel.md

## RESUMO EXECUTIVO
Nota: 8/10
Veredito: A

## O QUE FUNCIONA
- Três camadas × dez controles é estrutura elegante, completa e aplicável — cobre da auditoria técnica ao AI Council executivo.
- A escala de maturidade 0-4 (inexistente → declarado → implementado → auditado → melhoria contínua) é ferramenta de diagnóstico imediata.
- "Maturidade 2 sem auditoria é teatro" é a frase mais precisa do livro sobre o problema de governança de AI.
- O exemplo da seguradora com diagnóstico pré-incidente e plano pós-incidente é o mais realista dos exemplos do livro — vem de um cenário regulatório credível (ANPD, multa, negação automatizada).
- O output em ≤6 páginas é restrição pedagógica correta — governança eficaz não precisa de documento de 80 páginas.

## O QUE NÃO FUNCIONA
- O anti-padrão "Vamos terceirizar o problema" toca em accountability mas não orienta o que terceirizar é legítimo vs. o que é inevitavelmente interno. Há casos onde terceirizar é a resposta certa (auditoria externa, DPIA por especialista).
- O AI Council (controle 10) é o único controle executivo mas não tem cadência sugerida para primeiros 6 meses vs. regime estável — o exemplo da seguradora menciona "mensal nos primeiros 6 meses" mas o framework em si não generaliza isso.
- O RACI menciona "8 papéis × 12 decisões mínimas" mas não lista os 12 tipos de decisão — o leitor não sabe o que são essas 12 decisões sem ir ao Apêndice O.

## ACHADOS

### ACHADO 01
Categoria: P1
Problema: "8 papéis × 12 decisões mínimas" sem listagem das 12 decisões no corpo do framework
Por que é um problema: O leitor que quer construir o RACI imediatamente não sabe quais são as 12 decisões mínimas. O exemplo da seguradora lista 8 papéis mas apenas 3 exemplos de decisões (modelo, prompt, dataset). Para construir o RACI, o leitor precisa ir ao Apêndice O — que pode não estar disponível no contexto de leitura.
Impacto no leitor: Framework fica incompleto sem o Apêndice — quebra a autonomia do framework como ferramenta standalone.
Correção exata: Adicionar inline as 12 decisões mínimas do RACI em tabela compacta, com indicação de que o Apêndice O tem o template completo.
Texto sugerido: n/a (requer listagem das 12 decisões — verificar Apêndice O)
ROI: ALTO

### ACHADO 02
Categoria: P2
Problema: Anti-padrão "Vamos terceirizar o problema" sem distinção entre terceirização legítima e ilegítima
Por que é um problema: Auditoria externa periódica (controle 5 da tabela anti-padrão menciona que "auditoria interna sem auditoria externa periódica" é anti-padrão), consultoria de DPIA, certificação ISO/IEC 42001 — todos são exemplos de terceirização legítima. O anti-padrão como escrito pode ser interpretado como "não terceirize nada", o que é errado.
Impacto no leitor: Confusão entre terceirização de accountability (errada) e terceirização de execução especializada (correta em muitos casos).
Correção exata: Reformular: "Compliance terceirizado como substituto de accountability é anti-padrão — a responsabilidade nominal não pode ir para o terceiro. Execução especializada terceirizada (auditoria externa, consultoria de DPIA, certificação) é legítima e recomendada onde o time interno não tem capacidade técnica."
Texto sugerido: (acima)
ROI: MÉDIO

### ACHADO 03
Categoria: P2
Problema: AI Council sem cadência-padrão generalizada no framework
Por que é um problema: O exemplo da seguradora menciona "mensal nos primeiros 6 meses" mas o framework em si não generaliza uma cadência para o AI Council. Sem orientação, cada organização inventará sua própria cadência (tipicamente trimestral, que é insuficiente para os primeiros 12 meses).
Impacto no leitor: AI Council pode ser criado com cadência inadequada para o momento da organização.
Correção exata: Adicionar na descrição do controle 10: "Cadência mínima: mensal nos primeiros 12 meses, passando para trimestral com revisão de maturidade após o primeiro ano. Organizações em setor regulado (saúde, financeiro) mantêm mensal de forma permanente."
Texto sugerido: n/a
ROI: MÉDIO

## TESTE DA JOANA
Entenderia: SIM
O que ela entenderia: As três camadas, os dez controles, o exemplo da seguradora, a escala de maturidade 0-4.
O que ela NÃO entenderia: "Tracing (pilares 1 de LLMOps)" sem contexto do que são os pilares de LLMOps; "evals em CI" sem definição de CI.
Como corrigir: Adicionar parênteses: "Tracing (registro de cada chamada de IA com identificação, input, output e latência)" e "Evals em CI (testes automáticos de qualidade que rodam antes de qualquer mudança entrar em produção)".

## TESTE DE DURABILIDADE
Classificação: ALTA
2 anos / 5 anos / 10 anos: Os dez controles são independentes de modelo, versão ou fornecedor. A regulação citada (LGPD, AI Act, NIST AI RMF, ISO/IEC 42001) pode evoluir, mas os princípios de controle são estáveis.
Justificativa: Governança institucional como prática muda em décadas, não em meses. O framework duraria igualmente para governança de dados em 2015.

## TESTE DE DIFERENCIAÇÃO
Classificação: PROPRIEDADE INTELECTUAL
Justificativa: A combinação de três camadas + dez controles + escala de maturidade + output em ≤6 páginas é original. A distinção entre "maturidade declarada" e "maturidade implementada" como critério de teatro vs. prática real é especialmente precisa.

## TESTE DE MEMORIZAÇÃO
Ideia principal clara? SIM
Qual é a ideia principal: Governança real fecha o triângulo técnica-operacional-executiva com dez controles mensuráveis — declarado sem implementado é teatro.
Justificativa: "Maturidade 2 sem auditoria é teatro" é a frase mais citável do framework.

## TESTE DE TRANSFORMAÇÃO
Ao terminar, o leitor consegue fazer o que antes não conseguia:
- Diagnosticar a maturidade de governança atual em 10 dimensões em menos de uma hora
- Identificar quais controles estão em maturidade de teatro (declarado sem implementado)
- Montar plano de 90/180/365 dias com metas de maturidade por controle
- Construir AI Council com mandato, cadência e donos nominais

## NOTA FINAL
Estrutura: 9 | Pedagogia: 8 | Clareza: 8 | Autoridade: 9 | Durabilidade: 9 | Diferenciação: 9 | Memorização: 8 | Transformação: 9
**Nota Geral: 8.6**

## DECISÃO EDITORIAL
MANTER COM AJUSTES

---

# L1-F7 — composto-3t.md

## RESUMO EXECUTIVO
Nota: 8/10
Veredito: A

## O QUE FUNCIONA
- A fórmula explícita do custo composto (tokens × chamadas × redundância × tier) é o único framework do livro que entrega matemática direta — altamente citável.
- A ordem fixa T1 → T2 → T3 com justificativa de impacto e risco por alavanca é pedagogicamente excelente.
- "Economia típica observada" por alavanca com faixa percentual é orientação concreta que outros livros evitam por medo de comprometer-se.
- O caso Pólice.io com diagnóstico + plano + resultado em R$ é o exemplo mais numérico do livro — R$ 142 mil → R$ 47 mil, distribuição final de tiers.
- O anti-padrão "Otimizar tamanho do prompt enquanto agente loopa no Opus" é o mais memorável do livro inteiro.

## O QUE NÃO FUNCIONA
- "Economia típica observada" — as faixas percentuais (30-60%, 20-50%, 15-40%) não têm fonte declarada. São estimativas do autor ou de literatura pública? Sem fonte, um leitor técnico as questiona como marketing.
- T2 menciona "Circuit breaker contra runaway loops" mas não explica o que é um runaway loop ou como implementar o circuit breaker — é o mecanismo mais crítico de T2 e o menos explicado.
- O framework não orienta a ordem de diagnóstico: como o leitor sabe qual dos três termos (chamadas, redundância, tier) é o que mais escala em seu sistema sem instrumentação?

## ACHADOS

### ACHADO 01
Categoria: P1
Problema: Faixas de "economia típica observada" sem fonte
Por que é um problema: 30-60% de economia com T1, 20-50% com T2, 15-40% com T3 são afirmações de impacto que sustentam a decisão executiva de investir nas alavancas. Sem fonte, são assertivas sem evidência — exatamente o que o Princípio 7 (Termômetro) combate.
Impacto no leitor: Leitor técnico questiona as faixas. CFO que baseia justificativa de projeto nelas fica exposto.
Correção exata: Adicionar nota de fonte: "Faixas baseadas em análise de casos de uso corporativos documentados e em tabelas de pricing públicas dos principais fornecedores (consultar Apêndice J). Economia real depende de arquitetura atual, volume e mix de tarefas — validar contra atribuição de custo própria antes de usar como projeção."
Texto sugerido: n/a
ROI: ALTO

### ACHADO 02
Categoria: P1
Problema: "Circuit breaker" mencionado mas não explicado
Por que é um problema: Circuit breaker é mecanismo de T2 com ROI alto e implementação não trivial — limitar chamadas por sessão ou usuário exige instrumentação de estado que o framework não orienta.
Impacto no leitor: Leitor sabe que precisa de circuit breaker mas não sabe como implementá-lo nem o que dispara o bloqueio.
Correção exata: Adicionar 3-4 linhas: "Circuit breaker de custo: define um limite máximo de chamadas ao modelo premium por sessão de usuário (ex.: 5 chamadas Opus por sessão). Quando o limite é atingido, a sessão cai automaticamente para o tier inferior ou retorna erro amigável ao usuário. Implementação: contagem de chamadas por session_id com cache de curta duração (Redis ou equivalente); decremento automático na virada da janela de tempo."
Texto sugerido: n/a
ROI: ALTO

### ACHADO 03
Categoria: P2
Problema: Sem orientação de diagnóstico pré-aplicação das alavancas
Por que é um problema: O leitor que não tem instrumentação de custo por feature (Pilar 5 de LLMOps) não consegue identificar qual dos três termos é o dominante. O framework pressupõe que o leitor já tem atribuição de custo.
Impacto no leitor: Leitor sem instrumentação aplica T1 por padrão (porque é o mais visível) mesmo quando T2 seria o correto.
Correção exata: Adicionar "Diagnóstico de pré-requisito" antes das três alavancas: "Antes de aplicar qualquer T, instalar atribuição de custo por feature (Pilar 5 de LLMOps — F7 pressupõe isso). Sem atribuição, o diagnóstico inicial usa estimativa: se >70% do volume é tier premium, começar por T1; se o sistema tem loops de agente visíveis, começar por T2; se o contexto médio por chamada supera 50% da janela disponível, começar por T3."
Texto sugerido: n/a
ROI: MÉDIO

## TESTE DA JOANA
Entenderia: SIM (parcialmente)
O que ela entenderia: A fórmula, os três T, o caso Pólice.io com os números.
O que ela NÃO entenderia: "Prompt caching", "prefixo estável", "circuit breaker", "RAG enxuto" — todos mencionados sem definição inline.
Como corrigir: Adicionar glossário inline ou notas de rodapé para os quatro termos mais opacos.

## TESTE DE DURABILIDADE
Classificação: ALTA
2 anos / 5 anos / 10 anos: A fórmula custo = tokens × chamadas × redundância × tier é estruturalmente durável enquanto o modelo de pricing por token existir. As alavancas T1/T2/T3 são independentes de versão de modelo.
Justificativa: O risco de envelhecimento está nas faixas de "economia típica" — os percentuais podem mudar conforme fornecedores alteram preços. A estrutura permanece.

## TESTE DE DIFERENCIAÇÃO
Classificação: PROPRIEDADE INTELECTUAL
Justificativa: A fórmula explícita com os três termos e a ordem fixa de alavancas T1→T2→T3 com justificativa de impacto é original. "O termo trivial vs. o termo composto" é a distinção mais valiosa do framework.

## TESTE DE MEMORIZAÇÃO
Ideia principal clara? SIM
Qual é a ideia principal: O custo real de IA não está no preço por token (termo trivial) mas no produto de chamadas × redundância × tier — as três alavancas de otimização são arquiteturais, não textuais.
Justificativa: A fórmula e o anti-padrão "otimizar o prompt enquanto o agente loopa" são âncoras mnemônicas fortes.

## TESTE DE TRANSFORMAÇÃO
Ao terminar, o leitor consegue fazer o que antes não conseguia:
- Calcular o custo composto de uma feature com a fórmula explícita
- Identificar qual dos três termos é o dominante na fatura atual
- Aplicar T1 antes de T2 antes de T3, com justificativa de impacto
- Estimar a economia potencial de cada alavanca antes de priorizar

## NOTA FINAL
Estrutura: 9 | Pedagogia: 8 | Clareza: 7 | Autoridade: 7 | Durabilidade: 8 | Diferenciação: 9 | Memorização: 9 | Transformação: 8
**Nota Geral: 8.1**

## DECISÃO EDITORIAL
MANTER COM AJUSTES

---

# L1-F8 — eval-piramide.md

## RESUMO EXECUTIVO
Nota: 9/10
Veredito: A+

## O QUE FUNCIONA
- A pirâmide de três camadas (base determinística + meio golden set/LLM-judge + topo humano especialista) com faixa transversal adversarial é a estrutura de eval mais completa disponível em livro de não-ficção de IA.
- O custo crescente por camada (muito baixo → médio → alto) como critério de alocação de recursos é correto e raramente articulado.
- "LLM-as-judge sem calibração contra humano: viés institucionalizado" é o achado mais importante sobre avaliação de IA generativa e está correto.
- O exemplo Atlas Strategy (vibe-eval → pirâmide v1) é o mais completo do livro em termos de especificação técnica: golden set de 80 itens, correlação 0,82 contra 3 sócios, política de bloqueio com delta explícito.
- A camada adversarial com renovação trimestral e casos vindos de produção é orientação correta que distingue do que outros livros chamam de "testes de segurança".
- A correlação alvo ≥0,7 entre LLM-judge e humano é número operacional específico — raro e valioso.

## O QUE NÃO FUNCIONA
- A camada adversarial é descrita como "transversal" mas não está integrada à mecânica de CI (não está claro se bloqueia deploy ou apenas alerta).
- "30 casos: paciente com sycophancy, prompt injection via dado de cliente, números invertidos sutilmente..." no exemplo da Atlas Strategy são casos específicos de consultoria — o leitor sem esse contexto não sabe como construir seu próprio adversarial set para outro domínio.
- O framework não orienta como dimensionar o golden set além de "30-50 casos representativos" — sem critério de representatividade, o leitor constrói golden set enviesado.

## ACHADOS

### ACHADO 01
Categoria: P1
Problema: Camada adversarial não integrada explicitamente à política de bloqueio em CI
Por que é um problema: A política de bloqueio no output especifica "Delta que bloqueia merge, delta que alerta, delta que passa" mas não menciona a camada adversarial. O exemplo da Atlas Strategy diz "zero passagens" para adversarial mas isso não está na mecânica geral do framework.
Impacto no leitor: Leitor implementa CI com bloqueio na camada do meio mas não adiciona adversarial como gate — exatamente o ponto cego que o adversarial set existe para cobrir.
Correção exata: Adicionar à tabela de política de bloqueio: "Adversarial: qualquer passagem em adversarial de segurança bloqueia merge (zero-tolerance por padrão; exceção documentada requer aprovação do dono nominal do sistema)."
Texto sugerido: n/a
ROI: ALTO

### ACHADO 02
Categoria: P1
Problema: Critério de representatividade do golden set não definido
Por que é um problema: "30-50 casos representativos com gabarito" é instrução incompleta. O que torna um caso representativo? Sem critério, o leitor cria golden set dos casos mais fáceis (que o modelo já acerta) ou dos casos que vieram à mente mais rapidamente (viés de disponibilidade).
Impacto no leitor: Golden set que não representa a distribuição real de produção não detecta regressão real — a pirâmide parece funcionar mas não protege.
Correção exata: Adicionar: "Critério de representatividade: o golden set deve cobrir (1) os tipos de tarefa com maior volume em produção; (2) os subgrupos de usuário ou domínio onde regressão seria mais custosa; (3) casos de borda conhecidos (edge cases documentados em incidentes anteriores); (4) casos em que o modelo correntemente falha (para monitorar melhoria, não só manter o que funciona)."
Texto sugerido: n/a
ROI: ALTO

### ACHADO 03
Categoria: P2
Problema: Guia de construção de adversarial set específico de domínio ausente
Por que é um problema: O exemplo da Atlas Strategy lista categorias específicas de consultoria (sycophancy de cliente forçando conclusão, números invertidos sutilmente). O leitor de RH, saúde ou financeiro não sabe como adaptar para seu domínio.
Impacto no leitor: Adversarial set copiado do exemplo em vez de construído para o domínio real — cobertura teórica, falhas reais escapam (o próprio anti-padrão do F8).
Correção exata: Adicionar orientação de construção por domínio: "Construa o adversarial set a partir de três fontes: (1) incidentes anteriores do próprio sistema ou de sistemas similares no setor; (2) literatura de segurança (HarmBench, JailbreakBench, BBQ) como baseline; (3) brainstorm adversarial com o time de produto — 'o que queríamos que o modelo nunca fizesse?'. Para cada domínio, há categorias específicas: em RH, viés demográfico; em financeiro, sycophancy em análise de risco; em clínico, over-confidence em diagnóstico diferencial."
Texto sugerido: n/a
ROI: MÉDIO

## TESTE DA JOANA
Entenderia: SIM
O que ela entenderia: As três camadas, o custo crescente, o exemplo da Atlas Strategy, a política de bloqueio.
O que ela NÃO entenderia: "Faithfulness", "LLM-as-judge", "exact match", "schema validation" — termos técnicos de eval não definidos.
Como corrigir: Adicionar linha de definição por camada: "Schema validation: verificação automática de que a saída tem a estrutura correta (campos obrigatórios presentes, formato correto). Exact match: verificação de que um campo específico tem o valor exato esperado. LLM-as-judge: uso de um modelo de linguagem separado para avaliar a qualidade da saída do modelo principal, aplicando uma rubrica definida."

## TESTE DE DURABILIDADE
Classificação: ALTA
2 anos / 5 anos / 10 anos: A estrutura de três camadas é derivada de princípios de engenharia de qualidade que antecedem IA — smoke tests, regression tests, human QA. Sobrevive a qualquer mudança de modelo.
Justificativa: "LLM-as-judge calibrado" pode mudar de implementação com novos modelos, mas o princípio de calibração contra humano é durável.

## TESTE DE DIFERENCIAÇÃO
Classificação: PROPRIEDADE INTELECTUAL
Justificativa: A pirâmide com faixa adversarial transversal, política de bloqueio explícita, correlação alvo de LLM-judge e orientação de custo por camada forma o sistema de eval mais operacional disponível em livro de não-ficção sobre IA. Os livros da régua de comparação (Co-Intelligence, Competing in the Age of AI) não têm equivalente.

## TESTE DE MEMORIZAÇÃO
Ideia principal clara? SIM
Qual é a ideia principal: Eval tem três camadas com custo e cobertura inversamente proporcionais — construir de baixo para cima; base barata cobre tudo, topo caro cobre o crítico.
Justificativa: A metáfora da pirâmide é universalmente reconhecível; "vibe-eval" como anti-estado inicial é memorável.

## TESTE DE TRANSFORMAÇÃO
Ao terminar, o leitor consegue fazer o que antes não conseguia:
- Construir pirâmide de eval mínima em 1-4 semanas (base + golden set + adversarial básico)
- Calibrar LLM-as-judge contra humano com meta de correlação ≥0,7
- Definir política de bloqueio em CI com delta explícito por camada
- Identificar anti-padrões de eval em seu sistema atual (vibe-eval, golden set sem renovação, adversarial só de literatura)

## NOTA FINAL
Estrutura: 10 | Pedagogia: 9 | Clareza: 8 | Autoridade: 9 | Durabilidade: 9 | Diferenciação: 10 | Memorização: 9 | Transformação: 9
**Nota Geral: 9.1**

## DECISÃO EDITORIAL
MANTER COM AJUSTES MENORES

---

# L1-F9 — rota-dupla.md

## RESUMO EXECUTIVO
Nota: 7/10
Veredito: B

## O QUE FUNCIONA
- A mecânica de duas trilhas com cadências distintas é a materialização operacional do Princípio 3 (Camada Dupla) — a ponte é explícita e bem executada.
- A tabela de identificação do insumo da decisão (trilha + onde buscar) no exemplo do CTO é o melhor exercício de aplicação do livro — transforma a distinção teórica em protocolo concreto de pré-decisão.
- O anti-padrão "Atualizar o padrão na mesma cadência do número" é preciso e raramente articulado.
- A instrução de diagnóstico pessoal ("listar o que se sabe sobre IA hoje; para cada item, classificar: padrão ou número?") é exercício de alto valor pedagógico.

## O QUE NÃO FUNCIONA
- O F9 é o mais curto e o mais dependente dos outros — quase toda a seção de "O que vai aqui" na Trilha Padrão é uma lista de referências cruzadas (F1-F9, Caps 01-14, etc.). Isso é correto pedagogicamente mas torna o F9 o framework mais fraco como documento standalone.
- A Trilha Número inclui "Datas de regulação aplicável (versões de LGPD, AI Act, NIST AI RMF)" — mas regulação não é um "número volátil" no mesmo sentido que preço de token ou benchmark. Tem ciclos de atualização longos (meses a anos) e impacto jurídico, não apenas de mercado. Misturar regulação com preço de token na Trilha Número é classificação inexata.
- O framework não orienta o que fazer quando o leitor descobre, no diagnóstico inicial, que tem quase nenhum padrão internalizado — a trilha de migração pressupõe que algo já está classificado, não que tudo é "número" ou "não sei".
- Sobreposição com C00P (por que padrão dura e número morre): F9 é o framework operacional do que C00P argumenta conceitualmente, mas a divisão de conteúdo entre os dois não é sempre clara — alguns leitores podem sentir que um dos dois é dispensável.

## ACHADOS

### ACHADO 01
Categoria: P1
Problema: Regulação classificada como "número volátil" junto com preço de token
Por que é um problema: LGPD, AI Act e NIST AI RMF têm ciclos de atualização de 12-24 meses e impacto jurídico de compliance — não têm a mesma meia-vida de benchmark de modelo (semanas) ou preço de token (meses). Tratar os dois com a mesma cadência de consulta ("sob demanda antes de decisão") é correto operacionalmente mas a classificação como "número" é conceitualmente imprecisa.
Impacto no leitor: Risco de o leitor consultar status regulatório com mesma urgência que preço de token (insuficiente) ou tratar regulação como "padrão na cabeça" sem consultar versão vigente (perigoso juridicamente).
Correção exata: Criar subcategoria dentro da Trilha Número: "Número de alta meia-vida (regulação): LGPD, AI Act, NIST AI RMF — consulta periódica a cada 6 meses e antes de decisões com impacto de compliance. Número de baixa meia-vida (mercado): versões, preços, benchmarks — consulta sob demanda antes de cada decisão relevante."
Texto sugerido: n/a
ROI: MÉDIO

### ACHADO 02
Categoria: P1
Problema: Ausência de orientação para o leitor que descobre ter "zero padrão internalizado"
Por que é um problema: A mecânica de diagnóstico instrui "classificar cada item em padrão ou número". Um leitor iniciante pode descobrir que tem principalmente números (versões, preços, benchmark) e quase nenhum padrão. O F9 não orienta o que fazer nesse caso — não há caminho de entrada para o leitor em estado zero.
Impacto no leitor: O leitor mais importante (o que mais precisa do framework) sente que o framework não foi feito para ele.
Correção exata: Adicionar subseção: "Ponto de partida zero: se o diagnóstico mostra principalmente números e poucos padrões, o caminho de entrada é a Trilha Padrão em ordem linear do livro — os 9 Invariantes (C00M) + os 9 frameworks (F1-F9) são o núcleo mínimo de padrão. Prioridade: internalizar os 9 Invariantes antes de qualquer framework específico. Cadência sugerida para iniciante: dedicar 4 semanas à leitura do corpo do livro antes de consultar qualquer número do Apêndice J."
Texto sugerido: n/a
ROI: ALTO

### ACHADO 03
Categoria: P0
Problema: Sobreposição estrutural com C00P sem divisão de trabalho clara
Por que é um problema: L1-C00P demonstra a distinção padrão × número com quatro casos históricos. F9 operacionaliza essa distinção com duas trilhas. O leitor que lê C00P pode sentir que F9 é repetição com listas, e o leitor que lê F9 primeiro pode sentir que C00P é contexto desnecessário. A divisão de trabalho não está explicitada.
Impacto no leitor: Risco de pular um dos dois por perceber sobreposição — e perder ou a evidência histórica (C00P) ou o protocolo operacional (F9).
Correção exata: Adicionar ao início de F9: "Este framework é o protocolo operacional de o que C00P argumenta historicamente. Se você leu C00P, F9 é o 'como fazer' do que C00P demonstrou ser verdadeiro. Se você não leu C00P, F9 funciona como protocolo standalone — mas C00P entrega a evidência histórica que convence o CTO resistente."
Texto sugerido: (acima, com ajuste de tom)
ROI: ALTO

### ACHADO 04
Categoria: P2
Problema: F9 é o único framework sem exemplo memorável com números reais
Por que é um problema: F1 tem o caso de currículos. F3 tem o caso do e-mail de boas-vindas. F7 tem o caso Pólice.io. F8 tem o caso Atlas Strategy. F9 tem apenas "CTO de SaaS B2B" como cenário de exemplo — sem nome de empresa, sem números de resultado, sem ganho mensurável.
Impacto no leitor: O framework menos memorável do conjunto é também o que mais depende de engajamento ativo do leitor para ser internalized.
Correção exata: Adicionar caso com resultado mensurável: ex., CTO que perdeu 3 ciclos de migração seguindo números memorizados, e recuperou a decisão após aplicar F9 para separar o que sabia vs. o que precisava consultar.
Texto sugerido: n/a
ROI: MÉDIO

## TESTE DA JOANA
Entenderia: SIM
O que ela entenderia: As duas trilhas, o exemplo do CTO com a tabela de insumos, a instrução de diagnóstico pessoal.
O que ela NÃO entenderia: A lista de benchmarks na Trilha Número (SWE-bench Verified, GPQA Diamond, OSWorld) sem definição inline.
Como corrigir: Adicionar parêntese: "benchmarks de avaliação de modelos — listas atualizadas no Apêndice J".

## TESTE DE DURABILIDADE
Classificação: ALTA
2 anos / 5 anos / 10 anos: A distinção padrão × número é independente de tecnologia específica. A mecânica de duas trilhas com cadências diferentes é durável.
Justificativa: O framework perdura enquanto o mercado de IA tiver distinção entre o que muda rápido (versões, preços) e o que muda devagar (princípios, padrões arquiteturais).

## TESTE DE DIFERENCIAÇÃO
Classificação: DIFERENCIADO
Justificativa: O framework é original como protocolo operacional mas é menos diferenciado que F3 e F8 como propriedade intelectual — a ideia de "separar o que aprendo do que consulto" existe em outros contextos (Zettelkasten, Getting Things Done, etc.). A originalidade está na aplicação específica para o campo de IA e na ancoragem na estrutura do livro.

## TESTE DE MEMORIZAÇÃO
Ideia principal clara? SIM
Qual é a ideia principal: Toda peça de conhecimento sobre IA pertence a uma de duas trilhas com cadências distintas — padrão na cabeça, número no Apêndice J.
Justificativa: A bifurcação é simples e memorizável; "decore o padrão, consulte o número" é o slogan do framework.

## TESTE DE TRANSFORMAÇÃO
Ao terminar, o leitor consegue fazer o que antes não conseguia:
- Classificar qualquer peça de conhecimento sobre IA em padrão ou número em 30 segundos
- Construir o mapa pessoal de padrões dominados vs. gaps
- Consultar o Apêndice J como reflexo antes de qualquer decisão que use número como insumo
- Identificar quando está usando memória de número obsoleto como fundamento de decisão

## NOTA FINAL
Estrutura: 7 | Pedagogia: 7 | Clareza: 8 | Autoridade: 7 | Durabilidade: 9 | Diferenciação: 7 | Memorização: 8 | Transformação: 7
**Nota Geral: 7.5**

## DECISÃO EDITORIAL
MANTER COM AJUSTES

---

# ANÁLISE TRANSVERSAL — SOBREPOSIÇÃO E REDUNDÂNCIA ENTRE FRAMEWORKS

Esta seção é obrigatória dado o mandato da banca para os frameworks como propriedade intelectual central.

## MAPA DE SOBREPOSIÇÕES DETECTADAS

| Tema | Frameworks com sobreposição | Gravidade |
|------|-----------------------------|-----------|
| Observabilidade / tracing | F3 (eixo X da matriz) + F5 (dimensão observabilidade) + F6 (controle 5) + F7 (pré-requisito T2) | P0 — sem divisão de trabalho declarada |
| Responsabilidade nominal / dono | F1 (Pergunta 5) + F3 (gates de promoção) + F6 (RACI + donos nominais) | P1 — sobreposição funcional, mas cada um tem escopo diferente |
| Eval como gate de decisão | F1 (Pergunta 4) + F3 (gates de promoção) + F7 (eval sustenta T1) + F8 (pirâmide completa) | P1 — F8 é autoritativo; outros referenciando F8 é correto, mas a profundidade de cobertura varia |
| Camada Dupla / padrão vs. número | C00P (argumento histórico) + F9 (protocolo operacional) | P1 — divisão de trabalho não explicitada |
| Autonomia de agente e risco | F1 (Pergunta 3) + F3 (matriz completa) | P2 — F1 classifica o risco; F3 decide o nível — sequência correta, mas o leitor precisa seguir os dois |

## ACHADO TRANSVERSAL 01
Categoria: P0
Problema: Observabilidade como conceito aparece em quatro frameworks (F3, F5, F6, F7) com profundidades e escopos diferentes sem âncora declarada
Por que é um problema: F3 define observabilidade como eixo da matriz de autonomia (tracing por span, replay). F5 define observabilidade como dimensão da integração (OpenTelemetry, log estruturado). F6 define observabilidade como controle 5 (pilares de LLMOps). F7 pressupõe atribuição de custo (Pilar 5 de LLMOps). Cada definição é ligeiramente diferente e nenhuma delas aponta para uma âncora autoritativa. O leitor que aplica os quatro frameworks em sequência constrói quatro implementações de observabilidade que podem ser redundantes ou conflitantes.
Impacto no leitor: Risco real de implementação fragmentada — um sistema com tracing de integração (F5) mas sem tracing de agente (F3), e com log de custo (F7) mas sem auditoria imutável de governança (F6). Cada framework cobre um aspecto e o leitor sem visão sistêmica perde a integração.
Correção exata: Declarar âncora: observabilidade de IA em produção tem um capítulo autoritativo (Cap 22 — LLMOps) e quatro aplicações em contextos específicos (F3: autonomia de agente; F5: integração; F6: governança; F7: custo). Adicionar nota de escopo a cada framework que mencione observabilidade.
ROI: ALTO

## ACHADO TRANSVERSAL 02
Categoria: P1
Problema: Redundância entre F1 (Pergunta 4) e F8 cria dois "donos" de eval sem hierarquia clara
Por que é um problema: F1 exige "linha de medição" como gate para qualquer iniciativa ir para produção, e menciona "golden set inicial" como referência. F8 é o framework completo de pirâmide de eval. O leitor que aplica F1 sem F8 pode concluir que a "linha de medição" de F1 é suficiente; o que aplica F8 sem F1 pode não conectar eval ao gate de decisão de adoção.
Correção exata: Adicionar em F1 Pergunta 4: "A linha de medição aqui é o insumo mínimo para decisão de vai/não-vai. O sistema completo de eval que sustenta produção é definido em F8."
ROI: MÉDIO

## ACHADO TRANSVERSAL 03
Categoria: P1
Problema: F9 como framework de "meta-framework" enfraquece sua posição — o leitor pode não entender por que F9 existe separado da lógica do C00P
Por que é um problema: Dos nove frameworks, F9 é o único que descreve como usar os outros oito (e o livro inteiro) em vez de resolver um problema específico do operador. Isso é correto como síntese mas cria assimetria — F9 não é equivalente aos outros oito em profundidade e especificidade.
Correção exata: Ou (a) posicionar F9 como "Apêndice de Método" em vez de framework de mesmo nível, ou (b) aprofundar F9 com caso memorável próprio e guia de diagnóstico inicial que os outros oito não cobrem.
ROI: MÉDIO

---

## LINHAS-TRACKER

```
C00M|L1-C00M-manifesto-invariantes.md|01|P1|ALTO|Inconsistência nomenclatura princípios vs invariantes|Padronizar nome: Invariantes ou Princípios Permanentes|MANTER COM AJUSTES
C00M|L1-C00M-manifesto-invariantes.md|02|P1|ALTO|Princípio 9 sem mecânica causal identificável|Adicionar mecanismo de amplificação bidirecional|MANTER COM AJUSTES
C00M|L1-C00M-manifesto-invariantes.md|03|P2|MÉDIO|Analogia navegação longa demais para manifesto|Condensar para 1 parágrafo|MANTER COM AJUSTES
C00M|L1-C00M-manifesto-invariantes.md|04|P2|BAIXO|Drucker e Engelbart citados sem ponte para IA generativa|Explicitar conexão ou remover da seção de princípios|MANTER COM AJUSTES
C00M|L1-C00M-manifesto-invariantes.md|05|P2|MÉDIO|Exercício versão de bolso sem exemplo concreto|Adicionar exemplo de transformação para 2 princípios|MANTER COM AJUSTES
C00P|L1-C00P-porque-padrao-dura.md|01|P1|ALTO|Conflito de interesse: Anthropic citada como árbitro neutro no caso LangChain|Adicionar declaração de transparência ou citar outros fornecedores|MANTER COM AJUSTES
C00P|L1-C00P-porque-padrao-dura.md|02|P1|MÉDIO|Tese principal repetida 4x sem nova camada|Fundir P.6 com P.7; eliminar repetições em P.1 e P.8|MANTER COM AJUSTES
C00P|L1-C00P-porque-padrao-dura.md|03|P2|MÉDIO|Seção P.9 repete P.8.5 com menos elegância|Eliminar P.9 ou reduzir a 2 parágrafos|MANTER COM AJUSTES
C00P|L1-C00P-porque-padrao-dura.md|04|P2|ALTO|Preços de fine-tuning no corpo violam o método do próprio capítulo|Mover para nota de rodapé datada ou Apêndice J|MANTER COM AJUSTES
C00P|L1-C00P-porque-padrao-dura.md|05|P1|MÉDIO|Avaliação US$ 200M LangChain Inc. no corpo — número volátil e sem relevância para o argumento|Remover ou mover para nota datada|MANTER COM AJUSTES
F1|L1-F1-decid-ia.md|01|P1|ALTO|Ausência de gate de veto por risco irreversível alto|Adicionar cláusula de bloqueio automático para irreversível + impacto crítico|MANTER COM AJUSTES
F1|L1-F1-decid-ia.md|02|P1|ALTO|Nível de autonomia sem definição inline dos 4 níveis|Adicionar caixa de referência rápida inline|MANTER COM AJUSTES
F1|L1-F1-decid-ia.md|03|P2|MÉDIO|Campo Revisão Programada sem cadência sugerida|Adicionar cadência-padrão por nível de autonomia|MANTER COM AJUSTES
F2|L1-F2-encaixe-5.md|01|P1|ALTO|Eixo custo crítico conflate tier e self-hosted — decisões arquiteturais distintas|Separar em subeixos ou adicionar nota de decisão|MANTER COM AJUSTES
F2|L1-F2-encaixe-5.md|02|P1|ALTO|Ausência de lógica de desempate para eixos dominantes que apontam para modelos diferentes|Adicionar regra de desempate por custo de erro|MANTER COM AJUSTES
F2|L1-F2-encaixe-5.md|03|P2|MÉDIO|Benchmarks citados sem glossário mínimo inline|Adicionar definição entre parênteses para SWE-bench Verified|MANTER COM AJUSTES
F3|L1-F3-agente-prop.md|01|P2|ALTO|Ausência de matriz visual 4x4|Adicionar diagrama com quadrantes de autonomia|MANTER COM AJUSTES MENORES
F3|L1-F3-agente-prop.md|02|P1|ALTO|Tracing por span e replay sem definição inline|Adicionar definições operacionais inline|MANTER COM AJUSTES MENORES
F3|L1-F3-agente-prop.md|03|P2|MÉDIO|Critério de N dias para promoção sem guia de calibração|Adicionar tabela de N por nível de risco|MANTER COM AJUSTES MENORES
F4|L1-F4-prompt-ext.md|01|P1|ALTO|Sanitização de prompt injection mencionada sem instrução de como fazer|Adicionar 3-4 linhas de guia operacional + referência a Cap 19|MANTER COM AJUSTES
F4|L1-F4-prompt-ext.md|02|P2|MÉDIO|Ausência de cobertura de prompts multimodais|Adicionar nota ao Bloco 3 sobre posição do input visual|MANTER COM AJUSTES
F4|L1-F4-prompt-ext.md|03|P2|MÉDIO|Sem instrução de manejo do Bloco 3 quando cresce além do limite prático|Conectar explicitamente a T3 do F7|MANTER COM AJUSTES
F5|L1-F5-cobertura-integracoes.md|01|P1|MÉDIO|Título não reflete conteúdo principal do framework|Renomear para F5 — Decisão de Mecanismo de Integração|REVISAR PARCIALMENTE
F5|L1-F5-cobertura-integracoes.md|02|P1|ALTO|Protocolo de uso na seção 10 — deveria ser seção 2|Reorganizar estrutura do framework|REVISAR PARCIALMENTE
F5|L1-F5-cobertura-integracoes.md|03|P2|MÉDIO|Sem orientação sobre migração de mecanismo existente|Adicionar subseção Quando Migrar de Mecanismo|REVISAR PARCIALMENTE
F5|L1-F5-cobertura-integracoes.md|04|P0|ALTO|Sobreposição de observabilidade e conformidade com F3 e F6 sem divisão de trabalho|Adicionar nota de escopo que declara fronteira com F3 e F6|REVISAR PARCIALMENTE
F6|L1-F6-gov-indelegavel.md|01|P1|ALTO|12 decisões mínimas do RACI não listadas no corpo|Adicionar as 12 decisões inline com indicação de Apêndice O|MANTER COM AJUSTES
F6|L1-F6-gov-indelegavel.md|02|P2|MÉDIO|Anti-padrão terceirização sem distinção entre accountability e execução|Reformular para distinguir terceirização legítima da ilegítima|MANTER COM AJUSTES
F6|L1-F6-gov-indelegavel.md|03|P2|MÉDIO|AI Council sem cadência-padrão generalizada no framework|Adicionar orientação de cadência por fase de maturidade|MANTER COM AJUSTES
F7|L1-F7-composto-3t.md|01|P1|ALTO|Faixas de economia típica sem fonte declarada|Adicionar nota de fonte e limitação das estimativas|MANTER COM AJUSTES
F7|L1-F7-composto-3t.md|02|P1|ALTO|Circuit breaker mencionado sem explicação de implementação|Adicionar 3-4 linhas de guia operacional|MANTER COM AJUSTES
F7|L1-F7-composto-3t.md|03|P2|MÉDIO|Sem orientação de diagnóstico pré-aplicação das alavancas|Adicionar diagnóstico de pré-requisito com estimativa para leitor sem instrumentação|MANTER COM AJUSTES
F8|L1-F8-eval-piramide.md|01|P1|ALTO|Camada adversarial não integrada à política de bloqueio em CI|Adicionar zero-tolerance adversarial à tabela de política de bloqueio|MANTER COM AJUSTES MENORES
F8|L1-F8-eval-piramide.md|02|P1|ALTO|Critério de representatividade do golden set não definido|Adicionar 4 critérios de representatividade|MANTER COM AJUSTES MENORES
F8|L1-F8-eval-piramide.md|03|P2|MÉDIO|Guia de construção de adversarial set específico de domínio ausente|Adicionar orientação de construção por domínio com exemplos setoriais|MANTER COM AJUSTES MENORES
F9|L1-F9-rota-dupla.md|01|P1|MÉDIO|Regulação classificada como número volátil junto com preço de token|Criar subcategoria número de alta meia-vida vs baixa meia-vida|MANTER COM AJUSTES
F9|L1-F9-rota-dupla.md|02|P1|ALTO|Ausência de orientação para leitor com zero padrão internalizado|Adicionar subseção ponto de partida zero|MANTER COM AJUSTES
F9|L1-F9-rota-dupla.md|03|P0|ALTO|Sobreposição estrutural com C00P sem divisão de trabalho declarada|Adicionar nota de posicionamento relativo ao C00P no início do F9|MANTER COM AJUSTES
F9|L1-F9-rota-dupla.md|04|P2|MÉDIO|F9 é o único framework sem exemplo memorável com números reais|Adicionar caso com resultado mensurável|MANTER COM AJUSTES
TRANSV|TODOS-FRAMEWORKS|01|P0|ALTO|Observabilidade em 4 frameworks sem âncora autoritativa declarada|Declarar Cap 22 como âncora; adicionar nota de escopo em cada framework|REVISAR PARCIALMENTE
TRANSV|TODOS-FRAMEWORKS|02|P1|MÉDIO|Redundância F1 Pergunta 4 e F8 sem hierarquia de eval declarada|Adicionar em F1 P4 referência explícita a F8 como sistema autoritativo|MANTER COM AJUSTES
TRANSV|TODOS-FRAMEWORKS|03|P1|MÉDIO|F9 como meta-framework cria assimetria na série de 9|Ou reposicionar como Apêndice de Método ou aprofundar com caso próprio|MANTER COM AJUSTES
```

---

# BANCA EDITORIAL ADVERSARIAL — CAPÍTULOS 01 a 05
# Livro: INTELIGÊNCIA AUMENTADA
# Data: 2026-06-16
# Banca: Editor-Chefe de Aquisição + Editor de Desenvolvimento + Especialista em IA/Fact-checking + Leitora Joana

---

# C01 — L1-C01-o-que-e-ia.md

## RESUMO EXECUTIVO
Nota: 7,5/10
Veredito: B

## O QUE FUNCIONA
- A analogia do mecânico veterano vs. aprendiz (seção 1.2) é genuinamente memorável e encapsula a distinção simbólico/conexionista com precisão rara. Não existe em dezenas de outros livros dessa forma.
- A linha do tempo (1.4) é uma das mais completas e didaticamente equilibradas em livros de divulgação em português. Tem rigor histórico sem ser árida.
- O exemplo da empresa de seguros (1.7) cumpre exatamente o que a tese central promete: vocabulário preciso como vantagem competitiva. É o único bloco que prova, com cenário concreto, o valor executivo do capítulo.
- O alerta sobre hype (1.4.3) tem potencial de frase-ainda-citável-em-5-anos.
- A tabela final "Antes (2020–2024) / Agora (em diante)" (1.4.10) é direta e citável.

## O QUE NÃO FUNCIONA
- O capítulo tem 326 linhas para fundamentos introdutórios. A relação sinal/ruído sofre especialmente nas seções 1.9 a 1.15 (resumo + checklist + perguntas + exercícios + projeto + referências + autoavaliação). Sete seções de apparatus pedagógico para um único capítulo diluem o impacto.
- A seção 1.4.10 "Platô da Fronteira" é empiricamente frágil: é observação de mercado 2025–2026, não fato estabelecido, e pode envelhecer mal se modelos descolarem novamente em diferencial bruto em 12 meses.
- A citação da epígrafe é atribuída a Dijkstra de forma modificada sem indicar modificação exata, o que é tecnicamente desonesto para um livro que vende autoridade intelectual.
- Seção 1.3, Camada 2: "IA Generativa" classificada como "terceira grande família" paralela a Machine Learning e IA Simbólica é taxonomia imprecisa — IA Generativa é subconjunto do ML/Deep Learning, não uma família autônoma ao mesmo nível.
- Seção 1.4.2: afirma que o livro "Perceptrons" foi "lido pela comunidade como sentença de morte para redes neurais" — é uma narrativa simplificada e em parte revisada pela historiografia técnica recente; o paper de Minsky e Papert teve efeito real, mas outros fatores contribuíram igualmente para o corte de financiamento.
- Seção 1.4.7: "Em 2019, GPT-2... a OpenAI inicialmente recusou publicá-lo 'por medo de uso malicioso'" — o GPT-2 foi publicado de forma faseada, não recusado; o framing cria impressão exagerada.
- Seção 1.4.8: "Em março de 2023, a Anthropic... lançou publicamente o Claude, sendo o primeiro modelo competitivo a abordar segurança via Constitutional AI" — Claude 1 foi lançado em março de 2023, mas Constitutional AI foi publicada como técnica pela Anthropic em dezembro de 2022 (paper Bai et al.); a frase pode induzir o leitor a pensar que Constitutional AI foi introduzida com o lançamento do Claude, o que é incorreto e pode ser verificado.
- A seção sobre AGI (1.6) atribui a Sam Altman e Dario Amodei a posição "antes de 2030": Dario Amodei publicamente indicou acreditar em AGI em poucos anos, mas atribuir datas precisas a pessoas reais com base em declarações voláteis é fonte de descrédito quando as datas ficam erradas.

## ACHADOS

### ACHADO 01
Categoria: P0
Problema: Taxonomia incorreta — IA Generativa como "terceira grande família" paralela ao ML
Por que é um problema: IA Generativa é uma aplicação/subconjunto de Deep Learning, não uma categoria histórica de mesmo nível que "IA Simbólica" e "Machine Learning". A classificação está conceitualmente errada e ensina ao leitor uma estrutura que qualquer especialista vai corrigir, minando a autoridade do autor.
Impacto no leitor: Joana vai à reunião com esse modelo mental e um CTO corrige publicamente. Perda de credibilidade imediata.
Correção exata: Reformular Camada 2 para apresentar IA Generativa como especialização dentro do Deep Learning, não como família histórica paralela. O diagrama 1.2 (Camadas da IA) possivelmente já faz isso corretamente — o texto precisa ser consistente com o diagrama.
Texto sugerido: "A IA Generativa não é uma terceira família histórica independente, mas uma aplicação especialmente poderosa do Deep Learning: sistemas que, ao invés de apenas classificar ou prever, geram conteúdo novo — texto, imagem, código, áudio. É uma especialização dentro da segunda família, e a mais visível hoje."
ROI: ALTO

### ACHADO 02
Categoria: P0
Problema: Epígrafe atribuída a Dijkstra sem indicar adaptação
Por que é um problema: A frase é marcada como "adaptado de Edsger Dijkstra" mas Dijkstra nunca disse isso nessa forma. Uma busca rápida mostra que a frase original de Dijkstra frequentemente citada é outra. Citar como "adaptado de" sem indicar o original é forma de autoridade emprestada que especialistas identificam imediatamente.
Impacto no leitor: Leitor técnico verifica a fonte e perde confiança no rigor do livro já na página 1.
Correção exata: Ou localizar a citação original e indicar o trecho exato adaptado, ou substituir por epígrafe sem necessidade de atribuição a Dijkstra, ou remover.
Texto sugerido: n/a (depende de verificação da fonte original)
ROI: ALTO

### ACHADO 03
Categoria: P0
Problema: Constitutional AI apresentada como inovação introduzida com o lançamento público do Claude (março 2023)
Por que é um problema: A técnica Constitutional AI foi publicada pela Anthropic em dezembro de 2022 (Bai et al., arxiv:2212.08073). O Claude foi o primeiro modelo comercial a usar essa abordagem, mas a frase como escrita implica que a técnica nasceu com o produto, o que é factualmente incorreto.
Impacto no leitor: Qualquer leitor que leia o paper ou acompanhe a Anthropic detecta o erro e desconfia do rigor histórico geral do capítulo.
Correção exata: "Em março de 2023, a Anthropic lançou publicamente o Claude, primeiro modelo comercial competitivo construído sobre Constitutional AI — abordagem de segurança publicada pela empresa em dezembro de 2022 e tratada em profundidade no Capítulo 23."
Texto sugerido: Ver acima.
ROI: ALTO

### ACHADO 04
Categoria: P1
Problema: GPT-2 "recusado por medo de uso malicioso" — framing impreciso
Por que é um problema: A OpenAI publicou o GPT-2 de forma faseada (staged release) entre fevereiro e novembro de 2019, nunca "recusou publicar". O framing "recusou" é dramatização que circula em cobertura popular mas é tecnicamente incorreto; o modelo completo foi eventualmente publicado.
Impacto no leitor: Leitor que buscar confirmar encontrará a história diferente; perde confiança no rigor histórico.
Correção exata: "Em 2019, GPT-2 com 1,5 bilhão de parâmetros, com a OpenAI adotando publicação faseada por preocupações com uso malicioso — a primeira vez que um laboratório de IA adiou deliberadamente a publicação completa de um modelo."
Texto sugerido: Ver acima.
ROI: MÉDIO

### ACHADO 05
Categoria: P1
Problema: Datas atribuídas a pessoas reais para AGI ("antes de 2030")
Por que é um problema: Atribuir previsão de "antes de 2030" a Sam Altman e Dario Amodei com base em declarações públicas voláteis é risco editorial. Essas posições mudam; a data ficará errada ou parecerá errada; a atribuição nominal cria possibilidade de controvérsia.
Impacto no leitor: Em 2028, quando o leitor reler, a afirmação pode estar flagrantemente errada, ou os próprios personagens terão mudado de posição.
Correção exata: Remover nomes e datas específicos. "Otimistas como os líderes dos principais laboratórios frontier acreditam em prazo de menos de uma década; céticos como Yann LeCun e críticos como Gary Marcus defendem prazos muito maiores ou irrealismo conceitual do objetivo."
Texto sugerido: Ver acima.
ROI: MÉDIO

### ACHADO 06
Categoria: P1
Problema: Seção 1.4.10 "Platô da Fronteira" apresentada como fato estabelecido, não como observação conjuntural
Por que é um problema: O "platô" é narrativa de 2025–2026 que pode se desfazer com um único modelo disruptivo. Apresentá-la como tese central do contexto competitivo sem marcação de incerteza é frágil editorialmente e contraria a tese "modelos passam, método fica".
Impacto no leitor: Se um modelo nova geração descolara em 2027, a seção parecerá ingênua e datará o livro.
Correção exata: Adicionar qualificador explícito: "Em meados de 2026, observa-se uma convergência de capacidade bruta entre os modelos frontier — fenômeno que analistas chamam de 'platô'. Esse platô pode ser temporário, mas o que ele revela sobre onde o valor migrou é mais durável do que a observação em si."
Texto sugerido: Ver acima.
ROI: MÉDIO

### ACHADO 07
Categoria: P1
Problema: Seções 1.9 a 1.15 (apparatus pedagógico) são pesadas e repetitivas para um capítulo de fundamentos
Por que é um problema: Sete seções de fechamento (resumo, checklist, perguntas, exercícios, projeto, referências, autoavaliação) diluem o impacto de um capítulo que já tem boa densidade. O leitor executivo perde o fio antes do fim.
Impacto no leitor: Joana para de ler antes da seção 1.7 (a mais valiosa) porque o capítulo parece nunca terminar.
Correção exata: Consolidar em no máximo três seções de fechamento: Resumo Executivo (tabela), Exercícios (os dois mais impactantes apenas), e Conexões. O resto vai para um apêndice de workbook ou material digital.
Texto sugerido: n/a
ROI: MÉDIO

### ACHADO 08
Categoria: P2
Problema: Narrativa do Livro "Perceptrons" simplificada — atribui a Minsky/Papert papel maior do que evidências atuais suportam
Por que é um problema: A historiografia técnica recente (cf. Olazaran 1996, revisões de LeCun) aponta que o impacto do livro foi mais nuançado; o corte de financiamento teve causas múltiplas. A narrativa dramática é comum mas é simplificação.
Impacto no leitor: Especialista em história da IA (não a Joana) identifica como narrativa popular não verificada.
Correção exata: Adicionar qualificador: "O livro contribuiu significativamente para o clima de ceticismo — juntamente com cortes orçamentários que tinham causas independentes — e é hoje lembrado como símbolo do período."
Texto sugerido: n/a
ROI: BAIXO

### ACHADO 09
Categoria: P2
Problema: Referência ao "XCON da DEC que economizou US$ 40 milhões por ano" sem fonte citada
Por que é um problema: O número circula em literatura de IA mas a fonte primária não é citada. Em um livro que vende autoridade, afirmações com números precisos precisam de rastreabilidade.
Impacto no leitor: Leitor que cite esse número em reunião e seja desafiado não tem fonte para consultar.
Correção exata: Adicionar referência ao paper McDermott/DEC ou ao livro de Russell & Norvig que cita esse caso.
Texto sugerido: n/a
ROI: BAIXO

## TESTE DA JOANA
Entenderia: SIM (parcialmente)
O que ela entenderia: A analogia dos mecânicos, o exemplo da empresa de seguros, a diferença chatbot/agente, o "platô da fronteira" (bem explicado).
O que ela NÃO entenderia: A seção 1.4 é longa demais — ela começa a perder energia em torno de 1.4.5. A distinção IA Simbólica/Conexionista fica técnica rápido demais nas subseções históricas. O termo "pré-limiar" (insight da AlexNet) é jargão não definido.
Como corrigir: Resumir as subseções 1.4.1 a 1.4.5 em metade do texto atual, mantendo apenas o que o insight sobre invernos exige. Definir "efeito limiar" antes de usá-lo.

## TESTE DE DURABILIDADE
Classificação: MÉDIA
2 anos: A maioria resiste. O "platô" e as datas de AGI são os vulneráveis.
5 anos: Seção 1.4.9 (Era dos Agentes) e 1.4.10 (Platô) podem ser as partes mais datadas do livro inteiro.
10 anos: As fundações históricas (1.4.1 a 1.4.6), a taxonomia (com a correção do P0), e a lição sobre invernos da IA são genuinamente duráveis. A tese sobre "platô competitivo" é o maior risco de envelhecimento.
Justificativa: Nomes de modelos (Claude, GPT-4o, Gemini), datas de lançamento, previsões de AGI, e descrição da "Era dos Agentes" envelhecem. A seção 1.7 (exemplo executivo) é durável porque o problema que resolve (vocabulário) é estrutural.

## TESTE DE DIFERENCIAÇÃO
Classificação: DIFERENCIADO
Justificativa: A analogia dos mecânicos e o exemplo da empresa de seguros são originais. A linha do tempo é mais completa que a média de livros executivos sobre IA. A distinção chatbot/agente como filosófica (não só técnica) é ângulo genuíno. Abaixo do nível de Propriedade Intelectual porque a taxonomia tem erro (P0 #01) e a linha do tempo, sem ele, seria commodity.

## TESTE DE MEMORIZAÇÃO
Ideia principal clara? SIM
Qual é a ideia principal: Vocabulário preciso sobre IA é vantagem competitiva executiva — quem distingue ML, LLM e agente toma decisões melhores em reuniões onde os outros ficam em debate circular.
Justificativa: A ideia está presente, especialmente na seção 1.7, mas o capítulo como um todo não a enuncia como tese central no início — o leitor chega à ideia principal apenas depois de 60% do conteúdo.

## TESTE DE TRANSFORMAÇÃO
Ao terminar, o leitor consegue fazer o que antes não conseguia:
- Distinguir ML, Deep Learning, IA Generativa e LLMs em conversa executiva
- Usar a história dos invernos da IA como ferramenta de calibração de expectativas
- Separar conversas corporativas sobre IA em subconversas menores com decisões mais claras
- (parcialmente) Posicionar seu contexto organizacional no mapa de camadas da IA

## NOTA FINAL (0-10 cada eixo)
Estrutura: 6 | Pedagogia: 7 | Clareza: 7 | Autoridade: 6 | Durabilidade: 6 | Diferenciação: 7 | Memorização: 7 | Transformação: 8
**Nota Geral: 7,5**

## DECISÃO EDITORIAL
MANTER COM AJUSTES — corrigir P0s #01, #02, #03 antes de qualquer revisão final; consolidar apparatus pedagógico; adicionar qualificadores de incerteza em seções datadas.

---

# C02 — L1-C02-como-modelos-funcionam.md

## RESUMO EXECUTIVO
Nota: 8/10
Veredito: A

## O QUE FUNCIONA
- A distinção treinamento/inferência (2.3.1 e 2.3.2) é a melhor explicação de custo assimétrico que vi em livro não-técnico em português. Clara, com consequências práticas.
- A analogia do pianista cego (2.1) funciona bem para a Joana e é memorável. Introduz o conceito de emergência sem usar o termo.
- O caso do advogado de Nova York (2.4) é o exemplo mais eficaz do livro até agora: concreto, com autópsia técnica, com lição não-óbvia ("não é bug, é design").
- A distinção "plausibilidade vs. verdade" (2.4) é a contribuição mais citável do capítulo.
- O boxe técnico opcional sobre Q/K/V (2.3.3) é excelente: rigoroso, opcional, e inclui a referência ao "Lost in the Middle" com call-forward legítimo.
- A seção 2.6 (por que parecem inteligentes) tem três camadas bem estruturadas — é um dos únicos lugares no livro onde a emergência é abordada com honestidade sobre o que ainda é debatido.

## O QUE NÃO FUNCIONA
- O estagiário hipotético (2.2) é análogo ao mecânico do C01 — dois capítulos seguidos começam com analogia de trabalhador-que-aprendeu-tudo. Cria sensação de fórmula repetida.
- Seção 2.3.2: "entre 80 e 120 dessas camadas" para modelos frontier — esse número pode estar desatualizado ou ser impreciso; GPT-4 tem arquitetura não divulgada, Claude não divulga número de camadas. A afirmação específica sem fonte é problemática.
- Seção 2.7 (Limitações) é enumeração sem ancoragem em casos: lista seis limitações em texto corrido sem um único exemplo concreto para nenhuma. Contrasta negativamente com a qualidade do exemplo do advogado na seção anterior.
- Seção 2.3.1: O custo de treinamento "entre 50 e 500 milhões de dólares" em 2026 é estimativa com range de 10x — isso é imprecisão disfarçada de precisão. O número mais recente publicamente disponível (GPT-4: estimado ~$100M, Gemini Ultra: ~$190M segundo analistas) vale ser citado com fontes.
- RLHF é introduzido na seção 2.6 sem definir a sigla no corpo do texto — só aparece no glossário da seção 2.8. Para a Joana, que está no fluxo da leitura, a sigla chega antes da definição.
- A seção 2.5 "Por Que Modelos Não Pensam" faz afirmação filosófica forte ("Isso é fato técnico, não opinião filosófica") que é em si uma posição filosófica controversa. Filosofia da mente tem debate ativo sobre isso; a afirmação como absoluta pode ser questionada por qualquer leitor que conheça o debate sobre funcionalismo.

## ACHADOS

### ACHADO 01
Categoria: P0
Problema: "80 a 120 camadas" para modelos frontier — afirmação específica sem fonte para arquiteturas não-divulgadas
Por que é um problema: Nem OpenAI nem Anthropic divulgam número exato de camadas. O número 80–120 é estimativa da comunidade, não dado verificável. Em um capítulo sobre precisão técnica, afirmar número específico sem fonte destrói a posição do autor quando questionado.
Impacto no leitor: Um CTO que vai verificar não encontra confirmação. O autor perde credibilidade técnica no momento mais crítico.
Correção exata: "modelos frontier têm dezenas dessas camadas — estimativas da comunidade sugerem entre 80 e 120 para os maiores, mas arquiteturas não são divulgadas pelos principais laboratórios"
Texto sugerido: Ver acima.
ROI: ALTO

### ACHADO 02
Categoria: P0
Problema: "fato técnico, não opinião filosófica" sobre consciência em modelos — afirmação filosófica apresentada como fato técnico
Por que é um problema: A questão de se LLMs têm "consciência", "intenções" ou "crenças" é objeto ativo de debate filosófico (funcionalismo, IIT, debates Chalmers/Dennett). Afirmar que é "fato técnico" é em si uma posição filosófica (eliminativismo), não consenso científico. O livro precisa de mais humildade epistêmica aqui.
Impacto no leitor: Qualquer leitor familiarizado com filosofia da mente vai marcar essa passagem como desonesta intelectualmente, minando a autoridade do livro.
Correção exata: "Do ponto de vista da arquitetura atual, modelos não têm os mecanismos que associamos a consciência ou intenção humana. Se isso significa que não têm nenhuma forma dessas propriedades é questão que filósofos debatem ativamente — e que este livro não resolve. O que importa pragmaticamente é: não espere do modelo o que você esperaria de um colega que genuinamente compreende."
Texto sugerido: Ver acima.
ROI: ALTO

### ACHADO 03
Categoria: P1
Problema: Duas analogias de "trabalhador que aprendeu muito" em capítulos consecutivos (mecânico C01, estagiário C02)
Por que é um problema: A fórmula fica evidente e reduz o impacto de ambas. O leitor percebe o padrão e passa a aguardar a analogia como ritual, não como iluminação.
Impacto no leitor: O efeito de estranhamento produtivo que as analogias deveriam criar é atenuado pela repetição do formato.
Correção exata: Substituir o estagiário (2.2) por uma analogia genuinamente diferente no tipo (física, natural, artefato) em vez de mais um profissional-que-leu-tudo. Alternativamente, mover a analogia do mecânico para o C02 e criar nova abertura para o C01.
Texto sugerido: n/a (requer criação)
ROI: MÉDIO

### ACHADO 04
Categoria: P1
Problema: Seção 2.7 (Limitações) lista seis limitações sem exemplos concretos
Por que é um problema: Contrasta diretamente com a qualidade da seção 2.4 (caso do advogado). Uma lista seca de limitações sem ancoragem deixa o leitor sem memória episódica — ele não vai lembrar das limitações porque não tem história para ancorar cada uma.
Impacto no leitor: A Joana vai saber que "alucinação existe" (seção 2.4 ficou) mas não vai lembrar das outras cinco limitações.
Correção exata: Para cada limitação, uma frase de ancoragem concreta. "A janela de contexto finita: um sistema que parece perfeito em demo, com documento de 5 páginas, quebra em produção quando o documento tem 200."
Texto sugerido: n/a (requer expansão por limitação)
ROI: MÉDIO

### ACHADO 05
Categoria: P1
Problema: RLHF usada como sigla antes de ser definida no corpo do texto (aparece primeiro em 2.6, definida só em 2.8)
Por que é um problema: Para a Joana, que lê linearmente, a sigla aparece três vezes antes de ter o significado completo. Quebra o fluxo.
Impacto no leitor: Pequena mas sistemática frustração de leitura.
Correção exata: Na primeira aparição (2.6), adicionar: "um processo chamado RLHF (Reinforcement Learning from Human Feedback, ou Aprendizado por Reforço a partir de Feedback Humano)".
Texto sugerido: Ver acima.
ROI: BAIXO

### ACHADO 06
Categoria: P2
Problema: Custo de treino "50 a 500 milhões" — range de 10x sem fonte
Por que é um problema: Parece dado preciso mas é estimativa com range enorme. Sem fonte, não é defensável em discussão profissional.
Impacto no leitor: O executivo que citar esse número em reunião pode ser desafiado facilmente.
Correção exata: Citar fonte específica (ex: estimativas de Dylan Patel/SemiAnalysis ou relatórios públicos) e indicar que são estimativas externas, não dados divulgados.
Texto sugerido: n/a
ROI: BAIXO

## TESTE DA JOANA
Entenderia: SIM
O que ela entenderia: A distinção plausibilidade/verdade (ficará na cabeça dela), o caso do advogado, a diferença treinamento/inferência em termos de custo, por que modelos não "pensam" no sentido humano.
O que ela NÃO entenderia: O boxe técnico Q/K/V (mas é opcional, resolvido), a frase "função matemática com bilhões de parâmetros" sem analogia de apoio para o que são parâmetros, RLHF antes de ser definida.
Como corrigir: Adicionar uma frase de definição informal para "parâmetros/pesos" na primeira vez que aparece: "pesos são os números que o modelo aprendeu — como os reflexos que o pianista internalizou sem conseguir descrevê-los".

## TESTE DE DURABILIDADE
Classificação: ALTA
2 anos: Quase tudo resiste. A mecânica de treinamento/inferência/atenção não muda com lançamentos de modelos.
5 anos: O número de camadas e o custo de treino envelhecem; o princípio dura.
10 anos: A distinção plausibilidade/verdade e a explicação de alucinação como design feature são contribuições duráveis. O capítulo tem boa durabilidade estrutural.
Justificativa: O autor acertou ao focar em mecanismo, não em produto. As únicas vulnerabilidades são os números específicos (custo, camadas) e a caracterização do RLHF como prática dominante (que pode mudar com outras técnicas de alinhamento).

## TESTE DE DIFERENCIAÇÃO
Classificação: DIFERENCIADO
Justificativa: A distinção "plausibilidade vs. verdade" e a autópsia do caso do advogado estão perto de Propriedade Intelectual. O boxe Q/K/V é raro em livros executivos. A fórmula da analogia (trabalhador-que-leu-tudo) precisa de variação para não virar commodity de formato.

## TESTE DE MEMORIZAÇÃO
Ideia principal clara? SIM
Qual é a ideia principal: LLMs produzem texto plausível, não verdadeiro — e saber isso muda como você arquiteta soluções e valida saídas.
Justificativa: A frase "Modelos de linguagem produzem texto plausível, não texto verdadeiro" é a frase mais citável dos cinco capítulos revisados.

## TESTE DE TRANSFORMAÇÃO
Ao terminar, o leitor consegue fazer o que antes não conseguia:
- Explicar alucinação sem dizer "o modelo mentiu" (distinção plausível/verdadeiro)
- Identificar tarefas que precisam de validação externa vs. tarefas que admitem confiança direta
- Ter uma conversa técnica sobre treinamento vs. inferência com desenvolvedores
- Reconhecer RLHF/Constitutional AI como camada de alinhamento, não como o modelo em si

## NOTA FINAL (0-10 cada eixo)
Estrutura: 8 | Pedagogia: 8 | Clareza: 8 | Autoridade: 7 | Durabilidade: 9 | Diferenciação: 8 | Memorização: 9 | Transformação: 8
**Nota Geral: 8**

## DECISÃO EDITORIAL
MANTER COM AJUSTES — corrigir P0s #01 e #02; variar formato de analogia em 2.2; ancorar limitações em exemplos.

---

# C03 — L1-C03-tokens.md

## RESUMO EXECUTIVO
Nota: 8/10
Veredito: A

## O QUE FUNCIONA
- É o capítulo mais diretamente útil dos cinco para o leitor executivo. A promessa é cumprida: quem lê, sabe gerenciar custo.
- O caso da startup brasileira de educação (3.4) é concreto, verificável em estrutura, e as três lições têm ROI imediato.
- A seção 3.5 (estratégias em ordem de impacto) é lista diretamente acionável — rara em livros de IA.
- A seção 3.6 (erros comuns) é diagnóstica e honesta — não tenta impressionar, tenta prevenir.
- A comparação PT vs. EN em tokens (3.3.2) é dado relevante para mercado brasileiro e raramente aparece em materiais de língua inglesa.
- O capítulo tem a melhor proporção sinal/ruído dos cinco.

## O QUE NÃO FUNCIONA
- O número "40% a 60% mais tokens em português" (3.3.2) é apresentado com precisão específica mas sem fonte verificável. Afirmar "diferença consistente com a comparação direta em tokenizers públicos" não é citação.
- O cenário da startup (3.4) é explicitamente "cenário ilustrativo" — mas a terceira lição (prompt caching) cita uma solução que a startup teria adotado. Se é ilustrativo, a solução deve ser hipotética também; se é real, deve ser citado.
- "Output costuma ser mais caro que input, por um fator que varia entre 3x e 5x" (3.3.3): a variação depende do modelo; alguns modelos têm razão diferente. Afirmar como range universal pode confundir.
- A epígrafe "Você pensa em palavras. O modelo pensa em tokens" é boa. A conclusão "Toda vez que você esquece essa diferença, você gasta dinheiro à toa" é batida e levemente condescendente — o leitor é executivo, não um aluno sendo repreendido.
- Tiktoken é citado como "ferramenta oficial da OpenAI" (3.3.3); correto, mas como ferramenta de contagem ela funciona para modelos OpenAI, não para Claude ou Gemini (que têm tokenizers diferentes). A generalização "e equivalentes para outros modelos" é vaga demais para ser útil.

## ACHADOS

### ACHADO 01
Categoria: P0
Problema: "40% a 60% mais tokens em português" sem fonte primária verificável
Por que é um problema: É o dado mais citável do capítulo, vai aparecer em apresentações de executivos. Se a fonte não for verificável, qualquer pessoa que tentar reproduzir pode obter números diferentes dependendo do tokenizer, do texto, e da versão.
Impacto no leitor: O executivo usa o dado em uma proposta de orçamento e é desafiado pelo CTO.
Correção exata: Citar tokenizer específico, versão, e metodologia usada: "Em comparação direta usando Tiktoken (GPT-4o) sobre pares de textos paralelos PT/EN de 1.000 palavras, textos em português geraram entre 40% e 60% mais tokens. O número varia com tokenizer e conteúdo; a direção é consistente."
Texto sugerido: Ver acima.
ROI: ALTO

### ACHADO 02
Categoria: P1
Problema: Tiktoken apresentado como ferramenta de contagem genérica sem mencionar limitação a modelos OpenAI
Por que é um problema: Leitores que usam Claude ou Gemini vão tentar usar Tiktoken e obter contagens incorretas, gerando desconfiança na ferramenta ou no capítulo.
Impacto no leitor: Frustração prática; a recomendação falha para metade da audiência que não usa só OpenAI.
Correção exata: "Para modelos OpenAI, existe o Tiktoken oficial. Para Claude, a Anthropic oferece endpoint de contagem de tokens na API. Para Gemini, o Google oferece endpoint equivalente. Cada provedor tem seu próprio tokenizer — nunca use o contador de um provedor para estimar custo de outro."
Texto sugerido: Ver acima.
ROI: ALTO

### ACHADO 03
Categoria: P1
Problema: O cenário da startup é "ilustrativo" mas usa linguagem de caso real ("a startup sobreviveu, escalou, e hoje é caso de sucesso")
Por que é um problema: Ou é um caso real (e deve ser citado ou anonimizado com nota) ou é composto (e a linguagem emocional "sobreviveu, escalou" é manipulativa para um caso inventado). A ambiguidade corrói credibilidade.
Impacto no leitor: Leitor que tentar citar o caso em apresentação e for perguntado "qual startup?" não tem resposta.
Correção exata: Ou indicar claramente que é caso composto de múltiplos casos reais e remover o desfecho emocional ("sobreviveu"), ou citar o caso real anonimamente com nota.
Texto sugerido: Adicionar ao final do bloco: "Este cenário é composto a partir de três casos reais acompanhados pelo autor entre 2023 e 2025. Detalhes foram alterados para preservar confidencialidade."
ROI: MÉDIO

### ACHADO 04
Categoria: P1
Problema: "Output costuma ser mais caro que input, por um fator de 3x a 5x" — generalização que não reflete a variedade de modelos
Por que é um problema: Anthropic Claude Sonnet 4 (junho 2026) tem preços de input $3/MTok e output $15/MTok (5x). GPT-4o tem razão diferente. Modelos como Gemini Flash têm estruturas distintas. A afirmação como regra universal vai envelhecer com cada mudança de pricing.
Impacto no leitor: Leitor que for verificar vai encontrar razões diferentes e perder confiança no número.
Correção exata: "Na maioria dos modelos frontier disponíveis em 2026, output custa entre 3x e 5x mais que input — mas esse múltiplo varia por modelo e muda com atualizações de preço. Verifique a tabela de pricing do seu provedor antes de modelar orçamento."
Texto sugerido: Ver acima.
ROI: MÉDIO

### ACHADO 05
Categoria: P2
Problema: Epígrafe levemente condescendente no tom
Por que é um problema: "Toda vez que você esquece essa diferença, você gasta dinheiro à toa" tem tom de professor repreendendo aluno, não de par desafiando executivo.
Impacto no leitor: Pequena, mas o tom certo abre o leitor; tom levemente errado fecha.
Correção exata: "Você pensa em palavras. O modelo pensa em tokens. Quem entende essa diferença constrói sistemas que escalam; quem ignora paga para descobrir."
Texto sugerido: Ver acima.
ROI: BAIXO

## TESTE DA JOANA
Entenderia: SIM (o melhor resultado dos cinco capítulos)
O que ela entenderia: O problema do Lego (analogia clara), o caso da startup (aplicável ao negócio dela), a ordem de estratégias de economia (acionável), os cinco erros comuns (reconhecerá pelo menos três na sua operação).
O que ela NÃO entenderia: BPE/SentencePiece/Tiktoken na seção 3.3.1 — são nomes que ela não vai lembrar e não precisa lembrar. Essa seção pode ser condensada em uma frase.
Como corrigir: Transformar 3.3.1 em um parágrafo: "O algoritmo por trás é chamado BPE (Byte Pair Encoding). O que importa para você não é o nome, é o resultado: palavras comuns viram um token, palavras raras viram vários, e o tokenizer do modelo determina qual é qual."

## TESTE DE DURABILIDADE
Classificação: MÉDIA
2 anos: O princípio dura; os preços e o ratio 3x-5x podem mudar.
5 anos: BPE pode ser substituído por abordagens melhores; o princípio de custo assimétrico input/output pode mudar com modelos diferentes.
10 anos: O conceito de token como unidade de custo pode ser abstraído pelo mercado (como MB virou irrelevante para usuário de celular). Mas o capítulo existirá no horizonte de relevância de 5 anos com segurança.
Justificativa: Preços, ratios e nomes de ferramentas envelhecem. O princípio "output custa mais, encurte saída antes de entrada" é durável. A seção de língua (PT vs. EN) é durável enquanto tokenizers seguirem sendo treinados em corpora dominados pelo inglês.

## TESTE DE DIFERENCIAÇÃO
Classificação: DIFERENCIADO
Justificativa: A seção PT vs. EN é rara e valiosa para mercado brasileiro. A ordem de estratégias por impacto é melhor do que a maioria dos materiais de otimização de custo disponíveis. O caso da startup é memorável. Falta a fonte do dado central para chegar a Propriedade Intelectual.

## TESTE DE MEMORIZAÇÃO
Ideia principal clara? SIM
Qual é a ideia principal: Token é a unidade real de custo em IA — e quem a ignora paga para descobrir isso na fatura.
Justificativa: Clara desde a epígrafe, reforçada no caso da startup, ancorada nas estratégias. Este é o capítulo de memorização mais eficaz dos cinco.

## TESTE DE TRANSFORMAÇÃO
Ao terminar, o leitor consegue fazer o que antes não conseguia:
- Estimar custo de operação de IA em tokens antes de escalar
- Identificar onde estão os maiores gastos de token em uma aplicação real
- Priorizar prompt caching antes de qualquer outra otimização
- Instruir a equipe a encurtar output antes de encurtar input
- Usar o contador de tokens antes de modelar orçamento

## NOTA FINAL (0-10 cada eixo)
Estrutura: 8 | Pedagogia: 9 | Clareza: 9 | Autoridade: 7 | Durabilidade: 7 | Diferenciação: 8 | Memorização: 9 | Transformação: 9
**Nota Geral: 8**

## DECISÃO EDITORIAL
MANTER COM AJUSTES — corrigir P0 #01 (fonte do dado PT/EN) e P1 #02 (Tiktoken para outros modelos); qualificar preços/ratios; esclarecer natureza do cenário.

---

# C04 — L1-C04-janela-de-contexto.md

## RESUMO EXECUTIVO
Nota: 8,5/10
Veredito: A

## O QUE FUNCIONA
- A analogia da mesa do escritório (4.2) é a analogia mais eficaz dos cinco capítulos — concreta, extensível, e resolve de uma vez a intuição sobre contexto, RAG e "esquecer o que combinamos".
- O fenômeno Lost in the Middle (4.3.3) é explicado com precisão técnica e com implicação prática imediata. A referência ao paper original (Liu et al., 2023) é a melhor prática de fact-checking do livro inteiro.
- O caso do escritório de advocacia (4.4) é bem construído e a solução (chunking em vez de troca de modelo) é a lição mais valiosa do capítulo — demonstra que arquitetura bate capacidade de modelo.
- A seção 4.5 (Long Context vs. RAG) é o melhor framework de decisão dos cinco capítulos: binário, com critérios explícitos, acionável.
- A heurística das três zonas (4.3.4) é memorável e diretamente aplicável.

## O QUE NÃO FUNCIONA
- Seção 4.3.1: "custo computacional da atenção cresce de forma quadrática" é simplificação que pode ser enganosa. Modelos modernos usam atenção esparsa, Flash Attention, e outras técnicas que fazem o custo crescer de forma subquadrática na prática. Afirmar quadrático como regra pode ser tecnicamente desonesto em 2026.
- Seção 4.3.1: "modelos Gemini têm linhagens que chegam a 1 a 2 milhões de tokens" — correto para Gemini 1.5 Pro/Ultra, mas a família Gemini tem janelas variadas. A generalização pode confundir.
- Seção 4.3.1: "Modelos GPT modernos variam entre 128 mil e 400 mil" — GPT-4o (2024) tem 128k; afirmar 400k sem identificar qual modelo específico é vago.
- A seção 4.3.3 afirma que "pesquisadores de Stanford" identificaram Lost in the Middle. O paper Liu et al. 2023 teve pesquisadores de Stanford e Berkeley (co-autores de Berkeley incluem Percy Liang). Atribuir exclusivamente a Stanford é impreciso.
- Seção 4.6 introduz "Context Engineering" como disciplina emergente sem mencionar que o termo foi popularizado principalmente por Andrej Karpathy em 2025. Omitir a fonte de um termo recente é problemático em livro que vende autoridade.
- "taxa de recuperação cai significativamente, podendo chegar a menos de 50% em algumas configurações" (4.3.3) — o paper original documenta quedas variadas; "menos de 50%" em configurações extremas é plausível mas deve ser qualificado melhor (qual configuração, qual modelo).

## ACHADOS

### ACHADO 01
Categoria: P0
Problema: "custo quadrático da atenção" como regra geral em 2026 — tecnicamente impreciso dado estado da arte
Por que é um problema: Flash Attention (Dao et al., 2022), atenção esparsa, e outras otimizações reduzem o crescimento de custo na prática. Afirmar quadrático sem qualificação é tecnicamente desatualizado para qualquer leitor que conheça a literatura de eficiência de Transformers.
Impacto no leitor: Um engenheiro de ML que lê o capítulo vai marcar essa afirmação como incorreta, minando a autoridade do capítulo todo.
Correção exata: "O custo computacional da atenção padrão cresce de forma quadrática em relação ao contexto — um problema que levou a toda uma área de pesquisa em eficiência. Técnicas modernas como Flash Attention reduzem esse crescimento na prática, mas o princípio de que contexto longo é mais caro do que contexto curto permanece verdadeiro e relevante para decisões de orçamento."
Texto sugerido: Ver acima.
ROI: ALTO

### ACHADO 02
Categoria: P1
Problema: Atribuição de Lost in the Middle exclusivamente a "pesquisadores de Stanford"
Por que é um problema: O paper Liu et al. (2023) inclui co-autores de Stanford e Berkeley. Atribuir exclusivamente a Stanford é verificavelmente impreciso.
Impacto no leitor: Qualquer leitor que verifique a afiliação dos autores encontra o erro; pequeno mas sintomático de pesquisa de fonte incompleta.
Correção exata: "um fenômeno descoberto e batizado por pesquisadores de Stanford e Berkeley em 2023"
Texto sugerido: Ver acima.
ROI: BAIXO

### ACHADO 03
Categoria: P1
Problema: "Context Engineering" como disciplina sem mencionar a popularização por Andrej Karpathy
Por que é um problema: O termo foi popularizado no ecossistema em 2025 principalmente por Karpathy. Usar o termo como se fosse coinage do autor (ou sem citar origem) é omissão relevante em livro que promete autoridade.
Impacto no leitor: Leitor que pesquisar o termo encontrará a associação com Karpathy e sentirá que a atribuição foi omitida deliberadamente.
Correção exata: Adicionar nota: "O termo 'Context Engineering' foi popularizado em 2025, notavelmente por Andrej Karpathy, para descrever a evolução da engenharia de prompt para o design consciente do conteúdo do contexto."
Texto sugerido: Ver acima.
ROI: MÉDIO

### ACHADO 04
Categoria: P1
Problema: "menos de 50% em algumas configurações" para Lost in the Middle sem especificar configuração
Por que é um problema: O número específico sem contexto de qual modelo, qual tamanho de contexto, qual posição cria falsa impressão de precisão.
Impacto no leitor: Um leitor que rodar seus próprios experimentos pode obter números diferentes e questionar o dado.
Correção exata: Adicionar qualificador: "em configurações com janelas acima de 32k tokens e informação posicionada após o primeiro terço da janela, segundo Liu et al. 2023 — o efeito varia significativamente por modelo e continua sendo area ativa de pesquisa."
Texto sugerido: Ver acima.
ROI: MÉDIO

### ACHADO 05
Categoria: P2
Problema: Limites de janela de contexto por modelo (4.3.1) são os dados mais perecíveis do livro até aqui
Por que é um problema: Janelas de contexto aumentam a cada versão. Em 2027, os números de 2026 serão curiosidade histórica e não parâmetro de decisão.
Impacto no leitor: Em reedições ou versões digitais atualizadas, essa seção exige revisão constante.
Correção exata: Transformar a seção em princípio, não em tabela de dados: "Em 2026, modelos premium tipicamente suportam entre 200 mil e 2 milhões de tokens. Esses números crescem a cada geração — consulte a documentação do provedor para o dado atual."
Texto sugerido: Ver acima.
ROI: BAIXO

## TESTE DA JOANA
Entenderia: SIM
O que ela entenderia: A analogia da mesa (ficará), as três zonas (aplicará amanhã), Lost in the Middle no exemplo do contrato (concreta o suficiente), a decisão Long Context vs. RAG (tem critérios claros).
O que ela NÃO entenderia: "custo quadrático" — a palavra "quadrático" não comunica nada para ela; "dobrar o contexto multiplica o custo por três ou quatro" comunica muito melhor.
Como corrigir: Substituir "cresce de forma quadrática" por "dobrar o tamanho do contexto pode multiplicar o custo por três ou quatro, não por dois" em toda aparição.

## TESTE DE DURABILIDADE
Classificação: MÉDIA-ALTA
2 anos: Tudo resiste exceto os números específicos de tokens por modelo.
5 anos: Lost in the Middle, as três zonas, Long Context vs. RAG são duradores se desvinculados de números específicos.
10 anos: Se modelos resolverem o problema de Lost in the Middle (pesquisa ativa), a seção central perde relevância. Mas o princípio arquitetural (contexto é design, não depósito) é durável.
Justificativa: Risco principal são os números de janela por modelo, que são dados de catálogo que mudam trimestralmente.

## TESTE DE DIFERENCIAÇÃO
Classificação: DIFERENCIADO
Justificativa: A heurística das três zonas é memorável e original na forma como está apresentada. O framework Long Context vs. RAG é bem estruturado. A analogia da mesa é a melhor dos cinco capítulos. Propriedade Intelectual potencial se a atribuição de Context Engineering for corrigida e o dado quadrático for qualificado.

## TESTE DE MEMORIZAÇÃO
Ideia principal clara? SIM
Qual é a ideia principal: Contexto não é depósito — é palco que você deve desenhar conscientemente, com o crítico nas extremidades e o secundário no centro.
Justificativa: A epígrafe final "Contexto não é depósito, é palco" é a frase mais memorável dos cinco capítulos. Deveria estar no início, não só no fechamento.

## TESTE DE TRANSFORMAÇÃO
Ao terminar, o leitor consegue fazer o que antes não conseguia:
- Reorganizar um prompt longo colocando instruções críticas nas extremidades
- Diagnosticar falhas de sistema como problemas de posicionamento, não de capacidade do modelo
- Decidir entre Long Context e RAG com critérios explícitos
- Explicar Lost in the Middle para um colega usando o caso do contrato

## NOTA FINAL (0-10 cada eixo)
Estrutura: 9 | Pedagogia: 9 | Clareza: 8 | Autoridade: 7 | Durabilidade: 7 | Diferenciação: 9 | Memorização: 9 | Transformação: 9
**Nota Geral: 8,5**

## DECISÃO EDITORIAL
MANTER COM AJUSTES — corrigir P0 sobre custo quadrático; atribuir Context Engineering a Karpathy; qualificar Lost in the Middle com configuração específica; mover epígrafe final para o início do capítulo.

---

# C05 — L1-C05-embeddings.md

## RESUMO EXECUTIVO
Nota: 7/10
Veredito: B

## O QUE FUNCIONA
- A analogia do mapa das ideias (5.2) é clara e extensível — Joana vai usar essa linguagem daqui para frente.
- A explicação de similaridade do cosseno vs. distância euclidiana vs. produto interno (5.3.3) é correta, concisa, e nível certo de profundidade para executivo.
- A distinção modelos de embedding vs. LLMs (5.3.4) é rara em materiais executivos e resolve uma confusão que aparece constantemente em projetos.
- O caso da operadora de telecomunicações (5.4) é concreto e o "vocabulário diferente para o mesmo problema" é a melhor explicação de busca semântica vs. palavra-chave disponível para não-técnicos.
- A seção de limitações (5.6) é honesta e completa — o ponto sobre obsolescência ao trocar de modelo é frequentemente ignorado.

## O QUE NÃO FUNCIONA
- O capítulo é o mais fraco em originalidade dos cinco. A explicação de embeddings é correta mas existe em dezenas de materiais equivalentes (Jay Alammar, Simon Willison, materiais Anthropic). A analogia do mapa é boa mas não é nova.
- A citação a Firth ("você conhece uma palavra pela companhia que ela mantém") está no corpo do texto como "formulada por Firth na década de 1950" mas o contexto original de Firth é diferente — a frase exata que circula em NLP ("You shall know a word by the company it keeps") é atribuição popular que simplifica o trabalho original de Firth (1957, "Papers in Linguistics"). Não é erro grave, mas merece nota de rodapé.
- A seção 5.3.1 lista "text-embedding-3 da OpenAI ou voyage-3 da Voyage AI" como exemplos — esses nomes de modelos envelhecem rapidamente. A voyage-3 é nome específico de versão que pode já ter sido substituído.
- O caso da operadora de telecomunicações (5.4) usa "taxa de resolução de problemas em primeira chamada subiu mais de 30%" — número específico sem fonte. Se é cenário ilustrativo, o número precisa ser qualificado.
- A frase "A barreira passou a ser conceitual" (5.4) é assertiva mas não verificável. Há barreiras técnicas reais em implementação de RAG que a frase subestima.
- Seção 5.5 lista seis aplicações de embeddings. A sexta (recomendação) menciona "sem precisar de filtragem colaborativa complexa" — isso é verdade como primeira aproximação, mas sistemas de recomendação de qualidade quase sempre combinam as duas abordagens. A afirmação pode criar expectativa incorreta.
- O capítulo tem o menor apparatus pedagógico dos cinco (menor número de exercícios), e os exercícios que existem dependem de ferramentas específicas (TensorFlow Embedding Projector, API da OpenAI ou Voyage) — se essas ferramentas mudarem, os exercícios ficam quebrados.

## ACHADOS

### ACHADO 01
Categoria: P0
Problema: "taxa de resolução em primeira chamada subiu mais de 30%" em cenário declarado como "ilustrativo"
Por que é um problema: Se o cenário é ilustrativo (composto), inventar uma métrica específica é fabricação de dado. Se é caso real, deve ser citado como tal. "Mais de 30%" é precisão que requer fonte.
Impacto no leitor: Qualquer leitor que use esse dado em proposta interna e seja desafiado está em posição indefensável.
Correção exata: Se ilustrativo: remover o número e substituir por "a melhoria em acerto foi substancial — na maioria dos casos documentados, métricas de resolução em primeira chamada melhoram entre 20% e 40%." + citar fonte genérica. Se real: identificar a empresa com nota de anonimização.
Texto sugerido: "A taxa de resolução de problemas em primeira chamada subiu significativamente — caso típico documentado na literatura de implantações similares [citar referência]."
ROI: ALTO

### ACHADO 02
Categoria: P1
Problema: Nomes específicos de modelos de embedding (text-embedding-3, voyage-3) como exemplos fixos no texto
Por que é um problema: Esses nomes de versão envelhecem em meses. O leitor que tentar seguir o exercício em 2027 vai encontrar versões diferentes ou modelos descontinuados.
Impacto no leitor: Exercícios práticos quebrados reduzem confiança no livro.
Correção exata: Substituir nomes específicos por referência a "modelos de embedding atuais da OpenAI e Voyage AI — verifique a documentação do provedor para o modelo atual recomendado".
Texto sugerido: n/a
ROI: MÉDIO

### ACHADO 03
Categoria: P1
Problema: Citação a Firth sem rigor — "você conhece uma palavra pela companhia que ela mantém" como citação exata
Por que é um problema: A frase popular atribuída a Firth é paráfrase de NLP que simplifica o trabalho original. O texto de 1957 de Firth diz algo próximo mas não idêntico. Em livro que cita papers com URLs, esse cuidado inconsistente é notável.
Impacto no leitor: Especialista em linguística ou NLP detecta a imprecisão.
Correção exata: "A intuição central vem de uma observação clássica da linguística distribucional, associada ao linguista britânico John Rupert Firth: contexto define significado. Em termos práticos para NLP, palavras que aparecem em contextos parecidos tendem a ter significados parecidos."
Texto sugerido: Ver acima.
ROI: BAIXO

### ACHADO 04
Categoria: P1
Problema: "A barreira passou a ser conceitual" — subestima barreiras técnicas reais de implementação RAG
Por que é um problema: Implementar RAG com qualidade em produção tem complexidades reais: chunking strategy, indexação incremental, re-ranking, avaliação de relevância, latência. Dizer que a barreira "passou a ser conceitual" é oversimplification que pode criar expectativa de facilidade que não existe.
Impacto no leitor: Equipes que adotarem RAG "porque é fácil" vão descobrir a complexidade em produção e culpar o livro por não ter alertado.
Correção exata: "A barreira técnica de entrada despencou — APIs de embedding e bancos vetoriais ficaram acessíveis a qualquer equipe de desenvolvimento. A barreira que permanece não é de acesso à tecnologia, mas de qualidade da implementação: chunking bem-feito, avaliação contínua de relevância, e manutenção do índice são onde a maioria dos projetos sofre."
Texto sugerido: Ver acima.
ROI: MÉDIO

### ACHADO 05
Categoria: P1
Problema: Recomendação como aplicação de embeddings "sem filtragem colaborativa complexa" — cria expectativa incorreta
Por que é um problema: Sistemas de recomendação de qualidade em produção quase sempre combinam busca semântica com sinais comportamentais e filtragem colaborativa. Apresentar embeddings como substituto direto para filtragem colaborativa é simplificação que pode levar a arquiteturas ingênuas.
Impacto no leitor: Equipe que implementar recomendação "só com embeddings" vai obter resultado pior do que esperava e atribuir ao conselho do livro.
Correção exata: "A sexta é recomendação — encontrar itens similares a outros que o usuário gostou. Embeddings funcionam bem como camada de similaridade semântica, e em cenários com poucos dados de comportamento são frequentemente a melhor primeira abordagem. Em sistemas maduros, tipicamente se combinam com sinais de comportamento (filtragem colaborativa) para melhor precisão."
Texto sugerido: Ver acima.
ROI: MÉDIO

### ACHADO 06
Categoria: P2
Problema: O capítulo é o mais fraco em originalidade — a explicação de embeddings existe em dezenas de materiais
Por que é um problema: Em relação ao padrão de comparação (Co-Intelligence, Competing in the Age of AI), este capítulo não adiciona perspectiva própria além do caso da operadora. O mapa das ideias existe; a cosseno vs. euclidiana existe; a distinção LLM vs. embedding existe.
Impacto no leitor: Leitor que já viu materiais sobre RAG não terá revelação. O capítulo serve a quem não viu nada, mas falha para o leitor semiexperiente.
Correção exata: Adicionar uma perspectiva proprietária: o autor tem visão sobre quando NÃO usar embeddings (casos em que precisão é mais importante que recall, ou onde o domínio é muito estreito para beneficiar de busca semântica). Isso diferenciaria do genérico.
Texto sugerido: n/a (requer contribuição do autor)
ROI: MÉDIO

### ACHADO 07
Categoria: P2
Problema: Exercícios dependem de ferramentas específicas que podem mudar
Por que é um problema: Exercício 1 depende do TensorFlow Embedding Projector (ferramenta mantida pelo Google, pode ser descontinuada); Exercício 2 depende de "API da OpenAI ou Voyage". Se as ferramentas mudarem, o exercício fica quebrado.
Impacto no leitor: Leitor que tentar em 2027+ pode ter experiência frustrante.
Correção exata: Reformular exercícios em termos de objetivo (visualizar clusters, comparar similaridades) com nota "usando ferramentas disponíveis no momento — veja [URL do material suplementar atualizado]".
Texto sugerido: n/a
ROI: BAIXO

## TESTE DA JOANA
Entenderia: SIM (parcialmente)
O que ela entenderia: O mapa das ideias (ficará), o caso da operadora (reconhecerá o problema na própria empresa), a distinção busca semântica vs. palavras-chave, a lista de seis aplicações.
O que ela NÃO entenderia: Seção 5.3.3 (produto interno, softmax, FAISS, Pinecone, Weaviate, Qdrant, ChromaDB em sequência) — são cinco ferramentas em dois parágrafos sem distinção prática entre elas. Para a Joana, isso é ruído técnico sem valor imediato.
Como corrigir: Simplificar 5.3.3 para: "Para medir distância entre embeddings, a métrica mais comum é a similaridade do cosseno — pense nela como o ângulo entre dois ponteiros no mapa. Quanto menor o ângulo, mais parecidos os significados." Ferramentas específicas vão para nota de rodapé ou para o capítulo de RAG.

## TESTE DE DURABILIDADE
Classificação: MÉDIA
2 anos: O princípio dura. Os nomes de modelos e ferramentas não.
5 anos: Se a arquitetura de transformers mudar significativamente, embeddings podem funcionar de forma diferente. Mas o conceito de representação vetorial de significado é durável.
10 anos: O capítulo precisa sobreviver ao seguinte teste: "se a forma como embeddings são gerados mudar completamente, o que fica?" Fica: a ideia de que significado pode ser representado como ponto em espaço e que proximidade espacial corresponde a proximidade semântica. Isso é durável.
Justificativa: Nomes de modelos (voyage-3, text-embedding-3), ferramentas (ChromaDB, Pinecone, Qdrant, FAISS, Weaviate) envelhecem trimestralmente. O conceito central é mais durável do que a apresentação atual sugere.

## TESTE DE DIFERENCIAÇÃO
Classificação: COMMODITY
Justificativa: Com exceção do caso da operadora, o capítulo não adiciona perspectiva que não exista em materiais de documentação da OpenAI, posts do Jay Alammar, ou capítulos de RAG em outros livros recentes. A distinção LLM vs. embedding é bem feita mas não é nova. Falta a voz proprietária do autor.

## TESTE DE MEMORIZAÇÃO
Ideia principal clara? SIM
Qual é a ideia principal: Embeddings transformam significado em geometria — e geometria é o que os computadores entendem.
Justificativa: A epígrafe ("Embeddings transformam significado em geometria") é a ideia central e é boa. O problema é que ela compete com a explicação técnica das dimensões (768, 1536, 3072) que obscurece o princípio elegante.

## TESTE DE TRANSFORMAÇÃO
Ao terminar, o leitor consegue fazer o que antes não conseguia:
- Explicar busca semântica vs. palavra-chave para um gestor
- Reconhecer quando a base de conhecimento da sua organização seria beneficiada por busca semântica
- Entender o papel de embeddings em um sistema RAG antes de ler o Cap 6
- (parcialmente) Avaliar trade-offs entre modelos de embedding por qualidade vs. custo de armazenamento
- O que ele NÃO consegue fazer ainda: prototipar qualquer coisa, porque os exercícios dependem de ferramentas que podem não estar disponíveis

## NOTA FINAL (0-10 cada eixo)
Estrutura: 7 | Pedagogia: 7 | Clareza: 8 | Autoridade: 6 | Durabilidade: 7 | Diferenciação: 5 | Memorização: 7 | Transformação: 7
**Nota Geral: 7**

## DECISÃO EDITORIAL
REVISAR PARCIALMENTE — corrigir P0 #01 (métrica inventada); reformular P1 sobre barreira de implementação e recomendação; adicionar perspectiva proprietária do autor para sair do commodity; simplificar seção 5.3.3 para Joana.

---

## LINHAS-TRACKER

```
CODIGO|ARQUIVO|ACHADO_ID|CATEGORIA|ROI|PROBLEMA_CURTO|CORRECAO_CURTA|DECISAO_CAP
C01|L1-C01-o-que-e-ia.md|01|P0|ALTO|IA Generativa como família paralela ao ML — taxonomia incorreta|Reformular como subconjunto do Deep Learning, consistente com diagrama 1.2|MANTER COM AJUSTES
C01|L1-C01-o-que-e-ia.md|02|P0|ALTO|Epígrafe atribuída a Dijkstra sem indicar texto original|Localizar citação original ou remover atribuição|MANTER COM AJUSTES
C01|L1-C01-o-que-e-ia.md|03|P0|ALTO|Constitutional AI apresentada como introduzida com lançamento do Claude (março 2023) — paper é de dezembro 2022|Adicionar data do paper e separar técnica do lançamento do produto|MANTER COM AJUSTES
C01|L1-C01-o-que-e-ia.md|04|P1|MÉDIO|GPT-2 "recusado" — publicação foi faseada, não recusada|Substituir por "publicação faseada deliberada"|MANTER COM AJUSTES
C01|L1-C01-o-que-e-ia.md|05|P1|MÉDIO|Datas de AGI atribuídas nominalmente a Altman e Amodei|Remover nomes e usar posição genérica de "otimistas vs. céticos"|MANTER COM AJUSTES
C01|L1-C01-o-que-e-ia.md|06|P1|MÉDIO|"Platô da Fronteira" apresentado como fato, não como observação conjuntural datada|Adicionar qualificador de incerteza e referência temporal|MANTER COM AJUSTES
C01|L1-C01-o-que-e-ia.md|07|P1|MÉDIO|Apparatus pedagógico excessivo — sete seções de fechamento|Consolidar em três seções máximas; mover resto para workbook|MANTER COM AJUSTES
C01|L1-C01-o-que-e-ia.md|08|P2|BAIXO|Narrativa Minsky/Papert simplificada|Adicionar qualificador historiográfico|MANTER COM AJUSTES
C01|L1-C01-o-que-e-ia.md|09|P2|BAIXO|XCON economizou US$40M sem fonte citada|Adicionar referência a Russell&Norvig ou paper DEC|MANTER COM AJUSTES
C02|L1-C02-como-modelos-funcionam.md|01|P0|ALTO|"80 a 120 camadas" para frontier sem fonte — arquiteturas não divulgadas|Adicionar qualificador "estimativa da comunidade, não dado divulgado"|MANTER COM AJUSTES
C02|L1-C02-como-modelos-funcionam.md|02|P0|ALTO|"fato técnico não filosófico" sobre consciência — é posição filosófica apresentada como fato|Adicionar humildade epistêmica; reconhecer debate ativo em filosofia da mente|MANTER COM AJUSTES
C02|L1-C02-como-modelos-funcionam.md|03|P1|MÉDIO|Analogia do estagiário repete padrão do mecânico (C01) — fórmula visível|Substituir por analogia de natureza diferente (física, artefato)|MANTER COM AJUSTES
C02|L1-C02-como-modelos-funcionam.md|04|P1|MÉDIO|Seção 2.7 lista seis limitações sem ancoragem em exemplos concretos|Adicionar frase de ancoragem concreta para cada limitação|MANTER COM AJUSTES
C02|L1-C02-como-modelos-funcionam.md|05|P1|BAIXO|RLHF usada antes de ser definida no corpo do texto|Definir sigla na primeira aparição (seção 2.6)|MANTER COM AJUSTES
C02|L1-C02-como-modelos-funcionam.md|06|P2|BAIXO|Custo de treino "50 a 500 milhões" sem fonte — range de 10x|Citar estimativa de fonte específica (SemiAnalysis ou similar)|MANTER COM AJUSTES
C03|L1-C03-tokens.md|01|P0|ALTO|"40-60% mais tokens em português" sem fonte verificável|Citar tokenizer específico, versão, e metodologia|MANTER COM AJUSTES
C03|L1-C03-tokens.md|02|P1|ALTO|Tiktoken apresentado como ferramenta genérica — só funciona para modelos OpenAI|Mencionar contadores específicos de cada provedor (Anthropic API, Google API)|MANTER COM AJUSTES
C03|L1-C03-tokens.md|03|P1|MÉDIO|Cenário da startup usa linguagem emocional de caso real mas é declarado ilustrativo|Adicionar nota explícita sobre composição de casos ou citar como real com anonimização|MANTER COM AJUSTES
C03|L1-C03-tokens.md|04|P1|MÉDIO|"Output 3x a 5x mais caro" como regra universal — varia por modelo|Qualificar com referência a pricing atual e variação por provedor|MANTER COM AJUSTES
C03|L1-C03-tokens.md|05|P2|BAIXO|Epígrafe levemente condescendente — "você gasta dinheiro à toa"|Reescrever com tom de desafio executivo, não de repreensão|MANTER COM AJUSTES
C04|L1-C04-janela-de-contexto.md|01|P0|ALTO|"Custo quadrático da atenção" como regra geral — Flash Attention e variantes tornam isso subquadrático na prática|Qualificar como custo da atenção padrão; mencionar otimizações modernas|MANTER COM AJUSTES
C04|L1-C04-janela-de-contexto.md|02|P1|BAIXO|Lost in the Middle atribuído exclusivamente a "Stanford" — autores incluem Berkeley|Corrigir para "Stanford e Berkeley"|MANTER COM AJUSTES
C04|L1-C04-janela-de-contexto.md|03|P1|MÉDIO|"Context Engineering" sem citar popularização por Andrej Karpathy (2025)|Adicionar nota de atribuição ao coinage|MANTER COM AJUSTES
C04|L1-C04-janela-de-contexto.md|04|P1|MÉDIO|"menos de 50% em algumas configurações" para LitM sem especificar configuração|Adicionar especificação de tamanho de janela e modelo do estudo original|MANTER COM AJUSTES
C04|L1-C04-janela-de-contexto.md|05|P2|BAIXO|Números de janela por modelo são os dados mais perecíveis do livro|Converter tabela em princípio; apontar para documentação do provedor|MANTER COM AJUSTES
C05|L1-C05-embeddings.md|01|P0|ALTO|"taxa de resolução em primeira chamada subiu mais de 30%" em cenário ilustrativo — métrica inventada|Remover número específico ou citar fonte; qualificar como estimativa de casos documentados|REVISAR PARCIALMENTE
C05|L1-C05-embeddings.md|02|P1|MÉDIO|Nomes específicos de modelos de embedding (voyage-3, text-embedding-3) vão envelhecer|Substituir por referência genérica com instrução de verificar documentação do provedor|REVISAR PARCIALMENTE
C05|L1-C05-embeddings.md|03|P1|BAIXO|Citação a Firth imprecisa — paráfrase popular de NLP, não texto original|Reformular como "observação associada a Firth" sem usar aspas de citação direta|REVISAR PARCIALMENTE
C05|L1-C05-embeddings.md|04|P1|MÉDIO|"A barreira passou a ser conceitual" subestima complexidade real de RAG em produção|Adicionar ressalva sobre complexidade de implementação de qualidade|REVISAR PARCIALMENTE
C05|L1-C05-embeddings.md|05|P1|MÉDIO|Recomendação como aplicação de embeddings sem filtragem colaborativa — expectativa incorreta|Adicionar qualificador sobre combinação com sinais comportamentais|REVISAR PARCIALMENTE
C05|L1-C05-embeddings.md|06|P2|MÉDIO|Capítulo é commodity — falta perspectiva proprietária do autor|Adicionar visão de quando NÃO usar embeddings; diferencia do genérico disponível online|REVISAR PARCIALMENTE
C05|L1-C05-embeddings.md|07|P2|BAIXO|Exercícios dependem de ferramentas específicas que podem ser descontinuadas|Reformular em termos de objetivo; apontar para material suplementar atualizado|REVISAR PARCIALMENTE
```

---

# BANCA EDITORIAL ADVERSARIAL — CAPÍTULOS 06 A 11
# Livro: INTELIGÊNCIA AUMENTADA
# Tese: "Modelos passam. Método fica."

---

# C06 — L1-C06-rag.md

## RESUMO EXECUTIVO
Nota: 8/10
Veredito: A

## O QUE FUNCIONA
- A analogia do consultor com a biblioteca é imediatamente intuitiva e rastreável ao longo de todo o capítulo — é o tipo de imagem que o leitor cita depois
- A separação estrutural entre fase de indexação e fase de consulta está pedagogicamente impecável: nomes claros, passos numerados, lógica sequencial
- A seção de chunking (6.4) é didaticamente sólida: quatro estratégias em ordem crescente de sofisticação, com trade-offs honestos em cada uma
- A seção 6.7 (limitações) é corajosa e necessária — muitos livros de IA evitam dizer quando não usar a técnica que estão ensinando
- O exemplo do help desk (6.5) é funcional como cenário de ROI; os dois efeitos colaterais inesperados (qualidade dos juniores + diagnóstico de lacunas) são o tipo de insight citável
- A tabela de resumo executivo (6.9) e o checklist (6.10) funcionam como scaffolding cognitivo real

## O QUE NÃO FUNCIONA
- O exemplo quantitativo do help desk ("68% de redução") é preciso demais para um cenário declarado como ilustrativo — cria credibilidade falsa
- A seção 6.6 (casos de uso) é uma lista fria sem hierarquia ou critério de seleção — lembra uma apresentação de vendas, não um livro de método
- Ausência de qualquer discussão sobre avaliação/métricas de qualidade em RAG (Recall@K, MRR, RAGAS, avaliação human) — o capítulo diz que se pode medir mas não diz como
- O nível técnico oscila: às vezes fala com desenvolvedor (BM25 implícito nas estratégias, top-k, cross-encoders), outras vezes com executivo — Joana se perde especificamente no parágrafo de embeddings multidimensionais
- O capítulo lista bancos vetoriais ("Pinecone, Qdrant, Weaviate, ChromaDB, Milvus") como catálogo, o que viola a tese do livro — nenhum critério de escolha é dado
- Referência a "estado da arte em 2026" para chunking hierárquico: afirmação datada sem sustentação específica

---

## ACHADOS

### ACHADO 01
Categoria: P1
Problema: Seção 6.6 é lista de casos de uso sem método de seleção
Por que é um problema: Não ensina o leitor a raciocinar sobre quando usar RAG — apenas lista verticals. Isso é commodity de qualquer post de blog de IA e contradiz a tese "método fica".
Impacto no leitor: Joana decorará a lista mas não saberá aplicar o critério. O executivo lerá e ficará sem ferramenta de decisão.
Correção exata: Substituir a lista plana por um framework de 3 critérios para identificar candidatos a RAG na própria organização: (1) há base de conhecimento proprietária e volumosa?, (2) a informação muda com frequência?, (3) a rastreabilidade da resposta é requisito?. A lista atual pode ficar como apêndice ou exemplos, não como corpo principal.
Texto sugerido: "Antes de listar casos, vale nomear o critério. RAG entrega valor quando três condições se encontram: há conhecimento proprietário que o modelo genérico não tem, esse conhecimento muda com frequência suficiente para tornar fine-tuning impraticável, e a rastreabilidade da resposta tem valor real para quem usa. Onde esses três se somam, RAG é quase sempre a arquitetura certa. [Exemplos da lista atual como ilustrações desses critérios]"
ROI: ALTO

### ACHADO 02
Categoria: P1
Problema: Ausência total de métricas de avaliação de qualidade de RAG em produção
Por que é um problema: O capítulo termina com a pergunta de revisão "Como você mediria a qualidade de um sistema RAG em produção?" (6.11, Q5) sem jamais ter ensinado como fazer isso. Contradição pedagógica direta.
Impacto no leitor: O leitor que tenta aplicar o conhecimento em produção não tem critério para saber se o sistema está funcionando bem ou mal.
Correção exata: Adicionar ao menos um parágrafo em 6.3.2 (fase de consulta) sobre métricas básicas: Precision@K (quão relevantes são os chunks recuperados), Faithfulness (a resposta é fiel ao contexto recuperado?) e Answer Relevance. Mencionar frameworks como RAGAS para quem quiser aprofundar.
Texto sugerido: "Medir qualidade de RAG exige olhar para dois pontos distintos: a recuperação (os chunks certos estão sendo encontrados?) e a geração (a resposta é fiel ao que foi recuperado?). Métricas como Precision@K medem o primeiro. Frameworks como RAGAS combinam ambos em pipelines semi-automatizados de avaliação, e são o padrão de facto em times maduros."
ROI: ALTO

### ACHADO 03
Categoria: P0
Problema: Lista de bancos vetoriais sem critério de escolha viola a tese
Por que é um problema: Enumerar "Pinecone, Qdrant, Weaviate, ChromaDB, Milvus" sem dar nenhum critério diferenciador torna o livro num catálogo de ferramentas — exatamente o que a rubrica proíbe. Além disso, esse mercado muda rapidamente: a lista envelhecerá.
Impacto no leitor: O leitor não aprende nada sobre como escolher. Aprende apenas que existem opções, o que ele descobriria em 30 segundos de pesquisa.
Correção exata: Remover a lista de nomes específicos. Substituir pelos critérios de seleção que sobrevivem: escala necessária, latência exigida, necessidade de filtros por metadados, orçamento de operação, exigência de hospedagem própria (open source vs. SaaS). Mencionar que o mercado de bancos vetoriais evolui rápido e remeter o leitor para recursos online curados.
Texto sugerido: "O mercado de bancos vetoriais em 2026 tem pelo menos meia dúzia de opções maduras. A decisão entre elas raramente é técnica — é operacional: você precisa de SaaS gerenciado ou hospedagem própria? Qual o volume esperado de vetores? Há requisitos de filtro por metadados estruturados? Latência de consulta é crítica? Essas perguntas, não os nomes dos produtos, devem guiar a escolha."
ROI: ALTO

### ACHADO 04
Categoria: P1
Problema: Quantificação precisa em cenário declarado como ilustrativo ("68% de redução", "seis semanas de onboarding")
Por que é um problema: Cenário afirma explicitamente ser "cenário ilustrativo" mas apresenta métricas específicas de três casas que emprestam credibilidade factual indevida. Isso é epistemicamente desonesto e tecnicamente questionável.
Impacto no leitor: Leitor crítico — como um CTO que tentará reproduzir — ficará desconfiado do autor quando perceber a inconsistência. Leitor crédulo usará esses números em apresentações internas como benchmarks reais.
Correção exata: Generalizar os números ("redução significativa", "na ordem de meses, não semanas") ou adicionar nota metodológica como o capítulo 11 faz. Alternativamente, citar fonte real.
Texto sugerido: n/a — ajuste editorial de redação existente
ROI: MÉDIO

### ACHADO 05
Categoria: P2
Problema: Menção a "voyage-multilingual" como modelo de embedding no exemplo (6.5) introduz nome de produto específico em cenário ilustrativo
Por que é um problema: Pequena violação da tese — cita produto como se fosse escolha natural, sem critério; e esse produto pode não existir ou ter evoluído quando o leitor ler.
Impacto no leitor: Mínimo, mas consistência da obra exige coerência.
Correção exata: Substituir por "modelo de embedding com suporte multilingual" sem citar nome específico.
Texto sugerido: n/a
ROI: BAIXO

### ACHADO 06
Categoria: P2
Problema: A autoavaliação item 5 (6.15) tem espaço extra antes do checkbox ("Curiosidade ☐")
Por que é um problema: Erro tipográfico que aparece em todos os capítulos — indica que é erro sistêmico do template.
Impacto no leitor: Ruído visual menor.
Correção exata: Remover espaço duplo entre "Curiosidade" e "☐" em todos os capítulos.
Texto sugerido: n/a
ROI: BAIXO

---

## TESTE DA JOANA
Entenderia: SIM (parcialmente)
O que ela entenderia: A analogia do consultor com biblioteca, por que RAG resolve o problema de dados privados, e a lógica geral de chunking em versão superficial
O que ela NÃO entenderia: "embeddings só são comparáveis dentro do mesmo modelo" (seção 6.3.2, segundo parágrafo) — conceito jogado sem ancora; "reranking com cross-encoders" — terminologia técnica sem analogia de apoio; o significado prático de "top-k" sem explicação intuitiva de trade-off
Como corrigir: Adicionar uma linha de ancoragem antes de cada conceito técnico quando o capítulo muda de público implícito. Ex.: antes de falar de cross-encoders, uma frase: "imagine um segundo revisor, mais lento mas mais criterioso, que relê as respostas candidatas e as reordena por relevância — isso é o reranker".

## TESTE DE DURABILIDADE
Classificação: MÉDIA
2 anos: ALTA — conceitos de indexação, chunking e consulta são estáveis
5 anos: MÉDIA — nomes de bancos vetoriais, menção a "estado da arte em 2026" para chunking hierárquico, modelos de embedding específicos vão envelhecer
10 anos: BAIXA para partes específicas — o conceito de RAG como arquitetura sobrevive, mas toda a camada de implementação ficará desatualizada
Justificativa: A separação entre fase de indexação e consulta é invariante; as estratégias de chunking são princípios duráveis. Mas a lista de bancos vetoriais, os nomes de modelos de embedding, e a menção a "estado da arte em 2026" são time-bombs.

## TESTE DE DIFERENCIAÇÃO
Classificação: DIFERENCIADO
Justificativa: A combinação de analogia forte + estrutura pedagógica clara + seção honesta de limitações coloca este capítulo acima da média do que existe em livros de IA em português. O que impede a classificação PROPRIEDADE INTELECTUAL é a ausência de framework original de decisão e a seção de casos de uso genérica.

## TESTE DE MEMORIZAÇÃO
Ideia principal clara? SIM
Qual é a ideia principal (em 1 frase): RAG separa conhecimento proprietário do modelo e o injeta dinamicamente — o que resolve simultaneamente alucinação, atualização e rastreabilidade.
Justificativa: A analogia do consultor carrega a ideia central com força. A frase final do capítulo ("RAG não é só uma técnica. É uma camada de inteligência organizacional") é citável.

## TESTE DE TRANSFORMAÇÃO
Ao terminar, o leitor consegue fazer o que antes não conseguia:
- Explicar RAG para um não-técnico em 90 segundos usando a analogia correta
- Distinguir indexação de consulta com clareza operacional
- Identificar quando RAG não é a solução certa
- Conduzir auditoria básica de base de conhecimento antes de implementar
O leitor NÃO consegue ainda:
- Escolher entre bancos vetoriais com critério
- Medir se um sistema RAG está funcionando bem em produção
- Projetar estratégia de chunking para tipo específico de documento sem experimentação

## NOTA FINAL (0-10 cada eixo)
Estrutura: 9 | Pedagogia: 8 | Clareza: 7 | Autoridade: 8 | Durabilidade: 7 | Diferenciação: 7 | Memorização: 8 | Transformação: 7
**Nota Geral: 7.6**

## DECISÃO EDITORIAL
MANTER COM AJUSTES

---

# C07 — L1-C07-memoria.md

## RESUMO EXECUTIVO
Nota: 8/10
Veredito: A

## O QUE FUNCIONA
- A analogia do assistente com amnésia retrógrada e o "sistema ao redor dele" é provavelmente a mais forte dos seis capítulos: concreta, estruturante, memorável
- A taxonomia dos quatro tipos de memória (curto prazo, episódica, semântica, procedural) é bem ancorada na ciência cognitiva e cada tipo tem correspondência arquitetural clara
- O exemplo do CEO (7.4) é o mais rico dos cenários ilustrativos neste bloco: mostra as três camadas em uso coordenado, não isolado, e a frase "O LLM continuava sem memória dentro de si. Mas a arquitetura em volta dele era um arquiteto cognitivo competente" é citável
- A seção 7.5 (futuro da memória) é rara num livro de IA em português — especulação honesta sobre direções emergentes, sem promessas falsas
- A pergunta de revisão 5 ("Por que esquecer pode ser uma feature, não bug?") é elegante e abre raciocínio não óbvio

## O QUE NÃO FUNCIONA
- O capítulo não diz o que fazer quando a memória falha — há zero orientação sobre diagnóstico de falhas de continuidade em sistemas reais
- Memória procedural (7.3.4) é substancialmente menos desenvolvida que as outras três — recebe dois parágrafos e uma remissão ao Livro 2, que o leitor ainda não tem
- A seção 7.5 menciona "continual learning" como abordagem de memória nativa em modelos — afirmação tecnicamente delicada: continual learning é campo de pesquisa com problemas não resolvidos (catastrophic forgetting) que o texto não menciona
- O texto diz que "agente bem desenhado, ao final de cada interação relevante, executa um processo de consolidação" (7.3.3) sem explicar quem define "relevante" ou como isso é implementado — abstração sem aterramento
- Ausência de qualquer discussão sobre privacidade de dados em memória episódica — em contexto corporativo, guardar transcrições de interações tem implicações LGPD/GDPR que são relevantes para o público-alvo

---

## ACHADOS

### ACHADO 07
Categoria: P1
Problema: Memória procedural é tratada superficialmente e remetida ao Livro 2
Por que é um problema: O leitor deste livro não tem o Livro 2. Receber "será tratado no Livro 2" como resposta a um quarto do framework que acabou de ser introduzido é pedagogicamente frustrante e estruturalmente inconsistente com a profundidade das outras três seções.
Impacto no leitor: O leitor aprende três tipos de memória com substância e um sem substância, o que enfraquece o framework como ferramenta de diagnóstico.
Correção exata: Expandir 7.3.4 com pelo menos dois parágrafos concretos: o que é memória procedural em prática hoje (system prompts com workflows, skills no Claude, agentes especializados como ferramentas de outros agentes), e pelo menos um exemplo concreto de quando ela falha e como diagnosticar.
Texto sugerido: "Em termos operacionais, memória procedural em sistemas de IA se materializa hoje em três formas: system prompts que encapsulam fluxos de trabalho definidos ('para análise de contratos, sempre siga estas cinco etapas...'); ferramentas especializadas que agentes invocam para tarefas específicas; e workflows orquestrados que definem sequências de ações para processos recorrentes. O sinal de falha de memória procedural é característico: o agente sabe o que quer fazer mas não sabe como — gera steps genéricos em vez de seguir o protocolo definido."
ROI: ALTO

### ACHADO 08
Categoria: P0
Problema: Afirmação sobre continual learning em modelos sem mencionar catastrophic forgetting
Por que é um problema: "memória persistente nativa em modelos, via técnicas como continual learning" (7.5, quarta direção) é apresentada como direção promissora sem mencionar o principal obstáculo não resolvido do campo: o catastrophic forgetting, em que novos dados sobrescrevem conhecimento anterior. Isso induz o leitor a uma visão otimista sem base técnica adequada.
Impacto no leitor: Executivos que lerem isso podem questionar a necessidade de arquiteturas externas achando que "o modelo vai aprender sozinho em breve" — decisão arquitetural equivocada com consequências reais.
Correção exata: Adicionar uma frase sobre o principal desafio: "A maior barreira técnica para essa abordagem é o catastrophic forgetting — novos aprendizados tendem a sobrescrever conhecimento anterior nos pesos. Resolver isso de forma estável é um dos problemas em aberto mais difíceis da área."
Texto sugerido: (integrar na quarta direção da seção 7.5)
ROI: ALTO

### ACHADO 09
Categoria: P1
Problema: Ausência de qualquer orientação sobre privacidade em memória episódica
Por que é um problema: Memória episódica em contexto corporativo significa guardar transcrições de interações de usuários. Para o público-alvo do livro (executivos brasileiros), isso levanta questões LGPD imediatas que não são mencionadas. O livro fala em "guardar episódios com metadados como data, usuário envolvido, tópico identificado" — isso é dado pessoal em qualquer interpretação razoável da LGPD.
Impacto no leitor: O leitor implementará memória episódica sem as salvaguardas necessárias, expondo a organização a risco legal.
Correção exata: Adicionar caixa "Para Executivos" ou parágrafo em 7.3.2 alertando: memória episódica pode conter dados pessoais sob LGPD/GDPR, exigindo política explícita de retenção, consentimento quando aplicável, e processo de esquecimento a pedido do titular.
Texto sugerido: "Atenção para quem implementa: memória episódica que armazena histórico de interações com identificação de usuário é dado pessoal sob a LGPD. Isso implica base legal para tratamento, prazo de retenção definido, e processo de exclusão sob demanda. Sistemas sem essa política correm risco legal antes de qualquer risco técnico."
ROI: ALTO

### ACHADO 10
Categoria: P1
Problema: A definição de "consolidação" (7.3.3) é abstrata sem qualquer exemplo de implementação
Por que é um problema: "O agente executa um processo de consolidação em que extrai fatos da conversa atual e atualiza a memória semântica" — isso soa simples mas oculta complexidade significativa: quem classifica o que é "fato relevante"? Como se evita poluição da memória semântica com informação errada que o usuário disse? O livro não responde.
Impacto no leitor: O leitor tenta implementar consolidação e imediatamente esbarra em perguntas não respondidas pelo capítulo.
Correção exata: Adicionar um parágrafo de implementação mínima: "Na prática, consolidação é frequentemente implementada como uma chamada adicional ao LLM ao final de cada sessão relevante, com um prompt que pede ao modelo para extrair fatos estruturados da conversa (nome, preferências, decisões tomadas, restrições identificadas) e compará-los com o perfil existente. O maior risco é consolidar informação errada que o usuário disse de passagem como se fosse preferência permanente — o que exige mecanismo de confiança ou revisão periódica."
Texto sugerido: (integrar em 7.3.3)
ROI: MÉDIO

### ACHADO 11
Categoria: P2
Problema: A citação do Anthropic Memory na seção de referências aponta para feature que pode ter mudado de nome ou URL
Por que é um problema: "anthropic.com/news/memory" é URL específica de notícia que pode mudar ou ficar obsoleta rapidamente.
Impacto no leitor: Link quebrado em livro já publicado.
Correção exata: Substituir por referência mais estável: "Anthropic — documentação de features de memória em Claude" sem URL específica, ou URL para docs.anthropic.com.
Texto sugerido: n/a
ROI: BAIXO

---

## TESTE DA JOANA
Entenderia: SIM
O que ela entenderia: A analogia do assistente com amnésia + os quatro tipos de memória com exemplos concretos + o cenário do CEO que é o mais narrativo de todos os capítulos
O que ela NÃO entenderia: "banco vetorial específico para conversas anteriores" (7.3.2) sem a ponte explicativa de como vetores se relacionam com busca semântica (a ligação com Cap 5 e 6 é assumida, não explicada); "continual learning" (7.5) jogado sem definição
Como corrigir: Uma linha de ancoragem em 7.3.2 ("usando a mesma técnica de busca semântica do Cap 6") e remoção ou simplificação do termo "continual learning" em 7.5.

## TESTE DE DURABILIDADE
Classificação: ALTA
2 anos: ALTA — framework de quatro tipos de memória é arquitetural e estável
5 anos: ALTA — os conceitos são emprestados da ciência cognitiva, não de produtos específicos
10 anos: MÉDIA — a seção 7.5 sobre direções futuras pode envelhecer, especialmente a referência a MemGPT e Mem0 que são produtos
Justificativa: Este é o capítulo mais durável do bloco. A taxonomia cognitiva sobrevive qualquer mudança de produto. O risco principal são as referências específicas de produtos nas referências bibliográficas.

## TESTE DE DIFERENCIAÇÃO
Classificação: DIFERENCIADO
Justificativa: A distinção explícita entre "o LLM não lembra" e "a arquitetura em volta lembra" é genuinamente esclarecedora e não está articulada assim na maioria dos recursos de IA em português. O framework cognitivo aplicado a arquitetura de software é original na abordagem, mesmo não sendo nos conceitos.

## TESTE DE MEMORIZAÇÃO
Ideia principal clara? SIM
Qual é a ideia principal (em 1 frase): O LLM não tem memória — mas o sistema ao redor dele pode ter quatro tipos de memória que, juntos, criam a ilusão de continuidade.
Justificativa: A última citação do capítulo ("Memória boa em agentes não vem do modelo, vem da arquitetura. Quem confunde isso constrói brinquedos. Quem entende, constrói ferramentas.") é forte e citável.

## TESTE DE TRANSFORMAÇÃO
Ao terminar, o leitor consegue fazer o que antes não conseguia:
- Diagnosticar qual tipo de memória está faltando em uma aplicação com problema de continuidade
- Esboçar arquitetura de memória com quatro camadas para um caso concreto
- Distinguir o que vai dentro do modelo do que vai fora
- Perceber quando "o modelo esqueceu" é problema de arquitetura, não de modelo
O leitor NÃO consegue ainda:
- Implementar consolidação com critério para evitar poluição da memória semântica
- Tratar implicações de privacidade de memória episódica
- Implementar memória procedural de forma concreta (seção subdesenvolvida)

## NOTA FINAL (0-10 cada eixo)
Estrutura: 9 | Pedagogia: 8 | Clareza: 8 | Autoridade: 7 | Durabilidade: 9 | Diferenciação: 8 | Memorização: 9 | Transformação: 7
**Nota Geral: 8.1**

## DECISÃO EDITORIAL
MANTER COM AJUSTES

---

# C08 — L1-C08-fine-tuning.md

## RESUMO EXECUTIVO
Nota: 8.5/10
Veredito: A

## O QUE FUNCIONA
- A premissa negativa é a escolha certa: começar com "quando não usar" em vez de "como usar" diferencia este capítulo de 95% dos conteúdos de IA sobre fine-tuning
- A hierarquia das soluções (8.4) é o framework mais acionável dos seis capítulos — six degraus em ordem de custo e complexidade, com critério explícito para subir cada um
- O exemplo da seguradora (8.5) é o mais honesto e o mais didaticamente rico: a consultoria propõe piloto de alternativa antes de aceitar o projeto — isso ensina comportamento, não só técnica
- A seção de custos reais (8.6) com números concretos em dólares é rara e valiosa — o autor assume o risco de dar números que envelhecem, e isso é correto porque força concretude
- A frase "vaidade disfarçada de estratégia" no checklist é exatamente o tipo de formulação memorável que este livro precisa mais
- O texto "antes de aprovar qualquer projeto de fine-tuning na sua organização, exija..." (caixa Para Executivos) é acionável e específico

## O QUE NÃO FUNCIONA
- LoRA é mencionado mas "suas evoluções" (8.3.1) fica vago — QLoRA, DoRA, RSLoRA são variantes relevantes em 2026 que o texto referencia apenas na bibliografia
- Os custos em dólares (8.6) são apresentados como "típicos em 2026" para projetos com modelos open source — mas não diferenciam por tamanho de modelo (7B vs. 70B), o que é fator de magnitude
- Ausência de qualquer discussão sobre overfitting em fine-tuning — o risco mais comum em projetos com dados insuficientes não é mencionado
- A hierarquia de soluções (8.4) não menciona avaliação/testes — é possível subir a escada sem saber se o degrau atual realmente não bastou? Falta critério de "como saber que o degrau inferior não resolve"

---

## ACHADOS

### ACHADO 12
Categoria: P1
Problema: Ausência de discussão sobre overfitting em fine-tuning
Por que é um problema: Overfitting (modelo aprende os dados de treino em vez de generalizar) é o fracasso técnico mais comum em projetos de fine-tuning com dados insuficientes. O texto menciona "dados ruins amplificam problemas" mas não nomeia o mecanismo.
Impacto no leitor: O leitor que implementa fine-tuning sem conhecer overfitting vai gastar os recursos e produzir um modelo que performa bem no conjunto de treino e mal em produção, sem saber por quê.
Correção exata: Adicionar parágrafo em 8.3.1 ou 8.3.3: "O risco técnico principal é overfitting — o modelo memoriza os exemplos de treino sem generalizar o padrão. Em projetos com poucos dados (menos de mil exemplos), ou com exemplos repetitivos, o modelo aprende os casos específicos em vez da regra subjacente. Sinal de overfitting: performance alta no conjunto de treino, baixa em casos novos. Mitigação: diversidade nos dados, regularização, early stopping."
Texto sugerido: (integrar em 8.3.3 como sexto anti-padrão ou em 8.3.1 como risco técnico)
ROI: ALTO

### ACHADO 13
Categoria: P1
Problema: Hierarquia das soluções não define critério de quando subir degrau
Por que é um problema: A hierarquia diz "só suba quando o degrau inferior provadamente não basta" mas não diz como provar. Sem critério de avaliação, a hierarquia é preferência subjetiva, não método.
Impacto no leitor: O leitor apresenta a hierarquia numa reunião e alguém pergunta "como sabemos que RAG não bastou?" — sem resposta no capítulo.
Correção exata: Adicionar no início da seção 8.4 um parágrafo sobre o critério de avaliação: "Provar que um degrau não basta exige experimento, não intuição. Para cada degrau, defina uma métrica de sucesso antes de começar, execute em amostra representativa de casos reais, compare com baseline. Se a métrica não for atingida depois de iteração razoável, aí — e só aí — o próximo degrau está justificado."
Texto sugerido: (integrar como parágrafo inicial da seção 8.4)
ROI: ALTO

### ACHADO 14
Categoria: P0
Problema: Os custos em dólares (8.6) são específicos demais para serem duráveis e insuficientemente especificados para serem úteis
Por que é um problema: "Coleta e curadoria de dados... custa entre 20 e 100 mil dólares" — range de 5x sem qualquer variável explicativa. "Compute para o treinamento... entre 5 e 50 mil dólares" — range de 10x igualmente inexplicado. Esses números envelhecem com a velocidade dos custos de GPU que caem ~40% ao ano.
Impacto no leitor: Em dois anos os números estarão errados. Hoje, são amplos demais para uso em estimativas reais.
Correção exata: Manter a estrutura de categorias (curadoria, compute, validação, hospedagem, manutenção) que é durável, mas substituir valores fixos por dois elementos: (1) o driver de custo em cada categoria (ex.: para compute, o número de parâmetros e o número de exemplos determinam o custo), e (2) referência a onde buscar preços atualizados. Manter a comparação com RAG como elemento estrutural.
Texto sugerido: "Os valores variam conforme o tamanho do modelo (um modelo de 7B é 10x mais barato de treinar que um de 70B), o volume de dados, e os preços vigentes de GPU — que caem historicamente 30 a 40% ao ano. Em vez de citar valores fixos, que envelhecem rapidamente, vale estruturar a estimativa pelas categorias [manter categorias], consultando calculadoras públicas de provedores como AWS, GCP e Replicate para preços de GPU no momento da avaliação."
ROI: ALTO

### ACHADO 15
Categoria: P2
Problema: "GPT-5" mencionado na autoavaliação (8.14 via referência indireta ao Cap 9) — mas especificamente em 8.11, Q2, a pergunta menciona "fine-tunado para essa tarefa pode rodar mais barato e mais rápido que um modelo grande genérico" sem definir o que é "modelo grande genérico" em 2026
Por que é um problema: Definição implícita de "grande" muda a cada geração de modelos.
Impacto no leitor: Mínimo — mas a argumento fica datado.
Correção exata: Substituir "modelo grande genérico" por "modelo frontier comercial" que é terminologia mais estável.
Texto sugerido: n/a
ROI: BAIXO

### ACHADO 16
Categoria: P2
Problema: Referência na bibliografia ao "Anthropic — When to use prompting vs fine-tuning" aponta para URL específica de documentação que muda frequentemente
Por que é um problema: Links de documentação de API são voláteis.
Impacto no leitor: Link quebrado.
Correção exata: Remover URL específica, manter referência geral.
Texto sugerido: n/a
ROI: BAIXO

---

## TESTE DA JOANA
Entenderia: SIM
O que ela entenderia: A analogia da residência médica funciona bem. A hierarquia das soluções é o tipo de framework que ela aplica diretamente em reuniões. O exemplo da seguradora é o mais próximo do seu mundo (decisão executiva, não implementação técnica).
O que ela NÃO entenderia: "LoRA ajusta apenas pequenas matrizes adicionais em vez do modelo inteiro" (8.3.1) — sem analogia, vira jargão opaco. "Hiperparâmetros" em 8.6 aparece sem definição.
Como corrigir: Uma linha de analogia para LoRA: "LoRA é como adaptar um terno existente em vez de costurar um novo — ajustes pontuais em vez de reconstrução completa, muito mais barato e reversível."

## TESTE DE DURABILIDADE
Classificação: MÉDIA
2 anos: ALTA — a hierarquia das soluções e os critérios de quando usar/não usar são estáveis
5 anos: MÉDIA — os valores de custo em 8.6 estarão errados; nomes de modelos (Llama, Mistral, Gemma) vão mudar
10 anos: BAIXA para partes específicas — os princípios de decisão sobrevivem, os números e nomes não
Justificativa: O método (hierarquia, critérios, anti-padrões) é durável. Os valores numéricos são o ponto mais frágil.

## TESTE DE DIFERENCIAÇÃO
Classificação: PROPRIEDADE INTELECTUAL
Justificativa: A hierarquia das soluções como escada de seis degraus com critério de ascensão é genuinamente original como ferramenta de decisão. O ângulo de "não fazer fine-tuning" como posição padrão inverte o que 90% dos conteúdos de IA recomendam. O exemplo da seguradora, em que a consultoria propõe não fazer o que foi contratada para fazer, é o tipo de história que não existe em outros livros.

## TESTE DE MEMORIZAÇÃO
Ideia principal clara? SIM
Qual é a ideia principal (em 1 frase): Fine-tuning é o último recurso numa hierarquia de seis degraus, e a maioria das organizações pula para ele por vaidade antes de exaurir opções mais baratas e mais rápidas.
Justificativa: A hierarquia visual (quando materializada em diagrama) e a frase "vaidade disfarçada de estratégia" são os dois âncoras de memorização.

## TESTE DE TRANSFORMAÇÃO
Ao terminar, o leitor consegue fazer o que antes não conseguia:
- Questionar qualquer proposta de fine-tuning com quatro perguntas específicas de validação
- Aplicar a hierarquia das soluções sistematicamente antes de qualquer decisão arquitetural
- Estimar em ordem de grandeza o custo de um projeto de fine-tuning versus RAG
- Reconhecer "vaidade organizacional" como padrão de falha específico
- Estruturar piloto de alternativa de duas semanas antes de comprometer orçamento
O leitor NÃO consegue ainda:
- Detectar overfitting em fine-tuning (não ensinado)
- Definir critério objetivo para saber que o degrau inferior "não bastou"

## NOTA FINAL (0-10 cada eixo)
Estrutura: 9 | Pedagogia: 9 | Clareza: 8 | Autoridade: 9 | Durabilidade: 7 | Diferenciação: 9 | Memorização: 9 | Transformação: 8
**Nota Geral: 8.5**

## DECISÃO EDITORIAL
MANTER COM AJUSTES

---

# C09 — L1-C09-engenharia-prompt.md

## RESUMO EXECUTIVO
Nota: 7.5/10
Veredito: B+

## ALERTA ESPECIAL — RISCO DE "COLEÇÃO DE PROMPTS"
Este capítulo caminha na borda da linha proibida. Seção 9.4 ("Técnicas que fazem diferença real") é uma lista de seis técnicas sem hierarquia, sem critério de quando aplicar cada uma, sem framework de decisão. É exatamente o tipo de conteúdo que vira obsoleto em seis meses porque depende de comportamento específico de modelos atuais. A seção de referências (9.13) inclui link para "awesome-prompts (GitHub)" — um repositório de prompts prontos — o que é a antítese da tese do livro. Detalhe no Achado 17 e 18.

## O QUE FUNCIONA
- A reframing de "conversa" para "interface de programação" na abertura (9.1) é o ganho conceitual mais importante do capítulo e cumpre a tese "método fica"
- A anatomia dos cinco blocos funcionais (9.3.1) é pedagogicamente sólida: nomes claros, função de cada bloco, posicionamento justificado
- O exemplo da empresa de moda (9.5) é o mais detalhado dos cenários e tem os cinco passos descritos de forma reaplicável — funciona como checklist implícito
- A seção de governança e versionamento (9.6) é rara e relevante: trata prompts como ativos de engenharia, o que está alinhado com a tese
- A caixa "Para Executivos" no final de 9.5 é a mais acionável de todo o bloco de seis capítulos

## O QUE NÃO FUNCIONA
- Seção 9.4 é lista de técnicas sem framework — não ensina quando aplicar cada uma nem por quê certas técnicas funcionam no nível de mecanismo
- "awesome-prompts (GitHub)" na bibliografia é coleção de prompts prontos — diametralmente oposto à tese do livro
- A menção a "GPT-5" em 9.3.2 como modelo de referência é datada
- Ausência de discussão sobre falhas comuns de engenharia de prompt: prompt injection, jailbreaking não intencional, comportamento inconsistente entre versões de modelos
- A seção de role prompting (9.3.3) menciona "modelos modernos foram treinados com cuidado para resistir" a papéis manipuladores — afirmação verdadeira mas sem evidência, e o comportamento varia entre modelos e versões
- O capítulo não diferencia prompts para humanos (interface conversacional) de prompts para sistemas (pipeline automatizado) — são contextos com requisitos completamente diferentes

---

## ACHADOS

### ACHADO 17
Categoria: P0
Problema: Referência a "awesome-prompts (GitHub)" na bibliografia (9.13)
Por que é um problema: Este repositório é uma coleção de prompts prontos para copiar e usar — o oposto exato da tese "modelos passam, método fica". Incluí-lo como recurso recomendado contradiz explicitamente o posicionamento do livro.
Impacto no leitor: O leitor entende que a solução é colecionar prompts, não desenvolver método. Isso desfaz o trabalho pedagógico do capítulo inteiro.
Correção exata: Remover a referência. Se o autor quiser manter um recurso sobre repositórios, substituir por referência sobre gerenciamento e versionamento de prompts (ex.: PromptLayer, LangSmith) que são sobre governança, não coleção.
Texto sugerido: n/a — remoção pura
ROI: ALTO

### ACHADO 18
Categoria: P0
Problema: Seção 9.4 é lista de técnicas sem framework de decisão
Por que é um problema: Seis técnicas listadas sem critério de quando aplicar cada uma, sem hierarquia por caso de uso, sem explicação do mecanismo de cada uma. Isso é exatamente o padrão "coleção de receitas" que a rubrica proíbe. Algumas técnicas dependem de comportamento de modelos específicos (ex.: "instrução explícita para pensar antes de responder" funciona diferente em Claude vs. GPT vs. Gemini).
Impacto no leitor: O leitor tenta aplicar todas as seis em qualquer situação, o que é o anti-padrão clássico de engenharia de prompt fraca. Ou aplica aleatoriamente sem saber qual técnica resolve qual problema.
Correção exata: Reorganizar a seção em torno de três categorias de problema: (1) problemas de qualidade de raciocínio → instrução de pensar antes, critérios explícitos; (2) problemas de formato e consistência → formato verificável, separar persona de instrução; (3) problemas de complexidade → iteração com refinamento. Cada técnica deve ter uma frase de "quando usar" antes da descrição.
Texto sugerido: (reestruturação da seção 9.4 inteira com subcabeçalhos por categoria de problema)
ROI: ALTO

### ACHADO 19
Categoria: P1
Problema: Ausência de distinção entre prompts conversacionais e prompts de pipeline
Por que é um problema: O capítulo mistura os dois contextos sem avisar. Engenharia de prompt para humanos conversando com um assistente tem requisitos diferentes de engenharia de prompt para sistemas automatizados (onde não há humano para corrigir, onde formato de saída é parseado por código, onde consistência entre chamadas é crítica).
Impacto no leitor: O leitor aplica técnicas de prompt conversacional em pipelines automatizados e vice-versa, gerando resultados inconsistentes sem entender por quê.
Correção exata: Adicionar parágrafo em 9.1 ou 9.3 distinguindo os dois contextos: "Prompts para uso humano permitem ambiguidade — o usuário pode pedir esclarecimento. Prompts para sistemas automatizados exigem estrutura de saída garantida (JSON com schema, não texto livre), porque não há humano para corrigir. Muitas das técnicas deste capítulo se aplicam a ambos, mas o critério de sucesso é diferente."
Texto sugerido: (integrar na abertura de 9.3)
ROI: MÉDIO

### ACHADO 20
Categoria: P1
Problema: "GPT-5" em 9.3.2 como exemplo de modelo com comportamento específico
Por que é um problema: "funciona bem zero-shot em modelos como Claude Sonnet ou GPT-5" — cita comportamento de modelos específicos que pode mudar com qualquer atualização. Esta é uma afirmação frágil e datada.
Impacto no leitor: Leitor que usa GPT-4o ou Claude Haiku pode achar que o que o capítulo descreve não se aplica ao modelo que usa.
Correção exata: Substituir por "em modelos de alta capacidade" ou "em modelos frontier" sem citar versões específicas.
Texto sugerido: "funciona bem zero-shot em modelos de alta capacidade, mas modelos menores exigem mais contexto para o mesmo resultado."
ROI: MÉDIO

### ACHADO 21
Categoria: P1
Problema: Role prompting (9.3.3) diz que modelos "resistem" a papéis manipuladores sem nuance
Por que é um problema: "Modelos modernos foram treinados com cuidado para resistir a esse tipo de manipulação" — isso é verdade em média, mas varia significativamente por modelo, versão, e tipo de manipulação. A afirmação pode criar falsa sensação de segurança.
Impacto no leitor: Profissionais de segurança podem descartar preocupações com prompt injection baseados nessa afirmação.
Correção exata: Adicionar qualificador: "Modelos frontier foram treinados para resistir às formas mais óbvias de manipulação via role prompting, mas isso não elimina o risco de prompt injection em aplicações que recebem input não confiável de usuários. Em sistemas em produção, validação de input continua sendo necessária."
Texto sugerido: (integrar em 9.3.3 após o parágrafo sobre anti-padrões)
ROI: MÉDIO

### ACHADO 22
Categoria: P2
Problema: A menção ao "Anthropic Prompt Library" (9.13) como recurso é borderline com "coleção de prompts"
Por que é um problema: O Anthropic Prompt Library é uma biblioteca de prompts prontos, o que está na borda da linha proibida pela tese do livro.
Impacto no leitor: Menor que o achado 17, mas consistente com o padrão problemático.
Correção exata: Se mantido, recontextualizar explicitamente: "para ver exemplos de estrutura de prompt, não para copiar".
Texto sugerido: n/a
ROI: BAIXO

### ACHADO 23
Categoria: P2
Problema: O exemplo de ROI (R$ 520 mil/ano) está em reais para empresa brasileira, enquanto exemplos de custo de fine-tuning (Cap 8) estão em dólares — inconsistência de moeda no livro
Por que é um problema: Inconsistência de unidade entre capítulos adjacentes.
Impacto no leitor: Mínimo, mas revela falta de revisão de consistência cross-capítulo.
Correção exata: Padronizar em dólares ou reais em todo o livro. Preferência pelo dólar, dado que custos de APIs são globalmente cotados em dólar.
Texto sugerido: n/a
ROI: BAIXO

---

## TESTE DA JOANA
Entenderia: SIM
O que ela entenderia: A analogia do estagiário é precisa e memorável. Os cinco blocos do prompt fazem sentido intuitivo. A história da empresa de moda é concreta e próxima do mundo dela.
O que ela NÃO entenderia: "few-shot" e "zero-shot" são introduzidos como termos técnicos sem tradução de primeira linha (explica depois, mas o rótulo fica opaco); "function calling" em 9.3.4 aparece sem definição; "CMS" no exemplo de moda aparece sem tradução.
Como corrigir: Definir "few-shot" na primeira menção como "com exemplos" antes de usar o termo; adicionar "(sistema de gerenciamento de conteúdo)" após CMS.

## TESTE DE DURABILIDADE
Classificação: MÉDIA
2 anos: ALTA para blocos funcionais, governança, XML/JSON — BAIXA para técnicas específicas de seção 9.4
5 anos: MÉDIA — a anatomia do prompt sobrevive; comportamentos específicos de modelos citados não
10 anos: BAIXA para partes técnicas — "XML preferido pela Anthropic" pode mudar; comportamentos de modelos citados vão mudar
Justificativa: A estrutura metodológica (cinco blocos, governança, versionamento) é durável. As referências a comportamentos específicos de modelos são frágeis.

## TESTE DE DIFERENCIAÇÃO
Classificação: DIFERENCIADO
Justificativa: O ângulo de governança formal de prompts (repositório versionado, testes automatizados, revisão por pares) não existe com este nível de desenvolvimento em outros livros de IA em português. A reframing de "conversa" para "interface" é o ganho conceitual real. O que rebaixa de PROPRIEDADE INTELECTUAL é a seção 9.4, que é commodity.

## TESTE DE MEMORIZAÇÃO
Ideia principal clara? SIM (com ressalva)
Qual é a ideia principal (em 1 frase): Prompt não é conversa — é interface de programação, e deve ser tratado com o mesmo rigor que código: versionamento, testes, governança.
Justificativa: A ideia de prompt como ativo de engenharia é o insight diferencial. A frase de abertura e a de fechamento reforçam isso. O risco é que a seção 9.4 (lista de técnicas) dilui essa ideia central.

## TESTE DE TRANSFORMAÇÃO
Ao terminar, o leitor consegue fazer o que antes não conseguia:
- Decompor qualquer prompt em cinco blocos funcionais e diagnosticar o que está faltando
- Defender à liderança por que prompts precisam de governança formal
- Construir few-shot com curadoria de exemplos (não coletar aleatoriamente)
- Estruturar prompt em XML para Claude
O leitor NÃO consegue ainda:
- Saber quando aplicar cada uma das seis técnicas de 9.4 (sem framework de decisão)
- Distinguir entre prompts conversacionais e de pipeline (não ensinado)
- Proteger prompts contra injection em produção (mencionado mas não desenvolvido)

## NOTA FINAL (0-10 cada eixo)
Estrutura: 7 | Pedagogia: 7 | Clareza: 8 | Autoridade: 7 | Durabilidade: 6 | Diferenciação: 7 | Memorização: 8 | Transformação: 7
**Nota Geral: 7.4**

## DECISÃO EDITORIAL
REVISAR PARCIALMENTE

---

# C10 — L1-C10-chain-of-thought.md

## RESUMO EXECUTIVO
Nota: 8/10
Veredito: A

## O QUE FUNCIONA
- A explicação do mecanismo de por que CoT funciona (10.1, terceiro parágrafo) é a mais tecnicamente precisa do livro: conecta geração token-por-token com a lógica de por que externalizar raciocínio ajuda — isso é invariante e sobrevive qualquer modelo
- A analogia do contador que mostra o cálculo (10.2) é forte e tem as três dimensões certas: visibilidade de erro, explicitação de suposições, auditabilidade
- A distinção entre tarefas onde CoT ajuda e onde não muda nada (10.3.2) é honesta e pedagogicamente necessária — maioria dos conteúdos sobre CoT omite isso
- O exemplo da telemedicina (10.4) é o mais revelador eticamente: transforma "técnica de qualidade" em "prática de segurança", o que é insight de ordem superior
- A limitação sobre "falsa sensação de explicabilidade" (10.5, quarta limitação) é sofisticada — a pesquisa sobre raciocínio pós-hoc é real e subutilizada em discussões práticas
- A caixa "Para Executivos" em 10.4 ("auditabilidade não é luxo, é controle") é a mais estrategicamente formulada de todo o bloco

## O QUE NÃO FUNCIONA
- Menciona "30 a 60 pontos percentuais" de diferença de qualidade (legenda do Diagrama 10.1) sem citar fonte — é afirmação quantitativa forte que precisa de sustentação
- "Claude Sonnet, GPT-5 e Gemini 3" em 10.3.1 são nomes de modelos que envelhecem — especialmente "GPT-5" e "Gemini 3" que são versões que podem não existir quando o leitor ler
- A seção de técnicas avançadas (10.3.3) inclui cinco variantes mas não dá critério de quando usar Tree of Thoughts vs. Self-Consistency vs. Plan-and-Solve — lista sem framework de decisão (mesmo problema que o Cap 9)
- O capítulo não discute como CoT interage com o custo de latência em aplicações com SLA apertado — aspecto crítico para quem implementa em produção

---

## ACHADOS

### ACHADO 24
Categoria: P1
Problema: "30 a 60 pontos percentuais" de melhoria citado sem fonte específica
Por que é um problema: É uma afirmação quantitativa forte que aparece em legenda de diagrama sem qualquer referência. Os papers citados em 10.12 mostram ganhos em benchmarks específicos que variam muito por tipo de tarefa.
Impacto no leitor: Executivo que usar esse número em apresentação interna e for questionado ficará exposto.
Correção exata: Ou citar fonte específica (ex.: "Wei et al. (2022) reportam ganhos de X% em benchmarks de matemática"), ou generalizar para "ganhos tipicamente substanciais, variando por tipo de tarefa e modelo — os papers originais reportam entre 20 e 60 pontos percentuais em benchmarks específicos de raciocínio matemático."
Texto sugerido: Substituir legenda do diagrama 10.1 para: "Em benchmarks de raciocínio matemático, Wei et al. (2022) reportam ganhos de 20 a 60 pontos percentuais. Em tarefas simples, o ganho é marginal ou inexistente."
ROI: MÉDIO

### ACHADO 25
Categoria: P1
Problema: Nomes de modelos específicos em 10.3.1 ("Claude Sonnet, GPT-5 e Gemini 3")
Por que é um problema: "GPT-5" e "Gemini 3" são versões que podem não existir com esses nomes quando o livro for lido. "Claude Sonnet" é linha de modelos Anthropic sujeita a versões.
Impacto no leitor: Datação imediata do texto para o leitor futuro.
Correção exata: Substituir por "modelos frontier modernos" ou "modelos de alta capacidade dos principais laboratórios".
Texto sugerido: "Funciona surpreendentemente bem em modelos frontier modernos, que foram treinados com técnicas que reforçam essa resposta."
ROI: MÉDIO

### ACHADO 26
Categoria: P1
Problema: Cinco variantes de CoT listadas em 10.3.3 sem critério de quando usar cada uma
Por que é um problema: Self-Consistency, Tree of Thoughts, Self-Critique, Plan-and-Solve e reasoning models são cinco abordagens com trade-offs muito diferentes. Sem framework de decisão, a seção é lista de nomes.
Impacto no leitor: O leitor não sabe se usa Self-Consistency ou Tree of Thoughts para um problema específico. A seção fica informativa mas não acionável.
Correção exata: Adicionar tabela de decisão com três colunas: Variante | Use quando | Custo relativo. Alternativamente, uma árvore de decisão: "se o problema tem múltiplas abordagens válidas → Self-Consistency; se o problema é combinatório ou exige busca → Tree of Thoughts; se a qualidade da primeira geração está incerta → Self-Critique; se o problema tem fases distintas → Plan-and-Solve; se a tarefa é complexa e latência não é crítica → reasoning models."
Texto sugerido: (tabela de decisão para integrar no final de 10.3.3)
ROI: ALTO

### ACHADO 27
Categoria: P2
Problema: Ausência de discussão sobre CoT e latência em aplicações com SLA
Por que é um problema: CoT "triplica ou quadruplica o tamanho típico da resposta" (10.5, terceira limitação) — o capítulo menciona isso mas não discute o impacto em tempo de resposta. Para aplicações com SLA de segundos (atendimento ao cliente, assistentes em tempo real), CoT pode ser inviável mesmo onde entregaria ganho.
Impacto no leitor: O leitor implementa CoT em aplicação de atendimento e descobre o problema de latência em produção.
Correção exata: Adicionar meia seção em 10.5 ou no início de 10.3.2 sobre o trade-off latência/qualidade: "Em aplicações onde o usuário espera resposta em menos de dois a três segundos — atendimento ao cliente, assistentes em tempo real, interfaces de voz — CoT pode não ser viável pela latência adicional. Para esses casos, reasoning models nativos costumam ser mais eficientes que CoT explícito, pois otimizam o raciocínio interno. Se latência é crítica, teste CoT apenas nos casos onde a tarefa é claramente complexa."
Texto sugerido: (integrar em 10.3.2 ou 10.5)
ROI: MÉDIO

---

## TESTE DA JOANA
Entenderia: SIM
O que ela entenderia: A analogia do contador, a ideia de "pensar antes de responder", e o exemplo da telemedicina são todos dentro do alcance dela. A distinção entre onde CoT ajuda e onde não vale (10.3.2) é exatamente o tipo de critério que ela busca.
O que ela NÃO entenderia: "Tree of Thoughts" e "Plan-and-Solve" sem nenhuma analogia — os nomes em inglês ficam flutuando sem âncora. "Reasoning tokens" em 10.3.3 é jargão técnico sem definição.
Como corrigir: Uma linha de analogia para cada variante avançada: "Tree of Thoughts é como um comitê considerando múltiplas abordagens antes de escolher uma."

## TESTE DE DURABILIDADE
Classificação: ALTA
2 anos: ALTA — o mecanismo de por que CoT funciona é invariante à geração de modelos
5 anos: ALTA — os princípios de raciocínio explícito sobrevivem mesmo que os modelos mudem radicalmente
10 anos: MÉDIA — nomes de modelos específicos envelhecem; reasoning models nativos podem tornar CoT explícito obsoleto
Justificativa: Este é provavelmente o segundo capítulo mais durável do bloco (depois de Cap 7). A explicação do mecanismo token-por-token é tipo de insight que sobrevive gerações de modelos.

## TESTE DE DIFERENCIAÇÃO
Classificação: DIFERENCIADO
Justificativa: A elevação de CoT de "técnica de qualidade" para "prática de segurança" em domínios críticos (seção 10.4) é insight que não existe em outros textos com esta clareza. A quarta limitação (raciocínio pós-hoc) demonstra profundidade técnica genuína.

## TESTE DE MEMORIZAÇÃO
Ideia principal clara? SIM
Qual é a ideia principal (em 1 frase): Pedir ao modelo que pense em voz alta antes de responder melhora qualidade porque cada passo do raciocínio vira contexto para o próximo — e esse raciocínio visível é também controle em domínios críticos.
Justificativa: A frase final do capítulo ("Modelos que pensam antes de responder produzem trabalho auditável. Em domínios sérios, auditabilidade não é luxo, é controle.") é a mais cítavel do bloco todo.

## TESTE DE TRANSFORMAÇÃO
Ao terminar, o leitor consegue fazer o que antes não conseguia:
- Explicar por que CoT funciona no nível de mecanismo (não só "porque funciona")
- Distinguir onde CoT entrega ganho real de onde é desperdício de tokens
- Defender CoT em domínios críticos como controle, não luxo
- Reconhecer as cinco limitações antes de adotar CoT indiscriminadamente
O leitor NÃO consegue ainda:
- Escolher entre Self-Consistency, ToT, Self-Critique e Plan-and-Solve com critério
- Avaliar impacto de CoT na latência de uma aplicação específica

## NOTA FINAL (0-10 cada eixo)
Estrutura: 9 | Pedagogia: 8 | Clareza: 8 | Autoridade: 8 | Durabilidade: 9 | Diferenciação: 8 | Memorização: 9 | Transformação: 8
**Nota Geral: 8.4**

## DECISÃO EDITORIAL
MANTER COM AJUSTES

---

# C11 — L1-C11-context-engineering.md

## RESUMO EXECUTIVO
Nota: 8.5/10
Veredito: A

## O QUE FUNCIONA
- A distinção conceitual entre engenharia de prompt e context engineering (11.1) é o posicionamento mais forte do capítulo: "de peça única e estática" para "sistema dinâmico com camadas" — isso é invariante
- A analogia da orquestra (11.2) é bem executada: não apenas ilustra mas estrutura — system prompt como base das cordas, RAG como entrada calculada, query como gatilho — a estrutura metafórica é coerente e acionável
- O glossário bilíngue (11.3, duas caixas) é solução pedagógica inteligente: quem sabe pula, quem não sabe encontra o vocabulário sem interromper o fluxo
- O exemplo da fintech (11.4) é o mais rico em rigor metodológico de todos os seis capítulos: a nota de "rigor estatístico" ao final do cenário é o único exemplo de transparência metodológica explícita em todo o bloco, e eleva a credibilidade do livro
- A seção de anti-padrões (11.5) é acionável — especialmente o quarto anti-padrão ("otimizar input ignorando output") que é contra-intuitivo e genuinamente valioso
- O fato de o capítulo fechar a Parte 2 com integração explícita de todos os capítulos anteriores (11.6) é bem-feito como síntese

## O QUE NÃO FUNCIONA
- O glossário é duplicado: aparece em 11.2 e depois novamente em 11.3 com termos parcialmente sobrepostos — isso é confuso e revela problema de revisão estrutural
- A afirmação "entre 40% e 70% desse valor seja desperdício otimizável" (caixa Para Executivos em 11.4) é afirmação forte sem base metodológica — o caso da fintech está bem documentado, mas a generalização para "qualquer organização" não está
- Ausência de discussão sobre quando context engineering não resolve: há casos (modelo incapaz da tarefa, dados fundamentalmente insuficientes) em que otimizar contexto não adianta
- O capítulo menciona "janela efetiva (a porção realmente atendida pelo modelo) tendendo a ser menor que a nominal" no glossário mas não desenvolve isso — é ponto técnico importante que fica como nota de rodapé
- A nota de rigor estatístico ao final do caso (11.4) é boa, mas diz "caso composto a partir de padrões observados em mais de uma organização" — isso é metodologicamente adequado mas deveria estar no paratexto do livro, não embutido no caso

---

## ACHADOS

### ACHADO 28
Categoria: P0
Problema: Glossário duplicado entre seções 11.2 e 11.3
Por que é um problema: O capítulo tem dois glossários com termos parcialmente sobrepostos (prompt caching, Lost in the Middle, RAG aparecem em ambos). Isso revela falta de revisão estrutural e gera confusão: o leitor que leu o primeiro glossário encontra definições repetidas no segundo, com formulações diferentes.
Impacto no leitor: Confusão sobre qual definição é a "oficial"; sensação de texto inacabado; perda de credibilidade de revisão editorial.
Correção exata: Unificar os dois glossários em um único, posicionado antes da seção 11.3.1 (hierarquia do contexto). Remover o glossário de 11.2 que é parcialmente redundante e parcialmente diferente.
Texto sugerido: n/a — reestruturação editorial
ROI: ALTO

### ACHADO 29
Categoria: P1
Problema: "Entre 40% e 70% de desperdício" generalizado sem base metodológica
Por que é um problema: A caixa Para Executivos afirma "é altamente provável que entre 40% e 70% desse valor seja desperdício otimizável" para "qualquer organização que gaste mais de 5 mil dólares por mês". O caso da fintech mostrou 73% de redução, mas uma empresa pode ter prompts já otimizados e ver ganhos mínimos.
Impacto no leitor: Um executivo que auditar sua operação e encontrar ganho de 20% vai questionar a credibilidade do autor. Um executivo mais crédulo tomará decisão de investimento em consultoria baseada em número não fundamentado.
Correção exata: Qualificar a afirmação: "Em aplicações onde context engineering ainda não foi aplicado sistematicamente, auditorias típicas encontram entre 30% e 70% de oportunidade de redução de custo sem perda de qualidade. O range varia significativamente por maturidade da aplicação."
Texto sugerido: "Se sua organização gasta mais de 5 mil dólares por mês em chamadas a modelos e ainda não aplicou context engineering sistematicamente, auditar o custo por camada costuma revelar oportunidades significativas de redução — em organizações sem nenhuma otimização prévia, o potencial é tipicamente alto. Auditar isso costuma render ROI de algumas semanas."
ROI: ALTO

### ACHADO 30
Categoria: P1
Problema: "Janela efetiva menor que a nominal" mencionada no glossário sem desenvolvimento
Por que é um problema: Esta é uma das afirmações técnicas mais importantes sobre modelos de contexto longo — que o modelo processa tokens ao longo da janela mas com atenção degradada no meio. Essa ideia, mencionada apenas no glossário, é o fundamento do Lost in the Middle e da seção de posicionamento estratégico. Merece pelo menos dois parágrafos no corpo do capítulo.
Impacto no leitor: O leitor que usa modelos com 2M de tokens acha que pode colocar qualquer informação em qualquer posição — o glossário contradiz isso mas o corpo do capítulo não reforça a implicação prática.
Correção exata: Expandir em 11.3.4 (posicionamento estratégico) com uma explicação explícita de por que janela nominal ≠ janela efetiva, e como isso informa a decisão de posicionamento.
Texto sugerido: "Uma distinção crítica: janela de contexto nominal (quantos tokens o modelo aceita) é diferente de janela efetiva (quantos tokens o modelo usa com qualidade alta). Modelos com janela de 200 mil tokens ainda sofrem Lost in the Middle em janelas de 50 mil tokens. Arquitetar como se a janela efetiva fosse sempre menor que a nominal é postura conservadora correta."
ROI: MÉDIO

### ACHADO 31
Categoria: P1
Problema: Ausência de discussão sobre quando context engineering não é suficiente
Por que é um problema: O capítulo é dedicado às virtudes e técnicas de context engineering, com anti-padrões de implementação. Mas não discute o caso em que nenhuma otimização de contexto resolve: modelo incapaz da tarefa, dados fundamentalmente ausentes ou irrelevantes, ou tarefa que exige raciocínio que o modelo não possui.
Impacto no leitor: O leitor pode gastar semanas otimizando contexto de uma aplicação cujo problema fundamental é outro.
Correção exata: Adicionar parágrafo em 11.5 como sexto anti-padrão: "O sexto anti-padrão é aplicar context engineering quando o problema é o modelo. Nenhuma otimização de contexto resolve uma tarefa que o modelo genuinamente não tem capacidade de executar. Se após otimização bem-feita a qualidade permanece inadequada, o problema pode ser de capacidade do modelo — não de contexto."
Texto sugerido: (integrar em 11.5)
ROI: MÉDIO

### ACHADO 32
Categoria: P2
Problema: "Andrej Karpathy — Threads sobre context engineering como disciplina (2024)" na referência (11.12)
Por que é um problema: Referência a threads de X/Twitter é volátil (podem ser deletados, o perfil pode mudar), tem validade editorial questionável em livro de não-ficção, e o conteúdo não é recuperável de forma estável.
Impacto no leitor: Referência não verificável pelo leitor.
Correção exata: Substituir por referência ao blog post, artigo, ou palestra de Karpathy sobre o tema, se existir; ou remover.
Texto sugerido: n/a
ROI: BAIXO

### ACHADO 33
Categoria: P2
Problema: "Configuração leva 30 minutos" (legenda do Diagrama 11.3) é afirmação arriscada
Por que é um problema: O tempo de configuração de prompt caching varia muito por stack técnica (30 minutos para quem já tem a aplicação estruturada; muito mais para quem precisa refatorar a arquitetura de chamadas). Afirmação precisa em contexto variável.
Impacto no leitor: Leitor que tenta em 30 minutos e não consegue questiona a credibilidade do autor.
Correção exata: Substituir por "Configuração técnica é direta para aplicações bem estruturadas — o investimento real é em reorganizar o prompt para que o conteúdo estável venha antes do variável."
Texto sugerido: (substituir legenda do diagrama 11.3)
ROI: BAIXO

---

## TESTE DA JOANA
Entenderia: SIM
O que ela entenderia: A analogia da orquestra funciona. O exemplo da fintech (corte de 73% de custo sem trocar de modelo) é exatamente o tipo de resultado executivo que ela usa como argumento interno. Os anti-padrões são concretos e reconhecíveis.
O que ela NÃO entenderia: "BM25" no segundo glossário — aparece sem definição suficiente para leigo. "Dense retrieval" e "RAG fusion" idem. "Prefill" — a definição no glossário é técnica demais.
Como corrigir: O segundo glossário (11.3) concentra os termos mais técnicos — revisar para simplificar as definições ou remover os mais obscuros que não aparecem no corpo do capítulo.

## TESTE DE DURABILIDADE
Classificação: ALTA
2 anos: ALTA — hierarquia de camadas, caching, compressão, posicionamento são princípios arquiteturais estáveis
5 anos: ALTA — os conceitos de otimização de contexto sobrevivem mesmo que os provedores mudem as APIs
10 anos: MÉDIA — referências a preços específicos (10% do preço pela Anthropic), a janelas específicas (128k a 2M tokens), e a produtos específicos envelhecem
Justificativa: Este é o capítulo mais durável junto com Cap 7. Os princípios de hierarquização, caching, compressão e instrumentação são invariantes — são engenharia de sistemas, não comportamento de modelo específico.

## TESTE DE DIFERENCIAÇÃO
Classificação: PROPRIEDADE INTELECTUAL
Justificativa: A articulação de context engineering como disciplina distinta de engenharia de prompt, com framework de cinco camadas hierárquicas e critérios de otimização por camada, não existe com este nível de sistematização em nenhum livro de IA em português que conheço. O exemplo da fintech com nota de rigor metodológico eleva credibilidade além dos demais capítulos.

## TESTE DE MEMORIZAÇÃO
Ideia principal clara? SIM
Qual é a ideia principal (em 1 frase): Context engineering não é sobre escrever um prompt melhor — é sobre orquestrar todas as camadas do contexto com hierarquia, caching e instrumentação, o que reduz custo em dezenas de por cento sem trocar modelo.
Justificativa: A frase de fechamento do capítulo ("Prompt engineering é sobre escrever a frase certa. Context engineering é sobre orquestrar tudo.") é a mais precisa do livro. O caso da fintech é o exemplo mais memorável do bloco.

## TESTE DE TRANSFORMAÇÃO
Ao terminar, o leitor consegue fazer o que antes não conseguia:
- Decompor qualquer chamada de LLM nas cinco camadas hierárquicas
- Identificar quais camadas são cacheáveis e configurar caching adequado
- Calcular impacto financeiro de otimizações com estimativa de ordem de magnitude
- Instrumentar tokens por camada em uma aplicação real
- Reconhecer os cinco anti-padrões antes de cometê-los
O leitor NÃO consegue ainda:
- Saber quando nenhuma otimização de contexto resolve (problema não discutido)
- Implementar RAG fusion ou destilação semântica sem referência adicional

## NOTA FINAL (0-10 cada eixo)
Estrutura: 7 | Pedagogia: 9 | Clareza: 8 | Autoridade: 9 | Durabilidade: 9 | Diferenciação: 9 | Memorização: 9 | Transformação: 8
**Nota Geral: 8.5**

## DECISÃO EDITORIAL
MANTER COM AJUSTES

---

## LINHAS-TRACKER

```
CODIGO|ARQUIVO|ACHADO_ID|CATEGORIA|ROI|PROBLEMA_CURTO|CORRECAO_CURTA|DECISAO_CAP
C06|L1-C06-rag.md|01|P1|ALTO|Seção de casos de uso é lista sem critério de decisão|Substituir por framework de 3 critérios para identificar candidatos a RAG|MANTER COM AJUSTES
C06|L1-C06-rag.md|02|P1|ALTO|Ausência de métricas de avaliação de qualidade RAG em produção|Adicionar parágrafo sobre Precision@K, Faithfulness e RAGAS em 6.3.2|MANTER COM AJUSTES
C06|L1-C06-rag.md|03|P0|ALTO|Lista de bancos vetoriais sem critério de escolha viola a tese|Remover lista de nomes; substituir por critérios de seleção duráveis|MANTER COM AJUSTES
C06|L1-C06-rag.md|04|P1|MÉDIO|Percentuais precisos em cenário declarado como ilustrativo|Generalizar números ou adicionar nota metodológica|MANTER COM AJUSTES
C06|L1-C06-rag.md|05|P2|BAIXO|Nome de modelo de embedding específico em cenário ilustrativo|Substituir por descrição funcional sem nome de produto|MANTER COM AJUSTES
C06|L1-C06-rag.md|06|P2|BAIXO|Erro tipográfico sistêmico em autoavaliação (espaço duplo antes do checkbox)|Corrigir espaçamento em todos os capítulos|MANTER COM AJUSTES
C07|L1-C07-memoria.md|07|P1|ALTO|Memória procedural subdesenvolvida; remetida ao Livro 2|Expandir 7.3.4 com dois parágrafos de implementação concreta e sinal de falha|MANTER COM AJUSTES
C07|L1-C07-memoria.md|08|P0|ALTO|Continual learning mencionado sem citar catastrophic forgetting|Adicionar frase sobre o principal obstáculo não resolvido do campo|MANTER COM AJUSTES
C07|L1-C07-memoria.md|09|P1|ALTO|Ausência de discussão sobre privacidade e LGPD em memória episódica|Adicionar caixa ou parágrafo sobre implicações LGPD/GDPR em 7.3.2|MANTER COM AJUSTES
C07|L1-C07-memoria.md|10|P1|MÉDIO|Consolidação definida de forma abstrata sem implementação mínima|Adicionar parágrafo de implementação prática com mecanismo de chamada ao LLM|MANTER COM AJUSTES
C07|L1-C07-memoria.md|11|P2|BAIXO|URL de referência Anthropic Memory é volátil|Substituir por referência estável à documentação geral|MANTER COM AJUSTES
C08|L1-C08-fine-tuning.md|12|P1|ALTO|Ausência de discussão sobre overfitting em fine-tuning|Adicionar parágrafo sobre overfitting com sinal de detecção e mitigações|MANTER COM AJUSTES
C08|L1-C08-fine-tuning.md|13|P1|ALTO|Hierarquia das soluções não define critério para saber quando subir degrau|Adicionar parágrafo de critério de avaliação baseado em experimento antes de 8.4|MANTER COM AJUSTES
C08|L1-C08-fine-tuning.md|14|P0|ALTO|Custos em dólares específicos demais para serem duráveis; amplos demais para serem úteis|Substituir valores fixos por drivers de custo e referência a calculadoras de provedores|MANTER COM AJUSTES
C08|L1-C08-fine-tuning.md|15|P2|BAIXO|Definição implícita de modelo grande datada pela evolução do campo|Substituir por terminologia estável: modelo frontier comercial|MANTER COM AJUSTES
C08|L1-C08-fine-tuning.md|16|P2|BAIXO|URL específica de documentação Anthropic volátil nas referências|Remover URL específica; manter referência geral|MANTER COM AJUSTES
C09|L1-C09-engenharia-prompt.md|17|P0|ALTO|Referência a awesome-prompts GitHub contradiz tese do livro|Remover referência; substituir por recurso de governança de prompts|REVISAR PARCIALMENTE
C09|L1-C09-engenharia-prompt.md|18|P0|ALTO|Seção 9.4 é lista de técnicas sem framework de decisão — padrão de coleção de receitas|Reorganizar por categoria de problema com critério de quando aplicar cada técnica|REVISAR PARCIALMENTE
C09|L1-C09-engenharia-prompt.md|19|P1|MÉDIO|Ausência de distinção entre prompts conversacionais e de pipeline automatizado|Adicionar parágrafo de diferenciação em 9.1 ou 9.3|REVISAR PARCIALMENTE
C09|L1-C09-engenharia-prompt.md|20|P1|MÉDIO|Nomes de modelos específicos (GPT-5) em afirmação sobre comportamento de zero-shot|Substituir por classificação funcional: modelos de alta capacidade|REVISAR PARCIALMENTE
C09|L1-C09-engenharia-prompt.md|21|P1|MÉDIO|Afirmação sobre resistência de modelos a papel manipulador sem nuance de segurança|Adicionar qualificador sobre prompt injection em sistemas em produção|REVISAR PARCIALMENTE
C09|L1-C09-engenharia-prompt.md|22|P2|BAIXO|Anthropic Prompt Library borderline com coleção de prompts|Recontextualizar explicitamente como exemplo de estrutura, não de cópia|REVISAR PARCIALMENTE
C09|L1-C09-engenharia-prompt.md|23|P2|BAIXO|Inconsistência de moeda entre capítulos (reais em C09; dólares em C08)|Padronizar moeda em todo o livro (dólares recomendado)|REVISAR PARCIALMENTE
C10|L1-C10-chain-of-thought.md|24|P1|MÉDIO|30 a 60 pontos percentuais de melhoria citado sem fonte específica|Citar Wei et al. 2022 com contexto de benchmark específico ou generalizar|MANTER COM AJUSTES
C10|L1-C10-chain-of-thought.md|25|P1|MÉDIO|Nomes de modelos específicos (Claude Sonnet, GPT-5, Gemini 3) em 10.3.1|Substituir por modelos frontier modernos ou modelos de alta capacidade|MANTER COM AJUSTES
C10|L1-C10-chain-of-thought.md|26|P1|ALTO|Cinco variantes de CoT sem critério de quando usar cada uma|Adicionar tabela de decisão ou árvore com critérios por tipo de problema|MANTER COM AJUSTES
C10|L1-C10-chain-of-thought.md|27|P2|MÉDIO|Ausência de discussão sobre CoT e latência em aplicações com SLA apertado|Adicionar parágrafo sobre trade-off latência/qualidade em 10.3.2 ou 10.5|MANTER COM AJUSTES
C11|L1-C11-context-engineering.md|28|P0|ALTO|Glossário duplicado entre seções 11.2 e 11.3 com termos parcialmente sobrepostos|Unificar em único glossário antes de 11.3.1; remover o de 11.2|MANTER COM AJUSTES
C11|L1-C11-context-engineering.md|29|P1|ALTO|40-70% de desperdício generalizado sem base metodológica além do caso da fintech|Qualificar a afirmação com condicional explícito de aplicações sem otimização prévia|MANTER COM AJUSTES
C11|L1-C11-context-engineering.md|30|P1|MÉDIO|Janela efetiva menor que nominal mencionada no glossário sem desenvolvimento no corpo|Expandir em 11.3.4 com implicação prática para decisão de posicionamento|MANTER COM AJUSTES
C11|L1-C11-context-engineering.md|31|P1|MÉDIO|Ausência de discussão sobre quando context engineering não é suficiente|Adicionar sexto anti-padrão em 11.5: problema é o modelo, não o contexto|MANTER COM AJUSTES
C11|L1-C11-context-engineering.md|32|P2|BAIXO|Referência a threads de X/Twitter de Karpathy não é estável|Substituir por referência a blog post ou remover|MANTER COM AJUSTES
C11|L1-C11-context-engineering.md|33|P2|BAIXO|Afirmação de 30 minutos de configuração de prompt caching é arriscada|Substituir por afirmação qualificada sobre complexidade variável|MANTER COM AJUSTES
```

---

# BANCA EDITORIAL ADVERSARIAL — Capítulos 12, 13, 14, 14B, 14C
# Livro: INTELIGÊNCIA AUMENTADA
# Tese central: "Modelos passam. Método fica."

---

# C12 — L1-C12-agentes.md

## RESUMO EXECUTIVO
Nota: 7/10
Veredito: B

## O QUE FUNCIONA
- A distinção chatbot → assistente com tools → agente → multiagente em quatro níveis (12.3.2) é pedagogicamente precisa e praticamente útil: dá ao leitor um mapa imediato para classificar o que vê no mercado.
- A analogia do estagiário vs. assistente executivo (12.2) é memorável, citável e ancorada no que realmente diferencia as categorias: transferência de responsabilidade de execução. Essa formulação é forte.
- O caso da consultoria de M&A (12.4) é o ponto mais alto do capítulo: concreto, com números plausíveis, com lição que vai além do ROI imediato ("liberou o consultor para fazer trabalho de consultor").
- As cinco decisões arquiteturais (12.5) são genuinamente úteis para quem vai construir agentes e não figuram com essa clareza na maioria da literatura de IA disponível.
- O loop perceber-planejar-agir-observar-refletir (12.3.1) é bem estruturado e serve de ancoragem para o restante do capítulo.

## O QUE NÃO FUNCIONA
- O capítulo não testa sua própria tese: "Modelos passam. Método fica." O loop fundamental e a hierarquia de autonomia são robustos, mas nomes de produtos são citados livremente (Claude Code, AutoGen, CrewAI, LangGraph) sem qualquer alerta sobre efemeridade. Isso é inconsistência interna grave.
- A seção de sistemas multiagente (12.6) é superficial demais: quatro padrões em dois parágrafos cada, sem exemplo concreto nem critério de escolha entre eles. Contrasta com a profundidade das decisões arquiteturais de 12.5.
- O critic/camada de guardas (12.3.3) é listado como "não opcional em domínios sensíveis" mas não há nenhum exemplo concreto de como implementar, nem referência cruzada com o capítulo de segurança. É a decisão mais importante de governança em agentes e recebe o menor desenvolvimento proporcional.
- A nota ROI "5x a 15x em processos analíticos estruturados" (bloco "Para Executivos", 12.4) não tem sustentação apresentada. É afirmação de marketing, não de autoridade técnica.
- O exercício 3 (esboço de critério de sucesso) pede algo de alta dificuldade sem scaffolding: "escreva o critério explícito de sucesso da tarefa" é uma das cinco decisões mais difíceis em agentes (conforme 12.5), mas o exercício não orienta como começar nem oferece exemplo.
- Checklist item 5 diverge do texto: lista "quatro padrões principais" mas o resumo executivo em 12.8 lista igualmente quatro; o texto de 12.6 descreve quatro, mas o checklist do capítulo diz "quatro padrões principais de sistemas multiagente" — está correto, mas cria dúvida ao leitor sobre o número real ao longo do texto.

## ACHADOS

### ACHADO 01
Categoria: P0
Problema: Nomes de produtos como fonte de evidência sem proteção de durabilidade
Por que é um problema: Claude Code (nível 3), AutoGen (nível 4), LangGraph, CrewAI como exemplos de categoria em 2026 comprometem a afirmação "Modelos passam. Método fica." O loop e a hierarquia são invariantes; os produtos que os exemplificam não são.
Impacto no leitor: O leitor que comprar o livro em dois anos vai encontrar exemplos desatualizados no capítulo conceitual, corroendo a credibilidade de toda a taxonomia.
Correção exata: Isolar referências de produto em nota de rodapé com tag "Apêndice J" (como 14B já faz), deixar o corpo do texto com exemplos funcionais ("agentes de pesquisa profunda", "agentes de codificação") sem nome de produto.
Texto sugerido: "No nível 3 estão os agentes propriamente ditos — agentes de pesquisa profunda, agentes de codificação, agentes de browser, cada um executando o loop perceber-agir-refletir até cumprir o objetivo. [Nota: exemplos de produtos correntes no Apêndice J.]"
ROI: ALTO

### ACHADO 02
Categoria: P0
Problema: ROI de 5x a 15x sem fonte ou metodologia apresentadas
Por que é um problema: A tese do livro é de autoridade e julgamento, não de número. Um número de ROI genérico sem sustentação (fonte, metodologia, intervalos) é promessa de vendedor, não avaliação de profissional.
Impacto no leitor: Executivo que testa e obtém 2x vai questionar a credibilidade do livro inteiro. Executivo que obtém 20x vai achar o número conservador demais — e igualmente não saberá o que fazer com ele.
Correção exata: Remover o número ou ancorar com "em revisões pós-implementação reportadas por [referência]" e faixa de confiança. Alternativa: transformar em pergunta orientadora ("O ROI típico fica entre 5x e 15x em processos analíticos, mas o que determina onde você cai nessa faixa?").
Texto sugerido: "O ROI em agentes de análise estruturada varia amplamente — os fatores que determinam onde você cai nessa faixa são o redesenho do processo em torno do agente e a qualidade da validação humana nos pontos críticos. Sem os dois, o número desce; com os dois, sobe além do que a maioria dos gestores espera antes do piloto."
ROI: ALTO

### ACHADO 03
Categoria: P1
Problema: Seção de sistemas multiagente (12.6) é superficial comparada ao restante do capítulo
Por que é um problema: Os quatro padrões (orquestrador, debate, pipeline, swarm) são apresentados sem critério de escolha. "Útil em" não é critério — é preferência. Um leitor que precisa escolher entre pipeline e orquestrador sai do capítulo sem ferramenta.
Impacto no leitor: Incapaz de aplicar o conhecimento ao seu contexto. Exercício 4 (mapeamento de risco) não compensa a ausência de critério de escolha de padrão.
Correção exata: Adicionar uma tabela ou heurística de escolha: "quando o fluxo é linear e bem definido → pipeline; quando há especialização paralela → orquestrador; quando o problema admite múltiplas abordagens válidas → swarm; quando a decisão tem trade-offs genuinamente complexos e latência é tolerável → debate."
Texto sugerido: n/a (requer adição, não substituição)
ROI: MÉDIO

### ACHADO 04
Categoria: P1
Problema: O critic/camada de guardas é apresentado como componente crítico mas recebe zero profundidade
Por que é um problema: "Em domínios sensíveis, esse componente não é opcional, é estrutural" — mas não há um exemplo, não há referência ao capítulo de segurança, não há indicação de como implementar nem de quando ele falha. É o componente de governança mais importante de um agente e é o menos desenvolvido.
Impacto no leitor: O leitor sai sem saber como construir salvaguardas reais. A referência ao Capítulo 19 em 12.7 não é suficiente — o leitor precisa de âncora conceitual aqui.
Correção exata: Adicionar parágrafo mínimo com exemplo concreto: "Um critic em domínio financeiro pode ser tão simples quanto uma lista de ações proibidas que o agente verifica antes de executar (delete, transfer, publish) ou tão sofisticado quanto um segundo LLM que avalia o plano de ação contra uma política explícita antes de autorizar."
Texto sugerido: n/a (adição)
ROI: MÉDIO

### ACHADO 05
Categoria: P1
Problema: O exercício de construção de agente (12.12) cita frameworks por nome sem avisar sobre efemeridade
Por que é um problema: "Use Claude com function calling, ou frameworks como LangGraph, CrewAI ou AutoGen" — em dois anos esses frameworks podem não ser os dominantes. O projeto do capítulo vai envelhece junto com os nomes.
Impacto no leitor: Leitor de 2028 vai entrar num link quebrado e achar que o livro ficou obsoleto.
Correção exata: Reformular para "use o agente de codificação e os frameworks de orquestração disponíveis no seu contexto [ver Apêndice J para opções correntes]".
Texto sugerido: "Use o modelo de IA e o framework de orquestração que sua organização já opera — ou os que constam no Apêndice J para a data de leitura. O que importa não é a ferramenta, é executar o ciclo completo de definição de objetivo, tools e critério de parada com casos reais."
ROI: MÉDIO

### ACHADO 06
Categoria: P2
Problema: Typo: espaço duplo antes do asterisco em 12.14 item 5 "Curiosidade **"
Por que é um problema: Inconsistência tipográfica que aparece também nos demais capítulos — padrão do template tem espaço extra antes do fechamento do bold.
Impacto no leitor: Não compromete compreensão, mas indica falta de revisão final.
Correção exata: Remover espaço extra em "Curiosidade **" → "**Curiosidade**".
Texto sugerido: "| 5 | **Curiosidade** — Está com vontade de entender o padrão MCP que está mudando como tools são integradas em sistemas de IA modernos | ☐ |"
ROI: BAIXO

## TESTE DA JOANA
Entenderia: SIM (geral)
O que ela entenderia: A diferença entre chatbot e agente, o loop fundamental, a analogia do estagiário vs. assistente executivo, o caso da consultoria.
O que ela NÃO entenderia: O que exatamente é um "critic" e por que importa. A diferença prática entre os quatro padrões multiagente. O que fazer com o exercício 3 (critério de sucesso) sem scaffolding.
Como corrigir: Expandir critic com um exemplo concreto de lista de bloqueio. Adicionar tabela de escolha de padrão. Dar template mínimo no exercício 3.

## TESTE DE DURABILIDADE
Classificação: MÉDIA
2 anos: Loop e hierarquia sobrevivem. Nomes de produtos (Claude Code, AutoGen, LangGraph) ficam desatualizados.
5 anos: A taxonomia de níveis pode precisar de revisão se surgirem categorias novas. Os princípios de decisão arquitetural de 12.5 sobrevivem.
10 anos: O loop fundamental e a transferência de responsabilidade de execução são invariantes. A hierarquia pode precisar de expansão mas o princípio permanece.
Justificativa: O capítulo tem núcleo durável forte, mas está contaminado por referências a produtos que vão envelhece nos próximos dois anos. A correção é simples e de alto ROI.

## TESTE DE DIFERENCIAÇÃO
Classificação: DIFERENCIADO
Justificativa: A formulação "transferência de responsabilidade de execução" como diferença central entre chatbot e agente não é como a maioria dos textos framing o problema. A taxonomia de quatro níveis é clara e útil. O caso da consultoria tem especificidade que poucos livros de IA atingem. Onde perde diferenciação: a seção multiagente está em nível commodity.

## TESTE DE MEMORIZAÇÃO
Ideia principal clara? SIM
Qual é a ideia principal: "Chatbots respondem perguntas. Agentes cumprem objetivos. A diferença é quem carrega a responsabilidade de execução."
Justificativa: A epígrafe de abertura e o parágrafo final repetem a tese. A analogia do estagiário ancora a memória. O loop tem nome e fases claras.

## TESTE DE TRANSFORMAÇÃO
Ao terminar, o leitor consegue fazer o que antes não conseguia:
- Classificar corretamente uma aplicação de IA em um dos quatro níveis de autonomia
- Explicar para um diretor não-técnico a diferença entre chatbot e agente usando a analogia do estagiário/assistente executivo
- Nomear as cinco decisões arquiteturais críticas em construção de agentes
- Identificar candidatos a agente na própria organização com argumento de ROI

O que o leitor ainda não consegue fazer (lacuna):
- Escolher entre padrões multiagente com critério defensável
- Implementar um critic funcional
- Estimar custo e latência de um agente antes de construir

## NOTA FINAL
Estrutura: 8 | Pedagogia: 7 | Clareza: 8 | Autoridade: 6 | Durabilidade: 6 | Diferenciação: 7 | Memorização: 8 | Transformação: 7
**Nota Geral: 7.1**

## DECISÃO EDITORIAL
MANTER COM AJUSTES

---

## LINHAS-TRACKER

C12|L1-C12-agentes.md|01|P0|ALTO|Nomes de produto como evidência de categoria sem proteção de durabilidade|Isolar referências em Apêndice J; usar descritores funcionais no corpo|MANTER COM AJUSTES
C12|L1-C12-agentes.md|02|P0|ALTO|ROI 5x–15x sem fonte ou metodologia apresentadas|Remover número ou ancorar em fonte; transformar em pergunta orientadora|MANTER COM AJUSTES
C12|L1-C12-agentes.md|03|P1|MÉDIO|Seção multiagente superficial sem critério de escolha entre padrões|Adicionar tabela ou heurística: quando usar cada padrão|MANTER COM AJUSTES
C12|L1-C12-agentes.md|04|P1|MÉDIO|Critic/camada de guardas sem profundidade nem exemplo de implementação|Adicionar parágrafo com exemplo concreto de critic funcional|MANTER COM AJUSTES
C12|L1-C12-agentes.md|05|P1|MÉDIO|Projeto do capítulo cita frameworks por nome sem avisar sobre efemeridade|Reformular para "framework disponível no seu contexto [ver Apêndice J]"|MANTER COM AJUSTES
C12|L1-C12-agentes.md|06|P2|BAIXO|Typo: espaço duplo antes do fechamento de bold em item 5 de Autoavaliação|Remover espaço extra|MANTER COM AJUSTES

---

---

# C13 — L1-C13-mcp.md

## RESUMO EXECUTIVO
Nota: 6/10
Veredito: C

## O QUE FUNCIONA
- A formulação do problema M×N → M+N (13.1) é matematicamente elegante e pedagogicamente eficaz. É a melhor descrição estrutural do valor do MCP disponível em linguagem acessível.
- A analogia do USB-C (13.2) é memorável e precisa no ponto que importa: padronização de primitivas, não apenas de conector.
- A seção 13.2.5 é um ponto forte inesperado: a tabela comparativa MCP × gRPC × REST × Webhooks × Event-driven é genuinamente útil para quem toma decisões arquiteturais. É conteúdo de propriedade intelectual real.
- Os quatro eixos de decisão em produção (13.2.6) — latência, schema, segurança, composição em camadas — são o melhor conteúdo do capítulo e dificilmente existem com essa estrutura em outros livros.
- A seção de riscos (13.6) é honesta e específica, com quatro riscos nomeados e distintos, não genéricos.
- A lição estrutural do caso da telecom — "investimento em padronização como ativo reutilizável" — é genuinamente mais durável que o MCP em si.

## O QUE NÃO FUNCIONA
- O capítulo inteiro é sobre um protocolo de fornecedor lançado há dois anos. A tese "Modelos passam. Método fica." está em tensão estrutural permanente com um capítulo dedicado ao MCP. A Anthropic lançou o protocolo; se amanhã a OpenAI ou a Google definirem um padrão diferente com adoção maior, o capítulo envelhece com o MCP.
- O bloco "Para Executivos" de 13.4 diz "MCP deve ser a hipótese padrão" para novas integrações em 2026. Isso é afirmação de produto, não de método. Viola diretamente a tese do livro.
- A numeração de seções está quebrada: vai de 13.2 para 13.2.5, pulando 13.2.1 a 13.2.4. A analogia do USB-C termina em 13.2 e a próxima seção é 13.2.5. A estrutura de numeração sugere que conteúdo foi inserido sem renumeração, ou que há seções ausentes.
- A afirmação "em três anos ninguém vai lembrar de como funcionava antes" (epígrafe final) é exactamente o tipo de afirmação que envelhece mal se o MCP for substituído — e é a última palavra do capítulo.
- O caso da telecom tem elementos que erram na especificidade que o próprio livro pede de seus casos: "R$ 800 mil para entrega completa" é número preciso demais para um cenário composto. Ou é real (e precisa ser referenciado) ou deve ser removido.
- As primitivas Resources/Tools/Prompts são apresentadas sem exemplo de implementação mínimo. O leitor entende o conceito mas não consegue visualizar como um servidor MCP real expõe um Resource.

## ACHADOS

### ACHADO 01
Categoria: P0
Problema: Capítulo inteiro como endosso de protocolo de fornecedor viola a tese "Modelos passam. Método fica."
Por que é um problema: O MCP é protocolo lançado pela Anthropic em novembro de 2024. O capítulo defende ativamente sua adoção como "hipótese padrão" para novas integrações. Se o MCP for substituído por outro padrão (aberto ou não) nos próximos dois a três anos, o capítulo inteiro vira publicidade de produto desatualizado.
Impacto no leitor: Leitor de 2028 que lê "em três anos ninguém vai lembrar de como funcionava antes" e está vivendo em mundo pós-MCP vai perder a confiança no julgamento editorial do livro.
Correção exata: Reformular o capítulo para ensinar o MÉTODO (padrões de integração, problema M×N, primitivas de ferramentas para IA) usando o MCP como exemplo corrente — não como a resposta. O título poderia ser "Padrões de Integração para Agentes" com MCP como caso de estudo de 2024-2026.
Texto sugerido: (requer reformulação estrutural do capítulo — não redutível a uma substituição de parágrafo)
ROI: ALTO

### ACHADO 02
Categoria: P0
Problema: Bloco "Para Executivos" em 13.4 endossa MCP como "hipótese padrão" sem qualificação temporal ou competitiva
Por que é um problema: "MCP deve ser a hipótese padrão" é recomendação operacional de produto, não princípio de julgamento. Um livro que ensina avaliação e tomada de decisão não pode emitir recomendações de produto sem critério explícito e sem prazo de validade.
Impacto no leitor: Executivo que adota MCP baseado nessa frase e em dois anos descobre que a indústria migrou para outro padrão vai questionar a qualidade do julgamento do livro.
Correção exata: Substituir por critério de decisão: "Quando o problema é integração plural de sistemas com necessidade de descoberta dinâmica e expectativa de troca de provedor de LLM, padrões abertos de integração entregam retorno composto. Em 2026, o MCP é o candidato mais adotado para essa função. Avalie o ecossistema antes de comprometer."
Texto sugerido: "Se sua organização está planejando integrações de IA com múltiplos sistemas, o critério decisivo é: você precisa de descoberta dinâmica e quer flexibilidade para trocar de provedor de LLM? Se sim, invista em padrão aberto de integração. O que conta como padrão dominante na data de leitura está no Apêndice J."
ROI: ALTO

### ACHADO 03
Categoria: P0
Problema: Epígrafe final ("em três anos ninguém vai lembrar de como funcionava antes") é profecia de produto, não de método
Por que é um problema: A epígrafe final é a última impressão do capítulo. É a afirmação com maior risco de envelhecer mal de todo o livro. Se o MCP for substituído antes desse prazo, a frase vira evidência de má avaliação editorial.
Impacto no leitor: Pode ser citada ironicamente em reviews negativos se o MCP não sobreviver.
Correção exata: Substituir por epígrafe sobre o princípio — a necessidade de padrão intermediário em M×N —, não sobre o produto.
Texto sugerido: "O custo de integrar cada cliente com cada ferramenta sem padrão comum não escala. A história do software diz que em algum momento um padrão vence. O profissional que entende por que padrões emergem está sempre um passo à frente do que aprende apenas qual padrão está em uso hoje."
ROI: ALTO

### ACHADO 04
Categoria: P1
Problema: Numeração de seções quebrada: 13.2 → 13.2.5, pulando 13.2.1 a 13.2.4
Por que é um problema: Sinaliza conteúdo inserido sem revisão estrutural. Pode indicar seções 13.2.1–13.2.4 planejadas mas ausentes, ou inserção de bloco 13.2.5 sem renumeração.
Impacto no leitor: Desorientação de navegação. Leitor que procura 13.2.1 no sumário não vai encontrar.
Correção exata: Renumerar: a analogia USB-C vira 13.2; a seção de comparação de protocolos vira 13.3 (deslocando as seguintes); ou a analogia USB-C ganha subseções 13.2.1 e 13.2.2 e os blocos 13.2.5, 13.2.6, 13.2.7 são renumerados como 13.2.3, 13.2.4, 13.2.5.
Texto sugerido: n/a (renumeração estrutural)
ROI: MÉDIO

### ACHADO 05
Categoria: P1
Problema: Número preciso de R$ 800 mil em cenário composto sem fonte identificada
Por que é um problema: O capítulo avisa que o cenário é "ilustrativo, composto a partir de casos recorrentes", mas usa um número tão específico (R$ 800 mil) que soa como dado real. Isso cria problema de credibilidade: ou o número é real e precisa de fonte, ou é arbitrário e precisa ser tornado menos específico.
Impacto no leitor: Um leitor técnico vai questionar de onde vem o número. Um leitor de negócios vai tomá-lo como dado e tentar reproduzir o benchmark — e não vai conseguir.
Correção exata: Substituir por ordem de grandeza: "orçado em dezenas a centenas de milhares de reais para entrega completa" ou remover o número e focar no argumento estrutural (8 a 12 semanas de desenvolvimento, não o custo).
Texto sugerido: "A primeira estimativa calculou que construir integrações custom para os doze sistemas relevantes levaria entre oito e doze semanas de desenvolvimento — esforço que, a valores de mercado em 2025, representava dezenas de milhares de reais apenas na fase inicial, sem contar manutenção contínua."
ROI: MÉDIO

### ACHADO 06
Categoria: P1
Problema: Primitivas Resources/Tools/Prompts apresentadas sem exemplo mínimo concreto de implementação
Por que é um problema: O leitor técnico que vai implementar um servidor MCP precisa de âncora concreta. "Resources são dados consultáveis pelo modelo" é definição, não exemplo. O fluxo em 13.3.3 descreve o processo, mas sem mostrar como um Resource específico é declarado.
Impacto no leitor: O exercício 3 (esboço de servidor próprio) fica suspenso no ar: o leitor sabe o que declarar, mas não sabe como.
Correção exata: Adicionar exemplo mínimo em pseudocódigo ou YAML mostrando como um Resource e uma Tool são declarados em um servidor MCP: nome, descrição, schema de entrada/saída. Não precisa ser código completo — só o suficiente para fixar a forma.
Texto sugerido: n/a (adição de bloco de código mínimo)
ROI: MÉDIO

### ACHADO 07
Categoria: P1
Problema: Afirmação sobre "servidores oficiais mantidos pela Anthropic para GitHub, Google Drive, Slack" potencialmente incorreta ou datada
Por que é um problema: A afirmação de que "a Anthropic mantém [servidores oficiais] para GitHub, Google Drive, Slack" precisa ser verificada quanto à atualidade. Servidores de referência podem ter mudado de mantenedor entre a escrita e a publicação. Isso é exatamente o tipo de detalhe que envelhece silenciosamente.
Impacto no leitor: Leitor que vai ao GitHub da Anthropic e não encontra os servidores listados perde confiança na autoridade técnica do texto.
Correção exata: Substituir lista específica por "servidores de referência mantidos pela comunidade e pela Anthropic [ver repositório oficial em Apêndice J]" ou verificar e datar explicitamente: "[conforme repositório oficial em janeiro de 2026]".
Texto sugerido: "Os servidores oficiais — mantidos pelos próprios fornecedores ou pela Anthropic como referência — cobrem sistemas populares como GitHub, ferramentas de produtividade e bancos de dados [lista corrente no repositório oficial, Apêndice J]."
ROI: MÉDIO

### ACHADO 08
Categoria: P2
Problema: Typo em 13.14 item 5: "Curiosidade **" com espaço extra (padrão repetido de C12)
Por que é um problema: Inconsistência tipográfica de template.
Impacto no leitor: Mínimo, mas indica ausência de revisão final sistemática.
Correção exata: Remover espaço extra.
Texto sugerido: "| 5 | **Curiosidade** — Está com vontade de aprender como sistemas reais de IA são construídos, mantidos e governados em produção corporativa | ☐ |"
ROI: BAIXO

## TESTE DA JOANA
Entenderia: SIM (geral, com reservas)
O que ela entenderia: O problema M×N, a analogia do USB-C, o caso da telecom e a lição sobre investimento em padronização, os quatro riscos principais.
O que ela NÃO entenderia: A tabela comparativa MCP × gRPC × REST (vocabulário técnico denso em 13.2.5), os quatro eixos de decisão de produção (latência em milissegundos, mTLS, codegen), a diferença entre stdio e SSE.
Como corrigir: Mover a tabela e os quatro eixos para uma caixa "Para o arquiteto técnico" e adicionar parágrafo de transição para executivos ao final de 13.2.5: "Se você é executivo: o que importa é que cada protocolo serve a um tipo diferente de problema, e MCP serve ao problema específico de múltiplas ferramentas com descoberta dinâmica."

## TESTE DE DURABILIDADE
Classificação: BAIXA
2 anos: As primitivas Resources/Tools/Prompts e o problema M×N sobrevivem. O posicionamento de MCP como "hipótese padrão" já pode estar obsoleto.
5 anos: O MCP como tecnologia específica pode estar substituído. O princípio do padrão intermediário M→M+N sobrevive.
10 anos: Apenas o princípio estrutural (padrões emergem em fragmentação) e as primitivas conceituais (dados, ações, templates) sobrevivem com certeza.
Justificativa: Este é o capítulo com maior risco de durabilidade de todo o bloco revisado. A solução é reformular para ensinar o princípio usando o MCP como caso de estudo datado, em vez de ensinar o MCP como a resposta.

## TESTE DE DIFERENCIAÇÃO
Classificação: DIFERENCIADO (na seção técnica) / COMMODITY (na narrativa principal)
Justificativa: A tabela comparativa de protocolos (13.2.5) e os quatro eixos de decisão (13.2.6) são propriedade intelectual real, não encontrada com essa estrutura em outros livros. A narrativa principal (MCP é o USB-C da IA) está disponível em dezenas de posts de blog de 2024-2025. O capítulo oscila entre commodity e diferenciado dependendo de qual seção se está lendo.

## TESTE DE MEMORIZAÇÃO
Ideia principal clara? SIM
Qual é a ideia principal: "O problema M×N de integrações vira M+N com um padrão intermediário. O MCP é o padrão que a indústria está adotando para isso em IA."
Justificativa: A formulação M×N → M+N é memorável e citável. O problema: se amanhã o padrão mudar, a ideia principal do capítulo muda junto, porque está acoplada ao produto.

## TESTE DE TRANSFORMAÇÃO
Ao terminar, o leitor consegue fazer o que antes não conseguia:
- Explicar o problema M×N e por que padrões intermediários emergem
- Distinguir Resources, Tools e Prompts como primitivas de integração para IA
- Comparar MCP com REST, gRPC e Webhooks com critério estrutural (não apenas preferência)
- Identificar os quatro riscos principais de MCP em produção
- Defender ou questionar a adoção de MCP em reunião arquitetural com argumentos técnicos reais

O que o leitor ainda não consegue fazer:
- Implementar um servidor MCP mínimo (falta exemplo de código)
- Avaliar quando MCP específico vai envelhecer e precisar de revisão

## NOTA FINAL
Estrutura: 6 | Pedagogia: 7 | Clareza: 6 | Autoridade: 6 | Durabilidade: 4 | Diferenciação: 7 | Memorização: 7 | Transformação: 7
**Nota Geral: 6.3**

## DECISÃO EDITORIAL
REVISAR PARCIALMENTE

---

## LINHAS-TRACKER

C13|L1-C13-mcp.md|01|P0|ALTO|Capítulo inteiro endossa protocolo de fornecedor contrariando tese "Modelos passam. Método fica."|Reformular: MCP como caso de estudo; ensinar princípio M×N e primitivas de integração|REVISAR PARCIALMENTE
C13|L1-C13-mcp.md|02|P0|ALTO|Bloco Para Executivos recomenda MCP como "hipótese padrão" sem critério ou prazo de validade|Substituir por critério de decisão baseado em problema, não em produto|REVISAR PARCIALMENTE
C13|L1-C13-mcp.md|03|P0|ALTO|Epígrafe final é profecia de produto com alto risco de envelhecimento|Substituir por epígrafe sobre o princípio do padrão intermediário|REVISAR PARCIALMENTE
C13|L1-C13-mcp.md|04|P1|MÉDIO|Numeração de seções quebrada: 13.2 → 13.2.5 sem 13.2.1–13.2.4|Renumerar seções com revisão estrutural|REVISAR PARCIALMENTE
C13|L1-C13-mcp.md|05|P1|MÉDIO|Número preciso de R$ 800 mil em cenário composto sem fonte|Substituir por ordem de grandeza ou datar explicitamente|REVISAR PARCIALMENTE
C13|L1-C13-mcp.md|06|P1|MÉDIO|Primitivas sem exemplo mínimo concreto de declaração em servidor MCP|Adicionar bloco de pseudocódigo mínimo mostrando declaração de Resource e Tool|REVISAR PARCIALMENTE
C13|L1-C13-mcp.md|07|P1|MÉDIO|Lista de servidores oficiais mantidos pela Anthropic potencialmente datada|Substituir por referência ao repositório oficial no Apêndice J|REVISAR PARCIALMENTE
C13|L1-C13-mcp.md|08|P2|BAIXO|Typo: espaço duplo antes do fechamento de bold em item 5 de Autoavaliação|Remover espaço extra|REVISAR PARCIALMENTE

---

---

# C14 — L1-C14-ai-engineering.md

## RESUMO EXECUTIVO
Nota: 8/10
Veredito: A

## O QUE FUNCIONA
- A distinção entre AI Engineering, Data Science e ML Engineering (14.1) é clara, justa e necessária. Poucos livros definem o campo com essa precisão sem cair em marketing de profissão.
- A analogia do engenheiro de pontes × engenheiro de prédios (14.2) é precisa no que importa: mesma base, material de trabalho diferente o suficiente para exigir especialização. Funciona melhor que "novo tipo de engenheiro" genérico.
- O caso da seguradora (14.4) é o melhor caso do bloco revisado: tem causalidade clara (três fontes simultâneas de drift), tem resolução específica (três frentes coordenadas), tem lição cultural que vai além do técnico ("aplicações de IA sem observabilidade não estão em produção, estão em risco operacional latente"). A nota de rigor estatístico ao final é exemplo de como outros casos deveriam ser documentados.
- A stack de sete camadas (14.3.1) é genuinamente útil como checklist de maturidade organizacional. O glossário no início de 14.3 é decisão pedagógica correta.
- Os cinco princípios de LLMOps (14.5) são concretos e acionáveis, em contraste com LLMOps genérico de outros textos.
- A epígrafe final ("sem observabilidade não estão em produção, estão em risco operacional latente") é a melhor do bloco — precisa, memorável, ancorada no caso.

## O QUE NÃO FUNCIONA
- A seção 14.6 (perfil da nova profissão) lista ferramentas por nome (LangSmith, Helicone, Phoenix, LangGraph, CrewAI) sem qualificação de durabilidade. Contrasta negativamente com a disciplina do restante do capítulo.
- O lifecycle (14.3.2) tem a fase "medir e avaliar" separada da fase "observação", mas a fronteira entre as duas não é clara. O que é observar e o que é medir? Um leitor não-técnico vai confundir.
- A afirmação "demanda cresce mais rápido que a oferta em 2026, com salários comparáveis a engenheiros sêniors de plataforma" (14.6) é factualmente frágil: não tem fonte, vai envelhece, e não é o tipo de conteúdo que pertence a um livro de método.
- A seção de avaliação (14.3.3) menciona "LangSmith, Helicone, Phoenix Arize, Langfuse, e Datadog com integração IA" por nome — mesma fragilidade de durabilidade que os outros capítulos.
- O glossário inclui "Sandbox de evals" e "Self-consistency" mas estes não aparecem no texto principal com desenvolvimento suficiente. Self-consistency especialmente: é definido no glossário e não aparece mais.

## ACHADOS

### ACHADO 01
Categoria: P1
Problema: Seção de perfil profissional (14.6) lista ferramentas por nome sem qualificação de efemeridade
Por que é um problema: "Fluência em pelo menos uma stack de orquestração e observabilidade, como LangChain, LangGraph, CrewAI, com ferramentas como LangSmith, Helicone, Phoenix" — o mercado de observabilidade de LLMs é o que muda mais rápido em todo o ecossistema de IA. Em dois anos essa lista pode estar parcialmente obsoleta.
Impacto no leitor: Leitor de 2027 vai ler a lista e perceber que metade das ferramentas mudou — e isso vai minar a credibilidade do perfil profissional como um todo.
Correção exata: Substituir por categoria de competência, com nota de Apêndice J para ferramentas correntes. "Fluência em pelo menos uma stack de orquestração de agentes e pelo menos uma ferramenta de observabilidade de LLMs [ver Apêndice J para opções correntes]."
Texto sugerido: "Fluência em pelo menos uma stack de orquestração — frameworks de grafos ou pipelines de agentes disponíveis no contexto — e em pelo menos uma plataforma de observabilidade específica para LLMs [ver Apêndice J para as opções correntes em observabilidade e evals]."
ROI: MÉDIO

### ACHADO 02
Categoria: P1
Problema: Fronteira entre fase "observação" e fase "medir e avaliar" no lifecycle (14.3.2) não está clara
Por que é um problema: O lifecycle lista sete fases, mas a distinção entre "observar" (fase 5) e "medir e avaliar" (fase 6) é fraca. Observar não é medir? O diagrama vai ser a única salvação e pode não ser suficiente.
Impacto no leitor: A Joana — e muitos não-técnicos — vai tratar as duas como uma só fase e perder a distinção que importa (observar = coletar dados; medir = interpretar contra baseline e detectar drift).
Correção exata: Clarificar a distinção explicitamente no texto: "Observar é acumular dados em runtime. Medir e avaliar é interpretar esses dados contra baseline e detectar divergência — um processo ativo que exige decisão, não apenas coleta."
Texto sugerido: "A fase de **observação** é passiva: métricas são coletadas, logs acumulam, o sistema registra. A fase de **medir e avaliar** é ativa: o time compara o que observou contra a baseline esperada, detecta drift, e decide o que isso significa para a qualidade da aplicação. A distinção importa porque equipes que confundem as duas fases frequentemente têm dashboards lindos e degradação não detectada."
ROI: MÉDIO

### ACHADO 03
Categoria: P1
Problema: Afirmação sobre salários e demanda (14.6) sem fonte e com risco de envelhecimento
Por que é um problema: "A demanda cresce mais rápido que a oferta em 2026, com salários comparáveis a engenheiros sêniors de plataforma" é afirmação de mercado de trabalho que vai envelhece, não tem fonte, e é irrelevante para a tese do livro (método, não mercado de trabalho).
Impacto no leitor: Leitor de 2027 em mercado com superoferta de AI Engineers vai questionar a credibilidade da análise.
Correção exata: Remover ou mover para Apêndice J. Se mantido, citar fonte e datar explicitamente: "[conforme levantamentos salariais de X e Y, primeiro trimestre de 2026]".
Texto sugerido: (Remover o parágrafo de mercado de trabalho ou mover para apêndice. A autoridade do capítulo vem da clareza técnica, não de projeção de empregabilidade.)
ROI: MÉDIO

### ACHADO 04
Categoria: P1
Problema: "Self-consistency" definida no glossário não aparece desenvolvida no texto principal
Por que é um problema: Itens de glossário que não aparecem no texto principal geram expectativa não cumprida. O leitor lê a definição de self-consistency, espera encontrá-la aplicada na seção de evals, e não encontra.
Impacto no leitor: Confusão sobre para que serve o glossário se inclui itens não tratados no corpo.
Correção exata: Ou remover "self-consistency" do glossário, ou adicionar parágrafo mínimo na seção de evals explicando quando self-consistency é útil como técnica de avaliação (complemento ao eval heurístico em domínios com resposta não-binária).
Texto sugerido: n/a (adição ou remoção)
ROI: BAIXO

### ACHADO 05
Categoria: P2
Problema: Ferramentas de observabilidade citadas por nome no texto principal (14.3.3) sem proteção de durabilidade
Por que é um problema: "LangSmith, Helicone, Phoenix Arize, Langfuse, Datadog com integração IA" — mesmo problema que outros capítulos, mas aqui com menor intensidade pois é lista de exemplos, não recomendação de produto.
Impacto no leitor: Moderado — a lista pode ficar desatualizada mas o princípio (usar ferramenta de observabilidade especializada) permanece.
Correção exata: Adicionar nota entre parênteses "(exemplos correntes em 2026 — ver Apêndice J)" após a lista.
Texto sugerido: "Ferramentas como LangSmith, Helicone, Phoenix Arize, Langfuse e Datadog com integração IA estão consolidando esse espaço (exemplos correntes — Apêndice J para lista atualizada)."
ROI: BAIXO

### ACHADO 06
Categoria: P2
Problema: Typo em 14.14 item 5: "Curiosidade **" com espaço extra (padrão repetido)
Por que é um problema: Mesmo problema tipográfico de template que C12 e C13.
Impacto no leitor: Mínimo.
Correção exata: Remover espaço extra.
Texto sugerido: "| 5 | **Curiosidade** — Está com vontade de comparar os principais modelos do mercado para escolher o certo para cada caso de uso | ☐ |"
ROI: BAIXO

## TESTE DA JOANA
Entenderia: SIM
O que ela entenderia: A analogia do engenheiro de pontes × prédios, o caso da seguradora (drift silencioso), a frase final "sem observabilidade não estão em produção", os cinco princípios de LLMOps em linguagem executiva.
O que ela NÃO entenderia: A distinção precisa entre as sete camadas da stack (vai entender que são sete, não o que fazer com cada uma), os três tipos de evals em detalhe técnico (heurístico, judge model, gold standard), a diferença entre fase de observação e fase de medir e avaliar.
Como corrigir: Clarificar a distinção observar × medir (Achado 02). Adicionar parágrafo executivo ao final de 14.3.1 resumindo o que a stack de sete camadas significa em termos de decisão: "Se sua organização não tem as camadas 6 e 7 (observabilidade e governança), você não tem AI Engineering, tem protótipo em produção disfarçado."

## TESTE DE DURABILIDADE
Classificação: ALTA
2 anos: Stack de sete camadas, lifecycle, três famílias de evals, cinco princípios de LLMOps — tudo sobrevive com pequena atualização de ferramentas.
5 anos: Os princípios são invariantes do problema de operar sistemas probabilísticos em produção. O drift silencioso vai continuar sendo o maior risco enquanto houver IA em produção.
10 anos: A estrutura de sete camadas pode precisar de expansão, mas o princípio de que software de IA tem características que software determinístico não tem vai permanecer válido.
Justificativa: Este é o capítulo com melhor durabilidade do bloco. As ferramentas citadas são o único ponto frágil, e a correção é menor.

## TESTE DE DIFERENCIAÇÃO
Classificação: DIFERENCIADO
Justificativa: O caso da seguradora com três fontes simultâneas de drift, a nota de rigor estatístico no caso, e a frase "sem observabilidade não estão em produção, estão em risco operacional latente" são propriedade intelectual real. A stack de sete camadas é estrutura própria, mais útil do que as listas genéricas de "disciplinas de AI Engineering" que circulam no mercado.

## TESTE DE MEMORIZAÇÃO
Ideia principal clara? SIM
Qual é a ideia principal: "AI Engineering é disciplina própria, não profissão adjacente. O que a define é operar sistemas probabilísticos em produção, com observabilidade contínua como pré-requisito não negociável."
Justificativa: A epígrafe final cristaliza a ideia. O caso da seguradora ancora na memória. A stack de sete camadas dá estrutura de retenção.

## TESTE DE TRANSFORMAÇÃO
Ao terminar, o leitor consegue fazer o que antes não conseguia:
- Descrever as sete camadas da stack de AI Engineering e diagnosticar onde uma aplicação está madura ou imatura
- Distinguir os três tipos de evals e quando usar cada um
- Reconhecer os cinco princípios de LLMOps com aplicação prática
- Defender em reunião por que observabilidade é pré-requisito, não acessório
- Identificar drift silencioso de qualidade antes que vire incidente

## NOTA FINAL
Estrutura: 9 | Pedagogia: 8 | Clareza: 8 | Autoridade: 9 | Durabilidade: 8 | Diferenciação: 8 | Memorização: 9 | Transformação: 9
**Nota Geral: 8.5**

## DECISÃO EDITORIAL
MANTER COM AJUSTES

---

## LINHAS-TRACKER

C14|L1-C14-ai-engineering.md|01|P1|MÉDIO|Seção de perfil profissional lista ferramentas por nome sem proteção de durabilidade|Substituir por categoria de competência com Apêndice J para ferramentas correntes|MANTER COM AJUSTES
C14|L1-C14-ai-engineering.md|02|P1|MÉDIO|Fronteira entre fase "observação" e "medir e avaliar" no lifecycle não está clara|Adicionar parágrafo explicitando que observar é passivo (coletar) e medir é ativo (interpretar contra baseline)|MANTER COM AJUSTES
C14|L1-C14-ai-engineering.md|03|P1|MÉDIO|Afirmação sobre salários e demanda sem fonte e com risco de envelhecimento|Remover ou mover para Apêndice J com fonte e data|MANTER COM AJUSTES
C14|L1-C14-ai-engineering.md|04|P1|BAIXO|"Self-consistency" definida no glossário mas não desenvolvida no texto principal|Remover do glossário ou adicionar uso mínimo na seção de evals|MANTER COM AJUSTES
C14|L1-C14-ai-engineering.md|05|P2|BAIXO|Lista de ferramentas de observabilidade sem nota de durabilidade|Adicionar "(exemplos correntes — Apêndice J)" após a lista|MANTER COM AJUSTES
C14|L1-C14-ai-engineering.md|06|P2|BAIXO|Typo: espaço duplo antes do fechamento de bold em item 5 de Autoavaliação|Remover espaço extra|MANTER COM AJUSTES

---

---

# C14B — L1-C14B-reasoning-models.md

## RESUMO EXECUTIVO
Nota: 9/10
Veredito: A+

## O QUE FUNCIONA
- Este é o melhor capítulo do bloco. A estrutura de argumento é completa: o que é, como funciona, quando usar, quando evitar, com o blueprint técnico do DeepSeek R1 como âncora.
- A distinção entre zero-shot CoT, few-shot CoT e reasoning model treinado (14B.3.2) é a mais clara disponível em linguagem não-técnica. A tabela comparativa em 14B.1 (Pirâmide de Complexidade × Custo) é propriedade intelectual real.
- A questão da faithfulness (14B.3.3) é onde o capítulo se distingue radicalmente de todo material de marketing disponível. Nenhum outro livro para público executivo discute que o raciocínio articulado pode ser racionalização pós-hoc — e aqui está com referências específicas (Lanham et al., Anthropic).
- A analogia do engenheiro que rascunha antes de comitar é precisa e não tem os problemas de imprecisão que analogias de IA costumam ter.
- A nota editorial em 14B.3.4 sobre não-redundância com C18 e F7 é modelo do que outros capítulos deveriam fazer. Poupa o leitor de buscar onde esse tópico está tratado em detalhe.
- O caso do escritório de M&A (14B.4) tem a especificidade certa: tamanho do escritório, segmento, tipo de tarefa, métricas do piloto (112 operações, quatro meses, aumento de 84% para 93% de concordância, custo 8x). O aprendizado da faithfulness descoberto no piloto é excepcional como narrativa.
- A tabela de quando usar e quando evitar (14B.5) é o melhor exemplo de heurística acionável do livro inteiro até este ponto.
- A referência ao DeepSeek R1 como "paper na Nature em 2025" é a única que exige verificação factual — tratar com cuidado (ver Achado 01).

## O QUE NÃO FUNCIONA
- O capítulo 14B vem depois do 14C na autoavaliação de 14C ("Avance para o Capítulo 14B sobre reasoning models") — inversão de ordem de leitura sugerida.
- A referência ao DeepSeek R1 como publicado "na Nature em 2025" precisa de verificação factual: o paper original do DeepSeek R1 foi publicado como preprint em janeiro de 2025, mas a publicação em Nature (peer-reviewed) precisa ser confirmada. Se for incorreta, é erro factual em achado que o capítulo usa como pilar central.
- A formulação "emergiu como categoria comercial entre o segundo semestre de 2024 e o ano de 2025" vai envelhece — mas o capítulo já tem o mecanismo de Apêndice J, então a exposição é menor.
- A seção 14B.3.5 contém "reasoning model surpreendentemente perde" em conhecimento factual direto — esse ponto é contraintuitivo e importante, mas a explicação "gastou ciclos pensando sobre algo que o conhecimento direto já resolveria" é informal demais para o nível de rigor do restante do capítulo. Merece uma frase sobre por que isso acontece mecanicamente.

## ACHADOS

### ACHADO 01
Categoria: P0
Problema: DeepSeek R1 referenciado como publicado "na Nature em 2025" — precisa de verificação factual
Por que é um problema: O paper DeepSeek R1 foi originalmente publicado como preprint no arXiv em janeiro de 2025. A publicação em Nature peer-reviewed precisa ser verificada. Se o livro afirmar "publicado na Nature" e o paper não tiver sido publicado lá, é erro factual no pilar técnico mais importante do capítulo.
Impacto no leitor: Leitor técnico que vai verificar a referência e não encontrar paper na Nature vai questionar a curadoria bibliográfica do livro inteiro.
Correção exata: Verificar e corrigir para o canal de publicação correto. Se for preprint no arXiv: "DeepSeek R1, publicado em janeiro de 2025 [arXiv:2501.XXXXX]". Se Nature for correto, manter com DOI.
Texto sugerido: "com a publicação do DeepSeek R1 em janeiro de 2025, cujo paper [preprint arXiv / Nature — verificar antes de imprimir] forneceu o primeiro blueprint público completo..."
ROI: ALTO

### ACHADO 02
Categoria: P0
Problema: Inversão de ordem de leitura: 14C indica "avance para 14B" na autoavaliação, mas 14B é a sequência natural de 14
Por que é um problema: O sumário e a estrutura numérica sugerem 14B antes de 14C. Mas 14C (autoavaliação, último item) diz "Avance para o Capítulo 14B sobre reasoning models", como se 14C viesse antes de 14B. Isso cria ambiguidade sobre a ordem de leitura intencional.
Impacto no leitor: Desorientação de sequência. Se a ordem intencional é 14 → 14C → 14B, a numeração deveria refletir isso. Se é 14 → 14B → 14C, o texto em 14C precisa ser corrigido.
Correção exata: Verificar a ordem intencional e corrigir: ou renumerar (14, 14B→14C, 14C→14D), ou corrigir o texto da autoavaliação de 14C para referenciar o capítulo seguinte correto.
Texto sugerido: Depende da ordem intencional. Se a ordem é 14 → 14B → 14C: remover o texto "Avance para o Capítulo 14B" de 14C (já não faz sentido como próximo passo).
ROI: ALTO

### ACHADO 03
Categoria: P1
Problema: A explicação de por que reasoning model perde em conhecimento factual direto é informal demais
Por que é um problema: "gastou ciclos pensando sobre algo que o conhecimento direto já resolveria" não explica o mecanismo. O leitor não entende por que pensar mais sobre um fato estabelecido produz resultado pior — a intuição não é óbvia.
Impacto no leitor: O ponto mais contraintuitivo do capítulo — reasoning model perde para modelo padrão em certas tarefas — fica sem âncora técnica suficiente para ser defensável em discussão.
Correção exata: Adicionar frase explicativa do mecanismo: "Em tarefas de recuperação factual direta, o modelo de propósito geral com pré-treinamento amplo acessa o fato diretamente do peso; o reasoning model, ao reservar fase de pensamento, gera oportunidade de interferência entre o fato e o raciocínio sobre o fato, o que em alguns casos produz resposta menos precisa do que a recuperação direta produziria."
Texto sugerido: (incorporar variação da frase acima em 14B.3.5, após o parágrafo que identifica essa categoria)
ROI: MÉDIO

### ACHADO 04
Categoria: P1
Problema: A tabela Pirâmide de Complexidade × Custo de Raciocínio (14B.1) tem números de custo relativo (10x–50x) que vão envelhece mas não têm proteção de Apêndice J
Por que é um problema: O Apêndice J é mencionado em 14B.3.4 para preços, mas a tabela em 14B.1 lista "10x–50x" e "10x–30x" sem nota de que esses multiplicadores podem mudar com otimizações de provedor.
Impacto no leitor: Os multiplicadores são dependentes de momento de mercado. O capítulo é cuidadoso em não citar preços absolutos mas cita multiplicadores que podem envelhecer.
Correção exata: Adicionar nota sob a tabela: "* Multiplicadores aproximados para produção em 2026 — as tendências de direção (reasoning custa mais) são invariantes; os valores específicos podem mudar com otimizações de provedor [ver Apêndice J]."
Texto sugerido: "> *Nota: os multiplicadores de custo e latência acima são aproximações para 2026. A direção — reasoning custa mais e demora mais — é invariante; os valores específicos acompanham Apêndice J.*"
ROI: MÉDIO

### ACHADO 05
Categoria: P2
Problema: A referência a "Lanham e colegas" aparece duas vezes no texto (14B.1 e 14B.3.3) com descrição ligeiramente diferente, sem título completo no corpo do texto
Por que é um problema: Primeira referência: "pesquisa publicada por Anthropic e por outros laboratórios... com nomes como Lanham e colegas". Segunda: "Trabalhos publicados por Anthropic, por Lanham e colegas". O título completo e o ano só aparecem nas referências (14B.13), mas o leitor que vai verificar no corpo do texto não tem o título.
Impacto no leitor: Leve inconsistência de apresentação de fonte que não compromete a leitura mas reduz rastreabilidade inline.
Correção exata: Na primeira citação, adicionar o título resumido: "Lanham et al. (2023) — 'Measuring Faithfulness in Chain-of-Thought Reasoning'" ou pelo menos o ano.
Texto sugerido: "pesquisa publicada por Anthropic e por outros laboratórios, incluindo Lanham et al. (2023), conduzindo experimentos sistemáticos..."
ROI: BAIXO

### ACHADO 06
Categoria: P2
Problema: Typo em 14B.14 item 5: "Curiosidade ativa" sem espaço entre label e travessão (padrão diferente dos demais capítulos)
Por que é um problema: Os outros capítulos usam "Curiosidade **" (com espaço extra) — aqui o padrão é ligeiramente diferente ("Curiosidade ativa" sem negrito no label). Inconsistência de template.
Impacto no leitor: Mínimo.
Correção exata: Uniformizar com o padrão dos outros capítulos ou definir padrão único para todos.
Texto sugerido: n/a (decisão de estilo)
ROI: BAIXO

## TESTE DA JOANA
Entenderia: SIM
O que ela entenderia: A analogia do engenheiro que rascunha, a tabela de quando usar e quando evitar (14B.5), o caso do escritório de M&A e a lição de que raciocínio articulado não é garantia de raciocínio correto, a epígrafe final.
O que ela NÃO entenderia: O mecanismo técnico do aprendizado por reforço puro (RL puro, RLHF, fine-tuning supervisionado — vocabulário denso em 14B.3.1), a questão de faithfulness em detalhe técnico (14B.3.3).
Como corrigir: A seção técnica já tem a estrutura correta de profundidade progressiva. A Joana pode pular 14B.3.1 e 14B.3.3 e ainda sair com 80% do valor do capítulo. Seria útil uma nota de navegação: "Se você é executivo, pule para 14B.4 após ler 14B.3.2. Se você é arquiteto técnico, leia a seção inteira."

## TESTE DE DURABILIDADE
Classificação: ALTA
2 anos: Distinção de categorias, tabela de quando usar/evitar, questão de faithfulness — todos sobrevivem. Nomes de modelos específicos (DeepSeek R1, família o, Claude reasoning) envelhecem mas o Apêndice J já cobre isso.
5 anos: O princípio de que raciocínio mais longo tem custo, latência e auditabilidade específicos vai sobreviver independente de como os modelos evoluem.
10 anos: A questão da faithfulness é estrutural e provavelmente vai se tornar mais importante, não menos, com o tempo.
Justificativa: O capítulo trata princípios, não produtos. A questão de faithfulness é especialmente durável — é uma questão filosófica sobre a relação entre processo interno e relato exposto que não vai ser resolvida com iteração de modelo.

## TESTE DE DIFERENCIAÇÃO
Classificação: PROPRIEDADE INTELECTUAL
Justificativa: A combinação de (1) tabela comparativa de três modos de raciocínio com custo/latência/auditabilidade, (2) questão de faithfulness com referências específicas e implicação operacional, (3) tabela de quando usar/evitar com critério explícito, e (4) caso de M&A com piloto controlado de 112 operações — não existe em nenhum livro de IA para público executivo disponível. Este capítulo é o ponto mais diferenciado do bloco revisado.

## TESTE DE MEMORIZAÇÃO
Ideia principal clara? SIM
Qual é a ideia principal: "Reasoning model não é o modelo melhor — é a ferramenta certa para o problema certo, com custo e latência que só se justificam quando raciocínio profundo é o gargalo."
Justificativa: A epígrafe final cristaliza: "Modelos que pensam por mais tempo erram menos em problemas onde pensar resolve. Em problemas onde pensar não é o gargalo, pensar mais apenas faz a fatura crescer." Esta é a melhor epígrafe de fechamento do bloco.

## TESTE DE TRANSFORMAÇÃO
Ao terminar, o leitor consegue fazer o que antes não conseguia:
- Distinguir zero-shot CoT, few-shot CoT e reasoning model com critério de custo e latência
- Identificar tarefas candidatas e não-candidatas a reasoning model com heurística explícita
- Implementar piloto controlado com métricas antecipadas (qualidade, custo, latência)
- Instituir protocolo de auditoria de faithfulness em domínio sensível
- Defender em comitê por que reasoning model não é a escolha padrão

## NOTA FINAL
Estrutura: 9 | Pedagogia: 9 | Clareza: 9 | Autoridade: 9 | Durabilidade: 9 | Diferenciação: 10 | Memorização: 9 | Transformação: 9
**Nota Geral: 9.3**

## DECISÃO EDITORIAL
MANTER COM AJUSTES

---

## LINHAS-TRACKER

C14B|L1-C14B-reasoning-models.md|01|P0|ALTO|DeepSeek R1 referenciado como publicado "na Nature" — precisa de verificação factual|Verificar canal de publicação correto (preprint arXiv vs Nature peer-reviewed) e corrigir|MANTER COM AJUSTES
C14B|L1-C14B-reasoning-models.md|02|P0|ALTO|Inversão de ordem de leitura: 14C autoavaliação indica "avance para 14B" como próximo passo|Verificar ordem intencional e corrigir numeração ou texto de navegação|MANTER COM AJUSTES
C14B|L1-C14B-reasoning-models.md|03|P1|MÉDIO|Explicação de por que reasoning model perde em conhecimento factual é informal demais|Adicionar frase sobre o mecanismo de interferência entre fato e raciocínio|MANTER COM AJUSTES
C14B|L1-C14B-reasoning-models.md|04|P1|MÉDIO|Multiplicadores de custo na tabela 14B.1 sem nota de proteção temporal|Adicionar nota: "multiplicadores para 2026 — direção é invariante, valores acompanham Apêndice J"|MANTER COM AJUSTES
C14B|L1-C14B-reasoning-models.md|05|P2|BAIXO|Referência a "Lanham e colegas" sem ano inline na primeira citação no corpo|Adicionar ano "(2023)" na primeira citação inline|MANTER COM AJUSTES
C14B|L1-C14B-reasoning-models.md|06|P2|BAIXO|Inconsistência de template na autoavaliação item 5 vs demais capítulos|Uniformizar padrão de label na autoavaliação|MANTER COM AJUSTES

---

---

# C14C — L1-C14C-spec-driven-development.md

## RESUMO EXECUTIVO
Nota: 8/10
Veredito: A

## O QUE FUNCIONA
- A inversão spec/código como tese central ("a especificação vira o ativo durável e o código vira a saída descartável") é a ideia mais original do capítulo e é genuinamente memorável. É a aplicação mais clara da tese "Modelos passam. Método fica." em todo o livro — o método é escrever spec; o modelo que a executa é transitório.
- A analogia do CAD paramétrico (14C.2) é a mais precisa do bloco: não apenas superficialmente similar, mas estruturalmente isomórfica (projeto → fábrica → verificador; spec → agente → engenheiro).
- Os sete elementos da anatomia da spec (14C.3.1) são um framework acionável. A observação de que a ausência de cada elemento degrada o output em padrão identificável é pedagogicamente forte.
- O caso da fintech (14C.4) é bem construído e honesto: inclui a falha real (regressão silenciosa, custo 7x acima do esperado, engenheiros aceitando plano sem revisão), a intervenção com três medidas específicas, e a lição que "SDD multiplica a competência operacional pelo mesmo fator que multiplica a incompetência". Isso é diferente.
- A seção "onde SDD não cabe" (14C.3.6) é rara — o capítulo defende o método E explica onde ele falha. Isso é o que separa um livro de método de um manifesto de produto.
- As três peças públicas (14C.3.7) — GitHub Spec Kit, OpenAI Model Spec, Anthropic best practices — são referências verificáveis e bem contextualizadas. O uso do Model Spec da OpenAI como prova de conceito de que spec em linguagem natural pode ser fonte de verdade organizacional é o insight mais sofisticado do capítulo.
- A ancoragem em Invariantes (9, 3, 6, 8) é a melhor execução de integração sistêmica do bloco.

## O QUE NÃO FUNCIONA
- O capítulo tem uma lacuna estrutural séria: não há nenhuma comparação com práticas anteriores de engenharia que tentaram a mesma inversão (BDD — Behavior-Driven Development; Design by Contract de Meyer; Literate Programming de Knuth). As referências aparecem nas referências bibliográficas mas não são integradas ao argumento. Por que SDD vai ter sucesso onde BDD ficou restrito a nicho? Essa pergunta não é respondida.
- O GitHub Spec Kit ultrapassar "noventa mil estrelas" é dado de popularidade que vai envelhece e é irrelevante para o argumento metodológico.
- A inversão sugerida na autoavaliação ("5 de 5? Avance para o Capítulo 14B") inverte a sequência numérica, confirmando o problema de ordenação identificado em C14B.
- A afirmação "oitenta a noventa por cento do valor de um programador hoje está na comunicação estruturada" (Sean Grove) não tem qualificação de metodologia. É afirmação de keynote, não dado mensurável. O livro endossa a afirmação sem questioná-la.
- O checklist do capítulo (14C.9) tem 8 itens, o mais longo do bloco — pode ser comprimido para os 5-6 mais críticos.
- O Diagrama 14C.1 referencia Karpathy em "junho de 2025, palestra de abertura no Y Combinator AI Startup School" e Grove em "AI Engineer World's Fair" — esses são marcos datados que envelhecem, mas o conteúdo conceitual (Software 1.0/2.0/3.0) é mais durável. A ancoragem em evento específico é mais frágil que a ancoragem no conceito.

## ACHADOS

### ACHADO 01
Categoria: P0
Problema: Ausência de contraste com BDD, Design by Contract e Literate Programming que tentaram inversões similares
Por que é um problema: A tese de que "a especificação é a fonte de verdade e o código é o artefato derivado" foi tentada antes (Design by Contract de Meyer, BDD, Literate Programming de Knuth). O capítulo menciona as referências nas fontes bibliográficas mas não enfrenta a pergunta: por que SDD vai ter sucesso agora onde essas práticas ficaram restritas a nicho? Sem responder a isso, o argumento fica incompleto para um leitor crítico.
Impacto no leitor: Um CTO com 20 anos de experiência vai ler "a spec é a fonte de verdade" e lembrar de BDD e perguntar: "isso não tentamos em 2008?" Se o livro não tem resposta, perde autoridade com exatamente o leitor mais importante.
Correção exata: Adicionar parágrafo de contraste explícito: "A inversão spec/código já foi tentada antes — Design by Contract de Meyer, BDD, Literate Programming de Knuth. Nenhuma escalou além de nichos específicos porque o custo de manter a spec sincronizada com o código era maior que o benefício. O que muda com SDD em era de agentes é que o custo de manter a sincronização cai a zero: o código é regenerado da spec, não coexiste com ela. Essa é a diferença estrutural que faz a inversão viável pela primeira vez."
Texto sugerido: (incorporar variação do parágrafo acima em 14C.1 ou 14C.2, após a apresentação da tese central)
ROI: ALTO

### ACHADO 02
Categoria: P1
Problema: "Oitenta a noventa por cento do valor do programador está em comunicação estruturada" endossado sem qualificação metodológica
Por que é um problema: A afirmação é de keynote de produto (Sean Grove, OpenAI), não de estudo metodológico. É plausível e provocativa, mas o livro a endossa como dado sem questionar a metodologia por trás. Isso contradiz o princípio de plausibilidade que o próprio capítulo menciona (Inv. 1 referenciado indiretamente).
Impacto no leitor: Leitor crítico vai questionar: como isso foi medido? O que conta como "comunicação estruturada"? Sem resposta, o dado vira anedota citada como evidência.
Correção exata: Qualificar: "Grove propõe que oitenta a noventa por cento do valor esteja em comunicação estruturada — a proporção é contestável, mas o argumento direcional é corroborado pela observação empírica de times que adotam SDD: o gargalo migra de 'quem escreve o código mais rápido' para 'quem especifica com mais clareza'."
Texto sugerido: (substituição no parágrafo do Diagrama 14C.1 que cita Grove)
ROI: MÉDIO

### ACHADO 03
Categoria: P1
Problema: Número de estrelas do GitHub Spec Kit ("noventa mil estrelas") envelhece e é irrelevante para o argumento
Por que é um problema: Estrelas no GitHub são métrica de popularidade em momento específico, não de qualidade ou de durabilidade. Em dois anos pode ser 200 mil (não impressiona mais) ou 50 mil (se o projeto tiver perdido relevância). A afirmação não reforça o argumento metodológico.
Impacto no leitor: Leitor em 2028 vai verificar e encontrar número diferente, criando dissonância.
Correção exata: Remover o número de estrelas e substituir por afirmação sobre adoção: "adotado por dezenas de times internamente e com integração nativa a trinta ferramentas de codificação por agente no fim de 2026 [ver repositório oficial, Apêndice J, para estado atual]".
Texto sugerido: "Lançado em código aberto pela GitHub em meados de 2025, o Spec Kit operacionaliza o fluxo das quatro etapas com templates de Markdown, checklists de qualidade embutidos e integração nativa a trinta plataformas de agente de codificação no lançamento [estado atual do ecossistema em Apêndice J]."
ROI: MÉDIO

### ACHADO 04
Categoria: P1
Problema: A inversão de ordem de leitura em 14C.14 ("5 de 5? Avance para o Capítulo 14B") confirma problema estrutural de sequência
Por que é um problema: Se o leitor seguiu a sequência numérica (14 → 14B → 14C), chegou ao 14B antes de 14C e a instrução de "avance para 14B" no final de 14C não faz sentido. Isso indica que a ordem intencional pode ser 14 → 14C → 14B, o que conflita com a numeração.
Impacto no leitor: Desorientação. O leitor que chegou aqui pela numeração já leu 14B. O leitor que chegou pela sugestão de 14C vai para 14B depois de um capítulo onde 14B já é mencionado como pré-leitura.
Correção exata: Resolver o problema estrutural de ordenação (confirmado de Achado 02 em C14B): escolher a ordem certa (14 → 14B → 14C ou 14 → 14C → 14B) e fazer numeração e navegação consistentes.
Texto sugerido: n/a (resolução estrutural)
ROI: ALTO

### ACHADO 05
Categoria: P1
Problema: A ancoragem de Karpathy em evento específico ("keynote no Y Combinator AI Startup School, junho de 2025") é mais frágil que a ancoragem no conceito Software 1.0/2.0/3.0
Por que é um problema: O conceito de Software 1.0/2.0/3.0 é durável; a palestra específica de junho de 2025 é pontual. Livros que citam eventos específicos envelhecem mais rápido que os que citam o pensamento do autor.
Impacto no leitor: Leve — mas a referência de Karpathy em vídeo e a da palestra específica são formas de citar que têm vida útil diferente.
Correção exata: Manter o conceito, qualificar a referência: "Karpathy formalizou em 2025 a leitura de três eras do software [ver referências para palestra específica]" em vez de ancorar no evento e data no corpo principal do texto.
Texto sugerido: "Andrej Karpathy formalizou em 2025 a leitura de três eras do software — 1.0 (código imperativo), 2.0 (redes neurais), 3.0 (LLM como computador programável em linguagem natural) — com a especificação assumindo o papel que o código tinha em 1.0."
ROI: BAIXO

### ACHADO 06
Categoria: P2
Problema: Checklist do capítulo (14C.9) tem 8 itens — o mais longo do bloco
Por que é um problema: A extensão reduz a probabilidade de o leitor completar o checklist. Os itens 7 e 8 (articular Invariantes e esboçar piloto) são consequência dos demais e podem ser fundidos.
Impacto no leitor: Sensação de sobrecarga de check, reduzindo uso real do checklist.
Correção exata: Fundir itens 7 e 8 ou marcar itens 7 e 8 como "avançado" para diferenciar do núcleo do capítulo.
Texto sugerido: n/a (compressão editorial)
ROI: BAIXO

### ACHADO 07
Categoria: P2
Problema: Referência a "Kiro" como ferramenta de integração do Spec Kit — pode ser pouco conhecida e sem contexto
Por que é um problema: A lista de integrações do Spec Kit inclui "Claude Code, Cursor, Copilot, Gemini, Codex, Windsurf, Kiro, Forge" — a maioria é reconhecível, mas "Kiro" e "Forge" são ferramentas menos estabelecidas que podem não ser conhecidas pelo leitor brasileiro em 2026.
Impacto no leitor: Leve confusão sobre o que são ferramentas mencionadas sem contexto.
Correção exata: Ou adicionar "(produto da Amazon Web Services)" após Kiro ou remover da lista de exemplos no corpo, mantendo apenas nas referências.
Texto sugerido: "trinta integrações nativas (Copilot, Claude Code, Cursor, Codex, Gemini, Windsurf e outros agentes de codificação)"
ROI: BAIXO

## TESTE DA JOANA
Entenderia: SIM
O que ela entenderia: A analogia do CAD paramétrico, a inversão spec/código, o caso da fintech e a lição de que velocidade não é produtividade, os sete elementos em lista (mesmo sem detalhe técnico de cada), a tabela de quando usar e evitar.
O que ela NÃO entenderia: A distinção entre BDD, Design by Contract e SDD (não está no texto, mas deveria ser). O que é "Kiro" e "Forge" na lista de integrações. O Invariante 8 (Responsabilidade Indelegável) sem contexto de qual capítulo o define.
Como corrigir: Adicionar nota de rodapé ou glossário mínimo para os Invariantes referenciados no cabeçalho do capítulo. O leitor que chegou aqui sem ter lido os capítulos anteriores vai ter dificuldade com "Inv. 9 — Operador".

## TESTE DE DURABILIDADE
Classificação: ALTA
2 anos: Os sete elementos da spec, as quatro etapas do fluxo, os três modos de falha — sobrevivem. Números de estrelas, nomes de eventos específicos, listas de integrações — envelhecem.
5 anos: A inversão spec/código como princípio é estruturalmente durável. Se em 2031 os agentes forem mais competentes, a importância da spec vai aumentar, não diminuir.
10 anos: "O código deixou de ser onde a competência mora" — esta frase vai ou ser óbvia (porque a transição terá se completado) ou vai ser historicamente importante como documentação da transição. De qualquer forma, sobrevive com dignidade.
Justificativa: Este é um dos capítulos com durabilidade mais alta do bloco, atrás apenas de C14B. A inversão que ensina é estruturalmente alinhada com a tese do livro.

## TESTE DE DIFERENCIAÇÃO
Classificação: DIFERENCIADO
Justificativa: A formulação da inversão spec/código com a clareza de "código vira saída descartável de um compilador probabilístico" não existe com essa precisão em outros livros. A seção "onde SDD não cabe" é diferenciadora por honestidade — raríssima em capítulos sobre método novo. A utilização do OpenAI Model Spec como prova de conceito organizacional (áreas não-técnicas participando via spec) é insight sofisticado que não está disponível no mainstream. O que impede PROPRIEDADE INTELECTUAL: a ausência de contraste com BDD/Design by Contract deixa a tese sem o teste mais importante.

## TESTE DE MEMORIZAÇÃO
Ideia principal clara? SIM
Qual é a ideia principal: "A especificação é o ativo durável. O código é a saída descartável. Quem entender essa inversão lidera a próxima década de engenharia."
Justificativa: A epígrafe de abertura e a de fechamento dizem exatamente isso. A analogia do CAD ancora na memória. Os três modos de falha são memoráveis por nomeação precisa.

## TESTE DE TRANSFORMAÇÃO
Ao terminar, o leitor consegue fazer o que antes não conseguia:
- Escrever uma spec com os sete elementos mínimos para uma feature real
- Identificar os três modos de falha mais comuns de SDD e reconhecê-los quando aparecem
- Defender por que a spec é o ativo durável em reunião arquitetural
- Estruturar um piloto de quatro semanas com critério de sucesso antecipado
- Articular onde SDD não deve ser aplicado (exploração, mudança trivial, domínio com eval ruim)

O que o leitor ainda não consegue fazer:
- Responder por que SDD vai ter mais sucesso que BDD (ausência de contraste)
- Estimar custo de adoção de SDD para um time sem cultura de revisão de código

## NOTA FINAL
Estrutura: 8 | Pedagogia: 9 | Clareza: 8 | Autoridade: 8 | Durabilidade: 9 | Diferenciação: 8 | Memorização: 9 | Transformação: 8
**Nota Geral: 8.4**

## DECISÃO EDITORIAL
MANTER COM AJUSTES

---

## LINHAS-TRACKER

C14C|L1-C14C-spec-driven-development.md|01|P0|ALTO|Ausência de contraste com BDD/Design by Contract/Literate Programming — por que SDD vai ter mais sucesso?|Adicionar parágrafo explicando que o custo de sincronização spec/código cai a zero quando código é regenerado da spec|MANTER COM AJUSTES
C14C|L1-C14C-spec-driven-development.md|02|P1|MÉDIO|"80–90% do valor do programador" de Grove endossado sem qualificação metodológica|Qualificar como tese direcional, não dado mensurável, e ancorar em observação empírica de times|MANTER COM AJUSTES
C14C|L1-C14C-spec-driven-development.md|03|P1|MÉDIO|Número de estrelas do GitHub Spec Kit ("noventa mil") envelhece e é irrelevante para argumento|Substituir por afirmação sobre adoção funcional e remeter ao Apêndice J|MANTER COM AJUSTES
C14C|L1-C14C-spec-driven-development.md|04|P1|ALTO|Inversão de ordem de leitura confirmada: 14C autoavaliação indica avançar para 14B — conflito com numeração|Resolver ordenação estrutural de 14B/14C e tornar numeração e navegação consistentes|MANTER COM AJUSTES
C14C|L1-C14C-spec-driven-development.md|05|P1|BAIXO|Karpathy ancorado em evento específico ("keynote no YC, junho de 2025") mais frágil que ancoragem no conceito|Mover detalhes do evento para referências; manter apenas o conceito Software 1.0/2.0/3.0 no corpo|MANTER COM AJUSTES
C14C|L1-C14C-spec-driven-development.md|06|P2|BAIXO|Checklist com 8 itens — o mais longo do bloco, reduz probabilidade de uso real|Fundir itens 7 e 8 ou marcar como avançados|MANTER COM AJUSTES
C14C|L1-C14C-spec-driven-development.md|07|P2|BAIXO|"Kiro" e "Forge" na lista de integrações sem contexto para leitor brasileiro|Remover das menções no corpo ou adicionar brevíssimo contexto (ex: "Kiro da AWS")|MANTER COM AJUSTES

---

---

# VISÃO CONSOLIDADA DO BLOCO C12–C14C

## Ranking por nota geral
1. C14B — Reasoning Models: 9.3 (A+) — MANTER COM AJUSTES MENORES
2. C14 — AI Engineering: 8.5 (A) — MANTER COM AJUSTES MENORES
3. C14C — Spec-Driven Development: 8.4 (A) — MANTER COM AJUSTES
4. C12 — Agentes de IA: 7.1 (B) — MANTER COM AJUSTES
5. C13 — MCP: 6.3 (C) — REVISAR PARCIALMENTE

## Achados críticos transversais (P0 que afetam múltiplos capítulos)

1. **Problema de ordenação 14B/14C**: afeta dois capítulos. Resolver antes de qualquer outra revisão, pois a decisão de ordem muda referências cruzadas em ambos.

2. **Citação de nomes de produtos como evidência de categoria**: aparece em C12 (Claude Code, AutoGen, LangGraph), C13 (MCP como padrão), C14 (LangSmith, Helicone), C14C (Spec Kit, 90k estrelas). O livro não tem tratamento consistente — C14B tem o melhor tratamento (Apêndice J + sem número de versão no corpo). Padronizar o tratamento de C14B para todos os capítulos é ação de alto ROI e baixo esforço.

3. **Typo de template em Autoavaliação item 5**: aparece em C12, C13, C14 — busca e substituição global no template resolve.

4. **Tensão entre MCP (C13) e tese "Modelos passam. Método fica."**: é o achado estrutural mais sério do bloco. C13 é o único capítulo que viola a tese do livro de forma direta. A solução não é remover o capítulo — é reformulá-lo para ensinar o princípio (padrões intermediários em M×N, primitivas de integração para agentes) usando o MCP como caso de estudo datado, não como a resposta.

## Totais de achados por capítulo
| Capítulo | P0 | P1 | P2 | Total |
|---|---|---|---|---|
| C12 — Agentes | 2 | 3 | 1 | 6 |
| C13 — MCP | 3 | 4 | 1 | 8 |
| C14 — AI Engineering | 0 | 4 | 2 | 6 |
| C14B — Reasoning Models | 2 | 2 | 2 | 6 |
| C14C — Spec-Driven Development | 1 | 4 | 2 | 7 |
| **TOTAL** | **8** | **17** | **8** | **33** |

---

# BANCA EDITORIAL ADVERSARIAL — CAPÍTULOS 15 a 19
*Livro: INTELIGÊNCIA AUMENTADA | Tese: "Modelos passam. Método fica."*
*Leitura integral realizada em 16/06/2026*

---

# C15 — L1-C15-comparacao-modelos.md

## RESUMO EXECUTIVO
Nota: 7/10
Veredito: B

## O QUE FUNCIONA
- A analogia da frota de veículos é memorável, correta e escalonável mentalmente.
- A árvore de decisão (cinco perguntas sequenciais) é o coração durável do capítulo; sobrevive a qualquer rotação de modelos porque ancora em padrão de tarefa, não em lançamento.
- A seção 15.3.3 sobre benchmarks funciona bem: explica o que cada benchmark mede em vez de citar pontuação, o que é o movimento metodicamente correto.
- A delegação de números voláteis para o Apêndice J (Trilha do Número) é a decisão editorial mais acertada do capítulo.
- O exemplo da fintech com roteamento (15.5) está bem construído, com aviso de "cenário ilustrativo" explícito, números realistas e lição estrutural separada dos detalhes.
- A seção de Tendências (15.6) está correta e durável: comoditização, modelos especializados, integração com hardware.

## O QUE NÃO FUNCIONA
- O checklist (15.9) instrui o leitor a "citar os três frontier proprietários de 2026 e o que cada um lidera" — isso é exatamente o que o livro deveria evitar; instrução de memorização de catálogo.
- A tabela de forças relativas (seção 15.4) nomeia famílias específicas como "vencedoras" por eixo; ao lado da ressalva correta de que "padrões mudam pouco entre gerações", ainda convida o leitor a memorizar associações que podem ser falsas em 18 meses.
- O texto menciona "xAI" e "Z.AI (modelos GLM)" como actores relevantes sem o mesmo cuidado epistêmico aplicado às três grandes; esses players têm probabilidade alta de serem irrelevantes ou transformados em 2 anos.
- Referência a "Trainium da AWS, Tensor Processing Units do Google, e silicon proprietário da Apple" em 15.6 é lista de produtos que envelhece rápido sem entregar método.
- A autoavaliação final (15.14) tem traço de "Curiosidade " com espaço extra no final — erro tipográfico menor mas indica ausência de revisão.

---

## ACHADOS

### ACHADO 01
Categoria: P0
Problema: O checklist item 1 instrui o leitor a "Citar os três frontier proprietários de 2026 e o que cada um lidera" — objetivo de aprendizagem orientado a memorização de catálogo de nomes e associações.
Por que é um problema: Contradição direta com a tese da obra. O livro declara "Modelos passam. Método fica." mas o primeiro item do checklist pede que o leitor grave qual família lidera qual eixo em 2026. Em 18 meses, o item estará errado.
Impacto no leitor: Joana aprende que deve saber de cor "Claude = código, GPT = matemática, Gemini = multimodal", e usa isso como critério permanente quando deveria usar a árvore de decisão.
Correção exata: Substituir "Citar os três frontier proprietários de 2026 e o que cada um lidera" por "Aplicar o Framework Diagnóstico de Encaixe em um caso real, sem recorrer a memória de qual modelo lidera qual eixo".
Texto sugerido: `- [ ] Aplicar o Diagnóstico de Encaixe entre Tarefa e Modelo a um caso real, descendo a árvore pelas cinco perguntas sem depender de memorização de rankings correntes`
ROI: ALTO

### ACHADO 02
Categoria: P1
Problema: A tabela de "Pontos Fortes" por família (seção 15.3.1 e repetida na tabela do 15.4) fixa associações com nomes de famílias específicas ("Claude Opus em SWE-bench Verified, historicamente") sem sinalização adequada de volatilidade.
Por que é um problema: O leitor que ler em 2027 vai encontrar afirmações provavelmente incorretas apresentadas como padrão estrutural. A ressalva "esses padrões mudam pouco entre gerações" é insuficiente — mudam sim, e o próprio texto mostra isso ao citar que o DeepSeek reorganizou o mercado.
Impacto no leitor: Executivo usa a tabela como referência permanente em vez de consultá-la como snapshot datado.
Correção exata: Adicionar cabeçalho de aviso na tabela: "Estado observado em 2026 — consulte Apêndice J para atualização. Leia os padrões, não os nomes."
Texto sugerido: `> ⚠️ **Tabela datada (2026)** — Os padrões estruturais (código, multimodal, custo) tendem a ser estáveis; as famílias que lideram cada eixo mudam. Use esta tabela para entender os eixos, consulte o Apêndice J para saber quem lidera hoje.`
ROI: ALTO

### ACHADO 03
Categoria: P1
Problema: xAI e Z.AI (GLM) são mencionados sem cuidado epistemológico equivalente ao dos três grandes. A xAI é caracterizada por "tolerância maior a temas sensíveis" como se isso fosse vantagem estável — definição que pode ser interpretada como endosso de menor alinhamento.
Por que é um problema: Em livro que tem capítulo de Alignment (C23), endossar "tolerância maior a temas sensíveis" como característica neutra de produto é inconsistente filosoficamente e potencialmente embaraçoso.
Impacto no leitor: Joana pode inferir que escolher xAI é recomendação do livro para casos em que se quer menos restrição de segurança.
Correção exata: Reescrever a caracterização da xAI para ser factual sem conotação de endorsement, e adicionar nota sobre implicações de alinhamento.
Texto sugerido: `A **xAI** opera o Grok, com acesso em tempo real ao X e posicionamento em monitoramento de tendências de rede social. O menor filtro por padrão versus os três grandes é diferença arquitetural que pode ser vantagem em contextos específicos de análise e risco regulatório em outros — avalie conforme o Capítulo 23 (Alignment).`
ROI: MÉDIO

### ACHADO 04
Categoria: P1
Problema: A seção 15.6 cita "Trainium da AWS, Tensor Processing Units do Google, e silicon proprietário da Apple" como exemplos de integração com hardware. É uma lista de produtos que envelhece em 2 anos sem entregar o padrão durável.
Por que é um problema: Em 2027, a lista de chips mudou (AWS Trainium 3, novo silicon da Apple, concorrentes), e o leitor que leu a lista decorou nomes errados.
Impacto no leitor: Confunde sinal de curto prazo (esses chips específicos) com tendência durável (inferência especializada em hardware específico reduz custo).
Correção exata: Reescrever o parágrafo para expressar o padrão durável e colocar os exemplos entre parênteses com marcação de snapshot.
Texto sugerido: `A tendência durável é que chips dedicados de inferência (como Trainium da AWS, TPUs do Google e silicon da Apple — exemplos de 2026, ver Apêndice J) estão mudando a economia de inferência de forma estrutural. O padrão a acompanhar é: custo de inferência em hardware especializado cai mais rápido que custo de hardware genérico, o que desloca a fronteira do self-hosting continuamente.`
ROI: MÉDIO

### ACHADO 05
Categoria: P2
Problema: Erro tipográfico em 15.14 — "**Curiosidade **" com espaço antes do fechamento do negrito. Sinal de ausência de revisão de copydeck.
Por que é um problema: Pequeno mas sinal de que a seção de autoavaliação não passou por revisão final.
Impacto no leitor: Mínimo, mas prejudica a credibilidade de atenção ao detalhe.
Correção exata: Remover espaço extra: `**Curiosidade**`
Texto sugerido: `| 5 | **Curiosidade** — Está com vontade de entender em profundidade o ecossistema open source, suas vantagens reais e suas armadilhas | ☐ |`
ROI: BAIXO

### ACHADO 06
Categoria: P2
Problema: A pergunta de revisão 3 (seção 15.10) pede que o leitor decida entre "Claude Opus e o frontier GPT para sistema de agentes autônomos" — pergunta orientada a nomes de produtos específicos, não a critérios.
Por que é um problema: Reforça a memória de produto em vez do método de decisão.
Impacto no leitor: O leitor pratica responder com nomes de modelos em vez de com lógica de encaixe.
Correção exata: Reformular como: "Como você decidiria entre um modelo premium centrado em código e um modelo premium centrado em computer use para um sistema de agentes? Quais perguntas do Diagnóstico de Encaixe guiariam a decisão?"
Texto sugerido: n/a (reformulação estrutural da pergunta)
ROI: BAIXO

---

## TESTE DA JOANA
Entenderia: SIM (parcialmente)
O que ela entenderia: A analogia da frota é excelente — Joana vai lembrar dela. A árvore de cinco perguntas é clara. O exemplo da fintech com economia de US$ 380 mil é concreto e motivador.
O que ela NÃO entenderia: A menção a "MCP" em 15.3.1 sem definição no capítulo (referencia Cap 13, mas quem está lendo fora de ordem não tem contexto). A distinção entre "frontier proprietário" e "open source" aparece sem o cuidado de 15.3.1 ter sido introduzido — ela pode confundir "open source" com "gratuito".
Como corrigir: Adicionar uma linha de definição de "MCP" inline na primeira menção, ou remover da seção e deixar apenas a referência ao capítulo.

## TESTE DE DURABILIDADE
Classificação: MÉDIA
2 anos: O framework de decisão (árvore de perguntas) sobrevive bem. As associações de família-força (Claude = código, GPT = matemática, Gemini = multimodal) provavelmente são parcialmente incorretas em 2028.
5 anos: A analogia da frota sobrevive. Os nomes de família e benchmarks específicos (ARC-AGI-2, Humanity's Last Exam) provavelmente foram superados.
10 anos: O método de roteamento por categoria de complexidade sobrevive. Tudo com nome de produto específico está obsoleto.
Justificativa: O capítulo se salva por delegar os números ao Apêndice J, mas os nomes de família no corpo do texto criam risco de leitura desatualizada por leitor que não for ao apêndice.

## TESTE DE DIFERENCIAÇÃO
Classificação: DIFERENCIADO
Justificativa: A estrutura de árvore de decisão com critério explícito (não "qual é o melhor" mas "qual passa nos critérios") é genuinamente pedagógica e não é comum em livros de IA executivos. A maioria dos concorrentes faz catálogo. Este capítulo não faz catálogo — faz método. Exceção: as tabelas de força por família são commodity.

## TESTE DE MEMORIZAÇÃO
Ideia principal clara? SIM
Qual é a ideia principal: "Não existe melhor modelo universal; existe roteamento inteligente por categoria de tarefa, com frota gerenciada em vez de escolha única."
Justificativa: A mensagem emerge clara da analogia e é repetida na epígrafe de fechamento.

## TESTE DE TRANSFORMAÇÃO
Ao terminar, o leitor consegue fazer o que antes não conseguia:
- Responder em reunião "não existe melhor modelo" com argumento estruturado, não opinião.
- Aplicar árvore de decisão de cinco perguntas para rotear tarefas entre tiers de modelo.
- Estimar potencial de economia de roteamento em operação existente.
- Distinguir qual benchmark é relevante para o seu caso de uso.
- Não confiar em ranking único como decisão de fundação.

## NOTA FINAL
Estrutura: 8 | Pedagogia: 8 | Clareza: 7 | Autoridade: 7 | Durabilidade: 6 | Diferenciação: 7 | Memorização: 8 | Transformação: 8
**Nota Geral: 7.4**

## DECISÃO EDITORIAL
MANTER COM AJUSTES
*Correções prioritárias: reformular checklist item 1 (P0), adicionar aviso datado às tabelas de força por família (P1), revisar caracterização da xAI (P1). O método é sólido; o catálogo residual no corpo do texto é o risco principal.*

---
---

# C16 — L1-C16-open-source.md

## RESUMO EXECUTIVO
Nota: 8/10
Veredito: A

## O QUE FUNCIONA
- A distinção "open weights × open source estrito" (16.3.2) é pedagogicamente precisa e rara em livros executivos — entrega valor real ao leitor.
- A seção de quantização (16.3.3) é técnica sem ser inacessível para Joana e entrega a implicação prática (PME rodando 70B em uma GPU) de forma concreta.
- A matriz de TCO em 12 meses (Quadro 16.A) é um artefato executivo genuíno: combina componentes que a maioria dos guias omite (time especializado, atualização, contingência).
- O caso da healthtech (16.4) é o mais completo dos exemplos dos cinco capítulos: tem vetor de pressão, processo de decisão, resultado quantificado, lição estrutural, e a ressalva de "cenário composto" explícita.
- Os seis critérios (16.5) são claros, ordenados e duráveis — esta é a parte mais Invariante do capítulo.
- A referência ao PL 2338 com ressalva de "em tramitação" e delegação ao Apêndice J é modelo de como citar legislação em evolução.

## O QUE NÃO FUNCIONA
- O capítulo cita "Nota Técnica da ANPD sobre IA generativa de 2026" em múltiplos pontos como documento estabelecido, mas o próprio texto ressalva que precisa ser verificado. A repetição sem marcação datada clara dá impressão de autoridade que pode não existir na data de leitura.
- A tabela do Quadro 16.A tem célula com "~600.000 (~50.000/mês para 100k req/dia média)" — esse número envelhece em meses. Preços de API da Anthropic (Claude Sonnet) mudaram múltiplas vezes em 18 meses.
- A seção 16.3.1 lista famílias com nomes de versão específicos (DeepSeek V3.1, Qwen 2.5 e Qwen 3, Llama 3.3 e 4) — inventário que terá versões novas antes do livro ir à gráfica.
- A referência ao Phi 4 como "14B" pode estar desatualizada — a família Phi evoluiu para Phi 4.5 e outras variantes.
- O Quadro 16.A descreve o híbrido com "~735.000" sendo mais caro que API exclusiva "~725.000" mas afirma que o híbrido é o padrão maduro — a lógica financeira parece inconsistente sem explicação mais clara de quando o híbrido ganha.

---

## ACHADOS

### ACHADO 01
Categoria: P0
Problema: O Quadro 16.A mostra custo total do Híbrido (~735.000) maior que API exclusiva (~725.000) mas o texto conclui que "o híbrido é o que justifica a arquitetura na maioria dos casos". A inconsistência não é explicada: se o híbrido custa mais, por que é o padrão maduro economicamente?
Por que é um problema: O leitor executivo (especialmente o CFO de Joana) vai notar que o argumento econômico não sustenta a recomendação. A defesa do híbrido precisa estar nos "benefícios não-monetários" — mas a tabela não os destaca.
Impacto no leitor: Mina a credibilidade do argumento TCO. O CFO diz "os números mostram que API é mais barata" e o argumento do híbrido colapsa.
Correção exata: Adicionar coluna "Benefício não-monetário" na tabela, OU adicionar parágrafo de reconciliação explícita: "No exemplo acima, o híbrido custa marginalmente mais que API exclusiva — o argumento econômico puro favorece API. O híbrido se justifica pelos benefícios estruturais não capturados na fatura: soberania de dado sensível em 97% do volume, capacidade de fine-tuning, e resiliência ao lock-in. Se esses três não têm valor para a organização, API exclusiva é a resposta certa nesse volume."
Texto sugerido: (parágrafo acima como inserção após a tabela)
ROI: ALTO

### ACHADO 02
Categoria: P1
Problema: O Quadro 16.A usa preço de API específico ("~600.000 para Claude Sonnet, ~50k/mês para 100k req/dia média") — dado que envelhece em ciclos de meses conforme a Anthropic ajusta preços.
Por que é um problema: Em 12 meses, os preços de Sonnet podem ser 30-50% diferentes; o leitor que usar a tabela para decisão terá premissa errada.
Impacto no leitor: Cálculo de TCO errado → decisão arquitetural errada.
Correção exata: Substituir o valor específico de API por "custo corrente de API (verificar Apêndice J)" e transformar a tabela em template com células marcadas como "preencher com valor corrente do provedor escolhido".
Texto sugerido: Cabeçalho da tabela: `| Componente | API exclusiva (preencher com preço atual — Apêndice J) | Self-hosting | Híbrido |`
ROI: ALTO

### ACHADO 03
Categoria: P1
Problema: A seção 16.3.1 lista "DeepSeek V3.1", "Qwen 2.5 e Qwen 3", "Llama 3.3 e 4", "Phi 4" como inventário específico de versões. Esse nível de especificidade envelhece antes da impressão.
Por que é um problema: O capítulo inteiro tem a tese de que a decisão é sobre método, não catálogo. A própria seção 16.3.1 contraria essa tese ao fazer exatamente o catálogo que o capítulo deveria evitar.
Impacto no leitor: Em 2027, o leitor encontra versões defasadas e perde confiança no resto do capítulo.
Correção exata: Manter os nomes de família (DeepSeek, Meta Llama, Mistral, Qwen, Phi, Gemma) mas remover números de versão do corpo do texto e delegar para o Apêndice J. Adicionar instrução de consulta: "versão corrente em Apêndice J."
Texto sugerido: `**DeepSeek (laboratório chinês).** Família em licença MIT com foco em raciocínio, código e multilíngue. Versão corrente no Apêndice J. Qualidade de fronteira open weights em várias tarefas corporativas...`
ROI: MÉDIO

### ACHADO 04
Categoria: P1
Problema: "Nota Técnica da ANPD sobre IA generativa de 2026" é citada múltiplas vezes como se fosse documento estabelecido e bem-definido, mas a própria referência ao final do capítulo instrui "verificar versão corrente em fonte oficial datada". A citação no corpo do texto sem data específica e sem nota de rodapé cria falsa autoridade.
Por que é um problema: A Nota Técnica pode ter sido revisada, substituída, ou pode nem ter sido publicada com esse título exato. O leitor que tentar verificar pode não encontrar o documento nomeado.
Impacto no leitor: Profissional de compliance usa a referência em apresentação interna, não encontra o documento exato, perde credibilidade.
Correção exata: Em toda menção à Nota Técnica da ANPD, adicionar marcação "(verificar versão corrente em Apêndice J — Trilha do Número)" explicitamente, ou criar nota de rodapé padrão para o capítulo.
Texto sugerido: `...a Nota Técnica da ANPD sobre IA generativa (versão corrente: Apêndice J — Trilha do Número)...`
ROI: MÉDIO

### ACHADO 05
Categoria: P2
Problema: A analogia da frota corporativa (16.2) é boa mas longa. Quatro parágrafos para estabelecer a analogia antes de descer ao técnico. Em um livro de executivos, a analogia poderia ser comprimida em dois parágrafos sem perda de conteúdo.
Por que é um problema: Ritmo lento na entrada do capítulo pode fazer Joana pular para 16.3, perdendo a estrutura narrativa que o livro usa.
Impacto no leitor: Menor — mas analogia longa demais perde força.
Correção exata: Comprimir 16.2 de quatro para dois parágrafos, mantendo os quatro pontos de analogia mas de forma mais densa.
Texto sugerido: n/a (reescrita de compressão)
ROI: BAIXO

### ACHADO 06
Categoria: P2
Problema: A pergunta de revisão 5 cita "Nota Técnica da ANPD de 2026" como dado de fact — instrução de memorização que cria o mesmo problema de durabilidade.
Por que é um problema: Em 2027, o leitor não vai saber se a nota de 2026 ainda é a vigente.
Impacto no leitor: Leitor memora "2026" como referência correta quando deveria aprender a verificar a versão corrente.
Correção exata: Reformular: "Como a regulação de privacidade brasileira (atualmente LGPD + orientações da ANPD — verificar versão corrente) desloca a fronteira em favor de operação em território nacional?"
Texto sugerido: n/a
ROI: BAIXO

---

## TESTE DA JOANA
Entenderia: SIM
O que ela entenderia: A analogia da frota é acessível. O conceito de "API vs self-hosting" tem paralelo imediato com "terceirizar vs fazer em casa". A Quadro 16.A com valores em reais é diretamente utilizável por ela em conversa com CFO.
O que ela NÃO entenderia: "Quantização INT4 com AWQ" — o texto explica o que é INT4 mas AWQ fica como sigla sem desdobramento suficiente para quem não é técnico. "vLLM como engine de inferência" — não há definição do que é uma engine de inferência para não-técnico.
Como corrigir: Adicionar glossário inline para AWQ: "(AWQ — método de quantização que preserva melhor a qualidade; detalhes técnicos desnecessários para decisão executiva)".

## TESTE DE DURABILIDADE
Classificação: MÉDIA
2 anos: Os seis critérios de decisão (16.5), a distinção open weights × open source estrito, a lógica de TCO honesto — tudo isso sobrevive. As versões de modelo, os preços específicos e a referência à "Nota Técnica da ANPD de 2026" ficam desatualizados.
5 anos: O método de TCO honesto sobrevive. O Quadro 16.A precisa ser refaturado com novos números.
10 anos: Os princípios de soberania de dados, TCO composto e arquitetura híbrida sobrevivem. Os nomes de provedor (Magalu Cloud, etc.) podem não existir mais.
Justificativa: Capítulo bem construído com separação razoável entre método durável e exemplos datados. O risco principal são os números de preço e os números de versão.

## TESTE DE DIFERENCIAÇÃO
Classificação: DIFERENCIADO
Justificativa: A matriz de TCO com os cinco componentes (hardware, time, energia, atualização, contingência) é mais completa que qualquer framework equivalente em livros de gestão de IA disponíveis no mercado brasileiro. A distinção open weights × open source estrito é rara e precisa. O posicionamento de soberania de dados como driver estratégico, não apenas técnico, é genuíno.

## TESTE DE MEMORIZAÇÃO
Ideia principal clara? SIM
Qual é a ideia principal: "A decisão de 2026 não é 'open source ou API' — é arquitetura híbrida com classificador, calibrada por TCO honesto e soberania de dado."
Justificativa: A frase é repetida várias vezes e a epígrafe de fechamento a cristaliza bem.

## TESTE DE TRANSFORMAÇÃO
Ao terminar, o leitor consegue fazer o que antes não conseguia:
- Calcular TCO honesto de 12 meses com os cinco componentes (não apenas fatura de API).
- Distinguir open weights de open source estrito e saber que quase nenhum modelo grande é open source estrito.
- Identificar o ponto de virada econômico (volume mensal) para avaliar se self-hosting se justifica.
- Saber quais perguntas fazer ao DPO sobre soberania de dados sensíveis.
- Propor arquitetura híbrida com classificador como alternativa ao binário "API ou on-prem".

## NOTA FINAL
Estrutura: 9 | Pedagogia: 8 | Clareza: 7 | Autoridade: 8 | Durabilidade: 6 | Diferenciação: 9 | Memorização: 8 | Transformação: 9
**Nota Geral: 8.0**

## DECISÃO EDITORIAL
MANTER COM AJUSTES
*Correções prioritárias: resolver inconsistência do Quadro 16.A onde híbrido custa mais que API mas é recomendado (P0); transformar preços específicos em template com remissão ao Apêndice J (P1); remover números de versão de modelos do corpo (P1).*

---
---

# C17 — L1-C17-github-repos.md

## RESUMO EXECUTIVO
Nota: 9/10
Veredito: A+

## O QUE FUNCIONA
- Este é o capítulo mais autorreferente e metodologicamente consistente dos cinco. A epígrafe que abre, a analogia do imóvel, o protocolo de 30 minutos, o anti-padrão das estrelas — tudo é internamente coerente e genuinamente durável.
- A analogia do corretor de imóvel em trinta minutos é a mais precisa e útil dos cinco capítulos: tem seis blocos, cada um com lição direta, e o padrão de "cada bloco é trivialmente auditável em cinco minutos" é imediatamente aplicável.
- O Quadro 17.A (tabela do protocolo) é o melhor artefato operacional dos cinco capítulos: colunas claras, decisão binária, três saídas. Executável sem contexto adicional.
- A seção de anti-padrões (17.4) é pedagógica: as quatro armadilhas com o sinal real versus performático são precisas e não requerem atualização.
- O ciclo de vida do repositório (17.3.7) com cinco fases e quatro sinais cada é framework durável que sobrevive a qualquer rotação do ecossistema.
- A seção 17.6 tem a consciência editorial mais honesta de todo o livro: declara explicitamente que a lista vai envelhecer, que serve apenas como exercício de aplicação, e convida o leitor a comparar com sua própria auditoria. Isso é exatamente como o capítulo deveria se comportar.
- O exemplo da fintech (17.5) é concreto, realista, com números plausíveis e lição estrutural clara.

## O QUE NÃO FUNCIONA
- O capítulo referencia "imagens/cap-35-img-01-repos-categoria.svg" com código de capítulo (cap-35) diferente do número do capítulo (17). Erro de referência de arquivo que indica inconsistência na numeração interna.
- A seção 17.6 declara que lista oito repositórios mas a caracterização inclui "Weights & Biases" com "componente proprietário dominante" — confunde a ferramenta open source (SDK W&B) com o produto comercial. A distinção importa para o Critério 6 (encaixe).
- O texto menciona "OpenInterpreter" com "governança em pessoa física com empresa em formação" — informação de alta perecibilidade que contradiz a filosofia do capítulo.
- A regra "CI vermelho na branch principal" em 17.3.3 é apresentada como red flag absoluta, mas CI verde é trivialmente falsificável (basta não ter CI). A regra deveria ser CI presente e verde, não apenas "verde".

---

## ACHADOS

### ACHADO 01
Categoria: P1
Problema: Referência de imagem usa "imagens/cap-35-img-01-repos-categoria.svg" — cap-35 quando o capítulo é o 17. Inconsistência de numeração interna.
Por que é um problema: Indica que o arquivo de imagem pode não existir no caminho correto, ou que houve renumeração de capítulos sem atualização das referências.
Impacto no leitor: Imagem quebrada na versão digital; ilustração ausente na versão impressa.
Correção exata: Verificar o caminho correto do arquivo SVG e corrigir para "imagens/cap-17-img-01-repos-categoria.svg" (ou o padrão adotado pelo livro).
Texto sugerido: `![Mapa de categorias de repositórios relevantes no ecossistema de IA](imagens/cap-17-img-01-repos-categoria.svg)`
ROI: ALTO

### ACHADO 02
Categoria: P1
Problema: A caracterização do "OpenInterpreter" inclui "governança em pessoa física com empresa em formação" — informação extremamente perecível que contradiz a filosofia de método durável que o capítulo defende.
Por que é um problema: Se o livro instrui a não confiar em blog posts e README de marketing por envelhecerem, o próprio livro não pode fazer exatamente isso ao caracterizar a governança de um projeto pelo estado corrente da empresa do mantenedor.
Impacto no leitor: Em 6 meses, a informação estará desatualizada; o leitor perde confiança no método exatamente no capítulo que deveria defender o método.
Correção exata: Substituir "governança em pessoa física com empresa em formação" por observação sobre o critério que o leitor deve verificar: "verifique a fase do ciclo de vida conforme protocolo — em meados de 2026 estava em adoção real com sinais de transição, mas esse diagnóstico é exercício, não inventário."
Texto sugerido: `**OpenInterpreter.** Fase variável — audite conforme protocolo. Em meados de 2026: adoção real com sinais de transição, encaixe limitado em produção corporativa, natural em sandbox e uso individual. Leia a governança corrente no repositório ao aplicar Critério 5.`
ROI: MÉDIO

### ACHADO 03
Categoria: P1
Problema: A regra de CI (17.3.3) diz "CI vermelho na branch principal é red flag" mas não exige CI presente como condição. CI ausente é mais grave que CI vermelho, mas a formulação da regra não captura isso.
Por que é um problema: Projeto sem CI passa no critério (por não ter CI vermelho) mas deveria falhar.
Impacto no leitor: Adota projeto que passou no critério 3 sem ter CI algum.
Correção exata: Reformular: "A ausência de CI é red flag imediata em qualquer projeto que se apresenta como pronto para produção. CI presente e vermelho é sinal de descuido ou de quebra ativa — igualmente problemático."
Texto sugerido: `**CI/CD ativo.** A ausência de pipeline de integração contínua é red flag imediata para uso em produção. CI presente com status vermelho na branch principal indica quebra ativa ou descuido — ambos são red flag. Passes em CI com histórico verde nos últimos commits é o critério de aprovação.`
ROI: MÉDIO

### ACHADO 04
Categoria: P2
Problema: A seção de Weights & Biases (17.6) descreve "componente proprietário dominante" e "modelo de negócio em camada hospedada" mas não aprofunda o que isso significa para o Critério 6 (encaixe) — especificamente para a organização com restrição de operação totalmente self-hosted.
Por que é um problema: É o único dos oito repositórios em que a questão de licença e encaixe é relevante o suficiente para merecer destaque mas o texto não destaca.
Impacto no leitor: Organização com restrição regulatória de self-hosting total adota W&B sem perceber que a funcionalidade principal requer a camada cloud.
Correção exata: Adicionar frase explícita: "Para organização com restrição de self-hosting total por regulação, verifique se a funcionalidade requerida está no SDK open source ou exige a camada hospedada — essa verificação entra no Critério 6."
Texto sugerido: (adicionar ao final da linha sobre W&B)
ROI: BAIXO

### ACHADO 05
Categoria: P2
Problema: O exemplo (17.5) descreve sessão com "dois engenheiros sêniores e o tech lead da plataforma de IA" tomando "dez horas totais distribuídas em três tardes" — mas o protocolo diz 30 minutos por repositório. Vinte repositórios × 30 minutos = 10 horas, o que fecha. Mas o leitor pode interpretar que cada pessoa gastou 10 horas (30 horas totais) em vez de que a sessão total foi 10 horas. A ambiguidade é pequena mas real.
Por que é um problema: Leitor pode perceber que três pessoas dedicaram 10 horas cada = 30 horas para auditar 20 repositórios, o que não valida o protocolo de 30 min/repo.
Impacto no leitor: Questionamento sobre se o protocolo é realmente de 30 minutos.
Correção exata: Clarificar: "...dez horas totais de sessão coletiva (média de trinta minutos por repositório aplicada em trio), distribuídas em três tardes."
Texto sugerido: n/a (pequeno ajuste de clareza)
ROI: BAIXO

---

## TESTE DA JOANA
Entenderia: SIM
O que ela entenderia: A analogia do corretor de imóvel é o melhor ponto de entrada dos cinco capítulos para Joana. O Quadro 17.A é imediatamente utilizável por ela como checklist para perguntar ao time. Os quatro anti-padrões são reconhecíveis e memoráveis.
O que ela NÃO entenderia: "SemVer" sem definição inline (ela sabe o que é "versionamento semântico" pela explicação, mas o acrônimo SemVer aparece sem apresentação). "Bus factor de um" — jargão técnico não explicado.
Como corrigir: Definir bus factor inline: "(bus factor de um: risco de o projeto parar se uma única pessoa chave sair)".

## TESTE DE DURABILIDADE
Classificação: ALTA
2 anos: O protocolo de seis critérios, o ciclo de vida, os anti-padrões — tudo sobrevive. A lista de oito repositórios em 17.6 provavelmente está parcialmente desatualizada.
5 anos: O método sobrevive inteiramente. Os oito exemplos são exercício de aplicação, não inventário — o capítulo resiste.
10 anos: Este é o capítulo com maior durabilidade dos cinco. A analogia do imóvel e o protocolo de 30 minutos descrevem lógica de avaliação de qualidade de software que não tem data de validade.
Justificativa: O capítulo pratica o que prega — não faz catálogo, faz método. A seção 17.6 tem a maior consciência editorial sobre durabilidade de qualquer seção dos cinco capítulos.

## TESTE DE DIFERENCIAÇÃO
Classificação: PROPRIEDADE INTELECTUAL
Justificativa: O protocolo de 30 minutos com seis critérios duráveis, o ciclo de vida com quatro sinais por fase, os quatro anti-padrões com o mecanismo de sinal performático — em conjunto, isso é framework genuinamente novo que não existe em formato equivalente em nenhum livro de IA executivo do mercado. Este capítulo justifica o livro por si só para qualquer CTO que já perdeu tempo com repositório abandonado.

## TESTE DE MEMORIZAÇÃO
Ideia principal clara? SIM
Qual é a ideia principal: "Inventário envelhece em seis meses; método de auditoria dura uma carreira — e o método cabe em trinta minutos por repositório, com seis critérios e a coragem de descartar catorze de cada vinte."
Justificativa: A epígrafe inicial e a epígrafe final repetem a mesma ideia em formulações levemente diferentes. Memorável.

## TESTE DE TRANSFORMAÇÃO
Ao terminar, o leitor consegue fazer o que antes não conseguia:
- Auditar qualquer repositório GitHub em 30 minutos com critério explícito e decisão documentada.
- Reconhecer as quatro armadilhas (estrelas, README, demo, blog post) antes de tomá-las como sinal real.
- Classificar repositório em uma das cinco fases do ciclo de vida e tomar decisão proporcional.
- Estabelecer planilha estruturada de auditoria como padrão da casa.
- Proteger a organização de "lista de conferência" sem método de validação.

## NOTA FINAL
Estrutura: 9 | Pedagogia: 10 | Clareza: 9 | Autoridade: 9 | Durabilidade: 9 | Diferenciação: 10 | Memorização: 9 | Transformação: 10
**Nota Geral: 9.4**

## DECISÃO EDITORIAL
MANTER COM AJUSTES
*Apenas dois ajustes prioritários: corrigir referência de imagem com número de capítulo errado (P1) e reformular a caracterização de OpenInterpreter para não infringir a filosofia do próprio capítulo (P1). O resto é excelente — este é o capítulo mais alinhado com a tese do livro.*

---
---

# C18 — L1-C18-economia-tokens.md

## RESUMO EXECUTIVO
Nota: 7/10
Veredito: B

## O QUE FUNCIONA
- A fórmula do custo composto (18.2.1) com os quatro termos explícitos (tokens×preço, chamadas, redundância, tier) é o melhor artefato conceitual do capítulo — diferente do que se encontra nos guias de otimização típicos que tratam apenas o preço por token.
- A regra de ordem de implementação (T1 antes T2 antes T3) é contraintuitiva e valiosa: a maioria dos times começa por poda de contexto (T3) enquanto o maior impacto está em roteamento de tier (T1).
- O exemplo da SaaS (18.5) é limpo e convincente: comprova a regra de ordem com um caso real de "equipe otimizou o termo trivial enquanto a sangria estava no termo composto".
- O Quadro 18.A é util como referência rápida.
- A seção 18.6 (quando aprofundar e quando parar) é rara em guias de otimização e entrega valor genuíno — saber quando parar é tão importante quanto saber quando começar.

## O QUE NÃO FUNCIONA
- O capítulo é o mais curto dos cinco em extensão de análise e o menos desenvolvido em framework. Não tem analogia de abertura (a rubrica espera "CONCEITO INTUITIVO + ANALOGIA" mas aqui só há conceito). A seção 18.2 vai direto para a fórmula matemática sem rampa de acesso.
- A tabela 18.7 apresenta percentuais de economia "40-70%, 30-60%, 30-50%..." que se somam a mais de 100% sem explicação de que são ganhos compostos não-aditivos. Um CFO vai perguntar "isso dá 200% de economia total?" e a resposta não está no texto.
- A seção 18.1 tem o aviso metodológico sobre "ordens de grandeza observadas" — bom — mas o aviso aparece no topo antes de qualquer contexto, o que o torna invisível ao leitor que lê por diagonal.
- A referência ao Framework F7 é repetida 3 vezes mas o framework não está no capítulo. O leitor não sabe o que é F7 sem navegar para fora do capítulo.
- O capítulo não tem analogia. Para um tema de finanças corporativas, uma analogia de otimização financeira (ex: análise de Pareto em gastos operacionais) tornaria a entrada muito mais acessível para Joana.
- Perguntas de revisão (18.8) têm apenas 5 itens — todos os outros capítulos têm 7-8. Indica desenvolvimento incompleto.
- A autoavaliação (18.12) tem item 5 sobre "Curiosidade para segurança em escala corporativa" — que não tem relação com o capítulo de economia de tokens. Parece copypaste de outro capítulo.

---

## ACHADOS

### ACHADO 01
Categoria: P0
Problema: A tabela 18.7 lista percentuais de economia por alavanca (40-70%, 30-60%, etc.) sem explicar que são ganhos compostos aplicados a bases progressivamente menores, não aditivos sobre a fatura original. A soma ingênua ultrapassa 200%.
Por que é um problema: CFO ou analista financeiro vai somar as percentagens e perguntar "nossa fatura vai para zero?" — destruindo a credibilidade do autor.
Impacto no leitor: Decisão de investimento em otimização baseada em expectativa inflada. Descredita o capítulo para leitores com mentalidade quantitativa.
Correção exata: Adicionar nota de rodapé ou parágrafo após a tabela explicando: "Os percentuais são aplicados sequencialmente sobre o resíduo — não são aditivos. Aplicar todas as sete alavancas pode resultar em economia de 60-75% do total original, não na soma dos intervalos."
Texto sugerido: `> ⚠️ **Os percentuais não somam.** Cada alavanca é aplicada sobre o custo residual após as anteriores. Prompt caching de 40-70% reduz a base; roteamento de 30-60% incide sobre o que sobrou. A economia composta realista com todas as sete alavancas bem executadas é de 60 a 75% da fatura original — não a soma dos intervalos acima.`
ROI: ALTO

### ACHADO 02
Categoria: P1
Problema: O capítulo não tem analogia de abertura. A entrada vai direto para a fórmula matemática, o que é inacessível para Joana e para executivos financeiros sem background técnico.
Por que é um problema: A rubrica do livro exige Conceito Intuitivo + Analogia. Este capítulo pula a analogia, tornando a fórmula do custo composto mais difícil de internalizar do que precisa ser.
Impacto no leitor: Joana para na fórmula, lê o exemplo da SaaS e entende a mensagem, mas perde a estrutura analítica que permitiria aplicar em outras situações.
Correção exata: Adicionar analogia entre 18.1 e 18.2. Sugestão: "Pense em conta de energia elétrica corporativa. O preço do kWh aparece na fatura, mas o que explode a conta é a soma de equipamentos ligados × horas × quantidade de unidades. Cortar o preço do kWh em 5% via negociação com a distribuidora entrega menos que desligar equipamentos em stand-by que ninguém auditou. Tokens funcionam da mesma forma: preço por token é o kWh; chamadas, redundância e tier são os equipamentos esquecidos ligados."
Texto sugerido: (parágrafo acima como Seção 18.2 de analogia antes da fórmula)
ROI: ALTO

### ACHADO 03
Categoria: P1
Problema: A autoavaliação (18.12) item 5 diz "Curiosidade para segurança em escala corporativa" — completamente desconectado do tema do capítulo (economia de tokens). Claramente é texto de outro capítulo copiado sem ajuste.
Por que é um problema: Erro editorial básico que sinaliza que a seção de autoavaliação foi produzida por template sem revisão de conteúdo.
Impacto no leitor: Perde confiança na qualidade editorial; pode confundir o leitor sobre o que o capítulo cobre.
Correção exata: Substituir pelo critério correto de curiosidade para economia de tokens: "Curiosidade — Está motivado a instrumentar tokens por feature na sua operação nas próximas duas semanas para ter baseline real antes de iniciar o programa de otimização?"
Texto sugerido: `| 5 | **Curiosidade** — Está motivado a instrumentar tokens por feature na próxima semana para ter baseline real e iniciar o programa de otimização com diagnóstico honesto? | ☐ |`
ROI: ALTO

### ACHADO 04
Categoria: P1
Problema: O Framework F7 é referenciado três vezes no capítulo mas nunca definido. O leitor que lê o capítulo isoladamente não sabe o que é F7.
Por que é um problema: Referência circular sem âncora no texto cria sensação de que o capítulo está incompleto — como se a parte "real" estivesse em outro lugar.
Impacto no leitor: Leitor que não tem acesso ao framework completo não consegue aplicar T1/T2/T3 sistematicamente.
Correção exata: Adicionar mini-descrição do F7 na primeira menção: "Framework F7 — Custo Composto em Três Tempos: o plano operável das três alavancas (T1=tier, T2=topologia, T3=contexto) com metas, riscos e ordem de execução detalhados no módulo de Frameworks do livro."
Texto sugerido: n/a (inline na primeira menção de F7)
ROI: MÉDIO

### ACHADO 05
Categoria: P1
Problema: O aviso metodológico de 18.1 ("As reduções percentuais apresentadas... são ordens de grandeza observadas... não médias estatísticas de pesquisa peer-reviewed") está no início do capítulo antes de qualquer contexto, tornando-o invisível. O leitor que lê em diagonal vai ao título, à fórmula e ao exemplo — e nunca vê o aviso.
Por que é um problema: Os percentuais são usados por executivos em apresentações ao conselho sem a ressalva metodológica, criando expectativas incorretas.
Impacto no leitor: "O livro diz que economizamos 70%" → promessa não cumprida → descredita o autor.
Correção exata: Mover o aviso para próximo à tabela 18.7, onde os percentuais aparecem, em vez de no início do texto onde é ignorado.
Texto sugerido: Mover o parágrafo de ressalva de 18.1 para um bloco de rodapé da tabela 18.7.
ROI: MÉDIO

### ACHADO 06
Categoria: P2
Problema: Os preços de tier mencionados no Quadro 18.A ("30 a 50 vezes o preço do modelo pequeno") são afirmações de magnitude que envelhecem conforme os fornecedores ajustam pricing.
Por que é um problema: Em 18 meses, a razão premium/pequeno pode ser 10x ou 100x dependendo dos lançamentos.
Impacto no leitor: Leitor usa "30-50x" como dado firme em análise financeira.
Correção exata: Adicionar remissão: "(magnitude observada em 2026; confirmar razão atual nas fichas dos fornecedores — Apêndice J)".
Texto sugerido: n/a (inline na menção)
ROI: BAIXO

---

## TESTE DA JOANA
Entenderia: NÃO (sem a analogia)
O que ela entenderia: O exemplo da SaaS (18.5) é excelente para Joana — concreto, em reais, com narrativa de descoberta. A seção "Para executivos" inline em 18.2.3 é útil.
O que ela NÃO entenderia: A fórmula matemática em 18.2.1 (Σ, tokens_in, tokens_out) — não há rampa de acesso. Os percentuais da tabela 18.7 sem a explicação de que não são aditivos vão confundi-la ou fazê-la ignorar a tabela.
Como corrigir: A analogia da conta de energia proposta no Achado 02 resolve o problema de entrada para Joana.

## TESTE DE DURABILIDADE
Classificação: ALTA
2 anos: A fórmula do custo composto com quatro termos, a ordem de implementação T1>T2>T3, o exemplo estrutural da SaaS — tudo sobrevive.
5 anos: O framework sobrevive. Os percentuais específicos ficam como referência histórica.
10 anos: Os princípios de custo composto (multiplicadores, não termos isolados) são durávéis. Este capítulo tem a segunda maior durabilidade depois do C17.
Justificativa: A fórmula e a lógica de ordem de implementação são independentes de qualquer fornecedor ou modelo específico.

## TESTE DE DIFERENCIAÇÃO
Classificação: DIFERENCIADO
Justificativa: A fórmula explícita do custo composto com os quatro termos é genuinamente original na literatura de gestão de IA. A maioria dos guias trata apenas "preço por token" como variável de otimização. A instrução contraintuitiva de atacar tier antes de contexto é diferencial.

## TESTE DE MEMORIZAÇÃO
Ideia principal clara? SIM (mas com atrito)
Qual é a ideia principal: "O preço por token é o termo trivial; o custo real escala pelos multiplicadores de chamadas, redundância e tier — e otimizá-los nessa ordem entrega 60-75% de economia."
Justificativa: A ideia está clara mas exige que o leitor chegue ao exemplo (18.5) para cristalizar. Sem a analogia, muitos leitores vão perder a estrutura da fórmula.

## TESTE DE TRANSFORMAÇÃO
Ao terminar, o leitor consegue fazer o que antes não conseguia:
- Decompor fatura de IA nos quatro termos e identificar qual está sangrando.
- Defender para o time técnico por que começar por roteamento de tier (não por poda de prompt) é a ordem correta.
- Montar o golden set mínimo para validar migração de tier.
- Propor sequência de 8 semanas de otimização estruturada.
- Saber quando parar (quando ganho marginal não paga o tempo de engenharia).

## NOTA FINAL
Estrutura: 6 | Pedagogia: 6 | Clareza: 6 | Autoridade: 7 | Durabilidade: 8 | Diferenciação: 8 | Memorização: 7 | Transformação: 7
**Nota Geral: 6.9**

## DECISÃO EDITORIAL
REVISAR PARCIALMENTE
*Correções críticas: resolver a tabela de percentuais não-aditivos (P0); adicionar analogia de abertura (P1); corrigir item 5 da autoavaliação que é copypaste de outro capítulo (P1); mover aviso metodológico para próximo aos percentuais (P1). O capítulo tem estrutura conceitual sólida mas está incompleto no desenvolvimento pedagógico — é o menos acabado dos cinco.*

---
---

# C19 — L1-C19-seguranca.md

## RESUMO EXECUTIVO
Nota: 8/10
Veredito: A

## O QUE FUNCIONA
- A taxonomia de prompt injection em quatro famílias (direta, indireta via contexto, indireta via tool, multi-turn) é precisa, atualizada com referências a CVE-2025-32711 e ao ataque Crescendo da Microsoft, e durável enquanto arquitetura de LLM não mudar radicalmente.
- A analogia do sistema imune em camadas é a mais tecnicamente precisa das cinco analogias dos capítulos — mapeia de forma justa (cada camada falha em fração de eventos; robustez vem de redundância).
- O Quadro 19.A (OWASP LLM Top 10 com definição, defesa e capítulo de aprofundamento em uma linha cada) é artefato de referência genuinamente útil — o CTO que tiver o quadro na parede vai usá-lo como mapa de decisão de investimento em segurança.
- A seção de red team sistemático (19.5) com as três métricas (taxa de bypass, severidade ponderada, tempo de detecção) é framework concreto que falta em quase todos os livros de IA corporativa.
- O caso do banco (19.6) é o mais rico em detalhe técnico dos cinco capítulos: vetor de ataque identificado (prompt injection indireta via PDF), três falhas de arquitetura compostas, remediação em quatro semanas, custo total do incidente, resultado regulatório. É um caso real-ish que vai ser citado em apresentações.
- A seção de conformidade (19.7) usa a Camada Dupla corretamente: apresenta o padrão durável (classificação por risco, trilha de auditoria, direito à explicação) e delega o texto específico para o Apêndice J.
- A seção 19.8 sobre contratar consultoria é pedagogicamente honesta: lista red flags explícitos que distinguem consultoria séria de teatro.

## O QUE NÃO FUNCIONA
- A referência à ANPD "Nota Técnica de 2026" aparece novamente (como em C16) como documento estabelecido sem data específica ou fonte verificável inline.
- O capítulo é longo (350+ linhas) sem resumo intermediário em cada subseção de 19.3. O leitor que perde o fio em 19.3.4 (model inversion) precisa rolar muito para voltar ao contexto.
- A menção a "EchoLeak (CVE-2025-32711)" como caso público é boa, mas o texto não explica o que é CVE para Joana, e essa é a única referência a CVE no capítulo.
- O checklist (19.10) tem 14 itens — o mais longo dos cinco capítulos. Para Joana, é intimidante. Para o CTO, é útil mas poderia ser dividido em "checklist executivo" (6 itens) e "checklist técnico" (8 itens).
- A frase de abertura da seção 19.3.6 descreve "EchoLeak (CVE-2025-32711)" sem contexto de que CVE é um identificador padronizado de vulnerabilidade. Leitor não-técnico pode não saber o que significa.

---

## ACHADOS

### ACHADO 01
Categoria: P1
Problema: CVE-2025-32711 (EchoLeak) é referenciado como "a CVE pública" sem explicação do que é CVE para o leitor não-técnico. Joana vai ler "CVE-2025-32711" e não saber se é um regulamento, um ataque, um produto ou um padrão.
Por que é um problema: O capítulo é explicitamente voltado para CTO, Head de Segurança E Head de Engenharia — o Head de Engenharia sabe o que é CVE, o CTO de fundo comercial provavelmente não.
Impacto no leitor: Joana (e CTOs não-técnicos) perdem a força do exemplo porque não entendem o que é CVE.
Correção exata: Adicionar definição inline na primeira menção: "(CVE — Common Vulnerabilities and Exposures: identificador público padronizado de vulnerabilidade de segurança; CVE-2025-32711 é o registro oficial do ataque EchoLeak)".
Texto sugerido: `...com o caso público de EchoLeak (CVE-2025-32711 — identificador padronizado de vulnerabilidade pública) ilustrando a classe em ambiente corporativo.`
ROI: MÉDIO

### ACHADO 02
Categoria: P1
Problema: O capítulo tem 350+ linhas de seção técnica (19.3) sem cabeçalhos de resumo intermediário ou "regra prática" no final de cada subseção. O leitor que chega em 19.3.4 (model inversion) depois de ter lido 19.3.1, 2 e 3 está sem âncora de onde está no mapa.
Por que é um problema: A seção 19.3 cobre seis classes de ataque diferentes. Um leitor não-especialista que pausar a leitura vai ter dificuldade de retomar no ponto correto.
Impacto no leitor: Joana lê 19.3.1 (prompt injection) com atenção, chega em 19.3.5 (PII leakage) com fadiga, e para. O capítulo perde a metade mais operacional.
Correção exata: Adicionar "Regra prática para [classe de ataque]:" ao final de cada subseção de 19.3 (como 19.3.1 já tem para as subseções de injeção, mas 19.3.4 e 19.3.5 são mais longas e se beneficiariam). Alternativamente, adicionar mini-sumário no início de 19.3: "Seis classes de ataque, de 19.3.1 a 19.3.6. Leia as que são mais relevantes para o seu contexto — o Quadro 19.A ao final organiza a defesa para cada uma."
Texto sugerido: `> **Mapa de 19.3:** Seis classes de ataque tratadas em sequência: (1) prompt injection, (2) jailbreak, (3) data poisoning, (4) model inversion, (5) PII leakage, (6) tool exploitation. O Quadro 19.A no final do capítulo organiza defesa e aprofundamento para cada uma.`
ROI: MÉDIO

### ACHADO 03
Categoria: P1
Problema: O checklist (19.10) tem 14 itens sem distinção entre itens executivos e itens técnicos. Para um Head de Segurança, 14 itens é gerenciável. Para um CEO ou CFO, é um muro.
Por que é um problema: A rubrica orienta que o capítulo serve para CTO, Head de Segurança e Head de Engenharia — mas a mistura de itens técnicos ("Listar as tools de cada agente e classificá-las em leitura segura ou escrita com efeito") com itens executivos ("Apontar o Accountable nomeado por ativação do kill switch") não diferencia bem os dois públicos.
Impacto no leitor: Executivos descartam o checklist por extensão; técnicos perdem os itens mais estratégicos no meio dos operacionais.
Correção exata: Dividir o checklist em dois blocos: "Checklist executivo (6 itens — para CTO e liderança)" e "Checklist técnico (8 itens — para Head de Segurança e AI Engineer)".
Texto sugerido: n/a (reorganização de estrutura)
ROI: MÉDIO

### ACHADO 04
Categoria: P1
Problema: A "Nota Técnica da ANPD sobre IA generativa" é referenciada em 19.7 como documento estabelecido ("A ANPD publicou orientação específica sobre IA generativa e tratamento de dado pessoal em vigor a partir de 2026") sem data específica ou verificação de que o documento existe exatamente com esse nome e vigência.
Por que é um problema: Igual ao problema em C16 — profissional de compliance que tentar citar o documento pode não encontrá-lo com esse nome exato.
Impacto no leitor: Perde credibilidade em apresentação ao DPO.
Correção exata: Adicionar marcação de verificação: "(Nota Técnica da ANPD — verificar versão corrente e título exato em www.gov.br/anpd conforme Apêndice J — Trilha do Número)"
Texto sugerido: n/a (inline na menção)
ROI: MÉDIO

### ACHADO 05
Categoria: P2
Problema: A regra "cadência mínima viável é trimestral" para red team (19.5) é apresentada como absoluta, mas não considera que organizações em fase inicial sem red team algum têm horizonte diferente de organizações com red team maduro. A regra de "se o último red team foi há mais de noventa dias, a organização não tem red team, tem auditoria pontual antiga" é implacável mas não oferece rota de construção progressiva.
Por que é um problema: Organização em fase inicial lê "não tem red team" e se sente paralisada sem saber como começar.
Impacto no leitor: Paralisia de excelência — "se não posso fazer trimestral, não faço nada".
Correção exata: Adicionar parágrafo de "rota de entrada para organizações sem red team": "Para organizações que nunca fizeram red team, o primeiro objetivo é conduzir a primeira sessão em 90 dias, com suite de 20 casos cobrindo as cinco categorias de maior risco do OWASP LLM Top 10 para o contexto específico. A cadência trimestral é o regime maduro; chegar a ele é processo de dois a três ciclos."
Texto sugerido: (parágrafo acima como inserção após a regra de 90 dias)
ROI: BAIXO

### ACHADO 06
Categoria: P2
Problema: A seção de PII leakage (19.3.5) menciona "Microsoft Presidio" como ferramenta padrão para redaction de PII, sem notar que é uma dependência externa com seu próprio ciclo de vida (o protocolo do capítulo anterior exigiria auditar o repositório do Presidio antes de depender dele).
Por que é um problema: Contradição leve com o método de C17 — o livro recomenda uma ferramenta específica sem aplicar o próprio protocolo de avaliação a ela.
Impacto no leitor: Menor — mas leitores atentos que acabaram de ler C17 vão notar a inconsistência.
Correção exata: Adicionar nota: "(Microsoft Presidio — referência comum em 2026; antes de adotar, aplique o protocolo de trinta minutos do Cap 17 para verificar fase do ciclo de vida)".
Texto sugerido: n/a (inline)
ROI: BAIXO

---

## TESTE DA JOANA
Entenderia: SIM (com atrito em 19.3)
O que ela entenderia: A analogia do sistema imune é imediatamente compreensível. O caso do banco (19.6) vai ser a parte que ela mais lembra — é concreto, tem resolução, tem custo. As perguntas para o time técnico no bloco "Para Executivos" são diretamente usáveis por ela.
O que ela NÃO entenderia: "Differential privacy", "adversarial embedding", "rate limiting por sessão" — termos técnicos que aparecem sem definição suficiente para executivo não-técnico. "CVE-2025-32711" sem explicação do que é CVE.
Como corrigir: Glossário inline para os termos mais técnicos; o Achado 01 já propõe a solução para CVE. Para "differential privacy", uma linha basta: "(técnica que adiciona ruído matemático ao treino para que nenhuma amostra individual do dataset possa ser extraída do modelo)".

## TESTE DE DURABILIDADE
Classificação: ALTA
2 anos: A taxonomia de prompt injection, a arquitetura de defesa em camadas, o Quadro 19.A do OWASP LLM Top 10 — tudo sobrevive. O OWASP vai ter versão 2026 e o capítulo faz isso correto ao referenciar "versão 2025" com data.
5 anos: O modelo do queijo suíço, os seis ataques como classes, a lógica de red team sistemático — todos duráveis. Nomes específicos de ferramentas (Lakera, NeMo Guardrails) podem mudar.
10 anos: Os princípios de defesa em camadas e da separação instrução/dado são duráveis enquanto modelos de linguagem operarem por processamento de tokens. Isso é estrutural.
Justificativa: Este é o capítulo com segunda maior durabilidade depois de C17. A taxonomia de ataques é independente de modelo específico; a arquitetura de defesa é independente de fornecedor.

## TESTE DE DIFERENCIAÇÃO
Classificação: DIFERENCIADO
Justificativa: A combinação de taxonomia de ataques + arquitetura de defesa em sete camadas + framework de red team com três métricas + caso de incidente com custos reais + guia de contratação de consultoria com red flags explícitos — esse pacote não existe em formato equivalente no mercado de livros de gestão de IA. É mais completo que Co-Intelligence (Mollick) e mais aplicado que Competing in the Age of AI (Iansiti/Lakhani).

## TESTE DE MEMORIZAÇÃO
Ideia principal clara? SIM
Qual é a ideia principal: "Defesa de IA mora fora do modelo — em sete camadas externas. A diferença entre incidente contornado e manchete de capa é o tempo de detecção e a maturidade do playbook, construídos antes do ataque."
Justificativa: A epígrafe, a analogia do sistema imune e a lição do caso do banco repetem a mesma ideia em registros diferentes. Memorável.

## TESTE DE TRANSFORMAÇÃO
Ao terminar, o leitor consegue fazer o que antes não conseguia:
- Distinguir prompt injection direta de indireta e saber por que a segunda é mais difícil de defender.
- Mapear o stack de IA da organização contra as dez categorias do OWASP LLM Top 10.
- Estruturar um programa de red team com cadência, composição de equipe e três métricas.
- Redigir o playbook de SEV-1 para vazamento de PII com Accountable nomeado.
- Distinguir consultoria de segurança séria de teatro de pentest tradicional.
- Fazer as três perguntas duras ao time técnico no dia seguinte à leitura.

## NOTA FINAL
Estrutura: 8 | Pedagogia: 7 | Clareza: 7 | Autoridade: 9 | Durabilidade: 9 | Diferenciação: 9 | Memorização: 8 | Transformação: 9
**Nota Geral: 8.3**

## DECISÃO EDITORIAL
MANTER COM AJUSTES
*Correções prioritárias: dividir checklist em executivo + técnico (P1); adicionar mini-mapa de navegação em 19.3 para capítulo longo (P1); definir CVE inline (P1); adicionar marcação de verificação à referência da Nota Técnica da ANPD (P1). O capítulo é sólido — as correções são de acessibilidade, não de conteúdo.*

---
---

# ALERTA DE DURABILIDADE CRUZADO (capítulos 15-19)

## Risco sistêmico detectado

**Catálogos residuais em C15 e C16:** Ambos os capítulos resistem razoavelmente à tese "Modelos passam. Método fica." mas carregam catálogo residual em tabelas de força por família (C15) e em versões específicas de modelos (C16). O risco não é fatal mas requer marcação datada consistente em todas as tabelas com nomes de produto.

**Preços de API em C16 e C18:** Os valores específicos de custo de inferência (Quadro 16.A e referências em C18) são os componentes de maior risco de obsolescência rápida. Em 18 meses, os preços de Claude Sonnet, GPT-4 e Gemini podem ter variado 30-60%. Recomendação: transformar todos os valores específicos de preço em templates com remissão ao Apêndice J.

**"Nota Técnica da ANPD sobre IA generativa de 2026":** Citada em C16 e C19 como documento estabelecido. Risco de o documento não existir com esse nome exato, ter sido revisado, ou ainda estar em consulta pública. Recomendação: verificar a existência e título exato do documento; adicionar marcação de "verificar versão corrente" em toda citação.

**C17 é o modelo correto:** O protocolo de 30 minutos de C17, por ser método puro sem inventário de nomes específicos, é o benchmark editorial que os outros capítulos deveriam aspirar. C15 e C16 ficam abaixo desse padrão por carregarem mais catálogo que necessário.

---

## LINHAS-TRACKER

```
C15|L1-C15-comparacao-modelos.md|01|P0|ALTO|Checklist item 1 instrui memorização de catálogo contradizendo tese do livro|Reformular item para aplicação do framework de decisão sem memorização de família|MANTER COM AJUSTES
C15|L1-C15-comparacao-modelos.md|02|P1|ALTO|Tabela de forças por família fixa associações sem sinalização de volatilidade|Adicionar cabeçalho de aviso datado e instrução de consulta ao Apêndice J|MANTER COM AJUSTES
C15|L1-C15-comparacao-modelos.md|03|P1|MÉDIO|xAI caracterizada por "tolerância maior a temas sensíveis" como vantagem neutra|Reescrever com nota sobre implicações de alignment conforme C23|MANTER COM AJUSTES
C15|L1-C15-comparacao-modelos.md|04|P1|MÉDIO|Lista de chips específicos em 15.6 envelhece sem entregar padrão durável|Reescrever para expressar tendência; colocar exemplos entre parênteses com marcação de snapshot|MANTER COM AJUSTES
C15|L1-C15-comparacao-modelos.md|05|P2|BAIXO|Erro tipográfico "Curiosidade " com espaço antes do fechamento de negrito em 15.14|Remover espaço extra|MANTER COM AJUSTES
C15|L1-C15-comparacao-modelos.md|06|P2|BAIXO|Pergunta de revisão 3 orientada a nomes de produtos específicos|Reformular para perguntar por critérios de encaixe sem nomear modelos|MANTER COM AJUSTES
C16|L1-C16-open-source.md|01|P0|ALTO|Quadro 16.A mostra Híbrido mais caro que API mas recomenda híbrido sem reconciliar|Adicionar explicação de que benefícios não-monetários justificam o custo marginalmente maior|MANTER COM AJUSTES
C16|L1-C16-open-source.md|02|P1|ALTO|Preços específicos de API no Quadro 16.A envelhecem em meses|Transformar em template com remissão ao Apêndice J|MANTER COM AJUSTES
C16|L1-C16-open-source.md|03|P1|MÉDIO|Números de versão de modelos no corpo do texto envelhecem antes da impressão|Remover números de versão do corpo; manter nomes de família com remissão ao Apêndice J|MANTER COM AJUSTES
C16|L1-C16-open-source.md|04|P1|MÉDIO|Nota Técnica ANPD citada como documento estabelecido sem data específica ou verificação|Adicionar marcação de verificação em toda citação|MANTER COM AJUSTES
C16|L1-C16-open-source.md|05|P2|BAIXO|Analogia da frota (16.2) longa demais para ritmo de livro executivo|Comprimir de quatro para dois parágrafos mantendo os quatro pontos|MANTER COM AJUSTES
C16|L1-C16-open-source.md|06|P2|BAIXO|Pergunta de revisão 5 cita "Nota Técnica ANPD de 2026" como dado memorável|Reformular para perguntar pelo padrão regulatório durável não pela data específica|MANTER COM AJUSTES
C17|L1-C17-github-repos.md|01|P1|ALTO|Referência de imagem usa cap-35 sendo o capítulo 17|Corrigir para cap-17 no caminho do arquivo SVG|MANTER COM AJUSTES
C17|L1-C17-github-repos.md|02|P1|MÉDIO|OpenInterpreter caracterizado com "governança em pessoa física com empresa em formação" — informação perecível que contradiz a filosofia do capítulo|Substituir por observação sobre aplicação do protocolo de verificação|MANTER COM AJUSTES
C17|L1-C17-github-repos.md|03|P1|MÉDIO|Regra de CI não exige CI presente — projeto sem CI passa no critério|Reformular para exigir CI presente E verde como critério de aprovação|MANTER COM AJUSTES
C17|L1-C17-github-repos.md|04|P2|BAIXO|W&B descrito sem destaque para implicação de self-hosting restrito|Adicionar frase sobre verificação de encaixe para organizações com restrição regulatória|MANTER COM AJUSTES
C17|L1-C17-github-repos.md|05|P2|BAIXO|Exemplo de 10 horas com 3 pessoas é ambíguo sobre se é 10h total ou por pessoa|Clarificar que é 10h total de sessão coletiva|MANTER COM AJUSTES
C18|L1-C18-economia-tokens.md|01|P0|ALTO|Tabela 18.7 com percentuais não-aditivos que somam mais de 200% sem explicação|Adicionar nota explícita de que os percentuais são compostos sequenciais não aditivos|REVISAR PARCIALMENTE
C18|L1-C18-economia-tokens.md|02|P1|ALTO|Capítulo não tem analogia de abertura para Joana — entra direto na fórmula matemática|Adicionar analogia de conta de energia com quatro termos como 18.2 introdutória|REVISAR PARCIALMENTE
C18|L1-C18-economia-tokens.md|03|P1|ALTO|Autoavaliação item 5 é copypaste de outro capítulo sobre segurança — não tem relação com economia de tokens|Substituir por critério de curiosidade relevante ao capítulo|REVISAR PARCIALMENTE
C18|L1-C18-economia-tokens.md|04|P1|MÉDIO|Framework F7 referenciado três vezes sem definição no capítulo|Adicionar mini-descrição inline na primeira menção|REVISAR PARCIALMENTE
C18|L1-C18-economia-tokens.md|05|P1|MÉDIO|Aviso metodológico de 18.1 está no início do capítulo onde é ignorado|Mover para próximo à tabela de percentuais onde os números aparecem|REVISAR PARCIALMENTE
C18|L1-C18-economia-tokens.md|06|P2|BAIXO|Razão premium/pequeno de "30 a 50 vezes" pode envelhecer com ajustes de pricing|Adicionar remissão ao Apêndice J inline|REVISAR PARCIALMENTE
C19|L1-C19-seguranca.md|01|P1|MÉDIO|CVE-2025-32711 referenciado sem explicação do que é CVE para leitor não-técnico|Adicionar definição inline de CVE na primeira menção|MANTER COM AJUSTES
C19|L1-C19-seguranca.md|02|P1|MÉDIO|Seção 19.3 com 6 classes de ataque sem mini-mapa de navegação intermediário|Adicionar mapa de navegação no início de 19.3 e regras práticas ao final de subseções longas|MANTER COM AJUSTES
C19|L1-C19-seguranca.md|03|P1|MÉDIO|Checklist com 14 itens mistura executivo e técnico sem distinção de público|Dividir em checklist executivo (6 itens) e checklist técnico (8 itens)|MANTER COM AJUSTES
C19|L1-C19-seguranca.md|04|P1|MÉDIO|Nota Técnica ANPD em 19.7 citada como documento estabelecido sem verificação|Adicionar marcação de verificação em toda citação da nota ANPD|MANTER COM AJUSTES
C19|L1-C19-seguranca.md|05|P2|BAIXO|Regra de cadência trimestral de red team sem rota de entrada para organização sem red team|Adicionar parágrafo de construção progressiva para fase inicial|MANTER COM AJUSTES
C19|L1-C19-seguranca.md|06|P2|BAIXO|Microsoft Presidio recomendado sem instrução de aplicar o protocolo de C17|Adicionar nota de verificação conforme protocolo de C17|MANTER COM AJUSTES
```

---

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

---

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

---

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


---

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

---

# APX-L — Biblioteca de Prompts Profissionais

## RESUMO EXECUTIVO
Nota: 6/10
Veredito: B

---

## O QUE FUNCIONA

- **A estratégia de camada dupla (livro + repositório) é intelectualmente honesta.** Separar a ficha conceitual durável do XML executável volátil é a única arquitetura que salva o apêndice de envelhecer com o modelo. A justificativa na introdução é clara e bem argumentada.
- **O Changelog editorial é o melhor trecho do apêndice.** Mostrar iteração real — o que quebrou, por que foi corrigido, qual o impacto no golden set — é raro em livros de negócios e entrega exatamente o que a tese promete: método, não receita. Se houvesse um apêndice inteiro sobre isso, seria superior ao catálogo de fichas.
- **Os sete padrões de operação são transferíveis e duráveis.** Regras como "jamais concatene instrução com dado", "mantenha golden set de 20 casos", "reverifique contra o golden set ao trocar de modelo" — essas sobrevivem à próxima geração porque não dependem de nenhum modelo específico.
- **Os anti-padrões transversais têm alta densidade de utilidade.** São oito padrões de falha observados em campo, com justificativa causal, não apenas lista. Essa seção é citável e memorável.
- **A anatomia comentada do Framework Quatro (F4) é pedagogicamente sólida.** Explicar *por que* cada bloco XML está naquela posição — e não apenas *o que* ele faz — diferencia o conteúdo de um tutorial.
- **Cobertura setorial brasileira é genuinamente diferenciada.** LGPD, CLT, TST, ITR, ANPD, BACEN, ANS — a especificidade regulatória é uma forma real de propriedade intelectual que não existe em equivalentes internacionais do gênero.
- **A cadência de fichas é consistente.** Todos os 30 prompts seguem o mesmo molde de nove campos, o que permite leitura rápida comparada e navegação pontual.

---

## O QUE NÃO FUNCIONA

- **O apêndice é fundamentalmente um catálogo, e a tese do livro proíbe catálogos.** Trinta fichas organizadas por setor (Jurídico, Saúde, Financeiro, SaaS, Suporte, RH, Marketing, Educação, Transversais) com URL de repositório é, formalmente, o tipo de artefato que "Modelos passam. Método fica." deveria rejeitar. A estratégia de camada dupla mitiga o problema, mas não o elimina.
- **"Modelo recomendado: Sonnet equivalente" em 26 das 30 fichas é conteúdo sem informação.** Se 87% das fichas têm a mesma resposta, o campo não está diferenciando nada. É ruído que ocupa espaço conceitual valioso.
- **As métricas de qualidade são afirmações sem sustentação.** "Concordância com advogado sênior em pelo menos 85%" pressupõe golden set calibrado — mas o leitor não tem acesso a ele nem ao critério de seleção do advogado. A métrica parece rigorosa mas é inacessível para verificação.
- **A abertura promete mais do que entrega.** "Trinta fichas que foram desenhados como ativos de produção, com inputs reais, com riscos reais" — mas não há um caso real no apêndice. O único XML é esqueleto genérico. O leitor que veio buscando produção encontra conceito.
- **A estrutura Quando usar / Quando evitar repete padrão óbvio em excesso.** Em muitas fichas, o "Evitar" é trivialmente o inverso do "Usar" (ex: "Usar: triagem preliminar / Evitar: parecer final"). Isso ocupa espaço sem acrescentar discriminação real.
- **O apêndice não ensina o leitor a construir um prompt.** Ele ensina a usar os trinta que já estão no repositório. Isso inverte a lógica de método: o leitor que adaptar um dos 30 sem entender os princípios vai produzir prompt ruim, e o apêndice não o protege disso de forma suficiente.
- **A promessa do repositório é não-verificável no momento da leitura.** O URL aparece 30 vezes, mas se o repositório estiver vazio, com código-stub, ou diferente do prometido, toda a arquitetura colapsa. O leitor não tem como saber isso lendo o livro.

---

## ACHADOS

### ACHADO 01
**Categoria:** P0
**Problema:** Contradição estrutural com a tese central do livro.
**Por que é um problema:** A tese é "Modelos passam. Método fica." e a rubrica instrui a sinalizar explicitamente quando conteúdo transforma o livro em "coleção de prompts". Este apêndice é, na forma, uma coleção de trinta prompts categorizados por setor, com URLs para repositório. A estratégia de camada dupla *mitiga* a contradição mas não a resolve: o leitor que folheia o sumário e chega no Apêndice L vê trinta fichas com nomes como "P-LEG-01", "P-MED-02", "P-FIN-03". Isso é catálogo. A introdução argumenta contra isso, mas o leitor médio não lê introduções de apêndice.
**Impacto no leitor:** Quem chega de fora (resenha, sumário, folhear) conclui que o livro entrega receitas. Isso contradiz o posicionamento de obra de método e autoridade.
**Correção exata:** Duas opções. Opção A (cirúrgica): renomear o apêndice como "Arquitetura de Prompts Profissionais" e transformar a estrutura em três camadas — (1) princípios de design por tipo de tarefa, (2) três fichas completas como exemplos de aplicação, (3) referência para o repositório com os 27 restantes. Opção B (radical): extrair o catálogo inteiro para o repositório e deixar no livro apenas os princípios do Framework Quatro, os sete padrões de operação, os oito anti-padrões transversais e o changelog editorial. O livro ficaria mais coerente com a tese e o repositório ficaria mais completo.
**Texto sugerido:** n/a (intervenção estrutural, não textual)
**ROI:** ALTO

---

### ACHADO 02
**Categoria:** P0
**Problema:** "Modelo recomendado: Sonnet equivalente" em 26/30 fichas é afirmação sem valor informacional.
**Por que é um problema:** Se 87% das fichas têm a mesma resposta, o campo não está discriminando nada. Pior: "Sonnet equivalente" em 2026 pode ser Claude 3.5 Sonnet, GPT-4o, Gemini 1.5 Pro, Mistral Large — sem critério de equivalência definido. O que faz um modelo "equivalente"? Janela de contexto? MMLU? Benchmark jurídico específico? O campo promete especificidade e entrega generalidade.
**Impacto no leitor:** O leitor técnico (que mais usaria essa recomendação) percebe que o campo não foi preenchido com cuidado real. Reduz credibilidade do apêndice inteiro.
**Correção exata:** Ou definir "Sonnet equivalente" com critério operacional verificável na introdução da anatomia (ex: "modelo com contexto mínimo de 100k tokens, desempenho acima de X em benchmark jurídico Y, com suporte a structured output nativo"), ou substituir o campo por "Família de modelo" com três faixas: (1) Haiku equivalente — classificação/triagem de alta volumetria; (2) Sonnet equivalente — raciocínio com estrutura; (3) Sonnet com raciocínio estendido — análise jurídica/médica complexa. Apenas 8 fichas precisariam de nota diferenciada; as 22 restantes seriam "Sonnet equivalente" sem o vazio atual.
**Texto sugerido:** Na seção "A anatomia que toda ficha aplica", após a tabela do F4, adicionar: *"Convenção de modelo: ao longo das fichas, 'Sonnet equivalente' significa modelo com suporte a raciocínio estruturado, janela de contexto de 100k tokens ou mais e structured output nativo. 'Haiku equivalente' significa modelo otimizado para velocidade e custo em tarefas classificatórias de baixa complexidade semântica. A denominação é intencional para sobreviver à próxima geração de modelos — o critério, não o nome."*
**ROI:** MÉDIO

---

### ACHADO 03
**Categoria:** P0
**Problema:** As métricas de qualidade são inacessíveis para verificação independente.
**Por que é um problema:** "Concordância com advogado sênior em pelo menos 85% do golden set" — quem é o advogado sênior? Qual golden set? Com quantos casos? Calibrado como? Em qual modelo? Em que data? A métrica parece rigorosa mas é, na prática, uma afirmação de autoridade não auditável. Em um livro comparado a Superforecasting, onde calibração é central, isso é problema grave.
**Impacto no leitor:** O leitor executivo que citar essa métrica em apresentação interna vai encontrar a primeira pergunta: "de onde veio esse 85%?" e não vai ter resposta. Reduz a autoridade da obra em contexto de uso real.
**Correção exata:** Duas opções. Opção A: tornar as métricas prescrições em vez de afirmações — "Critério de qualidade que você deve exigir: concordância de pelo menos 85% com especialista sênior do domínio em um golden set de 20 casos representativos, com ao menos 5 casos limítrofes". Opção B: referenciar o golden set público no repositório, mostrando que o critério foi aplicado em condições reais documentadas. Se o repositório já tem os 20 casos calibrados, dizer isso explicitamente.
**Texto sugerido:** n/a (depende de qual opção o autor escolhe)
**ROI:** ALTO

---

### ACHADO 04
**Categoria:** P1
**Problema:** O apêndice não ensina a construir um prompt novo — apenas a usar os 30 existentes.
**Por que é um problema:** Um leitor que termina o apêndice sabe identificar qual dos 30 prompts é mais próximo do seu problema e sabe adaptar o conteúdo entre as tags (como o padrão 2 instrui). Mas se o problema do leitor for o prompt 31 — um que não está na lista — ele não sabe construir do zero. Os princípios estão dispersos (F4 na anatomia, padrões de operação, anti-padrões transversais) mas nunca são reunidos em um método explícito de construção.
**Impacto no leitor:** O leitor sai com biblioteca, não com método de biblioteca. A tese exige o contrário.
**Correção exata:** Adicionar, antes das 30 fichas, uma seção "Como construir um prompt que não está nesta lista" com 8 a 10 passos que combinam F4 + padrões de operação + anti-padrões transversais em sequência construtiva. Isso transforma o apêndice de catálogo em método com exemplos.
**Texto sugerido:** n/a (nova seção, conteúdo a criar)
**ROI:** ALTO

---

### ACHADO 05
**Categoria:** P1
**Problema:** A promessa do repositório é o ponto mais frágil do apêndice — e não há fallback declarado.
**Por que é um problema:** O apêndice é projetado como camada 1 de uma arquitetura de duas camadas. Se a camada 2 (repositório) não existir, estiver incompleta ou estiver desatualizada, o leitor que foi instruído a ir ao repositório "para a versão executável" encontra nada. Não há nota de quando o repositório foi populado, qual versão corresponde ao livro, ou o que fazer se o link estiver morto.
**Impacto no leitor:** Um leitor frustrado com repositório vazio ou desatualizado vai revisar a avaliação do livro inteiro para baixo. Em 2026, repositórios GitHub abandonados são comuns.
**Correção exata:** Adicionar no quadro de orientação da introdução uma linha explícita de SLA do repositório — ex: "Política de manutenção: o repositório é mantido ativo e com os 30 prompts populados enquanto o livro estiver em catálogo." E adicionar uma nota em cada ficha com a data de última verificação da versão executável.
**Texto sugerido:** No quadro de orientação, adicionar linha: *"Repositório público: [URL] · Política de manutenção: populado e auditado a cada release do livro. Se o link não funcionar, acesse [email/formulário alternativo]."*
**ROI:** MÉDIO

---

### ACHADO 06
**Categoria:** P1
**Problema:** A estrutura "Quando usar / Quando evitar" repete o óbvio em excesso e ocupa espaço que poderia ser usado para distinção real.
**Por que é um problema:** Em P-LEG-01: "Usar: Triagem de contratos novos / Evitar: Parecer final em litígio." Em P-LEG-02: "Usar: Revisão preliminar / Evitar: Parecer final sobre validade jurídica." Em P-LEG-04: "Usar: Auditoria interna / Evitar: Parecer técnico em contencioso." O padrão geral é "Usar para triagem / Evitar para decisão final" — que é a regra geral de todo prompt bem-desenhado, não uma característica específica de cada prompt. Apenas 8 a 10 fichas têm critérios realmente diferenciadores nessa seção.
**Impacto no leitor:** O leitor aprende a regra geral na segunda ficha e para de ler os quadros. Espaço desperdiçado que poderia ser casos de borda reais.
**Correção exata:** Transformar o campo em "Casos de borda" — situações não óbvias em que o prompt funciona melhor ou pior que o esperado. A regra geral (não use para decisão final) entra na introdução da anatomia uma única vez.
**Texto sugerido:** Substituir o cabeçalho "Quando usar e quando evitar" por "Casos de borda e limites não óbvios", e instrução ao autor para preencher apenas com situações que surpreendem — não com a regra geral.
**ROI:** MÉDIO

---

### ACHADO 07
**Categoria:** P1
**Problema:** P-MED-03 (Alerta de Interação Medicamentosa) tem risco regulatório não declarado que é estruturalmente diferente dos outros prompts de saúde.
**Por que é um problema:** Os prompts P-MED-01 e P-MED-02 são claros sobre seus limites (orientação leiga, fidelidade ao registro). P-MED-03 opera em território de decisão clínica — sinalizar "interação contraindicada" com "necessita validação farmacêutica" pode criar falsa sensação de segurança se usado fora de ambiente hospitalar supervisionado. A ficha não menciona responsabilidade regulatória do operador, CFM, CFF ou CFP, nem distingue uso hospitalar de uso em farmácia de bairro ou app de saúde B2C.
**Impacto no leitor:** Um empreendedor lendo a ficha pode construir um app de verificação de interações para consumidor final, citando o livro como base. Risco real de uso indevido.
**Correção exata:** Adicionar em "Quando evitar": "Uso B2C direto ao consumidor sem supervisão farmacêutica — regulatoriamente restrito no Brasil (CFF). Uso em prescrição pediátrica sem ajuste etário validado por farmacêutico. Ambiente fora de estabelecimento de saúde regulado."
**Texto sugerido:** *"Este prompt é desenhado para uso institucional sob supervisão farmacêutica, não para acesso direto do paciente. O uso em app B2C sem farmacêutico responsável configura, no Brasil, exercício irregular de atividade farmacêutica (CFF)."*
**ROI:** ALTO

---

### ACHADO 08
**Categoria:** P1
**Problema:** P-FIN-02 (Risco de Crédito PF) não menciona a Resolução CMN 4.557/2017 e a necessidade de explicabilidade do modelo de crédito exigida pelo BACEN.
**Por que é um problema:** Em 2026, instituições financeiras sob regulação BACEN precisam de sistemas de crédito com grau explicável de tomada de decisão. O prompt entrega classificação com fatores determinantes, o que é positivo — mas não menciona que o uso do output precisa ser documentado de forma que permita contestação pelo cliente (direito de conhecer a razão de recusa, previsto na LGPD art. 20 e nas normas BACEN). Um DPO lendo a ficha deveria ser alertado disso.
**Impacto no leitor:** O leitor de fintech que adotar o prompt sem essa nota pode estar em não-conformidade regulatória sem saber.
**Correção exata:** Adicionar em "Anti-padrões observados": "Usar o output sem registro auditável do fator determinante — o direito do titular à explicação da decisão de crédito está previsto na LGPD art. 20 e em normas BACEN."
**Texto sugerido:** n/a (adição pontual na lista de anti-padrões)
**ROI:** ALTO

---

### ACHADO 09
**Categoria:** P1
**Problema:** O Changelog editorial trata apenas seis prompts e está no final do apêndice, depois das 30 fichas.
**Por que é um problema:** O Changelog é o conteúdo mais valioso do apêndice do ponto de vista da tese. Ele mostra método de iteração, não produto final. Mas 96% dos leitores nunca vão chegar lá — estão na página 1600 de um apêndice que começa na 1. E os 24 prompts sem changelog aparecem como se tivessem saído prontos, sem cicatriz de iteração.
**Impacto no leitor:** A narrativa implícita dos 24 prompts sem changelog é "este prompt é definitivo". Isso contradiz os padrões de operação (reverifique ao trocar de modelo) e a filosofia do apêndice.
**Correção exata:** Mover o Changelog para a introdução, antes das fichas, como "O que este apêndice aprendeu" — e expandir para 10 a 12 casos. Isso ancora metodologicamente todo o catálogo antes de o leitor entrar nas fichas.
**Texto sugerido:** n/a (reorganização estrutural)
**ROI:** ALTO

---

### ACHADO 10
**Categoria:** P1
**Problema:** Nenhuma ficha menciona o comportamento esperado quando o modelo recusa a tarefa por política de conteúdo.
**Por que é um problema:** Em contextos reais de produção, modelos recusam tarefas. P-MED-03 (interações medicamentosas) e P-LEG-03 (M&A) são exemplos onde provedores como Anthropic ou OpenAI podem inserir recusas não esperadas dependendo de como o input chega. Nenhuma ficha instrui o operador sobre o que fazer quando isso acontece — rewrite do prompt? Fallback para humano? Log de recusa?
**Impacto no leitor:** Em produção, a primeira recusa inesperada quebra o pipeline e o operador não tem guia.
**Correção exata:** Adicionar um oitavo padrão de operação: "Mantenha registro de recusas do modelo por categoria de input. Uma taxa de recusa acima de N% em uma categoria específica indica ou ambiguidade no prompt ou mudança de política do modelo — ambos exigem ação."
**Texto sugerido:** *"8. Monitore recusas por categoria. Quando o modelo recusar a tarefa — seja por policy de conteúdo, seja por input fora do escopo da constituição — registre o motivo literal da recusa, o input que a gerou e o modelo/versão em uso. Taxa de recusa acima de 5% numa categoria específica é sinal de alarme que exige revisão da constituição ou do contexto."*
**ROI:** MÉDIO

---

### ACHADO 11
**Categoria:** P1
**Problema:** P-RH-01 (Triagem de Currículo) não menciona a exigência de auditoria de viés algorítmico que é tendência regulatória clara no Brasil e global.
**Por que é um problema:** Em 2026, recrutamento algorítmico está sob escrutínio crescente da ANPD e de tribunais trabalhistas. O prompt instrui a não usar variáveis vedadas, o que é correto, mas não instrui o operador a manter log de decisões de triagem com auditoria de viés — exigência provável em horizonte de 1 a 2 anos no Brasil, já presente na EU AI Act para sistemas de alto risco em emprego.
**Impacto no leitor:** Uma empresa que usar o prompt sem log auditável pode ter problema regulatório não antecipado.
**Correção exata:** Adicionar em "Anti-padrões observados": "Não manter log auditável de triagens realizadas com variáveis e pontuação registradas — em domínio regulado, auditoria de viés algorítmico exige rastreabilidade completa."
**Texto sugerido:** n/a (adição pontual)
**ROI:** MÉDIO

---

### ACHADO 12
**Categoria:** P2
**Problema:** A introdução usa o verbo "materializa" para descrever o Princípio Três (Camada Dupla), mas o Princípio Três não é identificado em lugar algum no texto com esse número ou nome.
**Por que é um problema:** "Essa separação é deliberada e materializa o Princípio Três, a Camada Dupla." Se o leitor não passou pelo capítulo onde esse princípio é definido — ou se o leitor lê o apêndice isoladamente — a referência flutua sem ancoragem.
**Impacto no leitor:** Leve desorientação. Joana não sabe o que é o Princípio Três.
**Correção exata:** Adicionar entre parênteses ou como nota de rodapé: "(ver Capítulo X)".
**Texto sugerido:** *"...materializa o Princípio Três, a Camada Dupla (Capítulo X)."*
**ROI:** BAIXO

---

### ACHADO 13
**Categoria:** P2
**Problema:** O campo "Versão executável" em cada ficha tem formato de link markdown mas é referência de repositório que pode ou não estar ativa. Em formato impresso ou PDF estático, o link não é clicável e o URL é longo.
**Por que é um problema:** "prompts/P-LEG-01-clausula-nao-concorrencia-clt" — em formato impresso, o leitor precisa digitar a URL base mais o caminho. Nenhum QR code ou URL encurtado é oferecido.
**Impacto no leitor:** Fricção de acesso em formato não-digital.
**Correção exata:** Adicionar uma URL base única ao início do apêndice: "github.com/falercia/inteligencia-aumentada-recursos" e nos campos de versão executável usar apenas o identificador curto: "P-LEG-01".
**Texto sugerido:** n/a (simplificação de formato)
**ROI:** BAIXO

---

### ACHADO 14
**Categoria:** P2
**Problema:** P-MKT-01 (Copy A/B Testável) menciona "Google Ads, Meta Ads, e-mail, LinkedIn, in-app" — todos com limites de caracteres distintos que mudam frequentemente.
**Por que é um problema:** Os limites de caracteres do Google Ads, Meta e LinkedIn são atualizados periodicamente pelas plataformas. Qualquer referência a esses limites no livro impresso envelhece no próximo ciclo de atualização das plataformas.
**Impacto no leitor:** Limite de 30 caracteres no headline do Google Ads hoje pode ser 40 amanhã. O livro fica errado.
**Correção exata:** O campo "Contexto" da ficha já instrui a incluir "limite de caracteres" como variável dinâmica — isso está correto. Mas o texto da ficha não deveria mencionar canais específicos como se fossem estáticos. Substituir a lista por "canais digitais com limite declarado pelo operador".
**Texto sugerido:** *"Domínio: copy para canais digitais com limite de caracteres declarado pelo operador. O prompt recebe o limite como variável dinâmica, sem assumir padrão fixo por plataforma — os limites mudam com frequência e o repositório mantém referência atualizada."*
**ROI:** BAIXO

---

## TESTE DA JOANA
**Entenderia:** PARCIALMENTE
**O que ela entenderia:** A estrutura geral — que existem 30 fichas organizadas por setor, que cada uma diz o que o prompt faz e quando usar. Ela conseguiria ir diretamente à seção de interesse (jurídico, RH) e ler a ficha em 90 segundos como prometido.
**O que ela NÃO entenderia:** O que é o Framework Quatro (F4) e por que importa a ordem das tags XML. A tabela da anatomia (persona, constituição, contexto, tarefa, formato_saida) pressupõe que o leitor já entende o que é um prompt de sistema — Joana pode não saber. A diferença entre "presença com risco" e "ausente" em P-LEG-01 (elementos do TST) é técnico-jurídica sem explicação. A instrução de "verificar contra golden set ao trocar de modelo" não é explicada para quem não sabe o que é regressão automatizada.
**Como corrigir:** Adicionar um glossário de três termos na introdução da anatomia: golden set (o que é, por que importa), constituição do prompt (analogia ao edital — regras que não podem ser violadas), e self-critique (por que o modelo precisa se revisar antes de devolver). Três parágrafos de 3 linhas cada são suficientes.

---

## TESTE DE DURABILIDADE
**Classificação:** MÉDIA
**2 anos:** As fichas conceituais sobrevivem bem. Os padrões de operação e anti-padrões transversais sobrevivem bem. Os campos "Modelo recomendado" envelhecem já em 2026-2027 quando a próxima geração de modelos chegar.
**5 anos:** A estrutura F4 (persona/constituição/contexto/tarefa/formato) é durável enquanto LLMs continuarem operando com system prompt. Se a interface mudar radicalmente (ex: agentes sem prompt estruturado), parte da anatomia fica obsoleta.
**10 anos:** Incerto. Os princípios (separar instrução de dado, manter golden set, versionar) provavelmente sobrevivem. A especificidade regulatória (CLT, TST, LGPD) pode mudar com reformas legislativas.
**Justificativa:** O que mais envelhece: nomes de modelos ("Sonnet equivalente"), referências a plataformas (Google Ads, Meta), número de prompts (trinta — qualquer revisão do livro precisa atualizar este número). O que menos envelhece: a lógica de camada dupla, os sete padrões de operação, o changelog editorial como prática, a anatomia F4.

---

## TESTE DE DIFERENCIAÇÃO
**Classificação:** DIFERENCIADO (com asterisco)
**Justificativa:** A especificidade regulatória brasileira (LGPD, CLT, ITR, ANPD, BACEN, CFF) é genuinamente diferenciadora — não existe equivalente com esse nível de aterramento em publicações de língua inglesa. A estratégia de camada dupla (livro + repositório) também é diferenciadora como arquitetura editorial. O asterisco: na *forma* de catálogo, o apêndice é commodity (listas de prompts por setor existem aos milhares no internet). A diferenciação está na *profundidade* de cada ficha — mas o leitor médio que folheia não percebe a profundidade antes de decidir se o livro é relevante para ele.

---

## TESTE DE MEMORIZAÇÃO
**Ideia principal clara?** NÃO
**Qual é a ideia principal (em 1 frase):** Não é possível responder em 1 frase — o apêndice tem duas ideias em tensão: "aqui está como construir prompts duráveis" (método) e "aqui estão 30 prompts prontos" (catálogo).
**Justificativa:** O leitor que sai do apêndice lembra das fichas, não do método. A ideia mais memorável acaba sendo a estrutura F4 (persona/constituição/contexto/tarefa/formato) — mas ela está enterrada na introdução e não é repetida nas fichas de forma a reforçar o conceito. O Changelog editorial é a segunda coisa mais memorável — e está no final.

---

## TESTE DE TRANSFORMAÇÃO
**Ao terminar, o leitor consegue fazer o que antes não conseguia:**
- Identificar qual dos 30 prompts é mais adequado para um problema específico e adaptar o contexto para o seu cenário
- Estruturar um prompt com os cinco blocos F4 na ordem correta e com separação clara entre instrução e dado
- Montar um golden set básico para testar regressão quando o modelo for atualizado
- Reconhecer os oito anti-padrões transversais na revisão de um prompt existente
- Interpretar o changelog editorial de um prompt como evidência de maturidade operacional, não de falha

**O que o leitor ainda NÃO consegue fazer (problema não resolvido):**
- Construir um prompt novo que não seja adaptação de um dos 30 — o apêndice não ensina design from scratch
- Avaliar se um modelo específico é adequado para uma tarefa específica sem depender do campo "Modelo recomendado" (que é vago)
- Calcular o custo real de operacionalizar um prompt em produção (falta integração com Apêndice J, mencionado no quadro de orientação mas não referenciado em nenhuma ficha individualmente)

---

## NOTA FINAL (0-10 cada eixo)
Estrutura: 7 | Pedagogia: 5 | Clareza: 7 | Autoridade: 6 | Durabilidade: 6 | Diferenciação: 7 | Memorização: 5 | Transformação: 6
**Nota Geral: 6**

## DECISÃO EDITORIAL
**REVISAR PARCIALMENTE**

Prioridade 1: Resolver a contradição com a tese (Achado 01) — seja pela Opção A (compactar para 3 fichas exemplo + repositório) ou pela Opção B (extrair o catálogo, manter o método).
Prioridade 2: Tornar as métricas de qualidade verificáveis ou transformá-las em prescrições (Achado 03).
Prioridade 3: Mover o Changelog para a abertura (Achado 09) — isso custa zero e eleva o apêndice de catálogo para método com cicatriz.
O apêndice tem material genuinamente bom disperso em uma estrutura que o posiciona errado. A revisão não precisa ser de volume — precisa ser de arquitetura.

---

---

# APX-P — Boxes Técnicos

## RESUMO EXECUTIVO
Nota: 8/10
Veredito: A

---

## O QUE FUNCIONA

- **A estrutura de sete blocos por box é exemplarmente consistente e pedagogicamente eficaz.** Por que existe / Conceito intuitivo / Analogia / Mecanismo técnico / Implicação executiva / Quando importa para o leitor brasileiro / Onde aprofundar — essa sequência não foi escolhida por decoração. Ela vai do "preciso me preocupar?" ao "o que isso muda na minha decisão" sem saltar etapas.
- **As analogias são genuinamente boas.** A consultoria com 200 especialistas para MoE, o sócio sênior revisando o estagiário para Speculative Decoding, o auditor com planilha lateral para KV Cache, o cozinheiro com despensa para FlashAttention — cada uma captura a propriedade estruturalmente relevante da técnica sem falsificar a mecânica.
- **A seção "Quando importa para o leitor brasileiro" é propriedade intelectual real.** Nenhum livro em inglês conecta MoE a deploy on-prem em fintechs reguladas brasileiras, FlashAttention a análise de contratos de M&A em português, ou quantização a servidores DGX herdados de datacenters brasileiros. Esse aterramento é diferenciador genuíno.
- **O Box 11 (Matriz de Interações) é o melhor conteúdo técnico do apêndice.** A matriz triangular com os três tipos de relação (sinergia, trade-off, conflito) e os oito pares aprofundados resolve exatamente o problema que o Box 11 identifica: "a decisão real vive nas zonas de fricção entre conceitos". Especialmente as interações 4 (Speculative Decoding × Reasoning Models), 6 (Structured Output × Faithfulness de CoT) e 7 (Mech Interp × Quantização) são conteúdo não encontrável em forma tão acessível na literatura.
- **As referências primárias são precisas e verificáveis.** Os papers citados têm autores, ano, venue e URL de arXiv — padrão comparável a Co-Intelligence e Designing Data-Intensive Applications. Isso constrói autoridade.
- **A precisão técnica é alta para um livro de negócios.** A descrição de grammar-constrained decoding, o algoritmo de speculative sampling com correção de distribuição, a fórmula de crescimento do KV cache, a lógica de superposição em sparse autoencoders — tudo está tecnicamente correto ao nível de profundidade escolhido.
- **O tom "implicação executiva" é calibrado.** Em nenhum momento o apêndice cai no erro oposto de subestimar o leitor — as implicações são concretas, prescritivas e diretamente acionáveis sem ser simplistas.

---

## O QUE NÃO FUNCIONA

- **Box 4 (FlashAttention) menciona "Claude 4 Sonnet" como exemplo de modelo com contexto longo** — nome que não existe no portfólio da Anthropic até a data desta revisão. É erro factual que compromete credibilidade.
- **Box 10 (Scaling Laws) é o mais frágil** porque sua "implicação executiva" central — platô em modelos frontier — é a afirmação mais dependente de data de todos os boxes. Se a próxima geração de modelos produzir salto de qualidade relevante, toda a seção sobre "retorno marginal decrescente" precisa ser reescrita.
- **A Interação 3 (FlashAttention × Scaling Laws) no Box 11 contém um non sequitur**: a lógica salta de "FlashAttention torna viável aumentar contexto" para "scaling laws em platô" como se a segunda fosse consequência da primeira. Não são causalmente conectados da forma que o texto sugere.
- **Box 9 (Interpretabilidade Mecanicista) é ligeiramente mais longo que os outros** sem justificativa pedagógica — o mecanismo técnico tem três frentes (superposição, attribution graphs, monossemanticidade) que poderiam ser comprimidas sem perda para o leitor executivo.
- **O Box 11 usa emojis (🔴🟢🟡⚪) na matriz** — em versão impressa em preto e branco, as cores são invisíveis e a tabela perde toda a informação visual. Não há legenda textual alternativa para impressão monocromática.

---

## ACHADOS

### ACHADO 01
**Categoria:** P0
**Problema:** Box 4 cita "Claude 4 Sonnet" como exemplo de modelo com janela de contexto longa.
**Por que é um problema:** "Claude 4 Sonnet" não é um modelo existente no portfólio da Anthropic em junho de 2026. O portfólio atual inclui Claude 3.5 Sonnet, Claude 3 Opus, Claude 3 Haiku e variantes do Claude 3.5/3.7. Citar um modelo inexistente num livro de autoridade técnica é erro factual que será notado imediatamente por qualquer leitor técnico.
**Impacto no leitor:** Reduz credibilidade de todo o apêndice — se o autor errou o nome de um modelo da Anthropic (a empresa que publica o livro), o que mais pode estar errado?
**Correção exata:** Verificar o portfólio atual da Anthropic, substituir "Claude 4 Sonnet" pelo modelo correto ou remover o nome e usar apenas "Claude (versão atual)" para preservar durabilidade.
**Texto sugerido:** *"...janelas de contexto de duzentos mil a um milhão de tokens, que aparecem como spec sheet em Gemini 1.5, Claude 3.5 Sonnet e GPT-4 Turbo, não foram resultado de uma descoberta teórica..."* (verificar versão correta do Claude antes de publicar)
**ROI:** ALTO

---

### ACHADO 02
**Categoria:** P0
**Problema:** Box 10 (Scaling Laws) tem sua implicação executiva central construída sobre um estado de facto extremamente frágil.
**Por que é um problema:** "A expectativa de que próximas gerações de modelos serão dramaticamente melhores apenas por escala bruta deve ser calibrada para baixo" — essa afirmação estava correta em 2024-2025, mas o campo de IA tem histórico de invalidar conclusões de platô com velocidade surpreendente (GPT-4 apareceu depois de meses de debate sobre limites de GPT-3). O livro está sendo escrito para sobreviver, mas a implicação executiva do Box 10 pode ser invalidada antes do fim do primeiro ciclo de vendas.
**Impacto no leitor:** Um executivo que tomar decisão de stack baseado em "platô de qualidade nos próximos 3 anos" e encontrar GPT-5 ou Claude 4 com salto de qualidade relevante vai associar o livro a conselho errado.
**Correção exata:** Reescrever a implicação executiva para ser epistemicamente honesta sobre a incerteza: "Historicamente, previsões de platô em IA têm sido invalidadas. A regra mais segura é arquitetar para capturar ganhos incrementais certos hoje, enquanto mantém arquitetura suficientemente modular para absorver saltos de qualidade imprevistos. Isso é diferente de apostar em salto — ou em platô."
**Texto sugerido:** *"A regra prática para quem decide em 2026 não é assumir platô nem assumir salto: é desenhar arquitetura que extrai valor dos modelos atuais com elegância e pode ser atualizada com custo baixo quando — não se — a fronteira mover. Os ganhos por geração estão se tornando mais dependentes de inovações em dados e arquitetura do que de escala bruta, mas a velocidade dessas inovações não é previsível com a precisão que uma decisão de investimento exige."*
**ROI:** ALTO

---

### ACHADO 03
**Categoria:** P1
**Problema:** A Interação 3 (FlashAttention × Scaling Laws) no Box 11 conecta causalmente dois fenômenos que são correlatos, não causais.
**Por que é um problema:** O texto afirma que FlashAttention "amplifica scaling laws" e depois conclui que "investir na ponta da escala virou aposta com retorno marginal decrescente". Mas o platô em scaling laws não é causado por FlashAttention — é causado por esgotamento de dados de alta qualidade e pela curva de retorno de parâmetros. FlashAttention e scaling laws são fenômenos independentes que o Box 11 conecta de forma que sugere causalidade onde há apenas co-ocorrência temporal.
**Impacto no leitor:** O leitor técnico que conhece ambos os fenômenos percebe o erro lógico e questiona a qualidade da análise das outras interações.
**Correção exata:** Separar os dois fenômenos. FlashAttention permite contextos longos com custo controlado — isso é sinergia com qualquer escala que use contexto longo. O platô em scaling laws tem causa independente (dados, não compute). Reescrever a interação para refletir isso.
**Texto sugerido:** *"FlashAttention torna economicamente viável o que parecia computacionalmente proibitivo em contextos longos. O platô observado em qualidade de modelos frontier desde 2024, porém, não é consequência de FlashAttention — é consequência do esgotamento de dados humanos de alta qualidade e do retorno decrescente de parâmetros além de certo limiar. Para o decisor, essas são duas alavancas diferentes: FlashAttention reduz custo por token gerado em contextos longos (sinergia com contextos ricos), enquanto a curva de scaling informa que comprar mais parâmetros rende menos por dólar. Otimize as duas de forma independente."*
**ROI:** MÉDIO

---

### ACHADO 04
**Categoria:** P1
**Problema:** Box 1 (MoE) menciona "tiebreak leakage (Hayes et al., outubro de 2024)" como risco de segurança — mas não informa se esse risco foi mitigado nos modelos frontier atuais.
**Por que é um problema:** Em 2026, provedores como Anthropic e OpenAI rodam modelos MoE em ambientes multi-tenant com isolamento. Se o tiebreak leakage foi mitigado nos serving stacks dos provedores principais, mencionar ele sem atualização de status cria alarme desnecessário e pode dissuadir o leitor de adotar MoE por razão que já não existe.
**Impacto no leitor:** Um CISO que leia este box pode bloquear adoção de MoE por risco que já foi mitigado no provedor que estava considerando.
**Correção exata:** Adicionar após a descrição do risco: "Em ambientes de API pública, esses riscos são gerenciados pelos provedores na camada de serving. Para deploys on-prem com modelo open weights, o risco permanece relevante e exige isolamento explícito de batch entre tenants."
**Texto sugerido:** *"Os riscos de tiebreak leakage e expert silencing são relevantes principalmente em deploy on-prem e em ambientes multi-tenant gerenciados diretamente pelo operador. Em APIs gerenciadas pelos provedores frontier, o isolamento de batch e o monitoramento de serving são responsabilidade do provedor — embora valha confirmar com o fornecedor quais salvaguardas estão em vigor antes de processar dados sensíveis em ambiente compartilhado."*
**ROI:** MÉDIO

---

### ACHADO 05
**Categoria:** P1
**Problema:** Box 11 usa emojis coloridos (🔴🟢🟡⚪) como única codificação da matriz de interações. Em impressão monocromática, todos os símbolos ficam visualmente idênticos.
**Por que é um problema:** Um livro técnico sério publicado em versão impressa não pode ter sua informação central (a matriz de interações do Box 11 é o coração do apêndice) depender de renderização colorida para ser legível.
**Impacto no leitor:** Em formato impresso em escala de cinza — como muitas impressões de e-book ou cópia física de baixo custo — a matriz é ilegível.
**Correção exata:** Substituir os emojis por marcadores textuais com legenda dupla. Exemplo: C (conflito), S (sinergia), T (trade-off), N (neutro). Manter os emojis como complemento visual, não como única codificação.
**Texto sugerido:** Substituir cabeçalho da legenda para: "C = conflito / S = sinergia / T = trade-off / N = neutro" e adicionar coluna de legenda equivalente na matriz.
**ROI:** MÉDIO

---

### ACHADO 06
**Categoria:** P1
**Problema:** Box 8 (Faithfulness de CoT) menciona "trabalho de seguimento sobre intervenções causais em CoT, 2024-2025" na seção "Onde aprofundar" sem citar paper específico.
**Por que é um problema:** A seção de referências de todos os outros boxes cita papers com autores, título, venue e URL. A referência vaga "trabalho de seguimento, 2024-2025" quebra o padrão e deixa o leitor sem caminho de aprofundamento real.
**Impacto no leitor:** O leitor técnico que quiser se aprofundar nessa linha específica (que é a mais recente e a mais relevante para aplicação prática) não tem onde ir.
**Correção exata:** Substituir a referência vaga por pelo menos dois papers específicos de 2024-2025 sobre faithfulness de CoT ou causal CoT training. Se nenhum paper específico existir, remover a referência e adicionar: "Esta linha de pesquisa está em desenvolvimento ativo; acompanhe publicações do ACL 2024-2025 e EMNLP 2024."
**Texto sugerido:** n/a (requer pesquisa de papers específicos)
**ROI:** BAIXO

---

### ACHADO 07
**Categoria:** P1
**Problema:** Box 5 (LoRA e PEFT) menciona "S-LoRA" (serving multi-tenant com dezenas de adaptadores) sem citar a referência primária.
**Por que é um problema:** S-LoRA foi formalizado em paper específico (Sheng et al., 2023). Todos os outros conceitos têm referência primária — S-LoRA é citado em passagem de texto sem ancoragem bibliográfica.
**Impacto no leitor:** Leitor que quiser implementar S-LoRA em produção não tem onde começar.
**Correção exata:** Adicionar na seção "Onde aprofundar" do Box 5: "S-LoRA: Sheng et al. *'S-LoRA: Serving Thousands of Concurrent LoRA Adapters'*. 2023. → arxiv.org/abs/2311.03285."
**Texto sugerido:** n/a (adição de referência)
**ROI:** BAIXO

---

### ACHADO 08
**Categoria:** P2
**Problema:** Box 6 (Quantização e Destilação) menciona "Phi-3, da Microsoft" e "Gemini Nano" como exemplos de modelos destilados — mas não menciona DeepSeek-R1-Distill, que é o caso mais relevante de destilação em 2025 e o mais próximo do público-alvo brasileiro (open weights, custo baixo).
**Por que é um problema:** Phi-3 e Gemini Nano são exemplos corretos mas datados. DeepSeek-R1-Distill demonstrou capacidade de reasoning próxima a modelos frontier em modelo destilado de 7B — caso muito mais impactante para a implicação executiva do box.
**Impacto no leitor:** O leitor de fintech ou jurídico que decide entre modelos open weights em 2026 tem DeepSeek como referência primária, não Phi-3.
**Correção exata:** Adicionar DeepSeek-R1-Distill como exemplo na seção de mecanismo técnico e incluir referência correspondente.
**Texto sugerido:** *"...Modelos como Phi-3, da Microsoft, Gemini Nano e a família DeepSeek-R1-Distill são exemplos públicos de modelos pequenos treinados com destilação intensiva a partir de modelos maiores, atingindo qualidade impressionante para seu tamanho — em particular em tarefas de raciocínio estruturado."*
**ROI:** BAIXO

---

### ACHADO 09
**Categoria:** P2
**Problema:** A epígrafe final do apêndice ("Cada um destes boxes existe porque algum executivo, em algum lugar, tomou uma decisão de stack sem saber o que estava escolhendo") é o único momento de voz autoral no texto — e está em formato de nota de rodapé em itálico no final.
**Por que é um problema:** É a frase mais memorável do apêndice inteiro e está enterrada onde ninguém vai encontrá-la.
**Impacto no leitor:** Desperdício de conteúdo. Se essa frase estivesse na abertura, mudaria o enquadramento de como o leitor leria os boxes.
**Correção exata:** Mover essa frase para a abertura do apêndice ("Como usar este apêndice"), como primeira frase ou última frase do primeiro parágrafo.
**Texto sugerido:** Mover como está: *"Cada um destes boxes existe porque algum executivo, em algum lugar, tomou uma decisão de stack sem saber o que estava escolhendo. Que a próxima decisão seja melhor informada."*
**ROI:** BAIXO

---

### ACHADO 10
**Categoria:** P2
**Problema:** O "Mapa de boxes" na tabela inicial referencia princípios como "P5 — Custo Composto" e "P7 — Termômetro" sem que o leitor saiba onde esses princípios estão definidos.
**Por que é um problema:** Um leitor que chega ao Apêndice P sem ter lido os capítulos 1-3 (como a introdução admite que pode acontecer) não sabe o que é "P1 — Plausibilidade" ou "P2 — Extremidades". A tabela assume familiaridade com nomenclatura interna da obra.
**Impacto no leitor:** Joana, lendo o mapa antes dos boxes, não consegue usar a coluna "Princípio relacionado" como orientação.
**Correção exata:** Adicionar nota de rodapé abaixo da tabela: "Os Princípios (P1 a P9) são definidos no Capítulo X e resumidos no Apêndice Y."
**Texto sugerido:** n/a (adição de nota)
**ROI:** BAIXO

---

## TESTE DA JOANA
**Entenderia:** PARCIALMENTE (melhor do que o Apêndice L)
**O que ela entenderia:** As analogias funcionam muito bem para Joana. A consultoria com especialistas (MoE), o sócio revisando o estagiário (Speculative Decoding), o auditor com planilha lateral (KV Cache) — todas são precisas e acessíveis sem background técnico. As implicações executivas são claramente escritas para ela. A seção "Quando importa para o leitor brasileiro" fala diretamente ao seu contexto.
**O que ela NÃO entenderia:** O mecanismo técnico de cada box vai além do que Joana precisa. "Softmax sobre top-K scores", "KL divergence sobre logits suavizados", "SRAM vs HBM" — esses termos aparecem sem glossário. Joana provavelmente pularia a seção de mecanismo técnico de cada box, e isso é aceitável — mas não está explicitamente autorizado no texto. O Box 11 (Matriz) seria difícil para Joana sem guia de leitura.
**Como corrigir:** Adicionar na abertura: "Se você é executivo não-técnico, leia Por que este box existe, Conceito intuitivo, Analogia e Implicação executiva em cada box. Pule o Mecanismo técnico na primeira leitura. Se precisar defender a decisão para um time de engenharia, volte ao mecanismo." Isso é permissão explícita para Joana navegar como precisa.

---

## TESTE DE DURABILIDADE
**Classificação:** ALTA (com ressalva no Box 10)
**2 anos:** Todos os boxes exceto Box 10 (Scaling Laws) sobrevivem bem. Os mecanismos descritos (MoE, speculative decoding, KV cache, FlashAttention, LoRA, quantização, structured output) são suficientemente estáveis para não mudar em dois anos.
**5 anos:** A maioria sobrevive. Risco médio em Box 9 (Interpretabilidade Mecanicista) — se a pesquisa avançar muito, o estado da arte descrito pode estar ultrapassado. Box 4 (FlashAttention) tem risco baixo de ser supersedido por outra técnica de IO-awareness.
**10 anos:** Incerto mas melhor que a média. Os conceitos (atenção, cache, roteamento, quantização) são mais duráveis que nomes de modelos. A questão é se a arquitetura transformer permanecerá dominante — se sim, quase tudo sobrevive.
**Justificativa:** O que mais envelhece: o nome "Claude 4 Sonnet" no Box 4 (já está errado), os exemplos de modelos específicos em Box 6 (Phi-3, Gemini Nano), a análise de platô no Box 10. O que menos envelhece: as analogias (nenhuma depende de modelo), os mecanismos técnicos dos boxes 1-4, a lógica de LoRA, a estrutura da matriz de interações.

---

## TESTE DE DIFERENCIAÇÃO
**Classificação:** PROPRIEDADE INTELECTUAL
**Justificativa:** Box 11 (Matriz de Interações) não existe em nenhuma outra publicação com esse nível de detalhe e aplicabilidade executiva. A combinação de "mecanismo técnico preciso + analogia acessível + implicação executiva brasileira" em cada box é formato que não encontra equivalente em livros de IA de negócios existentes. O apêndice como um todo está mais próximo de Designing Data-Intensive Applications (Kleppmann) em profundidade e aplicabilidade do que de qualquer livro de "IA para executivos" publicado em português.

---

## TESTE DE MEMORIZAÇÃO
**Ideia principal clara?** SIM
**Qual é a ideia principal (em 1 frase):** "Cada técnica arquitetural tem uma implicação executiva específica que muda o que você deve perguntar ao fornecedor antes de decidir o stack."
**Justificativa:** Essa ideia está presente em cada box e no Box 11, e é memorável porque é acionável. O leitor sai com 10 perguntas novas para fazer ao fornecedor — o que é exatamente o que um livro de método deve produzir.

---

## TESTE DE TRANSFORMAÇÃO
**Ao terminar, o leitor consegue fazer o que antes não conseguia:**
- Distinguir parâmetros totais de parâmetros ativos em MoE e fazer a pergunta certa ao comparar modelos
- Exigir do fornecedor informação sobre speculative decoding e avaliar o ganho real de latência
- Dimensionar memória GPU com KV cache em mente, não apenas com tamanho de pesos
- Entender por que contexto longo ficou barato (FlashAttention) e redesenhar arquitetura de RAG em consequência
- Avaliar LoRA como opção de roadmap de produto, não apenas de pesquisa
- Distinguir garantia sintática de garantia semântica em structured output e aplicar a implicação correta
- Tratar chain of thought como narrativa auditável, não como prova de raciocínio
- Planejar capacidade de auditoria não-quantizada quando mech interp for exigida por regulador
- Calibrar expectativa de ganho de qualidade por geração de modelo com base na análise de scaling laws
- Identificar o par dominante de conceitos no próprio produto e otimizar nessa ordem

---

## NOTA FINAL (0-10 cada eixo)
Estrutura: 9 | Pedagogia: 8 | Clareza: 8 | Autoridade: 8 | Durabilidade: 8 | Diferenciação: 9 | Memorização: 8 | Transformação: 9
**Nota Geral: 8**

## DECISÃO EDITORIAL
**MANTER COM AJUSTES**

Prioridade 1: Corrigir "Claude 4 Sonnet" (Achado 01) — erro factual imediato.
Prioridade 2: Reescrever a implicação executiva do Box 10 para ser epistemicamente honesta sobre incerteza de platô (Achado 02).
Prioridade 3: Corrigir a lógica causal da Interação 3 do Box 11 (Achado 03).
O restante são melhorias de detalhe. Este é o conteúdo mais forte dos apêndices revisados — mais próximo do padrão de comparação estabelecido pela rubrica.

---

---

## LINHAS-TRACKER

```
APX-L|L1-APX-L-biblioteca-prompts.md|01|P0|ALTO|Contradição estrutural: apêndice é catálogo que a tese proíbe|Restruturar como método com exemplos ou extrair catálogo para repositório|REVISAR PARCIALMENTE
APX-L|L1-APX-L-biblioteca-prompts.md|02|P0|MÉDIO|"Sonnet equivalente" em 26/30 fichas sem critério de equivalência|Definir critério operacional de equivalência na introdução da anatomia|REVISAR PARCIALMENTE
APX-L|L1-APX-L-biblioteca-prompts.md|03|P0|ALTO|Métricas de qualidade inacessíveis para verificação independente|Transformar em prescrições ou referenciar golden set público no repositório|REVISAR PARCIALMENTE
APX-L|L1-APX-L-biblioteca-prompts.md|04|P1|ALTO|Apêndice não ensina a construir prompt novo — apenas a usar os 30|Adicionar seção "Como construir um prompt que não está nesta lista"|REVISAR PARCIALMENTE
APX-L|L1-APX-L-biblioteca-prompts.md|05|P1|MÉDIO|Promessa do repositório não-verificável e sem fallback declarado|Adicionar política de manutenção e canal alternativo se URL falhar|MANTER COM AJUSTES
APX-L|L1-APX-L-biblioteca-prompts.md|06|P1|MÉDIO|Quando usar/evitar repete o óbvio — regra geral disfarçada de especificidade|Substituir por "Casos de borda e limites não óbvios"|MANTER COM AJUSTES
APX-L|L1-APX-L-biblioteca-prompts.md|07|P1|ALTO|P-MED-03 sem aviso de restrição regulatória B2C (CFF)|Adicionar nota de uso restrito a ambiente institucional supervisionado|MANTER COM AJUSTES
APX-L|L1-APX-L-biblioteca-prompts.md|08|P1|ALTO|P-FIN-02 sem menção à exigência de explicabilidade BACEN/LGPD art. 20|Adicionar anti-padrão: output sem registro auditável do fator determinante|MANTER COM AJUSTES
APX-L|L1-APX-L-biblioteca-prompts.md|09|P1|ALTO|Changelog editorial no final — conteúdo mais valioso enterrado na pág. 1600|Mover Changelog para a abertura, antes das fichas, como âncora metodológica|MANTER COM AJUSTES
APX-L|L1-APX-L-biblioteca-prompts.md|10|P1|MÉDIO|Nenhuma ficha menciona comportamento quando modelo recusa por policy|Adicionar 8º padrão de operação sobre monitoramento de recusas|MANTER COM AJUSTES
APX-L|L1-APX-L-biblioteca-prompts.md|11|P1|MÉDIO|P-RH-01 sem menção à auditoria de viés algorítmico exigida por regulação emergente|Adicionar anti-padrão: ausência de log auditável de triagens com variáveis|MANTER COM AJUSTES
APX-L|L1-APX-L-biblioteca-prompts.md|12|P2|BAIXO|"Princípio Três, a Camada Dupla" sem referência ao capítulo onde é definido|Adicionar "(ver Capítulo X)" na referência|MANTER COM AJUSTES
APX-L|L1-APX-L-biblioteca-prompts.md|13|P2|BAIXO|URL de repositório longa — inacessível em formato impresso|Usar URL base única + identificador curto por ficha|MANTER COM AJUSTES
APX-L|L1-APX-L-biblioteca-prompts.md|14|P2|BAIXO|P-MKT-01 menciona canais com limites de caracteres que mudam com frequência|Substituir por "canais com limite declarado pelo operador" como variável dinâmica|MANTER COM AJUSTES
APX-P|L1-APX-P-boxes-tecnicos.md|01|P0|ALTO|Box 4 cita "Claude 4 Sonnet" — modelo inexistente no portfólio Anthropic|Corrigir para versão atual verificada antes de publicar|MANTER COM AJUSTES
APX-P|L1-APX-P-boxes-tecnicos.md|02|P0|ALTO|Box 10: implicação executiva sobre platô é frágil e pode ser invalidada antes do fim do ciclo de vendas|Reescrever para ser epistemicamente honesto sobre incerteza de platô|MANTER COM AJUSTES
APX-P|L1-APX-P-boxes-tecnicos.md|03|P1|MÉDIO|Box 11 Interação 3: FlashAttention e platô de scaling laws conectados como causa-efeito quando são independentes|Separar os dois fenômenos e corrigir a lógica causal|MANTER COM AJUSTES
APX-P|L1-APX-P-boxes-tecnicos.md|04|P1|MÉDIO|Box 1: tiebreak leakage citado sem atualização de status em APIs gerenciadas|Distinguir risco on-prem vs. risco em API gerenciada pelo provedor|MANTER COM AJUSTES
APX-P|L1-APX-P-boxes-tecnicos.md|05|P1|MÉDIO|Box 11 usa emojis coloridos como única codificação da matriz — ilegível em impressão monocromática|Adicionar codificação textual alternativa (C/S/T/N) com legenda|MANTER COM AJUSTES
APX-P|L1-APX-P-boxes-tecnicos.md|06|P1|BAIXO|Box 8: referência "trabalho de seguimento CoT 2024-2025" sem paper específico|Substituir por referência específica ou orientar leitor para venue/conferência|MANTER COM AJUSTES
APX-P|L1-APX-P-boxes-tecnicos.md|07|P1|BAIXO|Box 5: S-LoRA mencionado sem referência primária|Adicionar: Sheng et al. S-LoRA, 2023, arxiv.org/abs/2311.03285|MANTER COM AJUSTES
APX-P|L1-APX-P-boxes-tecnicos.md|08|P2|BAIXO|Box 6: exemplos de destilação (Phi-3, Gemini Nano) sem DeepSeek-R1-Distill — caso mais relevante em 2026|Adicionar DeepSeek-R1-Distill como exemplo e referência|MANTER COM AJUSTES
APX-P|L1-APX-P-boxes-tecnicos.md|09|P2|BAIXO|Epígrafe final é a frase mais memorável do apêndice — está enterrada no final|Mover para abertura de "Como usar este apêndice"|MANTER COM AJUSTES
APX-P|L1-APX-P-boxes-tecnicos.md|10|P2|BAIXO|Mapa de boxes referencia princípios (P1-P9) sem indicar onde estão definidos|Adicionar nota de rodapé com capítulo/apêndice de referência|MANTER COM AJUSTES
```
