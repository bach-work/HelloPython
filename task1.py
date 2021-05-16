# 1. Создать программный файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных будет свидетельствовать пустая строка.

lines = []
while True:  # Формируем список
    text = input("Введите текст: ")
    if len(text) == 0:
        break
    lines.append(text)

with open('f_task1.txt', 'w') as f:
    f.write('\n'.join(lines))  # Соединяем в строку

with open('f_task1.txt') as f:
    print(f.read())  # Смотрим что получилось
