# 3. Создать текстовый файл (не программно). Построчно записать фамилии сотрудников и
# величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее
# 20 тысяч, вывести фамилии этих сотрудников. Выполнить подсчёт средней величины дохода
# сотрудников.
from file_generator import text_gen

workers = ['Иванов','Петров','Сидоров','Попов','Козлов','Шац','Кузнецов','Чернов','Овсов','Питонов']
if not text_gen.gen_salary_file('f_task3.txt', workers):
    print('Ошибка формирования файла')
    exit(-1)

with open('f_task3.txt', 'rt',  encoding='utf-8') as f:
    try:
        salary_list = []
        for name_line in f:  # для каждого сотрудника
            name, salary = name_line.split()
            salary = float(salary)
            salary_list.append(salary)
            if salary > 20000.00:
                print(f'{name} {salary}')
        print(f'Средняя зп сотрудников {sum(salary_list)/len(salary_list):.2f}')
    except BaseException as e:
        print('Призошла ошибка при чтении файла', e)