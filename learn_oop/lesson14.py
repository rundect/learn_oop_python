
# 2.10 Пространство имен класса
# методы находят имена только в глобальной области видимости
#  в методах можно обращаться к именам класса через self

class DepartmentIT:
    PYTHON_DEV = 4
    GO_DEV = 3
    REACT_DEV = 2

    def info(self):
        print(self.GO_DEV, self.PYTHON_DEV, self.REACT_DEV) # первый вариант через self

    def info2(self):
        print(DepartmentIT.REACT_DEV, DepartmentIT.PYTHON_DEV, DepartmentIT.GO_DEV) # второй вариант через сам класс

    # @property
    # def info_prop(self):
    #     print(self.GO_DEV, self.PYTHON_DEV, self.REACT_DEV)  # третий через декоратор property(свойства)
    #
    # @classmethod
    # def class_info(cls):
    #     print(cls.GO_DEV, cls.PYTHON_DEV, cls.REACT_DEV) # через дкоратор classmethod
    #
    # @staticmethod
    # def static_info():
    #     print(DepartmentIT.GO_DEV, DepartmentIT.PYTHON_DEV, DepartmentIT.REACT_DEV) # через декоратор staticmathod

    # def make_backend(self):
    #     print('Python and GO')
    #
    # def make_frontend(self):
    #     print('React')

    def hiring_py_dev(self):
        DepartmentIT.PYTHON_DEV = DepartmentIT.PYTHON_DEV + 1


it1 = DepartmentIT()
print(it1.PYTHON_DEV)
it1.hiring_py_dev()
print(it1.PYTHON_DEV)
print(DepartmentIT.PYTHON_DEV)
print(id(it1.PYTHON_DEV))
print(id(DepartmentIT.PYTHON_DEV))
print(it1.__dict__)

# it1.info()
# it1.info2()
# it1.info_prop
# it1.class_info()
# it1.static_info()







