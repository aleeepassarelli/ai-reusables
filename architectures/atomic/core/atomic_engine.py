# -----------------------------------------------------------------
# 🧩 Atomic Architecture - Motor de Orquestração (REFATORADO)
# core/atomic_engine.py
# -----------------------------------------------------------------

import yaml
import os
import json
import subprocess
import ollama
from neo4j import GraphDatabase
from redis import Redis

# --- Importações da Galáxia (AI Reusables Framework) ---
# (Assumindo que 'ai_reusables' está no PYTHONPATH)
try:
    from ai_reusables.core_engineering.prompt_modular import PromptBuilder
    from ai_reusables.core_engineering.scheme_traductor import SchemeAdapter
    FRAMEWORK_INTEGRADO = True
except ImportError:
    print("⚠️ Framework 'ai_reusables' não encontrado. Rodando em modo de simulação.")
    FRAMEWORK_INTEGRADO = False

# --- Constantes de Diretório (Baseado na sua estrutura) ---
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MOLECULES_DIR = os.path.join(BASE_DIR, "molecules")
ORGANISMS_DIR = os.path.join(BASE_DIR, "organisms")
TOOLS_DIR = os.path.join(os.path.join(ORGANISMS_DIR, "tools"))

class AtomicEngine:
    """
    O AtomicEngine (SLE Engine) é o orquestrador central.
    Ele lê 'Moléculas' (YAMLs de fluxo) e delega a 'Organismos' (Agentes).
    Esta versão é integrada ao AI Reusables Framework.
    """

    def __init__(self):
        print("Iniciando o AtomicEngine...")
        # --- Conexões (Ollama, Neo4j, Redis) ---
        # (O código de conexão existente vai aqui... omitido por brevidade)
        # ...
        try:
            self.ollama_client = ollama.Client(host='http://localhost:11434')
            self.ollama_client.list()
            print("✅ Conectado ao Ollama.")
        except Exception as e:
            self.ollama_client = None
            print(f"⚠️ Erro ao conectar ao Ollama: {e}.")
        # ... (Neo4j e Redis) ...

        # --- Inicializa os Módulos da Galáxia ---
        if FRAMEWORK_INTEGRADO:
            PROMPT_MODULES_PATH = os.path.join(BASE_DIR, "../core_engineering/prompt_modular")
            self.prompt_builder = PromptBuilder(base_path=PROMPT_MODULES_PATH)
            self.scheme_adapter = SchemeAdapter()
            print("✅ Framework (PromptBuilder, SchemeAdapter) integrado.")
        else:
            self.prompt_builder = None
            self.scheme_adapter = None
            print("⚠️ Framework NÃO integrado. Funcionalidade limitada.")

    # ... _load_yaml, _load_molecule, _load_organism ...
    # (Estas funções permanecem as mesmas)

    # ... _resolve_input ...
    # (Esta função permanece a mesma)

    # ... run_chain ...
    # (Esta função permanece a mesma)

    def _execute_step(self, step_config: dict, agent_config: dict, context: dict):
        """
        O Dispatcher.
        Verifica o 'tipo' de agente e chama a ferramenta correta.
        (Refatorado para simplicidade)
        """
        agent_type = agent_config.get("type")
        
        # Resolve o input (pode vir do trigger ou de outro passo)
        input_data = self._resolve_input(step_config.get("input"), context)
        
        # --- Estratégia 1: Agente LLM (Refatorado) ---
        if agent_type == "llm_chat":
            step_prompt = self._resolve_input(step_config.get("prompt"), context)
            
            return self._run_llm_chat(
                agent_config=agent_config,
                step_prompt=step_prompt,
                context_data=input_data # Passa o contexto resolvido
            )

        # --- Estratégia 2: Ferramenta Interna (Agente MCP) ---
        elif agent_type == "internal_tool":
            tool_name = agent_config.get("function_name") # Ex: "save_to_graph_db"
            return self._run_internal_tool(tool_name, input_data)
            
        # --- Estratégia 3: Script Local (Apenas para ferramentas reais, ex: OCR) ---
        elif agent_type == "local_tool":
            script_path = os.path.join(TOOLS_DIR, agent_config["local_tool_config"]["script_path"])
            return self._run_local_script(script_path, input_data)
            
        else:
            raise ValueError(f"Tipo de Agente desconhecido: {agent_type}")

    # --- Ferramentas de Execução (REFATORADAS) ---

    def _run_llm_chat(self, agent_config: dict, step_prompt: str, context_data: any):
        """
        Chama o cliente Ollama, mas agora usando
        o PromptBuilder e o SchemeAdapter do Framework.
        """
        model = agent_config["llm_config"]["model"]
        print(f"Chamando LLM (Ollama): {model}")
        if not self.ollama_client:
            raise Exception("Cliente Ollama não está conectado.")
            
        # 1. Construir o System Prompt (Refatoração 2: PromptBuilder)
        if self.prompt_builder and "prompt_modules" in agent_config:
            modules = agent_config["prompt_modules"] # Ex: ['persona/expert.yaml', 'format/json.yaml']
            system_prompt = self.prompt_builder.build(modules)
        else:
            # Fallback para o método antigo se o framework não for encontrado
            system_prompt = agent_config["llm_config"].get("system_prompt", "Você é um assistente prestativo.")

        # 2. Construir o User Prompt (combinando prompt do passo e contexto)
        # O 'context_data' é o output do passo anterior (ex: o markdown do OCR)
        # O 'step_prompt' é a instrução do 'molecules/*.yaml'
        user_prompt = f"Contexto para analisar:\n---\n{context_data}\n---\n\nTarefa:\n{step_prompt}"
        
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ]
        
        response = self.ollama_client.chat(model=model, messages=messages)
        content = response['message']['content']
        
        # 3. Forçar o Esquema (Refatoração 3: SchemeAdapter)
        output_schema = agent_config.get("output_schema", "text")
        
        if output_schema == "json" and self.scheme_adapter:
            # Usa o 'SchemeAdapter' para limpar e validar o JSON
            return self.scheme_adapter.map_schema_from_text(content)
        
        # Fallback se o 'SchemeAdapter' falhar ou não for JSON
        if output_schema == "json" and (content.strip().startswith('{') or content.strip().startswith('[')):
             try:
                return json.loads(content)
             except json.JSONDecodeError:
                pass # Cai para o raw_text
                
        return {"raw_text": content}

    # ... _run_internal_tool ...
    # (Esta função permanece a mesma)

    # ... _run_local_script ...
    # (Esta função permanece a mesma)
