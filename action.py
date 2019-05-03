class Action:

    def __init__(self, description, method):
        self.description = description
        self.method = method

    def execute(self, argument):
        if argument:
            self.method(argument)
        else:
            self.method()
