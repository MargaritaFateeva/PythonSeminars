# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, 
# с повторениями). Выдать без повторений в порядке возрастания все те числа, 
# которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. 
# m - кол-во элементов второго множества. 
# Затем пользователь вводит сами элементы множеств.
# 11 6 
# 2 4 6 8 10 12 10 8 6 4 2 
# 3 6 9 12 15 18 
# 6 12


from random import randint
count_el = [input('Введите N: '),input('Введите M: ')]
print(*count_el)
list_n=[]
list_m=[]
list_n=[randint(1, 12) for i in range(int(count_el[0]))]
list_m=[randint(1, 12) for i in range(int(count_el[1]))]
print(*list_n)
print(*list_m)
set_n=set(list_n)
set_m=set(list_m)
isect = set_n.intersection(set_m)
uncount1=list(isect)
result=[]
uncount=uncount1
if len(uncount1)<=1:
    result=uncount1   
else:
    buf=uncount[0]
    count=0
    while len(result)<len(isect) and len(uncount)>=1:
        buf=uncount[0]
        count=0
        for i in range(len(uncount)):
            if buf>uncount[i]:
                buf=uncount[i]
                count=i
        result.append(buf)
        uncount.pop(count)
    print(f'->{result}')