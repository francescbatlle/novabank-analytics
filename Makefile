# NovaBank Analytics: shortcuts for common commands.
# Run them from the repo root, e.g. make data or make all.

.PHONY: data build lint test all

# Generate the simulated NovaBank data into data/raw/
data:
	python bank_data/simulator/main.py

# Build the warehouse: dbt turns the raw data into clean tables
build:
	mkdir -p data
	cd bank_data/dbt && dbt build --profiles-dir .

# Check code style with ruff
lint:
	ruff check .

# Run the Python tests with pytest
test:
	pytest

# Run everything, in order
all: data build lint test
