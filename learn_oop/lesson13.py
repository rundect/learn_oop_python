# 2.9 Classmethod и staticmethod

# staticmethod - создаётся для того что бы можно было вызвать функцию и от класса и от экземпляра класса ток же
# он не привязывается ни классу ни к экземпляру класса
#  так же staticmethod можно использовать когда нам нужна функция но мы её хотим реализовать именно внутри класса а не
#  выносить её вне класса
# такие методы нужны когда мы ходим делать обработку не над экземпляром класса а над самим классом


class Example:

    def hello():
        print('hello')

    def instance_hello(self):
        print(f'instance_hello {self}')

    @staticmethod
    def static_hello():
        print('static_hello')

    @classmethod
    def class_hello(cls):
        print(f'instance_hello {cls}')


a = Example.hello()
print(a)
b = Example.instance_hello('d')
print(b)
c = Example.static_hello()
print(c)
d = Example.class_hello()
print(d)






