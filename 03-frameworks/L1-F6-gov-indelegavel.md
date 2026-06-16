# F6 — Governança Indelegável
## Governança de IA aplicada — 3 camadas × 10 controles

## 1. OBJETIVO

> **Escopo de observabilidade neste framework:** F6 usa observabilidade no contexto de governança — controle 2 (auditoria imutável) e controle 5 (tracing de LLMOps) garantem rastreabilidade das decisões de IA para fins regulatórios e de accountability. A âncora autoritativa de observabilidade técnica em produção é o Cap 22 — LLMOps; F3 cobre observabilidade de agente; F5 cobre observabilidade de integração; F7 cobre observabilidade de custo.

Construir governança de IA que **protege o negócio sem virar teatro de compliance**. Saída: Caderno de Governança v1 com política em ≤6 páginas + RACI assinado + plano de incidente testado em simulado + matriz de maturidade dos 10 controles.

## 2. FUNCIONAMENTO

Governança real opera em **três camadas que precisam fechar**, sustentadas por **dez controles canônicos**.

### As 3 camadas

| Camada | O que cobre | Quem responde |
|--------|-------------|----------------|
| **Técnica** | Acesso, auditoria imutável, kill switch, rollback, observability, evals em CI | CTO / Head de tecnologia |
| **Operacional** | RACI, AUP, política de incidentes, runbooks, treinamento, postmortem | Head de operações / VP de produto |
| **Executiva** | AI Council, política pública, accountability nominal, comitê de ética, comunicação com conselho | CEO / Diretor com mandato |

Cada camada tem dono nominal. Sem nome em cada camada, governança não fecha — vira documento publicado sem prática efetiva.

### Os 10 controles canônicos

| # | Controle | Camada |
|---|----------|--------|
| 1 | Controle de acesso por feature, por usuário, por papel | Técnica |
| 2 | Auditoria imutável de cada chamada de IA em produção | Técnica |
| 3 | Kill switch testado por tool, por agente, por modelo, por feature | Técnica |
| 4 | Rollback testado mensalmente em staging | Técnica |
| 5 | Observability com tracing (pilares 1 de LLMOps) | Técnica |
| 6 | Evals em CI com critério de bloqueio explícito | Técnica |
| 7 | RACI de IA assinado pela diretoria | Operacional |
| 8 | Política de Uso Aceitável (AUP) publicada e treinada | Operacional |
| 9 | Política de incidentes testada em simulado trimestral | Operacional |
| 10 | AI Council com mandato e cadência fixa. **Cadência mínima:** mensal nos primeiros 12 meses; trimestral após revisão de maturidade no primeiro ano. Organizações em setor regulado (saúde, financeiro) mantêm mensal de forma permanente. | Executiva |

### Mecânica de aplicação

1. **Diagnóstico de maturidade.** Pontuar cada um dos 10 controles em escala 0-4 (inexistente, declarado, implementado, auditado, melhoria contínua).
2. **Identificação de buracos.** Controles em maturidade ≤1 são prioridade. Maturidade 2 sem auditoria é teatro.
3. **Plano em 90/180/365 dias.** Cada controle com maturidade-alvo, dono, gate de promoção.
4. **Caderno em ≤6 páginas.** Política, RACI, plano de incidente e matriz de maturidade. Modelo aplicável pronto para uso no **Apêndice O — Caderno de Governança v1**.

> **As 12 decisões mínimas do RACI** (template completo no Apêndice O):
>
> | # | Decisão |
> |---|---------|
> | 1 | Escolha de modelo (família, tier, fornecedor) |
> | 2 | Mudança de prompt em produção |
> | 3 | Composição e atualização de dataset de treino ou eval |
> | 4 | Promoção de agente entre níveis de autonomia (F3) |
> | 5 | Adoção de novo mecanismo de integração (MCP, tool, API) |
> | 6 | Ativação de ferramenta com efeito externo (escrita, transação, comunicação) |
> | 7 | Declaração e resposta a incidente SEV-1 |
> | 8 | Aprovação de política de uso aceitável (AUP) |
> | 9 | Acesso a dado sensível por sistema de IA |
> | 10 | Publicação de relatório ou comunicação gerada por IA com efeito jurídico |
> | 11 | Acionamento de kill switch em produção |
> | 12 | Revisão trimestral de maturidade de governança |
5. **Revisão trimestral.** Maturidade atualizada, plano ajustado, incidentes do trimestre integrados.

## 3. OUTPUT

| Campo | Conteúdo |
|-------|----------|
| Política em ≤6 páginas | AUP + princípios + categorias de safety |
| RACI assinado | 8 papéis × 12 decisões mínimas (ver tabela na seção 2 — Funcionamento) |
| Plano de incidente testado | Severidades, comunicação, postmortem |
| Matriz de maturidade | 10 controles em escala 0-4, com meta de 90/180/365 dias |
| Donos nominais por camada | Técnica, Operacional, Executiva |
| Cadência de revisão | Trimestral, com pauta fixa |

## 4. EXEMPLO DE USO — SEGURADORA APÓS INCIDENTE (CENÁRIO ILUSTRATIVO)

Seguradora BR de médio porte, após multa ANPD por negação automatizada de cobertura sem trilha de auditoria.

**Diagnóstico de maturidade pré-incidente:**

| Controle | Maturidade |
|----------|-----------|
| 1 Acesso | 1 (declarado) |
| 2 Auditoria | 0 |
| 3 Kill switch | 0 |
| 4 Rollback | 1 |
| 5 Observability | 1 |
| 6 Evals em CI | 0 |
| 7 RACI | 0 (implícito, "o time de dados cuida") |
| 8 AUP | 0 |
| 9 Política de incidentes | 1 (documento sem teste) |
| 10 AI Council | 0 |

**Plano após incidente (90 dias):**

- Controle 7 (RACI): assinado pela diretoria com 8 papéis (CTO, Head Dados, DPO, Head Compliance, Diretor Operações, Diretor Comercial, Diretor Jurídico, CEO) × 12 decisões (modelo, prompt, dataset, agente, MCP, tool, incidente SEV-1, política, etc.)
- Controle 8 (AUP): 4 páginas, publicada, treinada em todo o time em ≤30 dias
- Controle 2 (Auditoria): retenção 5 anos para decisão automatizada com efeito jurídico
- Controle 6 (Evals em CI): golden set inicial para classificação de cobertura
- Controle 9 (Incidente): simulado trimestral com cronômetro
- Controle 10 (AI Council): mandato escrito, cadência mensal nos primeiros 12 meses

**Após 7 meses:** matriz com 8 de 10 controles em maturidade ≥3. Multa não voltou. Seguradora apresenta caso em comitê setorial como exemplo de remediação.

## 5. ANTI-PADRÕES

| Anti-padrão | Por que mata |
|-------------|--------------|
| Política publicada, processo inexistente, prática divergente | Governança morta no PDF; quando o incidente vier, o documento será exposto como teatro |
| RACI implícito ("o time X cuida") | Sem nome, ninguém responde. Princípio 8 viola por omissão |
| AI Council sem mandato | Vira reunião de tom sem decisão; conselho fica simbólico |
| Política de incidente nunca testada em simulado | Na hora do incidente, descobre-se que não funciona |
| Auditoria interna sem auditoria externa periódica | Auto-auditoria tende a falsa segurança |
| "Vamos terceirizar o problema" | **Accountability não terceiriza — responsabilidade nominal precisa de nome interno.** Execução especializada terceirizada (auditoria externa periódica, consultoria de DPIA, certificação ISO/IEC 42001) é legítima e recomendada onde o time interno não tem capacidade técnica. O que não terceiriza é a resposta à pergunta "quem assina?" |

## 6. CONEXÕES

- 🔗 Manifesto dos Invariantes
- 🔗 Cap 19 — Segurança
- 🔗 Cap 23 — Alignment (sustenta safety em produto)
- 🔗 Cap 24 — Governança
- 🔗 Cap 29 (L2) — Team, Cap 30 (L2) — Enterprise
- 🔗 Método de Decisão para Adotar IA (Pergunta 5 — Responsabilidade — alimenta o RACI)
- 🔗 Escala de Propriedade do Agente (níveis de autonomia precisam de governança proporcional)
- 🔗 Pirâmide da Avaliação (controle 6 — evals em CI — é a implementação técnica do F8)

---

> *"Governança não é documento publicado, é controle aplicado. Quem confunde, descobre na multa ou no processo."*
