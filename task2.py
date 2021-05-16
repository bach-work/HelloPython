# 2. Создать текстовый файл (не программно), сохранить в нём несколько строк,
# выполнить подсчёт строк и слов в каждой строке.
from file_generator import text_gen

# Мне стало лень придумывать слова и я написал генератор текстового файла
# формирует файл с именем f_task2.txt, 30ю строками и до 15 слов в каждой строке
if not text_gen.gen_file('f_task2.txt', 30, 15):
    print('Ошибка формирования файла')
    exit(-1)


with open('f_task2.txt') as f:
    for i, line in enumerate(f):
        print('Строка {:2d}: {:2d} слов, {:2d} букв    ({:5})'
              .format(i+1, len(line.split()), len(line.replace(" ", "")),
                      line.replace('\n', '')))





