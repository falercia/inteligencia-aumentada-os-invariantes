# Changelog de Pendências D18–D21
**Data de execução:** 16 jun 2026  
**Editor executivo:** Claude Sonnet 4.6 (agente de revisão)  
**Escopo:** correções factuais verificadas — DeepSeek-R1 (D18), PL 2338/2023 (D19), ANPD (D20), arXiv Hayes et al. (D21)

---

## D18 — DeepSeek-R1 agora é citável (C16)

**Arquivo:** `02-capitulos/L1-C16-open-source.md`

**Localização 1 — corpo do capítulo (§16.1, parágrafo da virada de 2024-2026):**
- **Antes:** `o DeepSeek R1, em janeiro de 2025, demonstrou que raciocínio em janela longa...`
- **Depois:** `o DeepSeek R1 (DeepSeek-AI, 2025; publicado na Nature, vol. 645, pp. 633–638, e como arXiv:2501.12948), em janeiro de 2025, demonstrou que raciocínio em janela longa...`

**Localização 2 — referências (§16.11):**
- **Antes:** `- [DeepSeek](https://www.deepseek.com/) e papers técnicos do DeepSeek V3 e R1`
- **Depois:** `- [DeepSeek](https://www.deepseek.com/) e papers técnicos do DeepSeek V3 e R1 — DeepSeek-AI. "DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning". *Nature*, vol. 645, pp. 633–638, 2025. DOI: 10.1038/s41586-025-09422-z. Pré-print: arXiv:2501.12948`

**Nota — arquivos com menção ao DeepSeek-R1 fora do C16 (para verificação final — NÃO editados aqui conforme instrução):**
- `02-capitulos/L1-C14B-reasoning-models.md` — CONTÉM menção ao DeepSeek R1 (verificado via grep). Não tocado aqui; checar se precisa da mesma âncora de citação em onda futura.
- `04-apendices/L1-APX-J-trilha-do-numero.md` — linha "DeepSeek-R1: Incentivizing Reasoning Capability..." na tabela de papers, §3, com nota "publicação em periódico revisado por pares não confirmada até a data desta revisão" → **esta ressalva está DESATUALIZADA**: o paper foi publicado na Nature, vol. 645, 2025. Recomenda-se atualizar APX-J nesta nota em onda futura (não editado aqui para evitar conflito de agentes).
- `04-apendices/L1-APX-P-boxes-tecnicos.md` — menção no Box 6 (destilação do R1). Não tocado aqui.
- Vários arquivos de build (`_build/`, `_build_diagramado/`) contêm menções derivadas — gerados automaticamente; não editados individualmente.

---

## D19 — PL 2338/2023 (C19 e C24)

**Status verificado (jun/2026):** aprovado no Senado em 10 de dezembro de 2024; em análise na Câmara dos Deputados desde março de 2025; votação final prevista para 2026; ainda NÃO é lei.

### Arquivo: `02-capitulos/L1-C19-seguranca.md`

**Localização 1 — §19.7, parágrafo PL 2338/2023:**
- **Antes:** `O projeto, em tramitação no Senado Federal, instala regime de classificação por risco...`
- **Depois:** `O projeto foi aprovado no Senado em dezembro de 2024 e está em análise na Câmara dos Deputados, com votação final prevista para 2026 — ainda não é lei (verificar status atual em fonte oficial, conforme Apêndice J — Trilha do Número). Instala regime de classificação por risco...`

**Localização 2 — §19.14 referências:**
- **Antes:** `- PL 2338/2023 — Marco Legal da IA no Brasil (em tramitação)`
- **Depois:** `- PL 2338/2023 — Marco Legal da IA no Brasil (aprovado no Senado em dez/2024; em análise na Câmara dos Deputados; verificar status atual — Apêndice J)`

### Arquivo: `02-capitulos/L1-C24-governanca.md`

**Localização 1 — §24.3.3 tabela "Trilha regulatória", linha PL de IA brasileiro:**
- **Antes:** `| **PL de IA brasileiro** (em tramitação) | ...`
- **Depois:** `| **PL de IA brasileiro** (aprovado no Senado dez/2024; em análise na Câmara; verificar status — Apêndice J) | ...`

**Localização 2 — §24.14 referências:**
- **Antes:** `- Brasil — PL 2338/2023 (em tramitação no Senado Federal)`
- **Depois:** `- Brasil — PL 2338/2023 (aprovado no Senado em dez/2024; em análise na Câmara dos Deputados; votação final prevista para 2026; verificar status atual — Apêndice J)`

**Nota:** APX-J §4 ("PL 2338/2023 no Brasil") já contém o status correto e completo — nenhuma edição necessária neste apêndice.

---

## D20 — Orientações ANPD (C24)

**Arquivo:** `02-capitulos/L1-C24-governanca.md`

**Localização — §24.14 referências:**
- **Antes:** `- ANPD — *Guia Orientativo de Proteção de Dados no uso de IA Generativa* (2024) e demais notas técnicas sobre IA (verificar lista atualizada em www.gov.br/anpd — conforme Apêndice J — Trilha do Número)`
- **Depois:** `- ANPD — *Radar Tecnológico: Inteligência Artificial Generativa* (nov/2024); Agenda Regulatória 2025–2026 (IA como tema prioritário); Resoluções CD/ANPD 30/2025 e 31/2025 (Mapa de Temas Prioritários de fiscalização 2026–2027) — verificar versão corrente em www.gov.br/anpd conforme Apêndice J — Trilha do Número`

**Nota:** o corpo do capítulo (§24.3.3 e o exemplo da seguradora) já usa linguagem durável suficientemente genérica — sem citar nome de documento específico vago — e a ressalva "verificar versão corrente" está presente. Edição mínima aplicada apenas na seção de referências.

---

## D21 — Correção de erro: arXiv Hayes et al.

**Número CORRETO verificado:** `arXiv:2410.22884`  
**Número ERRADO que circulou:** `arXiv:2410.10074`

### Resultado do grep global por "2410.10074" em todo o livro:

| Arquivo | Linha | Status |
|---------|-------|--------|
| `_build_diagramado/chunk-14-14-apendices-M-Q.md` | 2062 | **CORRIGIDO** (`2410.10074` → `2410.22884`) |
| `_revisao-editorial/08-CHANGELOG-ONDA5-GALE.md` | 54 | Histórico de galé — documento de rastreamento, não conteúdo editorial; mantido como registro do erro anterior |
| `_revisao-editorial/09-PENDENTES-ONDA5-DECISAO-AUTOR.md` | 60 | Histórico de pendências — documento de rastreamento; mantido como registro |
| `_revisao-editorial/changelog-onda5/apendices.md` | 66–98 | Changelog anterior que documenta a correção para `2410.22884` e lista `2410.10074` como valor de origem — mantido como registro histórico |

**Arquivos de conteúdo editorial com o número CORRETO (não alterados — já estavam certos):**
- `04-apendices/L1-APX-J-trilha-do-numero.md` → linha 86: `arxiv.org/abs/2410.22884` ✓
- `04-apendices/L1-APX-P-boxes-tecnicos.md` → linha 62: `arxiv.org/abs/2410.22884` ✓

**Autor/título do paper conforme APX-J (confirmar consistência):**
- Autores: Hayes et al. (Google DeepMind)
- Título: "Stealing User Prompts from Mixture of Experts (MoE Tiebreak Leakage)"
- Data: outubro de 2024
- URL correta: arxiv.org/abs/2410.22884

---

## Resumo de arquivos editados

| Item | Arquivo | Tipo de edição |
|------|---------|----------------|
| D18 | `02-capitulos/L1-C16-open-source.md` | 2 edições: citação ancorada no corpo + referência completa em §16.11 |
| D19 | `02-capitulos/L1-C19-seguranca.md` | 2 edições: status atualizado em §19.7 + referências em §19.14 |
| D19 | `02-capitulos/L1-C24-governanca.md` | 2 edições: tabela §24.3.3 + referências §24.14 |
| D20 | `02-capitulos/L1-C24-governanca.md` | 1 edição: referências §24.14 (documentos ANPD específicos) |
| D21 | `_build_diagramado/chunk-14-14-apendices-M-Q.md` | 1 edição: `2410.10074` → `2410.22884` |

**Total de ocorrências de `2410.10074` corrigidas em conteúdo editorial:** 1 (no build chunk; os arquivos fonte já estavam corretos).
