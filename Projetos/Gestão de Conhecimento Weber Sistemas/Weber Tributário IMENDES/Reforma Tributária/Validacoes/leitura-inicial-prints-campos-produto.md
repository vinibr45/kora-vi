# Leitura Inicial Dos Prints - Campos Tributarios De Produto

## Status

precisa confirmar

## Fonte

Pasta:

```text
C:\Kora\kora-vi\Projetos\Gestão de Conhecimento Weber Sistemas\Weber Tributário IMENDES\Reforma Tributária\Prints
```

Arquivos analisados:

```text
PRODUTOS ICMS.png
PRODUTOS PIS COFINS.png
PRODUTOS IBS CBS.png
```

## Entendimento Geral

Os prints mostram o cadastro/configuração fiscal de um produto no sistema WEBER, usando como exemplo o produto:

```text
Código Produto: 58
Nome/Descrição: ABACATE KG
Unidade de medida: KG
NCM: 0804.40.00
Grupo: 01.04 - HORTIFRUTI-FRUTAS
Fornecedor: TRANSANTA TRANSPORTE E COMERCIO DE FRUTAS LTDA - 834
```

O cadastro possui campos fiscais tradicionais, como ICMS, PIS e COFINS, e também uma área nova/relacionada à Reforma Tributária para configurações CBS/IBS.

## Tela Principal Do Cadastro De Produtos

Nos prints `PRODUTOS ICMS.png` e `PRODUTOS PIS COFINS.png`, aparece a tela:

```text
Cadastro de produtos Loja:01
```

Ela possui abas como:

```text
ICMs
PisCofins
Estoque
Detalhes
Validade
ConvCodigo
Kit
PrecoQtd
Precos
```

Também aparecem controles e campos gerais do produto:

- código do produto;
- código de preço;
- código de estoque;
- descrição;
- abreviação;
- unidade;
- NCM;
- CEST;
- grupo;
- fornecedor;
- estoque atual;
- mínimo;
- máximo;
- status de sincronização do Weber Tributário;
- opção `Habilita WeberTrib.`;
- botão `WeberTributário`;
- botão `ReformaTributária`;
- botão `Logs de alterações`.

## Entendimento Sobre Weber Tributário

A tela mostra sinais de integração com o Weber Tributário:

- checkbox `WeberTrib.Sincronizado`;
- data/hora de sincronização;
- checkbox `Habilita WeberTrib.`;
- botão `WeberTributário`.

Interpretação inicial:

O produto pode estar habilitado para integração com o Weber Tributário, e o sistema registra se houve sincronização/atualização fiscal relacionada ao serviço.

Precisa confirmar:

- se `WeberTrib.Sincronizado` indica atualização realizada pela IMENDES via Weber Tributário;
- se `Habilita WeberTrib.` permite que esse produto receba atualização fiscal automática;
- se o botão `WeberTributário` abre detalhes da integração, consulta, histórico ou comparação fiscal.

## Aba ICMS

No print `PRODUTOS ICMS.png`, a aba `ICMs` mostra campos ligados à tributação de ICMS no cupom eletrônico.

Campos visíveis:

- `ICMs No Cupom Eletronico`;
- CST;
- CSON;
- Trib;
- ICMS(%);
- PBC(%);
- Aliq.Final(%);
- FCP(%);
- MVA;
- IPI(%);
- tipo do produto;
- IBPT(%);
- benefício;
- descrição do código de benefício.

Também aparece a informação:

```text
CST: 040 PBC: 0% ALIQ: 0%
```

Interpretação inicial:

Esta aba representa a configuração fiscal tradicional de ICMS do produto, incluindo CST/CSOSN, alíquotas, benefício fiscal e classificação do tipo de produto.

Precisa confirmar:

- quais campos são atualizados pelo Weber Tributário/IMENDES;
- quais campos são editados manualmente pela equipe;
- como o benefício fiscal se relaciona com as regras da IMENDES;
- se `IBPT(%)` vem de outra fonte ou também entra no fluxo do Weber Tributário.

## Aba PIS/COFINS

No print `PRODUTOS PIS COFINS.png`, a aba `PisCofins` mostra configurações fiscais para entrada e saída.

Campos visíveis:

- `Pis e Cofins na Entrada`;
- CST-E;
- Aliq.Pis;
- PBC(%);
- Aliq.Cofins;
- PBC(%);
- `Pis e Cofins na Saida`;
- CST-S;
- Aliq.Pis;
- PBC(%);
- Aliq.Cofins;
- PBC(%);
- `Pis e Cofins Natureza da Receita`;
- Nat.Receita;
- Cod.ANP;
- descrição do código ANP.

Valores visíveis no exemplo:

```text
Entrada: 73 - Operação de Aquisição a Alíquota Zero
Saída: 06 - Operação Tributável a Alíquota Zero
Natureza da Receita: 116 - Produtos hortícolas e frutas
```

Interpretação inicial:

Esta aba define regras de PIS/COFINS tanto para entrada quanto para saída do produto, incluindo CST de entrada, CST de saída, alíquotas e natureza da receita.

Precisa confirmar:

- se a IMENDES recomenda CST de entrada, CST de saída e natureza da receita;
- se a WEBER aplica essas informações diretamente no cadastro;
- se alíquotas zeradas neste exemplo decorrem da categoria do produto ou de regra específica.

## Tela CBS/IBS

No print `PRODUTOS IBS CBS.png`, aparece uma janela separada:

```text
Configurações Fiscais por Produto
```

Ela traz uma seção:

```text
Configuração Tributária CBS/IBS
Configuração CBS/IBS para operação venda presencial para consumidor final
```

Campos visíveis:

- classificação tributária CBS/IBS;
- descrição CST;
- alíquota CBS;
- opção `Usar alíquota CBS personalizada (?)`;
- redução CBS/IBS:
  - `% Redução Aliq IBS`;
  - `% Redução Aliq CBS`;
- alíquota IBS Municipal;
- opção `Usar alíquota Municipal personalizada (?)`;
- alíquota IBS UF;
- opção `Usar alíquota IBS UF personalizada (?)`;
- opção `LEI COMPLEMENTAR 224/2025. (?)`;
- botões `Cancelar` e `Salvar`.

Valores visíveis no exemplo:

```text
Classificação Tributária CBS/IBS:
000001 - Situações tributadas integralmente pelo IBS e CBS.

Descrição CST:
CST 000 - Tributação integral.

Alíquota CBS:
0,9000

Alíquota IBS Municipal:
0,0000

Alíquota IBS UF:
0,1000

Redução Aliq IBS:
0,0000

Redução Aliq CBS:
0,0000
```

Interpretação inicial:

Esta tela parece ser o layout novo/relacionado à Reforma Tributária para configurar CBS e IBS por produto, especificamente para operação de venda presencial para consumidor final.

Ela parece complementar o cadastro tradicional de ICMS/PIS/COFINS, adicionando campos de CBS/IBS, classificação tributária e reduções.

Precisa confirmar:

- se essa tela abre pelo botão `ReformaTributária`;
- se CBS/IBS será configurado por produto, por operação ou ambos;
- se a classificação CBS/IBS vem da IMENDES;
- se as alíquotas padrão vêm da IMENDES ou de configuração interna;
- quando devem ser usadas alíquotas personalizadas;
- o significado operacional da opção `LEI COMPLEMENTAR 224/2025`;
- se a operação fixa é somente `venda presencial para consumidor final` ou se haverá outras operações.

## Relação Com Reforma Tributária

Entendimento inicial:

Os prints mostram a convivência entre a tributação atual/tradicional do produto e os novos campos de CBS/IBS ligados à Reforma Tributária.

A gestão de conhecimento deve explicar:

- o que continua sendo ICMS, PIS e COFINS;
- o que entra como CBS e IBS;
- quais campos vêm da IMENDES;
- quais campos são novos no sistema WEBER;
- quais campos o suporte pode orientar;
- quais campos exigem validação fiscal antes de orientar cliente.

## Próximas Validações Sugeridas

- Confirmar se o botão `ReformaTributária` abre exatamente a janela `Configurações Fiscais por Produto`.
- Confirmar quais campos são preenchidos automaticamente pelo Weber Tributário.
- Confirmar quais campos vêm da IMENDES.
- Confirmar se a tela CBS/IBS já está em produção, homologação ou desenvolvimento.
- Mapear cada campo da tela CBS/IBS em um glossário.
- Criar artigo interno explicando a diferença entre ICMS/PIS/COFINS e CBS/IBS dentro do cadastro do produto.
