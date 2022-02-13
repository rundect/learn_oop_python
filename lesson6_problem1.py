# Создайте класс Laptop, у которого есть:
# конструктор __init__, принимающий 3 аргумента: бренд, модель и цену ноутбука.
# На основании этих аргументов нужно для экземпляра создать атрибуты brand, model, price и
# также атрибут laptop_name - строковое значение, вида "<brand> <model>"
# И затем создайте 2 экземпляра класса Laptop и сохраните их в переменные laptop1 и laptop2.


class Laptop:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
        self.laptop_name = f'{brand} {model}'


hp = Laptop('hp', '15-bw0xx', 57000)
print(hp.price)  # выводит 57000
print(hp.laptop_name)  # выводит "hp 15-bw0xx"

laptop1 = Laptop('Asus', '18-bdfx', 37000)
laptop2 = Laptop('Samsung', '13-bsdf0xx', 47000)
print(laptop1.price)
print(laptop1.laptop_name)
print(laptop2.price)
print(laptop2.laptop_name)
