def merge_persona_context(intent: str, persona: dict) -> dict:
    """Combina intenção e persona em um bloco contextual unificado."""
    return {
        "role": persona.get("role", "especialista"),
        "tone": persona.get("tone", "neutro"),
        "intent": intent,
        "style": persona.get("style", "didático"),
    }

