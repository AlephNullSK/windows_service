.PHONY: lint check dev

check:
	poetry run pre-commit run --all-files

lint:
	poetry run black .
	poetry run isort . --profile black

dev:
	python3 -m pip install -U poetry
	poetry install
	poetry run pre-commit install
