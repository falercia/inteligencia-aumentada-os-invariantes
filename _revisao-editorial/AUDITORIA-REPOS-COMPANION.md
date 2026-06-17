# Auditoria dos repositórios companion

**Data:** 2026-06-17 · Estado ao vivo (não snapshot). Repos: `inteligencia-aumentada-recursos` e `deep-claude`, ambos `falercia`, públicos.

---

## Veredito

**Os dois repos estão sólidos e coerentes com o livro.** Estrutura organizada, READMEs fortes, design da "Camada Dupla" (número fora do livro) bem executado, ambos **sincronizados com o `origin`** (nada por commitar/empurrar). Dois reparos reais antes de apontar leitores publicamente.

---

## O que está certo (não mexer)

| Item | Estado |
|---|---|
| **Estrutura `recursos`** | Completa: `prompts/` (≈30, por domínio), `evals/`, `agents/`, `mcp/`, `governance/v1/`, `datasets/`, `notebooks/`, `ferramentas/`, `fontes/`, `repos-curados/`, `apendice-vivo/`. |
| **Estrutura `deep-claude`** | `apendice-vivo/` (populado), `governance/`, `labs/`, `lancamento/`, `mcps/`, `prompts/`, `skills/`. |
| **Apêndice Vivo (fonte única)** | **Desenho correto e intencional.** Os números vivem só em `deep-claude/apendice-vivo` (MODELOS, PRECOS, BENCHMARKS, JANELAS-SLA, FONTES, CHANGELOG). `recursos/apendice-vivo` é um **ponteiro deliberado** para lá — Camada Dupla aplicada, um só lugar para o dado mudar. |
| **Sincronização git** | `recursos` e `deep-claude` em `main`, em dia com `origin`. Último commit: migração Onda 2 (16/jun). |
| **Coerência de referências de prompt** | Os IDs que o livro cita (P-LEG-01, P-FIN-02, etc.) resolvem para pastas reais. |

---

## Reparos necessários

### 🟡 Reparo 1 — Deriva de marca no `recursos` (26 ocorrências)
O repositório `recursos` ainda chama o sistema dos nove de **"Princípio N"** ("Princípio Sete — Termômetro", "Princípio 8", "Princípio Três" no README do apêndice-vivo). Depois do rebrand do livro para **Invariantes**, o companion ficou **inconsistente com a obra**. (O `deep-claude` está limpo: 0 ocorrências.)
**Correção:** migrar as 26 referências do sistema "Princípio N" → "Invariante N" no `recursos`, preservando usos genéricos ("princípios condutores"). Mesmo método aplicado no livro. Baixo risco.

### 🟠 Reparo 2 — Referência órfã: `auditoria-quantitativa-l1.md`
O livro (Apêndice N) afirma: *"A lista completa desses casos está no arquivo `auditoria-quantitativa-l1.md` do repositório."* **Esse arquivo não existe em nenhum dos dois repos.** É uma promessa verificável que falha — o tipo de link quebrado que mina a confiança do leitor técnico.
**Duas saídas:**
- (A) **Criar** o `auditoria-quantitativa-l1.md` no `recursos` (exige a tabela real de números Tipo A do livro — trabalho de dados).
- (B) **Suavizar** a frase do APX-N para não prometer um arquivo específico inexistente (rápido, honesto).
*Recomendação: (B) agora para não bloquear, com (A) como item de backlog se você quiser o artefato.*

---

## Auditoria de execução (2026-06-17)

Rodei o harness em modo offline (deps `pyyaml`/`anthropic` instalam limpo; sem chamar API). Achados:

### 🔴 EXEC-1 — Pipeline de evals quebrado por deriva de esquema (alto)
O **gerador** `extract-prompts.py` escreve o golden set como **`golden-set.yaml`** (com hífen), nas 30 pastas de prompt de nome longo (`P-LEG-01-clausula-nao-concorrencia-clt/`). Mas os **consumidores** `compile_golden_sets.py` (linha 78) e `eval_runner.py` (linha 302) leem **`golden.yaml`** (sem hífen), por ID curto (`P-LEG-01`). Resultado: **`compile_golden_sets.py` falha para os 30 prompts** — o "motor de regressão executável", carro-chefe do repo, não roda como está. Há ainda **3 pastas-stub** (`P-LEG-01`, `P-MED-01`, `P-SUP-01`) com o esquema antigo (`golden.yaml` + `eval.config.yaml`), duplicando as completas.
**Correção:** reconciliar o esquema — alinhar o nome do arquivo (gerador é a fonte: `golden-set.yaml`) e o ID de pasta (curto vs longo) entre gerador e runner, e remover as 3 stubs. É decisão de design (qual nomenclatura é canônica).

### 🟡 EXEC-2 — Caminho local fixo no `extract-prompts.py` (médio)
O script aponta para o APX-L num caminho absoluto da máquina do autor (`/Users/fabiogarcia/.../L1-APX-L-...md`). Roda só no computador do Fabio; falha em qualquer clone (e o livro é privado). Aceitável como ferramenta de autor, mas frágil.
**Correção:** ler o caminho de variável de ambiente ou argumento, com o atual como default.

### ✅ O que roda
Dependências instalam limpo; os 30 prompts têm conteúdo rico e versionado (`prompt.xml`, `golden-set.yaml`, `README`, `anti-padroes`, `changelog`); a lógica dos scripts é sólida. O bloqueio é a fiação (nomes/IDs), não o conteúdo.

> Não rodei o modo *live* (precisa de `ANTHROPIC_API_KEY` — não usei sua cota). A validação live dos golden sets contra a API fica para quando você quiser, na sua máquina.

---

## Reparos aplicados (commits locais — falta `git push` da sua máquina)

| Repo | Commit | O quê |
|---|---|---|
| livro | `b9e17d3` | APX-N: remove referência ao arquivo inexistente (reparo 2); relatórios de posicionamento e auditoria |
| recursos | `31be39e` | Reparo 1: terminologia Princípios→Invariantes (27 trocas) |
| recursos | `4bcb475` | EXEC-1/EXEC-2: harness de evals alinhado ao gerador |

**O que o fix do harness destravou:** `compile_golden_sets.py` e `eval_runner.py` agora leem `golden-set.yaml`, resolvem ID curto→pasta longa e localizam `prompt.xml`/golden em pastas irmãs. O **dry-run roda fim-a-fim** nos 3 exemplares executáveis (`P-LEG-01`, `P-MED-01`, `P-SUP-01` — 20 casos cada). O compile passou a **distinguir honestamente** golden set executável de descritivo.

### ⚠️ Backlog do AUTOR (não automatizável — é calibração/PI sua)
1. **27 dos 30 golden sets são DESCRITIVOS** (`casos:` em prosa), não executáveis (`cases:` com `input`/`expected`). Só 3 estão no formato que o motor roda. Para o repo cumprir a promessa de "motor de regressão executável" em todos, é preciso **calibrar as asserções dos outros 27** — trabalho de domínio, não de wiring. Não fabriquei essas asserções de propósito (seriam números sem lastro).
2. **Consolidar a estrutura:** hoje, num prompt executável, o `prompt.xml` está na pasta longa e o golden executável na pasta curta (stub). Unificar um prompt = uma pasta com `prompt.xml` + `golden-set.yaml` executável + `eval.config.yaml`.
3. **Limpeza:** após (1)/(2), os 3 stubs curtos deixam de ser necessários; `datasets/*.jsonl` já estão no `.gitignore` como artefato.
