# Дан словарь my_dict и ключ my_key. Напишите код, который проверяет, 
# есть ли ключ my_key в словаре my_dict, и если да, то возвращает 
# соответствующее значение, а если нет, то возвращает значение по умолчанию None.

my_dict = {'a': 1, 'b': 2, 'c': 3}
my_key = 'b'
my_value = my_dict.get(my_key, None)
print(my_value) # 2

# Дан словарь my_dict и ключ my_key. Напишите код, который проверяет, 
# есть ли ключ my_key в словаре my_dict, и если да, то возвращает 
# соответствующее значение, а если нет, то создает новый элемент в словаре 
# с ключом my_key и значением 0, а затем возвращает 0.

my_dict = {'a': 1, 'b': 2, 'c': 3}
my_key = 'd'
my_value = my_dict.get(my_key, 0)
if my_value==0:
    my_dict[my_key]=my_value
print(my_value)
print(my_dict)