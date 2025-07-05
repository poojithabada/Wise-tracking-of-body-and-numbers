import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Wise tracking of body and numbers 💻❤️")
root.geometry("420x830")
root.config(bg="#e6f2ff")
root.resizable(False, False)

# -------- Placeholder Behavior -------- #
def clear_entry_placeholder(e, entry, placeholder):
    if entry.get() == placeholder:
        entry.delete(0, tk.END)

def restore_placeholder(e, entry, placeholder):
    if entry.get() == "":
        entry.insert(0, placeholder)

# -------- Calculator Logic -------- #
def perform_operation(op):
    try:
        a = float(entry_num1.get())
        b = float(entry_num2.get())
        if op == '+': res = a + b
        elif op == '-': res = a - b
        elif op == '*': res = a * b
        elif op == '/': res = a / b if b != 0 else 'Error: Divide by 0'
        elif op == '%': res = a % b
        elif op == '**': res = a ** b
        else: res = "Invalid"
        result_label.config(text=f"Result: {res}", fg="#003366")
    except:
        messagebox.showerror("Error", "Please enter valid numbers")

# -------- BMI Logic -------- #
def check_bmi():
    try:
        w = float(entry_weight.get())
        h = float(entry_height.get())
        bmi = w / (h ** 2)
        if bmi < 18.5: status = "Underweight"
        elif bmi < 25: status = "Normal weight"
        elif bmi < 30: status = "Overweight"
        else: status = "Obese"
        bmi_result.config(text=f"BMI: {round(bmi, 2)} ({status})", fg="#003366")
    except:
        messagebox.showerror("Error", "Enter valid weight and height")

# -------- Entry Styling Helper -------- #
def style_entry(entry, placeholder):
    entry.insert(0, placeholder)
    entry.config(font=("Segoe UI", 12), justify='center', bd=0, relief='flat',
                 bg="#ffffff", fg="#666666")
    entry.bind("<FocusIn>", lambda e: clear_entry_placeholder(e, entry, placeholder))
    entry.bind("<FocusOut>", lambda e: restore_placeholder(e, entry, placeholder))
    entry.pack(pady=6, ipadx=10, ipady=8, fill="x", padx=40)

# -------- Header -------- #
tk.Label(root, text="Smart Health & Calculator", font=("Segoe UI", 18, "bold"),
         bg="#e6f2ff", fg="#003366").pack(pady=20)

# -------- Calculator Section -------- #
tk.Label(root, text="Basic Calculator", font=("Segoe UI", 15, "bold"),
         bg="#e6f2ff", fg="#004080").pack(pady=(10, 5))

entry_num1 = tk.Entry(root)
style_entry(entry_num1, "First number")

entry_num2 = tk.Entry(root)
style_entry(entry_num2, "Second number")

tk.Label(root, text="Choose Operation", font=("Segoe UI", 11),
         bg="#e6f2ff", fg="#333333").pack(pady=(5, 0))

# -------- Operator Buttons (Small & Neat) -------- #
btn_frame = tk.Frame(root, bg="#e6f2ff")
btn_frame.pack(pady=5)

ops = ['+', '-', '*', '/', '%', '**']
for i, op in enumerate(ops):
    tk.Button(btn_frame, text=op, command=lambda o=op: perform_operation(o),
              bg="#007acc", fg="white", font=("Segoe UI", 10, "bold"),
              activebackground="#005f99", activeforeground="white",
              relief="flat", bd=0, width=4, height=1,
              highlightthickness=0).grid(row=i//3, column=i%3, padx=8, pady=6)

result_label = tk.Label(root, text="", font=("Segoe UI", 12, "bold"),
                        bg="#e6f2ff", fg="#003366")
result_label.pack(pady=10)

# -------- Divider -------- #
tk.Label(root, text="─" * 50, bg="#e6f2ff", fg="#bbbbbb").pack(pady=10)

# -------- BMI Checker Section -------- #
tk.Label(root, text="BMI Checker", font=("Segoe UI", 15, "bold"),
         bg="#e6f2ff", fg="#004080").pack(pady=(5, 5))

entry_weight = tk.Entry(root)
style_entry(entry_weight, "Weight in kg")

entry_height = tk.Entry(root)
style_entry(entry_height, "Height in meters")

tk.Button(root, text="Check BMI", command=check_bmi,
          bg="#28a745", fg="white", font=("Segoe UI", 11, "bold"),
          activebackground="#1e7e34", relief="flat", bd=0,
          width=20, height=1, padx=5, pady=5).pack(pady=10)

bmi_result = tk.Label(root, text="", font=("Segoe UI", 12, "bold"),
                      bg="#e6f2ff", fg="#003366")
bmi_result.pack(pady=5)

# -------- Exit Button (Bottom Right) -------- #
exit_frame = tk.Frame(root, bg="#e6f2ff")
exit_frame.pack(fill='both', expand=True)

tk.Button(exit_frame, text="Exit App", command=root.quit,
          bg="#dc3545", fg="white", font=("Segoe UI", 11, "bold"),
          activebackground="#c82333", relief="flat", bd=0,
          width=12, height=1, padx=10, pady=5).pack(side="bottom", padx=20, pady=10)

root.mainloop()
