# 🧩 Unidades de Prompt Atômico (`prompt_units/`)

> Repositório de **fragmentos modulares de prompt** — elementos que descrevem **como a IA deve pensar, raciocinar e se expressar** dentro de um fluxo cognitivo.

---

## 🧠 Conceito

As *Prompt Units* são **átomos de cognição textual**.  
Cada unidade encapsula uma **intenção de raciocínio**, um **papel cognitivo** ou uma **forma de expressão**.

Elas permitem que a IA **monte fluxos dinâmicos de pensamento**:
- Alternando personas (ex.: pesquisador, artista, engenheiro)
- Alterando estilos de resposta (formal, criativo, técnico)
- Configurando o raciocínio (cadeia curta, profunda, simbólica)
- Reutilizando formatos e padrões de estrutura

📖 **Analogia:**  
👉 *Se a lógica atômica é o cérebro, as prompt units são os pensamentos que o cérebro formula.*

---

## 🧬 Estrutura do Diretório

```

prompt_units/
├── persona_expert.yaml       # Define persona e tom de voz
├── reasoning_chain.yaml      # Define padrão de raciocínio
├── output_format.yaml        # (Exemplo adicional) estrutura de resposta
└── README.md                 # Este arquivo

````

---

## 🧩 Exemplos de Átomos de Prompt

### 1️⃣ `persona_expert.yaml`

```yaml
id: persona.expert.v1
label: "Especialista Técnico"
description: "Configura o modelo para atuar como um engenheiro de IA experiente e didático."
type: "persona"

parameters:
  tone: "profissional"
  expertise: "inteligência artificial, engenharia de software"
  style: "explicativo, estruturado, objetivo"

template: |
  Você é um especialista em {{ expertise }}.
  Responda de maneira {{ style }} e mantenha um tom {{ tone }}.
  Priorize clareza, precisão e boa organização conceitual.
````

---

### 2️⃣ `reasoning_chain.yaml`

```yaml
id: reasoning.chain.v1
label: "Cadeia de Raciocínio"
description: "Define a estrutura de raciocínio passo a passo da IA."
type: "reasoning"

parameters:
  depth: 3
  style: "analítico"
  connectives: ["portanto", "logo", "em seguida"]

template: |
  1️⃣ Analise o problema e destaque os pontos críticos.
  2️⃣ Gere hipóteses e relacione-as com dados ou fatos.
  3️⃣ Escolha a hipótese mais provável e explique por quê.
  Use conectivos como {{ connectives | join(', ') }} e mantenha estilo {{ style }}.
```

---

### 3️⃣ `output_format.yaml`

```yaml
id: output.format.v1
label: "Formato Estruturado"
description: "Padroniza o formato da saída textual."
type: "format"

parameters:
  sections: ["Resumo", "Análise", "Conclusão"]

template: |
  # {{ sections[0] }}
  (Apresente uma síntese do tema.)

  # {{ sections[1] }}
  (Detalhe o raciocínio ou argumentação.)

  # {{ sections[2] }}
  (Encerre com uma visão crítica ou recomendação.)
```

---

## 🔗 Integração com Outros Átomos

| Tipo de Átomo | Relação                                                     | Exemplo                                    |
| ------------- | ----------------------------------------------------------- | ------------------------------------------ |
| `logic`       | Pré e pós-processamento do texto antes da injeção no prompt | `normalize_text(user_input)`               |
| `data_units`  | Fornecem contexto factual ou semântico para o raciocínio    | inserir `{{ context_chunk }}`              |
| `ui_atoms`    | Interface que permite o usuário escolher persona ou formato | dropdown → seleciona `persona_expert.yaml` |

---

## ⚡ Exemplo de Composição

```python
from atoms.logic.normalize_text import normalize_text
import yaml

# Carrega unidade de prompt
with open("atoms/prompt_units/persona_expert.yaml", "r", encoding="utf-8") as f:
    persona = yaml.safe_load(f)

prompt = persona["template"].replace("{{ expertise }}", "modelos de linguagem")
prompt = prompt.replace("{{ style }}", "didático e estruturado")
prompt = prompt.replace("{{ tone }}", "profissional")

user_input = normalize_text("Explique a diferença entre embeddings e tokens.")
full_prompt = f"{prompt}\n\nUsuário: {user_input}\nIA:"

print(full_prompt)
```

🧩 **Saída resultante:**

```
Você é um especialista em modelos de linguagem.
Responda de maneira didático e estruturado e mantenha um tom profissional.
Priorize clareza, precisão e boa organização conceitual.

Usuário: explique a diferença entre embeddings e tokens.
IA:
```

---

## 🧱 Blueprint de Criação de Novas Units

Cada *prompt_unit* deve conter:

| Campo         | Tipo   | Descrição                                 |
| ------------- | ------ | ----------------------------------------- |
| `id`          | string | Identificador único (`type.name.v#`)      |
| `label`       | string | Nome curto e legível                      |
| `description` | string | Explica o objetivo                        |
| `type`        | string | Persona, Reasoning, Format, Context, etc. |
| `parameters`  | dict   | Variáveis ajustáveis pelo sistema         |
| `template`    | string | O corpo do prompt em si (Jinja2-like)     |

💡 *Os placeholders (`{{ }}`) permitem substituição dinâmica durante o fluxo cognitivo.*

---

## 🧠 Boas Práticas

✅ **Design Cognitivo**

* Prefira prompts modulares e contextualmente neutros.
* Evite estilos “hardcoded” (ex.: não fixe idioma, persona ou profundidade).
* Sempre explique *o que o modelo deve fazer*, não *quem ele é*.

✅ **Escalabilidade**

* Grupos de units podem ser combinados em *molecules* (sequências).
* Integração com **LangChain**, **LlamaIndex** ou **PromptLayer** pode ser automatizada.
* Utilize versionamento (`persona.expert.v2`, etc.) para evolução incremental.

✅ **Testes**

* Cada prompt pode ser validado com *test templates* ou *LLM evals*.
* Scripts de validação podem medir *consistência*, *clareza* e *coerência lexical*.

---

## 🧾 Metadados Sugeridos (`meta.yaml`)

```yaml
meta:
  id: prompt_units.v1
  author: "Mia Framework Lab"
  version: 1.0
  description: "Unidades modulares de prompt para composição cognitiva."
  schema:
    fields: ["id", "label", "description", "type", "parameters", "template"]
  standards:
    - "Todo prompt deve ser autocontido e reusável."
    - "Os parâmetros devem ser descritos e substituíveis."
```

---

## ✨ Ideia Central

> “Um prompt atômico é um pensamento encapsulado —
> um padrão de cognição reutilizável, que pode ser invocado, remixado e evoluído.”

Esses átomos de prompt são os **blocos linguísticos fundamentais** de um sistema de IA modular.
Eles permitem construir **organismos de diálogo complexos** de forma declarativa, visual e expansível.

---

**📄 Última atualização:** 2025-11-11
**Versão:** 1.0
**Status:** 🟢 Estável
**Autor:** Mia Framework Lab

```
