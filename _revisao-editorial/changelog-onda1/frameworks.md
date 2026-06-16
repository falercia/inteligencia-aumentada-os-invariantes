# CHANGELOG ONDA 1 — FRAMEWORKS
## Data: 2026-06-16
## Escopo: Correção de achados P0 da banca-01-manifesto-frameworks.md

---

## SUMÁRIO

| # | Framework | Achado | Categoria | Status |
|---|-----------|--------|-----------|--------|
| 1 | F5 | Achado 04 — Sobreposição observabilidade/conformidade com F3 e F6 | P0 | [EDITADO] |
| 2 | F9 | Achado 03 — Sobreposição estrutural com C00P sem divisão de trabalho | P0 | [EDITADO] |
| 3 | TRANSV-01 | Observabilidade em 4 frameworks sem âncora autoritativa | P0 | [EDITADO PARCIALMENTE — ver nota] |

---

## DETALHE DAS INTERVENÇÕES

---

### [EDITADO] F5 — Achado 04 P0
**Arquivo:** `03-frameworks/L1-F5-cobertura-integracoes.md`
**Problema:** Dimensão "Observabilidade" e dimensão "Conformidade" da Matriz de Cobertura duplicavam parcialmente escopo de F3 (eixo X) e F6 (controles 2 e 7), sem indicação de qual framework é autoritativo para cada aspecto.
**Correção aplicada:** Inserção de bloco "ESCOPO DESTE FRAMEWORK" antes da seção 1, delimitando:
- Observabilidade de integração (F5) vs. observabilidade de agente (F3) vs. LLMOps (Cap 22 — âncora autoritativa).
- Conformidade de integração (F5) vs. governança institucional (F6).
**Localização da edição:** Antes de `## 1. OBJETIVO`.
**Tipo de mudança:** Inserção de bloco de escopo — sem alteração de conteúdo existente.

---

### [EDITADO] F9 — Achado 03 P0
**Arquivo:** `03-frameworks/L1-F9-rota-dupla.md`
**Problema:** Sobreposição estrutural com C00P (Por Que Padrão Dura e Número Morre) sem divisão de trabalho explicitada. Leitor que lê ambos pode perceber F9 como repetição; leitor que lê apenas F9 pode saltar C00P perdendo a evidência histórica.
**Correção aplicada:** Inserção de bloco "POSICIONAMENTO RELATIVO AO C00P" antes da seção 1, com divisão de trabalho explícita:
- C00P = argumento histórico (*por que* a distinção existe).
- F9 = protocolo operacional (*como* operar a distinção no dia a dia).
**Localização da edição:** Antes de `## 1. OBJETIVO`.
**Tipo de mudança:** Inserção de bloco de posicionamento — sem alteração de conteúdo existente.

---

### [EDITADO PARCIALMENTE] TRANSV-01 — Observabilidade em 4 frameworks sem âncora
**Arquivos tocados:** `03-frameworks/L1-F3-agente-prop.md`, `03-frameworks/L1-F5-cobertura-integracoes.md`
**Arquivos NÃO tocados (deferidos):** `03-frameworks/L1-F6-gov-indelegavel.md`, `03-frameworks/L1-F7-composto-3t.md`
**Problema:** Conceito de observabilidade aparece em F3, F5, F6 e F7 com escopos distintos e sem âncora autoritativa declarada.
**Correção aplicada em F5:** Bloco de escopo (ver achado F5-04) nomeia Cap 22 como âncora e delimita F3, F5, F6 e F7.
**Correção aplicada em F3:** Inserção de nota de escopo inline após o objetivo, diferenciando observabilidade de agente (F3) de observabilidade de integração (F5), governança (F6) e custo (F7), com remissão ao Cap 22.

**Justificativa para não tocar F6 e F7:**
- F6 controle 5 já cita "pilares de LLMOps" — remissão implícita ao mesmo capítulo autoritativo; inserir mais uma nota criaria ruído sem ganho marginal.
- F7 já cita explicitamente "Pilar 5 de LLMOps" e "atribuição de custo" — o escopo está delimitado pela própria linguagem existente.
- Tocar F6 e F7 requereria leitura completa dos arquivos para garantir que a inserção não cria conflito com outras referências — escopo conservador de Onda 1 recomenda deixar para Onda 2 com revisão de P1.

---

## ACHADOS P0 NÃO EDITADOS (DEFERIDOS)

Nenhum P0 foi inteiramente deferido sem correção. O P0 transversal foi parcialmente editado (F3 e F5); F6 e F7 são deferidos para Onda 2 com justificativa acima.

---

## RECOMENDAÇÃO EDITORIAL — DIVISÃO DE TRABALHO SUGERIDA (para Onda 2)

Para F6 e F7, sugerir ao autor inserção de nota idêntica em formato padronizado:

> **Observabilidade neste contexto:** [F6: governança e auditoria imutável / F7: custo e atribuição por feature]. Âncora completa de observabilidade de IA em produção: Cap 22 — LLMOps.

Isso completa o mapa transversal de forma consistente sem edição estrutural dos frameworks.

---

## ARQUIVOS EDITADOS

1. `/Users/fabiogarcia/Documents/Personal/Livros/Ebook IA/Livro-1-Os-Invariantes/03-frameworks/L1-F5-cobertura-integracoes.md`
2. `/Users/fabiogarcia/Documents/Personal/Livros/Ebook IA/Livro-1-Os-Invariantes/03-frameworks/L1-F9-rota-dupla.md`
3. `/Users/fabiogarcia/Documents/Personal/Livros/Ebook IA/Livro-1-Os-Invariantes/03-frameworks/L1-F3-agente-prop.md`
