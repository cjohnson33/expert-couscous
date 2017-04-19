def methodInputs(menuOption):
    """Gathers user input depending on initial menu choice, casts variables,
       and passes that data on to the main functions"""
    equation = raw_input("\nEnter equation to be approximated (Please use valid python operators) \n y'= ")
    if menuOption == "tolerance":
        epsilon = float(raw_input("Enter desired tolerance\n "))
        maxHalvings = int(raw_input("Enter maximum number of halvings of step size\n "))
        printXY = 0
    x = float(raw_input("Enter inital x value\n "))
    y = float(raw_input("Enter inital y value\n "))
    xFinal = float(raw_input("Enter x value to approximate y at\n "))
    if menuOption == "base":
        iterations = int(raw_input("Enter a positive integer for the number of steps\n "))
        printXY = 1
    printSelection = printMenu()
    if menuOption == "base":
        return [equation, x, y, xFinal, iterations, printSelection, printXY]
    else:
        #For approximations with desired tolerance
        return [equation, epsilon, maxHalvings, x, y, xFinal, printSelection, printXY]

def printMenu():
    """Allows the user to select verbose data output"""
    done = False
    while not done:
        print "1. Print all values throughout computation"
        print "2. Print only final approximation from method"
        try:
            selection = int(raw_input("Select an option: "))
            if selection == 1:
                #Verbose Output
                return 1
            elif selection == 2:
                #Only final output
                return 0
            else:
                raise ValueError()
        except ValueError:
            print "\nInvalid Selection"
