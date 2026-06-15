#Requires -Version 5.1
$ErrorActionPreference = "Stop"

$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$toolkitRoot = Resolve-Path (Join-Path $scriptDir "..")

& python3 (Join-Path $toolkitRoot "scripts\install-all.py") --toolkit-root $toolkitRoot @args
