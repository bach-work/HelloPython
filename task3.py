# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента и
# возвращает сумму наибольших двух аргументов.

def my_func(fist, second, third):
    my_list = [fist, second, third]
    my_list.remove(min(my_list))
    return my_list[0] + my_list[1]


print(my_func(10, 2, 3))


