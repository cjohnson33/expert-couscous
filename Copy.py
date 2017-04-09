from __future__ import division
import numpy
print "Euler's Method"
#obtain function, initial values, goal value, and iterations/steps
def check_num_input(var):
    #checks to make sure input is a number or expression that can be evaluated
    #as a number
    if var == float or eval(var) == float or int
f = raw_input("Enter equation to be approximate \n y'= ")
x = float(eval(raw_input("Enter inital x value\n ")))
y = float(eval(raw_input("Enter inital y value\n ")))
g = float(eval(raw_input("Enter x value to approximate y at\n ")))
i = eval((raw_input("Enter a positive integer for the number of steps\n ")))
while type(i) != int or i <=0:
    i = eval((raw_input("Enter a positive integer for the number of steps\n ")))
h = (g - x) / i
print '\n', "%-15s %-15s" % ('x=', 'y=')
for n in range(i):
    print "%-15s %-15s" % (x, y)
    y = y + h * eval(f)
    x = x + h
print "%-15s %-15s" % (x, y)
