from linear_approx import utility

def rungeKutta():
    rungeKuttaMethod(*utility.baseMethodInputs())

def k1(x, y, stepSize, equation):
    return stepSize * utility.userFunction(x, y, equation)
def k2(x, y, stepSize, equation):
    return stepSize * utility.userFunction(x + stepSize / 2.0, y + k1(x, y, stepSize, equation) / 2.0, equation)
def k3(x, y, stepSize, equation):
    return stepSize * utility.userFunction(x + stepSize / 2.0, y + k2(x, y , stepSize, equation) / 2.0, equation)
def k4(x, y, stepSize, equation):
    return stepSize * utility.userFunction(x + stepSize, y + k3(x, y, stepSize, equation), equation)

def rungeKuttaMethod(equation, x, y, xFinal, iterationCount, stepSize, printOption, printXY):
    if printXY == 1:
        print '\n', "%-15s %-15s" % ('x=', 'y=')
    for n in range(iterationCount):
        if printOption == 1 and printXY == 1:
            print "%-15s %-15s" % (x, y)
        y = y + (1.0/6.0) * (k1(x, y, stepSize, equation) + 2 * k2(x, y, stepSize, equation) + 2 * k3(x, y, stepSize, equation) + k4(x, y, stepSize, equation))
        x = x + stepSize
    if printXY == True:
        print "%-15s %-15s" % (x, y)
