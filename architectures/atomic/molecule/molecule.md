## 🌐 1. Conceito Fundamental

A **Arquitetura Molecular** representa o **nível intermediário da cognição aplicada**.
Ela conecta os **átomos funcionais** (lógica, dados, linguagem, interface) em **estruturas orgânicas de cooperação** — *as moléculas cognitivas*.

Enquanto o átomo é **reutilizável e isolado**,
a molécula é **coordenada e emergente**:
ela nasce quando múltiplos átomos interagem em torno de um propósito semântico.

> ⚛️ Átomo = Função
> 🌿 Molécula = Relação
> 🧬 Organismo = Narrativa

---

## 🧩 2. Estrutura Molecular

Cada molécula é composta por um conjunto de **átomos interconectados** e um **conector de contexto**, que define:

* o propósito da molécula (função cognitiva)
* o protocolo de comunicação entre os átomos
* o grau de acoplamento semântico (baixo ou alto)


# ⚗️ Estrutura Geral — `molecular/`

```
molecular/
│
├── README.md
│
├── classify_text/
│   ├── molecule.yaml
│   ├── pipeline.py
│   ├── schema.yaml
│   ├── atoms/
│   │   ├── logic/
│   │   │   ├── normalize_text.py
│   │   │   └── vector_distance.py
│   │   ├── data_units/
│   │   │   └── micro_corpus.json
│   │   └── prompt_units/
│   │       └── reasoning_chain.yaml
│   └── tests/
│       └── test_pipeline.py
│
└── sentiment_analysis/
    ├── molecule.yaml
    ├── pipeline.py
    ├── schema.yaml
    └── atoms/
        ├── logic/
        │   └── sentiment_score.py
        └── prompt_units/
            └── mood_reasoning.yaml
```

---

# ⚗️ Molecular Layer — Composição de Átomos

A **camada molecular** representa a **primeira forma de vida funcional** na Arquitetura Atômica.

Enquanto os **átomos** são unidades puras e isoladas (funções, operadores, fragmentos de prompt ou dados),
as **moléculas** são **sistemas coordenados** que reúnem esses átomos em **pipelines executáveis** — microfluxos de cognição.

---

## 🌿 Conceito

Cada molécula:
- É composta por **átomos** de diferentes tipos (logic, data, prompt, ui);
- Possui um **esquema de entrada/saída (schema.yaml)**;
- Define seu próprio **DNA funcional (molecule.yaml)**;
- Expõe um **pipeline.py**, que é o script de composição.

---

## 🧩 Tipos de Moléculas

| Tipo | Função | Exemplo |
|------|---------|---------|
| 🧠 **Cognitiva** | Processa linguagem, raciocínio e contexto | `classify_text/` |
| 💾 **Analítica** | Agrega dados, faz predição e inferência | `sentiment_analysis/` |
| 🎨 **Interface** | Organiza interações e microcomponentes UI | `compose_dashboard/` |

---

## ⚙️ Convenções

- `molecule.yaml` → define o DNA estrutural (autor, tipo, IO, dependências)
- `schema.yaml` → especifica formato de entrada/saída
- `pipeline.py` → core funcional, interligando átomos
- `atoms/` → contém os componentes reutilizados
- `tests/` → define comportamentos esperados da molécula

---

## 🧬 Exemplo Visual

```mermaid
graph TD
  A[normalize_text ⚛️] --> B[vector_distance ⚛️]
  B --> C[data_unit.micro_corpus ⚛️]
  C --> D[prompt_unit.reasoning_chain ⚛️]
  D --> E[classify_text 🌿]
  E --> F[output: categoria semântica]
````

---

## ⚙️ 3. Blueprint da Molécula

```yaml
molecule:
  id: mol.cognition.classify_text
  name: "Classify Text"
  type: "Cognitive Molecule"
  purpose: >
    Classifica textos em categorias semânticas, combinando
    operadores lógicos, módulos de prompt e vetores de dados.

  structure:
    atoms_involved:
      - logic/normalize_text.py
      - logic/vector_distance.py
      - prompt_units/reasoning_chain.yaml
      - data_units/micro_corpus.json
    connector: "connector.py"

  connections:
    input: "texto bruto"
    process: ["normalização", "vetorização", "raciocínio semântico"]
    output: "categoria textual"

  dependencies:
    - numpy
    - scikit-learn
    - transformers

  relation_to_next_layer: "Pode se combinar com outras moléculas para formar organismos cognitivos."
```

---

## 🔌 4. `connector.py` — Exemplo de Conector Molecular

```python
from atoms.logic.normalize_text import normalize_text
from atoms.logic.vector_distance import vector_distance
from atoms.prompt_units.reasoning_chain import load_prompt
from atoms.data_units.micro_corpus import get_corpus

def classify_text(input_text: str):
    """
    Conecta átomos para executar a molécula de classificação textual.
    """
    text = normalize_text(input_text)
    corpus = get_corpus()
    prompt = load_prompt("reasoning_chain.yaml")

    # simulação de vetor semântico e inferência
    distance = vector_distance(text, corpus)
    reasoning = prompt.build_response(input_text, context=distance)
    
    return reasoning.get("category", "Desconhecida")
```

---

## 🔬 5. Tipos de Moléculas

| Tipo                            | Função                      | Exemplo                         |
| ------------------------------- | --------------------------- | ------------------------------- |
| **Moleculares Cognitivas**      | Operações mentais compostas | Classificação, Resumo, Tradução |
| **Moleculares Sensoriais**      | Interface e percepção       | UI + OCR + Áudio                |
| **Moleculares Operacionais**    | Controle e automação        | Logging, Feedback, Execução     |
| **Moleculares Metaestruturais** | Regulação de coerência      | Verificação de CNI, Guardrails  |

---

## 🧠 6. Integração com o Micélio Cognitivo (MLP)

Cada molécula, ao ser executada, **não grava dados**,
mas **gera uma relação semântica micelial** no grafo do MLP.

Exemplo de integração (pseudo-código):

```python
from mlp.graph import connect_nodes

connect_nodes(
    source="classify_text",
    target="sentiment_analysis",
    relation="EVOLUI_PARA",
    metadata={"forca_semantica": 0.82, "escala": "meso"}
)
```

> Assim, a molécula torna-se **parte viva da rede cognitiva** —
> cada execução é uma nova raiz no solo micelial.

---

## 📘 7. `meta.yaml` Global das Moléculas

```yaml
meta:
  id: molecule.architecture.v1
  author: "Mia Framework Lab"
  license: "CC-BY-SA-4.0"
  description: >
    Define a estrutura molecular da arquitetura cognitiva ELS,
    onde cada molécula representa uma relação funcional entre átomos.

  molecules:
    - cognition.classify_text
    - cognition.summarize_text
    - sensor.visual_input
    - system.feedback

  relations:
    - "molecules ↔ atoms (conexão lógica)"
    - "molecules ↔ mlp (relação semântica)"
    - "molecules ↔ organisms (integração cognitiva)"
```

## 💡 Filosofia Molecular

> A molécula não é apenas um somatório de átomos —
> ela é **um campo de relações vivas** que dá origem a comportamento.
> Assim como na biologia, **o sentido emerge da composição**,
> e não das partes isoladas.

---

## 🧱 Blueprint Padrão

```yaml
molecule:
  id: mol.namespace.name
  type: cognitive | analytic | interface
  version: 1.0
  author: "Nome do Criador"
  description: >
    Breve explicação sobre a molécula e sua função.
  atoms_used:
    - logic/
    - prompt_units/
    - data_units/
  io:
    input: texto
    output: categoria
  dependencies:
    - numpy
    - sklearn
  connected_to:
    - mol.namespace.other_molecule
```

---

## 🔬 Objetivo

Criar uma **biblioteca molecular**, onde cada unidade é um **organismo semântico modular**.
Essas moléculas podem:

* ser executadas isoladamente;
* ser combinadas em **organismos complexos** (nível superior da arquitetura);
* evoluir conforme feedback do sistema (aprendizado emergente).

---

> “Os átomos definem o que é possível.
> As moléculas decidem o que é vivo.”


## 🌾 Síntese Filosófica

> Átomos são pensamentos.
> Moléculas são relações.
> Organismos são consciências locais.

A **Arquitetura Molecular** é o primeiro degrau de **emergência cognitiva** —
onde funções isoladas passam a ter propósito, e a máquina começa a *significar o mundo*.

---

Posso agora gerar a **segunda parte do projeto molecular**, com o repositório de exemplo (`molecules/classify_text/` completo com YAML + connector funcional + teste unitário)?
Assim teremos o primeiro bloco funcional antes de partir para o nível “organismo”.
