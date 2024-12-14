#!/bin/bash

# Install dependencies
pip install -r requirements.txt

# Run migrations
python3.12 manage.py migrate

# Collect static files
python3.12 manage.py collectstatic --noinput
