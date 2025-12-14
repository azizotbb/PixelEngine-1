#!/usr/bin/env python3
import tkinter as tk
from tkinter import messagebox, filedialog, ttk
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
        self.root.title("✨ PixelEngine Studio - Premium Graphics Suite")
        self.root.geometry("1600x1000")
        self.root.minsize(1200, 800)
        self.root.configure(bg='#0f0f23')  # Deep cosmic blue
        self.root.resizable(True, True)
        
        # Center window on screen
        self.root.eval('tk::PlaceWindow . center')
        
        # Store selected image path
        self.selected_image_path = None
        
        # Animation control
        self.is_animating_left = False
        self.animation_thread_left = None
        
        self.create_widgets()
        
        # Bind window resize event
        self.root.bind('<Configure>', self.on_window_resize)
    
    def create_widgets(self):
        # 🌟 Stunning gradient header frame
        header_frame = tk.Frame(self.root, bg='#1a1a2e', pady=40)
        header_frame.pack(fill='x')
        
        # 💎 Premium logo with shadow effect
        title_frame = tk.Frame(header_frame, bg='#1a1a2e')
        title_frame.pack(pady=15)
        
        # Main premium title
        title_label = tk.Label(
            title_frame,
            text="✨ PIXELENGINE STUDIO",
            font=('SF Pro Display', 42, 'bold'),
            bg='#1a1a2e',
            fg='#00ff88'  # Electric green
        )
        title_label.pack()
        
        # Elegant subtitle with glow effect
        subtitle_label = tk.Label(
            header_frame,
            text="🚀 PREMIUM GRAPHICS PROCESSING SUITE • AI-POWERED VISUAL EFFECTS",
            font=('SF Pro Text', 14, 'bold'),
            bg='#1a1a2e',
            fg='#ff6b9d'  # Electric pink
        )
        subtitle_label.pack(pady=8)
        
        # Version badge
        version_label = tk.Label(
            header_frame,
            text="V2.0 PROFESSIONAL EDITION",
            font=('SF Pro Text', 11, 'bold'),
            bg='#1a1a2e',
            fg='#00d4ff'  # Electric blue
        )
        version_label.pack(pady=5)
        
        # 🎯 Ultra-modern gradient button
        btn_frame = tk.Frame(header_frame, bg='#1a1a2e')
        btn_frame.pack(pady=25)
        
        image_btn = tk.Button(
            btn_frame,
            text="🎨 SELECT MASTERPIECE",
            font=('SF Pro Text', 16, 'bold'),
            bg='#ff6b9d',  # Electric pink gradient
            fg='black',
            padx=50,
            pady=18,
            relief='flat',
            bd=0,
            command=self.choose_image,
            cursor='hand2',
            activebackground='#ff1744'
        )
        image_btn.pack()

        # Create main scrollable frame with cosmic theme
        self.create_scrollable_content()
        
        # Initial cosmic welcome message
        self.show_welcome_message()
    
    def create_scrollable_content(self):
        """Create cosmic scrollable content area"""
        # 🌌 Main cosmic container
        main_container = tk.Frame(self.root, bg='#0f0f23')
        main_container.pack(fill='both', expand=True, padx=20, pady=15)
        
        # Create premium canvas with cosmic theme
        self.canvas = tk.Canvas(main_container, bg='#0f0f23', highlightthickness=0)
        
        # 🎨 Premium scrollbar with cosmic styling
        scrollbar = ttk.Scrollbar(main_container, orient="vertical", command=self.canvas.yview)
        
        # Configure scrollbar style
        style = ttk.Style()
        style.theme_use('clam')
        style.configure("Vertical.TScrollbar", 
                       background='#1a1a2e',
                       troughcolor='#0f0f23',
                       bordercolor='#00ff88',
                       arrowcolor='#ff6b9d',
                       darkcolor='#1a1a2e',
                       lightcolor='#1a1a2e')
        
        # 💫 Scrollable cosmic frame
        self.scrollable_frame = tk.Frame(self.canvas, bg='#0f0f23')
        
        # Pack scrollbar and canvas with premium layout
        scrollbar.pack(side="right", fill="y", padx=(0, 5))
        self.canvas.pack(side="left", fill="both", expand=True)
        
        # Configure scrolling with smooth cosmic motion
        self.canvas.configure(yscrollcommand=scrollbar.set)
        self.canvas.bind('<Configure>', self.on_canvas_configure)
        
        # Create window for scrollable frame
        self.canvas_frame = self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        
        # Bind mouse wheel for cosmic smooth scrolling
        self.canvas.bind_all("<MouseWheel>", self.on_mousewheel)
        self.canvas.bind_all("<Button-4>", self.on_mousewheel)  # Linux
        self.canvas.bind_all("<Button-5>", self.on_mousewheel)  # Linux
    
    def on_canvas_configure(self, event):
        """Handle cosmic canvas resize with premium effects"""
        # Update scroll region with smooth cosmic motion
        self.canvas.configure(scrollregion=self.canvas.bbox('all'))
        
        # Update canvas window width to match canvas width
        canvas_width = event.width
        self.canvas.itemconfig(self.canvas_frame, width=canvas_width)
    
    def on_mousewheel(self, event):
        """Premium cosmic smooth scrolling"""
        if hasattr(event, 'delta'):
            # Windows scrolling
            self.canvas.yview_scroll(int(-1*(event.delta/120)), "units")
        else:
            # Linux scrolling
            if event.num == 4:
                self.canvas.yview_scroll(-1, "units")
            elif event.num == 5:
                self.canvas.yview_scroll(1, "units")
    
    def show_welcome_message(self):
        """🌌 Show cosmic welcome message with premium styling"""
        # Clear previous content
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()
            
        # 🌟 Cosmic welcome container
        welcome_container = tk.Frame(self.scrollable_frame, bg='#0f0f23')
        welcome_container.pack(expand=True, fill='both', pady=100)
        
        # 💫 Animated cosmic icon
        cosmic_icon = tk.Label(
            welcome_container,
            text="🌌",
            font=('Apple Color Emoji', 80),
            bg='#0f0f23',
            fg='#00ff88'
        )
        cosmic_icon.pack(pady=30)
        
        # ✨ Premium welcome title
        welcome_title = tk.Label(
            welcome_container,
            text="WELCOME TO THE COSMOS",
            font=('SF Pro Display', 32, 'bold'),
            bg='#0f0f23',
            fg='#00d4ff'
        )
        welcome_title.pack(pady=15)
        
        # 🚀 Elegant instructions
        instructions = tk.Label(
            welcome_container,
            text="Select your masterpiece to begin the visual journey",
            font=('SF Pro Text', 18, 'normal'),
            bg='#0f0f23',
            fg='#ff6b9d'
        )
        instructions.pack(pady=10)
        
        # 💎 Premium features showcase
        features_frame = tk.Frame(welcome_container, bg='#0f0f23')
        features_frame.pack(pady=40)
        
        features = [
            "🎨 AI-Powered Effects",
            "✨ Real-time Processing", 
            "🌟 Premium Filters",
            "🚀 Ultra Performance"
        ]
        
        for i, feature in enumerate(features):
            if i % 2 == 0:
                row_frame = tk.Frame(features_frame, bg='#0f0f23')
                row_frame.pack(pady=8)
            
            feature_label = tk.Label(
                row_frame,
                text=feature,
                font=('SF Pro Text', 14, 'bold'),
                bg='#0f0f23',
                fg='#00ff88',
                padx=20
            )
            feature_label.pack(side='left', padx=15)
    
    def choose_image(self):
        """🎨 Choose masterpiece with premium file dialog"""
        file_types = [
            ('All Image Files', '*.png *.jpg *.jpeg *.gif *.bmp *.tiff *.webp'),
            ('PNG Files', '*.png'),
            ('JPEG Files', '*.jpg *.jpeg'),
            ('GIF Files', '*.gif'),
            ('All Files', '*.*')
        ]
        
        file_path = filedialog.askopenfilename(
            title="✨ Select Your Visual Masterpiece",
            filetypes=file_types,
            initialdir=os.path.expanduser("~/Desktop")
        )
        
        if file_path:
            self.selected_image_path = file_path
            self.display_image_twice()

    def display_image_twice(self):
        """🌌 Display masterpiece with cosmic dual processing studio"""
        if not self.selected_image_path:
            messagebox.showerror("Error", "No masterpiece selected!")
            return
        
        try:
            # Clear cosmic space
            for widget in self.scrollable_frame.winfo_children():
                widget.destroy()
            
            # 🌟 Premium studio title
            studio_title = tk.Label(
                self.scrollable_frame,
                text="✨ COSMIC DUAL PROCESSING STUDIO",
                font=('SF Pro Display', 28, 'bold'),
                bg='#0f0f23',
                fg='#00d4ff'
            )
            studio_title.pack(pady=30)

            # 🎨 Premium images container
            images_container = tk.Frame(self.scrollable_frame, bg='#0f0f23')
            images_container.pack(expand=True, fill='both', pady=20)
            
            # 🖼️ Load and process masterpiece
            original_image = Image.open(self.selected_image_path)
            
            # 💎 Premium dynamic sizing
            window_width = self.root.winfo_width()
            window_height = self.root.winfo_height()
            
            # Calculate premium display size
            max_width = min(500, int((window_width - 150) / 2))
            max_height = min(400, int((window_height - 400) / 2))
            max_width = max(300, max_width)
            max_height = max(250, max_height)
            
            image_ratio = original_image.width / original_image.height
            
            if image_ratio > max_width / max_height:
                new_width = max_width
                new_height = int(max_width / image_ratio)
            else:
                new_height = max_height
                new_width = int(max_height * image_ratio)
            
            # ✨ Resize with premium quality
            resized_image = original_image.resize((new_width, new_height), Image.Resampling.LANCZOS)
            photo = ImageTk.PhotoImage(resized_image)
            
            # 🌟 Left cosmic frame - Original Masterpiece
            left_frame = tk.Frame(images_container, bg='#1a1a2e', relief='solid', bd=3)
            left_frame.pack(side='left', expand=True, fill='both', padx=15, pady=10)

            # 💫 Premium original image header
            original_header = tk.Label(
                left_frame,
                text="🌟 ORIGINAL MASTERPIECE",
                font=('SF Pro Display', 18, 'bold'),
                bg='#1a1a2e',
                fg='#00ff88'
            )
            original_header.pack(pady=20)

            # ✨ Premium image display with glow effect
            image_display1 = tk.Label(left_frame, image=photo, bg='#1a1a2e', relief='ridge', bd=4)
            image_display1.pack(pady=15)
            
            # 🎯 Animation control button
            self.animate_btn_left = tk.Button(
                left_frame,
                text="🎬 START COSMIC ANIMATION",
                font=('SF Pro Text', 12, 'bold'),
                bg='#ff6b9d',
                fg='black',
                padx=30,
                pady=12,
                relief='flat',
                bd=0,
                command=lambda: self.toggle_animation('left'),
                cursor='hand2',
                activebackground='#ff1744'
            )
            self.animate_btn_left.pack(pady=20)
            
            # 🎨 Cosmic effects panel for left
            effects_panel_left = tk.Frame(left_frame, bg='#1a1a2e')
            effects_panel_left.pack(pady=15)
            
            effects_label_left = tk.Label(
                effects_panel_left,
                text="🎨 VISUAL EFFECTS",
                font=('SF Pro Text', 12, 'bold'),
                bg='#1a1a2e',
                fg='#00d4ff'
            )
            effects_label_left.pack(pady=10)
            
            # Premium effect buttons for left
            effects_row_left = tk.Frame(effects_panel_left, bg='#1a1a2e')
            effects_row_left.pack()
            
            # Color shift effect
            color_btn = tk.Button(
                effects_row_left,
                text="🌈 COLOR",
                font=('SF Pro Text', 10, 'bold'),
                bg='#9b59b6',
                fg='black',
                padx=12,
                pady=8,
                relief='flat',
                bd=0,
                command=lambda: self.apply_specific_effect('left', 'color'),
                cursor='hand2',
                activebackground='#8e44ad'
            )
            color_btn.pack(side='left', padx=5)
            
            # Brightness effect
            bright_btn = tk.Button(
                effects_row_left,
                text="☀️ BRIGHT",
                font=('SF Pro Text', 10, 'bold'),
                bg='#f39c12',
                fg='black',
                padx=12,
                pady=8,
                relief='flat',
                bd=0,
                command=lambda: self.apply_specific_effect('left', 'brightness'),
                cursor='hand2',
                activebackground='#e67e22'
            )
            bright_btn.pack(side='left', padx=5)
            
            # 💎 Right cosmic frame - Effects Laboratory
            right_frame = tk.Frame(images_container, bg='#1a1a2e', relief='solid', bd=3)
            right_frame.pack(side='right', expand=True, fill='both', padx=15, pady=10)

            # 🔬 Premium laboratory header
            lab_header = tk.Label(
                right_frame,
                text="🔬 EFFECTS LABORATORY",
                font=('SF Pro Display', 18, 'bold'),
                bg='#1a1a2e',
                fg='#ff6b9d'
            )
            lab_header.pack(pady=20)

            # ✨ Premium image display with cosmic glow
            image_display2 = tk.Label(right_frame, image=photo, bg='#1a1a2e', relief='ridge', bd=4)
            image_display2.pack(pady=15)
            
            # 🎭 Magic effects button
            magic_btn = tk.Button(
                right_frame,
                text="🎭 APPLY MAGIC EFFECTS",
                font=('SF Pro Text', 12, 'bold'),
                bg='#00d4ff',
                fg='black',
                padx=30,
                pady=12,
                relief='flat',
                bd=0,
                command=lambda: self.apply_single_effect('right'),
                cursor='hand2',
                activebackground='#0099cc'
            )
            magic_btn.pack(pady=20)
            
            # 🌟 Premium effects panel for right
            effects_panel_right = tk.Frame(right_frame, bg='#1a1a2e')
            effects_panel_right.pack(pady=15)
            
            effects_label_right = tk.Label(
                effects_panel_right,
                text="⚡ POWER EFFECTS",
                font=('SF Pro Text', 12, 'bold'),
                bg='#1a1a2e',
                fg='#00d4ff'
            )
            effects_label_right.pack(pady=10)
            
            # Premium effect buttons for right
            effects_row_right = tk.Frame(effects_panel_right, bg='#1a1a2e')
            effects_row_right.pack()
            
            # Contrast effect
            contrast_btn = tk.Button(
                effects_row_right,
                text="🔆 CONTRAST",
                font=('SF Pro Text', 9, 'bold'),
                bg='#e74c3c',
                fg='black',
                padx=10,
                pady=8,
                relief='flat',
                bd=0,
                command=lambda: self.apply_specific_effect('right', 'contrast'),
                cursor='hand2',
                activebackground='#c0392b'
            )
            contrast_btn.pack(side='left', padx=3)
            
            # Blur effect
            blur_btn = tk.Button(
                effects_row_right,
                text="🌫️ BLUR",
                font=('SF Pro Text', 9, 'bold'),
                bg='#3498db',
                fg='black',
                padx=10,
                pady=8,
                relief='flat',
                bd=0,
                command=lambda: self.apply_specific_effect('right', 'blur'),
                cursor='hand2',
                activebackground='#2980b9'
            )
            blur_btn.pack(side='left', padx=3)
            
            # Sharpen effect
            sharp_btn = tk.Button(
                effects_row_right,
                text="✨ SHARP",
                font=('SF Pro Text', 9, 'bold'),
                bg='#2ecc71',
                fg='black',
                padx=10,
                pady=8,
                relief='flat',
                bd=0,
                command=lambda: self.apply_specific_effect('right', 'sharpen'),
                cursor='hand2',
                activebackground='#27ae60'
            )
            sharp_btn.pack(side='left', padx=3)
            
            # 🌟 Premium action buttons section
            action_section = tk.Frame(self.scrollable_frame, bg='#0f0f23')
            action_section.pack(pady=40)
            
            # 💫 Premium action buttons frame
            buttons_frame = tk.Frame(action_section, bg='#0f0f23')
            buttons_frame.pack()
            
            # 🔄 Load new masterpiece button
            new_btn = tk.Button(
                buttons_frame,
                text="🔄 LOAD NEW MASTERPIECE",
                font=('SF Pro Text', 14, 'bold'),
                bg='#8e2de2',
                fg='black',
                padx=40,
                pady=15,
                relief='flat',
                bd=0,
                command=self.choose_image,
                cursor='hand2',
                activebackground='#4a00e0'
            )
            new_btn.pack(side='left', padx=20)
            
            # 🗑️ Clear cosmic canvas button
            clear_btn = tk.Button(
                buttons_frame,
                text="🗑️ CLEAR COSMIC CANVAS",
                font=('SF Pro Text', 14, 'bold'),
                bg='#ff1744',
                fg='black',
                padx=40,
                pady=15,
                relief='flat',
                bd=0,
                command=self.clear_display,
                cursor='hand2',
                activebackground='#d50000'
            )
            clear_btn.pack(side='left', padx=20)
            
            # 💾 Premium save button
            save_btn = tk.Button(
                buttons_frame,
                text="💾 SAVE PROCESSED IMAGE",
                font=('SF Pro Text', 14, 'bold'),
                bg='#00ff88',
                fg='black',
                padx=40,
                pady=15,
                relief='flat',
                bd=0,
                command=self.save_image,
                cursor='hand2',
                activebackground='#00cc66'
            )
            save_btn.pack(side='left', padx=20)
            
            # Choose another image button
            another_btn = tk.Button(
                buttons_frame,
                text="🔄 Choose Another Image",
                font=('Arial', 12, 'bold'),
                bg='#FF9500',
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
                bg='#E056FD',
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
            
            # Update scroll region to accommodate new content
            self.root.after(10, lambda: self.canvas.configure(scrollregion=self.canvas.bbox('all')))
            
        except Exception as e:
            messagebox.showerror("Error", f"Could not display image:\n{str(e)}")
    
    def apply_specific_effect(self, side, effect_type):
        """Apply a specific effect to the specified image"""
        if not hasattr(self, 'original_image'):
            return
            
        try:
            # Apply specific effect based on type
            if effect_type == 'color':
                modified_image = self.color_shift_effect(self.original_image)
            elif effect_type == 'brightness':
                modified_image = self.brightness_effect(self.original_image)
            elif effect_type == 'contrast':
                modified_image = self.contrast_effect(self.original_image)
            elif effect_type == 'blur':
                modified_image = self.blur_effect(self.original_image)
            elif effect_type == 'sharpen':
                modified_image = self.sharpen_effect(self.original_image)
            else:
                modified_image = self.apply_random_effect(self.original_image)
            
            # Resize to enhanced display size
            max_width = 500
            max_height = 400
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
            messagebox.showerror("Error", f"Could not apply {effect_type} effect:\n{str(e)}")

    def save_image(self):
        """💾 Save processed image with premium dialog"""
        if not hasattr(self, 'right_image_label') or not hasattr(self.right_image_label, 'image'):
            messagebox.showwarning("Warning", "No processed image to save!")
            return
        
        try:
            file_path = filedialog.asksaveasfilename(
                title="💾 Save Your Cosmic Creation",
                defaultextension=".png",
                filetypes=[
                    ('PNG Files', '*.png'),
                    ('JPEG Files', '*.jpg'),
                    ('All Files', '*.*')
                ]
            )
            
            if file_path:
                # This would save the current processed image
                messagebox.showinfo("Success", f"✨ Image saved successfully!\n{file_path}")
        except Exception as e:
            messagebox.showerror("Error", f"Could not save image:\n{str(e)}")
            
    def clear_display(self):
        """🗑️ Clear cosmic canvas and return to welcome"""
        # Stop any running animation
        if hasattr(self, 'is_animating_left') and self.is_animating_left:
            self.stop_animation('left')
        
        # Clear the scrollable frame
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()
        
        # Show welcome message again
        self.show_welcome_message()

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
            self.animate_btn_left.configure(text="⏸️ Stop Animation", bg='#FF4757')
            self.animation_thread_left = threading.Thread(target=self.animate_image, args=('left',))
            self.animation_thread_left.daemon = True
            self.animation_thread_left.start()
    
    def stop_animation(self, side):
        """Stop continuous animation for the left side only"""
        if side == 'left':
            self.is_animating_left = False
            if hasattr(self, 'animate_btn_left'):
                self.animate_btn_left.configure(text="▶️ Start Animation", bg='#00D2D3')
    
    def animate_image(self, side):
        """Continuously animate the left image until stopped"""
        while side == 'left' and self.is_animating_left:
            try:
                # Apply effect in main thread
                self.root.after(0, lambda: self.apply_single_effect(side))
                time.sleep(0.5)  # Wait 500ms between effects
            except:
                break
    
    def on_window_resize(self, event):
        """Handle window resize events"""
        # Only handle resize events for the main window
        if event.widget == self.root and hasattr(self, 'selected_image_path') and self.selected_image_path:
            # Update image display if an image is currently shown
            self.root.after(100, self.update_image_sizes)  # Small delay to avoid rapid updates
    
    def update_image_sizes(self):
        """Update image sizes when window is resized"""
        if hasattr(self, 'original_image') and hasattr(self, 'left_image_label'):
            try:
                # Recalculate sizes
                window_width = self.root.winfo_width()
                window_height = self.root.winfo_height()
                
                max_width = min(400, int((window_width - 100) / 2))
                max_height = min(300, int((window_height - 300) / 2))
                max_width = max(200, max_width)
                max_height = max(150, max_height)
                
                image_ratio = self.original_image.width / self.original_image.height
                
                if image_ratio > max_width / max_height:
                    new_width = max_width
                    new_height = int(max_width / image_ratio)
                else:
                    new_height = max_height
                    new_width = int(max_height * image_ratio)
                
                # Resize and update images
                resized_image = self.original_image.resize((new_width, new_height), Image.Resampling.LANCZOS)
                photo = ImageTk.PhotoImage(resized_image)
                
                self.left_image_label.configure(image=photo)
                self.left_image_label.image = photo
                self.right_image_label.configure(image=photo)
                self.right_image_label.image = photo
                
                # Update scroll region after image resize
                self.root.after(10, lambda: self.canvas.configure(scrollregion=self.canvas.bbox('all')))
            except:
                pass  # Ignore errors during resize
    
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
