class Animal:
    def __init__(self, name, age, species):
        self.name = name
        self.age = age
        self.species = species
        self.commands = []

    def add_command(self, command):
        self.commands.append(command)

    def show_commands(self):
        return self.commands
