from random import randrange
def mergesort_dec(list):
    if len(list) > 1:
        
        middle = len(list)//2
        L = list[:middle]
        R = list[middle:]
        
        mergesort_dec(L)
        mergesort_dec(R)
        
        i = j = k = 0
        
        while i < len(L) and j < len(R):
            if L[i] > R[j]:
                list[k] = L[i]
                i += 1
            else:
                list[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            list[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            list[k] = R[j]
            j += 1
            k += 1
    return list

list = []
for e in range(50):
    list.append(randrange(1000))
#print(list)
list2 = list.copy()
list.sort()
list.reverse()
#print(list)
list2 = mergesort_dec(list2)
print(list2)
if list == list2:
    print("OK")
