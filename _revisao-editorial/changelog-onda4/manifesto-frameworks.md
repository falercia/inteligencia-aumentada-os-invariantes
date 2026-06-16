# CHANGELOG ONDA 4 — Manifesto + Frameworks
## Escopo: P2 da banca-01-manifesto-frameworks.md
## Data: 2026-06-16

---

## RESUMO

| Status | Quantidade |
|--------|-----------|
| EDITADO | 15 |
| JÁ RESOLVIDO (ondas anteriores) | 0 |
| DEFERIDO | 2 |

---

## EDITADOS

### C00M-03 — Analogia navegação condensada para 1 parágrafo
- **Arquivo:** L1-C00M-manifesto-invariantes.md
- **Seção:** A NAVEGAÇÃO COMO ANALOGIA
- **Ação:** Reduzido de 3 parágrafos densos para 1 parágrafo enxuto. O núcleo da analogia e a ponte com os invariantes foram preservados; os exemplos detalhados do barco (madeira→aço, vento→nuclear) foram condensados na abertura do parágrafo único.

### C00M-04 — Drucker e Engelbart com ponte para IA generativa
- **Arquivo:** L1-C00M-manifesto-invariantes.md
- **Seção:** REFERÊNCIAS PRINCIPAIS — Sobre o operador como multiplicador
- **Ação:** Adicionadas 1-2 frases de ponte explícita para cada referência, conectando o argumento original (Drucker: método > talento; Engelbart: ferramenta amplifica na proporção da habilidade) ao Princípio 9 (amplificação bidirecional da instrução).

### C00M-05 — Exercício versão de bolso com exemplos concretos
- **Arquivo:** L1-C00M-manifesto-invariantes.md
- **Seção:** EXERCÍCIOS — Versão de bolso para o time
- **Ação:** Adicionado bloco de exemplo após o exercício, demonstrando a transformação para dois princípios (Plausibilidade e Termômetro): linguagem técnica → linguagem operacional da empresa.

### C00P-03 — Seção P.9 reduzida (repetia P.8.5)
- **Arquivo:** L1-C00P-porque-padrao-dura.md
- **Seção:** P.9 — CONVITE AO LIVRO
- **Ação:** Seção reduzida de 3 parágrafos longos para 2 parágrafos curtos. Eliminadas repetições de instrução metodológica que P.8.5 já cobria com mais elegância. Mantido o remate com a lista dos quatro ciclos históricos.

### C00P-04 — Preços de fine-tuning movidos para nota datada
- **Arquivo:** L1-C00P-porque-padrao-dura.md
- **Seção:** P.4 — CASO HISTÓRICO 3
- **Ação:** "US$ 100.000 e US$ 500.000" substituído por "ticket de seis dígitos em dólares" com nota entre parênteses remetendo ao Apêndice J e reconhecendo autocontradição metodológica (o próprio capítulo prega separar número de padrão).

### F1-03 — Campo Revisão Programada com cadência-padrão
- **Arquivo:** L1-F1-decid-ia.md
- **Seção:** 3. OUTPUT — tabela de campos
- **Ação:** Campo "Revisão programada" expandido com cadência-padrão sugerida por nível de autonomia: 90 dias (piloto interno), 6 meses (Assistente/Co-piloto em produção), 3 meses (Agente Supervisionado/Autônomo Regulado).

### F2-03 — Benchmarks de código com glossário inline
- **Arquivo:** L1-F2-encaixe-5.md
- **Seção:** 2. FUNCIONAMENTO — eixo Código
- **Ação:** SWE-bench Verified, HumanEval e LiveCodeBench receberam definições inline entre parênteses explicando o que cada benchmark mede, com referência ao Apêndice J para posições correntes.

### F3-03 — Critério de N dias com guia de calibração
- **Arquivo:** L1-F3-agente-prop.md
- **Seção:** 2. FUNCIONAMENTO — Gates de promoção
- **Ação:** "N dias (tipicamente 14-30)" substituído por tabela de calibração explícita: 14 dias (reversível, impacto interno), 30 dias (efeito externo), 60 dias ou mais (irreversível, alto impacto). Exigência de justificativa para N abaixo do padrão.

### F4-02 — Cobertura de prompts multimodais
- **Arquivo:** L1-F4-prompt-ext.md
- **Seção:** 2. FUNCIONAMENTO — Bloco 3
- **Ação:** Adicionada nota sobre prompts multimodais: input visual vai no Bloco 3; a Constituição (Bloco 2) deve cobrir explicitamente o tratamento de conteúdo visual.

### F4-03 — Instrução para manejo do Bloco 3 quando cresce além do limite
- **Arquivo:** L1-F4-prompt-ext.md
- **Seção:** 2. FUNCIONAMENTO — Bloco 3
- **Ação:** Adicionada regra de posição inegociável: Bloco 3 cresce até o ponto em que Bloco 4 ainda está na posição forte. Referência explícita a T3 do F7 como protocolo de compressão.

### F5-03 — Subseção "Quando Migrar de Mecanismo Existente"
- **Arquivo:** L1-F5-cobertura-integracoes.md
- **Seção:** Nova seção 7 (seções 8-11 renumeradas de 8-10 para 9-11)
- **Ação:** Adicionada subseção com critérios que justificam migração (custo de manutenção, requisito não atendível, incidente recorrente) e critérios que não justificam (moda, conferência, SDK novo do fornecedor).

### F6-02 — Anti-padrão terceirização com distinção legítima/ilegítima
- **Arquivo:** L1-F6-gov-indelegavel.md
- **Seção:** 5. ANTI-PADRÕES
- **Ação:** Anti-padrão "Vamos terceirizar o problema" reformulado para distinguir: accountability não terceiriza (nome interno obrigatório); execução especializada terceirizada (auditoria externa, DPIA, certificação ISO) é legítima e recomendada.

### F6-03 — AI Council com cadência-padrão generalizada
- **Arquivo:** L1-F6-gov-indelegavel.md
- **Seção:** 2. FUNCIONAMENTO — Os 10 controles, controle 10
- **Ação:** Controle 10 expandido com cadência mínima generalizada: mensal nos primeiros 12 meses, trimestral após revisão de maturidade no primeiro ano; permanece mensal em setores regulados.

### F7-03 — Diagnóstico de pré-requisito antes das alavancas
- **Arquivo:** L1-F7-composto-3t.md
- **Seção:** 2. FUNCIONAMENTO — antes de "Ordem de aplicação"
- **Ação:** Adicionada subseção "Diagnóstico de pré-requisito" com dois caminhos: (1) com atribuição de custo instalada (Pilar 5 LLMOps) → decisão por dado; (2) sem atribuição → estimativa inicial por sintoma (volume premium > 70%, loops visíveis, contexto > 50%).

### F8-03 — Guia de construção de adversarial set por domínio
- **Arquivo:** L1-F8-eval-piramide.md
- **Seção:** 2. FUNCIONAMENTO — Transversal adversarial e segurança
- **Ação:** Adicionado parágrafo "Construção por domínio" com três fontes (incidentes anteriores, literatura de segurança, brainstorm adversarial) e exemplos de categorias dominantes por setor (RH, financeiro, clínico, consultoria).

### TRANSV-01 — Notas de escopo de observabilidade em F6 e F7
- **Arquivos:** L1-F6-gov-indelegavel.md, L1-F7-composto-3t.md
- **Seção:** 1. OBJETIVO (bloco de escopo adicionado ao início)
- **Ação:** F3 e F5 já tinham nota de escopo de ondas anteriores. F6 e F7 receberam nota equivalente declarando âncora autoritativa (Cap 22) e escopo restrito de cada framework (F6 = governança/auditoria; F7 = custo). Completa o achado transversal P0.

---

## DEFERIDOS

### F3-01 — Matriz visual 4×4
- **Arquivo:** L1-F3-agente-prop.md
- **Motivo:** Requer diagrama gráfico. Não implementável via edição de texto Markdown.

### F9-04 — F9 sem exemplo memorável com números reais
- **Arquivo:** L1-F9-rota-dupla.md
- **Status:** EDITADO (reclassificado de DEFERIDO para EDITADO durante execução)
- **Ação:** Adicionado caso ilustrativo composto "O custo de confundir número com padrão" — Head de Tecnologia de SaaS B2B, três migrações em 18 meses, R$ 280 mil em custo acumulado, quarta decisão resolvida em 45 minutos com aplicação do F2 + Apêndice J.

---

## NOTA DE RECONCILIAÇÃO

O item F9-04 foi inicialmente marcado como DEFERIDO mas foi executado durante a onda. Portanto:

| Status | Quantidade |
|--------|-----------|
| EDITADO | 16 |
| JÁ RESOLVIDO (ondas anteriores) | 0 |
| DEFERIDO | 1 (F3-01 — matriz visual) |
