from threading import Thread
from time import sleep


class Knight(Thread):

    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power
        

    def run(self):
        enemy = 100
        day = 0        
        while enemy != 0:
            if enemy==100:
                print(f'{self.name}, на нас напали!')
            enemy-=self.power
            day+=1            
            print(f'{self.name} сражается {day} день(дня)..., осталось {enemy} воинов.')
            sleep(1.0)
        print(f'{self.name} одержал победу спустя {day} дней(дня)!')



first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()