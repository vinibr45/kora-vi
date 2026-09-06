<#
.SYNOPSIS
Gera uma proposta de otimização somente para revisão humana.

.DESCRIPTION
Consulta dados da conta com a credencial de leitura e salva um Markdown local.
Não usa endpoints de mutação e não altera o Google Ads.
#>
[CmdletBinding()]
param(
    [string]$OutputDirectory
)

$ErrorActionPreference = 'Stop'

if ([string]::IsNullOrWhiteSpace($OutputDirectory)) {
    $OutputDirectory = Join-Path $PSScriptRoot 'plans'
}

function Get-LocalEnvValue {
    param([string]$Name, [hashtable]$Values)
    if (-not $Values.ContainsKey($Name) -or [string]::IsNullOrWhiteSpace($Values[$Name])) {
        throw "Configuração local ausente: $Name"
    }
    return $Values[$Name]
}

function ConvertTo-Base64Url {
    param([byte[]]$Bytes)
    return ([Convert]::ToBase64String($Bytes)).TrimEnd('=').Replace('+', '-').Replace('/', '_')
}

function Get-AccessTokenFromServiceAccount {
    param([pscustomobject]$ServiceAccount)

    $now = [DateTimeOffset]::UtcNow.ToUnixTimeSeconds()
    $header = ConvertTo-Base64Url ([Text.Encoding]::UTF8.GetBytes('{"alg":"RS256","typ":"JWT"}'))
    $payloadObject = @{
        iss   = $ServiceAccount.client_email
        scope = 'https://www.googleapis.com/auth/adwords'
        aud   = 'https://oauth2.googleapis.com/token'
        iat   = $now
        exp   = $now + 3600
    }
    $payload = ConvertTo-Base64Url ([Text.Encoding]::UTF8.GetBytes(($payloadObject | ConvertTo-Json -Compress)))
    $unsignedJwt = "$header.$payload"

    $privateKey = $ServiceAccount.private_key.Replace('-----BEGIN PRIVATE KEY-----', '').Replace('-----END PRIVATE KEY-----', '').Replace("`r", '').Replace("`n", '')
    $rsa = [System.Security.Cryptography.RSA]::Create()
    $bytesRead = 0
    $rsa.ImportPkcs8PrivateKey([Convert]::FromBase64String($privateKey), [ref]$bytesRead)
    $signature = ConvertTo-Base64Url ($rsa.SignData(
        [Text.Encoding]::ASCII.GetBytes($unsignedJwt),
        [System.Security.Cryptography.HashAlgorithmName]::SHA256,
        [System.Security.Cryptography.RSASignaturePadding]::Pkcs1
    ))

    $response = Invoke-RestMethod -Method Post -Uri 'https://oauth2.googleapis.com/token' `
        -ContentType 'application/x-www-form-urlencoded' `
        -Body @{ grant_type = 'urn:ietf:params:oauth:grant-type:jwt-bearer'; assertion = "$unsignedJwt.$signature" }
    return $response.access_token
}

function Invoke-GoogleAdsQuery {
    param(
        [string]$Query,
        [hashtable]$Headers,
        [string]$CustomerId,
        [string]$ApiVersion
    )
    $uri = "https://googleads.googleapis.com/$ApiVersion/customers/$CustomerId/googleAds:searchStream"
    $response = Invoke-RestMethod -Method Post -Uri $uri -Headers $Headers -ContentType 'application/json' `
        -Body (@{ query = $Query } | ConvertTo-Json -Compress)
    return @($response | ForEach-Object { $_.results } | Where-Object { $null -ne $_ })
}

$koraRoot = Split-Path -Parent (Split-Path -Parent (Split-Path -Parent $PSScriptRoot))
$envPath = Join-Path $koraRoot '.env'
if (-not (Test-Path -LiteralPath $envPath)) { throw 'Arquivo local C:\KORA\.env não encontrado.' }

$config = @{}
foreach ($line in Get-Content -LiteralPath $envPath) {
    if ($line -match '^\s*([^#=\s]+)\s*=\s*(.*)\s*$') {
        $config[$matches[1]] = $matches[2].Trim('"').Trim("'")
    }
}

$developerToken = Get-LocalEnvValue 'GOOGLE_ADS_DEVELOPER_TOKEN' $config
$managerId = Get-LocalEnvValue 'GOOGLE_ADS_LOGIN_CUSTOMER_ID' $config
$customerId = Get-LocalEnvValue 'GOOGLE_ADS_CUSTOMER_ID' $config
$readerKeyPath = Get-LocalEnvValue 'GOOGLE_ADS_SERVICE_ACCOUNT_KEY_PATH' $config
$apiVersion = if ($config.ContainsKey('GOOGLE_ADS_API_VERSION')) { $config['GOOGLE_ADS_API_VERSION'] } else { 'v25' }

if (-not (Test-Path -LiteralPath $readerKeyPath)) { throw 'A chave da conta de leitura configurada não foi encontrada.' }
$serviceAccount = Get-Content -LiteralPath $readerKeyPath -Raw | ConvertFrom-Json
$accessToken = Get-AccessTokenFromServiceAccount $serviceAccount
$headers = @{ Authorization = "Bearer $accessToken"; 'developer-token' = $developerToken; 'login-customer-id' = $managerId }

$campaignRows = Invoke-GoogleAdsQuery -Headers $headers -CustomerId $customerId -ApiVersion $apiVersion -Query @'
SELECT campaign.name, campaign.status, campaign.advertising_channel_type,
       campaign.bidding_strategy_type, campaign_budget.amount_micros,
       metrics.impressions, metrics.clicks, metrics.cost_micros, metrics.conversions
FROM campaign
WHERE campaign.status = ENABLED
  AND segments.date DURING LAST_30_DAYS
'@

$activeCampaigns = @($campaignRows | ForEach-Object {
    [pscustomobject]@{
        Name = $_.campaign.name
        Status = $_.campaign.status
        Channel = $_.campaign.advertisingChannelType
        Strategy = $_.campaign.biddingStrategyType
        BudgetBrl = [math]::Round(([double]$_.campaignBudget.amountMicros / 1000000), 2)
        Impressions = [int]$_.metrics.impressions
        Clicks = [int]$_.metrics.clicks
        CostBrl = [math]::Round(([double]$_.metrics.costMicros / 1000000), 2)
        Conversions = [double]$_.metrics.conversions
    }
})

$totalImpressions = ($activeCampaigns | Measure-Object -Property Impressions -Sum).Sum
$totalClicks = ($activeCampaigns | Measure-Object -Property Clicks -Sum).Sum
$totalCost = ($activeCampaigns | Measure-Object -Property CostBrl -Sum).Sum
$totalConversions = ($activeCampaigns | Measure-Object -Property Conversions -Sum).Sum
$averageCpc = if ($totalClicks -gt 0) { [math]::Round($totalCost / $totalClicks, 2) } else { 0 }
$campaignName = if ($activeCampaigns.Count -eq 1) { $activeCampaigns[0].Name } else { 'Mais de uma campanha ativa — revisar antes de executar' }

New-Item -ItemType Directory -Path $OutputDirectory -Force | Out-Null
$generatedAt = Get-Date
$reportPath = Join-Path $OutputDirectory ("proposta-{0}.md" -f $generatedAt.ToString('yyyy-MM-dd-HHmm'))

$campaignSummary = if ($activeCampaigns.Count -eq 0) {
    'Nenhuma campanha ativa foi encontrada no período. Não executar alterações até confirmar a conta e o período.'
} else {
    ($activeCampaigns | ForEach-Object {
        $safeName = $_.Name.Replace('|', '\\|')
        "| $safeName | $($_.Channel) | $($_.Strategy) | R$ $($_.BudgetBrl.ToString('N2')) | $($_.Impressions) | $($_.Clicks) | R$ $($_.CostBrl.ToString('N2')) | $($_.Conversions) |"
    }) -join [Environment]::NewLine
}

$content = @"
# Diagnostico Google Ads - Marcos Dev

**Status:** pendente de revisao humana<br>
**Gerado em:** $($generatedAt.ToString('dd/MM/yyyy HH:mm'))<br>
**Modo:** leitura e proposta; nenhuma alteracao foi enviada ao Google Ads.

## Diagnostico dos ultimos 30 dias

| Campanha ativa | Canal | Estrategia atual | Orcamento retornado | Impressoes | Cliques | Custo | Conversoes |
|---|---|---|---:|---:|---:|---:|---:|
$campaignSummary

- Total: **$totalImpressions impressoes**, **$totalClicks clique(s)**, **R$ $($totalCost.ToString('N2'))** de custo e **$totalConversions conversao(oes)**.
- CPC medio observado: **R$ $($averageCpc.ToString('N2'))**.
- Este arquivo e uma leitura operacional inicial. Decisoes comerciais exigem conferir busca real, pagina de destino, qualidade dos contatos e objetivo da campanha.

## Sinais para avaliar

| Area | O que observar | Cuidado antes de agir |
|---|---|---|
| Orcamento | Campanhas com gasto concentrado e baixo retorno aparente. | Nao aumentar ou reduzir verba sem meta e janela de avaliacao. |
| Cliques | CTR e CPC por campanha, grupo e termo de busca. | Clique barato nao basta se o contato nao for qualificado. |
| Conversoes | Volume, custo por conversao e confiabilidade da tag. | Validar se a conversao representa oportunidade real. |
| Intencao | Termos pesquisados e alinhamento com oferta. | Evitar negativas ou palavras-chave sem revisar impacto comercial. |
| Criativos | Promessa, segmentacao e chamada para contato. | Nao prometer resultado, ranking ou venda garantida. |
| Landing page | Mensagem, velocidade, contato e continuidade com o anuncio. | Ajustes na pagina devem respeitar identidade e conversao da Marcos Dev. |

## Proximas recomendacoes manuais

- Revisar termos de busca, palavras-chave, localizacoes, dispositivos e horarios antes de propor mudancas.
- Separar recomendacoes por campanha e classificar impacto, risco e reversibilidade.
- So transformar proposta em execucao depois de aprovacao explicita de Marcos.
- Qualquer execucao futura deve registrar antes/depois, itens aprovados, horario, conta, recurso alterado e plano de reversao.

## Bloqueios de seguranca

- Esta ferramenta nao chama endpoints `:mutate`.
- Esta ferramenta nao cria, edita ou remove campanhas, anuncios, lances, orcamentos, palavras-chave ou conversoes.
- Esta ferramenta usa somente a credencial de leitura `GOOGLE_ADS_SERVICE_ACCOUNT_KEY_PATH` configurada em `C:\KORA\.env`.
"@
Set-Content -LiteralPath $reportPath -Value $content -Encoding utf8
[pscustomobject]@{ generated = $true; mode = 'read_only_proposal'; path = $reportPath } | ConvertTo-Json -Compress



