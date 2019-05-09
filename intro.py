import helper


def play():
    print('Hallo, willkommen im Aufzug von Gebäude 7. Wie ist dein Name?')
    name = helper.read_user_input()
    print('Hey {0}! Schön dass du hier bist. Ich bringe dich mal ins 2. OG ...'.format(name))
    helper.wait(1)
    print('*pling*')
    helper.wait(1)
    return name