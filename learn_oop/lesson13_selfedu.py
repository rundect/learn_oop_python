
# ООП Python 3 #13: методы класса - @classmethod и статические методы - @staticmethod

class Vector:
    MIN_COORD = 0
    MAX_COORD = 100

    def setCoords(self, x, y):
        if Vector.validate(x) and Vector.validate(y):
            self.x = x
            self.y = y

    @classmethod
    def validate(cls, arg):
        if cls.MIN_COORD <= arg <= cls.MAX_COORD:
            return True
        return False

    @staticmethod
    def norm2(x, y):
        return x * x + y * y


print(Vector.validate(500))
print(Vector.norm2(1, 2))
# Vector.setCoords(1, 2)

v = Vector()
v.setCoords(1, 2)
print(Vector.setCoords(v, 1, 2))


















