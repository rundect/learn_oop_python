# 2.6 Геттеры и сеттеры, property атрибуты
# ООП Python 3 #3: режимы доступа - public, private, protected. Геттеры и сеттеры
# <attribute name> - public
# _<attribute name> - protected
# __<attribute name> - private

class Point:
    WIDTH = 5

    # Разрешенные свойства экземпляров класса
    __slots__ = ['__x', '__y']

    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    # Приватный метод
    def __checkValue(x):
        if isinstance(x, int) or isinstance(x, float):
            return True
        return False

    # Сеттер
    def setCoords(self, x, y):
        if Point.__checkValue(x) and Point.__checkValue(y):
            self.__x = x
            self.__y = y
        else:
            print('Координаты должны быть числами')

    # Геттер
    def getCoords(self):
        return self.__x, self.__y

    # Перегрузка метода __getattribute__(self, item) автоматически вызывается при получении свойства класса с
    # именем item
    def __getattribute__(self, item):
        if item == '_Point__x':
            return 'Частная переменная'
        else:
            return object.__getattribute__(self, item)

    # Перегрузка метода __setattr__(self, key, value) автоматически вызывается при изменении свойства item
    def __setattr__(self, key, value):
        if key == 'WIDTH':
            raise AttributeError
        else:
            self.__dict__[key] = value

    # Перегрузка метода __getattr__(self, item) автоматически вызывается при получении несуществующего свойства
    # item класса
    def __getattr__(self, item):
        print('__getattr__: ' + item)

    # Перегрузка метода __delattr__(self, item) автоматически вызывается при удалении несуществующего свойства
    # item класса
    def __delattr__(self, item):
        print('__delattr__: ' + item)

pt = Point(1, 2)
print(pt.getCoords())
# pt.setCoords('10', 20)
# print(pt.getCoords())

print(pt._Point__x)
# print(Point._Point__checkValue(4))

pt.WIDTH = 5


