"""
Реализовать класс Stationery (канцелярская принадлежность). Определить в нем
атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение
“Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш),
 Handle (маркер). В каждом из классов реализовать переопределение метода draw.
  Для каждого из классов метод должен выводить уникальное сообщение. Создать
экземпляры классов и проверить,
что выведет описанный метод для каждого экземпляра.
"""


class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print('запуск отрисовки карандашом')


class Pencil(Stationery):
    def draw(self):
        print('запуск отрисовки ручкой')


class Handle(Stationery):
    def draw(self):
        print('запуск отрисовки фломастером')


a = Pen('pen')
b = Pencil('pencil')
c = Handle('handle')
my_array = [a, b, c]
for el in my_array:
    el.draw()
