# Задача №33. Решение в группах 
# Хакер Василий получил доступ к классному журналу и хочет заменить 
# все свои минимальные оценки на максимальные. Напишите программу, 
# которая заменяет оценки Василия, но наоборот: все максимальные 
# – на минимальные. 
# Input: 5 -> 1 3 3 3 4 
# Output: 1 3 3 3 1

# def quicksort(array): 
#     if len(array) < 2: 
#         return array 
#     else: 
#         pivot = array[0] 
#         less = [i for i in array[1:] if i <= pivot] 
#         greater = [i for i in array[1:] if i > pivot] 
#         return quicksort(less) + [pivot] + quicksort(greater) 

# arr=[1,3,3,3,4]
# a=quicksort(arr)
# print(a)

from random import randint

def change_list(lst):
    max_val = max(lst)
    for i in range(len(lst)):
        if lst[i] == max_val:
            lst[i] = 1
    return lst

n = int(input('Введите длину списка: '))
marks = [randint(1, 5) for i in range(n)]
print('Исходный список:', marks)
marks = change_list(marks)
print('Измененный список:', marks)
