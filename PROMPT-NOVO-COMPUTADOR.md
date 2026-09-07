# Prompt Para Usar a Kora em Outro Computador

Este arquivo serve para ajudar a clonar o repositório privado da Kora do Vinícius em outro computador e recuperar o contexto desta conversa.

## 1. Clonar o repositório

No novo computador, abra o terminal na pasta onde deseja salvar a Kora e execute:

```powershell
git clone https://github.com/vinibr45/kora-vi.git
cd kora-vi
```

Se o Git pedir autenticação, entre com a conta GitHub `vinibr45`.

Se estiver usando GitHub CLI:

```powershell
gh auth login
git clone https://github.com/vinibr45/kora-vi.git
cd kora-vi
```

## 2. Arquivos importantes para recuperar o contexto

Depois de clonar, leia estes arquivos:

```text
README.md
COMECE-AQUI.md
memory/vinicius-borges-operational-briefing.md
memory/weber-raa-operational-knowledge.md
docs/chat-history/kora-weber-raa-chat-2026-09-06.md
```

As imagens enviadas durante a conversa ficam em:

```text
docs/chat-history/assets/
```

## 3. Prompt para colar no Codex/ChatGPT no outro computador

Use este prompt quando abrir a Kora em outro computador:

```text
Estou usando o repositório privado `kora-vi`, clonado de:

https://github.com/vinibr45/kora-vi

Quero que você use este repositório como minha Kora pessoal/operacional.

Antes de me ajudar, leia estes arquivos:

1. README.md
2. COMECE-AQUI.md
3. memory/vinicius-borges-operational-briefing.md
4. memory/weber-raa-operational-knowledge.md
5. docs/chat-history/kora-weber-raa-chat-2026-09-06.md

Objetivo:
Recuperar o contexto operacional sobre mim, Vinícius Borges, minha forma de trabalhar, meus projetos e principalmente a proposta de melhoria das RAAs no IOS da Weber Sistemas.

Contexto principal:
- Sou Vinícius Borges.
- Trabalho com suporte técnico avançado/N3, ERP, Firebird, SQL, infraestrutura, QA e análise de causa raiz.
- Quero usar a Kora para organizar conhecimento, ideias, processos, documentação, propostas e análises técnicas.
- Um dos assuntos principais é a reestruturação das RAAs no IOS da Weber Sistemas.
- A conversa exportada em `docs/chat-history/kora-weber-raa-chat-2026-09-06.md` contém todo o raciocínio construído sobre:
  - abertura de RAA pela recepção;
  - contato do cliente;
  - padronização de títulos;
  - classificação por módulo, rotina e categoria;
  - evidências operacionais;
  - problemas conhecidos;
  - solução definitiva versus contorno operacional;
  - validação pós-atendimento via WhatsApp;
  - apresentação para gerência.

Ao responder, siga meu estilo preferido:
- seja direto;
- organize ideias em estrutura clara;
- não simplifique demais assuntos técnicos;
- investigue por hipóteses quando for troubleshooting;
- aponte riscos, inconsistências e melhorias;
- transforme ideias soltas em documentação, proposta, backlog ou próximos passos.

Quando eu pedir ajuda com RAAs, IOS, Weber ou atendimento, use os arquivos de memória e o histórico exportado como contexto.
```

## 4. Comando para atualizar depois

Quando quiser puxar novidades do GitHub neste computador:

```powershell
git pull
```

Quando quiser enviar alterações feitas no novo computador:

```powershell
git status
git add .
git commit -m "Update Kora notes"
git push
```

## 5. Observação de privacidade

Este repositório contém contexto pessoal e operacional. Mantenha o repositório como privado.
