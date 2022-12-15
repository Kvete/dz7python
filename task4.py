"""
Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
 speed, color, name, is_police (булево). А также методы: go, stop,
 turn(direction), которые должны сообщать, что машина поехала, остановилась,
 повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar,
 WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed, который должен
  показывать текущую скорость автомобиля. Для классов TownCar и WorkCar
  переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и
   40 (WorkCar) должно выводиться сообщение о превышении скорости.Создайте
   экземпляры классов, передайте значения атрибутов. Выполните доступ к
   атрибутам, выведите результат. Выполните вызов методов и также покажите
   результат.
"""


class Car:
    def __init__(self, speed, color, name, ispolice):
        self.speed = speed
        self.color = color
        self.name = name
        self.ispolice = ispolice

    def go(self):
        print(f"{self.name} поехала")

    def stop(self):
        print(f"{self.name} остановилась")

    def turn(self):
        print(f"{self.name} повернула")

    def show_speed(self):
        print(f'cкорость={self.speed}')


class Town(Car):
    def show_speed(self):
        if self.speed > 60:
            print('превышение скорости!')
        else:
            print(f'скорость={self.speed}')


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print('превышение скорости!')
        else:
            print(f'скорость={self.speed}')


class SportCar(Car):
    def show_speed(self):
        if self.speed < 120:
            print(f'вы едете слишком медленно! ваша скорость: {self.speed}')
        else:
            print(f'скорость={self.speed}')


class Police(Car):
    def show_speed(self):
        if self.ispolice:
            print(f'я мент-виу,виу,виу')
        else:
            print(f'вам не сюда')


print('====================================================================')
a = WorkCar(50, 'yellow', 'reno', False)
b = Town(45, 'green', 'lada', False)
c = SportCar(110, 'red', 'lamba', False)
m = Police(22, 'blew', 'uaz', True)
our_array = [a, b, c, m]
for el in our_array:
    print(el.__dict__)
    el.go()
    el.show_speed()
    print(
        '====================================================================')
