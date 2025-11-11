# 🧩 Como Contribuir para a Atomic Architecture

Ficamos muito felizes com seu interesse em contribuir! Este projeto é construído com base na colaboração da comunidade.

Seja você um professor, um desenvolvedor, um pesquisador ou apenas um entusiasta de IA local, sua contribuição é bem-vinda. Queremos que este projeto seja uma ferramenta viva, moldada por quem a utiliza.

## 🌐 Filosofia de Contribuição

Buscamos manter as três filosofias operacionais do projeto:

1.  **Autonomia Local:** Priorize soluções que possam rodar offline ou com mínima dependência de nuvem.
2.  **Evolução Modular:** Pense em sua contribuição como um "bloco de Lego". Ela deve se encaixar sem quebrar o que já existe.
3.  **Transparência Educacional:** Sua contribuição deve ser bem documentada e fácil de entender.

## 🐛 Reportando Bugs

Se você encontrar um bug, por favor, [abra uma "Issue"](https://github.com/aleeepassarelli/atomic-architecture/issues) (link a ser atualizado) com as seguintes informações:

* Qual versão você está usando.
* Quais foram os passos para reproduzir o bug.
* O que você esperava que acontecesse.
* O que de fato aconteceu (incluindo logs de erro, se houver).

## 💡 Propondo Melhorias ou Novos Recursos

Se você tem uma ideia para uma nova "Molécula" (fluxo), um novo "Organismo" (agente) ou uma melhoria no `SLE Engine`, o melhor caminho é:

1.  Verificar as [Issues abertas](https://github.com/aleeepassarelli/atomic-architecture/issues) para ver se alguém já teve a mesma ideia.
2.  Se não, [abra uma nova Issue](https://github.com/aleeepassarelli/atomic-architecture/issues/new) para descrever sua proposta. Isso nos permite discutir a viabilidade e o design antes que você gaste tempo implementando.

## 🚀 Como Fazer sua Primeira Contribuição (Pull Request)

1.  **Faça o Fork** do repositório (`https--github.com/aleeepassarelli/atomic-architecture.git`).
2.  **Clone** o seu fork localmente: `git clone https--github.com/SEU-USUARIO/atomic-architecture.git`
3.  **Crie uma Branch** para sua feature: `git checkout -b minha-nova-feature`
4.  **Faça suas Alterações.** (Veja abaixo como adicionar Agentes ou Cadeias).
5.  **Faça o Commit** das suas alterações: `git commit -m 'Adiciona novo agente de OCR'`
6.  **Faça o Push** para a sua branch: `git push origin minha-nova-feature`
7.  **Abra um Pull Request** (PR) no repositório original.

---

### 🧬 Adicionando um novo "Organismo" (Agente)

1.  Use o `4_templates_forms/agent_template.yaml` como base.
2.  Crie seu novo `agent_meu-agente.yaml` no diretório `3_organisms_agents/`.
3.  Adicione a lógica Python (o "cérebro" do agente) no diretório `3_organisms_agents/tools/`.
4.  Atualize o `DEV_GUIDE.md` se houver passos de instalação específicos (ex: `pip install nova-lib`).

### 🧪 Adicionando uma nova "Molécula" (Cadeia Semântica)

1.  Use o `2_molecules_action/pipeline_skeleton.md` como guia.
2.  Crie seu novo `minha_cadeia.yaml` no diretório `2_molecules_action/`.
3.  Documente o objetivo da cadeia, as entradas e as saídas esperadas no topo do arquivo YAML (como comentário).

## 💬 Código de Conduta

Para garantir um ambiente acolhedor e profissional, esperamos que todos os contribuidores sigam um [Código de Conduta](LINK_PARA_CODE_OF_CONDUCT.md). (Podemos adicionar este arquivo depois, se desejar).

Obrigado por ajudar a construir ferramentas de IA locais, abertas e transparentes!
