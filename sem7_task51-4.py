# Написать функцию, которая принимает список строк и возвращает список строк, 
# содержащих только одно слово, с использованием лямбда-функции:

lst=['tyrrytu', 'ytut uiy fghf', 'fghfh qwe zxcv', 'sdfghjk hjk']
lst2=list(filter(lambda x: len(x.split()) == 1,lst))
print(lst2)