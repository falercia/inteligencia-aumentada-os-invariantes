# Apêndice N — Metodológico, sobre os números deste livro

> **Atualizado em:** junho de 2026
> **Próxima revisão:** anual, ou sob mudança relevante na base de auditorias operacionais

---

## 1. Por que este apêndice existe

Toda obra técnica que pretende durar precisa expor o piso epistemológico sobre o qual seus números repousam. Em IA, o piso é mais frágil do que parece. Modelos mudam, preços mudam, benchmarks mudam, populações de uso mudam, e qualquer número específico tem vida útil curta. O leitor merece saber, com clareza, qual é a origem de cada número usado no corpo do livro, qual é a postura adotada quando o número aparece sem fonte primária, e qual é o roteiro que o autor seguirá para revisar o material em ciclos futuros.

Este apêndice cumpre três funções. Primeira, declara a postura epistemológica do livro em relação a números. Segunda, classifica todas as afirmações quantitativas relevantes em quatro tipos, com tratamento próprio para cada um. Terceira, lista os números críticos que precisam de revisão programada e a cadência sugerida.

---

## 2. Postura epistemológica

A obra trabalha em três camadas de conhecimento, conforme o Invariante Três e o Framework Nove. A camada do padrão, que é frameworks, princípios operacionais e arquiteturas duráveis, vive no corpo dos capítulos. A camada do número, que é preço, benchmark, versão de modelo, posição regulatória, vive no Apêndice J, com data e fonte. A camada do exemplo, que é caso ilustrativo composto a partir de padrões observados, vive nos boxes memoráveis dos capítulos, com rótulo explícito.

Números são usados em três modos. Modo definicional, quando o número é parte do desenho do framework e não pretende descrever o mundo, por exemplo "cobertura de cem por cento na camada base da Pirâmide de Avaliação". Modo observacional, quando o número descreve faixa colhida de auditorias operacionais, com qualificador adequado, por exemplo "tipicamente entre quarenta e setenta por cento de economia em operações que migram para roteamento por tier". Modo ilustrativo, quando o número aparece em cenário composto que serve para ensinar padrão, por exemplo "fatura de cento e quarenta e dois mil reais caiu para quarenta e sete mil em três meses".

A regra editorial é simples. Número em modo definicional não exige fonte. Número em modo observacional exige qualificador, e quando descrever afirmação categórica que sustenta tese, exige link para experimento reproduzível ou para fonte primária. Número em modo ilustrativo exige rótulo de "cenário composto a partir de padrões observados", deve sempre vir sem identificação de empresa real e, quando descrever resultado, deve respeitar a ordem de grandeza típica do setor.

---

## 3. Classificação das afirmações quantitativas

Toda afirmação quantitativa relevante do livro foi mapeada em quatro tipos, conforme a tabela abaixo.

### Tipo A — Fonte necessária

Afirmação categórica que sustenta tese ou diagnóstico estrutural. Exige link para fonte primária, paper, documentação oficial ou leaderboard público, com data da consulta. Exemplos no livro: "português usa quarenta a sessenta por cento mais tokens que inglês"; "custo de treinar modelo de fronteira em 2026 está entre cinquenta e quinhentos milhões de dólares"; "output costuma custar entre três e cinco vezes mais que input"; "modelos modernos chegam a um ou dois milhões de tokens de janela em 2026".

Tratamento editorial: nota de rodapé com link na primeira aparição, atualização cruzada no Apêndice J quando se tratar de preço, benchmark ou versão de modelo.

### Tipo B — Exemplo composto

Números que aparecem em casos memoráveis compostos a partir de padrões observados em auditorias reais. Exemplos no livro: "Banco Solar, fintech com aproximadamente quatrocentas pessoas em 2024, três migrações em quatro meses"; "Pólice.io, fatura de cento e quarenta e dois mil reais caiu para quarenta e sete mil em três meses"; "fintech do Cap 11, trezentas mil consultas por mês, custo caiu setenta e três por cento após context engineering".

Tratamento editorial: rótulo explícito de "cenário ilustrativo composto a partir de padrões observados". Nomes de empresa fictícios. Faixa de valores plausível para o setor descrito. Nenhuma afirmação de validação por NDA até que efetivamente exista NDA com cliente real disposto à atribuição.

### Tipo C — Auto-evidente

Números que são parte do desenho do framework e não descrevem o mundo. Exemplos no livro: "cinco blocos no F4"; "três alavancas no F7"; "cobertura de cem por cento na camada base do F8"; "cobertura de cinco a quinze por cento na camada topo do F8"; "matriz quatro por quatro no F3".

Tratamento editorial: nenhum, pois o número é parte da definição. Aparece sem fonte porque é o próprio framework.

### Tipo D — Estimativa honesta

Números que descrevem faixa observada com qualificador explícito que protege contra leitura literal. Exemplos no livro: "tipicamente entre setenta e quinhentos bilhões de parâmetros em modelos de fronteira em 2026"; "em média entre um vírgula três e um vírgula cinco tokens por palavra em inglês"; "trinta a sessenta por cento de economia típica observada na primeira alavanca do F7".

Tratamento editorial: qualificador presente, data da observação implícita ou explícita, e quando aparecer em capítulo central, link para metodologia da auditoria que originou a faixa.

---

## 4. Tabela de números críticos com cadência de revisão

A tabela abaixo lista os números que mais envelhecem rápido na obra, organizados por cadência de revisão necessária. Itens da cadência crítica são revisados a cada seis meses. Itens da cadência moderada são revisados anualmente. Itens da cadência estável são revisados a cada dois ou três anos.

| Cadência | Número | Capítulo | Tratamento |
|---|---|---|---|
| Crítica | Preço por token dos provedores de fronteira | C03, C15, C18 | Movido para Apêndice J, datado, sem cadência fixa |
| Crítica | Janela máxima de contexto em fronteira | C02, C04 | Movido para Apêndice J, datado, sem cadência fixa |
| Crítica | Custo de treinar modelo de fronteira | C02 | Faixa qualificada como "estimativa pública até [ano]", citando Epoch AI e statements oficiais |
| Crítica | Score do líder em GPQA, SWE-bench, AIME, HLE | C15 | Movido para Apêndice J, datado, sem cadência fixa |
| Crítica | Estado de PL 2338 no Brasil | C19, C24 | Movido para Apêndice J, datado |
| Moderada | Tamanho típico de modelo em parâmetros | C02 | Faixa qualificada com "tipicamente", revisão anual |
| Moderada | Taxa de tokens por palavra em português versus inglês | C03 | Acompanhar versionamento de tokenizers principais; nota de rodapé com link para experimento público |
| Moderada | Ranges típicos de economia por alavanca do F7 | C18, F7 | Manter qualificador "típica observada", revisão anual com auditorias adicionadas |
| Moderada | Distribuição entre as três zonas de Lost in the Middle | C04 | Acompanhar papers que aprofundem Liu et al. 2023 e variantes |
| Estável | Os nove Invariantes e as suas mecânicas | Manifesto | Reescrita só sob mudança de arquitetura dominante (saída de Transformers) |
| Estável | Arquitetura básica de tokenizer BPE | C03 | Reescrita só sob substituição da família BPE no mercado |
| Estável | Mecanismo de atenção em transformers | C02 | Reescrita só sob substituição da arquitetura |

---

## 5. Auditoria das afirmações quantitativas do manuscrito

Foi feita varredura sistemática do manuscrito da Obra Um buscando todas as afirmações com números, percentuais, intervalos e métricas. A varredura identificou oitenta e sete afirmações quantitativas relevantes no corpo dos capítulos, frameworks e apêndices (18 Tipo A + 24 Tipo B + 31 Tipo C + 14 Tipo D), distribuídas conforme a tabela a seguir.

| Tipo | Quantidade aproximada | Tratamento editorial agregado |
|---|---|---|
| A — Fonte necessária | 18 | Nota de rodapé com link na primeira aparição, atualização cruzada no Apêndice J |
| B — Exemplo composto | 24 | Rótulo "cenário ilustrativo composto a partir de padrões observados" em todos |
| C — Auto-evidente | 31 | Sem alteração, pois é definição |
| D — Estimativa honesta | 14 | Qualificador presente verificado em todos, revisão para garantir consistência |

Auditoria detalhada por capítulo, com a lista linha a linha das afirmações classificadas em cada tipo, ficou registrada no repositório acompanhante. O leitor que quiser auditar item a item pode consultar o documento `auditoria-quantitativa-l1.md` no repositório em [github.com/falercia/inteligencia-aumentada-recursos/blob/main/auditoria-quantitativa-l1.md](https://github.com/falercia/inteligencia-aumentada-recursos/blob/main/auditoria-quantitativa-l1.md), atualizado a cada revisão do manuscrito.

---

## 6. Por que não citar fonte inline em todos os números

Algumas obras técnicas optam por nota de rodapé em cada número. A escolha deste livro é deliberadamente diferente, por três motivos.

Primeiro, os números mais voláteis foram movidos para o Apêndice J. Isso libera o corpo dos capítulos para defender padrão sem ruído de versionamento. O leitor que precisar do número exato consulta o Apêndice J na data da decisão.

Segundo, os números mais usados na obra são qualificados como faixa observada, com palavra como "tipicamente", "observado em", "cerca de", o que evita pretensão de precisão que não se sustenta. Faixa qualificada não exige fonte pontual, exige metodologia da auditoria, que está descrita neste apêndice.

Terceiro, as afirmações categóricas que sustentam tese estrutural recebem nota de rodapé com link na primeira aparição. São aproximadamente quinze a vinte casos no livro inteiro, e a contenção é deliberada, para que a nota seja sinal de que o número importa, em vez de virar ruído onipresente. A lista completa desses casos está no arquivo `auditoria-quantitativa-l1.md` do repositório, coluna "Tipo A com nota de rodapé", atualizada a cada revisão do manuscrito.

A combinação dessas três regras mantém o livro legível, deixa o número auditável quando necessário, e protege o autor contra o envelhecimento que afetaria qualquer obra que prometesse precisão que o campo não permite.

---

## 7. Compromisso com revisão futura

A próxima revisão deste apêndice acompanha o ciclo anual da obra. A cada doze meses, a tabela do item 4 é reavaliada, a base de auditorias operacionais que sustenta os números do Tipo B e do Tipo D é atualizada, e qualquer afirmação que tenha mudado de classificação por mudança no campo é registrada no log de revisão.

O log de revisão fica público no repositório acompanhante, com três campos por entrada: data da revisão, item revisado, motivo da revisão. O leitor que quiser entender por que tal número mudou na quarta edição em relação à primeira pode consultar o log e reconstituir o histórico.

---

*Apêndice N — Metodológico. Atualizado em: junho de 2026. Próxima revisão programada: junho de 2027.*
