using System;
using System.Drawing;
using PixelEngine.Console.Core;

namespace PixelEngine.Console
{
    /// <summary>
    /// Main console application for PixelEngine
    /// </summary>
    class Program
    {
        static void Main(string[] args)
        {
            // Display program logo
            DisplayLogo();
            
            // Display program information
            DisplayInfo();
            
            // Display features
            DisplayFeatures();
            
            // Run simple demo
            RunPixelDemo();
            
            // Wait for user input
            System.Console.WriteLine("\nPress any key to exit...");
            System.Console.ReadKey();
        }

        /// <summary>
        /// Display PixelEngine logo
        /// </summary>
        static void DisplayLogo()
        {
            System.Console.Clear();
            System.Console.ForegroundColor = ConsoleColor.Cyan;
            System.Console.WriteLine(@"
    ██████╗ ██╗██╗  ██╗███████╗██╗         ███████╗███╗   ██╗ ██████╗ ██╗███╗   ██╗███████╗
    ██╔══██╗██║╚██╗██╔╝██╔════╝██║         ██╔════╝████╗  ██║██╔════╝ ██║████╗  ██║██╔════╝
    ██████╔╝██║ ╚███╔╝ █████╗  ██║         █████╗  ██╔██╗ ██║██║  ███╗██║██╔██╗ ██║█████╗  
    ██╔═══╝ ██║ ██╔██╗ ██╔══╝  ██║         ██╔══╝  ██║╚██╗██║██║   ██║██║██║╚██╗██║██╔══╝  
    ██║     ██║██╔╝ ██╗███████╗███████╗    ███████╗██║ ╚████║╚██████╔╝██║██║ ╚████║███████╗
    ╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝╚══════╝    ╚══════╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝╚═╝  ╚═══╝╚══════╝
            ");
            
            System.Console.ResetColor();
            System.Console.ForegroundColor = ConsoleColor.White;
            System.Console.WriteLine("\n                               Advanced Graphics Engine");
            System.Console.WriteLine("                               Built with C# .NET 10");
            System.Console.ResetColor();
            
            // Draw colored separator line
            System.Console.ForegroundColor = ConsoleColor.Yellow;
            System.Console.WriteLine(new string('═', 90));
            System.Console.ResetColor();
        }

        /// <summary>
        /// Display program information
        /// </summary>
        static void DisplayInfo()
        {
            System.Console.ForegroundColor = ConsoleColor.Green;
            System.Console.WriteLine("\n📋 Program Information:");
            System.Console.ResetColor();
            
            System.Console.WriteLine("   🏷️  Version: 1.0.0");
            System.Console.WriteLine("   👨‍💻 Developer: AbdulAziz");
            System.Console.WriteLine("   📅 Date: December 2024");
            System.Console.WriteLine("   💻 Platform: .NET 10.0 (Cross-platform compatible)");
        }

        /// <summary>
        /// Display program features
        /// </summary>
        static void DisplayFeatures()
        {
            System.Console.ForegroundColor = ConsoleColor.Magenta;
            System.Console.WriteLine("\n✨ Key Features:");
            System.Console.ResetColor();
            
            string[] features = {
                "🎨 Pixel and color management",
                "🌈 Color space conversions",
                "🎭 Gradient generation",
                "🔧 Advanced graphics utilities",
                "💡 Extensible architecture",
                "🌍 Cross-platform compatible"
            };

            foreach (string feature in features)
            {
                System.Console.WriteLine($"   {feature}");
                System.Threading.Thread.Sleep(200); // Typing effect
            }
        }

        /// <summary>
        /// Run simple pixel demo
        /// </summary>
        static void RunPixelDemo()
        {
            System.Console.ForegroundColor = ConsoleColor.Yellow;
            System.Console.WriteLine("\n🚀 Running PixelEngine demo...");
            System.Console.ResetColor();

            try
            {
                // Create pixel manager
                var pixelManager = new PixelManager(10, 10);
                
                System.Console.WriteLine("\n✅ Pixel manager created successfully (10x10)");
                
                // Set some colored pixels
                pixelManager.SetPixel(0, 0, (255, 0, 0));     // Red
                pixelManager.SetPixel(1, 1, (0, 255, 0));     // Green  
                pixelManager.SetPixel(2, 2, (0, 0, 255));     // Blue
                pixelManager.SetPixel(3, 3, (255, 255, 0));   // Yellow
                
                System.Console.WriteLine("✅ Colored pixels set");
                
                // Display pixel information
                System.Console.ForegroundColor = ConsoleColor.Cyan;
                System.Console.WriteLine("\n📊 Pixel Information:");
                System.Console.ResetColor();
                
                System.Console.WriteLine($"   Pixel (0,0): RGB{pixelManager.GetPixel(0, 0)}");
                System.Console.WriteLine($"   Pixel (1,1): RGB{pixelManager.GetPixel(1, 1)}");
                System.Console.WriteLine($"   Pixel (2,2): RGB{pixelManager.GetPixel(2, 2)}");
                System.Console.WriteLine($"   Pixel (3,3): RGB{pixelManager.GetPixel(3, 3)}");
                
                // Test gradient
                System.Console.ForegroundColor = ConsoleColor.Green;
                System.Console.WriteLine("\n🎨 Creating color gradient:");
                System.Console.ResetColor();
                
                var gradient = GraphicsUtilities.CreateGradient((255, 0, 0), (0, 0, 255), 5);
                for (int i = 0; i < gradient.Length; i++)
                {
                    System.Console.WriteLine($"   Step {i + 1}: RGB{gradient[i]}");
                }
                
                // Color conversion
                System.Console.ForegroundColor = ConsoleColor.Magenta;
                System.Console.WriteLine("\n🔄 RGB to HSL conversion:");
                System.Console.ResetColor();
                
                var redColor = (255, 0, 0);
                var hsl = GraphicsUtilities.RgbToHsl(redColor.Item1, redColor.Item2, redColor.Item3);
                System.Console.WriteLine($"   Red RGB(255,0,0) = HSL({hsl.H:F1}°, {hsl.S:F1}%, {hsl.L:F1}%)");
                
                System.Console.ForegroundColor = ConsoleColor.Green;
                System.Console.WriteLine("\n🎉 Demo completed successfully!");
                System.Console.ResetColor();
            }
            catch (Exception ex)
            {
                System.Console.ForegroundColor = ConsoleColor.Red;
                System.Console.WriteLine($"\n❌ Error occurred: {ex.Message}");
                System.Console.ResetColor();
            }
        }
    }
}
