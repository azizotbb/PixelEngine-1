#!/bin/bash

# Create PixelEngine.app for macOS
echo "📦 Creating PixelEngine.app bundle for macOS..."

# Create app bundle structure
mkdir -p PixelEngine.app/Contents/MacOS
mkdir -p PixelEngine.app/Contents/Resources

# Create Info.plist
cat > PixelEngine.app/Contents/Info.plist << 'EOF'
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>CFBundleName</key>
    <string>PixelEngine</string>
    <key>CFBundleDisplayName</key>
    <string>PixelEngine</string>
    <key>CFBundleIdentifier</key>
    <string>com.abdulaziz.pixelengine</string>
    <key>CFBundleVersion</key>
    <string>1.0</string>
    <key>CFBundleExecutable</key>
    <string>PixelEngine</string>
    <key>CFBundleIconFile</key>
    <string>icon.icns</string>
    <key>CFBundlePackageType</key>
    <string>APPL</string>
    <key>CFBundleSignature</key>
    <string>????</string>
    <key>NSHighResolutionCapable</key>
    <true/>
    <key>LSUIElement</key>
    <false/>
</dict>
</plist>
EOF

# Build the application
echo "🔨 Building PixelEngine for macOS..."
dotnet publish src/PixelEngine.Mac -c Release -r osx-arm64 --self-contained true -p:PublishSingleFile=true

# Copy the executable
cp src/PixelEngine.Mac/bin/Release/net10.0/osx-arm64/publish/PixelEngine.Mac PixelEngine.app/Contents/MacOS/PixelEngine

# Make it executable
chmod +x PixelEngine.app/Contents/MacOS/PixelEngine

echo "✅ PixelEngine.app created successfully!"
echo "🚀 You can now double-click PixelEngine.app to run the application"
