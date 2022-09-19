import tkinter as tk

WIDTH = 800
HEIGHT = 600

window = tk.Tk()
window.title("My first gui program in python")
window.minsize(width=WIDTH, height=HEIGHT)
window.config(padx=200, pady=200)

# Label

my_label = tk.Label(text="I am label", font=("Arial", 24))
# my_label.place(x=WIDTH/2, y=HEIGHT/2)
my_label.config(text="I am label, but configured", padx=50, pady=50)
my_label.grid(row=0, column=0)



def button_click():
    # if my_label['text'] == "I am label, but configured":
    #     my_label.config(text="Button got clicked")
    # elif my_label['text'] == "Button got clicked":
    #     my_label.config(text="I am label, but configured")
    my_label.config(text=entry_input.get())


my_button = tk.Button(text="Click me", command=button_click)
my_button.grid(row=1, column=1)

new_button = tk.Button(text="New button")
new_button.grid(row=0, column=2)

# Entry component

entry_input = tk.Entry(width=10)
entry_input.grid(row=2, column=3)

window.mainloop()
