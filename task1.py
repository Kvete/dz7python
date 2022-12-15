"""
Создать класс TrafficLight (светофор) и определить у него один атрибут
color (цвет) и метод running (запуск). Атрибут реализовать как приватный.
В рамках метода реализовать переключение светофора в режимы: красный, желтый,
зеленый. Продолжительность первого состояния (красный) составляет 7 секунд,
второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
Переключение между режимами должно осуществляться только в указанном порядке
(красный, желтый, зеленый). Проверить работу примера, создав экземпляр и
вызвав описанный метод.Задачу можно усложнить, реализовав проверку порядка
режимов, и при его нарушении выводить соответствующее
сообщение и завершать скрипт.
"""
from time import time


class TrafficLight:
    _color = "red"

    def running(self):
        for i in range(3):
            temp = time()
            TrafficLight._color = "red"
            while temp + 2 > time():
                print(TrafficLight._color)
            TrafficLight._color = "yelow"
            while temp + 4 > time():
                print(TrafficLight._color)
            TrafficLight._color = "green"
            while temp + 6 > time():
                print(TrafficLight._color)


a = TrafficLight()
a.running()
