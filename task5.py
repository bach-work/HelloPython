# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых
# пробелами. Программа должна подсчитывать сумму чисел в файле и выводить её на экран.
from file_generator import text_gen

if not text_gen.gen_numbers_file('f_task5.txt', 50):
    print('Ошибка формирования файла')
    exit(-1)

with open('f_task5.txt') as f:
    numbers = [int(x) for x in f.read().split()]
    print(f'Сумма чисел в файле - {sum(numbers)}')