# 1. Создать класс TrafficLight (светофор).
# ● определить у него один атрибут color (цвет) и метод running (запуск);
# ● атрибут реализовать как приватный;
# ● в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
# ● продолжительность первого состояния
# (красный) составляет 7 секунд, второго (жёлтый) — 2 секунды, третьего (зелёный) — на ваше усмотрение;#
# ● переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
# ● проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов.
# При его нарушении выводить соответствующее сообщение и завершать скрипт.
from threading import Timer


class TrafficLight:
    def __init__(self):
        self.__states = {0: 'red', 1: 'yellow', 2: 'green', 3: 'yellow'}  # Карта состояний светофора
        self.__timeouts = {0: 7, 1: 2, 2: 4, 3: 2}  # Интервалы для каждого состояния
        self.__state = 0  # Текущее состояние
        self.__color = self.__states.get(self.__state)  # Текущий цвет
        self.__t = None  # Таймер

    def __set_next_light(self):
        """Переключает на след сигнал светофора"""
        self.__state = 0 if self.__state == max(self.__states.keys()) else self.__state + 1  # Выбор нового состояния
        self.__color = self.__states.get(self.__state)  # Новый цвет
        self.__print_state()  # Напечатали новое состояние
        self.__t = Timer(self.__timeouts.get(self.__state),  # Переинициализация таймера с новым интервалом
                         self.__set_next_light)
        self.__t.start()  # Запуск таймера

    def __print_state(self):
        """Цветом выводит в консоль состояние"""
        formats = {0: "\033[31m {}", 1: "\033[33m {}", 2: "\033[32m {}", 3: "\033[33m {}"}
        print(formats.get(self.__state).format(self.__color))

    def run(self):
        self.__print_state()
        self.__t = Timer(2, self.__set_next_light)
        self.__t.start()


# a = TrafficLight()
# a.run()

TrafficLight().run()
