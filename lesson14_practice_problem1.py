
from string import ascii_uppercase, ascii_letters

# Давайте создадим класс Registration, который поможет зарегистрировать пользователя с безопасным паролем

class Registration:
    DIGITS = '1234567890'

    # В классе Registration необходимо реализовать
    # Конструктор __init__ принимающий 2 аргумента (login, password). В конструкторе вы сохраняете переданные login и
    # password через сеттеры (см пункт 3 и пункт 5). То есть когда отработает данный код
    def __init__(self, login, password):
        self.login = login  # передаем в сеттер login значение логин
        self.password = password  # передаем в сеттер password значение пароль
        # должны сработать свойства сеттер login из пункта 3 и сеттер password из пункта 5 для проверки валидности
        # переданных значений

    # Cвойство геттер login, которое возвращает значение self.__login;
    @property
    def login(self):
        return self.__login

    # Свойство сеттер login, принимает значение емайла в случае если:
    @login.setter
    def login(self, login):
        self.verify_login(login)
        self.__login = login

    @classmethod
    def verify_login(cls, email):
        # майл(login) содержит хотя бы 1 символ "@". В случае ошибки выводим ValueError("Login must include at least
        # one ' @ '")
        if "@" not in email:
            raise ValueError("Login must include at least one ' @ '")
        # Email(login) содержит хотя бы 1 символ " . ".В случае ошибки выводим ValueError("Login must include at least
        # one ' . '")
        if "." not in email:
            raise ValueError("Login must include at least one ' . '")
        # Если значение проходит проверку новое значение логина сохраняется в атрибут (self.__login)

    # Свойство геттер password, которое возвращает значение self.__password;
    @property
    def password(self):
        return self.__password

    # Свойство сеттер password, принимает значение пароля в случае если:
    @password.setter
    def password(self, password):
        self.verify_password(password)
        self.__password = password

    @classmethod
    def verify_password(cls, password):
        # Password является строкой(не список, словарь и т.д.) в противном случае вызываем исключение
        # TypeError("Пароль должен быть строкой")
        if type(password) != str:
            raise TypeError("Пароль должен быть строкой")

        # Длина password должна быть от 5 до 11 символов, в противном случае вызывать исключение
        # ValueError('Пароль должен быть длиннее 4 и меньше 12 символов')
        if 5 > len(password) > 11:
            raise ValueError('Пароль должен быть длиннее 4 и меньше 12 символов')

        # Должен содержать хотя бы одну цифру. Для этого нужно в staticmethod создать функцию is_include_digit которая,
        # которая проходит по всем элементам строки и проверяет их наличие в digits. В случае ошибки выводим:
        # ValueError('Пароль должен содержать хотя бы одну цифру')
        increment_for_digits = 0
        for i in password:
            if i in cls.DIGITS:
                increment_for_digits += 1
        if increment_for_digits < 1:
            raise ValueError('Пароль должен содержать хотя бы одну цифру')

        # Строка password должна содержать элементы верхнего и нижнего регистра. В staticmethod создаем метод
        # (is_include_all_register), который с помощью цикла проверяет элемента строчки на регистр. В случае ошибки
        # выводит:
        # ValueError('Пароль должен содержать хотя бы 2 заглавные буквы')
        increment = 0
        for i in password:
            if i in ascii_uppercase:
                increment += 1
        if increment < 2:
            raise ValueError('Пароль должен содержать хотя бы 2 заглавные буквы')

        # Строка password должна содержать только латинские символы. Импортируем библиотеку string, в staticmethod
        # создаем метод(is_include_only_latin), которым проверяем, каждый элемент на наличие в string(проверка должна
        # быть как в верхнем, так и нижнем регистре). В случае ошибки
        # ValueError('Пароль должен содержать только латинский алфавит')

        for i in password:
            if i not in ascii_letters + cls.DIGITS:
                raise ValueError('Пароль должен содержать только латинский алфавит')

        # Пароль не должен совпадать ни с одним из легких паролей, хранящихся в файле easy_passwords.txt. Сохраните
        # данный файл к себе в папку с вашей программой. С помощью staticmethod создаем метод
        # check_password_dictionary и проверяем наличие нашего пароля в данном файле. Если значение совпадет со
        # значением из файла, то в сеттер добавляем исключение и выводим ошибку:
        # ValueError('Ваш пароль содержится в списке самых легких')
        with open('easy_password.txt', encoding='utf-8') as file:
            for i in file:
                if i.strip() == password:
                    raise ValueError('Ваш пароль содержится в списке самых легких')


a = Registration('login@gmail.com', 'paUYssword12')
print(a.__dict__)
s2 = Registration("translate@gmail.com", "as1SNdf")
