# 2. Реализовать класс Road (дорога).
# ● определить атрибуты: length (длина), width (ширина);
# ● значения атрибутов должны передаваться при создании экземпляра класса;
# ● атрибуты сделать защищёнными;
# ● определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
# ● использовать формулу: длина*ширина*масса асфальта для покрытия одного кв. метра дороги асфальтом,
# толщиной в 1 см*число см толщины полотна;
# ● проверить работу метода.
# Например: 20 м*5000 м*25 кг*5 см = 12500 т.


class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width
        self.__single_weight = 25  # масса для покртыия 1 кв м

    def calc_weight(self, height: int = 5):
        return self._length * self._width * self.__single_weight * height


r = Road(2, 2)
print(r.calc_weight())
