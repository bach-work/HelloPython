# 2. Представлен список чисел. Необходимо вывести элементы исходного списка, значения
# которых больше предыдущего элемента
from time import perf_counter

source = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]  # Исходный массив

# Первый вариант через range
result = [source[i + 1] for i in range(len(source) - 1) if source[i] < source[i + 1]]
print(result)
# Второй вариант через enumerate и срез без последнего элемента (ибо проверяем на i+1)
result = [source[i + 1] for i, el in enumerate(source[:-1]) if el < source[i + 1]]
print(result)
