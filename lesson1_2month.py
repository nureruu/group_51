# ООП

# class Transport: #наследование
#     def __init__(self, the_model, the_year, the_color):  # init = создать
#         self.model = the_model
#         self.year = the_year
#         self.color = the_color
#
#
#
#     def change_color(self, new_color):
#         self.color = new_color
# class Plane(Transport):
#     def __init__(self, the_model, the_year, the_color):  # init = создать
#         super().__init__(the_color,the_year,the_model)
#
# class Car(Transport):
#     # class attribute
#     counter = 0
#     def __init__(self, the_model, the_year, the_color, penalties = 0): # init = создать
#         super().__init__(the_color,the_year,the_model)
#         self.penalties = penalties
#         Car.counter += 1
#
#
# class Truck(Car):
#     def __init__(self,):
#
#     def drive(self, city):
#         print(f'Car: {self.model} is driving to {city}')
#
# # self = присвоение
# print('start')
#
#
#
# dmw = Car('BMW x7', 2020, 'red', 100)
# honda = Car('honda x7', 2022, 'black')
# dmw.change_color('black')
# print('end')
# print(f'model: {honda.model}, penalties: {honda.penalties},color: {honda.color}')
# print(f'model: {dmw.model}, penalties: {dmw.penalties}, color: {dmw.color}')
# honda.drive('Bishkek')
# dmw.drive('Issyk_Kul')
# print(f'factory Car produced: {Car.counter}')



class Person:
    def __init__(self, full_name, age, is_married):
        self.full_name = full_name
        self.age = age
        self.is_married = is_married
    def introduce_myself(self):
        status = "married" if self.is_married else "not married"
        print(f'hello! my name is : {self.full_name} im {self.age} years old, im {status}')
class Student(Person):
    def __init__(self, full_name, age, is_married, marks):
        super().__init__(full_name,age,is_married)
        self.marks = marks


    def calculate(self):
        if not self.marks:
            return False
        marks = sum(self.marks.values())
        return marks // len(self.marks)


class Teacher(Person):
    def __init__(self, full_name, age, is_married, experience):
        super().__init__(full_name,age,is_married)
        self.experience = experience
        base_salary = 50000

        def calculate_salary(self):
            bonus_years = max(0, self.experience - 3)
            bonus = bonus_years * (0.05 * self.base_salary)
            return self.base_salary + bonus

        teacher = Teacher("Ademi", 30, "not married", 10)


        print(Teacher.introduce_myself())
        print(f"Salary: {teacher.calculate_salary():.2f}")


        def create_students():
            students = [
                Student('nurperi', 17, 'not married', {'math': 5, 'english':4,'kyrgyz':5}),
                Student('emir',18,'married',{'math':4,'russian': 5,'spanish':3}),
                Student('amina',15,'not married', {'math': 5,'russian': 2, 'kyrgyz': 5})

            ]
            return students

        students = create_students()
        for student in students:
            student.introduce_myself()
            for subject, mark in student.marks.items():
                print(f"{subject}: {mark}")
            print(f"Average Mark: {student.calculate_average_mark():.2f}\n")