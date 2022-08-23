class QuizBrain:

    def __init__(self, question_list) -> None:
        self.points = 0
        self.question_number = 0
        self.question_list = question_list 
    
    def check_answer(self, question, answer):
        if answer.lower() == question.answer.lower():
            return True
        else:
            return False

    def next_question(self):
        question = self.question_list[self.question_number]
        answer = input(f" Q.{self.question_number+1}: {question.text} (True/False)?: ")
        if self.check_answer(question, answer):
            print("Correct answer \n")
            self.points += 1 
        else:
            print("Wrong answer \n")
        self.question_number += 1
    

    def still_has_questions(self):
        if self.question_number == len(self.question_list):
            print("No more questions.")
            print(f"You got {self.get_points()} points")
            return  False
        else:
            return True


    def get_points(self) -> int:
        return self.points


    