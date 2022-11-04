FROM jupyter/scipy-notebook:latest
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
ENV PYTHONPATH /app/bbit-learning-labs/PortfolioManager

ENTRYPOINT ["/bin/bash", "-c", "jupyter lab"]


