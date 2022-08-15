# Создайте класс Zebra, внутри которого есть метод which_stripe,
# который поочередно печатает фразы "Полоска белая", "Полоска черная", начиная именно с фразы "Полоска белая"

class Zebra:
    def __init__(self):
        self.increment = 0

    def which_stripe(self):
        if self.increment == 0:
            print("Полоска белая")
            self.increment += 1
        else:
            print("Полоска черная")
            self.increment -= 1


z1 = Zebra()
z1.which_stripe() # печатает "Полоска белая"
z1.which_stripe() # печатает "Полоска черная"
z1.which_stripe() # печатает "Полоска белая"

z2 = Zebra()
z2.which_stripe() # печатает "Полоска белая"

