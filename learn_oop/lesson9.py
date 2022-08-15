#  2.5 Публичные, приватные, защищенные атрибуты и методы
# что бы создать защищённый атрибут мы должны перед именем поставить одно нижнее подчёркивание
# что бы создать приватный атрибут мы должны перед именем поставить два нижних подчёркивания
# при помощи метода print_private_data происходит сокрытие обработки защищённых атрибутов
# или же этот метод называется инкапсуляция
# метод тоже может быть приватный и он тоже должен начинаться с двух подчёркиваний

# Итог: Инкапсуляция - механизм языка, позволяющий объединить данные и методы, работающие с этими данными,
# в единый объект и скрыть детали реализации от пользователя

class BankAccount:
    def __init__(self, name, balance, passport):
        self.__name = name
        self.__balance = balance
        self.__passport = passport

    def print_public_data(self):
        # print(self.name, self.balance, self.passport)
        self.__print_private_data()
    # def print_protected_data(self):
        # print(self._name, self._balance, self._passport)

    def __print_private_data(self):
        print(self.__name, self.__balance, self.__passport)


account1 = BankAccount('Bob', 100000, 45484564654)
# account1.print_public_data()
# print(account1.__name)
# print(account1.__balance)
# print(account1.__passport)

print(dir(account1))
account1._BankAccount__print_private_data()
print(account1._BankAccount__balance)



