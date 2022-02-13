# Функция как аттрибут класса
class Car:
    model = 'BMW'
    engine = '1.6'

    def drive():
        print('drive')


print(Car)
print(Car.__dict__)
print(Car.drive())
print(Car.drive)
print(getattr(Car, 'drive'))
print(getattr(Car, 'drive')())

a = Car()
print(a.__dict__)
print(a.drive)
# print(a.drive())



