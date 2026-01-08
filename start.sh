#!/bin/bash

# Script to start the Expense Tracker project
# This script starts MongoDB via Docker Compose and then runs the Django development server

echo "========================================="
echo "Starting Expense Tracker Project"
echo "========================================="

# Get the directory where the script is located
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$SCRIPT_DIR"

# Check if Docker is running
if ! docker info > /dev/null 2>&1; then
    echo "Error: Docker is not running. Please start Docker first."
    exit 1
fi

# Start MongoDB via Docker Compose
echo ""
echo "[1/4] Checking MongoDB container..."

# Check if container already exists
if docker ps -a --format '{{.Names}}' | grep -q '^expense_tracker_mongodb$'; then
    echo "MongoDB container already exists."
    # Check if it's running
    if docker ps --format '{{.Names}}' | grep -q '^expense_tracker_mongodb$'; then
        echo "MongoDB container is already running."
    else
        echo "Starting existing MongoDB container..."
        docker start expense_tracker_mongodb
    fi
else
    echo "Creating new MongoDB container..."
    docker-compose up -d
fi

# Wait for MongoDB to be ready
echo "[2/4] Waiting for MongoDB to be ready..."
echo -n "Checking MongoDB connection"
RETRIES=30
until docker exec expense_tracker_mongodb mongosh --eval "db.runCommand('ping').ok" expense_tracker_db --quiet > /dev/null 2>&1 || [ $RETRIES -eq 0 ]; do
    echo -n "."
    sleep 1
    RETRIES=$((RETRIES - 1))
done
echo ""

if [ $RETRIES -eq 0 ]; then
    echo "Warning: MongoDB might not be fully ready yet, but continuing..."
else
    echo "MongoDB is ready!"
fi

# Create logs directory if it doesn't exist
mkdir -p logs

# Activate virtual environment if it exists
echo "[3/4] Setting up Python environment..."
if [ -d "venv" ]; then
    source venv/bin/activate
    PYTHON_CMD="python"
else
    PYTHON_CMD="python3"
fi

# Apply migrations
echo "[4/4] Applying database migrations..."
if ! $PYTHON_CMD manage.py migrate --noinput; then
    echo "Warning: Migrations failed, but continuing..."
fi

# Start Django development server
echo ""
echo "========================================="
echo "Django development server starting..."
echo "Access the application at: http://localhost:8000"
echo "Press CTRL+C to stop the server"
echo "========================================="
echo ""

# Run Django development server
$PYTHON_CMD manage.py runserver
