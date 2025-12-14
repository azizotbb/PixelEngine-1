namespace PixelEngine.Console.Core
{
    /// <summary>
    /// Core class for managing pixels and colors (Console version)
    /// </summary>
    public class PixelManager
    {
        public int Width { get; private set; }
        public int Height { get; private set; }
        private (int R, int G, int B)[,] PixelData { get; set; }

        public PixelManager(int width, int height)
        {
            Width = width;
            Height = height;
            PixelData = new (int R, int G, int B)[width, height];
            InitializePixels();
        }

        /// <summary>
        /// Initialize pixels with white background
        /// </summary>
        private void InitializePixels()
        {
            for (int x = 0; x < Width; x++)
            {
                for (int y = 0; y < Height; y++)
                {
                    PixelData[x, y] = (255, 255, 255); // White
                }
            }
        }

        /// <summary>
        /// Set color of specific pixel
        /// </summary>
        public void SetPixel(int x, int y, (int R, int G, int B) color)
        {
            if (IsValidPosition(x, y))
            {
                PixelData[x, y] = color;
            }
        }

        /// <summary>
        /// Get color of specific pixel
        /// </summary>
        public (int R, int G, int B) GetPixel(int x, int y)
        {
            if (IsValidPosition(x, y))
            {
                return PixelData[x, y];
            }
            return (0, 0, 0); // Black (transparent)
        }

        /// <summary>
        /// Validate pixel position
        /// </summary>
        private bool IsValidPosition(int x, int y)
        {
            return x >= 0 && x < Width && y >= 0 && y < Height;
        }

        /// <summary>
        /// Clear all pixels
        /// </summary>
        public void Clear()
        {
            InitializePixels();
        }

        /// <summary>
        /// Get statistical information about pixels
        /// </summary>
        public PixelStatistics GetStatistics()
        {
            var stats = new PixelStatistics();
            
            for (int x = 0; x < Width; x++)
            {
                for (int y = 0; y < Height; y++)
                {
                    var pixel = PixelData[x, y];
                    
                    // Calculate average colors
                    stats.TotalRed += pixel.R;
                    stats.TotalGreen += pixel.G;
                    stats.TotalBlue += pixel.B;
                    
                    // Count white pixels
                    if (pixel.R == 255 && pixel.G == 255 && pixel.B == 255)
                        stats.WhitePixels++;
                    
                    // Count black pixels
                    if (pixel.R == 0 && pixel.G == 0 && pixel.B == 0)
                        stats.BlackPixels++;
                        
                    stats.TotalPixels++;
                }
            }
            
            if (stats.TotalPixels > 0)
            {
                stats.AverageRed = stats.TotalRed / stats.TotalPixels;
                stats.AverageGreen = stats.TotalGreen / stats.TotalPixels;
                stats.AverageBlue = stats.TotalBlue / stats.TotalPixels;
            }
            
            return stats;
        }
    }

    /// <summary>
    /// Statistics class for pixels
    /// </summary>
    public class PixelStatistics
    {
        public int TotalPixels { get; set; }
        public int WhitePixels { get; set; }
        public int BlackPixels { get; set; }
        public long TotalRed { get; set; }
        public long TotalGreen { get; set; }
        public long TotalBlue { get; set; }
        public double AverageRed { get; set; }
        public double AverageGreen { get; set; }
        public double AverageBlue { get; set; }
    }
}
