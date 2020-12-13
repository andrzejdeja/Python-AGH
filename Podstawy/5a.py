

class Complex:
    def __init__(self, real, im):
        self.real = real
        self.im = im
    
    def __add__(self, o):
        return Complex(self.real + o.real, self.im + self.im)
        
    def __sub__(self, o):
        return Complex(self.real - o.real, self.im - self.im)
        
    def __mul__(self, o):
        return Complex(self.real*o.real - self.im*o.im, self.im*o.real + self.real*o.im)
    def __eq__(self, o):
        if self.real == o.real and self.im == o.im:
            return True
        else:
            return False
    def __str__(self):
        return str(self.real) + " + " + str(self.im) + "i"
    
    def conjugate(self):
        self.im = -self.im
        
a = Complex(1,-2)
b = Complex(2, 4)
print(a)
a.conjugate()
print(a)
a = a+b
print(a)
a = a-b
print(a)
