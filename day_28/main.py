import math
from datetime import date, datetime
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #

SCREEN_WIDTH = 220
SCREEN_HEIGHT = 224
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
font = (FONT_NAME, 30, 'bold')
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 1
small_cycle_counter = 0
CHECK_MARK = "✓"
timer = None


# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="TIMER", fg=GREEN)
    check_mark_label.config(text="")
    global small_cycle_counter
    small_cycle_counter = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global small_cycle_counter
    small_cycle_counter += 1
    if small_cycle_counter % 8 == 0:
        countdown(LONG_BREAK_MIN * 5)
        title_label.config(text="BREAK", fg=RED)
    elif small_cycle_counter % 2 == 0:
        countdown(SHORT_BREAK_MIN * 5)
        title_label.config(text="BREAK", fg=YELLOW)
    else:
        countdown(WORK_MIN * 5)
        title_label.config(text="TIMER", fg=GREEN)



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


import time


def countdown(count):
    count_min = int(count / 60)
    count_sec = count % 60
    canvas.itemconfig(timer_text, text=f"{count_min:02d}:{count_sec:02d}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        marks = ""
        number_of_checkmarks = math.floor(small_cycle_counter / 2)
        for _ in range(number_of_checkmarks):
            marks = marks + CHECK_MARK
        check_mark_label.config(text=marks)


# def reset_timer():
#     global small_cycle_counter
#     small_cycle_counter = 0
#     countdown(0)


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro app")
window.config(padx=100, pady=50, bg=PINK)

title_label = Label(text="TIMER", font=font, fg=GREEN, bg=PINK)
title_label.grid(row=0, column=1)

canvas = Canvas(width=SCREEN_WIDTH, height=SCREEN_HEIGHT, highlightthickness=0)
tomato_image = PhotoImage(file='tomato.png')
canvas.create_image(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, image=tomato_image)

timer_text = canvas.create_text(115, 130, text="00:00", fill='white', font=font)
canvas.config(bg=PINK)
canvas.grid(row=1, column=1)

start_button = Button(text="Start", bg=GREEN, highlightthickness=0, command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", bg=GREEN, highlightthickness=0, command=reset_timer)
reset_button.grid(row=2, column=2)

check_mark_label = Label(bg=PINK, fg=RED, highlightthickness=0)
check_mark_label.grid(row=3, column=1)

window.mainloop()
