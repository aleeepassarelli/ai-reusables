"""
⚛️ Atomic Logic Unit — vector_distance
Autor: Mia Framework Lab
Descrição:
    Calcula a distância entre vetores (cosine ou euclidiana).
    Útil para comparar embeddings, similaridade semântica ou clustering atômico.
"""

import numpy as np


def vector_distance(a, b, method: str = "cosine") -> float:
    """
    Calcula a distância entre dois vetores numéricos.

    Args:
        a (list[float] | np.ndarray): Vetor A.
        b (list[float] | np.ndarray): Vetor B.
        method (str): Tipo de distância ('cosine' ou 'euclidean').

    Returns:
        float: Valor da distância.
    """
    a, b = np.array(a), np.array(b)
    if method == "cosine":
        dot = np.dot(a, b)
        norm = np.linalg.norm(a) * np.linalg.norm(b)
        return 1 - dot / norm if norm != 0 else 1.0
    elif method == "euclidean":
        return np.linalg.norm(a - b)
    else:
        raise ValueError("Método inválido. Use 'cosine' ou 'euclidean'.")
