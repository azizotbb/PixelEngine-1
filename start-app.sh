#!/bin/bash

echo "🚀 Launching PixelEngine Native App..."
echo "This will open a real Mac application window"
echo ""

cd "$(dirname "$0")"

# Build and run the native application
dotnet run --project src/PixelEngine.Native
