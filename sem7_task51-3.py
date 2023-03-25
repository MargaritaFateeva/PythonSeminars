# Дан список, вывести отдельно буквы и цифры.
# a = ( "a", 'b', '2', '3' ,'c')
# b = ( 'a' , 'b' , 'c')
# c = ( '1', '2', '3')

# a=input().split()
# b=[i for i in a if i.isdigit()==False]
# c=[i for i in a if i.isdigit()==True]
# print(b)
# print(c)

a = ( "a", 'b', '2', '3' ,'c')
# b = ( 'a' , 'b' , 'c')
# c = ( '1', '2', '3')
b= filter(str.isalpha, a)
c= filter(str.isdigit, a)
print(*b)
print(*c)
