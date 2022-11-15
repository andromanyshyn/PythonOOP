#  Создайте класс Student, у которого есть:
#
# конструктор __init__, принимающий 3 аргумента и создает приватные атрибуты __name, __age, __branch;
# приватный метод __display_details , который выводит на экран информацию о студенте в следующем виде
# Имя: <name>
# Возраст: <age>
# Направление: <branch>
# метод access_private_method, который вызывает приватный метод __display_details

class Student:

    def __init__(self, name, age, branch):
        self.__name = name
        self.__age = age
        self.__branch = branch

    def __display_details(self):
        print(f'Имя: {self.__name}\n'
              f'Возраст: {self.__age}\n'
              f'Направление: {self.__branch}')

    def access_private_method(self):
        self.__display_details()

