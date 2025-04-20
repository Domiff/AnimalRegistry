from counter import Counter
from animals.cat import Cat
from animals.dog import Dog
from animals.hamster import Hamster
from animals.camel import  Camel
from animals.donkey import Donkey
from animals.horse import Horse



def main():
    animals = []
    counter = Counter()

    while True:
        print("\nМеню:")
        print("1. Завести новое животное")
        print("2. Определить животное в правильный класс")
        print("3. Увидеть список команд, которое выполняет животное")
        print("4. Обучить животное новым командам")
        print("5. Выйти")

        choice = input("Выберите опцию: ")

        if choice == "1":
            with counter as c:
                name = input("Введите имя животного: ")
                age = int(input("Введите возраст животного: "))
                species = input("Введите вид животного (Dog, Cat, Hamster, Camel, Horse, Donkey): ").lower()
                if species == "Dog".lower():
                    animal = Dog(name, age)
                elif species == "Cat".lower():
                    animal = Cat(name, age)
                elif species == "Hamster".lower():
                    animal = Hamster(name, age)
                elif species == "Camel".lower():
                    animal = Camel(name, age)
                elif species == "Horse".lower():
                    animal = Horse(name, age)
                elif species == "Donkey".lower():
                    animal = Donkey(name, age)

                else:
                    print("Неизвестный вид животного")
                    continue
                animals.append(animal)
                c.add()
                print(f"Животное {name} добавлено в реестр.")

        elif choice == "2":
            name = input("Введите имя животного: ")
            for animal in animals:
                if animal.name == name:
                    print(f"{name} является {animal.species}")
                    break
            else:
                print("Животное не найдено")

        elif choice == "3":
            name = input("Введите имя животного: ")
            for animal in animals:
                if animal.name == name:
                    commands = animal.show_commands()
                    if commands:
                        print(f"Команды, которые выполняет {name}: {', '.join(commands)}")
                    else:
                        print(f"{name} не знает команд")
                    break
            else:
                print("Животное не найдено")

        elif choice == "4":
            name = input("Введите имя животного: ")
            for animal in animals:
                if animal.name == name:
                    command = input("Введите новую команду: ")
                    animal.add_command(command)
                    print(f"Команда '{command}' добавлена для {name}")
                    break
            else:
                print("Животное не найдено")

        elif choice == "5":
            counter.close()
            break

        else:
            print("Неверная опция, попробуйте снова")

if __name__ == "__main__":
    main()
