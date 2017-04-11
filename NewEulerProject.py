from linear_approx import methodScripts
from linear_approx import utility

def mainmenu():
    done = False
    while not done:
        print "\nMain Menu"
        print "1. Euler's Method"
        print "2. Improved Euler's Method"
        print "3. Runge-Kutta Method"
        print "4. Quit Program"
        try:
            selection = int(raw_input("Select an option: "))
            if selection == 1:
                methodScripts.eulersMethod(*utility.methodInputs("base"))
            elif selection == 2:
                ImprovedEulerMenu()
            elif selection == 3:
                RungeKuttaMenu()
            elif selection == 4:
                quit()
            else:
                raise ValueError()
        except ValueError:
            print "\nInvalid Selection"

def ImprovedEulerMenu():
    done = False
    while not done:
        print "\n"
        print "1. Base Improved Euler's Method"
        print "2. Improved Euler's Method with Tolerance - Stopping Based on Absolute Error"
        print "3. Improved Euler's Method with Tolerance - Stopping Based on Relative Error"
        print "4. Return to Main Menu"
        try:
            selection = int(raw_input("Select an option: "))
            if selection == 1:
                methodScripts.eulersImprovedMethod(*utility.methodInputs("base"))
            elif selection == 2:
                methodScripts.toleranceMethod(*utility.methodInputs("tolerance"), compMethod = "Improved Euler", stoppingMethod = "absolute")
            elif selection == 3:
                methodScripts.toleranceMethod(*utility.methodInputs("tolerance"), compMethod = "Improved Euler", stoppingMethod = "relative")
            elif selection == 4:
                mainmenu()
            else:
                raise ValueError()
        except ValueError:
            print "\nInvalid Selection"

def RungeKuttaMenu():
    done = False
    while not done:
        print "\n"
        print "1. Base Runge-Kutta Method"
        print "2. Runge-Kutta Method with Tolerance - Stopping Based on Absolute Error"
        print "3. Runge-Kutta Method with Tolerance - Stopping Based on Relative Error"
        print "4. Return to Main Menu"
        try:
            selection = int(raw_input("Select an option: "))
            if selection == 1:
                methodScripts.rungeKuttaMethod(*utility.methodInputs("base"))
            elif selection == 2:
                methodScripts.toleranceMethod(*utility.methodInputs("tolerance"), compMethod = "Runge-Kutta", stoppingMethod = "absolute")
            elif selection == 3:
                methodScripts.toleranceMethod(*utility.methodInputs("tolerance"), compMethod = "Runge-Kutta", stoppingMethod = "relative")
            elif selection == 4:
                mainmenu()
            else:
                raise ValueError()
        except ValueError:
            print "\nInvalid Selection"

if __name__ == "__main__":
    mainmenu()
