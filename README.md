# PixelEngine

Advanced graphics engine built with C# and WPF featuring a clean white background and elegant user interface.

## ✨ Features

- 🎨 **Elegant UI** - Modern design with clean white background
- 🌈 **Pixel Management** - Advanced pixel and color management system
- 🎭 **Animations** - Beautiful visual effects and smooth animations
- 🛠️ **Graphics Tools** - Comprehensive color and graphics utilities
- 🔧 **Extensible** - Clean and scalable architecture

## 🏗️ Project Structure

```
PixelEngine-CSharp/
├── PixelEngine.sln                 # Main solution file
├── run-mac.sh                      # Quick launcher for Mac
├── create-mac-app.sh               # Create Mac app bundle
├── src/
│   ├── PixelEngine/                # WPF Application (Windows)
│   │   ├── PixelEngine.csproj      # Project file
│   │   ├── App.xaml                # Main WPF application
│   │   ├── App.xaml.cs             # Application code
│   │   ├── MainWindow.xaml         # Main window
│   │   ├── MainWindow.xaml.cs      # Main window code
│   │   ├── GlobalUsings.cs         # Global using statements
│   │   └── Core/
│   │       ├── PixelManager.cs     # Pixel management
│   │       └── GraphicsUtilities.cs # Graphics utilities
│   ├── PixelEngine.Console/        # Console Application (Cross-platform)
│   │   ├── PixelEngine.Console.csproj # Project file
│   │   ├── Program.cs              # Main program with ASCII logo
│   │   └── Core/
│   │       ├── PixelManager.cs     # Pixel management
│   │       └── GraphicsUtilities.cs # Graphics utilities
│   └── PixelEngine.Mac/            # Mac-optimized version
│       ├── PixelEngine.Mac.csproj  # Project file
│       └── Program.cs              # Mac-specific optimizations
└── README.md                       # This file
```

## 🚀 Getting Started

### Requirements
- .NET 10.0 or later
- macOS 10.15+ (for Mac version)
- Windows 10+ (for WPF version)
- Visual Studio 2022 or VS Code

### Quick Start (macOS)

1. **Clone the repository**
```bash
git clone https://github.com/azizotbb/PixelEngine-CSharp.git
cd PixelEngine-CSharp
```

2. **Run directly on Mac**
```bash
./run-mac.sh
```

3. **Create Mac App Bundle (Optional)**
```bash
./create-mac-app.sh
```
Then double-click `PixelEngine.app` to run

### Build and Run (All Platforms)

**For Console version (cross-platform):**
```bash
dotnet run --project src/PixelEngine.Console
```

**For Mac-optimized version:**
```bash
dotnet run --project src/PixelEngine.Mac
```

**For WPF version (Windows only):**
```bash
dotnet run --project src/PixelEngine
```

Or using Visual Studio:
1. Open `PixelEngine.sln`
2. Press F5 to run

## 🎯 Usage

### Main Interface
- **PixelEngine Logo** - Colorful logo displayed at top
- **Main Title** - "PixelEngine" with elegant fonts and visual effects
- **Subtitle** - Engine description
- **Loading Bar** - Animated progress bar
- **Control Buttons** - "About" and "Exit" buttons

### Core Components

#### PixelManager
```csharp
var pixelManager = new PixelManager(800, 600);
pixelManager.SetPixel(100, 100, Colors.Red);
Color pixelColor = pixelManager.GetPixel(100, 100);
```

#### GraphicsUtilities
```csharp
// RGB to HSL conversion
var hsl = GraphicsUtilities.RgbToHsl(Colors.Red);

// Create color gradient
var gradient = GraphicsUtilities.CreateGradient(Colors.Blue, Colors.Red, 10);

// Apply blur filter
var blurredColor = GraphicsUtilities.BlurPixel(pixelManager, x, y, radius);
```

## 🎨 Design

### Color Palette
- **Background**: Pure white (`#FFFFFF`)
- **Primary Text**: Dark gray (`#2C3E50`)
- **Secondary Text**: Medium gray (`#7F8C8D`)
- **Buttons**: Blue (`#3498DB`) and Red (`#E74C3C`)
- **Pixel Logo**: Vibrant and diverse colors

### Typography
- **Main Title**: Segoe UI Light, 48px
- **Body Text**: Segoe UI, 18px
- **Buttons**: Segoe UI, 14px

## 🔧 Development

### Adding New Features
1. Add new files in appropriate folders
2. Use `GlobalUsings.cs` for common imports
3. Follow existing naming and documentation patterns

### Dependencies
- `Microsoft.WindowsAPICodePack.Shell` - For OS integration

## 📄 License

This project is open source and available under the MIT License.

## 👤 Developer

**AbdulAziz**
- GitHub: [@azizotbb](https://github.com/azizotbb)

## 🤝 Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Submit a Pull Request

---

**PixelEngine** - Advanced graphics engine built with ❤️