param(
    [string]$PythonCommand = "py",
    [string[]]$PythonArguments = @("-3"),
    [ValidateSet("marcos-dev", "marcar-hora")]
    [string]$Profile = "marcos-dev"
)

$ErrorActionPreference = "Stop"
$baseDir = Split-Path -Parent (Split-Path -Parent (Split-Path -Parent $PSScriptRoot))
$envPath = Join-Path $baseDir ".env"
$healthCheck = Join-Path $PSScriptRoot "health_check.py"

if (-not (Test-Path -LiteralPath $envPath)) {
    Write-Output ('{"profile":"' + $Profile + '","ready":false,"reason":"arquivo_env_ausente"}')
    exit 2
}

& $PythonCommand @PythonArguments $healthCheck --profile $Profile
exit $LASTEXITCODE
