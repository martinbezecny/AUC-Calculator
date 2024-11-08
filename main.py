import tkinter as tk
from tkinter import messagebox
import numpy as np


def calculate_auc():
    x_vals = []
    y_vals = []
    for i in range(26):
        x = x_entries[i].get().strip()
        y = y_entries[i].get().strip()

        if x and y:
            try:
                x = float(x)
                y = float(y)
                x_vals.append(x)
                y_vals.append(y)
            except ValueError:
                messagebox.showerror("Invalid Input", f"Please enter valid numbers in row {i + 1}.")
                return

    # Check for duplicate x-values
    if len(x_vals) != len(set(x_vals)):
        messagebox.showerror("Duplicate x-Values", "Duplicate x-values were detected. Enter unique x-values.")
        return

    if len(x_vals) < 2:
        messagebox.showerror("Insufficient Data", "At least two valid points are required to calculate AUC.")
        return

    sorted_coords = sorted(zip(x_vals, y_vals), key=lambda coord: coord[0])
    x_vals, y_vals = zip(*sorted_coords)

    auc = np.trapezoid(y_vals, x_vals)
    auc_result_field.config(state="normal")  # Make field editable to update
    auc_result_field.delete(0, tk.END)       # Clear current content
    auc_result_field.insert(0, f"{auc:.2f}") # Insert the new AUC result
    auc_result_field.config(state="readonly") # Make field readonly again

def show_help():
    messagebox.showinfo("Help",
                        "Input [x, y] coordinates and press 'Calculate' to calculate the area under curve (AUC). "
                        "Use decimal points, not decimal commas.\n\n© 2024 Martin Bezecný")


# GUI Setup
root = tk.Tk()
root.title("AUC Calculator")

# Center window on the screen
root.update_idletasks()
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
root.geometry(f"+{width // 4}+{height // 10}")  # Positioning near the center

# Frame for padding
frame = tk.Frame(root, padx=20, pady=20)
frame.pack(fill="both", expand=True)

# Header Label - centered with `nsew` alignment
heading_label = tk.Label(frame, text="AUC Calculator", font=("Tahoma", 16, "bold"))
heading_label.grid(row=0, column=0, columnspan=7, pady=(0, 10), sticky="nsew")

# Coordinate Entry Fields
x_entries = []
y_entries = []

# Left side: Points 1-13
for i in range(13):
    tk.Label(frame, text=f"Point {i + 1}").grid(row=i + 1, column=0, padx=5, pady=2, sticky="e")

    x_entry = tk.Entry(frame, width=10)
    x_entry.grid(row=i + 1, column=1, padx=5, pady=2)
    x_entries.append(x_entry)

    y_entry = tk.Entry(frame, width=10)
    y_entry.grid(row=i + 1, column=2, padx=5, pady=2)
    y_entries.append(y_entry)

# Right side: Points 14-26, with a slightly reduced gap
for i in range(13, 26):
    tk.Label(frame, text=f"Point {i + 1}").grid(row=i - 12, column=4, padx=5, pady=2, sticky="e")  # Reduced gap

    x_entry = tk.Entry(frame, width=10)
    x_entry.grid(row=i - 12, column=5, padx=5, pady=2)
    x_entries.append(x_entry)

    y_entry = tk.Entry(frame, width=10)
    y_entry.grid(row=i - 12, column=6, padx=5, pady=2)
    y_entries.append(y_entry)

# Buttons and Result Display
calc_button = tk.Button(frame, text="Calculate", command=calculate_auc)
calc_button.grid(row=14, column=3, pady=10, padx=(0, 0), sticky="n")

help_button = tk.Button(frame, text="?", command=show_help, font=("Tahoma", 10, "bold"), width=2, height=1)
help_button.grid(row=14, column=6, sticky="e", padx=(10, 0))

# Result Label and Wider Read-Only Entry
result_label = tk.Label(frame, text="AUC:", font=("Tahoma", 12, "bold"))
result_label.grid(row=15, column=2, sticky="e", pady=(10, 0), padx=(0, 20))

auc_result_field = tk.Entry(frame, font=("Tahoma", 12), width=20, state="readonly", justify="center")
auc_result_field.grid(row=15, column=3, columnspan=3, pady=(10, 0), sticky="w")

# Make the window adapt to content
root.update_idletasks()  # Update geometry based on added widgets
root.minsize(root.winfo_reqwidth(), root.winfo_reqheight())  # Set min size based on required size
root.geometry("")

root.mainloop()
