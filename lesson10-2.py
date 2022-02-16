# объекты свойства (property)

class Point:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def __getCoordX(self):
        print('вызов __getCoordX')
        return self.__x

    def __setCoordX(self, x):
        print('вызов __setCoordX')
        self.__x = x

    coordX = property(__getCoordX, __setCoordX)


pt = Point(1, 2)
pt.coordX = 100

x = pt.coordX

