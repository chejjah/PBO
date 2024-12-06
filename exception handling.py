import tkinter as tk 
from tkinter import messagebox

def divide_numbers():
    try:
        num1 = int(entry_num1.get())
        num2 = int(entry_num2.get())
        result = num1 / num2
        label_result.config(text=f"Result: {result}")
    except ZeroDivisionError:
        messagebox.showerror("Error", "Division by zero is not allowed.")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers.")

root = tk.Tk()
root.title("Exception Handling in Division")

tk.Label(root, text="Number 1:").pack()
entry_num1 = tk.Entry(root)
entry_num1.pack()

tk.Label(root, text="Number 2:").pack()
entry_num2 = tk.Entry(root)
entry_num2.pack()

button_divide = tk.Button(root, text="Divide", command=divide_numbers)
button_divide.pack()

label_result = tk.Label(root, text="Result: ")
label_result.pack()

# Tambahan fungsi reset input
def reset_input():
    entry_num1.delete(0, tk.END)
    entry_num2.delete(0, tk.END)
    label_result.config(text="Result: ")

# Tambahan tombol reset
button_reset = tk.Button(root, text="Reset", command=reset_input)
button_reset.pack(pady=5)

root.mainloop()
