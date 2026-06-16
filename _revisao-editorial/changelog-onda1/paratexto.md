# Changelog ONDA 1 — Correções P0 · Paratexto
Data: 2026-06-16
Editor: Claude (claude-sonnet-4-6)

---

## P0-1 · L1-00-capa-e-titulos.md · Achado 01
**Status:** [EDITADO]
**Problema:** Dois subtítulos concorrentes no mesmo arquivo sem declaração de qual é o canônico ("Os Princípios Permanentes da IA" na linha 2 vs. "O manual conceitual e executivo para entender, decidir e governar inteligência artificial moderna." na linha 9).
**Antes:** Seção `## TÍTULO E SUBTÍTULO` com os dois textos misturados sob o mesmo cabeçalho, sem distinção de função.
**Depois:** Separados em dois cabeçalhos explícitos: `## SUBTÍTULO CANÔNICO (capa, ISBN, distribuidores)` com "Os Princípios Permanentes da IA" e `## TAGLINE DE MARKETING (sinopse, e-mail, redes)` com a frase longa. Elimina ambiguidade para designer e distribuidores.

---

## P0-2 · L1-06-repositorio-acompanhante.md · Achado 01
**Status:** [REQUER DECISÃO DO AUTOR]
**Problema:** O repositório `github.com/falercia/inteligencia-aumentada-recursos` pode não existir ou estar vazio na data de publicação. O livro faz promessas substantivas sobre sete pastas de artefatos executáveis que dependem do repositório estar funcional.
**Ação editorial aplicada:** Adicionado bloco de alerta operacional no topo do arquivo com lista de verificação obrigatória pré-publicação e instrução explícita "NÃO PUBLICAR" sem essa verificação.
**Recomendação ao autor:** Criar o repositório no GitHub com as sete pastas (`/prompts`, `/governance`, `/evals`, `/datasets`, `/agents`, `/mcp`, `/notebooks`), README funcional em cada uma, e ao menos um artefato executável por pasta antes de enviar o livro para publicação. A banca classifica este risco como o de maior impacto em credibilidade de toda a obra.

---

## P0-3 · L1-12-quarta-capa.md · Achado 01
**Status:** [EDITADO]
**Problema:** Campos de produção abertos ("a definir após diagramação", "a ser atribuído", "a ser definido pela editora") no rodapé de arquivo canônico de quarta capa — risco de ir para impressão sem preenchimento.
**Antes:** Campos com texto genérico entre colchetes que não alerta o operador de produção sobre o risco.
**Depois:** Campos marcados com `[PENDENTE — ... — NÃO ENVIAR AO GRÁFICO]` em cada um dos três campos incompletos (Páginas, ISBN, Preço sugerido), tornando o estado de incompletude visível e o risco operacional explícito para qualquer pessoa que manuseie o arquivo.
