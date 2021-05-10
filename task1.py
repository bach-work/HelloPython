# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их
# деление. Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на
# ноль.

def division(dividend, divider):
    try:
        return dividend / divider
    except ZeroDivisionError:
        print("Произошло деление на 0")
        return 0


first, second = input("Введите 2 числа: ").split()
if first.isdigit() and second.isdigit():
    print(division(int(first), int(second)))
