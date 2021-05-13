# 5. Реализовать формироваие списка, используя функци range() и возможности генератора.
# В список должны войти четные числа от 100 до 1000 (включая границы). Нужно получить
# результат вычисления произведения всех элементов списка
from functools import reduce

my_list = [i for i in range(100, 1001) if i % 2 == 0]
print(my_list)
print(reduce(lambda prev, curr: prev*curr, my_list))
