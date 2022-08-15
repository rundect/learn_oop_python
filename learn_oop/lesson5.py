# 2.1 Методы экземпляра. Аргумент self

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __del__(self):
        print(f'Exemplar {self.__str__()} was deleted')
    x = 1
    y = 1

    def setCoords(self, x, y):
        self.x = x
        self.y = y


pt = Point()
pt2 = Point(5)
pt3 = Point(5, 10)
print(pt.__dict__, pt2.__dict__, pt3.__dict__, sep='\n')
