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

## Ressalva
Auditoria de conteúdo e estrutura, não de execução: não rodei os scripts (`extract-prompts.py`, evals, agents) nem validei os golden sets. Se quiser garantia de que os exemplos rodáveis de fato rodam, é uma segunda passada (montar ambiente e executar a suíte).
