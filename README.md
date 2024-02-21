python3 -m venv abc-env    
Activate env: source abc-env/bin/activate
Close env: deactivate

Install deps: pip freeze > requirements.txt
Save deps to file: pip install -r requirements.txt

run tests: python3 -m unittest