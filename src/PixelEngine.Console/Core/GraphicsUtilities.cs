using System;

namespace PixelEngine.Console.Core
{
    /// <summary>
    /// Graphics utilities for colors and drawing (Console version)
    /// </summary>
    public static class GraphicsUtilities
    {
        /// <summary>
        /// Convert RGB to HSL
        /// </summary>
        public static (double H, double S, double L) RgbToHsl(int r, int g, int b)
        {
            double rNorm = r / 255.0;
            double gNorm = g / 255.0;
            double bNorm = b / 255.0;

            double max = Math.Max(rNorm, Math.Max(gNorm, bNorm));
            double min = Math.Min(rNorm, Math.Min(gNorm, bNorm));

            double h = 0, s = 0, l = (max + min) / 2;

            if (Math.Abs(max - min) > 0.0001)
            {
                double delta = max - min;
                s = l > 0.5 ? delta / (2 - max - min) : delta / (max + min);

                if (Math.Abs(max - rNorm) < 0.0001)
                    h = (gNorm - bNorm) / delta + (gNorm < bNorm ? 6 : 0);
                else if (Math.Abs(max - gNorm) < 0.0001)
                    h = (bNorm - rNorm) / delta + 2;
                else if (Math.Abs(max - bNorm) < 0.0001)
                    h = (rNorm - gNorm) / delta + 4;

                h /= 6;
            }

            return (h * 360, s * 100, l * 100);
        }

        /// <summary>
        /// Convert HSL to RGB
        /// </summary>
        public static (int R, int G, int B) HslToRgb(double h, double s, double l)
        {
            h /= 360.0;
            s /= 100.0;
            l /= 100.0;

            double r, g, b;

            if (Math.Abs(s) < 0.0001)
            {
                r = g = b = l; // Grayscale
            }
            else
            {
                double q = l < 0.5 ? l * (1 + s) : l + s - l * s;
                double p = 2 * l - q;

                r = HueToRgb(p, q, h + 1.0 / 3.0);
                g = HueToRgb(p, q, h);
                b = HueToRgb(p, q, h - 1.0 / 3.0);
            }

            return ((int)(r * 255), (int)(g * 255), (int)(b * 255));
        }

        /// <summary>
        /// Helper function for Hue to RGB conversion
        /// </summary>
        private static double HueToRgb(double p, double q, double t)
        {
            if (t < 0) t += 1;
            if (t > 1) t -= 1;
            if (t < 1.0 / 6.0) return p + (q - p) * 6 * t;
            if (t < 1.0 / 2.0) return q;
            if (t < 2.0 / 3.0) return p + (q - p) * (2.0 / 3.0 - t) * 6;
            return p;
        }

        /// <summary>
        /// Create color gradient between two colors
        /// </summary>
        public static (int R, int G, int B)[] CreateGradient(
            (int R, int G, int B) startColor, 
            (int R, int G, int B) endColor, 
            int steps)
        {
            if (steps <= 0) throw new ArgumentException("Number of steps must be greater than zero", nameof(steps));
            
            var gradient = new (int R, int G, int B)[steps];

            for (int i = 0; i < steps; i++)
            {
                double ratio = steps == 1 ? 0 : (double)i / (steps - 1);

                int r = (int)(startColor.R + (endColor.R - startColor.R) * ratio);
                int g = (int)(startColor.G + (endColor.G - startColor.G) * ratio);
                int b = (int)(startColor.B + (endColor.B - startColor.B) * ratio);

                gradient[i] = (r, g, b);
            }

            return gradient;
        }

        /// <summary>
        /// Blend two colors with specified ratio
        /// </summary>
        public static (int R, int G, int B) BlendColors(
            (int R, int G, int B) color1, 
            (int R, int G, int B) color2, 
            double ratio)
        {
            if (ratio < 0 || ratio > 1)
                throw new ArgumentException("Ratio must be between 0 and 1", nameof(ratio));

            int r = (int)(color1.R * (1 - ratio) + color2.R * ratio);
            int g = (int)(color1.G * (1 - ratio) + color2.G * ratio);
            int b = (int)(color1.B * (1 - ratio) + color2.B * ratio);

            return (r, g, b);
        }

        /// <summary>
        /// Apply brightness filter
        /// </summary>
        public static (int R, int G, int B) AdjustBrightness((int R, int G, int B) color, double factor)
        {
            int r = Math.Max(0, Math.Min(255, (int)(color.R * factor)));
            int g = Math.Max(0, Math.Min(255, (int)(color.G * factor)));
            int b = Math.Max(0, Math.Min(255, (int)(color.B * factor)));

            return (r, g, b);
        }

        /// <summary>
        /// Calculate distance between two colors
        /// </summary>
        public static double CalculateColorDistance(
            (int R, int G, int B) color1, 
            (int R, int G, int B) color2)
        {
            double rDiff = color1.R - color2.R;
            double gDiff = color1.G - color2.G;
            double bDiff = color1.B - color2.B;

            return Math.Sqrt(rDiff * rDiff + gDiff * gDiff + bDiff * bDiff);
        }

        /// <summary>
        /// Convert color to grayscale
        /// </summary>
        public static (int R, int G, int B) ToGrayscale((int R, int G, int B) color)
        {
            // Use standard luminance formula for grayscale
            int gray = (int)(0.299 * color.R + 0.587 * color.G + 0.114 * color.B);
            return (gray, gray, gray);
        }

        /// <summary>
        /// Invert color
        /// </summary>
        public static (int R, int G, int B) InvertColor((int R, int G, int B) color)
        {
            return (255 - color.R, 255 - color.G, 255 - color.B);
        }
    }
}
