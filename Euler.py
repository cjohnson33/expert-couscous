from __future__ import division
import math
print "Euler's Method"
#obtain function, initial values, goal value, and iterations/steps
f = raw_input("Enter equation to be approximate \n y'= ")
def funcF(a,b):
    x = a
    y = b
    return eval(f)
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
    y = y + h * funcF(x, y)
    x = x + h
print "%-15s %-15s" % (x, y)
