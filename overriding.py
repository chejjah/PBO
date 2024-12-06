import tkinter as tk
from math import pi
from tkinter import messagebox

class Shape:
    def area(self):
        return "Not implemented"
    def perimeter(self):
        return "Not implemented"

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width
    def perimeter(self):
        return 2 * (self.length + self.width)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return pi * self.radius ** 2
    def perimeter(self):
        return 2 * pi * self.radius

def calculate():
    try:
        shape_type = shape_var.get()
        if shape_type == "Rectangle":
            shape = Rectangle(int(entry_param1.get()), int(entry_param2.get()))
        elif shape_type == "Circle":
            shape = Circle(int(entry_param1.get()))
        else:
            raise ValueError("Invalid shape")
        label_result.config(text=f"Area: {shape.area()}, Perimeter: {shape.perimeter()}")
    except ValueError as e:
        messagebox.showerror("Error", str(e))

root = tk.Tk()
root.title("Overriding in Shapes")

shape_var = tk.StringVar(value="Rectangle")

tk.Radiobutton(root, text="Rectangle", variable=shape_var, value="Rectangle").pack()
tk.Radiobutton(root, text="Circle", variable=shape_var, value="Circle").pack()

tk.Label(root, text="Parameter 1:").pack()
entry_param1 = tk.Entry(root)
entry_param1.pack()

tk.Label(root, text="Parameter 2 (if Rectangle):").pack()
entry_param2 = tk.Entry(root)
entry_param2.pack()

button_calculate = tk.Button(root, text="Calculate", command=calculate)
button_calculate.pack()

label_result = tk.Label(root, text="Area: , Perimeter: ")
label_result.pack()

# Tambahan fungsi reset
def reset_input():
    entry_param1.delete(0, tk.END)
    entry_param2.delete(0, tk.END)
    label_result.config(text="Area: , Perimeter: ")

# Tambahan tombol reset
button_reset = tk.Button(root, text="Reset", command=reset_input)
button_reset.pack(pady=5)

root.mainloop()
