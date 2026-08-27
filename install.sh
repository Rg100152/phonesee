#!/bin/bash
# PhoneSee Installation Script
# Created by Raj Gautam

echo "PhoneSee - Phone Number Intelligence Tool"
echo "Installing dependencies..."
echo ""

# Create virtual environment (optional)
if [ "$1" == "--venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
    source venv/bin/activate
    echo "Virtual environment activated"
    echo ""
fi

# Upgrade pip
echo "Upgrading pip..."
pip install --upgrade pip

# Install dependencies
echo "Installing requirements..."
pip install -r requirements.txt

# Create necessary directories
echo "Creating directories..."
mkdir -p reports
mkdir -p .cache
mkdir -p logs
mkdir -p exports

# Copy .env.example to .env if not exists
if [ ! -f .env ]; then
    echo "Creating .env file..."
    cp .env.example .env
    echo "Please edit .env with your API keys"
fi

echo ""
echo "Installation complete!"
echo "Run 'python phonesee.py' to start PhoneSee"