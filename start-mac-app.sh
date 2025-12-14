#!/bin/bash

echo "Starting PixelEngine for Mac..."
echo "================================"

cd "$(dirname "$0")/src/PixelEngine.MacApp"

# Build and run
dotnet build
if [ $? -eq 0 ]; then
    echo "Build successful! Starting application..."
    dotnet run
else
    echo "Build failed. Please check your .NET installation."
fi
