# Changelog Onda 5 — Galé: Paratextos + Manifestos
## Inteligência Aumentada · Os Princípios Permanentes da IA

**Data:** 2026-06-16
**Executor:** Editor de galé (Claude Sonnet 4.6)
**Escopo:** 15 paratextos (00-paratexto/) + 2 manifestos (01-manifesto/) + abertura de 02-capitulos/L1-C01-o-que-e-ia.md
**Metodologia:** Leitura linear corrida completa, lente de galé (ritmo, transições, repetições cruzadas, voz, setup/callback, consistência de termos)

---

## EDITADOS

### E1 — Frase duplicada em L1-06-repositorio-acompanhante.md
**Arquivo:** `00-paratexto/L1-06-repositorio-acompanhante.md`
**Localização:** Seção "Política de evolução", parágrafos 1 e 2

**Antes:**
```
...A política editorial é simples e dura: nenhuma promessa de release que não esteja pronta para ser cumprida, e nenhum release publicado sem ter passado pela mesma disciplina de revisão que o livro exige de qualquer artefato sério.

A política editorial é simples: nenhum release publicado sem ter passado pela mesma disciplina de revisão que o livro exige de qualquer artefato sério. O leitor que clona o repositório pode ativar *watch* no GitHub...
```

**Depois:** Os dois parágrafos foram fundidos. O início "A política editorial é simples:" do segundo parágrafo foi eliminado (repetição literal do início do parágrafo anterior). A frase sobre o *watch* no GitHub foi integrada ao parágrafo único resultante.

**Motivo de galé:** Repetição literal de abertura de frase em parágrafos consecutivos — só detectável por leitura corrida. O segundo parágrafo era eco redundante do primeiro, com a frase de ação (watch no GitHub) enterrada depois da repetição.

---

### E2 — Duplo separador horizontal em L1-C00P-porque-padrao-dura.md
**Arquivo:** `01-manifesto/L1-C00P-porque-padrao-dura.md`
**Localização:** Logo após a epígrafe de abertura, antes de "## ABERTURA"

**Antes:**
```
> *"Todo número que parece sólido hoje..."*

---

---

## ABERTURA
```

**Depois:**
```
> *"Todo número que parece sólido hoje..."*

---

## ABERTURA
```

**Motivo de galé:** Duplo `---` gera espaço visual duplo em qualquer renderizador. Provavelmente resquício de edição anterior. Só detectável por leitura contínua do arquivo.

---

### E3 — Inconsistência de contagem "Trinta exemplos" vs. "mais de 30"
**Arquivo:** `00-paratexto/L1-00c2-promessa.md`
**Localização:** Lista de ganhos, item bullet de exemplos

**Antes:** `- **Trinta exemplos memoráveis brasileiros**`
**Depois:** `- **Mais de trinta exemplos memoráveis brasileiros**`

**Motivo de galé:** O arquivo autoritativo (L1-00e-sobre-os-casos.md, o pacto editorial) declara "mais de trinta". Promessa, orelha e quarta-capa divergiam entre "Trinta" (exato), "mais de trinta" e "mais de 30". Galé detectou a inconsistência cruzada entre documentos. A versão canônica é "mais de trinta" por ser o número declarado no pacto editorial.

---

### E4 — Inconsistência "mais de 30" em extenso no Sobre os Casos
**Arquivo:** `00-paratexto/L1-00e-sobre-os-casos.md`
**Localização:** Parágrafo de abertura + tabela de tipos de caso

**Antes (parágrafo):** `Esta obra usa, ao longo dos 29 capítulos, mais de 30 exemplos memoráveis`
**Depois:** `mais de trinta exemplos memoráveis`

**Antes (tabela):** `**Mais de 30 compostos pedagógicos · todos os memoráveis desta edição**`
**Depois:** `**Mais de trinta compostos pedagógicos · todos os memoráveis desta edição**`

**Motivo de galé:** Mistura de algarismo ("30") e extenso ("trinta") no mesmo contexto editorial. Orelha e quarta-capa já usam extenso — padronizado para extenso em todo o paratexto.

---

### E5 — Capitalização inconsistente do nome do sistema na Introdução
**Arquivo:** `00-paratexto/L1-03-introducao.md`
**Localização:** Seção "Aposta 4 — Sistema citável próprio"

**Antes:** `os **nove princípios permanentes da inteligência artificial**`
**Depois:** `os **Nove Princípios Permanentes da Inteligência Artificial**`

**Motivo de galé:** Quando o nome do sistema é usado como nome próprio (em negrito, referência ao sistema da obra), deve seguir a capitalização estabelecida no prefácio ("**Nove Princípios Permanentes da Inteligência Artificial**") e na promessa ("**Nove Princípios Permanentes**"). A introdução usava minúsculas no mesmo contexto em que os outros documentos usam maiúsculas. Inconsistência só detectável por leitura cruzada.

---

### E6 — Capitalização híbrida na Quarta-capa
**Arquivo:** `00-paratexto/L1-12-quarta-capa.md`
**Localização:** Segundo parágrafo do texto editorial

**Antes:** `A obra organiza nove Princípios Permanentes, costurados em rede mútua`
**Depois:** `A obra organiza os Nove Princípios Permanentes, costurados em rede mútua`

**Motivo de galé:** "nove" em minúsculo com "Princípios Permanentes" em maiúsculo era híbrido inconsistente. O padrão da obra é "os Nove Princípios Permanentes" (maiúsculas quando é referência ao sistema). Artigo "os" adicionado para fluência.

---

### E7 — Inconsistência de capitalização no Sumário (título do segundo manifesto)
**Arquivo:** `00-paratexto/L1-04-sumario.md`
**Localização:** Tabela "OS NOVE PRINCÍPIOS PERMANENTES", segunda linha

**Antes:** `| Por que Padrão Dura e Número Morre — fundação intelectual da Camada Dupla | 22 |`
**Depois:** `| Por Que Padrão Dura e Número Morre — fundação intelectual da Camada Dupla | 22 |`

**Motivo de galé:** O título real do arquivo (L1-C00P-porque-padrao-dura.md, primeira linha) é "Por Que Padrão Dura e Número Morre" com "Que" maiúsculo. O sumário tinha "que" em minúsculo. Discrepância entre sumário e título real.

---

### E8 — Nota de produção visível convertida para comentário HTML em L1-06
**Arquivo:** `00-paratexto/L1-06-repositorio-acompanhante.md`
**Localização:** Início do arquivo, antes da epígrafe

**Antes:**
```
> **[PENDENTE — VERIFICAÇÃO PRÉ-PUBLICAÇÃO OBRIGATÓRIA]**
> O repositório `github.com/falercia/inteligencia-aumentada-recursos` deve estar público...
```

**Depois:** Convertido para comentário HTML `<!-- NOTA INTERNA DE PRODUÇÃO — NÃO INCLUIR NO ARQUIVO ENVIADO... -->`

**Motivo de galé:** A nota de produção estava em bloco citação Markdown (`>`), visível para o leitor em qualquer renderização. Diferente da nota da capa (que já estava em `<!-- -->`), esta teria sido impressa ou renderizada para o leitor. Convertida para comentário HTML seguindo o padrão já adotado na capa.

---

## PENDENTE-AUTOR

### PA-1 — Ordem dos princípios no Prefácio diverge da numeração canônica do Manifesto
**Arquivo:** `00-paratexto/L1-01-prefacio.md`, linha 39
**Situação:** O prefácio lista os princípios na ordem: Camada Dupla, Plausibilidade, Custo Composto, Extremidades, Encaixe, Termômetro, Autonomia Proporcional, Responsabilidade Indelegável, Operador. O manifesto os numera 1-Plausibilidade, 2-Extremidades, 3-Camada Dupla, 4-Encaixe, 5-Custo Composto, 6-Autonomia Proporcional, 7-Termômetro, 8-Responsabilidade Indelegável, 9-Operador.
**Risco:** Leitor que lê o prefácio e depois o manifesto pode ficar confuso com a reordenação. O prefácio não usa números, mas a ordem implícita difere.
**Recomendação:** Se a ordem numérica do manifesto é canônica, considerar reordenar a lista no prefácio para 1-Plausibilidade, 2-Extremidades, 3-Camada Dupla etc. Alternativa: manter a ordem do prefácio com nota editorial de que os números virão no manifesto. Decisão autoral — não edite sem confirmação.

---

### PA-2 — Título do manifesto C00M diverge do sumário
**Arquivo:** `01-manifesto/L1-C00M-manifesto-invariantes.md` (título: "Os Nove Invariantes da Inteligência Artificial") vs. `00-paratexto/L1-04-sumario.md` (entrada: "Os Nove Princípios Permanentes da Inteligência Artificial")
**Situação:** O sumário chama o capítulo de "Os Nove Princípios Permanentes" mas o arquivo real tem "Os Nove Invariantes". O leitor procura pelo título do sumário e encontra um título diferente.
**Risco:** Confusão de nomenclatura. "Invariantes" vs. "Princípios Permanentes" são termos usados como sinônimos ao longo da obra, mas a duplicidade não está declarada ao leitor antes de ele chegar ao manifesto.
**Recomendação:** Ou uniformizar o título do arquivo para "Os Nove Princípios Permanentes da Inteligência Artificial" (alinhando com o subtítulo da obra), ou manter "Invariantes" no arquivo e ajustar o sumário, ou acrescentar subtítulo explicativo. Decisão editorial central — não mexer sem confirmação.

---

### PA-3 — Contagem "29 capítulos" no Sobre os Casos não bate com estrutura do Sumário
**Arquivo:** `00-paratexto/L1-00e-sobre-os-casos.md`, primeira linha do texto
**Situação:** Declara "ao longo dos 29 capítulos". O sumário lista C1 a C28 (28 capítulos numerados) + C14B e C14C (subcapítulos ou capítulos adicionais). Nenhuma conta chega a 29 de forma direta.
**Risco:** Número errado na promessa explícita ao leitor.
**Recomendação:** Verificar contagem real após estrutura final dos capítulos e atualizar o número. Se C14B e C14C contam como capítulos plenos, o total é 30. Se não contam, é 28. Confirmar e corrigir.

---

### PA-4 — "Quem só lê o livro / quem opera só com o repositório" — dupla ocorrência no mesmo arquivo
**Arquivo:** `00-paratexto/L1-06-repositorio-acompanhante.md`
**Situação:** A ideia "Quem só lê o livro sai com método. Quem opera só com o repositório sem ler o livro opera no escuro." aparece duas vezes no arquivo: no parágrafo introdutório (linha ~12) e na citação de fechamento (linha ~66). A citação de fechamento é a versão mais lapidada. O parágrafo introdutório poderia ser comprimido ou reescrito para não repetir o conteúdo da citação.
**Recomendação:** Encurtar o parágrafo introdutório para manter apenas a afirmação sobre Camada Dupla, eliminando as frases "Quem só lê... / Quem opera só..." que a citação de fechamento já resolve. Decisão autoral de reescrita — não aplicar sem confirmação.

---

### PA-5 — Notas `[PENDENTE — NÃO ENVIAR AO GRÁFICO]` visíveis na Quarta-capa
**Arquivo:** `00-paratexto/L1-12-quarta-capa.md`, linhas finais
**Situação:** Os campos de Páginas, ISBN e Preço sugerido têm notas de produção inline visíveis (`[PENDENTE — aguardando diagramação final — NÃO ENVIAR AO GRÁFICO]`). Diferente das notas em comentário HTML da capa e do repositório (agora corrigido), estas ficariam visíveis no arquivo renderizado.
**Recomendação:** Converter para comentários HTML ou criar campo separado de "dados de produção" fora do arquivo de texto editorial. Decisão de fluxo de produção.

---

### PA-6 — Posicionamento do "Sobre os Casos" antes do Prefácio pode quebrar ritmo de entrada
**Arquivo:** `00-paratexto/L1-00e-sobre-os-casos.md`
**Situação:** O "Sobre os Casos" é um documento denso, com três tabelas e metadiscurso sobre verificabilidade metodológica. Posicionado antes do Prefácio, ele recebe o leitor com desafio epistêmico antes de qualquer convite emocional à leitura. Isso pode desacelerar leitores que entraram pelo canal de e-book (onde a ordem de páginas é mais linear).
**Recomendação:** Avaliar se "Sobre os Casos" poderia vir após o Prefácio (ou após a Introdução), quando o leitor já estiver comprometido com a obra. Alternativa: encurtar a nota para 1 parágrafo de transparência + link para a tabela completa em apêndice. Decisão estrutural — não mover sem confirmação do autor.

---

### PA-7 — "Curiosidade ativa" no critério 5 da autoavaliação do C00P
**Arquivo:** `01-manifesto/L1-C00P-porque-padrao-dura.md`, tabela de autoavaliação, critério 5
**Situação:** O critério 5 usa o termo "Curiosidade ativa" como nome de competência. Este é um dos 16 pendentes da revisão (verificar se "Curiosidade" ou "Curiosidade ativa" é o padrão da obra para esse tipo de critério de autoavaliação). No cluster atual, aparece apenas uma vez, sem definição prévia.
**Recomendação:** Confirmar se "Curiosidade ativa" é um framework/convenção nomeada da obra (que deveria ser capitalizado e definido) ou um critério informal de autoavaliação. Se for convenção nomeada, padronizar capitalização e verificar consistência em todos os capítulos.

---

### PA-8 — Epígrafe Dijkstra em C01 — atribuição como "adaptado de"
**Arquivo:** `02-capitulos/L1-C01-o-que-e-ia.md`, epígrafe
**Situação:** `> *"A pergunta não é se as máquinas pensam. A pergunta é se nós entendemos o que significa pensar."* / — adaptado de Edsger Dijkstra`
**Situação:** Este é um dos 16 pendentes. A frase como escrita não é citação direta verificável de Dijkstra — a atribuição "adaptado de" é honesta mas pode ser insuficiente para validação editorial rigorosa. A epígrafe funciona muito bem como gancho e o tom é consistente com Dijkstra.
**Recomendação:** Verificar se existe frase original verificável de Dijkstra que esta adapta, e citar a fonte primária. Se não existir, considerar reformular como "Inspirado por Dijkstra" ou usar sem atribuição como paráfrase. Decisão autoral.

---

## JÁ RESOLVIDO

### JR-1 — "Modelos passam. Método fica." em múltiplos arquivos
5 ocorrências em cluster distintos: epígrafe da promessa, corpo do prefácio, exemplo do Banco Solar no manifesto, fechamento do manifesto e orelha. Cada ocorrência tem enquadramento e função diferentes (epígrafe, tese revelada, moral de exemplo, citação de fechamento, chamada de marketing). A repetição é intencional e funciona como anáfora temática — não é redundância sem escalada. JÁ RESOLVIDO.

### JR-2 — "Para o profissional que quer construir, não apenas opinar" em orelha e quarta-capa
Orelha esquerda (versão curta) e quarta-capa (versão expandida em três chamadas) compartilham a frase. São peças físicas distintas lidas em momentos distintos pelo leitor-em-livraria. Repetição é norma editorial para taglines de marketing em peças do mesmo livro. JÁ RESOLVIDO.

### JR-3 — Bio do autor (Sobre o Autor vs. Orelha Direita)
O "Sobre o Autor" (longo, ao final do livro) e a Orelha Direita (curta, para o leitor-em-livraria) compartilham núcleo biográfico. É a convenção padrão de livros técnicos — bio curta na orelha, bio longa ao final. JÁ RESOLVIDO por convenção editorial.

### JR-4 — Subtítulo "Os Invariantes" vs. "Os Princípios Permanentes"
O nome do projeto interno usa "Invariantes"; o subtítulo de capa usa "Os Princípios Permanentes da IA"; o manifesto usa "os nove invariantes" como nome do sistema. A dualidade é deliberada: "Invariantes" é o nome interno/intelectual do sistema; "Princípios Permanentes" é a formulação de mercado no subtítulo. JÁ RESOLVIDO por intenção editorial (exceto o conflito sumário vs. título do manifesto, que vai para PA-2).

### JR-5 — "Como pensar em IA" na Promessa, "conceitos sobre ferramentas" na Introdução
Enquadramentos diferentes da mesma proposição de valor. Promessa: perspectiva do leitor ("você vai aprender a pensar"). Prefácio: perspectiva autoral ("recusei o catálogo"). Introdução: perspectiva sistêmica ("conceito sobrevive, ferramenta não"). Progressão de perspectiva, não repetição. JÁ RESOLVIDO.

### JR-6 — Nota de produção na capa (comentário HTML)
`<!-- NOTA INTERNA DE PRODUÇÃO: linha curta para canais digitais = "O livro que separa o padrão do botão." Não incluir em arquivo enviado ao designer ou distribuidor. -->` — já estava em comentário HTML correto. JÁ RESOLVIDO.

### JR-7 — Transição manifesto C00P → C01 (gancho)
O P.9 do C00P encaminha explicitamente: "O Capítulo 1 abre com a fundação sobre o que é IA na arquitetura generativa atual." O C01 abre com epígrafe de enquadramento filosófico (Dijkstra) e mergulha em "O Conceito Intuitivo" com a cena do motorista — gancho sensorial forte e consistente com o tom da obra. A transição funciona. JÁ RESOLVIDO.

---

## RESUMO

| Categoria | Quantidade |
|---|---|
| Edições aplicadas diretamente nos arquivos | **8** |
| PENDENTE-AUTOR (sinalizados, não editados) | **8** |
| JÁ RESOLVIDO (confirmados como intencional) | **7** |

**Arquivos editados:**
1. `00-paratexto/L1-06-repositorio-acompanhante.md` — edições E1 e E8
2. `01-manifesto/L1-C00P-porque-padrao-dura.md` — edição E2
3. `00-paratexto/L1-00c2-promessa.md` — edição E3
4. `00-paratexto/L1-00e-sobre-os-casos.md` — edição E4
5. `00-paratexto/L1-03-introducao.md` — edição E5
6. `00-paratexto/L1-12-quarta-capa.md` — edição E6
7. `00-paratexto/L1-04-sumario.md` — edição E7

**Top 3 achados de galé por impacto:**
1. **E8 (nota de produção visível no repositório)** — risco real de impressão de texto interno; só detectável por leitura corrida do arquivo bruto
2. **E3/E4 (inconsistência "Trinta" vs. "mais de trinta" vs. "mais de 30")** — o único número que aparece em promessa, orelha, quarta-capa e pacto editorial — com três variantes. Dano a credibilidade se o leitor perceber.
3. **E1 (frase duplicada no repositório)** — o parágrafo "A política editorial é simples" aparecia duas vezes em sequência com variação mínima; só detectável por leitura linear do arquivo.

**PENDENTE-AUTOR mais importantes (em ordem de urgência):**
1. **PA-2** — Título do manifesto vs. sumário: "Invariantes" vs. "Princípios Permanentes" — conflito entre o que o sumário promete e o que o capítulo entrega
2. **PA-3** — "29 capítulos" provavelmente errado (estrutura atual sugere 28 ou 30) — número em promessa explícita no pacto editorial
3. **PA-1** — Ordem dos princípios no prefácio diverge da numeração canônica — pode confundir o leitor na transição prefácio → manifesto
4. **PA-5** — Notas `[PENDENTE — NÃO ENVIAR AO GRÁFICO]` visíveis na quarta-capa — risco de produção
