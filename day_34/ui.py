from quiz_brain import QuizBrain
from tkinter import *

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        # Quiz brain
        self.quiz_brain = quiz_brain
        # Window
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)
        # Score label
        self.score_label = Label(text=f"Score: {quiz_brain.score} ", fg='white', bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)
        # Canvas
        self.canvas = Canvas(width=300, height=250, bg='white')
        self.canvas.create_image(150, 207)
        self.question_text = self.canvas.create_text(150,
                                                     125,
                                                     width=280,
                                                     font=("Arial", 20, "bold"),
                                                     fill=THEME_COLOR
                                                     )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        # Images to buttons
        false_image = PhotoImage(file='images/false.png')
        true_image = PhotoImage(file='images/true.png')
        # Buttons
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.false_answer)
        self.false_button.grid(row=2, column=1)
        self.true_button = Button(image=true_image, highlightthickness=0, command=self.true_answer)
        self.true_button.grid(row=2, column=0)
        # Starting program with some question
        self.next_question()
        # Window staying alive
        self.window.mainloop()

    def false_answer(self):
        self.check_answer(answer='False')

    def true_answer(self):
        self.check_answer(answer='True')

    def check_answer(self, answer: str):
        if self.quiz_brain.check_answer(user_answer=answer):
            self.quiz_brain.score += 1
            self.score_label.config(text=f"Score: {self.quiz_brain.score} ")
        self.next_question()

    def next_question(self):
        if self.quiz_brain.still_has_questions():
            question = self.quiz_brain.next_question()
            self.canvas.itemconfig(self.question_text, text=f"Q{self.quiz_brain.question_number}: {question.text}")
        else:
            self.canvas.itemconfig(self.question_text, text=f"No more questions. Your score is {self.quiz_brain.score}")
            self.true_button.config(state='disabled')
            self.false_button.config(state='disabled')
