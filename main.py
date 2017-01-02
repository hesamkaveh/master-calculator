from sympy import *


class complexNum(object):
    def __init__(self, cNum):
        self.cNum = cNum
        self.realImag = cNum.as_real_imag()
        self.u = self.realImag[0]
        self.v = self.realImag[1]

    def complexIntegral(self):
        self.func = complexNum(
            sympify(input('enter the function you want to calculate integral:\n>>'), locals={'x': x, 'y': y}))

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
                return ("It had'nt condition survey on Cauchy-Riemann or have differential on special point")
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


x, y, z, t = symbols('x y z t', real=True)


class text:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


# curNum value is the inputted value to evaluate solving
def set_whichcase():
    global whichcase
    whichcase = int(input(text.BOLD + "which proccese you want to do?\n" + text.ENDC +
                          "all proccess are supporting symbolic numbers\n"
                          + text.OKGREEN + "1- differential of normal number\n"
                                           "2- differential of complex number\n" + text.ENDC
                          + text.OKBLUE + "3- integral of normal number\n"
                                          "4- integral of complex number\n" + text.ENDC +
                          ">>"))


while 1:
    set_whichcase()
    if whichcase == 1:
        curNum = sympify(input('enter the function you want to calculate differential:\n>>'), locals={'x': x, 'y': y})
        i = sympify(input('enter the symbol value to get differential\n>>'), locals={'x': x, 'y': y})
        pprint(diff(curNum, i, 1))
        whichcase2 = bool(int(input('do you want to set symbols value?(1-yes , 2-no)\n>>')))

    elif whichcase == 2:
        curNum = complexNum(
            sympify(input('enter the function you want to calculate differential:\n>>'), locals={'x': x, 'y': y}))
        pprint(curNum.complexDiff())
        # whichcase2=bool(int(input('do you want to set symbols value?(1-yes , 2-no)\n>>')))
        # if whichcase2==1:
        #     print(curNum.getSettedSymbolValue())

    # elif whichcase == 3:
    elif whichcase == 4:
        f = sympify(input('enter the function you want to calculate integral(enter in term of z value):\n>>'),
                    locals={'x': x, 'y': y, 'z': z, 't': t})
        # func=
        curl = sympify(input('where you want to integral?(enter the curl in term of t value):\n>>'),
                       locals={'x': x, 'y': y, 'z': z, 't': t})
        startin = sympify(input('your integral start from where?:\n>>'), locals={'x': x, 'y': y, 'z': z, 't': t})
        endin = sympify(input('your integral end where?:\n>>'), locals={'x': x, 'y': y, 'z': z, 't': t})
        f = Lambda((z), f)
        curlDiff = diff(curl, t, 1)
        pprint(integrate((f(curl) * curlDiff), (t, startin, endin)))
    else:
        print("you should enter a number between 1 and 4 !!!")
        continue
        # break
    break

# bug: Cauchy-Riemann sufficient conditions checker: when we should equation the function
