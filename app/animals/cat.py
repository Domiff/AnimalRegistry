from .animal import Animal


class Cat(Animal):
    def __init__(self, name, age):
        super().__init__(name, age, "Cat")
        self.name = name
        self.age = age
        self.commands = ["play", "voice"]

    def play(self):
        state = False
        if state:
            return self.name, "already is playing", state
        else:
            state = True
            return self.name, "is playing", state

    def voice(self):
        state = False
        if state:
            return self.name, "already do voice", state
        else:
            state = True
            return self.name, "do voice",state
