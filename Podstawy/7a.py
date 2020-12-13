import threading
import time
from PIL import Image

def run(arr):
    tmp = [0] * 256
    for i in range(len(arr)):
        tmp[arr[i]] += 1
    with sema:
        for i in range(len(res)):
            res[i] += tmp[i]

sema = threading.BoundedSemaphore(1) #n-1

th = []

try:
    path = "IMG_0001.jpg"
    image = Image.open(path).convert(mode="L").tobytes() #to gray scale
except OSError:
    print("OSError")
    
print(len(image), "bytes")
res = [0] * 256
nothreads = 8
chunk_size = len(image)//nothreads
for i in range(nothreads-1):
    th.append(threading.Thread(target=run, args=(image[i*chunk_size:(i + 1)*chunk_size],)))
th.append(threading.Thread(target=run, args=(image[(nothreads - 1)*chunk_size:],)))
start_time = time.time()
for i in range(nothreads):
    th[i].start()
for i in range(nothreads):
    th[i].join()
end_time = time.time()

for i in range(len(res)):
    print(i, ":", res[i])
print("Run time:", end_time - start_time)

res1 = [0] * 256 #test
start_time = time.time()
for i in range(len(image)):
        res1[image[i]] += 1
print("Test time:", time.time() - start_time)
print(res1 == res)



