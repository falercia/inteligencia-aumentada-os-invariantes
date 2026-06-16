# F8 — Pirâmide da Avaliação
## Pirâmide de Evals por criticidade

## 1. OBJETIVO

Decidir **quanto investir em cada camada de eval**, em função do risco da tarefa e do custo de cada camada. Garantir que nenhum sistema entre em produção sem cobertura mínima e que recursos de eval mais caros (humano especialista) sejam alocados onde fazem diferença.

## 2. FUNCIONAMENTO

Hierarquia de três camadas verticais + uma faixa transversal. Cada camada cobre um percentual diferente da carga e tem custo diferente.

### Base — Determinística

**O que mede.** Estrutura da saída, formato, campos críticos, presença de elementos obrigatórios.

**Técnicas.** Schema validation, exact match em campos críticos, regex para padrões obrigatórios, validações estruturais.

**Cobertura.** 100% das chamadas, em CI antes do merge e em produção como primeiro filtro.

**Custo.** Muito baixo. Implementação leva horas a poucos dias.

**Detecta.** Regressões grosseiras (formato quebrado, campo faltante, alucinação estrutural).

### Meio — Golden Set + LLM-as-judge calibrado

**O que mede.** Qualidade semântica contra rubrica explícita, faithfulness, relevância, completude.

**Técnicas.** Golden set fixo com gabarito + LLM-as-judge aplicando rubrica calibrada contra humano em pelo menos 30 itens. Juiz diferente do gerador. Ensemble em decisões críticas.

**Cobertura.** 30% a 80% das chamadas conforme criticidade.

**Custo.** Médio. Implementação leva 1-4 semanas. Manutenção exige revisão do golden set e recalibração mensal do juiz.

**Detecta.** Regressão de qualidade que escapa da base. Cobre tarefas onde exact match não funciona (geração aberta).

### Topo — Rubrica humana especialista

**O que mede.** Nuances específicas de domínio que LLM-as-judge não capta.

**Técnicas.** Revisão de amostra por especialista do domínio, em release crítico, em auditoria mensal ou trimestral, em incidente sob investigação.

**Cobertura.** 5% a 15% da carga, por amostra.

**Custo.** Alto. Demanda especialista do domínio em horas dedicadas.

**Detecta.** Erros sutis específicos do domínio. Calibra o juiz LLM contra o critério humano.

### Transversal — Adversarial e segurança

**O que mede.** Casos que sabidamente quebram o sistema — jailbreak, prompt injection, conteúdo proibido, sycophancy, viés, honestidade de citação, over-refusal, calibração de incerteza.

**Técnicas.** Conjunto adversarial separado, renovado a cada trimestre. Casos vindos de produção (incidentes anteriores) e de literatura (HarmBench, JailbreakBench, BBQ).

**Construção por domínio.** Não copiar o adversarial set de outro sistema — construir a partir de três fontes: (1) incidentes anteriores do próprio sistema ou de sistemas similares no setor; (2) literatura de segurança como baseline (HarmBench, JailbreakBench, BBQ); (3) brainstorm adversarial com o time de produto: "o que queríamos que o modelo nunca fizesse?". Categorias dominantes por setor: em RH, viés demográfico na triagem; em financeiro, sycophancy em análise de risco (modelo concorda com a tese do analista mesmo quando os dados contradizem); em clínico, over-confidence em diagnóstico diferencial; em consultoria estratégica, números invertidos sutilmente e omissão de risco crítico.

**Cadência.** Mensal por padrão. **Política de bloqueio: zero passagens — qualquer passagem em adversarial de segurança bloqueia merge automaticamente.** Exceção documentada requer aprovação do dono nominal do sistema. Bloqueia release crítico se regredir.

**Custo.** Médio-alto. Exige curadoria contínua.

**Detecta.** Falhas comportamentais que as camadas verticais não cobrem por design.

## 3. OUTPUT

| Campo | Conteúdo |
|-------|----------|
| Mapa de cobertura por camada | % atual em base, meio, topo, adversarial |
| Mapa-meta em 90 dias | % desejado por camada |
| Golden set inicial | 30-50 casos com gabarito, cobrindo: (1) tipos de tarefa com maior volume em produção; (2) subgrupos onde regressão seria mais custosa; (3) edge cases de incidentes anteriores; (4) casos onde o modelo falha atualmente |
| Rubrica de LLM-as-judge calibrada | 4-6 critérios objetivos, com correlação alvo ≥0,7 contra humano |
| Adversarial set inicial | 20+ casos por categoria de segurança crítica |
| Política de bloqueio em CI | Delta que bloqueia merge, delta que alerta, delta que passa — incluindo adversarial: **zero passagens em adversarial de segurança bloqueia merge** (exceção requer aprovação documentada do dono nominal) |
| Cadência de revisão | Golden set: trimestral. Adversarial: mensal. Calibração de juiz: mensal. |

## 4. EXEMPLO DE USO — ATLAS STRATEGY PÓS-INCIDENTE

Consultoria estratégica BR, após o incidente dos números trocados no relatório (Cap 21).

**Estado anterior.** Vibe-eval (3 sócios na sexta). 0% de cobertura em qualquer camada da pirâmide.

**Plano de pirâmide v1:**

| Camada | Cobertura | Conteúdo |
|--------|-----------|----------|
| Base | 100% | Schema validation do relatório (seções obrigatórias, números formatados, citação presente) |
| Meio | 100% | Golden set de 80 relatórios reais com gabarito de números e tese. LLM-as-judge com rubrica de faithfulness numérico (4 critérios). Juiz = Claude Opus (gerador = Sonnet). Calibrado contra 3 sócios em 30 itens, correlação 0,82 |
| Topo | 10% | Auditoria semanal de partner em release crítico. Trimestralmente, auditoria externa por consultor sênior independente |
| Adversarial | mensal | 30 casos: paciente com sycophancy (cliente forçando conclusão), prompt injection via dado de cliente, números invertidos sutilmente, citação de fonte inexistente, omissão de risco crítico |

**Política de bloqueio.** Faithfulness numérico ≥0,95 (delta máximo 1 ponto contra baseline). Adversarial: zero passagens. Caso falhe, merge bloqueado automaticamente.

**Resultado em 6 meses.** Regressões silenciosas zeraram. Tempo de revisão humana caiu 50% — gate filtra ruído antes de o humano ver.

## 5. ANTI-PADRÕES

| Anti-padrão | Por que mata |
|-------------|--------------|
| Construir o topo da pirâmide sem a base | Humano revisa muito, identifica pouco, time não escala |
| LLM-as-judge sem calibração contra humano | Viés institucionalizado; auto-validação inflada |
| Golden set único, sem renovação | Vira folclore que não bate com produção atual |
| Adversarial só de literatura, sem casos de produção | Cobertura teórica, falhas reais escapam |
| Métrica única agregada (acurácia média) | Esconde regressão por subgrupo crítico |
| "Eval é caro" como justificativa para não fazer | Regressão silenciosa é mais cara, descoberta tarde |

## 6. CONEXÕES

- 🔗 Manifesto dos Invariantes
- 🔗 Cap 06 — RAG (RAGAS aplicado ao meio da pirâmide)
- 🔗 Cap 08 — Fine-tuning (decisão sustentada por golden set)
- 🔗 Cap 21 — Evals
- 🔗 Cap 22 — LLMOps (pilares 1, 2 e 3 sustentam o framework)
- 🔗 Cap 23 — Alignment (adversarial cobre 8 safety categories)
- 🔗 Cap 24 — Governança (eval em CI é controle técnico canônico)
- 🔗 Método de Decisão para Adotar IA (Pergunta 4 — linha de medição — alimenta o plano de pirâmide)
- 🔗 Escala de Propriedade do Agente (níveis de autonomia exigem cobertura proporcional na pirâmide)

---

> *"A pirâmide é barata na base, cara no topo. Quem inverte paga muito sem cobrir bem. Quem ignora paga em incidente."*
