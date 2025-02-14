PYTHON       ?= python3.12
DEPENDENCIES  = frontend/node_modules
FLASK_APP     = backend/app
FLASK_PORT    = 8000

.PHONY: help
help:
	@echo "Usage:"
	@echo "    help            - Prints this screen"
	@echo "    install         - Install all frontend and backend dependencies"
	@echo "    lint-backend    - Make the formatting changes directly to the backend code"
	@echo "    lint-backend    - Lints the backend code"
	@echo "    run-backend     - Run the development version of the backend flask app"
	@echo "    run-frontend    - Run the frontend version of this application"
	@echo "    clean           - Clean out temporaries"


.PHONY: install
install:
	cd backend && $(PYTHON) -m pip install -e .[dev]
	cd frontend && npm install --save-dev

.PHONY: fmt-backend
fmt-backend:
	$(PYTHON) -m ruff format
	$(PYTHON) -m ruff check --fix

.PHONY: run-backend
run-backend:
	FLASK_APP=$(FLASK_APP) flask run --host=0.0.0.0 --port=${FLASK_PORT}

.PHONY: lint-backend
lint-backend:
	$(PYTHON) -m ruff check
	$(PYTHON) -m mypy backend/app --show-error-codes

.PHONY: run-frontend
run-frontend:
	cd frontend && npm run dev

.PHONY: run
run:
	flask run --host=0.0.0.0 --port=${FLASK_PORT} &
	cd frontend && npm run dev &

.PHONY: clean
clean:
	@echo "Removing temporary files"
	-find -P . \( -name "venv" -o -name "build" -o -name "dist" -o -name "*.egg-info" -o -name "*.pyc" -type f -o -name ".mypy_cache" -o -name ".pytest_cache" -o -name "__pycache__" \) -exec rm -rf {} +
	rm -rf $(DEPENDENCIES)
