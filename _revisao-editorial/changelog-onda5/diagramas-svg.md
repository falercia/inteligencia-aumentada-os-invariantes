# Changelog — Produção de Diagramas SVG (Onda 5)

Data: 2026-06-16
Autor: Claude (designer de informação)
Escopo: 5 novos SVGs + inserção de referências nos .md + remoção de placeholders

---

## Arquivos SVG criados

### 1. `03-frameworks/imagens/L1-F3-img-01-matriz-4x4.svg`
- **Diagrama:** Matriz 4×4 — Observabilidade × Reversibilidade → Nível de Autonomia
- **viewBox:** 0 0 900 680
- **Conteúdo:** Matriz com cabeçalhos de coluna (Irreversível / Baixa / Média / Alta) e linha (Cega / Baixa / Média / Total). 16 células preenchidas com 4 níveis de autonomia em gradiente visual (creme → laranja → navy). Legenda dos 4 níveis na base.
- **Pasta criada:** `03-frameworks/imagens/` (não existia)

### 2. `02-capitulos/imagens/L1-C42-img-02-camadas-controle.svg`
- **Diagrama:** Pirâmide das 3 camadas de controle — Técnica / Operacional / Executiva
- **viewBox:** 0 0 900 620
- **Conteúdo:** Pirâmide com 4 faixas horizontais (ponta laranja = Estratégia, navy = Executiva, navy médio = Operacional, cinza escuro = Técnica). Coluna lateral direita com donos típicos por camada. Seta bidirecional lateral.

### 3. `02-capitulos/imagens/L1-C42-img-03-fluxo-incidente.svg`
- **Diagrama:** Fluxo de Resposta a Incidente — 7 etapas encadeadas + tabela de cadência por SEV
- **viewBox:** 0 0 1060 560
- **Conteúdo:** Fluxograma horizontal: Detecção → Triagem → Resposta → Comunicação Externa → Postmortem sem Culpa → Ações Corretivas → Retenção de Evidência. Escala SEV-1..SEV-4 no topo. Tabela de cadência na base.

### 4. `02-capitulos/imagens/L1-C43-img-02-arvore-decisao.svg`
- **Diagrama:** Árvore de Decisão Integrada dos 6 Trade-offs Canônicos
- **viewBox:** 0 0 700 820
- **Conteúdo:** 6 caixas verticais encadeadas com setas laranja: T4 → T1 → T5 → T2 → T6 → T3. Cada caixa: badge colorido com número e ordem, rótulo do trade-off, pergunta executiva, e eixo decisor.

### 5. `02-capitulos/imagens/L1-C43-img-03-triangulo-lqc.svg`
- **Diagrama:** Triângulo Latência × Qualidade × Custo
- **viewBox:** 0 0 700 620
- **Conteúdo:** Triângulo equilátero com vértices circulares coloridos (laranja = Latência, navy = Qualidade, cinza escuro = Custo). Micro-legendas em cada aresta. Texto central "Otimize dois, pague no terceiro." Tabela de decisão na base.

---

## Inserções nos arquivos .md

### `02-capitulos/L1-C24-governanca.md`
- **Diagrama 24.2:** Removida linha `<!-- [REQUER ASSET] Arquivo pendente de produção: imagens/L1-C42-img-02-camadas-controle.svg -->`. A linha `![...]` já existia e agora aponta para arquivo real.
- **Diagrama 24.3:** Removida linha `<!-- [REQUER ASSET] Arquivo pendente de produção: imagens/L1-C42-img-03-fluxo-incidente.svg -->`. A linha `![...]` já existia e agora aponta para arquivo real.

### `02-capitulos/L1-C25-trade-offs.md`
- **Diagrama 25.2:** Adicionada linha `> ![Árvore de decisão integrada dos seis trade-offs](imagens/L1-C43-img-02-arvore-decisao.svg)` no bloco do Diagrama 25.2, após a linha 📊.
- **Diagrama 25.3:** Adicionada linha `> ![Triângulo Latência × Qualidade × Custo](imagens/L1-C43-img-03-triangulo-lqc.svg)` no bloco do Diagrama 25.3, após a linha 📊.

### `03-frameworks/L1-F3-agente-prop.md`
- Adicionada linha `![Matriz 4×4 de propriedade do agente — observabilidade × reversibilidade](imagens/L1-F3-img-01-matriz-4x4.svg)` logo após a descrição "Matriz 4×4 cruzando observabilidade × reversibilidade..." na seção 2. FUNCIONAMENTO.

---

## Validação técnica

- Todos os SVGs: XML bem-formado, tags fechadas, `xmlns` declarado, `<title>` e `<desc>` no topo.
- Estilo da casa respeitado: fundo `#fefce8`, navy `#0d1b2a`/`#1b263b`, laranja `#E97451`, texto mínimo font-size 10.
- viewBoxes calibrados para o conteúdo (sem vazamento de elementos).
- Nenhum gradiente berrante; paleta executiva limpa.
