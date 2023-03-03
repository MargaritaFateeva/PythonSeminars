# Задача №11. Решение в группах
# Дано натуральное число A > 1. Определите, каким по
# счету числом Фибоначчи оно является, то есть
# выведите такое число n, что φ(n)=A. Если А не
# является числом Фибоначчи, выведите число -1.
# Input: 5
# Output: 6

# a=int(input('Введите натуральное число больше 1: '))
# while a<2:
#     print('!Ошибка')
#     a=int(input('Введите натуральное число больше 1: '))

# count=3
# f1=0
# f2=1
# buf=1
# fibonacci=f1+f2
# flag=True
# while flag==True:
#     if a==fibonacci:
#         flag=False
#         print(count)
#     elif a!=fibonacci and a<buf:
#         flag=False
#         print('-1')
#     count=count+1
#     buf=fibonacci
#     fibonacci=fibonacci+f2
#     f1=f2
#     f2=buf

n = int(input())
i = 2
a = 0
b = 0
c = 1
while a < n:
    a = b + c
    b = c
    c = a
    i += 1
    if a > n:
        i = 0
        if i == 0:
            print(-1)
        else:
            print(i)






