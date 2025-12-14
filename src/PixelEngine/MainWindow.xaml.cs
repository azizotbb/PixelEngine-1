using System.Windows;
using System.Windows.Media;
using System.Windows.Media.Animation;

namespace PixelEngine
{
    /// <summary>
    /// Main window for PixelEngine application
    /// </summary>
    public partial class MainWindow : Window
    {
        public MainWindow()
        {
            InitializeComponent();
            InitializeWindow();
            StartAnimations();
        }

        /// <summary>
        /// Initial window setup
        /// </summary>
        private void InitializeWindow()
        {
            // Set white background
            this.Background = new SolidColorBrush(Colors.White);
            
            // Configure window
            this.WindowState = WindowState.Maximized;
            this.WindowStartupLocation = WindowStartupLocation.CenterScreen;
            
            // Add shadow effect
            this.Effect = new System.Windows.Media.Effects.DropShadowEffect()
            {
                Color = Color.FromRgb(0, 0, 0),
                Opacity = 0.3,
                BlurRadius = 15,
                ShadowDepth = 5
            };
        }

        /// <summary>
        /// Start animations
        /// </summary>
        private void StartAnimations()
        {
            // Title fade-in animation
            var titleAnimation = new DoubleAnimation()
            {
                From = 0,
                To = 1,
                Duration = TimeSpan.FromSeconds(2),
                EasingFunction = new QuadraticEase() { EasingMode = EasingMode.EaseOut }
            };

            // Subtitle fade-in animation
            var subtitleAnimation = new DoubleAnimation()
            {
                From = 0,
                To = 1,
                Duration = TimeSpan.FromSeconds(2),
                BeginTime = TimeSpan.FromSeconds(0.5),
                EasingFunction = new QuadraticEase() { EasingMode = EasingMode.EaseOut }
            };

            // Apply animations
            TitleText.BeginAnimation(OpacityProperty, titleAnimation);
            SubtitleText.BeginAnimation(OpacityProperty, subtitleAnimation);

            // Slide up animation
            var translateAnimation = new DoubleAnimation()
            {
                From = 50,
                To = 0,
                Duration = TimeSpan.FromSeconds(1.5),
                EasingFunction = new QuadraticEase() { EasingMode = EasingMode.EaseOut }
            };

            var transform = new TranslateTransform();
            MainContainer.RenderTransform = transform;
            transform.BeginAnimation(TranslateTransform.YProperty, translateAnimation);
        }

        /// <summary>
        /// Exit button click handler
        /// </summary>
        private void ExitButton_Click(object sender, RoutedEventArgs e)
        {
            Application.Current.Shutdown();
        }

        /// <summary>
        /// About button click handler
        /// </summary>
        private void AboutButton_Click(object sender, RoutedEventArgs e)
        {
            MessageBox.Show("PixelEngine v1.0\n\nAdvanced graphics engine built with C# and WPF\n\nDeveloped by: AbdulAziz", 
                "About", MessageBoxButton.OK, MessageBoxImage.Information);
        }
    }
}
