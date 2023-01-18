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
        for i in range(len(self.mass) - 1):
            flag_ = True
            for j in range(len(self.mass) - i - 1):
                if self.mass[j] > self.mass[j + 1]:
                    self.mass[j], self.mass[j + 1] = self.mass[j + 1], self.mass[j]
                    flag_ = False
            if flag_:
                break

        return self.mass

    def bin(self, number):
        self.sort()
        l = 0
        r = len(self.mass) - 1
        while(l <= r):
            middle = (l + r) // 2
            if (number == self.mass[middle]):
                print('Индекс числа в отсортированном массиве ', middle)
                break;
            elif self.mass[middle] < number:
                l = middle + 1
            else:
                r = middle - 1
        else:
            print('Такого числа нет в массиве')

list_ = MiracleList([2, 10, 8, 5, 6, 12, 13,3])
list_.print()
print('Отсортированный массив', list_.sort())
list_.bin(12)