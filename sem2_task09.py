# Задача №9. Решение в группах
# По данному целому неотрицательному n вычислите
# значение n!. N! = 1 * 2 * 3 * … * N (произведение всех
# чисел от 1 до N) 0! = 1 Решить задачу используя цикл while.
# Input: 5
# Output: 120

# n=int(input('Введите неотрицательное число N: '))
# while n<0:
#     print('!Ошибка число меньше 0')
#     n=int(input('Введите неотрицательное число N: '))

# factorial=1
# count=1
# while count<n+1:
#     factorial=factorial*count
#     count=count+1
# print(f'{n}!={factorial}')

n=int(input('Введите число N: '))
f=1
while n>1:
    f=f*n
    n-=1
print (f)