.PHONY: data build lint test all

data:
	@echo "Phase 1: simulator goes here"

build:
	mkdir -p data
	cd bank_data/dbt && dbt build --profiles-dir .

lint:
	ruff check .

test:
	pytest

all: data build lint test
