PYTHON       ?= python3.12
DEPENDENCIES  = frontend/node_modules
FLASK_APP     = backend/app
FLASK_PORT    = 8000

.PHONY: help
help:
	@echo "Usage:"
	@echo "    help            - Prints this screen"
	@echo "    install         - Install all frontend and backend dependencies"
	@echo "    fmt-backend     - Make the formatting changes directly to the backend code"
	@echo "    lint-backend    - Lints the backend code"
	@echo "    redis-in-docker - Runs redis in a docker container"
	@echo "    run-backend     - Run the development version of the backend flask app"
	@echo "    run-frontend    - Run the frontend version of this application"
	@echo "    clean           - Clean out temporaries"

install:
	cd backend && $(PYTHON) -m pip install -e .[dev]
	cd frontend && npm install --save-dev

.PHONY: fmt-backend
fmt-backend: install
	$(PYTHON) -m ruff format
	$(PYTHON) -m ruff check --fix

.PHONY: lint-backend
lint-backend: install
	$(PYTHON) -m ruff check
	$(PYTHON) -m mypy backend/app --show-error-codes

.PHONY: run-backend
run-backend: install
	FLASK_APP=$(FLASK_APP) flask run --host=0.0.0.0 --port=${FLASK_PORT}

.PHONY: redis-in-docker
redis-in-docker:
	docker compose up -d redis

.PHONY: run-frontend
run-frontend: install
	cd frontend && npm run dev

.PHONY: clean
clean:
	@echo "Removing temporary files"
	-find -P . \( -name "venv" -o -name "build" -o -name "dist" -o -name "*.egg-info" -o -name "*.pyc" -type f -o -name ".mypy_cache" -o -name ".pytest_cache" -o -name "__pycache__" \) -exec rm -rf {} +
	rm -rf $(DEPENDENCIES)
