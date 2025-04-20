from .animal import Animal


class Camel(Animal):
    def __init__(self, name, age):
        super().__init__(name, age, "Camel")
        self.name = name
        self.age = age
        self.commands = ["spit", "sit"]

    def spit(self):
        state = False
        if state:
            return self.name, "already is spiting", state
        else:
            state = True
            return self.name, "is spiting", state

    def sit(self):
        state = False
        if state:
            return self.name, "already sitting", state
        else:
            state = True
            return self.name, "is sitting", state
