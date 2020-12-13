

class Complex:
    def __init__(self, real, im = None):
        if isinstance(real, int) or isinstance(real, float):
            self.real = real
            self.im = im
        elif isinstance(real, str):
            parts = real.partition("+")
            parts2 = []
            if parts[1] == "+":
                self.real = float(parts[0])
                parts2 = parts[2].partition("i")
            else:
                self.real = 0
                parts2 = parts[0].partition("i")
            if parts2[0].isdecimal() and parts2[1] == "i" and parts2[2] == "":
                self.im = float(parts2[0])
            else:
                self.im = 0
            
        
    def __add__(self, o):
        return Complex(self.real + o.real, self.im + o.im)
        
    def __sub__(self, o):
        return Complex(self.real - o.real, self.im - o.im)
        
    def __mul__(self, o):
        return Complex(self.real*o.real - self.im*o.im, self.im*o.real + self.real*o.im)
    def __eq__(self, o):
        if self.real == o.real and self.im == o.im:
            return True
        else:
            return False
    def __str__(self):
        if self.im == 0:
            return str(self.real)
        elif self.im > 0:
            return str(self.real) + "+" + str(self.im) + "i"
        return str(self.real) + str(self.im) + "i"
    
    def conjugate(self):
        self.im = -self.im
        
def isComplex(str):
    parts = str.partition("+")
    parts2 = []
    if parts[1] == "+":
        parts2 = parts[2].partition("i")
    else:
        parts2 = parts[0].partition("i")        
    if parts2[0].isdecimal() and parts2[1] == "i" and parts2[2] == "":
        return True
    else:
        return False

def compute(data):
    data = str(data)
    if data.isdecimal():
        return Complex(float(data), 0)
    elif isComplex(data):
        return Complex(data)
    for s in ("+", "-", "*"):
        parts = data.partition(s)
        if parts[1] == "*": 
            return compute(parts[0]) * compute(parts[2])
        elif parts[1] == "-":
            return compute(parts[0]) - compute(parts[2])
        elif parts[1] == "+":
            return compute(parts[0]) + compute(parts[2]) 
           
print("Podaj dzialanie - bez () / - przykladowo:")
data = "1*2-3*4i+5+6*7i-8i*9"
print(data)
print(compute(data))           
            
while True:
    print("Podaj dzialanie")
    data = input()
    print(compute(data))
    
    
