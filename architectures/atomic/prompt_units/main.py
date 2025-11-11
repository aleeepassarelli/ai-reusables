from core_engineering.prompt_modular import PromptBuilder

prompt = PromptBuilder()
prompt.add("atoms/prompt_units/persona_expert.yaml")
prompt.add("atoms/prompt_units/reasoning_chain.yaml")
system_prompt = prompt.build()
