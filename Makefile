.PHONY: generate clean install test build publish docs

generate:
	openapi-python-client generate --path ./openapi.yaml --output-path antfly-client --overwrite --config .openapi-generator-config.yaml

clean:
	rm -rf build dist *.egg-info
	rm -rf antfly-client
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete

install:
	pip install -e .[dev]

test:
	pytest tests/

build: clean generate
	python -m build

publish: build
	python -m twine upload dist/*

docs:
	cd docs && make html
