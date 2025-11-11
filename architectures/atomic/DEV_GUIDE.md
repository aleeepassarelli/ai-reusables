# 📚 Guia do Desenvolvedor (Developer Guide)

Bem-vindo ao guia de desenvolvimento da **Atomic Architecture**. Este documento é para desenvolvedores que desejam executar o sistema localmente, entender o motor principal e criar novos agentes ou fluxos.

Este projeto não é um simples script Python. É uma **stack de microsserviços local**, composta por 3 partes principais:

1.  **Serviços de Infra (`docker-compose.yml`):** Os bancos de dados (Neo4j, Redis, Zep) e os modelos de IA (Ollama) que rodam em contêineres.
2.  **Backend (`/core`, `/atomos`, etc.):** Uma aplicação FastAPI que expõe a `api_mcp` e executa o `SLE Engine`.
3.  **Frontend (`/ux/web_interface/`):** Uma aplicação React (Vite) que consome a API do backend e renderiza o "Mapa Cognitivo".

---

## 1. Pré-requisitos

Para executar o ambiente de desenvolvimento completo, você precisará ter instalados:

* [Docker](https://www.docker.com/) e [Docker Compose](https://docs.docker.com/compose/) (Essencial)
* [Python 3.10+](https://www.python.org/) e `venv` (Para o Backend)
* [Node.js v18+](https://nodejs.org/) e `npm` (Para o Frontend)
* [Git](https://git-scm.com/)

---

## 2. 🚀 Quick Start: Rodando o Ambiente (3 Terminais)

Para colocar o sistema no ar, você precisará de 3 terminais abertos.

### Terminal 1: Iniciar os Serviços (Docker)

Esta é a "infra" do seu sistema: os bancos de dados, o cache e o servidor de IA.

1.  **Clone o repositório** (se ainda não o fez):
    ```bash
    git clone [https://github.com/aleeepassarelli/atomic-architecture.git](https://github.com/aleeepassarelli/atomic-architecture.git)
    cd atomic-architecture
    ```

2.  **Inicie os serviços base** (Neo4j, Redis):
    ```bash
    docker-compose up -d
    ```

3.  **(Opcional, mas recomendado)** Inicie os serviços de desenvolvimento (Ollama, Grafana):
    ```bash
    docker-compose --profile dev up -d
    ```

4.  **IMPORTANTE (Apenas 1ª vez):** Baixe o modelo de IA do `agent_mcp` no Ollama:
    ```bash
    docker exec -it atomic_ollama ollama pull janhq/jan-v1-4b
    ```

### Terminal 2: Iniciar o Backend (FastAPI)

Este é o "cérebro" que executa o `SLE Engine` e serve a `api_mcp`.

1.  **Crie e ative o ambiente virtual** (na raiz do projeto):
    ```bash
    python -m venv venv
    source venv/bin/activate  # macOS/Linux
    .\venv\Scripts\activate   # Windows
    ```

2.  **Instale as dependências** do Python:
    ```bash
    pip install -r requirements.txt
    ```

3.  **Inicie o servidor FastAPI:**
    (Este passo assume que seu entrypoint da API se chamará `main_api.py` dentro da pasta `core/`)
    ```bash
    # (Aguardando Fase 2 - Criação do core/main_api.py)
    # Exemplo de comando futuro:
    # uvicorn core.main_api:app --reload --port 8000
    ```

### Terminal 3: Iniciar o Frontend (React)

Esta é a interface visual onde você verá o "Mapa Cognitivo".

1.  **Navegue até o diretório** do frontend:
    ```bash
    cd ux/web_interface
    ```

2.  **Instale as dependências** do Node.js:
    ```bash
    npm install
    ```

3.  **Inicie o servidor de desenvolvimento** (Vite):
    ```bash
    npm run dev
    ```

### ✅ Sucesso!

Se tudo funcionou, você pode abrir:

* **Frontend (React):** `http://localhost:5173`
    * Você verá o `@xyflow` renderizando os agentes (do `App.tsx`).
    * O Vite (`vite.config.ts`) redirecionará as chamadas de API (ex: `/api/v1/...`) para o seu backend.
* **Backend (FastAPI):** `http://localhost:8000/docs`
    * Você verá a documentação interativa da sua `api_mcp`.
* **Neo4j (DB):** `http://localhost:7474`
* **Grafana (Métricas):** `http://localhost:3000`

---

## 3. ⚙️ O Fluxo de Trabalho do Desenvolvedor

Como criar uma nova automação (ex: "Processar Fatura")?

1.  **Definir a "Molécula" (Backend):**
    * Crie o arquivo `molecules/proc_fatura.yaml`.
    * Defina os `steps` (passos):
        * `step 1`: Chamar `agent_OCR.yaml` (input: arquivo).
        * `step 2`: Chamar `agent_text_struct.yaml` (input: texto, prompt: "Extraia 'valor' e 'data'").
        * `step 3`: Chamar `agent_mcp.yaml` (tool: `save_to_graph_db`).

2.  **Expor a "Molécula" na API (Backend):**
    * No `core/main_api.py`, crie um novo endpoint (ex: `POST /api/v1/faturas`).
    * Este endpoint deve chamar o `SLE Engine` e dizer a ele para **executar** a cadeia `proc_fatura`.

3.  **Criar a Interação (Frontend):**
    * Em `ux/web_interface/src/App.tsx` (ou um novo componente), adicione um formulário de upload.
    * Ao enviar o formulário, faça uma chamada `axios.post('/api/v1/faturas', formData)`.
    * Use o resultado para atualizar os nós no `@xyflow` ou mostrar um relatório.

## 4. O Coração: `core/sle_engine.py`

Este **não é** o servidor de API. Este é o **orquestrador** que o servidor de API chama.

O `SLE Engine` é um módulo Python que:
1.  Recebe uma ordem (ex: "Execute a cadeia `proc_matricula_001`").
2.  Carrega e parseia `molecules/proc_matricula_001.yaml`.
3.  Lê o `step 1` e carrega a config de `organisms/agent_OCR.yaml`.
4.  Chama a ferramenta do Agente OCR (ex: um script em `tools/` que se conecta ao Ollama/Nanonets).
5.  Pega a saída, passa para o `step 2`, e assim por diante.

## 5. Gerenciamento de Memória (Stack C)

* **`Zep` (`zep-python`):** É o seu serviço de memória conversacional. Use-o para armazenar o histórico de interações do agente (`agent_assistant`).
* **`Graphiti` (`graphiti-core`):** É o seu construtor de Grafos de Conhecimento. Use-o (via `agent_mcp`) para salvar fatos e entidades estruturadas (ex: "Aluno X" *está matriculado na* "Turma Y") no **Neo4j**.
* **`Qdrant` (`qdrant-client`):** É o seu banco de dados vetorial. Use-o para salvar *embeddings* de documentos ou imagens para busca de similaridade (`agent_vision`).
* **`Redis`:** Use para cache de alta velocidade (ex: sessões de usuário, resultados de API).
