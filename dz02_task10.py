# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, 
# а некоторые – гербом. Определите минимальное число монеток, которые 
# нужно перевернуть, чтобы все монетки были повернуты вверх одной и 
# той же стороной. Выведите минимальное количество монет, которые 
# нужно перевернуть

n=int(input('Введите количество монет N: '))
monet=input('Введите значения для каждой монеты 0(решка) или 1(орел): ')
count=0
for i in range(len(monet)):
    if int(monet[i])==0 or int(monet[i])==1:
        count=count+1

while count!=n:
    if count>n:
        answ=(input(f'Вы ввели больше значений чем задано N. Оставить {count} значений?(Y/N)'))
        if answ=='Y':
            n=count
        else:
            n=int(input('Введите еще раз количество монет N: '))
            monet=input('Введите значения для каждой монеты 0(решка) или 1(орел): ')
            count=0
            for i in range(len(monet)):
                if int(monet[i])==0 or int(monet[i])==1:
                    count=count+1
    else:
        answ=(input(f'Вы ввели меньше значений чем задано N. Оставить {count} значений?(Y/N)'))
        if answ=='Y':
            n=count
        else:
            n=int(input('Введите еще раз количество монет N: '))
            monet=input('Введите значения для каждой монеты 0(решка) или 1(орел): ')
            count=0
            for i in range(len(monet)):
                if int(monet[i])==0 or int(monet[i])==1:
                    count=count+1

reshka=0
orel=0

for i in range(len(monet)):
    if int(monet[i])==0:
        reshka=reshka+1
    if int(monet[i])==1:
        orel=orel+1
if reshka>=orel:
    print(f'Мин перевернуть {orel} монет')
else:
    print(f'Мин перевернуть {reshka} монет')