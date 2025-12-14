using System;
using System.Threading;

namespace PixelEngine.Mac
{
    class Program
    {
        static void Main(string[] args)
        {
            // Clear screen and set up console
            Console.Clear();
            Console.Title = "PixelEngine - Advanced Graphics Engine";
            
            // Display the application
            ShowPixelEngine();
            
            // Keep the application running
            Console.WriteLine("\nPress any key to exit...");
            Console.ReadKey();
        }
        
        static void ShowPixelEngine()
        {
            // Set colors for Mac terminal
            Console.ForegroundColor = ConsoleColor.Cyan;
            
            // Display ASCII logo
            Console.WriteLine(@"
    ██████╗ ██╗██╗  ██╗███████╗██╗         
    ██╔══██╗██║╚██╗██╔╝██╔════╝██║         
    ██████╔╝██║ ╚███╔╝ █████╗  ██║         
    ██╔═══╝ ██║ ██╔██╗ ██╔══╝  ██║         
    ██║     ██║██╔╝ ██╗███████╗███████╗    
    ╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝╚══════╝    
                                           
    ███████╗███╗   ██╗ ██████╗ ██╗███╗   ██╗███████╗
    ██╔════╝████╗  ██║██╔════╝ ██║████╗  ██║██╔════╝
    █████╗  ██╔██╗ ██║██║  ███╗██║██╔██╗ ██║█████╗  
    ██╔══╝  ██║╚██╗██║██║   ██║██║██║╚██╗██║██╔══╝  
    ███████╗██║ ╚████║╚██████╔╝██║██║ ╚████║███████╗
    ╚══════╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝╚═╝  ╚═══╝╚══════╝
            ");
            
            Console.ResetColor();
            Console.ForegroundColor = ConsoleColor.White;
            Console.WriteLine("\n           Advanced Graphics Engine for Mac");
            Console.WriteLine("              Built with C# .NET 10");
            Console.ResetColor();
            
            // Animated separator
            Console.ForegroundColor = ConsoleColor.Yellow;
            for (int i = 0; i < 70; i++)
            {
                Console.Write("═");
                Thread.Sleep(20);
            }
            Console.WriteLine();
            Console.ResetColor();
            
            // Show features with animation
            ShowFeatures();
            
            // Show pixel demo
            ShowPixelDemo();
        }
        
        static void ShowFeatures()
        {
            Console.ForegroundColor = ConsoleColor.Green;
            Console.WriteLine("\n✨ Features:");
            Console.ResetColor();
            
            string[] features = {
                "🎨 Advanced Pixel Management",
                "🌈 Color Space Conversions", 
                "🎭 Gradient Generation",
                "🔧 Graphics Utilities",
                "💻 Cross-Platform Support",
                "🚀 High Performance"
            };
            
            foreach (var feature in features)
            {
                Console.WriteLine($"   {feature}");
                Thread.Sleep(300);
            }
        }
        
        static void ShowPixelDemo()
        {
            Console.ForegroundColor = ConsoleColor.Magenta;
            Console.WriteLine("\n🚀 Running Demo:");
            Console.ResetColor();
            
            // Simple pixel art display
            Console.WriteLine("\n   Creating 8x8 pixel art:");
            
            // Create a simple pattern
            char[,] pattern = {
                {'█','█','░','░','░','░','█','█'},
                {'█','░','█','░','░','█','░','█'},
                {'░','█','░','█','█','░','█','░'},
                {'░','░','█','█','█','█','░','░'},
                {'░','░','█','█','█','█','░','░'},
                {'░','█','░','█','█','░','█','░'},
                {'█','░','█','░','░','█','░','█'},
                {'█','█','░','░','░','░','█','█'}
            };
            
            Console.WriteLine();
            for (int i = 0; i < 8; i++)
            {
                Console.Write("   ");
                for (int j = 0; j < 8; j++)
                {
                    if (pattern[i,j] == '█')
                        Console.ForegroundColor = ConsoleColor.Red;
                    else if (pattern[i,j] == '░')
                        Console.ForegroundColor = ConsoleColor.Blue;
                    else
                        Console.ForegroundColor = ConsoleColor.White;
                        
                    Console.Write(pattern[i,j] + " ");
                    Thread.Sleep(50);
                }
                Console.WriteLine();
                Console.ResetColor();
            }
            
            Console.ForegroundColor = ConsoleColor.Green;
            Console.WriteLine("\n✅ Demo completed successfully!");
            Console.ResetColor();
            
            // Show system info
            Console.ForegroundColor = ConsoleColor.Cyan;
            Console.WriteLine($"\n💻 Running on: {Environment.OSVersion}");
            Console.WriteLine($"🖥️  Architecture: {Environment.OSVersion.Platform}");
            Console.WriteLine($"📁 Framework: {Environment.Version}");
            Console.ResetColor();
        }
    }
}
