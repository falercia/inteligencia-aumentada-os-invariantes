# Changelog Pendências D7 e D8 — Onda 5

Data de execução: 2026-06-16

---

## D7 — F5: Compactação ao template canônico

### Contagem de linhas

| Estado | Linhas |
|--------|--------|
| Antes (original) | 169 |
| Depois (reestruturado) | 138 |

### Mapa de consolidação: 11 seções → 6 seções

| Seção original (F5 antes) | Seção canônica (F5 depois) | Observação |
|---|---|---|
| Epígrafe de abertura (*"O agente vale o que ele alcança..."*) | **1. OBJETIVO** (1º parágrafo) | Conteúdo da epígrafe integrado como sentença de abertura do OBJETIVO; padrão exclusivo de F5 eliminado |
| ESCOPO DESTE FRAMEWORK (não numerada) | **1. OBJETIVO** (2º parágrafo) | Delimitações de observabilidade/conformidade/Cap22 preservadas na íntegra |
| 1. OBJETIVO | **1. OBJETIVO** (3º parágrafo) | Universo de escolha e cinco variáveis estruturais preservados |
| 2. NOTA EDITORIAL DE NEUTRALIDADE | **2. FUNCIONAMENTO** (subseção "Neutralidade analítica") | Texto preservado na íntegra; apenas reclassificado como subseção de FUNCIONAMENTO |
| 3. OS SEIS MECANISMOS DE INTEGRAÇÃO | **2. FUNCIONAMENTO** (subseção "Os seis mecanismos de integração") | Tabela completa preservada; parágrafo de síntese preservado |
| 4. AS CINCO DIMENSÕES DA MATRIZ DE COBERTURA | **2. FUNCIONAMENTO** (subseção "As cinco dimensões da Matriz de Cobertura") | Tabela completa (5 linhas) preservada; regra de níveis preservada |
| 5. MATRIZ DE DECISÃO POR CAPABILITY | **2. FUNCIONAMENTO** (subseção "Matriz de decisão por capability") | Tabela completa (7 linhas) preservada; parágrafo conclusivo preservado |
| 6. QUANDO CADA MECANISMO É A ESCOLHA ERRADA | **2. FUNCIONAMENTO** (subseção "Quando cada mecanismo é a escolha errada") | Todos os 6 mecanismos (REST, gRPC, Webhook, Event-driven, MCP, Tool ad-hoc) com critérios preservados |
| 7. QUANDO MIGRAR DE MECANISMO EXISTENTE | **2. FUNCIONAMENTO** (subseção "Quando migrar de mecanismo existente") | Todos os 3 critérios de migração + 4 critérios de não-migração preservados |
| 11. APLICAÇÃO PRÁTICA EM 30 MINUTOS | **2. FUNCIONAMENTO** (subseção "Protocolo de aplicação em 30 minutos") | Protocolo de 5 passos preservado na íntegra; regra inegociável preservada |
| (sem OUTPUT explícito no original) | **3. OUTPUT** | Criada do zero seguindo padrão canônico; sintetiza artefatos de saída do framework |
| 9. EXEMPLO MEMORÁVEL — A TELECOM | **4. EXEMPLO DE USO** | Caso completo preservado: narrativa, distribuição de mecanismos, números (R$800k→R$280k, 7 semanas, NPS +12pts), rigor estatístico |
| 8. ANTI-PADRÕES DE ADOÇÃO | **5. ANTI-PADRÕES** | 4 anti-padrões (A, B, C, D) preservados; convertidos de prosa para formato de tabela canônico |
| 10. CONEXÕES COM OUTROS CAPÍTULOS | **6. CONEXÕES** | Todas as 7 conexões preservadas |

### Verificação de preservação de PI

- [x] Tabela dos 6 mecanismos preservada (6 linhas × 3 colunas)
- [x] Tabela das 5 dimensões preservada (5 linhas × 3 colunas)
- [x] Tabela de decisão por capability preservada (7 linhas × 3 colunas)
- [x] Todos os critérios "quando é errado" preservados por mecanismo (6 mecanismos)
- [x] Todos os critérios de migração preservados (3 positivos + 4 negativos)
- [x] Protocolo de 30 minutos preservado (5 passos + regra inegociável)
- [x] Caso da telecom preservado com todos os números e nota de rigor estatístico
- [x] 4 anti-padrões preservados (A, B, C, D)
- [x] 7 conexões preservadas
- [x] Regra de níveis de cobertura (insuficiente/parcial/adequada/completa) preservada
- [x] Nota editorial de neutralidade preservada (incluindo exemplos de origem: REST, gRPC, Kafka, MCP, webhooks)

### Nota sobre contagem de linhas

138 linhas ficam ligeiramente acima do teto de 135 da faixa dos demais frameworks. A diferença de 3 linhas resulta de duas tabelas completas que não têm equivalente em F1 ou F7 (a tabela de 5 dimensões e a de 7 capabilities) — cortar essas tabelas significaria perder PI nuclear do framework. A decisão editorial é manter 138 linhas: o framework está no template canônico de 6 seções e dentro do espírito da faixa.

---

## D8 — F9: Ajuste menor de estrutura

### Contagem de linhas

| Estado | Linhas |
|--------|--------|
| Antes (original) | 129 |
| Depois (ajustado) | 119 |

### Ajuste realizado

| Elemento antes | Posição antes | Posição depois |
|---|---|---|
| Cabeçalho `## POSICIONAMENTO RELATIVO AO C00P` (não numerado, antes de "1. OBJETIVO") | Antes da seção 1, com separador `---` | Eliminado como cabeçalho independente |
| Conteúdo do posicionamento (3 parágrafos: divisão de trabalho C00P/F9, dois bullet points, leitura condicional) | Seção autônoma não numerada | Integrado como 1º parágrafo da seção **1. OBJETIVO**, sem perda de texto |

### Verificação de preservação

- [x] Texto completo do posicionamento C00P/F9 preservado (incluindo os dois bullet points e o parágrafo condicional "Se você leu C00P...")
- [x] Texto original de OBJETIVO preservado (parágrafo sobre padrão vs. número, envelhece bem, com fonte e data)
- [x] Seções 2 a 6 não alteradas
- [x] F9 mantém os 6 cabeçalhos canônicos: OBJETIVO / FUNCIONAMENTO / OUTPUT / EXEMPLO DE USO / ANTI-PADRÕES / CONEXÕES

---

## Confirmação final

- Nenhum framework teve nome, numeração (F1-F9) ou referências cruzadas alterados
- Apenas estrutura interna de F5 e F9 foi modificada
- Nenhum critério, tabela ou caso foi cortado — toda PI está presente nos novos cabeçalhos
