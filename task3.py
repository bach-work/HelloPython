# 3) Реализовать программу работы с органическими клетками, состоящими из ячеек. Необходимо
# создать класс Клетка. В его конструкторе инициализировать параметр, соответствующий
# количеству ячеек клетки (целое число). В классе должны быть реализованы методы
# перегрузки арифметических операторов: сложение (__add__()), вычитание (__sub__()),
# умножение (__mul__()), деление (__truediv__()). Данные методы должны применяться только
# к клеткам и выполнять увеличение, уменьшение, умножение и целочисленное (с округлением
# до целого) деление клеток, соответственно.


class Cellula:
    """Кле́тка (лат. cellula)"""

    def __init__(self, cell_count: int):
        self.cell_count = cell_count

    def __str__(self):
        return '*' * self.cell_count

    def __add__(self, other):
        """Сложение клеток"""
        if not isinstance(other, Cellula):
            return self
        return Cellula(self.cell_count + other.cell_count)

    def __sub__(self, other):
        """Вычитание клеток"""
        if not isinstance(other, Cellula):
            return self
        if self.cell_count < other.cell_count:
            print('Невозможно вычесть из маленькой клетки большую')
            return self
        return Cellula(self.cell_count - other.cell_count)

    def __mul__(self, other):
        """Умножение клеток"""
        if not isinstance(other, Cellula):
            return self
        return Cellula(self.cell_count * other.cell_count)

    def __truediv__(self, other):
        """Деление клеток"""
        if not isinstance(other, Cellula):
            return self
        if self.cell_count < other.cell_count:
            print('Невозможно разделить меньшую клетку на большую')
            return self
        try:
            return Cellula(self.cell_count // other.cell_count)
        except BaseException as e:
            print('Ошибка деления клеток', e)
        finally:
            return self

    def make_order(self, cell_in_rows: int):
        try:
            return '\n'.join(['\n'.join(['*' * cell_in_rows for _ in range(self.cell_count // cell_in_rows)]),
                              '*' * (self.cell_count % cell_in_rows)])
        except BaseException as e:
            print('Ошибка упорядочивания клеток', e)


print(Cellula(5) + Cellula(10))
print(Cellula(10) - Cellula(5))
print(Cellula(10) * Cellula(5))
print(Cellula(10) / Cellula(5))
print('-'*20)
c = Cellula(13)
print(c.make_order(5))
