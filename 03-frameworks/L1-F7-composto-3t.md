# F7 — Custo Composto em Três Tempos
## Adoção corporativa pelos 3 vetores arquiteturais de custo composto

## 1. OBJETIVO

> **Escopo de observabilidade neste framework:** F7 pressupõe atribuição de custo por feature, implementada via Pilar 5 de LLMOps (Cap 22). Observabilidade aqui é restrita ao vetor de custo — chamadas, redundância, tier, por feature. A âncora autoritativa de observabilidade de IA em produção é o Cap 22; F3 cobre observabilidade de agente; F5 cobre observabilidade de integração; F6 cobre observabilidade de governança.

Atacar o orçamento real de IA na empresa pelo lado certo — **arquitetural** — não pelo lado errado — **textual**. Garantir que esforço de otimização vai onde o termo composto escala, não onde aparece o termo trivial.

## 2. FUNCIONAMENTO

A fórmula do Custo Composto:

```
Custo Total = Σ (tokens_in × preço_in + tokens_out × preço_out)
              × chamadas
              × redundância
              × tier
```

O framework opera em **três alavancas arquiteturais** (os "3T"), em ordem fixa de impacto e de risco.

### T1 — Tier de modelo

**O que é:** rotear cada chamada ao **modelo mais barato suficiente** para a qualidade exigida.

**Mecânica.**
- Classificador leve (Haiku-like) na entrada da pipeline decide rota.
- Tarefas estruturadas, classificação binária, extração de campo → tier pequeno (Haiku).
- Tarefas de razão balanceada, sumarização, resposta em escala → tier balanceado (Sonnet).
- Tarefas críticas de razão profunda, código complexo, escrita executiva → tier premium (Opus).

**Implementação.** 1-3 semanas para versão inicial; classificador é prompt simples ou pequeno modelo dedicado.

**Economia típica observada.** 30% a 60% do gasto total na primeira virada de roteamento, em operações que usavam premium para tudo. *(Faixa baseada em análise de casos corporativos documentados e tabelas de pricing públicas dos principais fornecedores — consultar Apêndice J. Economia real depende da arquitetura atual, do volume e do mix de tarefas. Validar contra atribuição de custo própria antes de usar como projeção em relatório executivo.)*

**Risco.** Médio. Exige golden set para mostrar que tier pequeno entrega qualidade equivalente (Invariante 7 sustenta a decisão).

### T2 — Topologia de chamada

**O que é:** reduzir **redundância** dentro do fluxo, sem mexer em tier nem em prompt.

**Mecânica.**
- **Prompt caching** para prefixos estáveis (system prompt, instruções recorrentes).
- **Batching** de chamadas independentes.
- **Eliminação de loops** de agente que reconsultam o mesmo dado.
- **Circuit breaker** contra runaway loops por usuário ou sessão. (Um runaway loop ocorre quando o agente continua chamando o modelo em ciclo sem convergir — por instrução ambígua, tool que falha e é retentada indefinidamente, ou contexto que nunca satisfaz o critério de parada. O circuit breaker define um limite máximo de chamadas ao modelo por sessão de usuário, ex.: 5 chamadas ao tier premium por sessão. Ao atingir o limite, a sessão cai para tier inferior ou retorna mensagem de encaminhamento ao humano. Implementação: contagem de chamadas por session_id com cache de curta duração; decremento automático na virada da janela de tempo.)
- **Tool design** que devolve em uma chamada o contexto que o próximo passo precisa.

**Implementação.** 2-4 semanas para o conjunto inicial; depende do quanto a arquitetura já está modular.

**Economia típica observada.** 20% a 50% adicional, após T1. *(Faixa baseada em análise de casos corporativos documentados — consultar Apêndice J para referências de base. Validar contra atribuição de custo própria.)*

**Risco.** Médio-alto. Mudanças em topologia podem introduzir regressão se o pilar 1 de LLMOps (tracing) e o pilar 3 (deploy progressivo) não estiverem maduros.

### T3 — Tamanho de contexto

**O que é:** podar agressivamente o que entra no contexto da chamada.

**Mecânica.**
- **RAG enxuto:** top-k baixo após reranking; chunks compactos; descarte de duplicidade.
- **Compressão de histórico:** sumarização hierárquica de turnos antigos.
- **Expiração de memória:** turnos com idade ou irrelevância vão para sumário ou são descartados.
- **Bibliografia controlada:** evitar inflar context com documentação que não está sendo consultada.

**Implementação.** 1-3 semanas, depende de quanto havia de "carona" no contexto.

**Economia típica observada.** 15% a 40% adicional, após T1 e T2. *(Faixa baseada em análise de casos corporativos documentados — consultar Apêndice J. Validar contra atribuição de custo própria.)*

**Risco.** Baixo. Exige eval cuidadoso para detectar regressão de qualidade por contexto insuficiente.

### Diagnóstico de pré-requisito

Antes de aplicar qualquer T, instalar atribuição de custo por feature (Pilar 5 de LLMOps — Cap 22). Sem atribuição, o diagnóstico usa estimativa inicial: se mais de 70% do volume vai para tier premium, começar por T1; se o sistema tem loops de agente visíveis no tracing, começar por T2; se o contexto médio por chamada supera 50% da janela disponível, começar por T3. Com atribuição instalada, a escolha é por dado, não por estimativa.

### Ordem de aplicação

Mexer em T3 antes de T1 é o erro mais comum, porque T3 é o mais visível ("vamos cortar palavras do prompt"). Visível e marginal. A ordem é T1 → T2 → T3.

## 3. OUTPUT

| Campo | Conteúdo |
|-------|----------|
| Análise atual de custo por feature | Atribuição via Pilar 5 de LLMOps |
| Identificação do componente que mais escala | Tokens, chamadas, redundância ou tier |
| T1 plan | Quais features migrar de tier, em que ordem, com qual golden set |
| T2 plan | Onde implementar caching, batching, circuit breaker |
| T3 plan | RAG enxuto, compressão de histórico, expiração de memória |
| Meta de economia | % por T, por feature, por trimestre |
| Eval que sustenta cada mudança | Invariante 7 — sem eval, não muda |

## 4. EXEMPLO DE USO — PÓLICE.IO PÓS-INCIDENTE

Marketplace BR de seguros, após o incidente do loop com cartão de crédito (Cap 22).

**Diagnóstico inicial.**
- Fatura mensal: R$ 142 mil
- Atribuição por feature: 87% concentrado no agente de cotação
- Componente que mais escala: **redundância** (loop de agente reconsultando 7 seguradoras)
- Tier dominante: 92% das chamadas vão para Opus, mesmo em classificação intermediária

**Plano T1.** Migrar classificação de intent (~38% do volume) para Haiku. Migrar geração de resposta padrão (~24%) para Sonnet. Manter Opus apenas para casos com sinal de complexidade alta (~15%).

**Plano T2.** Prompt caching para system prompt das cotações (eliminar 6.4kb por chamada). Circuit breaker de 5 chamadas Opus por sessão. Reescrita do agente para não reconsultar seguradoras em mudança de campo não-crítico (resolve o bug raiz do incidente).

**Plano T3.** RAG enxuto de documentação de produtos (top-3 chunks após reranking, em vez de top-20). Sumarização hierárquica em sessões com mais de 6 turnos.

**Resultado em 3 meses.** R$ 142 mil → R$ 47 mil, com volume servido maior. Distribuição final: 60% Haiku, 28% Sonnet, 12% Opus.

## 5. ANTI-PADRÕES

| Anti-padrão | Por que mata |
|-------------|--------------|
| Otimizar tamanho do prompt enquanto agente loopa no Opus | Esforço no termo trivial, fatura segue subindo |
| Usar premium para classificação binária "por garantia" | 30-50× o preço para entregar a mesma qualidade do pequeno |
| Começar por T3 porque é visível | T1 entrega ordem de magnitude a mais |
| Migrar tier sem golden set | Sem eval, regressão silenciosa em subgrupo |
| Ignorar atribuição de custo por feature | Sem atribuição, decisão de corte é tiro no escuro |
| Cortar caching para "simplificar" | Caching é o ROI mais alto de T2; descartar é multiplicar fatura |

## 6. CONEXÕES

- 🔗 Manifesto dos Invariantes
- 🔗 Cap 03 — Tokens, Cap 04 — Janela, Cap 07 — Memória
- 🔗 Cap 11 — Context Engineering
- 🔗 Cap 18 — Economia de Tokens
- 🔗 Cap 22 — LLMOps Pilar 5 (atribuição de custo sustenta o framework)
- 🔗 Diagnóstico de Encaixe entre Tarefa e Modelo (decisão de tier do F2 alimenta o T1 do F7)
- 🔗 Pirâmide da Avaliação (eval sustenta cada virada de T1)

---

> *"Preço por token é o termo trivial da fórmula. Quem otimiza só ali está mexendo onde menos dói. Os 3T mexem onde dói de verdade."*
