from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface


# question_bank = []

question_bank = [Question(question['question'], question['correct_answer']) for question in question_data]
#
# for question in question_data:
#     question_text = question["question"]
#     question_answer = question["correct_answer"]
#     new_question = Question(question_text, question_answer)
#     question_bank.append(new_question)


quiz = QuizBrain(question_bank)
quiz_interface = QuizInterface(quiz)
