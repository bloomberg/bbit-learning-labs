# Use the official Jupyter Notebook Image as the base image
FROM jupyter/scipy-notebook:latest

# Set the working directory
WORKDIR /app

# Copy and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

#Set envrionmental variables
ENV PYTHONPATH /app

# Default command to be run once container starts
ENTRYPOINT ["/bin/bash","-c","jupyter lab"]