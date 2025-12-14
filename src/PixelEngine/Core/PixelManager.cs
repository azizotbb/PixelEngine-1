namespace PixelEngine.Core
{
    /// <summary>
    /// Core class for managing pixels and colors
    /// </summary>
    public class PixelManager
    {
        public int Width { get; private set; }
        public int Height { get; private set; }
        private Color[,] PixelData { get; set; }

        public PixelManager(int width, int height)
        {
            Width = width;
            Height = height;
            PixelData = new Color[width, height];
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
                    PixelData[x, y] = Colors.White;
                }
            }
        }

        /// <summary>
        /// Set color of specific pixel
        /// </summary>
        public void SetPixel(int x, int y, Color color)
        {
            if (x >= 0 && x < Width && y >= 0 && y < Height)
            {
                PixelData[x, y] = color;
            }
        }

        /// <summary>
        /// Get color of specific pixel
        /// </summary>
        public Color GetPixel(int x, int y)
        {
            if (x >= 0 && x < Width && y >= 0 && y < Height)
            {
                return PixelData[x, y];
            }
            return Colors.Transparent;
        }

        /// <summary>
        /// Clear all pixels
        /// </summary>
        public void Clear()
        {
            InitializePixels();
        }
    }
}
