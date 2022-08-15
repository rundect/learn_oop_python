# 2.4 Моносостояние для экземпляров класса

class Cat:
    breed = 'pers'
    __shared_attr = {'breed': 'pers', 'color': 'black'}

    def __init__(self):
        self.__dict__ = Cat.__shared_attr


# a = Cat()
# b = Cat()
# a.breed = 'siam'
# b.color = 'black'
# print(a.__dict__)
# print(b.__dict__)

d = Cat()
g = Cat()
d.breed = 'siam'
d.name = 'Bob'
h = Cat()

print(h.__dict__)

