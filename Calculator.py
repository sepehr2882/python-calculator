import tkinter as tk
from tkinter import font

def calculate():
    try:
        expression = entry.get()
        result = eval(expression)  # Safely evaluate the expression
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except ZeroDivisionError:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error: Division by zero!")
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error: Invalid input!")

def clear():
    entry.delete(0, tk.END)

def button_click(char):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(char))

# Create the main window
root = tk.Tk()
root.title("Python Calculator")
root.resizable(False, False)  # Disable resizing

# Custom font
custom_font = font.Font(size=12)

# Entry widget (display)
entry = tk.Entry(
    root, 
    width=20, 
    font=custom_font, 
    borderwidth=3, 
    justify="right"
)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Button layout: [text, row, column]
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), ("C", 4, 1), ("=", 4, 2), ("+", 4, 3)
]

# Create buttons
for (text, row, col) in buttons:
    if text == "=":
        btn = tk.Button(
            root, 
            text=text, 
            padx=20, 
            pady=10, 
            command=calculate,
            bg="#4CAF50",  # Green color for '='
            fg="white"
        )
    elif text == "C":
        btn = tk.Button(
            root, 
            text=text, 
            padx=20, 
            pady=10, 
            command=clear,
            bg="#f44336",  # Red color for 'C'
            fg="white"
        )
    else:
        btn = tk.Button(
            root, 
            text=text, 
            padx=20, 
            pady=10, 
            command=lambda t=text: button_click(t),
            bg="#e0e0e0"  # Light gray for numbers
        )
    btn.grid(row=row, column=col, sticky="nsew")

# Run the application
root.mainloop()