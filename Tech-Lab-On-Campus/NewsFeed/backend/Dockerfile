FROM python:3.12-slim

WORKDIR /workspace/backend

COPY . .

# Ensure the resources directory is copied
# COPY ./resources ./resources
# COPY resources/ /resources/

RUN --mount=type=cache,target=/root/.cache \
    python3.12 -m pip install -U pip && \
    python3.12 -m pip install -e .[dev]

ENV FLASK_APP=app

EXPOSE 8000
