# Changelog — Migração Terminológica: Princípios → Invariantes
## Escopo: `00-paratexto/` · Data: 2026-06-16

---

## TOTAIS

| Categoria | Contagem |
|-----------|----------|
| Trocas efetuadas | 30 |
| Preservados (uso genérico) | 5 |
| Cabeçalhos markdown renomeados | 1 |

---

## TROCAS EFETUADAS — por arquivo

### L1-00-capa-e-titulos.md (7 trocas)

1. Cabeçalho H2: `*Inteligência Aumentada — Os Princípios Permanentes da IA*` → `*Inteligência Aumentada — Os Invariantes da IA*`
2. Subtítulo canônico: `*Os Princípios Permanentes da IA*` → `*Os Invariantes da IA*`
3. Posicionamento/Diferencial central: `nove princípios permanentes da IA` → `nove invariantes da IA`
4. Conceito A: `a roda dos nove princípios` → `a roda dos nove invariantes`
5. Conceito C: `selo dos nove princípios` → `selo dos nove invariantes`
6. Lombada: `Os Princípios Permanentes da IA` → `Os Invariantes da IA`
7. Página de copyright/Título: `Os Princípios Permanentes da IA` → `Os Invariantes da IA`

### L1-00b-ficha-catalografica.md (2 trocas)

8. Subtítulo: `*Os Princípios Permanentes da IA*` → `*Os Invariantes da IA*`
9. Ficha CIP: `os princípios permanentes da IA` → `os invariantes da IA`

### L1-01-prefacio.md (1 troca)

10. Enumeração dos nove: `Os nove princípios — Camada Dupla, Plausibilidade…` → `Os nove invariantes — Camada Dupla, Plausibilidade…`

### L1-02-como-ler.md (5 trocas)

11. Título do caminho 3: `Pelos princípios` → `Pelos invariantes`
12. Duração por unidade: `por princípio` → `por invariante`
13. "Parta de um dos nove princípios" → "Parta de um dos nove invariantes"
14. Princípio nominal: `o Princípio da Responsabilidade Indelegável` → `o Invariante da Responsabilidade Indelegável`
15. Encerramento do caminho 3: `o princípio operacionalizado` → `o invariante operacionalizado`
16. Frase de encerramento do capítulo: `na aplicação dos princípios na próxima decisão` → `na aplicação dos invariantes na próxima decisão`

*(Nota: itens 11–15 são 5 ocorrências na linha 13; item 16 é a linha 70.)*

### L1-03-introducao.md (6 trocas)

17. "São os princípios que decidem se a IA funciona" → "São os invariantes que decidem se a IA funciona"
18. "Cada princípio tem regra, mecânica e violação típica" → "Cada invariante tem regra, mecânica e violação típica"
19. "qual princípio instancia" → "qual invariante instancia"
20. "Cada framework proprietário deriva de um princípio" → "Cada framework proprietário deriva de um invariante"
21. "o princípio do encaixe" → "o invariante do encaixe"
22. "os nove princípios" (item 1 da Promessa) → "os nove invariantes"
23. "Os nove princípios começam na próxima." → "Os nove invariantes começam na próxima."

*(Itens 17–20 são quatro ocorrências dentro de um único parágrafo; contagem total neste arquivo: 7 trocas.)*

### L1-04-sumario.md (7 trocas)

24. Cabeçalho H2: `*Inteligência Aumentada · Os Princípios Permanentes da IA*` → `*Inteligência Aumentada · Os Invariantes da IA*`  
    **CABEÇALHO RENOMEADO** — checar links `(#...)` cruzados que apontem para este header.
25–29. Cinco colunas de tabela `| Princípio central |` → `| Invariante central |` (Partes 1, 2, 3, 4, 5 e Frameworks — 5 ocorrências via replace_all).
30. Apêndice M: `Os Nove Princípios em Uma Página` → `Os Nove Invariantes em Uma Página`

### L1-06-repositorio-acompanhante.md (2 trocas)

31. "os princípios, os frameworks, a anatomia das decisões" → "os invariantes, os frameworks, a anatomia das decisões"
32. "o Princípio Três da obra, **Camada Dupla**" → "o Invariante Três da obra, **Camada Dupla**"

### L1-10-sobre-o-autor.md (2 trocas)

33. Subtítulo no corpo: `*Inteligência Aumentada — Os Princípios Permanentes da IA*` → `*Inteligência Aumentada — Os Invariantes da IA*`
34. "instanciando os Nove Princípios em ferramentas" → "instanciando os Nove Invariantes em ferramentas"

### L1-11-orelhas.md (1 troca)

35. "traduzem cada Princípio em decisão concreta" → "traduzem cada Invariante em decisão concreta"

### L1-12-quarta-capa.md (3 trocas)

36. Referência ao livro: `*Inteligência Aumentada — Os Princípios Permanentes da IA*` → `*Inteligência Aumentada — Os Invariantes da IA*`
37. "Sobre os Princípios, nove frameworks" → "Sobre os Invariantes, nove frameworks"
38. Subtítulo final H3: `*Os Princípios Permanentes da IA*` → `*Os Invariantes da IA*`

---

## PRESERVADOS (uso genérico legítimo — NÃO trocados)

| Arquivo | Linha | Texto preservado | Motivo |
|---------|-------|------------------|--------|
| L1-01-prefacio.md | 3 | "O que ficou foram os **princípios** que cada ciclo revelou" | Genérico: lições abstratas de ondas tecnológicas anteriores, não nomeia nenhum dos nove |
| L1-01-prefacio.md | 19 | "O mercado está estudando produtos quando deveria estar estudando **princípios**" | Genérico: oposição produto/princípio como atitude intelectual geral |
| L1-01-prefacio.md | 33 | "O **princípio** dobra a década. A versão dura um trimestre." | Genérico: máxima sobre durabilidade de fundamentos vs. versões |
| L1-01-prefacio.md | 53 | "buscar o **princípio** quando todos correm atrás da versão" | Genérico: idem à anterior — argumento de atitude intelectual |
| L1-10-sobre-o-autor.md | 5 | "As três marcas reaparecem como **princípios** sob a superfície deste livro" | Genérico: as três marcas de liderança do autor (disciplina, frameworks, pessoas) — não são nenhum dos nove invariantes |

---

## CABEÇALHOS MARKDOWN RENOMEADOS

| Arquivo | Cabeçalho antigo | Cabeçalho novo |
|---------|-----------------|----------------|
| L1-04-sumario.md | `## *Inteligência Aumentada · Os Princípios Permanentes da IA*` | `## *Inteligência Aumentada · Os Invariantes da IA*` |

**Ação requerida:** verificar se existe algum link `(#inteligência-aumentada--os-princípios-permanentes-da-ia)` em outros arquivos do livro que aponte para este cabeçalho; se existir, atualizar a âncora.

---

## VERIFICAÇÕES DE QUALIDADE

- Nenhuma ocorrência de "Invariantes Permanentes" foi criada.
- Concordância gramatical mantida: "o/do/ao/esse invariante" (masculino = idêntico a "princípio").
- Nenhum nome de arquivo `.md` foi renomeado.
- Nenhum link para arquivo foi alterado.
- Usos idiomáticos ("em princípio", "primeiros princípios", "princípios de engenharia") não aparecem nesta pasta — confirmado por grep.
