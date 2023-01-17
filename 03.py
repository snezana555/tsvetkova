class MiracleList:
    """
    Класс чудо список.
    - можно печатать
    - можно сортировать
    - можно находить (первый) индекс элемента
    """
    def __init__(self, mass: int = [0, 1, 0]):
        self.mass = mass

    def print(self):
        print(self.mass)

    def sort(self):
        return sorted(self.mass)

    def bin(self, number):
        if number in self.mass:
            return self.mass.index(number)
        else:
            return('Такого числа нет в массиве')

list_ = MiracleList([2, 2, 8])
list_.print()
print(list_.sort())
print(list_.bin(2))