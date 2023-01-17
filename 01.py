
class Car:
    """
    Автомобиль
    имеет цвет
    имеет мощность дивгателя
    имеет максимальный запас бензина в баке
    имеет расход (например 9.3 литра на 100 км)
    можно перекрасить
    можно заправить N литров
    можно проехать N киллометров
    можно узнать цвет
    мощность
    сколько осталось литров в баке
    узнать расход
    """
    color: str = 'violet'
    power: int = 106
    max_petrol: int = 48
    consumption: int = 10 # на 100 км
    petrol: int = 0

    def __init__(self, color: str = 'violet', power: int = 106, max_petrol: int = 48, consumption: int = 10):
        self.color = color
        self.power = power
        self.max_petrol = max_petrol
        self.petrol = 0
        self.consumption = consumption

    def change_color(self, color):
        self.color = color
        print('Машина покрашена')

    def add_petrol(self, petrol):
        if petrol <= 0:
            print('Вы точно хотите заправить машину?')
        elif (self.petrol + petrol) >= self.max_petrol:
            print('Этого слишком много')
            print('Вы можете добавить не больше ', self.petrol - self.max_petrol)
        else:
            self.petrol += petrol
            print('Машина заправлена')

    def drive(self, count_km):
        max_km = (self.consumption / 100) * self.petrol
        print(max_km)
        if count_km <= 0:
            print('Вы классный ездок, но величина неправильная')
        elif max_km > count_km:
            self.petrol -= (self.consumption / 100 * count_km)
            print('Отлично, вы проехали ', count_km, ' и потратили ', self.consumption / 100 * count_km , ' литров бензина')
        else:
            print('Вы можете проехать не больше ', max_km, ' км')

    def what_color(self):
        return self.color

    def what_power(self):
        return self.power

    def what_petrol(self):
        return self.petrol

    def what_consumption(self):
        return self.consumption

car_2 = Car(color = 'lightblue', power = 100, max_petrol = 45, consumption = 10)
car_2.change_color('yellow')
car_2.add_petrol(20)
car_2.drive(1)

print('Цвет машины ', car_2.what_color())
print('Мощность',car_2.what_power())
print('Осталось литров',car_2.what_petrol())
print('Расход',car_2.what_consumption())


