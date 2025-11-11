"""
atomic.atoms.text_ops
Átomos de manipulação textual: limpeza e tokenização simples.
"""

from typing import List

def normalize_text(text: str) -> str:
    """
    Remove espaços extras, normaliza caixa e trim.
    Entrada: str
    Saída: str (lowercased, trimmed, single spaces)
    """
    return " ".join(text.strip().lower().split())

def tokenize(text: str) -> List[str]:
    """Divide texto por espaços (tokenização simples)."""
    return text.split()

def count_tokens(text: str) -> int:
    """Conta tokens a partir do texto bruto."""
    return len(tokenize(normalize_text(text)))
