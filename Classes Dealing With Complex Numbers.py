import math
from unittest import result

class Complex(object):
    def __init__(self,Real,Imaginary):
        self.Real = Real
        self.Imaginary = Imaginary

    def __add__(self,no):
        self.i =  self.Real + no.Real
        self.j = self.Imaginary + no.Imaginary
        result = self.__str__()
        return result

    def __sub__(self,no):
        self.i =  self.Real - no.Real
        self.j = self.Imaginary - no.Imaginary
        result = self.__str__()
        return result

    def __mul__ (self,no):
        comp1 =  complex(self.Real , self.Imaginary)
        comp2 =  complex(no.Real , no.Imaginary)
        comp = comp1 * comp2
        self.i = comp.real
        self.j = comp.imag
        result = self.__str__()
        return result

    def __truediv__ (self,no):
        comp1 =  complex(self.Real , self.Imaginary)
        comp2 =  complex(no.Real , no.Imaginary)
        comp = comp1 / comp2
        self.i = comp.real
        self.j = comp.imag
        result = self.__str__()
        return result

    def mod(self):
        self.i =  math.sqrt(self.Real**2 + self.Imaginary**2)
        self.j = 0
        result = self.__str__()
        return result
    
    def __str__(self):
        if self.j == 0:
            result = "%.2f+0.00i" % (self.i)
        elif self.i == 0:
            if self.j >= 0:
                result = "0.00+%.2fi" % (self.j)
            else:
                result = "0.00-%.2fi" % (abs(self.j))
        elif self.j > 0:
            result = "%.2f+%.2fi" % (self.i, self.j)
        else:
            result = "%.2f-%.2fi" % (self.i, abs(self.j))
        return result

    


if __name__ == '__main__':
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x+y, x-y,x*y, x.mod(), y.mod()]), sep='\n')


# x = 2 + 1j
# y = 5 + 6j
# print(x.Real,x.imag)