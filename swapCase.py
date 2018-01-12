def swap_case(s):
    n = ''
    for i in s:
        if i.isalpha() and i.isupper():
            n = n + i.lower()
        elif i.isalpha() and i.islower():
            n = n + i.upper()
        '''else:
            n = n + i'''
    return n

s = input()
result = swap_case(s)
print(result)
