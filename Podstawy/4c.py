from random import randrange

a = [1, 2, 12, 4]
b = [2, 4, 2, 8]

if len(a) != len(b):
    print("err")
else:
    res = 0
    for i in range(len(a)):
        res += a[i] * b[i]
    print(res)

