def validate_prompt(prompt: str, criteria: dict) -> str:
    """Aplica validação simples baseada em regras e feedback."""
    min_length = criteria.get("min_length", 30)
    if len(prompt.strip()) < min_length:
        prompt += "\n# Nota: prompt expandido automaticamente para cumprir requisitos mínimos."
    if "?" not in prompt and criteria.get("require_question", False):
        prompt += "\n# Pergunta de reflexão adicionada: 'Você entendeu a tarefa?'"
    return prompt
