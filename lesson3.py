# number = 5
# print(number)
# number += 2
# number -= 1
# number /= 2
# number **= 2
# number %= 4
# print(number)
#
# #циклы повторяющиеся действия
# indefinite неопределенный

# n = 5
# while n > 0:
#     print(n)
#     n -= 1
#     if n == 3:
#         continue-игнорит

# counter = 0
# while counter < 10:
#     counter += 1
#     time = input(f'enter time: ({counter}) or exit: ').lower()
#     if time == "exit":
#         break
#     if time == "morning" or time =="утро":
#         print("good morning")
#     elif time =="day":
#         print("good afternoon")
#     elif time == "evening":
#         print("good evening")
#     else:
#         print("ошибка")
# for перебирает все цифры

# word = "kyrgyzstan"
# i = index
# for i in word:
#
#     if i == "s":
#         break
#     if i not in "kg":
#         continue
#     print(i)
#
vowels = "аАоОеЕуУыЫяЯиИэЭюЮeEyYuUiIoOaA"
while True:
    word = input("write your word: ")
    print(word)

    if word == "exit" or word == "выход":
        print("good bye")
        break
    total_letters = 0
    vowel_letters = 0
    consonant_letters = 0
    for i in word:
        total_letters += 1
        if i in vowels:
          vowel_letters += 1
        else:
            consonant_letters += 1
        if vowel_letters > 0:
            vowel_percentage = (total_letters / vowel_letters) * 100
        else:
            vowel_percentage = 0
        if consonant_letters > 0:
            consonants_percentage = (total_letters / consonant_letters) * 100
        else:
           consonants_percentage = 0
        print(f'vowel: {vowel_letters} consonants: {consonant_letters} '
                  f'total: {total_letters} vowel_percentage: {vowel_percentage} consonant_percentage: {consonants_percentage}')
