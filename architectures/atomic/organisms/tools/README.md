# README: Camada 3 - Ferramentas (`tools/`)

Este diretório é o "cinto de utilidades" executável para todos os Agentes (Organismos).

Aqui é onde **construímos as ferramentas** que tornam a arquitetura operante, exatamente como você descreveu: plugins, scripts de automação, conectores para serviços externos, APIs e MCPs externos.

## 🧠 Papel na Arquitetura: As "Mãos" dos Agentes

Este diretório contém os **scripts Python executáveis** que o `AtomicEngine` chama.

* Os `.yaml` em `organisms/` definem *o quê* um agente faz (sua missão).
* Os `.py` em `organisms/tools/` definem *como* ele faz (a habilidade).

Esta é a implementação da **"Pilha D" (Agente Root)**: o `agent_mcp` (o Agente Root) usa sua capacidade de "Function Calling" (Chamada de Função) para invocar as ferramentas definidas aqui.

## 🛠️ O que vai aqui?

Este diretório armazena dois tipos principais de ferramentas que o `AtomicEngine` utiliza:

### 1. Scripts Locais (para `type: "local_tool"`)

Estes são scripts Python isolados que executam tarefas complexas que um LLM não pode. O `AtomicEngine` os executa com segurança via subprocesso.

**Exemplos:**
* **`run_ocr.py`:** Um script que recebe um caminho de arquivo, usa a biblioteca `nanonets` para processá-lo e imprime o Markdown resultante (em JSON) para o `stdout`.
* **`run_vision_analysis.py`:** Um script que usa o `dashscope_provider.py` (de `providers_api/`) para enviar uma imagem ao Qwen-VL e retorna a análise.
* **`run_code_test.py`:** Um script que recebe um bloco de código do `agent_code`, o salva em um arquivo temporário, executa um `pytest` e retorna o resultado do teste.

### 2. Ferramentas Internas (para `type: "internal_tool"`)

Esta é a "API interna" do `AtomicEngine`, usada principalmente pelo `agent_mcp`.

Embora o *código* dessas ferramentas (como `_run_internal_tool`) possa viver no `core/atomic_engine.py` por eficiência, sua *lógica* e *propósito* pertencem a este diretório.

**Exemplos:**
* **`save_to_graph_db`:** A função que o `agent_mcp` chama para interagir com o `Graphiti` e salvar no Neo4j.
* **`get_from_cache`:** A função que o `agent_mcp` chama para buscar dados do `Redis`.
* **`add_to_zep_memory`:** A função para adicionar contexto à memória `Zep`.

## ⚙️ Fluxo de Trabalho (Exemplo de OCR)

1.  **Molécula:** `proc_matricula_001.yaml` (em `molecules/`) define um passo `leitura_OCR`.
2.  **Cadeia:** O Passo 1 chama `agent_OCR.yaml`.
3.  **Organismo:** O `organisms/agent_OCR.yaml` é carregado. Ele tem `type: "local_tool"` e aponta para `script_path: "run_ocr.py"`.
4.  **Motor:** O `AtomicEngine` executa o script: **`organisms/tools/run_ocr.py`**.
5.  **Ferramenta:** O script `run_ocr.py` (aqui neste diretório) faz o trabalho, e o `AtomicEngine` captura sua saída.
