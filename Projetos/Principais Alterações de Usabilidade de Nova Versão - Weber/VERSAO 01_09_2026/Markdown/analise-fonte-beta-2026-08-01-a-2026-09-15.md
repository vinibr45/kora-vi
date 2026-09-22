# Analise da fonte beta - 2026-08-01 a 2026-09-15

## Fonte analisada

Arquivo local:

```text
Alterações das versões de aplicativos beta por intervalo de data - Portal Gerencial Weber.html
```

Pagina salva do Portal Gerencial Weber:

```text
appsWeberBetaAlteracoesIntervaloData.php?dataInicial=2026-08-01&dataFinal=2026-09-15&submited=1
```

## O que esta fonte comprova

Esta fonte comprova que determinadas alteracoes foram registradas em aplicativos beta da Weber dentro do intervalo de **2026-08-01 a 2026-09-15**.

Foram extraidos:

- 109 registros de alteracao;
- 33 pacotes/aplicativos beta;
- data e hora da alteracao;
- usuario interno responsavel pelo registro;
- descricao textual da alteracao;
- nome do pacote `.ZIP` relacionado.

Arquivo extraido:

```text
alteracoes-beta-extraidas-2026-08-01-a-2026-09-15.csv
```

## O que esta fonte nao comprova

Esta fonte **nao comprova sozinha** que uma alteracao ja esta em producao.

Ela tambem nao comprova:

- data exata de promocao do beta para producao;
- clientes que receberam a atualizacao;
- pacote final publicado em producao;
- se houve rollback;
- se uma alteracao beta foi descartada antes de ir para producao;
- se uma recompilacao posterior substituiu a alteracao original.

## Como usar no Weber Patches

Usar estes registros como **fonte primaria de alteracoes beta**.

No Weber Patch, o status deve ser descrito com cuidado:

```text
Status da alteracao: Beta registrado
Status em producao: Nao confirmado
Fonte: Portal Gerencial Weber - alteracoes beta por intervalo de data
```

Quando houver evidencia posterior de que o pacote foi para producao, atualizar para:

```text
Status da alteracao: Promovida para producao
Fonte de confirmacao: [pagina/lista/arquivo/data]
```

## Criterio seguro de inferencia

Sem outra fonte, a KORA deve tratar cada item como:

```text
Alteracao registrada em beta, com producao nao confirmada.
```

Nao afirmar:

```text
Alteracao entregue em producao.
```

Exceto quando houver uma segunda evidencia, como:

- lista de arquivos de producao;
- pagina de downloads de producao;
- data de publicacao em producao;
- instalador final baixado do ambiente de producao;
- comunicacao interna confirmando promocao;
- chamado/RAA dizendo que a release ja esta aplicada em cliente.

## Caminho recomendado para confirmar producao

Para transformar os registros beta em Weber Patches de producao, o ideal e obter pelo menos uma destas fontes:

1. HTML salvo da pagina/lista de arquivos de producao.
2. Lista de nomes e datas dos arquivos atualmente publicados em producao.
3. Pasta local com os arquivos baixados de producao, preservando data de modificacao.
4. Pagina de "ultimas versoes" do beta para comparar com a area de producao.
5. Registro interno que informe quando o beta foi promovido.

Com isso, o processo fica:

```text
Beta registrado
-> comparar pacote, data e descricao
-> localizar equivalente em producao
-> marcar como producao confirmada ou nao confirmada
-> gerar Weber Patch por data de release
```

## Aplicativos com mais alteracoes no intervalo

```text
WGLCTONOTA.ZIP: 22
SERVIDOR.ZIP: 16
ECF_WS.ZIP: 8
MENU.ZIP: 8
WGESTOQUE.ZIP: 7
WGFINANC.ZIP: 6
```

## Datas com maior volume de registros

```text
2026-08-26: 16 registros
2026-08-27: 11 registros
2026-08-06: 8 registros
2026-08-13: 6 registros
2026-08-18: 6 registros
2026-08-03: 5 registros
2026-08-05: 5 registros
2026-09-03: 5 registros
```

## Conclusao

O arquivo ajuda bastante, mas deve ser usado como trilha de beta, nao como prova direta de producao.

Ele ja permite criar um Weber Patch preliminar com status **Beta registrado / Producao nao confirmada**.

Para transformar isso em patch final de release, ainda falta uma evidencia que conecte o beta ao pacote publicado em producao.

