# 1) Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод
# __init__()), который должен принимать данные (список списков) для формирования матрицы.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух
# объектов класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.

from random import randint


class Matrix:
    """Матрица"""

    def __init__(self, matrix: list = []):
        self.__matrix = matrix

    def __str__(self):
        return '\n'.join((' '.join(str(e) for e in row)) for row in self.__matrix)

    def __add__(self, other):
        try:
            # Не смог придумать как обойтись без enumerate
            return Matrix([[value + other.__matrix[row_index][col_index] for col_index, value in enumerate(row)]
                           for row_index, row in enumerate(self.__matrix)])
        except BaseException as e:
            print('Ошибка сложения матриц!', e)


def genMatrix(row_count: int, column_count: int) -> Matrix:
    """Формирует случайную матрицу размера [row_count, column_count]"""
    try:
        return Matrix([[randint(0, 100) for _ in range(column_count)] for _ in range(row_count)])
    except BaseException as e:
        print('Ошибка генерации матрицы', e)
        return Matrix()


simple_m = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
print(Matrix(simple_m) + Matrix(simple_m))

print(genMatrix(5, 5) + genMatrix(5, 5))
