.PHONY: generate clean install test build publish docs fmt

generate:
	openapi-python-client generate --path ../openapi.yaml --output-path src/antfly --overwrite --config .openapi-generator-config.yaml

clean:
	rm -rf build dist *.egg-info
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete

install:
	pip install -e ".[dev]"

test:
	pytest tests --cov=antfly --cov-report=xml

build: clean generate
	python -m build

publish: build
	python -m twine upload dist/*

docs:
	cd docs && make html

check:
	ruff check src tests --fix
	ruff format src tests --fix
	pyright src tests

update-deps:
	poetry update
