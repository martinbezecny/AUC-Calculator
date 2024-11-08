import customtkinter as ctk
from tkinter import messagebox
import numpy as np

# Set appearance and color theme
ctk.set_appearance_mode("Light")
ctk.set_default_color_theme("blue")


# Function to calculate AUC
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

    if len(x_vals) != len(set(x_vals)):
        messagebox.showerror("Duplicate x-values", "Duplicate x-values detected. Each x-value must be unique.")
        return

    sorted_coords = sorted(zip(x_vals, y_vals), key=lambda coord: coord[0])
    x_vals, y_vals = zip(*sorted_coords)

    auc = np.trapezoid(y_vals, x_vals)
    auc_result_field.configure(state="normal")
    auc_result_field.delete(0, ctk.END)
    auc_result_field.insert(0, f"{auc:.2f}")
    auc_result_field.configure(state="readonly")


def clear_fields():
    for entry in x_entries + y_entries:
        entry.delete(0, ctk.END)
    auc_result_field.configure(state="normal")
    auc_result_field.delete(0, ctk.END)
    auc_result_field.configure(state="readonly")


def show_help():
    messagebox.showinfo("Help",
                        "Input [x, y] coordinates and press 'Calculate' to calculate the area under curve (AUC). "
                        "Use decimal points, not decimal commas.\n\n© 2024 Martin Bezecný")


# GUI Setup with customtkinter
root = ctk.CTk()
root.title("AUC Calculator")
root.configure(bg="#EBEBEB")  # Set consistent background color

# Frame with consistent background color
frame = ctk.CTkFrame(root, fg_color="#EBEBEB")
frame.pack(fill="both", expand=True, padx=20, pady=20)

# Header Label - centered with `nsew` alignment
heading_label = ctk.CTkLabel(frame, text="AUC Calculator", font=("Arial", 25, "bold"))
heading_label.grid(row=0, column=0, columnspan=7, pady=(0, 10), sticky="nsew")

# Axis labels "x y x y" for columns
x1_label = ctk.CTkLabel(frame, text="x", font=("Arial", 14, "bold"))
x1_label.grid(row=1, column=1, pady=(0, 1), sticky="n")
y1_label = ctk.CTkLabel(frame, text="y", font=("Arial", 14, "bold"))
y1_label.grid(row=1, column=2, pady=(0, 1), sticky="n")

x2_label = ctk.CTkLabel(frame, text="x", font=("Arial", 14, "bold"))
x2_label.grid(row=1, column=5, pady=(0, 1), sticky="n")
y2_label = ctk.CTkLabel(frame, text="y", font=("Arial", 14, "bold"))
y2_label.grid(row=1, column=6, pady=(0, 1), sticky="n")

# Coordinate Entry Fields
x_entries = []
y_entries = []

# Left side: Points 1-13
for i in range(13):
    ctk.CTkLabel(frame, text=f"Point {i + 1}").grid(row=i + 2, column=0, padx=5, pady=2, sticky="e")

    x_entry = ctk.CTkEntry(frame, width=80)
    x_entry.grid(row=i + 2, column=1, padx=5, pady=2)
    x_entries.append(x_entry)

    y_entry = ctk.CTkEntry(frame, width=80)
    y_entry.grid(row=i + 2, column=2, padx=5, pady=2)
    y_entries.append(y_entry)

# Right side: Points 14-26
for i in range(13, 26):
    ctk.CTkLabel(frame, text=f"Point {i + 1}").grid(row=i - 11, column=4, padx=(30, 5), pady=2, sticky="e")

    x_entry = ctk.CTkEntry(frame, width=80)
    x_entry.grid(row=i - 11, column=5, padx=(5, 30), pady=2)
    x_entries.append(x_entry)

    y_entry = ctk.CTkEntry(frame, width=80)
    y_entry.grid(row=i - 11, column=6, padx=5, pady=2)
    y_entries.append(y_entry)


# Result and Buttons on Last Row with Extra Spacing
frame.grid_rowconfigure(15, minsize=20)  # Add space between inputs and buttons

result_label = ctk.CTkLabel(frame, text="AUC = ", font=("Arial", 18, "bold"))
result_label.grid(row=16, column=1, sticky="e", pady=(10, 0), padx=(5, 5))

auc_result_field = ctk.CTkEntry(frame, font=("Arial", 14), width=175, state="readonly", justify="center")
auc_result_field.grid(row=16, column=2, columnspan=2, pady=(10, 0), sticky="we")

# Calculate, Clear, and Help Buttons
calc_button = ctk.CTkButton(frame, text="Calculate", font=("Arial", 14, "bold"), command=calculate_auc)
calc_button.grid(row=16, column=4, sticky="we", padx=(5, 0), pady=(10, 0))

clear_button = ctk.CTkButton(frame, text="Clear", font=("Arial", 14, "bold"), command=clear_fields, fg_color="red", hover_color="#a83232", width=80, height=30)
clear_button.grid(row=16, column=5, sticky="we", padx=(5, 0), pady=(10, 0))

help_button = ctk.CTkButton(frame, text="?", font=("Arial", 14, "bold"), command=show_help, width=30, height=30)
help_button.grid(row=16, column=6, sticky="e", padx=(10, 0), pady=(10, 0))

# Set minimum window size based on required size of widgets
root.update_idletasks()
root.minsize(root.winfo_reqwidth(), root.winfo_reqheight())

root.mainloop()
