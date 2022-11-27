#   Создайте класс Date, у которого есть:
#
# конструктор __init__, принимающий 3 аргумента: день, месяц и год.
# свойство date , которое возвращает строку определенного формата "<день>/<месяц>/<год>";
# свойство usa_date, которое возвращает строку определенного формата "<месяц>-<день>-<год>";

class Date:

    def __init__(self, day, month, year):
        self.__day = day
        self.__month = month
        self.__year = year

    @property
    def date(self):
        if self.__year < 1000:
            if self.__day < 10 and self.__month < 10:
                return f"0{self.__day}/0{self.__month}/{self.__year:04}"
            elif self.__day < 10:
                return f"0{self.__day}/{self.__month}/{self.__year:04}"
            elif self.__month < 10:
                return f"{self.__day}/0{self.__month}/{self.__year:04}"

        else:
            if self.__day < 10 and self.__month < 10:
                return f"0{self.__day}/0{self.__month}/{self.__year}"
            elif self.__day < 10:
                return f"0{self.__day}/{self.__month}/{self.__year}"
            elif self.__month < 10:
                return f"{self.__day}/0{self.__month}/{self.__year}"

    @property
    def usa_date(self):
        if self.__year < 1000:
            if self.__day < 10 and self.__month < 10:
                return f"0{self.__month}-0{self.__day}-{self.__year:04}"
            elif self.__day < 10:
                return f"{self.__month}-0{self.__day}-{self.__year:04}"
            elif self.__month < 10:
                return f"0{self.__month}-{self.__day}-{self.__year:04}"
        else:
            if self.__day < 10 and self.__month < 10:
                return f"0{self.__month}-0{self.__day}-{self.__year}"
            elif self.__day < 10:
                return f"{self.__month}-0{self.__day}-{self.__year}"
            elif self.__month < 10:
                return f"0{self.__month}-{self.__day}-{self.__year}"
