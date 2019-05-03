import sys

import intro
from action import Action
from game_actions import GameActions
from map import Map

class Game:
    is_running = True

    def __init__(self, player_name):
        self.player_name = player_name
        self.map = Map()
        self.game_actions = GameActions()
        self.game_actions.set_actions(self.create_actions())

    def stop(self):
        self.is_running = False

    def play(self):
        while self.is_running:
            self.game_actions.handle_action()

    def create_actions(self):
        return {
            'schaue': Action('schaue - Zeigt dir, was es in diesem Raum zu sehen gibt.',
                             self.map.look),
            'gehe': Action('gehe <Richtung> - Gehe in diese Richtung.',
                           self.map.go_in_direction),
            'grüße': Action('grüße <Name> - Begrüße die Person im Raum',
                           self.map.greet_person),
            'frage': Action('frage <Name> - Frage eine Person, wie sie zur Software Entwicklung gekommen ist.',
                            self.map.ask_person),
            'beenden': Action('beenden - Beendet das Spiel.',
                              self.stop),
            'hilfe': Action('hilfe - Zeigt dir alle zulässigen Befehle.',
                            self.game_actions.show_list_of_actions)
        }


if __name__ == "__main__":
    try:
        player_name = intro.play()
        Game(player_name).play()
    except KeyboardInterrupt:
        sys.exit(0)

