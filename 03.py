class MiracleList:
    """
    Класс чудо список.
    - можно печатать
    - можно сортировать
    - можно находить (первый) индекс элемента
    """
    def __init__(self, mass: int = [0, 1, 0]):
        self.mass = mass

    def get_data(self):
        return self.mass

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

def test_get_data():
    ml = MiracleList([1, 2, 3])
    assert ml.get_data() == ml


def test_sort():
    ml = MiracleList([2, 3, 1])
    ml.sort()
    assert ml.get_data() == [1, 2, 3]


def test_bin():
    ml = MiracleList([2, 3, 1])
    ml.sort()
    assert ml.bin(1) == 1