
class Student:
    count_of_students = 0

    def say_hi(self):
        print(f'Hi! I`m {self.name}')

    def __init__(self, name, height):
        self.name = name
        self.height = height
        Student.count_of_students += 1

    def __del__(self):
        print('Bye! ')

    def __str__(self):
        return f'I`m student: {self.name}'

sergiy = Student('Sergiy', 180)
anton = Student('Anton', 160)

sergiy.say_hi()
anton.say_hi()

print(sergiy.height)
print(anton.height)
print(Student.count_of_students)