# Задача 34: Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку
# разобраться в его кричалках не настолько просто, насколько легко он их придумывает, 
# Вам стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов 
# (т.е. число гласных букв) в каждой фразе стихотворения одинаковое. Фраза может 
# состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами. 
# Фразы отделяются друг от друга пробелами. Стихотворение Винни-Пух вбивает в программу 
# с клавиатуры. В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и 
# “Пам парам”, если с ритмом все не в порядке
# Ввод: 
# пара-ра-рам рам-пам-папам па-ра-па-дам 
# Вывод:
# Парам пам-пам

winni = 'пара-ра-рам рам-пам-папам па-ра-па-дам'
print(winni)
lst_glasn=['а','e','ё','и','о','у','ы','э','ю','я']
lst=[list(str(i)) for i in list(winni.split())]
#print(lst)
win_glasn=[]
for i in range(len(lst)):
    count=0
    for j in lst[i]:
        if j in lst_glasn:
            count+=1
    win_glasn.append(count)
#print(win_glasn)

if len(list(filter(lambda x : x==win_glasn[0], win_glasn)))==len(win_glasn):
    print('Парам пам-пам (с ритмом все в порядке)')
else:
    print('Пам парам (с ритмом все не в порядке)')