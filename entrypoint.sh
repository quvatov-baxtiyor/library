#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

# Source environment variables from the .env file
if [ -f /app/library.env ]; then
    export $(cat /app/library.env | sed 's/#.*//g' | xargs)
fi

# Run database migrations
python manage.py migrate

# Collect static files
python manage.py collectstatic --noinput

# Execute the container's main process (specified as CMD in the Dockerfile)
exec "$@"
