# Description: Activates the virtual environment.

Write-Output "Activating the virtual environment..."

# Check if a virtual environment is already active
if ($env:VIRTUAL_ENV) {
    Write-Warning "The virtual environment is already active!."
    return
} else {
    # Check if '.venv' exists
    if (Test-Path .\.venv) {
        # Activate the virtual environment
        .\.venv\Scripts\activate
        Write-Output "Virtual environment activated."
        Write-Output "Type `"deactivate`" to deactivate the virtual environment."
    } else {
        Throw "'.venv' not found! Create a virtual environment using '.\scripts\setup-venv.ps1'."
    }
    
}

