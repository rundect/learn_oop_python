# 2.7 Декоратор Property

class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    def get_balance(self):
        print('get balance')
        return self.__balance

    def set_balance(self, value):
        print('set balance')
        if not isinstance(value, (int, float)):
            raise ValueError('Баланс должен быть числом')
        self.__balance = value

    def delete_balance(self):
        print('delete balance')
        del self.__balance

    balance = property(fget=get_balance,
                       fset=set_balance,
                       fdel=delete_balance)


# pt = BankAccount('John', 145)
# pt.balance = 100
# x = pt.balance
# y = pt.name
# print(x)
# print(y)
# del pt.balance
