# 2) Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная
# сущность (класс) этого проекта — одежда, которая может иметь определенное название. К
# типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют
# параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и
# H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто
# (V/6.5 + 0.5), для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке
# знания: реализовать абстрактные классы для основных классов проекта, проверить на
# практике работу декоратора @property
from functools import reduce


class Clothes:
    def __init__(self, name: str):
        self.name = name

    def get_cons(self) -> float:
        """Расход ткани"""
        pass


class Coat(Clothes):
    """Пальто"""

    def __init__(self, name, v: int):
        super(Coat, self).__init__(name)
        self.v = v

    @property
    def get_cons(self) -> float:
        return self.v / 6.5 + 0.5


class Suit(Clothes):
    """Костюм"""

    def __init__(self, name, h: int):
        super(Suit, self).__init__(name)
        self.h = h

    @property
    def get_cons(self) -> float:
        return 2 * self.h + 0.3


# Список вещей
list_clothes = [Coat('Мое пальто', 58), Suit('Мой костюм', 59), Coat('Мое пальто 2', 60), Suit('Мой костюм 2', 61)]
print(reduce(lambda prev, curr: prev + curr, [el.get_cons for el in list_clothes]))  # Считаем расход ткани
