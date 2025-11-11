# 🧩 Esqueleto de Pipeline (Guia de Criação de Moléculas)

Este documento é o guia prático para criar um novo arquivo `semantic_chain.yaml` (uma "Molécula").

Use este guia para garantir que sua nova automação siga os padrões de **Transparência Educacional** e seja compatível com o `AtomicEngine`.

---

## 1. 🎯 Objetivo (O "Porquê")

Antes de escrever o YAML, defina o objetivo em uma frase:

* **Exemplo Ruim:** "Um fluxo para coisas da escola."
* **Exemplo Bom:** "Processar Faturas de fornecedores: ler o PDF, extrair 'valor' e 'data', e salvar no Neo4j."

## 2. ⚛️ Átomos (Dados de Entrada)

Quais "ingredientes" (dados) este fluxo precisa?

* **Fonte:** O fluxo será iniciado (Trigger) por quem?
    * `[ ] web_interface` (ex: um upload de arquivo)
    * `[ ] cli_demo` (ex: um comando do desenvolvedor)
    * `[ ] api_call` (ex: outro serviço)
* **Payload:** Quais dados o gatilho deve fornecer?
    * `[ ] file_path` (um caminho para um arquivo local)
    * `[ ] text_input` (um campo de formulário)
    * `[ ] json_payload` (dados estruturados)

## 3. 🧬 Esqueleto (Skeleton-of-Thought)

Qual é a "espinha dorsal" lógica do seu fluxo? (Consulte o `sot_framework.md` para a teoria).

Use os **Arquétipos de Classe 5 ou 7** como inspiração.

* **Exemplo (Processar Fatura - Classe 5):**
    1.  `leitura_ocr`
    2.  `extracao_campos`
    3.  `validacao_dados` (ex: o valor é um número?)
    4.  `gravacao_banco`
    5.  `relatorio_final`

## 4. 🤖 Organismos (Agentes Necessários)

Com base no esqueleto, quais "chefs" (Agentes) você precisará orquestrar?

* **Exemplo (Processar Fatura):**
    * `etapa_1: leitura_ocr` -> **`agent_OCR.yaml`**
    * `etapa_2: extracao_campos` -> **`agent_text_struct.yaml`**
    * `etapa_3: validacao_dados` -> **`agent_assistant.yaml`** (para "pensar" sobre os dados)
    * `etapa_4: gravacao_banco` -> **`agent_mcp.yaml`** (para usar a ferramenta `save_to_graph_db`)
    * `etapa_5: relatorio_final` -> **`agent_assistant.yaml`**

## 5. 📋 A Receita (Molde YAML)

Copie o arquivo `molecules/semantic_chain.yaml` e renomeie-o (ex: `molecules/proc_fatura_001.yaml`).

Preencha as seções `input_trigger`, `sot`, `steps` e `output_report` com base nas definições que você fez acima.

### Checklist de Qualidade

* [ ] O `name` de cada `step` corresponde exatamente a um item do seu `sot.skeleton`?
* [ ] A `input` de um passo (ex: `$.steps[0].output`) corresponde à `output_variable` do passo anterior?
* [ ] O `output_report` está mapeando os dados corretos do contexto para o `report_template.md`?

---

> **Lembrete de Ouro:** Uma "Molécula" não faz o trabalho. Ela **apenas** orquestra os "Organismos" (Agentes) que fazem o trabalho. Se você precisar de uma nova *habilidade* (ex: "traduzir texto"), crie um novo *Agente* (ex: `agent_tradutor.yaml`) primeiro.
