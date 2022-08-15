# https://tirinox.ru/class-decorator/

class Functor:
    def __call__(self, a, b):
        print(a * b)


f = Functor()
# вызов как будто функция
f(10, 20)
