# Apêndice G — Papers Fundamentais
## *Curadoria de papers que sustentam o estado da arte conceitual em IA generativa*

> Curadoria por categoria. Cada entrada com uma ou duas linhas explicando por que ler.

---

## I. Transformer e arquitetura

1. **Vaswani et al. — *Attention Is All You Need* (Google, 2017).** O paper que mudou a IA moderna. Leitura inegociável.
2. **Devlin et al. — *BERT* (Google, 2018).** Pré-treinamento bidirecional. Fundamento de embeddings modernos.
3. **Radford et al. — *GPT* (OpenAI, 2018) e *GPT-2* (OpenAI, 2019).** Pré-treinamento generativo e ganho por escala.
4. **Brown et al. — *Language Models are Few-Shot Learners* (GPT-3, OpenAI, 2020).** Emergência de capacidade por escala.
5. **Touvron et al. — *Llama* (Meta, 2023) e *Llama 2* / *Llama 3* (Meta, 2023-2024).** Família open weights de referência.
6. **Jiang et al. — *Mistral 7B* (Mistral, 2023) e *Mixtral of Experts* (Mistral, 2024).** Mistura de especialistas em open weights.
7. **DeepSeek-AI — *DeepSeek-V3* e *DeepSeek-R1* (DeepSeek, 2024-2025).** Arquitetura MoE e raciocínio em peso aberto.
8. **Hoffmann et al. — *Training Compute-Optimal Large Language Models* (Chinchilla, DeepMind, 2022).** Leis de escala revisadas.
9. **Anil et al. — *PaLM 2 Technical Report* (Google, 2023) e *Gemini Technical Report* (Google DeepMind, 2023-2024).** Família de modelos multimodais.
10. **Anthropic — *The Claude 3 Model Family* (2024).** Documentação de família comercial.

---

## II. Contexto e atenção

11. **Liu et al. — *Lost in the Middle* (Stanford, 2023).** Base empírica do invariante das extremidades.
12. **Press et al. — *ALiBi: Train Short, Test Long* (Meta, 2022).** Encoding posicional alternativo.
13. **Su et al. — *RoFormer* (RoPE, 2023).** Rotary position embeddings.
14. **Dao et al. — *FlashAttention* e *FlashAttention-2* (Stanford, 2022-2023).** Eficiência de atenção em GPUs.

> **Nota sobre Context Engineering (C11):** Context Engineering como disciplina sistemática não tem paper seminal consolidado em 2026 — a fundamentação é baseada em prática documentada (ver documentação da Anthropic e OpenAI em APX-H, Seção IV) e nos papers de otimização de contexto acima. Para otimização programática de prompts por framework, ver Khattab et al. — *DSPy: Compiling Declarative Language Model Calls into State-of-the-Art Pipelines* (Stanford, 2023).

---

## III. Alinhamento, RLHF e preferência

15. **Christiano et al. — *Deep RL from Human Preferences* (OpenAI / DeepMind, 2017).** Primeira formalização moderna do RLHF.
16. **Ouyang et al. — *InstructGPT* (OpenAI, 2022).** RLHF aplicado em produção.
17. **Bai et al. — *Constitutional AI* (Anthropic, 2022).** RLAIF e CAI.
18. **Anthropic — *Collective Constitutional AI* (2023).** CAI com input público.
19. **Rafailov et al. — *Direct Preference Optimization* (Stanford, 2023).** Substituição do PPO no mercado.
20. **Hong et al. — *ORPO* (2024).** Variante sem modelo de referência.
21. **Ethayarajh et al. — *KTO* (2024).** Alinhamento por teoria do prospecto.

---

## IV. Evals e avaliação

22. **Liang et al. — *HELM* (Stanford CRFM, 2022).** Avaliação holística.
23. **Srivastava et al. — *BIG-bench* (Google e colaboradores, 2022).** Benchmark colaborativo.
24. **Hendrycks et al. — *Measuring Massive Multitask Language Understanding* (MMLU, 2020).** Benchmark de referência amplo.
25. **Zheng et al. — *Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena* (LMSYS, 2023).** Base de LLM-as-judge.
26. **Liu et al. — *G-Eval* (Microsoft, 2023).** Eval por LLM alinhada com humano.
27. **Es et al. — *RAGAS* (Exploding Gradients, 2023).** Eval específica para RAG.
28. **Mazeika et al. — *HarmBench* (CAIS, 2024).** Adversarial e red-teaming padronizados.
29. **Narayanan, A. & Kapoor, S. — *Evaluating LLMs is a minefield* (Princeton, 2023).** Análise crítica de como benchmarks podem enganar — antídoto necessário para quem usa evals como critério de decisão.

---

## V. Agentes e tool use

30. **Yao et al. — *ReAct* (Princeton e Google, 2022).** Padrão de raciocinar e agir.
31. **Schick et al. — *Toolformer* (Meta, 2023).** Modelos que aprendem a usar ferramentas.
32. **Wang et al. — *Voyager* (NVIDIA, 2023).** Agente em Minecraft como modelo de descoberta.
33. **Park, J. et al. — *Generative Agents: Interactive Simulacra of Human Behavior* (Stanford, 2023).** Arquitetura de agentes com memória, reflexão e planejamento — referência para design de sistemas multi-agente.

### Documentação técnica e guias de referência

> Os itens abaixo não são papers revisados por pares, mas são referências técnicas de alta relevância operacional citadas na obra.

34. **Anthropic — *Building Effective Agents* (2024).** Guia técnico de referência — distinção entre workflow e agente. Ver também APX-H, Seção IV.
35. **Significant Gravitas — *AutoGPT* technical reports (2023).** Relatório de repositório — marco histórico de agentes abertos de código aberto. Ver também APX-H, Seção IV.

---

## VI. Interpretabilidade mecanicista

36. **Olah et al. — *In-context Learning and Induction Heads* (Anthropic, 2022).** Circuitos identificados.
37. **Anthropic — *Towards Monosemanticity* (2023) e *Scaling Monosemanticity* (2024).** Sparse autoencoders aplicados a modelos comerciais.
38. **Nanda et al. — *Progress measures for grokking via mechanistic interpretability* (DeepMind, 2023).** Caso paradigmático de mech interp.

---

## VII. Segurança e comportamento

39. **Perez et al. — *Discovering Language Model Behaviors with Model-Written Evals* (Anthropic, 2022).** Auto-descoberta de comportamentos problemáticos.
40. **Ganguli et al. — *Red Teaming Language Models* (Anthropic, 2022).** Metodologia de red-teaming.
41. **Sharma et al. — *Towards Understanding Sycophancy* (Anthropic, 2023).** Mecânica da bajulação.
42. **Greshake et al. — *Indirect Prompt Injection in LLM-Integrated Applications* (2023).** Vetor de ataque dominante.
43. **Bender et al. — *On the Dangers of Stochastic Parrots* (Washington, 2021).** Crítica fundamentada.
44. **Weidinger et al. — *Taxonomy of Risks posed by Language Models* (DeepMind, 2022).** Mapa estruturado de riscos.

---

## VIII. RAG e retrieval

45. **Lewis et al. — *Retrieval-Augmented Generation* (Meta e UCL, 2020).** Paper seminal.
46. **Karpukhin et al. — *Dense Passage Retrieval* (Meta, 2020).** Retrieval moderno.
47. **Reimers, Gurevych — *Sentence-BERT* (UKP TU Darmstadt, 2019).** Embeddings para busca semântica.
48. **Izacard et al. — *Atlas: Few-shot Learning with Retrieval Augmented Language Models* (Meta, 2022).** RAG com retrieval profundo.

---

## Como ler papers de IA

1. Abstract e conclusão primeiro. Em sessenta por cento dos casos, isso basta.
2. Para os quarenta por cento que valem mais, leia diagramas e tabelas.
3. Equações apenas onde a matemática realmente sustenta a tese.
4. Discussões e limitações dizem mais que método em muitos casos.
5. Para citação séria, leia integralmente.
