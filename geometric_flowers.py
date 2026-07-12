import turtle
import math
import tkinter as tk
from tkinter import colorchooser
from tkinter import messagebox

class GeometricFlowerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Geometric Flower Generator")
        self.root.geometry("1000x800")
        
        self.colors = ["gold"]
        
        # Theme colors setup
        self.light_bg = "#f0f0f0"
        self.light_fg = "black"
        self.dark_bg = "#2b2b2b"
        self.dark_fg = "white"
        self.dark_canvas = "#1e1e1e"
        
        # Default to dark mode!
        self.is_dark_mode = tk.BooleanVar(value=True) 
        
        self.setup_ui()
        self.apply_theme()
        
    def setup_ui(self):
        # Left Panel for Controls
        self.control_frame = tk.Frame(self.root, padx=20, pady=20)
        self.control_frame.pack(side=tk.LEFT, fill=tk.Y)
        
        # Right Panel for Turtle Graphics
        self.canvas_frame = tk.Frame(self.root)
        self.canvas_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        
        # Setup Turtle Canvas
        self.canvas = tk.Canvas(self.canvas_frame, width=800, height=800)
        self.canvas.pack(fill=tk.BOTH, expand=True)
        
        self.t_screen = turtle.TurtleScreen(self.canvas)
        self.t_screen.tracer(0)
        
        self.t = turtle.RawTurtle(self.t_screen)
        self.t.hideturtle()
        self.t.speed(0)
        
        # Store widgets for dynamic theming
        self.themed_widgets = []
        self.themed_labels = []
        
        row = 0
        
        lbl_title = tk.Label(self.control_frame, text="Geometric Parameters", font=("Helvetica", 14, "bold"))
        lbl_title.grid(row=row, column=0, columnspan=2, pady=(0, 15))
        self.themed_labels.append(lbl_title)
        row += 1
        
        # Dark Mode Toggle
        self.chk_dark = tk.Checkbutton(self.control_frame, text="Dark Mode Enabled", variable=self.is_dark_mode, command=self.apply_theme)
        self.chk_dark.grid(row=row, column=0, columnspan=2, sticky="w", pady=(0, 10))
        self.themed_widgets.append(self.chk_dark)
        row += 1
        
        # Sides
        lbl1 = tk.Label(self.control_frame, text="Number of Sides:")
        lbl1.grid(row=row, column=0, sticky="e", pady=5)
        self.themed_labels.append(lbl1)
        self.var_sides = tk.IntVar(value=7)
        ent1 = tk.Entry(self.control_frame, textvariable=self.var_sides, width=10)
        ent1.grid(row=row, column=1, sticky="w", pady=5)
        self.themed_widgets.append(ent1)
        row += 1
        
        # Total Shapes
        lbl2 = tk.Label(self.control_frame, text="Number of Shapes:")
        lbl2.grid(row=row, column=0, sticky="e", pady=5)
        self.themed_labels.append(lbl2)
        self.var_shapes = tk.IntVar(value=45)
        ent2 = tk.Entry(self.control_frame, textvariable=self.var_shapes, width=10)
        ent2.grid(row=row, column=1, sticky="w", pady=5)
        self.themed_widgets.append(ent2)
        row += 1
        
        # Angle Step
        lbl3 = tk.Label(self.control_frame, text="Rotation Angle (°):")
        lbl3.grid(row=row, column=0, sticky="e", pady=5)
        self.themed_labels.append(lbl3)
        self.var_angle = tk.DoubleVar(value=8.0)
        ent3 = tk.Entry(self.control_frame, textvariable=self.var_angle, width=10)
        ent3.grid(row=row, column=1, sticky="w", pady=5)
        self.themed_widgets.append(ent3)
        row += 1
        
        # Auto Scale
        self.var_auto_scale = tk.BooleanVar(value=True)
        self.chk_auto = tk.Checkbutton(self.control_frame, text="Auto Scale (Pursuit Curve)", variable=self.var_auto_scale, command=self.toggle_scale_entry)
        self.chk_auto.grid(row=row, column=0, columnspan=2, sticky="w", pady=(15, 2))
        self.themed_widgets.append(self.chk_auto)
        row += 1
        
        # Custom Multiplier
        lbl4 = tk.Label(self.control_frame, text="Size Multiplier:")
        lbl4.grid(row=row, column=0, sticky="e", pady=2)
        self.themed_labels.append(lbl4)
        self.var_multiplier = tk.DoubleVar(value=0.92)
        self.entry_multiplier = tk.Entry(self.control_frame, textvariable=self.var_multiplier, width=10)
        self.entry_multiplier.grid(row=row, column=1, sticky="w", pady=2)
        self.entry_multiplier.config(state=tk.DISABLED)
        self.themed_widgets.append(self.entry_multiplier)
        row += 1
        
        lbl_colors = tk.Label(self.control_frame, text="Colors", font=("Helvetica", 14, "bold"))
        lbl_colors.grid(row=row, column=0, columnspan=2, pady=(25, 10))
        self.themed_labels.append(lbl_colors)
        row += 1
        
        # Color Listbox
        self.listbox_colors = tk.Listbox(self.control_frame, height=6, width=25)
        self.listbox_colors.grid(row=row, column=0, columnspan=2, pady=5)
        self.themed_widgets.append(self.listbox_colors)
        self.update_color_listbox()
        row += 1
        
        # Color Buttons
        self.btn_frame = tk.Frame(self.control_frame)
        self.btn_frame.grid(row=row, column=0, columnspan=2, pady=5)
        
        self.btn_add = tk.Button(self.btn_frame, text="Open Color Wheel", command=self.add_color)
        self.btn_add.pack(side=tk.LEFT, padx=5)
        
        self.btn_clear = tk.Button(self.btn_frame, text="Clear Colors", command=self.clear_colors)
        self.btn_clear.pack(side=tk.LEFT, padx=5)
        row += 1
        
        # Generate Button
        self.btn_gen = tk.Button(self.control_frame, text="Generate Flower", command=self.generate, font=("Helvetica", 14, "bold"), bg="#4CAF50", fg="black")
        self.btn_gen.grid(row=row, column=0, columnspan=2, pady=40, ipadx=10, ipady=5)

    def apply_theme(self):
        dark = self.is_dark_mode.get()
        bg_col = self.dark_bg if dark else self.light_bg
        fg_col = self.dark_fg if dark else self.light_fg
        
        self.root.config(bg=bg_col)
        self.control_frame.config(bg=bg_col)
        self.btn_frame.config(bg=bg_col)
        
        # Update canvas
        canvas_bg = self.dark_canvas if dark else "white"
        self.t_screen.bgcolor(canvas_bg)
        
        for lbl in self.themed_labels:
            lbl.config(bg=bg_col, fg=fg_col)
            
        for w in self.themed_widgets:
            if isinstance(w, tk.Listbox):
                if dark:
                    w.config(bg="#3b3b3b", fg="white")
                else:
                    w.config(bg="white", fg="black")
            elif isinstance(w, tk.Entry):
                if dark:
                    w.config(bg="#3b3b3b", fg="white", insertbackground="white")
                else:
                    w.config(bg="white", fg="black", insertbackground="black")
            elif isinstance(w, tk.Checkbutton):
                w.config(bg=bg_col, fg=fg_col, selectcolor="#4a4a4a" if dark else "white")
                
        # Handle mac specific button background workaround
        self.btn_gen.config(highlightbackground=bg_col) 
        self.btn_add.config(highlightbackground=bg_col)
        self.btn_clear.config(highlightbackground=bg_col)

    def toggle_scale_entry(self):
        if self.var_auto_scale.get():
            self.entry_multiplier.config(state=tk.DISABLED)
        else:
            self.entry_multiplier.config(state=tk.NORMAL)
            
    def add_color(self):
        color_data = colorchooser.askcolor(title="Pick a Color from the Wheel")
        if color_data[1]:
            if self.colors == ["gold"] and len(self.colors) == 1:
                self.colors = []
            self.colors.append(color_data[1])
            self.update_color_listbox()
            
    def clear_colors(self):
        self.colors = []
        self.update_color_listbox()
        
    def update_color_listbox(self):
        self.listbox_colors.delete(0, tk.END)
        for c in self.colors:
            self.listbox_colors.insert(tk.END, c)
            
    def draw_centered_polygon(self, sides, radius, rotation, color):
        self.t.fillcolor(color)
        
        # Use a contrasting pen color for the borders based on the theme
        pen_col = "white" if self.is_dark_mode.get() else "black"
        self.t.pencolor(pen_col)
        
        self.t.begin_fill()
        self.t.penup()
        
        for i in range(sides):
            angle_deg = rotation + i * (360 / sides)
            angle_rad = math.radians(angle_deg)
            x = radius * math.cos(angle_rad)
            y = radius * math.sin(angle_rad)
            
            self.t.goto(x, y)
            if i == 0:
                self.t.pendown()
                
        angle_rad = math.radians(rotation)
        x = radius * math.cos(angle_rad)
        y = radius * math.sin(angle_rad)
        self.t.goto(x, y)
        self.t.end_fill()

    def generate(self):
        try:
            sides = self.var_sides.get()
            total_shapes = self.var_shapes.get()
            angle_step = self.var_angle.get()
            is_auto = self.var_auto_scale.get()
            custom_mult = self.var_multiplier.get()
            
            if sides < 3:
                messagebox.showerror("Error", "Number of sides must be at least 3.")
                return
                
            active_colors = self.colors if self.colors else ["gold"]
            
            self.t.clear()
            
            current_radius = 350
            current_rotation = 0
            
            if is_auto:
                angle_step_rad = math.radians(angle_step)
                pi_over_n = math.pi / sides
                
                if angle_step >= (360 / sides):
                    messagebox.showwarning("Warning", f"Angle step is too large for pursuit curve. Must be less than {360/sides:.1f} degrees.")
                    size_multiplier = 0.9 
                else:
                    size_multiplier = math.cos(pi_over_n) / math.cos(angle_step_rad - pi_over_n)
            else:
                size_multiplier = custom_mult
                
            for i in range(total_shapes):
                current_color = active_colors[i % len(active_colors)]
                self.draw_centered_polygon(sides, current_radius, current_rotation, current_color)
                
                current_radius *= size_multiplier
                current_rotation += angle_step
                
                if current_radius < 1:
                    break
                    
            self.t_screen.update()
            
        except Exception as e:
            messagebox.showerror("Error", f"Invalid input: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = GeometricFlowerApp(root)
    root.mainloop()
