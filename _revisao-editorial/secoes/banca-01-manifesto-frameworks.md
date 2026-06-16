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
