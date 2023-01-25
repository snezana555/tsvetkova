
class my_queue:
    """
    Необходимо написать реализацию очереди на 2х стеках
    """
    def __init__(self):
        self.stack_1 = []
        self.stack_2 = []

    def push(self, el):
        """
        добавляет el в стек
        """
        self.stack_1 += [el]

    def pop(self):
        """
        удаляет элемент в стеке и возращает его
        """
        if self.stack_2:
            return self.stack_2.pop()
        else:
            while self.stack_1:
                self.stack_2 += [self.stack_1.pop()]
            return self.stack_2.pop()

    def size(self):
        """
        возращает размер стека
        """
        return len(self.stack_2 + self.stack_1)


def test_1():
    s = my_queue()
    s.push(1)
    assert s.pop() == 1


test_1()


def test_2():
    s = my_queue()
    s.push(1)
    assert s.size() == 1


test_2()


def test_3():
    s = my_queue()
    s.push(1)
    s.push(2)
    assert s.pop() == 1
    s.push(3)
    s.push(4)
    assert s.pop() == 2
    assert s.size() == 2
    assert s.pop() == 3


test_3()

s = my_queue()
s.push(4)
s.push(2)
print(s.pop())