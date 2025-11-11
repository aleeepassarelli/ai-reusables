# README: Camada 2 - Moléculas de Ação (`molecules/`)

Esta camada é o "livro de receitas" da **Atomic Architecture**.

Se os `atomos` (Camada 1) são os **ingredientes** e os `organisms` (Camada 3) são os **chefs especialistas**, as `molecules` (Camada 2) são as **receitas** que o `AtomicEngine` lê para preparar um prato.

Esta camada define o "COMO" — os fluxos de automação, as cadeias de raciocínio e os roteiros cognitivos.

---

## 1. `semantic_chain.yaml` (A Receita)

Este não é um único arquivo, mas sim um **tipo de arquivo** de configuração. Cada `.yaml` neste diretório representa uma **Cadeia Semântica** (ou fluxo de trabalho).

**Função:**
Um `semantic_chain.yaml` é um roteiro **declarativo** (não é código Python) que define uma sequência de passos. O `core/atomic_engine.py` lê este arquivo e o executa.

Cada passo na cadeia define:
1.  Qual "Organismo" (agente) chamar (ex: `agent_OCR.yaml`).
2.  Quais "Átomos" (dados) usar como entrada (ex: o arquivo do upload).
3.  O que fazer com a saída (ex: passá-la para o próximo agente).

**Exemplo:**
O arquivo `proc_matricula_001.yaml` (que podemos criar aqui) é um exemplo de "Molécula" que combina os "Organismos" `agent_OCR` e `agent_text_struct` para processar um documento.



## 2. `pipeline_skeleton.md` (O Molde da Receita)

Este arquivo é um **guia de documentação** (um "template") usado para criar *novos* arquivos `semantic_chain.yaml`.

**Função:**
Alinhado com a filosofia de **Transparência Educacional**, este esqueleto garante que toda nova automação seja padronizada e bem documentada.

Quando um desenvolvedor ou professor deseja criar um novo fluxo, ele usa este `.md` para definir:
* O **Objetivo** do fluxo.
* O **Gatilho** (o que o inicia).
* Os **Agentes** necessários.
* O **Formato de Saída** esperado.

---

## ⚙️ Conexão com o Motor

O `AtomicEngine` (em `core/atomic_engine.py`) é o motor de execução. Ele contém a função `run_chain("nome_da_cadeia")`. Essa função irá:

1.  Procurar o arquivo `molecules/nome_da_cadeia.yaml`.
2.  Ler os `steps` (passos) definidos nele.
3.  Executar cada passo, orquestrando os agentes da Camada 3.
