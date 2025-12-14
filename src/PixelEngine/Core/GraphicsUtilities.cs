using System.Windows.Media;

namespace PixelEngine.Core
{
    /// <summary>
    /// Graphics utilities for colors and drawing
    /// </summary>
    public static class GraphicsUtilities
    {
        /// <summary>
        /// Convert RGB to HSL
        /// </summary>
        public static (double H, double S, double L) RgbToHsl(Color color)
        {
            double r = color.R / 255.0;
            double g = color.G / 255.0;
            double b = color.B / 255.0;

            double max = Math.Max(r, Math.Max(g, b));
            double min = Math.Min(r, Math.Min(g, b));

            double h = 0, s = 0, l = (max + min) / 2;

            if (max != min)
            {
                double delta = max - min;
                s = l > 0.5 ? delta / (2 - max - min) : delta / (max + min);

                if (max == r)
                    h = (g - b) / delta + (g < b ? 6 : 0);
                else if (max == g)
                    h = (b - r) / delta + 2;
                else if (max == b)
                    h = (r - g) / delta + 4;

                h /= 6;
            }

            return (h * 360, s * 100, l * 100);
        }

        /// <summary>
        /// Create color gradient
        /// </summary>
        public static Color[] CreateGradient(Color startColor, Color endColor, int steps)
        {
            Color[] gradient = new Color[steps];

            for (int i = 0; i < steps; i++)
            {
                double ratio = (double)i / (steps - 1);

                byte r = (byte)(startColor.R + (endColor.R - startColor.R) * ratio);
                byte g = (byte)(startColor.G + (endColor.G - startColor.G) * ratio);
                byte b = (byte)(startColor.B + (endColor.B - startColor.B) * ratio);
                byte a = (byte)(startColor.A + (endColor.A - startColor.A) * ratio);

                gradient[i] = Color.FromArgb(a, r, g, b);
            }

            return gradient;
        }

        /// <summary>
        /// Apply simple blur filter
        /// </summary>
        public static Color BlurPixel(PixelManager pixelManager, int x, int y, int radius = 1)
        {
            int totalR = 0, totalG = 0, totalB = 0, count = 0;

            for (int dx = -radius; dx <= radius; dx++)
            {
                for (int dy = -radius; dy <= radius; dy++)
                {
                    Color pixel = pixelManager.GetPixel(x + dx, y + dy);
                    if (pixel != Colors.Transparent)
                    {
                        totalR += pixel.R;
                        totalG += pixel.G;
                        totalB += pixel.B;
                        count++;
                    }
                }
            }

            if (count > 0)
            {
                return Color.FromRgb(
                    (byte)(totalR / count),
                    (byte)(totalG / count),
                    (byte)(totalB / count)
                );
            }

            return Colors.White;
        }
    }
}
