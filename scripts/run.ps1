# Description: Runs the project in a virtual environment

# Check if '.venv' exists
if (Test-Path .\.venv) {
    # Activate the virtual environment
    . .\.venv\Scripts\activate

    # Run main.py
    Write-Output "Running the project..."
    python src\main.py
} else {
    Throw "'.venv' not found! Create a virtual environment using '.\scripts\setup-venv.ps1'."
}