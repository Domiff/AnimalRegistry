from .animal import Animal


class Donkey(Animal):
    def __init__(self, name, age):
        super().__init__(name, age, "Donkey")
        self.name = name
        self.age = age
        self.commands = ["jump", "kick"]

    def jump(self):
        state = False
        if state:
            return self.name, "already is jumping", state
        else:
            state = True
            return self.name, "is jumping", state

    def kick(self):
        state = False
        if state:
            return self.name, "already is kicking", state
        else:
            state = True
            return self.name, "is kicking", state
