# Контекстный менеджер “with”, работа с файлами
# w= write он может удалить все данные до него
#a = add добавляет новую запись к старой


# file = open('new_file.txt', 'w')
# file.write('строка на кириллице')
# file.close()

# with open('new_file.txt', 'a') as file:
#     file.write('\n третья строка') # /n переносит на другую строку когда остальные просто добавляются рядом со старым
#
# x = добавляет новый файл. Нельзя называть файлы одинаковыми


"""РЕЖИМ ЧТЕНИЯ"""
# with open('new_file.txt', 'r') as file:
#     print(file.read())


# from time import sleep
# with open('new_file.txt','r') as file:
#     for i in file.readlines():
#         sleep(2)
#         print(i)

#readline- перебирает каждую букву readlines- перебирает по строке





#homework

def guess_number():
    print("Загадайте число от 1 до 100")
    low = 1
    high = 100
    attempts = 0
    guesses = []

    while True:
        guess = (low + high) // 2
        attempts += 1
        guesses.append(guess)
        print(f"Ваше число {guess}?")



        user_input = input("Введите 'да', 'больше' или 'меньше': ").lower()

        if user_input == "да":
            print(f"Я угадал число {guess} за {attempts} попыток!")



            with open("results.txt", "w") as file:
                file.write(f"Загаданное число: {guess}\n")
                file.write(f"Количество попыток: {attempts}\n")
                file.write(f"Список попыток: {guesses}\n")
            break
        elif user_input == "больше":
            low = guess + 1
        elif user_input == "меньше":
            high = guess - 1
        else:
            print("Пожалуйста, введите один из этих ответов: 'да', 'больше' или 'меньше'.")

        if low > high:
            print("Произошла ошибка.")
            break


guess_number()
