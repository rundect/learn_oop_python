# Создайте класс Dog, у которого есть:
class Dog:
    # конструктор __init__, принимающий 2 аргумента: name, age.
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # метод description, который возвращает строку в виде "<name> is <age> years old"
    def description(self):
        return f'{self.name} is {self.age} years old'

    # метод speak принимающий один аргумент, который возвращает строку вида "<name> says <sound>";
    def speak(self, sound):
        return f'{self.name} says {sound}'


jack = Dog("Jack", 4)

print(jack.description()) # распечатает 'Jack is 4 years old'
print(jack.speak("Woof Woof")) # распечатает 'Jack says Woof Woof'
print(jack.speak("Bow Wow")) # распечатает 'Jack says Bow Wow'
