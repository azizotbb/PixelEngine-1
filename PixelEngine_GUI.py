import tkinter as tk
from tkinter import ttk
import threading
import time

class PixelEngineApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("PixelEngine - Graphics Engine")
        self.root.geometry("800x600")
        self.root.configure(bg='white')
        
        # Center the window
        self.root.eval('tk::PlaceWindow . center')
        
        self.setup_ui()
        
    def setup_ui(self):
        # Main frame
        main_frame = tk.Frame(self.root, bg='white')
        main_frame.pack(expand=True, fill='both', padx=20, pady=20)
        
        # Title
        title_label = tk.Label(
            main_frame,
            text="🎨 PixelEngine",
            font=('Arial', 48, 'bold'),
            bg='white',
            fg='#2E86C1'
        )
        title_label.pack(pady=(40, 20))
        
        # Subtitle
        subtitle_label = tk.Label(
            main_frame,
            text="Advanced Graphics Engine v1.0",
            font=('Arial', 18),
            bg='white',
            fg='#5D6D7E'
        )
        subtitle_label.pack(pady=(0, 30))
        
        # Features frame
        features_frame = tk.Frame(main_frame, bg='white')
        features_frame.pack(pady=20)
        
        features = [
            "🚀 High Performance Rendering",
            "🎯 Pixel Perfect Graphics", 
            "🖥️ Cross Platform Support",
            "⚡ Real-time Processing",
            "🎨 Beautiful UI Components"
        ]
        
        for feature in features:
            feature_label = tk.Label(
                features_frame,
                text=feature,
                font=('Arial', 14),
                bg='white',
                fg='#27AE60',
                anchor='w'
            )
            feature_label.pack(pady=5, padx=50, fill='x')
        
        # Status frame
        status_frame = tk.Frame(main_frame, bg='white')
        status_frame.pack(pady=30)
        
        # Status info
        status_info = [
            ("Platform:", "macOS"),
            ("Version:", "1.0.0"),
            ("Status:", "Ready"),
            ("Author:", "AbdulAziz")
        ]
        
        for label, value in status_info:
            row_frame = tk.Frame(status_frame, bg='white')
            row_frame.pack(pady=2)
            
            tk.Label(
                row_frame,
                text=label,
                font=('Arial', 12, 'bold'),
                bg='white',
                fg='#5D6D7E'
            ).pack(side='left', padx=(0, 10))
            
            tk.Label(
                row_frame,
                text=value,
                font=('Arial', 12),
                bg='white',
                fg='#E74C3C'
            ).pack(side='left')
        
        # Buttons frame
        buttons_frame = tk.Frame(main_frame, bg='white')
        buttons_frame.pack(pady=40)
        
        # Start button
        start_btn = tk.Button(
            buttons_frame,
            text="🚀 Start Engine",
            font=('Arial', 14, 'bold'),
            bg='#27AE60',
            fg='white',
            padx=30,
            pady=10,
            border=0,
            command=self.start_engine
        )
        start_btn.pack(side='left', padx=10)
        
        # About button
        about_btn = tk.Button(
            buttons_frame,
            text="ℹ️ About",
            font=('Arial', 14, 'bold'),
            bg='#3498DB',
            fg='white',
            padx=30,
            pady=10,
            border=0,
            command=self.show_about
        )
        about_btn.pack(side='left', padx=10)
        
        # Exit button
        exit_btn = tk.Button(
            buttons_frame,
            text="❌ Exit",
            font=('Arial', 14, 'bold'),
            bg='#E74C3C',
            fg='white',
            padx=30,
            pady=10,
            border=0,
            command=self.root.quit
        )
        exit_btn.pack(side='left', padx=10)
    
    def start_engine(self):
        # Show loading message
        loading_window = tk.Toplevel(self.root)
        loading_window.title("Starting...")
        loading_window.geometry("400x200")
        loading_window.configure(bg='white')
        loading_window.eval('tk::PlaceWindow . center')
        
        tk.Label(
            loading_window,
            text="🚀 Starting PixelEngine...",
            font=('Arial', 16, 'bold'),
            bg='white',
            fg='#27AE60'
        ).pack(expand=True)
        
        # Auto close after 3 seconds
        def close_loading():
            time.sleep(3)
            loading_window.destroy()
        
        threading.Thread(target=close_loading, daemon=True).start()
    
    def show_about(self):
        about_window = tk.Toplevel(self.root)
        about_window.title("About PixelEngine")
        about_window.geometry("500x400")
        about_window.configure(bg='white')
        about_window.eval('tk::PlaceWindow . center')
        
        about_text = """
🎨 PixelEngine Graphics Engine

Version: 1.0.0
Author: AbdulAziz
License: MIT

A powerful and beautiful graphics engine
designed for cross-platform development.

Features:
• High-performance rendering
• Pixel-perfect graphics
• Modern UI design
• Cross-platform support
• Real-time processing

Built with love ❤️ for the graphics community.
        """
        
        tk.Label(
            about_window,
            text=about_text,
            font=('Arial', 12),
            bg='white',
            fg='#2E86C1',
            justify='left'
        ).pack(expand=True, padx=20, pady=20)
    
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = PixelEngineApp()
    app.run()
