from __future__ import division
import numpy
print "Classical Fourth-Order Runge-Kutta Method"
#obtain function, initial values, goal value, and iterations/steps
f = raw_input("Enter equation to be approximate \n y'= ")
def funcF(a,b):
    x = a
    y = b
    return eval(f)
def k1(x, y, h):
    return h * funcF(x, y)
def k2(x, y, h):
    return h * funcF(x + h/2, y + k1(x, y, h)/2)
def k3(x, y, h):
    return h * funcF(x + h/2, y + k2(x, y , h)/2)
def k4(x, y, h):
    return h * funcF(x + h, y+ k3(x, y, h))
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
    y = y + (1/6) * (k1(x, y, h) + 2 * k2(x, y, h) + 2 * k3(x, y, h) + k4(x, y, h))
    x = x + h
print "%-15s %-15s" % (x, y)
