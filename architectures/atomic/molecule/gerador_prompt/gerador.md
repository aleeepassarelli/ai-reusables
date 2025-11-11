molecular/
└── gerador_prompt/
    ├── molecule.yaml
    ├── schema.yaml
    ├── pipeline.py
    ├── atoms/
    │   ├── logic/
    │   │   ├── extract_intent.py
    │   │   ├── merge_persona_context.py
    │   │   ├── compose_prompt.py
    │   │   └── validate_prompt.py
    │   ├── data_units/
    │   │   ├── persona_expert.yaml
    │   │   └── format_guidelines.yaml
    │   └── prompt_units/
    │       ├── meta_reasoning.yaml
    │       └── validation_feedback.yaml
    ├── assets/
    │   └── prompt_flow.mmd
    └── tests/
        └── test_pipeline.py
