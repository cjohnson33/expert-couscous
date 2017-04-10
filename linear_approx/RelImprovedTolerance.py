from linear_approx import utility
from linear_approx import ImprovedEuler

def relToleranceMethod(equation, epsilon, maxHalvings, x, y, xFinal, printOption, printXY):
    print '\n', "%-15s %-15s" % ('step size=', 'y=')
    yPrevious = y
    for m in range(maxHalvings):
        iterationCount = 2**m
        stepSize = (xFinal - x) / float(iterationCount)
        ImprovedEuler.eulersImprovedMethod(equation, x, y, xFinal, iterationCount, stepSize, printOption, printXY)
        print "%-15s %-15s" % (stepSize, y)
        if 0 < abs((y - yPrevious) / y) < epsilon :
            break
        else:
            yPrevious = y
    if m == (maxHalvings-1):
        print "\ny can be approximated as ", y, " but may not be within the relative tolerance ", epsilon
    else:
        print "\ny can be approximated as ", y, " with tolerance ", epsilon

def relImproved():
    relToleranceMethod(*utility.toleranceMethodInputs())
