"""
⚛️ Atomic Logic Unit — normalize_text
Autor: Mia Framework Lab
Descrição:
    Normaliza um texto reduzindo ruídos, padronizando espaços e acentuação.
    Este é um átomo fundamental para qualquer pipeline cognitivo baseado em NLP.
"""

import re
import unicodedata


def normalize_text(text: str, lowercase: bool = True) -> str:
    """
    Normaliza o texto removendo acentos, múltiplos espaços e caracteres não-ASCII.

    Args:
        text (str): Texto de entrada.
        lowercase (bool): Converte para minúsculas (default=True).

    Returns:
        str: Texto normalizado.
    """
    if not isinstance(text, str):
        raise ValueError("O parâmetro 'text' deve ser uma string.")

    # Remove acentuação
    text = unicodedata.normalize("NFD", text)
    text = text.encode("ascii", "ignore").decode("utf-8")

    # Remove caracteres especiais redundantes
    text = re.sub(r"[^a-zA-Z0-9\s.,!?-]", "", text)

    # Reduz espaços múltiplos
    text = re.sub(r"\s+", " ", text).strip()

    # Converte para minúsculas, se desejado
    if lowercase:
        text = text.lower()

    return text
