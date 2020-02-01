class Task:
    def __init__(self, question, solution):
        self.question = question
        self.solution = solution

    def is_answer_correct(self, answer):
        return self.solution == answer

    # FIXME
    def show_question(self):
        print(self.question + " [Tippe 'exit' um abzubrechen]: ")

    def run(self):
        while True:
            answer = input(self.question + " [Tippe 'exit' um abzubrechen]: ")
            if answer.lower() == "exit":
                return False
            if self.is_answer_correct(answer):
                return True
            else:
                print("Das war nicht korrekt.")
