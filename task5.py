# 5. Реализовать класс Stationery (канцелярская принадлежность).
# ● определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
# ● создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
# ● в каждом классе реализовать переопределение метода draw.
# Для каждого класса метод должен выводить уникальное сообщение;
# ● создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.


class Stationery:
    def __init__(self, title: str):
        try:
            self._title = title
        except BaseException as e:
            print('Ошибка инициализации класса', e)

    def draw(self) -> None:
        print('Запуск отрисовки "{}"'.format(self._title))


class Pen(Stationery):
    def __init__(self, title: str):
        super(Pen, self).__init__(title)

    def draw(self) -> None:
        super(Pen, self).draw()
        print('Рисуем ручку')


class Pencil(Stationery):
    def __init__(self, title: str):
        super(Pencil, self).__init__(title)

    def draw(self) -> None:
        super(Pencil, self).draw()
        print('Рисуем карандаш')


class Handle(Stationery):
    def __init__(self, title: str):
        super(Handle, self).__init__(title)

    def draw(self) -> None:
        super(Handle, self).draw()
        print('Рисуем маркер')


stationery_list = [Handle('Мой маркер'), Pencil('Синий карандаш'), Pen('Ручка ручка'), Stationery('Базовый')]

for s in stationery_list:
    s.draw()
