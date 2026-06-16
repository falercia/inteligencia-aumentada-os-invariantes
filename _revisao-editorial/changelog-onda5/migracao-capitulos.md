# Migração terminológica — 02-capitulos/ — Onda 5

Data: 2026-06-16  
Escopo: `/02-capitulos/` — 30 arquivos  
Decisão do autor: "Princípios" (sistema dos nove) → "Invariantes"

---

## Resumo por arquivo

| Arquivo | Trocado | Preservado (genérico) |
|---------|--------:|----------------------:|
| L1-C01-o-que-e-ia.md | 0 | 1 ("em princípio" — idiom.) |
| L1-C02-como-modelos-funcionam.md | 1 | 0 |
| L1-C03-tokens.md | 0 | 0 |
| L1-C04-janela-de-contexto.md | 0 | 6 (Context Engineering) |
| L1-C05-embeddings.md | 0 | 0 |
| L1-C06-rag.md | 0 | 0 |
| L1-C07-memoria.md | 0 | 1 (técnico de memória) |
| L1-C08-fine-tuning.md | 0 | 0 |
| L1-C09-engenharia-prompt.md | 0 | 1 (técnico genérico) |
| L1-C10-chain-of-thought.md | 0 | 0 |
| L1-C11-context-engineering.md | 0 | 1 (Context Engineering) |
| L1-C12-agentes.md | 0 | 0 |
| L1-C13-mcp.md | 0 | 2 (padrão de integração) |
| L1-C14-ai-engineering.md | 0 | 4 (princípio operacional interno + LLMOps) |
| L1-C14B-reasoning-models.md | 2 | 1 (estrutural — DeepSeek) |
| L1-C14C-spec-driven-development.md | 4 | 0 |
| L1-C15-comparacao-modelos.md | 1 | 0 |
| L1-C16-open-source.md | 0 | 0 |
| L1-C17-github-repos.md | 0 | 0 |
| L1-C18-economia-tokens.md | 5 | 1 (por princípio de — idiom.) |
| L1-C19-seguranca.md | 4 | 3 (mínimo privilégio × 3) |
| L1-C20-futuro.md | 1 | 0 |
| L1-C21-evals.md | 3 | 0 |
| L1-C22-llmops.md | 2 | 0 |
| L1-C23-alignment.md | 2 | 11 (constituição / CAI / clínico) |
| L1-C24-governanca.md | 6 | 4 (regulatório / política org.) |
| L1-C25-trade-offs.md | 2 | 2 (engenharia CAP / triângulo) |
| L1-C26-roadmap-pessoal.md | 0 | 0 |
| L1-C27-ia-para-pme-brasileira.md | 0 | 0 |
| L1-C28-interpretabilidade-mecanicista.md | 3 | 0 |
| **TOTAL** | **36** | **37** |

---

## Cabeçalho renomeado

- **L1-C24-governanca.md, seção 24.3.1** (cabeçalho `##`):  
  `## RACI de IA: o coração do Princípio 8`  
  → `## RACI de IA: o coração do Invariante 8`

- **L1-C28-interpretabilidade-mecanicista.md, L114** (corpo):  
  `A Princípio 8 lembra` → `O Invariante 8 lembra`  
  *(corrige também erro gramatical de gênero preexistente: "A" → "O")*

---

## Genéricos notáveis preservados

### C19 — Segurança (3 preservações críticas)
- `princípio do mínimo privilégio` (L20, L102, L119 — tabela OWASP LLM Top 10)  
  Conceito de segurança de computadores (least-privilege), não um dos nove. Preservado.

### C23 — Alignment (11 preservações — o caso mais denso)
- `princípios de comportamento desejado e indesejado` (L39) — constituição do modelo/RLAIF
- `princípios explícitos sobre o que o modelo deve e não deve fazer` (L84) — Constitutional AI
- `princípios derivados de fontes diversas` / `princípios de honestidade` / `princípios de redução de dano` / `princípios sobre informação` / `os princípios` (L86) — constituição da Anthropic
- `princípio ausente ou mal redigido` (L130) — diagnóstico de falha de constituição
- `quinze princípios específicos de triagem psiquiátrica` (L144) — constituição médica do caso clínico
- `sete princípios refinados` (L148) — iteração da constituição médica
- `publicada como princípio interno` (L154) — lição organizacional do caso clínico
- `dez princípios específicos do contexto do produto` (L224) — exercício de constituição interna  
  **Todos são princípios da constituição de alignment de IA, não um dos nove da obra.**

### C25 — Trade-offs (2 preservações técnicas)
- `princípio clássico de engenharia de sistemas` / `O princípio aparece em diversas formas na engenharia` (L99) — teorema CAP de Brewer; triângulo de trade-off em engenharia de sistemas
- `o princípio de que otimizar dois lados de um triângulo custa no terceiro precede a IA` (L294) — referência bibliográfica ao IEEE Computer 2012

### C24 — Governança (4 preservações)
- `princípios de IA no site institucional` (L11) — política publicada, genérico
- `princípios, AUP, posicionamento público` (L27) — tabela de camadas de governança
- `Mesmo princípio de classificação por risco` (L89) — tabela de regulação (AI Act)
- `princípios, escopo, casos de uso permitidos e proibidos` (L276) — documento de política

### C04 — Janela de contexto (6 preservações)
- `princípio econômico permanece: contexto longo é mais caro` (L42) — econômico genérico
- `princípio de que contexto longo, ainda que tecnicamente suportado` (L82) — técnico de contexto
- `os princípios principais` de Context Engineering (L103, L105, L146, L180) — CE ≠ sistema dos nove

### C13 — MCP (2 preservações)
- `o princípio — por que padrões de integração emergem` (L10, duas vezes) — padrão de integração M×N, não um dos nove

### C14 — AI Engineering (4 preservações)
- `A empresa adotou como princípio que` / `Esse princípio foi internalizado` (L124) — princípio organizacional interno da empresa fictícia
- `princípios principais` de LLMOps (L135, L195, L232)

---

## Observação sobre itens já migrados
Antes desta migração, alguns arquivos já continham "Invariante(s)" nos seguintes pontos:
- C14C L269: `Invariantes 9 (Operador), 3 (Camada Dupla), 6 (Autonomia Proporcional) e 8 (Responsabilidade Indelegável)` — tabela autoavaliação já migrada
- C14B L43: `Invariante 1 de Plausibilidade` — já migrado
- C16, C17, C19 (conexões), C26: ocorrências "Invariante N" já migradas em ondas anteriores  
  Esses não foram recontados no total acima (apenas trocas desta sessão = 36).
