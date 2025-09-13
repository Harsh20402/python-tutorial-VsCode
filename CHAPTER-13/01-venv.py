# Install the virtualenv package globally using pip (Python's package manager).
# This package allows you to create isolated Python environments.
pip install virtualenv


# Create a new virtual environment with a chosen name.
# Replace <name of your virtual environment> with your own name, e.g., env, venv, myproject, etc.
# This will create a folder with its own Python interpreter and dependencies separate from the system Python.
virtualenv <name of your virtual environment>


# Activate the virtual environment (Windows PowerShell command).
# Here, .\env\Scripts\activate.ps1 runs the activation script located in the env folder.
# After activation, your terminal will show the environment name in parentheses, e.g., (env).
# All Python packages you install now will stay inside this environment only.
.\env\Scripts\activate.ps1


# Deactivate the virtual environment.
# This command returns you back to the global/system Python environment.
deactivate
