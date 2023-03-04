# Дана последовательность из N целых чисел и число K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K – положительное число.

# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]

list =[2, 3, 5, 6, 8, 9, 5]
k = int(input('Введите k: '))
print(list[-k:len(list)] + list[:-k]) # срезы списка

from random import randint
list_1 = [randint(-3, 6) for i in range(1, 9)]
print(list_1)


lst = [1, 2, 3, 4, 5]
k = 2
for i in range(k):
    lst.insert(0, lst.pop(-1))
print(lst)
