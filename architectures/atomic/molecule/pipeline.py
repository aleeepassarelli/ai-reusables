# ============================================================
# 🧬 pipeline.py — Executor Genérico de Moléculas Atômicas
# ============================================================
# Interpreta molecule.yaml e executa o pipeline descrito.
# Cada molécula é composta de átomos (funções ou módulos)
# que cooperam para gerar um resultado emergente.
# ============================================================

import os
import yaml
import importlib.util
from typing import Any, Dict, Callable
from pathlib import Path
from collections import defaultdict


# ------------------------------------------------------------
# Utilitários
# ------------------------------------------------------------

def load_yaml(path: str) -> dict:
    """Carrega um arquivo YAML."""
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def dynamic_import(module_path: str, function_name: str) -> Callable:
    """Importa dinamicamente uma função de um arquivo Python."""
    spec = importlib.util.spec_from_file_location("dynamic_module", module_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return getattr(module, function_name)


def map_inputs(context: Dict[str, Any], mapping: Dict[str, str]) -> Dict[str, Any]:
    """
    Faz o binding das variáveis de entrada:
    Usa '@inputs' e '@pipeline' para resolver dependências dinâmicas.
    """
    resolved = {}
    for k, ref in mapping.items():
        if ref.startswith("@inputs."):
            key = ref.replace("@inputs.", "")
            resolved[k] = context["inputs"].get(key)
        elif ref.startswith("@pipeline."):
            key = ref.replace("@pipeline.", "")
            resolved[k] = context["pipeline"].get(key)
        else:
            resolved[k] = ref
    return resolved


def update_context(context: Dict[str, Any], output_map: Dict[str, str], result: Any):
    """Atualiza o contexto com as saídas do passo atual."""
    if isinstance(result, dict):
        for out_key, alias in output_map.items():
            if out_key in result:
                context["pipeline"][alias] = result[out_key]
    else:
        # Caso a função retorne valor simples
        for alias in output_map.values():
            context["pipeline"][alias] = result


# ------------------------------------------------------------
# Executor de Pipeline
# ------------------------------------------------------------

class MoleculeRunner:
    def __init__(self, molecule_yaml: str):
        self.yaml_path = Path(molecule_yaml)
        self.molecule = load_yaml(molecule_yaml)
        self.context = {
            "inputs": {},
            "pipeline": {},
            "outputs": {},
        }

    def _load_atoms(self):
        """Carrega funções de todos os átomos listados no YAML."""
        self.atoms = {}
        for atom in self.molecule.get("atoms", []):
            if "function" in atom and atom["path"].endswith(".py"):
                func = dynamic_import(atom["path"], atom["function"])
                self.atoms[atom["id"]] = func
        return self.atoms

    def run(self, **inputs) -> Dict[str, Any]:
        """Executa o pipeline completo da molécula."""
        print(f"🔹 Executando molécula: {self.molecule['name']}")
        self._load_atoms()
        self.context["inputs"] = inputs

        for step in self.molecule.get("pipeline", []):
            step_name = step["step"]
            uses = step["uses"]
            input_map = step.get("input_map", {})
            output_map = step.get("output_map", {})

            # Resolve entradas
            step_inputs = map_inputs(self.context, input_map)

            print(f"⚙️  Executando etapa: {step_name} ({uses})")

            # Executa a função do átomo ou placeholder (modelo)
            if uses in self.atoms:
                func = self.atoms[uses]
                result = func(**step_inputs)
            elif uses == "embedding_model":
                # Placeholder para modelo de vetorização
                from sentence_transformers import SentenceTransformer
                model = SentenceTransformer("all-MiniLM-L6-v2")
                result = {"vector": model.encode(step_inputs["text"]).tolist()}
            elif uses == "internal.selector":
                # Escolhe o rótulo de maior pontuação
                scores = step_inputs["scores"]
                label = max(scores, key=scores.get)
                result = {"label": label, "confidence": scores[label]}
            else:
                raise ValueError(f"Átomo ou componente desconhecido: {uses}")

            # Atualiza contexto com resultados
            update_context(self.context, output_map, result)

        # Monta outputs finais
        outputs_cfg = self.molecule.get("outputs", {})
        for out_key in outputs_cfg:
            alias = out_key
            self.context["outputs"][alias] = self.context["pipeline"].get(f"predicted_{alias}")

        print("✅ Pipeline concluído com sucesso!")
        return self.context["outputs"]


# ------------------------------------------------------------
# Execução direta (debug / exemplo)
# ------------------------------------------------------------

if __name__ == "__main__":
    runner = MoleculeRunner("molecule.yaml")
    result = runner.run(
        text="O GPT revolucionou o design de interfaces conversacionais.",
        candidate_labels=["tecnologia", "educação", "ciência"]
    )
    print("\n🔸 Resultado Final:")
    print(result)
