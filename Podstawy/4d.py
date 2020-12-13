from random import randrange

a = 128
b = 128
arr1 = []
arr2 = []

for i in range(a*b):
    arr1.append(randrange(100))
    arr2.append(randrange(100))
#print(arr1)
#print(arr2)
for i in range(a*b):
    arr1[i] += arr2[i]
#for i in range(a):
#    print(arr1[i * a:(i + 1) * a])
