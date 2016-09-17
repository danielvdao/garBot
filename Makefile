run: requirements.txt bot.py
	pip install -r requirements.txt
	python bot.py

upgrade: requirements.txt
	pip install -r requirements.txt --upgrade

freeze: requirements.txt
	pip freeze > requirements.txt
