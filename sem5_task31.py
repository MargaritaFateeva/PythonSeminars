# Задача №31. Решение в группах Последовательностью Фибоначчи 
# называется последовательность чисел a0 , a1 , ..., an , ..., 
# где a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1). 
# Требуется найти N-е число Фибоначчи 
# Input: 7 
# Output: 21 
# Задание необходимо решать через рекурсию

def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-2)+fibonacci(n-1)

a=int(input('введите целое число: '))    
print(fibonacci(a))

