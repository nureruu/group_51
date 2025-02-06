# #списки кортежи индексы и срезы
# # #1 это списки = list с помощью []
#
# # print(type(students))
# # print(students[3])
# # print(students[1][3])
#
# # срезы start:stop: step на стоп всегда на единицу выше
# students = ["islam" , "nurperi" , "saikal" , "pavel"]
# print(students[::-1])
# print(students[:-1])

# # students2 = [name.title() for name in students] # через for перебираем список имен и в каждое имя добавляем заглваную букву
# # students2 = [name.title() for name in students if 'a' in name] #добавляем условие если в имени есть буква а тогда оставляем
# # print(students2)
# # print(students)
#
# """кортежи- tuple"""
# # numbers = 1, 2, 3, 4, 5
# # print(numbers)
# # print(type(numbers))
# # """add"""
# # students.append("mirlan")#append-add в конец только один
# # students.insert(1, "raatbek") #добавляет не в конец, а куда хочешь например вместо 1 добавили раатбек
# # students.extend(["altynai", "jumagul"]) # добавляет больше одного
# # students += ["azamat", "alina", "madina"]
#
# """edit"""
# # students.reverse()
#
# # students.sort() #сортирует буквы по алфавиту, цифры по увеличению
# # students[0] = "lalala" #change name
# # print(students)
# """delete"""
# # students.remove("islam")
# # deleted = students.pop(-1)# вырезаеt
# # del students[0]
# # print(students)
#
#
# #встроенные фукнции к наборам элементов. Списковое включение
#
#
# # numbers = [12, 5.6, 34, 89, 11]
#
#
# # print(len(numbers)) #считвет сколько объектов
# # print(min(numbers)) #вернет самое минимальное число
# # print(max(numbers)) #вернет самое большое число
# # print(sum(numbers)) #плюсует все
# # print(all(numbers)) #если хотя бы будет один 0 в списке выйдет false, если не 0 тогда true
# # print(any(numbers)) #если хотя бы один не 0 тогда true
#
# # numbers2 = numbers.copy()
# # print(numbers is numbers2) #сравнивает это один списк или нет
# # print(numbers == numbers2) #сравнивает похожи ли они
# # print(id(numbers)) #выводит ид списка в терминал
# # print(id(numbers2))
# # print(numbers)
# # print(numbers2)

# data_tuple = ('h', 6.13, 'C', 'e', 'T', True, 'k', 'e', 3, 'e', 1, 'g')
# numbers = []
# letters = []
# for i in data_tuple:
#     if type(i) == str:
#         letters.append(i)
#     else:
#         numbers.append(i)
# numbers.remove(6.13)
# numbers.remove(True)
# letters.append(True)
#
# numbers.insert(1, 2)
# numbers.sort()
# letters.reverse()
# numbers[1] = 4
# numbers[2] = 9
# letters[1] = "G"
# letters[-2] = "c"
# letters_tuple = tuple(letters)
# numbers_tuple = tuple(numbers)
# print(f'numbers: {numbers_tuple} '
#       f'letters: {letters_tuple}')