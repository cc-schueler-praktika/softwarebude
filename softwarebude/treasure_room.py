import sys
from random import randint

from . import helper
from .room import Room
from .task import Task


class TreasureRoom(Room):
    def __init__(self, name, description, code):
        task = Task("Gib zum öffnen der Türe bitte den richtigen Code ein", code)
        super().__init__(name, description, is_locked=True, task_to_open=task)
        self.name = name
        self.description = description

    def intro(self):
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
        print("...eine Gehaltserhöhung! Du bekommst mehr Geld. 💸")
