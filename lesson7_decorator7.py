
# Декорирование методов

# Один из важных фактов, которые следует понимать, заключается в том, что функции и методы в Python'e — это
# практически одно и то же, за исключением того, что методы всегда ожидают первым параметром ссылку на сам
# объект (self). Это значит, что мы можем создавать декораторы для методов так же, как и для функций, просто
# не забывая про self.

def method_friendly_decorator(method_to_decorate):
    def wrapper(self, lie):
        lie = lie - 3  # действительно, дружелюбно - снизим возраст ещё сильней :-)
        return method_to_decorate(self, lie)
    return wrapper


class Lucy(object):

    def __init__(self):
        self.age = 32

    @method_friendly_decorator
    def sayYourAge(self, lie):
        print(lie)
        print("Мне %s, а ты бы сколько дал?" % (self.age + lie))


l = Lucy()
l.sayYourAge(-3)
# выведет: Мне 26, а ты бы сколько дал?