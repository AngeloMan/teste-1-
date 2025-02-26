# For this challenge, you are given two complex numbers, and you have to print the result of their addition,
# subtraction, multiplication, division and modulus operations.
# The real and imaginary precision part should be correct up to two decimal places.
import math
class Complex(object):
    def __init__(self, real, imaginary):
       ... 
       self.real = real
       self.imaginary = imaginary
    def __add__(self, no):
        real = self.real + no.real
        imaginary = self.imaginary + no.imaginary
        result = Complex(real=real, imaginary=imaginary)
        return result
        ... 
    def __sub__(self, no):
        ...
        real = self.real - no.real
        imaginary = self.imaginary - no.imaginary
        result = Complex(real=real, imaginary=imaginary)
        return result
    def __mul__(self, no):
        ...
        real = (self.real * no.real) - (self.imaginary * no.imaginary)
        imaginary = (self.real * no.imaginary) + (self.imaginary * no.real)
        result = Complex(real=real, imaginary=imaginary)
        return result
    def __truediv__(self, no):
        ...
        imaginary = (self.imaginary - ((self.real * no.imaginary)/no.real))/((no.imaginary**2/no.real)+no.real)
        real = (self.real + (no.imaginary * imaginary))/no.real
        result = Complex(real, imaginary)
        return result
    def mod(self):
        module = ((self.real**2)+(self.imaginary**2))**0.5
        result = Complex(module, 0)
        return result
    def __str__(self):
        if self.imaginary == 0:  
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result

if __name__ == '__main__':
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]), sep='\n')