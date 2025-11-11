# README: Conector `api_mcp/` (A API Central de Dados)

Este diretório contém a implementação da **API MCP (Master Context Persistence)**.

Este componente é a **aplicação FastAPI** principal que serve como o **gateway unificado** para toda a camada de `atomos/`.

## 🧠 Papel na Arquitetura

O `api_mcp` é o "balcão de atendimento" da sua memória. Nenhum outro serviço (seja o `core/atomic_engine` ou o frontend `ux/web_interface`) deve falar diretamente com os bancos de dados. Eles devem **sempre** falar com esta API.

**Sua principal função é a abstração.**

* O **Frontend** não precisa saber se a "memória do chat" está no `Zep` ou no `Redis`. Ele apenas chama `GET /api/v1/memory`.
* O **Atomic Engine** não precisa saber como o grafo é estruturado no `Neo4j`. Ele apenas chama `POST /api/v1/graph/save_entity`.



## 🛠️ Implementação Técnica

Este diretório conterá o código-fonte do servidor **FastAPI** (conforme definido na "Stack A" e no `requirements.txt`).

Suas responsabilidades incluem:

1.  **Expor Endpoints:** Definir rotas (endpoints) RESTful (ex: `/api/v1/...`) para interagir com os dados.
2.  **Validar Dados:** Usar o `Pydantic` (da sua stack) para garantir que todos os dados que entram e saem da API estejam no formato correto.
3.  **Orquestrar Conexões:** Gerenciar os *drivers* e *clientes* (definidos no `atomic_engine` ou aqui) para:
    * `graphiti_neo4j/` (Memória Semântica)
    * `zep-python/` (Memória Episódica)
    * `pieces_app/` (Memória de Fragmentos)
    * `Redis` (Cache)
4.  **Segurança:** Lidar com autenticação e autorização (usando `python-jose` e `PyJWT` da sua stack) para proteger o acesso aos dados.
5.  **Métricas:** Expor um endpoint `/metrics` para o `Prometheus` (da sua stack) monitorar a saúde da API.
