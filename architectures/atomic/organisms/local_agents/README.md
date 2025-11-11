# README: Camada 3 - Agentes Locais (`local_agents/`)

Este diretório é o coração da filosofia de **"Autonomia Local"** da arquitetura.

Enquanto `providers_api/` lida com APIs de nuvem (OpenAI, Google), este diretório define os **Agentes (Organismos) que rodam 100% localmente** no seu hardware.

## 🛠️ Implementação Técnica: Ollama

Todos os agentes definidos aqui são projetados para rodar em um servidor de IA local.

1.  **O Servidor (`docker-compose.yml`):** O serviço `ollama` é o "host" que serve os modelos de IA (ex: `janhq/jan-v1-4b`, `mistral`, etc.).
2.  **O Cliente (`requirements.txt`):** O `AtomicEngine` usa a biblioteca `ollama` para se comunicar com o servidor.

Os arquivos `.yaml` (como `agent_ocr.yaml`) no diretório `organisms/` são os arquivos de *configuração* que dizem ao `AtomicEngine` qual modelo (`model: "mistral"`) e qual `system_prompt` (missão) usar ao chamar o cliente Ollama.

## 🧠 A Estratégia: "Mixture of Experts" (MoE)

Nós não usamos um único modelo gigante para tudo. Em vez disso, usamos uma **"Mistura de Especialistas"** (Mixture of Experts) em nível de arquitetura. Cada agente é um especialista otimizado para uma tarefa, criando um sistema mais eficiente, barato e poderoso.

Esta é a nossa "Equipe Digital" de especialistas:

---

### 👑 O Orquestrador (Agente Mestre)

Este é o agente mais importante da camada, o "cérebro" de roteamento.

* **Agente:** `agent_mcp.yaml`
* **Modelo:** `janhq/jan-v1-4b`
* **Função:** Orquestração (Master Context Persistence).
* **Análise:** Este modelo foi explicitamente **otimizado para raciocínio agêntico, planejamento e uso de ferramentas**. Ele entende a tarefa, consulta a `api_mcp/` (Camada 1) para obter contexto e, em seguida, **chama o especialista certo** (visão, código, OCR) para fazer o trabalho.

---

### 🤖 A Equipe de Especialistas (Delegados)

Estes são os agentes que o `agent_mcp` gerencia:

#### 1. O Documentarista (OCR Semântico)
* **Agente:** `agent_OCR.yaml`
* **Modelo:** `nanonets-OCR2 3b`
* **Função:** Leitura e Formatação de Documentos.
* **Análise:** Este modelo não faz apenas OCR; ele faz **OCR semântico**. Ele é treinado para interpretar, organizar e formatar documentos (PDFs, imagens) em **Markdown limpo e contextualizado**, entendendo tabelas, fórmulas (LaTeX) e imagens. Ele transforma documentos escaneados em dados estruturados.

#### 2. O Estruturador (Texto para JSON)
* **Agente:** `agent_text_struct.yaml`
* **Modelo:** `gpt-oss-20b` (Modelo MoE)
* **Função:** Produção e Análise Semântica.
* **Análise:** A principal característica deste modelo é o suporte a **"Structured Outputs" (Saídas Estruturadas)**. Enquanto o `agent_OCR` lida com *documentos*, este agente é o especialista em pegar texto não estruturado (como um parágrafo) e convertê-lo em formatos de dados limpos como **JSON** ou **YAML** seguindo instruções.

#### 3. O Vidente (Visão)
* **Agente:** `agent_vision.yaml`
* **Modelo:** `qwen 2.5 vision 8b`
* **Função:** Análise de Imagem Contextual.
* **Análise:** Um poderoso Modelo de Linguagem e Visão (VLM). É especializado em **reconhecimento de imagens, localização de objetos e OCR básico**. Este agente é o "olho" do sistema, capaz de entender o conteúdo visual.

#### 4. O Engenheiro (Código)
* **Agente:** `agent_code.yaml`
* **Modelo:** `deepseek code 16b` (Modelo MoE)
* **Função:** Refatoração e Geração de Código.
* **Análise:** Um modelo de Mistura de Especialistas (MoE) focado **puramente em tarefas de código**. É leve (para 16B) e tem desempenho de nível de produção para gerar, analisar e depurar código.

#### 5. O Assistente (Conversa)
* **Agente:** `agent_assistant.yaml`
* **Modelo:** `mistral:7b-instruct`
* **Função:** Assistente Geral.
* **Análise:** Famoso por ser um dos modelos mais **rápidos, eficientes e competentes** para conversação geral, resumo e resposta a perguntas. É o assistente de "linha de frente" para interações rápidas.
