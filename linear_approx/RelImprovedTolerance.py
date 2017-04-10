def relImproved():

    def toleranceMethodInputs():
        equation = raw_input("Enter equation to be approximated \n y'= ")
        epsilon = float(raw_input("Enter desired tolerance\n "))
        maxHalvings = float(raw_input("Enter maximum number of halvings of step size\n "))
        x = float(raw_input("Enter inital x value\n "))
        y = float(raw_input("Enter inital y value\n "))
        xFinal = float(raw_input("Enter x value to approximate y at\n "))
        iterations = int(raw_input("Enter a positive integer for the number of steps\n "))
        printSelection = 0
        print2 = 0
        return [equation, epsilon, maxHalvings, x, y, xFinal, iterations, printSelection, print2 = 0]

    def relToleranceMethod(equation, epsilon, maxHalvings, x, y, xFinal, iterationCount, printOption, print2):
        yPrevious = y
        print '\n', "%-15s %-15s" % ('step size=', 'y=')
        for m in range(maxHalvings):
            iterationCount = 2**m
            stepSize = (xFinal - x) / float(iterationCount)
            for n in range(iterationCount):
                if printOption == 1:
                    print "%-15s %-15s" % (x, y)
                y = (y + stepSize
                * (userFunction(x, y, equation)
                + userFunction(x + stepSize, y + stepSize
                * userFunction(x, y, equation), equation)) / 2.0)
                x = x + stepSize
            if print2 == 1:
                print "%-15s %-15s" % (x, y)
            print "%-15s %-15s" % (stepSize, y)
            if abs((y - yPrevious) / y) < epsilon:
                break
            else:
                yPrevious = y
        if m == (maxHalvings-1):
            print "y can be approximated as ", y, " but may not be within the relative tolerance ", epsilon
        else:
            print "y can be approximated as ", y, " with tolerance ", epsilon

#want to import eulersImprovedMethod but there are some issues
#print function needs to be disabled - use keyword argument
#fix print functions so that each program only prints the correct things and the methods can be reused
#move stepSize calculation to within input statements - that entails adding it as an argument to all of the methods
#print2 could be set to 0 in the tolerance method to avoid stating it in the inputs section
#possibly mve stepsize in base cases up to inputs but rewrite when using tolerancemethods
