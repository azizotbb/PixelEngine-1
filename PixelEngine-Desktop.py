#!/usr/bin/env python3
import tkinter as tk
from tkinter import messagebox, filedialog
from PIL import Image, ImageTk
import subprocess
import sys
import os

class PixelEngineGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("PixelEngine - Desktop Graphics Engine")
        self.root.geometry("1000x700")
        self.root.configure(bg='white')
        self.root.resizable(True, True)
        
        # Center window on screen
        self.root.eval('tk::PlaceWindow . center')
        
        # Store selected image path
        self.selected_image_path = None
        
        self.create_widgets()
    
    def create_widgets(self):
        # Header frame
        header_frame = tk.Frame(self.root, bg='white', pady=20)
        header_frame.pack(fill='x')
        
        # Main title (Logo)
        title_label = tk.Label(
            header_frame,
            text="🎨 PixelEngine",
            font=('Arial', 36, 'bold'),
            bg='white',
            fg='#2E86C1'
        )
        title_label.pack(pady=10)
        
        # Subtitle
        subtitle_label = tk.Label(
            header_frame,
            text="Graphics Engine v1.0 - By AbdulAziz",
            font=('Arial', 14),
            bg='white',
            fg='#5D6D7E'
        )
        subtitle_label.pack(pady=5)
        
        # Choose Image button (main feature)
        image_btn = tk.Button(
            header_frame,
            text="🖼️ Choose Image to Display Twice",
            font=('Arial', 14, 'bold'),
            bg='#FF6B35',
            fg='white',
            padx=25,
            pady=10,
            relief='raised',
            bd=2,
            command=self.choose_image,
            cursor='hand2'
        )
        image_btn.pack(pady=15)
        
        # Instructions label
        instructions_label = tk.Label(
            header_frame,
            text="Click the button to select an image from your computer",
            font=('Arial', 11),
            bg='white',
            fg='#7F8C8D'
        )
        instructions_label.pack()
        
        # Main content frame for images
        self.content_frame = tk.Frame(self.root, bg='white')
        self.content_frame.pack(fill='both', expand=True, padx=20, pady=10)
        
        # Initial welcome message
        self.show_welcome_message()
    
    def show_welcome_message(self):
        """Show welcome message in content area"""
        welcome_label = tk.Label(
            self.content_frame,
            text="👆 Click the button above to choose an image",
            font=('Arial', 16),
            bg='white',
            fg='#BDC3C7'
        )
        welcome_label.pack(expand=True)
    
    def choose_image(self):
        """Choose an image file and display it twice"""
        file_types = [
            ('Image Files', '*.png *.jpg *.jpeg *.gif *.bmp *.tiff'),
            ('PNG Files', '*.png'),
            ('JPEG Files', '*.jpg *.jpeg'),
            ('All Files', '*.*')
        ]
        
        file_path = filedialog.askopenfilename(
            title="Choose an image to display twice",
            filetypes=file_types,
            initialdir=os.path.expanduser("~/Desktop")
        )
        
        if file_path:
            self.selected_image_path = file_path
            self.display_image_twice()
    
    def display_image_twice(self):
        """Display the selected image twice in the same window"""
        if not self.selected_image_path:
            messagebox.showerror("Error", "No image selected!")
            return
        
        try:
            # Clear previous content
            for widget in self.content_frame.winfo_children():
                widget.destroy()
            
            # Title for image display
            title_label = tk.Label(
                self.content_frame,
                text="🖼️ Image Displayed Twice",
                font=('Arial', 18, 'bold'),
                bg='white',
                fg='#2E86C1'
            )
            title_label.pack(pady=10)
            
            # Frame for images
            images_frame = tk.Frame(self.content_frame, bg='white')
            images_frame.pack(expand=True, fill='both', pady=10)
            
            # Open and resize image
            original_image = Image.open(self.selected_image_path)
            
            # Calculate size to fit in window
            max_width = 400
            max_height = 300
            image_ratio = original_image.width / original_image.height
            
            if image_ratio > max_width / max_height:
                new_width = max_width
                new_height = int(max_width / image_ratio)
            else:
                new_height = max_height
                new_width = int(max_height * image_ratio)
            
            # Resize image
            resized_image = original_image.resize((new_width, new_height), Image.Resampling.LANCZOS)
            photo = ImageTk.PhotoImage(resized_image)
            
            # Left frame for first image
            left_frame = tk.Frame(images_frame, bg='white', relief='ridge', bd=2)
            left_frame.pack(side='left', expand=True, fill='both', padx=10, pady=5)
            
            # First image
            image_label1 = tk.Label(
                left_frame,
                text="🖼️ Image Copy 1",
                font=('Arial', 14, 'bold'),
                bg='white',
                fg='#27AE60'
            )
            image_label1.pack(pady=10)
            
            image_display1 = tk.Label(left_frame, image=photo, bg='white')
            image_display1.pack(pady=5)
            
            # Image info
            info_label1 = tk.Label(
                left_frame,
                text=f"Size: {original_image.width}x{original_image.height}\nFormat: {original_image.format}",
                font=('Arial', 10),
                bg='white',
                fg='#5D6D7E'
            )
            info_label1.pack(pady=5)
            
            # Right frame for second image  
            right_frame = tk.Frame(images_frame, bg='white', relief='ridge', bd=2)
            right_frame.pack(side='right', expand=True, fill='both', padx=10, pady=5)
            
            # Second image (same as first)
            image_label2 = tk.Label(
                right_frame,
                text="🖼️ Image Copy 2",
                font=('Arial', 14, 'bold'),
                bg='white',
                fg='#E74C3C'
            )
            image_label2.pack(pady=10)
            
            image_display2 = tk.Label(right_frame, image=photo, bg='white')
            image_display2.pack(pady=5)
            
            # Image info
            info_label2 = tk.Label(
                right_frame,
                text=f"Same image displayed twice!\nFilename: {os.path.basename(self.selected_image_path)}",
                font=('Arial', 10),
                bg='white',
                fg='#5D6D7E'
            )
            info_label2.pack(pady=5)
            
            # Action buttons frame
            buttons_frame = tk.Frame(self.content_frame, bg='white')
            buttons_frame.pack(pady=15)
            
            # Choose another image button
            another_btn = tk.Button(
                buttons_frame,
                text="🔄 Choose Another Image",
                font=('Arial', 12, 'bold'),
                bg='#3498DB',
                fg='white',
                padx=20,
                pady=8,
                relief='flat',
                command=self.choose_image
            )
            another_btn.pack(side='left', padx=10)
            
            # Clear button
            clear_btn = tk.Button(
                buttons_frame,
                text="🗑️ Clear Display",
                font=('Arial', 12, 'bold'),
                bg='#95A5A6',
                fg='white',
                padx=20,
                pady=8,
                relief='flat',
                command=self.clear_display
            )
            clear_btn.pack(side='left', padx=10)
            
            # Keep reference to photo to prevent garbage collection
            image_display1.image = photo
            image_display2.image = photo
            
        except Exception as e:
            messagebox.showerror("Error", f"Could not display image:\n{str(e)}")
    
    def clear_display(self):
        """Clear the image display area"""
        for widget in self.content_frame.winfo_children():
            widget.destroy()
        
        # Show welcome message
        welcome_label = tk.Label(
            self.content_frame,
            text="👆 Click the button above to choose an image",
            font=('Arial', 16),
            bg='white',
            fg='#BDC3C7'
        )
        welcome_label.pack(expand=True)
    
    def run(self):
        self.root.mainloop()

def check_python():
    """Check if we have the required Python modules"""
    try:
        import tkinter
        return True
    except ImportError:
        return False

def main():
    if not check_python():
        print("❌ Error: Python tkinter not available")
        print("Please install Python with tkinter support")
        return 1
    
    print("🚀 Starting PixelEngine Desktop Application...")
    app = PixelEngineGUI()
    app.run()
    return 0

if __name__ == "__main__":
    sys.exit(main())
