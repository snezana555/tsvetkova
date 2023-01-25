
class TikTacToe:
    """
    Игра крестики-нолики
    """
    def __init__(self):
        self.field = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    def place_crosses(self, x, y):
        """
        Должен вернуть 1, если всё ок. Или 0, если нельзя осуществить операцию
        """
        if self.field[x - 1][y - 1] == ' ':
            self.field[x - 1][y - 1] = '*'
            return 1
        else:
            return 0

    def place_noughts(self, x, y ):
        """
        Должен вернуть 1, если всё ок. Или 0, если нельзя осуществить операцию
        """
        if self.field[x - 1][y - 1] == ' ':
            self.field[x - 1][y - 1] = '0'
            return 1
        else:
            return 0

    def get_winner(self):
        """
        Вернуть
        0 нет победителя
        1 победили crosses
        0 победили noughts
        """
        """Не учитывается ситуация, где на сетке совпадают больше 1 условия"""
        if self.field[0][0] == self.field[0][1] == self.field[0][2] != ' ':
            # победа по первой строке
            symbol = self.field[0][0]
        elif self.field[1][0] == self.field[1][1] == self.field[1][2] != ' ':
            # победа по второй строке
            symbol = self.field[1][0]
        elif self.field[2][0] == self.field[2][1] == self.field[2][2] != ' ':
            # победа по третьей строке
            symbol = self.field[2][0]
        elif self.field[0][0] == self.field[1][0] == self.field[2][0] != ' ':
            # победа по первому столбцу
            symbol = self.field[0][0]
        elif self.field[0][1] == self.field[1][1] == self.field[2][1] != ' ':
            # победа по второму столбцу
            symbol = self.field[0][1]
        elif self.field[0][2] == self.field[1][2] == self.field[2][2] != ' ':
            # победа по третьему столбцу
            symbol = self.field[0][2]
        elif self.field[0][0] == self.field[1][1] == self.field[0][2] != ' ':
            # победа по диагонали
            symbol = self.field[0][0]
        elif self.field[0][2] == self.field[1][1] == self.field[2][0] != ' ':
            # победа по диагонали
            symbol = self.field[0][2]

        if symbol == '*':
            return 1
        else:
            return 0


def test_1():
    game = TikTacToe()
    assert game.place_crosses(1, 3) == 1
    assert game.place_crosses(1, 3) == 0

test_1()