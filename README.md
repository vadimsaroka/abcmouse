python3 -m venv abc-env    

Activate env: "source abc-env/bin/activate"

Close env: "deactivate"

Save deps: "pip freeze > requirements.txt"

Install deps: "pip install -r requirements.txt"

run tests: "python3 -m unittest"

#shadow-root
TODO: chain .shadow_root from top to buttom for all tests to get correct locators (main_page.py, subscription.py, sign_up_page.py)