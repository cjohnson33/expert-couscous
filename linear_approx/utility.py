def baseMethodInputs():
    equation = raw_input("Enter equation to be approximated (please use standard python operators)\n y'= ")
    x = float(raw_input("Enter inital x value\n "))
    y = float(raw_input("Enter inital y value\n "))
    xFinal = float(raw_input("Enter x value to approximate y at\n "))
    iterationCount = int(raw_input("Enter a positive integer for the number of steps\n "))
    stepSize = (xFinal - x) / float(iterationCount)
    printSelection = printMenu()
    printXY = 1
    return [equation, x, y, xFinal, iterationCount, stepSize, printSelection, printXY]

def toleranceMethodInputs():
    equation = raw_input("Enter equation to be approximated \n y'= ")
    epsilon = float(raw_input("Enter desired tolerance\n "))
    maxHalvings = int(raw_input("Entera positive integer for the maximum step size halvings\n "))
    x = float(raw_input("Enter inital x value\n "))
    y = float(raw_input("Enter inital y value\n "))
    xFinal = float(raw_input("Enter x value to approximate y at\n "))
    printOption = printMenu()
    printXY = 0
    return [equation, epsilon, maxHalvings, x, y, xFinal, printOption, printXY]

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

def userFunction(xValue,yValue, equation):
    x = xValue
    y = yValue
    return eval(equation)
