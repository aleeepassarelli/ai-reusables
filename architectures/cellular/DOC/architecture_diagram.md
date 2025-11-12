%% Cellular Architecture – Diagrama Geral
flowchart TD

%% Nível 0 — Interface
U[👩‍💻 Usuário / Cliente] --> R[🧭 Cell Router]

%% Nível 1 — Roteador Central
R --> |Rota /users| C1[🧫 microservice-users]
R --> |Rota /appointments| C2[🧫 microservice-appointments]
R --> |Rota /reports| C3[🧫 microservice-reports]
R --> |API /admin| CTRL[🧬 Cell Controller]

%% Nível 2 — Núcleo de Cada Célula
subgraph C1_Cell ["Célula: microservice-users"]
    P1[📡 Presentation Layer] --> B1[⚙️ Business Logic]
    B1 --> D1[(🗃️ Database)]
end

subgraph C2_Cell ["Célula: microservice-appointments"]
    P2[📡 Presentation Layer] --> B2[⚙️ Business Logic]
    B2 --> D2[(🗃️ Database)]
end

subgraph C3_Cell ["Célula: microservice-reports"]
    P3[📡 Presentation Layer] --> B3[⚙️ Business Logic]
    B3 --> D3[(🗃️ Database)]
end

%% Nível 3 — Controle e Observabilidade
subgraph Observability ["📊 Observabilidade e Controle"]
    CTRL --> G[📈 Grafana Dashboard]
    CTRL --> P[📡 Prometheus Metrics]
end

%% Conexões entre células e monitoramento
C1 --> P
C2 --> P
C3 --> P

%% Feedback Loop (Controle)
CTRL --> |Health Check| R
CTRL --> |Clone / Pause / Resume| C1
CTRL --> |Clone / Pause / Resume| C2
CTRL --> |Clone / Pause / Resume| C3

%% Descrições
classDef router fill:#c5e1a5,stroke:#558b2f,stroke-width:2px,color:#000;
classDef cell fill:#e3f2fd,stroke:#1976d2,stroke-width:2px,color:#000;
classDef control fill:#fce4ec,stroke:#ad1457,stroke-width:2px,color:#000;
classDef observ fill:#fff9c4,stroke:#fbc02d,stroke-width:2px,color:#000;
classDef user fill:#d1c4e9,stroke:#4527a0,stroke-width:2px,color:#000;

class U user;
class R router;
class C1,C2,C3 cell;
class CTRL control;
class G,P observ;
