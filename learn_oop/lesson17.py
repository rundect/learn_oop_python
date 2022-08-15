# __add__, __mul__, __sub__, __truediv__

class BankAccount:
    def __init__(self, name, balance):
        print('new object init')
        self.name = name
        self.balance = balance

    def __repr__(self):
        return f"Клиент {self.name} с балансом {self.balance}"

    def __add__(self, other):
        print('__add__ call')
        if isinstance(other, BankAccount):
            return self.balance + other.balance
        if isinstance(other, (int, float)):
            return BankAccount(self.name, self.balance + other)  # self.balance + other
        raise NotImplemented

    # def __mul__(self, other):
    #     print('__add__ call')
    #     if isinstance(other, BankAccount):
    #         return self.balance * other.balance
    #     if isinstance(other, (int, float)):
    #         return self.balance * other
    #     if isinstance(other, str):
    #         return self.name + other
    #     raise NotImplemented
    #
    # def __radd__(self, other):
    #     print('__radd call')
    #     return self + other


b = BankAccount('ivan', 900)
# print(id(b))
# d = b+30
# print(id(d), d)
# print(b.balance + 400)
# print(b.balance)
# print(b + 300.0)
#
r = BankAccount('Tany', 0.500)
print(b+r)
# print(12+r)
#
# print(r*3)
# print(r*'ttt')
