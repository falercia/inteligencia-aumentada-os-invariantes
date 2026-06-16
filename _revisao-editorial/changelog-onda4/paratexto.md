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
