# Analise do cruzamento beta x producao - 2026-08-01 a 2026-09-15

## Fontes usadas

### Fonte 1 - Alteracoes beta por intervalo

```text
Alterações das versões de aplicativos beta por intervalo de data - Portal Gerencial Weber.html
```

Arquivo extraido:

```text
alteracoes-beta-extraidas-2026-08-01-a-2026-09-15.csv
```

### Fonte 2 - Ultimas versoes beta com tag de producao

```text
Versões de aplicativos beta - Portal Gerencial Weber.html
```

Arquivo extraido:

```text
versoes-beta-producao-extraidas.csv
```

## Resultado do cruzamento

Foi gerado o arquivo consolidado:

```text
alteracoes-beta-com-status-producao-2026-08-01-a-2026-09-15.csv
```

Resultado:

- 109 alteracoes beta analisadas;
- 26 alteracoes com producao confirmada;
- 83 alteracoes ainda sem confirmacao de producao por correspondencia exata.

## Criterio usado para confirmar producao

Uma alteracao foi marcada como **Producao confirmada** somente quando houve correspondencia exata entre:

```text
mesmo aplicativo
mesma data/hora de carregamento
tag "Enviado para producao em..."
```

Este criterio e conservador. Ele evita afirmar que uma alteracao foi para producao apenas porque pertence ao mesmo aplicativo.

## Alteracoes confirmadas em producao

```text
ATUALIZA.ZIP - 03/09/2026 17:29:29 -> producao em 03/09/2026 17:29:44
ATUALIZAPAC.ZIP - 17/08/2026 13:51:44 -> producao em 17/08/2026 13:51:57
ECF_WS.ZIP - 14/09/2026 13:31:21 -> producao em 14/09/2026 14:07:17
MENU.ZIP - 10/09/2026 18:33:20 -> producao em 14/09/2026 08:58:19
PROMIS.ZIP - 28/08/2026 19:52:53 -> producao em 03/09/2026 18:01:30
SCANTECH.ZIP - 27/08/2026 16:55:20 -> producao em 03/09/2026 18:01:08
WDLLNFE.ZIP - 10/09/2026 16:52:22 -> producao em 14/09/2026 08:58:27
WGALERTAS.ZIP - 26/08/2026 10:34:43 -> producao em 03/09/2026 18:03:42
WGCOMPRAS.ZIP - 27/08/2026 17:22:30 -> producao em 03/09/2026 18:01:24
WGFECHACX.ZIP - 27/08/2026 17:45:45 -> producao em 03/09/2026 18:01:12
WGFINANC.ZIP - 27/08/2026 10:34:37 -> producao em 03/09/2026 18:03:31
WGHELPS.ZIP - 26/08/2026 10:52:34 -> producao em 03/09/2026 18:03:39
WGLOGS.ZIP - 26/08/2026 10:24:14 -> producao em 03/09/2026 18:03:57
WGNFE.ZIP - 26/08/2026 10:16:41 -> producao em 03/09/2026 18:04:07
WGNOTIFICACOES.ZIP - 31/08/2026 13:25:12 -> producao em 03/09/2026 18:00:43
WGPED.ZIP - 26/08/2026 10:11:22 -> producao em 03/09/2026 18:04:15
WGPESSOA.ZIP - 26/08/2026 10:14:16 -> producao em 03/09/2026 18:04:11
WGPRECOS.ZIP - 27/08/2026 17:44:24 -> producao em 03/09/2026 18:01:17
WGPRODUTOS.ZIP - 01/09/2026 15:44:34 -> producao em 03/09/2026 18:00:14
WGREPORT.ZIP - 26/08/2026 10:18:06 -> producao em 03/09/2026 18:04:01
WGSYNC.ZIP - 27/08/2026 16:14:35 -> producao em 03/09/2026 18:03:28
WGSYNCLIB.ZIP - 02/09/2026 09:45:45 -> producao em 03/09/2026 17:59:46
WGTABS.ZIP - 26/08/2026 10:25:14 -> producao em 03/09/2026 18:03:53
WG_CCUSTO.ZIP - 26/08/2026 10:27:29 -> producao em 03/09/2026 18:03:50
WG_CONTAS.ZIP - 26/08/2026 10:28:22 -> producao em 03/09/2026 18:03:46
WPAC0001.ZIP - 26/08/2026 19:27:37 -> producao em 03/09/2026 18:03:35
```

## Observacao importante

Algumas descricoes podem conter observacoes antigas como "ainda e beta". Quando a segunda fonte marca a mesma versao como enviada para producao, o status mais forte passa a ser a tag de producao da pagina de ultimas versoes.

Mesmo assim, esse tipo de conflito deve aparecer no Weber Patch como observacao, porque pode indicar que a descricao nao foi revisada antes da promocao.

## Como usar no Weber Patches

Para cada item confirmado, usar:

```text
Status da alteracao: Producao confirmada
Fonte beta: Portal Gerencial Weber - alteracoes beta por intervalo de data
Fonte producao: Portal Gerencial Weber - ultimas versoes beta
Criterio: mesmo aplicativo e mesma data/hora de carregamento
```

Para os demais itens, manter:

```text
Status da alteracao: Beta registrado
Status em producao: Nao confirmado
```

## Proximo passo recomendado

Gerar um Weber Patch agrupado por **data de envio para producao**, especialmente para:

```text
2026-09-03
2026-09-14
```

Essas datas concentram varias promocoes para producao e podem funcionar como releases operacionais.

