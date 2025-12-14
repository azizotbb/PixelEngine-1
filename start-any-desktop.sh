#!/bin/bash

echo "🚀 Starting PixelEngine Desktop Applications..."
echo "==============================================="

# Check what's available and launch the best option
echo "🔍 Checking available runtimes..."

if pgrep -f "PixelEngine-Desktop.py" > /dev/null; then
    echo "✅ Python GUI is already running!"
    echo "   Check your desktop for the PixelEngine window."
    exit 0
fi

# Try Python GUI first
if command -v python3 &> /dev/null; then
    echo "✅ Python3 found. Launching GUI application..."
    python3 "$(dirname "$0")/PixelEngine-Desktop.py" &
    sleep 2
    if pgrep -f "PixelEngine-Desktop.py" > /dev/null; then
        echo "🎉 SUCCESS! PixelEngine GUI is now running!"
        echo "   Look for the desktop window with white background."
        exit 0
    else
        echo "⚠️  Python GUI failed to start."
    fi
fi

# Try Swift native app
if command -v swift &> /dev/null; then
    echo "✅ Swift found. Compiling native macOS app..."
    swift "$(dirname "$0")/PixelEngine-Native.swift" &
    echo "🎉 Native macOS app launched!"
    exit 0
fi

# Try .NET console app
if command -v dotnet &> /dev/null; then
    echo "✅ .NET found. Launching console application..."
    open -a Terminal "$(dirname "$0")/PixelEngine"
    echo "🎉 Console application launched in new terminal!"
    exit 0
fi

echo "❌ No suitable runtime found."
echo "   Please install one of: Python3, Swift, or .NET"
echo "   Visit: https://www.python.org or install Xcode"
