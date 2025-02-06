# name = 'nurperi'
# surname = 'asanova'
# print(name,surname)
# print(f'name:{name} surname:{surname}')


# monday = float(input("понедельник расход сегодняшнего дня: "))
# print(monday)
# tuesday = float(input("вторник расход сегодняшнего дня: "))
# print(tuesday)
# wednesday = float(input("среда расход сегодняшнего дня: "))
# print(wednesday)
# thursday = float(input("четверг расход сегодняшнего дня: "))
# print(thursday)
# friday = float(input("пятница расход сегодняшнего дня: "))
# print(friday)
# saturday = float(input("суббота расход сегодняшнего дня: "))
# print(saturday)
# sunday = float(input("воскресенье расход сегодняшнего дня: "))
# print(sunday)
# sum = monday+thursday+tuesday+wednesday+friday+saturday+sunday
# total_amount = sum // 7
# print(f'общая сумма: {sum} средний расход в день: {total_amount}')

days_of_week = ["понедельник", "вторник", "среда", "четверг", "пятница", "суббота", "воскресенье"]

expenses = []

for day in days_of_week:
    expense = float(input(f"Введите расход за {day}: "))
    expenses.append(expense)

total_expenses = sum(expenses)
average_expense = total_expenses / len(days_of_week)

print(f"Общая сумма расходов за неделю: {total_expenses}")
print(f"Средний расход в день: {average_expense}")
