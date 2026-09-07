# Conhecimento operacional — Atendimentos ERP Weber, RAA, IOS e causa raiz

Material preparado para alimentar a Kora/Codex com exemplos reais de atendimento de suporte, preservando contexto técnico útil e omitindo dados sensíveis de clientes, contatos, CNPJ, chaves, acessos e códigos internos quando necessário.

# Atendimento: [NFC-e] Contingência de duplicidade com cupom autorizado na SEFAZ

## Contexto

Atendimentos recorrentes em clientes varejistas utilizando Servidor NFC-e Weber, Frente de Caixa e envio de contingências. A situação aparece quando o cupom já consta autorizado na SEFAZ, mas permanece listado como contingência no servidor.

## Problema relatado

O cliente informa contingências de duplicidade pendentes no Servidor NFC-e e precisa regularizar o envio para liberar a operação.

## Sintomas / Evidências operacionais

- Contingência retornando como duplicidade.
- Cupom já localizado/autorizado na SEFAZ.
- Cupom permanece como contingência no Servidor NFC-e.
- Em um atendimento foi observado que a situação interna do XML ficou como `P`, indicando pendência/aguardo de confirmação.
- Em outro atendimento foi identificado ID de duplicidade informado pelo sistema.
- Em alguns casos foi necessário conferir se o valor do cupom no sistema batia com o valor autorizado na SEFAZ.

## Impacto

Gera acúmulo de contingências, insegurança no fechamento e risco de o suporte precisar fazer conferências manuais repetitivas para validar algo que o próprio sistema poderia consultar oficialmente.

## Classificação sugerida

- Subtipo: Contingência NFC-e
- Módulo: Servidor NFC-e
- Rotina/Tela: Envio de contingências
- Categoria do problema: Divergência entre status local e autorização SEFAZ
- Tags sugeridas: NFC-e, contingência, duplicidade, SEFAZ, protocolo, status XML
- Frequência: Recorrente
- Risco de recorrência: Alto

## Análise realizada

Foi validado que a duplicidade não significava necessariamente uma venda duplicada. O comportamento observado indica que o cupom pode estar autorizado na SEFAZ, mas o servidor local permanece com status de contingência por não atualizar corretamente protocolo, XML ou situação.

Em alguns atendimentos o contorno foi usar o validador do próprio Servidor NFC-e. Em outros, após confirmar que o documento estava correto na SEFAZ e no sistema, a contingência foi removida para regularizar a fila.

## Solução aplicada

Quando disponível, foi utilizado o caminho no Servidor NFC-e:

Botão direito na contingência > Enviar > Validar/Verificar chave selecionada > Enviar contingência.

Nos casos em que a validação confirmou que o cupom já estava autorizado corretamente, a pendência foi tratada para não continuar presa como contingência.

## Tipo de solução

Contorno operacional

## Status da causa raiz

Parcialmente identificada

## Existe documentação?

Parcial

## Aprendizado para base de conhecimento

Duplicidade em contingência não deve ser tratada automaticamente como venda duplicada. O primeiro passo é confirmar se o XML/cupom está autorizado na SEFAZ e se os valores batem com o sistema. Quando a autorização existe, o problema pode estar na atualização local de protocolo, XML ou situação do cupom.

## Possível problema conhecido

Sim.

- Título padrão: NFC-e autorizada na SEFAZ permanece como contingência de duplicidade
- Campos preenchidos automaticamente: Módulo Servidor NFC-e, categoria Status local divergente da SEFAZ, frequência recorrente, risco alto
- Evidências obrigatórias: número do cupom, série/caixa, retorno de duplicidade, consulta oficial SEFAZ, valor autorizado, valor no sistema, status exibido no Servidor NFC-e
- Solução padrão: consultar NFC-e pelo XML/chave, atualizar protocolo/XML/status quando autorizado e reenviar/regularizar a contingência por ação oficial do servidor
- Observações: evitar depender de validação manual em banco ou procura no mapa resumo quando o servidor puder executar consulta oficial

## Observações de melhoria para o IOS/RAA

Criar campo específico para “cupom consta na SEFAZ?” e outro para “status local do servidor”. Também seria útil uma ação no menu de contingências chamada “Consultar NFC-e pelo XML e atualizar protocolo/status”, registrando evidência e usuário que executou a consulta.

# Atendimento: [NFC-e] Contingências da loja antiga bloqueando fechamento após migração

## Contexto

Cliente migrado de código de loja/CNPJ antigo para novo cadastro. Permaneceram contingências antigas vinculadas à loja anterior no Servidor NFC-e.

## Problema relatado

Após a migração, o cliente ficou com contingências antigas presas no servidor, vinculadas à loja anterior, impedindo o fechamento dos caixas.

## Sintomas / Evidências operacionais

- Contingências associadas ao código e CNPJ da loja antiga.
- Rejeição: “Emitente não autorizado para emissão de NFC-e”.
- CNPJ antigo baixado/desativado.
- XMLs da loja antiga foram preservados em pasta de segurança antes de solicitar intervenção.
- Desenvolvimento acionado para exclusão/tratamento das contingências antigas.

## Impacto

O cliente não conseguia concluir fechamento de caixa enquanto as contingências antigas permaneciam ativas no Servidor NFC-e.

## Classificação sugerida

- Subtipo: Pós-migração de loja/CNPJ
- Módulo: Servidor NFC-e
- Rotina/Tela: Contingências e fechamento de caixa
- Categoria do problema: Pendência fiscal antiga bloqueando operação atual
- Tags sugeridas: NFC-e, contingência, migração CNPJ, loja antiga, fechamento de caixa
- Frequência: Pontual com alto risco em migrações
- Risco de recorrência: Médio

## Análise realizada

Foi verificado que as contingências pertenciam ao emitente antigo. Como o CNPJ anterior estava baixado, a autorização pela SEFAZ não era mais possível com os dados fiscais originais. Antes da solicitação ao desenvolvimento, os XMLs antigos foram salvos para preservar histórico.

## Solução aplicada

Foi solicitado ao desenvolvimento remover/tratar as contingências antigas da loja anterior para deixar o servidor sem pendências e permitir o fechamento dos caixas.

## Tipo de solução

Encaminhado para desenvolvimento

## Status da causa raiz

Identificada

## Existe documentação?

Parcial

## Aprendizado para base de conhecimento

Em migração de CNPJ/loja, contingências antigas devem ser analisadas antes da virada. Se o CNPJ antigo estiver baixado, elas podem ficar impossibilitadas de autorização e bloquear rotinas operacionais da nova loja. É importante salvar XMLs antes de qualquer limpeza.

## Possível problema conhecido

Sim.

- Título padrão: Contingências de loja antiga bloqueiam fechamento após migração de CNPJ
- Campos preenchidos automaticamente: Módulo Servidor NFC-e, subtipo Pós-migração, risco operacional alto
- Evidências obrigatórias: loja antiga, loja nova, rejeição SEFAZ, confirmação de XML salvo, impacto no fechamento
- Solução padrão: preservar XMLs antigos e solicitar tratamento controlado pelo desenvolvimento
- Observações: não substituir dados fiscais da contingência antiga pelos dados da loja nova

## Observações de melhoria para o IOS/RAA

Criar checklist de migração com etapa obrigatória “verificar contingências antes da troca de CNPJ/loja” e campo para indicar se os XMLs antigos foram salvos.

# Atendimento: [PDV] Cupom já existente no Mapa bloqueia nova venda

## Contexto

Atendimento em Frente de Caixa na versão informada pelo usuário como 25.05.2026. O cliente tentava finalizar uma venda em loja cheia, exigindo liberação rápida do caixa.

## Problema relatado

O PDV não finalizava a venda porque informava que o cupom já estava no Mapa.

## Sintomas / Evidências operacionais

- Mensagem/comportamento: cupom já estava no Mapa.
- Cupom informado já constava no Mapa Resumo.
- Cupom já havia sido enviado para o servidor.
- O problema ocorreu durante operação com cliente aguardando no caixa.
- Não houve tempo para aprofundar causa raiz no momento.

## Impacto

Venda travada no PDV e necessidade de liberar rapidamente a operação para o cliente continuar vendendo.

## Classificação sugerida

- Subtipo: Numeração de cupom
- Módulo: Frente de Caixa / Fiscal
- Rotina/Tela: Finalização de venda e Mapa Resumo
- Categoria do problema: Reutilização ou divergência de numeração fiscal
- Tags sugeridas: PDV, cupom, mapa resumo, numeração, venda travada
- Frequência: Não informado
- Risco de recorrência: Alto

## Análise realizada

Foi confirmado que o cupom citado realmente já existia no Mapa e havia sido enviado para o servidor. Como a loja estava cheia, a prioridade operacional foi liberar o PDV. A causa de o caixa tentar reutilizar a numeração não foi identificada durante o atendimento.

## Solução aplicada

Com usuário de suporte no PDV, a numeração do cupom foi ajustada manualmente para o próximo número disponível. Após isso, o cliente conseguiu emitir normalmente.

## Tipo de solução

Contorno operacional

## Status da causa raiz

Não identificada

## Existe documentação?

Não localizada

## Aprendizado para base de conhecimento

Quando o PDV acusa cupom já existente no Mapa, é necessário confirmar no Mapa Resumo se a numeração realmente já foi utilizada e se o envio ao servidor ocorreu. O ajuste manual da numeração libera a operação, mas deve gerar demanda de investigação porque existe risco fiscal e risco de recorrência.

## Possível problema conhecido

Sim.

- Título padrão: PDV tenta emitir cupom com numeração já existente no Mapa
- Campos preenchidos automaticamente: Módulo Frente de Caixa, categoria Numeração fiscal, risco alto
- Evidências obrigatórias: versão do PDV, número do cupom, caixa/série, tela do erro, Mapa Resumo comprovando existência, último cupom emitido antes/depois
- Solução padrão: confirmar numeração no Mapa e ajustar para o próximo número apenas em caráter emergencial
- Observações: sempre abrir investigação posterior para entender por que a numeração retornou ou ficou divergente

## Observações de melhoria para o IOS/RAA

Criar campo “houve liberação emergencial?” e “causa raiz investigada depois?”. O IOS também deveria marcar esse tipo de chamado como candidato automático a análise de causa raiz.

# Atendimento: [DANFE simplificada/TEF] Rejeição fiscal trava caixa após pagamento TEF

## Contexto

Atendimento em PDV com emissão de DANFE simplificada e pagamento T.E.F. A venda envolvia divergência de unidade de medida/quantidade/valor.

## Problema relatado

Cliente estava com PDV parado ao tentar emitir uma DANFE simplificada com pagamento TEF.

## Sintomas / Evidências operacionais

- DANFE simplificada retornou rejeição por unidade de medida diferente.
- Divergência fazia o valor total do produto não bater com a quantidade.
- Caixa travou durante a operação.
- Houve débito na conta do cliente final por causa do TEF.
- Cliente reclamou que ainda não funcionava, mas aceitou a orientação.

## Impacto

Impacto crítico: PDV travado, risco financeiro por pagamento TEF debitado e necessidade de orientar estorno ao consumidor.

## Classificação sugerida

- Subtipo: Emissão fiscal com pagamento TEF
- Módulo: Frente de Caixa / NF-e / TEF
- Rotina/Tela: DANFE simplificada
- Categoria do problema: Rejeição fiscal após autorização/fluxo de pagamento
- Tags sugeridas: DANFE simplificada, TEF, rejeição, unidade de medida, estorno
- Frequência: Não informado
- Risco de recorrência: Alto

## Análise realizada

A rejeição fiscal ocorreu após tentativa de emissão da DANFE simplificada. A divergência de unidade/quantidade/valor impediu a conclusão fiscal, enquanto o fluxo financeiro TEF já havia movimentado o pagamento.

## Solução aplicada

Cliente foi orientada a verificar o estorno do valor debitado, emitir um cupom da compra e depois transformar o cupom em DANFE.

## Tipo de solução

Contorno operacional

## Status da causa raiz

Parcialmente identificada

## Existe documentação?

Parcial

## Aprendizado para base de conhecimento

Em fluxos com TEF, a rejeição fiscal após pagamento tem impacto maior que uma rejeição comum. O atendimento precisa registrar se houve débito, se houve orientação de estorno e qual caminho fiscal foi usado para concluir a operação.

## Possível problema conhecido

Sim.

- Título padrão: DANFE simplificada rejeitada após pagamento TEF por divergência de unidade/valor
- Campos preenchidos automaticamente: Módulo PDV/NF-e/TEF, categoria Rejeição fiscal pós-pagamento
- Evidências obrigatórias: rejeição fiscal, forma de pagamento, comprovante/retorno TEF quando disponível, produto/unidade/quantidade/valor, status da venda
- Solução padrão: orientar verificação de estorno e emitir cupom para posterior transformação em DANFE quando aplicável
- Observações: avaliar melhoria de validação antes de acionar pagamento TEF

## Observações de melhoria para o IOS/RAA

Criar campo obrigatório para atendimentos TEF: “houve débito ao consumidor?” e “foi orientado estorno?”. Também seria importante um alerta preventivo no sistema validando unidade, quantidade e total antes de iniciar pagamento.

# Atendimento: [TEF] Erro de data inválida ao finalizar cupom

## Contexto

Atendimento em Frente de Caixa com TEF e integração com finalizadora. O caso foi acompanhado com orientação de técnico interno e investigação junto à fornecedora de TEF.

## Problema relatado

Cliente relatou erro no TEF no momento da finalização da venda.

## Sintomas / Evidências operacionais

- Erro informado: `NEGADO:ERRO:EXCEPT NO SERVER INSERT CUPOM FINALIZADORA ''is not a valid date.`
- Falha ocorre na finalização do cupom.
- Técnico interno estava verificando com a fornecedora do TEF o motivo do problema.

## Impacto

Venda não finaliza normalmente, podendo travar operação de caixa e exigir tratamento manual posterior.

## Classificação sugerida

- Subtipo: Integração TEF
- Módulo: Frente de Caixa / TEF
- Rotina/Tela: Finalização de venda
- Categoria do problema: Erro de integração ao gravar finalizadora
- Tags sugeridas: TEF, finalizadora, data inválida, cupom, Destaxa
- Frequência: Não informado
- Risco de recorrência: Médio

## Análise realizada

O erro indica falha na gravação/envio de dados da finalizadora com campo de data inválido ou vazio. A causa raiz não foi determinada no atendimento e ficou em análise com suporte da integração TEF.

## Solução aplicada

Cliente foi orientada de que, se o erro ocorrer novamente, deve colocar o caixa em modo contingência e enviar a contingência para o servidor, permitindo ajuste manual posterior.

## Tipo de solução

Contorno operacional

## Status da causa raiz

Não identificada

## Existe documentação?

Não localizada

## Aprendizado para base de conhecimento

Mensagens de TEF com erro de data devem registrar o texto completo, momento exato da finalização e integração envolvida. O contorno por contingência pode manter a operação funcionando enquanto a causa é investigada.

## Possível problema conhecido

Sim.

- Título padrão: TEF retorna erro de data inválida ao inserir cupom finalizadora
- Campos preenchidos automaticamente: Módulo TEF/PDV, categoria Integração de pagamento
- Evidências obrigatórias: mensagem completa, horário, PDV, forma de pagamento, retorno TEF, versão do PDV e integração TEF
- Solução padrão: orientar contingência e encaminhar evidências para análise da integração
- Observações: investigar se o campo de data está vazio, em formato inválido ou vindo da integração externa

## Observações de melhoria para o IOS/RAA

Criar campo para “fornecedor TEF” e “etapa da transação” porque isso ajuda a separar erro de autorização, erro de finalização e erro de gravação local.

# Atendimento: [Entrada de notas/SPED] Nota de entrada importada com valores zerados

## Contexto

Cliente recebeu apontamento da contabilidade durante validação do SPED Fiscal ICMS. A análise foi feita em nota de entrada dentro do período informado para geração do arquivo.

## Problema relatado

Contabilidade informou problemas no SPED Fiscal ICMS, incluindo ausência de CFOP e falta dos registros `C175` e `C150`.

## Sintomas / Evidências operacionais

- Nota apontada pela contabilidade estava com valor total igual a zero.
- Todos os produtos da nota também estavam com valor zerado.
- O problema foi descrito como recorrente na entrada de notas.
- Não houve print registrado no atendimento.
- A contabilidade já havia ajustado manualmente no programa de validação fiscal.

## Impacto

Geração de SPED com inconsistência, retrabalho da contabilidade e risco de envio fiscal com registros incompletos ou incorretos.

## Classificação sugerida

- Subtipo: Validação fiscal preventiva
- Módulo: Entrada de Notas / Fiscal
- Rotina/Tela: Entrada de notas e geração SPED Fiscal ICMS
- Categoria do problema: Documento fiscal com valores zerados
- Tags sugeridas: SPED, entrada de notas, valores zerados, CFOP, C150, C175
- Frequência: Recorrente
- Risco de recorrência: Alto

## Análise realizada

Foi analisada a nota indicada pela contabilidade e constatado que o problema não era apenas de SPED, mas de origem na entrada da nota: os valores estavam zerados. Ao apagar os produtos e reimportar a nota, os valores foram carregados corretamente.

Também foram revisadas outras notas do período e orientada a configuração de notas de remessa para não movimentar estoque quando os produtos já estavam no estoque.

## Solução aplicada

Os produtos da nota foram excluídos e a nota foi reimportada. Após a reimportação, os valores dos itens entraram corretamente. A cliente gerou novo SPED e enviou para a contabilidade validar.

## Tipo de solução

Correção técnica

## Status da causa raiz

Parcialmente identificada

## Existe documentação?

Não localizada

## Aprendizado para base de conhecimento

Quando o SPED aponta ausência de registros ou campos fiscais, deve-se validar a origem na nota de entrada antes de tratar apenas o arquivo SPED. Nota total e itens zerados podem gerar ausência ou inconsistência nos registros fiscais.

## Possível problema conhecido

Sim.

- Título padrão: Nota de entrada com valores zerados gera inconsistência no SPED Fiscal
- Campos preenchidos automaticamente: Módulo Entrada de Notas/Fiscal, categoria Valores zerados
- Evidências obrigatórias: período do SPED, nota afetada, total da nota, valores dos itens, CFOP dos itens, erro do validador
- Solução padrão: reimportar nota após remover itens incorretos e gerar novo SPED para validação
- Observações: demanda sugerida para validação automática das notas do período antes da geração do SPED

## Observações de melhoria para o IOS/RAA

Criar validação preventiva na geração do SPED para listar notas de entrada com total zerado, todos os itens zerados, divergência entre total dos itens e total da nota ou ausência de CFOP.

# Atendimento: [Entrada de notas] Produto com código divergente por zero à esquerda

## Contexto

Atendimento relacionado à entrada de notas em que o produto aparecia com zero à esquerda na nota, mas no cadastro de produtos constava sem o zero. O caso precisou de apoio de desenvolvimento para ajuste via banco de dados.

## Problema relatado

Cliente não conseguia cadastrar ou vincular corretamente um produto específico porque o código na entrada da nota possuía zero à esquerda, enquanto no cadastro o mesmo produto aparecia sem esse zero.

## Sintomas / Evidências operacionais

- Código do produto na entrada da nota iniciava com zero.
- Cadastro de produto apresentava o código sem o zero inicial.
- Produto específico não era localizado/vinculado como esperado.
- Foi confirmado posteriormente que o cadastro de produto e o Weber Tributário ficaram corretos após o ajuste.

## Impacto

Impedia a entrada correta da nota e exigia intervenção técnica para alinhar cadastro, tributação e identificação do produto.

## Classificação sugerida

- Subtipo: Cadastro de produto
- Módulo: Entrada de Notas / Cadastro de Produtos / Weber Tributário
- Rotina/Tela: Vinculação/cadastro de produto na entrada
- Categoria do problema: Divergência de código por formatação
- Tags sugeridas: produto, zero à esquerda, entrada de notas, cadastro, Weber Tributário
- Frequência: Não informado
- Risco de recorrência: Médio

## Análise realizada

A comparação entre entrada da nota e cadastro mostrou divergência de formatação do código. O produto era tratado como diferente por causa do zero inicial, mesmo representando o mesmo item.

## Solução aplicada

Foi aberta solicitação para desenvolvimento ajustar o cadastro via banco de dados. Em retorno posterior, foi mostrado ao cliente que o problema estava resolvido e que o cadastro no Weber Tributário também estava correto.

## Tipo de solução

Correção técnica

## Status da causa raiz

Parcialmente identificada

## Existe documentação?

Não localizada

## Aprendizado para base de conhecimento

Códigos com zero à esquerda precisam ser tratados com cuidado, pois o sistema pode interpretar o valor como numérico em uma tela e como texto em outra. A evidência principal é comparar como o código aparece na entrada da nota, no cadastro e nas integrações tributárias.

## Possível problema conhecido

Sim.

- Título padrão: Produto com zero à esquerda diverge entre entrada de nota e cadastro
- Campos preenchidos automaticamente: Módulo Entrada de Notas/Cadastro, categoria Divergência de identificador
- Evidências obrigatórias: código mascarado na nota, código mascarado no cadastro, tela de vínculo, tela do Weber Tributário
- Solução padrão: encaminhar para desenvolvimento quando exigir ajuste de cadastro/banco
- Observações: não expor código completo do produto quando o chamado for usado como base de conhecimento

## Observações de melhoria para o IOS/RAA

Criar campo “tipo de código do produto” e “há zero à esquerda?” para problemas de cadastro, principalmente em entrada de notas e tributação.

# Atendimento: [Entrada fiscal] Nota com unidade e operação divergentes do esperado

## Contexto

Cliente recebeu nota de fornecedor com unidade de medida diferente da habitual e natureza de operação divergente do que o fornecedor havia informado verbalmente. A decisão fiscal dependia da cliente e da contabilidade.

## Problema relatado

Cliente informou que sempre comprava o produto em unidade, mas o fornecedor enviou a nota em quilogramas. O fornecedor disse que seria bonificação, porém a nota veio com CFOP de venda de mercadoria e destaque de ICMS.

## Sintomas / Evidências operacionais

- Unidade informada na nota: KG.
- Operação esperada pela cliente: bonificação.
- Documento emitido pelo fornecedor: CFOP de venda.
- ICMS destacado.
- Valor do produto de bonificação informado como R$ 0,01.
- Cliente não quis gerar Contas a Pagar nem atualizar preço de custo.
- Cliente realizou a entrada aproveitando crédito de ICMS.
- Não foi feita conversão de unidade; foi habilitada unidade fracionada no cadastro do produto conforme solicitação da cliente.

## Impacto

Risco de lançamento fiscal/estoque diferente da operação esperada, possível reflexo em ICMS, custo, financeiro e unidade de estoque.

## Classificação sugerida

- Subtipo: Entrada fiscal com divergência de documento
- Módulo: Entrada de Notas / Cadastro de Produtos
- Rotina/Tela: Entrada de nota e cadastro de unidade
- Categoria do problema: Documento do fornecedor divergente da operação esperada
- Tags sugeridas: entrada de notas, bonificação, CFOP, ICMS, unidade fracionada
- Frequência: Não informado
- Risco de recorrência: Médio

## Análise realizada

Foi separado o que era decisão fiscal da cliente/contabilidade e o que era configuração operacional do sistema. O suporte ajustou a entrada para atender à movimentação solicitada, sem alterar informações fiscais do documento recebido. A cliente foi orientada de que correções de CFOP, tributação ou unidade fiscal devem ser tratadas com fornecedor e contabilidade.

## Solução aplicada

A entrada foi realizada sem gerar Contas a Pagar e sem atualizar custos. Foi habilitada unidade fracionada no cadastro do produto para permitir a entrada da nota como recebida. A cliente manteve o aproveitamento de crédito conforme decisão dela/contabilidade.

## Tipo de solução

Correção de cadastro/configuração

## Status da causa raiz

Não aplicável

## Existe documentação?

Parcial

## Aprendizado para base de conhecimento

Em notas com divergência entre o que o fornecedor disse e o que consta no XML, o suporte deve documentar claramente a decisão da cliente/contabilidade: financeiro, custo, crédito de ICMS, unidade e conversão. O sistema deve registrar o documento recebido, mas a responsabilidade fiscal de correção da nota é do fornecedor/contabilidade.

## Possível problema conhecido

Parcialmente. Pode virar guia de atendimento, mais do que problema conhecido técnico.

- Título padrão: Entrada de nota com operação informada pelo fornecedor diferente do XML recebido
- Campos preenchidos automaticamente: Módulo Entrada de Notas, categoria Divergência fiscal/documental
- Evidências obrigatórias: CFOP da nota, unidade do XML, decisão sobre Contas a Pagar, decisão sobre custo, decisão sobre crédito de ICMS, orientação da contabilidade
- Solução padrão: registrar conforme documento recebido e decisão fiscal, sem alterar informações fiscais sem respaldo
- Observações: evitar que a RAA pareça que o suporte decidiu tratamento fiscal sozinho

## Observações de melhoria para o IOS/RAA

Adicionar campos estruturados para “gerou financeiro?”, “atualizou custo?”, “houve conversão de unidade?”, “houve orientação da contabilidade?” e “crédito de ICMS foi aproveitado?”.

# Atendimento: [NF-e rural] Contranota referenciando NF-e de produtor rural

## Contexto

Cliente precisava emitir contranota de produtor rural. Diferente do processo anterior, o produtor havia emitido uma NF-e, exigindo ajuste no passo de referência.

## Problema relatado

Cliente tinha dúvidas sobre como enviar/fazer contranota de produto rural quando o produtor já havia emitido NF-e.

## Sintomas / Evidências operacionais

- Produtor rural emitiu NF-e.
- Cliente deu entrada da nota no sistema.
- No passo de referência do produtor rural, foi necessário marcar que era NF-e.
- Chave da nota de entrada foi informada no processo.
- Nota foi emitida com sucesso.

## Impacto

Sem orientação correta, havia risco de emissão incorreta da contranota ou duplicidade de escrituração/estoque.

## Classificação sugerida

- Subtipo: Contranota rural
- Módulo: NF-e / Entrada de Notas
- Rotina/Tela: Emissão de contranota e referência de produtor rural
- Categoria do problema: Dúvida operacional fiscal
- Tags sugeridas: NF-e, contranota, produtor rural, referência de chave
- Frequência: Recorrente em clientes com produtor rural
- Risco de recorrência: Médio

## Análise realizada

Foi acompanhado o fluxo com o cliente em linha. A principal diferença foi ajustar o passo de referência para NF-e e utilizar a chave da nota de entrada emitida pelo produtor.

## Solução aplicada

Cliente deu entrada na nota e, no passo de referência, marcou que se tratava de NF-e, colou a chave da nota de entrada e emitiu a contranota com sucesso.

## Tipo de solução

Orientação ao usuário

## Status da causa raiz

Não aplicável

## Existe documentação?

Parcial

## Aprendizado para base de conhecimento

Quando o produtor rural emite NF-e, o processo de contranota muda no passo de referência. A base de conhecimento deve diferenciar produtor com nota própria, produtor sem nota e cenário em que contabilidade orienta qual documento movimenta estoque/fiscal.

## Possível problema conhecido

Não como problema técnico. Sim como procedimento operacional.

- Título padrão: Emissão de contranota rural quando produtor emitiu NF-e
- Campos preenchidos automaticamente: Módulo NF-e, categoria Dúvida fiscal operacional
- Evidências obrigatórias: existência da NF-e do produtor, chave de acesso mascarada, orientação contábil quando houver, confirmação de entrada da nota
- Solução padrão: referenciar como NF-e e informar chave da nota de entrada
- Observações: confirmar com contabilidade se a entrada fiscal deve usar NF-e do produtor ou contranota, para evitar duplicidade

## Observações de melhoria para o IOS/RAA

Criar subtipo específico “Produtor rural / contranota” e campo “produtor emitiu NF-e?”.

# Atendimento: [Rede/Servidor] Retaguarda sem conexão por VPN apontando para IP antigo

## Contexto

Atendimento envolvendo cliente/parceiro externo tentando conectar ao retaguarda. Havia VPN configurada para endereço antigo do servidor após queda de internet no cliente.

## Problema relatado

Usuária informou que não conseguia conectar ao retaguarda.

## Sintomas / Evidências operacionais

- Retaguarda não conseguia conectar ao host servidor.
- VPN estava conectada a um IP antigo do servidor do cliente.
- Responsável do mercado informou que houve queda de internet.
- Novo IP gerado na ponta do cliente era diferente do IP configurado na VPN.

## Impacto

Impossibilidade de acessar o retaguarda remotamente pela VPN configurada.

## Classificação sugerida

- Subtipo: Conectividade VPN
- Módulo: Infraestrutura / Retaguarda
- Rotina/Tela: Acesso ao host servidor
- Categoria do problema: VPN apontando para endereço desatualizado
- Tags sugeridas: VPN, retaguarda, host servidor, IP, queda de internet
- Frequência: Pontual
- Risco de recorrência: Médio

## Análise realizada

Foi comparado o IP configurado na VPN com o novo IP disponível na ponta do cliente após a queda de internet. A divergência justificava a falha de conexão ao host servidor.

## Solução aplicada

O novo IP da VPN foi informado para a parte responsável acionar o TI deles e refazer a configuração.

## Tipo de solução

Orientação ao usuário

## Status da causa raiz

Identificada

## Existe documentação?

Não localizada

## Aprendizado para base de conhecimento

Quando o retaguarda não conecta ao servidor via VPN após queda de internet, validar primeiro se o IP público/endpoint mudou. Nem todo erro de conexão indica problema no retaguarda ou no servidor Weber.

## Possível problema conhecido

Sim.

- Título padrão: Retaguarda não conecta ao servidor porque VPN aponta para IP antigo
- Campos preenchidos automaticamente: Módulo Infraestrutura/Retaguarda, categoria Conectividade
- Evidências obrigatórias: IP configurado na VPN mascarado, novo IP informado pelo cliente mascarado, teste de conexão, confirmação de queda de internet
- Solução padrão: orientar TI do cliente/parceiro a atualizar endpoint da VPN
- Observações: não registrar IP completo em base de conhecimento pública/interna ampla

## Observações de melhoria para o IOS/RAA

Criar campo “ambiente acessado por VPN?” e “houve mudança de IP/queda de internet?”.

# Atendimento: [Rede/PDV] Lentidão no envio de cupom relacionada a caixas e switch

## Contexto

Cliente relatou lentidão para imprimir/enviar cupons ao Servidor NFC-e. O ambiente possuía servidor e retaguarda com desempenho melhor que os caixas, e os caixas passavam por um switch.

## Problema relatado

Cliente informou lentidão para imprimir cupons, especificamente no envio do cupom para o Servidor NFC-e.

## Sintomas / Evidências operacionais

- Caixas aparentavam ser muito lentos em comparação com servidor e retaguarda.
- Cliente informou que havia um switch conectado aos caixas.
- Servidor e retaguarda ficavam antes desse switch.
- Testes de ping mostraram intermitência/variação de alguns milissegundos entre caixas e servidor.

## Impacto

Lentidão no processo de emissão/impressão de cupons e possível impacto no atendimento de frente de caixa.

## Classificação sugerida

- Subtipo: Desempenho de rede no PDV
- Módulo: Frente de Caixa / Servidor NFC-e / Infraestrutura
- Rotina/Tela: Envio de cupom para servidor
- Categoria do problema: Latência/intermitência de rede local
- Tags sugeridas: PDV, lentidão, NFC-e, ping, switch, rede
- Frequência: Não informado
- Risco de recorrência: Médio

## Análise realizada

Foi feita comparação de desempenho entre caixas, servidor e retaguarda. A topologia informada pelo cliente indicou que o switch poderia ser ponto de atenção, já que os caixas estavam depois dele. Testes de ping mostraram variação/intermitência.

## Solução aplicada

Cliente foi orientado a buscar técnico local e retornar em data combinada para evidenciar o comportamento e realizar testes no switch.

## Tipo de solução

Solução parcial

## Status da causa raiz

Parcialmente identificada

## Existe documentação?

Não localizada

## Aprendizado para base de conhecimento

Lentidão de emissão de cupom nem sempre é problema fiscal. Deve-se comparar desempenho de estação, servidor e caminho de rede. Switch, Wi-Fi, cabo e máquina lenta podem afetar envio ao servidor.

## Possível problema conhecido

Sim.

- Título padrão: Lentidão no envio de cupom por instabilidade entre PDV e servidor
- Campos preenchidos automaticamente: Módulo PDV/Infraestrutura, categoria Rede/desempenho
- Evidências obrigatórias: teste de ping, topologia simplificada, equipamento intermediário, comparação com outra estação, horário de maior lentidão
- Solução padrão: testar rede local com técnico do cliente e isolar switch/cabo/porta
- Observações: registrar se servidor está antes ou depois do switch problemático

## Observações de melhoria para o IOS/RAA

Adicionar campo para “tipo de conexão do PDV” e “resultado do ping”. Também seria útil um campo simples de topologia: PDV > switch > servidor ou PDV > roteador > servidor.

# Atendimento: [Firebird] Recuperação de banco corrompido com procedimento R4

## Contexto

Atendimento em cliente com banco Firebird 2.5 corrompido. Foi seguido procedimento documentado em Wiki interna.

## Problema relatado

Cliente estava com banco de dados corrompido.

## Sintomas / Evidências operacionais

- Base Firebird 2.5 com corrupção.
- Procedimento R4 foi aplicado.
- Orientação operacional conhecida: realizar backup, renomear banco para `v` e executar o R4.
- Após execução do procedimento, a base foi recuperada.

## Impacto

Risco de indisponibilidade do sistema e perda de operação até recuperação da base.

## Classificação sugerida

- Subtipo: Banco corrompido
- Módulo: Banco de Dados / Infraestrutura
- Rotina/Tela: Recuperação Firebird
- Categoria do problema: Corrupção de base
- Tags sugeridas: Firebird 2.5, R4, banco corrompido, backup, recuperação
- Frequência: Não informado
- Risco de recorrência: Médio

## Análise realizada

Foi identificado que o caso se enquadrava no procedimento de recuperação R4 para Firebird 2.5. Antes da execução, foi realizado backup e preservação do banco original.

## Solução aplicada

Após backup, o banco foi renomeado para `v` e o R4 foi executado conforme Wiki interna. A base corrompida foi recuperada.

## Tipo de solução

Correção técnica

## Status da causa raiz

Não analisada

## Existe documentação?

Sim

## Aprendizado para base de conhecimento

Procedimentos de recuperação de banco precisam registrar obrigatoriamente se houve backup antes, qual versão do Firebird, qual script/procedimento foi utilizado e se o sistema voltou a operar.

## Possível problema conhecido

Sim.

- Título padrão: Recuperação de banco Firebird 2.5 corrompido com R4
- Campos preenchidos automaticamente: Módulo Banco de Dados, categoria Recuperação de base, documentação Sim
- Evidências obrigatórias: versão Firebird, erro/comportamento de corrupção, confirmação de backup, resultado após R4
- Solução padrão: seguir Wiki interna de R4, sempre com backup prévio
- Observações: causa raiz da corrupção deve ser registrada separadamente quando houver tempo/evidência

## Observações de melhoria para o IOS/RAA

Criar checklist obrigatório para banco corrompido: backup realizado, caminho validado, versão Firebird, tempo de parada, resultado do procedimento e recomendação preventiva.

# Atendimento: [PDV] Arquivo de configuração corrompido após desligamento inesperado

## Contexto

Atendimento em PDV em que o ícone do caixa desapareceu após desligamento inesperado. Foi identificado problema no arquivo de configuração do caixa.

## Problema relatado

Cliente informou que o ícone do caixa desapareceu.

## Sintomas / Evidências operacionais

- Computador sofreu desligamento inesperado.
- Arquivo de configuração de caixa foi corrompido.
- Necessário usar arquivo `ECFCFG.CFG` de outra máquina funcionando.
- Necessário executar `ecf_ws config` na pasta do PDV para reconfigurar.
- Último cupom emitido foi conferido no Retaguarda em Fiscal > Mapa Resumo.

## Impacto

Caixa indisponível até reconstrução da configuração, com risco de configuração incorreta de impressora, cliente, CNPJ e numeração.

## Classificação sugerida

- Subtipo: Configuração de PDV corrompida
- Módulo: Frente de Caixa / Retaguarda Fiscal
- Rotina/Tela: Configuração do PDV e Mapa Resumo
- Categoria do problema: Corrupção de arquivo local
- Tags sugeridas: PDV, ECFCFG.CFG, ecf_ws config, desligamento inesperado, Mapa Resumo
- Frequência: Não informado
- Risco de recorrência: Médio

## Análise realizada

Foi relacionado o desligamento inesperado com corrupção do arquivo de configuração. Para reconstruir o caixa com segurança, foi usada configuração base de uma estação funcional e conferido o último cupom no Mapa Resumo.

## Solução aplicada

Foi copiado o `ECFCFG.CFG` de uma máquina funcionando, executado `ecf_ws config`, reconfigurado o PDV, impressora, código do cliente/CNPJ e numeração. O último cupom foi validado pelo Mapa Resumo antes do teste.

## Tipo de solução

Correção técnica

## Status da causa raiz

Identificada

## Existe documentação?

Parcial

## Aprendizado para base de conhecimento

Ao recuperar configuração de PDV, a numeração fiscal precisa ser conferida no Mapa Resumo antes do teste. Copiar arquivo de outra máquina sem conferir cliente, CNPJ, impressora e último cupom pode gerar nova divergência.

## Possível problema conhecido

Sim.

- Título padrão: PDV perde configuração após desligamento inesperado e corrupção do ECFCFG
- Campos preenchidos automaticamente: Módulo PDV, categoria Configuração local corrompida
- Evidências obrigatórias: indício de desligamento inesperado, ausência do ícone/configuração, máquina usada como base, último cupom conferido, teste final
- Solução padrão: copiar configuração base, executar configurador e validar numeração pelo Mapa Resumo
- Observações: pode virar Wiki com passo a passo e alerta sobre numeração fiscal

## Observações de melhoria para o IOS/RAA

Criar campo “houve desligamento inesperado?” e “último cupom validado no Mapa?” para casos de reconstrução de PDV.

# Atendimento: [Servidor NFE/Robo XML] Alerta de versões diferentes causado por executável incorreto

## Contexto

Cliente possuía duas lojas na mesma máquina. O Servidor NFE apresentava erro de versões diferentes entre Robo XML e Server NFE, embora as versões estivessem iguais.

## Problema relatado

Cliente estava com erro de versões diferentes entre Robo XML e Server NFE.

## Sintomas / Evidências operacionais

- Sistema indicava divergência de versão entre Robo XML e Server NFE.
- Ao verificar, as versões estavam iguais.
- Existiam duas lojas configuradas na mesma máquina.
- O servidor estava puxando executável diferente do Robo XML.

## Impacto

Impossibilidade ou instabilidade no uso correto do Robo XML/Servidor NFE até carregar o executável certo.

## Classificação sugerida

- Subtipo: Executável incorreto em ambiente multi-loja
- Módulo: Servidor NFE / Robo XML
- Rotina/Tela: Inicialização do Servidor NFE
- Categoria do problema: Caminho/processo carregado incorretamente
- Tags sugeridas: Robo XML, Servidor NFE, versão, multi-loja, executável
- Frequência: Não informado
- Risco de recorrência: Médio

## Análise realizada

Foi validado que a mensagem de versão não representava, de fato, versões diferentes. A hipótese correta foi carregamento do executável errado por haver duas lojas na mesma máquina.

## Solução aplicada

O Servidor NFE foi parado, fechado e iniciado novamente. Após reiniciar corretamente, ele puxou o Robo XML correto.

## Tipo de solução

Contorno operacional

## Status da causa raiz

Parcialmente identificada

## Existe documentação?

Não localizada

## Aprendizado para base de conhecimento

Quando houver erro de versão entre Robo XML e Servidor NFE, confirmar a versão real e o caminho/executável carregado. Em ambiente com múltiplas lojas na mesma máquina, o problema pode ser apontamento incorreto, não atualização pendente.

## Possível problema conhecido

Sim.

- Título padrão: Servidor NFE acusa versão diferente por carregar Robo XML de outra loja
- Campos preenchidos automaticamente: Módulo Servidor NFE/Robo XML, categoria Ambiente multi-loja
- Evidências obrigatórias: versões exibidas, caminho do executável, quantidade de lojas na máquina, comportamento após reinício
- Solução padrão: fechar completamente e iniciar Servidor NFE validando executável correto
- Observações: avaliar melhoria para exibir caminho do executável carregado no erro

## Observações de melhoria para o IOS/RAA

Adicionar campo “há mais de uma loja na mesma máquina?” para erros de versão/apontamento.

# Atendimento: [Parâmetros] Reestruturação do File Manager por tags em BLOB

## Contexto

Pesquisa interna sobre o modelo atual do File Manager para parâmetros do sistema. Hoje diversos comportamentos são configurados por tags manuais armazenadas em campo BLOB.

## Problema relatado

O File Manager permite configuração manual de tags como texto, sem validação estruturada, catálogo de parâmetros, tipo de dado, descrição, valores aceitos ou escopo.

## Sintomas / Evidências operacionais

- Parâmetros armazenados no campo `CONFIG2` da tabela `ARQCONF`.
- Formato observado: `#NOME_DA_TAG=VALOR`.
- Banco armazena o texto, mas regras e valores aceitos ficam no código da aplicação.
- Recepção pode colocar tag qualquer por falta de conhecimento técnico, apenas para encaminhar chamado.
- Dificuldade de identificar parâmetros válidos, obsoletos, duplicados ou conflitantes.

## Impacto

Aumenta erro de configuração, dependência de conhecimento individual, dificuldade de suporte, auditoria fraca, documentação incompleta e risco de chamados classificados por tags erradas.

## Classificação sugerida

- Subtipo: Melhoria estrutural de configuração
- Módulo: Configurações / File Manager
- Rotina/Tela: Parâmetros do sistema
- Categoria do problema: Configuração sem catálogo e validação
- Tags sugeridas: File Manager, parâmetros, CONFIG2, ARQCONF, tags, auditoria
- Frequência: Estrutural
- Risco de recorrência: Alto

## Análise realizada

Foi percebido que o problema não é apenas visual. Criar uma tela em cima do BLOB manteria a fragilidade. A solução adequada é criar estrutura de banco para catálogo, valores, opções e histórico, permitindo janela de parâmetros com tipo, escopo, validação e auditoria.

## Solução aplicada

Foi elaborada RN sugerindo nova estrutura com tabelas de parâmetro, valores, opções e histórico, além de migração gradual das tags atuais para modelo estruturado.

## Tipo de solução

Encaminhado para desenvolvimento

## Status da causa raiz

Identificada

## Existe documentação?

Parcial

## Aprendizado para base de conhecimento

Parâmetros manuais em texto são origem de erro operacional e de classificação. Uma base de conhecimento deve registrar nome amigável, chave técnica, tipo, módulo, efeito, valor padrão, necessidade de reinício e impacto no PDV/servidor.

## Possível problema conhecido

Sim, como problema estrutural.

- Título padrão: Parâmetros por tags no File Manager dificultam validação, suporte e auditoria
- Campos preenchidos automaticamente: Módulo Configurações, categoria Parametrização estrutural
- Evidências obrigatórias: tag usada, comportamento esperado, comportamento obtido, módulo afetado, valor configurado, origem da orientação
- Solução padrão: migrar para janela estruturada de parâmetros com validação e histórico
- Observações: tags usadas na recepção não devem substituir classificação real do problema

## Observações de melhoria para o IOS/RAA

Separar “tag técnica do sistema” de “categoria do chamado”. O IOS deve permitir classificação por módulo, rotina, sintoma e causa, sem depender de uma tag escolhida manualmente por quem não conhece o parâmetro.

# Atendimento: [Precificação] Reajuste de preço em massa sem lucro, estoque e filtros seguros

## Contexto

Cliente consultou dúvidas sobre precificação e uso da ferramenta de Reajuste de preço em massa. O caso gerou RN de melhoria de produto.

## Problema relatado

Cliente queria usar o Reajuste de preço em massa, mas a ferramenta não mostrava cálculo de lucro nem quantidade em estoque na grade.

## Sintomas / Evidências operacionais

- Produto com markup de 20% apresentou lucro negativo.
- Foi identificado débito alto no produto, superior a R$ 7, afetando o lucro.
- Ferramenta de reajuste em massa não exibia lucro na grade.
- Ferramenta também não exibia quantidade em estoque.
- Cliente queria filtros por grupo/setor para aplicar ajustes com mais segurança.
- Foi levantada preocupação com produtos em encarte ou promoção.
- Foi solicitada existência de logs para alterações feitas pela ferramenta.

## Impacto

Risco de alteração em massa com baixa visibilidade, alteração de produtos promocionais/encarte, perda de margem e dificuldade de auditoria.

## Classificação sugerida

- Subtipo: Melhoria de ferramenta
- Módulo: Precificação
- Rotina/Tela: Reajuste de preço em massa
- Categoria do problema: Falta de visibilidade e controle em alteração em massa
- Tags sugeridas: precificação, reajuste em massa, lucro, estoque, log, promoção, encarte
- Frequência: Não informado
- Risco de recorrência: Alto

## Análise realizada

Foi explicado que o lucro negativo não era causado pelo markup em si, mas pelo débito alto do produto. A demanda principal, porém, era a limitação da ferramenta de reajuste, que não fornece dados suficientes para tomada de decisão segura.

## Solução aplicada

Foi aberta RN solicitando adicionar coluna de lucro, quantidade em estoque, filtros por grupo/setor, logs de alteração e tratamento para produtos com encarte ou promoção.

## Tipo de solução

Encaminhado para desenvolvimento

## Status da causa raiz

Identificada

## Existe documentação?

Não localizada

## Aprendizado para base de conhecimento

Ferramentas de alteração em massa precisam exibir indicadores de risco antes da confirmação. Em precificação, lucro, estoque, promoção, encarte e log são dados essenciais para evitar alteração cega.

## Possível problema conhecido

Não como erro técnico, mas sim como melhoria conhecida de produto.

- Título padrão: Reajuste de preço em massa sem lucro e estoque na grade
- Campos preenchidos automaticamente: Módulo Precificação, categoria Melhoria de segurança operacional
- Evidências obrigatórias: tela da grade, exemplo de produto, markup aplicado, lucro exibido em outra rotina, existência de promoção/encarte
- Solução padrão: encaminhar melhoria para desenvolvimento
- Observações: registrar impacto comercial, não apenas dúvida do cliente

## Observações de melhoria para o IOS/RAA

Criar tipo de chamado “melhoria de segurança operacional” para ferramentas de alteração em massa, com campos de impacto, risco e logs necessários.

# Atendimento: [Escrita Fiscal] Overview de entrada de notas para nova funcionária

## Contexto

Cliente solicitou apoio para nova funcionária entender o processo de entrada de notas pela escrita fiscal. Foi feito overview, não treinamento completo.

## Problema relatado

Nova funcionária precisava entender o fluxo básico de entrada de notas.

## Sintomas / Evidências operacionais

- Dúvidas gerais sobre Robo XML.
- Dúvidas sobre conversão de CST e CFOP.
- Dúvidas sobre entrada dos produtos.
- Dúvidas resumidas sobre precificação.
- Dúvidas sobre exclusão de nota lançada.
- Foi explicado que, para excluir nota, é necessário excluir itens, Contas a Pagar e depois deletar a nota.

## Impacto

Sem conhecimento do fluxo, há risco de entrada incorreta de notas, custos, fiscal, financeiro e estoque.

## Classificação sugerida

- Subtipo: Orientação operacional
- Módulo: Escrita Fiscal / Entrada de Notas
- Rotina/Tela: Robo XML, entrada de notas, precificação e exclusão de nota
- Categoria do problema: Treinamento/uso do sistema
- Tags sugeridas: entrada de notas, Robo XML, CST, CFOP, precificação, exclusão
- Frequência: Recorrente
- Risco de recorrência: Alto

## Análise realizada

Foi identificado que a necessidade era ampla demais para um atendimento pontual. O suporte apresentou uma visão geral e orientou que, se necessário, o cliente deve marcar treinamento para passo a passo completo.

## Solução aplicada

Foi demonstrado o fluxo resumido de entrada via Robo XML, conversão CST/CFOP, entrada de produtos, noções de precificação e exclusão de nota lançada.

## Tipo de solução

Orientação ao usuário

## Status da causa raiz

Não aplicável

## Existe documentação?

Parcial

## Aprendizado para base de conhecimento

Atendimentos de overview devem ser classificados diferente de incidentes. Quando o tema é amplo, a RAA precisa registrar o limite da orientação e sugerir treinamento formal.

## Possível problema conhecido

Não como problema técnico. Sim como trilha de treinamento.

- Título padrão: Overview de entrada de notas para novo usuário
- Campos preenchidos automaticamente: Módulo Escrita Fiscal, categoria Treinamento/orientação
- Evidências obrigatórias: tópicos abordados, limite do atendimento, recomendação de treinamento
- Solução padrão: orientar fluxo básico e sugerir treinamento quando necessário
- Observações: não misturar com incidente de erro sistêmico

## Observações de melhoria para o IOS/RAA

Criar categoria “Treinamento breve / overview” para não contaminar métricas de erro do sistema com dúvidas operacionais.

# Atendimento: [Financeiro] Recibo de contas a pagar não preenche histórico de baixa nas observações

## Contexto

Cliente queria reimprimir recibo de Contas a Pagar com histórico de baixa aparecendo nas observações do recibo.

## Problema relatado

Cliente queria que, ao imprimir recibo de Contas a Pagar, o histórico de baixa fosse junto nas observações.

## Sintomas / Evidências operacionais

- Caminho demonstrado: Financeiro > Contas a Pagar > localizar lançamento quitado > abrir lançamento > Opções > Imprimir recibo.
- O recibo abre com campos em branco, como CNPJ pagador, CNPJ recebedor e observações.
- Ao clicar em “preencher com os dados do lançamento”, o sistema preenche pagante e cedente.
- O campo observações permanece em branco.
- Histórico de baixa é informação diferente do campo de observação do recibo.

## Impacto

Usuário precisa preencher manualmente observações ou imprimir recibo sem histórico, prejudicando rastreabilidade e conferência financeira.

## Classificação sugerida

- Subtipo: Melhoria de impressão
- Módulo: Financeiro
- Rotina/Tela: Contas a Pagar / Imprimir recibo
- Categoria do problema: Informação não reaproveitada no documento
- Tags sugeridas: contas a pagar, recibo, histórico de baixa, observações
- Frequência: Não informado
- Risco de recorrência: Médio

## Análise realizada

Foi explicado que o histórico de baixa e as observações do recibo são campos diferentes. A necessidade do usuário é que o botão de preencher dados traga também o histórico de baixa.

## Solução aplicada

Foi demonstrado o procedimento atual de impressão e aberta RN solicitando que o histórico de baixa venha junto ao preencher os dados do lançamento.

## Tipo de solução

Encaminhado para desenvolvimento

## Status da causa raiz

Identificada

## Existe documentação?

Não localizada

## Aprendizado para base de conhecimento

Nem toda dúvida de uso é erro; às vezes o comportamento atual está correto tecnicamente, mas incompleto para o fluxo operacional do usuário.

## Possível problema conhecido

Não como erro. Pode virar melhoria conhecida.

- Título padrão: Recibo de Contas a Pagar não preenche histórico de baixa nas observações
- Campos preenchidos automaticamente: Módulo Financeiro, categoria Melhoria de impressão
- Evidências obrigatórias: lançamento quitado, tela do recibo em branco, resultado após preencher dados, histórico de baixa existente
- Solução padrão: orientar preenchimento manual até melhoria ser implementada
- Observações: esclarecer diferença entre histórico de baixa e observação de recibo

## Observações de melhoria para o IOS/RAA

Criar campo “comportamento atual x comportamento desejado” para RNs de melhoria.

# Atendimento: [Periféricos] Balança de check-in afetada por suspensão seletiva USB

## Contexto

Cliente relatou que balança de check-in não funcionava. O atendimento envolveu teste de porta, teste no caixa e configuração de energia do Windows.

## Problema relatado

Balança de check-in não estava funcionando.

## Sintomas / Evidências operacionais

- Teste na porta da balança comunicava normalmente.
- Teste no caixa funcionava normalmente.
- Opções avançadas de energia do Windows estavam com suspensão seletiva de USB ativada.

## Impacto

Interrupção intermitente ou aparente falha de comunicação da balança, afetando operação de pesagem/check-in.

## Classificação sugerida

- Subtipo: Periférico USB
- Módulo: PDV / Balança / Windows
- Rotina/Tela: Teste balança e balança de check-in
- Categoria do problema: Economia de energia interrompendo comunicação USB
- Tags sugeridas: balança, USB, suspensão seletiva, Windows, check-in
- Frequência: Recorrente em ambiente Windows
- Risco de recorrência: Médio

## Análise realizada

Como a balança comunicava no teste e no caixa, a falha não parecia ser da balança nem da porta lógica. A configuração de energia do Windows era compatível com interrupção de alimentação USB.

## Solução aplicada

A suspensão seletiva de energia USB foi desativada e o cliente foi orientado sobre a possibilidade de esse recurso causar interrupções.

## Tipo de solução

Correção de cadastro/configuração

## Status da causa raiz

Identificada

## Existe documentação?

Parcial

## Aprendizado para base de conhecimento

Quando periférico USB falha intermitentemente, testar comunicação antes de reinstalar driver. Se comunica em teste, verificar energia do Windows pode resolver sem troca de hardware.

## Possível problema conhecido

Sim.

- Título padrão: Balança USB falha por suspensão seletiva de energia do Windows
- Campos preenchidos automaticamente: Módulo Periféricos, categoria Configuração Windows
- Evidências obrigatórias: teste de porta, teste no sistema, status da suspensão USB, resultado após desativar
- Solução padrão: desativar suspensão seletiva USB nas opções avançadas de energia
- Observações: orientar cliente/técnico local quando houver recorrência após reinício ou troca de porta

## Observações de melhoria para o IOS/RAA

Criar checklist para periféricos USB: porta, driver, teste do sistema, energia USB, troca física e reinício.

# Padrões encontrados

## Problemas recorrentes

- Contingências NFC-e com status local divergente da SEFAZ.
- Duplicidade em contingência quando o cupom já está autorizado.
- Necessidade de validar XML/protocolo/status sem depender de banco ou mapa.
- Problemas pós-migração de loja/CNPJ com contingências antigas.
- Rejeições fiscais que travam operação de caixa ou fechamento.
- Entrada de notas causando reflexo posterior em SPED, estoque, financeiro e tributação.
- Falhas de conectividade estação/servidor por Wi-Fi, VPN, IP alterado ou switch.
- Configurações locais do PDV corrompidas após desligamento inesperado.
- Periféricos USB afetados por porta, driver, energia ou hardware.
- Dúvidas operacionais que viram atendimento, mas na prática são necessidade de treinamento.
- RNs surgindo de limitações de usabilidade, logs, validação e auditoria.

## Falhas no registro atual da RAA

- Falta de prints ou evidências em atendimentos críticos.
- Erro completo nem sempre é registrado.
- Versão do sistema nem sempre aparece.
- Nem sempre é informado se houve impacto financeiro, fiscal ou apenas operacional.
- Não fica claro se a solução foi definitiva, contorno ou encaminhamento.
- Causa raiz costuma ficar misturada com procedimento aplicado.
- Falta registrar quais hipóteses foram testadas.
- Falta registrar quando o cliente/contabilidade tomou uma decisão fiscal.
- Chamados de dúvida, treinamento, incidente e melhoria ficam parecidos.
- Tags são usadas como classificação principal mesmo quando não representam o problema real.
- Em casos de contingência, nem sempre fica claro se o cupom consta na SEFAZ.
- Em casos de rede, falta registrar topologia, tipo de conexão e teste de ping.
- Em casos de banco, falta checklist de backup, versão e resultado.

## Campos que deveriam existir no IOS

- Módulo afetado.
- Rotina/tela.
- Tipo de atendimento: incidente, dúvida, treinamento, RN, contorno, desenvolvimento.
- Categoria do problema independente de tag.
- Sintoma principal.
- Mensagem de erro completa.
- Versão do sistema.
- Ambiente: servidor, estação, PDV, loja, multi-loja.
- Impacto operacional.
- Impacto fiscal.
- Impacto financeiro/TEF.
- Cliente parado: sim/não.
- Fechamento de caixa bloqueado: sim/não.
- Cupom consta na SEFAZ: sim/não/não verificado.
- XML/protocolo atualizado localmente: sim/não/não verificado.
- Houve pagamento TEF debitado: sim/não/não informado.
- Houve orientação de estorno: sim/não/não aplicável.
- Causa raiz: identificada, parcial, não identificada, não analisada, não aplicável.
- Tipo de solução aplicada.
- Evidências anexadas.
- Necessita desenvolvimento: sim/não.
- Necessita treinamento: sim/não.
- Houve contabilidade envolvida: sim/não.
- Decisão fiscal foi do cliente/contabilidade: sim/não.
- Documentação existente: sim, não, parcial, desatualizada, não localizada.
- Problema conhecido relacionado.
- Recorrência percebida pelo suporte.

## Títulos padronizados sugeridos

- [NFC-e] Cupom autorizado na SEFAZ permanece como contingência de duplicidade
- [NFC-e] Contingências da loja antiga bloqueiam fechamento após migração
- [PDV] Cupom já existente no Mapa bloqueia finalização da venda
- [DANFE/TEF] Rejeição fiscal após pagamento trava o caixa
- [TEF] Erro de data inválida ao gravar cupom finalizadora
- [SPED] Nota de entrada com valores zerados gera inconsistência fiscal
- [Entrada de Notas] Produto com zero à esquerda diverge do cadastro
- [Entrada Fiscal] Documento do fornecedor diverge da operação esperada
- [NF-e Rural] Contranota referenciando NF-e emitida pelo produtor
- [Rede] VPN aponta para IP antigo e impede conexão ao servidor
- [PDV/Rede] Lentidão no envio de cupom por instabilidade entre caixa e servidor
- [Banco] Recuperação de base Firebird corrompida com R4
- [PDV] Configuração local corrompida após desligamento inesperado
- [Servidor NFE] Robo XML de outra loja causa alerta de versão
- [Configurações] Tags do File Manager dificultam validação e auditoria
- [Precificação] Reajuste em massa sem lucro, estoque e filtros seguros
- [Financeiro] Recibo de Contas a Pagar não preenche histórico de baixa
- [Periféricos] Balança USB falha por suspensão seletiva do Windows

## Categorias de problema sugeridas

- Contingência NFC-e
- Divergência de status SEFAZ x servidor local
- Rejeição fiscal em PDV
- Erro pós-pagamento TEF
- Numeração fiscal divergente
- Migração de loja/CNPJ
- Entrada fiscal inconsistente
- Validação SPED
- Cadastro de produto divergente
- Unidade de medida e conversão
- CFOP/CST/operação fiscal
- Conectividade estação-servidor
- VPN/IP/rede externa
- Lentidão de PDV
- Banco de dados corrompido
- Configuração local de PDV
- Periférico USB/serial
- Parâmetro/File Manager
- Melhoria de usabilidade
- Falta de log/auditoria
- Treinamento/orientação

## Evidências operacionais recomendadas

Para NFC-e/contingência:

- Número do cupom, caixa/série e data.
- Status no Servidor NFC-e.
- Retorno SEFAZ.
- Confirmação se consta autorizado na SEFAZ.
- Valor no sistema e valor autorizado.
- XML/protocolo quando disponível, sem expor chave completa em base de conhecimento.
- Ação executada: validar chave, verificar chave, reenviar, excluir, encaminhar desenvolvimento.

Para TEF:

- Mensagem completa de erro.
- Fornecedor/integração TEF.
- Forma de pagamento.
- Se houve débito ao consumidor.
- Se houve orientação de estorno.
- Status fiscal da venda.
- Horário e PDV.

Para entrada de notas/SPED:

- Período fiscal.
- Nota afetada, sem expor chave completa.
- Valor total da nota.
- Valores dos itens.
- CFOP/CST quando for parte do problema.
- Erro do validador SPED.
- Se houve reimportação.
- Se contabilidade validou ou orientou.

Para PDV/mapa:

- Versão do PDV.
- Número do cupom.
- Último cupom emitido antes/depois.
- Tela do erro.
- Mapa Resumo confirmando existência.
- Se houve ajuste manual emergencial.

Para rede/infraestrutura:

- Tipo de conexão: cabo, Wi-Fi, VPN.
- Teste de ping.
- Topologia resumida.
- Alteração recente de IP/internet.
- Máquina afetada e comparação com outra máquina.
- Se há switch, roteador ou VPN no caminho.

Para banco Firebird:

- Versão do Firebird.
- Sintoma de corrupção.
- Confirmação de backup.
- Procedimento aplicado.
- Resultado final.
- Tempo de indisponibilidade quando informado.

Para periféricos:

- Modelo do equipamento.
- Porta usada antes/depois.
- Teste no utilitário e teste no sistema.
- Driver reinstalado ou não.
- Configuração de energia USB.
- Resultado após reinício.

## Possíveis métricas futuras

- Chamados por módulo e rotina.
- Chamados por categoria real do problema, sem depender apenas de tags.
- Percentual de chamados com causa raiz identificada.
- Percentual de chamados resolvidos por contorno operacional.
- Frequência de contingências por cliente, loja, caixa e versão.
- Quantidade de casos em que NFC-e constava na SEFAZ mas ficou pendente localmente.
- Tempo médio para liberar cliente parado.
- Chamados com impacto fiscal.
- Chamados com impacto financeiro/TEF.
- Chamados com falta de evidência obrigatória.
- Reabertura por solução parcial ou causa raiz não identificada.
- Demandas de desenvolvimento originadas de recorrência.
- Top problemas conhecidos por versão.
- Rotinas com maior necessidade de treinamento.
- Chamados gerados por falha de infraestrutura do cliente.
- Chamados em que contabilidade/fornecedor definiu o procedimento fiscal.
- Taxa de uso de documentação/Wiki por atendimento.
- Lacunas de documentação mais frequentes.

