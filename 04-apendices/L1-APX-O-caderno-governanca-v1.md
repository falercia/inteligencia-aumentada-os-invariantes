# Apêndice O — Caderno de Governança de IA

## Por que este apêndice existe em duas camadas

O Caderno de Governança de IA é o artefato prometido pelo Framework Seis, e foi pensado desde a primeira versão como instrumento vivo, no sentido estrito de que deve ser preenchido com nomes humanos, assinado pela diretoria, revisado em cadência trimestral, atualizado a cada incidente material, e auditado contra evidência de execução, jamais contra a sua própria existência publicada. Um caderno que dorme em PDF assinado e não volta à mesa por seis trimestres seguidos não é governança ativa, é teatro de compliance, e a obra trata teatro como pior do que ausência declarada de governança, porque teatro mente para o conselho.

Construir um caderno desse tipo exige duas peças que vivem em andares diferentes, e a obra trata cada uma delas no andar certo. A primeira peça é o padrão durável, e ela vive aqui no livro, na forma de uma ficha conceitual única que entrega a anatomia do caderno, os princípios que o sustentam, os critérios de quando o modelo se aplica e quando exige adendo setorial, os padrões de adaptação ao contexto da organização, os anti-padrões observados em prática e a métrica que separa caderno vivo de caderno morto. A ficha é o que o executivo precisa entender para customizar o modelo ao próprio contexto, para defender a estrutura diante de auditoria externa e para reconhecer quando o caderno da sua casa começou a degradar.

A segunda peça é o caderno operacional executável, e ela vive no repositório acompanhante público em [github.com/falercia/inteligencia-aumentada-recursos/tree/main/governance/v1](https://github.com/falercia/inteligencia-aumentada-recursos/tree/main/governance/v1), em pasta dedicada, com o caderno inteiro em um arquivo único pronto para imprimir e assinar, as seis seções fatiadas em arquivos separados para edição independente por área, a lista dos seis anexos referenciados com modelos clonáveis, e o changelog editorial datado a cada revisão. Quem chega à ficha do livro com clareza conceitual encontra no repositório o artefato pronto para clonar, customizar, assinar e colocar em revisão trimestral, sem ter que reescrever cada seção do zero, e sem ter que decidir quais campos um caderno mínimo precisa ter.

Essa separação é deliberada e materializa o Princípio Três, a Camada Dupla. O padrão dura porque a estrutura conceitual de governança de IA sobrevive à próxima geração de modelo, ao próximo provedor, à próxima moda de framework, e à próxima onda regulatória, ainda que cada onda exija adendo específico sobre o que a versão atual do caderno carrega. O número muda porque o conteúdo dos dez controles vai sofrer iteração mensal conforme novos vetores de incidente apareçam em produção, conforme reguladores publiquem novas exigências, e conforme a comunidade de operadores brasileiros de IA contribua com calibração de RACI por setor. Manter as duas peças no mesmo arquivo, como faziam as primeiras versões deste apêndice, congelava o caderno em mídia impressa e impedia a evolução contínua do ativo. O leitor que entendeu o método vai ao repositório quando precisa do executável, e fica com a ficha quando precisa do método.

### Quadro de orientação — onde vive o quê

| Camada do conhecimento | Onde vive | Cadência de revisão |
|---|---|---|
| Anatomia dos seis blocos, princípios condutores, padrões de adaptação ao contexto, anti-padrões transversais, métrica de caderno vivo versus caderno morto | **LIVRO · ficha conceitual** | Anual, junto com a próxima edição |
| Caderno completo pronto para imprimir e assinar, seis seções fatiadas para edição independente, modelos dos seis anexos referenciados, changelog editorial datado | **REPO · `/governance/v1/`** | Sem cadência fixa, conforme evolução do instrumento |
| Calibração regulatória corrente (LGPD, AI Act, NIST AI RMF), adendos setoriais publicados, casos de incidente material registrados como lição pública | **APÊNDICE J · Trilha do Número** | Periódico, com fonte primária por linha |

> *Nota de alinhamento com o Apêndice N:* esta estrutura de camadas materializa, na prática do caderno, o Tipo C da taxonomia do APX-N — padrão durável que vive no livro — e o Tipo A — número datado com fonte primária — que vive no repositório e no Apêndice J.

### Quadro de navegação — onde começar dependendo da sua dor

> *Este caderno é instrumentação operacional de dois lugares da obra. O Framework Seis entrega a tese de governança indelegável e o porquê de cada bloco. O Capítulo 19 entrega o vocabulário de incidente e o desenho de severidades que sustenta o plano de resposta. Consulte os dois antes para o porquê do caderno; volte aqui para o como, e desça ao repositório para o pronto-para-assinar.*

| Se sua dor é | Comece por | Volte aqui para |
|---|---|---|
| Convencer a diretoria do porquê de governança formal | F6 — Governança Indelegável | Customizar a ficha conceitual ao vocabulário da casa |
| Construir o playbook de SEV-1 antes do primeiro incidente | C19 — Segurança e Riscos | Acoplar o plano de incidente do caderno ao desenho de severidades |
| Preencher o caderno operacional na próxima semana | `/governance/v1/` no repositório | Validar adaptação contra os sete padrões e os dez anti-padrões |
| Auditar caderno existente que parou de evoluir | Métrica de caderno vivo nesta ficha | Acionar diretoria com leitura dos sete indicadores em vermelho |

---

## A anatomia que toda governança de IA precisa fechar

Antes da ficha em si, vale percorrer uma única vez a anatomia do caderno, em seis blocos, com a função de cada um e a razão de estar naquela posição. A ordem dos blocos não foi escolhida por estética, ela emergiu da experiência de diretorias que tentaram montar caderno em ordem diferente, e descobriram tarde demais que sem identificação clara não há accountable, sem RACI específico não há decisão rastreável, e sem plano de incidente assinado não há resposta calibrada quando a crise vier.

| Bloco | Função | Por que está nesta posição |
|---|---|---|
| 1. Identificação, escopo e princípios | Define quem assina, o que está dentro e o que está fora, e quais princípios condutores a organização adota | Primeiro porque sem nome do patrocinador executivo e do responsável operacional, o caderno é documento órfão; sem escopo declarado, controles aplicáveis ficam ambíguos |
| 2. RACI e Comitê de IA | Atribui Accountable único por classe de decisão recorrente e define o órgão executivo permanente | Cedo no caderno porque o Princípio Oito, Responsabilidade Indelegável, exige que toda decisão tenha nome humano antes de qualquer controle técnico ser cobrado |
| 3. Política de uso aceitável (AUP) | Declara o que é permitido, o que é proibido e as sanções pelo descumprimento, para todo colaborador e prestador | No meio porque depende do escopo declarado no bloco 1 e do Accountable definido no bloco 2, e antecede os controles operacionais que vão fiscalizar a aderência |
| 4. Dez controles canônicos com nível de maturidade | Estabelece os controles técnicos, operacionais e executivos auditáveis, com maturidade autodeclarada e meta no horizonte de doze meses | Depois da AUP porque os controles fiscalizam a aderência à AUP e ao RACI; antes do plano de incidente porque incidente é falha de controle, e sem controle declarado a classificação de falha fica subjetiva |
| 5. Plano de incidente e severidades | Calibra detecção, resposta, comunicação e postmortem por nível de severidade | Penúltimo porque incidente é o estresse-teste de tudo que veio antes, e sem o que veio antes não há base de comparação para julgar a resposta |
| 6. Assinaturas, anexos e revisão | Vincula a diretoria ao compromisso, lista os anexos vivos do caderno e declara a política de revisão trimestral | Último porque assinatura é ato de fechamento, anexos são extensões controladas, e revisão é o motor que mantém o caderno vivo |

Os seis blocos compõem um documento de cerca de seis páginas no caderno operacional executável. A ficha no livro entrega o método para customizar cada bloco. O repositório entrega cada bloco em arquivo separado, com placeholders nomeados, para que a organização preencha em paralelo entre as áreas responsáveis.

---

## Os dez controles canônicos em uma linha

O Bloco 4 do caderno — "Dez controles canônicos com nível de maturidade" — é citado ao longo desta ficha conceitual e ao longo do Capítulo 24 como o coração da postura operacional da organização. Os dez controles são nomeados aqui para que o executivo possa defendê-los em reunião ou auditoria sem depender de acesso ao repositório. O detalhe de cada controle — definição de maturidade por nível, evidências esperadas por score e metas de progressão — está na seção 04 do caderno executável em `governance/v1/04-dez-controles-maturidade.md`.

Cada controle pertence a uma das três camadas: técnica, operacional ou executiva. A escala de maturidade é 0 (inexistente), 1 (declarado), 2 (implementado), 3 (auditado), 4 (melhoria contínua). Meta de operação saudável: média de 3,0 ou superior em todos os dez, com nenhum controle em 0 após os primeiros doze meses.

| # | Controle | Camada | O que verifica |
|---|---|---|---|
| 1 | Controle de acesso por feature, usuário e papel | Técnica | Quem pode usar e configurar qual feature de IA |
| 2 | Auditoria imutável de cada chamada em produção | Técnica | Trilha reconstrutível de toda decisão consequente |
| 3 | Kill switch por tool, agente, modelo e feature | Técnica | Capacidade de desligar em segundos, por escopo |
| 4 | Rollback testado mensalmente em staging | Técnica | Reversão a estado conhecido e seguro |
| 5 | Observabilidade com tracing fim a fim | Técnica | Visibilidade do que acontece em cada chamada |
| 6 | Evals em CI com bloqueio explícito | Técnica | Regressão detectada antes de chegar a produção |
| 7 | RACI de IA assinado pela diretoria | Operacional | Dono nominal e único por classe de decisão |
| 8 | AUP publicada, treinada e versionada | Operacional | Contrato interno sobre o que é e não é permitido |
| 9 | Política de incidentes testada em simulado trimestral | Operacional | Playbook que funciona quando a crise chega |
| 10 | AI Council com mandato escrito e cadência fixa | Executiva | Governança no nível decisório, não apenas no operacional |

> **Nota de derivação editorial:** esta tabela reproduz os dez controles canônicos definidos no Capítulo 24, seção "Os dez controles canônicos". Qualquer atualização futura da lista no Capítulo 24 deve ser refletida aqui na próxima revisão anual desta ficha. O conteúdo completo de cada controle, com rubrica de maturidade e exemplos de evidência por nível, está exclusivamente no caderno executável do repositório.

---

## Os nove princípios que sustentam o caderno

O caderno opera sobre os Nove Princípios da obra, com ênfase em quatro deles que carregam a maior parte do peso operacional do instrumento. O leitor que precise revisitar os princípios em sua versão completa encontra a discussão no Framework Seis, e a síntese de bolso no Apêndice M.

| Princípio | Como o caderno materializa |
|---|---|
| Princípio 1 · Plausibilidade não verdade | A AUP veda atribuir autoria humana a conteúdo gerado integralmente por IA quando a atribuição importa ao destinatário, e exige revisão humana proporcional ao risco em decisão crítica |
| Princípio 3 · Camada dupla | O próprio caderno é Camada Dupla aplicada, com o método aqui no livro e o número datado no repositório acompanhante |
| Princípio 6 · Propriedade do agente | A matriz RACI exige Accountable nomeado para promoção de agente entre níveis de autonomia, e o controle número três exige kill switch testado em simulado |
| Princípio 8 · Responsabilidade indelegável | A regra fundamental do caderno é que toda decisão de IA tem nome humano único, e quando alguém disser "foi a IA que decidiu", a organização precisa saber em até cinco minutos de quem é a cadeira |

Os outros cinco princípios aparecem de forma distribuída no caderno, e estão listados na íntegra na seção 1.3 do caderno operacional executável em `governance/v1/01-identificacao-escopo-principios.md`.

---

## Quando adotar este modelo, e quando ele exige adendo setorial

O caderno foi calibrado para organização brasileira entre 50 e 5.000 colaboradores (cinquenta a cinco mil), com uso de IA em produção em pelo menos um caso de uso material, e sem operação em setor criticamente regulado em que o regulador exija instrumento de governança próprio. Fora dessa faixa, o caderno continua útil como ponto de partida, mas exige adendo específico.

| Adotar como está | Exige adendo setorial antes de adotar |
|---|---|
| Organização entre 50 e 5000 colaboradores em qualquer setor | Instituição financeira sob CMN 4658/2018 e regulação prudencial específica do Banco Central |
| Adoção primeira de governança formal de IA | Hospital ou operadora de saúde sob ANS, com prontuário eletrônico tocado por IA |
| Operação multi-cloud com modelos próprios e de terceiros | Governo, autarquia ou empresa pública sob LGPD setorial e Marco Civil específico |
| Empresa que vende SaaS com IA embarcada como funcionalidade central | Operação em jurisdição não-brasileira com regulação distinta (EU AI Act, NIST AI RMF, regulação setorial estadual nos EUA) |
| Empresa que adota IA de terceiros via API como ferramenta auxiliar | Operação com dado pessoal sensível em volume material sem DPO efetivo previamente nomeado |

O adendo setorial não substitui o caderno, ele se anexa como camada adicional sobre o instrumento base, e é o instrumento setorial que define o trecho específico, jamais o contrário, porque regulação setorial sobrescreve governança interna por princípio.

---

## Sete padrões de adaptação ao contexto da organização

A customização do caderno segue sete padrões transversais, independentemente do setor e do porte. Pular qualquer um deles produz documento publicado com aparência de governança e prática divergente, que é exatamente o teatro que o Framework Seis combate.

1. **Patrocinador executivo nomeado, não apenas o cargo.** O caderno exige nome próprio na linha de patrocinador, não apenas "CTO" ou "CEO". Sem nome, a responsabilidade vira institucional, e institucional é eufemismo para ninguém.

2. **Princípios condutores customizados ao vocabulário da organização**, sem renomear os Nove Princípios da obra, e sem suprimir nenhum deles. Customização que apaga o Princípio Oito viola o pacto editorial do caderno.

3. **Matriz RACI estendida com as classes de decisão específicas do negócio.** As sete classes de decisão recorrentes do modelo são piso, jamais teto. Empresa que opera com agente autônomo em produção precisa adicionar classe específica para promoção de tier de autonomia, com gates de observabilidade explícitos.

4. **Comitê de IA com mandato declarado por escrito**, em ata da primeira reunião, com lista do que decide unilateralmente, do que escala à diretoria e do que precisa de quórum qualificado. Comitê sem mandato é fórum de debate filosófico, e fórum não para incidente.

5. **AUP traduzida ao contexto operacional da empresa**, com exemplos práticos do que é permitido e do que é proibido nas ferramentas reais que a organização adota. AUP genérica não orienta, AUP com exemplo orienta.

6. **Maturidade autodeclarada com evidência anexada por controle.** O preenchimento da coluna de maturidade na primeira assinatura exige link para artefato de evidência, jamais autodeclaração nua. Maturidade três sem artefato é maturidade um disfarçada.

7. **Revisão trimestral em calendário fixo da diretoria**, não em janela negociada por agenda. Sem data fixa, revisão escorrega para o trimestre seguinte, e o caderno entra em coma silencioso.

---

## Anti-padrões transversais de governança de IA

| Anti-padrão | Por que falha |
|---|---|
| Caderno publicado em PDF assinado sem revisão programada | Governança morre no momento da assinatura; o documento vira álibi quando o incidente vier, não defesa |
| RACI implícito com expressão como "o time X cuida" | Sem nome, ninguém responde; viola o Princípio Oito por omissão estrutural |
| Comitê de IA sem mandato escrito e sem quórum mínimo | Reuniões viram fórum de opinião, decisões empacam, incidentes escalam à diretoria sem filtro técnico |
| AUP genérica sem exemplo concreto da ferramenta adotada | Colaborador não sabe se a ferramenta nova do dia está permitida ou proibida, e o resultado é shadow AI |
| Maturidade autodeclarada sem evidência anexada | Conselho recebe quadro verde otimista que não resiste ao primeiro incidente |
| Plano de incidente sem simulado semestral | Quando a crise vier pela primeira vez, todo mundo descobre que o playbook não foi treinado |
| Ausência de log de edições do caderno | Cada revisão vira mudança não rastreável, e impossível defender o instrumento em auditoria |
| Revisão trimestral pulada sem registro formal | Caderno entra em coma silencioso, e quando alguém perceber, a versão vigente já estará desalinhada da operação |
| Atualização do caderno apenas após incidente material | Governança vira reativa; o objetivo é manter o caderno à frente do incidente, não atrás |
| Adoção integral sem adendo setorial em setor regulado | Conflito entre instrumento interno e exigência do regulador, com perda de validade jurídica do caderno em caso de fiscalização |

---

## A métrica que separa caderno vivo de caderno morto

Saber se o caderno está vivo não é função de quem publicou, e sim de quem usa o caderno em cadência. Sete indicadores quantitativos sustentam a leitura da saúde do instrumento, e devem ser revisados no relatório anual do Comitê de IA à diretoria.

| Indicador | O que mede | Faixa saudável no horizonte de doze meses |
|---|---|---|
| Atas do Comitê de IA arquivadas | Cadência real do órgão executivo | 12 atas no ano, sem ausência maior que 45 dias |
| Atualizações do caderno registradas no log | Quantas vezes o instrumento foi revisado de fato | Entre 4 e 8 atualizações no ano, com pelo menos uma por incidente material |
| Maturidade média dos 10 controles | Evolução agregada da postura operacional | Crescimento mínimo de 0,5 ponto na escala de 0 a 4, por ano, até atingir 3,0 médio |
| RACIs específicos assinados por caso de uso em produção | Cobertura nominal de Accountable por sistema | 100% dos casos de uso de IA em produção com RACI específico assinado |
| Simulados de SEV-1 executados | Maturidade real do plano de incidente | 2 simulados no ano, com tempo de resposta abaixo da meta declarada |
| Postmortems sem culpa publicados internamente | Aprendizado real a partir de incidentes | 100% dos SEV-1 e SEV-2 com postmortem em até 10 dias úteis |
| Treinamentos de AUP em onboarding | Difusão da AUP na operação | 100% dos colaboradores novos treinados no primeiro mês de casa |

Organização que olha esses sete indicadores e descobre quatro deles em vermelho não tem governança, tem caderno publicado. O Comitê de IA deve usar essa leitura para acionar a diretoria, jamais para esconder a degradação.

---

## Versão executável

O caderno operacional completo, com placeholders nomeados, com as seis seções fatiadas para edição independente, com os modelos dos seis anexos referenciados e com o changelog datado a cada revisão, está no repositório acompanhante na pasta dedicada `governance/v1` (URL na abertura deste apêndice).

O caminho recomendado de adoção é clonar a pasta, customizar a identificação e os princípios na seção 01, montar o RACI específico do negócio na seção 02, traduzir a AUP ao vocabulário e às ferramentas da organização na seção 03, preencher a maturidade autodeclarada com evidência anexada na seção 04, calibrar o plano de incidente ao SLA real do negócio na seção 05, colher as assinaturas da diretoria na seção 06, e marcar a próxima revisão no calendário do Comitê de IA no mesmo ato. Caderno que não nasce com data de próxima revisão marcada já nasce morto.

---

## Compromisso final do caderno

A diretoria, ao assinar o caderno, compromete-se com a regra fundamental do Princípio Oito, em que toda decisão de IA tem nome humano responsável. A IA executa, a responsabilidade tem dono. Quando alguém disser "foi a IA que decidiu", a organização precisa saber, em até cinco minutos, de quem é a cadeira.

Este é o pacto que o caderno materializa, e é a métrica final pela qual ele será julgado, ainda que muito antes disso o conselho já tenha julgado os sete indicadores de caderno vivo.

---

*Apêndice O · Caderno de Governança de IA. Ficha conceitual no livro, caderno operacional executável em `governance/v1` no repositório acompanhante. Política editorial: instrumento vivo, sem cadência fixa anunciada.*
