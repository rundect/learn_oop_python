
# 16. ООП Python 3: магические методы __str__, __repr__, __len__, __abs__

class Cat:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"{self.__class__}: {self.name}"

    def __str__(self):
        return f"{self.name}"


cat = Cat('Васька')
print(cat)


class Point:
    def __init__(self, *args):
        self.__coords = args

    def __len__(self):
        return len(self.__coords)

    def __abs__(self):
        return list(map(abs, self.__coords))


p = Point(1, -2, -5)
print(len(p))
print(abs(p))

