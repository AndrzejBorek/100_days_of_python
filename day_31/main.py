import time
from tkinter import PhotoImage, Tk, Button, Canvas, messagebox

import pandas as pd
import random as r

# ------------------- DATA ---------------- #
# In my case I downloaded data in format which looked like this: word in PL number of occurrences, word in EN number
# of occurrences. I had to get rid of numbers from my rows and then change words.csv file.
# data['PL'] = data['PL'].str.split().str[:-1]
# data['EN'] = data['EN'].str.split().str[:-1]
# data.to_csv('words.csv')
data = pd.read_csv('words.csv', index_col=0)

# Due to specification of Polish language and translation to english i had to get rid of [,],', , from my words
data['EN'] = data['EN'].map(lambda x: x.lstrip("'[").rstrip("']").replace(",", '').replace("'", ""))
data['PL'] = data['PL'].map(lambda x: x.lstrip("'[").rstrip("']"))
to_learn = data.to_dict(orient="index")
current_card = {}
known_words = []


# --------------- Buttons handlers -----------------#


# ---------------- Changing Word -------------------#
def generate_random_word():
    global current_card, flip_timer
    current_card = {}
    if current_card not in known_words:
        current_card = r.choice(to_learn)
        window.after_cancel(flip_timer)
        canvas.itemconfig(language_text, text=EN, fill="green")
        canvas.itemconfig(word_text, text=current_card['EN'], fill="green")
        canvas.itemconfig(canvas_image, image=card_front)
        flip_timer = window.after(3000, func=flip_card)
    else:
        try:
            generate_random_word()
        except RecursionError:
            messagebox.showinfo(title="!!!!", message="You do not have more words")
            window.destroy()


# # ---------------- Handling cards --------------#

def flip_card():
    canvas.itemconfig(language_text, text=PL, fill="white")
    canvas.itemconfig(word_text, text=current_card['PL'], fill="white")
    canvas.itemconfig(canvas_image, image=card_back)


def is_known():
    known_words.append(current_card)
    data = pd.DataFrame(to_learn).transpose()
    data.to_csv("words_to_learn.csv", index=False)
    generate_random_word()


# # ------------------- UI -------------------------#
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 526
BACKGROUND_COLOR = "#B1DDC6"
PL = "Polish"
EN = "English"
FONT_NAME = "Ariel"
LANGUAGE_FONT = (FONT_NAME, 40, 'italic')
WORD_FONT = (FONT_NAME, 60, 'bold')

window = Tk()
window.title("Flash card app")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

# Canvas
card_back = PhotoImage(file='images/card_back.png')
card_front = PhotoImage(file='images/card_front.png')

canvas = Canvas(width=SCREEN_WIDTH, height=SCREEN_HEIGHT, highlightthickness=0)
canvas_image = canvas.create_image(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, image=card_back)
language_text = canvas.create_text(400, 150, text=PL, fill='white', font=LANGUAGE_FONT)
word_text = canvas.create_text(400, 263, text=PL, fill='white', font=WORD_FONT)
canvas.grid(row=0, column=0, columnspan=2)

# Buttons
correct_answer_image = PhotoImage(file="images/right.png")
correct_answer_button = Button(image=correct_answer_image, highlightthickness=0, padx=50, pady=50,
                               command=is_known)
correct_answer_button.grid(row=1, column=0)

wrong_answer_image = PhotoImage(file="images/wrong.png")
wrong_answer_button = Button(image=wrong_answer_image, highlightthickness=0, padx=50, pady=50,
                             command=generate_random_word)
wrong_answer_button.grid(row=1, column=1)

window.mainloop()
