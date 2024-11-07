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

    if len(x_vals) < 2:
        messagebox.showerror("Insufficient Data", "At least two valid points are required to calculate AUC.")
        return

    sorted_coords = sorted(zip(x_vals, y_vals), key=lambda coord: coord[0])
    x_vals, y_vals = zip(*sorted_coords)

    auc = np.trapezoid(y_vals, x_vals)
    result_label.config(text=f"AUC: {auc:.2f}")


def show_help():
    messagebox.showinfo("Help",
                        "Input [x, y] coordinates and press 'Calculate' to calculate the area under curve (AUC). "
                        "Use decimal points, not decimal commas.\n\n© 2024 Martin Bezecný")


# GUI Setup
root = tk.Tk()
root.title("AUC Calculator")

# Add a frame with padding and prevent resizing based on the content
frame = tk.Frame(root, padx=20, pady=20)
frame.pack()
frame.pack_propagate(False)  # Prevent automatic resizing of the frame based on content

# Header Label - Centered
heading_label = tk.Label(frame, text="AUC Calculator", font=("Tahoma", 16, "bold"))
heading_label.grid(row=0, column=0, columnspan=3, pady=(0, 10), sticky="nsew")

# Configure columns to allow the header to center
frame.grid_columnconfigure(0, weight=1)
frame.grid_columnconfigure(1, weight=1)
frame.grid_columnconfigure(2, weight=1)

# Coordinate Entry Fields
x_entries = []
y_entries = []
for i in range(26):
    tk.Label(frame, text=f"Point {i + 1}").grid(row=i + 1, column=0, padx=5, pady=2)

    x_entry = tk.Entry(frame, width=10)
    x_entry.grid(row=i + 1, column=1, padx=5, pady=2)
    x_entries.append(x_entry)

    y_entry = tk.Entry(frame, width=10)
    y_entry.grid(row=i + 1, column=2, padx=5, pady=2)
    y_entries.append(y_entry)

# Buttons (Calculate AUC and Help) - Centered in the Window
calc_button = tk.Button(frame, text="Calculate", command=calculate_auc)
calc_button.grid(row=27, column=0, columnspan=2, pady=10, sticky="nsew")

help_button = tk.Button(frame, text="?", command=show_help, font=("Tahoma", 10, "bold"), width=2, height=1)
help_button.grid(row=27, column=2, pady=10)

# Configure row/column weights for centering
frame.grid_rowconfigure(27, weight=1)
frame.grid_columnconfigure(0, weight=1)
frame.grid_columnconfigure(1, weight=1)
frame.grid_columnconfigure(2, weight=1)

# Label to Display Result in Bold
result_label = tk.Label(frame, text="AUC: ", font=("Tahoma", 12, "bold"))
result_label.grid(row=28, column=0, columnspan=3, pady=(5, 0))

# Center the window on the screen
root.update_idletasks()  # Update "requested size" based on content
window_width = root.winfo_width()
window_height = root.winfo_height()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Calculate position x, y to center the window
position_x = int((screen_width - window_width) / 2)
position_y = int((screen_height - window_height) / 2)
root.geometry(f"{window_width}x{window_height}+{position_x}+{position_y}")

root.mainloop()