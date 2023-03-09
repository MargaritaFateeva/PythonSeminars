# Задача №25. Решение в группах Напишите программу, которая принимает 
# на вход строку, и отслеживает, сколько раз каждый символ уже встречался. 
# Количество повторов добавляется к символам с помощью постфикса формата _n. 
# Input: a a a b c a a d c d d 
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2 
# Для решения данной задачи используйте функцию .split()

list1='a a a b c a a d c d d'
set1=set(list1)
set1.remove(' ')
el=list(set1)
print(list1)
count = -1
result=[]
a=1
while a<=len(list1):
    for i in range(len(list1[:a])):
        for j in range(len(el)):
            if list1[i]==el[j]:
                count+=1
    if list1[:a].count(list1[:a][i])>1 and list1[i]!=" ":
        result.append(str(list1[i])+ '_'+ str(list1[:a].count(list1[:a][i])-1)+' ')
    elif list1[:a].count(list1[:a][i])==1 and list1[i]!=" ":
        result.append(str(list1[i]))
    a+=1        
print(*result)

first = 'a a a b c a a d c d d'
second = first.split()
third = []
for i in range(len(second)):
    if second[:i+1].count(second[i]) == 1:
        third.append(second[i])
    else:
        third.append(second[i] + '_' + str(second[:i].count(second[i])))
print(third)

first = 'a a a b c a a d c d d'
second = first.split()
for i in range(len(second)):
    if second[:- i - 1].count(second[- i - 1]) >= 1:
        second[- i - 1] = second[- i - 1] + '_' + str(second[:- i - 1].count(second[- i - 1]))
print(second)

string = str.upper('a a a b c a a d c d d')
print(string)
new_string = (string.split())
result = {}
for i in new_string:
    if i in result:
        print(f'{i}_{result[i]}', end=' ')
    else:
        print(i, end=' ')
    result[i] = result.get(i, 0) + 1
