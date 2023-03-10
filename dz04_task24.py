# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. 
# Она растет на круглой грядке, причем кусты высажены только по окружности. 
# Таким образом, у каждого куста есть ровно два соседних. Всего на грядке 
# растет N кустов. Эти кусты обладают разной урожайностью, поэтому ко времени 
# сбора на них выросло различное число ягод – на i-ом кусте выросло 
# РАНДОМНОЕ колличество ягод. В этом фермерском хозяйстве внедрена система 
# автоматического сбора черники. Эта система состоит из управляющего модуля 
# и нескольких собирающих модулей. Собирающий модуль за один заход, находясь 
# непосредственно перед некоторым кустом, собирает ягоды с этого куста и 
# с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, 
# которое может собрать за один заход собирающий модуль, находясь перед 
# некоторым кустом заданной во входном файле грядки.
# 4 -> 1 2 3 4 
# 9

from random import randint
n = int(input('Введите число N количество кустов: '))
list_n=[randint(1, 10) for i in range(n)]
print(f'{n} -> {list_n}')
lst=list_n
k = 1
cnt=[sum(lst[:3])]
while len(cnt)<n:
    for i in range(k):
        lst.insert(0, lst.pop(-1))
    cnt.append(sum(lst[:3]))
buf=cnt[0]
for i in range(len(cnt)):
    if buf<cnt[i]:
        buf=cnt[i]
print(buf)