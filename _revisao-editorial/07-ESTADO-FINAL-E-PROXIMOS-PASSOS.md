# ESTADO FINAL — Revisão Editorial · Os Invariantes
## As 4 ondas concluídas + o que resta na sua mão

---

## 1. O QUE FOI FEITO

Partimos de uma banca adversarial sobre **73 arquivos lidos 100%** (~231 mil palavras), que produziu **378 achados**. Os quatro foram executados:

| Onda | Foco | Achados | Status |
|---|---|---|---|
| **1** | P0 — credibilidade, coerência, tese | 52 | ✅ ~47 corrigidos no texto; 5 deferidos (decisão/asset) |
| **2** | Durabilidade — migração do perecível para a série | — | ✅ ~14k palavras perecíveis migradas; método + ponteiros |
| **3** | P1 — clareza, retenção, Teste da Joana | 204 | ✅ ~170 editados; resto já resolvido/obsoleto |
| **4** | P2 — acabamento | 122 | ✅ ~100 editados; resto resolvido/obsoleto |
| **5** | Galé — leitura linear (ritmo, transições, repetições, voz) | — | ✅ 45 emendas de fluência em 28 arquivos; 21 pendências autorais consolidadas |

> **Onda 5 (galé) concluída em 2026-06-16.** Detalhe em `08-CHANGELOG-ONDA5-GALE.md`; decisões na sua mão em `09-PENDENTES-ONDA5-DECISAO-AUTOR.md`; backup em `_backup-pre-onda5/`. Achados de maior peso: bug estrutural de numeração em C13 (corrigido), checklist ausente em C18 (adicionado), marcador "Parte 3" no lugar errado (movido), e — pendente de você — **a última frase do livro não ativa a tese "Modelos passam. Método fica."** (D1).

**Cobertura:** dos 378 achados, ~317 foram resolvidos diretamente no manuscrito; ~45 ficaram obsoletos porque ondas anteriores ou a migração já os eliminaram; ~16 são deferidos por dependerem de você (ver §3).

**Transformação estrutural:** o livro deixou de misturar camadas de meia-vida oposta. O perecível foi para os companions que já existiam:
- 30 prompts (APX-L) → `recursos/prompts` · listas → `recursos/ferramentas`, `repos-curados`, `fontes`
- Números cross-vendor → fonte única em `deep-claude/apendice-vivo` (cadência mensal)
- Ambos os repos commitados e sincronizados.

**Resultado mensurável:** capítulos + apêndices passaram de 200.544 → 196.937 palavras — estável em tamanho, mas com a camada perecível removida e método/clareza adicionados. O livro agora cumpre o nome "Os Invariantes".

---

## 2. ARTEFATOS DE CONTROLE (pasta `_revisao-editorial/`)

| Arquivo | Para quê |
|---|---|
| `00-SUMARIO-EXECUTIVO-E-PLANO-DE-ACAO.md` | banca completa + diagnóstico |
| `Tracker-Achados-Banca-Editorial.xlsx` | 378 achados rastreáveis (Dashboard / Achados / P0) |
| `01` a `06` (changelogs) | o que mudou em cada onda, arquivo por arquivo |
| `02-RECOMENDACAO-ESTRUTURA` · `03-MAPA-DE-MIGRACAO` | a estratégia de série |
| `_backup-pre-onda1..4/` | snapshots reversíveis de cada etapa |
| `secoes/` | banca íntegra por arquivo |

---

## 3. O QUE RESTA — só você pode decidir (≈16 itens)

Nenhum é editável por revisão cirúrgica; todos pedem decisão autoral, produção de arte ou verificação externa.

**Decisões estruturais**
- Ordem de leitura **14B ↔ 14C** (afeta numeração e referências cruzadas).
- Reposicionar a seção 10 do F5 / seção do F5 "Quando migrar" (reorganização).
- Política global de estilo: "Curiosidade" vs "Curiosidade ativa" nas autoavaliações.

**Produção de arte (SVG)**
- Diagramas **24.2 / 24.3** (camadas de controle, fluxo de incidente).
- Diagramas **25.2 / 25.3** (trade-offs).
- Matriz visual 4×4 do **F3**. *(placeholders e legendas já estão no texto, marcados `[REQUER ASSET]`.)*

**Voz do autor / verificação**
- Epígrafe **Dijkstra** (C01): localizar fonte, substituir ou remover atribuição.
- Perspectiva proprietária em C05 (quando **não** usar embeddings).
- Persona Desenvolvedor (C26): o "repositório de prompts" como entregável — reancorar em método (era P1).
- Verificação final pré-gráfica: status do **PL 2338/2023**, **DeepSeek-R1** (veículo de publicação), orientações **ANPD** — todos já marcados no texto com ressalva de verificação.

> **Nota:** o P0 do "repositório acompanhante vazio" deixou de ser risco — o `recursos` agora existe, está populado e commitado.

---

## 4. PRÓXIMOS PASSOS RECOMENDADOS

1. **Resolver os ~16 itens da §3** numa sessão de decisões (a maioria é rápida; os SVGs vão para o designer).
2. **Verificação pré-gráfica** dos 3-4 fatos datados marcados no texto.
3. **Revisão de leitura corrida (galé):** com a estrutura estável, uma leitura linear final pega ritmo e emendas que achados isolados não capturam — posso fazê-la como "Onda 5" se quiser.
4. **Cadência do Apêndice Vivo:** definir o ritual mensal de atualização do `deep-claude/apendice-vivo` (é o ponto único de falha da estratégia de durabilidade).

O livro está em condição de **referência**. O que falta é decisão e acabamento de arte — não mais correção de conteúdo.
