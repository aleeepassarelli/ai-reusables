import yaml
from atoms.logic.extract_intent import extract_intent
from atoms.logic.merge_persona_context import merge_persona_context
from atoms.logic.compose_prompt import compose_prompt
from atoms.logic.validate_prompt import validate_prompt


def run_pipeline(user_input: str):
    """Executa o pipeline do Gerador de Prompts."""
    
    # 🔹 Etapa 1: Extrair intenção do usuário
    intent = extract_intent(user_input)

    # 🔹 Etapa 2: Carregar persona e contexto
    with open("atoms/data_units/persona_expert.yaml", "r", encoding="utf-8") as f:
        persona = yaml.safe_load(f)
    with open("atoms/data_units/format_guidelines.yaml", "r", encoding="utf-8") as f:
        fmt = yaml.safe_load(f)

    context_block = merge_persona_context(intent, persona)

    # 🔹 Etapa 3: Gerar prompt bruto
    draft_prompt = compose_prompt(context_block, fmt)

    # 🔹 Etapa 4: Validar e refinar
    with open("atoms/prompt_units/validation_feedback.yaml", "r", encoding="utf-8") as f:
        criteria = yaml.safe_load(f)
    final_prompt = validate_prompt(draft_prompt, criteria)

    return final_prompt


if __name__ == "__main__":
    user_text = input("🧠 Descreva sua tarefa: ")
    print("\n✨ Prompt Gerado:\n")
    print(run_pipeline(user_text))
