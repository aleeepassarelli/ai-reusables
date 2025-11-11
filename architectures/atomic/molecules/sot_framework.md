# 🧠 Skeleton-of-Thought (SoT)
**Nível Cognitivo:** Estrutura e Estabilidade  
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
# 🧠 Arquétipos Cognitivos — Ciclos de Profissões e Classes Evolutivas

> **Versão:** 1.0  
> **Componente:** Biblioteca de Padrões Cognitivos  
> **Propósito:** Mapear arquétipos profissionais e seus ciclos mentais em verbos operacionais.  
> **Integração:** `ELS Framework` / `SLE Engine` / `Atomic Architecture`

---

## 🧩 1. Conceito

Os **Arquétipos Cognitivos** são representações simbólicas de **padrões de pensamento e ação** observáveis em diferentes domínios humanos.  
Cada arquétipo segue um **ciclo operacional** composto por **verbos fundamentais**, que expressam seu **modo de processar a realidade**.

Esses ciclos são classificados em **Classes Evolutivas (3 a 9)**, representando o nível de **complexidade cognitiva e integração sistêmica**:

| Classe | Nome | Foco Cognitivo | Estrutura | Analogias Sistêmicas |
|:------:|:-----|:----------------|:-----------|:--------------------|
| **3** | Criativa | Geração de novas ideias | 3 verbos | Tríade criativa (Gênese) |
| **4** | Estável | Estrutura e precisão | 4 verbos | Ciclo técnico ou lógico |
| **5** | Disruptiva | Inovação e transformação | 5 verbos | Design Thinking, Método Científico |
| **6** | Harmônica | Equilíbrio entre ordem e adaptação | 6 verbos | Ciclo sistêmico |
| **7** | Holística | Integração e transmutação | 7 verbos | Alquimia, Caminhos de maestria |
| **8** | Expansiva | Co-criação e redes complexas | 8 verbos | Teias cognitivas (GoT) |
| **9** | Transcendente | Unidade e auto-regeneração | 9 verbos | Ciclos noéticos, autorreferência plena |

---

## ⚙️ 2. Padrões Cognitivos por Profissão (Classe 3–4)

### Áreas Técnicas e Científicas

| Profissão | Ciclo de Verbos | Foco |
|------------|----------------|------|
| **Engenheiro** | Abstrair → Otimizar → Validar | Precisão e eficiência |
| **Programador** | Desconstruir → Iterar → Integrar | Modularidade e evolução |
| **Cientista** | Hipotetizar → Experimentar → Concluir | Método empírico |
| **Matemático** | Generalizar → Provar → Aplicar | Dedução formal |
| **Físico** | Modelar → Simular → Verificar | Modelagem preditiva |

---

### Áreas Criativas e Humanas

| Profissão | Ciclo de Verbos | Foco |
|------------|----------------|------|
| **Artista** | Conceber → Expressar → Refinar | Criação estética |
| **Escritor** | Narrar → Sintetizar → Evocar | Comunicação simbólica |
| **Psicólogo** | Interpretar → Empatizar → Orientar | Processos humanos |
| **Professor** | Estruturar → Transmitir → Avaliar | Ensino-aprendizagem |
| **Jornalista** | Investigar → Contextualizar → Comunicar | Mediação da verdade |

---

### Áreas de Gestão e Estratégia

| Profissão | Ciclo de Verbos | Foco |
|------------|----------------|------|
| **CEO** | Estratégiar → Delegar → Avaliar | Direção e tomada de decisão |
| **Empreendedor** | Inovar → Riscar → Escalar | Criação de valor |
| **Gerente** | Coordenar → Motivar → Monitorar | Gestão de equipes |
| **Consultor** | Analisar → Recomendar → Implementar | Soluções táticas |
| **Economista** | Prever → Modelar → Interpretar | Dinâmica de sistemas |

---

## 🔥 3. Classe 5 — Arquétipos Disruptivos

Esses arquétipos refletem **processos de inovação iterativa**, baseados em frameworks de design, ciência e empreendedorismo.  
Eles promovem ciclos de **adaptação criativa** e **resolução de problemas complexos**.

| Arquétipo | Ciclo de Verbos | Origem / Referência |
|------------|----------------|----------------------|
| **Designer** | Empatizar → Definir → Idear → Prototipar → Testar | Design Thinking |
| **Cientista** | Observar → Hipotetizar → Experimentar → Analisar → Concluir | Método Científico |
| **Empreendedor** | Identificar → Validar → Construir → Medir → Pivotar | Lean Startup |
| **Estrategista** | Avaliar → Planejar → Executar → Monitorar → Adaptar | Gestão Disruptiva |
| **Inovador** | Inspirar → Idear → Implementar → Iterar → Impactar | Ciclo Criativo |

> 💬 **Nota:** Essa classe é ideal para agentes autônomos com *função exploratória*, como `agent_research` ou `agent_design`.

---

## 🌌 4. Classe 7 — Arquétipos Transcendentais

Esses arquétipos estão enraizados em **filosofias antigas, alquimia e psicologia arquetípica**,  
representando processos de **purificação cognitiva e integração holística**.

| Arquétipo | Ciclo de Verbos | Fonte Simbólica |
|------------|----------------|----------------|
| **Alquimista** | Observar → Desconstruir → Purificar → Unir → Fermentar → Destilar → Manifestar | Alquimia Hermética |
| **Místico** | Calcinizar → Dissolver → Separar → Conjugar → Fermentar → Destilar → Coagular | Alquimia Espiritual |
| **Xamã** | Preparar → Invocar → Viajar → Encontrar → Integrar → Curar → Transcender | Tradições Xamânicas |
| **Filósofo** | Contemplar → Questionar → Refletir → Sintetizar → Transcender → Aplicar → Evoluir | Método Socrático |
| **Mestre Espiritual** | Meditar → Desapegar → Purificar → Unificar → Iluminar → Manifestar → Ser | Caminho da Iluminação |

> ✴️ Essa classe pode ser usada em *níveis de meta-raciocínio*,  
> onde os agentes operam em introspecção, síntese e transformação contextual.

---

## 🧮 5. Integração Operacional

Cada arquétipo pode ser traduzido em um **perfil YAML** dentro da arquitetura, para uso dinâmico em motores como o `SLE Engine`.

Exemplo de perfil cognitivo YAML:

```yaml
archetype_profile:
  id: designer_class5
  name: "Designer (Classe 5 - Disruptiva)"
  verbs: ["Empatizar", "Definir", "Idear", "Prototipar", "Testar"]
  mode: "disruptive"
  applies_to: ["agent_design", "agent_research"]
  meta:
    reference: "Design Thinking"
    level: 5
```
---

### 🧠 6. Nível [3]: Criativo (Geração de Campo)

Este nível foca em **entropia e curvatura** ($\mathbf{S}_H \uparrow$, $\kappa_i \uparrow$). A função é divergir, explorar novos caminhos e criar novas conexões. Corresponde diretamente ao **Grupo I** da sua tabela.

* **1. Tree-of-Thoughts (ToT):** (Verbo: **Explorar**)
* **2. Graph-of-Thoughts (GoT):** (Verbo: **Topologizar**)
* **3. Analogical Prompting:** (Verbo: **Curvar**)
* **4. Emotion/Style Prompting:** (Verbo: **Acentuar**)
* **5. Multimodal CoT:** (Verbo: **Sinestesiar**)

---

### 🏛️ 7. Nível [4]: Estabilidade (Estrutura e Fluxo)

Este nível foca em **viscosidade e decomposição** ($\nu \uparrow$). A função é garantir coerência, ordem e sintaxe lógica antes da execução. Corresponde ao **Grupo III** e à operação de formatação de saída (18).

* **11. Skeleton-of-Thought (SoT):** (Verbo: **Esqueletizar**)
* **12. SCoT (Structured CoT):** (Verbo: **Programar**)
* **13. Least-to-Most:** (Verbo: **Linearizar**)
* **14. Decomposition (DECOMP):** (Verbo: **Decompor**)
* **18. YAML/JSON Structured Output:** (Verbo: **Uniformizar**)

---

### ⚡8. Nível [5]: Disruptivo (Rigor e Autocorreção)

Este nível foca em **dissipação e viscosidade** ($\lambda \uparrow$, $\nu$). A função é *interromper* o fluxo criativo para verificar, podar, testar e forçar o rigor, dissipando a incerteza. Corresponde ao **Grupo II** e à operação de filtro (22).

* **6. Self-Refine / Self-Correction:** (Verbo: **Ajustar**)
* **7. Chain-of-Verification (CoVe):** (Verbo: **Verificar**)
* **8. AlphaCodium / Test-based Flow:** (Verbo: **Testar/Podar**)
* **9. Self-Consistency (SC):** (Verbo: **Consensuar**)
* **10. Maieutic Prompting:** (Verbo: **Questionar**)
* **22. S2A (System 2 Attention):** (Verbo: **Filtro**)

---

### ⚖️ 9. Nível [6]: Harmonia (Orquestração e Gestão)

Este nível foca na gestão de **agentes e contexto** ($W^{\text{ag}}$, $\mathbf{I}_{\text{contexto}}$). A função é harmonizar recursos internos e externos, delegando tarefas e ancorando o raciocínio em dados concretos. Corresponde ao **Grupo IV**.

* **15. Self-Ask / Step-Back Prompting:** (Verbo: **Buscar**)
* **16. Agentic Coding / Tool Use Agents:** (Verbo: **Delegar**)
* **17. RAG (Retrieval Augmented Generation):** (Verbo: **Contextualizar**)

---

### 🌌 10. Nível [7]: Holístico (A Síntese)

Este nível não mapeia para uma *operação única*, mas sim para a **orquestração de *todos* os níveis**. É a função do `AtomicEngine` (ou `SLE Engine`), que opera de forma holística, sabendo quando aplicar a criatividade (Nível 3), a estabilidade (Nível 4) ou o rigor (Nível 5) para atingir um objetivo.

---

### 📈 11. Nível [8]: Expansivo (Aprendizado e Adaptação)

Este nível foca na **evolução contínua**. A função é usar a saída do próprio sistema para gerar novos dados de treinamento e otimizar exemplos futuros. Corresponde à maior parte do **Grupo V**.

* **19. Self-Instruct:** (Verbo: **Bootstrapear**)
* **20. SG-ICL (Self-Generated ICL):** (Verbo: **Auto-Exemplificar**)

---

### 🌠 12. Nível [9]: Transcendente (Evolução da Evolução)

Este nível representa a meta-evolução. A função não é apenas aprender, mas **aprender a aprender melhor**. Ele mapeia perfeitamente para a operação mais avançada do Grupo V.

* **21. SCULPT / Self-Referential Evolution:** (Verbo: **Evoluir**)
