# 📖 Glossário — Termos de IA

- **Embedding**: Representação vetorial de um texto que captura sua semântica.
- **RAG (Retrieval-Augmented Generation)**: Técnica que combina busca e geração de texto.
- **Prompt Engineering**: Processo de criar e ajustar instruções para modelos de linguagem.
- **Fine-tuning**: Ajuste de um modelo pré-treinado em um domínio específico.
- **Chain of Thought (CoT)**: Estrutura lógica de raciocínio passo a passo.

🧠 Uso:

from atoms.logic.normalize_text import normalize_text

with open("atoms/data_units/glossary_ai_terms.md") as f:
    glossary = normalize_text(f.read())
