# README: Camada 1 - Átomos de Dados (`atomos/`)

Este diretório é o "Núcleo de Memória" (Memory Core) da **Atomic Architecture**. Ele não armazena os dados em si (eles vivem nos contêineres Docker), mas contém a *lógica de conexão* para acessar, salvar e consultar informações.

Esta camada fornece os "ingredientes" brutos que as "Moléculas" (fluxos) e os "Organismos" (agentes) irão consumir.

A estratégia de memória é baseada em um "cérebro duplo":

1.  **Memória Semântica (Fatos):** `Neo4j` + `Graphiti`
2.  **Memória Episódica (História):** `Zep`
3.  **Memória de Fragmentos (Notas):** `Pieces.app`

---

## 1. `graphiti_neo4j/` (A Memória Semântica)

* **Serviço:** `neo4j:5.26` (definido no `docker-compose.yml`)
* **Biblioteca:** `graphiti-core` (definida no `requirements.txt`)

Este é o banco de dados de **fatos estruturados**. Quando um agente (como o `agent_text_struct`) extrai informações de um documento (ex: "Aluno: João", "CPF: 123"), o `agent_mcp` usa o `graphiti-core` para salvar esses dados como um **Grafo de Conhecimento (Knowledge Graph)** no Neo4j.

Isso nos permite fazer perguntas complexas, como: "Quais alunos estão matriculados em turmas que o Professor Silva ensina?"

## 2. `zep-python/` (A Memória Episódica)

* **Serviço:** (O Zep pode rodar como um serviço Docker ou ser gerenciado via PostgreSQL/Qdrant)
* **Biblioteca:** `zep-python` (definida no `requirements.txt`)

Este é o banco de dados de **histórico de conversas**. O Zep automaticamente armazena, sumariza e vetoriza as interações dos agentes (`agent_assistant`).

Se um usuário disser "Lembre-se deste documento", o Zep armazena. Dez minutos depois, se o usuário perguntar "O que eu pedi para você lembrar?", o Zep recupera esse contexto.

## 3. `pieces_app/` (A Memória de Fragmentos)

* **Serviço:** Externo (aplicativo de desktop).

O Pieces é um "bloco de notas" local (on-device) que captura fragmentos de código, capturas de tela e notas. A `api_mcp` se conectará à API local do Pieces para salvar ou buscar "fragmentos" de conhecimento que ainda não estão formalizados no Neo4j.

## 4. `api_mcp/` (O Gateway da Memória)

Este é o **ponto de entrada unificado** para a camada de dados. É a aplicação **FastAPI** que o `core/atomic_engine.py` e o frontend (`ux/web_interface`) consomem.

A `api_mcp` expõe endpoints (ex: `/api/v1/graph`, `/api/v1/memory`) que, por sua vez, sabem como consultar o Neo4j, o Zep e o Pieces. Isso desacopla o resto da arquitetura de ter que saber *onde* os dados estão armazenados.
