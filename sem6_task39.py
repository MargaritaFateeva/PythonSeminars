# Задача №39. Решение в группах Даны два массива чисел. Требуется вывести 
# те элементы первого массива (в том порядке, в каком они идут 
# в первом массиве), которых нет во втором массиве. Пользователь вводит  
# число N - количество элементов в первом массиве, затем N чисел - 
# элементы массива. Затем число M - количество элементов во втором массиве. 
# Затем элементы второго 
# Ввод: 
# 7 
# 3 1 3 4 2 4 12 
# 6 
# 4 15 43 1 15 1 
# Вывод: 3 3 2 12 массива (каждое число вводится с новой строки)

n = int(input('Количество элементов a: '))
a = [input() for i in range(n)]
m = int(input('Количество элементов b: '))
b = [input() for i in range(m)]
result = list(set(a) - set(b))

print(a)
print(b)
print(result)

n = int(input('Введите количество элементов первого массива: '))
lst_one = [int(input(f'введите элемент второго массива {i}: ')) for i in range(n)]
m = int(input('Введите количество элементов второго массива: '))
lst_two = [int(input(f'введите элемент второго массива {i}: ')) for i in range(m)]

for i in range(len(lst_one)):
    if lst_one[i] not in lst_two:
        print(lst_one[i], end = ' ')