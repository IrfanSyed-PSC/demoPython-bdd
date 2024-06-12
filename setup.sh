#!/bin/sh

## Setup configuration for poetry
poetry config virtualenvs.in-project true
poetry lock --no-update
poetry install --no-ansi --no-root
source .venv/bin/activate
