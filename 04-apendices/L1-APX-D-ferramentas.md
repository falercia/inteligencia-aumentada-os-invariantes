# Apêndice D — Ferramentas e Stack
## *Curadoria datada, com critério quantitativo de escolha*

> *Estado: junho de 2026. Revisão periódica conforme o ecossistema evolui, sem cadência fixa anunciada. Esta lista envelhece, e o leitor deve consultar a versão atualizada no canal oficial da obra.*

---

## D.0 — Por que o apêndice de ferramentas precisa de data e critério, e não apenas inventário

O profissional brasileiro que abre apêndice de ferramentas em livro técnico costuma encontrar uma de duas armadilhas. Ou recebe lista de marcas sem critério de escolha, em que cabe ao leitor adivinhar por que uma plataforma aparece antes da outra, ou recebe lista datada implicitamente, sem cabeçalho de validação, e descobre seis meses depois que metade das opções mudou de preço, foi adquirida, mudou de licença ou foi descontinuada. Este apêndice opta por critério explícito e data declarada, com revisão programada, para evitar as duas armadilhas.

A regra estrutural é que cada ferramenta listada vem com nota curta de aplicação, e cada categoria vem com critério recomendado de escolha e sinais de armadilha. O leitor que aplicar o critério antes de adotar a ferramenta toma decisão informada; o leitor que copiar a lista sem critério está fazendo o mesmo erro que este apêndice quer evitar.

---

## D.1 — Critério quantitativo de escolha em seis dimensões

Para qualquer ferramenta ou plataforma desta lista, recomenda-se a avaliação nas seis dimensões abaixo antes da adoção. A avaliação não exige planilha sofisticada; vale anotação em folha em branco com nota de zero a dez por dimensão, e a regra prática é: ferramenta abaixo de seis em qualquer dimensão crítica para o caso de uso é candidata duvidosa, e ferramenta com média ponderada abaixo de sete não compensa adoção.

| Dimensão | O que avaliar | Âncoras de calibração (nota 1–10) | Sinal de risco |
|---|---|---|---|
| **Maturidade** | Anos desde lançamento, número de versões estáveis, presença de versão LTS, frequência de breaking changes nos últimos doze meses | 10 = LTS declarado, 3+ anos de mercado, menos de 1 breaking change por ano; 5 = produto lançado há 12–24 meses, sem LTS; 1 = lançado há menos de 6 meses, sem versão estável | Menos de doze meses no mercado, breaking changes a cada release menor, ausência de LTS declarado |
| **Adoção** | Downloads mensais, estrelas no GitHub, contribuidores ativos nos últimos noventa dias, presença em rankings de mercado (Gartner, Forrester) | 10 = top-3 da categoria, 100k+ stars, 50+ contribuidores ativos/mês; 5 = 10k–50k stars, comunidade ativa mas nichada; 1 = menos de 1k stars, contribuidor único | Tração baixa em estrelas e downloads, contribuidor único, sem citação em pesquisa independente |
| **Custo** | Camada gratuita real (não trial), preço mensal mínimo em reais ou dólares, modelo de cobrança (assento, uso, throughput), tendência de preços nos últimos vinte e quatro meses | 10 = camada gratuita generosa para produção real, preço previsível, histórico estável; 5 = trial de 30 dias ou freemium limitado, preço médio de mercado; 1 = sem camada gratuita, preço opaco, histórico de aumentos súbitos | Camada gratuita inadequada para teste real, preço enterprise opaco, histórico de aumentos súbitos |
| **Encaixe com stack brasileira** | Suporte explícito a português, integração com gateways nacionais (PIX, boletos), conformidade declarada com LGPD, presença comercial no Brasil | 10 = documentação em PT-BR, LGPD compliance declarada, parceiro comercial no Brasil; 5 = interface em inglês com suporte a português no modelo, sem parceiro local; 1 = sem suporte a português, sem documentação sobre LGPD | Sem suporte a português, sem documentação sobre LGPD, sem representação ou parceiro comercial nacional |
| **Suporte** | Documentação em inglês ou português, comunidade ativa em fóruns ou Discord, SLA declarado em planos pagos, presença de comunidade BR | 10 = documentação exemplar, Discord ativo com +1k membros, SLA contratual em plano pago; 5 = documentação suficiente, fórum com resposta em dias, sem SLA formal; 1 = documentação fragmentada, fórum inativo, sem SLA | Documentação incompleta, fórum vazio, sem SLA explícito, ausência total de comunidade em português |
| **Estabilidade** | Cadência de releases, qualidade do changelog público, histórico de breaking changes nos últimos doze meses, política de deprecation | 10 = releases previsíveis com changelog detalhado, zero breaking changes no ano, deprecation com 6+ meses de aviso; 5 = releases irregulares, changelog sumário, 1 breaking change no ano; 1 = releases sem aviso, changelog ausente, deprecation sem aviso | Releases imprevisíveis, changelog vago, mais de duas breaking changes em doze meses, deprecation sem aviso prévio |

Em casos críticos (produção em escala, conformidade regulatória, dependência estratégica), recomenda-se aplicar a matriz de cobertura do framework F5 em complemento, comparando a ferramenta candidata com pelo menos duas alternativas.

---

**Camada viva.** O método está aqui; os artefatos/listas que mudam vivem no repositório de recursos da obra ([github.com/falercia/inteligencia-aumentada-recursos](https://github.com/falercia/inteligencia-aumentada-recursos) → `ferramentas`), atualizados continuamente.

---

*Apêndice D · Ferramentas e Stack. Catálogo detalhado por categoria (plataformas de inferência, modelos open weights, frameworks de agente, bancos vetoriais, observabilidade, evals, MCP, gestão de prompts) disponível no repositório acompanhante, com estado datado e critério aplicado conforme D.1.*

