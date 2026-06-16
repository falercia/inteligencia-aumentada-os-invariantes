# CHANGELOG — Resolução das 21 pendências + migração terminológica

**Data:** 2026-06-16
**Mandato:** o autor delegou autoridade plena ("faça o melhor caminho; pode seguir sem me pedir nada"). Tudo abaixo foi executado e documentado para revisão/reversão. **Backup:** `_backup-pre-pendencias/` (73 arquivos).
**Método:** pesquisa de verificação na web → 5 subagentes editoriais por cluster → 1 decisão de marca do autor (título) → 5 subagentes de migração terminológica → 1 subagente de diagramas → verificação single-thread.

---

## 1. AS 21 PENDÊNCIAS (status)

### A. Alto impacto
- **D1 — Epílogo de fechamento** ✅ Escrito ("Epílogo — O que fica", ~370 palavras) e movido para a **última posição do livro** (depois da autoavaliação e da epígrafe de C28). Última linha do livro agora é **"Modelos passam. Método fica."**. Fecha o arco PME→CTO sob o método.
- **D2 — Nome canônico** ✅ **Decisão do autor: tudo "Invariantes".** Ver §2 (migração).
- **D3 — Contagem de capítulos** ✅ "ao longo dos 29 capítulos" → "ao longo dos capítulos" (número frágil removido).
- **D4 — Notas internas na quarta-capa** ✅ 3 notas `[NÃO ENVIAR AO GRÁFICO]` (Páginas/ISBN/Preço) convertidas para comentário HTML.
- **D5 — Ordem dos princípios no prefácio** ✅ Inserida nota: "a ordem aqui é a da história, não a da numeração; os nove estão numerados no manifesto". Sem reordenar.

### B. Estruturais
- **D6 — Ordem 14B↔14C** ✅ Resolvido por **pontes de transição** (não por reordenação física — decisão de trade-off: evitar fragilizar dezenas de referências cruzadas num livro-referência). Ponte 14B→14C e 14C→15 adicionadas.
- **D7 — F5 fora do template** ✅ Compactado de **11→6 seções** (169→138 linhas); toda a PI (tabelas, critérios, caso da telecom, anti-padrões) preservada. Resolve também o "reposicionar Quando Migrar".
- **D8 — F9 seção solta** ✅ "Posicionamento relativo ao C00P" incorporado ao OBJETIVO.
- **D9 — "Curiosidade ativa" → "Curiosidade"** ✅ Unificado (C14B, C14C, C00P).
- **D10 — Reordenação do bloco final** ✅ Resolvido via epílogo (D1), sem reordenar.

### C. Voz do autor
- **D11 — Epígrafe Dijkstra** ✅ A frase atribuída era inventada ("adaptado de"). Substituída pela **citação real e verificável**: *"A questão de saber se uma máquina pode pensar é tão relevante quanto a questão de saber se um submarino pode nadar."* — Dijkstra, EWD898, 1984.
- **D12 — "Quando NÃO usar embeddings" (C05)** ✅ Adicionada perspectiva proprietária: busca léxica (BM25/exata) vence em vocabulário controlado, precisão > recall, auditabilidade exigida; critério durável "embedding é semântica, não exatidão".
- **D13 — Persona Dev (entregável)** ✅ "repositório de prompts" → "repositório de casos de uso com framework de eval documentado" (APX-C). Reancora em método.
- **D14 — Exemplo jurídico repetido** ✅ C04 trocado de escritório de advocacia para **due diligence de M&A**; o caso real Mata v. Avianca (C02) preservado.

### D. Arte/SVG
- **D15 — Matriz 4×4 do F3** ✅ SVG criado (`L1-F3-img-01-matriz-4x4.svg`).
- **D16 — Diagramas 24.2 / 24.3** ✅ SVGs criados (camadas de controle; fluxo de incidente SEV-1..4).
- **D17 — Diagramas 25.2 / 25.3** ✅ SVGs criados (árvore de decisão dos 6 trade-offs; triângulo Latência×Qualidade×Custo).
> 5 SVGs em estilo da casa (navy/laranja/creme, Inter), XML validado (xmllint). Production-ready; o designer pode refinar o tratamento visual. Placeholders `[REQUER ASSET]` removidos.

### E. Verificação pré-gráfica (fatos checados na web)
- **D18 — DeepSeek-R1** ✅ Agora citável: publicado na **Nature, vol. 645, pp. 633–638 (2025)** (DOI s41586-025-09422-z) + arXiv:2501.12948. Ancorado em C16 e APX-J; nota "peer-review não confirmada" da APX-J atualizada.
- **D19 — PL 2338/2023** ✅ Status preciso: aprovado no Senado (dez/2024), em análise na Câmara, votação prevista 2026 — ainda não é lei. Atualizado em C19 e C24.
- **D20 — ANPD** ✅ Ancorado em docs vigentes: Radar Tecnológico IA Generativa (2024), Agenda Regulatória 2025-2026, Mapa de Temas Prioritários 2026-2027 (Res. 30/2025, 31/2025).
- **D21 — arXiv Hayes et al.** ✅ **Erro da galé corrigido**: o correto é **2410.22884** (não 2410.10074). Confirmado em APX-J e APX-P; corrigido onde aparecia.

---

## 2. MIGRAÇÃO TERMINOLÓGICA — "Princípios" → "Invariantes"

**Decisão do autor (D2):** o sistema dos nove deixa de se chamar "Princípios"/"Princípios Permanentes" e passa a **"Invariantes"** em toda a obra — incluindo o **subtítulo comercial** ("Os Princípios Permanentes da IA" → **"Os Invariantes da IA"**: capa, ISBN/copyright, lombada, ficha, sumário, sobre-o-autor, quarta-capa).

**Execução:** 5 subagentes, um por pasta, com regra trocar/preservar e nota gramatical (ambos masculinos → artigos intactos).

| Pasta | Trocados (sistema) | Preservados (genérico) |
|---|---|---|
| 00-paratexto | ~30 | "em/por princípio", máximas |
| 01-manifesto | ~46 | 4 idiomáticos. **C00M agora define "Invariante 1…9"** |
| 02-capitulos | ~36 | ~37: mínimo privilégio (C19), Constitutional AI (C23), teorema CAP (C25), context engineering (C04) |
| 03-frameworks | 9 | 1 ("AUP + princípios") |
| 04-apendices | ~130 | ~27: "princípios condutores" (APX-O), OECD AI Principles, etc. |

**Total:** ~250 referências migradas; ~75 usos genéricos preservados. ASCII art do APX-B realinhada. Cabeçalhos markdown renomeados (verificado: nenhum link de âncora `(#...)` quebrado).

**Verificação final:** 0 ocorrências de "Princípios Permanentes" / "Nove Princípios" / "Princípio N" no source; 0 "Invariantes Permanentes" (sem falsos positivos); concordância intacta.

---

## 3. ACHADO BÔNUS (galé tardia)
- **C28** tinha erro de gênero preexistente "A Princípio 8" → corrigido para "O Invariante 8".

---

## 4. CHANGELOGS DETALHADOS (pasta `changelog-onda5/`)
`pendencias-D1-D13`, `pendencias-D2-D9`, `pendencias-D11-D14`, `pendencias-D7-D8`, `pendencias-D18-D21`, `migracao-{paratexto,manifesto,capitulos,frameworks,apendices}`, `diagramas-svg`.

---

## 5. O QUE AINDA DEPENDE DE TERCEIRO
- **Verificação na data de fechamento** (fatos datados já marcados com ressalva): status final do PL 2338, versão corrente das Notas Técnicas da ANPD — confirmar em fonte oficial antes da gráfica.
- **Refino visual dos 5 SVGs** pelo designer, se desejado (conteúdo e rótulos já corretos).
- **ISBN / Ficha CIP** (campos `[PENDENTE]` na capa) — dependem de terceiros (autor/bibliotecário).

**O manuscrito está pronto para diagramação.** Não resta correção de conteúdo pendente sob controle do editor.
