# Repositório Acompanhante

> **[PENDENTE — VERIFICAÇÃO PRÉ-PUBLICAÇÃO OBRIGATÓRIA]**
> O repositório `github.com/falercia/inteligencia-aumentada-recursos` deve estar público, funcional e com as sete pastas listadas abaixo **antes do lançamento**. Verificar: (1) repositório existe e está público; (2) cada pasta listada existe com README funcional; (3) ao menos um artefato executável por pasta está disponível. Sem essa verificação, NÃO PUBLICAR — todas as promessas do livro sobre artefatos executáveis dependem deste repositório estar operacional.

> *O padrão dura no livro. O número muda no repositório.*

---

Este livro tem um companheiro executável público que carrega o que muda mais rápido do que a tinta no papel. Enquanto o livro entrega o método que sobrevive à próxima geração de modelo — os princípios, os frameworks, a anatomia das decisões, os anti-padrões observáveis — o repositório carrega o número datado: prompts em XML versionado, golden sets executáveis, scripts de regressão, caderno operacional de governança em arquivos editáveis, changelog público versionado.

A combinação dos dois materializa o Princípio Três da obra, **Camada Dupla**. Quem só lê o livro sai com método e precisa montar os artefatos do zero. Quem opera só com o repositório sem ler o livro opera no escuro, porque não vai entender por que cada peça está naquela posição. Quem usa os dois sai com modelo mental sólido e ativos prontos para entrar em pipeline.

---

## Endereço

**[github.com/falercia/inteligencia-aumentada-recursos](https://github.com/falercia/inteligencia-aumentada-recursos)**

Licenças: MIT para código, CC-BY 4.0 para conteúdo editorial. Uso comercial permitido com atribuição.

---

## O que vive lá agora

| Pasta | Conteúdo | Capítulos relacionados |
|---|---|---|
| `/prompts` | 30 prompts profissionais em XML, com golden set, prefill, self-critique, anti-padrões e métrica de qualidade por prompt | C9 · F4 · Apêndice L |
| `/governance` | Caderno de Governança v1.0 em 6 seções fatiadas, modelo de 6 páginas para imprimir e assinar, modelos clonáveis dos 6 anexos | C24 · F6 · Apêndice O |
| `/evals` | `eval_runner.py` executável, `compile_golden_sets.py`, judges integrados (substring, regex, json_schema, classification), gate de CI | C21 · F8 |
| `/datasets` | Golden sets em JSONL compilados a partir dos YAMLs originais, prontos para CI | C21 · C23 |
| `/agents` | Quatro agentes educacionais executáveis em Python puro — A01 (ReAct Simples), A02 (Escala de Propriedade nos 4 níveis F3 lado a lado), A03 (Orquestrador-Especialistas, multiagente cooperativo em estrela reusando `/prompts`) e A04 (Multiagente Debate, adversarial com juiz integrável a `/evals`). Todos com tools simuladas seguras, tracing local em JSONL, gates, kill switch testável e exemplos rodáveis | C12 · C14C · C21 · C25 · F3 · F8 |
| `/mcp` | Servidores MCP educacionais — M01 (Hello World com Resource, Tool e Prompt mínimos) e M02 (Biblioteca Interna que expõe os prompts de `/prompts` e o caderno de governança como Resources para qualquer cliente MCP), com cliente de teste local e config-exemplo para Claude Desktop | C13 · F5 |
| `/notebooks` | 4 notebooks fundacionais executáveis com narrativa didática célula a célula — tokenização com `tiktoken`, reprodução do experimento *Lost in the Middle*, embeddings com visualização 2D e busca semântica, e demonstração quantitativa de prompt caching | C3 · C4 · C5 · C18 |

## Cada pasta tem o seu próprio README

Cada pasta com conteúdo tem `README.md` próprio com instruções específicas, ficha técnica do que entrega, padrões de uso, exemplos rodáveis e conexão com os capítulos do livro. Antes de clonar artefato isolado, vale ler o README da pasta correspondente — quinze minutos de leitura economizam horas de tentativa-e-erro.

Quem identifica lacuna, anti-padrão útil para a obra, ou caso de uso não coberto pelas estruturas atuais, é convidado a abrir issue no repositório com o template correspondente. Contribuições qualificadas com fonte primária ou validação por especialista entram nas revisões seguintes, com atribuição quando o contribuidor autoriza.

---

## Como começar

Três caminhos, conforme a intenção:

1. **Quero entender antes de usar.** Abra `prompts/P-LEG-01/` e leia o `README.md` da pasta, depois compare com a ficha conceitual correspondente no Apêndice L. Em quinze minutos você terá o mapa mental completo de como livro e repositório se costuram.

2. **Quero colocar em produção rápido.** Pegue o prompt mais próximo do seu domínio, copie o diretório inteiro para o seu repositório interno, adapte a constituição ao seu contexto, construa seu golden set próprio com pelo menos vinte casos representativos do seu tráfego real, rode `eval_runner.py` antes de cada release.

3. **Quero contribuir.** Leia `CONTRATO.md` e abra issue com a categoria sugerida. Contribuições qualificadas com fonte primária são incorporadas nas revisões seguintes, com atribuição quando o contribuidor autoriza.

---

## Política de evolução

O repositório é atualizado quando há entrega de qualidade para fazer — não por calendário, mas por movimento relevante do mercado ou da segurança que justifique revisão. A prioridade é sempre a qualidade da entrega sobre o cumprimento de datas. Releases recebem tag semântica e `CHANGELOG.md` versionado, indicando mudança item por item, motivo da mudança, e impacto observado em golden set ou em produção. A política editorial é simples e dura: nenhuma promessa de release que não esteja pronta para ser cumprida, e nenhum release publicado sem ter passado pela mesma disciplina de revisão que o livro exige de qualquer artefato sério.

A política editorial é simples: nenhum release publicado sem ter passado pela mesma disciplina de revisão que o livro exige de qualquer artefato sério. O leitor que clona o repositório pode ativar *watch* no GitHub para receber notificação de novos releases, e o autor compromete-se apenas com a verdade do que foi entregue, jamais com data futura que não dependa só dele.

---

## Conexão capítulo a capítulo

Ao longo da leitura, cada vez que aparecer a marcação **▸ repo** ou a referência a um caminho `pasta/arquivo`, trata-se de artefato executável que vive no repositório. Quem está com pressa pode anotar o caminho e visitar depois; quem quer ver o instrumento em mãos pode abrir em outra aba enquanto lê.

> *Quem só lê o livro sai com método. Quem usa este repositório acrescenta implementação. Quem opera só com este repositório sem ler o livro opera no escuro.*
