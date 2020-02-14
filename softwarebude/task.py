from softwarebude.countdown import Countdown


class Task:
    def __init__(self, question, solution, seconds_to_solve=0):
        self.question = question
        self.solution = solution
        if seconds_to_solve > 0:
            self.countdown = Countdown(seconds_to_solve)
        else:
            self.countdown = None

    def is_answer_correct(self, answer):
        return self.solution == answer

    def show_question(self):
        print(self.question + " [Tippe 'exit' um abzubrechen]: ")

    def run(self):
        if self.countdown is not None:
            self.countdown.start()
        while self.is_time_to_answer_left():
            answer = input(self.question + " [Tippe 'exit' um abzubrechen]: ")
            if answer.lower() == "exit":
                self.stop_counter()
                return False
            if self.is_answer_correct(answer):
                self.stop_counter()
                return True
            elif self.is_time_to_answer_left():
                print("Das war nicht korrekt.")

    def is_time_to_answer_left(self):
        if self.countdown is not None:
            return not self.countdown.countdown_expired
        else:
            return True

    def stop_counter(self):
        if self.countdown is not None:
            self.countdown.stop_countdown()
