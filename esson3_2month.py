<<<<<<< HEAD
class Car:

    @classmethod
    def show(cls):
    def __init__(self, model, year, color):
        self.__model = model
        self.__year = year
        self.__color = color

    @property
    def model(self):
        return self.__model
    @property
    def year(self):
        return self.__year
    @property
    def color(self):
        return

    @color.setter
    def color(self, value):
        return

    def drive(self):
        print(f'car: {self.__model} is driving')

    def __str__(self):
        return f'model: {self.__model}'
some_car = Car('toyota',1999,'red')
print(some_car)


class FUerCar(Car):
    def __init__(self, model, year , color, fuelbank):
        Car.__init__(self, model, year, color)
        self.fuelbank = fuelbank

bmw = FUerCar('bmw',1000,'black',20)
print(bmw)


class ElectroCar(Car):
    def __init__(self, model, year , color, fuelbank, battery):
        Car.__init__(self, model, year, color)


number_1, number_2 = 2, 5
print(f'number 1 is greater than 2 number: {number_1 > number_2}')

=======
print("hello")
>>>>>>> feature-comments
