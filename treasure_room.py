from room import Room
from task import Task
from random import randint
import helper, sys


class TreasureRoom(Room):
    def __init__(self, name, description):
        super().__init__(name, description)
        self.name = name
        self.description = description
        self.task = None

    def intro_treasure_room(self):
        number = randint(0, 999)
        if sys.gettrace():  # if debug mode is on you'll get the number
            print(number)
        helper.wait(2)
        print(
            "Du stehst vor einem Tresor. Um diesen zu öffnen, musst du einen Zahlencode eingeben."
        )
        helper.wait(2)
        print(
            "Dieser Zahlencode liegt zwischen 0 und 999."
            "Versuche durch systematisches probieren, auf die Zahl zu kommen."
        )
        while True:
            try:
                eingabe = int(input("Zahl: "))
                if eingabe == number:
                    print("Richtig")
                    break
                if eingabe < number:
                    print("Gesuchte Zahl ist größer")
                if eingabe > number:
                    print("Gesuchte Zahl ist kleiner")
            except ValueError:
                print("Gib eine Zahl ein!")
        print("Der Code lautet", number)
        print("Der Tresor öffnet sich! Was ist das....")
        helper.wait(2)
        print("...eine Gehaltserhöhung! Du bekommst mehr Geld.")

    def lock_treasure_room(self, code):
        self.task = Task("Gib Code ein: ", code)
        print("Dieser Raum ist verriegelt.")
        print('Um zurück zu gehen, gebe "Exit" ein')
        while True:
            answer = input(self.task.show_question())
            if self.task.is_answer_correct(answer):
                return True
            if answer == "exit" or answer == "Exit":
                return False
