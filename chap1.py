#my_value = 2 * ((3 + 2)**2 / 5) - 4
#print(my_value)

import imp
from itertools import product
from lib2to3.pygram import Symbols


#x= int(input('Please input a number\n'))
#product = 3 * x
#print(product)


#def f(x) :
#    return 2 * x + 1

#x_values = [0, 1, 2, 3]

#for x in x_values:
#    y = f(x)
#    print(y)

#import matplotlib
#from sympy import *
#from sympy.plotting import plot3d

#x, y = symbols('x y')
#f = log(2*(x**3) + 3*(y**3),10)
#plot3d(f)

#x = [1, 4, 6, 2]
#n = len(x)
 
#summation = sum(10*x[i] for i in range(0,n))
#print(summation)

#from sympy import *
#i,n= symbols('i n')
#summation = Sum(2*i,(i,1,n))
#up_to_5 = summation.subs(n,5)
#print(up_to_5.doit())

#from sympy import *

#x = symbols('x')
#expr = x**2/x**5
#print(expr)

#from math import log

#x = log(10)
#print(x)

#from math import exp
#p = 100
#r = .20
#t = 2.0

#a = p * exp(r*t)
#print(a)

#from sympy import *

#x = symbols('x')
#f = (1 + 1 / x)**x
#result = limit(f, x, oo)
#print(result)
#print(result.evalf())

#from sympy import *

#x = symbols('x')

#f = 3 * x**2 + 1

#dx_f = diff(f)
#print(dx_f.subs(x, 3))

#from sympy import *
#from sympy.plotting import plot3d

#x, y = symbols('x y')
#f = 2*(x**3) + 3*(y**3)

#dx_f = diff(f, x)
#dy_f = diff(f, y)

#print(dx_f)
#print(dy_f)
#plot3d(f)

#def approximate_integral(a, b, n, f):
#    delta_x = (b - a) / n
#    total_sum = 0
    
#    for i in range(1, n + 1):
#        midpoint = 0.5 * (2 * a + delta_x * (2 * i - 1))
#        total_sum += f(midpoint)
    
#    return total_sum * delta_x

#def my_function(x):
#    return x**2 + 1

#area = approximate_integral(a=0, b=1, n=1000, f=my_function)

#print(area) 

from sympy import *

x = symbols('x')

f = 3 * x**2 + 1 

area = integrate(f, (x, 0, 2))
print(area)

#calculating monthly compound interest
#from math import exp

#def month_cpdint(p ,r ,t, n):
#    int = p * (1 + (r/n))**(n * t)
#    return int
#def cont_cpdint(p ,r ,t ):
#    int = p * exp(r*t)
#    return int
    
#print(month_cpdint(p=1000, r=0.05, t=3, n=12))
#print(cont_cpdint(p=1000, r=0.05, t=3))
