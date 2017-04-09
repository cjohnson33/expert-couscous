def rungeKutta():

    def BaseMethodInputs():
        equation = raw_input("Enter equation to be approximated \n y'= ")
        x = float(raw_input("Enter inital x value\n "))
        y = float(raw_input("Enter inital y value\n "))
        xFinal = float(raw_input("Enter x value to approximate y at\n "))
        iterations = int(raw_input("Enter a positive integer for the number of steps\n "))
        printSelection = printMenu()
        return [equation, x, y, xFinal, iterations, printSelection]

    def printMenu():
        done = False
        while not done:
            print "1. Print all values throughout computation"
            print "2. Print only final approximation from method"
            try:
                selection = int(raw_input("Select an option: "))
                if selection == 1:
                    return 1
                elif selection == 2:
                    return 0
                else:
                    raise ValueError()
            except ValueError:
                print "\nInvalid Selection"

    def userFunction(xValue, yValue, equation):
        x = xValue
        y = yValue
        return eval(equation)

    def k1(x, y, stepSize, equation):
        return stepSize * userFunction(x, y, equation)
    def k2(x, y, stepSize, equation):
        return stepSize * userFunction(x + stepSize / 2, y + k1(x, y, stepSize, equation) / 2, equation)
    def k3(x, y, stepSize, equation):
        return stepSize * userFunction(x + stepSize / 2, y + k2(x, y , stepSize, equation) / 2, equation)
    def k4(x, y, stepSize, equation):
        return stepSize * userFunction(x + stepSize, y + k3(x, y, stepSize, equation), equation)

    def rungeKuttaMethod(equation, x, y, xFinal, iterationCount, printOption):
        stepSize = (xFinal - x) / float(iterationCount)
        print '\n', "%-15s %-15s" % ('x=', 'y=')
        for n in range(iterationCount):
            if printOption == 1:
                print "%-15s %-15s" % (x, y)
            y = y + (1/6.0) * (k1(x, y, stepSize, equation) + 2 * k2(x, y, stepSize, equation) + 2 * k3(x, y, stepSize, equation) + k4(x, y, stepSize, equation))
            x = x + stepSize
        print "%-15s %-15s" % (x, y)

    rungeKuttaMethod(*BaseMethodInputs())
