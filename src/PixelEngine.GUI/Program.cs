using System;
using System.Drawing;
using System.Windows.Forms;

namespace PixelEngine.GUI
{
    public partial class MainForm : Form
    {
        private Timer animationTimer;
        private int animationStep = 0;
        
        public MainForm()
        {
            InitializeComponent();
            SetupWindow();
            StartAnimation();
        }
        
        private void SetupWindow()
        {
            // Window properties
            this.Text = "PixelEngine - Advanced Graphics Engine";
            this.Size = new Size(800, 600);
            this.BackColor = Color.White;
            this.StartPosition = FormStartPosition.CenterScreen;
            this.FormBorderStyle = FormBorderStyle.FixedSingle;
            this.MaximizeBox = false;
            
            // Add controls
            CreateControls();
        }
        
        private void CreateControls()
        {
            // Title Label
            Label titleLabel = new Label();
            titleLabel.Text = "PixelEngine";
            titleLabel.Font = new Font("Arial", 36, FontStyle.Bold);
            titleLabel.ForeColor = Color.FromArgb(44, 62, 80);
            titleLabel.Location = new Point(250, 100);
            titleLabel.Size = new Size(300, 50);
            titleLabel.TextAlign = ContentAlignment.MiddleCenter;
            this.Controls.Add(titleLabel);
            
            // Subtitle Label
            Label subtitleLabel = new Label();
            subtitleLabel.Text = "Advanced Graphics Engine";
            subtitleLabel.Font = new Font("Arial", 16, FontStyle.Regular);
            subtitleLabel.ForeColor = Color.FromArgb(127, 140, 141);
            subtitleLabel.Location = new Point(250, 160);
            subtitleLabel.Size = new Size(300, 30);
            subtitleLabel.TextAlign = ContentAlignment.MiddleCenter;
            this.Controls.Add(subtitleLabel);
            
            // Info Label
            Label infoLabel = new Label();
            infoLabel.Text = "✨ Features:\n🎨 Pixel Management\n🌈 Color Processing\n🔧 Graphics Utilities\n💻 Cross-Platform Support";
            infoLabel.Font = new Font("Arial", 12, FontStyle.Regular);
            infoLabel.ForeColor = Color.FromArgb(52, 73, 94);
            infoLabel.Location = new Point(50, 250);
            infoLabel.Size = new Size(300, 150);
            this.Controls.Add(infoLabel);
            
            // Pixel Art Panel
            Panel pixelPanel = new Panel();
            pixelPanel.Location = new Point(450, 250);
            pixelPanel.Size = new Size(200, 150);
            pixelPanel.BackColor = Color.LightGray;
            pixelPanel.Paint += PixelPanel_Paint;
            this.Controls.Add(pixelPanel);
            
            // About Button
            Button aboutButton = new Button();
            aboutButton.Text = "About";
            aboutButton.Size = new Size(100, 40);
            aboutButton.Location = new Point(300, 450);
            aboutButton.BackColor = Color.FromArgb(52, 152, 219);
            aboutButton.ForeColor = Color.White;
            aboutButton.FlatStyle = FlatStyle.Flat;
            aboutButton.Click += AboutButton_Click;
            this.Controls.Add(aboutButton);
            
            // Exit Button
            Button exitButton = new Button();
            exitButton.Text = "Exit";
            exitButton.Size = new Size(100, 40);
            exitButton.Location = new Point(420, 450);
            exitButton.BackColor = Color.FromArgb(231, 76, 60);
            exitButton.ForeColor = Color.White;
            exitButton.FlatStyle = FlatStyle.Flat;
            exitButton.Click += ExitButton_Click;
            this.Controls.Add(exitButton);
            
            // Status Label
            Label statusLabel = new Label();
            statusLabel.Text = "Ready - PixelEngine v1.0";
            statusLabel.Font = new Font("Arial", 10, FontStyle.Regular);
            statusLabel.ForeColor = Color.Gray;
            statusLabel.Location = new Point(20, 550);
            statusLabel.Size = new Size(200, 20);
            this.Controls.Add(statusLabel);
        }
        
        private void PixelPanel_Paint(object sender, PaintEventArgs e)
        {
            Graphics g = e.Graphics;
            
            // Draw pixel art pattern
            Color[] colors = { 
                Color.Red, Color.Green, Color.Blue, Color.Yellow, 
                Color.Purple, Color.Orange, Color.Pink, Color.Cyan 
            };
            
            int pixelSize = 20;
            for (int x = 0; x < 8; x++)
            {
                for (int y = 0; y < 6; y++)
                {
                    Color pixelColor = colors[(x + y + animationStep) % colors.Length];
                    Brush brush = new SolidBrush(pixelColor);
                    g.FillRectangle(brush, x * pixelSize + 10, y * pixelSize + 10, pixelSize - 2, pixelSize - 2);
                    brush.Dispose();
                }
            }
        }
        
        private void StartAnimation()
        {
            animationTimer = new Timer();
            animationTimer.Interval = 500; // 500ms
            animationTimer.Tick += AnimationTimer_Tick;
            animationTimer.Start();
        }
        
        private void AnimationTimer_Tick(object sender, EventArgs e)
        {
            animationStep++;
            this.Invalidate(); // Redraw the form
        }
        
        private void AboutButton_Click(object sender, EventArgs e)
        {
            MessageBox.Show("PixelEngine v1.0\n\nAdvanced Graphics Engine\nBuilt with C# and Windows Forms\n\nDeveloped by: AbdulAziz", 
                           "About PixelEngine", MessageBoxButtons.OK, MessageBoxIcon.Information);
        }
        
        private void ExitButton_Click(object sender, EventArgs e)
        {
            this.Close();
        }
        
        protected override void OnFormClosed(FormClosedEventArgs e)
        {
            animationTimer?.Stop();
            animationTimer?.Dispose();
            base.OnFormClosed(e);
        }
    }
    
    // Auto-generated Designer code placeholder
    public partial class MainForm
    {
        private void InitializeComponent()
        {
            this.SuspendLayout();
            this.ResumeLayout(false);
        }
    }
    
    class Program
    {
        [STAThread]
        static void Main()
        {
            Application.EnableVisualStyles();
            Application.SetCompatibleTextRenderingDefault(false);
            Application.Run(new MainForm());
        }
    }
}
