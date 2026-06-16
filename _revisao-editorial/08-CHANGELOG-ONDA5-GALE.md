# CHANGELOG — ONDA 5 (GALÉ / leitura linear)

**Data:** 2026-06-16
**Método:** 7 subagentes de galé (model sonnet) lendo o livro inteiro em ordem de leitura, por cluster contínuo, com lente de **ritmo, transições, repetições cruzadas, voz, setup/callback e consistência de termos** — o que achados isolados (Ondas 1–4) não capturam.
**Modo:** híbrido. Edição direta do objetivo e de baixo risco; sinalização (`PENDENTE-AUTOR`) do que é sensível à voz, estrutural ou exige decisão. Varredura paralela dos ~16 itens deferidos.
**Backup:** `_backup-pre-onda5/` (73 arquivos).
**Resultado:** **45 edições diretas em 28 arquivos** · **0 sequências quebradas** (renumerações C13/C18 auditadas) · changelogs por cluster em `changelog-onda5/`.

> Os 378 achados das Ondas 1–4 NÃO foram reabertos. Esta onda só registra o que a leitura corrida revelou.

---

## 1. EDIÇÕES DIRETAS APLICADAS (45)

### Paratexto + Manifesto (8) — `changelog-onda5/paratexto-manifesto.md`
- **L1-06-repositorio-acompanhante.md** — nota de produção `> [PENDENTE — VERIFICAÇÃO...]` visível convertida para comentário HTML `<!-- -->` (não vaza ao leitor/gráfica).
- **L1-06-repositorio-acompanhante.md** — dois parágrafos consecutivos iniciando "A política editorial é simples" com conteúdo quase idêntico → fundidos.
- **L1-00c2-promessa.md** + **L1-00e-sobre-os-casos.md** — número do composto pedagógico oscilava entre "Trinta" / "mais de trinta" / "mais de 30" → harmonizado para **"mais de trinta"** (alinhado ao pacto editorial autoritativo).
- **L1-C00P-porque-padrao-dura.md** — duplo separador `---` após a epígrafe de abertura → removido.
- **L1-03-introducao.md** + **L1-12-quarta-capa.md** — capitalização inconsistente de "Nove Princípios Permanentes" → corrigida.
- **L1-04-sumario.md** — "Por Que" no título do C00P harmonizado com a grafia do arquivo real.

### C01–C07 (4) — `changelog-onda5/C01-C07.md`
- **L1-C05-embeddings.md** (5.3.2) — frase idêntica duplicada no mesmo parágrafo ("Palavras que aparecem em contextos parecidos...") → 2ª ocorrência removida.
- **L1-C04-janela-de-contexto.md** — epígrafe de abertura duplicava a frase de fechamento → abertura limpa, fechamento preservado.
- **L1-C01-o-que-e-ia.md** (1.6 e 1.8) — referência cruzada errada "Capítulos 20 e 23" → **"Capítulos 19 e 23"** (C19 = segurança; C20 = futuro); rótulo "horizonte da AGI" → "alinhamento".

### C08–C14C (15) — `changelog-onda5/C08-C14C.md`
- **L1-C13-mcp.md** — **bug estrutural**: duas seções `13.3` (e `13.3.1/.2` duplicadas). Renumeração em cascata 13.4→13.15 (12 seções). Sequência auditada: limpa.
- **L1-C14C-spec-driven-development.md** — marcador `🎉 Você fechou a Parte 3` estava em C14B (com C14C ainda por vir) → movido para o fim de C14C.
- **L1-C14C** — seta "5 de 5 → Capítulo 14B" (já lido) → corrigida para **Capítulo 15**.
- **L1-C14B-reasoning-models.md** — remoção do marcador de fechamento de parte deslocado; outros ajustes de cruzamento interno.
- (demais micro-ajustes de conectivo/referência no cluster — ver changelog.)

### C15–C21 (4) — `changelog-onda5/C15-C21.md`
- **L1-C21-evals.md** — autoavaliação com itens 1–4 fora do padrão (`Rótulo: texto` sem negrito/em-dash) → normalizado para `**Rótulo** — Texto`.
- **L1-C18-economia-tokens.md** — **único capítulo sem "Checklist do capítulo"** → adicionada seção 18.8 (6 itens); 18.8→18.12 renumeradas para 18.9→18.13. Sequência auditada: limpa.

### C22–C28 (2) — `changelog-onda5/C22-C28.md`
- **L1-C24-governanca.md** + **L1-C25-trade-offs.md** — typo de template `**Curiosidade **` (espaço espúrio) → `**Curiosidade**`.

### Frameworks F1–F9 (4) — `changelog-onda5/frameworks.md`
- **L1-F2-encaixe-5.md** — "Viola o Princípio do Custo Composto" → **"Viola o Princípio 5 (Custo Composto)"** (numeração canônica, como F1/F4/F7).
- **L1-F6-gov-indelegavel.md** — "ver tabela abaixo" apontava para tabela que está acima → "ver tabela na seção 2 — Funcionamento".
- **L1-F6** — cadência do AI Council inconsistente (controle 10 = 12 meses; exemplo da seguradora = 6 meses) → unificada em **12 meses**.
- **L1-F6** — CONEXÕES não listava F8 (sendo o controle 6 o domínio de F8) → link adicionado.

### Apêndices A–Q (8) — `changelog-onda5/apendices.md`
- **L1-APX-H-bibliografia.md** — cabeçalho referenciava APX-F extinto → ponteiro corrigido para APX-E/APX-G.
- **L1-APX-I-indice-remissivo.md** — título obsoleto de APX-E + 3× "Manifesto dos Princípios" (nome inexistente) → **"Manifesto de Bolso (APX-M)"**.
- **L1-APX-J-trilha-do-numero.md** — typo sintático "um calendário que prometido demais" → "que promete demais".
- **L1-APX-G-papers.md** — duplo separador `---` residual removido.
- **L1-APX-L-biblioteca-prompts.md** — moldura dizia "sete padrões" com 8 itens no corpo → corrigido (2 ocorrências).
- **L1-APX-P-boxes-tecnicos.md** — URL do paper Hayes et al. divergia de APX-J → alinhada à canônica (`2410.10074`). *(ver pendência VP de verificação manual abaixo.)*
- **L1-APX-Q-manual-do-professor.md** — gabarito da aula 4 apontava "APX-K (C06)" para exercício de C04 → corrigido para "Em construção — repositório".

---

## 2. AVALIAÇÃO DE FLUÊNCIA (o que a leitura corrida disse)

- **Transições mais fortes:** C07→C08 (gancho de curiosidade casa com a abertura) e C21→C22 (fluida).
- **Voz:** consistente no corpo e — confirmado — nos 9 frameworks, que leem como sistema coeso de um mesmo autor.
- **Pontos de atrito de ritmo (sinalizados, não cortados):** "Sobre os Casos" desacelera a entrada antes do Prefácio; bloco C23/C24/C25 replica a mesma fôrma estrutural três vezes (efeito de manual); transição C27→C28 é o maior salto de audiência do livro (dono de PME → CTO diante da ANPD) sem ligação.
- **Encerramento:** **a última frase do livro (C28) ancora em "instrumento", não em "método" — a tese "Modelos passam. Método fica." não aparece na última página.** Maior achado de fluência da onda (ver §3, decisão D1).

---

*Continua na folha de decisões: `09-PENDENTES-ONDA5-DECISAO-AUTOR.md`.*
