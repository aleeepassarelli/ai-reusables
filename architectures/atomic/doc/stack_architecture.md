# ⚙️ Atomic Architecture — Stack Architecture v1.1

> **Documento Técnico de Referência**
>  
> **Objetivo:** Mapear os pacotes da stack para suas respectivas camadas cognitivas  
> **Foco:** Estrutura modular e autônoma para pequenas empresas e escolas  
> **Status:** Estável (v1.1)
>  
> 📅 Última atualização: 2025-11-11

---

## 🧩 Visão Geral

A **Atomic Architecture** é uma estrutura modular baseada em camadas cognitivas.  
Cada camada da arquitetura (Atoms → Molecules → Organisms → Templates → Experience) é mapeada diretamente para componentes técnicos específicos da stack Python.

| Camada | Descrição | Função Cognitiva |
|---------|------------|------------------|
| **1. Atoms** | Dados e Memória | Estrutura fundamental — “o corpo” do sistema |
| **2. Molecules** | Regras e Fluxos | Lógica semântica — “as sinapses” |
| **3. Organisms** | Agentes e Execução | Autonomia e ação — “os neurônios ativos” |
| **4. Templates** | Moldes e Output | Estrutura estética e programática — “a forma” |
| **5. Experience** | Interação e Feedback | Interface humana — “a percepção” |

---

## ⚛️ 1. Atoms — Núcleo de Memória e Dados

> **Função:** Armazenar, relacionar e contextualizar informações.  
> Esta é a base da cognição: memória factual, relacional, vetorial e temporal.

| Biblioteca | Versão | Função | Camada |
|-------------|---------|---------|---------|
| `graphiti-core[google-genai,falkordb]` | 0.17.0 | Motor grafo-semântico (Knowledge Graphs dinâmicos) | 🧠 Memória Estrutural |
| `zep-python` | 1.8.0 | Memória conversacional e episódica | 🧠 Contexto de Diálogo |
| `neo4j` | 5.26.0 | Banco de grafos (entidades e relações) | 🧩 Base Estrutural |
| `asyncpg` | 0.29.0 | Driver PostgreSQL assíncrono | ⚙️ Persistência SQL |
| `psycopg2-binary` | 2.9.9 | Fallback PostgreSQL (sincrônico) | ⚙️ Backup |
| `redis` | 5.2.0 | Cache de sessão e fila de tarefas | ⚡ Tempo Real |
| `qdrant-client` | 1.12.0 | Banco vetorial (embeddings semânticos) | 🔍 Memória de Similaridade |

🔹 **Resultado Cognitivo:**  
Combinação entre **memória estrutural (Neo4j)** + **episódica (Zep)** + **vetorial (Qdrant)**  
→ formando o “hipocampo digital” do sistema.

---

## 🧬 2. Molecules — Estrutura Lógica e Fluxos Semânticos

> **Função:** Controlar as regras do pensamento.  
> Interpreta YAMLs, aplica esquemas, e valida dados para execução segura.

| Biblioteca | Versão | Função |
|-------------|---------|--------|
| `pydantic` | 2.10.0 | Modelagem de dados e validação |
| `jsonschema` | 4.23.0 | Validação de estruturas semânticas |
| `httpx` | 0.27.0 | I/O assíncrono entre agentes |
| `requests` | 2.32.3 | Fallback síncrono de API calls |
| `graphiti-core` | — | Motor de ligação entre contextos (semantic chain) |

🔹 **Resultado Cognitivo:**  
As “Moléculas” são as **receitas cognitivas** — blocos YAML como `semantic_chain.yaml` —  
que descrevem *como pensar*, *em que ordem*, e *com que regras*.

---

## 🧠 3. Organisms — Agentes e Ação Autônoma

> **Função:** Dar vida aos agentes especialistas (OCR, visão, código, etc.)  
> Cada organismo é pareado com um modelo otimizado.

| Biblioteca | Versão | Função |
|-------------|---------|--------|
| `openai` | 1.54.0 | Interface universal para modelos (OpenAI, Ollama, Jan) |
| `google-generativeai` | 0.8.0 | Suporte multimodal e linguagem-visual (Vision Agent) |
| `anthropic` | 0.39.0 | Lógica de linguagem avançada (CoT, SoT) |
| `dashscope` | 1.18.0 | SDK para modelos Qwen (visão, OCR) |
| `docker` | 7.1.0 | Execução isolada de ferramentas e agentes externos |

🔹 **Resultado Cognitivo:**  
Camada **agentic** da arquitetura — a *equipe digital*.  
Cada agente (`agent_*.yaml`) opera como um especialista:

- `agent_vision` → Análise visual (Qwen2.5-VL)  
- `agent_OCR` → Extração documental (Nanonets-OCR2)  
- `agent_code` → Engenharia de código (DeepSeek 16B)  
- `agent_text_struct` → Estruturação de dados (GPT-OSS 20B)  
- `agent_assistant` → Conversação geral (Mistral 7B)  
- `agent_mcp` → Orquestrador (Jan-v1-4B)

---

## 🧩 4. Templates — Moldes de Saída e Estruturas de Exibição

> **Função:** Padronizar e estetizar os resultados.  
> Aqui vivem os `report_template.md`, `output.yaml`, e `jinja2` renderers.

| Biblioteca | Função |
|-------------|--------|
| `jinja2` *(implícito)* | Renderização de relatórios e documentos Markdown |
| `markdown` *(implícito)* | Conversão de saídas estruturadas |
| `yaml` *(nativo)* | Definição declarativa de fluxos e layouts |

🔹 **Resultado Cognitivo:**  
A tradução da lógica interna em **artefatos tangíveis** — planilhas, relatórios, painéis, dashboards.  
O “esqueleto de pensamento” toma forma visível aqui (SoT → Template).

---

## 💡 5. Experience — Interação, Feedback e Observabilidade

> **Função:** Conectar o humano ao sistema e permitir introspecção cognitiva.

| Biblioteca | Versão | Função |
|-------------|---------|--------|
| `fastapi` | 0.115.0 | API gateway e camada de interação |
| `uvicorn[standard]` | 0.32.0 | Servidor ASGI assíncrono |
| `gunicorn` | 23.0.0 | Executor multiprocessos (produção) |
| `orjson` | 3.10.7 | Serialização ultrarrápida de dados |
| `watchfiles` | 0.24.0 | Hot reload e monitoramento de ciclo |
| `prometheus-client` | 0.21.0 | Métricas e telemetria (Grafana, observabilidade) |

🔹 **Resultado Cognitivo:**  
Interface entre **sistema e consciência**.  
Permite que a arquitetura observe seu próprio desempenho — uma forma de *autopercepção operacional*.

---

## 🔐 6. Segurança — Confiança e Privacidade Local

> **Função:** Garantir que a cognição local seja ética, segura e rastreável.

| Biblioteca | Versão | Função |
|-------------|---------|--------|
| `python-jose` | 3.3.0 | Criação e validação de tokens JWT |
| `PyJWT` | 2.9.0 | Autenticação e autorização |
| `cryptography` | 43.0.0 | Criptografia simétrica/assimétrica, chaves locais |

🔹 **Resultado Cognitivo:**  
Cada fluxo de pensamento (pipeline semântico) pode ser **autenticado** e **assinado**,  
garantindo confiabilidade e auditoria educacional ou empresarial.

---

## 🧭 7. Mapeamento Cognitivo Final

| Camada | Domínio | Tecnologias-Chave | Operações ELS Dominantes |
|---------|----------|------------------|---------------------------|
| 🩸 **Atoms** | Memória e Dados | Neo4j, Redis, Qdrant, Graphiti | RAG, Self-Refine |
| ⚛️ **Molecules** | Regras e Fluxos | Pydantic, JSONSchema | SoT, SCoT, DECOMP |
| 🧠 **Organisms** | Agentes e Ação | OpenAI, Dashscope, Anthropic | CoT, GoT, Tool Use |
| 🧩 **Templates** | Moldes de Saída | Jinja2, Markdown | Structured Output |
| 💡 **Experience** | Interação e UX | FastAPI, Prometheus | Feedback Loop |

---

## 🧱 Filosofia Técnica

> “Cada camada pensa, sente e age dentro de sua natureza.”

- **Local-first:** todos os componentes podem rodar offline, preservando dados locais.  
- **Modular:** cada agente, memória e template é intercambiável.  
- **Transparente:** cada ação é registrada e compreensível (sem caixas-pretas).  
- **Educacional:** o sistema pode ser usado como laboratório de IA distribuída.

---

## 📦 Estrutura Recomendada de Diretórios

