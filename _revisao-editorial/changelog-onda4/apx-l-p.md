# Changelog Onda 4 — APX-L e APX-P

Data: 2026-06-16
Passa: ACABAMENTO (P2)
Arquivos editados:
- `04-apendices/L1-APX-L-biblioteca-prompts.md`
- `04-apendices/L1-APX-P-boxes-tecnicos.md`

---

## APX-L — Biblioteca de Prompts Profissionais

### Achado 12 [EDITADO] — P2
**Problema:** "Princípio Três, a Camada Dupla" sem referência ao capítulo onde é definido.
**Localização:** Seção "Por que este apêndice existe em duas camadas", terceiro parágrafo.
**Antes:** `...e materializa o Princípio Três, a Camada Dupla.`
**Depois:** `...e materializa o Princípio Três, a Camada Dupla (definido no capítulo de abertura "Os Nove Invariantes").`
**Decisão:** Referência cirúrgica ao capítulo real, sem número de capítulo pois o manifesto precede a numeração ordinária.

### Achado 13 [OBSOLETO] — P2
**Problema:** URL de repositório longa — inacessível em formato impresso.
**Status:** O apêndice foi completamente reescrito na Onda 2 e não contém mais fichas individuais com campo "Versão executável". O índice atual usa identificadores curtos `/prompts/P-LEG-01` etc. em tabela compacta. O problema reportado pela banca não existe na versão atual.

### Achado 14 [OBSOLETO] — P2
**Problema:** P-MKT-01 menciona canais com limites de caracteres que mudam.
**Status:** O apêndice atual não tem fichas expandidas. P-MKT-01 existe apenas como linha de índice na tabela final, sem corpo de ficha que pudesse conter texto sobre canais específicos. O conteúdo expandido vive no repositório (fora do livro). Problema inexistente na versão atual.

---

## APX-P — Boxes Técnicos

### Achado 08 [EDITADO] — P2
**Problema:** Box 6 (Quantização e Destilação) cita Phi-3 e Gemini Nano como exemplos de destilação sem mencionar DeepSeek-R1-Distill, caso mais relevante em 2025-2026.
**Localização:** Mecanismo técnico do Box 6, parágrafo sobre destilação clássica.
**Antes:** `Modelos como Phi-3, da Microsoft, e Gemini Nano são exemplos públicos de modelos pequenos treinados com destilação intensiva a partir de modelos maiores, atingindo qualidade impressionante para seu tamanho.`
**Depois:** `Modelos como Phi-3, da Microsoft, Gemini Nano e a família DeepSeek-R1-Distill são exemplos públicos de modelos pequenos treinados com destilação intensiva a partir de modelos maiores, atingindo qualidade impressionante para seu tamanho — em particular em tarefas de raciocínio estruturado, caso em que DeepSeek-R1-Distill demonstrou capacidade próxima a modelos frontier em variantes de sete bilhões de parâmetros.`
**Decisão:** Adição cirúrgica na sentença existente. Não adicionada referência bibliográfica específica ao DeepSeek-R1 (paper DeepSeek-AI, 2025 — arxiv.org/abs/2501.12948) pois o Box 6 já tem quatro referências e a menção no corpo basta para orientar o leitor técnico.

### Achado 09 [EDITADO] — P2
**Problema:** A epígrafe final ("Cada um destes boxes existe porque...") é o conteúdo mais memorável do apêndice e estava enterrada após o Box 11.
**Localização:** Movida de após o `---` final para o início da seção "Como usar este apêndice".
**Operação:** Epígrafe inserida como blockquote itálico imediatamente após o título da seção, antes do primeiro parágrafo do corpo. Versão original ao final do arquivo removida.
**Decisão:** A frase âncora o enquadramento antes de o leitor entrar nos boxes — exatamente o efeito que a banca recomendou.

### Achado 10 [EDITADO] — P2
**Problema:** Mapa de boxes referencia os Princípios (P1 a P9) sem indicar onde estão definidos; leitor que chega diretamente ao Apêndice P não sabe onde encontrá-los.
**Localização:** Tabela "Mapa de boxes", imediatamente após a linha do Box 11.
**Adição:** Nota de rodapé em blockquote após a tabela: `Nota: os Princípios (P1 a P9) são definidos no capítulo de abertura "Os Nove Invariantes da Inteligência Artificial". Verbetes rápidos em ordem alfabética estão no Apêndice A — Glossário.`
**Decisão:** Referência dupla (manifesto + glossário) cobre tanto o leitor que quer a definição completa quanto o que precisa de consulta rápida.

---

## Sumário por apêndice

| Apêndice | Editados | Já resolvidos | Obsoletos | Deferidos |
|---|---|---|---|---|
| APX-L | 1 | 0 | 2 | 0 |
| APX-P | 3 | 0 | 0 | 0 |
| **Total** | **4** | **0** | **2** | **0** |
