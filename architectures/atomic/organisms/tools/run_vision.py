#!/usr/bin/env python
# -----------------------------------------------------------------
# 🧩 Atomic Architecture - Ferramenta de Visão
# organisms/tools/run_vision.py
# -----------------------------------------------------------------
#
# Este script é uma "ferramenta local" executada pelo AtomicEngine.
# Ele é chamado pelo 'agent_vision.yaml' (type: "llm_chat", mas pode ser 'local_tool').
#
# 1. Recebe um JSON do 'stdin' (do engine) contendo o 'image_path' e uma 'question'.
# 2. Executa a análise de visão (aqui simulada) usando um VLM.
# 3. Imprime um JSON para o 'stdout' (para o engine).
#
# -----------------------------------------------------------------

import sys
import json
import os

# Em um cenário real, você importaria o provedor Ollama/Dashscope aqui.
# from organisms.providers_api.ollama_provider import run_qwen_vision # Exemplo
# from organisms.providers_api.dashscope_provider import run_qwen_vision # Exemplo

def read_input_from_stdin():
    """Lê e parseia o JSON vindo do stdin."""
    try:
        input_data = json.loads(sys.stdin.read())
        
        if not isinstance(input_data, dict):
            raise ValueError("Input (stdin) não é um objeto JSON.")
            
        required_keys = ['image_path', 'question']
        for key in required_keys:
            if key not in input_data:
                raise ValueError(f"Chave '{key}' ausente no input do stdin.")
        
        return input_data
        
    except json.JSONDecodeError as e:
        print(f"Erro de JSON no stdin: {e}", file=sys.stderr)
        return None
    except ValueError as e:
        print(f"Erro de Valor no stdin: {e}", file=sys.stderr)
        return None

def perform_vision_analysis(image_path: str, question: str):
    """
    Simula o 'qwen 2.5 vision 8b' analisando uma imagem.
    
    Na implementação real, aqui você usaria o cliente Ollama para
    chamar o modelo Qwen-VL.
    
    Ex:
    response = ollama_client.generate(
        model='qwen:v2.5-8b',
        prompt=question,
        images=[image_path]
    )
    return response['response']
    """
    # Verifica se o arquivo (simulado) existe
    if not os.path.exists(image_path):
        # Em um cenário real, você faria a verificação.
        # Como o engine já tem o path, vamos apenas simular.
        pass

    # --- SIMULAÇÃO ---
    # Simula a resposta do Qwen-VL baseada na pergunta.
    if "o que você vê" in question.lower() or "descreva a imagem" in question.lower():
        mock_response = (
            f"Eu vejo uma imagem localizada em '{image_path}'. "
            "É uma cena pitoresca com uma montanha ao fundo, um rio fluindo "
            "e uma pequena cabana na margem. A cor predominante é verde e azul."
        )
    elif "cores principais" in question.lower():
        mock_response = "As cores principais são verde (vegetação) e azul (céu e rio)."
    elif "existem pessoas" in question.lower():
        mock_response = "Não consigo identificar pessoas na imagem."
    else:
        mock_response = f"Simulação de análise visual para a pergunta: '{question}'. " \
                        "Parece uma bela paisagem natural."
                        
    return mock_response

def write_output_to_stdout(data: dict):
    """Envia o resultado para o stdout como uma string JSON."""
    try:
        json.dump(data, sys.stdout)
    except Exception as e:
        # Se falhar, envia um erro para o stderr
        print(json.dumps({"error": f"Falha ao serializar saída: {e}"}), file=sys.stderr)

def main():
    input_data = read_input_from_stdin()
    
    if input_data is None:
        write_output_to_stdout({"error": "Falha ao ler o input do stdin para visão."})
        sys.exit(1)

    image_path = input_data['image_path']
    question = input_data['question']

    try:
        # 2. Executa a análise de visão
        vision_analysis_result = perform_vision_analysis(image_path, question)
        
        # 3. Prepara a saída (conforme esperado pelo 'atomic_engine')
        # A 'output_variable' era 'vision_description'.
        output_data = {
            "vision_description": vision_analysis_result,
            "source_image": image_path,
            "question_asked": question,
            "vlm_model": "qwen:v2.5-8b (simulado)"
        }
        
        # 4. Envia o JSON para o stdout
        write_output_to_stdout(output_data)
        
    except Exception as e:
        write_output_to_stdout({"error": f"Erro durante a análise de visão: {e}"})
        sys.exit(1)

if __name__ == "__main__":
    main()
