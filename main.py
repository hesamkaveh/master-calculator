from __future__ import division
import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from sympy import *
import pyperclip

x, y, z, t = symbols('x y z t', real=True)

qtCreatorFile = "tax_calc.ui"  # Enter file here.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.limit_button.clicked.connect(self.limittfunc)
        self.diffButton_normal.clicked.connect(self.diff_normal)
        self.diffButton_complex.clicked.connect(self.diff_complex)
        self.integralButton_normal.clicked.connect(self.integral_normal)
        self.integralButton_complex.clicked.connect(self.integral_complex)
        self.allCalculator.clicked.connect(self.allcalc)
        self.binomialButton.clicked.connect(self.binomialfunc)
        self.solver_button.clicked.connect(self.solver)
        self.sumButton.clicked.connect(self.sumfunc)
        self.factorButton.clicked.connect(self.factorfunc)
        self.fourierButton.clicked.connect(self.fourier)
        self.integralButton_copy.clicked.connect(self.copy)
        self.integralButton_copy_3.clicked.connect(self.copy)
        self.integralButton_copy_9.clicked.connect(self.copy)
        self.integralButton_copy_10.clicked.connect(self.copy)
        self.integralButton_copy_11.clicked.connect(self.copy)
        self.integralButton_copy_12.clicked.connect(self.copy)
        self.integralButton_copy_13.clicked.connect(self.copy)
        self.integralButton_copy_2.clicked.connect(self.copy)
        self.integralButton_copy_4.clicked.connect(self.copy)

    def checkForCopy(self, arg):
        if self.checkBox_copy.isChecked() == True:
            pyperclip.copy(str(arg))

    def binomialfunc(self):
        global result
        binomialTop = sympify(str(self.binomialTop.toPlainText()), locals={'x': x, 'y': y})
        binomialDown = sympify(str(self.binomialDown.toPlainText()), locals={'x': x, 'y': y})
        result=binomial(binomialTop,binomialDown)
        if self.checkBox_expand.isChecked() == True:
            result = result.expand()
        self.binomialResult.setText(str(result))
        self.checkForCopy(result)


    def factorfunc(self):
        global result
        factorf = sympify(str(self.factorf.toPlainText()), locals={'x': x, 'y': y})
        result = factorial(factorf)
        self.factorResult.setText(str(result))
        self.checkForCopy(result)

    def fourier(self):
        global result
        fourierFunc = sympify(str(self.fourierFunc.toPlainText()), locals={'x': x, 'y': y})
        fourierPeriod = sympify(str(self.fourierPeriod.toPlainText()), locals={'x': x, 'y': y})
        result = fourier_series(fourierFunc, (x, -fourierPeriod, fourierPeriod)).scale(1).truncate()
        if self.checkBox_expand.isChecked() == True:
            result = result.expand()
        self.fourierResult.setText(str(result))
        self.checkForCopy(result)

    def solver(self):
        global result
        funcSolver = sympify(str(self.funcSolver.toPlainText()), locals={'x': x, 'y': y})
        solverSymbol = sympify(str(self.solverSymbol.toPlainText()), locals={'x': x, 'y': y})
        result = solve(funcSolver, solverSymbol)
        if self.checkBox_expand.isChecked() == True:
            result = result.expand()
        self.solverResult.setText(str(result))
        self.checkForCopy(result)

    def sumfunc(self):
        global result
        sumNum = sympify(str(self.sumNum.toPlainText()), locals={'x': x, 'y': y})
        sumTo = sympify(str(self.sumTo.toPlainText()), locals={'x': x, 'y': y})
        sumFrom = sympify(str(self.sumFrom.toPlainText()), locals={'x': x, 'y': y})
        result = sympify(summation(sumNum, (x, sumFrom, sumTo)))
        if self.checkBox_expand.isChecked() == True:
            result = result.expand()
        self.sumResult.setText(str(result))
        self.checkForCopy(result)

    def limittfunc(self):
        global result
        limfunc = sympify(str(self.limitFunc.toPlainText()), locals={'x': x, 'y': y})
        limit_to = sympify(str(self.limit_to.toPlainText()), locals={'x': x, 'y': y})
        limit_from = sympify(str(self.limit_from.toPlainText()), locals={'x': x, 'y': y})
        result = limit(limfunc, limit_from, limit_to)
        if self.checkBox_expand.isChecked() == True:
            result = result.expand()
        self.limit_result.setText(str(result))
        self.checkForCopy(result)

    def allcalc(self):
        global result
        curNum = sympify(str(self.calculator.toPlainText()), locals={'x': x, 'y': y})
        result = curNum
        if self.checkBox_trigsimp.isChecked() == True:
            result = result.trigsimp()
        if self.checkBox_expand.isChecked() == True:
            result = result.expand()
        self.result_calculator.setText(str(result))
        self.checkForCopy(result)

    def diff_normal(self):
        global result
        func = sympify(str(self.func.toPlainText()), locals={'x': x, 'y': y})
        times = sympify(str(self.diffNormalTimes.value()), locals={'x': x, 'y': y})
        result = diff(func, x, times)
        if self.checkBox_expand.isChecked() == True:
            result = result.expand()
        self.diff_normal_number.setText(str(result))
        self.checkForCopy(result)

    def diff_complex(self):
        global result
        func = sympify(str(self.func_2.toPlainText()), locals={'x': x, 'y': y})
        realImag = func.as_real_imag()
        u = realImag[0]
        v = realImag[1]
        uDiffx = diff(u, x, 1)
        uDiffy = diff(u, y, 1)
        vDiffx = diff(v, x, 1)
        vDiffy = diff(v, y, 1)
        f1 = Lambda((x, y), uDiffx)
        f2 = Lambda((x, y), vDiffy)
        f3 = Lambda((x, y), uDiffy)
        f4 = Lambda((x, y), -vDiffx)
        if (f1 == f2 and f3 == f4):
            global result
            result = (uDiffx + vDiffx * I)
            if self.checkBox_expand.isChecked() == True:
                result = result.expand()
            self.diff_normal_number.setText(str(result))
            self.checkForCopy(result)

        else:
            global result
            self.diff_normal_number.setText(
                ("It had'nt condition survey on Cauchy-Riemann or have differential on special point"))

    def integral_complex(self):
        global result
        function = sympify(str(self.function.toPlainText()), locals={'x': x, 'y': y, 'z': z})
        curl = sympify(str(self.curl.toPlainText()), locals={'x': x, 'y': y, 'z': z, 't': t})
        curlDiff = diff(curl, t, 1)
        endin = sympify(str(self.endin.toPlainText()), locals={'x': x, 'y': y, 'z': z})
        startin = sympify(str(self.startin.toPlainText()), locals={'x': x, 'y': y, 'z': z})
        function = Lambda((z), function)
        result = integrate((function(curl) * curlDiff), (t, startin, endin))
        if self.checkBox_expand.isChecked() == True:
            result = result.expand()
        self.integral_number.setText(str(result))
        self.checkForCopy(result)

    def integral_normal(self):
        global result
        function_2 = sympify(str(self.function_2.toPlainText()), locals={'x': x, 'y': y, 'z': z})
        endin_2 = sympify(str(self.endin_2.toPlainText()), locals={'x': x, 'y': y, 'z': z})
        startin_2 = sympify(str(self.startin_2.toPlainText()), locals={'x': x, 'y': y, 'z': z})
        result = integrate((function_2), (x, startin_2, endin_2))
        if self.checkBox_expand.isChecked() == True:
            result = result.expand()
        self.integral_number.setText(str(result))
        self.checkForCopy(result)

    def copy(self):
        pyperclip.copy(str(result))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
