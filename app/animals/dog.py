from .animal import Animal


class Dog(Animal):
    def __init__(self, name, age):
        super().__init__(name, age, "Dog")
        self.name = name
        self.age = age
        self.commands = ["play", "sit"]

    def play(self):
        state = False
        if state:
            return self.name, "already is playing", state
        else:
            state = True
            return self.name, "is playing", state

    def sit(self):
        state = False
        if state:
            return self.name, "already is sitting", state
        else:
            state = True
            return self.name, "is sitting", state
