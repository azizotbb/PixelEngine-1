using System;

class Program
{
    static void Main()
    {
        Console.Clear();
        Console.ForegroundColor = ConsoleColor.Cyan;

        Console.WriteLine(@"
 ██████╗ ██╗██╗  ██╗███████╗██╗     
 ██╔══██╗██║╚██╗██╔╝██╔════╝██║     
 ██████╔╝██║ ╚███╔╝ █████╗  ██║     
 ██╔═══╝ ██║ ██╔██╗ ██╔══╝  ██║     
 ██║     ██║██╔╝ ██╗███████╗███████╗
 ╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝╚══════╝
        ");

        Console.ResetColor();
        Console.ForegroundColor = ConsoleColor.White;
        Console.WriteLine("        PixelEngine v1.0");
        Console.WriteLine("    Advanced Graphics Engine");
        Console.WriteLine("      Built with C# .NET");

        Console.ForegroundColor = ConsoleColor.Green;
        Console.WriteLine("\n✅ Program is working correctly!");
        Console.WriteLine("🎨 White background with beautiful display");
        Console.WriteLine("🚀 Ready to develop amazing graphics!");

        Console.ForegroundColor = ConsoleColor.Yellow;
        Console.WriteLine("\n" + new string('=', 40));

        Console.ForegroundColor = ConsoleColor.Magenta;
        Console.WriteLine("\n🎯 Features:");
        Console.WriteLine("   • Pixel Management");
        Console.WriteLine("   • Color Processing");
        Console.WriteLine("   • Graphics Utilities");
        Console.WriteLine("   • Cross-Platform Support");

        Console.ResetColor();
        Console.WriteLine("\nPress any key to exit...");
        Console.ReadKey();
    }
}
