# README: Camada 5 - Experiência do Usuário (`ux/`)

Este diretório contém todas as interfaces humano-computador (HCI) para a **Atomic Architecture**. É a "pele" do sistema, permitindo que os usuários interajam com os agentes (`organisms`) e fluxos de trabalho (`molecules`).

A filosofia desta camada é fornecer duas interfaces distintas para dois públicos diferentes:

1.  **Usuários Finais e Educadores:** Uma interface web rica e visual (`web_interface`).
2.  **Desenvolvedores e Power-Users:** Uma interface de linha de comando rápida e programável (`cli_demo`).

---

## 🖥️ 1. `web_interface/` (O Dashboard Visual)

Este é o "Painel Educacional" e o dashboard principal do projeto. É um aplicativo web moderno (React + Vite + TypeScript) projetado para a interação visual com a arquitetura.

### Recurso Principal: O Mapa Cognitivo

O objetivo principal desta interface é usar a biblioteca **`@xyflow/react`** para renderizar visualmente os "Organismos" (agentes), as "Moléculas" (cadeias) e os "Átomos" (dados) como um **mapa cognitivo** ou **"micélio"** interativo.

Os usuários poderão, eventualmente, criar e editar `semantic_chain.yaml` arrastando e soltando nós neste painel.

### Como Executar (Desenvolvimento)

```bash
# Navegue até o diretório do frontend
cd ux/web_interface

# Instale as dependências (definidas no package.json)
npm install

# Inicie o servidor de desenvolvimento (Vite)
# (Ele se conectará ao backend FastAPI na porta 8000)
npm run dev
