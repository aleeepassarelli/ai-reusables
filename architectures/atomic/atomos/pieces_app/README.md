# README: Conector `pieces_app/`

Este diretório contém a lógica de integração para o **Pieces for Developers**.

## 🧩 O que é o Pieces?

O [Pieces](https://pieces.app/) é uma ferramenta de produtividade ("segundo cérebro") que funciona **localmente (on-device)**. Ele é projetado para capturar, enriquecer e organizar automaticamente fragmentos do seu fluxo de trabalho, como:

* Snippets de código
* Capturas de tela (screenshots)
* Links úteis
* Notas e pensamentos

## 🧠 Papel na Arquitetura: A Memória de Fragmentos

Na Atomic Architecture, o Pieces serve como a **"Memória de Fragmentos"** ou **"Memória de Trabalho"** (Working Memory).

Enquanto o `Neo4j` armazena fatos estruturados (a "Memória Semântica"), o Pieces armazena o **contexto bruto e diário** do que você está fazendo.

**Caso de uso:**
Um agente pode perguntar ao conector do Pieces: "Quais snippets de código Python o usuário salvou hoje?" ou "Qual foi a última captura de tela que o usuário analisou?"

## 🛠️ Implementação Técnica

O Pieces oferece um [SDK local](https://docs.pieces.app/getting-started/python) e uma API que roda no desktop do usuário.

Este diretório conterá o script Python (o "conector") que:

1.  Se conecta à API local do Pieces.
2.  Expõe funções para a `api_mcp` (o gateway de dados) poder **salvar** ou **buscar** fragmentos.

Este conector será usado por agentes que precisam de acesso ao contexto imediato do seu trabalho.
