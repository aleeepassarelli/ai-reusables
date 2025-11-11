# 🧩 Unidades de Dados Atômicos (`data_units/`)

> Repositório de **fragmentos de informação mínima e reutilizável**, projetados para alimentar o raciocínio da IA.  
> Cada *data unit* encapsula um pedaço de conhecimento factual, um exemplo contextual ou um microdataset.

---

## 🧬 Conceito

As *Data Units* são **células de informação viva**.  
Elas não representam apenas *dados brutos*, mas **dados contextualizados** —  
pequenos fragmentos de conhecimento que a IA pode usar em diferentes raciocínios.

📖 **Analogia:**
> *Se os prompts são pensamentos, as data units são as memórias que os sustentam.*

Cada unidade é projetada para:
- Ser **autoexplicativa e independente**  
- Poder ser **combinada** em moléculas (coleções de dados relacionados)  
- Ser **versionada e validada** como parte do conhecimento do sistema  

---

## 🧩 Estrutura do Diretório

```

data_units/
├── texts/
│   ├── ethics_in_ai.json       # Contexto textual temático
│   ├── embeddings_sample.npy   # Vetores pré-calculados
│   └── dataset_metadata.yaml   # Metadados descritivos
├── knowledge/
│   ├── glossary_terms.yaml     # Vocabulário técnico
│   ├── reference_papers.yaml   # Referências acadêmicas
│   └── ontology_map.yaml       # Mapa conceitual
└── README.md

````

---

## 🧠 Tipos de Data Units

| Tipo | Descrição | Exemplo de Conteúdo |
|------|------------|--------------------|
| `text` | Fragmentos de texto curado (contextos, citações, trechos de manual) | `"A arquitetura atômica organiza funções em camadas evolutivas..."` |
| `embedding` | Representação vetorial do texto para busca semântica | `embeddings_sample.npy` |
| `ontology` | Estrutura conceitual que define relações entre termos | `"Organismo → composto de → Moléculas"` |
| `metadata` | Descrições de datasets ou fragmentos | autor, fonte, versão, validade |
| `reference` | Fontes de verdade (papers, artigos, links) | `"https://arxiv.org/abs/2401.XXXX"` |

---

## 📦 Exemplo 1 — Unidade Textual

📄 `data_units/texts/ethics_in_ai.json`

```json
{
  "id": "ethics_ai.v1",
  "topic": "Ética em Inteligência Artificial",
  "language": "pt",
  "source": "Stanford HAI Papers (2023)",
  "content": "A ética em IA envolve princípios de transparência, responsabilidade e justiça algorítmica.",
  "tags": ["ética", "ia", "transparência", "responsabilidade"]
}
````

💬 Essa unidade pode ser injetada como contexto em um prompt modular:

```python
from atoms.logic.normalize_text import normalize_text
import json

with open("atoms/data_units/texts/ethics_in_ai.json", "r", encoding="utf-8") as f:
    ethics_data = json.load(f)

context = normalize_text(ethics_data["content"])
```

---

## 📦 Exemplo 2 — Ontologia Conceitual

📄 `data_units/knowledge/ontology_map.yaml`

```yaml
id: ontology.architecture.atomic
description: "Relações conceituais dentro da arquitetura atômica."
nodes:
  - Atom
  - Molecule
  - Organism
  - Template
  - Experience
relations:
  - { from: "Atom", to: "Molecule", type: "compose" }
  - { from: "Molecule", to: "Organism", type: "aggregate" }
  - { from: "Organism", to: "Template", type: "structure" }
  - { from: "Template", to: "Experience", type: "deliver" }
```

🔗 Essa ontologia pode ser usada para **mapear fluxos conceituais** dentro de pipelines de IA explicável.

---

## ⚙️ Integração Atômica

| Tipo de Átomo  | Função Relacionada                                       | Exemplo                                            |
| -------------- | -------------------------------------------------------- | -------------------------------------------------- |
| `logic`        | Pré-processar e normalizar texto ou metadados            | `normalize_text(data["content"])`                  |
| `prompt_units` | Injetar contexto dentro de uma persona ou raciocínio     | `prompt.replace("{{ context }}", data["content"])` |
| `ui_atoms`     | Permitir ao usuário selecionar o conjunto de dados usado | dropdown → seleciona `ethics_in_ai.json`           |

---

## 📘 Blueprint de Criação de Data Units

Cada unidade deve conter (em JSON ou YAML):

| Campo      | Tipo   | Descrição                                 |
| ---------- | ------ | ----------------------------------------- |
| `id`       | string | Identificador único (`categoria.nome.v#`) |
| `topic`    | string | Tema ou escopo semântico                  |
| `language` | string | Idioma do conteúdo                        |
| `source`   | string | Origem (paper, dataset, autor)            |
| `content`  | string | Texto ou representação semântica          |
| `tags`     | list   | Palavras-chave de classificação           |

📁 **Recomendado:** manter arquivos leves, ≤ 5 KB cada, para modularidade e versionamento granular.

---

## 🧪 Exemplo de Uso Integrado

```python
import json, yaml
from atoms.logic.vector_distance import vector_distance

# Carrega contexto
with open("atoms/data_units/texts/ethics_in_ai.json", "r") as f:
    ethics = json.load(f)

# Carrega ontologia
with open("atoms/data_units/knowledge/ontology_map.yaml", "r") as f:
    ontology = yaml.safe_load(f)

# Exemplo simbólico de relação
print(f"O conceito '{ontology['relations'][0]['from']}' compõe '{ontology['relations'][0]['to']}'.")

# Simula busca semântica (vetores hipotéticos)
distance = vector_distance([0.2, 0.4, 0.6], [0.1, 0.5, 0.6])
print(f"Distância semântica entre fragmentos: {distance:.3f}")
```

---

## 🧾 Metadados (`meta.yaml`)

```yaml
meta:
  id: data_units.v1
  author: "Mia Framework Lab"
  version: 1.0
  description: "Unidades modulares de dados e contexto cognitivo."
  schema:
    fields: ["id", "topic", "language", "source", "content", "tags"]
  standards:
    - "Os dados devem ser interpretáveis e reusáveis."
    - "Cada fragmento deve conter contexto mínimo e identificável."
```

---

## 📚 Boas Práticas

✅ **Curadoria** — mantenha fontes verificadas e atualizadas.
✅ **Granularidade** — prefira microfragmentos bem definidos a datasets monolíticos.
✅ **Versionamento** — trate cada unidade como um *snapshot de conhecimento*.
✅ **Semântica Viva** — permita que as data units sejam consultadas e evoluídas com o uso do usuário.

---

## ✨ Ideia Central

> “Cada data unit é uma célula de conhecimento,
> que, combinada com pensamento e forma,
> gera consciência digital contextual.”

As *data_units* são o **substrato cognitivo** da arquitetura atômica.
Elas conectam a IA ao seu contexto, permitindo **aprendizado incremental, privado e local**.

---

**📄 Última atualização:** 2025-11-11
**Versão:** 1.0
**Status:** 🟢 Estável
**Autor:** Mia Framework Lab

```
 atômica (UX local, dashboards, visualizações)?
```
