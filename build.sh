#!/bin/bash
# Build script for Render
echo "=== Starting build process ==="
echo "Python version: $(python --version)"
echo "Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt
echo "=== Build complete ==="
echo "Listing installed packages:"
pip list | grep -E "(flask|gunicorn|pymysql)"
echo "=== Ready for deployment ==="
