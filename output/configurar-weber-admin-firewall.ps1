#requires -version 5.1

[CmdletBinding(SupportsShouldProcess = $true)]
param(
    [switch]$ForCurrentUserOnly
)

$ErrorActionPreference = 'Stop'

$executables = @(
    'C:\Weber\SERVIDOR\VPN\ServerNFe.exe',
    'C:\Weber\SERVIDOR\VPN\RoboXML.exe',
    'C:\Weber\SERVIDOR\VPN\wgsync.exe',
    'C:\Weber\SERVIDOR\VPN\ScanTech.exe',
    'C:\Weber\ESTACAO\menu.exe',
    'C:\Weber\ESTACAO\Gondola.exe'
)

function Test-IsAdministrator {
    $identity = [Security.Principal.WindowsIdentity]::GetCurrent()
    $principal = [Security.Principal.WindowsPrincipal]::new($identity)
    return $principal.IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)
}

if (-not (Test-IsAdministrator)) {
    Write-Host 'Solicitando permissao de administrador...'

    $arguments = @(
        '-NoProfile',
        '-ExecutionPolicy', 'Bypass',
        '-File', ('"{0}"' -f $PSCommandPath)
    )

    if ($ForCurrentUserOnly) {
        $arguments += '-ForCurrentUserOnly'
    }

    Start-Process -FilePath 'powershell.exe' -ArgumentList $arguments -Verb RunAs
    exit
}

$missingExecutables = $executables | Where-Object { -not (Test-Path -LiteralPath $_ -PathType Leaf) }

if ($missingExecutables.Count -gt 0) {
    Write-Warning 'Os executaveis abaixo nao foram encontrados. Eles serao ignorados:'
    $missingExecutables | ForEach-Object { Write-Warning " - $_" }
}

$existingExecutables = $executables | Where-Object { Test-Path -LiteralPath $_ -PathType Leaf }

if ($existingExecutables.Count -eq 0) {
    throw 'Nenhum executavel foi encontrado nos caminhos informados.'
}

$runAsRegistryPath = if ($ForCurrentUserOnly) {
    'HKCU:\Software\Microsoft\Windows NT\CurrentVersion\AppCompatFlags\Layers'
} else {
    'HKLM:\Software\Microsoft\Windows NT\CurrentVersion\AppCompatFlags\Layers'
}

if ($PSCmdlet.ShouldProcess($runAsRegistryPath, 'Configurar executaveis para executar como administrador')) {
    if (-not (Test-Path -LiteralPath $runAsRegistryPath)) {
        New-Item -Path $runAsRegistryPath -Force | Out-Null
    }

    foreach ($executable in $existingExecutables) {
        New-ItemProperty `
            -Path $runAsRegistryPath `
            -Name $executable `
            -Value '~ RUNASADMIN' `
            -PropertyType String `
            -Force | Out-Null

        Write-Host "Admin permanente configurado: $executable"
    }
}

foreach ($executable in $existingExecutables) {
    $baseName = [IO.Path]::GetFileNameWithoutExtension($executable)
    $rulePrefix = "Weber Sistemas - $baseName"

    $rules = @(
        @{
            DisplayName = "$rulePrefix - Entrada"
            Direction   = 'Inbound'
        },
        @{
            DisplayName = "$rulePrefix - Saida"
            Direction   = 'Outbound'
        }
    )

    foreach ($rule in $rules) {
        if ($PSCmdlet.ShouldProcess($rule.DisplayName, 'Recriar regra de firewall')) {
            Get-NetFirewallRule -DisplayName $rule.DisplayName -ErrorAction SilentlyContinue |
                Remove-NetFirewallRule

            New-NetFirewallRule `
                -DisplayName $rule.DisplayName `
                -Program $executable `
                -Direction $rule.Direction `
                -Action Allow `
                -Profile Private,Public `
                -Enabled True `
                -Description 'Regra criada por configurar-weber-admin-firewall.ps1' |
                Out-Null

            Write-Host "Firewall liberado ($($rule.Direction), Public/Private): $executable"
        }
    }
}

Write-Host ''
Write-Host 'Concluido.'
Write-Host "Modo RunAs aplicado em: $runAsRegistryPath"
Write-Host 'Perfis de firewall liberados: Public e Private'
