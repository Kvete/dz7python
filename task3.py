"""
Реализовать базовый класс Worker (работник), в котором определить атрибуты:
name, surname, position (должность), income (доход). Последний атрибут должен
быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность)
на базе класса Worker. В классе Position реализовать методы получения полного
имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
Проверить работу примера на реальных данных(создать экземпляры класса Position,
 передать данные, проверить значения атрибутов, вызвать методы экземпляров).
"""


class Worker:
    def __init__(self, name, surname, position, _income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = _income


class Position(Worker):
    def get_full_name(self):
        print(self.name + " " + self.surname)

    def get_total_income(self):
        print(self._income["wage"] + self._income["bonus"])


print(
    '========================================================================='
    '=================================')
a = Position('ilia', 'kvete', 'student', {"wage": 1000, "bonus": 400})
print(a.__dict__)
a.get_full_name()
a.get_total_income()
print(
    '========================================================================='
    '=================================')
b = Position('alex', 'mordasow', 'worker', {"wage": 100000, "bonus": 20000})
print(b.__dict__)
b.get_full_name()
b.get_total_income()
print(
    '========================================================================='
    '=================================')
