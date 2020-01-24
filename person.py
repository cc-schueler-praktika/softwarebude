import random


class Person:
    GREETINGS = ["Hey!", "Hallo!", "Huhu!"]

    def __init__(self, name, emoji, story):
        self.name = name
        self.emoji = emoji
        self.story = story

    def show_description(self):
        print(self.emoji, self.name)

    def say_hello(self):
        random_greeting = self.GREETINGS[random.randint(0, len(self.GREETINGS) - 1)]
        print(self.emoji, "👋 {0} Mein Name ist {1}.".format(random_greeting, self.name))

    def tell_story(self):
        print(self.emoji, self.story)
