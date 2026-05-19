import tkinter as tk
from tkinter import ttk

def convert():
    try:
        kg = float(kg_entry.get())
        
        # Calculations
        grams = kg * 1000
        pounds = kg * 2.20462
        ounces = kg * 35.274
        
        # Update labels with formatted strings
        gram_val.config(text=f"{grams:,.2f} g")
        pound_val.config(text=f"{pounds:,.2f} lbs")
        ounce_val.config(text=f"{ounces:,.2f} oz")
        error_label.config(text="") # Clear any previous error
    except ValueError:
        error_label.config(text="Please enter a valid number!")
        # Clear results on error
        gram_val.config(text="-")
        pound_val.config(text="-")
        ounce_val.config(text="-")

# Color Palette (Modern Dark Theme)
BG_MAIN = "#1e1e2e"       # Deep dark blue/gray
BG_CARD = "#252538"       # Lighter gray for result boxes
TEXT_MAIN = "#cdd6f4"     # Soft white
TEXT_MUTED = "#a6adc8"    # Soft gray for labels
ACCENT = "#89b4fa"        # Vibrant pastel blue for button/highlights
ERROR_COLOR = "#f38ba8"   # Soft red for errors

# Setup Root Window
root = tk.Tk()
root.title("Modern Weight Converter")
root.geometry("450x500")
root.configure(bg=BG_MAIN)
root.resizable(False, False)

# App Title
title_label = tk.Label(root, text="Weight Converter", font=("Helvetica", 22, "bold"), bg=BG_MAIN, fg=ACCENT)
title_label.pack(pady=(30, 10))

subtitle_label = tk.Label(root, text="Convert Kilograms to multiple units instantly", font=("Helvetica", 10), bg=BG_MAIN, fg=TEXT_MUTED)
subtitle_label.pack(pady=(0, 20))

# Input Section Frame
input_frame = tk.Frame(root, bg=BG_MAIN)
input_frame.pack(pady=10)

kg_label = tk.Label(input_frame, text="Enter Weight (kg):", font=("Helvetica", 12, "bold"), bg=BG_MAIN, fg=TEXT_MAIN)
kg_label.pack(anchor="w", padx=5, pady=2)

# Styled Entry Box
kg_entry = tk.Entry(input_frame, font=("Helvetica", 16), bg=BG_CARD, fg=TEXT_MAIN, insertbackground=TEXT_MAIN, bd=0, justify="center", width=18)
kg_entry.pack(ipady=8, pady=5)
kg_entry.focus()

# Error Message Label
error_label = tk.Label(root, text="", font=("Helvetica", 10), bg=BG_MAIN, fg=ERROR_COLOR)
error_label.pack()

# Convert Button
convert_btn = tk.Button(root, text="CONVERT", font=("Helvetica", 12, "bold"), bg=ACCENT, fg=BG_MAIN, activebackground=TEXT_MAIN, activeforeground=BG_MAIN, bd=0, width=15, height=2, cursor="hand2", command=convert)
convert_btn.pack(pady=15)

# Results Container
results_frame = tk.Frame(root, bg=BG_MAIN)
results_frame.pack(fill="x", padx=40, pady=10)

# Helper function to create clean visual result cards
def create_card(parent, label_text):
    card = tk.Frame(parent, bg=BG_CARD, bd=0)
    card.pack(fill="x", pady=5, ipady=10)
    
    lbl = tk.Label(card, text=label_text, font=("Helvetica", 10, "bold"), bg=BG_CARD, fg=TEXT_MUTED)
    lbl.pack(side="left", padx=20)
    
    val = tk.Label(card, text="-", font=("Helvetica", 14, "bold"), bg=BG_CARD, fg=ACCENT)
    val.pack(side="right", padx=20)
    
    return val

# Generate the UI Cards
gram_val = create_card(results_frame, "Grams")
pound_val = create_card(results_frame, "Pounds")
ounce_val = create_card(results_frame, "Ounces")

# Start the Application
root.mainloop()