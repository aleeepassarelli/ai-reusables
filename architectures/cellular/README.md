# 🧬 Cellular Architecture — Sistemas Vivos e Escaláveis

> Uma arquitetura inspirada em **biologia**, projetada para criar **sistemas distribuídos**, **resilientes** e **educacionais**.  
> Cada célula é uma unidade autônoma que pensa, armazena, e se comunica com as outras.

---

## 🌱 1. CONCEITO

A **Cellular Architecture** nasce da ideia de que um sistema pode funcionar como um **organismo vivo**:  
composto por **células independentes**, cada uma com suas funções, mas colaborando em harmonia.

💡 **Analogia biológica:**
- 🧫 **Célula** → Microserviço completo (com seu banco, lógica e API)  
- 🧠 **Núcleo** → Regras de negócio local  
- 🧍 **Organismo** → O sistema escolar (ou qualquer aplicação)  
- 🕸️ **Rede neural** → O roteador celular, que conecta todas as células  

---

## 🧩 2. ESTRUTURA GERAL

```

/cellular-architecture
│
├── /cell-template                # Template base para infraestrutura
│   ├── main.tf                   # Terraform (ou CloudFormation)
│   ├── variables.tf
│   └── outputs.tf
│
├── /microservice-appointments    # Serviço de agendamentos (API FastAPI)
│   ├── /presentation
│   ├── /business
│   └── /data_access
│
├── /microservice-users           # Serviço de usuários (login, perfis)
│
└── /cell-router                  # Núcleo de roteamento e controle
├── router_config.yaml
└── deployment_script.sh

````

---

## ⚙️ 3. FLUXO CELULAR

Cada célula é **autônoma**, **reutilizável** e **isolada** — mas todas se comunicam via o **Cell Router**.

```mermaid
flowchart LR
A[Usuário 👩‍💻] -->|Request| B[🧭 Cell Router]
B -->|Regra A-M| C[🧫 Célula A]
B -->|Regra N-Z| D[🧫 Célula B]
C --> E[(Banco A)]
D --> F[(Banco B)]
B --> G[🧬 Painel de Controle]
````

* O **Cell Router** recebe as requisições e decide **qual célula** processará.
* Cada **célula** contém seu próprio banco e lógica, o que garante isolamento e resiliência.
* O **painel de controle** supervisiona o conjunto e pode clonar, pausar ou replicar células.

---

## 🧱 4. CAMADAS INTERNAS DE UMA CÉLULA

Cada célula segue uma estrutura modular:

```mermaid
graph TD
A[Apresentação] --> B[Lógica de Negócio]
B --> C[Acesso a Dados]
C --> D[Memória Local / Vetorial]
```

| Camada           | Função                                 | Exemplo                     |
| ---------------- | -------------------------------------- | --------------------------- |
| **Presentation** | API FastAPI (entrada de requisições)   | `/routes/appointments.py`   |
| **Business**     | Regras de negócio (validações, fluxos) | `/services/logic.py`        |
| **Data Access**  | Persistência de dados                  | `/repositories/postgres.py` |
| **Memory Layer** | Memória vetorial ou grafo              | `zep`, `qdrant`, `graphiti` |

---

## 🧩 5. STACK TECNOLÓGICA

| Nível               | Tecnologia                 | Descrição                           |
| ------------------- | -------------------------- | ----------------------------------- |
| **API Core**        | FastAPI, Uvicorn, Pydantic | Backend leve e assíncrono           |
| **Segurança**       | PyJWT, Cryptography, JOSE  | Tokens, autenticação e criptografia |
| **Memória e Grafo** | Graphiti-Core, Zep, Neo4j  | Persistência e raciocínio semântico |
| **Vetores**         | Qdrant                     | Armazenamento vetorial              |
| **Infraestrutura**  | Terraform, Docker          | Provisionamento e containers        |
| **Monitoramento**   | Prometheus, Grafana        | Observabilidade e métricas          |

---

## 🧠 6. COMO EXECUTAR

### 1️⃣ Clonar o Repositório

```bash
git clone https://github.com/seu-usuario/AI_Reusables_Framework.git
cd AI_Reusables_Framework/cellular-architecture
```

### 2️⃣ Subir Ambiente

```bash
docker-compose up --build
```

### 3️⃣ Rodar APIs Locais

```bash
cd microservice-users
uvicorn main:app --reload --port 8001

cd ../microservice-appointments
uvicorn main:app --reload --port 8002
```

### 4️⃣ Roteador Celular

```bash
cd cell-router
python main.py
```

---

## 🧬 7. COMO ESCALAR CÉLULAS

Você pode criar novas células clonando o `cell-template`:

```bash
cp -r cell-template microservice-inventory
```

E adicionando-a no roteador:

```yaml
# router_config.yaml
routes:
  users: http://localhost:8001
  appointments: http://localhost:8002
  inventory: http://localhost:8003
```

> ⚡ Cada nova célula é um novo mundo — independente, mas conectado.

---

## 🧩 8. PADRÕES REUTILIZÁVEIS (AI-READY)

Cada célula pode integrar **IA Reusables** diretamente do repositório principal:

```
from core_engineering.prompt_modular import PromptBuilder
from core_engineering.scheme_traductor import SchemeAdapter
```

📘 Exemplo:

```python
from core_engineering.prompt_modular import PromptBuilder

prompt = PromptBuilder()
prompt.add("persona/assistant.yaml")
prompt.add("format/json_output.yaml")

system_prompt = prompt.build()
```

---

## 🎓 9. CASO DE USO EDUCACIONAL

**Sistema Escolar Celular** — um protótipo didático de como aplicar a arquitetura.

| Célula                 | Função                | Escopo                |
| ---------------------- | --------------------- | --------------------- |
| **Célula A**           | Atende usuários A–M   | Banco + API isolada   |
| **Célula B**           | Atende usuários N–Z   | Banco + API isolada   |
| **Célula de Controle** | Gerencia o sistema    | Painel administrativo |
| **Cell Router**        | Direciona requisições | Load Balancer lógico  |

---

## 🔭 10. VISÃO FILOSÓFICA

> “Quando um sistema cresce demais, ele deixa de aprender.
> Quando se divide em células, ele começa a evoluir.”

A arquitetura celular permite:

* Escalabilidade orgânica 🌿
* Isolamento e resiliência 🔒
* Reuso e replicabilidade ♻️
* Educação e experimentação 💡

---

## 🔗 11. RECURSOS

* 📘 **Documentação:** `/DOC/cellular_architecture.md`
* 🧩 **Templates:** `/cell-template/`
* 🧠 **AI Reusables:** [AI Reusables Framework](../README.md)
* ⚙️ **Infraestrutura:** Terraform + Docker

---

## 🧭 12. LICENÇA E AUTORIA

MIT License © 2025
Desenvolvido por **Alexandre Passarelli**
🌐 Projeto: **AI Reusables Framework — Galáxias de Arquiteturas Educacionais**

```

---

Quer que eu gere também o **banner visual (ASCII + emoji + cores Markdown)** para o topo desse README — tipo uma *assinatura visual de arquitetura*, no estilo:

```

╔════════════════════════════════════╗
║   🧬 CELLULAR ARCHITECTURE v1.0    ║
║   Sistemas Vivos e Escaláveis      ║
╚════════════════════════════════════╝

```

Assim ele ganha identidade visual própria dentro do repositório principal (como se fosse um “selo biológico”). Deseja isso na versão final?
```
