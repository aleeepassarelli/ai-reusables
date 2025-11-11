# 🧠 Skeleton-of-Thought (SoT)
**Nível Cognitivo:** 5 – Estrutura e Estabilidade  
**Função:** Garantir coerência lógica e estrutural antes da expansão paralela do raciocínio.  
**Tipo:** Operação de Viscosidade Cognitiva  
**Dependências:** DECOMP, SCoT, Least-to-Most  

---

## 1. Conceito
O **Skeleton-of-Thought (SoT)** é a fase em que o sistema organiza seu raciocínio em **uma estrutura mínima coerente**, criando um *esqueleto* lógico antes de gerar conteúdo completo.  
Ele evita dispersão, garante consistência e fornece uma “espinha dorsal” para que agentes ou processos subsequentes possam expandir o contexto sem perda de integridade semântica.

---

## 2. Função na Arquitetura ELS
| Componente | Papel no Fluxo |
|-------------|----------------|
| **Entrada** | Ideia, contexto ou problema bruto (ruído sem estrutura). |
| **Operação SoT** | Organiza o raciocínio em tópicos, subtarefas ou blocos estruturados. |
| **Saída** | Representação formal em YAML, JSON, Markdown, ou esquema hierárquico. |

O SoT atua como uma **ferramenta de estabilização cognitiva**. Ele é acionado antes da execução paralela (ex.: CoT, ToT, GoT) e depois da fase de geração criativa inicial.

---

## 3. Estrutura Operacional
Um SoT segue o seguinte formato interno:

```yaml
sot:
  id: <identificador>
  goal: <descrição da tarefa>
  context: <sumário do problema>
  skeleton:
    - etapa_1: <descrição breve>
    - etapa_2: <descrição breve>
    - etapa_3: <descrição breve>
  expansion_rules:
    - detalhar cada etapa em subtarefas concretas
    - validar dependências entre blocos
    - preservar coerência global
