# 3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить, к какому времени года
# относится месяц (зима, весна, лето, осень). Напишите решения через list и dict.

month = 0
while month not in range(1, 13):
    month = int(input("Введите номер месяца (1..12): "))

list_seasons = ('Winter', 'Spring', 'Summer', 'Autumn')  # Список сезонов
dict_seasons = {0: 'Winter', 1: 'Spring', 2: 'Summer', 3: 'Autumn'}  # Словарь сезонов
s = month % 12  # изза того, что декабрь - зима
s = s // 3      # получаем номер сезона
print(list_seasons[s], dict_seasons.get(s))



