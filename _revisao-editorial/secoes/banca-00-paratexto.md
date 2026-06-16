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
