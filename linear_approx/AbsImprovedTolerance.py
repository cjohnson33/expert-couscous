from __future__ import division
import numpy
print "Improved Euler's Method with tolerance based on absolute error"
#obtain function, initial values, goal value, and iterations/steps
f = raw_input("Enter equation to be approximate \n y'= ")
def funcF(a,b):
    x = a
    y = b
    return eval(f)
e = float(eval(raw_input("Enter desired tolerance\n ")))
m = eval(raw_input("Enter maximum number of halvings of step size\n "))
a = float(eval(raw_input("Enter inital x value\n ")))
b = float(eval(raw_input("Enter inital y value\n ")))
g = float(eval(raw_input("Enter x value to approximate y at\n ")))
#i = eval((raw_input("Enter a positive integer for the number of steps\n ")))
while type(m) != int or m <=0:
    m = eval((raw_input("Enter maximum number of halvings of step size\n ")))
print '\n'
z = b
for q in range(m):
    n = 2**q
    h = (g - a) / n
    x = a
    y = b
    #print '\n', "%-15s %-15s" % ('x=', 'y=')
    for i in range(n):
        #print "%-15s %-15s" % (x, y)
        y = y + h * (funcF(x, y) + funcF(x + h, y + h * funcF(x, y))) / 2
        x = x + h
    #print "%-15s %-15s" % (x, y)
    print "%-15s %-15s" % (h, y)
    if abs(y - z) < e:
        break
    else:
        z = y
if q == (m-1):
    print "y can be approximated as ", y, " but may not be within the tolerance ", e
else:
    print "y can be approximated as ", y, " with tolerance ", e
