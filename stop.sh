#!/bin/bash

# Script to stop the Expense Tracker project
# This script stops the Django server and MongoDB container

echo "========================================="
echo "Stopping Expense Tracker Project"
echo "========================================="

# Get the directory where the script is located
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$SCRIPT_DIR"

# Stop MongoDB container
echo "[1/2] Stopping MongoDB container..."
docker-compose down --remove-orphans
docker rm -f expense_tracker_mongodb 2>/dev/null || true

# Kill Django development server if running
echo "[2/2] Stopping Django development server..."
pkill -f "manage.py runserver" 2>/dev/null || echo "Django server was not running"

echo ""
echo "========================================="
echo "Project stopped successfully!"
echo "========================================="
