# Changelog Onda 5 — Pendências D1 e D13
*Data: 2026-06-16 | Executor: Editor Executivo*

---

## D1 — EPÍLOGO DE FECHAMENTO (C28)

### Problema
A última página do livro (fim de `L1-C28-interpretabilidade-mecanicista.md`) ancorava em "instrumento", não em "método". A tese "Modelos passam. Método fica." não aparecia na última página. O livro não fechava onde abria.

Última frase anterior:
> *"A pergunta do auditor deslocou-se de 'o modelo funciona bem' para 'como você sabe que o modelo decidiu como decidiu', e a resposta defensável exige instrumento que precisa estar pronto antes do ofício chegar."*

### Ação executada
Inserido epílogo de 370 palavras **imediatamente antes da seção 28.13 — Autoavaliação**, tornando-se a verdadeira última palavra do corpo do livro (antes das seções de autoavaliação e exercícios finais).

**Localização:** `L1-C28-interpretabilidade-mecanicista.md`, entre o fim da seção 28.12 (Referências) e o início da seção 28.13 (Autoavaliação).

### Texto integral do epílogo inserido

---

**## Epílogo — O que fica**

Você chegou até aqui por dois caminhos possíveis.

O primeiro é o da dona de empresa em Blumenau que quer entender se a IA serve para o balcão dela antes de assinar contrato com o próximo consultor. O segundo é o do CTO de banco médio que precisa responder à ANPD em noventa e cinco dias com evidência técnica de que o modelo não usa atributo protegido como feature de risco. Caminhos diferentes, leituras diferentes, urgências diferentes.

O livro foi escrito para os dois ao mesmo tempo, e isso parece impossível até você perceber que não é. Porque o que separa o CTO defensável do CTO que chega à perícia sem instrumento não é a ferramenta que ele usou — é o método com que ele decidiu quando usar e como medir. E o que separa a dona de empresa que ganha margem com IA da dona de empresa que queima caixa tentando acompanhar o lançamento da semana não é o modelo que ela escolheu — é o critério com que ela avaliou antes de contratar.

O modelo da semana passada já mudou. O que você precisava entender para decidir se ele servia, se ele custava o que custava, se o agente poderia operar sem supervisão humana, se a saída era auditável — isso não mudou. E não vai mudar na semana que vem, nem no ano que vem.

É esse o argumento do livro. Não é um argumento sobre ferramentas. É um argumento sobre onde mora a vantagem competitiva durável em campo que muda toda semana. Mora no método. Sempre morou.

O profissional que saiu daqui sabendo citar o Princípio 7 — IA sem eval é fé, não engenharia — vai conseguir auditar qualquer sistema de qualquer fornecedor em qualquer benchmark futuro. O profissional que saiu daqui com uma lista de prompts vai ter que refazer a lista no próximo release.

O executivo que saiu daqui com um Caderno de Governança vivo, um AI Council com mandato e um processo de simulado de incidente vai conseguir defender a operação diante de qualquer regulador que apareça. O executivo que saiu daqui com o modelo mais cotado da semana vai ter que recomeçar quando o benchmark mudar.

A dona de empresa que saiu daqui sabendo fazer as oito perguntas antes de contratar IA vai economizar o caixa que a concorrente vai queimar em projeto mal dimensionado. O arquiteto que saiu daqui sabendo o que os evals precisam cobrir vai pegar regressão silenciosa antes que ela chegue ao cliente.

O barco muda. A navegação fica.

Você tem o método. O que faz com ele, a partir daqui, é sua decisão — e responsabilidade sua, não da IA que vai ajudar a executar.

**Modelos passam. Método fica.**

---

### Critérios atendidos
- Reativa explicitamente a tese "Modelos passam. Método fica." — última sentença em negrito, ancorando em método.
- Fecha o arco de audiência: cita explicitamente a dona de empresa (C27) e o CTO diante da ANPD (C28), costurando os dois mundos sob o mesmo método.
- Não introduz conceito novo — é síntese e convocação.
- Voz: provocativo, comparativo, sem "Em suma" ou "Em conclusão", sem bullets.
- Título: "O que fica" — eco direto da tese, memorável, citável.
- Formatação: seção de nível `##` coerente com a estrutura do capítulo, inserida como bloco de corpo antes da autoavaliação.

---

## D13 — PERSONA DESENVOLVEDOR: "REPOSITÓRIO DE PROMPTS" (APX-C)

### Problema
O arquivo `L1-C26-roadmap-pessoal.md` já havia sido corrigido em Onda 3 (confirmado em JR-G02 do changelog de galé). Porém o Apêndice C (`L1-APX-C-roadmaps.md`) ainda continha a formulação original, criando inconsistência entre o capítulo e o apêndice de referência sintética.

**Arquivo com problema remanescente:** `04-apendices/L1-APX-C-roadmaps.md`, seção "Roadmap 3 — Desenvolvedor / Arquiteto", Marco 365 dias.

### Antes
```
### Marco 365 dias
- Mentor de outros devs no método dos Princípios
- Contribuição ao repositório de prompts da empresa
- Participação em decisão de arquitetura citando os métodos derivados
```

### Depois
```
### Marco 365 dias
- Mentor de outros devs no método dos Princípios
- Contribuição ao repositório de casos de uso com framework de eval documentado por caso — o que sobrevive é a estrutura de avaliação, não o prompt específico
- Participação em decisão de arquitetura citando os métodos derivados
```

### Justificativa da troca
"Repositório de prompts" cria uma coleção de artefatos datados — em doze meses, os prompts estão obsoletos e o entregável perdeu valor. "Repositório de casos de uso com framework de eval documentado por caso" ancora em julgamento e critério durável: a estrutura que decide o que avaliar, com que critério e como detectar regressão sobrevive a qualquer troca de modelo ou versão. Alinha com o Princípio 7 (Termômetro) e com a tese central. Formulação é consistente com o que já estava no corpo de C26 (seção 26.3.3, linha 186).

---

## RESUMO DAS EDIÇÕES

| ID | Arquivo | Localização | Tipo | Status |
|----|---------|-------------|------|--------|
| D1 | `02-capitulos/L1-C28-interpretabilidade-mecanicista.md` | Entre 28.12 e 28.13 | Inserção de epílogo (370 palavras) | FEITO |
| D13 | `04-apendices/L1-APX-C-roadmaps.md` | Roadmap 3, Marco 365 dias | Substituição cirúrgica de 1 bullet | FEITO |
