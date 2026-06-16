# Changelog Onda 3 — APX-L e APX-P

Data: 2026-06-16
Editora: agente Claude (Onda 3 — Clareza, Retenção, Teste da Joana)
Escopo: somente P1; P0 e P2 fora do escopo desta onda

---

## APX-L — Biblioteca de Prompts Profissionais

### Achado 04 — P1 — OBSOLETO PÓS-ONDA2
"Apêndice não ensina a construir prompt novo — apenas a usar os 30."
Referia-se a uma seção a adicionar antes das 30 fichas. As fichas foram removidas do livro na Onda 2 (apenas moldura + índice permaneceram). Achado não se aplica à moldura atual.

### Achado 05 — P1 — [EDITADO]
"Promessa do repositório não-verificável e sem fallback declarado."
Arquivo: `04-apendices/L1-APX-L-biblioteca-prompts.md`
Intervenção: adicionado URL explícito do repositório na célula da tabela de orientação (coluna "Onde vive") e acrescentado parágrafo de política de manutenção com canal de fallback logo após a tabela.
Trecho inserido: "Política de manutenção do repositório: os trinta prompts estão populados e são auditados a cada release do livro. Se o link não funcionar ou o prompt específico não for encontrado, o canal de fallback é o e-mail declarado na página de créditos do livro."

### Achado 06 — P1 — OBSOLETO PÓS-ONDA2
"Quando usar/evitar repete o óbvio em excesso."
Problema era interno às fichas individuais (campo "Quando usar / Quando evitar"). As fichas não existem mais no livro; apenas o índice permanece. Achado não se aplica.

### Achado 07 — P1 — OBSOLETO PÓS-ONDA2
"P-MED-03 sem aviso de restrição regulatória B2C (CFF)."
Ficha específica não está no livro (foi para o repositório). Achado não se aplica.

### Achado 08 — P1 — OBSOLETO PÓS-ONDA2
"P-FIN-02 sem menção à explicabilidade BACEN/LGPD art. 20."
Ficha específica não está no livro. Achado não se aplica.

### Achado 09 — P1 — OBSOLETO PÓS-ONDA2
"Changelog editorial no final — conteúdo mais valioso enterrado."
Não existe changelog editorial no arquivo atual. A moldura pós-Onda 2 não contém changelog de prompts individuais. Achado não se aplica.

### Achado 10 — P1 — [EDITADO]
"Nenhuma ficha menciona comportamento quando modelo recusa por política."
O achado sugeria adicionar um 8º padrão de operação. A seção "Padrões de operação" existe na moldura atual com 7 padrões. Intervenção aplicada diretamente ali.
Arquivo: `04-apendices/L1-APX-L-biblioteca-prompts.md`
Adicionado padrão 8: "Monitore recusas do modelo por categoria de input. [...] Taxa de recusa acima de 5% numa categoria específica é sinal de alarme que exige revisão da constituição ou do contexto."

### Achado 11 — P1 — OBSOLETO PÓS-ONDA2
"P-RH-01 sem menção à auditoria de viés algorítmico."
Ficha específica não está no livro. Achado não se aplica.

### Resumo APX-L
- Editados: 2 (Achados 05, 10)
- Obsoletos pós-Onda 2: 5 (Achados 04, 06, 07, 08, 09, 11) — 6 no total, contando 11
- Já resolvidos: 0
- Deferidos: 0

---

## APX-P — Boxes Técnicos

### Achado 03 — P1 — [EDITADO]
"Box 11 Interação 3: FlashAttention e platô de scaling laws conectados como causa-efeito quando são independentes."
Arquivo: `04-apendices/L1-APX-P-boxes-tecnicos.md`
Intervenção: reescrita completa da Interação 3 (FlashAttention × Scaling Laws). O texto anterior implicava que FlashAttention "amplifica" scaling laws e que o platô decorre dessa relação. Novo texto separa explicitamente as duas alavancas — FlashAttention como alavanca de custo de inferência em contexto longo, platô de scaling como consequência de esgotamento de dados humanos de qualidade e retorno decrescente de parâmetros. Instrução direta ao decisor: otimizar as duas de forma independente.

### Achado 04 — P1 — [EDITADO]
"Box 1: tiebreak leakage citado sem diferenciação de risco on-prem vs. API gerenciada."
Arquivo: `04-apendices/L1-APX-P-boxes-tecnicos.md`
Intervenção: adicionado parágrafo após a descrição dos riscos de tiebreak leakage e expert silencing, distinguindo explicitamente o regime de APIs gerenciadas (responsabilidade do provedor, mas confirmar por escrito) do regime de deploy on-prem com open weights (responsabilidade inteiramente do operador). Reformulada a pergunta estratégica: "quem é responsável pelo isolamento de batch e quais garantias posso exigir por escrito?"

### Achado 05 — P1 — [EDITADO]
"Box 11 usa emojis coloridos como única codificação — ilegível em impressão monocromática."
Arquivo: `04-apendices/L1-APX-P-boxes-tecnicos.md`
Intervenção: adicionado código textual duplo em toda a legenda e em todas as células da matriz (C/S/T/N como codificação primária, emoji como complemento visual). Todas as referências a pares na narrativa do parágrafo abaixo da tabela também atualizadas para usar os códigos textuais. A tabela agora é legível em formato impresso monocromático sem perda de informação.
Nota: a célula Quantização × Mech Interp foi corrigida de T para C (conflito), consistente com o que o texto da Interação 7 descreve como "diretamente conflituosa".

### Achado 06 — P1 — [EDITADO]
"Box 8: referência 'trabalho de seguimento CoT 2024-2025' sem paper específico."
Arquivo: `04-apendices/L1-APX-P-boxes-tecnicos.md`
Intervenção: substituída a referência vaga por orientação de busca ativa com venue/conferência específicos (ACL 2024-2025, EMNLP 2024-2025) e termo de busca em arxiv.org ("causal faithfulness chain-of-thought"). Mantém o espírito de indicar onde aprofundar sem citar paper que pode não existir ou estar ultrapassado.

### Achado 07 — P1 — [EDITADO]
"Box 5: S-LoRA mencionado sem referência primária."
Arquivo: `04-apendices/L1-APX-P-boxes-tecnicos.md`
Intervenção: adicionada referência primária na seção "Onde aprofundar" do Box 5: Sheng et al. "S-LoRA: Serving Thousands of Concurrent LoRA Adapters", 2023, arxiv.org/abs/2311.03285. Padrão de citação agora consistente com os demais boxes.

### Resumo APX-P
- Editados: 5 (Achados 03, 04, 05, 06, 07)
- Obsoletos pós-Onda 2: 0
- Já resolvidos: 0
- Deferidos: 0

---

## Totais consolidados

| Apêndice | Editados | Já resolvidos | Obsoletos pós-Onda 2 | Deferidos |
|---|---|---|---|---|
| APX-L | 2 | 0 | 6 | 0 |
| APX-P | 5 | 0 | 0 | 0 |
| **Total** | **7** | **0** | **6** | **0** |

Total de P1s analisados: 13 (8 APX-L + 5 APX-P)
