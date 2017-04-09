from __future__ import division
import numpy
print "Improved Euler's Method"
#obtain function, initial values, goal value, and iterations/steps
f = raw_input("Enter equation to be approximate \n y'= ")
def funcF(a,b):
    x = a
    y = b
    return eval(f)
a = float(eval(raw_input("Enter inital x value\n ")))
b = float(eval(raw_input("Enter inital y value\n ")))
g = float(eval(raw_input("Enter x value to approximate y at\n ")))
n = eval((raw_input("Enter a positive integer for the number of steps\n ")))
while type(n) != int or n <=0:
    n = eval((raw_input("Enter a positive integer for the number of steps\n ")))
h = (g - a) / n
x = a
y = b
print '\n', "%-15s %-15s" % ('x=', 'y=')
for i in range(n):
    print "%-15s %-15s" % (x, y)
    y = y + h * (funcF(x, y) + funcF(x + h, y + h * funcF(x, y))) / 2
    x = x + h
print "%-15s %-15s" % (x, y)
