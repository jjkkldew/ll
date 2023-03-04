import  random


class Student:
    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.alive =  True

    def is_alive(self):
          if self.progress <= -0.5:
              print('Cast out')
              self.alive = False
          elif self.gladness <= 0:
              print('Depresion......')
              self.alive = False
          elif self.progress > 5:
              print('Passed extrenally')
              self.alive = False

    def end_of_day(self):
        print(f'Glandless = {self.gladness}')
        print(f'Progress = {round(self.progress, 2)}')

    def Live(self, day):
        day = f'Day #{day} of {self.name} life!'
        print(f'{day:=^50}')
        cube = random.randint(1, 3)
        if cube == 1:
            self.to_study()
        elif cube == 2:
            self.to_chill()
        elif cube == 3:
            self.to_sleep()
        self.end_of_day()
        self.is_alive()

    def to_study(self):
        print('Time to study! ')
        self.progress += 0.12
        self.gladness -= 3

    def to_sleep(self):
        print('I will sleep! ')
        self.gladness += 3

    def to_chill(self):
        print('Rest time')
        self.gladness += 5
        self.progress -= 0.1


egor = Student('Egor')

for day in range(1, 366):
    if egor.alive:
        egor.Live(day)
    else:
        print('The end!')
        break
else:
    print('Game complete!')