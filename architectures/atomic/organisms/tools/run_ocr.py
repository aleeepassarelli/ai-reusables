#!/usr/bin/env python
# -----------------------------------------------------------------
# 🧩 Atomic Architecture - Ferramenta de OCR
# organisms/tools/run_ocr.py
# -----------------------------------------------------------------
#
# Este script é uma "ferramenta local" executada pelo AtomicEngine.
# Ele é chamado pelo 'agent_OCR.yaml' (type: "local_tool").
#
# 1. Recebe um JSON do 'stdin' (do engine) contendo o file_path.
# 2. Executa a lógica de OCR (aqui simulada) no arquivo.
# 3. Imprime um JSON para o 'stdout' (para o engine).
#
# -----------------------------------------------------------------

import sys
import json
import os

def read_input_from_stdin():
    """Lê e parseia o JSON vindo do stdin."""
    try:
        input_str = sys.stdin.read()
        if not input_str:
            raise ValueError("Input (stdin) está vazio.")
        
        # O 'atomic_engine' envia o file_path como JSON
        # Ex: "path/para/doc.pdf" (o engine já resolveu o JSON)
        # Por simplicidade, vamos assumir que o engine envia o file_path direto.
        # Atualização: O engine envia o 'input_data' como JSON.
        # ex: '"/tmp/doc.pdf"' (string JSON) ou '{"path": "/tmp/doc.pdf"}'
        
        # Vamos tratar o input como o file_path direto (enviado como string JSON)
        file_path = json.loads(input_str)
        if not isinstance(file_path, str):
            raise ValueError("Input (stdin) não é uma string JSON de caminho.")
            
        return file_path
        
    except json.JSONDecodeError as e:
        print(f"Erro de JSON no stdin: {e}", file=sys.stderr)
        return None
    except ValueError as e:
        print(f"Erro de Valor no stdin: {e}", file=sys.stderr)
        return None

def perform_semantic_ocr(file_path: str):
    """
    Simula o 'nanonets-OCR2 3b' processando um arquivo.
    
    Na implementação real, aqui você usaria a biblioteca
    'nanonets' ou faria uma chamada de API para o modelo.
    
    Retorna o documento como Markdown limpo.
    """
    # Verifica se o arquivo (simulado) existe
    if not os.path.exists(file_path):
        # Em um cenário real, você faria a verificação.
        # Como o engine já tem o path, vamos apenas simular.
        pass

    # --- SIMULAÇÃO ---
    # Simulamos o resultado do OCR para o 'proc_matricula_001.yaml'
    # Esta é a "mágica" do OCR semântico: ele já retorna Markdown.
    
    mock_markdown_output = """
# Ficha de Matrícula - Aluno 123

## Dados do Aluno
- **Nome:** João da Silva
- **CPF:** 123.456.789-00
- **Data de Nascimento:** 2010-05-15
- **Endereço:** Rua das Flores, 123, São Paulo, SP

## Dados do Responsável
- **Nome:** Maria da Silva
- **CPF:** 987.654.321-99
- **Telefone:** (11) 98765-4321
"""
    return mock_markdown_output

def write_output_to_stdout(data: dict):
    """Envia o resultado para o stdout como uma string JSON."""
    try:
        json.dump(data, sys.stdout)
    except Exception as e:
        # Se falhar, envia um erro para o stderr
        print(json.dumps({"error": f"Falha ao serializar saída: {e}"}), file=sys.stderr)

def main():
    file_path = read_input_from_stdin()
    
    if file_path is None:
        write_output_to_stdout({"error": "Falha ao ler o caminho do arquivo do stdin."})
        sys.exit(1)

    try:
        # 2. Executa o OCR
        markdown_content = perform_semantic_ocr(file_path)
        
        # 3. Prepara a saída (conforme esperado pelo 'atomic_engine')
        # O engine espera um dict/JSON.
        # A 'output_variable' era 'raw_markdown_content'.
        output_data = {
            "raw_markdown_content": markdown_content,
            "source_file": file_path,
            "ocr_engine": "nanonets-OCR2 (simulado)"
        }
        
        # 4. Envia o JSON para o stdout
        write_output_to_stdout(output_data)
        
    except Exception as e:
        write_output_to_stdout({"error": f"Erro durante o processamento do OCR: {e}"})
        sys.exit(1)

if __name__ == "__main__":
    main()
