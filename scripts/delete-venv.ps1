# Description: Deletes the virtual environment.

# Check if a virtual environment is active
if ($env:VIRTUAL_ENV) {
    Write-Warning "The virtual environment is active!"
    Write-Output "Deactivating the virtual environment..."
    deactivate
}

# Check if '.venv' exists
if (Test-Path .\.venv) {
    # Delete '.venv' recursively
    Write-Output "Deleting the virtual environment..."
    Remove-Item .\.venv -Recurse -Force
    Write-Output "The virtual environment has been successfully deleted!"
} else {
    Throw "'.venv' not found! Create a virtual environment using '.\scripts\setup-venv.ps1'."
}