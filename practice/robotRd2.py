class Robot:
    def set_name(self, name):
        self.name = name

    def say_hello(self):
        if hasattr(self, "name"):
            print("Hello, human! My name is " + self.name)
        else:
            print("У робота нет имени")

    def say_bye(self):
        print("See u later alligator")