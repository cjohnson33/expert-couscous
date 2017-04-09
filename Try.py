print "Euler's Method"
#obtain function, initial values, goal value, and iterations/steps
f = raw_input("""Please enter the equation you wish to evaluate
y'=""") # somehow convert user input from str to usable function
a = float(raw_input("Enter the initial x value x = "))
b = float(raw_input("Enter the initial y value y = "))
g = float(raw_input("Enter the final x value you wish to evaluate to x = "))
#h = input("Enter the size of step you wish to use h = ") #to implement later
i = int(raw_input("Enter the number of steps you wish use i = "))
h = (g - a)/i
x = a
y = b
#f = float(eq)
for s in range(i):
    #print "x before is ", x
    #print "y before is", y
    y = y+h*(eval(f)) # need to implement user equation here f
    #print "y after is ", y
    x = x+h
    #print "x after is", x
print "y finally is ", y
