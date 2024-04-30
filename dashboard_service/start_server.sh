#!/bin/bash

# Migrate
python manage.py migrate &
# Start the second Django server
python manage.py runserver 0.0.0.0:8001