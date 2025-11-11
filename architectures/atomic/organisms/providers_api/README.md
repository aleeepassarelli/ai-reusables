# README: Camada 3 - Provedores de API (`providers_api/`)

Este diretório contém os "Adaptadores" (Adapters) para se conectar a **serviços de IA externos e APIs de terceiros**.

Enquanto os `local_agents/` rodam modelos no seu `docker-compose` (Ollama), os `providers_api/` rodam modelos na nuvem (OpenAI, Google, Anthropic, Dashscope, etc.), conforme definido no `requirements.txt`.

## 🧠 Papel na Arquitetura

Cada script Python neste diretório atua como um "tradutor" padronizado.

Por exemplo, o `atomic_engine` não deve se importar se está chamando o `Qwen (Dashscope)` ou o `GPT-4 (OpenAI)`. Ele simplesmente chama o `agent_vision.yaml`, que por sua vez usa um adaptador deste diretório (ex: `dashscope_provider.py`).

Isso nos permite trocar os provedores de nuvem sem quebrar o motor central.

## 🔐 Gerenciamento de Chaves (API Keys)

Este é um ponto crítico de segurança.

**NÃO COLOQUE ARQUIVOS `.env` OU CHAVES DE API NESTE DIRETÓRIO.**

As chaves de API (API Keys) devem ser gerenciadas de forma segura:

1.  **Arquivo `.env` (na Raiz):** Crie um arquivo chamado `.env` na **raiz principal** do projeto (ao lado do `docker-compose.yml`).
2.  **`.gitignore` (na Raiz):** Certifique-se de que o arquivo `.gitignore` (na raiz) contenha a linha `.env` para que suas chaves **nunca** sejam enviadas para o GitHub.
3.  **Carregamento:** Os scripts Python neste diretório (ex: `openai_provider.py`) usarão bibliotecas como `python-dotenv` para carregar as chaves do arquivo `.env` da raiz.

### Exemplo: `.env.example`

Para ajudar os contribuidores, podemos criar um arquivo `.env.example` (na raiz) com este formato:

```ini
# .env.example (Arquivo de Exemplo na Raiz do Projeto)

# Provedores da Camada 3 (Organisms)
OPENAI_API_KEY="sk-..."
GOOGLE_API_KEY="AIza..."
DASHSCOPE_API_KEY="sk-..."
ANTHROPIC_API_KEY="..."

# Banco de Dados da Camada 1 (Atoms)
NEO4J_PASSWORD="sua-senha-segura-aqui"
