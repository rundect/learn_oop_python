# 1.3 Атрибуты экземпляра класса

class Car:
    model = 'BMW'
    engine = '1.6'


print(Car.__dict__)

a1 = Car()
a2 = Car()

print(a1.model)
print(a2.engine)
print(a1.__dict__)
print(a2.__dict__)

# Add attribute to exemplar of class
a1.seat = 4
print(a1.__dict__)
print(a2.__dict__)
print(Car.__dict__)

# Change attribute of exemplar of class
a1.model = 'Lada'
print(a1.model)
print(a2.model)
print(a1.engine)
# Имя переменной ищется сначала в пространстве имен экземпляра, потом класса

a2.size = 80
print(a2.size)
# print(a1.size)
# print(Car.size)

Car.size = 100
print(a2.size)
print(a1.size)
print(Car.size)
print(a1.__dict__)
print(a2.__dict__)
print(Car.__dict__)

a3 = Car()
print(a3.size)

print(dir(a3))
