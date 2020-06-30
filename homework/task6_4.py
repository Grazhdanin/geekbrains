"""
Реализуйте базовый класс Car.
У данного класса должны быть следующие атрибуты:
speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать,
что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""

class Car:
    _car_type = 'Car'
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return print(f'{self.name} поехала')

    def stop(self):
        return print(f'{self.name} остановилась')

    def turn(self, direction):
        return print(f'{self.name} поворачивает на {direction}')

    def show_speed(self, show):
        return print(f'{self.name}  {show}')


class TownCar(Car):
    _car_type = 'Town'
    def show_speed(self, show):

        if show > 60:
             town = f'{self.name} превышение скорости {show}. Допустимое {60}'
        else:
             town = f'{self.name} скорость {show}'
        return print(town)
class SportCar(Car):
    _car_type = 'Sport'


class WorkCar(Car):
    _car_type = 'Work'
    def show_speed(self, show):

        if show > 40:
            work = f'{self.name} превышение скорости {show}. Допустимое {40}'
        else:
            work = f'{self.name} скорость {show}'

        return print(work)

class PoliceCar(Car):
    _car_type = 'Police'
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

mazda = SportCar(100, 'Черный', 'Mazda', False)
print(f"{mazda.name} {mazda.color} {mazda.speed} {mazda.is_police}")
mazda.go()
mazda.show_speed(105)
mazda.turn("На лево")
mazda.stop()
lada = TownCar(60, 'Серый', 'LADA', False)
print(f"{lada.name} {lada.color} {lada.speed} {lada.is_police}")
lada.go()
lada.show_speed(50)
lada.turn("На право")
lada.stop()
ford = WorkCar(70, 'Зеленый', 'Ford', False)
print(f"{ford.name} {ford.color} {ford.speed} {ford.is_police}")
ford.go()
ford.show_speed(60)
ford.turn("На лево")
ford.stop()
bmv = PoliceCar(110, 'Белый',  'bmv', True)
print(f"{bmv.name} {bmv.color} {bmv.speed} {bmv.is_police}")
bmv.go()
bmv.show_speed(110)
bmv.turn("На право")
bmv.stop()