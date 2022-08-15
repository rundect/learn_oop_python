
# 3.1 Магические методы. Методы __str__ и __repr__

class Lion:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'The object Lion - {self.name}'

    def __str__(self):
        return f'Lion - {self.name}'


w = Lion('Vasya')
print(w)
print(str(w))



