# 4. Реализуйте базовый класс Car.
# ● у класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать,
# что машина поехала, остановилась, повернула (куда);
# ● опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# ● добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
# ● для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и
# 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат. Вызовите методы и покажите результат.


class Car:
    """Базовый класс машины"""
    def __init__(self, speed: int, color: str, name: str, is_police: bool = False):
        try:
            self.__speed = speed
            self.__color = color
            self.__name = name
            self.__is_police = is_police
        except BaseException as e:
            print('Ошибка инициализации класса', e)

    def speed(self) -> int:
        return self.__speed

    def color(self) -> str:
        return self.__color

    def name(self) -> str:
        return self.__name

    def isPolice(self) -> bool:
        return self.__is_police

    def go(self) -> None:
        print("Машина поехала")

    def stop(self) -> None:
        print("Машина остановилась")

    def turn(self, direction: str) -> None:
        print("Машина повернулась в {}".format(direction))

    def show_speed(self) -> None:
        print('Скорость = {}'.format(self.__speed))


class TowmCar(Car):
    """Городская машина"""
    def __init__(self, speed: int, color: str, name: str):
        super(TowmCar, self).__init__(speed, color, name)

    def show_speed(self) -> None:
        super().show_speed()
        if self.speed() > 60:
            print('\033[31m{}\033[37m'.format('!!! Превышение скорости !!!'))


class SportCar(Car):
    """Спортивная машина"""
    def __init__(self, speed: int, color: str, name: str):
        super(SportCar, self).__init__(speed, color, name)


class WorkCar(Car):
    """Рабочая машина"""
    def __init__(self, speed: int, color: str, name: str):
        super(WorkCar, self).__init__(speed, color, name)

    def show_speed(self) -> None:
        super().show_speed()
        if self.speed() > 40:
            print('\033[31m{}\033[37m'.format('!!! Превышение скорости !!!'))


class PoliceCar(Car):
    """Копы"""
    def __init__(self, speed: int, color: str, name: str):
        super(PoliceCar, self).__init__(speed, color, name, True)


def touch_car(car: Car):
    """Трогает все, что есть в машине"""
    print('--- {} ---'.format(car.name()))
    print('Скорость {}'.format(car.speed()))
    print('Цвет {}'.format(car.color()))
    print('Коп? {}'.format(car.isPolice()))
    car.go()
    car.show_speed()
    car.turn('Left')
    car.stop()


car_list = [TowmCar(80, 'green', 'Largus'), SportCar(200, 'red', 'Lamborgini'),
            WorkCar(50, 'brown', 'BobCat'), PoliceCar(110, 'white', 'Kia')]

for c in car_list:
    touch_car(c)

