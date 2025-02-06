# length = 10
# width = 6
# square_3 = length + width
# print(square_3)
# length = 200
# width = 10
# square_hall = length * width
# print(square_hall)


# def get_square(length: int, width: int) -> int:
#     return length * width
# print(help(get_square))
# print(get_square(__doc__))
# square_3 = get_square(10, 5)
# square_hall = get_square(200, 10)
# print(square_hall)
# print(square_3)
"""из чего состоит функция?"""
# определение наименование(параметры)
# тело функции
# влзвращение результата

# def get_data(name, surname = " no"):
#     print(f'name: {name} surname: {surname}')
# get_data('nurperi', 'asanova')
# get_data(surname='akbaralieva', name='ademi') #keywoard argument


#
# len_world = len('geeks')
# print(len_world)

# len_world = len('geeks')
# print(len_world)
# def len1(objects):
#     counter = 0
#     for _ in objects:
#         counter += 1
#     return objects
# len_world1 = len1('python')
# print(len_world1)


"""виды аргументов"""
# def plus(*args): все что пишем может сохранятся в одном
#     return sum(args)
# print(plus(1, 2, 3, 4, 5))

# def menu(**kwargs): все что пишем сохраняется в словаре
#     return kwargs
# monday = menu(eat = 'pizza', drink = 'cola')
# print(monday)
# tuesday = menu(eat = 'manty', drink = 'tea')
# print(tuesday)
#
def check_password():
    l = ['q','w','e','r','t','y','u','i','o','p','l','k','j','h','g','f','d','s','a','z','x','c','v','b','n','m']
    L = ['Q','W','E','R','T','Y','U','I','O','P','L','K','J','H','G','F','D','S','A','Z','X','C','V','B','N','M']
    S = ['!','@','#','$','%','^','&','*']
    while True:
        password = input("create a new password: ")


        if password =='12345' or password=='password':
            print('very easy password!Try again!')
            continue
        if len(password) < 6:
            print("very short password! Try again!")
            continue
        for
        else:
            print(True)
            break


check_password()
