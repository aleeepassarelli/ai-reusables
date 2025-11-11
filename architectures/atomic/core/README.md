# README: O Núcleo do Motor (`core/`)

Este diretório é o "motor" da **Atomic Architecture**. Ele contém o código Python que dá vida e executa toda a lógica definida nas outras pastas.

Enquanto as outras pastas (`atomos`, `molecules`, `organisms`) definem "o quê" (os dados e as regras), o `core/` define "o como" (a execução).

Este diretório contém os dois scripts mais importantes do projeto:

## 1. `atomic_engine.py` (O Orquestrador)

Este arquivo contém a classe `AtomicEngine`. Pense nele como o **"Motor de Execução"** ou o **"SLE Engine"** (Semantic Latent Engineering).

**Função Principal:**
Sua única responsabilidade é ler uma "Molécula" (um `semantic_chain.yaml`) e orquestrar os "Organismos" (agentes) para executar os passos definidos.

1.  Ele **carrega** o YAML da molécula.
2.  Ele **lê** o `sot.skeleton` (esqueleto) para entender a lógica.
3.  Ele **executa** os `steps` (passos) um por um.
4.  Para cada passo, ele **carrega** o YAML do agente (`organisms/`) correspondente.
5.  Ele **chama** a ferramenta correta (Ollama, um script em `tools/`, ou uma função interna como `save_to_graph_db`).
6.  Ele **gerencia o contexto**, passando a saída de um passo como entrada para o próximo.

Este script **não sabe** o que é uma API ou uma interface web. Ele apenas sabe como executar cadeias.

## 2. `main_api.py` (O Gateway da API)

Este arquivo é o **"Motor de Ignição"**. É o servidor **FastAPI** (a `api_mcp`) que "liga" o `atomic_engine`.

**Função Principal:**
Ele serve como a principal interface para o mundo exterior (como o frontend `ux/web_interface/`).

1.  Ele **importa e inicia** uma instância única do `AtomicEngine` quando o servidor sobe.
2.  Ele **expõe endpoints** HTTP (ex: `POST /api/v1/run_chain`).
3.  Ele **recebe requisições** do frontend (ex: o ID da cadeia e os dados de entrada).
4.  Ele **chama** a função `engine.run_chain(...)` para fazer o trabalho pesado.
5.  Ele **retorna** o resultado (o `output_report`) como uma resposta JSON para o frontend.
6.  Ele **expõe** o endpoint `/metrics` para o Prometheus monitorar a saúde do sistema.
