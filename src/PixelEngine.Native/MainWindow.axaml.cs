using Avalonia.Controls;
using Avalonia.Interactivity;
using Avalonia.Media;
using Avalonia.Threading;
using System;

namespace PixelEngine.Native;

public partial class MainWindow : Window
{
    private DispatcherTimer? _timer;
    private int _animationStep = 0;

    public MainWindow()
    {
        InitializeComponent();
        SetupWindow();
        StartAnimation();
    }

    private void SetupWindow()
    {
        Title = "PixelEngine - Advanced Graphics Engine";
        Width = 800;
        Height = 600;
        Background = Brushes.White;
        WindowStartupLocation = WindowStartupLocation.CenterScreen;
    }

    private void StartAnimation()
    {
        _timer = new DispatcherTimer
        {
            Interval = TimeSpan.FromMilliseconds(500)
        };
        _timer.Tick += Timer_Tick;
        _timer.Start();
    }

    private void Timer_Tick(object? sender, EventArgs e)
    {
        _animationStep++;
        // Force redraw
        InvalidateVisual();
    }

    private void AboutButton_Click(object? sender, RoutedEventArgs e)
    {
        var aboutWindow = new Window
        {
            Title = "About PixelEngine",
            Width = 400,
            Height = 300,
            WindowStartupLocation = WindowStartupLocation.CenterOwner,
            Content = new StackPanel
            {
                Margin = new Avalonia.Thickness(20),
                Children =
                {
                    new TextBlock
                    {
                        Text = "PixelEngine v1.0",
                        FontSize = 24,
                        FontWeight = FontWeight.Bold,
                        HorizontalAlignment = Avalonia.Layout.HorizontalAlignment.Center,
                        Margin = new Avalonia.Thickness(0, 0, 0, 20)
                    },
                    new TextBlock
                    {
                        Text = "Advanced Graphics Engine\nBuilt with C# and Avalonia\n\nDeveloped by: AbdulAziz",
                        TextAlignment = TextAlignment.Center,
                        HorizontalAlignment = Avalonia.Layout.HorizontalAlignment.Center
                    }
                }
            }
        };
        aboutWindow.Show(this);
    }

    private void ExitButton_Click(object? sender, RoutedEventArgs e)
    {
        Close();
    }

    protected override void OnClosed(EventArgs e)
    {
        _timer?.Stop();
        base.OnClosed(e);
    }
}
