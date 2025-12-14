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
        self.root.title("PixelEngine")
        self.root.geometry("800x600")
        self.root.configure(bg='white')
        
        # Store selected image path
        self.selected_image_path = None
        
        # Animation control
        self.is_animating_left = False
        self.animation_thread_left = None
        
        self.create_widgets()
    
    def create_widgets(self):
        # Simple header
        header_frame = tk.Frame(self.root, bg='lightblue', pady=20)
        header_frame.pack(fill='x')
        
        # Simple title
        title_label = tk.Label(
            header_frame,
            text="PixelEngine",
            font=('Arial', 24, 'bold'),
            bg='lightblue',
            fg='black'
        )
        title_label.pack(pady=10)
        
        # Simple button
        image_btn = tk.Button(
            header_frame,
            text="اختر صورة",
            font=('Arial', 12),
            command=self.choose_image
        )
        image_btn.pack(pady=10)

        # Content frame
        self.content_frame = tk.Frame(self.root, bg='white')
        self.content_frame.pack(fill='both', expand=True, padx=20, pady=20)
        
        # Welcome message
        self.show_welcome_message()
    
    def show_welcome_message(self):
        welcome_label = tk.Label(
            self.content_frame,
            text="مرحبا! اختر صورة لبدء المعالجة",
            font=('Arial', 16),
            bg='white',
            fg='black'
        )
        welcome_label.pack(pady=50)
    
    def choose_image(self):
        file_types = [
            ('Image Files', '*.png *.jpg *.jpeg *.gif *.bmp'),
            ('All Files', '*.*')
        ]
        
        file_path = filedialog.askopenfilename(
            title="اختر صورة",
            filetypes=file_types
        )
        
        if file_path:
            self.selected_image_path = file_path
            self.display_image_twice()
    
    def display_image_twice(self):
        if not self.selected_image_path:
            messagebox.showerror("خطأ", "لم يتم اختيار صورة!")
            return
        
        try:
            # Clear previous content
            for widget in self.content_frame.winfo_children():
                widget.destroy()
            
            # Title
            title_label = tk.Label(
                self.content_frame,
                text="معالجة الصور",
                font=('Arial', 18, 'bold'),
                bg='white',
                fg='black'
            )
            title_label.pack(pady=10)

            # Frame for images
            images_frame = tk.Frame(self.content_frame, bg='white')
            images_frame.pack(fill='both', expand=True, pady=20)
            
            # Open and resize image
            original_image = Image.open(self.selected_image_path)
            
            # Resize image to fit
            max_size = 300
            image_ratio = original_image.width / original_image.height
            
            if image_ratio > 1:
                new_width = max_size
                new_height = int(max_size / image_ratio)
            else:
                new_height = max_size
                new_width = int(max_size * image_ratio)
            
            resized_image = original_image.resize((new_width, new_height), Image.Resampling.LANCZOS)
            photo = ImageTk.PhotoImage(resized_image)
            
            # Left side
            left_frame = tk.Frame(images_frame, bg='lightgray', padx=10, pady=10)
            left_frame.pack(side='left', expand=True, fill='both', padx=10)

            left_label = tk.Label(left_frame, text="الصورة الأصلية", font=('Arial', 12, 'bold'))
            left_label.pack(pady=5)

            self.left_image_display = tk.Label(left_frame, image=photo)
            self.left_image_display.pack(pady=10)
            
            # Simple animation button
            self.animate_btn = tk.Button(
                left_frame,
                text="تشغيل التحريك",
                command=self.toggle_animation
            )
            self.animate_btn.pack(pady=10)
            
            # Right side
            right_frame = tk.Frame(images_frame, bg='lightgray', padx=10, pady=10)
            right_frame.pack(side='right', expand=True, fill='both', padx=10)

            right_label = tk.Label(right_frame, text="التأثيرات", font=('Arial', 12, 'bold'))
            right_label.pack(pady=5)

            self.right_image_display = tk.Label(right_frame, image=photo)
            self.right_image_display.pack(pady=10)
            
            # Simple effect button
            effect_btn = tk.Button(
                right_frame,
                text="تطبيق تأثير",
                command=self.apply_single_effect
            )
            effect_btn.pack(pady=10)
            
            # Bottom buttons
            buttons_frame = tk.Frame(self.content_frame, bg='white')
            buttons_frame.pack(pady=20)
            
            # Simple buttons
            new_btn = tk.Button(
                buttons_frame,
                text="صورة جديدة",
                command=self.choose_image
            )
            new_btn.pack(side='left', padx=10)
            
            clear_btn = tk.Button(
                buttons_frame,
                text="مسح",
                command=self.clear_display
            )
            clear_btn.pack(side='left', padx=10)
            
            # Store references
            self.left_image_display.image = photo
            self.right_image_display.image = photo
            self.original_image = original_image
            
        except Exception as e:
            messagebox.showerror("خطأ", f"لا يمكن عرض الصورة:\n{str(e)}")
    
    def clear_display(self):
        # Stop animation
        if self.is_animating_left:
            self.stop_animation()
        
        for widget in self.content_frame.winfo_children():
            widget.destroy()
        
        # Show welcome message again
        self.show_welcome_message()
    
    def apply_single_effect(self):
        if not hasattr(self, 'original_image'):
            return
            
        try:
            modified_image = self.apply_random_effect(self.original_image)
            
            # Resize to fit display
            max_size = 300
            image_ratio = modified_image.width / modified_image.height
            
            if image_ratio > 1:
                new_width = max_size
                new_height = int(max_size / image_ratio)
            else:
                new_height = max_size
                new_width = int(max_size * image_ratio)
            
            resized_image = modified_image.resize((new_width, new_height), Image.Resampling.LANCZOS)
            photo = ImageTk.PhotoImage(resized_image)
            
            self.right_image_display.configure(image=photo)
            self.right_image_display.image = photo
                
        except Exception as e:
            messagebox.showerror("خطأ", f"لا يمكن تطبيق التأثير:\n{str(e)}")
    
    def apply_random_effect(self, image):
        effects = [
            self.color_shift_effect,
            self.brightness_effect,
            self.blur_effect
        ]
        
        effect = random.choice(effects)
        return effect(image)
    
    def color_shift_effect(self, image):
        pixels = image.load()
        width, height = image.size
        new_image = image.copy()
        new_pixels = new_image.load()
        
        shift = random.randint(-30, 30)
        
        for x in range(width):
            for y in range(height):
                r, g, b = pixels[x, y][:3]
                new_r = max(0, min(255, r + shift))
                new_g = max(0, min(255, g + shift))
                new_b = max(0, min(255, b + shift))
                
                if len(pixels[x, y]) == 4:
                    new_pixels[x, y] = (new_r, new_g, new_b, pixels[x, y][3])
                else:
                    new_pixels[x, y] = (new_r, new_g, new_b)
        
        return new_image
    
    def brightness_effect(self, image):
        enhancer = ImageEnhance.Brightness(image)
        factor = random.uniform(0.7, 1.5)
        return enhancer.enhance(factor)
    
    def blur_effect(self, image):
        radius = random.uniform(0.5, 2.0)
        return image.filter(ImageFilter.GaussianBlur(radius=radius))
    
    def toggle_animation(self):
        if self.is_animating_left:
            self.stop_animation()
        else:
            self.start_animation()
    
    def start_animation(self):
        self.is_animating_left = True
        self.animate_btn.configure(text="إيقاف التحريك")
        self.animation_thread_left = threading.Thread(target=self.animate_image)
        self.animation_thread_left.daemon = True
        self.animation_thread_left.start()
    
    def stop_animation(self):
        self.is_animating_left = False
        if hasattr(self, 'animate_btn'):
            self.animate_btn.configure(text="تشغيل التحريك")
    
    def animate_image(self):
        while self.is_animating_left:
            try:
                if hasattr(self, 'original_image'):
                    modified_image = self.apply_random_effect(self.original_image)
                    
                    max_size = 300
                    image_ratio = modified_image.width / modified_image.height
                    
                    if image_ratio > 1:
                        new_width = max_size
                        new_height = int(max_size / image_ratio)
                    else:
                        new_height = max_size
                        new_width = int(max_size * image_ratio)
                    
                    resized_image = modified_image.resize((new_width, new_height), Image.Resampling.LANCZOS)
                    photo = ImageTk.PhotoImage(resized_image)
                    
                    self.root.after(0, lambda p=photo: self.update_left_image(p))
                
                time.sleep(0.8)
            except:
                break
    
    def update_left_image(self, photo):
        if hasattr(self, 'left_image_display') and self.is_animating_left:
            self.left_image_display.configure(image=photo)
            self.left_image_display.image = photo
    
    def run(self):
        self.root.mainloop()

def main():
    print("تشغيل تطبيق PixelEngine...")
    app = PixelEngineGUI()
    app.run()

if __name__ == "__main__":
    main()
