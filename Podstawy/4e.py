from random import randrange

#square matrix
a = 8

arr1 = []
arr2 = []
arr3 = []

for i in range(a*a):
    arr1.append(randrange(10))
    arr2.append(randrange(10))
    arr3.append(0)
print("Arr1:")
for i in range(a):
    print(arr1[i * a:(i + 1) * a])
print("Arr2:")
for i in range(a):
    print(arr2[i * a:(i + 1) * a])


for i in range(a):
    for j in range(a):
        for k in range(a):
            arr3[i * a + j] += arr1[i * a + k] * arr2[k * a + j]
print("Ans:")
for i in range(a):
    print(arr3[i * a:(i + 1) * a])
