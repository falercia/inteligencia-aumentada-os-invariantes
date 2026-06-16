# F2 — Diagnóstico de Encaixe entre Tarefa e Modelo
## Escolha de modelo por 5 eixos de tarefa

## 1. OBJETIVO

Decidir qual modelo usar para uma tarefa específica, sem cair em "modelo do mês". A decisão é função do **padrão da tarefa** (durável), não da liderança da semana em benchmark agregado (volátil).

## 2. FUNCIONAMENTO

Pontuar a tarefa de 0 a 5 em cinco eixos canônicos, e aplicar a matriz de perfis de família. Modelo escolhido é o de **melhor encaixe ponderado**, não o de melhor benchmark agregado.

### Os 5 eixos

| Eixo | O que pontuar | Perfil de modelo que tende a vencer |
|------|---------------|-------------------------------------|
| **Razão complexa** | Tarefas com múltiplos passos, auditoria do percurso, decisão lógica encadeada | Tier premium dos provedores de fronteira (Claude, GPT, Gemini); reasoning models proprietários e abertos (R1 e equivalentes) |
| **Código** | Edição de código real, com testes, contexto longo, refatoração | Tier premium com força específica em SWE-bench Verified *(mede resolução de bugs reais em repositórios open source — o padrão mais próximo de engenharia real)*, HumanEval *(mede geração de função a partir de docstring)* e LiveCodeBench *(mede código em competições com data de corte recente, evita contaminação de treino)*  — varia por release; posições correntes no Apêndice J |
| **Contexto longo** | Análise de documentos extensos, bases volumosas, múltiplos arquivos | Modelo com janela de contexto mais ampla disponível no provedor escolhido — consultar Apêndice J |
| **Multimodal** | Vídeo, imagem, áudio nativos; OCR, leitura de gráfico | Modelo com suporte multimodal nativo e maturidade em vídeo e áudio — consultar Apêndice J |
| **Custo crítico** | Volume altíssimo, margem apertada, classificação simples em produção | Variante econômica do tier (Haiku, Mini, Flash) ou modelo open weights self-hosted (Llama, Mistral, DeepSeek, Qwen, Phi). **Atenção: são dois caminhos diferentes.** Tier pequeno de provedor = custo variável por API, SLA garantido pelo fornecedor. Self-hosted = custo fixo de infraestrutura + operação de MLOps, SLA gerenciado internamente. A decisão entre os dois é arquitetural — ver Cap 16 para o fluxo completo. |

### Mecânica de aplicação

1. **Pontuar a tarefa** de 0 a 5 em cada eixo. Notas altas indicam que o eixo importa muito para essa tarefa.
2. **Identificar o eixo dominante** (maior nota). Se houver empate entre dois ou três eixos, marcar todos.
3. **Consultar o Apêndice J** para a família corrente que lidera cada eixo dominante.
4. **Escolher pelo melhor encaixe**, com fallback explícito. Se o eixo dominante é "código" + "razão complexa", o premium da família com força em ambos vence.
5. **Definir critério de reavaliação**: a cada seis meses, a cada lançamento de mesmo eixo, ou conforme custo cruzar limite.

> **Regra de desempate quando eixos dominantes apontam para modelos diferentes:** priorize o eixo com maior custo de erro para o negócio. Razão complexa (alto custo de erro em decisões jurídicas, clínicas ou financeiras) vence custo crítico. Custo crítico vence em tarefas de classificação simples e alto volume onde regressão é rapidamente detectável e barata. Em caso de dúvida: qual eixo, se ignorado, causaria o problema mais caro em produção? Esse é o dominante.

## 3. OUTPUT

| Campo | Conteúdo |
|-------|----------|
| Tarefa pontuada nos 5 eixos | Tabela 5×1 com notas |
| Eixo(s) dominante(s) | 1 a 3 eixos com nota ≥4 |
| Modelo escolhido | Família + tier + variante específica (com link ao Apêndice J) |
| Modelo fallback | Para resiliência ou cost ceiling |
| Critério de reavaliação | Cadência e gatilho |

## 4. EXEMPLOS DE USO

### Exemplo A — Classificação de e-mail em larga escala (5M/mês)

| Eixo | Nota |
|------|------|
| Razão complexa | 1 |
| Código | 0 |
| Contexto longo | 1 |
| Multimodal | 0 |
| Custo crítico | 5 |

Eixo dominante: **custo crítico**. Encaixe: variante pequena (Haiku-like) com prompt enxuto ou fine-tuning leve. Fallback: variante pequena de outro vendor. Reavaliação: trimestral ou quando volume mudar de magnitude.

### Exemplo B — Agente de engenharia para refatoração de código legado

| Eixo | Nota |
|------|------|
| Razão complexa | 5 |
| Código | 5 |
| Contexto longo | 4 |
| Multimodal | 0 |
| Custo crítico | 2 |

Eixos dominantes: **código + razão complexa + contexto longo**. Encaixe: tier premium do provedor com melhor desempenho corrente em SWE-bench Verified, consultado no Apêndice J e validado por teste cego na carga real do time. Fallback: tier premium de outro provedor com força em raciocínio matemático complexo. Reavaliação: a cada release relevante de qualquer um dos provedores acompanhados; teste cego comparado em PRs reais a cada quinze dias.

### Exemplo C — Análise de relatório técnico com gráficos e tabelas

| Eixo | Nota |
|------|------|
| Razão complexa | 3 |
| Código | 0 |
| Contexto longo | 4 |
| Multimodal | 5 |
| Custo crítico | 2 |

Eixos dominantes: **multimodal + contexto longo**. Encaixe: modelo com maior maturidade multimodal corrente e janela ampla, consultado no Apêndice J. Fallback: arranjo híbrido com modelo de texto preferido do time e chamada multimodal específica para o anexo via API separada. Reavaliação: semestral, com gatilho antecipado caso o provedor escolhido perca liderança em benchmark multimodal por dois trimestres consecutivos.

## 5. ANTI-PADRÕES

| Anti-padrão | Por que mata |
|-------------|--------------|
| "Lançou novo, vou trocar" | Migração sem teste cego na própria carga troca problema conhecido por desconhecido |
| Usar tier premium para tudo "porque é o melhor" | Viola o Princípio do Custo Composto; em meses, a fatura mostra o erro |
| Não ter fallback | Outage do provedor escolhido vira incidente para o cliente final |
| Decidir por benchmark agregado | Esconde força em eixo específico que importa para sua carga |
| Reavaliar só quando "a equipe quiser" | Sem cadência fixa, vira reação ao boato da semana |
| Confiar em ranking público sem teste cego na carga real | Benchmark agregado não captura o perfil de uso da organização |

## 6. CONEXÕES

- 🔗 Manifesto dos Invariantes
- 🔗 Cap 15 — Comparação de modelos
- 🔗 Cap 18 — Modelos Claude (L2)
- 🔗 Matriz de Cobertura de Integrações (decisão complementar para integração)
- 🔗 Custo Composto em Três Tempos (decisão de tier como vetor de custo)

---

> *"Padrão da tarefa não muda toda rodada. Líder da rodada muda toda rodada. Decida pelo que dura."*
