#!/bin/bash

echo "🚀 Starting PixelEngine GUI..."
echo "This will open PixelEngine in your web browser"
echo ""

cd "$(dirname "$0")"

# Kill any existing processes on port 5000
lsof -ti:5000 | xargs kill -9 2>/dev/null || true

# Start the web application
dotnet run --project src/PixelEngine.Web
