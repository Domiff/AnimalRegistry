from .animal import Animal


class Horse(Animal):
    def __init__(self, name, age):
        super().__init__(name, age, "Horse")
        self.name = name
        self.age = age
        self.commands = ["voice", "rush"]

    def voice(self):
        state = False
        if state:
            return self.name, "already do voice", state
        else:
            state = True
            return self.name, "do voice", state

    def rush(self):
        state = False
        if state:
            return self.name, "already is rush", state
        else:
            state = True
            return self.name, "is rush", state
