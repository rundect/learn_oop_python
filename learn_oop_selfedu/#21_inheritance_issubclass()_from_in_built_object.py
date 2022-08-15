
"""
Функция issubclass(). Наследование от встроенных типов и от object
https://proproprogs.ru/python_oop/python-funkciya-issubclass-nasledovanie-ot-vstroennyh-tipov-i-ot-object

Пользовательский класс по умолчанию автоматически наследуется от базового класса object языка Python.
"""


class Geom(object):
    pass


class Line(Geom):
    pass


l = Line()
print(l.__class__)

print(issubclass(Line, Geom))
print(issubclass(Geom, Line))
# print(issubclass(l, Geom))

print(isinstance(l, Geom))
print(isinstance(l, Line))
print(isinstance(l, object))


# -----------------Наследование от встроенных типов данных
"""
Интересный факт языка Python, что все стандартные типы данных являются классами
"""
print(issubclass(int, object))
print(issubclass(list, object))


class Vector(list):
    def __str__(self):
        return " ".join(map(str, self))


v = Vector([1, 2, 3])
print(v)
"""
Мы здесь переопределили магический метод __str__ для вывода списка в виде набора данных через пробел. 
Мало того, теперь тип данных нашего списка стал не list, а Vector
"""
print(type(v))


