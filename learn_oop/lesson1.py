# 1.1 Классы, объекты, экземпляры классов

l = [4, 5, 34]

# string
s = 'ggfd'

print(type(s))
print(isinstance(s, list))

# All values are objects
print(isinstance(s, object))

# Class type
print(type(int))


# Класс - шаблон для создания объектов
class Car:
    model = 'BMW'
    engine = '1.6'

print(Car)

# Каждый при вызове класса возвращает экземпляр класса
a = Car()
print(type(a))
print(isinstance(s, object))

c = Car()