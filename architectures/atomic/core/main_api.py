# -----------------------------------------------------------------
# 🧩 Atomic Architecture - API Gateway (api_mcp)
# core/main_api.py
# -----------------------------------------------------------------
#
# Este é o servidor FastAPI (a "Pilha A").
# É o ponto de entrada principal que conecta o Frontend (React),
# o Motor (AtomicEngine) e a Infra (Docker).
#
# Para executar (conforme DEV_GUIDE.md):
# uvicorn core.main_api:app --reload --port 8000
#
# -----------------------------------------------------------------

import uvicorn
from fastapi import FastAPI, HTTPException, Body
from pydantic import BaseModel, Field
from typing import Dict, Any

# Métricas do Prometheus (da Stack C e requirements.txt)
from prometheus_client import make_asgi_app, Counter

# O Motor (nosso código principal)
from core.atomic_engine import AtomicEngine

# --- Modelos de Dados (Pydantic) ---
# Define a "forma" dos dados que a API espera.

class ChainRequest(BaseModel):
    """
    Define o corpo (body) da requisição para executar uma cadeia.
    """
    chain_id: str = Field(
        ...,
        description="O ID da 'molécula' a ser executada. Ex: 'proc_matricula_001'",
        examples=["proc_matricula_001"]
    )
    trigger_input: Dict[str, Any] = Field(
        default_factory=dict,
        description="Os dados de entrada para o gatilho. Ex: {'file_path': '/tmp/doc.pdf'}",
        examples=[{"file_path": "docs/fatura_exemplo.pdf"}]
    )

# --- Inicialização ---

print("INFO:     Iniciando o servidor FastAPI...")

app = FastAPI(
    title="Atomic Architecture API (MCP)",
    description="O gateway de API unificado (api_mcp) e o motor de execução (AtomicEngine).",
    version="1.0.0"
)

# Cria a instância única do motor que será usada pela API
try:
    engine = AtomicEngine()
    print("INFO:     AtomicEngine carregado com sucesso.")
except Exception as e:
    print(f"ERRO FATAL: Não foi possível iniciar o AtomicEngine: {e}")
    print("ERRO FATAL: Verifique as conexões (Docker, Neo4j, Redis, Ollama).")
    engine = None

# --- Métricas (Prometheus) ---
# Adiciona o endpoint /metrics que o Prometheus (Stack C) irá ler
metrics_app = make_asgi_app()
app.mount("/metrics", metrics_app)

# Contador de métrica customizado
CHAIN_COUNTER = Counter(
    "atomic_chain_runs_total",
    "Total de cadeias semânticas executadas",
    ["chain_id", "status"]
)

# --- Endpoints da API ---

@app.get("/", tags=["Status"])
def get_status():
    """Verifica a saúde da API e do motor."""
    engine_status = "online"
    if not engine or not engine.neo4j_driver or not engine.redis_client or not engine.ollama_client:
        engine_status = "degradado (verifique os logs do motor)"
    
    return {
        "status": "online",
        "engine_status": engine_status,
        "message": "Bem-vindo à Atomic Architecture API (MCP)"
    }

@app.post("/api/v1/run_chain", tags=["Engine"], response_model=Dict[str, Any])
def execute_chain(request: ChainRequest = Body(...)):
    """
    Ponto de entrada principal para executar uma cadeia semântica (Molécula).
    """
    if not engine:
        CHAIN_COUNTER.labels(chain_id=request.chain_id, status="failed").inc()
        raise HTTPException(
            status_code=503, # Service Unavailable
            detail="Motor não inicializado. Verifique os serviços de infra (Docker)."
        )
    
    print(f"INFO:     Recebida requisição para a cadeia: {request.chain_id}")
    
    try:
        # Executa a cadeia usando o motor
        result = engine.run_chain(
            chain_id=request.chain_id,
            trigger_input=request.trigger_input
        )
        
        if "error" in result:
            CHAIN_COUNTER.labels(chain_id=request.chain_id, status="error").inc()
            raise HTTPException(status_code=400, detail=result["error"])
        
        CHAIN_COUNTER.labels(chain_id=request.chain_id, status="success").inc()
        return result

    except Exception as e:
        CHAIN_COUNTER.labels(chain_id=request.chain_id, status="failed").inc()
        print(f"ERRO:     Falha crítica ao executar a cadeia {request.chain_id}: {e}")
        raise HTTPException(status_code=500, detail=f"Erro interno do motor: {str(e)}")

# --- Endpoints da API MCP (Exemplos) ---
# O frontend usará estes endpoints para o "mapa cognitivo"

@app.get("/api/v1/graph/map", tags=["Graph (MCP)"])
def get_cognitive_map():
    """
    (NÃO IMPLEMENTADO) Retorna os nós e arestas do Neo4j
    para o frontend React (@xyflow).
    """
    # TODO: Chamar 'engine.neo4j_driver' para buscar nós
    # Exemplo de dados que o App.tsx espera:
    nodes = [
        {"id": "mcp", "position": {"x": 0, "y": 0}, "data": {"label": "🤖 Agent MCP"}},
        {"id": "ocr", "position": {"x": -200, "y": 150}, "data": {"label": "📄 Agent OCR"}},
    ]
    edges = [
        {"id": "mcp-ocr", "source": "mcp", "target": "ocr", "label": "Chama"},
    ]
    return {"nodes": nodes, "edges": edges}

# --- Runner (para Debug) ---
if __name__ == "__main__":
    print("--- ATENÇÃO: Executando em modo de DEBUG ---")
    print("--- NÃO USE EM PRODUÇÃO ---")
    # Este comando permite executar o arquivo diretamente com: python core/main_api.py
    uvicorn.run("main_api:app", host="0.0.0.0", port=8000, reload=True)
