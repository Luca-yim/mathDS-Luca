from sympy import *
from sympy.plotting import plot3d

x, y = symbols('x y')
f = log(2*(x**3) + 3*(y**3),10)
plot3d(f)