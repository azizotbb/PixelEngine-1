#!/bin/bash

echo "🚀 Starting PixelEngine Desktop App..."
echo "====================================="

cd "$(dirname "$0")"

# Check if Python is available
if command -v python3 &> /dev/null; then
    echo "✅ Python3 found. Starting GUI application..."
    python3 PixelEngine-Desktop.py
elif command -v python &> /dev/null; then
    echo "✅ Python found. Starting GUI application..."
    python PixelEngine-Desktop.py
else
    echo "❌ Python not found. Trying .NET version..."
    if command -v dotnet &> /dev/null; then
        echo "✅ .NET found. Starting console application..."
        ./PixelEngine
    else
        echo "❌ Neither Python nor .NET found. Please install Python or .NET."
    fi
fi

echo ""
echo "Press any key to exit..."
read -n 1
