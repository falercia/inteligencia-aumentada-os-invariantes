# F1 — Método de Decisão para Adotar IA
## Decisão de adoção de IA por iniciativa

## 1. OBJETIVO

Decidir, em até 30 minutos, se uma iniciativa específica deve usar IA, com qual nível de autonomia, e quem é o dono. Sai com cinco respostas duras e um plano mínimo, ou sai com a recusa documentada da iniciativa por critério explícito.

## 2. FUNCIONAMENTO

Cinco perguntas em ordem rígida. Sair em qualquer uma delas com resposta vaga interrompe o framework: ou se torna específica, ou a iniciativa não passa.

### Pergunta 1 — Tarefa
*"O que exatamente a IA vai fazer?"* Verbo + objeto + critério de sucesso, em uma frase.

Exemplo aceitável: "Classificar tickets de suporte em uma de cinco categorias com F1 mínimo de 0,85 contra rótulo humano". Exemplo não aceitável: "Ajudar o time de suporte com IA".

### Pergunta 2 — Operador
*"Quem opera, com que critério de aceitação?"* Pessoa nominal e regra explícita de quando aceita a saída.

Se a resposta for "ninguém define" ou "o usuário decide", a iniciativa não passa. Voltar à pergunta 1 e estreitar.

### Pergunta 3 — Risco
*"O que acontece se a saída estiver errada? Reversível ou não?"* Tipologia: financeiro, jurídico, reputacional, clínico, operacional. Reversibilidade em escala de quatro: totalmente reversível (idempotente), reversível com custo (compensável), parcialmente reversível, irreversível.

> **Gate de veto:** Se o risco for irreversível **e** o impacto for financeiro, jurídico ou clínico de alta magnitude, a iniciativa não passa para produção sem aprovação de nível executivo nominal (CEO ou equivalente com mandato explícito). Documente o gatilho de veto antes de continuar o framework. Não é lógica de ajuste — é bloqueio.

### Pergunta 4 — Linha de medição
*"Como saberemos que está funcionando?"* Métrica primária + golden set inicial + frequência de revisão.

Sem golden set planejado, a iniciativa pode passar para piloto interno mas não para produção. Princípio 7 manda.

### Pergunta 5 — Responsabilidade
*"Quem assina?"* Nome próprio, com cadeira específica, com competência para responder pela decisão.

Sem nome, não passa. Princípio 8 manda.

## 3. OUTPUT

A saída do F1, em uma página, contém:

| Campo | Conteúdo |
|-------|----------|
| Vai / Não-vai | Decisão binária com justificativa em uma frase |
| Nível de autonomia | Assistente · Co-piloto · Agente supervisionado · Agente autônomo regulado (define-se via Escala de Propriedade do Agente — F3) |
| Plano de eval | Golden set inicial, métrica primária, gate de bloqueio (via Pirâmide da Avaliação — F8) |
| Dono nominal | Nome + cadeira + cláusula de accountability |
| Revisão programada | Quando o framework volta a rodar para reavaliar. **Cadência-padrão sugerida:** 90 dias para piloto interno; 6 meses para produção com nível Assistente ou Co-piloto; 3 meses para Agente Supervisionado ou Autônomo Regulado. Justificar explicitamente qualquer cadência mais longa. |

> **Referência rápida — Níveis de autonomia** (definição completa em F3):
> - **Assistente:** humano executa sempre; IA gera proposta
> - **Co-piloto:** IA executa com confirmação humana a cada passo crítico
> - **Agente supervisionado:** IA executa em lote; humano monitora trace em tempo real e pode interromper
> - **Agente autônomo regulado:** IA executa em produção sem supervisão direta, com observabilidade completa, eval online e kill switch testado

## 4. EXEMPLO DE USO

| Pergunta | Resposta concreta |
|----------|--------------------|
| 1 — Tarefa | Triar currículos em "candidato com fit > 0,7 contra rubrica do hiring manager" (NÃO decisão de contratação) |
| 2 — Operador | Recrutador sênior + hiring manager; aceitação se humano revisa top-15 antes de contato |
| 3 — Risco | Reputacional alto (alegação de discriminação); irreversível em reputação; reversível em decisão |
| 4 — Linha de medição | Golden set de 400 currículos com gabarito de sêniores; viés ≤2% em adversarial de variantes equivalentes; revisão trimestral |
| 5 — Responsabilidade | Diretor de RH + DPO assinam Caderno de Governança da iniciativa |

**Decisão:** vai como **assistente** (humano decide sempre), nunca como decisor único. Eval comportamental mensal (Cap 23). Auditoria de viés trimestral (Cap 24). Política de transparência com candidato.

## 5. ANTI-PADRÕES

| Anti-padrão | Por que mata |
|-------------|--------------|
| Pular a pergunta 2 (operador) | Iniciativa fica sem dono operacional; falha quando precisa iterar |
| Pular a pergunta 5 (responsabilidade) | Falha jurídica e institucional quando der ruim |
| Aceitar "depois a gente decide isso" em qualquer pergunta | Toda dúvida adiada vira incidente |
| Aplicar o framework retroativamente, em iniciativa já em produção, sem corrigir buracos | Vira teatro de processo |

## 6. CONEXÕES

- 🔗 Manifesto dos Invariantes
- 🔗 Cap 21 — Evals (linha de medição da Pergunta 4)
- 🔗 Cap 22 — LLMOps (nível de autonomia da Pergunta 3)
- 🔗 Cap 24 — Governança (responsabilidade nominal da Pergunta 5)
- 🔗 Escala de Propriedade do Agente (decide o nível de autonomia)
- 🔗 Governança Indelegável (governança da iniciativa)
- 🔗 Pirâmide da Avaliação (plano de eval da iniciativa)

---

> *"Vai ou não-vai não é palpite, é resposta a cinco perguntas duras. Quem pula uma delas paga depois."*
