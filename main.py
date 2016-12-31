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
        self.f1 = Lambda((x, y), self.uDiffx)
        self.f2 = Lambda((x, y), self.vDiffy)
        self.f3 = Lambda((x, y), self.uDiffy)
        self.f4 = Lambda((x, y), -self.vDiffx)
        if (self.f1 == self.f2 and self.f3 == self.f4):
            return 1

        # elif age
        else:
            return 0

    def complexDiff(self):
        complexNum.eachDiff(self)
        checker = bool(int(input(
            "to calculate diff on a particular point enter \'0\' or calculate as symbolic number enter \'1\'?")))
        if checker == 1:
            # if (1):
            if (complexNum.checkDiff(self)):
                return (self.uDiffx + self.vDiffx * I)
            else:
                return ("It had'nt condition survey on Cauchy-Riemann")
        elif checker == 0:

            complexNum.setSymbols(self)

    def setSymbols(self):
        self.x = int(input("enter x value: "))
        self.y = int(input("enter y value: "))
        f = Lambda((x, y), self.cNum)
        return (f(self.x, self.y))

    def printNum(self):
        print(self.cNum)

    def getSettedSymbolValue(self):
        complexNum.setSymbols(self)
        # complexNum.print(self)

        # def __mul__(self, other):
        #     return (self.u * other.u + self.u * other.v * I + self.v * other.u * I - self.v * other.v)
        #
        # def __add__(self, other):
        #     return (self.u + other.u + self.v * I + other.v * I)
        #
        # def __sub__(self, other):
        #     return (self.u - other.u + self.v * I - other.v * I)  # class normalNum(object):


# def __init__(self, obj):
#         self.num = obj
#
#     def __mul__(self, other):
#         self.num * other.num
#
#     def __add__(self, other):
#         sef.num + other.num
#
#     def __sub__(self, other):
#         self.num - other.num
#
#     def __rdiv__(self, other):
#         self.num / other.num


x, y, c = symbols('x y c', real=True)


# b = sympify(input())
# print(type(b))
# b = complexNum(sympify(input()))
# b.printNum()
#
class text:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


whichcase = int(input(text.BOLD + "which proccese do you want to do?\n" + text.ENDC
                      + text.OKGREEN + "1- differential of normal number\n"
                                       "2- differential of complex number\n" + text.ENDC
                      + text.OKBLUE + "3- integral of normal number\n"
                                      "4- integral of complex number" + text.ENDC))


# bug: Cauchy-Riemann sufficient conditions checker: when we should equation the function
