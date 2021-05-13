# 6. Реализовать два небольших скрипта:
# ● итератор, генерирующий целые числа, начиная с указанного;
# ● итератор, повторяющий элементы некоторого списка, определённого заранее.
from itertools import count, cycle
from random import randrange

# ● итератор, генерирующий целые числа, начиная с указанного;
for i in count(3):
    print(i)
    if i == 10:
        break

print("-"*30)

my_list = [randrange(100) for i in range(5)]  # некоторый список, определённый заранее
# ● итератор, повторяющий элементы некоторого списка, определённого заранее.
print_count = len(my_list) * 3  # 3 раза список напечатаем
c = 0
for el in cycle(my_list):
    print(el)
    c += 1
    if c == print_count:
        break
