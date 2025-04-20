from .animal import Animal


class Hamster(Animal):
    def __init__(self, name, age):
        super().__init__(name, age, "Hamster")
        self.name = name
        self.age = age
        self.commands = ["stay", "turn around"]

    def stay(self):
        state = False
        if state:
            return self.name, "already is staying", state
        else:
            state = True
            return self.name, "is staying", state

    def turn_around(self):
        state = False
        if state:
            return self.name, "already was turn around", state
        else:
            state = True
            return self.name, "is turn around", state
