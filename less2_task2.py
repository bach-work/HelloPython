# 2. Для списка реализовать обмен значений соседних элементов. Значениями обмениваются
# элементы с индексами 0 и 1, 2 и 3 и т. д. При нечётном количестве элементов последний
# сохранить на своём месте. Для заполнения списка элементов нужно использовать функцию
# input().

# my_list = [0, 'one', 2, 'three', 4, 'five', 6, 'seven']
# print(my_list)
my_list = []
res = True
while res:
    value = input("Введите элемент (или 'f', что бы закончить ввод): ")
    if value == 'f':
        break
    my_list.append(value)

print("Исходный список {}".format(my_list))
i = 0
while i < len(my_list):
    if (i + 1) > len(my_list) - 1:  # нет элемента с i+1
        break
    next_value = my_list[i+1]  # сохраняем элемент i+1
    my_list[i+1] = my_list[i]  # в i+1 кладем предыдцщий
    my_list[i] = next_value  # в i кладем i+1
    i += 2


print("Конечный список {}".format(my_list))
