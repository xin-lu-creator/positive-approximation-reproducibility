$ErrorActionPreference = "Stop"
$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
python (Join-Path $ScriptDir "run_all.py")
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
