# Description: Sets up the virtual environment and installs dependencies.

# Check if a virtual environment is already active
if ($env:VIRTUAL_ENV) {
    Throw "The virtual environment is active! Deactivate the virtual environment using 'deactivate'."
}

# Check if '.venv' exists
if (Test-Path .\.venv) {
    Throw "The virtual environment already exists! Delete the existing virtual environment using '.\scripts\delete-venv.ps1'."
}

# Install virtualenv package
pip install virtualenv

# Create virtual environment
Write-Output "Creating virtual environment..."
virtualenv .venv

# Activate the virtual environment
.\.venv\Scripts\activate

# Install the required packages
Write-Output "Installing required packages..."
pip install pygame
pip install pygame_gui

# Deactivate the virtual environment
deactivate

Write-Output "Virtual environment setup complete!"
Write-Output "Activate the virtual environment using `".\scripts\activate.ps1`""