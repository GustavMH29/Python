# Written by RF

from sympy import *
x=symbol("x")
f=sin(x)/x
y=limit(f, x, 0)
print(y)
