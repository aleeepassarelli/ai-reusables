🧾  Exemplos de Data & Prompt Units
persona_expert.yaml
role: "Pesquisador de IA"
tone: "curioso e analítico"
style: "preciso e técnico"

format_guidelines.yaml
structure: "objetiva e estruturada"
language: "pt-BR"
require_examples: true

meta_reasoning.yaml
description: "Promove coerência entre intenção, persona e estrutura"
rules:
  - "Se o objetivo é 'explicação', enfatize clareza e exemplos"
  - "Se o objetivo é 'resumo', limite a 3 parágrafos"

validation_feedback.yaml
min_length: 60
require_question: true
quality_signals:
  - "clareza"
  - "coesão"
  - "adequação de tom"

🧭  Blueprint Visual — assets/prompt_flow.mmd
graph TD
    A[🗣️ user_input] --> B[🔍 extract_intent]
    B --> C[🧩 merge_persona_context]
    C --> D[🧠 compose_prompt]
    D --> E[✅ validate_prompt]
    E --> F[📜 final_prompt]

🧪  Teste Rápido — tests/test_pipeline.py
from pipeline import run_pipeline

def test_prompt_generation():
    result = run_pipeline("Explique o funcionamento de uma RNN.")
    assert "RNN" in result
    assert "tarefa" in result or "responda" in result.lower()
