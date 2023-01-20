class Car:
    """
    класс автомобиль
    """
    color = 'white'  # цвет
    engine_power = 90  # мощность двигателя
    tank_capacity = 50  # объем бака
    fuel_consumption = 9.3  # расход топлива на 100 км
    fuel_now = 0  # топлива в баке сейчас

    def __init__(self, color: str  = 'white', engine_power: int  =  90, tank_capacity: int  =  50, fuel_consumption: int  =  9.3, fuel_now: int = 0):
        self.color = color
        self.engine_power = engine_power
        self.tank_capacity = tank_capacity
        self.fuel_consumption = fuel_consumption
        if fuel_now <= tank_capacity:
            self.fuel_now = fuel_now
        else:
            raise BaseException

    def set_color(self, color):
        """
        перекрасить автомобиль
        """
        self.color = color

    def get_color(self):
        """
        узнать цвет
        """
        return self.color

    def get_fuel_now(self):
        """
        :return: топлива есть сейчас
        """
        return self.fuel_now

    def refuel(self, liters_of_fuel):
        """
        заправить liters_of_fuel топлива
        :param liters_of_fuel:
        :return:
        """
        if liters_of_fuel + self.fuel_now <= self.tank_capacity:
            self.fuel_now += liters_of_fuel
            return self.fuel_now
        else:
            raise BaseException


    def get_engine_power(self):
        """
        узнать мощность двигателя
        :return:
        """
        return self.engine_power

    def get_fuel_consumption(self):
        """
        узнать расход топлива
        :return:
        """
        return self.fuel_consumption


def test_init_1():
    Car(color='white',
        engine_power=90,
        tank_capacity=50,
        fuel_consumption=9.3,
        fuel_now=0)


def test_init_2():
    Car(color='white')


def test_color_1():
    c = Car(color='white',
            engine_power=90,
            tank_capacity=50,
            fuel_consumption=9.3,
            fuel_now=0)
    assert c.get_color() == 'white'


def test_color_2():
    c = Car(color='white',
            engine_power=90,
            tank_capacity=50,
            fuel_consumption=9.3,
            fuel_now=0)
    assert c.get_color() == 'white'
    c.set_color('red')


def test_color_3():
    c = Car(color='white',
            engine_power=90,
            tank_capacity=50,
            fuel_consumption=9.3,
            fuel_now=0)
    assert c.get_color() == 'white'
    c.set_color('red')

    assert c.get_color() == 'red'


