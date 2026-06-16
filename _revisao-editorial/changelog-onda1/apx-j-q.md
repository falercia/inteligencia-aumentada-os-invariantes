# CHANGELOG ONDA 1 — APÊNDICES J, K, O
# Livro: INTELIGÊNCIA AUMENTADA — Livro 1: Os Invariantes
# Data: 2026-06-16
# Escopo: Apenas P0 (conforme instruções da Onda 1)

---

## SUMÁRIO

- P0 editados: 3
- P0 deferidos: 0
- Total P0 identificados na banca (apêndices J, K, O): 3

---

## EDITADOS

### [EDITADO] APX-J-P0-02 — DeepSeek-R1: remoção de afirmação "publicado em Nature em 2025" sem DOI confirmado
**Arquivo:** `04-apendices/L1-APX-J-trilha-do-numero.md`
**Seção:** Seção 3 — Papers que estão movendo o campo em 2025-2026 (tabela, linha DeepSeek-R1)
**Problema (banca):** A célula da coluna "Mês e ano" afirmava "janeiro de 2025, publicado em Nature em 2025" para o paper arXiv:2501.12948. O paper DeepSeek-R1 foi divulgado pelos autores via arXiv em janeiro de 2025; publicação em periódico revisado por pares (Nature ou outro) não estava confirmada com DOI até a data desta revisão. Afirmação incorreta em seção cuja premissa editorial é rastreabilidade factual.
**Alteração aplicada:**
- Texto anterior: `janeiro de 2025, publicado em Nature em 2025`
- Texto posterior: `janeiro de 2025, divulgado por seus autores via arXiv (publicação em periódico revisado por pares não confirmada até a data desta revisão)`
**Princípio editorial aplicado:** vendor-neutral e factualmente defensável — nenhuma afirmação de publicação em periódico sem DOI confirmado. Suavizado sem afirmar veículo e com marcador explícito de verificação pendente, conforme instrução P0.
**Status:** [EDITADO]

---

### [EDITADO] APX-K-P0-01 — Gabaritos: nota honesta de cobertura e escopo adicionada no início do apêndice
**Arquivo:** `04-apendices/L1-APX-K-gabaritos.md`
**Seção:** Cabeçalho (bloco de citação inicial, imediatamente após o bloco de citação de instrução de uso)
**Problema (banca):** O apêndice apresenta-se como "Gabaritos Comentados" sem declarar que cobre menos de 60% dos capítulos com exercícios. O APX-Q (Manual do Professor) admite internamente que o gabarito completo está em construção, mas o leitor do APX-K não tem essa informação. Experiência de frustração capaz de erodir confiança na obra.
**Alteração aplicada:** Adicionado segundo bloco de citação (`>`) imediatamente após o bloco de instrução de uso existente, com:
- Título explícito "Nota editorial — cobertura e escopo (junho de 2026)"
- Lista dos capítulos cobertos na edição atual
- Declaração explícita dos capítulos sem gabarito: C08 (Fine-tuning), C10 (Reasoning), C12-C13 (Agentes), C14 (AI Engineering), C15-C16 (Posicionamento de Mercado)
- Indicação de repositório com link e instrução de *watch* para notificação
**Derivação de conteúdo:** capítulos cobertos e pendentes derivados da análise da banca (Achado 01) e da estrutura interna do APX-K. Lista de capítulos pendentes alinhada com os citados pelo APX-Q e pela banca.
**Status:** [EDITADO]

---

### [EDITADO] APX-O-P0-01 — Governança: dez controles canônicos nomeados e tabelados na ficha conceitual
**Arquivo:** `04-apendices/L1-APX-O-caderno-governanca-v1.md`
**Seção:** Nova seção inserida entre "A anatomia que toda governança de IA precisa fechar" e "Os nove princípios que sustentam o caderno"
**Problema (banca):** Os "dez controles canônicos" eram citados múltiplas vezes na ficha (Bloco 4 da anatomia, anti-padrões, indicadores de saúde) mas nunca nomeados individualmente. Executivo que leva o livro a reunião de board não consegue responder "quais são os dez controles?" sem acesso ao repositório, contrariando a promessa da ficha de ser autossuficiente para defesa diante de auditoria.
**Alteração aplicada:** Inserida seção "Os dez controles canônicos em uma linha" com:
- Parágrafo de contexto situando a seção e apontando para o caderno executável para detalhes de maturidade
- Descrição da escala 0-4 e da meta de operação saudável
- Tabela completa com os dez controles: número, nome, camada (técnica/operacional/executiva) e função resumida
- Nota de derivação editorial informando que o conteúdo reproduz a seção homônima do Capítulo 24 e declarando procedimento de sincronização em revisões futuras
**Derivação de conteúdo:** tabela derivada diretamente do Capítulo 24 (seção "Os dez controles canônicos", linhas 37-48 do arquivo `02-capitulos/L1-C24-governanca.md`). Não é conteúdo novo — é espelhamento da fonte canônica interna do livro para a ficha de referência. Proposta para validação do autor: confirmar que os nomes dos controles no Capítulo 24 são a versão final antes de publicação; se o Capítulo 24 for revisado, esta ficha deve ser atualizada na mesma operação.
**Status:** [EDITADO]

---

## DEFERIDOS

Nenhum P0 deferido neste bloco. Todos os três P0 identificados foram resolvidos com edição cirúrgica nos arquivos reais.

---

## RASTREABILIDADE

| ID banca | Arquivo | Categoria | Status |
|---|---|---|---|
| APX-J/02 | `04-apendices/L1-APX-J-trilha-do-numero.md` | P0 | [EDITADO] |
| APX-K/01 | `04-apendices/L1-APX-K-gabaritos.md` | P0 | [EDITADO] |
| APX-O/01 | `04-apendices/L1-APX-O-caderno-governanca-v1.md` | P0 | [EDITADO] |
