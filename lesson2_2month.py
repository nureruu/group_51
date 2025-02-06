# class Animal():
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def info(self):
#         return (f'{self.name} is {self.age} years old. Birth year: {2025 - self.age}')
#
# some_animal = Animal('bobik',4)
# print(some_animal.info())
#
# class Dog(Animal):
#
#     def __init__(self, name, age, commands):
#         super().__init__(name,age)
#         self.__commands = commands
#
#
#     @property
#     def commands(self):
#         return self.__commands
#     @commands.setter
#     def commands(self, value):
#         self.__commands = value
#
#     def make_voice(self):
#         print('woof')
#
#
# dog = Dog('snoopy', 5, 'sit')
# print(dog.commands)
#
# class Cat(Animal):
#     def __init__(self, name, age):
#         super(Cat, self).__init__(name, age)
#
#     def make_voice(self):
#         print('meow')
#
# cat = Cat('tom',3)
# class FightingDog(Dog):
#     def __init__(self, name, age, commands, win):
#         super(Cat, self).__init__(name, age, commands)
#         self.__win = win
#
#     def make_voice(self):
#         print('rrr')
#
#     @property
#     def wins(self):
#         return
#
#     @wins.setter
#     def wins(self, value):
#         pass
# fightDog = FightingDog('rex',1,'fight',14)
#
#
# class Fish(Animal):
#
#     def __init__(self, name, age):
#         super(Fish, self).__init__(name, age)
#
#         fish = Fish('nemo',43)
#
#     def make_voice(self):
#         pass
#
#
# ann = [cat, dog, fightDog]
# for animal in ann:
#     print(ann)
#
#


#HOMEWORK


class Figure:
    unit = "cm"
    def __init__(self):
        pass
    def calculate_area(self):
        raise NotImplementedError
    def info(self):
        raise NotImplementedError

class Square(Figure):
    def __init__(self, side_length):

        super().__init__()
        self.__length = side_length

    def calculate_area(self):
        return self.__length ** 2

    def info(self):
        area = self.calculate_area()
        return f'Square side length:{self.__length} cm, area: {self.calculate_area()}'

class Rectangle(Figure):
    def __init__(self, length, width):
        super().__init__(length)
        self.__width = width

    def calculate_area(self):
        return self.__length ** self.__width

    def info(self):
        area = self.calculate_area()
        return f'Rectangle length: {self.__length}, width: {self.__width}, area: {self.calculate_area()}'

shapes = [
    Square(3),
    Square(8),
    Rectangle(1,2),
    Rectangle(8,19)
]
for shape in shapes:
    shape.info()