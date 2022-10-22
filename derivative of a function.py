from sympy import *

x = symbols('x')

f = 3 * x**2 + 1

dx_f = diff(f)
print(dx_f.subs(x, 3))