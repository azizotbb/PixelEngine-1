#!/usr/bin/env python3
import tkinter as tk
from tkinter import messagebox, filedialog
from PIL import Image, ImageTk, ImageFilter, ImageEnhance
import subprocess
import sys
import os
import random
import threading
import time

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
        
        # Animation control (only for left image)
        self.is_animating_left = False
        self.animation_thread_left = None
        
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
            
            # Buttons for left image - Animation only
            left_buttons_frame = tk.Frame(left_frame, bg='white')
            left_buttons_frame.pack(pady=10)
            
            # Continuous animation button for left image  
            self.animate_btn_left = tk.Button(
                left_buttons_frame,
                text="▶️ Start Animation",
                font=('Arial', 12, 'bold'),
                bg='#27AE60',
                fg='white',
                padx=20,
                pady=8,
                relief='flat',
                command=lambda: self.toggle_animation('left')
            )
            self.animate_btn_left.pack()
            
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
            
            # Buttons for right image - Single effect only
            right_buttons_frame = tk.Frame(right_frame, bg='white')
            right_buttons_frame.pack(pady=10)
            
            # Single effect button for right image
            effect_btn_right = tk.Button(
                right_buttons_frame,
                text="🎨 Apply Effect",
                font=('Arial', 12, 'bold'),
                bg='#9B59B6',
                fg='white',
                padx=20,
                pady=8,
                relief='flat',
                command=lambda: self.apply_single_effect('right')
            )
            effect_btn_right.pack()
            
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
            
            # Store references for animation
            self.left_image_label = image_display1
            self.right_image_label = image_display2
            self.original_image = original_image
            
        except Exception as e:
            messagebox.showerror("Error", f"Could not display image:\n{str(e)}")
    
    def clear_display(self):
        """Clear the image display area"""
        # Stop left animation only
        if hasattr(self, 'is_animating_left'):
            self.stop_animation('left')
        
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
    
    def apply_single_effect(self, side):
        """Apply a random effect to the specified image once"""
        if not hasattr(self, 'original_image'):
            return
            
        try:
            # Apply random effect
            modified_image = self.apply_random_effect(self.original_image)
            
            # Resize to fit display
            max_width = 400
            max_height = 300
            image_ratio = modified_image.width / modified_image.height
            
            if image_ratio > max_width / max_height:
                new_width = max_width
                new_height = int(max_width / image_ratio)
            else:
                new_height = max_height
                new_width = int(max_height * image_ratio)
            
            resized_image = modified_image.resize((new_width, new_height), Image.Resampling.LANCZOS)
            photo = ImageTk.PhotoImage(resized_image)
            
            # Update the specified image
            if side == 'left':
                self.left_image_label.configure(image=photo)
                self.left_image_label.image = photo
            else:
                self.right_image_label.configure(image=photo)
                self.right_image_label.image = photo
                
        except Exception as e:
            messagebox.showerror("Error", f"Could not apply effect:\n{str(e)}")
    
    def apply_random_effect(self, image):
        """Apply a random effect to an image"""
        effects = [
            self.color_shift_effect,
            self.pixel_distort_effect,
            self.brightness_effect,
            self.contrast_effect,
            self.saturation_effect,
            self.blur_effect,
            self.sharpen_effect
        ]
        
        effect = random.choice(effects)
        return effect(image)
    
    def color_shift_effect(self, image):
        """Shift RGB colors randomly"""
        pixels = image.load()
        width, height = image.size
        new_image = image.copy()
        new_pixels = new_image.load()
        
        r_shift = random.randint(-50, 50)
        g_shift = random.randint(-50, 50)
        b_shift = random.randint(-50, 50)
        
        for x in range(width):
            for y in range(height):
                r, g, b = pixels[x, y][:3]
                new_r = max(0, min(255, r + r_shift))
                new_g = max(0, min(255, g + g_shift))
                new_b = max(0, min(255, b + b_shift))
                
                if len(pixels[x, y]) == 4:  # RGBA
                    new_pixels[x, y] = (new_r, new_g, new_b, pixels[x, y][3])
                else:  # RGB
                    new_pixels[x, y] = (new_r, new_g, new_b)
        
        return new_image
    
    def pixel_distort_effect(self, image):
        """Randomly distort some pixels"""
        new_image = image.copy()
        pixels = new_image.load()
        width, height = image.size
        
        # Randomly change 20% of pixels
        for _ in range(int(width * height * 0.2)):
            x = random.randint(0, width - 1)
            y = random.randint(0, height - 1)
            
            # Random color
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            
            if len(pixels[x, y]) == 4:  # RGBA
                pixels[x, y] = (r, g, b, pixels[x, y][3])
            else:  # RGB
                pixels[x, y] = (r, g, b)
        
        return new_image
    
    def brightness_effect(self, image):
        """Change brightness randomly"""
        enhancer = ImageEnhance.Brightness(image)
        factor = random.uniform(0.5, 2.0)
        return enhancer.enhance(factor)
    
    def contrast_effect(self, image):
        """Change contrast randomly"""
        enhancer = ImageEnhance.Contrast(image)
        factor = random.uniform(0.5, 2.0)
        return enhancer.enhance(factor)
    
    def saturation_effect(self, image):
        """Change saturation randomly"""
        enhancer = ImageEnhance.Color(image)
        factor = random.uniform(0.0, 2.0)
        return enhancer.enhance(factor)
    
    def blur_effect(self, image):
        """Apply blur effect"""
        radius = random.uniform(0.5, 3.0)
        return image.filter(ImageFilter.GaussianBlur(radius=radius))
    
    def sharpen_effect(self, image):
        """Apply sharpen effect"""
        return image.filter(ImageFilter.SHARPEN)
    
    def toggle_animation(self, side):
        """Toggle continuous animation for the left side only"""
        if side == 'left':
            if self.is_animating_left:
                self.stop_animation('left')
            else:
                self.start_animation('left')
    
    def start_animation(self, side):
        """Start continuous animation for the left side only"""
        if side == 'left':
            self.is_animating_left = True
            self.animate_btn_left.configure(text="⏸️ Stop Animation", bg='#E74C3C')
            self.animation_thread_left = threading.Thread(target=self.animate_image, args=('left',))
            self.animation_thread_left.daemon = True
            self.animation_thread_left.start()
    
    def stop_animation(self, side):
        """Stop continuous animation for the left side only"""
        if side == 'left':
            self.is_animating_left = False
            if hasattr(self, 'animate_btn_left'):
                self.animate_btn_left.configure(text="▶️ Start Animation", bg='#27AE60')
    
    def animate_image(self, side):
        """Continuously animate the left image until stopped"""
        while side == 'left' and self.is_animating_left:
            try:
                # Apply effect in main thread
                self.root.after(0, lambda: self.apply_single_effect(side))
                time.sleep(0.5)  # Wait 500ms between effects
            except:
                break
    
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
