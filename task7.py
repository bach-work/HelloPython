# 7. Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая
# строка будет содержать данные о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также
# среднюю прибыль. Если фирма получила убытки, в расчёт средней прибыли её не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а
# также словарь со средней прибылью. Если фирма получила убытки, также добавить её в
# словарь (со значением убытков).
import json

from file_generator import text_gen

if not text_gen.gen_firm_list_file('f_task7.txt', 10):
    print('Ошибка формирования файла')
    exit(-1)


with open('f_task7.txt', 'r', encoding='utf8') as f:
    try:
        result_list = []
        profit_list = []
        firm_dict = {}
        for line in f:
            firm_name, form, proceeds, costs = line.split()  # Декомпозировали строку
            proceeds = int(proceeds)
            costs = int(costs)
            profit = proceeds - costs  # Считаем прибыль
            if profit > 0:  # Если прыбыль +, то значение в список
                profit_list.append(profit)
            firm_dict[firm_name] = profit  # кдладем в словарь фирму и ее прибыль

        result_list.append(firm_dict)  # В результат кладем словарб фирм
        result_list.append({'average_profit': (sum(profit_list)/len(profit_list))})  # Туда же считаем среднюю прибыль

        with open('firm_stats.json', 'w') as f_json:
            json.dump(result_list, f_json)  # и в файл все это

    except BaseException as e:
        print('Ошибка разбора файла', e)