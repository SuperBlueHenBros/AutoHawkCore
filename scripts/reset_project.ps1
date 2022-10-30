<#
    Delete files added by the project
#>
Write-Host -ForegroundColor Red "Deleting env/"
Remove-Item -Recurse -Force env

Write-Host -ForegroundColor Red "Deleting lib/"
Remove-Item -Recurse -Force lib
