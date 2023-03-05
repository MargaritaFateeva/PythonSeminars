# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине 
# элемент к заданному числу X. Пользователь в первой строке вводит 
# натуральное число N – количество элементов в массиве. В последующих  
# строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*
# 5
#     1 2 3 4 5
#     6
#     -> 5

from random import randint
n = int(input('Введите число N количество элементов массива: '))
list1=list()
list1=[randint(1, 10) for i in range(n)]
print(*list1)
x = int(input('Введите число X: '))
buf=list1[0]
list2=list()
for i in range(n):
    if abs(x-list1[i])<=abs(x-buf):
        buf=list1[i]
    list2.append(buf)
list3=list()
for i in range(n):
    if abs(x-list2[i])<=abs(x-buf):
        buf=list2[i]
    list3.append(buf)
print('->')
print(*set(list3))