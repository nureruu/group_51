# animals = ['cat','dog','horse']
# fruits = ['apple','banana']
# for ani in animals:
#     for fr in fruits:
#         print(f'{ani} loves {fr}')
#
#
# num = 0
# while num < len(animals):
#     for fr in fruits:
#         print(fr)
#
#     for ani in animals:
#         print(ani)
#         num += 1
#     #O((F + A) * A) = > O(FA + A ** 2)  алгоритм данного кода
#
#
#     def counter(n):
#         print(n)
#         if n > 0:
#             counter(n-1)
#     counter(3)
#     # функция stack грокаем алгоритм- книга


# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n-1)



# HOMEWORK binary search
def search(n, val):
    n = 5000
    resultOk =False
    First = 0
    Last = n - 1
    Pos = -1
    while First < Last:
        Middle = (First+ Last) / 2
        if val == A[Middle]:
            First = Middle
            Last = First
            resultOk = True
            Pos = Middle
            break
        elif val > A[Middle]:
            First = Middle + 1
        else:
            Last = Middle - 1

        if resultOk == True:
            print("Элемент найден!")

        else:
            print("Элемент не найден!")
            break
n = [12,33,788,3,222,4,9,4]
val = [4]
print(search(n, val))

# selection search
def selection_search(n):
    arr = len(n)
    for i in range(arr):
        smallest = 1
        for j in range(i+1, arr):
            minimum = 1
            if j < smallest:
                j = smallest
                n[i], n[smallest] = n[minimum], n[i]

n = [8, 3, 6, 3, 2, 4, 9]
selection_search(n)
print(n)
#fsf