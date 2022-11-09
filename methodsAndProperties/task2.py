class Worker:
    def __init__(self, name, salary, gender, passport):
        self.name = name
        self.salary = salary
        self.gender = gender
        self.passport = passport

    def get_info(self):
        print(f"Worker {self.name}; passport-{self.passport}")


object_one = Worker('Allison Hill', 334053, 'M', '1635644202')
object_two = Worker('Megan Mcclain', 191161, 'F', '2101101595')
object_three = Worker('Brandon Hall', 731262, 'M', '6054749119')
object_four = Worker('Michelle Miles', 539898, 'M', '1355368461')
object_five = Worker('Donald Booth', 895667, 'M', '7736670978')
object_six = Worker('Gina Moore', 900581, 'F', '7018476624')
object_seven = Worker('James Howard', 460663, 'F', '5461900982')
object_eight = Worker('Monica Herrera', 496922, 'M', '2955495768')
object_nine = Worker('Sandra Montgomery', 479201, 'M', '5111859731')
object_ten = Worker('Amber Perez', 403445, 'M', '0602870126')

worker_objects = []

worker_objects.append(object_one)
worker_objects.append(object_two)
worker_objects.append(object_three)
worker_objects.append(object_four)
worker_objects.append(object_five)
worker_objects.append(object_six)
worker_objects.append(object_seven)
worker_objects.append(object_eight)
worker_objects.append(object_nine)
worker_objects.append(object_ten)

for i in worker_objects:
    i.get_info()

persons = [
    ('Allison Hill', 334053, 'M', '1635644202'),
    ('Megan Mcclain', 191161, 'F', '2101101595'),
    ('Brandon Hall', 731262, 'M', '6054749119'),
    ('Michelle Miles', 539898, 'M', '1355368461'),
    ('Donald Booth', 895667, 'M', '7736670978'),
    ('Gina Moore', 900581, 'F', '7018476624'),
    ('James Howard', 460663, 'F', '5461900982'),
    ('Monica Herrera', 496922, 'M', '2955495768'),
    ('Sandra Montgomery', 479201, 'M', '5111859731'),
    ('Amber Perez', 403445, 'M', '0602870126')
]
