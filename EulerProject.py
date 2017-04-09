from linear_approx import Euler
def mainmenu():
    done = False
    while not done:
        print "\nMain Menu"
        print "1. Euler's Method"
        print "2. Improved Euler's Method"
        print "3. Runge-Katta Method"
        print "4. Quit Program"
        try:
            selection = int(raw_input("Select an option: "))
            if selection == 1:
                Euler.eulers()
            elif selection == 2:
                ImprovedEulerMenu()
            elif selection == 3:
                RungeKattaMenu()
            elif selection == 4:
                quit()
            else:
                raise ValueError()
        except ValueError:
            print "\nInvalid Selection\n"
def ImprovedEulerMenu():
    done = False
    while not done:
        print "\n"
        print "1. Base Improved Euler's Method"
        print "2. Improved Euler's Method with Tolerance Based on Absolute Error"
        print "3. Improved Euler's Method with Tolerance Based on Relative Error"
        print "4. Return to Main Menu"
        try:
            selection = int(raw_input("Select an option: "))
            if selection == 1:
                pass
            elif selection == 2:
                pass
            elif selection == 3:
                pass
            elif selection == 4:
                mainmenu()
            else:
                raise ValueError()
        except ValueError:
            print "\nInvalid Selection\n"
def RungeKattaMenu():
    done = False
    while not done:
        print "\n"
        print "1. Base Runge-Katta Method"
        print "2. Runge-Katta Method with Tolerance Based on Absolute Error"
        print "3. Runge-Katta Method with Tolerance Based on Relative Error"
        print "4. Return to Main Menu"
        try:
            selection = int(raw_input("Select an option: "))
            if selection == 1:
                pass
            elif selection == 2:
                pass
            elif selection == 3:
                pass
            elif selection == 4:
                mainmenu()
            else:
                raise ValueError()
        except ValueError:
            print "\nInvalid Selection\n"
if __name__ == "__main__":
    mainmenu()
