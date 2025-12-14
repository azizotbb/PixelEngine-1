#!/bin/bash

echo "🚀 Starting PixelEngine..."
cd "$(dirname "$0")"

# Run the simple version that works
dotnet run --project src/PixelEngine.Simple
