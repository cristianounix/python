install:
	pip install -r requirements.txt

env:
	virtualenv venv
	soruce venv/bin/activate

run:
	python mini_app/app.py

generate_requirements:
	pip-compile requirements.in

clean:
	rm -rf __pycache__/ tests/__pycache__ mini_app/__pycache__
