import threading
import time

class Widelec:
    def __init__(self, nr):
        self.nr = nr
        self.user = -1
    
    def pickup(self, user):
        if (self.user == -1):
            self.user = user
            return True
        else:
            return False
       
    def putdown(self, user):
        if (self.user == user):
            self.user = -1
            return True
        else:
            return False

class Filozof:
    def __init__(self, nr, left, right):
        self.nr = nr
        self.left = left
        self.right = right
        
def run(f):
    i = 3
    while i > 0:
        with sema:
            try:
                if not f.right.pickup(f.nr):
                    raise Exception("Right pickup failed")
                time.sleep(0.01)
                if not f.left.pickup(f.nr):
                    raise Exception("Left pickup failed")
                print(f.nr, ": ate")
                i -= 1
            except Exception as err:
                pass
                #print(f.nr, ": ", err)
            finally:
                f.left.putdown(f.nr)
                f.right.putdown(f.nr)
                time.sleep(0.1)

sema = threading.BoundedSemaphore(4) #n-1

th = []
w = [Widelec(i) for i in range(5)]
f = [Filozof(i, w[i], w[(i+1)%5]) for i in range(5)]
for i in range(5):
    th.append(threading.Thread(target=run, args=(f[i],)))
start_time = time.time()
for i in range(5):
    th[i].start()
for i in range(5):
    th[i].join()
print(time.time() - start_time)



