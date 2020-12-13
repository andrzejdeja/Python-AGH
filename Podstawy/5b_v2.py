class Complex:
    def __init__(self, real, im = None):
        if isinstance(real, int) or isinstance(real, float):
            self.real = real
            self.im = im
        elif isinstance(real, str):
            real_s = 1    
            if real[0] == "-":
                real_s = -1
                real = real.strip("-")
            parts = real.partition("+")
            parts2 = []
            if parts[1] == "+":
                self.real = float(parts[0])
                parts2 = parts[2].partition("i")
            else:
                parts = real.partition("-")
                if parts[1] == "-":
                    parts2 = parts[2].partition("i")
                    self.real = float(parts[0])
            if parts2[0].isdecimal() and parts2[1] == "i" and parts2[2] == "":
                self.im = float(parts2[0])
            else:
                self.im = 0
            if parts[1] == "-":
                self.im *= -1
            self.real *= real_s
        
    def __add__(self, o):
        return Complex(self.real + o.real, self.im + o.im)
        
    def __sub__(self, o):
        return Complex(self.real - o.real, self.im - o.im)
        
    def __mul__(self, o):
        return Complex(self.real*o.real - self.im*o.im, self.im*o.real + self.real*o.im)
        
    def __truediv__(self, o):
        return Complex(((self.real*o.real) + (self.im*o.im)) / ( o.real**2 + o.im**2 ), ((self.im*o.real) - (self.real*o.im)) / ( o.real**2 + o.im**2 ))
    
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
        

def isComplex2(str):
    if str[0] == "-":
        str = str.strip("-")
    parts = str.partition("+")
    parts2 = []
    if parts[1] == "+":
        parts2 = parts[2].partition("i")
    else:
        parts = str.partition("-")
        if parts[1] == "-":
            parts2 = parts[2].partition("i")        
        else:
            return False
    if parts2[0].isdecimal() and parts2[1] == "i" and parts2[2] == "":
        return True
    else:
        return False
           
def compute1(data):
    parts = data.partition("*")
    if parts[1] == "*":
        return compute2(parts[0]) * compute2(parts[2])
    else:
        parts = data.partition("/")
        if parts[1] == "/":
            return compute2(parts[0]) / compute2(parts[2])
        else:
            return float("nan")
        
def compute2(data):
    data = data.strip("()")
    if isComplex2(data):
        return Complex(data)
    else:
        return float("nan")
     
      
print("Podaj dzialanie w zapisie: (a+-bi)*/(c+-di)")
data = "(-2-3i)*(4+5i)"
print(data)
print(compute1(data)) 
data = "(2-3i)/(-4+5i)"
print(data)
print(compute1(data))
            
while True:
    print("Podaj dzialanie")
    data = input()
    print(compute1(data))
    
    
