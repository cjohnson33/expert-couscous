from linear_approx import Euler
def mainmenu():
    done = False
    while not done:
        print "1. Euler's Method"
        print "2. Improved Euler's Method"
        print "3. Runge-Katta Method"
        print "4. Quit Program"
        try:
            selection = int(raw_input("Select an option: "))
            if selection == 1:
                Euler.eulers()
            elif selection == 2:
                pass
            elif selection == 3:
                pass
            elif selection == 4:
                quit()
            else:
                raise ValueError()
        except ValueError:
            print "\nInvalid Selection \n"
if __name__ == "__main__":
    mainmenu()
