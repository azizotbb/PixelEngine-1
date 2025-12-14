#!/usr/bin/env python3
import tkinter as tk
from tkinter import messagebox, filedialog
from PIL import Image, ImageTk, ImageFilter, ImageEnhance
import os
import random
import threading
import time

class PixelEngineGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("PixelEngine - Desktop Application")
        self.root.geometry("800x600")
        self.root.configure(bg='white')  # White background as originally requested
        self.root.resizable(True, True)
        
        # Center window on screen
        self.root.eval('tk::PlaceWindow . center')
        
        # Store selected image path
        self.selected_image_path = None
        
        # Animation control
        self.is_animating_left = False
        self.animation_thread_left = None
        
        self.create_widgets()
    
    def create_widgets(self):
        # Header frame
        header_frame = tk.Frame(self.root, bg='lightblue', pady=20)
        header_frame.pack(fill='x')
        
        # Title
        title_label = tk.Label(
            header_frame,
            text="PixelEngine",
            font=('Arial', 24, 'bold'),
            bg='lightblue',
            fg='darkblue'
        )
        title_label.pack(pady=10)
        
        # Simple action button
        image_btn = tk.Button(
            header_frame,
            text="اختر صورة",
            font=('Arial', 12),
            bg='lightgray',
            fg='black',
            padx=20,
            pady=8,
            relief='raised',
            bd=2,
            command=self.choose_image
        )
        image_btn.pack(pady=10)

        # Main content frame
        self.content_frame = tk.Frame(self.root, bg='white')
        self.content_frame.pack(fill='both', expand=True, padx=20, pady=10)
        
        # Initial welcome message
        self.show_welcome_message()
    
    def show_welcome_message(self):
        """Show welcome message"""
        welcome_frame = tk.Frame(self.content_frame, bg='white')
        welcome_frame.pack(expand=True, fill='both', pady=50)
        
        # Welcome text
        welcome_label = tk.Label(
            welcome_frame,
            text="مرحبا بك في PixelEngine\nاختر صورة لبدء التجربة",
            font=('Arial', 16),
            bg='white',
            fg='black',
            justify='center'
        )
        welcome_label.pack(pady=50)
    
    def choose_image(self):
        """Choose an image file and display it twice"""
        file_types = [
            ('Image Files', '*.png *.jpg *.jpeg *.gif *.bmp'),
            ('All Files', '*.*')
        ]
        
        file_path = filedialog.askopenfilename(
            title="اختر صورة",
            filetypes=file_types,
            initialdir=os.path.expanduser("~/Desktop")
        )
        
        if file_path:
            self.selected_image_path = file_path
            self.display_image_twice()
    
    def display_image_twice(self):
        """Display the selected image twice"""
        if not self.selected_image_path:
            messagebox.showerror("خطأ", "لم يتم اختيار صورة!")
            return
        
        try:
            # Clear previous content
            for widget in self.content_frame.winfo_children():
                widget.destroy()
            
            # Title for image display
            title_label = tk.Label(
                self.content_frame,
                text="عرض مزدوج للصورة",
                font=('Arial', 18, 'bold'),
                bg='white',
                fg='darkblue'
            )
            title_label.pack(pady=10)

            # Frame for images
            images_frame = tk.Frame(self.content_frame, bg='white')
            images_frame.pack(expand=True, fill='both', pady=10)
            
            # Open and resize image
            original_image = Image.open(self.selected_image_path)
            
            # Calculate size
            max_width = 300
            max_height = 250
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
            
            # Left frame
            left_frame = tk.Frame(images_frame, bg='lightgray', relief='raised', bd=2)
            left_frame.pack(side='left', expand=True, fill='both', padx=10, pady=5)

            # First image header
            image_label1 = tk.Label(
                left_frame,
                text="الصورة الأصلية",
                font=('Arial', 12, 'bold'),
                bg='lightgray',
                fg='black'
            )
            image_label1.pack(pady=10)

            image_display1 = tk.Label(left_frame, image=photo, bg='lightgray')
            image_display1.pack(pady=5)

            # Animation button - classic style
            self.animate_btn_left = tk.Button(
                left_frame,
                text="تشغيل الحركة",
                font=('Arial', 10),
                bg='lightgreen',
                fg='black',
                padx=10,
                pady=5,
                relief='raised',
                bd=2,
                command=lambda: self.toggle_animation('left')
            )
            self.animate_btn_left.pack(pady=10)
            
            # Right frame
            right_frame = tk.Frame(images_frame, bg='lightgray', relief='raised', bd=2)
            right_frame.pack(side='right', expand=True, fill='both', padx=10, pady=5)

            # Second image header
            image_label2 = tk.Label(
                right_frame,
                text="التأثيرات",
                font=('Arial', 12, 'bold'),
                bg='lightgray',
                fg='black'
            )
            image_label2.pack(pady=10)

            image_display2 = tk.Label(right_frame, image=photo, bg='lightgray')
            image_display2.pack(pady=5)
            
            # Effect button - classic style
            effect_btn_right = tk.Button(
                right_frame,
                text="تطبيق تأثير",
                font=('Arial', 10),
                bg='lightyellow',
                fg='black',
                padx=10,
                pady=5,
                relief='raised',
                bd=2,
                command=lambda: self.apply_single_effect('right')
            )
            effect_btn_right.pack(pady=10)
            
            # Action buttons frame
            buttons_frame = tk.Frame(self.content_frame, bg='white')
            buttons_frame.pack(pady=20)
            
            # Choose another image button - classic style
            another_btn = tk.Button(
                buttons_frame,
                text="اختر صورة أخرى",
                font=('Arial', 11),
                bg='lightblue',
                fg='black',
                padx=15,
                pady=8,
                relief='raised',
                bd=2,
                command=self.choose_image
            )
            another_btn.pack(side='left', padx=10)
            
            # Clear button - classic style
            clear_btn = tk.Button(
                buttons_frame,
                text="مسح العرض",
                font=('Arial', 11),
                bg='lightcoral',
                fg='black',
                padx=15,
                pady=8,
                relief='raised',
                bd=2,
                command=self.clear_display
            )
            clear_btn.pack(side='left', padx=10)
            
            # Keep reference to photo
            image_display1.image = photo
            image_display2.image = photo
            
            # Store references for animation
            self.left_image_label = image_display1
            self.right_image_label = image_display2
            self.original_image = original_image
            
        except Exception as e:
            messagebox.showerror("خطأ", f"لا يمكن عرض الصورة:\n{str(e)}")
    
    def clear_display(self):
        """Clear the image display area"""
        # Stop animation
        if hasattr(self, 'is_animating_left'):
            self.stop_animation('left')
        
        for widget in self.content_frame.winfo_children():
            widget.destroy()
        
        # Show welcome message
        self.show_welcome_message()
    
    def apply_single_effect(self, side):
        """Apply a random effect to the specified image once"""
        if not hasattr(self, 'original_image'):
            return
            
        try:
            # Apply random effect
            modified_image = self.apply_random_effect(self.original_image)
            
            # Resize to fit display
            max_width = 300
            max_height = 250
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
            messagebox.showerror("خطأ", f"لا يمكن تطبيق التأثير:\n{str(e)}")
    
    def apply_random_effect(self, image):
        """Apply a random effect to an image"""
        effects = [
            self.color_shift_effect,
            self.brightness_effect,
            self.contrast_effect,
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
    
    def blur_effect(self, image):
        """Apply blur effect"""
        radius = random.uniform(0.5, 3.0)
        return image.filter(ImageFilter.GaussianBlur(radius=radius))
    
    def sharpen_effect(self, image):
        """Apply sharpen effect"""
        return image.filter(ImageFilter.SHARPEN)
    
    def toggle_animation(self, side):
        """Toggle animation for the left side"""
        if side == 'left':
            if self.is_animating_left:
                self.stop_animation('left')
            else:
                self.start_animation('left')
    
    def start_animation(self, side):
        """Start animation for the left side"""
        if side == 'left':
            self.is_animating_left = True
            self.animate_btn_left.configure(text="إيقاف الحركة", bg='lightcoral')
            self.animation_thread_left = threading.Thread(target=self.animate_image, args=('left',))
            self.animation_thread_left.daemon = True
            self.animation_thread_left.start()
    
    def stop_animation(self, side):
        """Stop animation for the left side"""
        if side == 'left':
            self.is_animating_left = False
            if hasattr(self, 'animate_btn_left'):
                self.animate_btn_left.configure(text="تشغيل الحركة", bg='lightgreen')
    
    def animate_image(self, side):
        """Continuously animate the image until stopped"""
        while side == 'left' and self.is_animating_left:
            try:
                self.root.after(0, lambda: self.apply_single_effect(side))
                time.sleep(0.5)
            except:
                break
    
    def run(self):
        self.root.mainloop()

def main():
    print("تشغيل PixelEngine Desktop Application...")
    app = PixelEngineGUI()
    app.run()
    return 0

if __name__ == "__main__":
    main()
