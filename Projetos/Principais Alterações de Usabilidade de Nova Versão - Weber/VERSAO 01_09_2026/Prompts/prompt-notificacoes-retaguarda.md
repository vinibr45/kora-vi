# Prompt - Novas Notificações no Retaguarda

```text
Crie um artigo para a Wiki de Versão Weber Sistemas seguindo o padrão da página base.

Tema:
Novas notificações no Retaguarda

Objetivo:
Explicar para técnicos, suporte e implantação o que mudou nas notificações do Retaguarda, para que consigam orientar o cliente de forma simples e correta.

Regras:
- Não citar DLL, ZIP, executável, pacote, beta ou produção confirmada.
- Não usar linguagem de marketing.
- Escrever de forma clara, operacional e útil para atendimento.
- Evitar repetição de explicações.
- Cada seção deve trazer uma informação nova.
- Usar poucos emojis, somente quando necessário:
  - ⚙️ para configuração
  - ⚠️ para atenção/importante
  - ✅ para benefício/confirmação, se fizer sentido
- Não ensinar o passo a passo de rotinas que o técnico já conhece.
- Colocar entre parênteses onde devem entrar GIFs ou prints.

Contexto:
O Retaguarda recebeu novas notificações. Elas aparecem quando existe alguma informação que precisa ser exibida ao usuário. Além de aparecerem no Retaguarda, também emitem um som de notificação.

Notificações:

1. Produtos sem Ajuste Tributário
Indica que existem produtos que ainda não foram sincronizados com o Weber Tributário.
O Weber Tributário auxilia na sincronização dos dados fiscais dos produtos, usando informações como NCM ou descrição do produto.

2. Produtos Rejeitados pelo Ajuste Weber Tributário
Indica que alguns produtos foram rejeitados no processo de ajuste tributário.
Isso pode ocorrer quando a descrição do produto não está clara o suficiente para que o Weber Tributário identifique corretamente o item e busque os dados fiscais na iMendes.

3. Carga PDV Desatualizada
Indica que foi realizada alguma alteração no Retaguarda, como em produto, promoção ou cliente, e que ainda não foi executado o Comunica PDV após essa alteração.
A notificação lembra o usuário que essas informações precisam ser enviadas para os caixas para que os PDVs recebam as atualizações feitas no Retaguarda.

Configuração:
As notificações podem ser conferidas/configuradas no Retaguarda, na área de notificações.

Importante:
Antes de tratar a notificação como erro, verificar se a configuração está correta para apresentar esses dados.

Estrutura obrigatória em HTML:

<h2><span style="color:hsl(210, 75%, 60%);">Novas notificações no Retaguarda</span></h2>

<h2>O que mudou?</h2>
Explique que o Retaguarda recebeu novas notificações para avisar quando existirem informações que precisam de atenção.
Explique que elas aparecem no Retaguarda e emitem som de aviso.
Não repetir essa explicação nas próximas seções.

(INSERIR AQUI PRINT OU GIF MOSTRANDO A NOTIFICAÇÃO APARECENDO NO RETAGUARDA)

<h2>Quais notificações foram adicionadas?</h2>
Criar uma subseção para cada notificação:
- Produtos sem Ajuste Tributário
- Produtos Rejeitados pelo Ajuste Weber Tributário
- Carga PDV Desatualizada

<h2>⚙️ Onde configurar essas notificações?</h2>
Explicar que podem ser conferidas/configuradas no Retaguarda, na área de notificações.

(INSERIR AQUI O GIF MOSTRANDO RETAGUARDA > NOTIFICAÇÕES > CONFIGURAÇÕES)

<h2>⚠️ Importante</h2>
Explicar que a configuração deve ser conferida antes de tratar a notificação como erro.

<h2>Oriente o cliente da seguinte forma</h2>
Explicar em linguagem simples o que dizer ao cliente para cada notificação:
- Produtos sem Ajuste Tributário: produtos ainda precisam passar pela sincronização fiscal.
- Produtos Rejeitados pelo Ajuste Weber Tributário: produtos precisam de revisão, principalmente na descrição.
- Carga PDV Desatualizada: houve alteração em produto, promoção ou cliente e ainda não foi executado o Comunica PDV depois da alteração.
Finalizar dizendo que a notificação indica uma situação pendente ou uma configuração que precisa ser conferida.

Saída esperada:
Entregar um arquivo HTML final do artigo.
```

