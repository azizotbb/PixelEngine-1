using System;
using System.Threading;

namespace PixelEngine.MacApp
{
    public class Program
    {
        private static string[] titleFrames = {
            @"
╔═══════════════════════════════════════════════╗
║                                               ║
║   ████████╗ ██╗ ██╗  ██╗ ███████╗ ██╗        ║
║   ██╔══██║ ██║ ╚██╗██╔╝ ██╔════╝ ██║        ║
║   ████████║ ██║  ╚███╔╝  █████╗   ██║        ║
║   ██╔══██║ ██║  ██╔██╗  ██╔══╝   ██║        ║
║   ██║  ██║ ██║ ██╔╝ ██╗ ███████╗ ███████╗   ║
║   ╚═╝  ╚═╝ ╚═╝ ╚═╝  ╚═╝ ╚══════╝ ╚══════╝   ║
║                                               ║
║              ENGINE  v1.0                    ║
║                                               ║
╚═══════════════════════════════════════════════╝
",
            @"
╔═══════════════════════════════════════════════╗
║                                               ║
║   ██████╗  ██╗ ██╗  ██╗ ███████╗ ██╗         ║
║   ██╔══██╗ ██║ ╚██╗██╔╝ ██╔════╝ ██║         ║
║   ██████╔╝ ██║  ╚███╔╝  █████╗   ██║         ║
║   ██╔═══╝  ██║  ██╔██╗  ██╔══╝   ██║         ║
║   ██║      ██║ ██╔╝ ██╗ ███████╗ ███████╗    ║
║   ╚═╝      ╚═╝ ╚═╝  ╚═╝ ╚══════╝ ╚══════╝    ║
║                                               ║
║              ENGINE  v1.0                    ║
║                                               ║
╚═══════════════════════════════════════════════╝
"
        };

        public static void Main(string[] args)
        {
            Console.Title = "PixelEngine - Graphics Engine";

            // Force white background and black text
            Console.BackgroundColor = ConsoleColor.White;
            Console.ForegroundColor = ConsoleColor.Black;
            Console.Clear();

            // Set terminal size for better display
            try
            {
                Console.SetWindowSize(80, 30);
            }
            catch { /* Ignore if not supported */ }

            // Welcome message
            Console.ForegroundColor = ConsoleColor.DarkBlue;
            Console.WriteLine("\n   🎨 Welcome to PixelEngine!");
            Console.WriteLine("   🚀 A Beautiful Graphics Engine for Mac\n");

            // Animated title with better colors
            for (int i = 0; i < 3; i++)
            {
                Console.Clear();
                Console.BackgroundColor = ConsoleColor.White;
                Console.ForegroundColor = ConsoleColor.DarkBlue;
                Console.WriteLine("\n🎨 PixelEngine Graphics Engine v1.0\n");
                Console.WriteLine(titleFrames[i % 2]);

                // Colorful features with emojis
                Console.ForegroundColor = ConsoleColor.DarkGreen;
                Console.WriteLine("   🚀 Cross-platform graphics");
                Console.ForegroundColor = ConsoleColor.DarkMagenta;
                Console.WriteLine("   ✨ Beautiful rendering");
                Console.ForegroundColor = ConsoleColor.DarkRed;
                Console.WriteLine("   🖥️  Mac optimized");
                Console.ForegroundColor = ConsoleColor.DarkCyan;
                Console.WriteLine("   ⚡ High performance");

                Console.ForegroundColor = ConsoleColor.Black;
                Console.WriteLine("\n   Loading... Press any key to continue");

                Thread.Sleep(1000);
            }

            // Final display with better formatting
            Console.Clear();
            Console.BackgroundColor = ConsoleColor.White;
            Console.ForegroundColor = ConsoleColor.DarkBlue;
            Console.WriteLine("\n🎨 PixelEngine Graphics Engine v1.0\n");
            Console.WriteLine(titleFrames[0]);

            // Menu with better styling
            Console.ForegroundColor = ConsoleColor.DarkGreen;
            Console.WriteLine("   📋 Features:");
            Console.WriteLine("   • 2D/3D Graphics Rendering");
            Console.WriteLine("   • Pixel-perfect animations");
            Console.WriteLine("   • Cross-platform support");
            Console.WriteLine("   • Easy-to-use API");

            Console.ForegroundColor = ConsoleColor.DarkMagenta;
            Console.WriteLine("\n   📊 System Info:");
            Console.WriteLine($"   🎯 Status: Ready");
            Console.WriteLine($"   🖥️  Platform: {Environment.OSVersion.Platform}");
            Console.WriteLine($"   📦 Version: 1.0.0");
            Console.WriteLine($"   👤 Author: AbdulAziz");

            Console.ForegroundColor = ConsoleColor.DarkRed;
            Console.WriteLine("\n   🚀 PixelEngine is ready to use!");
            Console.ForegroundColor = ConsoleColor.Black;
            Console.WriteLine("\n   Press any key to exit...");
            Console.ReadKey();
        }
    }
}
