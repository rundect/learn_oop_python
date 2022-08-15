
# 2.8 Вычисляемые свойства. Property

class Square:
    def __init__(self, s):
        self.__side = s
        self.__area = None
        self.__perimeter = None

    @property
    def side(self):
        return self.__side

    @side.setter
    def side(self, value):
        self.__side = value
        self.__area = None
        self.__perimeter = None

    @property
    def area(self):
        if self.__area is None:
            print('calculate area')
            self.__area = self.__side**2
        return self.__area

    @property
    def perimeter(self):
        if self.__perimeter is None:
            print('calculate perimeter')
            self.__perimeter = self.__side * 4
        return self.__perimeter


a = Square(5)
print(a.area)










