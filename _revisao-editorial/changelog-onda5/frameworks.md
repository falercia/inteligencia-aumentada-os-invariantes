# Changelog Onda 5 — Frameworks (F1–F9)
## Galé: leitura linear corrida, 9 frameworks em sequência

**Data:** 2026-06-16
**Escopo:** `/03-frameworks/` — L1-F1 a L1-F9

---

## MINI-TABELA DE AUDITORIA DE TEMPLATE

| Framework | Subtítulo | OBJETIVO | FUNCIONAMENTO | OUTPUT | EXEMPLO DE USO | ANTI-PADRÕES | CONEXÕES | Seções extras | Status template |
|-----------|-----------|----------|---------------|--------|----------------|--------------|----------|---------------|-----------------|
| F1 | ✓ | ✓ (1) | ✓ (2) | ✓ (3) | ✓ (4) | ✓ (5) | ✓ (6) | — | PADRÃO |
| F2 | ✓ | ✓ (1) | ✓ (2) | ✓ (3) | ✓ (4) plural¹ | ✓ (5) | ✓ (6) | — | PADRÃO (¹) |
| F3 | ✓ | ✓ (1) | ✓ (2) | ✓ (3) | ✓ (4) | ✓ (5) | ✓ (6) | — | PADRÃO |
| F4 | ✓ | ✓ (1) | ✓ (2) | ✓ (3) | ✓ (4) | ✓ (5) | ✓ (6) | — | PADRÃO |
| F5 | ✓ (itálico²) | ✓ (1) | ausente³ | ausente³ | ✓ (9) | ✓ (8) | ✓ (10) | ESCOPO, NOTA EDITORIAL, 3 seções de mecânica, APLICAÇÃO 30 MIN (11 seções total) | QUEBRA TOTAL |
| F6 | ✓ | ✓ (1) | ✓ (2) | ✓ (3) | ✓ (4) | ✓ (5) | ✓ (6) | — | PADRÃO |
| F7 | ✓ | ✓ (1) | ✓ (2) | ✓ (3) | ✓ (4) | ✓ (5) | ✓ (6) | — | PADRÃO |
| F8 | ✓ | ✓ (1) | ✓ (2) | ✓ (3) | ✓ (4) | ✓ (5) | ✓ (6) | — | PADRÃO |
| F9 | ✓ | ✓ (1) | ✓ (2) | ✓ (3) | ✓ (4) | ✓ (5) | ✓ (6) | POSICIONAMENTO (antes do 1)⁴ | QUASE PADRÃO (⁴) |

**Notas:**
1. F2 usa "EXEMPLOS DE USO" (plural) porque tem 3 exemplos (A, B, C). Os demais usam singular. Justificado pelo conteúdo, mas é variação de nomenclatura.
2. F5 subtítulo em itálico com asteriscos (`## *texto*`) — todos os outros são texto simples (`## texto`).
3. F5 não tem seção "2. FUNCIONAMENTO" nem "3. OUTPUT" com os rótulos canônicos. O FUNCIONAMENTO está distribuído nas seções 3–7 e o OUTPUT está ausente como seção nomeada.
4. F9 tem `## POSICIONAMENTO RELATIVO AO C00P` não numerada antes do `## 1. OBJETIVO`.

---

## EDITADOS

### E1 — F2, linha 85: nomenclatura de Princípio inconsistente

**Arquivo:** `L1-F2-encaixe-5.md`

**Problema:** Anti-padrão "Usar tier premium para tudo" usava "Viola o Princípio do Custo Composto" por extenso, enquanto todos os outros frameworks referenciam os Princípios por número (ex.: Princípio 7, Princípio 8, Princípio 2). O Manifesto (C00M) define claramente: Princípio 5 = Custo Composto.

**Antes:**
```
| Usar tier premium para tudo "porque é o melhor" | Viola o Princípio do Custo Composto; em meses, a fatura mostra o erro |
```

**Depois:**
```
| Usar tier premium para tudo "porque é o melhor" | Viola o Princípio 5 (Custo Composto); em meses, a fatura mostra o erro |
```

**Impacto:** Consistência de nomenclatura. Zero risco de voz.

---

### E2 — F6, linha 69: referência interna quebrada no OUTPUT

**Arquivo:** `L1-F6-gov-indelegavel.md`

**Problema:** O campo OUTPUT dizia "8 papéis × 12 decisões mínimas (ver tabela abaixo)" mas a tabela das 12 decisões está na seção 2 FUNCIONAMENTO — ou seja, ACIMA do OUTPUT, não abaixo. O leitor que seguia a instrução não encontrava nada.

**Antes:**
```
| RACI assinado | 8 papéis × 12 decisões mínimas (ver tabela abaixo) |
```

**Depois:**
```
| RACI assinado | 8 papéis × 12 decisões mínimas (ver tabela na seção 2 — Funcionamento) |
```

**Impacto:** Referência funcional. Zero risco de voz.

---

### E3 — F6, linha 101: inconsistência interna de cadência do AI Council

**Arquivo:** `L1-F6-gov-indelegavel.md`

**Problema:** O controle 10 (seção 2, tabela de controles) define explicitamente: "**Cadência mínima:** mensal nos primeiros **12 meses**". O mesmo documento, na seção 4 EXEMPLO (seguradora), dizia "cadência mensal nos primeiros **6 meses**". Contradição interna no mesmo framework.

**Antes:**
```
- Controle 10 (AI Council): mandato escrito, cadência mensal nos primeiros 6 meses
```

**Depois:**
```
- Controle 10 (AI Council): mandato escrito, cadência mensal nos primeiros 12 meses
```

**Impacto:** Elimina contradição interna. O exemplo agora segue a regra canônica da seção 2.

---

### E4 — F6, seção 6 CONEXÕES: assimetria com F8

**Arquivo:** `L1-F6-gov-indelegavel.md`

**Problema:** F8 (Pirâmide da Avaliação) cita explicitamente F6 em suas CONEXÕES ("Cap 24 — Governança: eval em CI é controle técnico canônico"). O controle 6 de F6 é exatamente "Evals em CI com critério de bloqueio explícito" — que é o coração de F8. A ausência de F8 nas CONEXÕES de F6 criava assimetria unidirecional na rede.

**Adicionado:**
```
- 🔗 Pirâmide da Avaliação (controle 6 — evals em CI — é a implementação técnica do F8)
```

**Impacto:** Fecha a reciprocidade F6 ↔ F8. Zero risco de voz.

---

## PENDENTE-AUTOR

### P1 — F5: quebra total de template (DECISÃO ESTRUTURAL URGENTE)

**Arquivo:** `L1-F5-cobertura-integracoes.md`

**Problema:** F5 é o único framework que rompe completamente o template de 6 seções. Tem 11 seções numeradas, não tem seção "2. FUNCIONAMENTO" nem "3. OUTPUT" com rótulos canônicos, tem seção "ESCOPO DESTE FRAMEWORK" não numerada antes do 1. OBJETIVO, e tem epígrafe de abertura (linha 5) antes do primeiro conteúdo — padrão ausente em todos os outros 8 frameworks.

**Auditoria das seções de F5:**
- ESCOPO DESTE FRAMEWORK (extra, não numerada)
- 1. OBJETIVO ✓
- 2. NOTA EDITORIAL DE NEUTRALIDADE (substitui FUNCIONAMENTO)
- 3. OS SEIS MECANISMOS DE INTEGRAÇÃO (conteúdo de FUNCIONAMENTO)
- 4. AS CINCO DIMENSÕES DA MATRIZ DE COBERTURA (conteúdo de FUNCIONAMENTO)
- 5. MATRIZ DE DECISÃO POR CAPABILITY (conteúdo de FUNCIONAMENTO + OUTPUT)
- 6. QUANDO CADA MECANISMO É A ESCOLHA ERRADA (sem equivalente)
- 7. QUANDO MIGRAR DE MECANISMO EXISTENTE (sem equivalente)
- 8. ANTI-PADRÕES DE ADOÇÃO ✓ (mas numerado 8, não 5)
- 9. EXEMPLO MEMORÁVEL (✓ mas numerado 9, não 4)
- 10. CONEXÕES COM OUTROS CAPÍTULOS ✓ (mas numerado 10, não 6)
- 11. APLICAÇÃO PRÁTICA EM 30 MINUTOS (sem equivalente em outros frameworks)

**Impacto na leitura corrida:** O leitor que lê os 9 frameworks em sequência percebe F5 como documento diferente. Em leitura contínua, a quebra é abrupta. F5 é 169 linhas com 11 seções; os demais têm 89–134 linhas com 6 seções. É o framework mais longo e mais denso do bloco.

**Recomendação do editor:** A riqueza de conteúdo de F5 é legítima — integração é o assunto mais complexo do bloco. Três opções:
1. **Manter como está com nota editorial** ("F5 usa formato expandido por complexidade do tema") — solução de menor custo.
2. **Compactar para o template de 6 seções**, consolidando as seções 3–7 em FUNCIONAMENTO, a seção 5 em OUTPUT, e movendo as seções 6–7 e 11 para o interior das seções correspondentes.
3. **Extrair F5 para documento standalone** e criar um F5 compacto com o template padrão que remete ao documento expandido.

A recomendação do editor é a opção 2 (compactar): a NOTA EDITORIAL vira parágrafo de abertura do FUNCIONAMENTO; AS SEIS MECANISMOS + CINCO DIMENSÕES + MATRIZ ficam em FUNCIONAMENTO; QUANDO MIGRAR vai dentro de FUNCIONAMENTO; a seção OUTPUT consolida as decisões; EXEMPLO + ANTI-PADRÕES + CONEXÕES + APLICAÇÃO ficam em seções 4, 5, 6 expandidas. A epígrafe de abertura vai para o final no padrão canônico.

**Decisão pertence ao autor.**

---

### P2 — F9: seção POSICIONAMENTO antes do 1. OBJETIVO (avaliação de posição)

**Arquivo:** `L1-F9-rota-dupla.md`

**Problema:** F9 tem `## POSICIONAMENTO RELATIVO AO C00P` não numerada antes do `## 1. OBJETIVO`. Nenhum outro framework tem seção extra antes do 1.

**Avaliação editorial:** A seção é curta (8 linhas), bem escrita, e cumpre função real: situa F9 em relação ao C00P para que o leitor saiba que os dois se complementam sem repetir. Em leitura corrida dos 9 frameworks, essa seção não cria atrito — é uma âncora de orientação. Porém é variação de formato.

**Opções:**
1. **Manter**: seção de posicionamento tem valor editorial claro e F9 é o framework de meta-método (o framework dos frameworks) — alguma diferença estrutural pode ser defendida.
2. **Incorporar como bloco inicial do OBJETIVO**: o conteúdo de POSICIONAMENTO pode se tornar o primeiro parágrafo da seção 1 OBJETIVO, preservando o texto e restabelecendo o padrão de 6 seções.

**Recomendação:** opção 2 (incorporar), pois elimina a variação sem perder nada. Mas é decisão do autor.

---

### P3 — F3: matriz visual 4×4 ausente (REQUER ASSET)

**Arquivo:** `L1-F3-agente-prop.md`

**Status:** A seção 2 FUNCIONAMENTO descreve "Matriz 4×4 cruzando observabilidade × reversibilidade" textualmente, com os dois eixos e seus 4 níveis cada, mas não há visualização da matriz em formato tabular ou gráfico — nem placeholder marcado como `[REQUER ASSET]`.

**Achado:** O texto descreve os eixos e os 4 níveis canônicos mas nunca apresenta a matriz cruzada em si (os 16 quadrantes com o nível de autonomia resultante). A tabela existente (linhas 31–36) apresenta os 4 níveis canônicos, mas não a matriz de cruzamento. O leitor precisa inferir o cruzamento.

**Recomendação:** Inserir tabela 4×4 completa (observabilidade 1–4 × reversibilidade 1–4 = 16 células com o nível de autonomia em cada quadrante) OU confirmar que a tabela atual (resumo dos 4 níveis) é suficiente como substituto e que a matriz expandida vai apenas na versão diagramada. Confirmar com o autor se a representação visual expandida já está encomendada ou se o texto atual é o definitivo.

---

### P4 — F5: reposicionar a seção "Quando migrar" (seção 7) — avaliação de posição

**Arquivo:** `L1-F5-cobertura-integracoes.md`

**Status:** A seção 7 "QUANDO MIGRAR DE MECANISMO EXISTENTE" fica entre "QUANDO CADA MECANISMO É A ESCOLHA ERRADA" (6) e "ANTI-PADRÕES DE ADOÇÃO" (8). Em termos de fluxo de decisão, "Quando migrar" segue naturalmente do diagnóstico de escolha — o leitor que chegou na seção 6 entendendo quando não usar determinado mecanismo está pronto para decidir se deve migrar. A posição atual lê bem.

**Recomendação:** Manter a posição atual. Se o framework for reestruturado para o template de 6 seções (ver P1), "Quando migrar" pode integrar o FUNCIONAMENTO ou virar um bloco do EXEMPLO expandido.

---

### P5 — F2: "EXEMPLOS DE USO" (plural) vs padrão "EXEMPLO DE USO" (singular)

**Arquivo:** `L1-F2-encaixe-5.md`

**Problema menor:** F2 tem `## 4. EXEMPLOS DE USO` (plural) enquanto todos os outros 8 frameworks usam `## 4. EXEMPLO DE USO` (singular). F2 tem 3 exemplos (A, B, C), o que justifica o plural.

**Recomendação:** Padronizar para `## 4. EXEMPLOS DE USO` em todos os frameworks que têm mais de um exemplo (verificar F1 e F4 que podem ter estrutura interna com subcasos). Alternativamente, manter o singular em todos e usar subtítulos internos para os subcasos. É decisão menor de estilo editorial.

---

## JÁ RESOLVIDO

- Escopo de observabilidade: as notas de "Escopo de observabilidade neste framework" em F3, F5, F6, F7 são intencionais e corretas — demarcam fronteiras entre os frameworks sem contradição. NÃO são repetição indevida.
- Nomenclatura dos 4 níveis de autonomia: consistente entre F1 (referência rápida) e F3 (tabela canônica) — Assistente, Co-piloto, Agente supervisionado, Agente autônomo regulado. Capitalização idêntica nos dois pontos.
- Referências F1 ↔ F3: F1 cita F3 para definição de autonomia; F3 cita F1 para origem do risco. Recíprocas e corretas.
- Referências F3 ↔ F8: F3 cita F8 para eval de promoção; F8 cita F3 para cobertura proporcional. Recíprocas e corretas.
- Referências F7 ↔ F8: F7 cita F8 para eval de T1; F8 cita F7 via LLMOps. Corretas.
- Referências F7 ↔ F2: F7 cita F2 para decisão de tier; F9 cita F2 para encaixe. Corretas.
- Referências F4 → F7: F4 cita T3 do F7 para compressão de contexto. F7 não precisa referenciar F4 de volta — a remissão é direcional (F4 usa F7 como ferramenta, não o contrário). Aceitável.
- Epígrafe de fecho: todos os 9 frameworks terminam com `---` seguido de epígrafe em itálico. Padrão consistente.
- Voz e registro: os 9 frameworks soam como o mesmo autor. Registro é consistentemente técnico-executivo, direto, sem ornamento. F5 tem voz ligeiramente mais didática pelo volume de conteúdo, mas não destoa.
- Referência "Cap 24 — Claude Code (L2)" em F3 CONEXÕES: ligeiramente incomum (Cap 24 é Governança em outros frameworks), mas é referência de seção L2 que não compete com a referência de L1.

---

## RESUMO

| Categoria | Quantidade |
|-----------|------------|
| Edições diretas aplicadas (E1–E4) | **4** |
| Pendentes-autor (P1–P5) | **5** |
| Já resolvidos / aceitáveis | **11** |

**Frameworks editados:** F2, F6
**Frameworks sem edição:** F1, F3, F4, F5, F7, F8, F9

**Achados principais:**
- F5 quebra totalmente o template (11 seções vs 6) — único problema estrutural sistêmico do bloco
- F6 tinha 3 problemas corrigíveis: referência interna quebrada, inconsistência de cadência (12 vs 6 meses), assimetria de conexão com F8
- F2 usava Princípio por extenso enquanto todos os outros usam número
- Rede de referências cruzadas está em 85% consistente; F4→F7 e F6→F8 tinham assimetrias (F6↔F8 corrigida; F4→F7 é unidirecional aceitável)
- Nomenclatura dos 4 níveis de autonomia: perfeita em todos os pontos de ocorrência
- Voz e registro: coesos nos 9 frameworks — sistema lê como obra única
