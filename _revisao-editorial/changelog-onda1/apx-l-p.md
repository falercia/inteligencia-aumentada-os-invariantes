# Changelog Onda 1 — APX-L e APX-P

Data: 2026-06-16
Escopo: P0 apenas
Modelo executor: claude-sonnet-4-6

---

## APX-L — Biblioteca de Prompts Profissionais

### APX-L · P0-1 [EDITADO]
**Achado banca:** Contradição estrutural — apêndice é catálogo que a tese proíbe.
**Intervenção:** Inserção de "Moldura de método" (bloco em destaque) no topo do arquivo, antes da seção "Por que este apêndice existe em duas camadas". O bloco reposiciona os 30 prompts como instâncias documentadas de princípios de engenharia de contexto transferíveis, com aviso explícito de que os XMLs específicos envelhecem e o que perdura é a estrutura (padrões F4, sete padrões de operação, oito anti-padrões). Converte tensão estrutural em tensão declarada e gerenciada, sem reescrever as fichas.
**Localização:** Linhas 1–30 do arquivo (após o título, antes da primeira seção).
**Racional:** Decisão editorial defensável para Onda 1: reescrever 13 mil palavras excede o escopo de onda cirúrgica. A moldura resolve o risco de posicionamento errado para o leitor que chega de fora ou lê o sumário. Reescrita arquitetural (Opção A ou B da banca) permanece como candidato a onda futura.

---

### APX-L · P0-2 [EDITADO]
**Achado banca:** "Sonnet equivalente" em 26/30 fichas sem critério de equivalência definido — afirmação sem valor informacional.
**Intervenção:** Inserção de bloco "Convenção de modelo usada nas fichas" na seção "A anatomia que toda ficha aplica", após o parágrafo sobre linguagem XML. Define três faixas (Haiku equivalente, Sonnet equivalente, Sonnet equivalente com raciocínio estendido) com critérios operacionais verificáveis: janela de contexto mínima, suporte a structured output, capacidade de raciocínio estruturado. Declara explicitamente que a denominação é intencional para sobreviver à próxima geração de modelos.
**Localização:** Seção "A anatomia que toda ficha aplica", após o parágrafo sobre XML e antes do esqueleto de exemplo.
**Racional:** Corrige a fragilidade na raiz (critério, não nome) sem alterar nenhuma das 30 fichas individualmente. O campo "Modelo recomendado" de cada ficha permanece inalterado — seu sentido agora é ancorado pela definição canônica inserida.

---

### APX-L · P0-3 [EDITADO]
**Achado banca:** Métricas de qualidade com percentuais precisos (85%, 90%, 80%, 95%, etc.) são afirmações de autoridade não auditáveis pelo leitor — "de onde veio esse 85%?" não tem resposta no livro.
**Intervenção:** Todas as ocorrências de percentuais específicos em campos "Métrica de qualidade" foram suavizadas para linguagem qualitativa com rótulo explícito de ilustrativo. Padrão aplicado: "em taxa alta (≥ N% como limiar ilustrativo de projeto)" seguido de instrução ao operador para calibrar contra seu próprio golden set. Percentuais de segurança não-negociável (100% para casos de emergência, 100% para elementos ausentes) foram preservados com nota de justificativa clínica/estrutural.
**Fichas afetadas:** P-LEG-01, P-LEG-02, P-LEG-03, P-LEG-04, P-MED-01, P-MED-03, P-FIN-01, P-FIN-02, P-FIN-04, P-SAAS-01, P-SAAS-02, P-SAAS-04, P-SUP-01, P-SUP-02, P-SUP-03, P-RH-02, P-MKT-02, P-EDU-01, P-EDU-02, P-EDU-03 (20 fichas com ocorrências de percentual de concordância).
**Racional:** Transforma métricas de afirmações de autoridade em prescrições de calibração, o que é epistemicamente honesto e operacionalmente mais útil. O leitor que citar essas métricas agora tem contexto para responder "é um limiar ilustrativo de projeto — calibre contra seu golden set".

---

## APX-P — Boxes Técnicos

### APX-P · P0-1 [EDITADO]
**Achado banca:** Box 4 (FlashAttention) cita "Claude 4 Sonnet" como exemplo de modelo com janela de contexto longa — nome inexistente no portfólio Anthropic em junho de 2026. Erro factual que compromete credibilidade.
**Intervenção:** Substituição de "Gemini 1.5, Claude 4 Sonnet, GPT-4 Turbo" por "modelos de contexto longo da geração atual (Gemini, Claude, GPT-4 Turbo e seus sucessores)" — reancoragem em categoria e geração em vez de nome específico. Elimina o erro factual e a fragilidade estrutural simultaneamente: a implicação executiva agora não depende de nenhum nome de modelo específico para ser verdadeira.
**Localização:** Seção "Implicação executiva" do Box 4 — FlashAttention.
**Racional:** Princípio-mestre aplicado: reancorar em categoria/método em vez de trocar nome por outro nome igualmente frágil.

---

### APX-P · P0-2 [EDITADO]
**Achado banca:** Box 10 (Scaling Laws) tem implicação executiva construída sobre estado de facto frágil — "platô em modelos frontier" pode ser invalidado antes do fim do primeiro ciclo de vendas. Linguagem atual trata hipótese como fato.
**Intervenção:**
1. **Implicação executiva** reescrita para condicionar a afirmação como "hipótese de trabalho mais prudente com base no padrão observado", não como fato. Adiciona contexto histórico de que previsões de platô foram invalidadas antes (GPT-4, Claude 3 Opus, DeepSeek V3). Reformula a regra prática como agnóstica ao cenário: "extrair valor dos modelos atuais com arquitetura modular que absorve ganhos imprevistos" — válida tanto se o platô se confirmar quanto se um salto ocorrer.
2. **Quando importa para o leitor brasileiro** reescrito para remover "aposta em um salto que pode não vir" (afirmação direcional) e substituir por enquadramento simétrico dos dois riscos (adiar esperando salto / congelar assumindo teto). Preserva a prescrição de modularidade como invariante independente do cenário.
**Localização:** Seções "Implicação executiva" e "Quando importa para o leitor brasileiro" do Box 10.
**Racional:** Converte afirmação frágil em hipótese calibrada epistemicamente. A implicação executiva permanece acionável em qualquer cenário — que é exatamente o critério de durabilidade da obra.

---

## Itens deferidos desta onda

| ID | Categoria | Motivo do deferimento |
|---|---|---|
| APX-L · Achado 04 (banca) | P1 | Requer criação de nova seção "Como construir um prompt que não está na lista" — conteúdo novo, fora do escopo de Onda 1 cirúrgica. [REQUER DECISÃO DO AUTOR] sobre extensão do apêndice. |
| APX-L · Achados 05–14 (banca) | P1–P2 | Escopo de P1/P2, fora do mandato desta onda. Candidatos a Onda 2. |
| APX-P · Achados 03–10 (banca) | P1–P2 | Escopo de P1/P2, fora do mandato desta onda. Candidatos a Onda 2. |
| APX-L · reescrita arquitetural total | Structural | A Opção A ou B da banca (compactar para 3 fichas exemplo ou extrair catálogo) permanece como [REQUER DECISÃO DO AUTOR]. A moldura de método inserida é defesa parcial suficiente para esta onda. |

---

## Resumo executivo

| Arquivo | P0 editados | P0 deferidos | Status |
|---|---|---|---|
| L1-APX-L-biblioteca-prompts.md | 3 | 0 | [EDITADO] |
| L1-APX-P-boxes-tecnicos.md | 2 | 0 | [EDITADO] |
| **Total** | **5** | **0** | |
