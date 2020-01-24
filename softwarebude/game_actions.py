from . import helper


class GameActions:
    def __init__(self):
        self.actions = {}

    def set_actions(self, actions):
        self.actions = actions

    def handle_action(self):
        while True:
            argument = None
            user_input = helper.read_user_input().split()

            if not user_input:
                self.show_invalid_action_message()
                continue

            command = user_input[0].lower()

            if len(user_input) > 1:
                argument = user_input[1].lower()

            if command in self.actions:
                action = self.actions[command]
                action.execute(argument)
                break
            else:
                self.show_invalid_action_message()

    def show_invalid_action_message(self):
        print(
            'Tut mir leid, das verstehe ich nicht. Wenn ich dir weiterhelfen kann, dann tippe doch "hilfe"'
        )

    def show_list_of_actions(self):
        print("-" * 55)
        print("Folgende Befehle stehen dir zur Verfügung:")
        for action in self.actions:
            print(" -", self.actions[action].description)
        print("-" * 55)
