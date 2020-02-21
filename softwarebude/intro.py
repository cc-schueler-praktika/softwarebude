import os

from pyfiglet import Figlet

from . import helper


def play():
    os.system("clear")
    print("\n\n\n\n")
    f = Figlet(font="roman")
    print(f.renderText("Softwarebude"))
    print("Hallo, willkommen im Aufzug von Gebäude 7. Wie ist dein Name?")
    name = helper.read_user_input()
    print(
        "Hey {0}! Schön dass du hier bist. Ich bringe dich mal ins 2. OG ... "
        'Tippe "hilfe", wenn du nicht mehr weiterweißt'.format(name)
    )
    helper.wait(1)
    print("*pling*")
    helper.wait(1)
    return name
