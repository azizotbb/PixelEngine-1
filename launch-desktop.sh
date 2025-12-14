#!/bin/bash

echo "🚀 Launching PixelEngine Desktop Application..."
echo "============================================="

# Try to run the desktop GUI
if command -v python3 &> /dev/null; then
    echo "✅ Found Python3. Starting desktop application..."
    python3 "$(dirname "$0")/PixelEngine-Desktop.py" &
    echo "📱 Desktop application launched successfully!"
    echo "   Check your screen for the PixelEngine window."
elif command -v python &> /dev/null; then
    echo "✅ Found Python. Starting desktop application..."
    python "$(dirname "$0")/PixelEngine-Desktop.py" &
    echo "📱 Desktop application launched successfully!"
    echo "   Check your screen for the PixelEngine window."
else
    echo "❌ Python not found. Installing Python with Homebrew..."
    if command -v brew &> /dev/null; then
        brew install python-tk
        echo "✅ Python installed. Trying again..."
        python3 "$(dirname "$0")/PixelEngine-Desktop.py" &
    else
        echo "❌ Please install Python or Homebrew first."
        echo "   Visit: https://www.python.org or https://brew.sh"
    fi
fi

echo ""
echo "✅ Desktop application should now be running!"
echo "   Look for the PixelEngine window on your screen."
