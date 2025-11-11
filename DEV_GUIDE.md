# 📚 Guia do Desenvolvedor (Developer Guide)

Bem-vindo ao guia de desenvolvimento da **Atomic Architecture**. Este documento é para desenvolvedores que desejam executar o sistema localmente, entender o motor principal e criar novos agentes ou fluxos.

## 1. Configuração do Ambiente

### Pré-requisitos
* [Python 3.10+](https://www.python.org/)
* [Git](https://git-scm.com/)
* (Recomendado) Um servidor local de modelos de IA, como [Ollama](https://ollama.com/)

### Passos de Instalação

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/aleeepassarelli/atomic-architecture.git](https://github.com/aleeepassarelli/atomic-architecture.git)
    cd atomic-architecture
    ```

2.  **Crie um Ambiente Virtual (Venv):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # macOS/Linux
    .\venv\Scripts\activate   # Windows
    ```

3.  **Instale as Dependências:**
    (Este arquivo será criado na Fase 1)
    ```bash
    pip install -r requirements.txt
    ```

## 2. 🤖 Configurando os Modelos Locais (Agentes)

Esta arquitetura é **local-first**. Os "Organismos" (Agentes) definidos em `3_organisms_agents/` são arquivos `.yaml` que apontam para modelos de IA.

Para que o sistema funcione, você precisa ter esses modelos servindo localmente. Recomendamos usar o [Ollama](https://ollama.com/) para facilitar este processo.

**Exemplo de Configuração:**

1.  **Instale o Ollama.**

2.  **Baixe os modelos** que usaremos (conforme nossa lista de agentes):
    ```bash
    ollama pull mistral           # Para agent_assistant.yaml
    ollama pull qwen:v2.5-8b      # Para agent_vision.yaml (exemplo)
    ollama pull deepseek-coder    # Para agent_code.yaml
    ```
    *(Nota: Modelos específicos como `nanonets-OCR2` ou `gpt-oss` podem exigir configuração manual ou scripts de inferência dedicados em `3_organisms_agents/tools/`).*

3.  Os arquivos `agent_*.yaml` serão pré-configurados para "procurar" por esses modelos no endpoint padrão do Ollama (`http://localhost:11434`).

## 3. ⚙️ O Fluxo de Trabalho Padrão

Seu ciclo de desenvolvimento para criar uma nova automação será:

**Passo 1: Criar/Editar um "Organismo" (Agente)**
* **Definição:** Um Agente é definido por seu arquivo de configuração `.yaml` em `3_organisms_agents/`.
* **Exemplo:** Você quer um agente que traduza textos.
* **Ação:**
    1.  Copie o `4_templates_forms/agent_template.yaml` para `3_organisms_agents/agent_tradutor.yaml`.
    2.  Edite o `agent_tradutor.yaml` para usar o modelo `mistral` (ou outro) com um *prompt de sistema* focado em tradução.
    3.  Se o agente precisar de uma lógica complexa (ex: chamar uma API externa), você pode adicionar um script Python em `3_organisms_agents/tools/` e referenciá-lo no YAML.

**Passo 2: Criar/Editar uma "Molécula" (Cadeia Semântica)**
* **Definição:** Uma Cadeia é o "roteiro" que o `SLE Engine` lê. Ela define quais agentes chamar em qual ordem.
* **Exemplo:** Você quer um fluxo que *lê um documento (OCR)* e depois o *traduz (Agente Tradutor)*.
* **Ação:**
    1.  Use o `2_molecules_action/pipeline_skeleton.md` como guia.
    2.  Crie um novo `traduzir_documento.yaml` em `2_molecules_action/`.
    3.  Defina os `steps`:
        * `step 1`: Chama `agent_OCR.yaml` (input: arquivo).
        * `step 2`: Chama `agent_tradutor.yaml` (input: a saída do step 1).

**Passo 3: Testar via CLI (Linha de Comando)**
* **Definição:** A `5_experience_ux/cli_demo/` será a principal ferramenta para testar suas cadeias.
* **Ação:**
    1.  Navegue até o diretório `5_experience_ux/cli_demo/`.
    2.  Execute o `main.py` (que conterá o `SLE Engine`) apontando para sua nova cadeia:
    ```bash
    # (Comando futuro - Fase 4)
    python main.py --chain "traduzir_documento" --input "/caminho/para/meu_doc.pdf"
    ```

## 4. O Coração: `core/sle_engine.py`

Toda a mágica acontece aqui. O `SLE Engine` é um script Python responsável por:

1.  **Ler** o arquivo `.yaml` da "Molécula" (Cadeia) solicitada.
2.  **Validar** os `steps` (passos).
3.  **Carregar** as configurações dos "Organismos" (Agentes) necessários para cada passo.
4.  **Executar** os passos em ordem, gerenciando o contexto (passando a saída de um passo como entrada para o próximo).
5.  **Chamar** as ferramentas corretas (seja uma chamada de API para o Ollama, seja um script local em `tools/`).

Ao desenvolver, seu foco principal será nos arquivos **YAML (Camadas 2 e 3)**, não em modificar o *core engine*.

## 5. Testes

(Esta seção será preenchida na Fase 5)

* Usaremos `pytest` para testes unitários do `SLE Engine`.
* Testes de integração verificarão cadeias completas (ex: `proc_matricula_001`).
