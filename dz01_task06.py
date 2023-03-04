# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы 
# расплачивались за проезд и получали билет с номером. 
# Счастливым билетом называют такой билет с шестизначным номером, 
# где сумма первых трех цифр равна сумме последних трех. 
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. 
# Вам требуется написать программу, которая проверяет счастливость билета.
# *Пример:*
# 385916 -> yes
# 123456 -> no

n=int(input('Введите номер билета: '))
while (n > 999999 or n<100000):
    print('!ошибка')
    n=int(input('Введите положительное 6-значное число: '))
else:
    s1=n//1000                     # первая половина номера билета
    s2=n-(n//1000)*1000            # вторая половина номера билета

    a1=s1//100                                      # число 1 в билете
    b1=(s1-(s1//100*100))//10                       # число 2 в билете
    c1=s1-(s1//100)*100-((s1-(s1//100*100))//10)*10 # число 3 в билете
    a2=s2//100                                      # число 4 в билете
    b2=(s2-(s2//100*100))//10                       # число 5 в билете
    c2=s2-(s2//100)*100-((s2-(s2//100*100))//10)*10 # число 6 в билете
    
    if a1+b1+c1==a2+b2+c2:
        print(f'{n} -> YES')
    else:
        print(f'{n} -> NO')
