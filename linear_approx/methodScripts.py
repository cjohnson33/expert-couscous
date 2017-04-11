from linear_approx import utility

def eulersMethod(equation, x, y, xFinal, iterationCount, printOption, printXY):
    if printXY == 1:
        print '\n', "%-15s %-15s" % ('x=', 'y=')
    stepSize = (xFinal - x) / float(iterationCount)
    for n in range(iterationCount):
        if printXY == 1 and printOption == 1:
            print "%-15s %-15s" % (x, y)
        y = y + stepSize * utility.userFunction(x, y, equation)
        x = x + stepSize
    if printXY == 1:
        print "%-15s %-15s" % (x, y)
    return y

def eulersImprovedMethod(equation, x, y, xFinal, iterationCount, printOption, printXY):
    if printXY == 1:
        print '\n', "%-15s %-15s" % ('x=', 'y=')
    stepSize = (xFinal - x) / float(iterationCount)
    for n in range(iterationCount):
        if printXY == 1 and printOption == 1:
            print "%-15s %-15s" % (x, y)
        y = (y + stepSize
        * (utility.userFunction(x, y, equation)
        + utility.userFunction(x + stepSize, y + stepSize
        * utility.userFunction(x, y, equation), equation)) / 2.0)
        x = x + stepSize
    if printXY == 1:
        print "%-15s %-15s" % (x, y)
    return y

def k1(x, y, stepSize, equation):
    return stepSize * utility.userFunction(x, y, equation)
def k2(x, y, stepSize, equation):
    return stepSize * utility.userFunction(x + stepSize / 2.0, y + k1(x, y, stepSize, equation) / 2.0, equation)
def k3(x, y, stepSize, equation):
    return stepSize * utility.userFunction(x + stepSize / 2.0, y + k2(x, y , stepSize, equation) / 2.0, equation)
def k4(x, y, stepSize, equation):
    return stepSize * utility.userFunction(x + stepSize, y + k3(x, y, stepSize, equation), equation)

def rungeKuttaMethod(equation, x, y, xFinal, iterationCount, printOption, printXY):
    if printXY == 1:
        print '\n', "%-15s %-15s" % ('x=', 'y=')
    stepSize = (xFinal - x) / float(iterationCount)
    for n in range(iterationCount):
        if printXY == 1 and printOption == 1:
            print "%-15s %-15s" % (x, y)
        y = y + (1.0/6.0) * (k1(x, y, stepSize, equation) + 2 * k2(x, y, stepSize, equation) + 2 * k3(x, y, stepSize, equation) + k4(x, y, stepSize, equation))
        x = x + stepSize
    if printXY == 1:
        print "%-15s %-15s" % (x, y)
    return y

def toleranceMethod(equation, epsilon, maxHalvings, x, y, xFinal, printOption, printXY, compMethod, stoppingMethod):
    print '\n'
    yPrevious = y
    for m in range(maxHalvings):
        iterationCount = 2**m
        stepSize = (xFinal - x) / iterationCount
        if compMethod == "Improved Euler":
            yCurrent = eulersImprovedMethod(equation, x, y, xFinal, iterationCount, printOption, printXY)
        else:
            yCurrent = rungeKuttaMethod(equation, x, y, xFinal, iterationCount, printOption, printXY)
        if printOption == 1:
            print "%-15s %-15s" % (stepSize, yCurrent)
        if stoppingMethod == "absolute":
            if abs(yCurrent - yPrevious) < epsilon:
                break
        elif stoppingMethod == "relative":
            if abs((yCurrent - yPrevious) / yCurrent) < epsilon:
                break
        yPrevious = yCurrent
    if m == (maxHalvings-1):
        print "y can be approximated as ", yCurrent, " but may not be within the tolerance ", epsilon
    else:
        print "y can be approximated as ", yCurrent, " with tolerance ", epsilon
