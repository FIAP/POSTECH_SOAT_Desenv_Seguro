#!/usr/bin/env bash

# Install dependencies
apt-get update && \
apt-get install make -y && \
apt-get install curl -y

# Run Coverage and Fails if under 80%
# Substituir o path (--source ...) pelo path do projeto
coverage run --source ... -m pytest
coverage xml -o coverage.xml
coverage report -m --fail-under=80
