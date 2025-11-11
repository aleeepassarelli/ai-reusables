# 📁 Estrutura de Diretórios

```
molecules/
└── classify_text/
    ├── __init__.py
    ├── molecule.yaml
    ├── connector.py
    ├── tests/
    │   └── test_classify_text.py
    └── atoms/
        ├── logic/
        │   ├── normalize_text.py
        │   └── vector_distance.py
        ├── prompt_units/
        │   └── reasoning_chain.yaml
        └── data_units/
            └── micro_corpus.json
```

---

## 🧬 `molecule.yaml`

> Define o DNA funcional da molécula.

```yaml
molecule:
  id: mol.cognition.classify_text
  name: "Classify Text"
  version: 1.0
  type: "Cognitive Molecule"
  author: "Mia Framework Lab"
  description: >
    Molécula cognitiva composta por operadores lógicos, módulos de prompt
    e unidades de dados. Sua função é classificar textos em categorias
    semânticas, com base em similaridade vetorial e raciocínio contextual.

  created_at: "2025-11-11"
  atoms_involved:
    logic:
      - normalize_text.py
      - vector_distance.py
    prompt_units:
      - reasoning_chain.yaml
    data_units:
      - micro_corpus.json

  io_schema:
    input: "texto bruto"
    output: "categoria semântica inferida"

  dependencies:
    - numpy
    - scikit-learn
    - transformers

  integration:
    connected_to:
      - mol.cognition.summarize_text
      - mol.system.feedback

  memory_relation: "Micélio Cognitivo (MLP)"
  semantic_link:
    relation: "EVOLUI_PARA"
    target: "organism.semantic_agent"
    force: 0.82

  tags: ["nlp", "semantic", "classification", "molecule"]
```

---

## 🔌 `connector.py`

> O conector molecular coordena os átomos, define a sequência de execução
> e produz uma saída coerente.

```python
import json
from atoms.logic.normalize_text import normalize_text
from atoms.logic.vector_distance import vector_distance
from atoms.prompt_units.reasoning_chain import load_prompt
from atoms.data_units.micro_corpus import get_corpus

def classify_text(input_text: str):
    """
    Conecta átomos para executar a molécula de classificação textual.
    Retorna uma categoria inferida com base em contexto semântico.
    """
    text = normalize_text(input_text)
    corpus = get_corpus()
    prompt = load_prompt("reasoning_chain.yaml")

    similarities = []
    for entry in corpus:
        dist = vector_distance(text, entry["text"])
        similarities.append((entry["category"], 1 - dist))

    # Escolhe categoria mais semelhante
    category, score = max(similarities, key=lambda x: x[1])

    # Raciocínio simbólico via prompt
    reasoning = prompt.build_response(
        input_text,
        context={"categoria": category, "confiança": round(score, 2)}
    )

    return {
        "input": input_text,
        "categoria": reasoning["categoria"],
        "confiança": reasoning["confiança"],
        "explicação": reasoning["raciocínio"]
    }

if __name__ == "__main__":
    sample = "O modelo apresentou erro de conexão ao servidor."
    result = classify_text(sample)
    print(json.dumps(result, ensure_ascii=False, indent=2))
```

---

## ⚙️ `atoms/logic/normalize_text.py`

```python
import re

def normalize_text(text: str) -> str:
    """Remove pontuações, converte para minúsculas e limpa espaços extras."""
    text = re.sub(r"[^a-zA-ZÀ-ÿ\s]", "", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip().lower()
```

---

## ⚙️ `atoms/logic/vector_distance.py`

```python
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_distances

_vectorizer = TfidfVectorizer()

def vector_distance(text_a: str, text_b: str) -> float:
    """Calcula distância vetorial entre dois textos."""
    vectors = _vectorizer.fit_transform([text_a, text_b])
    dist = cosine_distances(vectors[0], vectors[1])[0][0]
    return float(dist)
```

---

## 🧩 `atoms/prompt_units/reasoning_chain.yaml`

```yaml
prompt:
  name: "Raciocínio para Classificação"
  steps:
    - "Analise o texto e identifique seu contexto principal."
    - "Compare com as categorias conhecidas."
    - "Selecione a mais apropriada."
    - "Explique brevemente a razão."
  output_schema:
    categoria: str
    confiança: float
    raciocínio: str
```

---

## 🧠 `atoms/data_units/micro_corpus.json`

```json
[
  {"category": "erro_sistema", "text": "falha na conexão do servidor"},
  {"category": "melhoria_produto", "text": "sugestão de nova funcionalidade"},
  {"category": "elogio", "text": "excelente desempenho do modelo"},
  {"category": "reclamação", "text": "o aplicativo travou novamente"}
]
```

---

## 🧪 `tests/test_classify_text.py`

```python
from molecules.classify_text.connector import classify_text

def test_classify_error_case():
    text = "O sistema apresentou erro ao carregar os dados."
    result = classify_text(text)
    assert result["categoria"] in ["erro_sistema", "reclamação"]
    assert 0 <= result["confiança"] <= 1
    assert isinstance(result["explicação"], str)
```

---

## 🧬 Síntese

> A **molécula** é a **primeira unidade de inteligência colaborativa**.
>
> Diferente do átomo, ela já **negocia significados** — interliga raciocínio, dados e função.
> Cada execução dela pode gerar um **novo nó micelial** dentro do MLP, expandindo a rede viva de cognição.

---
