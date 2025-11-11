def compose_prompt(context: dict, format_rules: dict) -> str:
    """Gera um prompt inicial conforme formato e contexto."""
    return f"""
Você é um {context['role']} com estilo {context['style']}.
Sua tarefa é: {context['intent']}.
Responda de forma {format_rules.get('structure', 'concisa e clara')}.
Tome o tom {context['tone']}.
"""
