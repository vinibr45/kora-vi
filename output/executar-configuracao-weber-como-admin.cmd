@echo off
setlocal

set "SCRIPT_DIR=%~dp0"
set "PS_SCRIPT=%SCRIPT_DIR%configurar-weber-admin-firewall.ps1"

if not exist "%PS_SCRIPT%" (
    echo Nao encontrei o script:
    echo "%PS_SCRIPT%"
    pause
    exit /b 1
)

powershell.exe -NoProfile -ExecutionPolicy Bypass -Command "Start-Process powershell.exe -Verb RunAs -ArgumentList '-NoProfile -ExecutionPolicy Bypass -File ""%PS_SCRIPT%""'"

endlocal
