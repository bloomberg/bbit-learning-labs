FROM python:3.12-slim

# Install Node.js 18
RUN apt-get update && apt-get install -y curl && \
    curl -fsSL https://deb.nodesource.com/setup_18.x | bash - && \
    apt-get install -y \
    nodejs \
    npm \
    && \
    apt-get clean

# Install other development dependencies
RUN apt-get install -y \
    git \
    make \
    && \
    apt-get clean

WORKDIR /workspace

# Set up pip config
RUN python -m pip install --upgrade pip
RUN pip config set global.trusted-host "pypi.org files.pythonhosted.org pypi.python.org"

CMD ["/bin/bash"]
