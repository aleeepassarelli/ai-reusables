import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [react()],
  
  server: {
    // Define a porta em que o frontend irá rodar (ex: http://localhost:5173)
    port: 5173,
    
    // Configuração do Proxy: A parte mais importante.
    // Redireciona chamadas da API do frontend para o backend (FastAPI).
    proxy: {
      // Qualquer requisição que comece com '/api'
      '/api': {
        // Será redirecionada para o seu backend FastAPI
        target: 'http://localhost:8000', 
        changeOrigin: true,
        // Opcional: reescreve '/api/v1/users' para '/v1/users'
        // rewrite: (path) => path.replace(/^\/api/, ''),
      },
    },
  },
})
