# 🎨 Átomos de Interface (`ui_atoms/`)

> Módulos mínimos de **interação e percepção** do usuário.  
> Cada *UI Atom* é um componente visual ou funcional simples —  
> projetado para ser combinado e evoluir junto com a experiência do sistema.

---

## 🌱 Conceito

Os **UI Atoms** são os **tijolos visuais fundamentais** da arquitetura atômica.  
Cada átomo representa uma ação, um input, uma visualização ou um elemento de resposta.

Enquanto:
- `logic/` representa a **função**,
- `prompt_units/` representa o **pensamento**, e
- `data_units/` representa o **conhecimento**,

os `ui_atoms/` representam a **presença** —  
a forma como o usuário *vê, sente e reage* ao sistema.

---

## 🧩 Estrutura de Diretório

```

ui_atoms/
├── components/
│   ├── button_basic.py
│   ├── card_display.py
│   ├── input_text.py
│   └── loader_spinner.py
├── templates/
│   ├── base_ui.yaml
│   └── theme_dark.yaml
└── README.md

````

---

## 🧠 Pilares de Design Atômico

| Pilar | Descrição | Exemplo |
|--------|------------|---------|
| **Isolamento** | Cada átomo deve funcionar sozinho | `button_basic` não depende de um “card” |
| **Recomposição** | Múltiplos átomos criam moléculas (ex: “Formulário”) | `input_text + button_basic` |
| **Consistência** | Visual e funcional entre átomos | mesmo espaçamento, tema, tipografia |
| **Escalabilidade** | Podem crescer em organismos e templates | `card_display` → `dashboard_component` |

---

## 🧱 Exemplo 1 — Átomo: `button_basic.py`

```python
# ui_atoms/components/button_basic.py

import streamlit as st

def button_basic(label: str, key: str = None, color: str = "primary"):
    """
    Botão atômico básico — elemento mínimo de interação.
    """
    clicked = st.button(label, key=key)
    if clicked:
        st.toast(f"🔘 {label} clicado!", icon="💡")
    return clicked
````

🧩 **Uso em um organismo:**

```python
from ui_atoms.components.button_basic import button_basic

if button_basic("Executar Modelo"):
    run_model()
```

---

## 🧱 Exemplo 2 — Átomo: `input_text.py`

```python
# ui_atoms/components/input_text.py

import streamlit as st

def input_text(label: str, placeholder: str = "", key: str = None):
    """
    Campo de texto simples.
    """
    return st.text_input(label, placeholder=placeholder, key=key)
```

💡 Pode ser combinado com `button_basic`:

```python
user_query = input_text("Pergunta:", "Digite aqui...")
if button_basic("Enviar"):
    st.write(f"🧠 Processando: {user_query}")
```

---

## 🧱 Exemplo 3 — `card_display.py`

```python
# ui_atoms/components/card_display.py

import streamlit as st

def card_display(title: str, content: str, icon: str = "📦"):
    """
    Elemento visual para mostrar blocos de informação contextual.
    """
    st.markdown(f"### {icon} {title}")
    st.info(content)
```

Exemplo:

```python
card_display("Resultado", "A IA detectou padrões relevantes no dataset.")
```

---

## 🎨 Blueprint de UI Atoms

Cada átomo deve declarar suas **propriedades mínimas** e **interações básicas**.

| Campo      | Tipo     | Descrição                                             |
| ---------- | -------- | ----------------------------------------------------- |
| `id`       | string   | Identificador único (`ui_atom.nome`)                  |
| `type`     | string   | Tipo de elemento (`button`, `input`, `display`, etc.) |
| `stateful` | bool     | Indica se mantém estado entre interações              |
| `event`    | callable | Função acionada em evento de interação                |
| `meta`     | dict     | Informações adicionais (cor, ícone, tema)             |

Exemplo YAML (`ui_atoms/templates/base_ui.yaml`):

```yaml
id: ui.button_basic
type: button
label: "Executar"
stateful: false
event: "run_model"
meta:
  color: "primary"
  icon: "⚡"
```

---

## 🧩 Integração com Outros Átomos

| Tipo           | Interação                        | Exemplo                                       |
| -------------- | -------------------------------- | --------------------------------------------- |
| `logic`        | Reage a eventos                  | `button_basic` → aciona `normalize_text()`    |
| `prompt_units` | Exibe o raciocínio em tempo real | `card_display` → mostra prompt formatado      |
| `data_units`   | Mostra contexto dinâmico         | `input_text` → injeta dado em unidade textual |

---

## 📘 Exemplo de Organismo Atômico (Mini UI)

```python
import streamlit as st
from ui_atoms.components.input_text import input_text
from ui_atoms.components.button_basic import button_basic
from ui_atoms.components.card_display import card_display

st.title("🧠 Atomic Interaction Demo")

user_text = input_text("Digite algo:", "Olá, mundo atômico!")
if button_basic("Analisar"):
    response = f"O texto '{user_text}' contém {len(user_text.split())} palavras."
    card_display("Resultado", response, "📊")
```

Resultado:

```
🧠 Atomic Interaction Demo
[ Input ] [ Button ] → [ Display ]
```

---

## 🧾 Metadados (`meta.yaml`)

```yaml
meta:
  id: ui_atoms.v1
  author: "Mia Framework Lab"
  version: 1.0
  description: "Componentes atômicos de interface para visualização e interação modular."
  dependencies:
    - streamlit
    - rich
```

---

## 💡 Boas Práticas

✅ **Acessibilidade:** mantenha contraste, legibilidade e interações por teclado.
✅ **Neutralidade:** evite dependências visuais complexas — mantenha átomos simples.
✅ **Composição:** projete cada átomo para ser usado em qualquer molécula.
✅ **Sincronia:** mantenha coesão entre estados visuais e dados.

---

## ✨ Ideia Central

> “Cada UI Atom é uma célula sensorial —
> traduz o raciocínio interno da IA em percepção tangível para o humano.”

Essa camada torna o sistema **visível, responsivo e emocionalmente compreensível**,
fechando o ciclo da **cognição estética** da arquitetura atômica.

---

**📄 Última atualização:** 2025-11-11
**Versão:** 1.0
**Status:** 🟢 Estável
**Autor:** Mia Framework Lab

```
