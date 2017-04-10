from linear_approx import utility

def eulerImproved():
    eulersImprovedMethod(*utility.baseMethodInputs())

def eulersImprovedMethod(equation, x, y, xFinal, iterationCount, stepSize, printOption, printXY):
    if printXY == 1:
        print '\n', "%-15s %-15s" % ('x=', 'y=')
    for n in range(iterationCount):
        if printOption == 1 and printXY == 1:
            print "%-15s %-15s" % (x, y)
        y = (y + stepSize
        * (utility.userFunction(x, y, equation)
        + utility.userFunction(x + stepSize, y + stepSize
        * utility.userFunction(x, y, equation), equation)) / 2.0)
        x = x + stepSize
    return x, y
    if printXY == 1:
        print "%-15s %-15s" % (x, y)
