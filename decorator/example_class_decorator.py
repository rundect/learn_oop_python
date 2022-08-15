# https://tirinox.ru/class-decorator/

import time


# это вспомогательный декоратор будет декорировать каждый метод класса, см. ниже
def timeit(method):
    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()
        delta = (te - ts) * 1000
        print(f'{method.__name__} выполнялся {delta:2.2f} ms')
        return result
    return timed


def timeit_all_methods(cls):
    class NewCls:
        def __init__(self, *args, **kwargs):
            # проксируем полностью создание класса
            # как создали этот NewCls, также создадим и декорируемый класс
            self._obj = cls(*args, **kwargs)

        def __getattribute__(self, s):
            try:
                # папа, у меня есть атрибут s?
                x = super().__getattribute__(s)
            except AttributeError:
                # нет сынок, это не твой атрибут
                pass
            else:
                # да сынок, это твое
                return x

            # объект, значит у тебя должен быть атрибут s
            attr = self._obj.__getattribute__(s)

            # метод ли он?
            if isinstance(attr, type(self.__init__)):
                # да, обернуть его в измеритель времени
                return timeit(attr)
            else:
                # не метод, что-то другое
                return attr
    return NewCls


@timeit_all_methods
class Foo:
    def a(self):
        print("метод a начался")
        time.sleep(0.666)
        print("метод a кончился")


f = Foo()
f.a()

# метод a начался
# метод a кончился
# a 668.74 ms