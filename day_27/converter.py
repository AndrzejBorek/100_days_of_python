import tkinter as tk

WIDTH = 400
HEIGHT = 400

window = tk.Tk()
window.title("Mile to Kilometres Converter")
window.minsize(width=WIDTH, height=HEIGHT)
window.config(padx=50, pady=50)

entry_input = tk.Entry(width=10)
entry_input.grid(row=1, column=1)


def convert():
    miles = float(entry_input.get())
    kilometres = round(miles*1.60934,2)
    result_label.config(text=str(kilometres))


button = tk.Button(text="Convert", padx=50, pady=50, command=convert)
button.grid(row=3, column=1)

miles_label = tk.Label(text="Miles")
miles_label.grid(row=1, column=2)

km_label = tk.Label(text="Kilometres")
km_label.grid(row=2, column=2)

result_label = tk.Label(text="0")
result_label.grid(row=2, column=1)

is_equal_label = tk.Label(text="Is equal: ")
is_equal_label.grid(row=2, column=0)

window.mainloop()
