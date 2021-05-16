import string
from random import choice, randint


def random_word(max_length: int) -> str:
    """Возвращает слово произвольной длинны(максимум - max_length) из случайных латинских букв"""
    try:
        current_length = max_length if max_length > 2 else 2
        return ''.join(choice(string.ascii_lowercase) for _ in range(randint(2, current_length)))
    except TypeError as e:
        print('Ошибка входного типа! Длина - это целое число.', e)
    except BaseException as e:
        print('Ошибка!', e)


def random_string(max_words_count: int, max_word_length: int=6) -> str:
    """
    Возвращает строку, состоящую из случайных слов.
    Количество слов не больше чем max_words_count
    """
    try:
        words_count = randint(1, max_words_count)
        return ' '.join([random_word(max_word_length) for _ in range(words_count)])
    except BaseException as e:
        print('Ошибка!', e)


def random_generator(row_count: int, max_column_count: int):
    """Возвращает генератор текста"""
    try:
        for _ in range(row_count):
            yield random_string(max_column_count)
    except BaseException as e:
        print('Ошибка!', e)


def random_text(row_count: int, max_column_count: int) -> str:
    """Возвращает текст из случайных слов

    :param row_count: Количество строк
    :param max_column_count:  максимально число слов в одной строке
    """
    try:
        return '\n'.join([random_string(max_column_count) for _ in range(row_count)])
    except BaseException as e:
        print('Ошибка!', e)


def gen_file(filename: str, row_count: int, max_column_count: int):
    """Генерирует файл со случайными словами"""
    try:
        with open(filename, 'w') as file:
            file.write(random_text(row_count, max_column_count))
        return True
    except BaseException as e:
        print('Ошибка!', e)
        return False


# if __name__ == '__main__':
    # print(random_word('q'))
    # print( random_string(15) )
    # g = random_generator(7, 10)
    # for el in g:
    #     print(el)