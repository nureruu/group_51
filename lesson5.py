# # словарь
# student = {
#     'name': 'nurperi',
#     'age': 17,
#     'surname': 'asanova',
#     'country': 'kg'
# }
# print(student)
#
# """add"""
# student['height'] = 1.65
# student.update({'surname': 'lololo', 'country': 'korea'})
# """delete"""
# student.pop('name')
# # del student['surname']
# """edit"""
# student['age'] = 20
# print(student)
# print(student.keys()) #выписывает перед двоеточием
# print(student.values()) #после двоеточия
# print(student.items()) #по парам
# for key, values in student.items():
#     print(f'{key}: {values}')
"""МНОЖЕСТВА set"""
# beshbarmak = {'meat', 'noodle', 'onion'}
# plov = {'meat', "carrot", 'rice'}
# print(beshbarmak, plov)
# print(beshbarmak.difference(plov)) #чем отличается бещ от плова
# print(beshbarmak.intersection(plov)) #что у плова и беш есть связанное
# print(beshbarmak.union(plov)) #выписывает все рецепты
# print(beshbarmak.symmetric_difference(plov)) #выписывает то что непохоже




# numbers = (1, 2, 3, 4, 5, 1) #tuple
# numbers2 = {1, 2, 3, 4, 5, 1} #множества set
# print(numbers)
# print(numbers2)





# while True:
#
#         color = input("введи цвет светофора: ").lower()
#         for i in color:
#             if color == "red" or color == "красный":
#                 print("Стой!")
#             elif color == "yellow" or color == "желтый":
#                 print("подожди!")
#             elif color == "green" or color == "зеленый":
#                 print("вперед!")
#             elif color == "exit" or color == "выход":
#                 print("good bye")
#
#             else:
#                 print("ошибка")
#                 break

"""homework"""
Geeks = {
    'address': 'Toktogula 175',
    'courses': ['Android', 'Backend', 'Frontend'],
    'bag': {'fails', 'errors', 'stack'}
}
Geeks.pop('bag')
Geeks['address'] = 'ibraimova'
Geeks.update({'instagram':'geeks_edu', 'phone number': '0700666550'})
Geeks['courses'] = {'Android', 'Backend', 'Frontend', 'SMM', 'Java', 'Java Script', 'iOS'}

print(Geeks)
print(Geeks['courses'])
print(Geeks.keys())
print(Geeks.values())
print(Geeks.items())
for keys, values in Geeks.items():
    print(f'keys: {keys} v3alues: {values}')