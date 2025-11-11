def extract_intent(user_input: str) -> str:
    """Extrai intenção semântica do texto de entrada."""
    if "resuma" in user_input.lower():
        return "resumir_texto"
    if "traduz" in user_input.lower():
        return "traduzir_conteudo"
    if "explique" in user_input.lower():
        return "explicacao_detalhada"
    return "gerar_texto"
