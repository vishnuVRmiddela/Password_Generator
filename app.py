import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    try:
        length = int(length_entry.get())
        if length <= 0:
            raise ValueError("Password length must be a positive integer.")
        
        characters = ""
        if use_uppercase.get():
            characters += string.ascii_uppercase
        if use_lowercase.get():
            characters += string.ascii_lowercase
        if use_digits.get():
            characters += string.digits
        if use_symbols.get():
            characters += string.punctuation
        
        if not characters:
            messagebox.showerror("Error", "Please select at least one character type.")
            return
        
        password = ''.join(random.choice(characters) for _ in range(length))
        password_entry.delete(0, tk.END)
        password_entry.insert(0, password)
    except ValueError as e:
        messagebox.showerror("Error", str(e))

# Create the main window
root = tk.Tk()
root.title("Password Generator")

# Create and place widgets
length_label = tk.Label(root, text="Password Length:")
length_label.pack(pady=5)

length_entry = tk.Entry(root, width=30)
length_entry.pack(pady=5)

use_uppercase = tk.BooleanVar()
use_lowercase = tk.BooleanVar()
use_digits = tk.BooleanVar()
use_symbols = tk.BooleanVar()

uppercase_checkbox = tk.Checkbutton(root, text="Include Uppercase Letters", variable=use_uppercase)
uppercase_checkbox.pack(pady=2)

lowercase_checkbox = tk.Checkbutton(root, text="Include Lowercase Letters", variable=use_lowercase)
lowercase_checkbox.pack(pady=2)

digits_checkbox = tk.Checkbutton(root, text="Include Digits", variable=use_digits)
digits_checkbox.pack(pady=2)

symbols_checkbox = tk.Checkbutton(root, text="Include Symbols", variable=use_symbols)
symbols_checkbox.pack(pady=2)

generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack(pady=10)

password_label = tk.Label(root, text="Generated Password:")
password_label.pack(pady=5)

password_entry = tk.Entry(root, width=30)
password_entry.pack(pady=5)

# Start the Tkinter event loop
root.mainloop()