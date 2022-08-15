# https://tirinox.ru/class-decorator/

from functools import wraps


class Repeater:
    def __init__(self, n):
        self.n = n

    def __call__(self, f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            for _ in range(self.n):
                f(*args, **kwargs)
        return wrapper


@Repeater(3)
def foo():
    print('foo')


foo()
# foo
# foo
# foo