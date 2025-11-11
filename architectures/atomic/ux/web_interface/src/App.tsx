// -----------------------------------------------------------------
// 🧩 Atomic Architecture - Frontend Entrypoint
// ux/web_interface/src/App.tsx
// -----------------------------------------------------------------

import { useState, useCallback } from 'react';
import {
  ReactFlow,
  Controls,
  Background,
  addEdge,
  MiniMap,
  useNodesState,
  useEdgesState,
  Node,
  Edge,
  Connection,
} from '@xyflow/react';

// Importa os estilos CSS obrigatórios do React Flow
import '@xyflow/react/dist/style.css';

// --- Nós Iniciais ---
// Estes são os "Organismos" (Agentes) da sua arquitetura,
// representando o "micélio cognitivo" que você descreveu.
const initialNodes: Node[] = [
  {
    id: 'mcp',
    type: 'input', // O Agente MCP é um "input" do fluxo
    position: { x: 0, y: 0 },
    data: { label: '🤖 Agent MCP (Gerente)' },
    style: { backgroundColor: '#ffc107', color: 'black' },
  },
  {
    id: 'ocr',
    position: { x: -200, y: 150 },
    data: { label: '📄 Agent OCR (Leitor)' },
  },
  {
    id: 'struct',
    position: { x: 200, y: 150 },
    data: { label: '🧬 Agent Text Struct (Organizador)' },
  },
  {
    id: 'neo4j',
    type: 'output', // O Neo4j é um "output" (destino)
    position: { x: 0, y: 300 },
    data: { label: '🗄️ Neo4j (Memória)' },
  },
];

// --- Arestas Iniciais ---
// Representam uma "semantic_chain" (Molécula) visual.
const initialEdges: Edge[] = [
  { id: 'mcp-ocr', source: 'mcp', target: 'ocr', label: '1. Ler PDF' },
  { id: 'mcp-struct', source: 'mcp', target: 'struct', label: '2. Estruturar' },
  { id: 'struct-neo4j', source: 'struct', target: 'neo4j', label: '3. Salvar' },
];

function App() {
  const [nodes, setNodes, onNodesChange] = useNodesState(initialNodes);
  const [edges, setEdges, onEdgesChange] = useEdgesState(initialEdges);

  // Função para lidar com novas conexões (arrastar e soltar)
  const onConnect = useCallback(
    (params: Connection) => setEdges((eds) => addEdge(params, eds)),
    [setEdges]
  );

  // TODO: Adicionar lógica useEffect() para buscar nós/arestas da 'api_mcp'
  // useEffect(() => {
  //   axios.get('/api/v1/cognitive-map').then((response) => {
  //     setNodes(response.data.nodes);
  //     setEdges(response.data.edges);
  //   });
  // }, []);

  return (
    <div style={{ width: '100vw', height: '100vh' }}>
      <ReactFlow
        nodes={nodes}
        edges={edges}
        onNodesChange={onNodesChange}
        onEdgesChange={onEdgesChange}
        onConnect={onConnect}
        fitView // Centraliza o grafo na tela
      >
        <MiniMap />
        <Controls />
        <Background />
      </ReactFlow>
    </div>
  );
}

export default App;
