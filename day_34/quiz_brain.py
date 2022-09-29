from day_34.question_model import Question


class QuizBrain:

    def __init__(self, question_list: list[Question]):
        self.question_number: int = 0
        self.score: int = 0
        self.question_list = question_list
        self.current_question = None

    def still_has_questions(self) -> bool:
        return self.question_number < len(self.question_list)

    def next_question(self) -> Question:
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        return self.current_question

    def check_answer(self, user_answer: str):
        correct_answer = self.current_question.answer
        return user_answer.lower() == correct_answer.lower()
