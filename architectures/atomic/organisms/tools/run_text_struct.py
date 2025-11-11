#!/usr/bin/env python
# -----------------------------------------------------------------
# 🧩 Atomic Architecture - Ferramenta de Estruturação
# organisms/tools/run_text_struct.py
# -----------------------------------------------------------------
#
# Este script é uma "ferramenta local" executada pelo AtomicEngine.
# Ele é chamado pelo 'agent_text_struct.yaml' (type: "local_tool").
#
# 1. Recebe um JSON do 'stdin' contendo 'text_content' e 'prompt'.
# 2. Chama o 'gpt-oss-20b' (simulado) para forçar o texto no
#    formato JSON/YAML solicitado.
# 3. Imprime um JSON para o 'stdout'.
#
# -----------------------------------------------------------------

import sys
import json
import os
import re

# Na implementação real, você importaria o cliente Ollama
# import ollama

def read_input_from_stdin():
    """Lê e parseia o JSON vindo do stdin."""
    try:
        input_data = json.loads(sys.stdin.read())
        
        if not isinstance(input_data, dict):
            raise ValueError("Input (stdin) não é um objeto JSON.")
            
        required_keys = ['text_content', 'prompt']
        for key in required_keys:
            if key not in input_data:
                raise ValueError(f"Chave '{key}' ausente no input do stdin.")
        
        return input_data['text_content'], input_data['prompt']
        
    except json.JSONDecodeError as e:
        print(f"Erro de JSON no stdin: {e}", file=sys.stderr)
        return None, None
    except ValueError as e:
        print(f"Erro de Valor no stdin: {e}", file=sys.stderr)
        return None, None

def perform_text_structuring(text_content: str, prompt: str):
    """
    Simula o 'gpt-oss-20b' (via Ollama) executando a tarefa de
    saída estruturada.
    
    Na implementação real, você usaria o cliente Ollama:
    
    client = ollama.Client(host='http://localhost:11434')
    
    # O prompt do 'semantic_chain' é o 'user_prompt'
    # O 'text_content' é o contexto
    full_user_prompt = f"Contexto para analisar:\n{text_content}\n\nInstrução:\n{prompt}"
    
    response = client.chat(
        model='gpt-oss:20b',
        messages=[
            {'role': 'system', 'content': 'Sua missão é retornar APENAS o JSON solicitado.'},
            {'role': 'user', 'content': full_user_prompt}
        ]
    )
    # O gpt-oss-20b é otimizado para isso, então esperamos um JSON limpo
    return json.loads(response['message']['content'])
    """
    
    # --- SIMULAÇÃO ---
    # Simula a resposta do gpt-oss-20b.
    # Esta simulação é "inteligente": ela lê o 'prompt'
    # para descobrir quais chaves extrair do 'text_content'.
    
    mock_json_output = {}
    
    # Simula o caso de uso 'proc_matricula_001.yaml'
    if "nome_aluno" in prompt and "cpf_aluno" in prompt:
        # Simula a extração do texto (que recebemos do run_ocr.py)
        mock_json_output = {
            "nome_aluno": "João da Silva",
            "cpf_aluno": "123.456.789-00",
            "data_nascimento": "2010-05-15",
            "nome_responsavel": "Maria da Silva",
            "cpf_responsavel": "987.654.321-99",
            "telefone_contato": "(11) 98765-4321"
        }
    
    # Simula o caso de uso 'proc_fatura'
    elif "valor_total" in prompt and "data_vencimento" in prompt:
        mock_json_output = {
            "valor_total": 1500.75,
            "data_vencimento": "2025-11-30",
            "fornecedor": "Simulated Inc."
        }
    
    else:
        # Fallback genérico
        mock_json_output = {
            "error": "Prompt de estruturação não reconhecido pela simulação.",
            "original_text": text_content[:50] + "..."
        }
                        
    return mock_json_output

def write_output_to_stdout(data: dict):
    """Envia o resultado para o stdout como uma string JSON."""
    try:
        # O resultado (data) já é um JSON/dict
        json.dump(data, sys.stdout)
    except Exception as e:
        # Se falhar, envia um erro para o stderr
        print(json.dumps({"error": f"Falha ao serializar saída JSON: {e}"}), file=sys.stderr)

def main():
    text_content, prompt = read_input_from_stdin()
    
    if text_content is None or prompt is None:
        write_output_to_stdout({"error": "Falha ao ler o input (texto/prompt) do stdin."})
        sys.exit(1)

    try:
        # 2. Executa a estruturação do texto
        structured_data = perform_text_structuring(text_content, prompt)
        
        # 3. Envia o JSON (o dicionário Python) para o stdout
        write_output_to_stdout(structured_data)
        
    except Exception as e:
        write_output_to_stdout({"error": f"Erro durante a estruturação do texto: {e}"})
        sys.exit(1)

if __name__ == "__main__":
    main()
