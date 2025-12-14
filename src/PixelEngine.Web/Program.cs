var builder = WebApplication.CreateBuilder(args);

var app = builder.Build();

app.UseStaticFiles();

app.MapGet("/", () => Results.Content(@"
<!DOCTYPE html>
<html lang='en'>
<head>
    <meta charset='UTF-8'>
    <meta name='viewport' content='width=device-width, initial-scale=1.0'>
    <title>PixelEngine - Advanced Graphics Engine</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #ffffff 0%, #f8f9fa 50%, #ffffff 100%);
            min-height: 100vh;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
        }
        
        .container {
            text-align: center;
            background: white;
            padding: 60px 40px;
            border-radius: 20px;
            box-shadow: 0 20px 60px rgba(0,0,0,0.1);
            max-width: 800px;
            width: 90%;
        }
        
        .pixel-logo {
            display: flex;
            justify-content: center;
            gap: 5px;
            margin-bottom: 30px;
            flex-wrap: wrap;
        }
        
        .pixel {
            width: 20px;
            height: 20px;
            border-radius: 3px;
            animation: pulse 2s infinite ease-in-out;
        }
        
        .pixel:nth-child(1) { background: #4A90E2; animation-delay: 0s; }
        .pixel:nth-child(2) { background: #7ED321; animation-delay: 0.1s; }
        .pixel:nth-child(3) { background: #F5A623; animation-delay: 0.2s; }
        .pixel:nth-child(4) { background: #D0021B; animation-delay: 0.3s; }
        .pixel:nth-child(5) { background: #BD10E0; animation-delay: 0.4s; }
        .pixel:nth-child(6) { background: #50E3C2; animation-delay: 0.5s; }
        .pixel:nth-child(7) { background: #B8E986; animation-delay: 0.6s; }
        .pixel:nth-child(8) { background: #F8E71C; animation-delay: 0.7s; }
        
        @keyframes pulse {
            0%, 100% { transform: scale(1); opacity: 1; }
            50% { transform: scale(1.2); opacity: 0.8; }
        }
        
        h1 {
            font-size: 4rem;
            font-weight: 300;
            color: #2C3E50;
            margin: 30px 0 20px 0;
            animation: slideInUp 1s ease-out;
        }
        
        .subtitle {
            font-size: 1.5rem;
            color: #7F8C8D;
            margin-bottom: 40px;
            animation: slideInUp 1s ease-out 0.2s both;
        }
        
        .features {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 20px;
            margin: 40px 0;
            animation: slideInUp 1s ease-out 0.4s both;
        }
        
        .feature {
            padding: 20px;
            background: #f8f9fa;
            border-radius: 10px;
            border-left: 4px solid #3498DB;
        }
        
        .buttons {
            display: flex;
            gap: 20px;
            justify-content: center;
            margin-top: 40px;
            animation: slideInUp 1s ease-out 0.6s both;
        }
        
        .btn {
            padding: 15px 30px;
            border: none;
            border-radius: 8px;
            font-size: 1.1rem;
            cursor: pointer;
            transition: all 0.3s ease;
            text-decoration: none;
            display: inline-block;
        }
        
        .btn-primary {
            background: #3498DB;
            color: white;
        }
        
        .btn-primary:hover {
            background: #2980B9;
            transform: translateY(-2px);
        }
        
        .btn-secondary {
            background: #95a5a6;
            color: white;
        }
        
        .btn-secondary:hover {
            background: #7f8c8d;
            transform: translateY(-2px);
        }
        
        @keyframes slideInUp {
            from {
                opacity: 0;
                transform: translateY(30px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }
        
        .status-bar {
            position: fixed;
            bottom: 0;
            left: 0;
            right: 0;
            background: #34495E;
            color: white;
            padding: 10px 20px;
            display: flex;
            justify-content: space-between;
            font-size: 0.9rem;
        }
        
        .demo-canvas {
            margin: 30px auto;
            border: 2px solid #ecf0f1;
            border-radius: 10px;
            animation: slideInUp 1s ease-out 0.8s both;
        }
    </style>
</head>
<body>
    <div class='container'>
        <div class='pixel-logo'>
            <div class='pixel'></div>
            <div class='pixel'></div>
            <div class='pixel'></div>
            <div class='pixel'></div>
            <div class='pixel'></div>
            <div class='pixel'></div>
            <div class='pixel'></div>
            <div class='pixel'></div>
        </div>
        
        <h1>PixelEngine</h1>
        <div class='subtitle'>Advanced Graphics Engine</div>
        
        <div class='features'>
            <div class='feature'>
                <h3>🎨 Pixel Management</h3>
                <p>Advanced pixel manipulation and color processing</p>
            </div>
            <div class='feature'>
                <h3>🌈 Color Processing</h3>
                <p>RGB, HSL conversions and gradient generation</p>
            </div>
            <div class='feature'>
                <h3>🔧 Graphics Utilities</h3>
                <p>Comprehensive graphics tools and filters</p>
            </div>
            <div class='feature'>
                <h3>💻 Cross-Platform</h3>
                <p>Works on Mac, Windows, and Linux</p>
            </div>
        </div>
        
        <canvas class='demo-canvas' id='demoCanvas' width='400' height='200'></canvas>
        
        <div class='buttons'>
            <button class='btn btn-primary' onclick='runDemo()'>Run Demo</button>
            <button class='btn btn-secondary' onclick='showAbout()'>About</button>
        </div>
    </div>
    
    <div class='status-bar'>
        <span>Ready</span>
        <span>PixelEngine v1.0 - Running on Mac</span>
    </div>
    
    <script>
        function runDemo() {
            const canvas = document.getElementById('demoCanvas');
            const ctx = canvas.getContext('2d');
            
            // Clear canvas
            ctx.clearRect(0, 0, canvas.width, canvas.height);
            
            // Draw animated pixels
            const colors = ['#4A90E2', '#7ED321', '#F5A623', '#D0021B', '#BD10E0', '#50E3C2', '#B8E986', '#F8E71C'];
            const pixelSize = 20;
            let frame = 0;
            
            function animate() {
                ctx.clearRect(0, 0, canvas.width, canvas.height);
                
                for (let x = 0; x < 20; x++) {
                    for (let y = 0; y < 10; y++) {
                        const colorIndex = (x + y + frame) % colors.length;
                        ctx.fillStyle = colors[colorIndex];
                        ctx.fillRect(x * pixelSize, y * pixelSize, pixelSize - 2, pixelSize - 2);
                    }
                }
                
                frame++;
                if (frame < 50) {
                    setTimeout(animate, 100);
                }
            }
            
            animate();
        }
        
        function showAbout() {
            alert('PixelEngine v1.0\\n\\nAdvanced Graphics Engine\\nBuilt with C# and ASP.NET Core\\n\\nDeveloped by: AbdulAziz\\n\\nRunning in your web browser on Mac!');
        }
        
        // Auto-run demo on load
        window.onload = function() {
            setTimeout(runDemo, 1000);
        };
    </script>
</body>
</html>
", "text/html"));

Console.WriteLine("🚀 PixelEngine Web Server Started!");
Console.WriteLine("🌐 Open your browser and go to: http://localhost:5000");
Console.WriteLine("📱 The application will open in your default web browser");
Console.WriteLine("⏹️  Press Ctrl+C to stop the server");

// Auto-open browser
try
{
    System.Diagnostics.Process.Start(new System.Diagnostics.ProcessStartInfo
    {
        FileName = "open",
        Arguments = "http://localhost:5000",
        UseShellExecute = true
    });
}
catch
{
    Console.WriteLine("Could not auto-open browser. Please manually open http://localhost:5000");
}

app.Run();
