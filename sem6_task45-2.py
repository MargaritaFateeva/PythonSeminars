# при помощи рекурсии определить является ли слово палиндромом

slovo_a=input()

def pal(slovo):
    if slovo[0]==slovo[-1] and len(slovo)>2:
        return pal(slovo[1:-1])
    elif slovo[0]!=slovo[-1]:
        return 'no'
    return 'yes'

print(pal(slovo_a))





def is_palindrome(word):
    if len(word) < 2:
        return True
    elif word[0] != word[-1]:
        return False
    else:
        return is_palindrome(word[1:-1])