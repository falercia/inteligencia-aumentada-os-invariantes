# MAPA DE LEITURA POR NÍVEL
## A partir de onde você está

A maior parte dos livros técnicos densos cobra do leitor um preço alto quando ele tenta ler linearmente sem reconhecer o próprio ponto de partida. O iniciante absoluto trava em capítulos avançados e abandona; o profissional experiente perde tempo nos capítulos iniciais e desiste na metade; o cientista de dados pula direto para a profundidade técnica e perde a costura conceitual que sustenta o sistema. Esta nota existe para evitar os três destinos.

A obra é desenhada para três níveis de leitor, e cada nível tem trilha recomendada de leitura, com volume horário estimado e capítulos prioritários. O leitor honesto faz primeiro o diagnóstico de cinco perguntas abaixo, identifica o próprio nível, e segue a trilha correspondente. As trilhas por nível são subsets enxutos: quem quiser leitura integral encontra o roteiro de cinquenta horas mais adiante, na seção *Roteiros de leitura por orçamento de tempo*.

---

## Diagnóstico em cinco perguntas

Responda sim ou não para cada uma, com honestidade.

| # | Pergunta | Sim | Não |
|---|---|:---:|:---:|
| 1 | Sabe explicar, com analogia ou linguagem técnica, o que é um *embedding* e por que ele importa em sistemas modernos de IA? | ☐ | ☐ |
| 2 | Já operou, em ambiente profissional, um sistema baseado em LLM que usa ferramentas externas (APIs, banco de dados, busca) de forma automática para completar tarefas além de gerar texto? | ☐ | ☐ |
| 3 | Lê papers técnicos no arXiv ou em conferências (NeurIPS, ICML, ACL, ICLR) com regularidade suficiente para reconhecer trabalhos recentes do campo? | ☐ | ☐ |
| 4 | Consegue explicar, em pelo menos linguagem intermediária, como funciona o mecanismo de *attention* em arquiteturas Transformer? | ☐ | ☐ |
| 5 | Já conduziu, em produção ou em projeto-piloto sério, processo de *fine-tuning* ou de *engenharia de prompt* em escala, com métrica de qualidade auditável? | ☐ | ☐ |

### Sua trilha pela contagem de "sim"

| Sim | Seu nível | Trilha recomendada |
|:---:|---|---|
| **0-2** | Iniciante absoluto | Trilha INICIANTE (12h em 4 semanas) |
| **3-4** | Intermediário | Trilha INTERMEDIÁRIO (30h em 6-8 semanas) |
| **5** | Avançado ou especialista | Trilha AVANÇADO (18h focadas + leitura cruzada) |

### Fluxo entre trilhas

| Trilha atual | Avança quando | Recua quando |
|---|---|---|
| **Iniciante** | Consolida C5 (embeddings) + C9 (engenharia de prompt) com autoavaliação ≥ 4/5 em três capítulos seguidos | — |
| **Intermediário** | Opera C11 (context) + C14 (AI engineering) + C21 (evals) em produção, com critério explícito | Três autoavaliações seguidas < 3/5 → volta para Iniciante |
| **Avançado** | — | Três autoavaliações seguidas < 3/5 em capítulo avançado → volta para Intermediário |

Voltar uma trilha é movimento normal, não custo de orgulho. Avançar acontece naturalmente conforme a base consolida.

---

## Trilha do leitor INICIANTE ABSOLUTO

**Pressupostos:** nunca operou IA generativa regularmente em ambiente profissional, não domina vocabulário básico (prompt, token, modelo, fine-tuning, embedding), entrou na obra para construir base sólida.

**Volume estimado:** cerca de doze horas de leitura ativa, em quatro semanas.

**Capítulos prioritários, em ordem de leitura:**

| Ordem | Item | Por que vir agora |
|---|---|---|
| 1 | Manifesto C00P — Por que padrão dura e número morre | Fundação intelectual; lê em qualquer nível |
| 2 | Manifesto C00M — Os Nove Invariantes da Inteligência Artificial | Espinha da obra; lê com calma |
| 3 | C1 — O que é IA | Contexto histórico e conceitual mínimo |
| 4 | C2 — Como modelos funcionam | Versão intuitiva da arquitetura |
| 5 | C3 — Tokens | Conceito que abre tudo o resto |
| 6 | C4 — Janela de contexto | Limite prático que estrutura uso real |
| 7 | C5 — Embeddings | Conceito fundamental para entender RAG |
| 8 | C9 — Engenharia de prompt | Habilidade prática imediata |
| 9 | C26 — Roadmap pessoal | Define o próximo passo para seu caso |
| 10 | Apêndices A (glossário) e B (mapa mental) | Consulta permanente |

**Pular nesta primeira passada:** C11, C14, C21, C22, C28, todos os frameworks F3 a F9, Apêndices L, P, O. Voltar a eles quando o vocabulário e os fundamentos estiverem consolidados.

---

## Trilha do leitor INTERMEDIÁRIO

**Pressupostos:** usa IA generativa regularmente, opera prompts profissionais, conhece vocabulário básico, busca sistematizar conhecimento, ampliar profundidade técnica e instalar disciplina executiva.

**Volume estimado:** cerca de trinta horas de leitura ativa, em seis a oito semanas.

**Trilha completa, com prioridades:**

| Prioridade | Capítulos e Frameworks |
|---|---|
| **Alta** | C00P, C00M, C6 (RAG), C7 (memória), C9, C10 (chain of thought), C11 (context engineering), C12 (agentes), C13 (MCP), C14 (AI Engineering), C18 (economia de tokens), C24 (governança), C25 (trade-offs), C26 (roadmap), C27 (PME se for fundador) |
| **Frameworks essenciais** | F1 (decisão), F2 (encaixe), F4 (prompt estendido), F6 (governança), F7 (custo), F8 (avaliação) |
| **Apêndices essenciais** | L (biblioteca de prompts), J (trilha do número), O (caderno de governança), D (ferramentas) |
| **Média** | C8 (fine-tuning), C15 (comparação), C16 (open source), C19 (segurança), C20 (futuro), C21 (evals), C22 (LLMOps), C23 (alignment) |
| **Frameworks médios** | F3 (agente), F5 (cobertura), F9 (rota dupla) |
| **Apêndices médios** | M (síntese), N (metodológico), P (boxes técnicos) |

**Pular nesta primeira passada:** C14B (reasoning models — voltar quando estiver operando reasoning em produção), C28 (interpretabilidade mecanicista — voltar quando enfrentar caso regulatório real), C17 (auditoria de repositórios — usar como referência operacional). Apêndice Q (Manual do Professor) somente se for docente.

---

## Trilha do leitor AVANÇADO ou ESPECIALISTA

**Pressupostos:** trabalha com IA em produção, lê papers, opera evals e LLMOps, busca sistema próprio coeso, profundidade técnica em pontos centrais e diferenciação intelectual da obra.

**Volume estimado:** cerca de dezoito horas focadas em capítulos centrais, com leitura cruzada do restante.

**Trilha prioritária:**

| Bloco | Capítulos e itens |
|---|---|
| **Sistema intelectual** | C00P e C00M *(se ainda não leu, comece aqui; se já leu, pule direto para o Núcleo técnico)*, F3, F8, F9 |
| **Núcleo técnico** | C11 (context engineering), C14 (AI Engineering), C14B (reasoning models), C21 (evals), C22 (LLMOps), C23 (alignment) |
| **Fronteira técnica** | C28 (interpretabilidade), Apêndice P (boxes técnicos), Apêndice J (trilha do número) |
| **Operação rigorosa** | C19 (segurança), C24 (governança), C25 (trade-offs), Apêndice O (caderno) |
| **Diferenciação** | Apêndice N (postura metodológica), F6 (governança indelegável) |

**Apêndices de referência permanente:** N, P, J, O, L.

**Não precisa ler na primeira passada:** C1 a C4 (revisão de fundamentos — pode pular ou ler em diagonal), C27 (PME — só se for atuar em consultoria neste segmento), Apêndice Q (somente se for docente).

---

## Bandeira por capítulo

Para o leitor que quiser identificar rapidamente o público primário de cada capítulo, a obra mantém a seguinte classificação:

| Nível primário | Capítulos |
|---|---|
| **Iniciante** | C1, C2, C3, C4, C9 |
| **Iniciante + Intermediário** | C5, C6, C7, C8 |
| **Intermediário** | C10, C11, C12, C13, C15, C16, C18, C24, C25, C26, C27 |
| **Intermediário + Avançado** | C14, C19, C20, C21, C22 |
| **Avançado / Especialista** | C14B, C17, C23, C28 |
| **Todos os níveis (fundação)** | Manifesto C00P, Manifesto C00M |

Frameworks (F1 a F9) e Apêndices são consulta permanente, não leitura sequencial obrigatória.

---

## Roteiros de leitura por orçamento de tempo

**8 horas (executivo com agenda apertada):**
C00P → C00M → F1 (Método de Decisão) → C24 (governança) → C25 (trade-offs) → C26 (roadmap pessoal) → Apêndice O (caderno) → Apêndice M (síntese de bolso).

**20 horas (intermediário em primeira passada):**
Manifestos C00P e C00M → C1 a C9 em ritmo regular → C11, C12, C13 com profundidade → C18, C24, C25, C26 → frameworks F1, F4, F6, F7 → apêndices L, J, O.

**50 horas (leitura completa para construir referência interna):**
Leitura sequencial integral com pausa em cada Autoavaliação. Aplicação dos exercícios numerados ao longo dos capítulos. Construção do roadmap pessoal (C26). Aplicação do Caderno de Governança v1 no contexto do leitor (Apêndice O). Revisão da Trilha do Número (Apêndice J) e da Biblioteca de Prompts (Apêndice L) como instrumentos diários.

---

## Como saber se a trilha está funcionando

Cada capítulo termina com Autoavaliação em tabela de cinco critérios. A regra prática de recalibração:

| Sinal observado | O que fazer |
|---|---|
| 3 capítulos seguidos com Autoavaliação ≥ 4/5 | Considerar avançar uma trilha |
| 3 capítulos seguidos com Autoavaliação ≤ 2/5 | Voltar uma trilha |
| 1-2 capítulos com nota baixa entre vários ≥ 3/5 | Reler o capítulo específico, não mudar trilha |
| Autoavaliação inconsistente entre temas | Trilha mista provável — seguir por interesse, não por nível |

A leitura honesta deste mapa, antes do primeiro capítulo, economiza horas de esforço mal direcionado. Escolher a trilha que você aspira ser, em vez da que efetivamente serve agora, produz o resultado típico: abandono nos capítulos errados por frustração ou tédio.
