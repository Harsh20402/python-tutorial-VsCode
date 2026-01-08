# Create two virtual environments, install few packages in the first one. How do you create a similar environment in the second one? 

# 1. Create the first virtual environment (env1)
virtualenv env1

# 2. Create the second virtual environment (env2)
virtualenv env2


# ------------------------------
# Work inside the first environment
# ------------------------------

# 3. Activate the first environment (env1)
.\env1\Scripts\activate.ps1

# 4. Install some packages (example: flask)
pip install flask

# 5. Export the installed packages to a file (requirements.txt)
pip freeze > requirements.txt

# 6. Deactivate env1
deactivate


# ------------------------------
# Recreate the same environment in env2
# ------------------------------

# 7. Activate the second environment (env2)
.\env2\Scripts\activate.ps1

# 8. Install the packages listed in requirements.txt
pip install -r .\requirements.txt

# 9. Deactivate env2 (optional, after done)
deactivate
