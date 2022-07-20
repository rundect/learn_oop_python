
"""
Методы классов. Параметр self
https://proproprogs.ru/python_oop/metody-klassov-parametr-self
"""


class Point:
    color = 'red'
    circle = 2

    def set_coords(self, x, y):
        self.x = x
        self.y = y

    def get_coords(self):
        return (self.x, self.y)


# Point.set_coords()  #не можем вызвать данный метод через класс без указания первого аргумента
pt = Point()
# pt.set_coords()
pt.set_coords(1, 2)
print(pt.__dict__)

pt2 = Point()
pt2.set_coords(10, 20)
print(pt2.__dict__)

print(pt.get_coords())

res = getattr(pt, 'get_coords')
print(res)
print(res())
