from sympy import *


class complexNum(object):
    def __init__(self, complexNum):
        self.realImag = complexNum.as_real_imag()
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
        if (1):
            return (self.uDiffx + self.vDiffx * I)
        else:
            return ("It had'nt condition survey on Cauchy-Riemann")

    def setSymbols(self):
        f = Lambda((x, y), complexNum)
        return (f(1, 2, 3, 4))

    def getSettedSymbolValue(self):
        self.setSymbol(complexNum)


x, y, c = symbols('x y c', real=True)
a = complexNum(x ** 2 + y ** 2 + 2*I)
print(a.complexDiff())

# bug: Cauchy-Riemann sufficient conditions checker
# bug: have error if we have'nt any symbol on real or imag of complex number