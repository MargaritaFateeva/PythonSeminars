# Задача 14: Требуется вывести все целые степени двойки 
# (т.е. числа вида 2k), не превосходящие числа N.

n = int(input('Введите число N: '))
for i in range(n):
    a=2**i
    if a<n:
        print(f'{i} - 2**{i}={2**i}')