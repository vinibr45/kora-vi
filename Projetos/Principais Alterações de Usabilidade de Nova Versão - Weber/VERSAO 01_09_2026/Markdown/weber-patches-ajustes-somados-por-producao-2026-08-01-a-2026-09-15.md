# Weber Patches - cruzamento beta x producao com ajustes somados

## Regra atual

Se houver aplicativo beta sem confirmacao de producao, nao gerar prompt final de imagem/comunicado para esse item. Primeiro listar os pendentes para localizar a tag correta.

Para aplicativos com tag de producao, foram somadas todas as alteracoes do campo `O que mudou` registradas no beta com data/hora menor ou igual a data de envio para producao.

Alteracoes do mesmo aplicativo com data/hora maior que a data de envio para producao foram separadas como `Proximos passos`.

## Resultado geral

- Aplicativos analisados no beta: 33
- Aplicativos com tag de producao: 28
- Alteracoes somadas em versoes de producao: 96
- Alteracoes classificadas como proximos passos: 2
- Aplicativos ainda sem confirmacao de producao: 5

## Pendentes antes de gerar prompt final

- APP_MIGRACAO_FIREBIRD4.ZIP: 1 alteracao(oes) beta sem tag de producao localizada nas fontes analisadas.
- DBIMP.ZIP: 1 alteracao(oes) beta sem tag de producao localizada nas fontes analisadas.
- WGCRESCEVENDAS.ZIP: 1 alteracao(oes) beta sem tag de producao localizada nas fontes analisadas.
- WGESTOQUE.ZIP: 7 alteracao(oes) beta sem tag de producao localizada nas fontes analisadas.
- WPROTRIB.ZIP: 1 alteracao(oes) beta sem tag de producao localizada nas fontes analisadas.

## Arquivos prioritarios

### SERVIDOR.ZIP

- Status: Producao confirmada
- Enviado para producao em: 14/09/2026 08:58:23 por FRANCISCO SCHWARZ MORAES
- Versao listada: 10/09/2026 18:30:06
- Fonte da confirmacao: Portal Gerencial Weber - historico beta SERVIDOR.ZIP
- Alteracoes somadas: 16
- Proximos passos: 0

Alteracoes somadas na versao em producao:
- 03/08/2026 19:40:51: * - Implementada danfe simplificada para poder ficar pendente caso ocorra erro de comuinicacao com se-faz | * - Adicionado upd_220 entrada em Y | * - Adicionado a Mensagem quando item faz faz parte da lei complementar "Operação sujeita ao disposto na LC n° 224 de 2025"
- 05/08/2026 18:29:47: Ajustes no XML para danfe simplificada | tpimp = 6 | Removido tag data e hora saida | Removido tag PISST
- 06/08/2026 12:03:03: Retornado para tpimp=3 para danfe simplificada e adicionada a tag PISST + dthr saida
- 10/08/2026 18:16:28: Ajustado para venda NFCe e DanfeSimplificada no PDV a gravacao na tabela PV_ATEND  para o pre-venda | Adicionado Upd_221
- 12/08/2026 14:03:33: Adicionado UPDs_222,223,224,225
- 13/08/2026 13:53:14: Adicionado UPD_226  com correção de juros/multa no ServerNFe
- 14/08/2026 11:37:09: Retirado excecao no sequencia.ib qdo atingir o limite de alter Table
- 18/08/2026 13:35:39: adicionado upd_227 | ajustado para danfe simplificada, para quando cStat 120  Autorizado o uso da NF-e com Alerta, Retorna Msg de Alerta. | Obs: Atualizar ecf_ws.zip e servidor.zip
- 18/08/2026 14:38:31: Recompilado pacote. ajustado erro no upd_227
- 19/08/2026 14:45:21: 2174 -  No PDV quando consultava o X-MAPA o ServerNFE não estava considerando a Hora.
- 26/08/2026 19:00:20: Adicionado o UPD_228
- 31/08/2026 10:54:26: Adicionado UPD_229 referente notificacao do comunica PDV
- 02/09/2026 17:14:00: Adicionado os UPDs  230 ate 291 referente estoque novo
- 08/09/2026 13:36:53: Ajustado API da listagem do fechamneto Mapa
- 09/09/2026 17:38:24: Adicionado UPD_292, Correcao de lentidao, Cria Indices
- 10/09/2026 18:31:09: Atualizado e substituido os upds 234,249,250

### MENU.ZIP

- Status: Producao confirmada
- Enviado para producao em: 14/09/2026 08:58:19 por FRANCISCO SCHWARZ MORAES
- Versao listada: 10/09/2026 18:32:32
- Fonte da confirmacao: Portal Gerencial Weber - ultimas versoes beta
- Alteracoes somadas: 8
- Proximos passos: 0

Alteracoes somadas na versao em producao:
- 03/08/2026 19:39:02: Feito seguranca na emissao de danfe para situacao pendente | 184 - Relatorio Atendidos por Faixa de Horario adicionar danfe simplificada | 184 - Relatorio Markup por Data adicionar danfe simplificada
- 07/08/2026 00:04:28: Perdia Conexao com BD quando enviava E-Mail nos relatorios antigos
- 10/08/2026 18:21:02: Incluido submenu para Precificação Avançada e Simples
- 13/08/2026 18:38:57: 107 - Ajuste nos relatorios CR antigo.  Pagtos Atrasados, adicionado vlr multa + vlr_correcco + vlr_acrescimo + Juros na coluna acrescimos
- 18/08/2026 13:39:03: 184 - Relatorio Markup por Data adicionar danfe simplificada, ajustado para somar os 2 numa unica linha | Ajustado no Manutencao PDV  a opçao Abertura de Caixa no PDV. | Atualizar menu.zip e ecf_ws.zip
- 28/08/2026 19:55:54: Na EMISSÃO DE NOTA FISCAL]Validação correta da soma de faturas criadas manualmente na emissão da NF-e, passado de float para currency | Ajustado Problema no Cadastro de Produtos, quando fizer insert default do CST sera branco agora | Ajustado Tratamento de exceção de banco de dados (EXC_ESTOQUE_INSUFICIENTE) na inclusão de item sem estoque em Pedidos de Saída | Ajustado Memorizar Layout de Grade (Robô do XML)
- 01/09/2026 15:18:30: Ajustadoo Relatório (Markup por Data) | Refeito Bloqueio de campos fiscais com Weber Tributário habilitado | Alterarado mensagem de except do Banco de Dados na Entrada de Notas | Ajustado Correção na chamada das Formulações de Estoque | Implementado chamada da entrada de notas em Y no Retaguarda(rodar menu senhaa)
- 10/09/2026 18:33:20: Adicionado UUID na tabela EST_MENSAL_APONTA no Apontamento Automático Estoque Negativo

### ECF_WS.ZIP

- Status: Producao confirmada
- Enviado para producao em: 14/09/2026 14:07:17 por FRANCISCO SCHWARZ MORAES
- Versao listada: 14/09/2026 13:31:10
- Fonte da confirmacao: Portal Gerencial Weber - ultimas versoes beta
- Alteracoes somadas: 8
- Proximos passos: 0

Alteracoes somadas na versao em producao:
- 10/08/2026 18:19:10: 2178 - F1  para listar finalizadoras no F8 quando estiver no campo do Codigo Finalizadora | Tela do F8 nao fica mais invisivel, permanece visivel ate final das operacoes
- 18/08/2026 13:42:01: Ajustado para interpretar MSG de alerta da danfe simplificada | Adicionado no menu Finalizadoras a opcao abertura de Caixa, necessita da wgfechacx.dll | Obs:Atualizar menu.zip e ecf_ws.zip e rodar menu senha em ambos
- 24/08/2026 10:09:59: Ajustado para considerar MEI no PDO | Quando PDO e e OFF-Line estava considrando On-Line | Tipo Documento | 55=Danfe | 65=NFCe | 0=PDO, não estava considerando
- 28/08/2026 19:51:57: RN — Alterarado o critério de busca de produtos no F2 do PDV | Ajustado Problema na Emissão de Cupom - Regime MEI para PDO | Ajustado Problema na Emissão de NFC-e com Entrega a Domicílio. rejeição 787 da SEFAZ: | Ajustado Problema no Fluxo de Vendas no PDV (Convênio/Cresce Vendas)
- 01/09/2026 16:12:45: Colocado Default = 1 para o tipo de Impressao | Removido a opção E-Mail | Removido uma Mensagem de Rastreio que havia ficado. Mostrava S ou N
- 04/09/2026 19:12:38: Ajustado BUG no F7 Origem_lcto estava tratando como Inteiro e deveria ser como String
- 09/09/2026 19:30:33: 2178 - Configuração da Opção Padrão no “Questiona Tipo Impressão” foi Ajustado | 39 - Guilhotina dos Comprovantes TEF/Convênio no PDO foi Ajustado
- 14/09/2026 13:31:21: Ajustado para quando nao tiver um default de tipo de impressão, assumir 1 = Imprimir

### WGSYNC.ZIP

- Status: Producao confirmada
- Enviado para producao em: 03/09/2026 18:03:28 por FRANCISCO SCHWARZ MORAES
- Versao listada: 27/08/2026 16:14:32
- Fonte da confirmacao: Portal Gerencial Weber - ultimas versoes beta
- Alteracoes somadas: 1
- Proximos passos: 0

Alteracoes somadas na versao em producao:
- 27/08/2026 16:14:35: - Ajuste no sistema de Logs, incluindo opção de gravação em BD. | - Recompilação do Projeto visando atualizar Utilitarios.cs

### WGCRESCEVENDAS.ZIP

- Status: Beta sem tag de producao localizada
- Alteracoes somadas: 0
- Proximos passos: 0

### WGLCTONOTA.ZIP

- Status: Producao confirmada
- Enviado para producao em: 03/09/2026 18:05:18 por FRANCISCO SCHWARZ MORAES
- Versao listada: 03/09/2026 18:03:14
- Fonte da confirmacao: Portal Gerencial Weber - historico beta WGLCTONOTA.ZIP
- Alteracoes somadas: 20
- Proximos passos: 2

Alteracoes somadas na versao em producao:
- 03/08/2026 15:57:08: A sugestão de CFOP da entrada manual foi ajustada: | UF do fornecedor igual à UF da loja: 5102 | UF diferente: 6102 | ----- | Ajustado para todos os pontos onde seja possível preencher manualmente o campo Documento da fatura limitar a 30 caracteres, tamanho do banco de dados, evitando Overflow. | ----- | Ajustado ordenação da revisão de faturas na entrada assistida e manual. | ---- | Melhorada a busca e associação de produtos:GTIN correspondente não força mais 100% de similaridade. | Descrição passou a representar 98% da similaridade. | UNM e NCM acrescentam 1% cada quando compatíveis. | Divergências de UNM/NCM continuam reduzindo a pontuação. | Incluídos alertas para divergências de descrição, peso/apresentação, unidade, NCM e fornecedor. | Adicionado ícone de sucesso na coluna Critério quando o GTIN corresponde. | ----- | Redesenhada a tela de associação de produtos para resolução mínima de 1000×600 px, com melhor distribuição dos dados e da grade. | ----- | Implementado o bloqueio de valores negativos. | Entrada Manual: frete, seguro, despesas e desconto são rejeitados ao incluir o item; a regra também foi reforçada no cálculo e na validação final. | Auditoria: incluídas validações para custo de compra e todos os campos de ICMS ST. | Salvamento central: valida todas as propriedades decimais dos itens antes de persistir, cobrindo campos preenchidos indiretamente. | ----- | CFOP e CST agora são validados contra os registros ativos de TAB_CFOP e TAB_CST na entrada manual, tanto ao adicionar o item quanto antes de gravar a nota. | Incluídos botões F4 e atalho F4 para pesquisar CFOP e CST na entrada manual. | O CST digitado passou a ser preservado; não é mais substituído silenciosamente pelo CST do produto na entrada manual. | ---- | Analise > Variações preço compra: | Ajustado: o botão agora abre o cadastro com o código do produto da linha selecionada. Sem seleção, exibe um aviso e não abre o cadastro vazio.
- 04/08/2026 11:04:26: ## Entrada de Notas — Configuração Financeira | - Incluída configuração de meio de pagamento e espécie de documento por fornecedor, com prevalência sobre a configuração da loja. | - Permite selecionar ou alterar essas configurações na etapa de faturas das entradas manual e assistida; a seleção da fatura prevalece sobre as configurações padrão. | - Atualizadas as validações e mensagens para orientar a configuração por fornecedor ou loja. | - Na entrada manual, ao alterar o fornecedor, produtos, faturas e configurações financeiras carregadas são limpos.
- 04/08/2026 17:14:17: ---- | Adicionada validação de configuração financeira ao abrir o Controle de Entradas. | Regra central de gravação preservada. | ---- | Raking de produtos comprados: | Corrigida a ordenação do Ranking por valor numérico. | Corrigida a ordenação do Código do Produto. | Corrigida a ordenação cronológica de Última Compra. | ---- | Analise: Variação de preço de compra | Corrigida a ordenação numérica da coluna Produto. | Corrigida a ordenação cronológica de Data de Entrada e Data Anterior. | ---- | Corrigido layout do valor total do item no lançamento manual. | Grades da revisão com redimensionamento de colunas habilitado. | ----
- 05/08/2026 09:23:52: Ajuste overflow na serie da NF na entrada manual.
- 05/08/2026 10:34:57: Ajustado coluna Conv. CFOP da etapa de CFOP/CST da entrada manual, mas segue a situação auto-size.
- 05/08/2026 13:20:47: Corrigido Dashboard: As duas roscas agora reduzem automaticamente o raio interno conforme a área útil do gráfico; em 1366×768 elas permanecem inteiras, sem invadir a grade
- 05/08/2026 16:55:38: - Corrigida a conversão da quantidade do item na tela de lotes da Entrada Assistida. | - Lotes importados do XML agora exibem a quantidade já convertida pelo fator da associação. | - Exemplo: `0,100 MIL × 50` passa a exibir `5,000` unidades. | - Validação de quantidade inteira dos lotes passa a considerar o valor convertido.
- 06/08/2026 10:15:39: - Ajustado responsividade do Dashboard
- 06/08/2026 10:34:15: Ajustado posição das colunas da etapa de conversão CFOP e CST
- 06/08/2026 11:02:53: Adicionado validação da configuração de plano financeiro sugerido ao abrir o módulo, mas mantem validação antes da gravação da entrada.
- 06/08/2026 13:13:08: Bloqueado edição do local e a variação de estoque na auditoria do item.
- 06/08/2026 14:09:49: Adicionado opção "Logs - Auditoria" no Dashboard. | - Esta opção é controlada pela permissão "Consultar logs de auditoria"
- 12/08/2026 15:05:24: - Incluído lançamento, importação e leitura de XML de CT-e modelo 57. | - Implementado vínculo e rateio de CT-e nos itens das NF-es. | - Adicionados frete bruto e crédito tributário do CT-e nos itens de entrada. | - Atualização automática de custos do rateio CT-e e tabelas de preços conforme configurações e produtos associados. | - Auditoria da entrada agora exibe Frete CT-e e Crédito CT-e. | - Fórmulas de Compra e Custo Final disponíveis por tooltip na auditoria, centralizadas com o cálculo para evitar divergências futuras. | - Entrada manual: validação de UF para aceitar somente estados brasileiros válidos. | - Entrada manual: validação de CFOP por origem, bloqueando a inclusão de itens com primeiro dígito diferente na mesma nota. | - Entrada manual: CST/CSOSN filtrado e validado pelo regime tributário do fornecedor, conforme enum próprio do fluxo manual.
- 12/08/2026 17:05:54: -Liberado filtros de Status NF e Tipo/Condição | -Melhorar mensagem de cadastro de Usuario Master ( Especifica o caminho de onde configurar caso não tenha configurado ainda )
- 18/08/2026 15:18:06: Ajuste em NF-es referenciadas no CT-e: | - Grade de NF-e agora exibe valor total, fornecedor e data/hora de lançamento. | - Adicionado “Ver NF-e” ao lado de “Ignorar justificadamente”. | ---------------- | Ajuste em grade “Memória do rateio” no CT-e: | - Agrupa fixamente por versão, sem permitir remover o agrupamento. | - Ordena versões da mais recente para a mais antiga. | - Expande somente a versão mais recente ao carregar. | - Mostra, no rodapé de cada versão, os totais de frete bruto, crédito e frete custo.
- 18/08/2026 15:24:20: Ajuste em NF-es referenciadas no CT-e: | - Grade de NF-e agora exibe valor total, fornecedor e data/hora de lançamento. | - Adicionado “Ver NF-e” ao lado de “Ignorar justificadamente”. | ---------------- | Ajuste em grade “Memória do rateio” no CT-e: | - Agrupa fixamente por versão, sem permitir remover o agrupamento. | - Ordena versões da mais recente para a mais antiga. | - Expande somente a versão mais recente ao carregar. | - Mostra, no rodapé de cada versão, os totais de frete bruto, crédito e frete custo. | ------------- | Ajuste no botão Cancelar CT-e: | -Tooltip no botão “Cancelar CT-e” explicando que o cancelamento é interno, estorna o rateio e altera o status, sem cancelar na SEFAZ. | -Confirmação reforçada com as mesmas informações e a pergunta “Deseja continuar com essas informações?”.
- 19/08/2026 15:55:08: A revisão da entrada assistida agora mostra PIS e COFINS calculados pelas regras de entrada.
- 25/08/2026 15:53:18: Ajuste na validação do ICMs na auditoria do item da entrada de notas
- 26/08/2026 10:04:29: Recompilado devido a desativação da gravação de log em LOG_FORM.
- 03/09/2026 18:02:59: Recompilado por conta de alteração no utilitários para não gravar mais LOG_FORM

Proximos passos:
- 04/09/2026 16:10:52: Desativado obrigatoriamente a loja a ter estoque novo para usar o módulo de controle de entradas
- 11/09/2026 15:05:50: Ajustado botão de cadastro de produtos na tela de associação de código do fornecedor

## Demais aplicativos com producao confirmada

### ATUALIZA.ZIP

- Enviado para producao em: 03/09/2026 17:29:44 por FRANCISCO SCHWARZ MORAES
- Versao listada: 03/09/2026 17:29:46
- Alteracoes somadas: 2
- Proximos passos: 0

### WGSYNCLIB.ZIP

- Enviado para producao em: 03/09/2026 17:59:46 por FRANCISCO SCHWARZ MORAES
- Versao listada: 02/09/2026 09:45:45
- Alteracoes somadas: 2
- Proximos passos: 0

### WGPRODUTOS.ZIP

- Enviado para producao em: 03/09/2026 18:00:14 por FRANCISCO SCHWARZ MORAES
- Versao listada: 01/09/2026 15:44:49
- Alteracoes somadas: 3
- Proximos passos: 0

### WGNOTIFICACOES.ZIP

- Enviado para producao em: 03/09/2026 18:00:43 por FRANCISCO SCHWARZ MORAES
- Versao listada: 31/08/2026 13:25:29
- Alteracoes somadas: 3
- Proximos passos: 0

### SCANTECH.ZIP

- Enviado para producao em: 03/09/2026 18:01:08 por FRANCISCO SCHWARZ MORAES
- Versao listada: 27/08/2026 16:55:18
- Alteracoes somadas: 1
- Proximos passos: 0

### WGFECHACX.ZIP

- Enviado para producao em: 03/09/2026 18:01:12 por FRANCISCO SCHWARZ MORAES
- Versao listada: 27/08/2026 17:45:41
- Alteracoes somadas: 1
- Proximos passos: 0

### WGPRECOS.ZIP

- Enviado para producao em: 03/09/2026 18:01:17 por FRANCISCO SCHWARZ MORAES
- Versao listada: 27/08/2026 17:44:21
- Alteracoes somadas: 2
- Proximos passos: 0

### WGCOMPRAS.ZIP

- Enviado para producao em: 03/09/2026 18:01:24 por FRANCISCO SCHWARZ MORAES
- Versao listada: 27/08/2026 17:22:22
- Alteracoes somadas: 1
- Proximos passos: 0

### PROMIS.ZIP

- Enviado para producao em: 03/09/2026 18:01:30 por FRANCISCO SCHWARZ MORAES
- Versao listada: 28/08/2026 19:52:43
- Alteracoes somadas: 1
- Proximos passos: 0

### WGFINANC.ZIP

- Enviado para producao em: 03/09/2026 18:03:31 por FRANCISCO SCHWARZ MORAES
- Versao listada: 27/08/2026 10:34:50
- Alteracoes somadas: 6
- Proximos passos: 0

### WPAC0001.ZIP

- Enviado para producao em: 03/09/2026 18:03:35 por FRANCISCO SCHWARZ MORAES
- Versao listada: 26/08/2026 19:27:31
- Alteracoes somadas: 1
- Proximos passos: 0

### WGHELPS.ZIP

- Enviado para producao em: 03/09/2026 18:03:39 por FRANCISCO SCHWARZ MORAES
- Versao listada: 26/08/2026 10:52:46
- Alteracoes somadas: 1
- Proximos passos: 0

### WGALERTAS.ZIP

- Enviado para producao em: 03/09/2026 18:03:42 por FRANCISCO SCHWARZ MORAES
- Versao listada: 26/08/2026 10:34:55
- Alteracoes somadas: 2
- Proximos passos: 0

### WG_CONTAS.ZIP

- Enviado para producao em: 03/09/2026 18:03:46 por FRANCISCO SCHWARZ MORAES
- Versao listada: 26/08/2026 10:28:34
- Alteracoes somadas: 1
- Proximos passos: 0

### WG_CCUSTO.ZIP

- Enviado para producao em: 03/09/2026 18:03:50 por FRANCISCO SCHWARZ MORAES
- Versao listada: 26/08/2026 10:27:41
- Alteracoes somadas: 1
- Proximos passos: 0

### WGTABS.ZIP

- Enviado para producao em: 03/09/2026 18:03:53 por FRANCISCO SCHWARZ MORAES
- Versao listada: 26/08/2026 10:25:25
- Alteracoes somadas: 1
- Proximos passos: 0

### WGLOGS.ZIP

- Enviado para producao em: 03/09/2026 18:03:57 por FRANCISCO SCHWARZ MORAES
- Versao listada: 26/08/2026 10:24:25
- Alteracoes somadas: 2
- Proximos passos: 0

### WGREPORT.ZIP

- Enviado para producao em: 03/09/2026 18:04:01 por FRANCISCO SCHWARZ MORAES
- Versao listada: 26/08/2026 10:18:17
- Alteracoes somadas: 4
- Proximos passos: 0

### WGNFE.ZIP

- Enviado para producao em: 03/09/2026 18:04:07 por FRANCISCO SCHWARZ MORAES
- Versao listada: 26/08/2026 10:16:52
- Alteracoes somadas: 2
- Proximos passos: 0

### WGPESSOA.ZIP

- Enviado para producao em: 03/09/2026 18:04:11 por FRANCISCO SCHWARZ MORAES
- Versao listada: 26/08/2026 10:13:59
- Alteracoes somadas: 1
- Proximos passos: 0

### WGPED.ZIP

- Enviado para producao em: 03/09/2026 18:04:15 por FRANCISCO SCHWARZ MORAES
- Versao listada: 26/08/2026 10:11:05
- Alteracoes somadas: 1
- Proximos passos: 0

### WDLLNFE.ZIP

- Enviado para producao em: 14/09/2026 08:58:27 por FRANCISCO SCHWARZ MORAES
- Versao listada: 10/09/2026 16:52:15
- Alteracoes somadas: 3
- Proximos passos: 0

### ATUALIZAPAC.ZIP

- Enviado para producao em: 17/08/2026 13:51:57 por FRANCISCO SCHWARZ MORAES
- Versao listada: 17/08/2026 13:51:54
- Alteracoes somadas: 1
- Proximos passos: 0

