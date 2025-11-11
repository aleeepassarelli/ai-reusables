# ⚙️ Núcleo de Lógica Atômica (`logic/`)

> Contém funções puras, operadores matemáticos, e kernels cognitivos —  
> as **unidades fundamentais de processamento e transformação** dentro da arquitetura atômica.

---

## 🧩 Conceito

Os *logic atoms* são **funções minimamente autocontidas**, projetadas para:
- Operar **sem dependências externas complexas**.
- Ser **determinísticas e testáveis**.
- Permitir **composição** (várias funções podem se combinar em moléculas lógicas).
- Suportar **portabilidade entre camadas** (podem ser usados por scripts, APIs, agentes, ou UIs).

📖 **Analogia:**  
👉 *Se o prompt é o “pensamento” e o dado é o “mundo”, o átomo lógico é o “músculo” que os conecta.*

---

## 🧬 Estrutura do Diretório

```

logic/
├── normalize_text.py       # Limpeza e padronização de texto
├── vector_distance.py      # Operações de similaridade vetorial
└── README.md               # Este arquivo

````

---

## 🔍 Funções Incluídas

### 1. `normalize_text.py`

```python
import re
import unicodedata

def normalize_text(text: str) -> str:
    """
    Normaliza e limpa um texto para processamento linguístico.

    Etapas:
    - Converte para minúsculas
    - Remove acentos e caracteres especiais
    - Substitui múltiplos espaços por um único
    - Remove pontuações não essenciais

    Exemplo:
        >>> normalize_text("Olá, Mundo!!!")
        'ola mundo'
    """
    text = text.lower()
    text = unicodedata.normalize("NFD", text)
    text = text.encode("ascii", "ignore").decode("utf-8")
    text = re.sub(r"[^a-z0-9\s]", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text
````

---

### 2. `vector_distance.py`

```python
import numpy as np

def vector_distance(v1: np.ndarray, v2: np.ndarray, metric: str = "cosine") -> float:
    """
    Calcula a distância entre dois vetores (text embeddings, features, etc.).

    Parâmetros:
      - v1, v2: arrays vetoriais
      - metric: 'cosine' ou 'euclidean'

    Retorna:
      - Distância (float)

    Exemplo:
        >>> vector_distance(np.array([1,0]), np.array([0,1]), "cosine")
        1.0
    """
    if metric == "cosine":
        return 1 - np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))
    elif metric == "euclidean":
        return np.linalg.norm(v1 - v2)
    else:
        raise ValueError("Metric must be 'cosine' or 'euclidean'")
```

---

## 🔗 Integração com Outros Átomos

| Tipo de Átomo  | Relação com Logic                                      | Exemplo                           |
| -------------- | ------------------------------------------------------ | --------------------------------- |
| `prompt_units` | Usa funções de normalização antes da geração de prompt | `normalize_text(user_input)`      |
| `data_units`   | Pré-processamento de datasets                          | `normalize_text(line['summary'])` |
| `ui_atoms`     | Aplicação em filtros de busca e limpeza de input       | `normalize_text(ui_input)`        |

---

## ⚡ Exemplo de Composição

```python
from atoms.logic.normalize_text import normalize_text
from atoms.logic.vector_distance import vector_distance
import numpy as np

text_a = "Inteligência Artificial é incrível!"
text_b = "A inteligência artificial é impressionante."

# 1️⃣ Normaliza
norm_a = normalize_text(text_a)
norm_b = normalize_text(text_b)

# 2️⃣ Gera embeddings simulados
embed_a = np.random.rand(3)
embed_b = np.random.rand(3)

# 3️⃣ Mede similaridade
dist = vector_distance(embed_a, embed_b)
print(f"Distância vetorial: {dist:.4f}")
```

---

## 🧩 Boas Práticas

✅ **Padrões de Design**

* Cada arquivo `.py` deve conter **uma única função ou classe autocontida**.
* Evite imports cruzados entre átomos.
* Nomeie funções de forma descritiva e curta (`normalize_text`, `calculate_score`, etc.).
* Documente com docstring padrão e exemplos executáveis.

✅ **Testes**

* Inclua um arquivo `test_<function>.py` no mesmo diretório ou em `/tests/`.
* Use `pytest` com asserts simples e comparações determinísticas.

✅ **Escalabilidade**

* Para operadores complexos, considere agrupá-los em `molecules/logic/` (camada seguinte).
* Mantenha compatibilidade com **NumPy**, **PyTorch** e **scikit-learn** quando aplicável.

---

## 🧾 Metadados Sugeridos (`meta.yaml`)

```yaml
meta:
  id: logic.v1
  author: "Mia Framework Lab"
  version: 1.0
  description: "Conjunto de funções puras e kernels atômicos reutilizáveis."
  standards:
    - "Cada átomo deve ser independente e testável."
    - "Deve conter docstring, exemplo e metadados básicos."
  tests:
    framework: "pytest"
    path: "tests/"
```

---

## 🧠 Ideia Central

> “A lógica é a gravidade da inteligência —
> ela mantém cada átomo cognitivo ancorado à coerência.”

Essas funções são as bases sobre as quais todas as moléculas e organismos do framework se apoiam.
Sem dependências, sem estado, apenas **razão pura, modular e reusável**.

---

**📄 Última atualização:** 2025-11-11
**Versão:** 1.0
**Status:** 🟢 Estável
**Autor:** Mia Framework Lab

```

