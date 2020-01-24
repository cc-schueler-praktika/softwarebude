class Task:

    def __init__(self, question, solution):
        self.question = question
        self.solution = solution

    def is_answer_correct(self, answer):
        return self.solution == answer

    def show_question(self):
        print(self.question)