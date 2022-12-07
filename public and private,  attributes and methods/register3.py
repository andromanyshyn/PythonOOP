# Создайте класс  File, у которого есть:
#
# метод __init__, который должен принимать на вход имя файла и записывать его в атрибут name. Также необходимо создать атрибуты in_trash , is_deleted  и записать в них значение False
# метод  restore_from_trash, который печатает фразу «Файл {name} восстановлен из корзины» и проставляет атрибут in_trash в значение False
# метод  remove, который печатает фразу «Файл {name} был удален» и проставляет атрибут is_deleted  в значение True
# метод read, который
# печатает фразу «ErrorReadFileDeleted({name})», если атрибут is_deleted истин, и выходит из метода
# печатает фразу «ErrorReadFileTrashed({name})», если атрибут in_trash истин, и выходит из метода
# печатает фразу «Прочитали все содержимое файла {self.name}» если файл не удален и не в корзине
# метод write, который принимает значение content для записи и
# печатает фразу «ErrorWriteFileDeleted({name})», если атрибут is_deleted истин, и выходит из метода
# печатает фразу «ErrorWriteFileTrashed({name})», если атрибут in_trash истин, и выходит из метода
# печатает фразу «Записали значение {content} в файл {self.name}», если файл не удален и не в корзине


class File:

    def __init__(self, name):
        self.name = name
        self.in_trash = False
        self.is_deleted = False

    def restore_from_trash(self):
        print(f"Файл {self.name} восстановлен из корзины")
        self.in_trash = False

    def remove(self):
        print(f"Файл {self.name} был удален")
        self.is_deleted = True

    def read(self):
        if self.in_trash is False and self.is_deleted is False:
            print(f"Прочитали все содержимое файла {self.name}")
        if self.is_deleted is True:
            print(f"ErrorReadFileDeleted({self.name})")
            if self.in_trash is True:
                print(f"ErrorReadFileTrashed({self.name})")
        if self.in_trash is True:
            print(f"ErrorReadFileTrashed({self.name})")
            if self.is_deleted is True:
                print(f"ErrorReadFileDeleted({self.name})")

    def write(self, content):
        if self.in_trash is False and self.is_deleted is False:
            print(f"Записали значение {content} в файл {self.name}")
        if self.is_deleted is True:
            print(f"ErrorWriteFileDeleted({self.name})")
            if self.in_trash is True:
                print(f"ErrorWriteFileTrashed({self.name})")
        if self.in_trash is True:
            print(f"ErrorWriteFileTrashed({self.name})")
            if self.is_deleted is True:
                print(f"ErrorWriteFileDeleted({self.name})")
