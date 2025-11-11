# -----------------------------------------------------------------
# 🧩 Atomic Architecture - Motor de Orquestração
# core/atomic_engine.py
# -----------------------------------------------------------------

import yaml
import os
import json
import subprocess
import ollama
from neo4j import GraphDatabase
from redis import Redis
# Importar o cliente Zep (quando implementado)
# from zep_python import ZepClient 

# --- Constantes de Diretório (Baseado na sua estrutura) ---
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MOLECULES_DIR = os.path.join(BASE_DIR, "molecules")
ORGANISMS_DIR = os.path.join(BASE_DIR, "organisms")
TOOLS_DIR = os.path.join(os.path.join(ORGANISMS_DIR, "tools"))

class AtomicEngine:
    """
    O AtomicEngine (SLE Engine) é o orquestrador central.
    Ele não executa tarefas; ele lê 'Moléculas' (YAMLs de fluxo) e
    deleter 'Organismos' (Agentes) para executar cada passo.
    """

    def __init__(self):
        print("Iniciando o AtomicEngine...")
        # --- Conexão aos Serviços (Stack C) ---
        # Estes clientes são injetados ou iniciados aqui,
        # vindo do docker-compose.yml.
        
        # Conexão com Ollama (Camada 3)
        try:
            self.ollama_client = ollama.Client(host='http://localhost:11434')
            self.ollama_client.list() # Testa a conexão
            print("✅ Conectado ao Ollama.")
        except Exception as e:
            print(f"⚠️ Erro ao conectar ao Ollama: {e}. (Verifique se o docker-compose está rodando)")
            self.ollama_client = None

        # Conexão com Neo4j (Camada 1)
        try:
            self.neo4j_driver = GraphDatabase.driver(
                "bolt://localhost:7687", 
                auth=("neo4j", "sua-senha-segura-aqui") # (Use variáveis de ambiente!)
            )
            self.neo4j_driver.verify_connectivity()
            print("✅ Conectado ao Neo4j.")
        except Exception as e:
            print(f"⚠️ Erro ao conectar ao Neo4j: {e}.")
            self.neo4j_driver = None

        # Conexão com Redis (Camada 1)
        try:
            self.redis_client = Redis(host='localhost', port=6379, db=0, decode_responses=True)
            self.redis_client.ping()
            print("✅ Conectado ao Redis.")
        except Exception as e:
            print(f"⚠️ Erro ao conectar ao Redis: {e}.")
            self.redis_client = None

        # TODO: Conexão com Zep (Memória)
        # self.zep_client = ZepClient(base_url="http://localhost:8000") 

    def _load_yaml(self, filepath):
        """Carrega um arquivo YAML de forma segura."""
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                return yaml.safe_load(f)
        except FileNotFoundError:
            print(f"Erro: Arquivo YAML não encontrado em {filepath}")
            return None
        except yaml.YAMLError as e:
            print(f"Erro ao parsear YAML em {filepath}: {e}")
            return None

    def _load_molecule(self, chain_id: str):
        """Carrega a 'Molécula' (cadeia semântica) pelo ID."""
        filename = f"{chain_id}.yaml" # Ex: proc_matricula_001.yaml
        filepath = os.path.join(MOLECULES_DIR, filename)
        return self._load_yaml(filepath)

    def _load_organism(self, agent_name: str):
        """Carrega o 'Organismo' (agente) pelo nome do arquivo."""
        # Ex: agent_ocr.yaml
        filepath = os.path.join(ORGANISMS_DIR, agent_name)
        return self._load_yaml(filepath)

    def _resolve_input(self, input_data: any, context: dict):
        """
        Resolve referências de contexto (ex: "$.steps[0].output").
        Versão simplificada.
        """
        if isinstance(input_data, str) and input_data.startswith("$."):
            try:
                # Remove "$.", ex: "steps[0].output"
                key_path = input_data[2:]
                
                # Assume uma estrutura simples de acesso
                # TODO: Implementar um parser JSONPath real para robustez
                if "steps[0]" in key_path:
                    key = key_path.split('.')[-1]
                    return context['steps'][0][key]
                if "steps[1]" in key_path:
                    key = key_path.split('.')[-1]
                    return context['steps'][1][key]
                if "input_trigger" in key_path:
                    key = key_path.split('.')[-1]
                    return context['input_trigger'][key]
                    
            except Exception as e:
                print(f"Erro ao resolver contexto para '{input_data}': {e}")
                return None
        # Se não for uma referência, retorna o valor literal
        return input_data

    def run_chain(self, chain_id: str, trigger_input: dict):
        """
        Ponto de entrada principal. Executa uma cadeia semântica completa.
        """
        print(f"\n--- 🚀 EXECUTANDO CADEIA: {chain_id} ---")
        
        # 1. Carregar a Molécula (a "receita")
        molecule_config = self._load_molecule(chain_id)
        if not molecule_config:
            return {"error": f"Molécula {chain_id} não encontrada."}

        # 2. Inicializar o Contexto (a "memória" desta execução)
        context = {
            "input_trigger": trigger_input,
            "steps": [] # Armazena a saída de cada passo
        }

        # 3. Iterar e Executar os Passos
        for i, step_config in enumerate(molecule_config.get("steps", [])):
            agent_name = step_config.get("agent")
            print(f"\n--- PASSO {i+1}: {step_config.get('name')} (Agente: {agent_name}) ---")

            # 4. Carregar o Organismo (o "agente" do passo)
            agent_config = self._load_organism(agent_name)
            if not agent_config:
                return {"error": f"Organismo {agent_name} não encontrado."}

            # 5. Executar o Passo e Obter a Saída
            try:
                output = self._execute_step(step_config, agent_config, context)
                context["steps"].append(output)
            except Exception as e:
                error_msg = f"Falha no Passo {i+1} ({agent_name}): {e}"
                print(f"🛑 {error_msg}")
                return {"error": error_msg}

        # 6. Formatar o Relatório Final (Camada 4)
        print("--- ✅ CADEIA CONCLUÍDA ---")
        output_config = molecule_config.get("output_report", {})
        final_data = self._resolve_input(output_config.get("data"), context)
        
        return {
            "deliver_to": output_config.get("deliver_to"),
            "template": output_config.get("template"),
            "data": final_data
        }

    def _execute_step(self, step_config: dict, agent_config: dict, context: dict):
        """
        O Dispatcher.
        Verifica o 'tipo' de agente e chama a ferramenta correta.
        """
        agent_type = agent_config.get("type")
        
        # Resolve o input (pode vir do trigger ou de outro passo)
        input_data = self._resolve_input(step_config.get("input"), context)
        
        # --- Estratégia 1: Agente LLM (Ex: Mistral, Jan) ---
        if agent_type == "llm_chat":
            prompt = self._resolve_input(step_config.get("prompt"), context)
            full_prompt = f"{input_data}\n\n{prompt}"
            
            return self._run_llm_chat(
                model=agent_config.get("model"),
                system_prompt=agent_config.get("system_prompt"),
                user_prompt=full_prompt
            )

        # --- Estratégia 2: Ferramenta Interna (Ex: Salvar no Grafo) ---
        elif agent_type == "internal_tool":
            tool_name = agent_config.get("function_name")
            return self._run_internal_tool(tool_name, input_data)
            
        # --- Estratégia 3: Script Local (Ex: OCR, Análise) ---
        elif agent_type == "local_tool":
            script_path = os.path.join(TOOLS_DIR, agent_config.get("script_path"))
            return self._run_local_script(script_path, input_data)
            
        else:
            raise ValueError(f"Tipo de Agente desconhecido: {agent_type}")

    # --- Ferramentas de Execução ---

    def _run_llm_chat(self, model: str, system_prompt: str, user_prompt: str):
        """Chama o cliente Ollama."""
        print(f"Chamando LLM (Ollama): {model}")
        if not self.ollama_client:
            raise Exception("Cliente Ollama não está conectado.")
            
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ]
        
        response = self.ollama_client.chat(model=model, messages=messages)
        content = response['message']['content']
        
        # Tenta parsear JSON se a resposta parecer um JSON
        if content.strip().startswith('{') and content.strip().endswith('}'):
            try:
                return json.loads(content)
            except json.JSONDecodeError:
                return {"raw_text": content} # Retorna como texto se o JSON falhar
        
        return {"raw_text": content}

    def _run_internal_tool(self, tool_name: str, data: dict):
        """
        Chama ferramentas internas (Graphiti/Neo4j, Zep, Redis).
        Esta é a implementação da "Stack D" (Agente Root).
        """
        print(f"Chamando Ferramenta Interna: {tool_name}")
        
        if tool_name == "save_to_graph_db":
            if not self.neo4j_driver:
                raise Exception("Driver Neo4j não está conectado.")
            
            # (Lógica 'Graphiti' simplificada: salvar um nó)
            with self.neo4j_driver.session() as session:
                entity_type = data.get("params", {}).get("entity_type", "Document")
                primary_key = data.get("params", {}).get("primary_key")
                node_data = data.get("data", {})
                
                query = f"""
                MERGE (n:{entity_type} {{{primary_key}: $cpf_aluno}})
                SET n += $props
                RETURN n
                """
                
                props = {
                    "cpf_aluno": node_data.get(primary_key),
                    "props": node_data
                }
                
                result = session.run(query, props)
                node = result.single()[0]
                print(f"Nó salvo/atualizado no Neo4j: {node['cpf_aluno']}")
                return {"status": "success", "node_id": node.element_id}
        
        # TODO: Implementar chamadas para Zep (add_memory) e Redis (cache)
        
        else:
            raise ValueError(f"Ferramenta interna desconhecida: {tool_name}")

    def _run_local_script(self, script_path: str, input_data: any):
        """
        Executa um script Python em 'tools/' como um subprocesso.
        Isso isola dependências (ex: Nanonets-OCR).
        """
        print(f"Executando Script Local: {script_path}")
        
        # Passa dados via STDIN (serializado como JSON)
        input_json = json.dumps(input_data)
        
        try:
            # Garante que o script seja executado com o python do venv
            python_exec = os.path.join(os.path.dirname(BASE_DIR), "venv", "bin", "python")
            if not os.path.exists(python_exec):
                 python_exec = "python" # Fallback

            process = subprocess.run(
                [python_exec, script_path],
                input=input_json,
                text=True,
                capture_output=True,
                check=True,
                encoding='utf-8'
            )
            # A saída do script (STDOUT) deve ser um JSON
            return json.loads(process.stdout)
            
        except subprocess.CalledProcessError as e:
            print(f"Erro ao executar script: {e.stderr}")
            raise Exception(f"Falha no script {script_path}: {e.stderr}")
        except json.JSONDecodeError as e:
            raise Exception(f"Script {script_path} não retornou um JSON válido: {e}")
