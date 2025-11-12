## 🧱 Visão Geral

Cada **célula** representa um microserviço independente e completo.  
Ela segue uma estrutura modular em **camadas funcionais**, que se comunicam de forma controlada.

---

## 🔹 1. Diagrama das Camadas

```mermaid
graph TD
A[📡 Presentation Layer] --> B[⚙️ Business Logic Layer]
B --> C[🗄️ Data Access Layer]
C --> D[🧠 Memory Layer]
D --> E[📊 Monitoring & Metrics]
````

---

## 🔹 2. Descrição das Camadas

| Camada                   | Função                                                                                                            | Exemplos de Implementação                   |
| ------------------------ | ----------------------------------------------------------------------------------------------------------------- | ------------------------------------------- |
| **Presentation Layer**   | Responsável pela interface de comunicação com o mundo externo. Expõe endpoints REST/GraphQL e valida requisições. | FastAPI, Flask, GraphQL, API Gateway        |
| **Business Logic Layer** | Contém as regras de negócio específicas da célula. Processa dados, aplica validações e coordena fluxos.           | Pydantic Models, Service Classes, Use Cases |
| **Data Access Layer**    | Realiza operações diretas de persistência e consulta de dados.                                                    | PostgreSQL, Redis, Neo4j, AsyncPG           |
| **Memory Layer**         | Armazena e recupera vetores semânticos ou grafos relacionais. Pode integrar motores de IA.                        | Zep, Qdrant, Graphiti-Core                  |
| **Monitoring & Metrics** | Coleta e expõe métricas de performance, logs e health checks.                                                     | Prometheus, Grafana, OpenTelemetry          |

---

## 🔹 3. Fluxo Interno

```mermaid
sequenceDiagram
participant Client as 👩‍💻 Usuário / API Caller
participant Presentation as 📡 Presentation Layer
participant Business as ⚙️ Business Logic
participant Data as 🗄️ Data Access
participant Memory as 🧠 Memory
participant Monitor as 📊 Monitoramento

Client->>Presentation: Envia requisição HTTP (POST /users)
Presentation->>Business: Valida e encaminha payload
Business->>Data: Consulta ou grava em banco relacional
Business->>Memory: Armazena contexto semântico (opcional)
Data-->>Business: Retorna resultado
Business-->>Presentation: Monta resposta formatada
Presentation-->>Client: Retorna resposta JSON (200 OK)
Business-->>Monitor: Atualiza métricas de execução
```

---

## 🔹 4. Ciclo de Vida de uma Célula

1. **Inicialização** — carregamento de variáveis, dependências e registro no roteador.
2. **Operação** — recebe e processa requisições de forma isolada.
3. **Monitoramento** — coleta métricas e envia ao painel central.
4. **Escalonamento** — o *Cell Controller* pode replicar, pausar ou substituir a célula.

---

## 🔹 5. Princípios Arquiteturais

| Princípio                     | Descrição                                                           |
| ----------------------------- | ------------------------------------------------------------------- |
| **Isolamento Funcional**      | Cada célula opera de forma autônoma, evitando dependências diretas. |
| **Reusabilidade Modular**     | As camadas podem ser extraídas e aplicadas em outros contextos.     |
| **Escalabilidade Horizontal** | Novas instâncias podem ser criadas sem reconfigurar o núcleo.       |
| **Observabilidade Integrada** | Cada célula reporta seu próprio estado e performance.               |
| **Fail-Safe Design**          | Uma célula pode falhar sem comprometer o restante do sistema.       |

---

## 🔹 6. Estrutura de Pastas Recomendada

```bash
/microservice-example
│
├── /presentation        # Endpoints REST / GraphQL
│   ├── routes/
│   └── validators/
│
├── /business            # Regras de negócio e casos de uso
│   ├── services/
│   └── models/
│
├── /data_access         # Repositórios e persistência
│   ├── repositories/
│   └── schemas/
│
├── /memory              # Integração com bancos vetoriais e de grafo
│   ├── adapters/
│   └── embeddings/
│
└── /monitoring          # Métricas, health checks e logs
    ├── metrics.py
    └── healthcheck.py
```

---

## 🔹 7. Integrações de IA (Opcional)

Células podem incluir recursos **AI-Ready** do repositório principal:

```python
from core_engineering.prompt_modular import PromptBuilder
from core_engineering.scheme_traductor import SchemeAdapter
```

Exemplo de uso:

```python
prompt = PromptBuilder()
prompt.add("context/school.yaml")
prompt.add("persona/teacher.yaml")

final_prompt = prompt.build()
```

---

## 🔹 8. Métricas e Health Checks

| Tipo             | Endpoint   | Exemplo de Retorno                       |
| ---------------- | ---------- | ---------------------------------------- |
| **Health Check** | `/health`  | `{ "status": "ok", "uptime": "3h 22m" }` |
| **Metrics**      | `/metrics` | Prometheus-format data                   |
| **Logs**         | `/logs`    | JSON estruturado, nível INFO/ERROR       |

---

## 🔹 9. Benefícios Educacionais

* Facilita o ensino de **microserviços**, **camadas**, e **observabilidade**.
* Permite que alunos **vejam o ciclo de vida completo** de uma célula em execução.
* Pode ser facilmente replicado em laboratórios com **Docker + FastAPI + Prometheus**.

---

## 📘 Referência Cruzada

* 📂 [`DOC/architecture_diagram.mmd`](architecture_diagram.mmd)
* 📄 [`README.md`](../README.md)
* ⚙️ [`cell-template/`](../cell-template/)

---

## 🧭 Autor e Licença

MIT License © 2025
Desenvolvido por **Alexandre Passarelli**
Parte integrante do projeto **AI Reusables Framework — Galáxias de Arquiteturas Educacionais**

```
```mermaid
%% include ./DOC/architecture_layers.mmd


