# 2.2 Инициализация объекта. Метод init
# Метод нужен для инициализации

class Cat:
    # breed = 'pers'

    # def set_value(self, value, age=0):
        # self.name = value
        # self.age = age

    def __init__(self, name, breed='pers', age=1, color='white'):
        print('Hello new object id ', self, name, breed, age, color)
        self.name = name
        self.breed = breed
        self.age = age
        self.color = color


# bob = Cat()
# bob.set_value('Bob')
# print(bob.__dict__)
# print(Cat('Tom', 'siam', 40, 'black'))
# tom = Cat()
# jerry = Cat()
walt = Cat('Walt')
print(walt.__dict__)

kelly = Cat('Kelly', age=40)
print(kelly.__dict__)