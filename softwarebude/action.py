import inspect


class Action:
    def __init__(self, description, method):
        self.description = description
        self.method = method

    def execute(self, argument):
        number_of_function_parameters = len(inspect.signature(self.method).parameters)
        if number_of_function_parameters == 1:
            if argument:
                self.method(argument)
            else:
                print("This action needs another parameter")
        elif number_of_function_parameters == 0:
            if argument:
                print("This action needs no parameter")
            else:
                self.method()
