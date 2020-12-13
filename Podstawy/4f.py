from random import randrange

#square matrix
a = randrange(3,7)


def wyznacznik(arr, a):
    if a == 1:
        return arr[0]
    det = 0
    for i in range(a):
        tmp = []
        for k in range(1, a):
            for j in range(a):
                if j != i:
                    tmp.append(arr[k * a + j])
        #print(tmp)
        det += wyznacznik(tmp, a - 1)*arr[i]*(-1)**i
    #print(str(det) + " " + str(a))
    return det

arr = []


for i in range(a*a):
    arr.append(randrange(10))
for i in range(a):
    print(arr[i * a:(i + 1) * a])


ans = wyznacznik(arr, a)
print(ans)
