# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчёта заработной
# платы сотрудника. Используйте в нём формулу: (выработка в часах*ставка в час) + премия. Во
# время выполнения расчёта для конкретных значений необходимо запускать скрипт с
# параметрами.
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-w', type=int, help='Выработка в часах')
parser.add_argument('-p', type=int, help='Ставка в час')
parser.add_argument('-a', type=int, help='Премия')
list_args = parser.parse_args()
print(f"Зп сотрудника {list_args.w * list_args.p + list_args.a}$")

# Example: 'python .\task1.py -p 10 -a 5 -w 100'
