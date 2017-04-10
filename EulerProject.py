from linear_approx import Euler
from linear_approx import ImprovedEuler
from linear_approx import RungeKutta
from linear_approx import RelImprovedTolerance
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
                Euler.eulers()
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
                ImprovedEuler.eulerImproved()
            elif selection == 2:
                pass
            elif selection == 3:
                RelImprovedTolerance.relImproved()
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
                RungeKutta.rungeKutta()
            elif selection == 2:
                pass
            elif selection == 3:
                pass
            elif selection == 4:
                mainmenu()
            else:
                raise ValueError()
        except ValueError:
            print "\nInvalid Selection"
if __name__ == "__main__":
    mainmenu()
