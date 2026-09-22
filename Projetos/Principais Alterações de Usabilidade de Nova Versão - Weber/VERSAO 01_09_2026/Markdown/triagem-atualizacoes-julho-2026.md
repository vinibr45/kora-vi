# Triagem para Wiki - Atualizacoes de Julho 2026

Fonte analisada:

`Html/Alteracoes do beta de maio a julho - Portal Gerencial Weber.html`

Periodo da consulta salva:

`01/05/2026` ate `25/07/2026`

## Criterio usado

Separar itens que podem virar wiki quando:

- mudam algum processo percebido pelo cliente;
- criam campo, opcao, aba, menu ou etapa nova;
- exigem configuracao;
- criam ou alteram parametro/flag/tag;
- ajudam o tecnico a explicar uma mudanca operacional.

Itens puramente internos, correcao tecnica silenciosa, DLL/ZIP/UPD ou ajuste de compatibilidade foram deixados como baixa prioridade, salvo quando mudam a rotina do usuario.

## Itens mais fortes para pesquisar

### 1. Nova Entrada de Notas / Entrada Assistida

Por que pesquisar:

E o maior bloco funcional do periodo. Tem modulo novo, fluxo novo, etapa nova, relatorios, permissoes e recurso de lotes.

Pontos encontrados na fonte:

- Primeira versao da nova entrada de notas.
- Entrada assistida com ajustes de interface.
- Navegacao com teclas na entrada assistida e manual.
- Coluna `Detalhes` na associacao de produtos.
- Mascara de NCM ao cadastrar pela entrada de notas.
- Nova etapa `Faturas`, para revisar as faturas do XML.
- Aba `Relatorios`, iniciando com `Variacao de precos`.
- Opcoes de `Analise` no dashboard inicial.
- Recurso de informar/consultar lotes das entradas.
- Cadastro manual de lotes quando o produto usa lotes.
- Controle de permissao para formularios de Analise.
- Analise de associacoes produto x fornecedor.

O que pesquisar antes de escrever:

- Caminho exato do menu em producao.
- Quais telas merecem gif: menu, entrada assistida, etapa Faturas, lotes e Analise.
- Quais configuracoes/permissoes sao obrigatorias.
- Se o nome final para cliente sera `Entrada de Notas Recebe Facil` ou outro nome.

Sugestao de wiki:

`Nova Entrada de Notas: mais controle na conferencia do XML`

### 2. Notificacao: Produtos sem venda

Por que pesquisar:

E uma nova notificacao operacional que pode impactar diretamente loja, compras e cadastro de produtos.

Pontos encontrados na fonte:

- Nova notificacao `Produtos sem venda`.
- Identifica itens ativos da loja que nao tiveram venda por PDV ou NFe no periodo configurado.
- Periodo padrao de 30 dias.
- Periodo pode ser ajustado por loja na configuracao da notificacao.
- A notificacao so aparece quando ha historico suficiente para evitar falso positivo.

O que pesquisar antes de escrever:

- Onde configura essa notificacao.
- Se aparece junto das demais notificacoes do Retaguarda.
- Print/gif da configuracao.
- Linguagem simples para o cliente entender que nao e erro, e sim alerta de acompanhamento.

Sugestao de wiki:

`Novo alerta para produtos sem venda`

### 3. Pre-venda: parametros, seguranca e acesso pelo menu

Por que pesquisar:

Ha mudanca de processo e de configuracao. O cliente pode perceber bloqueio quando parametros estiverem incorretos.

Pontos encontrados na fonte:

- Chamada da Pre-Venda no menu `Faturamento > Pre-Venda`.
- Tela de parametros da Pre-Venda.
- Validacao de parametros e melhoria de mensagens.
- Nova seguranca para nao iniciar Pre-Venda quando houver erro nos parametros.
- Tooltips nas opcoes de parametrizacao.
- Ajustes para importacao da Pre-Venda considerar lote, local e variacao.
- Manutencao PDV ganhou campo/flag `USA_PREVENDA`.

O que pesquisar antes de escrever:

- Caminho final da tela de parametros.
- Quais campos aparecem para o cliente.
- Quais mensagens de bloqueio podem aparecer.
- Quando o tecnico deve revisar parametrizacao antes de liberar o uso.

Sugestao de wiki:

`Pre-Venda com validacao de parametros antes de iniciar`

### 4. Cadastro de Produtos: promocao com hora de inicio/fim

Por que pesquisar:

Muda um processo conhecido: promocao deixa de ser apenas por data e passa a ter controle por horario.

Pontos encontrados na fonte:

- Cadastro de produtos recebeu hora na data de promocao.
- Calendario adicionado nas datas inicial e final das promocoes.
- Ajuste referente a `Hora Inicio/Fim da Promocao - Cadastro de Produtos`.
- Novo calendario com controle de data inicio e fim.

O que pesquisar antes de escrever:

- Print dos campos de data/hora da promocao.
- Se o PDV respeita imediatamente a hora ou depende de comunica/carga.
- Como explicar ao cliente que a promocao pode ser programada com mais precisao.

Sugestao de wiki:

`Promocoes com data e horario no Cadastro de Produtos`

### 5. Cadastro de Produtos: avisos/alertas e beneficiamento

Por que pesquisar:

Sao novos controles no cadastro de produtos, visiveis para usuario.

Pontos encontrados na fonte:

- Botao de avisos no Cadastro de Produtos.
- Botao de avisos/Alertas Sistema.
- Checkbox permitindo ou nao usar beneficiamento no item.
- Exibicao do codigo do fornecedor no cadastro de produtos.

O que pesquisar antes de escrever:

- O que aparece dentro do botao de avisos.
- Quando o beneficiamento deve ser marcado.
- Se esses recursos precisam de permissao ou configuracao.
- Quais prints ajudam a evitar duvida do cliente.

Sugestao de wiki:

`Novos controles no Cadastro de Produtos`

### 6. Clientes e Fornecedores: multiplos enderecos

Por que pesquisar:

E mudanca bem perceptivel e facil de explicar. Pode impactar clientes com entrega, cobranca ou cadastro mais completo.

Pontos encontrados na fonte:

- Botao `Multi_enderecos` no Cadastro de Clientes/Fornecedores.
- Cadastro de clientes ajustado para aceitar multiplos enderecos.
- Aba `Cadastros` recebeu opcao `Cadastro de Multi_enderecos`.
- Primeiro upload com recursos de cadastro de enderecos.

O que pesquisar antes de escrever:

- Caminho do cadastro.
- Se os enderecos aparecem em cliente, fornecedor ou ambos.
- Em quais rotinas esses enderecos podem ser usados.
- Print do botao e da tela de cadastro.

Sugestao de wiki:

`Cadastro de clientes e fornecedores com multiplos enderecos`

### 7. Cadastro de Fornecedores: prazo de entrega

Por que pesquisar:

Novo campo simples, mas com impacto em compra/recebimento.

Pontos encontrados na fonte:

- No cadastro de fornecedores, aba detalhes, foi criado o campo `prazo de entregas`.

O que pesquisar antes de escrever:

- Nome exato do campo na tela.
- Se o prazo e apenas informativo ou usado em alguma rotina.
- Print da aba Detalhes.

Sugestao de wiki:

`Novo campo de prazo de entrega no fornecedor`

### 8. DANFE Simplificada e NFC-e Simplificada

Por que pesquisar:

Houve varias mudancas em torno de DANFE simplificada, fechamento de relatorios, convenio, financeiro e cliente novo.

Pontos encontrados na fonte:

- DANFE simplificada no fechamento dos relatorios PDVs.
- Ajustes para gravar cliente novo na DANFE simplificada.
- Diferenciacao de DANFE simplificada com ou sem convenio.
- Checkbox `integra financeiro` na emissao da DANFE, para financeiro novo.
- Relatorio Markup por data nao considera vendas de DANFE simplificada.
- Relatorio Atendidos por Data passou a adicionar DANFE simplificada.
- Parametro/tag relacionado a NFC-e simplificada: `#HAB_OPCAO_NFCE_SIMPLIFICADA=True`.

O que pesquisar antes de escrever:

- O que ficou novo para o usuario final e o que foi apenas correcao.
- Onde aparece a opcao de DANFE/NFC-e simplificada.
- Se o cliente precisa configurar algo para usar.
- Quais relatorios passaram a considerar ou separar essa movimentacao.

Sugestao de wiki:

`DANFE Simplificada integrada a mais rotinas`

### 9. PDV: venda a domicilio, cliente bloqueado e regras de finalizacao

Por que pesquisar:

Alguns pontos impactam diretamente o caixa e podem gerar duvida no atendimento.

Pontos encontrados na fonte:

- Adicionado `F6 + Checkbox` para venda a domicilio no Form do F8.
- Cliente bloqueado nao consegue pagar no caixa.
- Ajustes em convenio e troco quando nao for a ultima finalizadora.
- Parametro/tag `#PERMITE_TRANSACAO_TEF_PDO=False`.
- Regra de NFG: CPF so vai ao XML da NFC-e se a flag `NF_Gaucha` estiver como `S`.

O que pesquisar antes de escrever:

- Quais dessas mudancas foram liberadas para todos ou so para clientes especificos.
- Tela do F8 com venda a domicilio.
- O que o operador do caixa precisa saber.
- Quais mudancas exigem configuracao previa.

Sugestao de wiki:

`Novos controles no PDV para venda e finalizacao`

### 10. Relatorios com novas colunas, filtros ou exportacao

Por que pesquisar:

Pode gerar uma secao curta de melhorias de consulta, caso haja print e utilidade clara.

Pontos encontrados na fonte:

- Relatorio `Estoque > Listagem do saldo de estoque dos produtos` ganhou coluna `Grupo`.
- Ajuste na opcao `Exportar para Excel` do Log de Precos.
- Somatorio da media na coluna Margem e tooltip em relatorios de produtos/grupos vendidos por periodo.
- Ajuste em `Produtos vendidos para clientes identificados`.

O que pesquisar antes de escrever:

- Quais relatorios ficaram visualmente diferentes.
- Se a nova coluna `Grupo` pode fazer alguns relatorios ficarem com mais paginas.
- Prints antes/depois, se houver.

Sugestao de wiki:

`Melhorias em relatorios para analise de vendas e estoque`

### 11. Extrato OFX Verdecard

Por que pesquisar:

E um novo recurso com configuracao obrigatoria, mas talvez seja especifico para poucos clientes.

Pontos encontrados na fonte:

- Criado recurso para obter Extrato OFX do Verdecard.
- Caminho informado: `Utilitarios > Extrato OFX - Verdecard`.
- Exige configuracao de `client id` e `client secret` do cliente.

O que pesquisar antes de escrever:

- Se esse recurso e usado por muitos clientes ou apenas um caso especifico.
- Onde configurar as credenciais.
- Se deve entrar em wiki geral ou wiki separada para Verdecard.

Sugestao de wiki:

`Novo recurso para consulta de Extrato OFX Verdecard`

## Itens bons, mas talvez internos demais

### Inativar todos os centros de custos

Encontrado:

- Recurso em `Utilitarios > Inativar todos os centros de custos`.
- Apenas usuario do suporte tem permissao.

Recomendacao:

Nao colocar em wiki para cliente, a menos que exista procedimento interno para o tecnico usar em atendimento.

### Ajustes de atualizador, compatibilidade, DLL/ZIP/UPD

Recomendacao:

Usar apenas como fonte tecnica. Nao colocar na wiki do cliente, pois nao muda a orientacao operacional.

### Correcoes pontuais de bug

Recomendacao:

So documentar quando o bug antigo gerava comportamento conhecido pelo cliente e a correcao muda a forma de atendimento.

## Possivel indice para a wiki de julho

1. Nova Entrada de Notas
   1.1 Entrada Assistida
   1.2 Etapa de Faturas
   1.3 Lotes
   1.4 Analises e Relatorios
2. Nova Notificacao de Produtos sem Venda
3. Pre-Venda com Validacao de Parametros
4. Cadastro de Produtos
   4.1 Promocoes com Data e Horario
   4.2 Avisos e Beneficiamento
5. Clientes e Fornecedores
   5.1 Multiplos Enderecos
   5.2 Prazo de Entrega do Fornecedor
6. DANFE Simplificada e NFC-e Simplificada
7. Melhorias no PDV
8. Melhorias em Relatorios
9. Extrato OFX Verdecard

## Perguntas que faltam confirmar

- Essa wiki de julho sera para o cliente ler sozinho ou para o tecnico ler em linha?
- A wiki deve cobrir tudo que entrou no beta ate 25/07 ou apenas o que subiu em producao em julho?
- A `Nova Entrada de Notas` deve entrar na wiki de julho ou ficar reservada para a wiki de setembro, ja que ela tambem apareceu como tema principal posterior?
- O recurso Verdecard entra na wiki geral ou fica em material especifico?
- Existem parametros de File Manager confirmados fora desse HTML? No arquivo analisado, encontrei tags/flags e configuracoes, mas nao encontrei a expressao `File Manager` explicitamente.
