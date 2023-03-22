# Задача №43. Решение в группах Дан список чисел. 
# Посчитайте, сколько в нем пар элементов, равных друг другу. 
# Считается, что любые два элемента, равные друг другу образуют одну пару, 
# которую необходимо посчитать. Вводится список чисел. Все числа списка 
# находятся на разных строках. 
# Ввод:
# 1 2 3 2 3
# Вывод: 
# 2

n = int(input('Количество элементов: '))
a = [input() for i in range(n)]
counter = 0
for i in range(n):
    for j in range(i + 1, n):
        if a[i] == a[j]:
            counter += 1
print('Количество пар:', counter)

# проверка индексов

import random as rd
r = int(input('Введите количество элементов массива: '))
lst_rnd = [rd.randint(0,10) for i in range(r)]

ecsept_index = []
count = 0

print(lst_rnd)

for i in range(r - 1):
    for j in range(i + 1, r):
        if lst_rnd[i] == lst_rnd[j] and j not in ecsept_index and i not in ecsept_index:
            count += 1
            ecsept_index.append(i)
            ecsept_index.append(j)
            print(f'{lst_rnd[i]}(индекс {i}), {lst_rnd[j]}(индекс {j})')
print(f'Всего пар : {count}')