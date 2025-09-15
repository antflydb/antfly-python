.PHONY: generate clean install test build publish docs fmt

generate:
	openapi-python-client generate --path ../openapi.yaml --output-path src/antfly --overwrite --config .openapi-generator-config.yaml

clean:
	rm -rf build dist *.egg-info
	rm -rf antfly-client
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete

install:
	pip install -e ".[dev]"

test:
	pytest tests/

build: clean generate
	python -m build

publish: build
	python -m twine upload dist/*

docs:
	cd docs && make html

fmt:
	ruff check src tests --fix
	black src tests

update-deps:
	python3 -m pip install --upgrade -e ".[dev]"
	#pip install -U -r requirements.txt
	#pip install -U -r requirements-dev.txt
	#pip freeze > requirements.txt
	#pip freeze > requirements-dev.txt
