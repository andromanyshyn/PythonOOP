# Создайте класс Rectangle, у которого есть:
#
# конструктор __init__, принимающий 2 аргумента: длину и ширину.
# свойство area, которое возвращает площадь прямоугольника;
# r1 = Rectangle(3, 5)
# r2 = Rectangle(6, 1)
#
# print(r1.area) # 15
# print(r2.area) # 6


class Rectangle:

    def __init__(self, length, width):
        self.__length = length
        self.__width = width
        self.__area = None

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, value):
        self.__length = value
        self.__area = None

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value
        self.__area = None

    @property
    def area(self):
        if self.__area is None:
            self.__area = self.__length * self.__width
        return self.__area
