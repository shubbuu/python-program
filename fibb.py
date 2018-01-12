#!/usr/bin/env python3
n = int(input("Enter number of terms : "))
a, b = 1, 1
i = 0
while i < n:
    if i == 0:
        print("%d "%a)
    elif i == 1:
        print("%d "%b)
    else:
        print(a + b)
        t = a
        a = b
        b = a + t
    i += 1
    