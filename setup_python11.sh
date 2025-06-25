#!/bin/bash
# Setup script for AI Engine Service with Python 3.11
echo "Setting up AI Engine Service with Python 3.11..."

# Check if python3.11 is available
if ! command -v python3.11 &> /dev/null; then
    echo "Python 3.11 not found. Installing via Homebrew..."
    brew install python@3.11
fi

# Remove existing venv if it exists
if [ -d "venv" ]; then
    echo "Removing existing virtual environment..."
    rm -rf venv
fi

# Create new virtual environment with Python 3.11
echo "Creating virtual environment with Python 3.11..."
python3.11 -m venv venv

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Upgrade pip
echo "Upgrading pip..."
pip install --upgrade pip

# Install requirements
echo "Installing requirements..."
pip install -r requirements.txt

echo "Setup complete! AI Engine Service is ready."
echo "To activate: source venv/bin/activate"
echo "To run: uvicorn main:app --reload --host 0.0.0.0 --port 8001"