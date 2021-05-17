# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1 Two — 2 Three — 3 Four — 4
# Напишите программу, открывающую файл на чтение и считывающую построчно данные. При
# этом английские числительные должны заменяться на русские. Новый блок строк должен
# записываться в новый текстовый файл.
with open('f_task4.txt', 'w', encoding='utf8') as source_file:
    source_file.write('One — 1\nTwo — 2\nThree — 3\nFour — 4')

number_words = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
with open('f_task4.txt', 'r', encoding='utf8') as source_file, \
        open('f_task4_ru.txt', 'w', encoding='utf8') as target_file:
    for line in source_file:
        key = line.split()[0]
        if key in number_words.keys():
            target_file.write(line.replace(key, number_words.get(key)))
