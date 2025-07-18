import tkinter as tk  # Import tkinter and give it a short name "tk"
# Create the MAIN APPLICATIONS WINDOW
root = tk.Tk()
root.title("Simple Calculator") # Set window title
# Set window size (optional)
root.geometry("250x340")


# --- Step 2: Add Entry widget for input/output display ---
entry = tk.Entry(root, width=10, font=('Arial', 20), borderwidth=2, relief='solid', justify='right')
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

def click(value):
    entry.insert(tk.END, value)

def evaluate():
    try:  #eval() is a built-in Python function that takes a string and Solves the math
        result = eval(entry.get()) #Gets the expression as text because the Entry box accepts text only.
        entry.delete(0, tk.END) # Clears previous text.
        entry.insert(0, str(result))#insert the result (answer) into the text box Convert the number (like 5) into a string ("5"),
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")    

def clear():
    entry.delete(0, tk.END)

buttons = [ #This is a list of tuples representing each button.
             #Each tuple = (button_text, row_number, column_number)
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3),
]

for (text, row, col) in buttons:
    if text == '=':
        btn = tk.Button(root, text=text, width=4, height=2, font=("Ariel", 15), command=evaluate)
    elif text == 'C':
        btn = tk.Button(root, text=text, width=4, height=2, font=("Ariel", 15), command=clear)
    else:
        btn = tk.Button(root, text=text, width=4, height=2, font=("Ariel", 15), command=lambda t=text: click(t))
    btn.grid(row=row, column=col, padx=4, pady=4)

# Run the GUI loop so the window stays open
root.mainloop()
