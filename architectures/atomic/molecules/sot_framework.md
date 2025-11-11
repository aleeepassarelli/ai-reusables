# 🧠 Skeleton-of-Thought (SoT)
**Nível Cognitivo:** 5 – Estrutura e Estabilidade  
**Função:** Garantir coerência lógica e estrutural antes da expansão paralela do raciocínio.  
**Tipo:** Operação de Viscosidade Cognitiva  
**Dependências:** DECOMP, SCoT, Least-to-Most  

---

## 1. Conceito
O **Skeleton-of-Thought (SoT)** é a fase em que o sistema organiza seu raciocínio em **uma estrutura mínima coerente**, criando um *esqueleto* lógico antes de gerar conteúdo completo.  
Ele evita dispersão, garante consistência e fornece uma “espinha dorsal” para que agentes ou processos subsequentes possam expandir o contexto sem perda de integridade semântica.

---

## 2. Função na Arquitetura ELS
| Componente | Papel no Fluxo |
|-------------|----------------|
| **Entrada** | Ideia, contexto ou problema bruto (ruído sem estrutura). |
| **Operação SoT** | Organiza o raciocínio em tópicos, subtarefas ou blocos estruturados. |
| **Saída** | Representação formal em YAML, JSON, Markdown, ou esquema hierárquico. |

O SoT atua como uma **ferramenta de estabilização cognitiva**. Ele é acionado antes da execução paralela (ex.: CoT, ToT, GoT) e depois da fase de geração criativa inicial.

---

## 3. Estrutura Operacional
Um SoT segue o seguinte formato interno:

```yaml
sot:
  id: <identificador>
  goal: <descrição da tarefa>
  context: <sumário do problema>
  skeleton:
    - etapa_1: <descrição breve>
    - etapa_2: <descrição breve>
    - etapa_3: <descrição breve>
  expansion_rules:
    - detalhar cada etapa em subtarefas concretas
    - validar dependências entre blocos
    - preservar coerência global
```

---

### 🧠 Nível 3: Criativo (Geração de Campo)

Este nível foca em **entropia e curvatura** ($\mathbf{S}_H \uparrow$, $\kappa_i \uparrow$). A função é divergir, explorar novos caminhos e criar novas conexões. Corresponde diretamente ao **Grupo I** da sua tabela.

* **1. Tree-of-Thoughts (ToT):** (Verbo: **Explorar**)
* **2. Graph-of-Thoughts (GoT):** (Verbo: **Topologizar**)
* **3. Analogical Prompting:** (Verbo: **Curvar**)
* **4. Emotion/Style Prompting:** (Verbo: **Acentuar**)
* **5. Multimodal CoT:** (Verbo: **Sinestesiar**)

---

### 🏛️ Nível 4: Estabilidade (Estrutura e Fluxo)

Este nível foca em **viscosidade e decomposição** ($\nu \uparrow$). A função é garantir coerência, ordem e sintaxe lógica antes da execução. Corresponde ao **Grupo III** e à operação de formatação de saída (18).

* **11. Skeleton-of-Thought (SoT):** (Verbo: **Esqueletizar**)
* **12. SCoT (Structured CoT):** (Verbo: **Programar**)
* **13. Least-to-Most:** (Verbo: **Linearizar**)
* **14. Decomposition (DECOMP):** (Verbo: **Decompor**)
* **18. YAML/JSON Structured Output:** (Verbo: **Uniformizar**)

---

### ⚡ Nível 5: Disruptivo (Rigor e Autocorreção)

Este nível foca em **dissipação e viscosidade** ($\lambda \uparrow$, $\nu$). A função é *interromper* o fluxo criativo para verificar, podar, testar e forçar o rigor, dissipando a incerteza. Corresponde ao **Grupo II** e à operação de filtro (22).

* **6. Self-Refine / Self-Correction:** (Verbo: **Ajustar**)
* **7. Chain-of-Verification (CoVe):** (Verbo: **Verificar**)
* **8. AlphaCodium / Test-based Flow:** (Verbo: **Testar/Podar**)
* **9. Self-Consistency (SC):** (Verbo: **Consensuar**)
* **10. Maieutic Prompting:** (Verbo: **Questionar**)
* **22. S2A (System 2 Attention):** (Verbo: **Filtro**)

---

### ⚖️ Nível 6: Harmonia (Orquestração e Gestão)

Este nível foca na gestão de **agentes e contexto** ($W^{\text{ag}}$, $\mathbf{I}_{\text{contexto}}$). A função é harmonizar recursos internos e externos, delegando tarefas e ancorando o raciocínio em dados concretos. Corresponde ao **Grupo IV**.

* **15. Self-Ask / Step-Back Prompting:** (Verbo: **Buscar**)
* **16. Agentic Coding / Tool Use Agents:** (Verbo: **Delegar**)
* **17. RAG (Retrieval Augmented Generation):** (Verbo: **Contextualizar**)

---

### 🌌 Nível 7: Holístico (A Síntese)

Este nível não mapeia para uma *operação única*, mas sim para a **orquestração de *todos* os níveis**. É a função do `AtomicEngine` (ou `SLE Engine`), que opera de forma holística, sabendo quando aplicar a criatividade (Nível 3), a estabilidade (Nível 4) ou o rigor (Nível 5) para atingir um objetivo.

---

### 📈 Nível 8: Expansivo (Aprendizado e Adaptação)

Este nível foca na **evolução contínua**. A função é usar a saída do próprio sistema para gerar novos dados de treinamento e otimizar exemplos futuros. Corresponde à maior parte do **Grupo V**.

* **19. Self-Instruct:** (Verbo: **Bootstrapear**)
* **20. SG-ICL (Self-Generated ICL):** (Verbo: **Auto-Exemplificar**)

---

### 🌠 Nível 9: Transcendente (Evolução da Evolução)

Este nível representa a meta-evolução. A função não é apenas aprender, mas **aprender a aprender melhor**. Ele mapeia perfeitamente para a operação mais avançada do Grupo V.

* **21. SCULPT / Self-Referential Evolution:** (Verbo: **Evoluir**)
