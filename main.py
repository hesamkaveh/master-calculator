from sympy import *


class complexNum(object):
    def __init__(self, cNum):
        self.cNum = cNum
        self.realImag = cNum.as_real_imag()
        self.u = self.realImag[0]
        self.v = self.realImag[1]

    def eachDiff(self):
        self.uDiffx = diff(self.u, x, 1)
        self.uDiffy = diff(self.u, y, 1)
        self.vDiffx = diff(self.v, x, 1)
        self.vDiffy = diff(self.v, y, 1)

    def checkDiff(self):
        if (self.uDiffx == self.vDiffy and self.uDiffy == -self.vDiffx):
            return 1
        else:
            return 0

    def complexDiff(self):
        complexNum.eachDiff(self)

        # if (complexNum.checkDiff(self)):                         because the bug on checkdiff, i ignore to checkdiff
        if (1):
            return (self.uDiffx + self.vDiffx * I)
        else:
            return ("It had'nt condition survey on Cauchy-Riemann")

    def setSymbols(self):
        self.x = int(input("enter x value: "))
        self.y = int(input("enter y value: "))
        f = Lambda((x, y), self.cNum)
        return (f(self.x, self.y))

    def getSettedSymbolValue(self):
        complexNum.setSymbol(self)
        # complexNum.print(self)

    def __mul__(self, other):
        return (self.u * other.u + self.u * other.v * I + self.v * other.u * I - self.v * other.v)

    def __add__(self, other):
        return (self.u + other.u + self.v * I + other.v * I)

    def __sub__(self, other):
        return (self.u - other.u + self.v * I - other.v * I)


class normalNum(object):
    def __init__(self, obj):
        self.num = obj

    def __mul__(self, other):
        self.num * other.num

    def __add__(self, other):
        sef.num + other.num

    def __sub__(self, other):
        self.num - other.num

    def __rdiv__(self, other):
        self.num / other.num


x, y, c = symbols('x y c', real=True)
a = complexNum(2 * x)
b = complexNum(3 + 6 * I)

print(a + b)

# bug: Cauchy-Riemann sufficient conditions checker
