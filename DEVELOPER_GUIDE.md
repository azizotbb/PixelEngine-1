# دليل المطور - PixelEngine

## 📚 نظرة عامة

PixelEngine هو محرك رسومات متقدم مكتوب بـ C# مع دعم لنظامين:

- **WPF Application** - للويندوز مع واجهة رسومية أنيقة
- **Console Application** - لجميع الأنظمة (Windows, macOS, Linux)

## 🏗️ البنية المعمارية

### المكونات الأساسية

#### 1. PixelManager

مسؤول عن إدارة البكسلات والألوان:

```csharp
// إنشاء مدير البكسلات
var pixelManager = new PixelManager(800, 600);

// تعيين بكسل ملون
pixelManager.SetPixel(100, 100, (255, 0, 0)); // أحمر

// قراءة بكسل
var color = pixelManager.GetPixel(100, 100);
```

#### 2. GraphicsUtilities

مجموعة من الأدوات المساعدة للمعالجة الرسومية:

```csharp
// تحويل الألوان
var hsl = GraphicsUtilities.RgbToHsl(255, 0, 0);

// إنشاء تدرج
var gradient = GraphicsUtilities.CreateGradient(
    (255, 0, 0),    // أحمر
    (0, 0, 255),    // أزرق
    10              // 10 خطوات
);

// مزج الألوان
var blended = GraphicsUtilities.BlendColors(
    (255, 0, 0),    // أحمر
    (0, 255, 0),    // أخضر
    0.5             // نسبة 50%
);
```

## 🎨 أمثلة الاستخدام

### إنشاء لوحة ألوان

```csharp
var pixelManager = new PixelManager(256, 256);

// إنشاء تدرج أفقي من الأسود للأبيض
for (int x = 0; x < 256; x++)
{
    var gray = (byte)x;
    for (int y = 0; y < 256; y++)
    {
        pixelManager.SetPixel(x, y, (gray, gray, gray));
    }
}
```

### تطبيق فلاتر الألوان

```csharp
// تحويل صورة للرمادي
for (int x = 0; x < width; x++)
{
    for (int y = 0; y < height; y++)
    {
        var originalColor = pixelManager.GetPixel(x, y);
        var grayColor = GraphicsUtilities.ToGrayscale(originalColor);
        pixelManager.SetPixel(x, y, grayColor);
    }
}
```

### إنشاء دائرة ملونة

```csharp
void DrawCircle(PixelManager pm, int centerX, int centerY, int radius, (int R, int G, int B) color)
{
    for (int x = centerX - radius; x <= centerX + radius; x++)
    {
        for (int y = centerY - radius; y <= centerY + radius; y++)
        {
            int dx = x - centerX;
            int dy = y - centerY;

            if (dx * dx + dy * dy <= radius * radius)
            {
                pm.SetPixel(x, y, color);
            }
        }
    }
}
```

## 🔧 التطوير والتوسع

### إضافة فلاتر جديدة

1. أضف الدالة في `GraphicsUtilities`:

```csharp
public static (int R, int G, int B) MyCustomFilter((int R, int G, int B) color)
{
    // معالجة مخصصة للألوان
    return (modifiedR, modifiedG, modifiedB);
}
```

2. استخدمها في الكود:

```csharp
var filteredColor = GraphicsUtilities.MyCustomFilter(originalColor);
```

### إضافة أشكال هندسية

إنشاء فئة جديدة للأشكال:

```csharp
public static class GeometricShapes
{
    public static void DrawRectangle(PixelManager pm, int x, int y, int width, int height, (int R, int G, int B) color)
    {
        for (int i = x; i < x + width; i++)
        {
            for (int j = y; j < y + height; j++)
            {
                pm.SetPixel(i, j, color);
            }
        }
    }
}
```

## 🧪 اختبار الأداء

### قياس سرعة المعالجة

```csharp
var stopwatch = System.Diagnostics.Stopwatch.StartNew();

// عملية معالجة البكسلات
for (int i = 0; i < 1000000; i++)
{
    pixelManager.SetPixel(i % width, (i / width) % height, (255, 0, 0));
}

stopwatch.Stop();
Console.WriteLine($"وقت المعالجة: {stopwatch.ElapsedMilliseconds} ms");
```

### اختبار الذاكرة

```csharp
var initialMemory = GC.GetTotalMemory(false);

// إنشاء بيانات كبيرة
var largePixelManager = new PixelManager(4000, 4000);

var finalMemory = GC.GetTotalMemory(false);
Console.WriteLine($"استهلاك الذاكرة: {(finalMemory - initialMemory) / 1024 / 1024} MB");
```

## 📊 تحليل الألوان

### استخراج الألوان السائدة

```csharp
public static Dictionary<(int R, int G, int B), int> GetColorFrequency(PixelManager pm)
{
    var colorCount = new Dictionary<(int R, int G, int B), int>();

    for (int x = 0; x < pm.Width; x++)
    {
        for (int y = 0; y < pm.Height; y++)
        {
            var color = pm.GetPixel(x, y);

            if (colorCount.ContainsKey(color))
                colorCount[color]++;
            else
                colorCount[color] = 1;
        }
    }

    return colorCount.OrderByDescending(kvp => kvp.Value)
                    .ToDictionary(kvp => kvp.Key, kvp => kvp.Value);
}
```

## 🎯 أفضل الممارسات

### 1. إدارة الذاكرة

- استخدم `using` statements للموارد القابلة للتخلص
- قم بتنظيف البكسلات الكبيرة عند الانتهاء
- راقب استهلاك الذاكرة في التطبيقات الكبيرة

### 2. الأداء

- استخدم `Parallel.For` للعمليات الكبيرة:

```csharp
Parallel.For(0, height, y =>
{
    for (int x = 0; x < width; x++)
    {
        // معالجة البكسل
    }
});
```

### 3. معالجة الأخطاء

```csharp
try
{
    pixelManager.SetPixel(x, y, color);
}
catch (ArgumentOutOfRangeException)
{
    Console.WriteLine($"البكسل ({x}, {y}) خارج النطاق");
}
```

## 🔮 التطويرات المستقبلية

- دعم تنسيقات الصور (PNG, JPEG, BMP)
- فلاتر رسومية متقدمة (Gaussian Blur, Edge Detection)
- دعم الرسوم المتحركة
- واجهة برمجة تطبيقات RESTful
- دعم GPU للمعالجة المتوازية

## 📞 الدعم

لأي استفسارات أو مشاكل:

- GitHub Issues
- التوثيق في الكود
- أمثلة في مجلد `examples/`

---

**PixelEngine** - محرك رسومات قوي ومرن لجميع احتياجاتك الرسومية! 🚀
