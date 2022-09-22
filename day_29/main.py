import json
from tkinter import *
from random import *
import string
from tkinter import messagebox

import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_random_password():
    password = ""
    for _ in range(14):
        sign = randint(1, 3)
        if sign == 1:
            password += choice(string.ascii_letters)
        elif sign == 2:
            password += choice(string.digits)
        else:
            password += choice(string.punctuation)
    password_entry.delete(0, END)
    password_entry.insert(0, password)
    password = password_entry.get()
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {username} "
                                                              f"\nPassword: {password} \nIs it ok to save?")
        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {username} | {password}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200, highlightthickness=0)
lock_image = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=lock_image)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

username_label = Label(text="Username/Email:")
username_label.grid(row=2, column=0)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# Buttons
generate_password_button = Button(text="Generate", command=generate_random_password, width=12)
generate_password_button.grid(row=3, column=1, sticky='e')

add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)

# Entries
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2, sticky="w")

username_entry = Entry(width=35)
username_entry.insert(END, string="USERNAME")
username_entry.grid(row=2, column=1, columnspan=2, sticky="w")

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1, sticky="w")

# Mainloop
window.mainloop()
