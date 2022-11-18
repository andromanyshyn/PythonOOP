# Создайте класс UserMail, у которого есть:
#
# конструктор __init__, принимающий 2 аргумента: логин и почтовый адрес.
# Их необходимо сохранить в экземпляр как атрибуты login и __email
# (обратите внимание, защищенный атрибут)
# метод геттер get_email, который возвращает защищенный атрибут __email ;
# метод сеттер set_email, который принимает в виде строки новую почту. Метод должен проверять,
# что в новой почте есть только один символ @ и после нее есть точка.
# Если данные условия выполняются, новая почта сохраняется в атрибут __email,
# в противном случае выведите сообщение "ErrorMail:<почта>";
# создайте свойство email, у которого геттером будет метод get_email, а сеттером - метод set_email

class UserMail:

    def __init__(self, login, email):
        self.login = login
        self.__email = email

    def get_email(self):
        return self.__email

    def set_email(self, value):
        if type(value) != str:
            print(f"ErrorMail:{value}")
        else:
            if value.count("@") == 1 and "." in value and value.index(".") > value.index("@"):
                self.__email = value
            else:
                print(f"ErrorMail:{value}")

    email = property(fget=get_email, fset=set_email)
