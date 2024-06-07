# Description: Generates the 'requirements.txt' file.

# Check if a virtual environment is not active
if (!$env:VIRTUAL_ENV) {
    Write-Warning "The virtual environment is not active!"
    .\scripts\activate.ps1
}

# Generate the requirements.txt file
Write-Output "Generating the 'requirements.txt' file..."
python -m pip freeze > requirements.txt
Write-Output "The 'requirements.txt' file has been generated!"

