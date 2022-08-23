from question import Question
from data import question_data
from quiz_brain import QuizBrain
import random as r


question_bank = []

for question in question_data:
    text = question["text"]
    answer = question["answer"]
    question_bank.append(Question(text, answer))
    
    
quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()
    