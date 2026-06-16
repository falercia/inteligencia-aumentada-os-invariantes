# Migração de Conteúdo Perecível → Repo Recursos

> Data: 2026-06-16
> Operação: população do repositório COMPANION `inteligencia-aumentada-recursos` com conteúdo extraído do livro

---

## Arquivos criados no repositório recursos

**Repositório:** `github.com/falercia/inteligencia-aumentada-recursos`
**Caminho host base:** `/Users/fabiogarcia/Documents/Repositorios/Github falercia/inteligencia-aumentada-recursos/`

### 1. `apendice-vivo/README.md`
**Criado em:** 2026-06-16
**Conteúdo:** Ponteiro para a fonte única de números cross-vendor da série (modelos, preços, benchmarks, janelas de contexto) mantida no repositório `deep-claude/apendice-vivo`. Não duplica dados — explica a decisão editorial de fonte única (Camada Dupla, Princípio Três) e entrega o método vendor-neutral de ler comparações de modelo e preço de token: o que olhar, como normalizar, por que não memorizar ranking. Inclui tabela de estrutura do Apêndice Vivo do deep-claude, cadência de atualização mensal e capítulos relacionados do livro.
**Fonte primária:** APX-J (Trilha do Número), `deep-claude/apendice-vivo/README.md`

### 2. `ferramentas/README.md`
**Criado em:** 2026-06-16
**Conteúdo:** Catálogo completo de ferramentas e stack extraído do APX-D do livro. Cobre oito categorias: plataformas de inferência (D.2), modelos open weights para self-host (D.3), frameworks de agente e orquestração (D.4), bancos vetoriais (D.5), observabilidade e LLMOps (D.6), frameworks de evals (D.7), MCP (D.8) e gestão de prompts (D.9). A coluna de critério de seleção em seis dimensões (Maturidade, Adoção, Custo, Encaixe com stack brasileira, Suporte, Estabilidade) foi preservada como cabeçalho do catálogo. Estado de cada ferramenta referenciado como "junho/2026". Nota de data e cadência de revisão no cabeçalho. Tom vendor-neutral.
**Fonte primária:** `_backup-pre-onda2/04-apendices/L1-APX-D-ferramentas.md`

### 3. `repos-curados/README.md`
**Criado em:** 2026-06-16
**Conteúdo:** Lista de repositórios GitHub extraída do Cap 17 do livro (seção 17.6 "Lista corrente como exercício de aplicação"). Estruturada com o Protocolo de 30 Minutos (tabela dos seis critérios duráveis com onde olhar, sinal de passa e sinal de falha) e as quatro armadilhas clássicas (estrelas, README de marketing, demonstração, post de blog) como cabeçalho antes da lista — para que o método apareça antes do inventário. Inclui descrição do ciclo de vida do repositório (cinco fases com sinais). Data de observação junho/2026 declarada com aviso explícito de que a lista envelhece e o método não.
**Fonte primária:** `_backup-pre-onda2/02-capitulos/L1-C17-github-repos.md`

### 4. `fontes/README.md`
**Criado em:** 2026-06-16
**Conteúdo:** Fusão do APX-E (Leituras Complementares) e APX-F (Comunidade Brasileira de IA em 2026) em arquivo único, organizados por tipo: livros de fundamento técnico, livros de IA aplicada, livros de governança e operação, blogs e newsletters em inglês (divididos em fonte de provedor vs. análise independente), cursos e recursos de aprendizado, newsletters brasileiras, podcasts brasileiros (divididos em dedicados a IA vs. tecnologia ampla), comunidades online, conferências brasileiras e crítica honesta da cena brasileira. Critérios de curadoria declarados no cabeçalho (profundidade sobre divulgação, fonte primária verificável, validade temporal declarada). Data de revisão no cabeçalho; revisão anual para a seção de comunidade brasileira.
**Fonte primária:** `_backup-pre-onda2/04-apendices/L1-APX-E-leituras.md` e `L1-APX-F-newsletters.md`

---

## Arquivo editado no repositório recursos

### 5. `README.md` (raiz do repositório) — edição aditiva
**Editado em:** 2026-06-16
**O que mudou:** Adicionadas quatro novas linhas na tabela "O que vive aqui" (`/apendice-vivo`, `/ferramentas`, `/repos-curados`, `/fontes`) e quatro novas linhas na tabela de status "Outras pastas" (seção "Estado atual"). Nenhuma linha existente foi removida ou alterada.

---

## Decisões editoriais registradas

- **Não duplicar números.** O `apendice-vivo/README.md` é ponteiro, não cópia. A decisão de manter modelos, preços e benchmarks exclusivamente no `deep-claude/apendice-vivo` evita inconsistência quando os números mudarem.
- **Critério antes da lista.** Em `repos-curados/README.md` e `ferramentas/README.md`, o critério de avaliação aparece antes do inventário — aplicação direta do que o Cap 17 prega sobre postura epistêmica.
- **Fusão APX-E + APX-F.** As duas fontes foram fundidas em `fontes/README.md` porque são complementares e o leitor que busca "onde aprender" ou "onde encontrar comunidade" não deveria precisar navegar para dois arquivos separados.
- **Backups estáveis como fonte.** Todo conteúdo foi extraído dos arquivos em `_backup-pre-onda2`, não dos arquivos vivos do livro, para estabilidade da base.
