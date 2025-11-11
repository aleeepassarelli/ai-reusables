#!/usr/bin/env python
# -----------------------------------------------------------------
# 🧩 Atomic Architecture - Ferramenta de Assistente
# organisms/tools/run_assistant.py
# -----------------------------------------------------------------
#
# Este script é uma "ferramenta local" executada pelo AtomicEngine.
# Ele é chamado pelo 'agent_assistant.yaml'.
#
# 1. Recebe um JSON do 'stdin' contendo o 'prompt'.
# 2. Chama o 'mistral:7b-instruct' (simulado) para executar a tarefa.
# 3. Imprime um JSON para o 'stdout'.
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
            
        if "prompt" not in input_data:
            raise ValueError(f"Chave 'prompt' ausente no input do stdin.")
        
        return input_data['prompt']
        
    except json.JSONDecodeError as e:
        print(f"Erro de JSON no stdin: {e}", file=sys.stderr)
        return None
    except ValueError as e:
        print(f"Erro de Valor no stdin: {e}", file=sys.stderr)
        return None

def perform_general_task(prompt: str):
    """
    Simula o 'mistral:7b-instruct' (via Ollama) executando a tarefa.
    
    Na implementação real, você usaria o cliente Ollama:
    
    client = ollama.Client(host='http://localhost:11434')
    response = client.chat(
        model='mistral:7b-instruct',
        messages=[
            {'role': 'system', 'content': 'Você é um assistente prestativo, rápido e conciso.'},
            {'role': 'user', 'content': prompt}
        ]
    )
    return response['message']['content']
    """
    
    # --- SIMULAÇÃO ---
    # Simula a resposta do Mistral baseada na tarefa
    prompt_lower = prompt.lower()
    
    if "resuma o texto a seguir" in prompt_lower:
        mock_response = "Este é um resumo simulado do texto fornecido. O Mistral 7B é eficiente em sumarização."
    
    # Simula o caso de uso 'proc_matricula_001.yaml' (Passo 5)
    elif "aluno" in prompt_lower and "processado com status" in prompt_lower:
        mock_response = "O aluno João da Silva foi processado e salvo com sucesso no banco de dados."
        
    elif "qual é a capital" in prompt_lower and "frança" in prompt_lower:
        mock_response = "A capital da França é Paris."
        
    else:
        mock_response = f"Esta é uma resposta genérica simulada do Mistral 7B para o prompt: '{prompt[:30]}...'"
                        
    return mock_response

def write_output_to_stdout(data: dict):
    """Envia o resultado para o stdout como uma string JSON."""
    try:
        json.dump(data, sys.stdout)
    except Exception as e:
        # Se falhar, envia um erro para o stderr
        print(json.dumps({"error": f"Falha ao serializar saída: {e}"}), file=sys.stderr)

def main():
    prompt = read_input_from_stdin()
    
    if prompt is None:
        write_output_to_stdout({"error": "Falha ao ler o 'prompt' do stdin."})
        sys.exit(1)

    try:
        # 2. Executa a tarefa do assistente
        generated_text = perform_general_task(prompt)
        
        # 3. Prepara a saída (conforme esperado pelo 'atomic_engine')
        # A 'output_variable' era 'summary_text' ou similar
        output_data = {
            "raw_text": generated_text,
            "original_prompt": prompt,
            "model": "mistral:7b-instruct (simulado)"
        }
        
        # 4. Envia o JSON para o stdout
        write_output_to_stdout(output_data)
        
    except Exception as e:
        write_output_to_stdout({"error": f"Erro durante a tarefa do assistente: {e}"})
        sys.exit(1)

if __name__ == "__main__":
    main()
