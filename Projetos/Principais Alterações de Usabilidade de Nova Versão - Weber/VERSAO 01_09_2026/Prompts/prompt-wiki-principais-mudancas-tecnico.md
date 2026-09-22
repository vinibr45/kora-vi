# Prompt - Wiki técnica para leitura em linha com cliente

```text
Crie um arquivo HTML para a Wiki de Versão Weber Sistemas.

Objetivo:
Gerar uma versão técnica da wiki para o técnico ler em linha com o cliente durante o atendimento.

Importante:
- O cliente não terá acesso direto ao arquivo.
- A linguagem deve ajudar o técnico a conduzir a explicação com clareza.
- Pode conter orientação de atendimento, cuidados e pontos de validação.
- Não escrever como artigo público para o cliente ler sozinho.

Tema:
Principais Mudanças - Versão 01.09.2026

Regras:
- Manter linguagem simples, mas com orientação operacional para o técnico.
- Não citar DLL, ZIP, executável, beta, produção confirmada ou dados técnicos internos.
- Evitar repetição de nomes e explicações.
- Manter os mesmos emojis usados no material:
  - ⚠️ para pontos de atenção.
  - ⚙️ para configuração.
- Não usar linguagem de marketing.
- Manter as diferenças do texto base.
- Na parte da Entrada de Notas Recebe Fácil, manter o requisito como Financeiro Novo/Gestão Financeira ativo.
- Na parte de notificações, manter a explicação de que executar a tarefa mencionada não remove a notificação; para tirar da tela, é preciso marcar como lida.
- Entregar em HTML.

Imagens disponíveis:
- ../Imagens/weber tributario 1.png
- ../Imagens/weber tributario 2.png
- ../Imagens/weber tributario 3.png
- ../Imagens/weber tributario 4.png
- ../Gifs/Menu Entada de Notas Recebe Facil.gif
- ../Imagens/DashBoard Entrada de notas Recebe Facil.png
- ../Gifs/Configuração Notificação Retaguarda.gif

Estrutura obrigatória:

<h2><span style="color:hsl(210, 75%, 60%);">Principais Mudanças - Versão 01.09.2026</span></h2>

Criar uma introdução informando que é material de apoio para o técnico conduzir a explicação em linha com o cliente.

Criar índice numerado com:
1. Alterações no Cadastro de Produtos - Weber Tributário
2. Nova Opção para Entrada de Notas
3. Novas Notificações no Retaguarda

Para cada tema, criar:
- o que mudou;
- explicação objetiva;
- imagens ou marcação de onde inserir imagem;
- cuidados importantes;
- uma seção chamada "Roteiro de atendimento".

Conteúdo obrigatório:

1. Weber Tributário:
- Campos bloqueados: descrição do produto, NCM, CEST, aba ICMS, aba PIS/COFINS.
- Explicar como liberar edição desabilitando a flag "Habilita Weber Tributário".
- Alertar que, ao desabilitar, o produto deixa de receber saneamento fiscal automático.
- Explicar importância da descrição clara.
- Usar exemplos como "Bolinha" e "Carne bovina moída - formato bolinha".

2. Entrada de Notas Recebe Fácil:
- Menu Estoque recebeu nova opção para acessar Entrada de Notas Recebe Fácil.
- Diferencial: possibilidade de realizar entradas automáticas.
- Possui dashboards para acompanhamento de novas entradas e auditoria para produtos novos cadastrados.
- Ajuda a acompanhar notas disponíveis, criar notas manuais, realizar entradas automáticas ou assistidas, auditar notas/produtos/fornecedores e acompanhar indicadores.
- Requisito: Financeiro Novo/Gestão Financeira ativo.

3. Notificações:
- Retaguarda recebeu novas notificações e som de aviso.
- Produtos sem Ajuste Tributário: produtos ainda não sincronizados com Weber Tributário.
- Produtos Rejeitados pelo Ajuste Weber Tributário: produtos rejeitados, geralmente por descrição pouco clara.
- Carga PDV Desatualizada: houve alteração em produto, promoção ou cliente e ainda não foi executado o Comunica PDV após essa alteração.
- Notificações podem ser conferidas/configuradas na área de notificações.
- Verificar configuração antes de tratar como erro.
- Executar a tarefa indicada não remove automaticamente a notificação; é preciso marcar como lida.

Saída esperada:
Entregar um arquivo HTML final da wiki técnica.
```

