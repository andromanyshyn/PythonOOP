# У нас уже имеется с предыдущего урока класс Registration. Давайте добавим в него следующее:
#
# в метод  __init__ добавляется еще один аргумент: пароль. Как в примере с логином, вы должны будете сохранить переданный пароль через password через сеттер  password (см пункт 3 в этом задании). Примерный код метода __init__
# def __init__(self, логин, пароль):
#     self.login = логин # передаем в сеттер login значение логин
#     self.password = пароль # передаем в сеттер password значение пароль
# Должны сработать свойства сеттер login из предыдущего задания  и сеттер password из пункта 3 для проверки валидности переданных значений
#
# Свойство геттер password, которое возвращает значение self.__password;
# Свойство сеттер password, принимает значение нового пароля. Его необходимо перед сохранением проверить на следующее:
# новое значение пароля должно быть строкой(не список, словарь и т.д. ) в противном случае вызываем исключение TypeError("Пароль должен быть строкой")
# Длина нового пароля должна быть от 5 до 11 символов, в противном случае вызывать исключение ValueError('Пароль должен быть длиннее 4 и меньше 12 символов')
# Новый пароль должен содержать хотя бы одну цифру.
# Для этого создаем staticmethod is_include_digit , который проходит по всем элементам строки и проверяет наличие цифр. В случае отсутствия цифрового символа вызываем исключение: ValueError('Пароль должен содержать хотя бы одну цифру')
# Строка password должна содержать элементы верхнего и нижнего регистра.
# Создаем staticmethod is_include_all_register, который с помощью цикла проверяет элемента строчки на регистр. В случае ошибки вызываем: ValueError('Пароль должен содержать хотя бы один символ верхнего и нижнего регистра')
# Строка password помимо цифр должна содержать только латинские символы.
# Для этого создайте staticmethod is_include_only_latin , который проверяет каждый элемент нового значения на принадлежность к латинскому алфавиту(проверка должна быть как в верхнем, так и нижнем регистре).
# В случае, если встретится нелатинский символ, вызвать ошибку ValueError('Пароль должен содержать только латинский алфавит'). Подсказка: из модуля string можно импортировать переменную ascii_letters, она хранит в себе все латинские символы в верхнем и нижнем регистре
# Пароль не должен совпадать ни с одним из легких паролей, хранящихся в файле easy_passwords.txt. Сохраните данный файл к себе в папку с вашей программой и не меняйте название. С помощью staticmethod создаем метод check_password_dictionary и проверяем наличие нашего пароля в данном файле. Если значение совпадет со значением из файла, то в сеттер вызываем исключение:
# ValueError('Ваш пароль содержится в списке самых легких')


from string import digits
from string import ascii_lowercase
from string import ascii_uppercase
from string import ascii_letters


class Registration:

    def __init__(self, login, password):
        self.login = login
        self.password = password

    @staticmethod
    def check_password_dictionary(password):
        password = password + "\n"
        with open("easy_passwords.txt") as file:
            if password in file:
                return True
            else:
                return False

    @staticmethod
    def is_include_only_latin(password):
        for i in ascii_letters:
            if i in password:
                return True
        return False

    @staticmethod
    def is_include_all_register(password):
        alphabet = ascii_uppercase + ascii_lowercase
        for i in alphabet:
            if i in password:
                return True
        return False

    @staticmethod
    def is_include_digit(password):
        for digit in digits:
            if digit in password:
                return True
        return False

    @property
    def password(self):
        return self.__pasword

    @password.setter
    def password(self, value):
        if type(value) is not str:
            raise TypeError("Пароль должен быть строкой")
        if len(value) < 5 or len(value) > 11:
            raise ValueError('Пароль должен быть длиннее 4 и меньше 12 символов')
        if not Registration.is_include_digit(value):
            raise ValueError('Пароль должен содержать хотя бы одну цифру')
        if not Registration.is_include_all_register(value):
            raise ValueError('Пароль должен содержать хотя бы один символ верхнего и нижнего регистра')
        if not Registration.is_include_only_latin(value):
            raise ValueError('Пароль должен содержать только латинский алфавит')
        if Registration.check_password_dictionary(value) is True:
            raise ValueError('Ваш пароль содержится в списке самых легких')
        self.__pasword = value

    @property
    def login(self):
        return self.__login

    @login.setter
    def login(self, value):
        if type(value) is not str:
            raise TypeError("Wrong data type")
        if value.count("@") == 0 or value.count("@") > 1:
            raise ValueError("Логин должен содержать один символ '@'")
        if value.count(".") == 0:
            raise ValueError("Логин должен содержать символ '.'")
        if value.index(".") < value.index("@"):
            raise ValueError
        self.__login = value