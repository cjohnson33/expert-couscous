def approxMethod(equation, x, y, xFinal, iterationCount, printOption, printXY, compMethod):
    """The main computational function of the program.
       It approximates the differential equation using the selected method and user input data"""
    if printXY == 1:
        print '\n', "%-20s %-20s" % ('x=', 'y=')

    stepSize = (xFinal - x) / float(iterationCount)
    for n in range(iterationCount):
        if printXY == 1 and printOption == 1:
            print "%-20s %-20s" % (x, y)

        if compMethod == "Euler's Method":
            y = y + stepSize * userFunction(x, y, equation)

        elif compMethod == "Improved Euler's Method":
            y = (y + stepSize
            * (userFunction(x, y, equation)
            + userFunction(x + stepSize, y + stepSize
            * userFunction(x, y, equation), equation)) / 2.0)

        else:
            #The Runge-Kutta Method
            y = y + (1.0/6.0) * (k1(x, y, stepSize, equation)
            + 2 * k2(x, y, stepSize, equation)
            + 2 * k3(x, y, stepSize, equation)
            + k4(x, y, stepSize, equation))

        x += stepSize
    if printXY == 1:
        print "%-20s %-20s" % (x, y)
    return y

def userFunction(xValue,yValue, equation):
    """Allows the user input equation to be reevaluated with current x & y values as the approximation proceeds"""
    x = xValue
    y = yValue
    return eval(equation)

def k1(x, y, stepSize, equation):
    """The first equation for the classical fourth-order Runge-Kutta method"""
    return stepSize * userFunction(x, y, equation)

def k2(x, y, stepSize, equation):
    """The second equation for the classical fourth-order Runge-Kutta method"""
    return stepSize * userFunction(x + stepSize / 2.0, y + k1(x, y, stepSize, equation) / 2.0, equation)

def k3(x, y, stepSize, equation):
    """The third equation for the classical fourth-order Runge-Kutta method"""
    return stepSize * userFunction(x + stepSize / 2.0, y + k2(x, y , stepSize, equation) / 2.0, equation)

def k4(x, y, stepSize, equation):
    """The fourth equation for the classical fourth-order Runge-Kutta method"""
    return stepSize * userFunction(x + stepSize, y + k3(x, y, stepSize, equation), equation)

def toleranceMethod(equation, epsilon, maxHalvings, x, y, xFinal, printOption, printXY, compMethod, stoppingMethod):
    """Computes the approximation to a desired accuracy unless a user set safeguard is tripped"""
    if printOption == 1:
        print '\n', "%-20s %-20s" % ('step size=', 'y=')
    yPrevious = y
    for m in range(maxHalvings):
        iterationCount = 2**m
        stepSize = (xFinal - x) / iterationCount
        yCurrent = approxMethod(equation, x, y, xFinal, iterationCount, printOption, printXY, compMethod)
        if printOption == 1:
            print "%-20s %-20s" % (stepSize, yCurrent)

        #Checks to see if desired accuracy has been acquired
        #and either repeats approximation with half the step size or terminates the loop.
        if stoppingMethod == "absolute":
            if abs(yCurrent - yPrevious) < epsilon:
                break
        elif stoppingMethod == "relative":
            if abs((yCurrent - yPrevious) / yCurrent) < epsilon:
                break
        yPrevious = yCurrent

    if m == (maxHalvings-1):
        #The maximum number of halvings was met but the desired accuracy was not
        print "\ny can be approximated as ", yCurrent, " but may not be within the tolerance ", epsilon
    else:
        #The desired accuracy was achieved
        print "\ny can be approximated as ", yCurrent, " with tolerance ", epsilon
