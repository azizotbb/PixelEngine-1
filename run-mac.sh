#!/bin/bash

# PixelEngine Mac Launcher
# This script builds and runs PixelEngine on macOS

echo "🚀 Starting PixelEngine for Mac..."
echo "=================================="

# Navigate to the project directory
cd "$(dirname "$0")"

# Check if .NET is installed
if ! command -v dotnet &> /dev/null; then
    echo "❌ .NET is not installed. Please install .NET 10 from: https://dotnet.microsoft.com/download"
    exit 1
fi

# Build the Mac version
echo "🔨 Building PixelEngine for Mac..."
dotnet build src/PixelEngine.Mac --configuration Release

if [ $? -eq 0 ]; then
    echo "✅ Build successful!"
    echo "🎮 Running PixelEngine..."
    echo ""
    
    # Run the application
    dotnet run --project src/PixelEngine.Mac --configuration Release
else
    echo "❌ Build failed!"
    exit 1
fi
