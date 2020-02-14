from . import helper
from .room import Room
from .task import Task


class EscapeRoom(Room):
    def __init__(self, name, description):
        super().__init__(name, description)
        self.task = None
        self.count = None

    def intro(self):
        self.task = Task(
            "Wie heißt das erste Program, was jeder Programmierer lernt",
            "hello world",
            30,
        )
        print("Oh. Hallo. Gut das du da bist. Ich brauche deine Hilfe!")
        helper.wait(2)
        print("Ich komme bei diesem Problem nicht weiter. Kannst du es für mich lösen?")
        helper.wait(2)
        print(
            "Eigentlich hast du keine anderer Möglichkeit. Dafür bezahle ich dich schließlich."
        )
        helper.wait(2)
        task_resolved = self.task.run()
        if task_resolved:
            print("Du hast die Aufgabe erfüllt!!!")
            print("Gut gemacht! Der Code für die Schatzkammer ist 7854")
