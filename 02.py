class TikTacToe:
    """
    Описание: игра в крестики-нолики
    Рассматриваются 3 случая победы игрока:
    1. 3 знака по горизонтали
    2. 3 знака по вертикали
    3. 3 знака по диагонали
    """
    first: str = 'первый игрок'
    second: str = 'второй игрок'

    field = [['', '', ''], ['', '', ''], ['', '', '']]
    """
    рассмотрим 3 случая победы игрока:
    1. 3 знака по горизонтали
    2. 3 знака по вертикали
    3. 3 знака по диагонали
    """
    def __init__(self, first: str = 'первый игрок', second: str = 'второй игрок'):
        self.first = first
        self.second = second
        self.field = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

    def place_crosses(self):
        for i in self.field:
            for j in i:
                print('|'+ j, end='|')
            print()
            print('---------')
        print()

    def place_noughts(self, name, i, j):
        if self.field[i][j] == ' ':
            if name == self.first:
                self.field[i][j] = '*'
            elif name == self.second:
                self.field[i][j] = 'o'
            else:
                print('Введите имя игрока ещё раз')
            self.get_winner(name,i,j)
        else:
            print('Эта клетка уже занята, выберите другую')


    def get_winner(self,name, i, j):
        if self.field[i][0] == self.field[i][1] == self.field[i][2] != ' ':
            print('Победил ', name)
        elif self.field[0][j] == self.field[1][j] == self.field[1][j] != ' ':
            print('Победил ', name)
        elif self.field[0][0] == self.field[i][j] == self.field[2][2] != ' ':
            print('Победил ', name)
        elif self.field[0][2] == self.field[i][j] == self.field[2][0] != ' ':
            print('Победил ', name)
        elif '' in self.field:
            print('Ничья')



play = TikTacToe(first = 'Кирилл', second = 'Артём')
play.place_noughts(play.first, 2, 2)
play.place_crosses()
play.place_noughts(play.second, 0, 1)
play.place_crosses()
play.place_noughts(play.first, 2, 1)
play.place_crosses()
play.place_noughts(play.second, 1, 0)
play.place_crosses()
play.place_noughts(play.first, 1, 1)
play.place_crosses()
play.place_noughts(play.second, 0, 2)
play.place_crosses()
play.place_noughts(play.first, 2, 0)