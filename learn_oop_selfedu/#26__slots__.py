import timeit

"""
Коллекция __slots__
https://proproprogs.ru/python_oop/python-kollekciya-slots

-3-
Вот такие три особенности дает коллекция __slots__ экземплярам класса:
ограничение создаваемых локальных свойств;
уменьшение занимаемой памяти;
ускорение работы с локальными свойствами. 
"""


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def calc(self):
        self.x += 1
        del self.y
        self.y = 0


"""
-2-
Коллекция __slots__ ускоряет работу с локальными свойствами экземпляров класса. Например, если добавить в 
каждый класс метод def calc(), замерить скорость его работы, то мы увидим, что t1 больше, чем t2, то есть, 
класс Point2D работает быстрее с локальными свойствами, чем класс Point. 
"""


class Point2D:
    """
    -0-
    Мы хотим объявить класс точки на плоскости, чтобы у его экземпляров были только два свойства x и y
    и никакие другие. Как это сделать? Для этого, как раз и применяется коллекция __slots__. В кортеже перечисляем
    атрибуты с именами x и y (указываются в виде строки) и только такие локальные свойства могут существовать в
    экземплярах этого класса
    """
    __slots__ = ('x', 'y')
    MAX_COORD = 100

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def calc(self):
        self.x += 1
        del self.y
        self.y = 0


pt = Point(1, 2)
print(pt.x)
pt.y = 100
pt.z = 4
print(pt.__dict__)

pt2 = Point2D(10, 20)
print(pt2.x)
print(pt2.y)
# print(pt2.__dict__)  # AttributeError: 'Point2D' object has no attribute '__dict__'
# pt2.z = 30  # AttributeError: 'Point2D' object has no attribute 'z'
print(pt2.__slots__)
pt2.x = 50
del pt2.y
pt2.y = 100

"""
-1-
Коллекция __slots__ помимо ограничения создаваемых локальных свойств, еще уменьшает объем памяти, 
занимаемый экземпляром класса. Смотрите, если создать  два экземпляра, то первый будет содержать ссылку, 
как на объект класса, так и на коллекцию __dict__. А второй – только на пространство имен класса Point2D
"""
print(pt.__sizeof__(), pt.__dict__.__sizeof__())
print(pt2.__sizeof__())

t1 = timeit.timeit(pt.calc)
t2 = timeit.timeit(pt2.calc)
print(t1, t2)



