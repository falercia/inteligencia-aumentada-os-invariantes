# Apêndice M — Manifesto de Bolso: Os Nove Princípios em Uma Página

> *Imprima. Cole na parede. Distribua ao time. Leve para a próxima decisão de IA.*

---

## Os Nove Princípios

### 1 — Plausibilidade
**"O modelo entrega o plausível, não o verdadeiro — e os dois coincidem, até a hora em que não."**
*Mecânica:* o modelo de linguagem é motor de plausibilidade; calibrar confiança é trabalho do operador, em proporção ao custo do erro.
*Violação típica:* aceitar número jurídico ou financeiro porque soou certo.

### 2 — Extremidades
**"O meio do contexto é onde a informação vai morrer."**
*Mecânica:* atenção alta nas pontas, diluída no centro; densidade de relevância vence volume bruto.
*Violação típica:* enterrar a regra crítica no parágrafo quarenta do prompt.

### 3 — Camada Dupla
**"Decore o padrão, consulte o número."**
*Mecânica:* o que muda em semanas vive em apêndice datado; o que dura por anos vive na cabeça.
*Violação típica:* memorizar que o modelo X lidera o benchmark Y e ficar obsoleto no próximo release.

### 4 — Encaixe
**"Escolha pelo padrão da tarefa, nunca pela versão da moda."**
*Mecânica:* o modelo decide-se por eixo de tarefa — código, matemática, multimodal, contexto longo — ponderado por custo composto, nunca pelo lançamento da semana.
*Violação típica:* migrar o stack para o release recente sem teste cego na carga real.

### 5 — Custo Composto
**"Trivial é o preço do token; o que quebra o orçamento é quantas vezes você o paga."**
*Mecânica:* custo é tokens vezes chamadas vezes tier vezes redundância; as alavancas são arquiteturais.
*Violação típica:* otimizar prompt enquanto um loop de agente dispara quarenta chamadas redundantes.

### 6 — Autonomia Proporcional
**"Só dê ao agente a autonomia que você consegue medir e desfazer."**
*Mecânica:* o nível de agência é função da capacidade de rastrear e reverter.
*Violação típica:* agente com escrita em produção sem tracing nem kill switch.

### 7 — Termômetro
**"IA sem eval é fé, não engenharia."**
*Mecânica:* nenhum sistema entra em produção sem detecção de regressão; prompt sem golden set é opinião.
*Violação típica:* trocar prompt porque ficou melhor sem dataset que prove que não piorou.

### 8 — Responsabilidade Indelegável
**"A IA executa; a responsabilidade tem sempre um nome humano."**
*Mecânica:* toda saída em produção tem dono, controle de acesso, trilha de auditoria e caminho de reversão.
*Violação típica:* foi a IA que decidiu, como desculpa para decisão que ninguém assume.

### 9 — Operador
**"A IA multiplica competência e incompetência pelo mesmo fator."**
*Mecânica:* o ganho vem do operador que sabe pedir, rejeitar e validar.
*Violação típica:* esperar que a IA cubra a falta de critério de quem a opera.

---

## A frase-síntese

> ## *Modelos passam. Método fica.*
>
> O modelo que lidera hoje o benchmark será ultrapassado no próximo trimestre. A capacidade de escolher com critério, avaliar com método, governar com responsabilidade e aprender continuamente — essa não envelhece. É o que a obra inteira treina.

---

## Como usar

| Situação | Pergunte-se |
|----------|-------------|
| Vou escolher um modelo | Princípio 4: qual o encaixe por eixo de tarefa? |
| Vou subir um agente | Princípio 6: tenho tracing e rollback proporcionais? |
| Vou trocar um prompt em produção | Princípio 7: rodou contra o golden set? |
| Vou apresentar a iniciativa à diretoria | Princípios 8 e 9: há dono e há decisão estruturada? |
| Vou cortar custo de IA | Princípio 5: mexi nas três alavancas arquiteturais? |
| Vou citar um benchmark | Princípio 3: conferi a data e a fonte? |

---

## Ressalva

Os Princípios 1 (Plausibilidade) e 2 (Extremidades) dependem da arquitetura generativa atual. Arquiteturas futuras podem mudar a mecânica. Os outros sete são princípios de prática e julgamento, independentes de arquitetura.

---

## Atribuição

Os Nove Princípios Permanentes da Inteligência Artificial — sistema da obra *Inteligência Aumentada* (Fabio Garcia, 2026). Distribuição livre com atribuição.
