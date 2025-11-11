#!/usr/bin/env python
# -----------------------------------------------------------------
# 🧩 Atomic Architecture - Ferramenta de Código
# organisms/tools/run_code.py
# -----------------------------------------------------------------
#
# Este script é uma "ferramenta local" executada pelo AtomicEngine.
# Ele é chamado pelo 'agent_code.yaml' (type: "local_tool").
#
# 1. Recebe um JSON do 'stdin' (do engine) contendo a 'task_description'.
# 2. Chama o modelo DeepSeek Code (aqui simulado) para executar a tarefa.
# 3. Imprime um JSON para o 'stdout' (para o engine).
#
# -----------------------------------------------------------------

import sys
import json
import os

# Na implementação real, você importaria o cliente Ollama
# import ollama

def read_input_from_stdin():
    """Lê e parseia o JSON vindo do stdin."""
    try:
        input_data = json.loads(sys.stdin.read())
        
        if not isinstance(input_data, dict):
            raise ValueError("Input (stdin) não é um objeto JSON.")
            
        if "task_description" not in input_data:
            raise ValueError(f"Chave 'task_description' ausente no input do stdin.")
        
        return input_data['task_description']
        
    except json.JSONDecodeError as e:
        print(f"Erro de JSON no stdin: {e}", file=sys.stderr)
        return None
    except ValueError as e:
        print(f"Erro de Valor no stdin: {e}", file=sys.stderr)
        return None

def perform_code_generation(task_description: str):
    """
    Simula o 'deepseek code 16b' (via Ollama) executando a tarefa.
    
    Na implementação real, você usaria o cliente Ollama:
    
    client = ollama.Client(host='http://localhost:11434')
    response = client.chat(
        model='deepseek-coder:16b',
        messages=[
            {'role': 'system', 'content': 'Sua missão é gerar APENAS o bloco de código solicitado.'},
            {'role': 'user', 'content': task_description}
        ]
    )
    return response['message']['content']
    """
    
    # --- SIMULAÇÃO ---
    # Simula a resposta do DeepSeek baseada na tarefa
    task_lower = task_description.lower()
    
    if "função python" in task_lower and "somar" in task_lower:
        mock_code = """
```python
def somar(a: int, b: int) -> int:
    \"\"\"Soma dois números inteiros e retorna o resultado.\"\"\"
    return a + b
