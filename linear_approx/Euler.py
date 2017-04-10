from linear_approx import utility

def eulers():
    eulersMethod(*utility.baseMethodInputs())

def eulersMethod(equation, x, y, xFinal, iterationCount, stepSize, printOption, printXY):
    if printXY == 1:
        print '\n', "%-15s %-15s" % ('x=', 'y=')
    for n in range(iterationCount):
        if printOption == 1 and printXY == 1:
            print "%-15s %-15s" % (x, y)
        y = y + stepSize * utility.userFunction(x, y, equation)
        x = x + stepSize
    if printXY == True:
        print "%-15s %-15s" % (x, y)
