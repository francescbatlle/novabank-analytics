.PHONY: data build lint test all

data:
	python bank_data/simulator/main.py

build:
	mkdir -p data
	cd bank_data/dbt && dbt build --profiles-dir .

lint:
	ruff check .

test:
	pytest

all: data build lint test
