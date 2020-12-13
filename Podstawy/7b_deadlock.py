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
    for i in range(3):
        while True:
            if f.right.pickup(f.nr):
                break
            print(str(f.nr) + ": Right pickup failed")
            time.sleep(1)
        time.sleep(0.1)
        while True:
            if f.left.pickup(f.nr):
                break
            print(str(f.nr) + ": Left pickup failed")
            time.sleep(1)
        f.left.putdown(f.nr)
        f.right.putdown(f.nr)
        print(str(f.nr) + " ate")



th = []
w = [Widelec(i) for i in range(5)]
f = [Filozof(i, w[i], w[(i+1)%5]) for i in range(5)]
for i in range(5):
    th.append(threading.Thread(target=run, args=(f[i],)))
    th[i].start()
for i in range(5):
    th[i].join()


