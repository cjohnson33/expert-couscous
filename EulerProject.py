from numerical_approximation import methodScripts
from numerical_approximation import utility

def mainmenu():
    """Provides the point of entry to the program"""
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
                Menu2("Euler's Method")
            elif selection == 2:
                Menu2("Improved Euler's Method")
            elif selection == 3:
                Menu2("Runge-Kutta Method")
            elif selection == 4:
                quit()
            else:
                raise ValueError()
        except ValueError:
            print "\nInvalid Selection"

def Menu2(method):
    """Secondary level menu adapted based on initial menu choice"""
    done = False
    while not done:
        print "\n"
        print "1. Base", method
        print "2.", method, "with Tolerance - Stopping Based on Absolute Error"
        print "3.", method, "with Tolerance - Stopping Based on Relative Error"
        print "4. Return to Main Menu"
        try:
            selection = int(raw_input("Select an option: "))
            if selection == 1:
                methodScripts.approxMethod(*utility.methodInputs("base"), compMethod=method)
            elif selection == 2:
                methodScripts.toleranceMethod(*utility.methodInputs("tolerance"), compMethod=method, stoppingMethod = "absolute")
            elif selection == 3:
                methodScripts.toleranceMethod(*utility.methodInputs("tolerance"), compMethod=method, stoppingMethod = "relative")
            elif selection == 4:
                mainmenu()
            else:
                raise ValueError()
        #The following lines handle possible exceptions and thus prevent program crashing and traceback.
        except ValueError:
            print "\nInvalid Input"
        except ZeroDivisionError:
            print "\nDivision by Zero"
        except OverflowError:
            print "\nOverflow"
        except (SyntaxError, NameError):
            print "\nInvalid equation. Please use only x's and y's with valid python operators"
        except MemoryError:
            print "\nOperation exceeds memory capacity."
        except EOFError:
            quit()
        except KeyboardInterrupt:
            print "\nUser Interrupt"

if __name__ == "__main__":
    mainmenu()
