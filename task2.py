# Выполнить функцию, которая принимает несколько параметров, описывающих данные
# пользователя: имя, фамилия, год рождения, город проживания, email, телефон. Функция
# должна принимать параметры как именованные аргументы. Осуществить вывод данных о
# пользователе одной строкой

def printPersonInfo(first_name, second_name, year, current_city, mail, phone):
    print('Имя: {}, Фамилия: {}, Год рождения: {}, Город проживания: {}, Email: {}, Телефон: {}'
          .format(first_name, second_name, year, current_city, mail, phone))


printPersonInfo(first_name='Leo',
                second_name='J.',
                year=1812,
                current_city='London',
                mail='qqq@www.com',
                phone='9578451214')
