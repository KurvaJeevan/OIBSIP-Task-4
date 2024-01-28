from tkinter import *
from tkinter import ttk, messagebox
from tkinter import simpledialog
import random
import string
import pyperclip

a = Tk()
a.title("Password Generator")

font1 = ("Times", 30, "bold")
title = Label(a, font=font1, text="Password Generator").grid(row=0, column=0, columnspan=2, pady=10)

length_var = IntVar()  # Use IntVar to store the length
length_Label = Label(a, text="Password Length").grid(row=1, column=0, padx=10, pady=10)
length_entry = Entry(a, textvariable=length_var).grid(row=1, column=1, padx=10, pady=10)

complexity = StringVar(value="Medium")
password = StringVar(value="")

def GeneratePass():
    length = length_var.get()  # Use get() to retrieve the value
    if length <= 0:
        messagebox.showerror("Error", "Please enter a valid password length.")
        return
    c = complexity.get()
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    if c == "Low":  # Compare with c instead of complexity
        characters = lowercase + uppercase
    elif c == "Medium":
        characters = lowercase + uppercase + digits
    elif c == "High":
        characters = lowercase + uppercase + digits + "!@#$%^&*"
    password1 = ''.join(random.choice(characters) for _ in range(length))
    password.set(password1)

def copy():
    password1 = password.get()
    pyperclip.copy(password1)
    messagebox.showinfo("Password Copied", "Password copied to clipboard!")

Complexity_Label = Label(a, text="Password Complexity").grid(row=2, column=0, padx=10, pady=10)
Complexity_entry = ttk.Combobox(a, textvariable=complexity, state="readonly", values=["Low", "Medium", "High"]).grid(row=2, column=1, padx=10, pady=10)
Generate_Button = Button(a, text="Generate Password", command=lambda: GeneratePass()).grid(row=3, column=0, columnspan=2, pady=10)
Password_Label = Label(a, text="Password").grid(row=4, column=0, padx=10, pady=10)
password_entry = ttk.Entry(a, textvariable=password, state="readonly").grid(row=4, column=1, padx=10, pady=10)
copy_button = Button(a, text="Copy Password", command=lambda: copy()).grid(row=5, column=0, columnspan=2, pady=10)

a.mainloop()
